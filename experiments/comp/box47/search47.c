/* L-COMP box 47: annealing search on T_key over Ξ-acyclic genomes with an e-vertex numbering (gen47.h), model = MODEL (compile with
   -DMODEL='"one47.h"'; the model provides  long run1p(const Gen *g, long cap, long *sw)  = T, the number of steps of the model run before
   its first fallback / stop, or -1 on an error; sw[x] = the number of steps at which mover x switches).
   K modes (K, KD, KR; Lead 12:08Z / REFEREE-2 41): every mover of the seed must have degree exactly 2 (asserted) and the add / remove-option
   moves are OFF, so every genome of a K lane has degree 2 (a degree-1 mover counts as «full» with |K| = 1, sw = 0 and inflates k).
   Objectives (env SCORE): T (default): T, ties smaller N + M. K: the ENUMERATION DEPTH k(G) (Lead 09:15Z, L-NEW box 217 §5 track A) = the largest
   k such that a level-(k − 1) mover x makes sw(x) = |K(x)| − 1 switches, |K(x)| = the number of W-paths from x to level 0 (= its keys; saturating
   at 2^62); SCORE=KD: the same with kfront = max over level-k movers of sw − (|K| − 1) (the deficit to a full enumeration, 0 = full),
   stored + 2^19 (BEST lines show it so offset). SCORE=KR: kfront = max over level-k movers of floor(2^19 · sw / (|K| − 1)) (the ratio).
   CLASS=UP: moves restricted to the upward-ladder class (see upmutate). score (k, kfront, T) with kfront = the largest sw of a level-k mover (the next level; a gradient toward k + 1), ties smaller N + M. Every best line logs T, k, the depth d = max level + 1, N, M. Moves: gen47.h gmutate (wt, xt kept acyclic, gate order, β rank, β parity, start, e-numbering
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
/* CLASS=UP (Lead 12:12Z, L-SI 55's UPWARD LADDERS): 2 movers per level (2l, 2l + 1), each with 2 options whose W-targets are the two movers
   one level down; every Ξ-target a mover of a STRICTLY HIGHER level, or X; β ranks increasing with the level (options of level l hold ranks
   4l .. 4l + 3); e-numbering = gate order (er = gt: R104's IDEAL model). Moves stay inside the class: swap the W-targets of a mover's two
   options; re-draw one Ξ-target; swap two gate indices (er follows); swap two β ranks of one level; flip a β parity; flip a start. */
static int UPCLASS;
static int upmutate(Gen *g) {
  int M = g->M, i = gr(M), r = gr(6), t;
  switch (r) {
  case 0: { int x = g->ox[i]; if (!g->lev[x]) return -1; int a = g->first[x]; t = g->wt[a]; g->wt[a] = g->wt[a + 1]; g->wt[a + 1] = t; return 0; }
  case 1: { int l = g->lev[g->ox[i]], c = 0, pick = -1; for (int y = 0; y < g->N; y++) if (g->lev[y] > l && gr(++c) == 0) pick = y;
            if (gr(c + 1) == 0) pick = -1; g->xt[i] = pick; return 1; }
  case 2: { int j = gr(M); t = g->gt[i]; g->gt[i] = g->gt[j]; g->gt[j] = t; g->er[i] = g->gt[i]; g->er[j] = g->gt[j]; return 2; }
  case 3: { int l = g->lev[g->ox[i]], j = 4 * l + gr(4); if (j >= M) return -1; int jj = -1; for (int q = g->first[2 * l]; q < M && g->lev[g->ox[q]] == l; q++) if (q == j) jj = q;
            if (jj < 0) return -1; t = g->br[i]; g->br[i] = g->br[jj]; g->br[jj] = t; return 3; }
  case 4: g->bp[i] ^= 1; return 4;
  case 5: { int x = gr(g->N); g->st[x] ^= 1; return 5; }
  } return -1; }
static Gen cur, best, prop; static long SW[GMAXN]; static int KMODE;
static long maxsw;    /* set by kdepth: max_x sw(x) */
static long khalf;    /* set by kdepth: the «half enumeration» depth (Lead 10:03Z): largest level l with a level-l mover at sw >= |K|/2 - 1 */
static long kfront;   /* set by kdepth: the largest sw over movers of level k (the next level to enumerate) */
static int kdepth(const Gen *g, const long *sw) {   /* enumeration depth k(G); levels processed bottom-up */
  static long P[GMAXN]; int maxl = 0, k = 0; for (int x = 0; x < g->N; x++) if (g->lev[x] > maxl) maxl = g->lev[x];
  for (int l = 0; l <= maxl; l++) for (int x = 0; x < g->N; x++) if (g->lev[x] == l) { long p = 0;
    for (int i = g->first[x]; i < g->first[x + 1]; i++) { long a = l ? P[g->wt[i]] : 1; p = (p > (1L << 62) - a) ? (1L << 62) : p + a; }
    P[x] = p; if (sw[x] == p - 1 && l + 1 > k) k = l + 1; }
  kfront = KMODE == 2 ? -(1L << 40) : 0; khalf = -1; maxsw = 0; for (int x = 0; x < g->N; x++) { if (sw[x] > maxsw) maxsw = sw[x]; if (g->lev[x] == k) { long f = KMODE == 2 ? sw[x] - (P[x] - 1) : KMODE == 3 ? (P[x] > 1 && P[x] < (1L << 40) ? (sw[x] << 19) / (P[x] - 1) : 0) : sw[x]; if (f > kfront) kfront = f; } if (P[x] >= 2 && sw[x] >= P[x] / 2 - 1 && g->lev[x] > khalf) khalf = g->lev[x]; }
  return k; }
static int depth(const Gen *g) { int m = 0; for (int x = 0; x < g->N; x++) if (g->lev[x] > m) m = g->lev[x]; return m + 1; }
/* score of a run: T mode: T. K mode: (k, kfront, T) packed as k << 40 | min(kfront, 2^20 - 1) << 20 | min(T, 2^20 - 1) */
#define KF(sc) (((sc) >> 20) & ((1L << 20) - 1))
#define KT(sc) ((sc) & ((1L << 20) - 1))
static long score(const Gen *g, long T) { if (!KMODE) return T; long k = kdepth(g, SW), f = KMODE == 2 ? kfront + (1L << 19) : kfront; f = f < 0 ? 0 : f < (1L << 20) ? f : (1L << 20) - 1; long t = T < (1L << 20) ? T : (1L << 20) - 1;
  return (k << 40) | (f << 20) | t; }
int main(int argc, char **argv) {
  if (argc < 6) { fprintf(stderr, "usage\n"); return 2; }
  const char *out = argv[2]; int CAP = atoi(argv[3]); long ITERS = atol(argv[4]); unsigned long long SEED = strtoull(argv[5], 0, 10);
  double TEMP0 = argc > 6 ? atof(argv[6]) : 2.0; long UNIT = argc > 7 ? atol(argv[7]) : 20000; long CAPT = 1L << 40;
  char sp[4096], lp[4096]; snprintf(sp, sizeof sp, "%s.state", out); snprintf(lp, sizeof lp, "%s.log", out);
  KMODE = !getenv("SCORE") ? 0 : !strcmp(getenv("SCORE"), "K") ? 1 : !strcmp(getenv("SCORE"), "KD") ? 2 : !strcmp(getenv("SCORE"), "KR") ? 3 : 0;
  UPCLASS = getenv("CLASS") && !strcmp(getenv("CLASS"), "UP");
  long it = 0; long tc, tb; FILE *f = fopen(sp, "r");
  if (f) { if (fscanf(f, "%ld %llu %ld %ld", &it, &grs, &tc, &tb) != 4 || !gread(&cur, f) || !gread(&best, f)) { fprintf(stderr, "bad state\n"); return 2; } fclose(f); }
  else { f = fopen(argv[1], "r"); if (!f || !gread(&cur, f)) { fprintf(stderr, "bad seed\n"); return 2; } fclose(f);
         if (!gvalid(&cur)) { fprintf(stderr, "seed invalid (structure or Ξ-cyclic)\n"); return 2; }
         if (KMODE) for (int x = 0; x < cur.N; x++) if (cur.first[x + 1] - cur.first[x] != 2) { fprintf(stderr, "K modes need every mover of degree 2 (mover %d has %d)\n", x, cur.first[x + 1] - cur.first[x]); return 2; }
         grs = SEED * 2654435761ULL + 12345; if (!grs) grs = 1; { long T0 = run1p(&cur, CAPT, SW); tc = tb = score(&cur, T0); } best = cur;
         FILE *L = fopen(lp, "a"); fprintf(L, "START seed %s N %d M %d N+M %d d %d score %ld (k %ld T %ld) SCORE %s CAP %d ITERS %ld SEED %llu TEMP0 %g UNIT %ld\n", argv[1], cur.N, cur.M, cur.N + cur.M, depth(&cur), tc, KMODE ? tc >> 40 : -1L, KMODE ? KT(tc) : tc, KMODE == 3 ? "KR" : KMODE == 2 ? "KD" : KMODE ? "K" : "T", CAP, ITERS, SEED, TEMP0, UNIT); fclose(L); }
  time_t t0 = time(0), tsave = t0; long errs = 0, acc = 0;
  for (; it < ITERS; it++) {
    if (it % UNIT == 0 && it) { cur = best; tc = tb; }
    double temp = TEMP0 * (1.0 - (double)(it % UNIT) / UNIT);
    prop = cur; int nm = 1 + gr(3), done = 0; for (int k = 0; k < nm; k++) if ((UPCLASS ? upmutate(&prop) : gmutate(&prop, CAP, !KMODE)) >= 0) done++;
    if (!done) continue;
    long tp = run1p(&prop, CAPT, SW); if (tp < 0) { errs++; continue; } tp = score(&prop, tp);
    int better = tp > tc || (tp == tc && prop.N + prop.M <= cur.N + cur.M);
    if (better || (temp > 0 && (double)(grnd() % 1000000) / 1e6 < exp(-(double)(KMODE ? ((tc >> 40) != (tp >> 40) ? 1000000 : (KMODE == 3 ? (KF(tc) - KF(tp)) / 32768.0 : (KF(tc) - KF(tp)) * 4.0) + (KT(tc) - KT(tp)) / 8.0) : (tc - tp)) / temp))) { cur = prop; tc = tp; acc++;
      if (tc > tb || (tc == tb && cur.N + cur.M < best.N + best.M)) { int newT = KMODE ? ((tc >> 40) > (tb >> 40) || ((tb >> 40) == 0 && tc > tb)) : tc > tb; best = cur; tb = tc;
        if (newT) { char bp[4096]; long bk = KMODE ? tb >> 40 : -1, bT = KMODE ? KT(tb) : tb;
          snprintf(bp, sizeof bp, "%s_BEST_k%ld_T%ld_d%d_N%d_NM%d_%016llx.txt", out, bk, bT, depth(&best), best.N, best.N + best.M, fnv(&best));
          FILE *B = fopen(bp, "w"); gwrite(&best, B); fclose(B);
          FILE *L = fopen(lp, "a"); fprintf(L, "BEST k %ld kfront %ld khalf %ld maxsw %ld T %ld d %d N %d M %d N+M %d file %s iter %ld acc %ld errs %ld sec %ld\n", bk, KMODE ? KF(tb) : -1L, (kdepth(&best, SW), khalf), maxsw, bT, depth(&best), best.N, best.M, best.N + best.M, bp, it, acc, errs, (long)(time(0) - t0)); fclose(L); } } }
    if (time(0) - tsave >= 30 || it + 1 == ITERS) { char tp2[4200]; snprintf(tp2, sizeof tp2, "%s.tmp", sp); FILE *S = fopen(tp2, "w");
      fprintf(S, "%ld %llu %ld %ld\n", it + 1, grs, tc, tb); gwrite(&cur, S); gwrite(&best, S); fclose(S); rename(tp2, sp); tsave = time(0); } }
  FILE *L = fopen(lp, "a"); fprintf(L, "DONE iters %ld best score %ld (k %ld T %ld) d %d N %d M %d N+M %d errs %ld\n", ITERS, tb, KMODE ? tb >> 40 : -1L, KMODE ? KT(tb) : tb, depth(&best), best.N, best.M, best.N + best.M, errs); fclose(L);
  return 0; }
