/* L-LOWER 10 (item 2): C port of anneal.py (same score, same moves; d <= 32 -> 64 movers, 128 options).
   Score of a genome = violations of the error-tolerant greedy decision list (gsolve.py) on the constraints of the full trajectory
   in which movers 0..K-1 are clamped to the target (core file) and helpers follow the genome's rules (sim6 / R104).
   Score 0 = the exact greedy (l7/ranksolve.py) succeeds; the final genome is re-checked in Python (ranksolve + sim6).
   Preferences by ENC: top option of chain(x,0) xor chain(x,1) by rank (128-bit masks), no big integers.
   Usage: ann GENOME.txt CORE.txt OUT SEED SECONDS TEMP [X:y1,y2,...]   (resumes from OUT if it exists)
   Optional 8th argument: comma list of option indices whose targets are never re-pointed (a hand-wired gadget).
   Optional order constraint: no mover y_i may reach mover X (or any of X1+X2+..) by Xi-edges (closure); enforced on every move and repaired at start.
   Build: gcc -O2 -o ann ann.c -lm */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
typedef unsigned __int128 u128;
#define MAXN 64
#define MAXO 128
#define MAXT 1100
int d, N, NO, K, T;
int xt[MAXO], br[MAXO], bp[MAXO], gate[4 * 32], start[MAXN];
unsigned char core[MAXT][MAXN];
unsigned char S[MAXT][MAXN];
static int topo_ord[MAXN];
unsigned long long rs = 88172645463325252ULL;
unsigned long long rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
double urand(void) { return (rnd() >> 11) * (1.0 / 9007199254740992.0); }
int rd_genome(const char *p) {
  FILE *f = fopen(p, "r"); if (!f) return 0; char w[64];
  while (fscanf(f, "%63s", w) == 1) {
    if (!strcmp(w, "d")) { if (fscanf(f, "%d", &d) != 1) return 0; N = 2 * d; NO = 2 * N; }
    else if (!strcmp(w, "xt")) for (int i = 0; i < NO; i++) { if (fscanf(f, "%d", &xt[i]) != 1) return 0; }
    else if (!strcmp(w, "br")) for (int i = 0; i < NO; i++) { if (fscanf(f, "%d", &br[i]) != 1) return 0; }
    else if (!strcmp(w, "bp")) for (int i = 0; i < NO; i++) { if (fscanf(f, "%d", &bp[i]) != 1) return 0; }
    else if (!strcmp(w, "gate")) for (int i = 0; i < 2 * N; i++) { if (fscanf(f, "%d", &gate[i]) != 1) return 0; }
    else if (!strcmp(w, "start")) for (int i = 0; i < N; i++) { if (fscanf(f, "%d", &start[i]) != 1) return 0; }
    else { int c; while ((c = fgetc(f)) != '\n' && c != EOF); }
  }
  fclose(f); return 1;
}
void wr_genome(const char *p) {
  char tmp[512]; snprintf(tmp, sizeof tmp, "%s.tmp", p); FILE *f = fopen(tmp, "w");
  fprintf(f, "d %d\nxt", d); for (int i = 0; i < NO; i++) fprintf(f, " %d", xt[i]);
  fprintf(f, "\nbr"); for (int i = 0; i < NO; i++) fprintf(f, " %d", br[i]);
  fprintf(f, "\nbp"); for (int i = 0; i < NO; i++) fprintf(f, " %d", bp[i]);
  fprintf(f, "\ngate"); for (int i = 0; i < 2 * N; i++) fprintf(f, " %d", gate[i]);
  fprintf(f, "\nstart"); for (int i = 0; i < N; i++) fprintf(f, " %d", start[i]);
  fprintf(f, "\n"); fclose(f); rename(tmp, p);
}
int vis[MAXN], nord;
int dfs(int x) {
  if (vis[x] == 2) return 1; if (vis[x] == 1) return 0; vis[x] = 1;
  for (int k = 0; k < 2; k++) { int y = xt[2 * x + k]; if (y >= 0 && !dfs(y)) return 0; }
  vis[x] = 2; topo_ord[nord++] = x; return 1;
}
int topo(void) { memset(vis, 0, sizeof vis); nord = 0; for (int x = 0; x < N; x++) if (!dfs(x)) return 0; return 1; }
/* masks of the chain of each mover's CURRENT option: by rank (rm, with sign mask rn) and by option id (im) */
u128 rm[MAXN], rn[MAXN], im[MAXN];
#define B1 ((u128)1)
void chains(const unsigned char *s) {
  for (int i = 0; i < N; i++) {
    int x = topo_ord[i], m = 2 * x + s[x], y = xt[m];
    rm[x] = (B1 << br[m]) | (y >= 0 ? rm[y] : 0); rn[x] = (bp[m] ? (B1 << br[m]) : 0) | (y >= 0 ? rn[y] : 0);
    im[x] = (B1 << m) | (y >= 0 ? im[y] : 0);
  }
}
static inline int topbit(u128 v) { unsigned long long hi = (unsigned long long)(v >> 64), lo = (unsigned long long)v;
  return hi ? 127 - __builtin_clzll(hi) : 63 - __builtin_clzll(lo); }
int pref(int x, const unsigned char *s) {   /* uses rm/rn of state s */
  u128 a[2], an[2];
  for (int k = 0; k < 2; k++) { int m = 2 * x + k, y = xt[m];
    a[k] = (B1 << br[m]) | (y >= 0 ? rm[y] : 0); an[k] = (bp[m] ? (B1 << br[m]) : 0) | (y >= 0 ? rn[y] : 0); }
  u128 dl = a[0] ^ a[1]; int tb = topbit(dl); u128 bit = B1 << tb; int in1 = (a[1] & bit) != 0, neg = (an[in1] & bit) != 0;
  /* option-1 chain better iff top in chain1 and positive, or top in chain0 and negative */
  return in1 ? !neg : neg;
}
int okey_l(const unsigned char *s, int l, int c) {
  if (l == 0) return gate[0 + s[0]] > gate[2 + s[1]];
  int a = s[2 * l], b = s[2 * l + 1];
  return a != b ? (a != c) : (gate[4 * l + a] > gate[4 * l + 2 + a]);
}
/* constraints */
#define MAXC 40000
u128 cA[MAXC], cB[MAXC]; unsigned char cp[MAXC]; int nc;
int simulate(void) {
  unsigned char s[MAXN], ns[MAXN];
  for (int x = 0; x < N; x++) s[x] = x < K ? core[0][x] : start[x];
  memcpy(S[0], s, N); nc = 0;
  for (int t = 1; t <= T; t++) {
    chains(s); int c = 0;
    for (int l = 0; l < d; l++) {
      for (int q = 0; q < 2; q++) {
        int x = 2 * l + q, fr;
        if (l == 0) fr = gate[2 * x + 1 - s[x]] < gate[2 * x + s[x]]; else fr = s[x] != c;
        if (x < K) ns[x] = core[t][x];
        else ns[x] = (fr && pref(x, s) != s[x]) ? (l == 0 ? 1 - s[x] : c) : s[x];
        if (fr && nc < MAXC) { int m0 = 2 * x, m1 = 2 * x + 1;
          cA[nc] = (B1 << m0) | (xt[m0] >= 0 ? im[xt[m0]] : 0); cB[nc] = (B1 << m1) | (xt[m1] >= 0 ? im[xt[m1]] : 0);
          cp[nc] = ns[x]; nc++; }
      }
      c = okey_l(ns, l, c);
    }
    memcpy(s, ns, N); memcpy(S[t], s, N);
  }
  return nc;
}
/* error-tolerant greedy decision list; writes ranks/signs into gbr/gbp */
int gbr[MAXO], gbp[MAXO];
int gsolve(void) {
  static int pos[MAXO], neg[MAXO]; static unsigned char open[MAXC]; static int *by[MAXO]; static int nby[MAXO], cap[MAXO];
  for (int m = 0; m < NO; m++) { pos[m] = neg[m] = 0; nby[m] = 0; if (!by[m]) { cap[m] = 1024; by[m] = malloc(cap[m] * sizeof(int)); } }
  for (int i = 0; i < nc; i++) {
    u128 D = cA[i] ^ cB[i]; open[i] = 1;
    while (D) { int m = topbit(D); D &= ~(B1 << m); int inB = (cB[i] >> m) & 1; int sg = (inB == (cp[i] == 1));
      if (sg) pos[m]++; else neg[m]++;
      if (nby[m] == cap[m]) { cap[m] *= 2; by[m] = realloc(by[m], cap[m] * sizeof(int)); } by[m][nby[m]++] = i; }
  }
  int left[MAXO], nl = NO, rank = NO - 1, viol = 0; for (int m = 0; m < NO; m++) left[m] = 1;
  while (1) {
    int best = -1, bk1 = 0, bk2 = 0;
    for (int m = 0; m < NO; m++) if (left[m] && pos[m] + neg[m] > 0) {
      int k1 = pos[m] < neg[m] ? pos[m] : neg[m], k2 = -(pos[m] > neg[m] ? pos[m] : neg[m]);
      if (best < 0 || k1 < bk1 || (k1 == bk1 && k2 < bk2)) { best = m; bk1 = k1; bk2 = k2; } }
    if (best < 0) break;
    int m = best, sg = pos[m] >= neg[m]; viol += bk1; gbr[m] = rank--; gbp[m] = sg ? 0 : 1; left[m] = 0; nl--;
    for (int j = 0; j < nby[m]; j++) { int i = by[m][j]; if (!open[i]) continue; open[i] = 0;
      u128 D = cA[i] ^ cB[i];
      while (D) { int mm = topbit(D); D &= ~(B1 << mm); int inB = (cB[i] >> mm) & 1; int s2 = (inB == (cp[i] == 1));
        if (s2) pos[mm]--; else neg[mm]--; } }
  }
  for (int m = 0; m < NO; m++) if (left[m]) { gbr[m] = rank--; gbp[m] = bp[m]; }
  return viol;
}
int nrX = -1; unsigned long long nrMask = 0, nrXmask = 0;
int reaches(int y, int X) { /* DFS over options */
  static int st[MAXN], seen[MAXN]; int sp = 0; memset(seen, 0, sizeof seen); st[sp++] = y; seen[y] = 1;
  while (sp) { int z = st[--sp]; for (int k = 0; k < 2; k++) { int w = xt[2 * z + k]; if (w < 0) continue; if (X >= 0 ? w == X : ((nrXmask >> w) & 1ULL)) return 1; if (!seen[w]) { seen[w] = 1; st[sp++] = w; } } }
  return 0; }
int order_ok(void) { if (!nrMask) return 1; for (int y = 0; y < N; y++) if ((nrMask >> y) & 1ULL && reaches(y, nrX)) return 0; return 1; }
int score(void) { if (!topo() || !order_ok()) return 1 << 30; simulate(); return gsolve(); }
/* genome copy */
typedef struct { int xt[MAXO], br[MAXO], bp[MAXO], gate[4 * 32], start[MAXN]; } G;
void save(G *g) { memcpy(g->xt, xt, sizeof xt); memcpy(g->br, br, sizeof br); memcpy(g->bp, bp, sizeof bp); memcpy(g->gate, gate, sizeof gate); memcpy(g->start, start, sizeof start); }
void load(G *g) { memcpy(xt, g->xt, sizeof xt); memcpy(br, g->br, sizeof br); memcpy(bp, g->bp, sizeof bp); memcpy(gate, g->gate, sizeof gate); memcpy(start, g->start, sizeof start); }
unsigned char frozen[MAXO];
void mutate(void) {
  double r = urand();
  if (r < 0.55) { for (int k = 0; k < 20; k++) { int m = rnd() % NO, x = m / 2, y = (int)(rnd() % (N + 1)) - 1;
      if (y == x || frozen[m]) continue; int old = xt[m]; xt[m] = y; if (topo()) return; xt[m] = old; } return; }
  if (r < 0.75) { int a = rnd() % NO, b = rnd() % NO, t = br[a]; br[a] = br[b]; br[b] = t; return; }
  if (r < 0.85) { bp[rnd() % NO] ^= 1; return; }
  if (r < 0.93) { int l = 8 + rnd() % (d - 8); for (int i = 3; i > 0; i--) { int j = rnd() % (i + 1), t = gate[4 * l + i]; gate[4 * l + i] = gate[4 * l + j]; gate[4 * l + j] = t; } return; }
  start[K + rnd() % (N - K)] ^= 1;
}
int main(int argc, char **argv) {
  if (argc < 7) { fprintf(stderr, "usage: ann GENOME CORE OUT SEED SECONDS TEMP\n"); return 2; }
  const char *out = argv[3]; FILE *tf = fopen(out, "r");
  if (tf) { fclose(tf); if (!rd_genome(out)) return 3; } else if (!rd_genome(argv[1])) return 3;
  gate[28] = 1028; gate[29] = 1029; gate[30] = 1030; gate[31] = 1031;   /* level 7: joined value 0 */
  FILE *cf = fopen(argv[2], "r"); int n1; if (fscanf(cf, "%d %d", &n1, &K) != 2) return 4; T = n1 - 1;
  for (int t = 0; t <= T; t++) { char buf[128]; if (fscanf(cf, "%127s", buf) != 1) return 4; for (int x = 0; x < K; x++) core[t][x] = buf[x] - '0'; }
  fclose(cf);
  if (argc > 7 && argv[7][0] != '-') { char *q = argv[7];
    /* X part: one mover, or several separated by '+' (then nrX = -1 and nrXmask holds them) */
    if (strchr(q, '+') && strchr(q, '+') < strchr(q, ':')) { nrX = -1; while (*q != ':') { nrXmask |= 1ULL << atoi(q); while (*q != '+' && *q != ':') q++; if (*q == '+') q++; } }
    else nrX = atoi(q);
    q = strchr(q, ':') + 1;
    while (*q) { nrMask |= 1ULL << atoi(q); while (*q && *q != ',') q++; if (*q == ',') q++; }
    /* repair: cut options that make a constrained mover reach X (set them to exit) until the order holds */
    for (int pass = 0; pass < 200 && !order_ok(); pass++)
      for (int y = 0; y < N; y++) if ((nrMask >> y) & 1ULL) for (int k = 0; k < 2; k++) { int w = xt[2 * y + k];
        if (w >= 0) { int bad = (nrX >= 0 ? w == nrX : ((nrXmask >> w) & 1ULL)) || reaches(w, nrX); if (bad) xt[2 * y + k] = -1; } }
    printf("order constraint X %d mask %llx ok %d\n", nrX, nrMask, order_ok()); }
  if (argc > 8) { char *q = argv[8]; while (*q) { frozen[atoi(q)] = 1; while (*q && *q != ',') q++; if (*q == ',') q++; } }
  rs ^= (unsigned long long)atoll(argv[4]) * 2654435761ULL; double secs = atof(argv[5]), temp = atof(argv[6]);
  int cur = score(), best = cur; G g, bestg; save(&g); save(&bestg); long it = 0, acc = 0; time_t t0 = time(0), last = t0;
  printf("start score %d constraints %d\n", cur, nc); fflush(stdout);
  while (difftime(time(0), t0) < secs) {
    it++; load(&g); mutate(); int v = score();
    if (v <= cur || urand() < exp((cur - v) / temp)) {
      save(&g); cur = v; acc++;
      if (acc % 50 == 0) { memcpy(br, gbr, sizeof br); memcpy(bp, gbp, sizeof bp); int v2 = score(); if (v2 <= cur) { save(&g); cur = v2; } else load(&g); }
      if (cur < best) { best = cur; save(&bestg); wr_genome(out); if (best == 0) { printf("HIT score 0\n"); break; } }
    }
    if (difftime(time(0), last) >= 60) { last = time(0); struct tm *u = gmtime(&last);
      printf("%02d:%02d:%02d it %ld acc %ld cur %d best %d\n", u->tm_hour, u->tm_min, u->tm_sec, it, acc, cur, best); fflush(stdout); }
  }
  printf("end best %d it %ld\n", best, it); return 0;
}
