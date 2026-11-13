/* L-RED 70 R244: fast climb for the enumeration depth k on general 2-per-level ladders (own engine, C; model 1P(G), box 217 section 1 / 6.1).
   Movers 2l, 2l+1 at level l; option c W-points to mover 2(l-1)+c; Xi-target of every option: any mover or the exit (Xi-acyclic, checked);
   gates: a permutation of 4 per level (only the within-level order matters for root-first keys); beta ranks: a permutation of 4d; signs; starts.
   Score (lexicographic): k = number of full levels from level 0 (best switches at level l = 2^(l+1) - 1), then best(k) (capped), then T.
   Simulated annealing with restarts; prints every improvement of k and the best genome (JSON, enum243 / sim244 format).
   Seeded mode (SEEDFILE INS): the start (and every restart) is the seed genome (text, dumpseed244.py) with d - d_seed new random levels
   inserted at level INS (old levels >= INS move up; old Xi-targets, gate orders, starts and the relative beta rank order are kept).
   Usage: lad244 d SEED EVALS OUT.json TEMP [SEEDFILE INS]     (d <= 15: values in __int128) */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef __int128 i128;
#define MAXD 15
#define MAXN 30
static int N, d, M;
typedef struct { int xt[MAXN][2], gp[MAXD], br[4 * MAXD], bp[4 * MAXD], st[MAXN]; } gen;
static int perms[24][4];
static void mkperms(void) { int n = 0; for (int a = 0; a < 4; a++) for (int b = 0; b < 4; b++) for (int c = 0; c < 4; c++) for (int e = 0; e < 4; e++)
  if (a != b && a != c && a != e && b != c && b != e && c != e) { perms[n][0] = a; perms[n][1] = b; perms[n][2] = c; perms[n][3] = e; n++; } }
static int topo[MAXN], sw[MAXN];
static int mktopo(const gen *g) {      /* Xi-targets first; 0 if cyclic */
  int col[MAXN] = {0}, n = 0, stk[MAXN], it[MAXN];
  for (int r = 0; r < N; r++) { if (col[r]) continue; int sp = 0; stk[0] = r; it[0] = 0; col[r] = 1;
    while (sp >= 0) { int v = stk[sp];
      if (it[sp] < 2) { int w = g->xt[v][it[sp]++]; if (w < 0) continue; if (col[w] == 1) return 0; if (col[w] == 0) { col[w] = 1; stk[++sp] = w; it[sp] = 0; } }
      else { col[v] = 2; topo[n++] = v; sp--; } } }
  return 1;
}
static long run(const gen *g, long cap) {
  int s[MAXN], ns[MAXN], key[MAXN][MAXD], gate[MAXN][2]; i128 V[MAXN + 1], om[MAXN][2]; long T = 0;
  for (int x = 0; x < N; x++) { s[x] = g->st[x]; sw[x] = 0; int l = x / 2, m = x % 2;
    for (int c = 0; c < 2; c++) { int b = 4 * l + 2 * m + c; gate[x][c] = perms[g->gp[l]][2 * m + c];
      om[x][c] = ((i128)1 << (2 * g->br[b] + g->bp[b])) * (g->bp[b] == 0 ? 1 : -1); } }
  V[N] = 0;
  while (T < cap) {
    for (int i = 0; i < N; i++) { int x = topo[i], t = g->xt[x][s[x]]; V[x] = om[x][s[x]] + V[t < 0 ? N : t]; }
    int ch = 0;
    for (int x = 0; x < N; x++) {
      int l = x / 2, best = -1, bk[MAXD];
      for (int c = 0; c < 2; c++) {
        int t = g->xt[x][c];
        if (c != s[x] && !(om[x][c] + V[t < 0 ? N : t] > V[x])) continue;
        int kk[MAXD]; if (l > 0) memcpy(kk, key[2 * (l - 1) + c], sizeof(int) * l); kk[l] = gate[x][c];
        int less = 0;
        if (best < 0) less = 1; else for (int i = 0; i <= l; i++) if (kk[i] != bk[i]) { less = kk[i] < bk[i]; break; }
        if (less) { best = c; memcpy(bk, kk, sizeof(int) * (l + 1)); }
      }
      memcpy(key[x], bk, sizeof(int) * (l + 1)); ns[x] = best; if (best != s[x]) { sw[x]++; ch = 1; }
    }
    if (!ch) break;
    memcpy(s, ns, sizeof(int) * N); T++;
  }
  return T;
}
static double score(const gen *g, int *kk, long *TT) {
  if (!mktopo(g)) { *kk = -1; *TT = 0; return -1; }
  long T = run(g, 50000); int k = 0; long part = 0;
  for (int l = 0; l < d; l++) { int b = sw[2 * l] > sw[2 * l + 1] ? sw[2 * l] : sw[2 * l + 1]; long c = (1L << (l + 1)) - 1;
    if (b == c && k == l) k++; else { if (l == k) part = b < c ? b : 0; break; } }
  *kk = k; *TT = T; return k * 1e6 + part * 1e3 + (T < 999 ? T : 999);
}
static unsigned long long rs;
static unsigned rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return (unsigned)(rs >> 11); }
static void randgen(gen *g) {
  for (int x = 0; x < N; x++) { for (int c = 0; c < 2; c++) g->xt[x][c] = -1; g->st[x] = rnd() & 1; }
  for (int l = 0; l < d; l++) g->gp[l] = rnd() % 24;
  for (int b = 0; b < M; b++) { g->br[b] = b; g->bp[b] = rnd() & 1; }
  for (int b = M - 1; b > 0; b--) { int j = rnd() % (b + 1), t = g->br[b]; g->br[b] = g->br[j]; g->br[j] = t; }
  for (int x = 0; x < N; x++) for (int c = 0; c < 2; c++) { int old = g->xt[x][c]; g->xt[x][c] = (rnd() % 100 < 12) ? -1 : (int)(rnd() % N); if (g->xt[x][c] == x || !mktopo(g)) g->xt[x][c] = old; }
}
static gen seedg; static int seedd = 0, INS = 0;
static void lift(gen *g) {
  int add = d - seedd; double keyr[4 * MAXD]; int idx[4 * MAXD];
  for (int l = 0; l < d; l++) { int ol = l < INS ? l : (l >= INS + add ? l - add : -1);
    for (int m = 0; m < 2; m++) { int x = 2 * l + m;
      if (ol >= 0) { int ox = 2 * ol + m; g->st[x] = seedg.st[ox];
        for (int c = 0; c < 2; c++) { int t = seedg.xt[ox][c]; if (t >= 0) { int tl = t / 2; t = 2 * (tl < INS ? tl : tl + add) + t % 2; } g->xt[x][c] = t;
          keyr[2 * x + c] = seedg.br[2 * ox + c] + 0.5; g->bp[2 * x + c] = seedg.bp[2 * ox + c]; } }
      else { g->st[x] = rnd() & 1; for (int c = 0; c < 2; c++) { g->xt[x][c] = -1; keyr[2 * x + c] = (rnd() % 1000000) / 1000000.0 * (4 * seedd); g->bp[2 * x + c] = rnd() & 1; } } }
    g->gp[l] = ol >= 0 ? seedg.gp[ol] : (int)(rnd() % 24); }
  for (int b = 0; b < M; b++) idx[b] = b;
  for (int i = 0; i < M; i++) for (int j = i + 1; j < M; j++) if (keyr[idx[j]] < keyr[idx[i]]) { int t = idx[i]; idx[i] = idx[j]; idx[j] = t; }
  for (int r = 0; r < M; r++) g->br[idx[r]] = r;
  for (int l = INS; l < INS + add; l++) for (int m = 0; m < 2; m++) for (int c = 0; c < 2; c++) { int x = 2 * l + m; g->xt[x][c] = (rnd() % 100 < 12) ? -1 : (int)(rnd() % N); if (g->xt[x][c] == x || !mktopo(g)) g->xt[x][c] = -1; }
}
static void fresh(gen *g) { if (seedd) lift(g); else randgen(g); }
static void mutate(gen *g) {
  int n = 1 + (rnd() % 100 < 30) + (rnd() % 100 < 10);
  while (n--) { int r = rnd() % 100;
    if (r < 40) { int x = rnd() % N, c = rnd() & 1; g->xt[x][c] = (rnd() % 100 < 12) ? -1 : (int)(rnd() % N); }
    else if (r < 60) { int a = rnd() % M, b = rnd() % M, t = g->br[a]; g->br[a] = g->br[b]; g->br[b] = t; }
    else if (r < 72) g->bp[rnd() % M] ^= 1;
    else if (r < 88) g->gp[rnd() % d] = rnd() % 24;
    else g->st[rnd() % N] ^= 1; }
}
static void dump(const gen *g, const char *fn, int k, long T) {
  FILE *f = fopen(fn, "w"); fprintf(f, "{\"N\": %d, \"deg\": 2, \"lev\": [", N);
  for (int x = 0; x < N; x++) fprintf(f, "%d%s", x / 2, x < N - 1 ? ", " : "], \"opts\": [");
  for (int x = 0; x < N; x++) fprintf(f, "[[%d, %d, %d], [%d, %d, %d]]%s", x < 2 ? -1 : 2 * (x / 2 - 1), g->xt[x][0], 4 * (x / 2) + 2 * (x % 2), x < 2 ? -1 : 2 * (x / 2 - 1) + 1, g->xt[x][1], 4 * (x / 2) + 2 * (x % 2) + 1, x < N - 1 ? ", " : "], \"gate\": [");
  for (int x = 0; x < N; x++) fprintf(f, "[%d, %d]%s", 4 * (x / 2) + perms[g->gp[x / 2]][2 * (x % 2)], 4 * (x / 2) + perms[g->gp[x / 2]][2 * (x % 2) + 1], x < N - 1 ? ", " : "], \"br\": [");
  for (int b = 0; b < M; b++) fprintf(f, "%d%s", g->br[b], b < M - 1 ? ", " : "], \"bp\": [");
  for (int b = 0; b < M; b++) fprintf(f, "%d%s", g->bp[b], b < M - 1 ? ", " : "], \"start\": [");
  for (int x = 0; x < N; x++) fprintf(f, "%d%s", g->st[x], x < N - 1 ? ", " : "]");
  fprintf(f, ", \"k\": %d, \"T\": %ld}\n", k, T); fclose(f);
}
int main(int argc, char **argv) {
  d = atoi(argv[1]); long seed = atol(argv[2]); long EV = atol(argv[3]); const char *out = argv[4]; double temp = argc > 5 ? atof(argv[5]) : 0.0;
  rs = 88172645463325252ULL ^ (unsigned long long)seed * 0x9E3779B97F4A7C15ULL; N = 2 * d; M = 4 * d; mkperms();
  if (argc > 7) { FILE *f = fopen(argv[6], "r"); INS = atoi(argv[7]); if (fscanf(f, "%d", &seedd) != 1) return 2;
    for (int x = 0; x < 2 * seedd; x++) { int g0, g1, pi = -1; if (fscanf(f, "%d %d %d %d %d", &seedg.st[x], &seedg.xt[x][0], &seedg.xt[x][1], &g0, &g1) != 5) return 2;
      if (x % 2 == 1) { int w[4] = {seedg.br[0], seedg.br[1], g0, g1}; for (int p = 0; p < 24; p++) if (perms[p][0] == w[0] && perms[p][1] == w[1] && perms[p][2] == w[2] && perms[p][3] == w[3]) pi = p; if (pi < 0) return 4; seedg.gp[x / 2] = pi; }
      else { seedg.br[0] = g0; seedg.br[1] = g1; } }
    for (int b = 0; b < 4 * seedd; b++) if (fscanf(f, "%d", &seedg.br[b]) != 1) return 2;
    for (int b = 0; b < 4 * seedd; b++) if (fscanf(f, "%d", &seedg.bp[b]) != 1) return 2;
    fclose(f); }
  gen g, gb; int k, kb = -1; long T, Tb = 0; double sc, sb = -2; fresh(&g); sc = score(&g, &k, &T); long since = 0;
  for (long e = 0; e < EV; e++) {
    gen h = g; mutate(&h); int k2; long T2; double s2 = score(&h, &k2, &T2);
    if (s2 >= sc || (temp > 0 && s2 >= 0 && (rnd() % 1000000) < 1e6 * exp((s2 - sc) / temp))) { if (s2 > sc) since = 0; g = h; sc = s2; k = k2; T = T2; }
    if (sc > sb) { if (k > kb) { printf("LAD244 d %d seed %ld eval %ld: k %d T %ld\n", d, seed, e, k, T); fflush(stdout); dump(&g, out, k, T); } sb = sc; gb = g; kb = k; Tb = T; }
    if (++since > 400000) { fresh(&g); sc = score(&g, &k, &T); since = 0; }      /* restart from random after a long plateau */
  }
  dump(&gb, out, kb, Tb); printf("LAD244 END d %d seed %ld evals %ld best k %d T %ld score %.0f\n", d, seed, EV, kb, Tb, sb);
  return 0;
}
