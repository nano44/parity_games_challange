#!/usr/bin/env python3
"""L-SI succ. 7, box 12: DATA for Lemma XG and the U-play anatomy at in-scope THR fallbacks (docs/si/N5-LV3-box12.md).
σ* := Even's optimal G_τ strategy returned by the dual engine (Ed.evaluate(τ)'s Odd choices on G^d), U := its valuation (= Ξτ, G's order).
Per THR fallback (run states and PERT perturbed start pairs per state):
  XG   : every y ∈ R with z = σ*(y) ∈ F whose σ*-play stays in F gives a gate (y, z) of level >= r   [checked, counted]
  kind : the U-play from x0: 'o' (reaches o), 'F' (after its last R̄ -> F step it stays in F; then XG applies), 'RC' (its cycle meets R)
  CR   : for kind RC, the cycle node c* of the U-play: rank c* <= r whenever M < r (the COARSE_r telescoping prediction)
Usage: xg.py SEED PERT game.pg ..."""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import betasearch as B
from betasearch import *

def ranks(g):
    rk = sorted(range(g.n), key=lambda u: (g.prio[u], u)); return {v: i for i, v in enumerate(rk)}

def anat(g, o, a, E, Ed, rk, C, M, r, ex, name):
    s, t, Xi, W, R = a["s"], a["t"], a["Xi"], a["W"], a["R"]; Rb = R | {o}
    U, sst = Ed.evaluate(tuple(t))
    nxt = lambda v: sst[v] if g.owner[v] == 0 else t[v]
    def play(v):
        p = [v]
        while nxt(p[-1]) not in p: p.append(nxt(p[-1]))
        return p, p.index(nxt(p[-1]))
    gl = {(y, z): lev(Xi[s[y]], Xi[z]) for y, z in a["Is"]}
    for y in R:
        if g.owner[y] != 0: continue
        z = sst[y]
        if z in Rb: continue
        p, _ = play(z)
        if all(v not in Rb for v in p):
            C["XG_cases"] += 1
            if (y, z) not in gl: C["XG_FAIL_notgate"] += 1; ex.setdefault("XG_notgate", (name, y, z))
            elif gl[(y, z)] < r: C["XG_FAIL_low"] += 1; ex.setdefault("XG_low", (name, y, z, gl[(y, z)], r))
            else: C["XG_ok"] += 1
    p, ci = play(a["sb"][o])
    sbo = a["sb"]
    def nonexc(seq):
        """indices of Even vertices v on seq (excluding the last) whose σ*-edge is a NON-exceptional Ξ-gate (exceptional: v is its own
        Ξ-cycle node and Ξ(z) = (v, ∅, ·)); seq is a vertex sequence along σ*."""
        out = []
        for v in seq:
            if g.owner[v] != 0 or sst[v] == s[v]: continue
            z = sst[v]
            if (v, z) not in gl: continue
            exc = Xi[v][0] == v and Xi[z][0] == v and Xi[z][1] == 0
            if not exc: out.append((v, z, gl[(v, z)]))
        return out
    if o in p:
        lam = p[:p.index(o)]; rest = p[p.index(o) + 1:]
        A2 = ci <= p.index(o)
        C["A2" if A2 else "A1"] += 1
        if not A2:
            if nonexc(lam) or nonexc(rest): C["A1_uses_nonexc_gate"] += 1
            else: C["A1_FAIL"] += 1; ex.setdefault("A1", (name, p))
        else:
            C["A2_uses_nonexc_gate"] += bool(nonexc(p))
    else:
        if nonexc(p): C["B_uses_nonexc_gate"] += 1
        else: C["B_FAIL"] += 1; ex.setdefault("B", (name, p))
    if o in p: kind = "o"
    else:
        cyc = p[ci:]
        kind = "RC" if any(v in R for v in cyc) else "F"
        if kind == "RC":
            cs = max(cyc, key=lambda v: rk[v])
            C[f"RC_M{'<' if M < r else '>='}r"] += 1
            if M < r:
                if rk[cs] <= r: C["CR_ok"] += 1
                else: C["CR_FAIL"] += 1; ex.setdefault("CR", (name, cs, rk[cs], r, M))
    C["kind_" + kind] += 1

def main(seed, pert, files):
    rng = random.Random(seed); C = Counter(); ex = {}
    for p in files:
        g = load(p); o = odd_choice(g)
        if o is None or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1) != 1: continue
        E, Ed = n5.Engine(g), n5.Engine(n5.dual(g)); B.E_key = E.key; rk = ranks(g)
        try: _, out = states(g)
        except AssertionError: continue
        ev = [v for v in range(g.n) if g.owner[v] == 0 and len(set(g.succ[v])) > 1]
        cands = [(out[i]["s"], out[i]["t"]) for i in range(len(out) - 1)]
        for i in range(len(out)):
            for _ in range(pert):
                s, t = list(out[i]["s"]), list(out[i]["t"])
                for v in rng.sample(ev, min(len(ev), rng.randint(1, 3))): s[v] = rng.choice(g.succ[v])
                if rng.random() < 1 / 3: t[o] = rng.choice(g.succ[o])
                cands.append((tuple(s), tuple(t)))
        for s, t in cands:
            a = info(g, E, Ed, o, s, t)
            if not a["fb"]: continue
            b = info(g, E, Ed, o, a["ns"], a["nt"]); c = classify(g, o, a, b)
            if not isinstance(c, tuple): continue
            r, M, kinds = c; C["THR"] += 1
            if r < 0: C["THR_r=-1"] += 1; continue
            anat(g, o, a, E, Ed, rk, C, M, r, ex, os.path.basename(p))
    print("TOTAL", dict(sorted(C.items())))
    for k, v in ex.items(): print("EX", k, v)

if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3:])
