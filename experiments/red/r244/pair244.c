/* L-RED 70 R244: PAIR-ON-TOP joint screen (own engine, C; model 1P(G), general Xi-acyclic genome, degree 2).
   Base genome G (text dump by dump244.py) with a full block whose top full mover is F (index FI) over the pair (A, B) = (F's W-targets),
   B = the old second mover of the level below (index BI). The screen adds ONE mover y at F's level (W-targets A, B; own betas at the two
   lowest ranks, both rank orders and parities; gates above every gate, both orders; both starts; Xi-targets v0, v1 over exit + all movers)
   and RE-WIRES B's two Xi-targets (u0, u1) so that at least one of them is y (MODE 1), or leaves B as it is (MODE 0, control).
   Every candidate is simulated in full. Filter INTACT: the per-level best switch counts of the levels below F's level are unchanged and
   sw(F) is unchanged. Reported: number of candidates, of acyclic ones, of INTACT ones; best (KF, sw(y)) among INTACT, KF = number of
   changes of the key order between F and y along the run (the key flips a mover one level up with W-targets (F, y) would see; a
   staggered full pair has KF = 2 sw(F)); and the histogram of KF among INTACT candidates.
   Usage: pair244 G.txt FI BI MODE */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#define MAXN 64
#define MAXL 24
typedef struct { uint64_t w[3]; } big;
static inline big badd(big a, big b) { big r; unsigned __int128 c = (unsigned __int128)a.w[0] + b.w[0]; r.w[0] = (uint64_t)c; c = (c >> 64) + a.w[1] + b.w[1]; r.w[1] = (uint64_t)c; r.w[2] = a.w[2] + b.w[2] + (uint64_t)(c >> 64); return r; }
static inline int bgt(big a, big b) { if (a.w[2] != b.w[2]) return (int64_t)a.w[2] > (int64_t)b.w[2]; if (a.w[1] != b.w[1]) return a.w[1] > b.w[1]; return a.w[0] > b.w[0]; }
static big bpow(int e, int neg) { big r = {{0, 0, 0}}; r.w[e / 64] = 1ULL << (e % 64); if (neg) { r.w[0] = ~r.w[0]; r.w[1] = ~r.w[1]; r.w[2] = ~r.w[2]; big one = {{1, 0, 0}}; r = badd(r, one); } return r; }
static int N, lev[MAXN], st[MAXN], wt[MAXN][2], xt[MAXN][2], ex[MAXN][2], gate[MAXN][2], lord[MAXN], topo[MAXN], sw[MAXN];
static big om[MAXN][2];
static int mktopo(void) {
  int col[MAXN] = {0}, n = 0, stk[MAXN], it[MAXN];
  for (int r = 0; r < N; r++) { if (col[r]) continue; int sp = 0; stk[0] = r; it[0] = 0; col[r] = 1;
    while (sp >= 0) { int v = stk[sp];
      if (it[sp] < 2) { int w = xt[v][it[sp]++]; if (w < 0) continue; if (col[w] == 1) return 0; if (col[w] == 0) { col[w] = 1; stk[++sp] = w; it[sp] = 0; } }
      else { col[v] = 2; topo[n++] = v; sp--; } } }
  return 1;
}
static int FI, YI; static long KF;
static long run(long cap) {
  int s[MAXN], ns[MAXN], key[MAXN][MAXL]; big V[MAXN + 1]; long T = 0; int prev = -1; KF = 0;
  for (int x = 0; x < N; x++) { s[x] = st[x]; sw[x] = 0; }
  memset(&V[N], 0, sizeof(big));
  while (T < cap) {
    for (int i = 0; i < N; i++) { int x = topo[i], t = xt[x][s[x]]; V[x] = badd(om[x][s[x]], V[t < 0 ? N : t]); }
    int ch = 0;
    for (int i = 0; i < N; i++) { int x = lord[i], l = lev[x], best = -1, bk[MAXL];
      for (int c = 0; c < 2; c++) { int t = xt[x][c];
        if (c != s[x] && !bgt(badd(om[x][c], V[t < 0 ? N : t]), V[x])) continue;
        int kk[MAXL]; if (l > 0) memcpy(kk, key[wt[x][c]], sizeof(int) * l); kk[l] = gate[x][c];
        int less = 0; if (best < 0) less = 1; else for (int j = 0; j <= l; j++) if (kk[j] != bk[j]) { less = kk[j] < bk[j]; break; }
        if (less) { best = c; memcpy(bk, kk, sizeof(int) * (l + 1)); } }
      memcpy(key[x], bk, sizeof(int) * (l + 1)); ns[x] = best; if (best != s[x]) { sw[x]++; ch = 1; } }
    if (YI >= 0) { int l = lev[FI], o = 0; for (int j = 0; j <= l; j++) if (key[FI][j] != key[YI][j]) { o = key[FI][j] < key[YI][j]; break; }
      if (prev >= 0 && o != prev) KF++; prev = o; }
    if (!ch) break;
    memcpy(s, ns, sizeof(int) * N); T++;
  }
  return T;
}
int main(int argc, char **argv) {
  FILE *f = fopen(argv[1], "r"); FI = atoi(argv[2]); int BI = atoi(argv[3]); int MODE = atoi(argv[4]); int N0;
  if (fscanf(f, "%d", &N0) != 1) return 2;
  for (int x = 0; x < N0; x++) { if (fscanf(f, "%d %d", &lev[x], &st[x]) != 2) return 2; for (int c = 0; c < 2; c++) if (fscanf(f, "%d %d %d %d", &wt[x][c], &xt[x][c], &ex[x][c], &gate[x][c]) != 4) return 2; }
  fclose(f);
  int gmax = 0; for (int x = 0; x < N0; x++) for (int c = 0; c < 2; c++) if (gate[x][c] > gmax) gmax = gate[x][c];
  /* base run */
  N = N0; YI = -1; { int idx[MAXN]; for (int i = 0; i < N; i++) idx[i] = i; for (int i = 0; i < N; i++) for (int j = i + 1; j < N; j++) if (lev[idx[j]] < lev[idx[i]] || (lev[idx[j]] == lev[idx[i]] && idx[j] < idx[i])) { int t = idx[i]; idx[i] = idx[j]; idx[j] = t; } memcpy(lord, idx, sizeof(int) * N); }
  for (int x = 0; x < N0; x++) for (int c = 0; c < 2; c++) om[x][c] = bpow(ex[x][c], ex[x][c] & 1);
  if (!mktopo()) return 3; long T0 = run(1000000); int LF = lev[FI], base[MAXL] = {0}, swF = sw[FI];
  for (int x = 0; x < N0; x++) if (lev[x] < LF && sw[x] > base[lev[x]]) base[lev[x]] = sw[x];
  printf("PAIR244 base %s: N %d T %ld F %d (level %d, sw %d) B %d (sw %d); best per level below F:", argv[1], N0, T0, FI, LF, swF, BI, sw[BI]); for (int l = 0; l < LF; l++) printf(" %d", base[l]); printf("\n");
  /* add y */
  int y = N0; N = N0 + 1; YI = y; lev[y] = LF; wt[y][0] = wt[FI][0]; wt[y][1] = wt[FI][1];
  { int idx[MAXN]; for (int i = 0; i < N; i++) idx[i] = i; for (int i = 0; i < N; i++) for (int j = i + 1; j < N; j++) if (lev[idx[j]] < lev[idx[i]] || (lev[idx[j]] == lev[idx[i]] && idx[j] < idx[i])) { int t = idx[i]; idx[i] = idx[j]; idx[j] = t; } memcpy(lord, idx, sizeof(int) * N); }
  for (int x = 0; x < N0; x++) for (int c = 0; c < 2; c++) om[x][c] = bpow(ex[x][c] + 4, ex[x][c] & 1);
  int bu0 = xt[BI][0], bu1 = xt[BI][1]; long cand = 0, acyc = 0, intact = 0, hist[400] = {0}; long bestKF = -1; int bestsw = -1, brec[10] = {0};
  int nb = MODE == 0 ? 1 : 2 * (N0 + 1);
  for (int bv = 0; bv < nb; bv++) {
    if (MODE == 1) { int other = bv / 2 - 1; if (other == y) continue; if (bv % 2 == 0) { xt[BI][0] = y; xt[BI][1] = other; } else { xt[BI][1] = y; xt[BI][0] = other; } if (other == BI) continue; }
    for (int v0 = -1; v0 < N0; v0++) for (int v1 = -1; v1 < N0; v1++) {
      xt[y][0] = v0; xt[y][1] = v1; if (!mktopo()) { cand += 32; continue; }
      for (int var = 0; var < 32; var++) { cand++; acyc++;
        int p0 = var & 1, p1 = (var >> 1) & 1, ro = (var >> 2) & 1, go = (var >> 3) & 1, s0 = (var >> 4) & 1;
        om[y][0] = bpow(2 * ro + p0, p0); om[y][1] = bpow(2 * (1 - ro) + p1, p1); gate[y][0] = gmax + 1 + go; gate[y][1] = gmax + 2 - go; st[y] = s0;
        run(100000); int ok = sw[FI] == swF; int b[MAXL] = {0};
        for (int x = 0; x < N0 && ok; x++) if (lev[x] < LF && sw[x] > b[lev[x]]) b[lev[x]] = sw[x];
        for (int l = 0; l < LF && ok; l++) if (b[l] != base[l]) ok = 0;
        if (!ok) continue;
        intact++; hist[KF < 399 ? KF : 399]++;
        if (KF > bestKF || (KF == bestKF && sw[y] > bestsw)) { bestKF = KF; bestsw = sw[y]; int r[10] = {xt[BI][0], xt[BI][1], v0, v1, p0, p1, ro, go, s0, sw[BI]}; memcpy(brec, r, sizeof(r)); }
      } }
  }
  xt[BI][0] = bu0; xt[BI][1] = bu1;
  printf("PAIR244 MODE %d: candidates %ld acyclic %ld INTACT %ld | best KF %ld (staggered full pair: %d) with sw(y) %d at B Xi-targets (%d, %d) y Xi-targets (%d, %d) parities (%d, %d) rankorder %d gateorder %d start %d, sw(B) %d\n",
         MODE, cand, acyc, intact, bestKF, 2 * swF, bestsw, brec[0], brec[1], brec[2], brec[3], brec[4], brec[5], brec[6], brec[7], brec[8], brec[9]);
  printf("PAIR244 KF histogram among INTACT (KF:count):"); for (int i = 0; i < 400; i++) if (hist[i]) printf(" %d:%ld", i, hist[i]); printf("\n");
  return 0;
}
