#!/usr/bin/env python3
"""L-SI box 90: re-arming census with the per-pair MULTIPLICITY, on two engines.
Per (v, maximal Lambda-interval I): tops (most relevant e of each change of E_t(v)); for letters y, z: m(y, z) := #gaps between consecutive
y-tops whose most relevant top is z (so RA(y) = {z : m(y, z) >= 1}, c_y - 1 = sum_z m(y, z)); P(y) = 1 + sum_{z in RA(y)} P(z) (box 198
RA-PATHS); depth = longest RA chain (letters); fan-in = max |RA(y)|; A = longest alternation of two letters.
Counters (unit (v, I, y)): idfail (c_y - 1 != sum_z m(y, z)), rafail (an RA letter not above y), lexdec (unit change: top not in the new set).
Records: T, C = max c_y, maxP, depth, fanin, A, maxm = max m(y, z).
Engines (read-only, pinned; see pins.txt): own = L-RED R221 own.py (IDEAL-CYC Howard, G's start), dir in $OWN_DIR;
g3 = L-NEW's Gamma3 N5'-xi engine from S3 (gamma3 / n5v / n5x / eg195 as box 198 uses them), tree root in $ROOT.
Usage: mult90.py own|g3 G.json ..."""
import sys, os, json, collections
def census(tops_per_vi, rank, T):
    c = collections.Counter(T=T)
    for tops, newsets in tops_per_vi:
        if not tops: continue
        for z, ns in zip(tops, newsets):
            if z not in ns: c["lexdec"] += 1
        L = sorted(set(tops), key=lambda e: -rank[e]); pos = collections.defaultdict(list)
        for i, z in enumerate(tops): pos[z].append(i)
        P = {}; dep = {}
        for y in L:
            m = collections.Counter()
            for i, j in zip(pos[y], pos[y][1:]):
                if j > i + 1: m[max(tops[i + 1:j], key=lambda e: rank[e])] += 1
            if len(pos[y]) - 1 != sum(m.values()): c["idfail"] += 1
            if any(rank[z] <= rank[y] for z in m): c["rafail"] += 1
            P[y] = 1 + sum(P[z] for z in m); dep[y] = 1 + max((dep[z] for z in m), default=0)
            c["C"] = max(c["C"], len(pos[y])); c["maxP"] = max(c["maxP"], P[y]); c["depth"] = max(c["depth"], dep[y])
            c["fanin"] = max(c["fanin"], len(m)); c["maxm"] = max(c["maxm"], max(m.values(), default=0))
        for a in range(len(L)):
            for b in range(a + 1, len(L)):
                x, y = L[a], L[b]; n = 0; want = None
                for z in tops:
                    if z in (x, y) and z != want: n += 1; want = z
                c["A"] = max(c["A"], n)
        c["A"] = max(c["A"], 1)
    return c
def intervals(T, lam, eset, n):
    out = []
    for v in range(n):
        t = 0
        while t <= T:
            u = t
            while u + 1 <= T and lam(u + 1, v) == lam(t, v): u += 1
            Es = [eset(i, v) for i in range(t, u + 1)]; tops = []; news = []
            for a, b in zip(Es, Es[1:]):
                if a != b: d = a ^ b; tops.append(d); news.append(b)
            out.append((tops, news)); t = u + 1
    return out
def run_own(G):
    sys.path.insert(0, os.environ["OWN_DIR"]); import own
    out, V, O, _ = own.run(G, 3000); n, prio, _, _, _, _ = own.build(G); rk = own.VJ(prio).rk; evs = {V[("e", q)] for q in O}
    T = len(out) - 1
    iv = intervals(T, lambda t, v: out[t][1][v][0], lambda t, v: frozenset(e for e in out[t][1][v][1] if e in evs), n)
    iv = [([max(d, key=lambda e: rk[e]) for d in tops], news) for tops, news in iv]
    return census(iv, rk, T)
def run_g3(G):
    R = os.environ["ROOT"]; os.environ.setdefault("EG195_ROOT", R)
    sys.path[:0] = [os.path.join(R, p) for p in ("experiments/new/box195", "experiments/new/box191", "experiments/new/box189",
                    "experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
    import eg195, gamma3, n5v, n5x
    g0, _, _, V = gamma3.build(G, eg195.PADS); g = eg195.topg(g0); n = g.n; name = {v: k for k, v in V.items()}
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None)
    evs = [v for v in range(n) if isinstance(name[v], tuple) and name[v][0] == "e"]; bit = {E.bit[f]: f for f in evs}; ES = sum(bit)
    hist = []
    while len(hist) <= 20000:
        vs, _ = E.evaluate(tuple(sigma)); hist.append(vs)
        res = n5v.step(g, E, Ed, sigma, tau, "xi")
        if res is None or res[4]: break
        sigma, tau = res[0], res[1]
    T = len(hist) - 1
    def es(t, v):
        x = hist[t][v][1] & ES; return frozenset(f for b, f in bit.items() if x & b)
    iv = intervals(T, lambda t, v: hist[t][v][0], es, n)
    iv = [([max(d, key=lambda e: E.rank[e]) for d in tops], news) for tops, news in iv]
    return census(iv, E.rank, T)
if __name__ == "__main__":
    eng = sys.argv[1]; K = ("T", "C", "maxP", "depth", "fanin", "A", "maxm", "idfail", "rafail", "lexdec")
    print("engine", eng, "instance N+M", " ".join(K))
    for f in sys.argv[2:]:
        G = json.load(open(f)); G = G.get("genome", G)
        c = (run_own if eng == "own" else run_g3)(G)
        print(eng, os.path.basename(f), G["N"] + sum(len(o) for o in G["opts"]), " ".join(str(c[k]) for k in K), flush=True)
