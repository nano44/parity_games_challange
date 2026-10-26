#!/usr/bin/env python3
"""L-SI succ. 5, box 10: DATA for CONJECTURE RISE-LAST (L-RED R68 §6). Per scope run (reltrace.runs_of), each COARSE_L(θ) rise after an
in-scope fallback (L := the level of the last fallback before it): the transitions left in the run, why the run ends (end of game /
phase change (λ_Ξ or τ) / ¬(h) at the next state / w changes), r right after the rise, and the next fallback anywhere after the rise.
Usage: rlprobe.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "coarse"))
from reltrace import *

def why_end(out, i, o):
    if i + 1 >= len(out): return "END"
    a, b = out[i], out[i + 1]
    if a["key"] != b["key"]: return "PHASE"
    if not a["h"]: return "noh_a"
    if not b["h"]:
        g1 = "H1" if b["Xi"][o][0] != b["W"][o][0] else "h"
        return "noh_b"
    if a["W"][o] != b["W"][o]: return "WCHG"
    return "?"

def scan(g, name):
    runs, d_o, exits, out = runs_of(g, name); o = odd_choice(g); C = Counter(); rows = []
    for S in runs:
        L = None
        for t, e in enumerate(S):
            if e["k"] == "F": L = e["M"]; continue
            if L is None or e["lt"] <= L: continue
            C["rises"] += 1; i = e["i"]; last = S[-1]["i"]
            nfb_run = sum(1 for u in S[t + 1:] if u["k"] == "F")
            nxt = next((k for k in range(i + 1, len(out)) if out[k]["fb"]), None)
            why = why_end(out, last + 1, o) if last + 1 < len(out) else "END"
            rows.append((name, i, L, e["lt"], e["r"], S[t + 1]["r"] if t + 1 < len(S) else None, last - i, why, nfb_run,
                         None if nxt is None else nxt - i))
            C["fb_in_run_after"] += nfb_run; C["end_" + why] += 1
    return C, rows

if __name__ == "__main__":
    T = Counter(); X = []
    for p in sys.argv[1:]:
        g = load(p)
        assert sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1) == 1, p
        c, r = scan(g, os.path.basename(p)); T.update(c); X += r
    print("TOTAL", dict(T))
    print("name i L lt r r_next left_in_run why_end fb_in_run_after next_fb_dist")
    for r in X: print(*r)
