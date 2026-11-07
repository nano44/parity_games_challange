/* L-RED R214 tw.c: SINGLE-START climber for R197 ladders of L^R_d (d <= 13), built from r214/fa.c's step (stepL, validated against
   r187/ideal.py via r212/xvalfl.py) and mutation operators. Genome text as fa/fl plus a line "start b0 b1 ... b_{N-1}".
   Score: moves of the best mover of level LEV (env LEV; LEV=-1: any mover) along the run from the stored start, x 256, + T.
   Mutations: fa's genome mutations, or (prob. 1/5) flip a start bit. Search tool only; every output is replayed by r214/lowrep.py.
   Usage: tw eval m < g.txt | tw climb m seed iters out.txt seed.txt    (env ANNEAL temp, LEV) */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <math.h>
#define MAXN 26
int m, N, NU, M;                      /* N movers (levels 0..m), NU = 2m upper movers, M = 2N options */
typedef struct { int xt[MAXN][2]; int br[2*MAXN]; int bp[2*MAXN]; int gate[MAXN][2]; } Gen;
static int lev(int v) { return v / 2; }
static int wt(int v, int k) { return lev(v) > 0 ? 2 * (lev(v) - 1) + k : -1; }
static int64_t eps(const Gen *g, int v, int k) { int o = 2 * v + k; int64_t e = (int64_t)1 << g->br[o]; return g->bp[o] ? -e : e; }
static int64_t face(const Gen *g, const int *st, int v, int k) {
    int64_t t = 0; int guard = 0;
    while (1) { t += eps(g, v, k); int x = g->xt[v][k]; if (x < 0) return t; v = x; k = st[x]; if (++guard > 1000) { fprintf(stderr, "cyc\n"); exit(2); } }
}
static int q0[2][2]; static int ISO = 0; static int ALLM = 0; static int trueT[MAXN];                   /* level-0 config per bit */
static void setq(const Gen *g) {
    int have[2] = {0, 0};
    for (int a = 0; a < 2; a++) for (int c = 0; c < 2; c++) { int b = g->gate[0][a] < g->gate[1][c]; if (!have[b]) { have[b] = 1; q0[b][0] = a; q0[b][1] = c; } }
    if (!have[0] || !have[1]) { fprintf(stderr, "level 0 cannot realise both bits\n"); exit(2); }
}
/* full-ladder step: state bitmask over all N movers */
static uint64_t stepL(const Gen *g, uint64_t up) {
    int st[MAXN], ns[MAXN], avail[MAXN], any = 0;
    for (int v = 0; v < N; v++) st[v] = (up >> v) & 1;
    for (int v = 0; v < N; v++) { avail[v] = face(g, st, v, 1 - st[v]) > face(g, st, v, st[v]); any |= avail[v]; }
    if (!any) return up;
    int lt[MAXN];
    for (int j = 0; j < 2; j++) { ns[j] = st[j]; if (avail[j]) ns[j] = g->gate[j][0] < g->gate[j][1] ? 0 : 1; }
    lt[0] = g->gate[0][ns[0]] < g->gate[1][ns[1]]; lt[1] = !lt[0];
    for (int l = 1; l <= m; l++) {
        for (int j = 0; j < 2; j++) { int v = 2 * l + j; ns[v] = avail[v] ? (lt[2 * (l - 1)] ? 0 : 1) : st[v]; }
        int a = 2 * l, c = 2 * l + 1, wa = wt(a, ns[a]), wc = wt(c, ns[c]);
        int alt = (wa != wc) ? lt[wa] : (g->gate[a][ns[a]] < g->gate[c][ns[c]]);
        lt[a] = alt; lt[c] = !alt;
    }
    uint64_t r = 0; for (int v = 0; v < N; v++) r |= (uint64_t)ns[v] << v; return r;
}
static int reach(const Gen *g, int from, int to) { /* is 'to' reachable from 'from' in the Xi-graph */
    int stk[MAXN], sp = 0, seen[MAXN] = {0}; stk[sp++] = from; seen[from] = 1;
    while (sp) { int v = stk[--sp]; if (v == to) return 1; for (int k = 0; k < 2; k++) { int x = g->xt[v][k]; if (x >= 0 && !seen[x]) { seen[x] = 1; stk[sp++] = x; } } }
    return 0;
}
static uint64_t rs; static uint64_t rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
static int rn(int n) { return (int)(rnd() % (uint64_t)n); }
static void randg(Gen *g) {
    for (int v = 0; v < N; v++) for (int k = 0; k < 2; k++) g->xt[v][k] = -1;
    for (int v = 0; v < N; v++) for (int k = 0; k < 2; k++) { int lo = ISO ? 2 : 0; int t = lo + rn(N - lo + 1); if (t == N) t = -1; if (t == v || (t >= 0 && reach(g, t, v))) t = -1; g->xt[v][k] = t; }
    for (int i = 0; i < M; i++) g->br[i] = i;
    for (int i = M - 1; i > 0; i--) { int j = rn(i + 1); int t = g->br[i]; g->br[i] = g->br[j]; g->br[j] = t; }
    for (int i = 0; i < M; i++) g->bp[i] = rn(2);
    int gp[2 * MAXN]; for (int i = 0; i < M; i++) gp[i] = i;
    for (int i = M - 1; i > 0; i--) { int j = rn(i + 1); int t = gp[i]; gp[i] = gp[j]; gp[j] = t; }
    for (int v = 0; v < N; v++) { g->gate[v][0] = gp[2 * v]; g->gate[v][1] = gp[2 * v + 1]; }
    /* level 0 must realise both bits */
    int lo = g->gate[0][0] < g->gate[0][1] ? g->gate[0][0] : g->gate[0][1];
    (void)lo;
}
static int bothbits(const Gen *g) { int h[2] = {0, 0}; for (int a = 0; a < 2; a++) for (int c = 0; c < 2; c++) h[g->gate[0][a] < g->gate[1][c]] = 1; return h[0] && h[1]; }
static void mutate(Gen *g) {
    int r = rn(100);
    if (r < 30) { /* Xi retarget */
        for (int tries = 0; tries < 50; tries++) {
            int lo = ISO ? 2 : 0; int v = rn(N), k = rn(2), t = lo + rn(N - lo + 1); if (t == N) t = -1;
            if (t == v) continue; int old = g->xt[v][k]; g->xt[v][k] = -1;
            if (t >= 0 && reach(g, t, v)) { g->xt[v][k] = old; continue; }
            g->xt[v][k] = t; return;
        }
    } else if (r < 60) { int i = rn(M), j = rn(M); int t = g->br[i]; g->br[i] = g->br[j]; g->br[j] = t; }
    else if (r < 75) { g->bp[rn(M)] ^= 1; }
    else { for (int tries = 0; tries < 50; tries++) { int a = rn(N), ka = rn(2), c = rn(N), kc = rn(2); int t = g->gate[a][ka]; g->gate[a][ka] = g->gate[c][kc]; g->gate[c][kc] = t; if (bothbits(g)) return; t = g->gate[a][ka]; g->gate[a][ka] = g->gate[c][kc]; g->gate[c][kc] = t; } }
}
static void printg(FILE *f, const Gen *g) {
    fprintf(f, "m %d\nxt", m); for (int v = 0; v < N; v++) for (int k = 0; k < 2; k++) fprintf(f, " %d", g->xt[v][k]);
    fprintf(f, "\nbr"); for (int i = 0; i < M; i++) fprintf(f, " %d", g->br[i]);
    fprintf(f, "\nbp"); for (int i = 0; i < M; i++) fprintf(f, " %d", g->bp[i]);
    fprintf(f, "\ngate"); for (int v = 0; v < N; v++) for (int k = 0; k < 2; k++) fprintf(f, " %d", g->gate[v][k]);
    fprintf(f, "\n");
}
static int readg(FILE *f, Gen *g) {
    char w[16]; int mm; if (fscanf(f, "%15s %d", w, &mm) != 2 || mm != m) return 0;
    fscanf(f, "%15s", w); for (int v = 0; v < N; v++) for (int k = 0; k < 2; k++) fscanf(f, "%d", &g->xt[v][k]);
    fscanf(f, "%15s", w); for (int i = 0; i < M; i++) fscanf(f, "%d", &g->br[i]);
    fscanf(f, "%15s", w); for (int i = 0; i < M; i++) fscanf(f, "%d", &g->bp[i]);
    fscanf(f, "%15s", w); for (int v = 0; v < N; v++) for (int k = 0; k < 2; k++) fscanf(f, "%d", &g->gate[v][k]);
    return 1;
}

static int ST[MAXN]; static int LEV = -1; static int Mbest, Zbest, Tbest, MV[MAXN];
static long evalr(const Gen *g) {
    uint64_t u = 0; for (int v = 0; v < N; v++) u |= (uint64_t)ST[v] << v;
    for (int v = 0; v < N; v++) MV[v] = 0; int T = 0;
    while (T < 100000) { uint64_t w = stepL(g, u); if (w == u) break; for (int v = 0; v < N; v++) MV[v] += (int)(((w ^ u) >> v) & 1); u = w; T++; }
    Mbest = -1; for (int v = 0; v < N; v++) if ((LEV < 0 || v / 2 == LEV) && MV[v] > Mbest) { Mbest = MV[v]; Zbest = v; }
    Tbest = T; return (long)Mbest * 256 + T;
}
static void printgs(FILE *f, const Gen *g) { printg(f, g); fprintf(f, "start"); for (int v = 0; v < N; v++) fprintf(f, " %d", ST[v]); fprintf(f, "\n"); }
static int readgs(FILE *f, Gen *g) { if (!readg(f, g)) return 0; char w[16]; if (fscanf(f, "%15s", w) != 1) return 0; for (int v = 0; v < N; v++) if (fscanf(f, "%d", &ST[v]) != 1) return 0; return 1; }
int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage\n"); return 1; }
    m = atoi(argv[2]); N = 2 * (m + 1); NU = 2 * m; M = 2 * N; if (N > MAXN) { fprintf(stderr, "too big\n"); return 1; }
    LEV = getenv("LEV") ? atoi(getenv("LEV")) : -1; Gen g;
    if (!strcmp(argv[1], "eval")) { if (!readgs(stdin, &g)) { fprintf(stderr, "bad genome\n"); return 1; } evalr(&g);
        printf("T %d best mover %d lev %d moves %d | moves", Tbest, Zbest, Zbest / 2, Mbest); for (int v = 0; v < N; v++) printf(" %d", MV[v]); printf("\n"); return 0; }
    rs = 0x9E3779B97F4A7C15ULL ^ (uint64_t)atoll(argv[3]) * 2654435761ULL; if (!rs) rs = 1; for (int i = 0; i < 10; i++) rnd();
    long iters = atol(argv[4]); const char *out = argv[5];
    FILE *f = fopen(argv[6], "r"); if (!f || !readgs(f, &g)) { fprintf(stderr, "bad seed\n"); return 1; } fclose(f);
    long cs = evalr(&g), best = cs; Gen bg = g; int bst[MAXN]; memcpy(bst, ST, sizeof ST); int cst[MAXN]; memcpy(cst, ST, sizeof ST);
    double T0a = getenv("ANNEAL") ? atof(getenv("ANNEAL")) : 0.0; long stale = 0;
    printf("seed score %ld moves %d mover %d T %d\n", cs, Mbest, Zbest, Tbest); fflush(stdout);
    for (long it = 0; it < iters; it++) {
        Gen h = g; memcpy(ST, cst, sizeof ST); int nm = 1 + rn(3);
        for (int j = 0; j < nm; j++) { if (rn(5) == 0) ST[rn(N)] ^= 1; else mutate(&h); }
        long s = evalr(&h); double temp = T0a * (1.0 - (double)it / iters);
        int acc = s >= cs || (temp > 0 && (double)(rnd() % 1000000) / 1e6 < exp((double)(s - cs) / temp));
        if (acc) { g = h; memcpy(cst, ST, sizeof ST); if (s > cs) stale = 0; cs = s; } else stale++;
        if (cs > best) { best = cs; bg = g; memcpy(bst, cst, sizeof ST); memcpy(ST, bst, sizeof ST); FILE *o = fopen(out, "w"); printgs(o, &bg); fclose(o);
            printf("it %ld moves %ld T %ld\n", it, best / 256, best % 256); fflush(stdout); }
        if (stale > 200000) { g = bg; memcpy(cst, bst, sizeof ST); stale = 0; for (int j = 0; j < 6; j++) mutate(&g); memcpy(ST, cst, sizeof ST); cs = evalr(&g); }
    }
    printf("FINAL best %ld moves %ld T %ld\n", best, best / 256, best % 256); return 0;
}
