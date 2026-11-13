/* L-COMP box 47: genome layer shared by the 1P(G) port and the search (C). A genome = R104's genome space with an e-vertex numbering:
   movers 0..N-1 with levels lev[], options 0..M-1 (canonical order: by mover, then k) with mover ox, W-target wt (a mover one level down,
   -1 at level 0), Ξ-target xt (a mover or -1 = X), gate index gt (a permutation of 0..M-1), β rank br (a permutation), β parity bp,
   start option per mover st[] (k), and er[] = the e-slot rank of each option's e-vertex (a permutation of 0..M-1; box 189's own numbering
   is er = gt). Text format (gen47.py converts JSON <-> text):
     N M / lev x N / M lines «x wt xt gt br bp er» in canonical order / st x N.  Ξ-graph: x -> xt(x, k); must be ACYCLIC (self-loops count). */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define GMAXN 1024
#define GMAXM 4096
typedef struct { int N, M; int lev[GMAXN]; int ox[GMAXM], wt[GMAXM], xt[GMAXM], gt[GMAXM], br[GMAXM], bp[GMAXM], er[GMAXM]; int st[GMAXN];
                 int first[GMAXN + 1]; } Gen;   /* first[x] .. first[x + 1] - 1 = x's options (canonical order) */
static void gfix(Gen *g) { int i = 0; for (int x = 0; x < g->N; x++) { g->first[x] = i; while (i < g->M && g->ox[i] == x) i++; } g->first[g->N] = g->M; }
static int gread(Gen *g, FILE *f) {
  if (fscanf(f, "%d %d", &g->N, &g->M) != 2 || g->N > GMAXN || g->M > GMAXM) return 0;
  for (int x = 0; x < g->N; x++) if (fscanf(f, "%d", &g->lev[x]) != 1) return 0;
  for (int i = 0; i < g->M; i++) if (fscanf(f, "%d %d %d %d %d %d %d", &g->ox[i], &g->wt[i], &g->xt[i], &g->gt[i], &g->br[i], &g->bp[i], &g->er[i]) != 7) return 0;
  for (int x = 0; x < g->N; x++) if (fscanf(f, "%d", &g->st[x]) != 1) return 0;
  gfix(g); return 1; }
static void gwrite(const Gen *g, FILE *f) {
  fprintf(f, "%d %d\n", g->N, g->M); for (int x = 0; x < g->N; x++) fprintf(f, "%d%c", g->lev[x], x + 1 < g->N ? ' ' : '\n');
  for (int i = 0; i < g->M; i++) fprintf(f, "%d %d %d %d %d %d %d\n", g->ox[i], g->wt[i], g->xt[i], g->gt[i], g->br[i], g->bp[i], g->er[i]);
  for (int x = 0; x < g->N; x++) fprintf(f, "%d%c", g->st[x], x + 1 < g->N ? ' ' : '\n'); }
static int gvis[GMAXN];
static int gdfs(const Gen *g, int x) { if (gvis[x] == 2) return 1; if (gvis[x] == 1) return 0; gvis[x] = 1;
  for (int i = g->first[x]; i < g->first[x + 1]; i++) if (g->xt[i] >= 0 && !gdfs(g, g->xt[i])) return 0; gvis[x] = 2; return 1; }
static int gacyclic(const Gen *g) { memset(gvis, 0, sizeof(int) * g->N); for (int x = 0; x < g->N; x++) if (!gdfs(g, x)) return 0; return 1; }
static int gvalid(const Gen *g) {   /* structural check (permutations, levels, targets, start) */
  static int seen[3][GMAXM]; memset(seen, 0, sizeof seen);
  for (int i = 0; i < g->M; i++) { int x = g->ox[i]; if (x < 0 || x >= g->N || (i && g->ox[i - 1] > x)) return 0;
    if (g->lev[x] == 0 ? g->wt[i] != -1 : (g->wt[i] < 0 || g->lev[g->wt[i]] != g->lev[x] - 1)) return 0;
    if (g->xt[i] < -1 || g->xt[i] >= g->N || g->bp[i] < 0 || g->bp[i] > 1) return 0;
    const int *a[3] = { g->gt, g->br, g->er }; for (int j = 0; j < 3; j++) { int v = a[j][i]; if (v < 0 || v >= g->M || seen[j][v]++) return 0; } }
  for (int x = 0; x < g->N; x++) { int d = g->first[x + 1] - g->first[x]; if (d < 1 || g->st[x] < 0 || g->st[x] >= d) return 0; }
  return gacyclic(g); }
static unsigned long long grs = 88172645463325252ULL;
static unsigned long long grnd(void) { grs ^= grs << 13; grs ^= grs >> 7; grs ^= grs << 17; return grs; }
static int gr(int n) { return (int)(grnd() % (unsigned long long)n); }
static int grandlow(const Gen *g, int l) { int c = 0, pick = -1; for (int y = 0; y < g->N; y++) if (g->lev[y] == l && gr(++c) == 0) pick = y; return pick; }
/* insert a fresh value p into a permutation column a[0..M-1] (values >= p shift up) */
static void pins(int *a, int M, int p) { for (int i = 0; i < M; i++) if (a[i] >= p) a[i]++; }
static void pdel(int *a, int M, int p) { for (int i = 0; i < M; i++) if (a[i] > p) a[i]--; }
/* one random mutation in place; returns its kind (0..10) or -1 if not applicable. CAPNM: N + M cap. */
static int gmutate(Gen *g, int CAPNM, int allow_add) {
  int r = gr(allow_add ? 11 : 9), M = g->M, i = gr(M), j = gr(M), t;
  switch (r) {
  case 0: { int x = g->ox[i]; if (!g->lev[x]) return -1; g->wt[i] = grandlow(g, g->lev[x] - 1); return 0; }
  case 1: { int old = g->xt[i]; g->xt[i] = gr(g->N + 1) - 1; if (!gacyclic(g)) { g->xt[i] = old; return -1; } return 1; }
  case 2: t = g->gt[i]; g->gt[i] = g->gt[j]; g->gt[j] = t; return 2;
  case 3: t = g->br[i]; g->br[i] = g->br[j]; g->br[j] = t; return 3;
  case 4: g->bp[i] ^= 1; return 4;
  case 5: { int x = gr(g->N), d = g->first[x + 1] - g->first[x]; if (d < 2) return -1; g->st[x] = gr(d); return 5; }
  case 6: case 7: t = g->er[i]; g->er[i] = g->er[j]; g->er[j] = t; return r;   /* e-numbering transposition (weight 2) */
  case 8: { int a = g->er[i], b = a + 1 + gr(5); if (b >= M) return -1;           /* e-numbering: rotate a short block */
            for (int k = 0; k < M; k++) { if (g->er[k] == a) g->er[k] = b; else if (g->er[k] > a && g->er[k] <= b) g->er[k]--; } return 8; }
  case 9: { if (g->N + M + 1 > CAPNM || M + 1 > GMAXM) return -1;                 /* add an option to mover x (after its last) */
            int x = gr(g->N), pos = g->first[x + 1];
            int wt = g->lev[x] ? grandlow(g, g->lev[x] - 1) : -1, xt = gr(g->N + 1) - 1, pg = gr(M + 1), pb = gr(M + 1), pe = gr(M + 1);
            pins(g->gt, M, pg); pins(g->br, M, pb); pins(g->er, M, pe);
            memmove(&g->ox[pos + 1], &g->ox[pos], sizeof(int) * (M - pos)); memmove(&g->wt[pos + 1], &g->wt[pos], sizeof(int) * (M - pos));
            memmove(&g->xt[pos + 1], &g->xt[pos], sizeof(int) * (M - pos)); memmove(&g->gt[pos + 1], &g->gt[pos], sizeof(int) * (M - pos));
            memmove(&g->br[pos + 1], &g->br[pos], sizeof(int) * (M - pos)); memmove(&g->bp[pos + 1], &g->bp[pos], sizeof(int) * (M - pos));
            memmove(&g->er[pos + 1], &g->er[pos], sizeof(int) * (M - pos));
            g->ox[pos] = x; g->wt[pos] = wt; g->xt[pos] = xt; g->gt[pos] = pg; g->br[pos] = pb; g->bp[pos] = gr(2); g->er[pos] = pe; g->M = M + 1; gfix(g);
            if (!gacyclic(g)) { g->xt[pos] = -1; } return 9; }
  case 10: { int x = g->ox[i], d = g->first[x + 1] - g->first[x]; if (d < 2) return -1;   /* remove option i */
            int k = i - g->first[x]; pdel(g->gt, M, g->gt[i]); pdel(g->br, M, g->br[i]); pdel(g->er, M, g->er[i]);
            int *col[7] = { g->ox, g->wt, g->xt, g->gt, g->br, g->bp, g->er };
            for (int c = 0; c < 7; c++) memmove(&col[c][i], &col[c][i + 1], sizeof(int) * (M - i - 1));
            g->M = M - 1; if (g->st[x] == k) g->st[x] = 0; else if (g->st[x] > k) g->st[x]--; gfix(g); return 10; }
  }
  return -1; }
