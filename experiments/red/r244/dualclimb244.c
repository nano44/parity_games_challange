/* L-RED 70 R244: climb on NON-homogeneous self-dual ladders (see dual244.c): per level l a template (xi 4 bits, gate perm, beta rank perm,
   beta signs 4 bits, starts 2 bits); Xi-targets one level UP (XUP=1) or, with XUP=2, one or two levels up (xi then has 8 bits: 2 per option:
   0,1 = the pair one level up, 2,3 = the pair two levels up); beta rank groups by level, top level highest.
   Score = (sum over levels of min(best switches at the level, hillcap(l)), T), hillcap(l) = min(2^(l+1), 2^(d-l)) - 1 (box 217 A2 for this shape).
   Usage: dualclimb244 d SEED EVALS RESTARTS [XUP]   prints the best genome as one line (fields per level). */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef __int128 i128;
#define MAXN 32
#define MAXD 16
static int N, d, XUP = 1;
static int wt[MAXN][2], xt[MAXN][2], gate[MAXN][2], start[MAXN];
static i128 om[MAXN][2];
static int sw[MAXN];
static long run(long cap) {
  int s[MAXN], ns[MAXN]; i128 V[MAXN + 1]; int key[MAXN][MAXD]; long T = 0;
  for (int x = 0; x < N; x++) { s[x] = start[x]; sw[x] = 0; }
  V[N] = 0;
  while (T < cap) {
    for (int x = N - 1; x >= 0; x--) { int t = xt[x][s[x]]; V[x] = om[x][s[x]] + V[t < 0 ? N : t]; }
    int ch = 0;
    for (int x = 0; x < N; x++) {
      int l = x / 2, best = -1; int bk[MAXD];
      for (int c = 0; c < 2; c++) {
        int t = xt[x][c];
        if (c != s[x] && !(om[x][c] + V[t < 0 ? N : t] > V[x])) continue;
        int kk[MAXD];
        if (l > 0) memcpy(kk, key[wt[x][c]], sizeof(int) * l);
        kk[l] = gate[x][c];
        int less = 0;
        if (best < 0) less = 1; else { for (int i = 0; i <= l; i++) { if (kk[i] != bk[i]) { less = kk[i] < bk[i]; break; } } }
        if (less) { best = c; memcpy(bk, kk, sizeof(int) * (l + 1)); }
      }
      memcpy(key[x], bk, sizeof(int) * (l + 1)); ns[x] = best;
      if (best != s[x]) { sw[x]++; ch = 1; }
    }
    if (!ch) break;
    memcpy(s, ns, sizeof(int) * N); T++;
  }
  return T;
}
static int perms[24][4];
static void mkperms(void) { int n = 0; for (int a = 0; a < 4; a++) for (int b = 0; b < 4; b++) for (int c = 0; c < 4; c++) for (int e = 0; e < 4; e++)
  if (a != b && a != c && a != e && b != c && b != e && c != e) { perms[n][0] = a; perms[n][1] = b; perms[n][2] = c; perms[n][3] = e; n++; } }
typedef struct { int xi[MAXD], gp[MAXD], rp[MAXD], sg[MAXD], st[MAXD]; } gen;
static void build(const gen *g) {
  for (int x = 0; x < N; x++) { int l = x / 2, m = x % 2;
    for (int c = 0; c < 2; c++) {
      wt[x][c] = l == 0 ? -1 : 2 * (l - 1) + c;
      int q = (g->xi[l] >> (2 * (2 * m + c))) & 3; int up = 1 + (q >> 1), tl = l + up;
      xt[x][c] = tl > d - 1 ? -1 : 2 * tl + (q & 1);
      gate[x][c] = 4 * l + perms[g->gp[l]][2 * m + c];
      int br = 4 * l + perms[g->rp[l]][2 * m + c]; int bp = (g->sg[l] >> (2 * m + c)) & 1;
      om[x][c] = ((i128)1 << (2 * br + bp)) * (bp == 0 ? 1 : -1);
    }
    start[x] = (g->st[l] >> m) & 1; }
}
static long hillcap(int l) { int a = l + 1, b = d - l; int e = a < b ? a : b; return (1L << e) - 1; }
static void eval(const gen *g, long *score, long *T, int *best) {
  build(g); *T = run(200000); long sc = 0;
  for (int l = 0; l < d; l++) { int b = sw[2 * l] > sw[2 * l + 1] ? sw[2 * l] : sw[2 * l + 1]; best[l] = b; long c = hillcap(l); sc += b < c ? b : c; }
  *score = sc;
}
static unsigned long long rs;
static unsigned rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return (unsigned)(rs >> 11); }
static void randlevel(gen *g, int l) { g->xi[l] = XUP == 2 ? rnd() % 256 : (rnd() % 16 & 1) | ((rnd() & 1) << 2) | ((rnd() & 1) << 4) | ((rnd() & 1) << 6); g->gp[l] = rnd() % 24; g->rp[l] = rnd() % 24; g->sg[l] = rnd() % 16; g->st[l] = rnd() % 4; }
static void mutate(gen *g) {
  int n = 1 + rnd() % 2;
  while (n--) { int l = rnd() % d;
    switch (rnd() % 6) {
      case 0: { int sh = 2 * (rnd() % 4); int q = XUP == 2 ? rnd() % 4 : rnd() % 2; g->xi[l] = (g->xi[l] & ~(3 << sh)) | (q << sh); break; }
      case 1: g->gp[l] = rnd() % 24; break;
      case 2: g->rp[l] = rnd() % 24; break;
      case 3: g->sg[l] ^= 1 << (rnd() % 4); break;
      case 4: g->st[l] ^= 1 << (rnd() % 2); break;
      default: randlevel(g, l);
    } }
}
int main(int argc, char **argv) {
  d = atoi(argv[1]); rs = 88172645463325252ULL ^ (unsigned long long)atol(argv[2]) * 0x9E3779B97F4A7C15ULL; long EV = atol(argv[3]); int RS = atoi(argv[4]);
  if (argc > 5) XUP = atoi(argv[5]);
  N = 2 * d; mkperms(); long full = 0; for (int l = 0; l < d; l++) full += hillcap(l);
  gen gb; long gbs = -1, gbT = 0; int gbest[MAXD];
  for (int r = 0; r < RS; r++) {
    gen g; for (int l = 0; l < d; l++) randlevel(&g, l);
    long sc, T; int best[MAXD]; eval(&g, &sc, &T, best);
    for (long e = 0; e < EV; e++) {
      gen h = g; mutate(&h); long s2, T2; int b2[MAXD]; eval(&h, &s2, &T2, b2);
      if (s2 > sc || (s2 == sc && T2 >= T)) { g = h; sc = s2; T = T2; memcpy(best, b2, sizeof(best)); }
    }
    if (sc > gbs || (sc == gbs && T > gbT)) { gb = g; gbs = sc; gbT = T; memcpy(gbest, best, sizeof(best)); }
    printf("restart %d: score %ld / %ld T %ld | global best %ld T %ld\n", r, sc, full, T, gbs, gbT); fflush(stdout);
  }
  printf("DUALCLIMB244 d %d XUP %d best score %ld / %ld T %ld per-level best:", d, XUP, gbs, full, gbT);
  for (int l = 0; l < d; l++) printf(" %d", gbest[l]); printf("\nGENOME d %d XUP %d :", d, XUP);
  for (int l = 0; l < d; l++) printf(" %d,%d,%d,%d,%d", gb.xi[l], gb.gp[l], gb.rp[l], gb.sg[l], gb.st[l]); printf("\n");
  return 0;
}
