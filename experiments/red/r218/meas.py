#!/usr/bin/env python3
"""L-RED 55 R218: measure an own.py run of a named genome: T; bit word per state (bits = movers named B<k>, '1' iff on option SET
and its gate's face is e); re-arms = switches INTO an option labelled X (lane / F exits) per mover; D(v) = distinct values of Omega(v)
for named movers (default H). Usage: meas.py G.json [names...]"""
import sys, json
import own
f = sys.argv[1]; G = json.load(open(f)); nm = json.load(open(f[:-5] + ".names.json")); lab = json.load(open(f[:-5] + ".labels.json"))
inv = {v: k for k, v in nm.items()}; out, V, O, ow = own.run(G); ig = {V[("g", q)]: q for q in O}
bits = sorted((k for k in nm if k[0] == "B" and k[1:].isdigit()), key=lambda k: -int(k[1:]))
def word(s, tau):
    w = ""
    for bn in bits:
        x = nm[bn]; q = ig[s[x]]; w += "1" if lab[bn][q[1]] == "SET" and tau[V[("g", q)]] == V[("e", q)] else "0"
    return w
words = [word(s, tau) for s, _, tau in out]
comp = [words[0]] + [w for i, w in enumerate(words[1:], 1) if w != words[i - 1]]
rearm = {}
for t in range(1, len(out)):
    for x in range(G["N"]):
        k0, k1 = ig[out[t - 1][0][x]][1], ig[out[t][0][x]][1]
        if k0 != k1 and lab[inv[x]][k1] == "X": rearm[inv[x]] = rearm.get(inv[x], 0) + 1
Dn = sys.argv[2:] or ["H"]
Dv = {m: len(set(vals[nm[m]] for _, vals, _ in out)) for m in Dn if m in nm}
print(f"{f.split('/')[-1]} N {G['N']} T {len(out) - 1} words {len(comp)}: {' '.join(comp)}")
print(f"  re-arms (switches into X) total {sum(rearm.values())} max/mover {max(rearm.values(), default=0)}; D {Dv}")
