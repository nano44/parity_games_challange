#!/usr/bin/env python3
"""L-RED box 6 (produced on Opus 5.5): graded fitness for L-ALG succ. 6's KT targets (GAP-C.md §18g, l-alg 312c918;
Lead 06:38Z): (P-KT) a depth-0 P piece (Dom(prevV), Q empty) never breaks KT; (KT-STEP-first) the first depth-0 piece
breaking KT learns inside D or finds a dominion; (K-in). Uses L-ALG's dtl_step5.build and dtl_step5stats.kthr
(unmodified, imported read-only from LALG7_DIR >= 312c918), the same KT(R) as dtl_step5stats.py ("KTHR" lines).
Copy of carry/pk.py with K replaced by KT; kmin = least |c-list after| / |c-list before| at a P piece. Per search of p with
D = W_p(G') != {} and no dominion:
  pk    = depth-0 P pieces with KT(R) true and KT(R minus the piece) false     ((P-KT) violated iff > 0)
  kfv   = 1 if the first KT break is barren with nothing learned inside D before  ((KT-STEP-first) violated)
  kmin  = least (#c with KT after) / (#c before) over depth-0 P pieces with KT true before (gradient)
  pD    = D-vertices removed by depth-0 P pieces
  tb    = depth-0 T pieces that break KT; tbar = those whose recursion learns nothing inside D, with nothing learned
          inside D before ((T-STEP) violated iff tbar > 0; l-alg 37d3440, GAP-C.md §18i)
Score: 1e12 incomplete + 1e11 (kin + pk + kfv + tbar) + 1e9 min(tb, 9) + 1e6 (1000 - best kmin per mille) + 1e3 min(pD, 999) + searches.
Order from DTL_ORDER. Usage: kt.py G.pg ..."""
import sys, os
ld = os.path.join(os.environ["LALG7_DIR"], "experiments", "alg")
sys.path.insert(0, ld); sys.path.insert(0, os.path.join(ld, "..", "harness"))
import pg, dtl_step5 as S5, dtl_step5stats as ST

def measure_game(g):
    d = S5.build(g); d.run()
    m = dict(incomplete=len(d.G), kin=0, pk=0, kfv=0, tb=0, tbar=0, kmin=1000, pD=0, searches=len(d.trace), wsearch=0)
    for tr in d.trace:
        Dw, G, p = tr["Wp"], tr["G"], tr["p"]
        if not Dw or tr["dom"]: continue
        m["wsearch"] += 1; pcs = tr["pieces"]
        if not any(C <= Dw for pc in pcs if pc["kind"] == "S" for C in pc["new"]): m["kin"] += 1
        first = True
        for i, pc in enumerate(pcs):
            if pc["depth"] != 0 or pc["kind"] == "E": continue
            R0 = set(pc["R"]); R1 = R0 - pc["rem"]
            k0 = ST.kthr(d, p, Dw, R0, G); k1 = ST.kthr(d, p, Dw, R1, G)
            if pc["kind"] == "P":
                m["pD"] += len(pc["rem"] & Dw)
                if k0:
                    m["kmin"] = min(m["kmin"], int(1000 * len(k1) / len(k0)))
                    if not k1: m["pk"] += 1
            if pc["kind"] == "T" and k0 and not k1:                       # (T-STEP), GAP-C.md §18i (l-alg 37d3440)
                m["tb"] += 1
                nxt = next((j for j in range(i + 1, len(pcs)) if pcs[j]["depth"] == 0), len(pcs))
                rec = any(C <= Dw for q in pcs[i + 1:nxt] if q["kind"] == "S" for C in q["new"])
                before = any(C <= Dw for q in pcs[:i] if q["kind"] == "S" for C in q["new"])
                if not rec and not before: m["tbar"] += 1
            if k0 and not k1 and first:
                first = False
                nxt = next((j for j in range(i + 1, len(pcs)) if pcs[j]["depth"] == 0), len(pcs))
                learned = any(C <= Dw for q in pcs[i:nxt] if q["kind"] == "S" for C in q["new"])
                before = any(C <= Dw for q in pcs[:i] if q["kind"] == "S" for C in q["new"])
                if not learned and not before: m["kfv"] += 1
    return m

def measure(path): return measure_game(pg.read(path))

def score(path):
    m = measure(path)
    if m["wsearch"] == 0: return 0
    return (10 ** 12 * m["incomplete"] + 10 ** 11 * (m["kin"] + m["pk"] + m["kfv"] + m["tbar"]) + 10 ** 9 * min(m["tb"], 9) + 10 ** 6 * (1000 - m["kmin"])
            + 10 ** 3 * min(m["pD"], 999) + min(m["searches"], 999))

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f in sys.argv[1:]:
        print(os.path.basename(f), os.environ.get("DTL_ORDER", "stable"), measure(f))
