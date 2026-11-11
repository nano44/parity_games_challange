/* L-COMP box 38 (= box36/fast36.c + T3 argmax in block mode; nothing else changed) item 2(a): FAST N5'-xi-on-Gamma3 engine with per-gate flip census.
   A line-by-line C port of L-COMP's own Python engine (experiments/comp/box34/own34.py: build, run; n5b.py SpecSI.evaluate_choice;
   pgsolver_si.py SI: rel, reward, rew, nvo, initial_strategy_by_best_reward) and of box36/own36.py census (flips, lamch).
   Used for counts only after validation against own34/own36 and L-NEW asc197/gflip202 (box36/val36.py).
   Bitsets of W 64-bit words (compile with -DW=1 for n <= 64, -DW=8 for n <= 512).
   Valuations: (L, P, k); P stored over RELEVANCE RANK bits (rank = position in ascending (prio, index)), so the most relevant
   element of a set is its highest bit.
   Modes:
     fast36 one            < genome.txt   -> "T3 <t> fb <0|1>" then one line "gate x k flips lamch" per gate in (x, k) order
     fast36 block N M lev.. D.. xts..      -> one JSON object: block stats as sweep36.merge (same tie rules)
   genome.txt: N M / lev[N] / per option in option order: x wt xt b gate / br[M] / bp[M] / start[N]. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#ifndef W
#define W 1
#endif
#define NMAX (64 * W)
typedef uint64_t u64;
typedef struct { u64 w[W]; } BS;
static inline void bz(BS *a) { memset(a, 0, sizeof *a); }
static inline void bset(BS *a, int i) { a->w[i >> 6] |= 1ULL << (i & 63); }
static inline void bclr(BS *a, int i) { a->w[i >> 6] &= ~(1ULL << (i & 63)); }
static inline int btest(const BS *a, int i) { return (a->w[i >> 6] >> (i & 63)) & 1; }
static inline int bany(const BS *a) { for (int j = 0; j < W; j++) if (a->w[j]) return 1; return 0; }
static inline int beq(const BS *a, const BS *b) { for (int j = 0; j < W; j++) if (a->w[j] != b->w[j]) return 0; return 1; }
static inline BS band(BS a, BS b) { for (int j = 0; j < W; j++) a.w[j] &= b.w[j]; return a; }
static inline BS bandn(BS a, BS b) { for (int j = 0; j < W; j++) a.w[j] &= ~b.w[j]; return a; }
static inline BS bxor(BS a, BS b) { for (int j = 0; j < W; j++) a.w[j] ^= b.w[j]; return a; }
static inline int bhi(const BS *a) { for (int j = W - 1; j >= 0; j--) if (a->w[j]) return 64 * j + 63 - __builtin_clzll(a->w[j]); return -1; }
static inline int bcount(const BS *a) { int c = 0; for (int j = 0; j < W; j++) c += __builtin_popcountll(a->w[j]); return c; }
/* iterate set bits ascending */
#define FORBITS(bs, var) for (int _j = 0; _j < W; _j++) for (u64 _m = (bs).w[_j]; _m; _m &= _m - 1) for (int var = 64 * _j + __builtin_ctzll(_m), _once = 1; _once; _once = 0)

typedef struct { int L; BS P; int k; } Val;
typedef struct { int n; int pr[NMAX]; int pl[NMAX]; BS succ[NMAX]; int asc[NMAX]; } Game;

static int n_g, rk[NMAX], vrk[NMAX];        /* relevance rank of the current Gamma3 (shared by g, dual, restrictions) */

static inline int cmpi(int a, int b) { return (a > b) - (a < b); }
static inline int reward(int p) { return (p % 2 != 0 && p >= 0) ? -p : p; }      /* player EVEN */
static inline int rew(const Game *G, int i, int j) {
    int ri = reward(G->pr[i]), rj = reward(G->pr[j]);
    if (ri != rj) return ri < rj ? -1 : 1;
    return (ri % 2 == 0) ? cmpi(i, j) : cmpi(j, i);
}
static int nvo(const Game *G, const Val *a, const Val *b) {
    int c = rew(G, a->L, b->L);
    if (c) return c;
    BS r = bxor(a->P, b->P);
    if (bany(&r)) {
        int wr = bhi(&r), w = vrk[wr];
        return ((G->pr[w] % 2 == 0 && btest(&b->P, wr)) || (G->pr[w] % 2 == 1 && btest(&a->P, wr))) ? -1 : 1;
    }
    if (a->k == b->k) return 0;
    int v = b->L;
    return ((G->pr[v] % 2 == 1 && a->k < b->k) || (G->pr[v] % 2 == 0 && a->k > b->k)) ? -1 : 1;
}
static const Game *SG_;
static int asc_cmp(const void *x, const void *y) {
    int i = *(const int *)x, j = *(const int *)y;
    int ri = reward(SG_->pr[i]), rj = reward(SG_->pr[j]);
    if (ri != rj) return ri < rj ? -1 : 1;
    int ki = (ri % 2 == 0) ? i : -i, kj = (rj % 2 == 0) ? j : -j;
    return cmpi(ki, kj);
}
static void prep(Game *G) {
    for (int i = 0; i < G->n; i++) G->asc[i] = i;
    SG_ = G; qsort(G->asc, G->n, sizeof(int), asc_cmp);
}
static void mkdual(const Game *g, Game *d, const BS *succ) {
    d->n = g->n;
    for (int i = 0; i < g->n; i++) { d->pr[i] = g->pr[i] + 1; d->pl[i] = 1 - g->pl[i]; d->succ[i] = succ ? succ[i] : g->succ[i]; }
    prep(d);
}
static void mkrestrict(const Game *g, Game *h, const BS *A) {
    h->n = g->n;
    for (int i = 0; i < g->n; i++) { h->pr[i] = g->pr[i]; h->pl[i] = g->pl[i]; h->succ[i] = A[i]; }
    memcpy(h->asc, g->asc, sizeof(int) * g->n);
}

/* SpecSI.evaluate_choice */
static BS hs[NMAX], hp[NMAX];
static int gd_cache[NMAX], gd_has[NMAX], *gd_choice, gd_v;
static int get_dist(int x) {
    if (gd_has[x]) return gd_cache[x];
    int best = -1, bw = -1, any = 0;
    FORBITS(hs[x], y) { int dy = get_dist(y); if (!any || dy > best) { best = dy; bw = y; any = 1; } }
    if (!any) { fprintf(stderr, "get_dist: empty hs\n"); exit(3); }
    gd_has[x] = 1; gd_cache[x] = 1 + best; gd_choice[x] = bw;
    return gd_cache[x];
}
static BS reach(int start, int excl) {
    BS s; bz(&s); static int st[NMAX * 16]; int sp = 0;
    st[sp++] = start;
    while (sp) {
        int x = st[--sp];
        if (btest(&s, x)) continue;
        bset(&s, x);
        FORBITS(hp[x], y) if (y != excl && !btest(&s, y)) { if (sp < NMAX * 16) st[sp++] = y; else { fprintf(stderr, "stack\n"); exit(3); } }
    }
    return s;
}
static inline void del_other(int x, const BS *m) {
    BS d = bandn(hs[x], *m);
    FORBITS(d, y) { bclr(&hs[x], y); bclr(&hp[y], x); }
}
static void evaluate_choice(const Game *G, const int *strat, Val *valu, int *choice) {
    int n = G->n; static BS gs[NMAX], gp[NMAX]; BS alive; bz(&alive);
    for (int i = 0; i < n; i++) { bz(&gp[i]); }
    for (int i = 0; i < n; i++) {
        if (strat[i] == -1) gs[i] = G->succ[i]; else { bz(&gs[i]); bset(&gs[i], strat[i]); }
        bset(&alive, i);
    }
    for (int i = 0; i < n; i++) FORBITS(gs[i], j) bset(&gp[j], i);
    int assigned[NMAX]; memset(assigned, 0, sizeof(int) * n);
    for (int i = 0; i < n; i++) { choice[i] = -1; valu[i].L = -1; bz(&valu[i].P); valu[i].k = 0; }
    int stack[NMAX], parent[NMAX], dist[NMAX];
    for (int ai = 0; ai < n; ai++) {
        int v = G->asc[ai];
        if (assigned[v] || !btest(&alive, v)) continue;
        int sp = 0, found = -1; BS vis; bz(&vis);
        stack[sp++] = v; bset(&vis, v);
        while (sp && found < 0) {
            int x = stack[--sp];
            FORBITS(gs[x], y) {
                if (found >= 0) break;
                if (y == v) { found = x; break; }
                if (!btest(&vis, y) && btest(&alive, y) && rk[y] < rk[v]) { bset(&vis, y); parent[y] = x; stack[sp++] = y; }
            }
        }
        if (found < 0) continue;
        int cyc = found;
        while (cyc != v && parent[cyc] != v) cyc = parent[cyc];
        if (found == v) cyc = v;
        /* nodes: backward closure from v */
        BS nodes; bz(&nodes); sp = 0; stack[sp++] = v;
        static int st2[NMAX * 16]; int sp2 = 0; st2[sp2++] = v;
        while (sp2) {
            int w = st2[--sp2];
            if (btest(&nodes, w)) continue;
            bset(&nodes, w);
            FORBITS(gp[w], u) if (!btest(&nodes, u)) { if (sp2 >= NMAX * 16) { fprintf(stderr, "stack2\n"); exit(3); } st2[sp2++] = u; }
        }
        static BS paths[NMAX];
        int order[NMAX], no = 0;
        FORBITS(nodes, w) { hs[w] = band(gs[w], nodes); hp[w] = band(gp[w], nodes); bz(&paths[w]); }
        for (int r = n - 1; r >= 0; r--) { int u = vrk[r]; if (btest(&nodes, u)) order[no++] = u; }
        for (int oi = 0; oi < no; oi++) {
            int u = order[oi];
            if (rk[u] > rk[v]) {
                if (G->pr[u] % 2 == 0) {
                    BS m = reach(v, u);
                    BS out = bandn(nodes, m);
                    FORBITS(out, q) bset(&paths[q], rk[u]);
                    del_other(u, &m);
                    FORBITS(m, q) del_other(q, &m);
                } else {
                    BS m = reach(u, v);
                    FORBITS(m, q) bset(&paths[q], rk[u]);
                    FORBITS(m, x) if (x != u) del_other(x, &m);
                }
            }
        }
        FORBITS(nodes, w) dist[w] = 0;
        if (G->pr[v] % 2 == 0) {
            FORBITS(nodes, w) gd_has[w] = 0;
            gd_has[v] = 1; gd_cache[v] = 0; gd_choice = choice; gd_v = v;
            FORBITS(nodes, x) dist[x] = get_dist(x);
        } else {
            int q[NMAX], qh = 0, qt = 0; BS disc; bz(&disc); bset(&disc, v); q[qt++] = v;
            while (qh < qt) {
                int y = q[qh++];
                FORBITS(hp[y], x) if (!btest(&disc, x)) { bset(&disc, x); dist[x] = dist[y] + 1; choice[x] = y; q[qt++] = x; }
            }
        }
        choice[v] = cyc;
        FORBITS(nodes, u) { valu[u].L = v; valu[u].P = paths[u]; valu[u].k = dist[u]; assigned[u] = 1; }
        alive = bandn(alive, nodes);
        FORBITS(alive, y) { gs[y] = bandn(gs[y], nodes); gp[y] = bandn(gp[y], nodes); }
    }
    for (int v = 0; v < n; v++) if (G->pl[v] != 1) choice[v] = -1;
}

static void initial_best_reward(const Game *G, int *s) {
    for (int i = 0; i < G->n; i++) {
        if (G->pl[i] == 1) { s[i] = -1; continue; }
        int acc = -1;
        FORBITS(G->succ[i], x) { if (acc < 0) acc = x; if (rew(G, acc, x) <= 0) acc = x; }
        s[i] = acc;
    }
}

/* ---------------- genome and Gamma3 (own34.build) ---------------- */
#define MMAX NMAX
typedef struct { int N, M, lev[MMAX], own[MMAX], wt[MMAX], xt[MMAX], bi[MMAX], gate[MMAX], br[MMAX], bp[MMAX], start[MMAX], kof[MMAX]; } Genome;
/* option q = global option-order position; own[q] = mover, kof[q] = its index k among x's options */
static int VX[MMAX], Vg[MMAX], Vb[MMAX], Ve[MMAX], VcX, VcW, VK[4], VpA, Vs, Vq, Vr, Vpe[MMAX], VpB[MMAX], Vpb[MMAX], Vm[MMAX];
static int ELEV = 1, CTRL = 0;   /* CTRL 1 (control): [N5XI] rule off = plain SPEC S4a; must make val36 fire */
static int gcmp_key[MMAX], ecmp_lev[MMAX];
static int cmp_gate(const void *a, const void *b) { return cmpi(gcmp_key[*(const int *)a], gcmp_key[*(const int *)b]); }
static int cmp_e(const void *a, const void *b) {
    int x = *(const int *)a, y = *(const int *)b;
    if (ELEV && ecmp_lev[x] != ecmp_lev[y]) return cmpi(ecmp_lev[x], ecmp_lev[y]);
    return cmpi(gcmp_key[x], gcmp_key[y]);
}
static void build(const Genome *G, Game *g) {
    int N = G->N, M = G->M, byg[MMAX], eo[MMAX], i = 0;
    for (int q = 0; q < M; q++) { byg[q] = q; eo[q] = q; gcmp_key[q] = G->gate[q]; ecmp_lev[q] = G->lev[G->own[q]]; }
    qsort(byg, M, sizeof(int), cmp_gate);
    qsort(eo, M, sizeof(int), cmp_e);
    for (int x = 0; x < N; x++) VX[x] = i++;
    for (int j = 0; j < M; j++) Vg[byg[j]] = i++;
    for (int q = 0; q < M; q++) Vb[q] = i++;
    for (int j = 0; j < M; j++) Ve[byg[j]] = i++;
    VcX = i++; VcW = i++;
    for (int j = 0; j < 4; j++) VK[j] = i++;
    VpA = i++; Vs = i++; Vq = i++; Vr = i++;
    for (int j = 0; j < M; j++) Vpe[byg[j]] = i++;
    for (int j = 0; j < M; j++) VpB[byg[j]] = i++;
    for (int q = 0; q < M; q++) Vpb[q] = i++;
    for (int j = 0; j < M; j++) Vm[byg[j]] = i++;
    int n = i;
    if (n > NMAX) { fprintf(stderr, "n %d > NMAX %d\n", n, NMAX); exit(2); }
    g->n = n;
    for (int v = 0; v < n; v++) { g->pr[v] = 0; g->pl[v] = 0; bz(&g->succ[v]); }
    for (int q = 0; q < M; q++) g->pr[Vb[q]] = 6 + 2 * G->br[G->bi[q]] + G->bp[G->bi[q]];
    int eb = 0;
    for (int q = 0; q < M; q++) if (g->pr[Vb[q]] > eb) eb = g->pr[Vb[q]];
    eb += 1; eb += eb % 2;
    for (int j = 0; j < M; j++) g->pr[Ve[eo[j]]] = eb + 2 * j;
    g->pr[VcX] = 2;
    int top = 0;
    for (int v = 0; v < n; v++) if (g->pr[v] > top) top = g->pr[v];
    top += 2; top += top % 2;
    g->pr[VcW] = top; g->pr[VK[0]] = top + 2; g->pr[VK[1]] = 5; g->pr[VK[2]] = 3; g->pr[VK[3]] = top + 3; g->pl[VK[2]] = 1;
    for (int q = 0; q < M; q++) bset(&g->succ[VX[G->own[q]]], Vm[q]);
    for (int q = 0; q < M; q++) {
        int gv = Vg[q];
        g->pl[gv] = 1; g->pr[gv] = 1; bset(&g->succ[gv], Vpe[q]); bset(&g->succ[gv], VpB[q]);
        bset(&g->succ[Vpe[q]], Ve[q]); g->pr[Vpe[q]] = 1;
        bset(&g->succ[VpB[q]], Vb[q]); g->pr[VpB[q]] = 0;
        if (G->xt[q] >= 0) bset(&g->succ[Vb[q]], VX[G->xt[q]]);
        bset(&g->succ[Vb[q]], Vpb[q]);
        bset(&g->succ[Vpb[q]], VK[0]); g->pr[Vpb[q]] = 1;
        bset(&g->succ[Ve[q]], G->wt[q] >= 0 ? VX[G->wt[q]] : VcW);
        bset(&g->succ[Vm[q]], gv); g->pr[Vm[q]] = (G->start[G->own[q]] == G->kof[q]) ? 2 : 0;
    }
    bset(&g->succ[VcX], VcX); bset(&g->succ[VcW], VcW);
    bset(&g->succ[VK[0]], VK[1]); bset(&g->succ[VK[0]], VpA); bset(&g->succ[VpA], VK[3]); g->pr[VpA] = 0;
    bset(&g->succ[VK[1]], Vq); bset(&g->succ[VK[1]], Vs); bset(&g->succ[Vq], VK[0]); g->pr[Vq] = 1;
    bset(&g->succ[Vs], VK[1]); g->pr[Vs] = 0;
    bset(&g->succ[VK[2]], Vr); bset(&g->succ[VK[2]], VK[2]); bset(&g->succ[Vr], VK[1]); g->pr[Vr] = 0;
    bset(&g->succ[VK[3]], VK[1]); bset(&g->succ[VK[3]], VK[2]);
    prep(g);
    /* relevance rank: ascending (prio, index) */
    int ord[NMAX];
    for (int v = 0; v < n; v++) ord[v] = v;
    for (int a = 1; a < n; a++) { int t = ord[a], b = a - 1; while (b >= 0 && (g->pr[ord[b]] > g->pr[t] || (g->pr[ord[b]] == g->pr[t] && ord[b] > t))) { ord[b + 1] = ord[b]; b--; } ord[b + 1] = t; }
    for (int r = 0; r < n; r++) { rk[ord[r]] = r; vrk[r] = ord[r]; }
    n_g = n;
}

/* ---------------- run (own34.run) + census (own36) ---------------- */
typedef struct { int T3, fb, capped, C, flips[MMAX], lamch[MMAX], chpe[MMAX], chpb[MMAX], lpe[MMAX], lpb[MMAX]; } Res;
/* ch_f = #t with Omega_t(f) != Omega_(t-1)(f) (full value), lam_f = #t with Lambda change at f, f in {pe_g, pB_g}; nl_f = ch_f - lam_f
   (L-SI box 93 (d), claude/l-si f723957b docs/si/box93-k7k6.md §2 (d)). */
/* C (own34.counters 'C', box 198 §1): for every vertex v and maximal interval of states with Lambda_t(v) constant, c_y = #changes of
   E_t(v) = e-vertices of P_t(v) whose top (most relevant vertex of the symmetric difference) is y; C = max c_y over (v, interval, y). */
static int *ccnt = NULL, ccap = 0, ej[NMAX];
static BS emask;
static int CAP = 20000;
static Val vs[NMAX], vt[NMAX], Wst[NMAX], prev_vs[NMAX], tmpv[NMAX];
static void run(const Genome *Gn, Res *R) {
    static Game g, d, hg, dh, h3; int n, M = Gn->M;
    build(Gn, &g); n = g.n; mkdual(&g, &d, NULL);
    int sigma[NMAX], tau[NMAX], sig2[NMAX], tau2[NMAX], sbar[NMAX], prev_sbar[NMAX], ch[NMAX], dummy[NMAX];
    initial_best_reward(&g, sigma); initial_best_reward(&d, tau);
    for (int q = 0; q < M; q++) { R->flips[q] = 0; R->lamch[q] = 0; R->chpe[q] = R->chpb[q] = R->lpe[q] = R->lpb[q] = 0; }
    R->C = 0; bz(&emask);
    for (int q = 0; q < M; q++) { bset(&emask, rk[Ve[q]]); ej[rk[Ve[q]]] = q; }
    if (ccap < n * M) { ccap = n * M; ccnt = realloc(ccnt, sizeof(int) * ccap); }
    memset(ccnt, 0, sizeof(int) * n * M);
    int it = 0; R->capped = 0;
    static BS A[NMAX], Is[NMAX], It[NMAX];
    for (;;) {
        evaluate_choice(&g, sigma, vs, sbar);
        evaluate_choice(&d, tau, vt, dummy);
        if (it > 0) for (int q = 0; q < M; q++) {
            int gv = Vg[q], pe = Vpe[q], pb = VpB[q];
            R->flips[q] += prev_sbar[gv] != sbar[gv];
            R->lamch[q] += (prev_vs[pe].L != vs[pe].L) || (prev_vs[pb].L != vs[pb].L);
            R->lpe[q] += prev_vs[pe].L != vs[pe].L; R->lpb[q] += prev_vs[pb].L != vs[pb].L;
            R->chpe[q] += !(prev_vs[pe].L == vs[pe].L && prev_vs[pe].k == vs[pe].k && beq(&prev_vs[pe].P, &vs[pe].P));
            R->chpb[q] += !(prev_vs[pb].L == vs[pb].L && prev_vs[pb].k == vs[pb].k && beq(&prev_vs[pb].P, &vs[pb].P));
        }
        if (it > 0) for (int v = 0; v < n; v++) {
            if (prev_vs[v].L != vs[v].L) { memset(ccnt + v * M, 0, sizeof(int) * M); continue; }
            BS a = band(prev_vs[v].P, emask), b = band(vs[v].P, emask);
            if (beq(&a, &b)) continue;
            BS x = bxor(a, b); int y = bhi(&x), c = ++ccnt[v * M + ej[y]];
            if (c > R->C) R->C = c;
        }
        memcpy(prev_vs, vs, sizeof(Val) * n); memcpy(prev_sbar, sbar, sizeof(int) * n);
        int anyI = 0, anyT = 0;
        for (int v = 0; v < n; v++) {
            bz(&Is[v]); bz(&It[v]);
            if (sigma[v] != -1) FORBITS(g.succ[v], w) if (nvo(&g, &vs[sigma[v]], &vs[w]) < 0) { bset(&Is[v], w); anyI = 1; }
            if (tau[v] != -1) FORBITS(d.succ[v], w) if (nvo(&d, &vt[tau[v]], &vt[w]) < 0) { bset(&It[v], w); anyT = 1; }
        }
        if (!anyI && !anyT) { R->T3 = it; R->fb = 0; return; }
        if (anyI) {
            for (int v = 0; v < n; v++) {
                bz(&A[v]);
                if (g.pl[v] == 0) { bset(&A[v], sigma[v]); for (int j = 0; j < W; j++) A[v].w[j] |= Is[v].w[j]; }
                else bset(&A[v], tau[v]);
            }
            mkrestrict(&g, &hg, A); mkdual(&hg, &dh, A);
            int st[NMAX];
            for (int v = 0; v < n; v++) st[v] = g.pl[v] == 1 ? tau[v] : -1;
            evaluate_choice(&dh, st, tmpv, ch);
            int sig_spec[NMAX];
            for (int v = 0; v < n; v++) sig_spec[v] = g.pl[v] == 0 ? ch[v] : -1;
            evaluate_choice(&hg, sig_spec, Wst, dummy);
            memcpy(sig2, sig_spec, sizeof(int) * n);
            for (int v = 0; v < n; v++) {
                if (CTRL == 1 || g.pl[v] != 0 || bcount(&A[v]) < 2 || Wst[v].L == v) continue;
                int cand[NMAX], nc = 0, have = 0; Val bestv; int ntie = 0;
                FORBITS(A[v], w) {
                    Val e = Wst[w]; e.k += 1;
                    if (rk[v] > rk[e.L]) bset(&e.P, rk[v]);
                    if (!(e.L == Wst[v].L && e.k == Wst[v].k && beq(&e.P, &Wst[v].P))) continue;
                    ntie++;
                    if (!have || nvo(&g, &vs[w], &bestv) > 0) { bestv = vs[w]; nc = 0; cand[nc++] = w; have = 1; }
                    else if (nvo(&g, &vs[w], &bestv) == 0) cand[nc++] = w;
                }
                if (!ntie) { fprintf(stderr, "empty TIE\n"); exit(4); }
                int in = 0, mx = -1;
                for (int c = 0; c < nc; c++) { if (cand[c] == sig_spec[v]) in = 1; if (cand[c] > mx) mx = cand[c]; }
                sig2[v] = in ? sig_spec[v] : mx;
            }
        } else memcpy(sig2, sigma, sizeof(int) * n);
        if (anyT) {
            for (int v = 0; v < n; v++) {
                bz(&A[v]);
                if (g.pl[v] == 1) { bset(&A[v], tau[v]); for (int j = 0; j < W; j++) A[v].w[j] |= It[v].w[j]; }
                else bset(&A[v], sigma[v]);
            }
            mkrestrict(&g, &h3, A);
            evaluate_choice(&h3, sigma, tmpv, ch);
            for (int v = 0; v < n; v++) tau2[v] = g.pl[v] == 1 ? ch[v] : -1;
        } else memcpy(tau2, tau, sizeof(int) * n);
        if (!memcmp(sig2, sigma, sizeof(int) * n) && !memcmp(tau2, tau, sizeof(int) * n)) { R->T3 = it; R->fb = 1; return; }
        it++;
        if (it >= CAP) { R->T3 = it; R->fb = 0; R->capped = 1; return; }
        memcpy(sigma, sig2, sizeof(int) * n); memcpy(tau, tau2, sizeof(int) * n);
    }
}

static void read_one(Genome *G) {
    if (scanf("%d %d", &G->N, &G->M) != 2) exit(5);
    for (int x = 0; x < G->N; x++) scanf("%d", &G->lev[x]);
    int cnt[MMAX] = {0};
    for (int q = 0; q < G->M; q++) { scanf("%d %d %d %d %d", &G->own[q], &G->wt[q], &G->xt[q], &G->bi[q], &G->gate[q]); G->kof[q] = cnt[G->own[q]]++; }
    for (int q = 0; q < G->M; q++) scanf("%d", &G->br[q]);
    for (int q = 0; q < G->M; q++) scanf("%d", &G->bp[q]);
    for (int x = 0; x < G->N; x++) scanf("%d", &G->start[x]);
}

/* gates reported in (x, k) order = option order q */
static int next_perm(int *a, int n) {
    int i = n - 2; while (i >= 0 && a[i] >= a[i + 1]) i--;
    if (i < 0) return 0;
    int j = n - 1; while (a[j] <= a[i]) j--;
    int t = a[i]; a[i] = a[j]; a[j] = t;
    for (int l = i + 1, r = n - 1; l < r; l++, r--) { t = a[l]; a[l] = a[r]; a[r] = t; }
    return 1;
}
static void pr_list(const int *a, int n) { printf("["); for (int i = 0; i < n; i++) printf(i ? ", %d" : "%d", a[i]); printf("]"); }

int main(int argc, char **argv) {
    if (getenv("FAST36_NOELEV")) ELEV = 0;
    if (getenv("FAST36_CTRL")) CTRL = atoi(getenv("FAST36_CTRL"));
    if (argc >= 2 && !strcmp(argv[1], "one")) {
        Genome G; read_one(&G); Res R; run(&G, &R);
        printf("T3 %d fb %d capped %d C %d\n", R.T3, R.fb, R.capped, R.C);
        for (int q = 0; q < G.M; q++) printf("gate %d %d %d %d %d %d %d %d\n", G.own[q], G.kof[q], R.flips[q], R.lamch[q], R.chpe[q], R.lpe[q], R.chpb[q], R.lpb[q]);
        return 0;
    }
    if (argc >= 2 && !strcmp(argv[1], "block")) {
        Genome G; int a = 2; G.N = atoi(argv[a++]); G.M = atoi(argv[a++]); int N = G.N, M = G.M, D[MMAX];
        for (int x = 0; x < N; x++) G.lev[x] = atoi(argv[a++]);
        for (int x = 0; x < N; x++) D[x] = atoi(argv[a++]);
        int xts[MMAX]; for (int q = 0; q < M; q++) xts[q] = atoi(argv[a++]);
        int q = 0;
        for (int x = 0; x < N; x++) for (int k = 0; k < D[x]; k++, q++) {
            G.own[q] = x; G.kof[q] = k; G.xt[q] = xts[q]; G.bi[q] = q;
            int wt = -1; if (G.lev[x] > 0) for (int y = 0; y < N; y++) if (G.lev[y] == G.lev[x] - 1) { wt = y; break; }
            G.wt[q] = wt;
        }
        int gate[MMAX], br[MMAX], bp[MMAX], st[MMAX];
        long genomes = 0, c2fail = 0; int maxflip = 0, maxT3 = 0, havekfx = 0, maxkfx = 0;
        int rA = -1, rL = 0; /* maxratio = rA / (rL + 1); -1 initial */
        int ra_inner[4][MMAX], ra_gate = 0, ra_f = 0, ra_l = 0, ra_T = 0, ka_inner[4][MMAX], ka_gate = 0, ka_f = 0, ka_l = 0, ka_T = 0;
        static long hist[512][512]; memset(hist, 0, sizeof hist); int hmaxf = 0, hmaxl = 0;
        int ta_inner[4][MMAX], ta_T = -1; /* box 38: T3 argmax (first max in enumeration order) */
        int ncap = 0, maxC = -1; long nC2 = 0, Chist[64] = {0}; int ca_inner[4][MMAX], ca_T = 0;
        for (int i = 0; i < M; i++) gate[i] = i;
        do {
            for (int i = 0; i < M; i++) br[i] = i;
            do {
                for (int i = 0; i < M; i++) G.gate[i] = gate[i], G.br[i] = br[i];
                for (long bm = 0; bm < (1L << M); bm++) {
                    for (int i = 0; i < M; i++) bp[i] = (bm >> (M - 1 - i)) & 1, G.bp[i] = bp[i];
                    for (int x = 0; x < N; x++) st[x] = 0;
                    for (;;) {
                        for (int x = 0; x < N; x++) G.start[x] = st[x];
                        Res R; run(&G, &R); genomes++; ncap += R.capped;
                        /* am = max over gates by (flips/(lamch+1), flips), first max; ak = max by flips - 2(lamch+1), first max */
                        int am = 0, ak = 0, mf = 0;
                        for (int g2 = 0; g2 < M; g2++) {
                            int f = R.flips[g2], l = R.lamch[g2], fa = R.flips[am], la = R.lamch[am];
                            long lhs = (long)f * (la + 1), rhs = (long)fa * (l + 1);
                            if (lhs > rhs || (lhs == rhs && f > fa)) am = g2;
                            if (f - 2 * (l + 1) > R.flips[ak] - 2 * (R.lamch[ak] + 1)) ak = g2;
                            if (f > mf) mf = f;
                        }
                        int af = R.flips[am], al = R.lamch[am], kf = R.flips[ak], kl = R.lamch[ak], kfx = kf - 2 * (kl + 1);
                        if ((long)af * (rL + 1) > (long)rA * (al + 1)) {
                            rA = af; rL = al; ra_gate = am; ra_f = af; ra_l = al; ra_T = R.T3;
                            memcpy(ra_inner[0], gate, sizeof gate); memcpy(ra_inner[1], br, sizeof br); memcpy(ra_inner[2], bp, sizeof bp); memcpy(ra_inner[3], st, sizeof st);
                        }
                        if (!havekfx || kfx > maxkfx) {
                            havekfx = 1; maxkfx = kfx; ka_gate = ak; ka_f = kf; ka_l = kl; ka_T = R.T3;
                            memcpy(ka_inner[0], gate, sizeof gate); memcpy(ka_inner[1], br, sizeof br); memcpy(ka_inner[2], bp, sizeof bp); memcpy(ka_inner[3], st, sizeof st);
                        }
                        if (R.C > maxC) { maxC = R.C; ca_T = R.T3; memcpy(ca_inner[0], gate, sizeof gate); memcpy(ca_inner[1], br, sizeof br); memcpy(ca_inner[2], bp, sizeof bp); memcpy(ca_inner[3], st, sizeof st); }
                        nC2 += R.C >= 2; Chist[R.C < 63 ? R.C : 63]++;
                        if (mf > maxflip) maxflip = mf;
                        if (R.T3 > maxT3) maxT3 = R.T3;
                        if (R.T3 > ta_T) { ta_T = R.T3; memcpy(ta_inner[0], gate, sizeof gate); memcpy(ta_inner[1], br, sizeof br); memcpy(ta_inner[2], bp, sizeof bp); memcpy(ta_inner[3], st, sizeof st); }
                        c2fail += kfx > 0;
                        if (af < 512 && al < 512) { hist[af][al]++; if (af > hmaxf) hmaxf = af; if (al > hmaxl) hmaxl = al; }
                        else { fprintf(stderr, "hist overflow\n"); exit(6); }
                        int x = N - 1;
                        while (x >= 0 && ++st[x] == D[x]) st[x--] = 0;
                        if (x < 0) break;
                    }
                }
            } while (next_perm(br, M));
        } while (next_perm(gate, M));
        printf("{\"genomes\": %ld, \"maxratio\": %.17g, \"ratio_arg\": {\"inner\": [", genomes, rA < 0 ? -1.0 : (double)rA / (rL + 1));
        pr_list(ra_inner[0], M); printf(", "); pr_list(ra_inner[1], M); printf(", "); pr_list(ra_inner[2], M); printf(", "); pr_list(ra_inner[3], N);
        printf("], \"gate\": [%d, %d], \"flips\": %d, \"lamch\": %d, \"T3\": %d}, ", G.own[ra_gate], G.kof[ra_gate], ra_f, ra_l, ra_T);
        printf("\"maxkfx\": %d, \"kfx_arg\": {\"inner\": [", maxkfx);
        pr_list(ka_inner[0], M); printf(", "); pr_list(ka_inner[1], M); printf(", "); pr_list(ka_inner[2], M); printf(", "); pr_list(ka_inner[3], N);
        printf("], \"gate\": [%d, %d], \"flips\": %d, \"lamch\": %d, \"T3\": %d}, ", G.own[ka_gate], G.kof[ka_gate], ka_f, ka_l, ka_T);
        printf("\"maxC\": %d, \"nC2\": %ld, \"C_arg\": {\"inner\": [", maxC, nC2);
        pr_list(ca_inner[0], M); printf(", "); pr_list(ca_inner[1], M); printf(", "); pr_list(ca_inner[2], M); printf(", "); pr_list(ca_inner[3], N);
        printf("], \"T3\": %d}, \"Chist\": {", ca_T);
        { int fz = 1; for (int c = 0; c < 64; c++) if (Chist[c]) { printf(fz ? "\"%d\": %ld" : ", \"%d\": %ld", c, Chist[c]); fz = 0; } }
        printf("}, ");
        printf("\"T3_arg\": {\"inner\": ["); pr_list(ta_inner[0], M); printf(", "); pr_list(ta_inner[1], M); printf(", "); pr_list(ta_inner[2], M); printf(", "); pr_list(ta_inner[3], N); printf("], \"T3\": %d}, ", ta_T);
        printf("\"maxflip\": %d, \"maxT3\": %d, \"c2fail\": %ld, \"capped\": %d, \"hist\": {", maxflip, maxT3, c2fail, ncap);
        int first = 1;
        for (int f = 0; f <= hmaxf; f++) for (int l = 0; l <= hmaxl; l++) if (hist[f][l]) { printf(first ? "\"%d,%d\": %ld" : ", \"%d,%d\": %ld", f, l, hist[f][l]); first = 0; }
        printf("}}\n");
        return 0;
    }
    fprintf(stderr, "usage: fast36 one < genome.txt | fast36 block N M lev.. D.. xts..\n");
    return 1;
}
