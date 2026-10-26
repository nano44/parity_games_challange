#!/usr/bin/env python3
"""L-SI succ. 7, box 12: DATA for Lemma STALE-GATE and Corollary EV-G (docs/si/N5-LV4-box12.md).
STALE-GATE: k0 an S4c fallback at which Even switches, k > k0 in the same run: every gate (y, z) at k has Ξ_k(z) ≠ Ξ_{k0}(z).
EV-G: k0 an in-phase THR S4c fallback with (h), k > k0 in the same phase: every gate target z ∈ F_k has its σ_k-play leaving F_{k0}.
(Checked for all pairs; the phase key is reltrace's (λ_Ξ, τ, λ_U).) Usage: stale.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import betasearch as B
from betasearch import *

def main(files):
    C = Counter(); ex = []
    for p in files:
        g = load(p); o = odd_choice(g)
        if o is None: continue
        E, Ed = n5.Engine(g), n5.Engine(n5.dual(g)); B.E_key = E.key
        try: _, out = states(g)
        except AssertionError: continue
        A = [info(g, E, Ed, o, x["s"], x["t"]) for x in out]
        for k0 in range(len(A) - 1):
            a0 = A[k0]
            if not a0["fb"] or not a0["Is"]: continue
            thr0 = a0["h"] and E.key(a0["Xi"][o]) < E.key(a0["W"][o])
            F0 = set(range(g.n)) - a0["R"] - {o}
            for k in range(k0 + 1, len(A)):
                a = A[k]
                for y, z in a["Is"]:
                    C["SG_checks"] += 1
                    if a["Xi"][z] == a0["Xi"][z]: C["SG_FAIL"] += 1; ex.append(("SG", p, k0, k, y, z))
                if thr0 and a["key"] == a0["key"]:
                    Fk = set(range(g.n)) - a["R"] - {o}
                    nxt = lambda v: a["s"][v] if g.owner[v] == 0 else a["t"][v]
                    for y, z in a["Is"]:
                        if z not in Fk: continue
                        pl = [z]
                        while nxt(pl[-1]) not in pl: pl.append(nxt(pl[-1]))
                        C["EVG_checks"] += 1
                        if all(v in F0 for v in pl): C["EVG_FAIL"] += 1; ex.append(("EVG", p, k0, k, y, z))
                if a["key"] != a0["key"]: pass
    print("TOTAL", dict(sorted(C.items())))
    for e in ex[:10]: print("EX", e)

if __name__ == "__main__":
    main(sys.argv[1:])
