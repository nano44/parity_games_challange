/* REFEREE successor 25: ref_rup_del.c, a variant of successor 24's ref_rup.c (my own RUP checker) that APPLIES deletions.
   Purpose: an independent check of the Glucose 4 DRUP proof of P-IDEAL-IM (6.5M lemmas; the deletion-ignoring ref_rup took > 5 h).
   Changes against ref_rup.c (everything else is unchanged):
   - "d l1 ... lk 0": the clause is looked up as a SET of literals (order-independent hash, then exact set comparison with a mark
     array) among the live stored clauses; ONE live copy is marked deleted and dropped lazily from the watch lists. A deletion that
     matches no live clause is counted and ignored (removing nothing is sound).
   - Top-level assignments are KEPT when a clause is deleted (also a deleted unit or reason). Soundness: every top-level literal is
     implied by the clause DB at the time it was set, and every DB clause is implied by the input, so keeping it can only accept
     lemmas implied by the input. Deletions only remove clauses, so they never make an unsound lemma pass.
   - So "s VERIFIED" still means: every lemma is RUP w.r.t. (input + earlier lemmas, minus deleted clauses, plus implied top-level
     units), and a top-level conflict was reached; hence the input CNF is UNSAT.
   Usage: ref_rup_del F.cnf P.proof */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int V;                       /* number of variables */
static signed char *asg;            /* asg[v] in {-1, 0, 1} */
static int *trail, ntrail, qh;      /* assignment trail and propagation head */
static int *lits; static long nlits, caplits;   /* flat literal store */
static long *start; static int *len; static long ncls, capcls;
static unsigned char *dead; static long capdead;
static long **wat; static int *wn, *wcap;       /* watch lists indexed by literal code */
static int code(int l) { return l > 0 ? 2 * l : -2 * l + 1; }
static int value(int l) { int a = asg[l > 0 ? l : -l]; return l > 0 ? a : -a; }
static void setlit(int l) { asg[l > 0 ? l : -l] = l > 0 ? 1 : -1; trail[ntrail++] = l; }
static void addwatch(int l, long c) {
  int k = code(l);
  if (wn[k] == wcap[k]) { wcap[k] = wcap[k] ? 2 * wcap[k] : 8; wat[k] = realloc(wat[k], sizeof(long) * wcap[k]); }
  wat[k][wn[k]++] = c;
}
/* propagate from qh; return 1 iff conflict */
static int prop(void) {
  while (qh < ntrail) {
    int f = -trail[qh++];            /* literal that just became false */
    int k = code(f); long *w = wat[k]; int n = wn[k], i, j = 0;
    for (i = 0; i < n; i++) {
      long c = w[i]; if (dead[c]) continue; int *L = lits + start[c];
      if (L[0] == f) { L[0] = L[1]; L[1] = f; }      /* keep the false watch at position 1 */
      if (value(L[0]) == 1) { w[j++] = c; continue; }
      int m, moved = 0;
      for (m = 2; m < len[c]; m++)
        if (value(L[m]) != -1) { int t = L[1]; L[1] = L[m]; L[m] = t; addwatch(L[1], c); moved = 1; break; }
      if (moved) continue;
      w[j++] = c;
      if (value(L[0]) == -1) { for (i++; i < n; i++) w[j++] = w[i]; wn[k] = j; return 1; }
      setlit(L[0]);
    }
    wn[k] = j;
  }
  return 0;
}
static int conflict_top = 0;
/* store a clause (deduped, not a tautology); maintain top-level propagation */
static long store(int *c, int n) {
  if (conflict_top) return -1;
  if (nlits + n > caplits) { caplits = 2 * (nlits + n) + 1024; lits = realloc(lits, sizeof(int) * caplits); }
  if (ncls == capcls) { capcls = capcls ? 2 * capcls : 65536; start = realloc(start, sizeof(long) * capcls); len = realloc(len, sizeof(int) * capcls); }
  if (ncls >= capdead) { long o = capdead; capdead = capdead ? 2 * capdead : 65536; dead = realloc(dead, capdead); memset(dead + o, 0, capdead - o); }
  long id = ncls++; start[id] = nlits; len[id] = n; memcpy(lits + nlits, c, sizeof(int) * n); nlits += n;
  int *L = lits + start[id];
  if (n == 0) { conflict_top = 1; return id; }
  /* move non-false literals to the front */
  int nf = 0, i;
  for (i = 0; i < n; i++) if (value(L[i]) != -1) { int t = L[nf]; L[nf] = L[i]; L[i] = t; nf++; }
  for (i = 0; i < nf; i++) if (value(L[i]) == 1) { if (n >= 2) { addwatch(L[0], id); addwatch(L[1], id); } return id; }  /* satisfied */
  if (nf == 0) { conflict_top = 1; return id; }
  if (n >= 2) { addwatch(L[0], id); addwatch(L[1], id); }
  if (nf == 1) { setlit(L[0]); if (prop()) conflict_top = 1; }
  return id;
}

/* order-independent clause hash table: bucket chains of clause ids */
static unsigned long long lh(int l) { unsigned long long x = (unsigned long long)(unsigned)l * 0x9E3779B97F4A7C15ULL; x ^= x >> 29; x *= 0xBF58476D1CE4E5B9ULL; return x ^ (x >> 32); }
static unsigned long long chash(int *c, int n) { unsigned long long s = 0, p = 1, x = 0; int i; for (i = 0; i < n; i++) { unsigned long long h = lh(c[i]); s += h; x ^= h; p *= (h | 1); } return s ^ (x * 31) ^ (p * 7) ^ (unsigned long long)n; }
#define HB (1L << 24)
static long *head, *nxt; static long capnxt;
static unsigned char *mark;   /* indexed by literal code */
static void hinsert(long id, int *c, int n) {
  if (id < 0) return;
  if (id >= capnxt) { capnxt = 2 * (id + 1); nxt = realloc(nxt, sizeof(long) * capnxt); }
  long b = (long)(chash(c, n) & (HB - 1)); nxt[id] = head[b]; head[b] = id;
}
static long ndel_found = 0, ndel_missing = 0;
static void hdelete(int *c, int n) {
  long b = (long)(chash(c, n) & (HB - 1)), id, *pp = &head[b]; int i;
  for (i = 0; i < n; i++) mark[code(c[i])] = 1;
  for (id = *pp; id >= 0; pp = &nxt[id], id = *pp) {
    if (dead[id] || len[id] != n) continue;
    int *L = lits + start[id], ok = 1;
    for (i = 0; i < n && ok; i++) if (!mark[code(L[i])]) ok = 0;
    if (ok) { dead[id] = 1; *pp = nxt[id]; ndel_found++; break; }
  }
  if (id < 0) ndel_missing++;
  for (i = 0; i < n; i++) mark[code(c[i])] = 0;
}
static int *buf; static int bcap;
static int push(int x, int n) { if (n == bcap) { bcap = bcap ? 2 * bcap : 256; buf = realloc(buf, sizeof(int) * bcap); } buf[n] = x; return n + 1; }
/* dedupe in place; return -1 for a tautology */
static int clean(int n) {
  int m = 0, i, j;
  for (i = 0; i < n; i++) { int dup = 0; for (j = 0; j < m; j++) { if (buf[j] == buf[i]) dup = 1; else if (buf[j] == -buf[i]) return -1; } if (!dup) buf[m++] = buf[i]; }
  return m;
}
int main(int argc, char **argv) {
  if (argc != 3) { fprintf(stderr, "usage: ref_rup_del F.cnf P.proof\n"); return 2; }
  FILE *F = fopen(argv[1], "r"); if (!F) { printf("s ERROR cnf\n"); return 2; }
  char line[256]; long C = -1;
  while (fgets(line, sizeof line, F)) { if (line[0] == 'c') continue; if (sscanf(line, "p cnf %d %ld", &V, &C) == 2) break; printf("s ERROR header\n"); return 2; }
  if (C < 0 || V <= 0) { printf("s ERROR header\n"); return 2; }
  asg = calloc(V + 1, 1); trail = malloc(sizeof(int) * (V + 1));
  head = malloc(sizeof(long) * HB); { long b; for (b = 0; b < HB; b++) head[b] = -1; } mark = calloc(2 * V + 2, 1);
  wat = calloc(2 * V + 2, sizeof(long *)); wn = calloc(2 * V + 2, sizeof(int)); wcap = calloc(2 * V + 2, sizeof(int));
  long ci; int x;
  for (ci = 0; ci < C; ci++) {
    int n = 0;
    for (;;) { if (fscanf(F, "%d", &x) != 1) { printf("s ERROR clause %ld truncated\n", ci); return 2; }
      if (x == 0) break; if (x > V || x < -V) { printf("s ERROR literal %d out of range\n", x); return 2; } n = push(x, n); }
    n = clean(n); if (n < 0) continue; { long id = store(buf, n); hinsert(id, buf, n); }
  }
  if (fscanf(F, "%d", &x) == 1) { printf("s ERROR more than %ld clauses\n", C); return 2; }
  fclose(F);
  fprintf(stderr, "input: %d vars, %ld clauses, conflict after input %d\n", V, C, conflict_top);
  FILE *P = fopen(argv[2], "r"); if (!P) { printf("s ERROR proof\n"); return 2; }
  long nlem = 0, ndel = 0; int ch;
  while (!conflict_top) {
    do ch = fgetc(P); while (ch == ' ' || ch == '\n' || ch == '\r' || ch == '\t');
    if (ch == EOF) break;
    int del = 0;
    if (ch == 'd') del = 1; else ungetc(ch, P);
    int n = 0;
    for (;;) { if (fscanf(P, "%d", &x) != 1) { printf("s ERROR proof item %ld unterminated\n", nlem + ndel + 1); return 2; }
      if (x == 0) break; if (x > V || x < -V) { printf("s ERROR proof literal %d out of range\n", x); return 2; } n = push(x, n); }
    if (del) { ndel++; n = clean(n); if (n >= 0) hdelete(buf, n); else ndel_missing++; continue; }
    nlem++;
    n = clean(n); if (n < 0) continue;                    /* tautology: trivially implied; not stored */
    int base = ntrail, ok = 0, i;
    for (i = 0; i < n && !ok; i++) { int v = value(buf[i]); if (v == 1) ok = 1; else if (v == 0) setlit(-buf[i]); }
    if (!ok) ok = prop();
    while (ntrail > base) { int l = trail[--ntrail]; asg[l > 0 ? l : -l] = 0; }
    qh = ntrail;
    if (!ok) { printf("s NOT VERIFIED: lemma %ld is not RUP\n", nlem); return 1; }
    { long id = store(buf, n); hinsert(id, buf, n); }
    if (nlem % 500000 == 0) fprintf(stderr, "progress: %ld lemmas, %ld deletions applied, %ld unmatched\n", nlem, ndel_found, ndel_missing);
  }
  fclose(P);
  fprintf(stderr, "lemmas %ld, deletion lines %ld (applied %ld, unmatched %ld)\n", nlem, ndel, ndel_found, ndel_missing);
  if (conflict_top) { printf("s VERIFIED (%ld lemmas RUP-checked, %ld deletions applied, %ld unmatched)\n", nlem, ndel_found, ndel_missing); return 0; }
  printf("s NOT VERIFIED: no refutation reached\n"); return 1;
}
