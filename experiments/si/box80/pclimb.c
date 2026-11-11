/* L-SI box 80: pulse-aware climb on L^R_d genomes (R110 wiring), IDEAL model (R104 definition), own simulator (same rule as
   sim80.py / box76 tw.py: A-sets on the old state, keys level by level on the new state, lexicographic W-chain keys; gates of the
   four options of a level are assumed distinct, checked at load).
   Text genome: "d D" then lines "xt", "br", "bp", "gate" (2N ints, option m = 2x + k) and "start" (N ints).
   Score (env H = target number of capped levels, LV = H - 1):
     guard = |F(0) - 2| * 4 + sum_{l=1}^{H-2} |F(l) - 2F(l-1) - 2|          (keep levels 0..H-2 capped)
     P     = sum_{j=1}^{H-2} sum_{j-windows} max(0, (H - j) - pulse)          (PULSE-NEST deficits for H capped levels)
     score = -100000 guard - PW * P + 64 F(LV) + min(T, 63)
   Usage: pclimb in.txt seed iters ; env H, PW (default 16), ANNEAL (temperature), OUT, FROZENBELOW (movers < 2*FB not mutated),
   MUT (comma list: only these movers mutated), WIN=1 (also count j-window lengths below H - j + 1, j = 1..H-1: PULSE-NEST's
   second clause, which covers the gaps between pulses as well).
   Exactness: values are __int128; ranks must stay <= ~125 (d <= 31 for the j2t.py lifts); a 4-level lift of a d-28 genome overflows. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define MAXN 80
typedef __int128 VT;
int d, N; int xt[2*MAXN], br[2*MAXN], bp[2*MAXN], gate[2*MAXN], st[MAXN];
static unsigned long long rs = 88172645463325252ULL;
static unsigned long long rnd(void){ rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
static int topo_[MAXN], vis[MAXN], nt;
static int dfs(int x){ if (vis[x] == 2) return 1; if (vis[x] == 1) return 0; vis[x] = 1;
  for (int k = 0; k < 2; k++){ int y = xt[2*x+k]; if (y >= 0 && !dfs(y)) return 0; } vis[x] = 2; topo_[nt++] = x; return 1; }
static int acyclic(void){ memset(vis, 0, sizeof vis); nt = 0; for (int x = 0; x < N; x++) if (!dfs(x)) return 0; return 1; }
static VT bv(int m){ VT b = ((VT)1) << br[m]; return bp[m] ? -b : b; }
#define TMAX 20000
static int F[MAXN], MV[MAXN], T; static short mvstep[MAXN][2*TMAX/8]; static int nmv[MAXN]; /* move steps per pair */
static int bstep[MAXN][TMAX/2]; static int nb[MAXN];   /* flip steps per pair */
static int run(void){
  int s[MAXN], ns[MAXN], o[MAXN], op[MAXN]; VT v[MAXN];
  memcpy(s, st, sizeof(int)*N); memset(F, 0, sizeof F); memset(MV, 0, sizeof MV); memset(nmv, 0, sizeof nmv); memset(nb, 0, sizeof nb);
  /* order bits of s_0 */
  { int c = 0; for (int l = 0; l < d; l++){ int a = s[2*l], b = s[2*l+1];
      op[l] = l == 0 ? (gate[0+a] < gate[2+b]) : (a != b ? (a == c) : (gate[4*l+a] < gate[4*l+2+a]));
      c = op[l] ? 0 : 1; } }
  for (T = 0; T < TMAX - 1; ){
    for (int i = 0; i < N; i++){ int x = topo_[i], m = 2*x + s[x]; v[x] = bv(m) + (xt[m] >= 0 ? v[xt[m]] : 0); }
    int av[MAXN], any = 0;
    for (int x = 0; x < N; x++){ int m = 2*x + 1 - s[x]; VT ov = bv(m) + (xt[m] >= 0 ? v[xt[m]] : 0); av[x] = ov > v[x]; any |= av[x]; }
    if (!any) break;
    int c = 0, ch = 0;
    for (int l = 0; l < d; l++){
      for (int q = 0; q < 2; q++){ int x = 2*l + q; ns[x] = s[x];
        if (l == 0){ if (av[x] && gate[2*x+1-s[x]] < gate[2*x+s[x]]) ns[x] = 1 - s[x]; }
        else if (av[x] && s[x] != c) ns[x] = c; }
      int a = ns[2*l], b = ns[2*l+1];
      o[l] = l == 0 ? (gate[0+a] < gate[2+b]) : (a != b ? (a == c) : (gate[4*l+a] < gate[4*l+2+a]));
      c = o[l] ? 0 : 1; }
    T++;
    for (int l = 0; l < d; l++){
      int mv = 0; for (int q = 0; q < 2; q++){ int x = 2*l+q; if (ns[x] != s[x]){ MV[x]++; mv = 1; ch = 1; } }
      if (mv && nmv[l] < (int)(sizeof mvstep[0]/sizeof(short))) mvstep[l][nmv[l]++] = T;
      if (o[l] != op[l]){ F[l]++; if (nb[l] < TMAX/2) bstep[l][nb[l]++] = T; } op[l] = o[l]; }
    if (!ch){ T--; break; }
    memcpy(s, ns, sizeof(int)*N); }
  return T; }
static int H = 7, PW = 16;
/* pulse deficits of level j (j >= 1) for the requirement pulse >= need: windows delimited by the flips of pair j - 1 */
static long pulsedef(int j, int need){
  long P = 0; int wb = 0, mi = 0; /* window k = [bstep[j-1][k-1], bstep[j-1][k] - 1] */
  for (int k = 0; k <= nb[j-1]; k++){
    int a = k == 0 ? 1 : bstep[j-1][k-1], z = k == nb[j-1] ? T + 1 : bstep[j-1][k];
    int u[4], n = 0; while (mi < nmv[j] && mvstep[j][mi] < z){ if (mvstep[j][mi] >= a && n < 4) u[n++] = mvstep[j][mi]; mi++; }
    int pl = n == 2 ? u[1] - u[0] : 0; if (pl < need) P += need - pl; (void)wb; }
  return P; }
/* window-length deficits of level j (j >= 1): every j-window must have length >= need (PULSE-NEST's second clause) */
static long windef(int j, int need){
  long P = 0;
  for (int k = 0; k <= nb[j-1]; k++){
    int a = k == 0 ? 1 : bstep[j-1][k-1], z = k == nb[j-1] ? T + 1 : bstep[j-1][k];
    if (z - a < need) P += need - (z - a); }
  return P; }
static int WIN = 0;
static long score(int *g, long *P){
  run(); long gd = 4L*abs(F[0] - 2); for (int l = 1; l <= H - 2; l++) gd += labs((long)F[l] - 2L*F[l-1] - 2);
  long p = 0; for (int j = 1; j <= H - 2; j++) p += pulsedef(j, H - j);
  if (WIN) for (int j = 1; j <= H - 1; j++) p += windef(j, H - j + 1);
  *g = (int)gd; *P = p; int LV = H - 1;
  return -100000L*gd - (long)PW*p + 64L*F[LV] + (T < 63 ? T : 63); }
static void rd(const char *fn){ FILE *f = fopen(fn, "r"); char w[64]; if (!f){ perror(fn); exit(1); }
  while (fscanf(f, "%63s", w) == 1){
    if (!strcmp(w, "d")){ if (fscanf(f, "%d", &d) != 1) exit(1); N = 2*d; continue; }
    int *a = !strcmp(w,"xt") ? xt : !strcmp(w,"br") ? br : !strcmp(w,"bp") ? bp : !strcmp(w,"gate") ? gate : !strcmp(w,"start") ? st : NULL;
    if (!a){ int ch; while ((ch = fgetc(f)) != EOF && ch != '\n'); continue; }
    int n = !strcmp(w, "start") ? N : 2*N; for (int i = 0; i < n; i++) if (fscanf(f, "%d", &a[i]) != 1) exit(1); }
  fclose(f); }
static void wr(const char *fn, long sc){ FILE *f = fopen(fn, "w"); fprintf(f, "d %d\nxt", d);
  for (int i = 0; i < 2*N; i++) fprintf(f, " %d", xt[i]); fprintf(f, "\nbr"); for (int i = 0; i < 2*N; i++) fprintf(f, " %d", br[i]);
  fprintf(f, "\nbp"); for (int i = 0; i < 2*N; i++) fprintf(f, " %d", bp[i]); fprintf(f, "\ngate"); for (int i = 0; i < 2*N; i++) fprintf(f, " %d", gate[i]);
  fprintf(f, "\nstart"); for (int i = 0; i < N; i++) fprintf(f, " %d", st[i]);
  fprintf(f, "\n# score %ld T %d F", sc, T); for (int l = 0; l < d; l++) fprintf(f, " %d", F[l]); fprintf(f, "\n"); fclose(f); }
int main(int argc, char **argv){
  if (argc < 4){ fprintf(stderr, "usage\n"); return 1; }
  rd(argv[1]); rs += (unsigned long long)atol(argv[2]) * 7919ULL; long iters = atol(argv[3]);
  if (getenv("H")) H = atoi(getenv("H")); if (getenv("WIN")) WIN = atoi(getenv("WIN")); if (getenv("PW")) PW = atoi(getenv("PW"));
  int FB = getenv("FROZENBELOW") ? atoi(getenv("FROZENBELOW")) : 0;
  int mutl[MAXN], nmut = 0;   /* MUT="x1,x2,...": only these movers' fields are mutated (ranks: swapped with any option) */
  if (getenv("MUT")){ char *p = strdup(getenv("MUT")); for (char *t = strtok(p, ","); t; t = strtok(NULL, ",")) mutl[nmut++] = atoi(t); }
  double temp = getenv("ANNEAL") ? atof(getenv("ANNEAL")) : 0; const char *out = getenv("OUT") ? getenv("OUT") : "/dev/null";
  for (int l = 0; l < d; l++) for (int i = 0; i < 4; i++) for (int j = 0; j < i; j++) if (gate[4*l+i] == gate[4*l+j]){ fprintf(stderr, "gate tie\n"); return 1; }
  if (!acyclic()){ fprintf(stderr, "cyclic\n"); return 1; }
  int g; long P; long cur = score(&g, &P), best = cur; wr(out, best);
  printf("start score %ld guard %d P %ld T %d F", cur, g, P, T); for (int l = 0; l < d; l++) printf(" %d", F[l]); printf("\n"); fflush(stdout);
  static int sxt[2*MAXN], sbr[2*MAXN], sbp[2*MAXN], sg[2*MAXN], sst[MAXN];
  for (long it = 0; it < iters; it++){
    memcpy(sxt, xt, sizeof xt); memcpy(sbr, br, sizeof br); memcpy(sbp, bp, sizeof bp); memcpy(sg, gate, sizeof gate); memcpy(sst, st, sizeof st);
    int nm = 1 + rnd() % 3;
    for (int q = 0; q < nm; q++){ int r = rnd() % 6, m = nmut ? 2*mutl[rnd() % nmut] + (int)(rnd() % 2) : 2*2*FB + rnd() % (2*N - 4*FB);
      if (r <= 1){ int y = (int)(rnd() % (N + 1)) - 1; if (y == m/2) y = -1; xt[m] = y; }
      else if (r == 2){ int m2 = rnd() % (2*N); int t = br[m]; br[m] = br[m2]; br[m2] = t; }
      else if (r == 3){ bp[m] ^= 1; }
      else if (r == 4){ int l = (m/2)/2, i = rnd() % 4, j = rnd() % 4; int t = gate[4*l+i]; gate[4*l+i] = gate[4*l+j]; gate[4*l+j] = t; }
      else { st[m/2] ^= 1; } }
    long sc = -(1L << 60);
    if (acyclic()) sc = score(&g, &P);
    if (sc >= cur || (temp > 0 && sc > -(1L << 59) && exp((sc - cur) / (temp * 256.0)) > (rnd() % 1000000) / 1e6)){
      cur = sc;
      if (sc > best){ best = sc; wr(out, best); printf("it %ld score %ld guard %d P %ld T %d F", it, sc, g, P, T);
        for (int l = 0; l < d && l < H + 2; l++) printf(" %d", F[l]); printf("\n"); fflush(stdout); } }
    else { memcpy(xt, sxt, sizeof xt); memcpy(br, sbr, sizeof br); memcpy(bp, sbp, sizeof bp); memcpy(gate, sg, sizeof gate); memcpy(st, sst, sizeof st); }
  }
  printf("done best %ld\n", best); return 0; }
