// L-SI fast engine: Voege-Jurdzinski valuations (same algorithm and conventions as si.py: ranks by (priority, index),
// path component = set of ranks above the cycle node, keys (reward of cycle node, path set lexicographic by rank with
// even ranks good, length shorter-is-worse at odd cycles / longer-is-worse at even cycles) and the rules
// switch-all, rar (Random-Action-Removal, Zwick 2607.06334 Fig. 1), zadeh, cunningham, msf, lsf, random-edge.
// Usage: vjfast RULE game.pg [--seed S] [--start best|first|last] [--dump]   (prints "solved with K iterations, E evaluations.")
//        vjfast valu game.pg --strat "v:w v:w ..."   prints the valuation of each vertex (cycle node, path ranks, length)
// Validation: xcheck_fast.py compares valuations and iteration counts with si.py.
#include <bits/stdc++.h>
using namespace std;
typedef vector<uint64_t> Bits;
struct Game { int n; vector<int> prio, owner; vector<vector<int>> succ; };
static Game readpg(const string& path) {
    ifstream in(path); string line; map<int, tuple<int,int,vector<int>>> rows;
    while (getline(in, line)) {
        if (line.empty() || line.rfind("parity", 0) == 0 || line[0] == '%') continue;
        for (size_t p = 0; p < line.size();) {
            size_t q = line.find(';', p); string st = line.substr(p, q == string::npos ? string::npos : q - p);
            p = (q == string::npos) ? line.size() : q + 1;
            // strip label
            size_t qu = st.find('"'); if (qu != string::npos) st = st.substr(0, qu);
            stringstream ss(st); int v, pr, ow; string sl;
            if (!(ss >> v >> pr >> ow >> sl)) continue;
            vector<int> s; stringstream t(sl); string tok;
            while (getline(t, tok, ',')) if (!tok.empty()) s.push_back(stoi(tok));
            sort(s.begin(), s.end()); s.erase(unique(s.begin(), s.end()), s.end());
            rows[v] = make_tuple(pr, ow, s);
        }
    }
    Game g; g.n = rows.size(); g.prio.resize(g.n); g.owner.resize(g.n); g.succ.resize(g.n);
    for (auto& kv : rows) { int v = kv.first; g.prio[v] = get<0>(kv.second); g.owner[v] = get<1>(kv.second); g.succ[v] = get<2>(kv.second); }
    return g;
}
struct Val { int c; Bits path; int len; };
struct Engine {
    Game g; int n, W; vector<int> rank, par, rew; vector<vector<int>> pred;
    long evals = 0;
    map<vector<int>, pair<vector<Val>, vector<int>>> cache;
    Engine(const Game& gg) : g(gg) {
        n = g.n; W = (n + 63) / 64; rank.assign(n, 0); par.assign(n, 0); rew.assign(n, 0); pred.assign(n, {});
        vector<int> order(n); iota(order.begin(), order.end(), 0);
        sort(order.begin(), order.end(), [&](int a, int b) { return make_pair(g.prio[a], a) < make_pair(g.prio[b], b); });
        for (int r = 0; r < n; r++) rank[order[r]] = r;
        for (int v = 0; v < n; v++) { par[v] = g.prio[v] % 2; int pp = 2 * rank[v] + par[v]; rew[v] = par[v] == 0 ? pp : -pp; }
        for (int v = 0; v < n; v++) for (int w : g.succ[v]) pred[w].push_back(v);
    }
    // compare valuations a, b: returns <0 if a worse for Even, 0 equal, >0 better
    int cmp(const Val& a, const Val& b) const {
        if (a.c != b.c) return rew[a.c] < rew[b.c] ? -1 : (rew[a.c] > rew[b.c] ? 1 : 0);
        for (int w = W - 1; w >= 0; w--) {
            uint64_t d = a.path[w] ^ b.path[w];
            if (d) { int r = w * 64 + 63 - __builtin_clzll(d); bool inA = (a.path[w] >> (r - w * 64)) & 1;
                     bool evenr = rankpar[r] == 0; return (inA == evenr) ? 1 : -1; }
        }
        if (a.len == b.len) return 0;
        if (par[a.c] == 1) return a.len < b.len ? -1 : 1;   // odd cycle: shorter is worse
        return a.len > b.len ? -1 : 1;                       // even cycle: longer is worse
    }
    vector<int> rankpar;
    void init() { rankpar.assign(n, 0); for (int v = 0; v < n; v++) rankpar[rank[v]] = par[v]; }
    const pair<vector<Val>, vector<int>>& evaluate(const vector<int>& strat) {
        auto it = cache.find(strat); if (it != cache.end()) return it->second;
        evals++;
        vector<vector<int>> gs(n), gp(n);
        for (int v = 0; v < n; v++) { if (g.owner[v] == 0) gs[v] = {strat[v]}; else gs[v] = g.succ[v]; for (int w : gs[v]) gp[w].push_back(v); }
        vector<char> alive(n, 1); vector<Val> val(n); vector<int> tau(n, -1);
        vector<int> order(n); iota(order.begin(), order.end(), 0);
        sort(order.begin(), order.end(), [&](int a, int b) { return rew[a] < rew[b]; });
        for (int v : order) {
            if (!alive[v]) continue;
            int rv = rank[v];
            // cycle through v via alive vertices of lower rank?
            vector<char> seen(n, 0); vector<int> st = {v}; seen[v] = 1; bool found = false; vector<int> parent(n, -1); int cyc = -1;
            while (!st.empty() && !found) { int x = st.back(); st.pop_back();
                for (int y : gs[x]) { if (y == v) { found = true; cyc = x; break; } if (alive[y] && rank[y] < rv && !seen[y]) { seen[y] = 1; parent[y] = x; st.push_back(y); } } }
            if (!found) continue;
            // R: alive vertices reaching v
            vector<char> inR(n, 0); vector<int> R; st = {v}; inR[v] = 1;
            while (!st.empty()) { int x = st.back(); st.pop_back(); R.push_back(x); for (int y : gp[x]) if (alive[y] && !inR[y]) { inR[y] = 1; st.push_back(y); } }
            unordered_map<int, vector<int>> hs, hp; for (int x : R) { for (int y : gs[x]) if (inR[y]) hs[x].push_back(y); for (int y : gp[x]) if (inR[y]) hp[x].push_back(y); }
            unordered_map<int, Bits> path; for (int x : R) path[x] = Bits(W, 0);
            auto reach = [&](int start, int excl) { vector<char> s(n, 0); vector<int> q = {start}; s[start] = 1;
                while (!q.empty()) { int x = q.back(); q.pop_back(); for (int y : hp[x]) if (y != excl && !s[y]) { s[y] = 1; q.push_back(y); } } return s; };
            auto restrict = [&](int x, const vector<char>& M) { vector<int> keep; for (int y : hs[x]) { if (M[y]) keep.push_back(y); else { auto& v2 = hp[y]; v2.erase(find(v2.begin(), v2.end(), x)); } } hs[x] = keep; };
            vector<int> above; for (int x : R) if (rank[x] > rv) above.push_back(x);
            sort(above.begin(), above.end(), [&](int a, int b) { return rank[a] > rank[b]; });
            for (int u : above) {
                if (par[u] == 0) { auto M = reach(v, u); for (int q : R) if (!M[q]) path[q][rank[u] / 64] |= 1ULL << (rank[u] % 64);
                    restrict(u, M); for (int q : R) if (M[q]) restrict(q, M); }
                else { auto M = reach(u, v); for (int q : R) if (M[q]) { path[q][rank[u] / 64] |= 1ULL << (rank[u] % 64); if (q != u) restrict(q, M); } }
            }
            unordered_map<int, int> dist;
            if (par[v] == 0) { // longest path to v in the restricted graph (DAG + v)
                unordered_map<int, int> state; // -1 in progress
                function<int(int)> longest = [&](int x) -> int { if (x == v) return 0; auto f = state.find(x); if (f != state.end()) { if (f->second < 0) { fprintf(stderr, "cycle in restricted graph\n"); exit(2); } return f->second; }
                    state[x] = -1; int best = -1, arg = -1; for (int y : hs[x]) { int d = longest(y); if (d > best) { best = d; arg = y; } } state[x] = best + 1; if (g.owner[x] == 1) tau[x] = arg; return best + 1; };
                for (int x : R) dist[x] = longest(x);
            } else { dist[v] = 0; vector<int> layer = {v};
                while (!layer.empty()) { vector<int> nxt; for (int x : layer) for (int y : hp[x]) if (!dist.count(y)) { dist[y] = dist[x] + 1; if (g.owner[y] == 1) tau[y] = x; nxt.push_back(y); } layer = nxt; } }
            if (g.owner[v] == 1) { int x = cyc; while (parent[x] != v && parent[x] != -1) x = parent[x]; tau[v] = (x != v) ? x : cyc; }
            for (int x : R) { val[x] = {v, path[x], dist[x]}; alive[x] = 0; }
        }
        auto res = cache.emplace(strat, make_pair(val, tau)); return res.first->second;
    }
    vector<pair<int,int>> improving(const vector<int>& strat, const vector<Val>& val) const {
        vector<pair<int,int>> out; for (int v = 0; v < n; v++) if (g.owner[v] == 0) for (int w : g.succ[v]) if (w != strat[v] && cmp(val[w], val[strat[v]]) > 0) out.push_back({v, w}); return out; }
    vector<int> initial(const string& kind, mt19937_64& rng) const {
        vector<int> s(n, -1);
        for (int v = 0; v < n; v++) { if (g.owner[v] == 1) continue; const auto& sc = g.succ[v];
            if (kind == "first") s[v] = sc.front(); else if (kind == "last") s[v] = sc.back();
            else if (kind == "random") s[v] = sc[rng() % sc.size()];
            else if (kind.rfind("spec:", 0) == 0) { s[v] = sc.front(); }
            else { // best reward, PGSolver tie-break: max by (reward, index for even / -index for odd)
                auto key = [&](int w) { int r = g.prio[w] % 2 == 0 ? g.prio[w] : -g.prio[w]; return make_pair(r, r % 2 == 0 ? w : -w); };
                int b = sc[0]; for (int w : sc) if (key(w) > key(b)) b = w; s[v] = b; } }
        return s; }
    int level3(const Val& a, const Val& b) const { // class of first difference: 3 cycle, 2 path (rank), 1 length
        if (a.c != b.c) return 3 * 100000 + max(rank[a.c], rank[b.c]);
        for (int w = W - 1; w >= 0; w--) { uint64_t d = a.path[w] ^ b.path[w]; if (d) return 2 * 100000 + w * 64 + 63 - __builtin_clzll(d); }
        return 100000; }
    // rules
    long rar_switches = 0;
    // Random-Facet* (one random permutation of Even's edges fixed at the start; always remove the first available edge in
    // that order: Friedmann-Hansen-Zwick SODA 2011 / errata 1410.7871 section 2): the variant whose lower bound stands.
    vector<pair<int,int>> perm;
    vector<int> rfstar(vector<int> a, vector<vector<int>> F) {
        vector<pair<int,int>> B; for (int v = 0; v < n; v++) if (g.owner[v] == 0) for (int w : F[v]) if (w != a[v]) B.push_back({v, w});
        if (B.empty()) return a;
        pair<int,int> pick = {-1,-1}; for (auto& e : perm) { if (find(B.begin(), B.end(), e) != B.end()) { pick = e; break; } }
        auto [v, r] = pick;
        auto& Fv = F[v]; Fv.erase(find(Fv.begin(), Fv.end(), r));
        vector<int> b = rfstar(a, F);
        F[v].push_back(r);
        const auto& val = evaluate(b).first;
        if (cmp(val[r], val[b[v]]) > 0) { b[v] = r; rar_switches++; return rfstar(b, F); }
        return b; }
    vector<int> rar(vector<int> a, vector<vector<int>> F, mt19937_64& rng) {
        vector<pair<int,int>> B; for (int v = 0; v < n; v++) if (g.owner[v] == 0) for (int w : F[v]) if (w != a[v]) B.push_back({v, w});
        if (B.empty()) return a;
        auto [v, r] = B[rng() % B.size()];
        auto& Fv = F[v]; Fv.erase(find(Fv.begin(), Fv.end(), r));
        vector<int> b = rar(a, F, rng);
        F[v].push_back(r);
        const auto& val = evaluate(b).first;
        if (cmp(val[r], val[b[v]]) > 0) { b[v] = r; rar_switches++; return rar(b, F, rng); }
        return b; }
};
int main(int argc, char** argv) {
    if (argc < 3) { fprintf(stderr, "usage\n"); return 1; }
    string rule = argv[1], path = argv[2], start = "best", stratspec; long seed = 0; bool dump = false; bool trace = false;
    for (int i = 3; i < argc; i++) { string a = argv[i]; if (a.rfind("--", 0) != 0) continue; if (a == "--seed") seed = atol(argv[++i]); else if (a == "--start") start = argv[++i]; else if (a == "--strat") stratspec = argv[++i]; else if (a == "--dump") dump = true; else if (a == "--trace") trace = true; }
    Game g = readpg(path); Engine e(g); e.init(); mt19937_64 rng(seed);
    if (rule == "valu") { vector<int> s = e.initial("first", rng); stringstream ss(stratspec); string tok;
        while (ss >> tok) { int c = tok.find(':'); s[stoi(tok.substr(0, c))] = stoi(tok.substr(c + 1)); }
        const auto& val = e.evaluate(s).first;
        for (int v = 0; v < g.n; v++) { printf("%d %d", v, val[v].c); vector<int> rs; for (int r = 0; r < g.n; r++) if ((val[v].path[r / 64] >> (r % 64)) & 1) rs.push_back(r); printf(" ["); for (size_t i = 0; i < rs.size(); i++) printf("%s%d", i ? "," : "", rs[i]); printf("] %d\n", val[v].len); }
        return 0; }
    vector<int> strat = e.initial(start, rng); long it = 0; long ties_idx_global = 0;
    if (start.rfind("spec:", 0) == 0) { stringstream ss(start.substr(5)); string tok; while (ss >> tok) { int c = tok.find(':'); strat[stoi(tok.substr(0, c))] = stoi(tok.substr(c + 1)); } }
    if (rule == "rfstar") { vector<vector<int>> F(g.n); for (int v = 0; v < g.n; v++) if (g.owner[v] == 0) { F[v] = g.succ[v]; for (int w : g.succ[v]) e.perm.push_back({v, w}); }
        shuffle(e.perm.begin(), e.perm.end(), rng); strat = e.rfstar(strat, F); it = e.rar_switches; }
    else if (rule == "rar") { vector<vector<int>> F(g.n); for (int v = 0; v < g.n; v++) if (g.owner[v] == 0) F[v] = g.succ[v]; strat = e.rar(strat, F, rng); it = e.rar_switches; }
    else {
        map<pair<int,int>, long> entered; pair<int,int> last = {-1, -1}; long ties_idx = 0;
        while (true) { e.cache.clear(); const auto& ev0 = e.evaluate(strat); const auto& val = ev0.first; const auto& tau0 = ev0.second; auto imp = e.improving(strat, val); if (imp.empty()) break; it++;
            if (rule.rfind("df-", 0) == 0) {   // downstream-first filter: keep edges at vertices v with no OTHER improving vertex on v's play
                vector<char> isimp(g.n, 0); for (auto& ed : imp) isimp[ed.first] = 1;
                vector<pair<int,int>> keep;
                for (auto& ed : imp) { int v = ed.first; int x = (g.owner[v] == 0) ? strat[v] : tau0[v]; vector<char> seen(g.n, 0); bool ok = true;
                    while (!seen[x]) { if (x != v && isimp[x]) { ok = false; break; } seen[x] = 1; x = (g.owner[x] == 0) ? strat[x] : tau0[x]; }
                    if (ok) keep.push_back(ed); }
                imp = keep; }
            string base = rule.rfind("df-", 0) == 0 ? rule.substr(3) : rule;
            if (base == "switch-all") { vector<int> nw = strat; for (int v = 0; v < g.n; v++) if (g.owner[v] == 0) { int b = g.succ[v][0]; for (int w : g.succ[v]) { int c = e.cmp(val[w], val[b]); if (c > 0 || (c == 0 && w > b)) b = w; } if (e.cmp(val[b], val[strat[v]]) > 0) nw[v] = b; } strat = nw; }
            else if (base == "random-edge") { auto [v, w] = imp[rng() % imp.size()]; strat[v] = w; }
            else if (base == "zadeh") { auto best = imp[0]; long bc = entered[best]; for (auto& ed : imp) { long c = entered[ed]; if (c < bc || (c == bc && ed < best)) { best = ed; bc = c; } } entered[best]++; strat[best.first] = best.second; }
            else if (base == "cunningham") { pair<int,int> pick = {-1,-1}; for (auto& ed : imp) if (ed > last && (pick.first < 0 || ed < pick)) pick = ed; if (pick.first < 0) pick = *min_element(imp.begin(), imp.end()); last = pick; strat[pick.first] = pick.second; }
            else if (base == "index") { auto best = *min_element(imp.begin(), imp.end()); strat[best.first] = best.second; }
            else if (base == "most-improved") { // S7: switch maximising the number of vertices whose valuation strictly improves;
                // ties: best new valuation at v (cmp), then smallest (v, w) (index; non-invariant last resort, counted in ties_idx)
                pair<int,int> best = {-1,-1}; long bc = -1; Val bv; vector<int> bs;
                for (auto& ed : imp) { vector<int> s2 = strat; s2[ed.first] = ed.second; const auto& v2 = e.evaluate(s2).first;
                    long c = 0; for (int x = 0; x < g.n; x++) if (e.cmp(v2[x], val[x]) > 0) c++;
                    int better = 0; if (best.first < 0 || c > bc) better = 1; else if (c == bc) { int d = e.cmp(v2[ed.first], bv); if (d > 0) better = 1; else if (d == 0) { ties_idx++; if (ed < best) better = 1; } }
                    if (better) { best = ed; bc = c; bv = v2[ed.first]; bs = s2; } }
                if (trace) { long tot = 0; for (int x = 0; x < g.n; x++) tot += val[x].len; fprintf(stderr, "T it=%ld v=%d w=%d count=%ld improving=%zu sumlen=%ld\n", it, best.first, best.second, bc, imp.size(), tot); }
                strat = bs; ties_idx_global = ties_idx; }
            else if (base == "msf" || base == "lsf") { auto best = imp[0]; int bl = e.level3(val[strat[best.first]], val[best.second]);
                for (auto& ed : imp) { int l = e.level3(val[strat[ed.first]], val[ed.second]); bool better = base == "msf" ? (l > bl || (l == bl && ed < best)) : (l < bl || (l == bl && ed < best)); if (better) { best = ed; bl = l; } }
                strat[best.first] = best.second; }
            else { fprintf(stderr, "unknown rule\n"); return 1; } }
    }
    const auto& ev = e.evaluate(strat); const auto& val = ev.first; const auto& tau = ev.second;
    fprintf(stderr, "solved with %ld iterations, %ld evaluations.\n", it, e.evals);
    if (rule == "most-improved") fprintf(stderr, "index tie-breaks used: %ld\n", ties_idx_global);
    FILE* out = stdout; if (argc > 3 && string(argv[3]).rfind("--", 0) != 0) out = fopen(argv[3], "w");
    fprintf(out, "paritysol %d;\n", g.n);
    for (int v = 0; v < g.n; v++) { int win = e.par[val[v].c];
        if (g.owner[v] == win) fprintf(out, "%d %d %d;\n", v, win, g.owner[v] == 0 ? strat[v] : tau[v]); else fprintf(out, "%d %d;\n", v, win); }
    if (out != stdout) fclose(out);
    return 0;
}
