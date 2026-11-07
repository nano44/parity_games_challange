/* L-NEW box 185 mv.c: moves per mover on full 2-wide R197 ladders (RESULTS R110's L^R_d: movers 2l, 2l+1 on level l, option k of a
   level-l mover W-points to 2(l-1)+k), IDEAL step of RESULTS R104 (Xi-availability on the OLD state, key-least on the NEW state, lowest
   level first). Step function copied from L-RED R212 fl.c (claude/l-red experiments/red/r212/fl.c, stepL), validated there against
   r187/ideal.py; this file re-validates against L-NEW box150/check.py Gen through xval.py.
   Text genome format = fl.c's ("m" = top level; d = m + 1 levels; N = 2d movers).
   Usage: mv eval m < g.txt        per-level max moves of Xi-targets (levmax) and of all movers (levall), longest run of CONSECUTIVE
                                   steps moving one Xi-target (levdense), all 2^N starts; REDUCE check; TRACE=1 prints the arg-max run
          mv opt m x < g.txt     exhaustive re-wiring of mover x's two options (Xi-targets, ranks, parities): max moves(x)
          mv climb m LEV seed iters out.txt [seed.txt]   maximise max moves of a Xi-target mover of level LEV (LEV -1: any level),
                                                         tie-break by the run length; env FAM=W restricts Xi-targets to W-targets or X;
                                                         env ANNEAL=t: simulated annealing (score unit: 256 per move); env ANYZ=1: score every mover, Xi-target or not. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <math.h>
#define MAXN 22
int m, N, M, NS;
typedef struct { int xt[MAXN][2]; int br[2*MAXN]; int bp[2*MAXN]; int gate[MAXN][2]; } Gen;
static int lev(int v) { return v / 2; }
static int64_t eps(const Gen *g, int v, int k) { int o = 2 * v + k; int64_t e = (int64_t)1 << g->br[o]; return g->bp[o] ? -e : e; }
static int64_t face(const Gen *g, const int *st, int v, int k) {
    int64_t t = 0; int guard = 0;
    while (1) { t += eps(g, v, k); int x = g->xt[v][k]; if (x < 0) return t; v = x; k = st[x]; if (++guard > 1000) { fprintf(stderr, "cyc\n"); exit(2); } }
}
static int ltglob[MAXN];
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
        int a = 2 * l, c = 2 * l + 1, wa = 2 * (l - 1) + ns[a], wc = 2 * (l - 1) + ns[c];
        int alt = (wa != wc) ? lt[wa] : (g->gate[a][ns[a]] < g->gate[c][ns[c]]);
        lt[a] = alt; lt[c] = !alt;
    }
    for (int v = 0; v < N; v++) ltglob[v] = lt[v];
    uint32_t r = 0; for (int v = 0; v < N; v++) r |= (uint32_t)ns[v] << v; return r;
}
static uint32_t *NX; static int *TL, *MZ, *DZ; static int levdense[MAXN]; static int isT[MAXN];
static int trun(uint32_t u) {
    int *p = &TL[u]; if (*p >= 0) return *p; if (*p == -2) { fprintf(stderr, "run cycle\n"); exit(3); }
    *p = -2; uint32_t w = NX[u]; int r = (w != u) ? 1 + trun(w) : 0; *p = r; return r;
}
static int *ord;
static int best, bz, bT; static uint32_t barg; static int LEV = -1; static int levmax[MAXN], levall[MAXN]; static int ANYZ = 0;
static void evalg(const Gen *g) {
    for (int u = 0; u < NS; u++) { NX[u] = stepL(g, u); TL[u] = -1; }
    for (int u = 0; u < NS; u++) trun(u);
    for (int z = 0; z < N; z++) isT[z] = 0;
    for (int v = 0; v < N; v++) for (int k = 0; k < 2; k++) if (g->xt[v][k] >= 0) isT[g->xt[v][k]] = 1;
    int cnt[130] = {0}; for (int u = 0; u < NS; u++) cnt[TL[u] + 1]++;
    for (int i = 1; i < 130; i++) cnt[i] += cnt[i - 1];
    for (int u = 0; u < NS; u++) ord[cnt[TL[u]]++] = u;
    best = -1; for (int l = 0; l <= m; l++) levmax[l] = levall[l] = levdense[l] = 0;
    for (int i = 0; i < NS; i++) { uint32_t u = ord[i], w = NX[u];
        for (int z = 0; z < N; z++) { int r = 0, dz = 0; if (w != u) { r = (int)(((w ^ u) >> z) & 1) + MZ[(size_t)w * N + z]; dz = (((w ^ u) >> z) & 1) ? 1 + DZ[(size_t)w * N + z] : 0; }
            MZ[(size_t)u * N + z] = r; DZ[(size_t)u * N + z] = dz; if (isT[z] && dz > levdense[lev(z)]) levdense[lev(z)] = dz;
            if (isT[z] && r > levmax[lev(z)]) levmax[lev(z)] = r;
            if (r > levall[lev(z)]) levall[lev(z)] = r;
            if ((isT[z] || ANYZ) && (LEV < 0 || lev(z) == LEV) && (r > best || (r == best && TL[u] > bT))) { best = r; bz = z; bT = TL[u]; barg = u; } } }
}
static int reach(const Gen *g, int from, int to) {
    int stk[MAXN], sp = 0, seen[MAXN] = {0}; stk[sp++] = from; seen[from] = 1;
    while (sp) { int v = stk[--sp]; if (v == to) return 1; for (int k = 0; k < 2; k++) { int x = g->xt[v][k]; if (x >= 0 && !seen[x]) { seen[x] = 1; stk[sp++] = x; } } }
    return 0;
}
static uint64_t rs; static uint64_t rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
static int rn(int n) { return (int)(rnd() % (uint64_t)n); }
static int FAMW = 0;
static int pick_target(const Gen *g, int v, int k) {
    if (FAMW) { if (lev(v) == 0 || rn(4) == 0) return -1; return 2 * (lev(v) - 1) + k; }
    int t = rn(N + 1); if (t == N) t = -1; return t;
}
static int bothbits(const Gen *g) { int h[2] = {0, 0}; for (int a = 0; a < 2; a++) for (int c = 0; c < 2; c++) h[g->gate[0][a] < g->gate[1][c]] = 1; return h[0] && h[1]; }
static void randg(Gen *g) {
    for (int v = 0; v < N; v++) for (int k = 0; k < 2; k++) g->xt[v][k] = -1;
    for (int v = 0; v < N; v++) for (int k = 0; k < 2; k++) { int t = pick_target(g, v, k); if (t == v || (t >= 0 && reach(g, t, v))) t = -1; g->xt[v][k] = t; }
    for (int i = 0; i < M; i++) g->br[i] = i;
    for (int i = M - 1; i > 0; i--) { int j = rn(i + 1); int t = g->br[i]; g->br[i] = g->br[j]; g->br[j] = t; }
    for (int i = 0; i < M; i++) g->bp[i] = rn(2);
    int gp[2 * MAXN]; for (int i = 0; i < M; i++) gp[i] = i;
    for (int i = M - 1; i > 0; i--) { int j = rn(i + 1); int t = gp[i]; gp[i] = gp[j]; gp[j] = t; }
    for (int v = 0; v < N; v++) { g->gate[v][0] = gp[2 * v]; g->gate[v][1] = gp[2 * v + 1]; }
}
static void mutate(Gen *g) {
    int r = rn(100);
    if (r < 30) { for (int tries = 0; tries < 50; tries++) {
            int v = rn(N), k = rn(2), t = pick_target(g, v, k);
            if (t == v) continue; int old = g->xt[v][k]; g->xt[v][k] = -1;
            if (t >= 0 && reach(g, t, v)) { g->xt[v][k] = old; continue; }
            g->xt[v][k] = t; return; } }
    else if (r < 60) { int i = rn(M), j = rn(M); int t = g->br[i]; g->br[i] = g->br[j]; g->br[j] = t; }
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
    if (fscanf(f, "%15s", w) != 1) return 0; for (int v = 0; v < N; v++) for (int k = 0; k < 2; k++) if (fscanf(f, "%d", &g->xt[v][k]) != 1) return 0;
    if (fscanf(f, "%15s", w) != 1) return 0; for (int i = 0; i < M; i++) if (fscanf(f, "%d", &g->br[i]) != 1) return 0;
    if (fscanf(f, "%15s", w) != 1) return 0; for (int i = 0; i < M; i++) if (fscanf(f, "%d", &g->bp[i]) != 1) return 0;
    if (fscanf(f, "%15s", w) != 1) return 0; for (int v = 0; v < N; v++) for (int k = 0; k < 2; k++) if (fscanf(f, "%d", &g->gate[v][k]) != 1) return 0;
    return 1;
}
int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage\n"); return 1; }
    m = atoi(argv[2]); N = 2 * (m + 1); M = 2 * N; NS = 1 << N;
    NX = malloc(sizeof(uint32_t) * NS); TL = malloc(sizeof(int) * NS); ord = malloc(sizeof(int) * NS);
    MZ = malloc(sizeof(int) * (size_t)NS * N); DZ = malloc(sizeof(int) * (size_t)NS * N);
    FAMW = getenv("FAM") && !strcmp(getenv("FAM"), "W"); ANYZ = getenv("ANYZ") && atoi(getenv("ANYZ"));
    Gen g;
    if (!strcmp(argv[1], "eval")) {
        if (!readg(stdin, &g)) { fprintf(stderr, "bad genome\n"); return 1; }
        evalg(&g);
        int Tmax = 0; for (int u = 0; u < NS; u++) if (TL[u] > Tmax) Tmax = TL[u];
        /* REDUCE: every run, T <= 1 + #{steps moving a Xi-target mover} */
        long viol = 0; int slackmin = 1 << 30;
        for (int u = 0; u < NS; u++) { int T = TL[u], c = 0; uint32_t s = u;
            for (int t = 0; t < T; t++) { uint32_t w = NX[s], d = w ^ s; int hit = 0; for (int z = 0; z < N; z++) if (isT[z] && ((d >> z) & 1)) hit = 1; c += hit; s = w; }
            if (T > 1 + c) viol++; if (T >= 1 && 1 + c - T < slackmin) slackmin = 1 + c - T; }
        printf("d %d Tmax %d maxmoves %d z %d lev %d runT %d start ", m + 1, Tmax, best, bz, lev(bz), bT);
        for (int v = 0; v < N; v++) printf("%d", (barg >> v) & 1);
        printf(" levmax"); for (int l = 0; l <= m; l++) printf(" %d", levmax[l]);
        printf(" levall"); for (int l = 0; l <= m; l++) printf(" %d", levall[l]);
        printf(" levdense"); for (int l = 0; l <= m; l++) printf(" %d", levdense[l]);
        printf(" REDUCE_viol %ld minslack %d\n", viol, slackmin);
        if (getenv("TRACE")) { uint32_t s = barg; int T = TL[barg];
            for (int t = 0; t <= T; t++) { printf("  t %2d ", t); for (int v = 0; v < N; v++) printf("%d", (s >> v) & 1); printf("\n"); s = NX[s]; } }
        return 0;
    }
    if (!strcmp(argv[1], "opt")) { /* exhaustive re-wiring of ONE mover x: both Xi-targets (X or any mover, acyclic), both ranks
           (re-inserted at every pair of positions among the other ranks), both parities; score = max over starts of moves(x) */
        int x = atoi(argv[3]); if (!readg(stdin, &g)) { fprintf(stderr, "bad genome\n"); return 1; }
        int others[2 * MAXN], no = 0; for (int i = 0; i < M; i++) if (i != 2 * x && i != 2 * x + 1) others[no++] = i;
        /* order others by rank */
        for (int i = 0; i < no; i++) for (int j = i + 1; j < no; j++) if (g.br[others[j]] < g.br[others[i]]) { int t = others[i]; others[i] = others[j]; others[j] = t; }
        int bestx = -1; Gen bg = g; long nev = 0;
        for (int t0 = -1; t0 < N; t0++) for (int t1 = -1; t1 < N; t1++) {
            if (t0 == x || t1 == x) continue; g.xt[x][0] = -1; g.xt[x][1] = -1;
            if ((t0 >= 0 && reach(&g, t0, x)) || (t1 >= 0 && reach(&g, t1, x))) continue;
            g.xt[x][0] = t0; g.xt[x][1] = t1;
            for (int r0 = 0; r0 < M; r0++) for (int r1 = 0; r1 < M; r1++) { if (r0 == r1) continue;
                int k = 0; for (int r = 0; r < M; r++) { if (r == r0) g.br[2 * x] = r; else if (r == r1) g.br[2 * x + 1] = r; else g.br[others[k++]] = r; }
                for (int pp = 0; pp < 4; pp++) { g.bp[2 * x] = pp & 1; g.bp[2 * x + 1] = pp >> 1;
                    LEV = -2; evalg(&g); nev++;
                    int mx = 0; for (int u = 0; u < NS; u++) { int r = MZ[(size_t)u * N + x]; if (r > mx) mx = r; }
                    if (mx > bestx) { bestx = mx; bg = g; printf("moves(x) %d xt %d %d r %d %d p %d isT %d\n", mx, t0, t1, r0, r1, pp, isT[x]); fflush(stdout); } } } }
        printf("FINAL x %d best %d evals %ld\n", x, bestx, nev); printg(stdout, &bg); return 0;
    }
    LEV = atoi(argv[3]); rs = 0x9E3779B97F4A7C15ULL ^ (uint64_t)atoll(argv[4]) * 2654435761ULL; if (!rs) rs = 1;
    long iters = atol(argv[5]); const char *out = argv[6];
    for (int i = 0; i < 10; i++) rnd();
    if (argc > 7) { FILE *f = fopen(argv[7], "r"); if (!f || !readg(f, &g)) { fprintf(stderr, "bad seed\n"); return 1; } fclose(f); }
    else { do randg(&g); while (!bothbits(&g)); }
    evalg(&g); long cs = (long)best * 256 + bT, bs = cs; Gen bg = g; long stale = 0; double T0a = getenv("ANNEAL") ? atof(getenv("ANNEAL")) : 0.0;
    for (long it = 0; it < iters; it++) {
        Gen h = g; int nm = 1 + rn(3); for (int j = 0; j < nm; j++) mutate(&h);
        evalg(&h); long s = (long)best * 256 + bT;
        double temp = T0a * (1.0 - (double)it / iters);
        if (s >= cs || (temp > 0 && (double)(rnd() % 1000000) / 1e6 < exp((double)(s - cs) / temp))) { g = h; if (s > cs) stale = 0; cs = s; } else stale++;
        if (cs > bs) { bs = cs; bg = g; FILE *f = fopen(out, "w"); printg(f, &bg); fclose(f);
            printf("it %ld moves %ld runT %ld\n", it, bs / 256, bs % 256); fflush(stdout); }
        if (stale > 20000) { g = bg; stale = 0; for (int j = 0; j < 8; j++) mutate(&g); evalg(&g); cs = (long)best * 256 + bT; }
    }
    printf("FINAL moves %ld runT %ld\n", bs / 256, bs % 256); return 0;
}
