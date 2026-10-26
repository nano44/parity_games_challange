#!/usr/bin/env python3
"""L-SI box 17 (successor 13): corrected forms of LEVEL-COUNT after its count form died (lcount_n23, lcount2_n23; note §15).
Same segments as lvl.py (stretch_D segments of fallback-free in-phase runs with (h3_D); v with constant cycle nodes). Per v:
  SL(v)   the set of (score, level) pairs of rises (score W or Xi; level = top rank of P_k delta P_k+1 at a weight-increasing change)
  LC2_V   |OC(v)| > |SL(v)|                      (CONJECTURE LC2, the per-(score, level) count form)
  PAIR_V  one score rises twice at one level     (PAIR-ONCE, a strong form that would give |rises| <= |SL| <= 2n), v with |OC| >= 1
  PAIROC_V  one (score, level) rises at two offset changes (PAIR-OC; implies LC2). OC_NORISE: an offset change with no rise (TWIN-GAP (i) says 0)
  PAIR_ALL_V  the same for every v with constant cycle nodes (rises without offset changes included)
  EVENTS  per v with |OC| >= 2: the sequence of (transition, W rise level, Xi rise level, offset change) (with -v)
MUT=1: only the W score is counted in SL (control: must fail on the instances). Usage as lvl.py: --one GAME [START] | --list FILE [KMIN]"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import lvl
from collections import Counter
C = lvl.C; VIOL = lvl.VIOL; top = lvl.top; MUT = os.environ.get("MUT") == "1"; VERB = "-v" in sys.argv

def seg(g, E, name, rows, a, b):
    C["segs"] += 1
    for v in range(g.n):
        if len({(rows[x]["vs"][v][0], rows[x]["W"][v][0]) for x in range(a, b + 1)}) > 1: continue
        oc, sl, rises, ev = 0, set(), Counter(), []
        for k in range(a, b):
            x0, x1, w0, w1 = rows[k]["vs"][v], rows[k + 1]["vs"][v], rows[k]["W"][v], rows[k + 1]["W"][v]
            r = {}
            for sc, y0, y1 in (("W", w0, w1), ("X", x0, x1)):
                L = top(y0[1] ^ y1[1])
                if L >= 0 and E.weight(y1[1]) > E.weight(y0[1]): r[sc] = L; rises[(sc, L)] += 1
            if not MUT: sl |= set(r.items())
            elif "W" in r: sl.add(("W", r["W"]))
            d = (E.weight(w1[1]) - E.weight(x1[1])) - (E.weight(w0[1]) - E.weight(x0[1]))
            oc += bool(d); ev.append((k - a, r.get("W"), r.get("X"), bool(d)))
        if any(c > 1 for c in rises.values()):
            C["PAIR_ALL_V"] += 1; VIOL.append(("PAIR_ALL", name, a, b, v, [e for e in ev if e[1] is not None or e[2] is not None]))
        C["v_with_rise"] += bool(rises); C["max_rises_any"] = max(C["max_rises_any"], sum(rises.values()))
        if not oc: continue
        C["v_with_oc"] += 1; C["max_oc"] = max(C["max_oc"], oc); C["max_rises"] = max(C["max_rises"], sum(rises.values()))
        ocp = Counter((sc, L) for e in ev if e[3] for sc, L in (("W", e[1]), ("X", e[2])) if L is not None)
        if any(c > 1 for c in ocp.values()): C["PAIROC_V"] += 1; VIOL.append(("PAIROC", name, a, b, v, [e for e in ev if e[3]]))
        if any(not ((e[1] is not None) or (e[2] is not None)) for e in ev if e[3]): C["OC_NORISE"] += 1; VIOL.append(("OC_NORISE", name, a, b, v))
        if oc > len(sl): C["LC2_V"] += 1; VIOL.append(("LC2", name, a, b, v, oc, sorted(sl)))
        if any(c > 1 for c in rises.values()): C["PAIR_V"] += 1; VIOL.append(("PAIR", name, a, b, v, [e for e in ev if e[1] or e[2]]))
        if VERB and oc >= 2: print("EVENTS", name, a, b, "v", v, "oc", oc, "SL", sorted(sl), [e for e in ev if e[1] is not None or e[2] is not None or e[3]])

lvl.seg = seg
if __name__ == "__main__":
    sys.argv = [x for x in sys.argv if x != "-v"]
    lvl.main()
