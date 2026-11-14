#!/usr/bin/env python3
"""Box 209 (L-NEW successor 72): the READINGS of Gamma3's construction used in docs/new/N5-LEVEL3-box209.md §1, checked on the graph
built by box189/gamma3.py (the builder of R117-R125), genome by genome. No run is made. Must-0 counter, unit (genome, clause):
  structfail: one of the clauses fails:
   n     n = N + 7M + 10 and the number of Even vertices is N + 6M + 9                                           [n_E3]
   pad   every pad is Even, has one successor and priority <= 2                                                   [R117]
   d1    the only in-edge of e_g is from pe_g, and the only in-edge of pe_g is from g                             [(D1')]
   d3    the only edges into the core {K0, K1, K2, K3, pA, s, q, r} from outside are pb_g -> K0                   [(D3')]
   d4    c_W's and c_X's only out-edge is the own self-loop                                                       [(D4')]
   edom  every vertex of priority above the lowest e-priority is an e-vertex, c_W, K0 or K3; e-priorities are even [(E-DOM3)]
   odd   the Odd vertices are the gates and K2
Usage: struct209.py G.json ... | struct209.py --rand SEED COUNT MODE"""
import sys, os, json, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.environ.get("ROOT") or os.path.abspath(os.path.join(HERE, "..", "..", ".."))
os.environ.setdefault("EG195_ROOT", ROOT)
sys.path[:0] = [os.path.join(ROOT, p) for p in ("experiments/new/box202", "experiments/new/box195", "experiments/new/box189", "experiments/new/box190",
                "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
import gamma3, eg195
def check(G, c):
    gm, _, _, V = gamma3.build(G, eg195.PADS); n = gm.n; N = G["N"]; M = sum(len(o) for o in G["opts"])
    kind = {v: (k[0] if isinstance(k, tuple) else k) for k, v in V.items()}; ins = collections.defaultdict(set)
    for v in range(n):
        for w in gm.succ[v]: ins[w].add(v)
    bad = collections.Counter()
    if n != N + 7 * M + 10 or sum(1 for v in range(n) if gm.owner[v] == 0) != N + 6 * M + 9: bad["n"] += 1
    PAD = ("pA", "s", "q", "r", "pe", "pbeta", "pb", "m")
    if any(kind[v] in PAD and (gm.owner[v] != 0 or len(gm.succ[v]) != 1 or gm.prio[v] > 2) for v in range(n)) or sum(1 for v in range(n) if kind[v] in PAD) != 4 * M + 4: bad["pad"] += 1
    for k, v in V.items():
        if isinstance(k, tuple) and k[0] == "e":
            pe, g = V[("pe", k[1])], V[("g", k[1])]
            if ins[v] != {pe} or ins[pe] != {g}: bad["d1"] += 1; break
    core = {V[("K", i)] for i in range(4)} | {V[x] for x in ("pA", "s", "q", "r")}; K0 = V[("K", 0)]
    if any(w in core and v not in core and not (kind[v] == "pb" and w == K0) for v in range(n) for w in gm.succ[v]): bad["d3"] += 1
    if gm.succ[V["cW"]] != [V["cW"]] or gm.succ[V["cX"]] != [V["cX"]]: bad["d4"] += 1
    emin = min(gm.prio[v] for v in range(n) if kind[v] == "e")
    if any(gm.prio[v] > emin and not (kind[v] == "e" or v in (V["cW"], K0, V[("K", 3)])) for v in range(n)) or any(gm.prio[v] % 2 for v in range(n) if kind[v] == "e"): bad["edom"] += 1
    if {v for v in range(n) if gm.owner[v] == 1} != {v for v in range(n) if kind[v] == "g"} | {V[("K", 2)]}: bad["odd"] += 1
    c["structfail"] += sum(bad.values()); c["genomes"] += 1
    return bad
if __name__ == "__main__":
    a = sys.argv[1:]; c = collections.Counter()
    if a[0] == "--rand":
        seed, cnt, mode = int(a[1]), int(a[2]), a[3]; rng = random.Random(seed); g = 0
        if mode == "k1":
            os.environ["K1_MODE"] = "1"; import k1srch202
            mk = lambda: k1srch202.mk(rng)
        else: mk = lambda: eg195.gen(rng, mode)
        while g < cnt:
            G = mk()
            if G is None or G["N"] < 2: continue
            g += 1; check(G, c)
        print("struct3 rand", mode, "seed", seed, "genomes", c["genomes"], "structfail", c["structfail"])
    else:
        for fn in a:
            G = json.load(open(fn))
            if not (isinstance(G, dict) and "N" in G and "opts" in G): c["skipped"] += 1; continue
            bad = check(G, c)
            if bad: print("struct3", os.path.basename(fn), "FAIL", dict(bad))
        print("struct3 files genomes", c["genomes"], "structfail", c["structfail"], "skipped (not a genome file)", c["skipped"])
