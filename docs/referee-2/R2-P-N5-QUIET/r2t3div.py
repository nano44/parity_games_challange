#!/usr/bin/env python3
"""REFEREE-2 succ. 33: where do the Howard runs on Γ(G) and Γ3(G) (own r2acyc builder/VJ/Odd PI; Howard at movers, ties -> largest
vertex id, keep current if best) first differ? Prints per genome (index in a .jsonl): T, T3, first state s with different mover choices,
and at s - 1 the sets of ⊴-best options per mover on Γ and on Γ3 (option indices), and whether each set has > 1 element (a Howard tie).
Usage: r2t3div.py SET.jsonl IDX ..."""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2-P-ACYC")); import r2acyc as A
A.EORDER = "lev"
def run(G, pads):
    g = A.build(G, pads); vj = A.VJ(g); V = g["V"]; ms = list(G["start"]); out = []
    while True:
        sig = A.mover_sig(g, ms); tau, val = A.odd_opt(g, vj, sig, A.worst_start(g)); best = []
        new = list(ms); ch = False
        for x in range(g["N"]):
            s = g["succ"][V[("x", x)]]; b = max(range(len(s)), key=lambda k: A.cmp_to_key(lambda a, c: vj.cmp(val[s[a]], val[s[c]]))(k))
            bl = [k for k in range(len(s)) if vj.cmp(val[s[k]], val[s[b]]) == 0]; best.append(bl)
            if vj.cmp(val[s[b]], val[s[ms[x]]]) > 0: new[x] = max(bl, key=lambda k: s[k]); ch = True
        out.append((tuple(ms), best))
        if not ch: return out
        ms = new
lines = open(sys.argv[1]).read().split("\n")
for i in map(int, sys.argv[2:]):
    G = json.loads(lines[i]); a, b = run(G, False), run(G, True)
    s = next((k for k in range(min(len(a), len(b))) if a[k][0] != b[k][0]), min(len(a), len(b)))
    print(f"#{i} N {G['N']} T {len(a) - 1} T3 {len(b) - 1} first diff state {s}; at {s - 1}: best Γ {a[s - 1][1]} best Γ3 {b[s - 1][1]}")
