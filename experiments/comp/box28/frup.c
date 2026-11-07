/* L-COMP box 28 (successor 10): frup, my own FORWARD RUP proof checker with deletions applied; written for speed, with the same
   check semantics as box27/drup.c (which it must agree with: README "frup cross-validation").
   Usage: frup F.cnf P.proof   -> prints "s VERIFIED (n lemmas RUP-checked)" and exits 0, or "s NOT VERIFIED: ..." and exits 1.
   SEMANTICS (identical to drup.c, default mode):
   - Input clauses: duplicates inside a clause removed; tautologies skipped; the empty clause or a top-level conflict sets TOPCONF.
   - Proof lines: "l1 ... lk 0" = lemma, "d l1 ... lk 0" = deletion; comment lines 'c' and a 'p' line are skipped.
   - Lemma (after dedupe; a tautology is counted and skipped): RUP check = on top of the top-level assignment, assign the negation of
     each literal in order (if a literal is already TRUE at top level the lemma is accepted at once), unit-propagate over the live
     clause DB; accepted iff a conflict arises. A lemma that fails stops the check: "s NOT VERIFIED: lemma i is not RUP".
     An accepted lemma joins the DB (unit / all-false handling at top level as for input clauses).
   - Deletion: removes ONE live DB clause with the same literal set (after dedupe), if any; top-level assigned literals stay
     assigned (each was implied when derived). Deleting cannot make an unsound step pass; it can only make a later check fail.
   - Verdict: VERIFIED iff TOPCONF is reached (the check stops there); otherwise "s NOT VERIFIED: no refutation reached".
   SOUNDNESS: every clause ever in the DB is implied by the input formula, so RUP against any subset of the DB is sound.
   DIFFERENCES FROM drup.c (implementation only): watch entries carry a "blocker" literal of the clause (if it is true the clause
   is skipped without reading it); clause ids index a pointer table and deleted clauses are dropped lazily from watch lists (as
   drup.c); a buffered integer parser instead of fscanf; the deletion hash sorts into a reusable buffer. No RAT, no backward mode. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

typedef struct { int cid; int blk; } W;
static int nv = 0; static signed char *val;            /* val[v] = 1 true, -1 false, 0 unassigned */
static int **cl; static long ncl = 0, capcl = 0;        /* cl[c] = int[len + 1]: cl[c][0] = len, literals from cl[c] + 1; NULL = deleted */
static uint64_t *chash; static long *hnext; static long *htab; static const long HS = 1L << 24;
static W **wl; static int *wn, *wc;
static int *trail; static int tn = 0, qhead = 0; static int topconf = 0;

static inline int idx(int l) { return l > 0 ? 2 * l : 2 * (-l) + 1; }
static inline int lv(int l) { int v = val[l > 0 ? l : -l]; return l > 0 ? v : -v; }
static inline void assign(int l) { val[l > 0 ? l : -l] = l > 0 ? 1 : -1; trail[tn++] = l; }
static void watch(int l, int c, int blk) { int i = idx(l);
  if (wn[i] == wc[i]) { wc[i] = wc[i] ? 2 * wc[i] : 4; wl[i] = realloc(wl[i], sizeof(W) * wc[i]); if (!wl[i]) { printf("s ERROR memory\n"); exit(2); } }
  wl[i][wn[i]++] = (W){c, blk}; }

static int propagate(void) { /* 1 on conflict */
  while (qhead < tn) { int fl = -trail[qhead++]; int i = idx(fl); W *ws = wl[i]; int n = wn[i], j = 0, k;
    for (k = 0; k < n; k++) { W w = ws[k];
      if (lv(w.blk) == 1) { ws[j++] = w; continue; }
      int *C = cl[w.cid]; if (!C) continue;                     /* deleted: drop the watch */
      int len = C[0]; int *L = C + 1;
      if (L[0] == fl) { L[0] = L[1]; L[1] = fl; }
      if (lv(L[0]) == 1) { ws[j++] = (W){w.cid, L[0]}; continue; }
      int found = 0;
      for (int m = 2; m < len; m++) if (lv(L[m]) != -1) { L[1] = L[m]; L[m] = fl; watch(L[1], w.cid, L[0]); found = 1; break; }
      if (found) continue;
      ws[j++] = (W){w.cid, L[0]};
      if (lv(L[0]) == -1) { for (k++; k < n; k++) ws[j++] = ws[k]; wn[i] = j; return 1; }
      assign(L[0]); }
    wn[i] = j; }
  return 0; }

static int *sbuf; static int scap = 0;
static int cmpint(const void *a, const void *b) { int x = *(const int *)a, y = *(const int *)b; return (x > y) - (x < y); }
static uint64_t hashset(const int *L, int n) { if (n > scap) { scap = 2 * n; sbuf = realloc(sbuf, sizeof(int) * scap); }
  memcpy(sbuf, L, sizeof(int) * n); qsort(sbuf, n, sizeof(int), cmpint);
  uint64_t h = 1469598103934665603ULL; for (int i = 0; i < n; i++) h = (h ^ (uint32_t)sbuf[i]) * 1099511628211ULL; return h ^ (uint64_t)n; }

static void addclause(const int *L, int n) { /* deduped, no tautology */
  if (topconf) return;
  if (n == 0) { topconf = 1; return; }
  int nf = 0, sat = 0; for (int i = 0; i < n; i++) { int v = lv(L[i]); if (v == 1) sat = 1; if (v != -1) nf++; }
  if (ncl == capcl) { capcl = capcl ? 2 * capcl : 1 << 20; cl = realloc(cl, sizeof(int *) * capcl); chash = realloc(chash, sizeof(uint64_t) * capcl);
    hnext = realloc(hnext, sizeof(long) * capcl); if (!cl || !chash || !hnext) { printf("s ERROR memory\n"); exit(2); } }
  long c = ncl++; int *C = malloc(sizeof(int) * (n + 1)); if (!C) { printf("s ERROR memory\n"); exit(2); }
  C[0] = n; memcpy(C + 1, L, sizeof(int) * n); cl[c] = C;
  uint64_t h = hashset(L, n); chash[c] = h; long b = (long)(h & (HS - 1)); hnext[c] = htab[b]; htab[b] = c;
  int *K = C + 1;
  if (n == 1) { if (lv(K[0]) == -1) topconf = 1; else if (lv(K[0]) == 0) { assign(K[0]); if (propagate()) topconf = 1; } return; }
  for (int w = 0; w < 2; w++) for (int i = w; i < n; i++) if (lv(K[i]) != -1) { int t = K[w]; K[w] = K[i]; K[i] = t; break; }
  watch(K[0], (int)c, K[1]); watch(K[1], (int)c, K[0]);
  if (sat) return;
  if (nf == 0) { topconf = 1; return; }
  if (nf == 1) { assign(K[0]); if (propagate()) topconf = 1; } }

static long delclause(const int *L, int n) { /* one live clause with the same literal set */
  uint64_t h = hashset(L, n); long b = (long)(h & (HS - 1));
  for (long c = htab[b]; c >= 0; c = hnext[c]) { int *C = cl[c]; if (!C || chash[c] != h || C[0] != n) continue;
    int same = 1; for (int i = 0; i < n && same; i++) { int f = 0; for (int j = 1; j <= n; j++) if (C[j] == L[i]) { f = 1; break; } same = f; }
    if (!same) continue; free(C); cl[c] = NULL; return 1; }
  return 0; }

/* buffered parser */
typedef struct { FILE *f; char *b; size_t n, p; } R;
static char *bigbuf(void) { char *b = malloc(1 << 22); if (!b) { printf("s ERROR memory\n"); exit(2); } return b; }
static inline int rc(R *r) { if (r->p == r->n) { r->n = fread(r->b, 1, 1 << 22, r->f); r->p = 0; if (r->n == 0) return EOF; } return (unsigned char)r->b[r->p++]; }
static int *buf; static int bcap = 0;
static int readclause(R *r, int *isdel) { /* length, or -1 at EOF */
  int n = 0, ch; *isdel = 0;
  for (;;) { ch = rc(r); if (ch == EOF) return -1;
    if (ch == 'c' || ch == 'p') { while ((ch = rc(r)) != '\n' && ch != EOF); continue; }
    if (ch == 'd') { *isdel = 1; continue; }
    if (ch == ' ' || ch == '\n' || ch == '\r' || ch == '\t') continue;
    break; }
  for (;;) { /* ch holds the first character of a number */
    int neg = 0; long x = 0; if (ch == '-') { neg = 1; ch = rc(r); }
    if (ch < '0' || ch > '9') { printf("s ERROR parse\n"); exit(2); }
    while (ch >= '0' && ch <= '9') { x = 10 * x + (ch - '0'); if (x > 2000000000L) { printf("s ERROR parse\n"); exit(2); } ch = rc(r); }
    if (x == 0) return n;
    if (n == bcap) { bcap = bcap ? 2 * bcap : 64; buf = realloc(buf, sizeof(int) * bcap); }
    buf[n++] = neg ? -(int)x : (int)x;
    while (ch == ' ' || ch == '\t' || ch == '\r' || ch == '\n') ch = rc(r);
    if (ch == EOF) { printf("s ERROR parse (clause without 0)\n"); exit(2); } } }
static int norm(int n) { int m = 0; for (int i = 0; i < n; i++) { int dup = 0; for (int j = 0; j < m; j++) { if (buf[j] == buf[i]) dup = 1; if (buf[j] == -buf[i]) return -1; } if (!dup) buf[m++] = buf[i]; } return m; }
static void grow(int v) { if (v <= nv) return; int nn = v + 100000;
  val = realloc(val, nn + 1); memset(val + nv + 1, 0, nn - nv);
  wl = realloc(wl, sizeof(W *) * (2 * (size_t)nn + 2)); wn = realloc(wn, sizeof(int) * (2 * (size_t)nn + 2)); wc = realloc(wc, sizeof(int) * (2 * (size_t)nn + 2));
  for (long i = 2 * (long)nv + 2; i < 2 * (long)nn + 2; i++) { wl[i] = NULL; wn[i] = wc[i] = 0; }
  trail = realloc(trail, sizeof(int) * (nn + 1)); nv = nn; }

int main(int argc, char **argv) {
  if (argc < 3) { printf("usage: frup F.cnf P.proof\n"); return 2; }
  FILE *F = fopen(argv[1], "r"), *P = fopen(argv[2], "r"); if (!F || !P) { printf("s ERROR open\n"); return 2; }
  R rf = {F, bigbuf(), 0, 0}, rp = {P, bigbuf(), 0, 0};
  htab = malloc(sizeof(long) * HS); for (long i = 0; i < HS; i++) htab[i] = -1;
  grow(1); long nin = 0, nlem = 0, ndel = 0, ndelfound = 0; int d, n;
  while ((n = readclause(&rf, &d)) >= 0) { for (int i = 0; i < n; i++) grow(abs(buf[i])); n = norm(n); nin++; if (n < 0) continue; addclause(buf, n); }
  fprintf(stderr, "input clauses %ld, top-level conflict after input: %d\n", nin, topconf);
  while (!topconf && (n = readclause(&rp, &d)) >= 0) {
    for (int i = 0; i < n; i++) grow(abs(buf[i]));
    if (d) { ndel++; int m = norm(n); if (m > 0) ndelfound += delclause(buf, m); continue; }
    n = norm(n); nlem++; if (n < 0) continue;
    int base = tn, conf = 0;
    for (int i = 0; i < n && !conf; i++) { int l = buf[i]; int v = lv(l); if (v == 1) conf = 1; else if (v == 0) assign(-l); }
    if (!conf) conf = propagate();
    while (tn > base) val[abs(trail[--tn])] = 0; qhead = tn;
    if (!conf) { printf("s NOT VERIFIED: lemma %ld is not RUP\n", nlem); return 1; }
    addclause(buf, n); }
  fprintf(stderr, "lemmas checked %ld, deletion lines %ld (applied; clauses removed %ld)\n", nlem, ndel, ndelfound);
  if (topconf) { printf("s VERIFIED (%ld lemmas RUP-checked)\n", nlem); return 0; }
  printf("s NOT VERIFIED: no refutation reached\n"); return 1; }
