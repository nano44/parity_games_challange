#!/usr/bin/env python3
"""L-RED 65 R231 item (a): why Odd avoids e_(qh_k): per state, c_k's choice (option index; which Xi-target), Odd's face, the values
(Lambda, |Pi|) of e_g and beta_g with Lambda's name and priority parity, and the e-face play's first vertices.
Usage: ediag231.py G.json NAMES.json k [states]"""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r221q"))
import own
G = json.load(open(sys.argv[1])); nm = json.load(open(sys.argv[2])); kq = int(sys.argv[3]); N = G["N"]
out, V, O, ow = own.run(G, 20000); n, prio, _, succ, _, _ = own.build(G); inv = {v: k for k, v in V.items()}; rn = {v: k for k, v in nm.items()}
def nmv(u):
    k = inv[u]
    if isinstance(k, tuple) and k[0] == "x": return rn.get(k[1], f"x{k[1]}")
    if isinstance(k, tuple): return f"{k[0]}{k[1]}"
    return k
x = nm[f"qh{kq}"]; g, e, b = V[("g", (x, 0))], V[("e", (x, 0))], V[("b", (x, 0))]; ck = G["opts"][x][0][0]
sts = [int(a) for a in sys.argv[4].split(",")] if len(sys.argv) > 4 else range(len(out))
for t in sts:
    s, vals, tau = out[t]; ch = inv[s[ck]][1][1] if ck >= 0 else None
    nxt = lambda u: (s[u] if u < N else succ[u][0]) if ow[u] == 0 else tau[u]
    u = e; pl = []
    for _ in range(14): pl.append(nmv(u)); u = nxt(u) if u != g else e
    ve, vb = vals[e], vals[b]
    print(f"t {t}: c_k=x{ck} choice opt {ch} (Xi-target {G['opts'][ck][ch][1] if ck >= 0 else None}); face {'e' if tau[g] == e else 'b'}; "
          f"val(e) Λ {nmv(ve[0])} pr {prio[ve[0]]} |Π| {len(ve[1])}; val(β) Λ {nmv(vb[0])} pr {prio[vb[0]]} |Π| {len(vb[1])}; e-play {' '.join(map(str, pl))}")
