#!/usr/bin/env python3
"""L-SI box 83: tiny genome DSL (own; same JSON as R104's IDEAL genome / box 193: opts[x][k] = [W-target, Xi-target, beta id]).
mv(name, level); opt(x, wt|None, xt|None, beta_key, parity, gate_key, label): wt None = e-face to c_W (Odd never takes it),
xt None = beta escapes to u = K0. Beta ranks = order of beta keys; e order inside a level = order of (gate key, (mover, option)) as R217 gdsl ([E-LEV]: by (level, gate)).
genome(start) -> (G, names) with names = {"movers": [...], "opts": [[label, ...], ...]}."""
import json
class Gen:
    def __init__(s): s.names = []; s.lev = {}; s.opts = {}
    def mv(s, nm, lv): s.names.append(nm); s.lev[nm] = lv; s.opts[nm] = []; return nm
    def opt(s, x, wt, xt, bkey, par, gkey, label): s.opts[x].append((wt, xt, bkey, par, gkey, label))
    def genome(s, start=None):
        ix = {nm: i for i, nm in enumerate(s.names)}; N = len(s.names); betas = []; opts = []; gk = []; labs = []
        for x in s.names:
            o = []; l = []
            for (wt, xt, bk, par, g, lab) in s.opts[x]:
                o.append([ix[wt] if wt else -1, ix[xt] if xt else -1, len(betas)]); betas.append((bk, par)); gk.append(g); l.append(lab)
            opts.append(o); labs.append(l)
        assert len({b[0] for b in betas}) == len(betas), "beta keys must be distinct"
        order = sorted(range(len(betas)), key=lambda b: betas[b][0]); br = [0] * len(betas)
        for r, b in enumerate(order): br[b] = r
        q = [(xi, k) for xi in range(N) for k in range(len(opts[xi]))]
        qs = sorted(q, key=lambda qq: (gk[opts[qq[0]][qq[1]][2]], qq)); gate = [[0] * len(o) for o in opts]
        for i, qq in enumerate(qs): gate[qq[0]][qq[1]] = i
        st = [0] * N
        for nm, k in (start or {}).items(): st[ix[nm]] = k
        G = {"N": N, "lev": [s.lev[x] for x in s.names], "opts": opts, "gate": gate, "br": br, "bp": [b[1] for b in betas], "start": st}
        return G, {"movers": list(s.names), "opts": labs}
def save(G, names, path):
    json.dump(G, open(path, "w")); json.dump(names, open(path[:-5] + ".names.json", "w"))
