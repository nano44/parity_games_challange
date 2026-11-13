// scratch: anneal the key-run length T on 2-per-level ladders with bi-ladder (jump 1) or upward (jump<=J) Xi-wiring and FREE beta ranks.
// usage: ann d J seed iters [target]   -> prints best T and the genome as L-NEW JSON (replay with one217.OneP)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define MAXD 16
typedef unsigned long long u64;
int d, N, Q, J;
typedef struct { int xt[2*MAXD][2]; int rank[4*MAXD]; int pos[4*MAXD]; int eps0[4]; int sW[MAXD][2]; int c0[2*MAXD]; } G;
static u64 rng = 88172645463325252ULL;
static inline u64 rnd(void){ rng ^= rng << 13; rng ^= rng >> 7; rng ^= rng << 17; return rng; }
static int run(const G *g, int cap, int *swout){
  int c[2*MAXD], n[2*MAXD], om[MAXD]; u64 val[2*MAXD+1], posmask = 0; int T = 0, x, o, l;
  for (x = 0; x < Q; x++) if (g->pos[x]) posmask |= 1ULL << g->rank[x];
  memcpy(c, g->c0, sizeof(int)*N); if (swout) memset(swout, 0, sizeof(int)*N);
  val[N] = 0;
  while (T < cap){
    int ch = 0;
    for (x = N-1; x >= 0; x--) val[x] = (1ULL << g->rank[2*x + c[x]]) | val[g->xt[x][c[x]]];
    for (l = 0; l < d; l++){
      for (o = 0; o < 2; o++){
        x = 2*l + o; int cur = c[x], oth = 1 - cur, kc, vc;
        if (l == 0) kc = g->eps0[2*o + oth] < g->eps0[2*o + cur]; else kc = (oth == om[l-1]);
        n[x] = cur;
        if (!kc) continue;
        u64 A = (1ULL << g->rank[2*x + oth]) | val[g->xt[x][oth]], B = (1ULL << g->rank[2*x + cur]) | val[g->xt[x][cur]], D = A ^ B;
        if (!D) continue;
        u64 top = 1ULL << (63 - __builtin_clzll(D));
        vc = ((A & top) != 0) == ((posmask & top) != 0);
        if (vc){ n[x] = oth; ch = 1; if (swout) swout[x]++; }
      }
      int a = n[2*l], b = n[2*l+1];
      if (l == 0) om[0] = (g->eps0[2 + b] < g->eps0[a]); else om[l] = (a == b) ? g->sW[l][a] : (b == om[l-1]);
    }
    if (!ch) break;
    memcpy(c, n, sizeof(int)*N); T++;
  }
  return T;
}
static void rndtarget(G *g, int x, int o){
  int l = x/2; if (l == d-1){ g->xt[x][o] = N; return; }
  int jmp = 1 + (int)(rnd() % (u64)J); int L = l + jmp; if (L > d-1) { g->xt[x][o] = (J > 1 && (rnd() & 3) == 0) ? N : 2*(d-1) + (int)(rnd() & 1); return; }
  g->xt[x][o] = 2*L + (int)(rnd() & 1);
}
static void init(G *g){ int i; for (i = 0; i < Q; i++){ g->rank[i] = i; g->pos[i] = rnd() & 1; }
  for (i = Q-1; i > 0; i--){ int j = rnd() % (u64)(i+1), t = g->rank[i]; g->rank[i] = g->rank[j]; g->rank[j] = t; }
  for (i = 0; i < 4; i++) g->eps0[i] = i; for (i = 3; i > 0; i--){ int j = rnd() % (u64)(i+1), t = g->eps0[i]; g->eps0[i] = g->eps0[j]; g->eps0[j] = t; }
  for (i = 0; i < d; i++){ g->sW[i][0] = rnd() & 1; g->sW[i][1] = rnd() & 1; }
  for (i = 0; i < N; i++){ g->c0[i] = rnd() & 1; rndtarget(g, i, 0); rndtarget(g, i, 1); } }
static void mutate(G *g){ int k = rnd() % 10, i, j, t;
  if (k < 4){ i = rnd() % (u64)Q; j = rnd() % (u64)Q; t = g->rank[i]; g->rank[i] = g->rank[j]; g->rank[j] = t; }
  else if (k < 6){ g->pos[rnd() % (u64)Q] ^= 1; }
  else if (k == 6){ i = rnd() % (u64)N; rndtarget(g, i, rnd() & 1); }
  else if (k == 7){ g->sW[1 + rnd() % (u64)(d-1)][rnd() & 1] ^= 1; }
  else if (k == 8){ i = rnd() & 3; j = rnd() & 3; t = g->eps0[i]; g->eps0[i] = g->eps0[j]; g->eps0[j] = t; }
  else { g->c0[rnd() % (u64)N] ^= 1; } }
static void dump(const G *g, int T){ int x, o, l; int sw[2*MAXD]; run(g, 1000000, sw);
  printf("{\"N\":%d,\"lev\":[", N); for (x = 0; x < N; x++) printf("%d%s", x/2, x < N-1 ? "," : "");
  printf("],\"deg\":2,\"opts\":["); for (x = 0; x < N; x++){ printf("["); for (o = 0; o < 2; o++) printf("[%d,%d,%d]%s", x >= 2 ? 2*(x/2-1)+o : -1, g->xt[x][o] == N ? -1 : g->xt[x][o], 2*x+o, o ? "" : ","); printf("]%s", x < N-1 ? "," : ""); }
  printf("],\"gate\":[[%d,%d],[%d,%d]", g->eps0[0], g->eps0[1], g->eps0[2], g->eps0[3]);
  for (l = 1; l < d; l++){ int ga[2], gb[2]; for (o = 0; o < 2; o++){ if (g->sW[l][o]){ ga[o] = 1000*l+2*o+1; gb[o] = 1000*l+2*o; } else { ga[o] = 1000*l+2*o; gb[o] = 1000*l+2*o+1; } } printf(",[%d,%d],[%d,%d]", ga[0], ga[1], gb[0], gb[1]); }
  printf("],\"br\":["); for (x = 0; x < Q; x++) printf("%d%s", g->rank[x], x < Q-1 ? "," : "");
  printf("],\"bp\":["); for (x = 0; x < Q; x++) printf("%d%s", g->pos[x] ? 0 : 1, x < Q-1 ? "," : "");
  printf("],\"start\":["); for (x = 0; x < N; x++) printf("%d%s", g->c0[x], x < N-1 ? "," : "");
  printf("],\"T\":%d,\"sw\":[", T); for (x = 0; x < N; x++) printf("%d%s", sw[x], x < N-1 ? "," : ""); printf("]}\n"); }
int main(int argc, char **argv){ d = atoi(argv[1]); J = atoi(argv[2]); rng ^= (u64)atoll(argv[3]) * 0x9E3779B97F4A7C15ULL; long iters = atol(argv[4]); int target = argc > 5 ? atoi(argv[5]) : 1 << 30;
  N = 2*d; Q = 4*d; G g, h, best; init(&g); int T = run(&g, 100000, 0), bT = T; best = g; long it; double temp = 1.5;
  for (it = 0; it < iters && bT < target; it++){ h = g; mutate(&h); if (rnd() % 3 == 0) mutate(&h); int T2 = run(&h, 100000, 0);
    if (T2 >= T || exp((T2 - T) / temp) * 18446744073709551615.0 > (double)rnd()){ g = h; T = T2; if (T > bT){ bT = T; best = g; } }
    if (it % 200000 == 199999){ temp *= 0.9; if (temp < 0.3){ temp = 1.5; g = best; T = bT; } } }
  fprintf(stderr, "d %d J %d seed %s iters %ld best T %d\n", d, J, argv[3], it, bT); dump(&best, bT); return 0; }
