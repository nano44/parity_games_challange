#!/usr/bin/env python3
"""Box 192: MERGE types of R-flips. At an R-flip at gate g (state t+1, after the flip) classify by MERGE's first common vertex m of the
plays P_A (from e_g) and P_B (from beta_g): RET = m is e_g (the beta-play runs back through g and then through e_g, A' empty);
DISJ = A', B' both non-empty. Also records whether the decisive vertex is an e or a beta. Usage: mtype192.py FILES.json"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import rpot192

def play(h, sigma, sb, v):
    seen = []; s = set()
    while v not in s:
        seen.append(v); s.add(v); v = sigma[v] if h.owner[v] == 0 else sb[v]
    return seen

def analyse(G):
    h, E, V, name, movers, ev = rpot192.states(G)
    import idealcyc
    # reconstruct strategies: Even succ: movers from run, others frozen
    hh, s0, mv, inv = idealcyc.build(G); st = idealcyc.run(G)
    gi = {}
    for x in range(G["N"]):
        for v in hh.succ[mv[x]]: gi[(x, inv[v])] = v
    cnt = {}
    for t in range(1, len(ev)):
        (pv, ps), (vs, sb) = ev[t - 1], ev[t]
        if any(pv[v][0] != vs[v][0] for v in range(h.n)): continue
        cur = list(s0)
        for x in range(G["N"]): cur[mv[x]] = gi[(x, st[t][x])]
        for g in range(h.n):
            if h.owner[g] != 1 or name[g][0] != "g" or ps[g] == sb[g]: continue
            q = name[g][1]; e, b = V[("e", q)], V[("b", q)]
            PA, PB = play(h, cur, sb, e), play(h, cur, sb, b)
            m = next(v for v in PA if v in set(PB))
            typ = "RET" if m == e else ("BRET" if m == b else "DISJ")
            to = "e" if sb[g] == e else "b"
            cnt[(typ, to)] = cnt.get((typ, to), 0) + 1
    return cnt

if __name__ == "__main__":
    tot = {}
    for f in sys.argv[1:]:
        c = analyse(json.load(open(f)))
        for k, v in c.items(): tot[k] = tot.get(k, 0) + v
        print(os.path.basename(f), sorted(c.items()))
    print("TOTAL", sorted(tot.items()))
