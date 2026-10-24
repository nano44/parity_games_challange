#!/usr/bin/env python3
"""Box 29 (NH'): per phase ((λ_Ξ, λ_U, τ(o)) constant), the OTHER-touching transitions split into crossing ones (already charged
to X by Theorem X) and NON-crossing ones (O'), by the clause pattern of the OTHER endpoint(s) and by kind (arena / fallback,
value-changing or not). OTHER := (h) fails and Ξ ≠ W. Usage: otherx.py game.pg [start] | otherx.py --rand N lo hi seed [--randstart]"""
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../box28"))
from fbre import *

def phases(g, start=None):
    rows, ph = profile(g, start); o = odd_choice(g)
    for r in rows:
        r["R"] = reach_o(g, r["s"], r["t"], o); r["other"] = (not all(r["h"])) and r["Xk"] != r["Wk"]
    out = []
    for (x, y) in ph:
        st = dict(phase=(x, y), it=y - x, O=0, Ocross=0, Oprime=0, Oprime_vc=0, Oprime_fb=0, pat={})
        for k in range(x, y):
            a, b = rows[k], rows[k + 1]
            if not (a["other"] or b["other"]): continue
            st["O"] += 1
            if a["R"] != b["R"]: st["Ocross"] += 1; continue
            st["Oprime"] += 1; vc = a["Xk"] != b["Xk"] or a["Wk"] != b["Wk"]; st["Oprime_vc"] += vc; st["Oprime_fb"] += bool(a["fb"])
            p = "/".join(clause(r["h"]) + ("s" if r["split"] else "c") for r in (a, b) if r["other"])
            st["pat"][p] = st["pat"].get(p, 0) + 1
        out.append(st)
    return rows, out

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] != "--rand":
        g = load(a[0]); _, out = phases(g, readstart(a[1]) if len(a) > 1 else None)
        for st in out:
            if st["O"]: print(os.path.basename(a[0]), "n", g.n, st)
        sys.exit()
    RS = "--randstart" in a; N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
    tot = dict(runs=0, O=0, Ocross=0, Oprime=0, Oprime_vc=0, Oprime_fb=0); pat = {}; best = (0, None)
    for i in range(N):
        g = rand_c1o(rng, lo, hi, forced=0.0)
        if g is None: continue
        start = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                 {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
        _, out = phases(g, start); tot["runs"] += 1
        for st in out:
            for kk in ("O", "Ocross", "Oprime", "Oprime_vc", "Oprime_fb"): tot[kk] += st[kk]
            for p, c in st["pat"].items(): pat[p] = pat.get(p, 0) + c
            if st["Oprime_vc"] > best[0]: best = (st["Oprime_vc"], g.n)
    print(tot, "max value-changing O' per phase", best); print("patterns of O':", dict(sorted(pat.items(), key=lambda kv: -kv[1])))
