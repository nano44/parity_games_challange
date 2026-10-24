#!/usr/bin/env python3
"""Per-iteration trace of N5 on a labelled game: the gate I_sigma, I_tau and the switches made, by vertex label.
Usage: meitrace.py game.pg [startfile] [--switchall]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
for d in ("../../harness", "../../si", "../../new", "../../si/orlens"): sys.path.insert(0, os.path.join(HERE, d))
import ortrace as OT
args = [a for a in sys.argv[1:] if not a.startswith("--")]
g, st = OT.load(args[0], args[1] if len(args) > 1 else None)
L = g.labels or [str(v) for v in range(g.n)]
E, Ed, S, fb, (it, nfb) = OT.run_states(g, st, mode="switchall" if "--switchall" in sys.argv else "n5")
lab = lambda es: " ".join(f"{L[v]}>{L[w]}" for v, w in sorted(es))
for k, s in enumerate(S):
    sig, tau, vs, sbar, vt, tbar, Is, It = s
    print(f"[{k}] Is: {lab(Is)} | It: {lab(It)}")
    if k + 1 < len(S):
        ns, nt = S[k + 1][0], S[k + 1][1]
        print(f"     sigma: {lab((v, ns[v]) for v in range(g.n) if ns[v] != sig[v])}  tau: {lab((v, nt[v]) for v in range(g.n) if nt[v] != tau[v])}"
              f"  sbar-tau mismatch: {lab((v, sbar[v]) for v in range(g.n) if g.owner[v] == 1 and sbar[v] != tau[v])}  fb={fb[k]}")
print(f"iterations={it} fallback={nfb}")
