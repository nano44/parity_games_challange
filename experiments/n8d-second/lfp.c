/* C port of kl2.py's least-fixed-point step mu^{G_tau up} (Algorithm 3 LabelSetting + Algorithm 2 Dijkstra,
   arXiv 2108.13338v5 §4), line for line; used by kl2fast.py. Same conventions as kl2.py:
   labels are h ints (position j = component xi_{2h-1-2j}), top[v] = 1 means TOP; pi is the shifted priority (C1);
   K[p] = number of leading components kept by the p-truncation. Dijkstra selects the minimum potential with an indexed heap
   (decrease-key; ties: smallest id); by Thm 4.2 / Cor 4.3 the result does not depend on tie-breaking or on the valid Phi chosen. */
#include <stdlib.h>
#include <string.h>

static int n, h, d, ell;
static const int *pi, *owner, *off, *adj, *tau, *K;
static int *nu, *top;          /* current labeling, n*h and n */
static int *tmp;               /* scratch label */

static int viol(int v, int w) {
    if (top[v]) return 0;
    if (top[w]) return 1;
    int p = pi[v], k = K[p];
    const int *a = nu + (size_t)v * h, *b = nu + (size_t)w * h;
    for (int j = 0; j < k; j++) {
        if (a[j] < b[j]) return 1;
        if (a[j] > b[j]) return 0;
    }
    return (p % 2 == 1);       /* equal prefixes: violated iff odd */
}

/* tighten(nu, vw) into out; returns 1 if TOP */
static int tighten(int v, int w, int *out) {
    if (top[w]) return 1;
    int p = pi[v], k = K[p];
    const int *b = nu + (size_t)w * h;
    for (int j = 0; j < k; j++) out[j] = b[j];
    for (int j = k; j < h; j++) out[j] = 0;
    if (p % 2 == 1) {
        int j = k - 1;
        while (j >= 0) {
            out[j] += 1;
            if (out[j] < ell) break;
            out[j] = 0;
            j--;
        }
        if (j < 0) return 1;
    }
    return 0;
}

/* label compare: (lt, ltop) vs (rt, rtop): -1, 0, 1 */
static int lcmp(const int *l, int ltop, const int *r, int rtop) {
    if (ltop || rtop) return ltop == rtop ? 0 : (ltop ? 1 : -1);
    for (int j = 0; j < h; j++) {
        if (l[j] < r[j]) return -1;
        if (l[j] > r[j]) return 1;
    }
    return 0;
}

/* ---- iterative Tarjan over nodes with pi <= p; succ given by a callback-free mode switch */
static int *t_index, *t_low, *t_on, *t_st, *t_wv, *t_wi, *t_comp;
static int *sel;               /* graph mode: 0 = G_tau, 1 = H (sel[v] = 1 if v is a base node: no out-arcs) */
static int mode;

static int nsucc(int v) {
    if (mode == 1 && sel[v]) return 0;
    return owner[v] == 0 ? off[v + 1] - off[v] : 1;
}
static int succ_i(int v, int i) { return owner[v] == 0 ? adj[off[v] + i] : tau[v]; }

/* comp id per node (completion order from 1), 0 for pi > p. returns #comps */
static int tarjan(int p, int *comp) {
    int c = 0, sp = 0, wp = 0, ncomp = 0;
    for (int v = 0; v < n; v++) { t_index[v] = -1; t_on[v] = 0; comp[v] = 0; }
    for (int root = 0; root < n; root++) {
        if (pi[root] > p || t_index[root] >= 0) continue;
        t_index[root] = t_low[root] = c++; t_st[sp++] = root; t_on[root] = 1;
        t_wv[wp] = root; t_wi[wp] = 0; wp++;
        while (wp > 0) {
            int v = t_wv[wp - 1];
            int pushed = 0;
            int ns = nsucc(v);
            while (t_wi[wp - 1] < ns) {
                int w = succ_i(v, t_wi[wp - 1]);
                t_wi[wp - 1]++;
                if (pi[w] > p) continue;
                if (t_index[w] < 0) {
                    t_index[w] = t_low[w] = c++; t_st[sp++] = w; t_on[w] = 1;
                    t_wv[wp] = w; t_wi[wp] = 0; wp++;
                    pushed = 1;
                    break;
                }
                if (t_on[w] && t_index[w] < t_low[v]) t_low[v] = t_index[w];
            }
            if (pushed) continue;
            wp--;
            if (wp > 0) {
                int u = t_wv[wp - 1];
                if (t_low[v] < t_low[u]) t_low[u] = t_low[v];
            }
            if (t_low[v] == t_index[v]) {
                ncomp++;
                int w;
                do { w = t_st[--sp]; t_on[w] = 0; comp[w] = ncomp; } while (w != v);
            }
        }
    }
    return ncomp;
}

/* potential order (Phi^nu, §4): TOP largest; else interleave Phi_{2h-2j}(v), nu(v)_j; ties by id */
static int pot_less(const int *phi, int v, int u) {
    if (top[v] || top[u]) { if (top[v] != top[u]) return top[u]; return v < u; }
    for (int j = 0; j < h; j++) {
        int a = phi[(size_t)j * n + v], b = phi[(size_t)j * n + u];
        if (a != b) return a < b;
        a = nu[(size_t)v * h + j]; b = nu[(size_t)u * h + j];
        if (a != b) return a < b;
    }
    return v < u;
}
static void sift_up(int *hp, int *pos, int i, const int *phi) {
    while (i > 0) {
        int par = (i - 1) / 2;
        if (!pot_less(phi, hp[i], hp[par])) break;
        int t = hp[i]; hp[i] = hp[par]; hp[par] = t; pos[hp[i]] = i; pos[hp[par]] = par; i = par;
    }
}
static void sift_down(int *hp, int *pos, int hn, int i, const int *phi) {
    for (;;) {
        int l = 2 * i + 1, r = l + 1, m = i;
        if (l < hn && pot_less(phi, hp[l], hp[m])) m = l;
        if (r < hn && pot_less(phi, hp[r], hp[m])) m = r;
        if (m == i) break;
        int t = hp[i]; hp[i] = hp[m]; hp[m] = t; pos[hp[i]] = i; pos[hp[m]] = m; i = m;
    }
}

/* returns 0 on success. mu/topv in: current labeling; out: mu^{G_tau up}. */
int kl_lfp(int n_, int h_, int d_, int ell_, const int *pi_, const int *owner_, const int *off_, const int *adj_,
           const int *tau_, const int *K_, int *mu, int *topv) {
    n = n_; h = h_; d = d_; ell = ell_; pi = pi_; owner = owner_; off = off_; adj = adj_; tau = tau_; K = K_;
    nu = mu; top = topv;
    int *B = calloc(n, sizeof(int)), *comp = calloc(n, sizeof(int));
    int *csize = calloc(n + 1, sizeof(int)), *chasp = calloc(n + 1, sizeof(int));
    t_index = malloc(n * sizeof(int)); t_low = malloc(n * sizeof(int)); t_on = malloc(n * sizeof(int));
    t_st = malloc(n * sizeof(int)); t_wv = malloc(n * sizeof(int)); t_wi = malloc(n * sizeof(int));
    tmp = malloc((h + 1) * sizeof(int));
    int *best = malloc((h + 1) * sizeof(int));
    sel = B;
    /* base nodes: pi(v) even and v on a cycle of G_tau[pi <= pi(v)] */
    mode = 0;
    char *present = calloc(d + 2, 1);
    for (int v = 0; v < n; v++) present[pi[v]] = 1;
    for (int p = 2; p <= d; p += 2) {
        if (!present[p]) continue;
        int nc = tarjan(p, comp);
        for (int i = 0; i <= nc; i++) { csize[i] = 0; chasp[i] = 0; }
        for (int v = 0; v < n; v++) if (comp[v]) csize[comp[v]]++;
        for (int v = 0; v < n; v++) {
            if (pi[v] != p) continue;
            if (csize[comp[v]] > 1) B[v] = 1;
            else {
                int ns = nsucc(v);
                for (int i = 0; i < ns; i++) if (succ_i(v, i) == v) { B[v] = 1; break; }
            }
        }
    }
    /* Algorithm 3 line 3: nu(v) <- min over vw in E_tau of lift(nu, vw), base nodes in id order */
    for (int v = 0; v < n; v++) {
        if (!B[v]) continue;
        int btop = 1;
        int ns = nsucc(v);
        for (int i = 0; i < ns; i++) {
            int w = succ_i(v, i);
            int ltop; const int *l;
            if (!viol(v, w)) { ltop = top[v]; l = nu + (size_t)v * h; }
            else { ltop = tighten(v, w, tmp); l = tmp; }
            if (lcmp(l, ltop, best, btop) <= 0) { btop = ltop; if (!ltop) memcpy(best, l, h * sizeof(int)); }
        }
        top[v] = btop;
        if (!btop) memcpy(nu + (size_t)v * h, best, h * sizeof(int));
    }
    /* Algorithm 2 */
    int *S = calloc(n, sizeof(int));
    for (int v = 0; v < n; v++) { S[v] = B[v]; if (!S[v]) top[v] = 1; }
    mode = 1;                                   /* H = G_tau minus out-arcs of base nodes */
    int hh = h;                                 /* Phi_{2h-2j} for j = 0..h-1, stored phi[j*n + v] */
    int *phi = calloc((size_t)hh * n, sizeof(int));
    for (int j = 0; j < hh; j++) {
        int p = 2 * h - 2 * j;
        tarjan(p, phi + (size_t)j * n);
    }
    /* predecessor lists in H */
    int *pcnt = calloc(n + 1, sizeof(int));
    for (int v = 0; v < n; v++) { int ns = nsucc(v); for (int i = 0; i < ns; i++) pcnt[succ_i(v, i) + 1]++; }
    for (int v = 0; v < n; v++) pcnt[v + 1] += pcnt[v];
    int *pfill = malloc(n * sizeof(int)); memcpy(pfill, pcnt, n * sizeof(int));
    int *padj = malloc((pcnt[n] + 1) * sizeof(int));
    for (int v = 0; v < n; v++) { int ns = nsucc(v); for (int i = 0; i < ns; i++) padj[pfill[succ_i(v, i)]++] = v; }
    #define DROP(v, u) do { int tt = tighten((v), (u), tmp); \
        if (lcmp(tmp, tt, nu + (size_t)(v) * h, top[v]) < 0) { top[v] = tt; if (!tt) memcpy(nu + (size_t)(v) * h, tmp, h * sizeof(int)); } } while (0)
    for (int u = 0; u < n; u++) {
        if (!S[u]) continue;
        for (int q = pcnt[u]; q < pcnt[u + 1]; q++) { int v = padj[q]; if (!S[v]) DROP(v, u); }
    }
    /* indexed binary min-heap over V \ S keyed by the potential; potentials only decrease (drop), so decrease-key */
    int *hp = malloc(n * sizeof(int)), *pos = malloc(n * sizeof(int)), hn = 0;
    for (int v = 0; v < n; v++) { pos[v] = -1; if (!S[v]) { hp[hn] = v; pos[v] = hn; hn++; } }
    for (int i = hn / 2 - 1; i >= 0; i--) sift_down(hp, pos, hn, i, phi);
    while (hn > 0) {
        int u = hp[0];
        hn--; pos[u] = -1;
        if (hn > 0) { hp[0] = hp[hn]; pos[hp[0]] = 0; sift_down(hp, pos, hn, 0, phi); }
        S[u] = 1;
        for (int q = pcnt[u]; q < pcnt[u + 1]; q++) {
            int v = padj[q];
            if (S[v]) continue;
            int tt = tighten(v, u, tmp);
            if (lcmp(tmp, tt, nu + (size_t)v * h, top[v]) < 0) {
                top[v] = tt; if (!tt) memcpy(nu + (size_t)v * h, tmp, h * sizeof(int));
                sift_up(hp, pos, pos[v], phi);
            }
        }
    }
    free(hp); free(pos);
    free(B); free(comp); free(csize); free(chasp); free(t_index); free(t_low); free(t_on); free(t_st); free(t_wv);
    free(t_wi); free(tmp); free(best); free(present); free(S); free(phi); free(pcnt); free(pfill); free(padj);
    return 0;
}

/* Admissible arcs (§3) and the §0 arc choice: for every Odd node v (increasing id) with a violated arc, cand[k] = v and
   arc[k] = the admissible successor with the largest Tighten (TOP largest), ties smallest successor id. Returns k. */
int kl_adm(int n_, int h_, int d_, int ell_, const int *pi_, const int *owner_, const int *off_, const int *adj_,
           const int *K_, int *mu, int *topv, int *cand, int *arc) {
    n = n_; h = h_; d = d_; ell = ell_; pi = pi_; owner = owner_; off = off_; adj = adj_; K = K_; nu = mu; top = topv;
    int *bl = malloc((h + 1) * sizeof(int)), *tl = malloc((h + 1) * sizeof(int));
    int k = 0;
    for (int v = 0; v < n; v++) {
        if (owner[v] != 1) continue;
        int bw = -1, btop = 0;
        /* successors in increasing id: adj of v is sorted by the caller (kl_sorted) */
        for (int q = off[v]; q < off[v + 1]; q++) {
            int w = adj[q];
            if (!viol(v, w)) continue;
            int tt = tighten(v, w, tl);
            if (bw < 0 || lcmp(tl, tt, bl, btop) > 0) { bw = w; btop = tt; if (!tt) memcpy(bl, tl, h * sizeof(int)); }
        }
        if (bw >= 0) { cand[k] = v; arc[k] = bw; k++; }
    }
    free(bl); free(tl);
    return k;
}
