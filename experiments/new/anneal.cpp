// L-NEW N1 DISC-ANNEAL, C++ port of anneal.py (--nocompress semantics: input priorities, no merging).
// Same algorithm: gamma_j = 1 - 2^-j, j = J0, J0+1, ...; per phase: Odd's best response to sigma by the highest-gain
// (Dantzig) single switch (Post-Ye 1208.5083 Thm 3.7), warm-started; then Even's Howard (switch-all to argmax x(w), ties:
// keep sigma(v), then smallest w); repeat until Even has no improving switch. Rewards n^pr (even pr) / -n^pr (odd pr).
// Exact values: X = Q*x with Q = b^n * prod_C (b^|C| - a^|C|), a = 2^j - 1, b = 2^j (boost::multiprecision::cpp_int).
// Stop test (certificate): win = [x > 0 ? Even : Odd]; sigma on Even's region and tau on Odd's region are closed and win
// (no cycle of the restricted graph whose top priority has the opponent's parity; recursive SCC check, as harness/verify.py).
// Best-reward start and initial tau = first successor, as anneal.py. --odd-howard: Odd's Howard rule instead.
// Usage: anneal_c game.pg [out.sol] [--j0 J] [--odd-howard]
//   prints: RESULT n=.. phases=J even_iters=E odd_iters=O max_phase=M nonzero=[..] secs=S
#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std; using boost::multiprecision::cpp_int;
struct Game { int n; vector<int> prio, owner; vector<vector<int>> succ; };
static Game readpg(const string& path) {
    ifstream in(path); string line; map<int, tuple<int,int,vector<int>>> rows;
    while (getline(in, line)) {
        if (line.empty() || line.rfind("parity", 0) == 0 || line[0] == '%' || line.rfind("start", 0) == 0) continue;
        for (size_t p = 0; p < line.size();) {
            size_t q = line.find(';', p); string st = line.substr(p, q == string::npos ? string::npos : q - p);
            p = (q == string::npos) ? line.size() : q + 1;
            size_t qu = st.find('"'); if (qu != string::npos) st = st.substr(0, qu);
            stringstream ss(st); int v, pr, ow; string sl; if (!(ss >> v >> pr >> ow >> sl)) continue;
            vector<int> s; stringstream t(sl); string tok; while (getline(t, tok, ',')) if (!tok.empty()) s.push_back(stoi(tok));
            sort(s.begin(), s.end()); s.erase(unique(s.begin(), s.end()), s.end()); rows[v] = make_tuple(pr, ow, s);
        }
    }
    Game g; g.n = rows.size(); g.prio.resize(g.n); g.owner.resize(g.n); g.succ.resize(g.n);
    for (auto& kv : rows) { g.prio[kv.first] = get<0>(kv.second); g.owner[kv.first] = get<1>(kv.second); g.succ[kv.first] = get<2>(kv.second); }
    return g;
}
static vector<cpp_int> values(int n, const vector<int>& nxt, const vector<cpp_int>& r, int j) {
    // gamma = a/b, b = 2^j, a = 2^j - 1: multiplication by a is (x << j) - x, division by b is an exact right shift.
    vector<int> state(n, 0); vector<vector<int>> cycles, order;
    for (int s = 0; s < n; s++) { if (state[s]) continue; vector<int> path; int v = s;
        while (state[v] == 0) { state[v] = 1; path.push_back(v); v = nxt[v]; }
        if (state[v] == 1) { int i = find(path.begin(), path.end(), v) - path.begin(); cycles.push_back(vector<int>(path.begin() + i, path.end())); path.resize(i);
            for (int c : cycles.back()) state[c] = 2; }
        for (int u : path) state[u] = 2; order.push_back(path); }
    auto mula = [&](const cpp_int& x) { return cpp_int((x << j) - x); };
    size_t K = cycles.size(); vector<cpp_int> dens(K);
    for (size_t k = 0; k < K; k++) { cpp_int ap = 1; for (size_t i = 0; i < cycles[k].size(); i++) ap = mula(ap);
        dens[k] = (cpp_int(1) << (j * cycles[k].size())) - ap; }
    vector<cpp_int> pre(K + 1, 1), suf(K + 1, 1);
    for (size_t k = 0; k < K; k++) pre[k + 1] = pre[k] * dens[k];
    for (size_t k = K; k-- > 0;) suf[k] = suf[k + 1] * dens[k];
    cpp_int Q = pre[K] << (j * n); vector<cpp_int> X(n);
    for (size_t k = 0; k < K; k++) { auto& C = cycles[k]; int L = C.size();
        cpp_int H = r[C[L - 1]];                                   // H_k = r_k b^(L-1-k) + a H_{k+1}
        for (int i = L - 2; i >= 0; i--) H = (r[C[i]] << (j * (L - 1 - i))) + mula(H);
        X[C[0]] = ((pre[k] * suf[k + 1]) << (j * n)) * (H << j);   // (Q / d_k) * S with S = H * b
        for (int i = L - 1; i >= 1; i--) X[C[i]] = Q * r[C[i]] + (mula(X[C[(i + 1) % L]]) >> j); }
    for (auto& path : order) for (int i = (int)path.size() - 1; i >= 0; i--) { int u = path[i]; X[u] = Q * r[u] + (mula(X[nxt[u]]) >> j); }
    return X;
}
// does the graph on 'nodes' (succ restricted) contain a cycle whose top priority has parity 'bad'? recursive SCC check
static bool bad_cycle(const Game& g, const vector<vector<int>>& es, vector<int> nodes, int bad) {
    vector<pair<vector<int>, int>> stack_; stack_.push_back({nodes, 0});
    vector<int> inset(g.n, 0), idx(g.n, -1), low(g.n, 0), on(g.n, 0); int stamp = 0;
    while (!stack_.empty()) { auto cur = stack_.back().first; stack_.pop_back(); stamp++;
        for (int v : cur) inset[v] = stamp;
        // Tarjan iterative
        int counter = 0; vector<int> st; vector<vector<int>> comps; for (int v : cur) idx[v] = -1;
        for (int root : cur) { if (idx[root] != -1) continue; vector<pair<int,size_t>> work = {{root, 0}}; idx[root] = low[root] = counter++; st.push_back(root); on[root] = 1;
            while (!work.empty()) { int v = work.back().first; size_t& it = work.back().second;
                if (it < es[v].size()) { int w = es[v][it++]; if (inset[w] != stamp) continue;
                    if (idx[w] == -1) { idx[w] = low[w] = counter++; st.push_back(w); on[w] = 1; work.push_back({w, 0}); }
                    else if (on[w]) low[v] = min(low[v], idx[w]); }
                else { work.pop_back(); if (!work.empty()) low[work.back().first] = min(low[work.back().first], low[v]);
                    if (low[v] == idx[v]) { vector<int> comp; int w; do { w = st.back(); st.pop_back(); on[w] = 0; comp.push_back(w); } while (w != v); comps.push_back(comp); } } } }
        for (auto& comp : comps) { bool nontriv = comp.size() > 1; if (!nontriv) { int v = comp[0]; for (int w : es[v]) if (w == v) nontriv = true; }
            if (!nontriv) continue; int top = -1; for (int v : comp) top = max(top, g.prio[v]);
            if (top % 2 == bad) return true;
            vector<int> rest; for (int v : comp) if (g.prio[v] != top) rest.push_back(v); if (!rest.empty()) stack_.push_back({rest, 0}); }
        for (int v : cur) inset[v] = 0; }
    return false;
}
static bool certificate(const Game& g, const vector<int>& win, const vector<int>& strat) {
    for (int p = 0; p < 2; p++) { vector<vector<int>> es(g.n); vector<int> nodes;
        for (int v = 0; v < g.n; v++) { if (win[v] != p) continue; nodes.push_back(v);
            if (g.owner[v] == p) { if (win[strat[v]] != p) return false; es[v] = {strat[v]}; }
            else { for (int w : g.succ[v]) if (win[w] != p) return false; es[v] = g.succ[v]; } }
        if (bad_cycle(g, es, nodes, 1 - p)) return false; }
    return true;
}
int main(int argc, char** argv) {
    if (argc < 2) { fprintf(stderr, "usage: anneal_c game.pg [out.sol] [--j0 J] [--odd-howard]\n"); return 1; }
    string path = argv[1], out; int j0 = 1; bool oddhoward = false;
    for (int i = 2; i < argc; i++) { string a = argv[i]; if (a == "--j0") j0 = atoi(argv[++i]); else if (a == "--odd-howard") oddhoward = true; else if (a.rfind("--", 0) != 0) out = a; }
    Game g = readpg(path); int n = g.n; auto t0 = chrono::steady_clock::now();
    vector<cpp_int> r(n); for (int v = 0; v < n; v++) { cpp_int x = boost::multiprecision::pow(cpp_int(n), g.prio[v]); r[v] = g.prio[v] % 2 == 0 ? x : cpp_int(-x); }
    vector<int> sigma(n, -1), tau(n, -1);
    for (int v = 0; v < n; v++) { const auto& sc = g.succ[v];
        if (g.owner[v] == 0) { auto key = [&](int w) { int rr = g.prio[w] % 2 == 0 ? g.prio[w] : -g.prio[w]; return make_pair(rr, rr % 2 == 0 ? w : -w); };
            int b = sc[0]; for (int w : sc) if (key(w) > key(b)) b = w; sigma[v] = b; }
        else tau[v] = sc[0]; }
    long ev = 0, od = 0; vector<long> per; vector<int> win(n), strat(n);
    for (int j = j0; j < 200000; j++) {
        long ph = 0; vector<cpp_int> X;
        while (true) {
            while (true) { vector<int> nxt(n); for (int v = 0; v < n; v++) nxt[v] = g.owner[v] == 0 ? sigma[v] : tau[v];
                X = values(n, nxt, r, j); bool ch = false;
                if (!oddhoward) { int bv = -1, bw = -1; cpp_int bd = 0;
                    for (int v = 0; v < n; v++) if (g.owner[v] == 1) for (int w : g.succ[v]) { cpp_int d = X[w] - X[tau[v]];
                        if (d < 0 && (bv < 0 || d < bd)) { bd = d; bv = v; bw = w; } }   // ties: first (v, w) in order = smallest
                    if (bv >= 0) { tau[bv] = bw; ch = true; } }
                else { for (int v = 0; v < n; v++) if (g.owner[v] == 1) { int b2 = g.succ[v][0]; for (int w : g.succ[v]) if (X[w] < X[b2]) b2 = w; if (X[b2] < X[tau[v]]) { tau[v] = b2; ch = true; } } }
                if (!ch) break; od++; }
            bool ch = false;
            for (int v = 0; v < n; v++) if (g.owner[v] == 0) { int b2 = sigma[v]; for (int w : g.succ[v]) if (X[w] > X[b2]) b2 = w;
                // ties among equal maxima: smallest index (anneal.py: max by (x, -w)); keep sigma only if strictly not improved
                if (X[b2] > X[sigma[v]]) { for (int w : g.succ[v]) if (X[w] == X[b2]) { b2 = w; break; } sigma[v] = b2; ch = true; } }
            if (!ch) break; ph++; ev++; }
        per.push_back(ph);
        for (int v = 0; v < n; v++) { win[v] = X[v] > 0 ? 0 : 1; strat[v] = g.owner[v] == win[v] ? (g.owner[v] == 0 ? sigma[v] : tau[v]) : -1; }
        if (certificate(g, win, strat)) {
            double secs = chrono::duration<double>(chrono::steady_clock::now() - t0).count(); long mx = *max_element(per.begin(), per.end());
            printf("RESULT n=%d phases=%d even_iters=%ld odd_iters=%ld max_phase=%ld nonzero=[", n, j, ev, od, mx);
            bool first = true; for (long p : per) if (p) { printf("%s%ld", first ? "" : ", ", p); first = false; } printf("] secs=%.2f\n", secs);
            if (!out.empty()) { FILE* f = fopen(out.c_str(), "w"); fprintf(f, "paritysol %d;\n", n);
                for (int v = 0; v < n; v++) { if (strat[v] >= 0) fprintf(f, "%d %d %d;\n", v, win[v], strat[v]); else fprintf(f, "%d %d;\n", v, win[v]); } fclose(f); }
            return 0; }
    }
    fprintf(stderr, "maxj reached\n"); return 2;
}
