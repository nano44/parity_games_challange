// L-NEW renumbering adversary for index-dependent SI rules (S5 zadeh, S6 cunningham; L-SI's definitions).
// Engine: vjfast_copy.cpp = verbatim copy of experiments/si/vjfast.cpp (L-SI; its main is renamed and unused).
// A renumbering pi (old vertex v -> new index pi[v]) changes (a) priority-rank ties, (b) best-reward start ties,
// (c) the zadeh tie-break / cunningham cyclic order. Hill climb (swaps; sideways moves allowed) maximises iterations.
// Usage: renum RULE game.pg [--restarts R] [--steps S] [--seed X] [--cap C] [--out best.pg] [--rev]
//   prints the identity count, the best count, and writes the best renumbered game to --out.
#define main vjfast_main
#include "vjfast_copy.cpp"
#undef main
static Game relabel(const Game& g, const vector<int>& pi) {
    Game h; h.n = g.n; h.prio.assign(g.n, 0); h.owner.assign(g.n, 0); h.succ.assign(g.n, {});
    for (int v = 0; v < g.n; v++) { int u = pi[v]; h.prio[u] = g.prio[v]; h.owner[u] = g.owner[v];
        for (int w : g.succ[v]) h.succ[u].push_back(pi[w]); sort(h.succ[u].begin(), h.succ[u].end()); }
    return h;
}
// same loop as vjfast main for zadeh / cunningham / index, start best; returns iterations (cap -> cap+1)
static long runrule(const Game& g, const string& rule, long cap, vector<int>* final_strat = nullptr) {
    Engine e(g); e.init(); mt19937_64 rng(0); vector<int> strat = e.initial("best", rng); long it = 0;
    map<pair<int,int>, long> entered; pair<int,int> last = {-1, -1};
    while (true) { e.cache.clear(); const auto& val = e.evaluate(strat).first; auto imp = e.improving(strat, val); if (imp.empty()) break;
        if (++it > cap) break;
        if (rule == "zadeh") { auto best = imp[0]; long bc = entered[best]; for (auto& ed : imp) { long c = entered[ed]; if (c < bc || (c == bc && ed < best)) { best = ed; bc = c; } } entered[best]++; strat[best.first] = best.second; }
        else if (rule == "cunningham") { pair<int,int> pick = {-1,-1}; for (auto& ed : imp) if (ed > last && (pick.first < 0 || ed < pick)) pick = ed; if (pick.first < 0) pick = *min_element(imp.begin(), imp.end()); last = pick; strat[pick.first] = pick.second; }
        else if (rule == "index") { auto best = *min_element(imp.begin(), imp.end()); strat[best.first] = best.second; }
        else { fprintf(stderr, "unknown rule\n"); exit(1); } }
    if (final_strat) *final_strat = strat;
    return it;
}
static void writepg(const Game& g, const string& path) {
    FILE* f = fopen(path.c_str(), "w"); fprintf(f, "parity %d;\n", g.n - 1);
    for (int v = 0; v < g.n; v++) { fprintf(f, "%d %d %d ", v, g.prio[v], g.owner[v]);
        for (size_t i = 0; i < g.succ[v].size(); i++) fprintf(f, "%s%d", i ? "," : "", g.succ[v][i]); fprintf(f, ";\n"); }
    fclose(f);
}
int main(int argc, char** argv) {
    if (argc < 3) { fprintf(stderr, "usage: renum RULE game.pg [--restarts R] [--steps S] [--seed X] [--cap C] [--out f]\n"); return 1; }
    string rule = argv[1], path = argv[2], out; long restarts = 4, steps = 300, seed = 1, cap = 2000000; bool rev = false;
    for (int i = 3; i < argc; i++) { string a = argv[i];
        if (a == "--restarts") restarts = atol(argv[++i]); else if (a == "--steps") steps = atol(argv[++i]);
        else if (a == "--seed") seed = atol(argv[++i]); else if (a == "--cap") cap = atol(argv[++i]);
        else if (a == "--out") out = argv[++i]; else if (a == "--rev") rev = true; }
    Game g = readpg(path); int n = g.n; mt19937_64 rng(seed);
    vector<int> id(n); iota(id.begin(), id.end(), 0);
    long base = runrule(g, rule, cap); vector<int> rv(n); for (int v = 0; v < n; v++) rv[v] = n - 1 - v;
    long revc = runrule(relabel(g, rv), rule, cap);
    printf("identity %ld reverse %ld\n", base, revc); fflush(stdout);
    vector<int> best = id; long bestc = base; if (revc > bestc) { best = rv; bestc = revc; }
    for (long r = 0; r < restarts; r++) {
        vector<int> cur; long curc;
        if (r == 0) { cur = best; curc = bestc; } else { cur = id; shuffle(cur.begin(), cur.end(), rng); curc = runrule(relabel(g, cur), rule, cap); }
        for (long s = 0; s < steps; s++) {
            vector<int> nx = cur; int k = 1 + rng() % 3;
            for (int t = 0; t < k; t++) { int a = rng() % n, b = rng() % n; swap(nx[a], nx[b]); }
            long c = runrule(relabel(g, nx), rule, cap);
            if (c >= curc) { cur = nx; curc = c; }
            if (curc > bestc) { bestc = curc; best = cur; printf("  restart %ld step %ld: %ld\n", r, s, bestc); fflush(stdout); }
        }
    }
    printf("RESULT rule=%s game=%s n=%d identity=%ld best=%ld\n", rule.c_str(), path.c_str(), n, base, bestc);
    if (!out.empty()) writepg(relabel(g, best), out);
    return 0;
}
