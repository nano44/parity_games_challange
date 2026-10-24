#!/usr/bin/env python3
"""L-SI box 7: DATA for the exit potential D (docs/si/N5-C-box7.md §9). On 𝒞^1O inside a phase, ω := τ(o) (constant). At a state with
H2, D_k := {exits e ∉ R̄_k : Ξ_k(e) ◁ Ξ_k(ω)}. Checks at in-phase transitions k -> k+1 with H1, H2 at k, H2 at k+1 and w constant:
  (D1) at a THR state σ̄_k(o) ∈ D_k;   (D2) D_{k+1} ⊆ D_k ∪ {exits released at k -> k+1 (in R_k, not in R̄_{k+1})};
  (D3) at a non-tame transition σ̄_k(o) ∉ D_{k+1};
  (REL-NJ) inside one maximal scope run, an exit released into D at a fallback is never σ̄_k(o) at a later non-tame transition;
  (D1') at an in-scope non-tame transition σ̄_k(o) ∈ D_k (no H3 needed).
Scope: (h) at k (H3 dropped with NOH3=1), H2 at k+1, w constant. Counts: non-tame transitions in scope / out of scope; releases into D, split by fallback / arena step.
Usage: dpot.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tame import *
sys.path.insert(0, os.path.join(ROOT, "experiments/new/box28"))
from nhprof import oncycle

NOH3 = os.environ.get("NOH3") == "1"   # NOH3=1: drop H3 from the scope (tests D1'-D3, JD and NOREL-A at OTHER states)

def scan_d(g):
    E, out = states(g); n = g.n; o = odd_choice(g); assert o is not None
    Ed = n5.Engine(n5.dual(g)); ex = sorted(set(g.succ[o])); res = []
    c = dict(relnj_chk=0, relnj_viol=0, D1p=0, D1pviol=0, chk=0, D1=0, D1viol=0, D2viol=0, D3=0, D3viol=0, J_in=0, J_out=0, rel_fb=0, rel_ar=0, maxD=0)
    for a in out:
        gl = [lev(a["Xi"][a["s"][y]], a["Xi"][z]) for y, z in a["Is"]]; a["M"] = max(gl) if gl else -3
        a["key"] = (tuple(x[0] for x in a["Xi"]), a["t"], tuple(x[0] for x in Ed.evaluate(tuple(a["t"]))[0]))
        _, W = wvals(g, a["s"], a["t"]); a["W"] = W; a["R"] = reach(g, a["s"], a["t"], o)
        a["h1"] = not oncycle(g, a["s"], a["sb"], o); a["h2"] = not oncycle(g, a["s"], a["t"], o)
        if a["h2"]:
            om = a["t"][o]; a["D"] = {e for e in ex if e != o and e not in a["R"] and E.key(a["Xi"][e]) < E.key(a["Xi"][om])}
            c["maxD"] = max(c["maxD"], len(a["D"]))
    released = set()
    for i in range(len(out) - 1):
        a, b = out[i], out[i + 1]
        if a["key"] != b["key"]: released = set(); continue
        M = a["M"]; tame = all(coarse(b["Xi"][v], M) == coarse(a["Xi"][v], M) for v in range(n))
        scope = a["h1"] and a["h2"] and b["h2"] and a["W"][o] == b["W"][o] and (NOH3 or a["Xi"][o][0] == a["W"][o][0])
        if not tame: c["J_in" if scope else "J_out"] += 1
        if not scope: released = set(); continue
        if not tame:
            c["relnj_chk"] += 1; c["D1p"] += 1
            if a["sb"][o] in released: c["relnj_viol"] += 1; res.append(("REL-NJ", i, a["sb"][o]))
            if a["sb"][o] not in a["D"]: c["D1pviol"] += 1; res.append(("D1'", i))
        c["chk"] += 1; sa = a["sb"][o]
        if E.key(a["Xi"][o]) < E.key(a["W"][o]) and a["Xi"][o][0] == a["W"][o][0]:
            c["D1"] += 1
            if sa not in a["D"]: c["D1viol"] += 1; res.append(("D1", i))
        rel = {e for e in ex if e in a["R"] and e not in b["R"] and e != o}
        if not b["D"] <= a["D"] | rel: c["D2viol"] += 1; res.append(("D2", i, sorted(b["D"] - a["D"] - rel)))
        for e in b["D"] & rel: c["rel_fb" if a["fb"] else "rel_ar"] += 1; released.add(e)
        if not tame:
            c["D3"] += 1
            if sa in b["D"]: c["D3viol"] += 1; res.append(("D3", i))
    return c, res

if __name__ == "__main__":
    T = {}
    for p in sys.argv[1:]:
        g = load(p); c, r = scan_d(g)
        for kk, v in c.items(): T[kk] = max(T.get(kk, 0), v) if kk.startswith("max") else T.get(kk, 0) + v
        if r or c["J_in"] or c["J_out"] or c["rel_fb"] or c["rel_ar"]: print(f"{os.path.basename(p):22s}", c, r[:3])
    print("TOTAL", T)
