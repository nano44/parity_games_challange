#!/usr/bin/env python3
"""L-RED box 6 (produced on Opus 5.5): graded (K-in)/(K-low) fitness (L-ALG GAP-C.md §14-§17; Lead fitness 04:55Z:
incomplete/wrong > K-in > K-low > TW straddle > ...). Uses the piece tracer experiments/red/k4b/pieces.py (L-ALG's
dtl_kin.KI, unmodified, LALG5_DIR). For every search of p with W_p(G') != {} and no dominion:
  prod  = stable pieces that learn a new tangle inside W_p (prod = 0 is a (K-in) violation, hence also (K-low));
  eaten = p-priority vertices of W_p removed by -1 pieces before the first productive piece, over all p-priority
          vertices of W_p (the §17 Step 5 removal, Dom(prevV) with Q empty, and threshold pieces).
Score: 1e12 incomplete + 1e11 K-in + 1e9 straddle(TW) + 1e7 * (9 - min prod) + 1e6 duplicate-check hits inside W_p
(at that search) + 1e3 * best eaten fraction (per mille, at the
search with the least prod) + searches. Order from DTL_ORDER. Usage: klow.py G.pg ..."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "k4b"))
import pieces as PC, pg

def measure_game(g, order=None):
    order = order or os.environ.get("DTL_ORDER", "stable")
    d0 = PC.K.P.build(g); d = PC.PT(d0.pr, d0.ow, d0.outs, ins_desc=(order == "oink")); d.run()
    m = dict(incomplete=len(d.G), kin=0, straddle=0, minprod=9, dupmin=0, eaten=0, searches=len(d.trace), wsearch=0)
    for tr in d.trace:
        W = tr["Wp"]
        if not W or tr["d1"] > tr["dom"]: continue
        m["wsearch"] += 1; p = tr["p"]
        Pw = {v for v in W if d.pr[v] % 2 == p}
        prod = 0; eaten = set(); seen = False
        for dep, kind, V, rem, newt, Rin in tr["log"]:
            for C in newt:
                if C & W and not C <= W: m["straddle"] += 1
            if kind == "STABLE" and any(C <= W for C in newt):
                prod += 1; seen = True
            elif kind != "STABLE" and not seen:
                eaten |= rem & Pw
        if prod == 0: m["kin"] += 1
        dw = sum(1 for C in tr["dups"] if set(C) <= W); m["dupW"] = m.get("dupW", 0) + dw
        fr = int(1000 * len(eaten) / max(1, len(Pw)))
        if (prod, -dw, -fr) < (m["minprod"], -m["dupmin"], -m["eaten"]): m["minprod"], m["dupmin"], m["eaten"] = prod, dw, fr
    return m

def measure(path): return measure_game(pg.read(path))

def score(path):
    m = measure(path)
    if m["wsearch"] == 0: return 0
    return (10 ** 12 * m["incomplete"] + 10 ** 11 * m["kin"] + 10 ** 9 * min(m["straddle"], 9) + 10 ** 7 * (9 - min(m["minprod"], 9)) + 10 ** 6 * min(m["dupmin"], 9)
            + 10 ** 3 * min(m["eaten"], 999) + min(m["searches"], 999))

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f in sys.argv[1:]:
        print(os.path.basename(f), os.environ.get("DTL_ORDER", "stable"), measure(f))
