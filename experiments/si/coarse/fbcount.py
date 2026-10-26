#!/usr/bin/env python3
"""L-SI box 7: DATA check of Theorem FB (docs/si/N5-C-box7.md §4). Inside each joint λ-phase (λ_Ξ, λ_U, τ constant), cut the
transitions into BLOCKS: maximal runs of consecutive transitions with NC (mono.py) and constant M. Per block and Even vertex y,
β(y) := key of COARSE_{M-1}(Ξ(σ(y))) (full key when M = -1). Checks:
  (i) β(y) is non-decreasing inside a block (at every transition of the block);
  (ii) at every fallback transition of a block, some y with a level-M gate edge has β(y) strictly increased;
  (iii) every in-phase fallback has M < INF (mono.INF; 99 before box 9);
  (iv) #fallbacks in a block <= #Even vertices (M >= 0) or <= #Even·(n-1) (M = -1).
Reports per instance: fallbacks in phases, NC failures (INRs) in phases, blocks, max fallbacks per block, and the bound 2n²(1 + I).
Usage: fbcount.py game.pg ...   |   fbcount.py --random|--c1o SEED COUNT NMIN NMAX"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mono import *

def ckey(E, val, L):
    """engine key of COARSE_L(val): (reward of cycle node, weight of the path set restricted to ranks > L) (+ length if L < -1)"""
    if L >= -1: return (E.rew[val[0]], E.weight((val[1] >> (L + 1)) << (L + 1)))
    return E.key(val)

def scan(g, start=None):
    E, out = states(g, start); n = g.n; ev = [v for v in range(n) if g.owner[v] == 0]
    c = dict(tr=0, fb=0, inr=0, blocks=0, maxfb_block=0, viol_i=0, viol_ii=0, viol_iii=0, viol_iv=0, phases=0, worst_ratio=0.0)
    ex = []
    info = []
    for j in range(len(out)):
        a = out[j]
        gl = [lev(a["Xi"][a["s"][y]], a["Xi"][z]) for y, z in a["Is"]]; a["M"] = max(gl) if gl else -3
        a["key"] = (tuple(x[0] for x in a["Xi"]), a["t"])
    # λ_U: cycle nodes of Odd's dual valuation, as in the box 28 phase key
    Ed = n5.Engine(n5.dual(g))
    for a in out: a["key"] = a["key"] + (tuple(x[0] for x in Ed.evaluate(tuple(a["t"]))[0]),)
    def nc_at(j):
        a, b = out[j], out[j + 1]; lam = [a["Xi"][v][0] for v in range(n)]
        return all(lam[t] == t for t in (max(C, key=lambda v: E.rank[v]) for C in cycles(g, b["s"], a["sb"])))
    j = 0
    while j < len(out) - 1:
        # phase = maximal run of states with equal key
        k = j
        while k + 1 < len(out) and out[k + 1]["key"] == out[j]["key"]: k += 1
        c["phases"] += 1; fbp = inr = 0; blk = None; bfb = 0
        for i in range(j, k):
            a, b = out[i], out[i + 1]; c["tr"] += 1; nc = nc_at(i)
            if a["fb"]:
                fbp += 1
                if a["M"] >= INF: c["viol_iii"] += 1; ex.append(("iii", i))
            if not nc: inr += 1; blk = None; continue
            if blk is None or blk != a["M"]:
                if bfb: c["maxfb_block"] = max(c["maxfb_block"], bfb)
                blk = a["M"]; bfb = 0; c["blocks"] += 1
            M = a["M"]
            ba = {y: ckey(E, a["Xi"][a["s"][y]], M - 1) for y in ev}
            bb = {y: ckey(E, b["Xi"][b["s"][y]], M - 1) for y in ev}
            if any(bb[y] < ba[y] for y in ev): c["viol_i"] += 1; ex.append(("i", i))
            if a["fb"]:
                bfb += 1
                gt = {y for y, z in a["Is"] if lev(a["Xi"][a["s"][y]], a["Xi"][z]) == M}
                if not any(bb[y] > ba[y] for y in gt): c["viol_ii"] += 1; ex.append(("ii", i))
                cap = len(ev) if M >= 0 else len(ev) * (n - 1)
                if bfb > cap: c["viol_iv"] += 1; ex.append(("iv", i))
        if bfb: c["maxfb_block"] = max(c["maxfb_block"], bfb)
        c["fb"] += fbp; c["inr"] += inr
        if fbp: c["worst_ratio"] = max(c["worst_ratio"], fbp / (1 + inr))
        info.append((fbp, inr))
        j = k + 1
    c["max_fb_phase"] = max((f for f, _ in info), default=0); c["max_inr_phase"] = max((i for _, i in info), default=0)
    return c, ex

if __name__ == "__main__":
    T = {}
    def add(c):
        for k, v in c.items(): T[k] = max(T.get(k, 0), v) if k.startswith(("max", "worst")) else T.get(k, 0) + v
    if sys.argv[1] == "--c1o":   # random o-cyclic one-Odd-choice games (experiments/new/box25/common.py rand_c1o), random starts
        sys.path.insert(0, os.path.join(ROOT, "experiments/new/box25")); from common import rand_c1o
        seed, cnt, a, b = map(int, sys.argv[2:6]); rnd = random.Random(seed); EX = []; ng = 0
        for i in range(cnt):
            g = rand_c1o(rnd, a, b, forced=0.0)
            if g is None: continue
            assert odd_choice(g) is not None; ng += 1
            st = ({v: rnd.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                  {v: rnd.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1})
            c, ex = scan(g, st); add(c); EX += ex
        print("c1o", seed, ng, T, EX[:5]); sys.exit()
    if sys.argv[1] == "--random":
        seed, cnt, a, b = map(int, sys.argv[2:6]); rnd = random.Random(seed); EX = []
        for i in range(cnt):
            n = rnd.randint(a, b)
            prio = [rnd.randrange(n) for _ in range(n)]; own = [rnd.randrange(2) for _ in range(n)]
            succ = [sorted(set(rnd.sample(range(n), rnd.randint(1, min(3, n))))) for _ in range(n)]
            c, ex = scan(pg.Game(prio, own, succ)); add(c); EX += ex
        print("random", seed, cnt, T, EX[:5])
    else:
        for p in sys.argv[1:]:
            g = load(p); assert odd_choice(g) is not None, f"{p}: not one-Odd-choice"; c, ex = scan(g); add(c)
            print(f"{os.path.basename(p):22s} n {g.n:3d}", c, ex[:3])
        print("TOTAL", T)
