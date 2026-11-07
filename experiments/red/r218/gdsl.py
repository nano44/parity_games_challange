#!/usr/bin/env python3
"""L-RED 54 R217: tiny genome DSL. Movers by name with level; options (wt name|None, xt name|None('u'), beta key, parity, gate key).
Beta ranks follow the sorted beta keys; e order within a level follows gate keys. start = option 0."""
import json
class Gen:
    def __init__(s): s.names = []; s.lev = {}; s.opts = {}
    def mv(s, nm, lv): s.names.append(nm); s.lev[nm] = lv; s.opts[nm] = []; return nm
    def opt(s, x, wt, xt, bkey, par, gkey=(0,)): s.opts[x].append((wt, xt, bkey, par, gkey))
    def genome(s, start=None):
        ix = {nm: i for i, nm in enumerate(s.names)}; N = len(s.names); betas = []; opts = []; gk = []
        for x in s.names:
            o = []
            for (wt, xt, bk, par, g) in s.opts[x]:
                o.append([ix[wt] if wt else -1, ix[xt] if xt else -1, len(betas)]); betas.append((bk, par)); gk.append(g)
            opts.append(o)
        order = sorted(range(len(betas)), key=lambda b: betas[b][0]); br = [0] * len(betas)
        for r, b in enumerate(order): br[b] = r
        q = [(xi, k) for xi in range(N) for k in range(len(opts[xi]))]; flat = {qq: i for i, qq in enumerate(q)}
        qs = sorted(q, key=lambda qq: (gk[opts[qq[0]][qq[1]][2]], qq)); gate = [[0] * len(o) for o in opts]
        for i, qq in enumerate(qs): gate[qq[0]][qq[1]] = i
        st = [0] * N
        if start:
            for nm, k in start.items(): st[ix[nm]] = k
        return {"N": N, "lev": [s.lev[x] for x in s.names], "opts": opts, "gate": gate, "br": br, "bp": [b[1] for b in betas], "start": st}, ix
