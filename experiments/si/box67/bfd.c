/* L-SI box 67: bff.c of box 66 + TAU hook: per genome (transition table x gate order) T0G = max flip-free run above level 0 (any start)
   and T1G = max run with <= 1 flip; prints D[tau] = max T1G over genomes with T0G = tau, the count of genomes per tau and of those with
   T1G = 2 tau (DOUBLE), one witness per tau.
   Based on: L-SI box 66: bfg.c of box 65 + FRONTIER hook (every start (u, c), every flip time t on the flip-free b-run, pre = t,
   post = flip-free run with the other bit from s_t, max over level-0 configurations of that bit; records every attained (pre, post),
   whether the flip is at the stuck end of the b-run (STUCK) or mid-run, and one witness per pair).
   Based on: L-SI box 65: COPY of claude/l-comp 557b045b experiments/comp/box27/bfk.c (L-COMP successor 9) with one addition marked GAIN:
   the exact one-flip gain g*(m) = max over genomes, upper states u and bits b of (best run from (u, b) with <= 1 flip) - M(u),
   M(u) = max over b of the flip-free run from u (box 65 Lemma GAIN-IND). Original header follows.
   L-COMP box 27 (b): exhaustive T_k(m), m = 1, 2, k = 0..KMAX (L-NEW box 160 FREE0 + ISO model), my own code from R104's text.
   Ladder of m+1 levels in the R197 wiring (option k of a level-l >= 1 mover has W-target mover 2(l-1)+k). Level 0 (movers 0, 1) is
   EXTERNAL: at every step an outside agent sets both level-0 options freely; b_0 := [key(mover 0) < key(mover 1)] may change at most
   k times over s_0 .. s_T. ISO: every Xi-target is an upper mover or the exit. Every step must move a mover of level >= 1; T counts
   steps. Upper movers follow R104's rule: A-sets read at s_(t-1) (literal beta-set comparison), keys under the NEW state s_t
   (lexicographic, lowest level first, literal gate tuples).
   Enumerated: every acyclic ISO Xi-graph, every rank order, every parity vector, every relative gate order inside every level
   (incl. level 0 and the top level), every start s_0 (all levels), every level-0 schedule (by longest-path DP).
   Usage: bfk m PART NPARTS */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned long long u64;
#ifndef KMAX
#define KMAX 12
#endif
static int unb = 0;
static int m, U, NO, NS; /* U upper movers, NO options, NS = 2^(2+U) full states */
static int xt[8];        /* Xi-target of upper option o (o = 2*(x-2)+k): upper mover index (2..) or -1 */
static int nF; static unsigned char (*F)[16][4]; static unsigned char (*Fb)[4]; static int (*Fg)[12];
static int perms[24][4];
static u64 *H; static u64 HM; static u64 hcount = 0; static int z0 = 0, z1 = 0;
static int hins(u64 v) {
  if (v == 0) { if (z0) return 0; z0 = 1; return 1; }
  if (v == ~0ULL) { if (z1) return 0; z1 = 1; return 1; }
  u64 h = (v * 0x9E3779B97F4A7C15ULL) >> 20;
  for (u64 i = h & HM;; i = (i + 1) & HM) { if (H[i] == v) return 0; if (!H[i]) { H[i] = v; hcount++; return 1; } } }
static int lev(int x) { return x / 2; }
static int W(int x, int k) { return 2 * (lev(x) - 1) + k; }
static void buildF(void) {
  int np = 0;
  for (int a = 0; a < 4; a++) for (int b = 0; b < 4; b++) for (int c = 0; c < 4; c++) for (int d = 0; d < 4; d++) {
    if (a==b||a==c||a==d||b==c||b==d||c==d) continue; perms[np][0]=a; perms[np][1]=b; perms[np][2]=c; perms[np][3]=d; np++; }
  int nlev = m + 1; long ng = 1; for (int l = 0; l < nlev; l++) ng *= 24;
  F = malloc(sizeof(*F) * NS * ng); Fb = malloc(sizeof(*Fb) * ng); Fg = malloc(sizeof(*Fg) * ng);
  unsigned char (*T)[16][4] = malloc(sizeof(*T) * NS);
  for (long gi = 0; gi < ng; gi++) {
    int g[12]; long r = gi; for (int l = 0; l < nlev; l++) { int p = r % 24; r /= 24; for (int j = 0; j < 4; j++) g[4*l+j] = 16*l + perms[p][j]; }
    unsigned char bb[4];
    for (int c = 0; c < 4; c++) bb[c] = g[0 + (c & 1)] < g[2 + ((c >> 1) & 1)];
    for (int s = 0; s < NS; s++) for (int a = 0; a < (1 << U); a++) for (int c = 0; c < 4; c++) {
      long key[8]; int ns = c; key[0] = g[0 + (c & 1)]; key[1] = g[2 + ((c >> 1) & 1)];
      for (int x = 2; x < 2 + U; x++) { int sx = (s >> x) & 1; long best = -1; int bk = 0;
        for (int k = 0; k < 2; k++) { if (k != sx && !((a >> (x-2)) & 1)) continue;
          long kk = key[W(x,k)] * 64 + g[2*x+k]; if (best < 0 || kk < best) { best = kk; bk = k; } }
        key[x] = best; ns |= bk << x; }
      T[s][a][c] = ns; }
    int dup = 0;
    for (int f = 0; f < nF && !dup; f++) if (!memcmp(F + (long)f * NS, T, sizeof(*T) * NS) && !memcmp(Fb[f], bb, 4)) dup = 1;
    if (!dup) { memcpy(F + (long)nF * NS, T, sizeof(*T) * NS); memcpy(Fb[nF], bb, 4); for (int j = 0; j < 4*nlev; j++) Fg[nF][j] = g[j]; nF++; } }
  free(T);
}
static u64 tab; static int fcur; static int memo[64][KMAX+1], onst[64][KMAX+1], cyc = 0;
static int bof(int s) { return Fb[fcur][s & 3]; }
static int L(int s, int r) {
  if (memo[s][r] >= 0) return memo[s][r];
  if (onst[s][r]) { cyc = 1; return 0; }
  onst[s][r] = 1; int best = 0, su = s >> 2, a = 0;
  for (int i = 0; i < U; i++) a |= (int)(((tab >> (su * U + i)) & 1) ^ ((su >> i) & 1)) << i;
  if (a) for (int c = 0; c < 4; c++) { int ns = F[(long)fcur * NS + s][a][c]; if ((ns >> 2) == su) continue;
    int fl = unb ? 0 : (Fb[fcur][c] != bof(s)); if (fl && r == 0) continue; int v = 1 + L(ns, r - fl); if (v > best) best = v; }
  onst[s][r] = 0; memo[s][r] = best; return best; }
int main(int argc, char **argv) {
  unb = getenv("UNB") != NULL; m = atoi(argv[1]); int part = atoi(argv[2]), nparts = atoi(argv[3]);
  U = 2 * m; NO = 2 * U; NS = 1 << (2 + U);
  HM = (1ULL << 26) - 1; H = calloc(HM + 1, 8);
  buildF(); fprintf(stderr, "m %d: distinct (transition, b_0) functions over all in-level gate orders: %d\n", m, nF);
  int fact = 1; for (int i = 2; i <= NO; i++) fact *= i;
  int (*rp)[8] = malloc(sizeof(*rp) * fact); int np = 0; { int a[8]; for (int i = 0; i < NO; i++) a[i] = i;
    for (;;) { memcpy(rp[np++], a, sizeof a); int i = NO - 2; while (i >= 0 && a[i] > a[i+1]) i--; if (i < 0) break;
      int j = NO - 1; while (a[j] < a[i]) j--; int t = a[i]; a[i] = a[j]; a[j] = t; for (int l = i+1, r = NO-1; l < r; l++, r--) { t = a[l]; a[l] = a[r]; a[r] = t; } } }
  int gbest = -99; char gwit[600] = ""; /* GAIN */
  static int Dt[40], Dn[40], Ddbl[40]; static char Dw[40][300]; for (int i = 0; i < 40; i++) Dt[i] = -1; /* TAU */
  static int seenP[40][40][2]; static char pw[40][40][2][300]; /* FRONTIER */
  int best[KMAX+1]; char wit[KMAX+1][600]; for (int k = 0; k <= KMAX; k++) { best[k] = -1; wit[k][0] = 0; }
  long gidx = -1, ngraph = 0; u64 ntab = 0; long ncomb = 1; for (int o = 0; o < NO; o++) ncomb *= (U + 1);
  int nst = 1 << U; /* upper states */
  for (long cidx = 0; cidx < ncomb; cidx++) {
    long cc = cidx; int bad = 0;
    for (int o = 0; o < NO; o++) { int v = (int)(cc % (U + 1)); cc /= (U + 1); xt[o] = v == U ? -1 : 2 + v; if (xt[o] == 2 + o / 2) bad = 1; }
    if (bad) continue;
    int r[8][8] = {{0}}; for (int o = 0; o < NO; o++) if (xt[o] >= 0) r[o/2][xt[o]-2] = 1;
    for (int k = 0; k < U; k++) for (int i = 0; i < U; i++) for (int j = 0; j < U; j++) if (r[i][k] && r[k][j]) r[i][j] = 1;
    for (int i = 0; i < U; i++) if (r[i][i]) bad = 1; if (bad) continue;
    gidx++; if (gidx % nparts != part) continue; ngraph++;
    int C[16][8];
    for (int s = 0; s < nst; s++) for (int o = 0; o < NO; o++) { int msk = 1 << o, t = xt[o];
      while (t >= 0) { int oo = 2*(t-2) + ((s >> (t-2)) & 1); msk |= 1 << oo; t = xt[oo]; } C[s][o] = msk; }
    int D[64], C1[64]; int nI = nst * U;
    for (int s = 0; s < nst; s++) for (int i = 0; i < U; i++) { D[s*U+i] = C[s][2*i] ^ C[s][2*i+1]; C1[s*U+i] = C[s][2*i+1]; }
    static unsigned char seen[1 << 16][64]; static int seenv[1 << 16]; static int stamp = 0; stamp++;
    for (int pi = 0; pi < np; pi++) { int *rk = rp[pi]; int ord[8]; for (int o = 0; o < NO; o++) ord[NO-1-rk[o]] = o;
      unsigned char top[64]; memset(top, 0, 64); unsigned long long sig = 1469598103934665603ULL;
      for (int i = 0; i < nI; i++) { int t = -1; for (int q = 0; q < NO; q++) if (D[i] >> ord[q] & 1) { t = ord[q]; break; } top[i] = t; sig = (sig ^ (t + 1)) * 1099511628211ULL; }
      int dup = 0; for (unsigned j = sig & 0xFFFF;; j = (j + 1) & 0xFFFF) { if (seenv[j] != stamp) { seenv[j] = stamp; memcpy(seen[j], top, 64); break; } if (!memcmp(seen[j], top, 64)) { dup = 1; break; } }
      if (dup) continue;
      u64 base = 0, Mo[8] = {0};
      for (int i = 0; i < nI; i++) { if (C1[i] >> top[i] & 1) base |= 1ULL << i; Mo[top[i]] |= 1ULL << i; }
      for (int pv = 0; pv < (1 << NO); pv++) { u64 tb = base; for (int o = 0; o < NO; o++) if (pv >> o & 1) tb ^= Mo[o];
        if (!hins(tb)) continue; ntab++; tab = tb;
        for (int f = 0; f < nF; f++) { fcur = f; memset(memo, -1, sizeof memo); memset(onst, 0, sizeof onst);
          for (int k = 0; k <= KMAX; k++) for (int s0 = 0; s0 < NS; s0++) { int v = L(s0, k);
            if (cyc) { printf("CYCLE found (unbounded run)\n"); return 3; }
            if (v > best[k]) { best[k] = v; int n = sprintf(wit[k], "T %d k %d xt", v, k);
              for (int o = 0; o < NO; o++) n += sprintf(wit[k]+n, " %d", xt[o]);
              n += sprintf(wit[k]+n, " rank"); for (int o = 0; o < NO; o++) n += sprintf(wit[k]+n, " %d", rk[o]);
              n += sprintf(wit[k]+n, " par"); for (int o = 0; o < NO; o++) n += sprintf(wit[k]+n, " %d", pv >> o & 1);
              n += sprintf(wit[k]+n, " gate"); for (int j = 0; j < 4*(m+1); j++) n += sprintf(wit[k]+n, " %d", Fg[f][j]);
              sprintf(wit[k]+n, " start %d", s0); } }
          /* TAU */
          { int T0G = 0, T1G = 0; for (int s0 = 0; s0 < NS; s0++) { if (memo[s0][0] > T0G) T0G = memo[s0][0]; if (memo[s0][1] > T1G) T1G = memo[s0][1]; }
            Dn[T0G]++; if (T1G == 2 * T0G) Ddbl[T0G]++;
            if (T1G > Dt[T0G]) { Dt[T0G] = T1G; int n = sprintf(Dw[T0G], "xt"); for (int o = 0; o < NO; o++) n += sprintf(Dw[T0G]+n, " %d", xt[o]);
              n += sprintf(Dw[T0G]+n, " rank"); for (int o = 0; o < NO; o++) n += sprintf(Dw[T0G]+n, " %d", rk[o]);
              n += sprintf(Dw[T0G]+n, " par"); for (int o = 0; o < NO; o++) n += sprintf(Dw[T0G]+n, " %d", pv >> o & 1);
              n += sprintf(Dw[T0G]+n, " gate"); for (int j = 0; j < 4*(m+1); j++) n += sprintf(Dw[T0G]+n, " %d", Fg[f][j]); } }
          /* FRONTIER */
          for (int s0 = 0; s0 < NS; s0++) { int b = Fb[fcur][s0 & 3]; int s = s0, t = 0;
            for (;;) { int su = s >> 2, post = -1;
              for (int c = 0; c < 4; c++) if (Fb[fcur][c] != b) { int v = memo[(su << 2) | c][0]; if (v > post) post = v; }
              /* next state of the b-run (deterministic above level 0: any c with bit b) */
              int a = 0; for (int i = 0; i < U; i++) a |= (int)(((tab >> (su * U + i)) & 1) ^ ((su >> i) & 1)) << i;
              int nx = -1; if (a) for (int c = 0; c < 4; c++) if (Fb[fcur][c] == b) { int ns = F[(long)fcur * NS + s][a][c]; if ((ns >> 2) != su) { nx = ns; break; } }
              int stuck = nx < 0;
              if (post < 0) break; /* b_0 constant over all level-0 configurations of this gate order: no flip possible */
              if (!seenP[t][post][stuck]) { seenP[t][post][stuck] = 1;
                int n = sprintf(pw[t][post][stuck], "xt"); for (int o = 0; o < NO; o++) n += sprintf(pw[t][post][stuck]+n, " %d", xt[o]);
                n += sprintf(pw[t][post][stuck]+n, " rank"); for (int o = 0; o < NO; o++) n += sprintf(pw[t][post][stuck]+n, " %d", rk[o]);
                n += sprintf(pw[t][post][stuck]+n, " par"); for (int o = 0; o < NO; o++) n += sprintf(pw[t][post][stuck]+n, " %d", pv >> o & 1);
                n += sprintf(pw[t][post][stuck]+n, " gate"); for (int j = 0; j < 4*(m+1); j++) n += sprintf(pw[t][post][stuck]+n, " %d", Fg[f][j]);
                sprintf(pw[t][post][stuck]+n, " start %d", s0); }
              if (stuck) break; s = nx; t++; } }
          /* GAIN: per upper state u: M(u) = max_c L((u,c),0); V1 = max_c L((u,c),1) (KMAX >= 1) */
          for (int su = 0; su < (1 << U); su++) { int Mu = -1, V1 = -1;
            for (int c = 0; c < 4; c++) { int s0 = (su << 2) | c; if (memo[s0][0] > Mu) Mu = memo[s0][0]; if (memo[s0][1] > V1) V1 = memo[s0][1]; }
            if (V1 - Mu > gbest) { gbest = V1 - Mu; int n = sprintf(gwit, "g %d V1 %d M %d xt", gbest, V1, Mu);
              for (int o = 0; o < NO; o++) n += sprintf(gwit+n, " %d", xt[o]);
              n += sprintf(gwit+n, " rank"); for (int o = 0; o < NO; o++) n += sprintf(gwit+n, " %d", rk[o]);
              n += sprintf(gwit+n, " par"); for (int o = 0; o < NO; o++) n += sprintf(gwit+n, " %d", pv >> o & 1);
              n += sprintf(gwit+n, " gate"); for (int j = 0; j < 4*(m+1); j++) n += sprintf(gwit+n, " %d", Fg[f][j]);
              sprintf(gwit+n, " upper %d", su); } } } } }
  }
  printf("m %d part %d/%d graphs %ld distinct_tables %llu\n", m, part, nparts, ngraph, ntab);
  for (int k = 0; k <= KMAX; k++) printf("T_%d(%d) %d\n", k, m, best[k]);
  for (int k = 0; k <= KMAX; k++) printf("witness %s\n", wit[k]);
  for (int a = 0; a < 40; a++) for (int c = 0; c < 40; c++) for (int k = 0; k < 2; k++) if (seenP[a][c][k])
    printf("PAIR pre %d post %d %s witness %s\n", a, c, k ? "STUCK" : "MID", pw[a][c][k]);
  for (int i = 0; i < 40; i++) if (Dn[i]) printf("TAU T0G %d genomes %d max_T1G %d double %d witness %s\n", i, Dn[i], Dt[i], Ddbl[i], Dw[i]);
  printf("GAIN g*(%d) part %d/%d = %d\nGAIN witness %s\n", m, part, nparts, gbest, gwit);
  return 0; }
