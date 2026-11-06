/* L-RED R212 fl.c (derived from fk.c): IDEAL runs of FULL R197 ladders (level 0 moves too; T^R and, with ISO=1, T^R_ISO).
   Genome text format as fk.c ("m" = top level, so d = m + 1 levels, N = 2d movers). Level-0 key = gate; level l >= 1 option k W-points to
   mover 2(l-1)+k. Xi-targets: any mover (ISO=1: not 0, 1), acyclic. T = max over all 2^N starts of the number of steps.
   Validated against r187/ideal.py (xvalfl.py). Original fk.c header follows.
   fk.c: fast T_k / T_inf of L-NEW's external-flip model E_m on ISO R197 2-wide ladders, plus a hill climb.
   Same step rule as L-SI box64 flipdp.py (Ext.step): level 0 frozen to a configuration with bit b = [key(0) < key(1)]; upper movers
   (levels 1..m, two per level, two options each; option k of a level-l mover has W-target mover 2(l-1)+k) are available on their
   current option or a strictly Xi-better one (face = sum of +-2^br along the Xi-chain under the OLD state); each mover takes its
   key-least available option, keys on the NEW state, lowest level first, key = (key(W-target), gate) lexicographic.
   Every output genome is re-checked by flipdp.py (Python, XSIM vs box 150 Gen) and r212/verify.py; this file is only a search tool.
   Usage: fk eval m < genome.txt            (text genome as printed by fk)
          fk climb m K score seed iters out.txt [seed_genome.txt]
          score: 0 = T_K, 1 = T_K - T_0 (per genome), 2 = T_K*64 + (T_K - T_0)
   env ANNEAL=t: simulated annealing, a worse move is accepted with probability exp(-loss / temp), temp falling linearly from t to 0. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <math.h>
#define MAXN 20
int m, N, NU, M;                      /* N movers (levels 0..m), NU = 2m upper movers, M = 2N options */
typedef struct { int xt[MAXN][2]; int br[2*MAXN]; int bp[2*MAXN]; int gate[MAXN][2]; } Gen;
static int lev(int v) { return v / 2; }
static int wt(int v, int k) { return lev(v) > 0 ? 2 * (lev(v) - 1) + k : -1; }
static int64_t eps(const Gen *g, int v, int k) { int o = 2 * v + k; int64_t e = (int64_t)1 << g->br[o]; return g->bp[o] ? -e : e; }
static int64_t face(const Gen *g, const int *st, int v, int k) {
    int64_t t = 0; int guard = 0;
    while (1) { t += eps(g, v, k); int x = g->xt[v][k]; if (x < 0) return t; v = x; k = st[x]; if (++guard > 1000) { fprintf(stderr, "cyc\n"); exit(2); } }
}
static int q0[2][2]; static int ISO = 0;                   /* level-0 config per bit */
static void setq(const Gen *g) {
    int have[2] = {0, 0};
    for (int a = 0; a < 2; a++) for (int c = 0; c < 2; c++) { int b = g->gate[0][a] < g->gate[1][c]; if (!have[b]) { have[b] = 1; q0[b][0] = a; q0[b][1] = c; } }
    if (!have[0] || !have[1]) { fprintf(stderr, "level 0 cannot realise both bits\n"); exit(2); }
}
/* full-ladder step: state bitmask over all N movers */
static uint32_t stepL(const Gen *g, uint32_t up) {
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
    uint32_t r = 0; for (int v = 0; v < N; v++) r |= (uint32_t)ns[v] << v; return r;
}
static uint32_t *NX[2]; static int *TK; static int *TI; static int NS;
/* T[k][u][b] stored at ((k*NS)+u)*2+b; compute via memo recursion along functional graph */
static int KMAX;
static int t0(int u, int b, int depth);
static int tk(int k, uint32_t u, int b) {
    int *p = &TK[((size_t)k * NS + u) * 2 + b];
    if (*p >= 0) return *p;
    if (*p == -2) { fprintf(stderr, "run cycle\n"); exit(3); }
    *p = -2;
    uint32_t w = NX[b][u]; int best = 0;
    if (w != u) best = 1 + tk(k, w, b);
    if (k > 0) { int x = tk(k - 1, u, 1 - b); if (x > best) best = x; }
    *p = best; return best;
}
static int tinf(uint32_t u) {
    int *p = &TI[u]; if (*p >= 0) return *p; if (*p == -2) { fprintf(stderr, "inf cycle\n"); exit(3); }
    *p = -2; int best = 0;
    for (int b = 0; b < 2; b++) { uint32_t w = NX[b][u]; if (w != u) { int x = 1 + tinf(w); if (x > best) best = x; } }
    *p = best; return best;
}
static int Tres[16], Tinf_res; static uint32_t argmax;
static int trun(uint32_t u) {
    int *p = &TK[u]; if (*p >= 0) return *p; if (*p == -2) { fprintf(stderr, "run cycle\n"); exit(3); }
    *p = -2; uint32_t w = NX[0][u]; int r = (w != u) ? 1 + trun(w) : 0; *p = r; return r;
}
static void evalg(const Gen *g, int K) {
    (void)K;
    for (int u = 0; u < NS; u++) NX[0][u] = stepL(g, u);
    for (int u = 0; u < NS; u++) TK[u] = -1;
    int best = 0; for (int u = 0; u < NS; u++) { int x = trun(u); if (x > best) { best = x; argmax = u; } }
    Tres[0] = best; Tinf_res = best;
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
static long score(int mode, int K) { (void)mode; (void)K; return Tres[0]; }
int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage\n"); return 1; }
    m = atoi(argv[2]); N = 2 * (m + 1); NU = 2 * m; M = 2 * N; NS = 1 << N;
    int K = 8; KMAX = K;
    NX[0] = malloc(sizeof(uint32_t) * NS); NX[1] = malloc(sizeof(uint32_t) * NS);
    TK = malloc(sizeof(int) * (size_t)(K + 1) * NS * 2 + 16); TI = malloc(sizeof(int) * NS);
    Gen g;
    ISO = getenv("ISO") && atoi(getenv("ISO"));
    if (!strcmp(argv[1], "eval")) {
        if (!readg(stdin, &g)) { fprintf(stderr, "bad genome\n"); return 1; }
        if (ISO) for (int v = 0; v < N; v++) for (int k = 0; k < 2; k++) if (g.xt[v][k] == 0 || g.xt[v][k] == 1) { printf("NOT ISO\n"); return 1; }
        evalg(&g, K); printf("T %d start", Tres[0]); for (int v = 0; v < N; v++) printf("%d", (argmax >> v) & 1); printf("\n"); return 0;
    }
    int Kc = atoi(argv[3]), mode = atoi(argv[4]); rs = 0x9E3779B97F4A7C15ULL ^ (uint64_t)atoll(argv[5]) * 2654435761ULL; if (!rs) rs = 1;
    long iters = atol(argv[6]); const char *out = argv[7];
    for (int i = 0; i < 10; i++) rnd();
    if (argc > 8) { FILE *f = fopen(argv[8], "r"); if (!f || !readg(f, &g)) { fprintf(stderr, "bad seed\n"); return 1; } fclose(f); }
    else { do randg(&g); while (!bothbits(&g)); }
    evalg(&g, Kc); long cs = score(mode, Kc), best = cs; Gen bg = g;
    long stale = 0; double T0a = getenv("ANNEAL") ? atof(getenv("ANNEAL")) : 0.0;
    for (long it = 0; it < iters; it++) {
        Gen h = g; int nm = 1 + rn(3); for (int j = 0; j < nm; j++) mutate(&h);
        evalg(&h, Kc); long s = score(mode, Kc);
        double temp = T0a * (1.0 - (double)it / iters);
        int acc = s >= cs || (temp > 0 && (double)(rnd() % 1000000) / 1e6 < exp((double)(s - cs) / temp));
        if (acc) { g = h; if (s > cs) stale = 0; cs = s; } else stale++;
        if (cs > best) {
            best = cs; bg = g; FILE *f = fopen(out, "w"); printg(f, &bg); fclose(f);
            printf("it %ld T %ld\n", it, best); fflush(stdout);
        }
        if (stale > 200000) { g = bg; cs = best; stale = 0; for (int j = 0; j < 6; j++) mutate(&g); evalg(&g, Kc); cs = score(mode, Kc); }
    }
    printf("FINAL best %ld\n", best); return 0;
}
