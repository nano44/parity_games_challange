/* L-COMP box 47: annealing search on T_key over Ξ-acyclic genomes with an e-vertex numbering (gen47.h), model = MODEL (compile with
   -DMODEL='"one47.h"'; the model provides  long run1p(const Gen *g, long cap, long *sw)  = T, the number of steps of the model run before
   its first fallback / stop, or -1 on an error; sw[x] = the number of steps at which mover x switches).
   Objectives (env SCORE): T (default): T, ties smaller N + M. K: the ENUMERATION DEPTH k(G) (Lead 09:15Z, L-NEW box 217 §5 track A) = the largest
   k such that a level-(k − 1) mover x makes sw(x) = |K(x)| − 1 switches, |K(x)| = the number of W-paths from x to level 0 (= its keys; saturating
   at 2^62); score (k, T), ties smaller N + M. Every best line logs T, k, the depth d = max level + 1, N, M. Moves: gen47.h gmutate (wt, xt kept acyclic, gate order, β rank, β parity, start, e-numbering
   (transpositions, short rotations), add / remove option), 1-3 moves per proposal. Size: N fixed by the seed (lanes lift N beforehand),
   N + M <= CAP. Score: T (larger better; ties: smaller N + M). Annealing: accept a worse proposal with prob exp(-(T - T')/temp), temp
   from TEMP0 to 0 linearly within each unit of UNIT proposals; every unit restarts from the lane's best.
   Resumable: OUT.state (iteration, RNG state, current and best genome). Every NEW best: OUT_BEST_T<T>_N<N>_NM<N+M>.txt + a BEST line in OUT.log.
   Usage: search47 seed.txt OUT CAP ITERS SEED [TEMP0 UNIT]   (OUT = path prefix) */
#include "gen47.h"
#include <math.h>
#include <time.h>
#ifndef MODEL
#error "compile with -DMODEL='\"model.h\"'"
#endif
#include MODEL
static unsigned long long fnv(const Gen *g) { unsigned long long h = 1469598103934665603ULL; const int *cols[7] = { g->ox, g->wt, g->xt, g->gt, g->br, g->bp, g->er };
  for (int c = 0; c < 7; c++) for (int i = 0; i < g->M; i++) { h ^= (unsigned)cols[c][i] + 7; h *= 1099511628211ULL; }
  for (int x = 0; x < g->N; x++) { h ^= (unsigned)g->st[x] + 3 + 97 * (unsigned)g->lev[x]; h *= 1099511628211ULL; } return h; }
static Gen cur, best, prop; static long SW[GMAXN]; static int KMODE;
static int kdepth(const Gen *g, const long *sw) {   /* enumeration depth k(G); levels processed bottom-up */
  static long P[GMAXN]; int maxl = 0, k = 0; for (int x = 0; x < g->N; x++) if (g->lev[x] > maxl) maxl = g->lev[x];
  for (int l = 0; l <= maxl; l++) for (int x = 0; x < g->N; x++) if (g->lev[x] == l) { long p = 0;
    for (int i = g->first[x]; i < g->first[x + 1]; i++) { long a = l ? P[g->wt[i]] : 1; p = (p > (1L << 62) - a) ? (1L << 62) : p + a; }
    P[x] = p; if (sw[x] == p - 1 && l + 1 > k) k = l + 1; }
  return k; }
static int depth(const Gen *g) { int m = 0; for (int x = 0; x < g->N; x++) if (g->lev[x] > m) m = g->lev[x]; return m + 1; }
/* score of a run: (k, T) in K mode, T otherwise, packed into one long */
static long score(const Gen *g, long T) { if (!KMODE) return T; long t = T < (1L << 40) ? T : (1L << 40) - 1; return ((long)kdepth(g, SW) << 40) | t; }
int main(int argc, char **argv) {
  if (argc < 6) { fprintf(stderr, "usage\n"); return 2; }
  const char *out = argv[2]; int CAP = atoi(argv[3]); long ITERS = atol(argv[4]); unsigned long long SEED = strtoull(argv[5], 0, 10);
  double TEMP0 = argc > 6 ? atof(argv[6]) : 2.0; long UNIT = argc > 7 ? atol(argv[7]) : 20000; long CAPT = 1L << 40;
  char sp[4096], lp[4096]; snprintf(sp, sizeof sp, "%s.state", out); snprintf(lp, sizeof lp, "%s.log", out);
  KMODE = getenv("SCORE") && !strcmp(getenv("SCORE"), "K");
  long it = 0; long tc, tb; FILE *f = fopen(sp, "r");
  if (f) { if (fscanf(f, "%ld %llu %ld %ld", &it, &grs, &tc, &tb) != 4 || !gread(&cur, f) || !gread(&best, f)) { fprintf(stderr, "bad state\n"); return 2; } fclose(f); }
  else { f = fopen(argv[1], "r"); if (!f || !gread(&cur, f)) { fprintf(stderr, "bad seed\n"); return 2; } fclose(f);
         if (!gvalid(&cur)) { fprintf(stderr, "seed invalid (structure or Ξ-cyclic)\n"); return 2; }
         grs = SEED * 2654435761ULL + 12345; if (!grs) grs = 1; { long T0 = run1p(&cur, CAPT, SW); tc = tb = score(&cur, T0); } best = cur;
         FILE *L = fopen(lp, "a"); fprintf(L, "START seed %s N %d M %d N+M %d d %d score %ld (k %ld T %ld) SCORE %s CAP %d ITERS %ld SEED %llu TEMP0 %g UNIT %ld\n", argv[1], cur.N, cur.M, cur.N + cur.M, depth(&cur), tc, KMODE ? tc >> 40 : -1L, KMODE ? tc & ((1L << 40) - 1) : tc, KMODE ? "K" : "T", CAP, ITERS, SEED, TEMP0, UNIT); fclose(L); }
  time_t t0 = time(0), tsave = t0; long errs = 0, acc = 0;
  for (; it < ITERS; it++) {
    if (it % UNIT == 0 && it) { cur = best; tc = tb; }
    double temp = TEMP0 * (1.0 - (double)(it % UNIT) / UNIT);
    prop = cur; int nm = 1 + gr(3), done = 0; for (int k = 0; k < nm; k++) if (gmutate(&prop, CAP, 1) >= 0) done++;
    if (!done) continue;
    long tp = run1p(&prop, CAPT, SW); if (tp < 0) { errs++; continue; } tp = score(&prop, tp);
    int better = tp > tc || (tp == tc && prop.N + prop.M <= cur.N + cur.M);
    if (better || (temp > 0 && (double)(grnd() % 1000000) / 1e6 < exp(-(double)(KMODE && (tc >> 40) != (tp >> 40) ? 1000000 : (tc - tp)) / temp))) { cur = prop; tc = tp; acc++;
      if (tc > tb || (tc == tb && cur.N + cur.M < best.N + best.M)) { int newT = KMODE ? ((tc >> 40) > (tb >> 40) || ((tb >> 40) == 0 && tc > tb)) : tc > tb; best = cur; tb = tc;
        if (newT) { char bp[4096]; long bk = KMODE ? tb >> 40 : -1, bT = KMODE ? tb & ((1L << 40) - 1) : tb;
          snprintf(bp, sizeof bp, "%s_BEST_k%ld_T%ld_d%d_N%d_NM%d_%016llx.txt", out, bk, bT, depth(&best), best.N, best.N + best.M, fnv(&best));
          FILE *B = fopen(bp, "w"); gwrite(&best, B); fclose(B);
          FILE *L = fopen(lp, "a"); fprintf(L, "BEST k %ld T %ld d %d N %d M %d N+M %d file %s iter %ld acc %ld errs %ld sec %ld\n", bk, bT, depth(&best), best.N, best.M, best.N + best.M, bp, it, acc, errs, (long)(time(0) - t0)); fclose(L); } } }
    if (time(0) - tsave >= 30 || it + 1 == ITERS) { char tp2[4200]; snprintf(tp2, sizeof tp2, "%s.tmp", sp); FILE *S = fopen(tp2, "w");
      fprintf(S, "%ld %llu %ld %ld\n", it + 1, grs, tc, tb); gwrite(&cur, S); gwrite(&best, S); fclose(S); rename(tp2, sp); tsave = time(0); } }
  FILE *L = fopen(lp, "a"); fprintf(L, "DONE iters %ld best score %ld (k %ld T %ld) d %d N %d M %d N+M %d errs %ld\n", ITERS, tb, KMODE ? tb >> 40 : -1L, KMODE ? tb & ((1L << 40) - 1) : tb, depth(&best), best.N, best.M, best.N + best.M, errs); fclose(L);
  return 0; }
