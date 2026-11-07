#!/usr/bin/env python3
"""L-RED 55 R219 (a): independent ascent-gate classifier on own.py runs (cf. L-NEW box 193 asc193.py; no code shared).
For each state t and mover v with Lambda_t(v) less relevant than every e: seq(v) = e-vertices of Pi_t(v) in play order. For each ascent
(a, b) (consecutive, rank(b) > rank(a)), each gate h strictly between a and b on the play (Odd takes beta there) is classified
ASC-GATE case i (Lambda(e_h) != Lambda(beta_h)), ii (b on e_h's play), iii (e_h's pre-merge part has an e above b), first that holds.
Per (gate, state) the case set is recorded once. RELEASE: h classified at t and sigma_bar_(t+1)(h) = e. REARM: a release followed later
by a return to beta. Prints counts per case: (gate,state) pairs, releases, re-arms, max flips over gates of that case.
Usage: asc219.py G.json ..."""
import sys, json
import own
def analyse(f):
    G = json.load(open(f)); out, V, O, ow = own.run(G); n, prio, o_, succ, _, _ = own.build(G); vj = own.VJ(prio); rk = vj.rk; N = G["N"]
    evs = {V[("e", q)]: q for q in O}; gof = {V[("g", q)]: q for q in O}; emin = min(rk[e] for e in evs)
    seen_case = {}  # (h, t) -> case
    for t, (s, vals, tau) in enumerate(out):
        nxt = lambda v: (s[v] if v < N else (tau[v] if o_[v] == 1 else succ[v][0]))
        def play(v):
            p, pos = [], {}
            while v not in pos: pos[v] = len(p); p.append(v); v = nxt(v)
            return p, pos[v]
        for v in range(N):
            lam = vals[v][0]
            if rk[lam] >= emin: continue
            p, c = play(v); Pi = vals[v][1]
            ep = [i for i, u in enumerate(p) if u in evs and u in Pi]
            for i0, i1 in zip(ep, ep[1:]):
                a, b = p[i0], p[i1]
                if rk[b] <= rk[a]: continue
                for j in range(i0 + 1, i1):
                    h = p[j]
                    if h not in gof or (h, t) in seen_case: continue
                    q = gof[h]; eh, bh = V[("e", q)], V[("b", q)]
                    if tau[h] != bh: continue          # the gate whose e-face IS b (the play enters b there): not a declined gate
                    if vals[eh][0] != vals[bh][0]: seen_case[(h, t)] = "i"; continue
                    pe, _ = play(eh); pb, _ = play(bh); sb = set(pb)
                    if b in pe: seen_case[(h, t)] = "ii"; continue
                    pre = []
                    for u in pe:
                        if u in sb: break
                        pre.append(u)
                    seen_case[(h, t)] = "iii" if any(u in evs and rk[u] > rk[b] for u in pre) else "FAIL"
    face = lambda t, h: out[t][2][h] == V[("e", gof[h])]
    res = {}
    for (h, t), c in seen_case.items():
        r = res.setdefault(c, [0, 0, 0, set()]); r[0] += 1; r[3].add(h)
        if t + 1 < len(out) and face(t + 1, h):
            r[1] += 1
            if any(not face(u, h) for u in range(t + 2, len(out))): r[2] += 1
    fl = lambda h: sum(face(t, h) != face(t - 1, h) for t in range(1, len(out)))
    row = " | ".join(f"{c}: pairs {r[0]} gates {len(r[3])} releases {r[1]} rearms {r[2]} maxflips {max(fl(h) for h in r[3])}" for c, r in sorted(res.items()))
    print(f"{f.split('/')[-1]} N {N} T {len(out) - 1} || {row}", flush=True)
for f in sys.argv[1:]:
    J = json.load(open(f))
    if isinstance(J, dict) and "N" in J and "opts" in J: analyse(f)
