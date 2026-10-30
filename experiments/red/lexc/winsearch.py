#!/usr/bin/env python3
"""L-RED R143: hill-climb (mutating succ / prio / owner of a seed game, default start) for W-constant intervals with several non-trivial
SETTLE windows (an event that restarts the bottom-up settling). Score = (max windows with a switch in one interval, its length).
Usage: winsearch.py SEED.pg RNGSEED SECONDS OUT.pg"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import settle
pg = settle.pg; n5b = settle.n5b
def windows(g):
    r = settle.analyse(g, max_iter=400)
    if r is None: return (0, 0)
    out, _ = r
    if not out: return (0, 0)
    return max((o["NW"], o["LEN"]) for o in out)
def mutate(rng, g):
    pr, ow, sc = list(g.prio), list(g.owner), [list(s) for s in g.succ]; n = len(pr); v = rng.randrange(n); r = rng.random()
    if r < 0.4: sc[v] = sorted(set(sc[v] + [rng.randrange(n)]))
    elif r < 0.6 and len(sc[v]) > 1: sc[v].pop(rng.randrange(len(sc[v])))
    elif r < 0.85: pr[v] = rng.randrange(2 * n)
    else: ow[v] ^= 1
    return pg.Game(pr, ow, sc)
if __name__ == "__main__":
    g = pg.read(sys.argv[1]); rng = random.Random(int(sys.argv[2])); end = time.time() + float(sys.argv[3]); out = sys.argv[4]
    f = windows(g); best = (f, g); it = 0
    while time.time() < end:
        it += 1; h = mutate(rng, g)
        for _ in range(rng.randint(0, 2)): h = mutate(rng, h)
        fh = windows(h)
        if fh >= f: g, f = h, fh
        if fh > best[0]: best = (fh, h); print("improve", it, fh, flush=True)
    f, g = best
    with open(out, "w") as fo:
        fo.write(f"parity {g.n - 1};\n" + "".join(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n" for v in range(g.n)))
    print(f"WINSEARCH {os.path.basename(sys.argv[1])} seed {sys.argv[2]} best (windows, len) {f} tries {it} -> {out}")
