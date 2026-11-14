#!/usr/bin/env python3
"""Box 198 (L-NEW successor 65): Lemma PAIR-HIGH on the Gamma3 Howard run (box 196 / 197 engine).
Per (v, Lambda-interval I): tops(v, I); for a letter y, c_y := #changes whose top is y; Dhi_y := #distinct values of E_t(v) restricted to
the e-vertices more relevant than y, over I. For every pair x, y of letters (y the more relevant): A_xy = longest x/y alternation in tops.
  ph1fail : c_y > Dhi_y                  [should be 0: Lemma PAIR-HIGH (a)]
  ph2fail : A_xy > 2 Dhi_y + 1            [should be 0: Lemma PAIR-HIGH (b)]
  rafail  : the most relevant top between two consecutive y-tops is not more relevant than y [should be 0: PAIR-HIGH's proof]
  rpfail  : c_y > paths(y), paths(y) := 1 + sum of paths(z) over y's re-arming letters z [should be 0: Lemma RA-PATHS]
  record  : maxC (max c_y), maxP (max paths(y)), maxDep (longest chain y < z1 < z2 ... of re-arming letters, counting y), maxRA (max number of distinct re-arming letters of one y), A (max A_xy), tight (letters y with c_y = Dhi_y >= 2), and the (v, I) of max A with its letters (level, c, Dhi), most relevant first.
Controls: P198_CTRL=1 uses Dhi_y := 1 (ph1fail must fire wherever some letter has two tops); P198_CTRL=2 uses paths(y) := 1 (rpfail must fire
likewise).
Usage: pair198.py G.json ...   (ROOT defaults to the repo root from this file's place)"""
import sys, os, json, collections
ROOT = os.environ.get("ROOT") or os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
os.environ.setdefault("EG195_ROOT", ROOT)
sys.path[:0] = [os.path.join(ROOT, p) for p in ("experiments/new/box195", "experiments/new/box191", "experiments/new/box189",
                "experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
import eg195, gamma3, n5v, n5x
CTRL = os.environ.get("P198_CTRL", "0")

def alt(seq, x, y):
    L = 0; want = None
    for z in seq:
        if z in (x, y) and z != want: L += 1; want = z
    return L

def run(G, cap=20000):
    g0, _, _, V = gamma3.build(G, eg195.PADS); g = eg195.topg(g0); n = g.n; name = {v: k for k, v in V.items()}
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None)
    evs = [v for v in range(n) if isinstance(name[v], tuple) and name[v][0] == "e"]; ES = sum(E.bit[v] for v in evs)
    hist = []
    while len(hist) <= cap:
        vs, sb = E.evaluate(tuple(sigma)); hist.append(vs)
        res = n5v.step(g, E, Ed, sigma, tau, "xi")
        if res is None or res[4]: break
        sigma, tau = res[0], res[1]
    c = collections.Counter(); best = None
    hi = {f: sum(E.bit[z] for z in evs if E.rank[z] > E.rank[f]) for f in evs}
    for v in range(n):
        t = 0
        while t < len(hist):
            s = t
            while t + 1 < len(hist) and hist[t + 1][v][0] == hist[s][v][0]: t += 1
            sets = [hist[u][v][1] & ES for u in range(s, t + 1)]
            tops = []
            for a, b in zip(sets, sets[1:]):
                if a != b: tops.append(max((f for f in evs if (a ^ b) & E.bit[f]), key=lambda f: E.rank[f]))
            letters = sorted(set(tops), key=lambda f: -E.rank[f]); cy = collections.Counter(tops)
            dhi = {y: (1 if CTRL == "1" else len({x & hi[y] for x in sets})) for y in letters}
            pos = collections.defaultdict(list)
            for i, z in enumerate(tops): pos[z].append(i)
            paths = {}; dep = {}
            for y in letters:                     # most relevant first; re-arming letters: the most relevant top strictly between two consecutive y-tops
                rs = set()
                for i, j in zip(pos[y], pos[y][1:]):
                    rs.add(max(tops[i + 1:j], key=lambda f: E.rank[f]))
                c["maxRA"] = max(c["maxRA"], len(rs)); c["maxC"] = max(c["maxC"], cy[y])
                if any(E.rank[z] <= E.rank[y] for z in rs): c["rafail"] += 1
                paths[y] = 1 if CTRL == "2" else 1 + sum(paths[z] for z in rs)      # Lemma RA-PATHS: c_y <= paths(y)
                dep[y] = 1 + max((dep[z] for z in rs), default=0); c["maxDep"] = max(c["maxDep"], dep[y])
                if cy[y] > paths[y]: c["rpfail"] += 1
                c["maxP"] = max(c["maxP"], paths[y])
            for y in letters:
                if cy[y] > dhi[y]: c["ph1fail"] += 1
                if cy[y] == dhi[y] >= 2: c["tight"] += 1
            A = 1 if tops else 0
            for i, y in enumerate(letters):
                for x in letters[i + 1:]:
                    a = alt(tops, x, y); A = max(A, a)
                    if a > 2 * dhi[y] + 1: c["ph2fail"] += 1
            if best is None or A > best[0]:
                best = (A, name[v], s, t, [(name[y][1], G["lev"][name[y][1][0]], cy[y], dhi[y]) for y in letters])
            t += 1
    return len(hist) - 1, c, best

if __name__ == "__main__":
    for fn in sys.argv[1:]:
        G = json.load(open(fn)); G = G.get("genome", G) if isinstance(G, dict) else G
        if not (isinstance(G, dict) and "opts" in G and "start" in G): print(os.path.basename(fn), "skipped"); continue
        T, c, b = run(G)
        print(f"{os.path.basename(fn)} T3 {T} ph1fail {c['ph1fail']} ph2fail {c['ph2fail']} rafail {c['rafail']} rpfail {c['rpfail']} maxC {c['maxC']} maxP {c['maxP']} maxDep {c['maxDep']} maxRA {c['maxRA']} tight {c['tight']} A {b[0]} at {b[1]} states {b[2]}-{b[3]}", flush=True)
        print("   letters (option, level, c, Dhi), most relevant first:", b[4], flush=True)
