#!/usr/bin/env python3
"""Block-structured search for ZP (C3) call growth: K copies of a psolC-blind gadget (S_2 = psolc_min_n4_m6, or the C2
killers), priorities of block i shifted by 2*i*SHIFT (so blocks nest by priority), E random inter-block edges (random
owners kept), plus optional player swap per block. For each K: SAMPLES random games, record max and mean ZP calls and
plain Zielonka calls (plain skipped when > 1e6). Usage: zp_blocks.py KMAX SAMPLES SEED [--shift 1] [--edges-per-block 2]"""
import sys, os, json, random, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import alglib, pg, zielonka, zp, strfam


def build(K, rnd, shift, epb, gadgets):
    prio, owner, succ = [], [], []
    base = []
    for i in range(K):
        g = rnd.choice(gadgets)
        swap = rnd.random() < 0.5
        off = len(prio); base.append((off, g.n))
        for v in range(g.n):
            p = g.prio[v] + (1 if swap else 0)
            prio.append(p + 2 * i * shift)
            owner.append(g.owner[v] ^ (1 if swap else 0))
            succ.append([w + off for w in sorted(set(g.succ[v]))])
    n = len(prio)
    for i in range(K):
        for _ in range(epb):
            off, sz = base[i]
            v = off + rnd.randrange(sz)
            j = rnd.randrange(K)
            if j == i:
                continue
            w = base[j][0] + rnd.randrange(base[j][1])
            if w not in succ[v]:
                succ[v] = sorted(succ[v] + [w])
    return pg.Game(prio, owner, succ)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    KMAX, SAMPLES, seed = int(args[0]), int(args[1]), int(args[2])
    opt = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
    shift = int(opt("--shift", 1)); epb = int(opt("--edges-per-block", 2))
    rnd = random.Random(seed)
    gadgets = [strfam.S(2)]
    if "--c2" in sys.argv:
        gadgets += [alglib.from_record(json.loads(l)) for l in open(os.path.join(HERE, "out", "c2k1_small_seeds.jsonl"))]
    best = {}
    for K in range(1, KMAX + 1):
        mx, tot, mxplain, t0 = 0, 0, 0, time.time()
        for s in range(SAMPLES):
            g = build(K, rnd, shift, epb, gadgets)
            z = zp.ZP(g, True); z.run(); c = z.calls
            tot += c
            if c > mx:
                mx = c; best[K] = pg.dumps(g)
            if K <= 6:
                zz = zp.ZP(g, False); zz.run(); mxplain = max(mxplain, zz.calls)
        print(f"K={K} (n={4*K}): ZP calls max {mx} mean {tot/SAMPLES:.1f}; plain Zielonka max {mxplain if K <= 6 else '-'}  ({time.time()-t0:.0f}s)", flush=True)
    os.makedirs(os.path.join(HERE, "instances"), exist_ok=True)
    with open(os.path.join(HERE, "out", f"zp_blocks_s{seed}.jsonl"), "w") as f:
        for K, txt in best.items():
            g = pg.parse(txt); f.write(json.dumps(alglib.game_record(g, zielonka.solve(g), K=K)) + "\n")


if __name__ == "__main__":
    main()
