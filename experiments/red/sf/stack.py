#!/usr/bin/env python3
"""L-RED: structured search for N5-SF SBC growth. A GADGET (ng vertices: owner, local priority rank, successor list of
(local target, stage offset in {-1, 0, +1})) is stacked K times; stage s's vertex v gets priority s*ng + rank(v) + 2 (so higher stages
dominate), and offsets leaving the stack go to the sink (vertex 0: priority 1, Odd, self-loop). The climb maximises SBC (sigma + tau) at
K = KMAX from the SPEC S3 start, and prints SBC for K = 2..KMAX for every improvement. Usage: stack.py ng KMAX SEED STEPS OUTPREFIX"""
import sys, os, random, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sf2, pg


def build(gad, K):
    ng = len(gad["own"]); n = 1 + K * ng
    prio = [1] + [0] * (n - 1); own = [1] + [0] * (n - 1); succ = [[0]] + [[] for _ in range(n - 1)]
    for s in range(K):
        for v in range(ng):
            x = 1 + s * ng + v
            prio[x] = 2 + s * ng + gad["rank"][v]; own[x] = gad["own"][v]
            for (w, o) in gad["succ"][v]:
                t = s + o
                succ[x].append(0 if t < 0 or t >= K else 1 + t * ng + w)
            succ[x] = sorted(set(succ[x]))
    return pg.Game(prio, own, succ)


def sbc(g):
    rec = []
    try:
        sf2.SF(g).run_sf(rec=rec, max_iter=20000)
    except Exception:
        return -1, -1
    _, a, _, b, _ = sf2.stats(rec)
    return a + b, len(rec) - 1


def rand_gad(ng, R):
    rank = list(range(ng)); R.shuffle(rank)
    return {"own": [R.randint(0, 1) for _ in range(ng)], "rank": rank,
            "succ": [[(R.randrange(ng), R.choice((-1, 0, 0, 1))) for _ in range(R.randint(1, 3))] for _ in range(ng)]}


def mutate(gad, R):
    g = json.loads(json.dumps(gad)); ng = len(g["own"]); v = R.randrange(ng); k = R.randint(0, 4)
    if k == 0: g["own"][v] ^= 1
    elif k == 1:
        w = R.randrange(ng); g["rank"][v], g["rank"][w] = g["rank"][w], g["rank"][v]
    elif k == 2 and len(g["succ"][v]) < 3: g["succ"][v].append([R.randrange(ng), R.choice((-1, 0, 1))])
    elif k == 3 and len(g["succ"][v]) > 1: g["succ"][v].pop(R.randrange(len(g["succ"][v])))
    else:
        i = R.randrange(len(g["succ"][v])); g["succ"][v][i] = [R.randrange(ng), R.choice((-1, 0, 1))]
    return g


if __name__ == "__main__":
    ng, KMAX, seed, steps, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    R = random.Random(seed); gad = rand_gad(ng, R); best, _ = sbc(build(gad, KMAX))
    for t in range(steps):
        h = mutate(gad, R); s, it = sbc(build(h, KMAX))
        if s >= best:
            if s > best:
                prof = [sbc(build(h, k)) for k in range(2, KMAX + 1)]
                print(f"step {t} SBC@K {[p[0] for p in prof]} it@K {[p[1] for p in prof]}", flush=True)
                json.dump(h, open(out + ".json", "w"))
            gad, best = h, s
    print("final", best)
