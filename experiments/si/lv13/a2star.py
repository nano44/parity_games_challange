#!/usr/bin/env python3
"""L-SI succ. 8, box 13: DATA for the A2* closing argument (docs/si/N5-A2STAR-box13.md). At in-scope THR fallbacks with r >= 0 (run states
and perturbed start pairs, as experiments/si/lv/xg.py, whose helpers are imported), for the U-play P from x0 whose cycle K' contains o:
  shape A2*: the top m' of K' lies after o, and every vertex of lam + {o} (lam := P before o) ranks below m'.
  checks on A2* shapes: (F-a) U(x0) >= U(t); m' odd; c = m' or (c odd and rank c > rank m'); rew(m_K) > rew(c);
  and lam carries a non-exceptional Xi-gate on a sigma*-edge (the data form of "the sigma'' argument must fail on lam").
Usage: a2star.py SEED PERT game.pg ..."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "lv"))
import betasearch as B
from betasearch import *
from xg import ranks

def rew(g, rk, v): pp = 2 * rk[v] + (g.prio[v] % 2); return pp if g.prio[v] % 2 == 0 else -pp

def check(g, o, a, Ed, rk, C, ex, name):
    s, t, Xi = a["s"], a["t"], a["Xi"]; U, sst = Ed.evaluate(tuple(t))
    nxt = lambda v: sst[v] if g.owner[v] == 0 else t[v]
    x0 = a["sb"][o]; p = [x0]
    while nxt(p[-1]) not in p: p.append(nxt(p[-1]))
    ci = p.index(nxt(p[-1]))
    if o not in p or ci > p.index(o): return
    io = p.index(o); K2 = p[ci:]; mp = max(K2, key=lambda v: rk[v]); lam = p[:io]
    C["cycle_through_o"] += 1
    if p.index(mp) <= io or any(rk[v] >= rk[mp] for v in lam + [o]): return
    C["A2star_shape"] += 1; c = Xi[o][0]; mK = max(lam + [o], key=lambda v: rk[v]); tt = t[o]
    if E_key(U[x0]) < E_key(U[tt]): C["FAIL_Fa"] += 1; ex.setdefault("Fa", (name, p))
    if g.prio[mp] % 2 == 0: C["FAIL_mprime_even"] += 1; ex.setdefault("mpe", (name, p))
    if not (c == mp or (g.prio[c] % 2 == 1 and rk[c] > rk[mp])): C["FAIL_c"] += 1; ex.setdefault("c", (name, p, c))
    if not rew(g, rk, mK) > rew(g, rk, c): C["FAIL_rew"] += 1; ex.setdefault("rew", (name, p, mK, c))
    gl = {(y, z) for y, z in a["Is"]}
    ne = [v for v in lam if g.owner[v] == 0 and sst[v] != s[v] and (v, sst[v]) in gl
          and not (Xi[v][0] == v and Xi[sst[v]][0] == v and Xi[sst[v]][1] == 0)]
    C["lam_has_nonexc_gate" if ne else "FAIL_lam_no_nonexc_gate"] += 1
    if not ne: ex.setdefault("lam", (name, p))

def main(seed, pert, files):
    rng = random.Random(seed); C = Counter(); ex = {}
    for p in files:
        g = load(p); o = odd_choice(g)
        if o is None or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1) != 1: continue
        E, Ed = n5.Engine(g), n5.Engine(n5.dual(g)); B.E_key = E.key; rk = ranks(g); globals()["E_key"] = E.key
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
            if r < 0: continue
            C["THR_r>=0"] += 1; check(g, o, a, Ed, rk, C, ex, os.path.basename(p))
    print("TOTAL", dict(sorted(C.items())))
    for k, v in ex.items(): print("EX", k, v)
if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3:])
