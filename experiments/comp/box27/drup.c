/* L-COMP box 27: my own forward RUP proof checker (DRUP / the RUP part of DRAT), for the d 3 UNSAT certificates.
   Usage: drup F.cnf P.proof  -> "s VERIFIED" iff every added lemma is RUP w.r.t. the input clauses plus the lemmas before it,
   and the input plus the lemmas is refuted by unit propagation at the end (empty clause / top-level conflict).
   SOUNDNESS: every clause ever in the DB (input or checked lemma) is implied by the input formula, so a RUP step against ANY
   subset of the DB is sound. Mode IGNDEL=1 (env): deletion lines are ignored (the DB only grows; the version used for cube 1).
   Default: deletion lines remove the matching clause (same literal multiset after dedupe) from the DB; literals already assigned
   at top level stay assigned (each was implied when it was derived). Deleting only shrinks the DB, so it cannot make an unsound
   step pass; it can only make a check fail. No RAT step is accepted: a lemma that is not RUP makes the check FAIL.
   Textual proofs only (pysat get_proof lines written one per line). */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int nv = 0; static int *val; /* val[v] = 1 true, -1 false, 0 unassigned */
static int **cl; static int *clen; static long ncl = 0, capcl = 0; static char *cdel;
/* deletion index: hash of the sorted literal set -> clause ids (chained through hnext) */
static long *htab; static long hsize = 1 << 22; static long *hnext; static unsigned long long *chash;
static int cmpint(const void *a, const void *b) { int x = *(const int *)a, y = *(const int *)b; return (x > y) - (x < y); }
static unsigned long long hashlits(int *L, int n) { int *t = malloc(sizeof(int) * (n ? n : 1)); memcpy(t, L, sizeof(int) * n); qsort(t, n, sizeof(int), cmpint);
  unsigned long long h = 1469598103934665603ULL; for (int i = 0; i < n; i++) h = (h ^ (unsigned)t[i]) * 1099511628211ULL; free(t); return h ^ (unsigned long long)n; }
static long **wl; static int *wn, *wc; /* watch lists per literal index */
static int *trail; static int tn = 0, qhead = 0;
static int idx(int l) { return l > 0 ? 2 * l : 2 * (-l) + 1; }
static int lv(int l) { int v = val[abs(l)]; return l > 0 ? v : -v; }
static void watch(int l, long c) { int i = idx(l); if (wn[i] == wc[i]) { wc[i] = wc[i] ? 2 * wc[i] : 4; wl[i] = realloc(wl[i], sizeof(long) * wc[i]); } wl[i][wn[i]++] = c; }
static void assign(int l) { val[abs(l)] = l > 0 ? 1 : -1; trail[tn++] = l; }
static int propagate(void) { /* returns 1 on conflict */
  while (qhead < tn) { int p = trail[qhead++]; int fl = -p; int i = idx(fl); long *ws = wl[i]; int n = wn[i], j = 0;
    for (int k = 0; k < n; k++) { long c = ws[k]; if (cdel[c]) continue; int *C = cl[c];
      if (C[0] == fl) { C[0] = C[1]; C[1] = fl; }
      if (lv(C[0]) == 1) { ws[j++] = c; continue; }
      int found = 0;
      for (int m = 2; m < clen[c]; m++) if (lv(C[m]) != -1) { C[1] = C[m]; C[m] = fl; watch(C[1], c); found = 1; break; }
      if (found) continue;
      ws[j++] = c;
      if (lv(C[0]) == -1) { for (k++; k < n; k++) ws[j++] = ws[k]; wn[i] = j; return 1; }
      assign(C[0]); }
    wn[i] = j; }
  return 0; }
static int topconf = 0;
static void addclause(int *L, int n) { /* n >= 0 literals, deduped, no tautology; top-level state maintained */
  if (topconf) return;
  if (n == 0) { topconf = 1; return; }
  /* count non-false literals at top level */
  int nf = 0, sat = 0; for (int i = 0; i < n; i++) { if (lv(L[i]) == 1) sat = 1; if (lv(L[i]) != -1) nf++; }
  if (ncl == capcl) { capcl = capcl ? 2 * capcl : 1 << 16; cl = realloc(cl, sizeof(int *) * capcl); clen = realloc(clen, sizeof(int) * capcl);
    cdel = realloc(cdel, capcl); hnext = realloc(hnext, sizeof(long) * capcl); chash = realloc(chash, sizeof(unsigned long long) * capcl); }
  long c = ncl++; cdel[c] = 0; { unsigned long long h = hashlits(L, n); chash[c] = h; long b = h & (hsize - 1); hnext[c] = htab[b]; htab[b] = c; } cl[c] = malloc(sizeof(int) * (n > 1 ? n : 2)); memcpy(cl[c], L, sizeof(int) * n); clen[c] = n;
  if (n == 1) { if (lv(L[0]) == -1) topconf = 1; else if (lv(L[0]) == 0) { assign(L[0]); if (propagate()) topconf = 1; } return; }
  /* put two best literals first: non-false preferred */
  int *C = cl[c];
  for (int w = 0; w < 2; w++) for (int i = w; i < n; i++) if (lv(C[i]) != -1) { int t = C[w]; C[w] = C[i]; C[i] = t; break; }
  watch(C[0], c); watch(C[1], c);
  if (sat) return;
  if (nf == 0) { topconf = 1; return; }
  if (nf == 1) { assign(C[0]); if (propagate()) topconf = 1; } }
static long delclause(int *L, int n) { /* mark one live clause with the same literal set deleted; returns 1 if found */
  unsigned long long h = hashlits(L, n); long b = h & (hsize - 1);
  for (long c = htab[b]; c >= 0; c = hnext[c]) { if (cdel[c] || chash[c] != h || clen[c] != n) continue;
    int same = 1; for (int i = 0; i < n && same; i++) { int f = 0; for (int j = 0; j < n; j++) if (cl[c][j] == L[i]) { f = 1; break; } same = f; }
    if (!same) continue; cdel[c] = 1; free(cl[c]); cl[c] = NULL; return 1; }
  return 0; }
static int *buf; static int bcap = 0;
static int readclause(FILE *f, int *isdel) { /* returns length or -1 at EOF; skips comments / p line */
  int n = 0, x, ch; *isdel = 0;
  for (;;) { ch = fgetc(f); if (ch == EOF) return -1;
    if (ch == 'c' || ch == 'p') { while ((ch = fgetc(f)) != '\n' && ch != EOF); continue; }
    if (ch == 'd') { *isdel = 1; continue; }
    if (ch == ' ' || ch == '\n' || ch == '\r' || ch == '\t') continue;
    ungetc(ch, f); break; }
  while (fscanf(f, "%d", &x) == 1 && x != 0) { if (n == bcap) { bcap = bcap ? 2 * bcap : 64; buf = realloc(buf, sizeof(int) * bcap); } buf[n++] = x; }
  return n; }
static int norm(int n) { /* dedupe; return -1 if tautology */
  int m = 0; for (int i = 0; i < n; i++) { int dup = 0; for (int j = 0; j < m; j++) { if (buf[j] == buf[i]) dup = 1; if (buf[j] == -buf[i]) return -1; } if (!dup) buf[m++] = buf[i]; } return m; }
static void grow(int v) { if (v <= nv) return; int nn = v + 1000;
  val = realloc(val, sizeof(int) * (nn + 1)); memset(val + nv + 1, 0, sizeof(int) * (nn - nv));
  wl = realloc(wl, sizeof(long *) * (2 * nn + 2)); wn = realloc(wn, sizeof(int) * (2 * nn + 2)); wc = realloc(wc, sizeof(int) * (2 * nn + 2));
  for (int i = 2 * nv + 2; i < 2 * nn + 2; i++) { wl[i] = NULL; wn[i] = wc[i] = 0; }
  trail = realloc(trail, sizeof(int) * (nn + 1)); nv = nn; }
int main(int argc, char **argv) {
  FILE *F = fopen(argv[1], "r"), *P = fopen(argv[2], "r"); if (!F || !P) { printf("s ERROR open\n"); return 2; }
  int igndel = getenv("IGNDEL") != NULL; htab = malloc(sizeof(long) * hsize); for (long i = 0; i < hsize; i++) htab[i] = -1;
  grow(1); long nin = 0, nlem = 0, ndel = 0, ndelfound = 0; int d, n;
  while ((n = readclause(F, &d)) >= 0) { for (int i = 0; i < n; i++) grow(abs(buf[i])); n = norm(n); nin++; if (n < 0) continue; addclause(buf, n); }
  fprintf(stderr, "input clauses %ld, vars %d, top-level conflict after input: %d\n", nin, nv, topconf);
  while (!topconf && (n = readclause(P, &d)) >= 0) {
    if (d) { ndel++; if (!igndel) { for (int i = 0; i < n; i++) grow(abs(buf[i])); int m = norm(n); if (m > 0) ndelfound += delclause(buf, m); } continue; }
    for (int i = 0; i < n; i++) grow(abs(buf[i]));
    n = norm(n); nlem++; if (n < 0) continue;
    /* RUP check: assign the negation of every literal, propagate, expect a conflict */
    int base = tn, conf = 0;
    for (int i = 0; i < n && !conf; i++) { int l = buf[i]; if (lv(l) == 1) conf = 1; else if (lv(l) == 0) assign(-l); }
    if (!conf) conf = propagate();
    while (tn > base) val[abs(trail[--tn])] = 0; qhead = tn;
    if (!conf) { printf("s NOT VERIFIED: lemma %ld is not RUP\n", nlem); return 1; }
    addclause(buf, n); }
  fprintf(stderr, "lemmas checked %ld, deletion lines %ld (%s; clauses removed %ld)\n", nlem, ndel, igndel ? "ignored" : "applied", ndelfound);
  if (topconf) { printf("s VERIFIED (%ld lemmas RUP-checked)\n", nlem); return 0; }
  printf("s NOT VERIFIED: no refutation reached\n"); return 1; }
