// L-RED-B B7: C++ port of si7.py (own engine; same definitions, Friedmann arXiv 1106.0778v2 Section 3) with the rules
// howard and rf (ROOT-FIRST, L-SI 57's pseudocode as relayed by the Lead 2026-11-14 14:52Z).
// Cross-checked against si7.py by cmp7.py (iterations and the final strategy must be equal).
// Path sets are bit vectors over relevance ranks; comparison = the paper's set order (most relevant differing vertex).
// Usage: rf7 RULE game.pg start|best [--tie high|low] [--sigma] [--max N] [--prog K]
#include <bits/stdc++.h>
using namespace std;
typedef vector<uint64_t> Bits;
static int n, W;
static vector<int> prio, owner_, rnk, par, rew, byrew;
static vector<vector<int>> succ;
static vector<string> names;

struct Val { int w; Bits p; int k; };
static inline int cmpset(const Bits& a, const Bits& b, const vector<int>& rankpar) {
    for (int i = W - 1; i >= 0; --i) if (a[i] != b[i]) {
        uint64_t x = a[i] ^ b[i]; int r = i * 64 + 63 - __builtin_clzll(x);
        bool ina = (a[i] >> (r & 63)) & 1; bool even = rankpar[r] == 0;
        return (ina == even) ? 1 : -1;
    }
    return 0;
}
static vector<int> rankpar;
static int cmpval(const Val& a, const Val& b) {
    if (a.w != b.w) return rew[a.w] < rew[b.w] ? -1 : 1;
    int c = cmpset(a.p, b.p, rankpar); if (c) return c;
    int ka = par[a.w] ? a.k : -a.k, kb = par[b.w] ? b.k : -b.k;
    return ka < kb ? -1 : (ka > kb ? 1 : 0);
}

static long evals = 0;
static void evaluate(const vector<int>& sigma, vector<Val>& val, vector<int>& tau) {
    ++evals;
    vector<int> eu, ev;                        // edges of G_sigma
    vector<vector<int>> hs(n), hp(n);
    for (int v = 0; v < n; ++v) {
        if (owner_[v] == 0) { hs[v].push_back(eu.size()); hp[sigma[v]].push_back(eu.size()); eu.push_back(v); ev.push_back(sigma[v]); }
        else for (int y : succ[v]) { hs[v].push_back(eu.size()); hp[y].push_back(eu.size()); eu.push_back(v); ev.push_back(y); }
    }
    vector<char> ealive(eu.size(), 1), alive(n, 1), inR(n, 0), inS(n, 0);
    val.assign(n, Val{-1, Bits(W, 0), 0}); tau.assign(n, -1);
    vector<int> st, R, S, dist(n), outdeg(n), best(n);
    for (int w : byrew) {
        if (!alive[w]) continue;
        int rw = rnk[w];
        // cycle through w inside alive vertices less relevant than w?
        bool found = false; vector<char> seen(n, 0); seen[w] = 1; st.assign(1, w);
        while (!st.empty() && !found) {
            int x = st.back(); st.pop_back();
            for (int e : hs[x]) { if (!ealive[e]) continue; int y = ev[e];
                if (y == w) { found = true; break; }
                if (alive[y] && rnk[y] < rw && !seen[y]) { seen[y] = 1; st.push_back(y); } }
        }
        if (!found) continue;
        R.assign(1, w); inR[w] = 1; st.assign(1, w);
        while (!st.empty()) { int x = st.back(); st.pop_back();
            for (int e : hp[x]) { if (!ealive[e]) continue; int y = eu[e];
                if (alive[y] && !inR[y]) { inR[y] = 1; R.push_back(y); st.push_back(y); } } }
        // restrict to R: kill edges leaving R
        for (int x : R) for (int e : hs[x]) if (ealive[e] && !inR[ev[e]]) ealive[e] = 0;
        vector<int> hi; for (int x : R) if (rnk[x] > rw) hi.push_back(x);
        sort(hi.begin(), hi.end(), [](int a, int b) { return rnk[a] > rnk[b]; });
        auto back = [&](int start, int excl) {
            S.assign(1, start); inS[start] = 1; st.assign(1, start);
            while (!st.empty()) { int x = st.back(); st.pop_back();
                for (int e : hp[x]) { if (!ealive[e]) continue; int y = eu[e];
                    if (!inR[y] || y == excl || inS[y]) continue; inS[y] = 1; S.push_back(y); st.push_back(y); } }
        };
        auto confine = [&](int q) { for (int e : hs[q]) if (ealive[e] && !inS[ev[e]]) ealive[e] = 0; };
        for (int u : hi) {
            int ru = rnk[u];
            if (par[u] == 0) {
                back(w, u);
                for (int q : R) if (!inS[q]) val[q].p[ru >> 6] |= 1ULL << (ru & 63);
                for (int q : S) confine(q);
                confine(u);
            } else {
                back(u, w);
                for (int q : S) { val[q].p[ru >> 6] |= 1ULL << (ru & 63); if (q != u) confine(q); }
            }
            for (int q : S) inS[q] = 0;
        }
        for (int x : R) dist[x] = -1;
        if (par[w] == 1) {
            dist[w] = 0; vector<int> fr(1, w), nx;
            while (!fr.empty()) { nx.clear();
                for (int x : fr) for (int e : hp[x]) { if (!ealive[e]) continue; int y = eu[e];
                    if (inR[y] && dist[y] < 0) { dist[y] = dist[x] + 1; nx.push_back(y); } }
                fr.swap(nx); }
        } else {
            for (int x : R) { int c = 0; if (x != w) for (int e : hs[x]) if (ealive[e]) ++c; outdeg[x] = c; best[x] = 0; }
            dist[w] = 0; st.assign(1, w);
            while (!st.empty()) { int x = st.back(); st.pop_back();
                for (int e : hp[x]) { if (!ealive[e]) continue; int y = eu[e]; if (y == w || !inR[y]) continue;
                    if (dist[x] + 1 > best[y]) best[y] = dist[x] + 1;
                    if (--outdeg[y] == 0) { dist[y] = best[y]; st.push_back(y); } } }
        }
        for (int x : R) { if (dist[x] < 0) { fprintf(stderr, "valuation: lost vertex\n"); exit(3); } val[x].w = w; val[x].k = dist[x]; }
        for (int x : R) if (owner_[x] == 1) {
            int c = -1;
            for (int e : hs[x]) { if (!ealive[e]) continue; int y = ev[e];
                bool ok = (x == w) ? all_of(val[y].p.begin(), val[y].p.end(), [](uint64_t z) { return z == 0; }) : (dist[y] + 1 == dist[x]);
                if (ok && (c < 0 || y < c)) c = y; }
            if (c < 0) { fprintf(stderr, "valuation: no consistent successor\n"); exit(3); }
            tau[x] = c;
        }
        for (int x : R) { alive[x] = 0; inR[x] = 0; }
    }
    for (int v = 0; v < n; ++v) if (alive[v]) { fprintf(stderr, "valuation: unassigned\n"); exit(3); }
}

int main(int argc, char** argv) {
    if (argc < 4) { fprintf(stderr, "usage\n"); return 2; }
    string rule = argv[1]; bool tiehigh = true, showsigma = false; long maxit = LONG_MAX, prog = 0;
    for (int i = 4; i < argc; ++i) { string a = argv[i];
        if (a == "--tie") tiehigh = string(argv[++i]) == "high";
        else if (a == "--sigma") showsigma = true;
        else if (a == "--max") maxit = atol(argv[++i]);
        else if (a == "--prog") prog = atol(argv[++i]); }
    // parse pg
    { ifstream in(argv[2]); string all((istreambuf_iterator<char>(in)), istreambuf_iterator<char>());
      map<int, tuple<int, int, vector<int>, string>> rows; size_t pos = 0;
      while (pos < all.size()) { size_t e = all.find(';', pos); if (e == string::npos) break; string line = all.substr(pos, e - pos); pos = e + 1;
          size_t a = line.find_first_not_of(" \t\r\n"); if (a == string::npos) continue; line = line.substr(a);
          if (line.rfind("parity", 0) == 0 || line.rfind("start", 0) == 0) continue;
          string nm; size_t q = line.find('"'); if (q != string::npos) { nm = line.substr(q + 1, line.rfind('"') - q - 1); line = line.substr(0, q); }
          istringstream ss(line); int v, p, o; string sl; ss >> v >> p >> o >> sl; vector<int> s; string tok; istringstream s2(sl);
          while (getline(s2, tok, ',')) if (!tok.empty()) s.push_back(atoi(tok.c_str()));
          rows[v] = make_tuple(p, o, s, nm.empty() ? to_string(v) : nm); }
      n = rows.size(); prio.resize(n); owner_.resize(n); succ.resize(n); names.resize(n);
      for (auto& kv : rows) { int v = kv.first; prio[v] = get<0>(kv.second); owner_[v] = get<1>(kv.second); succ[v] = get<2>(kv.second); names[v] = get<3>(kv.second); } }
    W = (n + 63) / 64;
    vector<int> order(n); iota(order.begin(), order.end(), 0);
    sort(order.begin(), order.end(), [](int a, int b) { return prio[a] != prio[b] ? prio[a] < prio[b] : a < b; });
    rnk.resize(n); par.resize(n); rew.resize(n); rankpar.resize(n);
    for (int r = 0; r < n; ++r) rnk[order[r]] = r;
    for (int v = 0; v < n; ++v) { par[v] = prio[v] & 1; rew[v] = par[v] ? -(rnk[v] + 1) : (rnk[v] + 1); rankpar[rnk[v]] = par[v]; }
    byrew.resize(n); iota(byrew.begin(), byrew.end(), 0); sort(byrew.begin(), byrew.end(), [](int a, int b) { return rew[a] < rew[b]; });
    vector<int> sigma(n, -1);
    if (string(argv[3]) == "best") { for (int v = 0; v < n; ++v) if (owner_[v] == 0) { int b = succ[v][0]; for (int u : succ[v]) if (rew[u] > rew[b] || (rew[u] == rew[b] && u > b)) b = u; sigma[v] = b; } }
    else { ifstream in(argv[3]); int a, b; while (in >> a >> b) sigma[a] = b; }
    for (int v = 0; v < n; ++v) if (owner_[v] == 0 && find(succ[v].begin(), succ[v].end(), sigma[v]) == succ[v].end()) { fprintf(stderr, "bad start at %d\n", v); return 2; }
    vector<Val> val; vector<int> tau; long its = 0; long switches = 0, maximp = 0;
    while (true) {
        evaluate(sigma, val, tau);
        // improving targets
        vector<int> imp; vector<vector<int>> T(n); vector<int> bestt(n, -1);
        for (int v = 0; v < n; ++v) if (owner_[v] == 0) {
            const Val& cur = val[sigma[v]];
            for (int u : succ[v]) if (cmpval(val[u], cur) > 0) T[v].push_back(u);
            if (!T[v].empty()) { imp.push_back(v); int b = T[v][0];
                for (int u : T[v]) { int c = cmpval(val[u], val[b]); if (c > 0 || (c == 0 && (tiehigh ? u > b : u < b))) b = u; }
                bestt[v] = b; }
        }
        if (imp.empty() || its >= maxit) break;
        maximp = max<long>(maximp, imp.size());
        vector<int> sw;
        if (rule == "howard") sw = imp;
        else {
            // B[x] = improvable vertices on the play from x (functional graph nxt)
            vector<int> nxt(n); for (int v = 0; v < n; ++v) nxt[v] = owner_[v] == 0 ? sigma[v] : tau[v];
            vector<char> isimp(n, 0); for (int v : imp) isimp[v] = 1;
            vector<Bits> B(n); vector<char> state(n, 0);
            for (int s = 0; s < n; ++s) { if (state[s]) continue;
                vector<int> path; int x = s; while (!state[x]) { state[x] = 1; path.push_back(x); x = nxt[x]; }
                if (state[x] == 1) {           // x on the current path: a new cycle
                    size_t i = 0; while (path[i] != x) ++i; Bits c(W, 0);
                    for (size_t j = i; j < path.size(); ++j) if (isimp[path[j]]) c[path[j] >> 6] |= 1ULL << (path[j] & 63);
                    for (size_t j = i; j < path.size(); ++j) { B[path[j]] = c; state[path[j]] = 2; }
                    path.resize(i); }
                Bits acc = B[x];
                for (int j = (int)path.size() - 1; j >= 0; --j) { int y = path[j]; if (isimp[y]) acc[y >> 6] |= 1ULL << (y & 63); B[y] = acc; state[y] = 2; }
            }
            int m = imp.size(); vector<int> id(n, -1); for (int i = 0; i < m; ++i) id[imp[i]] = i;
            vector<vector<int>> adj(m);
            for (int i = 0; i < m; ++i) { int v = imp[i]; Bits d = B[sigma[v]]; for (int w : T[v]) for (int z = 0; z < W; ++z) d[z] |= B[w][z];
                d[v >> 6] &= ~(1ULL << (v & 63));
                for (int z = 0; z < W; ++z) { uint64_t b = d[z]; while (b) { int t = __builtin_ctzll(b); b &= b - 1; adj[i].push_back(id[z * 64 + t]); } } }
            // Tarjan
            vector<int> idx(m, -1), low(m), comp(m, -1), stk; vector<char> on(m, 0); int cnt = 0, nc = 0;
            for (int s = 0; s < m; ++s) { if (idx[s] >= 0) continue;
                vector<pair<int, size_t>> work; work.push_back({s, 0}); idx[s] = low[s] = cnt++; stk.push_back(s); on[s] = 1;
                while (!work.empty()) { int v = work.back().first; size_t& k = work.back().second;
                    if (k < adj[v].size()) { int w = adj[v][k++];
                        if (idx[w] < 0) { idx[w] = low[w] = cnt++; stk.push_back(w); on[w] = 1; work.push_back({w, 0}); }
                        else if (on[w]) low[v] = min(low[v], idx[w]); }
                    else { work.pop_back(); if (!work.empty()) { int p = work.back().first; low[p] = min(low[p], low[v]); }
                        if (low[v] == idx[v]) { while (true) { int w = stk.back(); stk.pop_back(); on[w] = 0; comp[w] = nc; if (w == v) break; } ++nc; } } } }
            vector<char> sink(nc, 1);
            for (int i = 0; i < m; ++i) for (int w : adj[i]) if (comp[w] != comp[i]) sink[comp[i]] = 0;
            for (int i = 0; i < m; ++i) if (sink[comp[i]]) sw.push_back(imp[i]);
        }
        if (sw.empty()) { fprintf(stderr, "rule switched nothing\n"); return 4; }
        for (int v : sw) sigma[v] = bestt[v];
        switches += sw.size(); ++its;
        if (prog && its % prog == 0) { fprintf(stderr, "... %ld iterations\n", its); }
    }
    int oddwon = 0; for (int v = 0; v < n; ++v) oddwon += par[val[v].w];
    // FNV-1a of the final strategy
    uint64_t h = 1469598103934665603ULL; for (int v = 0; v < n; ++v) { h ^= (uint64_t)(sigma[v] + 2); h *= 1099511628211ULL; }
    long m = 0; for (auto& s : succ) m += s.size();
    printf("%s tie %s n %d m %ld iterations %ld evals %ld switches %ld maximp %ld odd-won %d sigmahash %016llx\n", rule.c_str(), tiehigh ? "high" : "low", n, m, its, evals, switches, maximp, oddwon, (unsigned long long)h);
    if (showsigma) { for (int v = 0; v < n; ++v) if (owner_[v] == 0) printf("%d %d\n", v, sigma[v]); }
    return 0;
}
