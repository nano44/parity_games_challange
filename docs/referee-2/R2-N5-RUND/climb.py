#!/usr/bin/env python3
r"""REFEREE-2 successor 16 (Opus 5.5, D15): hill climb for LONG fallback-free in-phase runs with lambda_W constant (so that the
freeze-dependent RUND items, CR-REL and TWIN-GAP (ii), and CHARGE-U are exercised), on multi-Odd games, from a seed instance + start.
score = 100 * (longest such run's transitions - (n - 1)) + (U_{-1} events on it) + (offset changes at tail transitions of h3 runs).
Mutations: succ. 12's fbred_check.mutate (priority, owner, add/remove edge); the start pair is repaired to a valid successor.
Usage: climb.py seed.pg seed.start steps seed out_prefix  (seed.start may be '-' for the S3 start)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FBRED"))
import rund_check as R
import fbred_check as FC
DC, pg = R.DC, R.pg


def score(gp, s, t):
    states, fbs = DC.Runner(gp).run(s, t, cap=400)
    ctx = R.Ctx(gp); n = gp.n
    st = R.Stats()
    I = [R.state_info(ctx, a, b, st, "c") for a, b in states]
    tauk = [tuple(b[v] for v in range(n) if gp.owner[v] == 1) for _, b in states]
    best = -10 ** 9
    k = 0
    while k < len(states) - 1:
        e = k
        while (e + 1 < len(states) and not fbs[e] and tauk[e + 1] == tauk[k] and I[e + 1]["lamX"] == I[k]["lamX"]
               and I[e + 1]["lamW"] == I[k]["lamW"]):
            e += 1
        if e > k:
            sc = 100 * (e - k - (n - 1))
            F = [set((x, z) for x in range(n) if gp.owner[x] == 0 for z in set(gp.succ[x]) if R.forbidden(ctx, I[j], -1, x, z))
                 for j in range(k, e + 1)]
            for j in range(k, e):
                for y in range(n):
                    if gp.owner[y] == 0 and I[j + 1]["sg"][y] != I[j]["sg"][y]:
                        ed = (y, I[j + 1]["sg"][y])
                        if any(ed in F[f - k] for f in range(max(j - n + 1, k), j)): sc += 1
            best = max(best, sc)
        k = e + 1 if e > k else k + 1
    return best


def repair(gp, s):
    return [x if x in gp.succ[v] else gp.succ[v][0] for v, x in enumerate(s)]


def main():
    a = sys.argv[1:]
    g0 = pg.read(a[0]); steps, seed, out = int(a[2]), int(a[3]), a[4]
    s0, t0 = R.read_start(g0, a[1]) if a[1] != "-" else R.starts(g0, 0, None)
    rng = random.Random(seed)
    best, bs, bt = g0, s0, t0
    bsc = score(g0, s0, t0)
    print("seed score", bsc, flush=True)
    for it in range(steps):
        cand = FC.mutate(rng, best)
        if any(len(x) == 0 for x in cand.succ): continue
        cs, ct = repair(cand, bs), repair(cand, bt)
        if rng.random() < 0.2:
            v = rng.randrange(cand.n); (cs if cand.owner[v] == 0 else ct)[v] = rng.choice(cand.succ[v])
        try:
            sc = score(cand, cs, ct)
        except Exception as ex:
            print("skip", it, ex); continue
        if sc >= bsc:
            if sc > bsc: print("it", it, "score", sc, flush=True)
            bsc, best, bs, bt = sc, cand, cs, ct
            open(out + ".pg", "w").write(pg.dumps(best))
            open(out + ".start", "w").write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in enumerate(bs) if best.owner[v] == 0) +
                                            "\nTAU0 " + " ".join(f"{v}:{w}" for v, w in enumerate(bt) if best.owner[v] == 1) +
                                            f"\nscore {bsc}\n")
    print("final", bsc)


if __name__ == "__main__":
    main()
