/* REFEREE successor 24: my own forward RUP checker, written independently of L-COMP's drup.c (I read drup.c for the audit but
   did not copy it). Purpose: an independent second check of the Glucose 4 DRUP proofs of P-TR3 (claude/l-comp d03d8370).
   Design (deliberately simple):
   - DIMACS: the header "p cnf V C" is REQUIRED; exactly C clauses, each ending in 0, literals in [-V, V] \ {0}; else ERROR.
   - Proof: one item per line; "d ..." lines are IGNORED (the clause DB only grows: sound, since every DB clause is implied by the
     input); every other line is a lemma "l1 ... lk 0" (k >= 0), literals checked against V (a lemma may not add new variables).
   - A lemma is accepted iff it is RUP w.r.t. the input plus all earlier accepted lemmas: some literal is true at top level, or
     assigning the negation of every literal and unit-propagating gives a conflict. Otherwise: "s NOT VERIFIED" (no RAT).
   - "s VERIFIED" iff the top-level unit propagation of the DB reaches a conflict (by the input alone, or after some lemma).
   Propagation: two watched literals per clause of length >= 2; unit clauses assigned at top level.
   Usage: ref_rup F.cnf P.proof */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int V;                       /* number of variables */
static signed char *asg;            /* asg[v] in {-1, 0, 1} */
static int *trail, ntrail, qh;      /* assignment trail and propagation head */
static int *lits; static long nlits, caplits;   /* flat literal store */
static long *start; static int *len; static long ncls, capcls;
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
      long c = w[i]; int *L = lits + start[c];
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
static void store(int *c, int n) {
  if (conflict_top) return;
  if (nlits + n > caplits) { caplits = 2 * (nlits + n) + 1024; lits = realloc(lits, sizeof(int) * caplits); }
  if (ncls == capcls) { capcls = capcls ? 2 * capcls : 65536; start = realloc(start, sizeof(long) * capcls); len = realloc(len, sizeof(int) * capcls); }
  long id = ncls++; start[id] = nlits; len[id] = n; memcpy(lits + nlits, c, sizeof(int) * n); nlits += n;
  int *L = lits + start[id];
  if (n == 0) { conflict_top = 1; return; }
  /* move non-false literals to the front */
  int nf = 0, i;
  for (i = 0; i < n; i++) if (value(L[i]) != -1) { int t = L[nf]; L[nf] = L[i]; L[i] = t; nf++; }
  for (i = 0; i < nf; i++) if (value(L[i]) == 1) { if (n >= 2) { addwatch(L[0], id); addwatch(L[1], id); } return; }  /* satisfied */
  if (nf == 0) { conflict_top = 1; return; }
  if (n >= 2) { addwatch(L[0], id); addwatch(L[1], id); }
  if (nf == 1) { setlit(L[0]); if (prop()) conflict_top = 1; }
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
  if (argc != 3) { fprintf(stderr, "usage: ref_rup F.cnf P.proof\n"); return 2; }
  FILE *F = fopen(argv[1], "r"); if (!F) { printf("s ERROR cnf\n"); return 2; }
  char line[256]; long C = -1;
  while (fgets(line, sizeof line, F)) { if (line[0] == 'c') continue; if (sscanf(line, "p cnf %d %ld", &V, &C) == 2) break; printf("s ERROR header\n"); return 2; }
  if (C < 0 || V <= 0) { printf("s ERROR header\n"); return 2; }
  asg = calloc(V + 1, 1); trail = malloc(sizeof(int) * (V + 1));
  wat = calloc(2 * V + 2, sizeof(long *)); wn = calloc(2 * V + 2, sizeof(int)); wcap = calloc(2 * V + 2, sizeof(int));
  long ci; int x;
  for (ci = 0; ci < C; ci++) {
    int n = 0;
    for (;;) { if (fscanf(F, "%d", &x) != 1) { printf("s ERROR clause %ld truncated\n", ci); return 2; }
      if (x == 0) break; if (x > V || x < -V) { printf("s ERROR literal %d out of range\n", x); return 2; } n = push(x, n); }
    n = clean(n); if (n < 0) continue; store(buf, n);
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
    if (del) { ndel++; continue; }
    nlem++;
    n = clean(n); if (n < 0) continue;                    /* tautology: trivially implied; not stored */
    int base = ntrail, ok = 0, i;
    for (i = 0; i < n && !ok; i++) { int v = value(buf[i]); if (v == 1) ok = 1; else if (v == 0) setlit(-buf[i]); }
    if (!ok) ok = prop();
    while (ntrail > base) { int l = trail[--ntrail]; asg[l > 0 ? l : -l] = 0; }
    qh = ntrail;
    if (!ok) { printf("s NOT VERIFIED: lemma %ld is not RUP\n", nlem); return 1; }
    store(buf, n);
  }
  fclose(P);
  fprintf(stderr, "lemmas %ld, deletion lines ignored %ld\n", nlem, ndel);
  if (conflict_top) { printf("s VERIFIED (%ld lemmas RUP-checked, deletions ignored)\n", nlem); return 0; }
  printf("s NOT VERIFIED: no refutation reached\n"); return 1;
}
