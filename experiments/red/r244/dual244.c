/* L-RED 70 R244: SELF-DUAL LADDER screen (own engine, C). Model 1P(G) (box 217 section 1 / 6.1) on 2-per-level ladders:
   movers 2l, 2l+1 at level l; option c W-points to mover 2(l-1)+c (none at level 0) and Xi-points UP to mover 2(l+1)+x[m][c]
   (exit at the top level): the Xi-order is the reverse of the W-order (W-level l has Xi-height d-1-l).
   Homogeneous template (the same at every level): x[m][c] (16), gate order gp (24), beta rank order rp (24), beta signs (16), starts (4);
   beta rank groups by level, GROUP=0: top level highest (the dual of root-first keys), GROUP=1: bottom level highest.
   For every template: T (steps of the key run), max switches, per-level best. Prints the best templates by T.
   Usage: dual244 d GROUP TOPN [CAP]      (d <= 12; values in __int128) */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef __int128 i128;
#define MAXN 32
static int N, d;
static int wt[MAXN][2], xt[MAXN][2], gate[MAXN][2], start[MAXN];
static i128 om[MAXN][2];
static int sw[MAXN];
static long run(long cap) {
  int s[MAXN], ns[MAXN]; i128 V[MAXN + 1]; int key[MAXN][16]; long T = 0;
  for (int x = 0; x < N; x++) { s[x] = start[x]; sw[x] = 0; }
  V[N] = 0;
  while (T < cap) {
    for (int x = N - 1; x >= 0; x--) { int t = xt[x][s[x]]; V[x] = om[x][s[x]] + V[t < 0 ? N : t]; }   /* Xi-targets are above: topological */
    int ch = 0;
    for (int x = 0; x < N; x++) {
      int l = x / 2, best = -1; int bk[16];
      for (int c = 0; c < 2; c++) {
        int t = xt[x][c];
        if (c != s[x] && !(om[x][c] + V[t < 0 ? N : t] > V[x])) continue;
        int kk[16];
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
typedef struct { long T; int maxsw; int xi, gp, rp, sg, st; } rec;
static int cmp(const void *a, const void *b) { const rec *p = a, *q = b; return q->T > p->T ? 1 : q->T < p->T ? -1 : q->maxsw - p->maxsw; }
int main(int argc, char **argv) {
  d = atoi(argv[1]); int GROUP = atoi(argv[2]); int TOPN = atoi(argv[3]); long cap = argc > 4 ? atol(argv[4]) : 100000;
  N = 2 * d; mkperms(); rec *R = malloc(sizeof(rec) * 16 * 24 * 24 * 16 * 4); long nr = 0; long hist[64] = {0};
  for (int xi = 0; xi < 16; xi++) for (int gp = 0; gp < 24; gp++) for (int rp = 0; rp < 24; rp++) for (int sg = 0; sg < 16; sg++) for (int st = 0; st < 4; st++) {
    for (int x = 0; x < N; x++) { int l = x / 2, m = x % 2;
      for (int c = 0; c < 2; c++) {
        wt[x][c] = l == 0 ? -1 : 2 * (l - 1) + c;
        xt[x][c] = l == d - 1 ? -1 : 2 * (l + 1) + ((xi >> (2 * m + c)) & 1);
        gate[x][c] = 4 * l + perms[gp][2 * m + c];
        int grp = GROUP == 0 ? l : d - 1 - l; int br = 4 * grp + perms[rp][2 * m + c]; int bp = (sg >> (2 * m + c)) & 1;
        om[x][c] = ((i128)1 << (2 * br + bp)) * (bp == 0 ? 1 : -1);
      }
      start[x] = (st >> m) & 1; }
    long T = run(cap); int mx = 0; for (int x = 0; x < N; x++) if (sw[x] > mx) mx = sw[x];
    R[nr++] = (rec){T, mx, xi, gp, rp, sg, st};
    int b = 0; while ((1L << b) <= T && b < 63) b++; hist[b]++;
  }
  qsort(R, nr, sizeof(rec), cmp);
  printf("DUAL244 d %d GROUP %d templates %ld cap %ld\n", d, GROUP, nr, cap);
  printf("histogram of T (bucket b: 2^(b-1) <= T < 2^b):"); for (int b = 0; b < 40; b++) if (hist[b]) printf(" b%d:%ld", b, hist[b]); printf("\n");
  for (int i = 0; i < TOPN && i < nr; i++) printf("top %d: T %ld maxsw %d xi %d gp %d rp %d sg %d st %d\n", i, R[i].T, R[i].maxsw, R[i].xi, R[i].gp, R[i].rp, R[i].sg, R[i].st);
  return 0;
}
