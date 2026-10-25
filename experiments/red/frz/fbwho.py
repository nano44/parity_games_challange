#!/usr/bin/env python3
"""Box 41: for each in-phase Even fallback, which vertices S4c switches: in U (λ = c_θ) or not, cycle node (λ(v) = v) or not, and
σ(v) ∈ R̄ or not. Per θ-run: |U|, #fallbacks. Usage: fbwho.py game.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "so"))
import sox, pfz17
g = sox.load(sys.argv[1]); rows, o, E = pfz17.states(g); N = len(rows)
for k in range(N - 1):
    r, r1 = rows[k], rows[k + 1]
    if not r["fb"]: continue
    inph = r1["lam"] == r["lam"] and r1["t"] == r["t"]
    ct = r["Xi"][o][0]; U = {z for z in range(g.n) if r["Xi"][z][0] == ct}
    sw = [v for v in range(g.n) if g.owner[v] == 0 and r["s"][v] != r1["s"][v]]
    cls = [(v, "U" if v in U else "out", "cyc" if r["Xi"][v][0] == v else "", "sigR" if (r["s"][v] in r["R"] or r["s"][v] == o) else "") for v in sw]
    print(k, "inphase" if inph else "PHASE-END", "|U|", len(U), "theta", r["Xi"][o], "->", r1["Xi"][o], "h1h2", r["h1"], r["h2"], cls)
