/* REFEREE-2 succ. 28: independent forward RUP checker (second implementation; written without reusing drup.c code).
   Usage: r2rup F.cnf P.proof  ->  "R2RUP VERIFIED <lemmas>" iff every added lemma is RUP w.r.t. (input + earlier lemmas) and the
   final DB is refuted by unit propagation. Deletions are IGNORED (the DB only grows), which is sound: every DB clause is implied by the
   input. Every unit implication and every conflict is re-verified by scanning the WHOLE clause before it is used (so a watch-list bug
   can only lose propagations, never invent one). Strict parser: only '-', digits, spaces, newlines; 'p cnf' header in F; 'd' prefix in
   P; anything else aborts with "R2RUP PARSE ERROR". */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct { int *a; int n, cap; } vec;
static void push(vec *v, int x) { if (v->n == v->cap) { v->cap = v->cap ? 2 * v->cap : 4; v->a = realloc(v->a, sizeof(int) * v->cap); } v->a[v->n++] = x; }
static int NV = 0; static signed char *A; static vec *W; static int **CL; static int *CN; static int NC = 0, CAP = 0;
static int *TR; static int TN = 0, QH = 0, TCAP = 0;
static int L2I(int l) { return l > 0 ? 2 * l : -2 * l + 1; }
static int VAL(int l) { int v = A[abs(l)]; return l > 0 ? v : -v; }
static void ensure(int v) { if (v <= NV) return; int nn = v * 2 + 16; A = realloc(A, nn + 1); memset(A + NV + 1, 0, nn - NV);
  W = realloc(W, sizeof(vec) * (2 * nn + 2)); memset(W + 2 * NV + 2, 0, sizeof(vec) * (2 * nn - 2 * NV)); NV = nn;
  if (TCAP < nn + 1) { TCAP = nn + 1; TR = realloc(TR, sizeof(int) * TCAP); } }
static void SET(int l) { A[abs(l)] = l > 0 ? 1 : -1; TR[TN++] = l; }
static int unit_of(int c) { /* full scan: returns the unique non-false literal if all others false and it is unassigned; 0 if not unit;
                               -0x7fffffff if every literal is false (conflict); 1<<30 if satisfied */
  int u = 0, cnt = 0; for (int i = 0; i < CN[c]; i++) { int v = VAL(CL[c][i]); if (v == 1) return 1 << 30; if (v == 0) { cnt++; u = CL[c][i]; } }
  if (cnt == 0) return -0x7fffffff; if (cnt == 1) return u; return 0; }
static int prop(void) { /* 1 = conflict */
  while (QH < TN) { int f = -TR[QH++]; vec *w = &W[L2I(f)]; int j = 0;
    for (int k = 0; k < w->n; k++) { int c = w->a[k]; int *C = CL[c];
      if (C[0] == f) { C[0] = C[1]; C[1] = f; }
      if (C[1] != f) { continue; } /* stale entry (should not happen); dropped */
      if (VAL(C[0]) == 1) { w->a[j++] = c; continue; }
      int moved = 0; for (int m = 2; m < CN[c]; m++) if (VAL(C[m]) != -1) { int t = C[m]; C[m] = f; C[1] = t; push(&W[L2I(t)], c); moved = 1; break; }
      if (moved) continue;
      w->a[j++] = c; int u = unit_of(c);
      if (u == -0x7fffffff) { for (k++; k < w->n; k++) w->a[j++] = w->a[k]; w->n = j; return 1; }
      if (u != 0 && u != (1 << 30)) SET(u); }
    w->n = j; }
  return 0; }
static int TOPC = 0;
static void add(int *L, int n) { if (TOPC) return; if (NC == CAP) { CAP = CAP ? 2 * CAP : 65536; CL = realloc(CL, sizeof(int *) * CAP); CN = realloc(CN, sizeof(int) * CAP); }
  int c = NC++; CL[c] = malloc(sizeof(int) * (n < 2 ? 2 : n)); memcpy(CL[c], L, sizeof(int) * n); CN[c] = n;
  if (n == 0) { TOPC = 1; return; }
  if (n == 1) { int v = VAL(L[0]); if (v == -1) TOPC = 1; else if (v == 0) { SET(L[0]); if (prop()) TOPC = 1; } return; }
  int *C = CL[c]; /* move non-false literals to the front */
  for (int p = 0, i = 0; i < n && p < 2; i++) if (VAL(C[i]) != -1) { int t = C[p]; C[p] = C[i]; C[i] = t; p++; }
  push(&W[L2I(C[0])], c); push(&W[L2I(C[1])], c);
  int u = unit_of(c); if (u == -0x7fffffff) TOPC = 1; else if (u != 0 && u != (1 << 30)) { SET(u); if (prop()) TOPC = 1; } }
static vec B; static long LINE = 0;
static int rd(FILE *f, int inproof, int *isdel) { /* -1 EOF; else clause length in B; strict */
  int ch; B.n = 0; *isdel = 0; long x = 0; int neg = 0, innum = 0, started = 0;
  for (;;) { ch = fgetc(f);
    if (ch == EOF) { if (innum || started) { fprintf(stderr, "R2RUP PARSE ERROR: clause without 0 at EOF\n"); exit(3); } return -1; }
    if (!started && !innum && (ch == 'p') && !inproof) { while ((ch = fgetc(f)) != '\n' && ch != EOF); LINE++; continue; }
    if (!started && !innum && ch == 'd' && inproof && !*isdel) { *isdel = 1; started = 1; continue; }
    if (ch == '-') { if (innum || neg) goto bad; neg = 1; continue; }
    if (ch >= '0' && ch <= '9') { x = x * 10 + (ch - '0'); innum = 1; started = 1; if (x > 100000000) goto bad; continue; }
    if (ch == ' ' || ch == '\n') { if (ch == '\n') LINE++;
      if (innum) { if (x == 0) { if (neg) goto bad; return B.n; } push(&B, neg ? -(int)x : (int)x); x = 0; neg = 0; innum = 0; }
      else if (neg) goto bad;
      continue; }
    bad: fprintf(stderr, "R2RUP PARSE ERROR near line %ld (char %d)\n", LINE, ch); exit(3); } }
static int norm(void) { int m = 0; for (int i = 0; i < B.n; i++) { int dup = 0; for (int j = 0; j < m; j++) { if (B.a[j] == -B.a[i]) return -1; if (B.a[j] == B.a[i]) dup = 1; } if (!dup) B.a[m++] = B.a[i]; } B.n = m; return m; }
int main(int argc, char **argv) {
  FILE *F = fopen(argv[1], "r"), *P = fopen(argv[2], "r"); if (!F || !P) { puts("R2RUP OPEN ERROR"); return 2; }
  ensure(1); int d, n; long nin = 0, nlem = 0, ndel = 0;
  while ((n = rd(F, 0, &d)) >= 0) { for (int i = 0; i < n; i++) ensure(abs(B.a[i])); nin++; if (norm() < 0) continue; add(B.a, B.n); }
  fprintf(stderr, "input %ld clauses, top conflict after input %d\n", nin, TOPC);
  LINE = 0;
  while (!TOPC && (n = rd(P, 1, &d)) >= 0) {
    if (d) { ndel++; continue; }
    for (int i = 0; i < n; i++) ensure(abs(B.a[i])); nlem++; if (norm() < 0) continue;
    int base = TN, ok = 0;
    for (int i = 0; i < B.n && !ok; i++) { int v = VAL(B.a[i]); if (v == 1) ok = 1; else if (v == 0) SET(-B.a[i]); }
    if (!ok) ok = prop();
    while (TN > base) A[abs(TR[--TN])] = 0; QH = TN;
    if (!ok) { printf("R2RUP NOT VERIFIED: lemma %ld not RUP\n", nlem); return 1; }
    add(B.a, B.n); }
  fprintf(stderr, "lemmas %ld, deletions ignored %ld\n", nlem, ndel);
  if (TOPC) { printf("R2RUP VERIFIED %ld\n", nlem); return 0; }
  puts("R2RUP NOT VERIFIED: no refutation"); return 1; }
