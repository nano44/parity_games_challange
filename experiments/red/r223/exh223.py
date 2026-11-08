#!/usr/bin/env python3
"""L-RED 58 R223 item 1: EXHAUSTIVE small-genome attack on P-N5-END (claude/l-new 131b4c1c) Lemmas E0-E4 / ENDGAME-3(-N5).
Uses R222's end222.check (algorithm = frozen box190 n5v.step on frozen box189 gamma3.build; every check by L-RED's own.py).
Enumerates every genome with N <= 2 movers (level patterns [0], [0,0], [0,1]), degree 1-2 per mover, every W-target, every Xi-target
in {X, movers} (self-loops included), every start, every beta parity vector, beta ranks in {identity, reversed}, gate index order in
{identity, reversed}. Modes spec (N5), xi (N5'-xi), idx. Counter: genomes with any end222 fail counter > 0 (unit: genome x mode).
Usage: exh223.py OUT.txt [N3SAMPLES SEED]  (env WT = WT3 = worktree of claude/l-new 131b4c1c; resumable by genome key)"""
import sys, os, itertools, random, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../r222"))
import end222
def genomes():
    for lev in ([0], [0, 0], [0, 1]):
        N = len(lev)
        for degs in itertools.product((1, 2), repeat=N):
            wts = [[-1] if lev[x] == 0 else [y for y in range(N) if lev[y] == lev[x] - 1] for x in range(N)]
            slots = [(x, k) for x in range(N) for k in range(degs[x])]; M = len(slots)
            for wt in itertools.product(*[wts[x] for (x, k) in slots]):
                for xt in itertools.product(range(-1, N), repeat=M):
                    for st in itertools.product(*[range(d) for d in degs]):
                        for bp in itertools.product((0, 1), repeat=M):
                            for brr in (0, 1):
                                for gr in (0, 1):
                                    yield lev, degs, slots, wt, xt, st, bp, brr, gr
def mk(lev, degs, slots, wt, xt, st, bp, brr, gr):
    N, M = len(lev), len(slots); opts = [[] for _ in range(N)]; gate = [[] for _ in range(N)]
    perm = list(range(M))[::-1] if gr else list(range(M))
    for i, (x, k) in enumerate(slots): opts[x].append([wt[i], xt[i], i]); gate[x].append(perm[i])
    br = list(range(M))[::-1] if brr else list(range(M))
    return {"N": N, "lev": list(lev), "opts": opts, "gate": gate, "br": br, "bp": list(bp), "start": list(st)}
def rand3(rng):
    lev = rng.choice([[0, 0, 0], [0, 0, 1], [0, 1, 1], [0, 1, 2]]); N = 3; degs = [rng.randint(1, 3) for _ in range(N)]
    opts, gate = [[] for _ in range(N)], [[] for _ in range(N)]; M = sum(degs); perm = list(range(M)); rng.shuffle(perm); i = 0
    for x in range(N):
        for k in range(degs[x]):
            w = rng.choice([y for y in range(N) if lev[y] == lev[x] - 1]) if lev[x] else -1
            opts[x].append([w, rng.randrange(-1, N), i]); gate[x].append(perm[i]); i += 1
    br = list(range(M)); rng.shuffle(br)
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": [rng.randrange(2) for _ in range(M)], "start": [rng.randrange(d) for d in degs]}
def run(G, key, fo, tally):
    res = []
    for mode in ("spec", "xi", "idx"):
        c, T, F = end222.check(G, mode); res.append((mode, T, F, c))
        tally[mode] = max(tally.get(mode, 0), F or 0)
    bad = [(m, {k: v for k, v in c.items() if v}) for m, T, F, c in res if any(c.values())]
    if bad:
        fo.write(f"BAD {key} {bad} {json.dumps(G)}\n"); fo.flush(); tally["bad"] = tally.get("bad", 0) + 1
    tally["n"] = tally.get("n", 0) + 1
if __name__ == "__main__":
    outf = sys.argv[1]; fo = open(outf, "a"); tally = {}
    for t in genomes(): run(mk(*t), "exh", fo, tally)
    fo.write(f"EXH genomes {tally['n']} bad {tally.get('bad', 0)} maxF spec {tally['spec']} xi {tally['xi']} idx {tally['idx']}\n"); fo.flush()
    if len(sys.argv) > 2:
        cnt, seed = int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); tally = {}
        for i in range(cnt): run(rand3(rng), f"n3_{seed}_{i}", fo, tally)
        fo.write(f"N3 seed {seed} genomes {tally['n']} bad {tally.get('bad', 0)} maxF spec {tally['spec']} xi {tally['xi']} idx {tally['idx']}\n")
