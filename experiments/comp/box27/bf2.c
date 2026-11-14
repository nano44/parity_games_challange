/* L-COMP box 27 (a): exhaustive T^R(2) by brute force, my own code from the text of RESULTS R104.
   Class: 2-wide degree-2 ladders, d = 2, R197 wiring (option k of a level-1 mover has W-target level-0 mover k), no padding.
   Movers u0=0 v0=1 (level 0), u1=2 v1=3 (level 1); option o = 2x+k, beta id = o.
   Enumerated: every acyclic Xi-target assignment (8 options, target = exit or another mover), every rank order (8!), every
   parity vector (2^8), every relative gate order inside each level (24 x 24; keys compare position by position, position j
   holds a level-j gate, so only the order inside a level can matter), every start (16).
   Xi comparison: literal R104 rule on beta sets (largest rank of the symmetric difference, parity decides).
   Usage: bf2 PART NPARTS  (graphs with index % NPARTS == PART). Prints max T, histogram, a witness. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef unsigned long long u64;
static int xt[8];
static int nF; static unsigned char F[600][16][16]; static int Fg[600][8];
static u64 *H; static u64 HM; static u64 hcount = 0;
static int z0 = 0, z1 = 0;
static int hins(u64 v) { /* returns 1 if new; 0 and ~0 are tracked separately (0 marks an empty slot) */
  if (v == 0) { if (z0) return 0; z0 = 1; return 1; }
  if (v == ~0ULL) { if (z1) return 0; z1 = 1; return 1; }
  u64 h = (v * 0x9E3779B97F4A7C15ULL) >> 20;
  for (u64 i = h & HM;; i = (i + 1) & HM) { if (H[i] == v) return 0; if (!H[i]) { H[i] = v; hcount++; return 1; } }
}
static int acyc(void) { int col[4] = {0}; /* iterative 3-colour DFS on 4 vertices: check by Floyd closure */
  int r[4][4] = {{0}}; for (int o = 0; o < 8; o++) if (xt[o] >= 0) r[o/2][xt[o]] = 1;
  for (int k = 0; k < 4; k++) for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++) if (r[i][k] && r[k][j]) r[i][j] = 1;
  for (int i = 0; i < 4; i++) if (r[i][i]) return 0; (void)col; return 1; }
static void buildF(void) { /* literal key computation for every pair of in-level gate orders, deduplicated */
  int p[4] = {0,1,2,3}, q[4];
  int perms[24][4], np = 0;
  for (int a = 0; a < 4; a++) for (int b = 0; b < 4; b++) for (int c = 0; c < 4; c++) for (int d = 0; d < 4; d++) {
    if (a==b||a==c||a==d||b==c||b==d||c==d) continue; perms[np][0]=a; perms[np][1]=b; perms[np][2]=c; perms[np][3]=d; np++; }
  (void)p; (void)q;
  for (int i = 0; i < 24; i++) for (int j = 0; j < 24; j++) {
    int g[8]; for (int o = 0; o < 4; o++) { g[o] = perms[i][o]; g[4+o] = 4 + perms[j][o]; }
    unsigned char T[16][16];
    for (int s = 0; s < 16; s++) for (int a = 0; a < 16; a++) {
      int ns[4], key0[2];
      for (int x = 0; x < 2; x++) { int sx = (s >> x) & 1; int best = -1, bk = 0;
        for (int k = 0; k < 2; k++) { if (k != sx && !((a >> x) & 1)) continue; int key = g[2*x+k]; if (best < 0 || key < best) { best = key; bk = k; } }
        ns[x] = bk; key0[x] = best; }
      for (int x = 2; x < 4; x++) { int sx = (s >> x) & 1; int best = -1, bk = 0;
        for (int k = 0; k < 2; k++) { if (k != sx && !((a >> x) & 1)) continue; int key = key0[k] * 64 + g[2*x+k]; if (best < 0 || key < best) { best = key; bk = k; } }
        ns[x] = bk; }
      T[s][a] = ns[0] | ns[1] << 1 | ns[2] << 2 | ns[3] << 3; }
    int dup = 0; for (int f = 0; f < nF && !dup; f++) if (!memcmp(F[f], T, 256)) dup = 1;
    if (!dup) { memcpy(F[nF], T, 256); for (int o = 0; o < 8; o++) Fg[nF][o] = g[o]; nF++; } }
}
int main(int argc, char **argv) {
  int part = atoi(argv[1]), nparts = atoi(argv[2]);
  HM = (1ULL << 27) - 1; H = calloc(HM + 1, 8);
  buildF(); fprintf(stderr, "distinct transition functions from 576 gate orders: %d\n", nF);
  static int perms[40320][8]; int np = 0; { int a[8]; for (int i = 0; i < 8; i++) a[i] = i;
    /* Heap-free: lexicographic next_permutation */
    for (;;) { memcpy(perms[np++], a, sizeof a); int i = 6; while (i >= 0 && a[i] > a[i+1]) i--; if (i < 0) break;
      int j = 7; while (a[j] < a[i]) j--; int t = a[i]; a[i] = a[j]; a[j] = t; for (int l = i+1, r = 7; l < r; l++, r--) { t = a[l]; a[l] = a[r]; a[r] = t; } } }
  long hist[64] = {0}; int bestT = -1; char wit[512] = "";
  long gidx = -1, ngraph = 0; u64 ntab = 0;
  int tg[8];
  for (int c = 0; c < 65536; c++) {
    int cc = c, ok = 1; for (int o = 0; o < 8; o++) { tg[o] = (cc % 5) - 1; cc /= 5; } /* 5^8 > 65536: loop below */
    (void)ok; break; }
  /* enumerate 5^8 target vectors */
  for (long c = 0; c < 390625; c++) {
    long cc = c; for (int o = 0; o < 8; o++) { tg[o] = (int)(cc % 5) - 1; cc /= 5; }
    int bad = 0; for (int o = 0; o < 8; o++) if (tg[o] == o / 2) bad = 1; if (bad) continue;
    memcpy(xt, tg, sizeof xt); if (!acyc()) continue;
    gidx++; if (gidx % nparts != part) continue; ngraph++;
    unsigned char C[16][8]; /* chain masks */
    for (int s = 0; s < 16; s++) for (int o = 0; o < 8; o++) { int m = 1 << o, t = xt[o];
      while (t >= 0) { int oo = 2*t + ((s >> t) & 1); m |= 1 << oo; t = xt[oo]; } C[s][o] = m; }
    /* per (s,x): delta mask and chain(x,1) mask */
    unsigned char D[64], C1[64];
    for (int s = 0; s < 16; s++) for (int x = 0; x < 4; x++) { D[s*4+x] = C[s][2*x] ^ C[s][2*x+1]; C1[s*4+x] = C[s][2*x+1]; }
    /* per-graph dedupe of the top assignment (which option is the largest-rank element of each delta) */
    static unsigned char seen[1 << 16][64]; static int seenv[1 << 16]; static int stamp = 0; stamp++;
    for (int pi = 0; pi < np; pi++) { int *rk = perms[pi]; /* rk[o] = rank of option o */
      int ord[8]; for (int o = 0; o < 8; o++) ord[7 - rk[o]] = o; /* decreasing rank */
      unsigned char top[64]; u64 sig = 1469598103934665603ULL;
      for (int i = 0; i < 64; i++) { int t = -1; for (int r = 0; r < 8; r++) if (D[i] >> ord[r] & 1) { t = ord[r]; break; } top[i] = t; sig = (sig ^ (t + 1)) * 1099511628211ULL; }
      u64 hslot = sig & 0xFFFF; int dup = 0;
      for (u64 j = hslot;; j = (j + 1) & 0xFFFF) { if (seenv[j] != stamp) { seenv[j] = stamp; memcpy(seen[j], top, 64); break; } if (!memcmp(seen[j], top, 64)) { dup = 1; break; } }
      if (dup) continue; /* exact: full 64-entry top arrays compared */
      u64 base = 0, Mo[8] = {0};
      for (int i = 0; i < 64; i++) { if (C1[i] >> top[i] & 1) base |= 1ULL << i; Mo[top[i]] |= 1ULL << i; }
      for (int pv = 0; pv < 256; pv++) { u64 tab = base; for (int o = 0; o < 8; o++) if (pv >> o & 1) tab ^= Mo[o];
        /* tab bit (s,x) = 1 iff chain(x,1) is strictly better than chain(x,0) at state s */
        if (!hins(tab)) continue; ntab++;
        if (hcount > (HM * 7) / 10) { fprintf(stderr, "hash full\n"); return 2; }
        for (int f = 0; f < nF; f++) for (int s0 = 0; s0 < 16; s0++) { int s = s0, T = 0;
          for (;;) { int a = 0; for (int x = 0; x < 4; x++) a |= (int)(((tab >> (s*4+x)) & 1) ^ ((s >> x) & 1)) << x;
            if (!a) break; int ns = F[f][s][a]; if (ns == s) break; s = ns; T++; if (T > 60) break; }
          hist[T]++;
          if (T > bestT) { bestT = T; int n = sprintf(wit, "T %d xt", T); for (int o = 0; o < 8; o++) n += sprintf(wit+n, " %d", xt[o]);
            n += sprintf(wit+n, " rank"); for (int o = 0; o < 8; o++) n += sprintf(wit+n, " %d", rk[o]);
            n += sprintf(wit+n, " par"); for (int o = 0; o < 8; o++) n += sprintf(wit+n, " %d", pv >> o & 1);
            n += sprintf(wit+n, " gate"); for (int o = 0; o < 8; o++) n += sprintf(wit+n, " %d", Fg[f][o]);
            sprintf(wit+n, " start %d", s0); } } } }
  }
  printf("part %d/%d graphs %ld distinct_tables %llu maxT %d\n", part, nparts, ngraph, ntab, bestT);
  printf("hist(T: count over tables x transition fns x starts):"); for (int i = 0; i < 64; i++) if (hist[i]) printf(" %d:%ld", i, hist[i]); printf("\n");
  printf("witness %s\n", wit);
  return 0;
}
