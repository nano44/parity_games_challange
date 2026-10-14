#!/usr/bin/env python3
"""Seeded random parity-game generator (independent of Oink's rngame, which seeds from random_device and is
therefore not reproducible). Every game is a function of (n, d, dmin, dmax, peven, selfloops, seed).

Usage: gen.py n d dmin dmax seed [--peven P] [--no-self-loops] [-o out.pg]
       gen.py corpus DIR COUNT SEED [--nmin A --nmax B]   (varied sizes/degrees/priorities/owner mix, manifest.csv)
Priorities are drawn uniformly from 0..d-1 (so the game has at most d distinct priorities); every vertex gets
a uniform out-degree in [dmin, dmax] (capped at the number of allowed targets), targets distinct, uniform."""
import sys, os, argparse, csv
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pg, hashlib

M64 = (1 << 64) - 1


class Rng:
    """splitmix64; self-contained so games are identical across Python versions (random.Random is not pinned)."""
    def __init__(self, key):
        self.s = int.from_bytes(hashlib.sha256(str(key).encode()).digest()[:8], "little")

    def next64(self):
        self.s = (self.s + 0x9E3779B97F4A7C15) & M64
        z = self.s
        z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & M64
        z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & M64
        return z ^ (z >> 31)

    def randrange(self, k):  # uniform in 0..k-1, rejection sampling
        lim = (1 << 64) - ((1 << 64) % k)
        while True:
            x = self.next64()
            if x < lim:
                return x % k

    def randint(self, a, b):
        return a + self.randrange(b - a + 1)

    def random(self):
        return (self.next64() >> 11) / float(1 << 53)

    def choice(self, xs):
        return xs[self.randrange(len(xs))]

    def sample(self, xs, k):  # partial Fisher-Yates
        xs = list(xs)
        for i in range(k):
            j = i + self.randrange(len(xs) - i)
            xs[i], xs[j] = xs[j], xs[i]
        return xs[:k]


def random_game(n, d, dmin, dmax, seed, peven=0.5, selfloops=True):
    rnd = Rng(f"pg|{n}|{d}|{dmin}|{dmax}|{peven}|{int(selfloops)}|{seed}")
    prio = [rnd.randrange(d) for _ in range(n)]
    owner = [0 if rnd.random() < peven else 1 for _ in range(n)]
    succ = []
    for v in range(n):
        targets = list(range(n)) if selfloops else [w for w in range(n) if w != v]
        if not targets:  # n == 1 without self-loops is impossible; fall back to the self-loop
            targets = [v]
        k = max(1, min(len(targets), rnd.randint(dmin, dmax)))
        succ.append(sorted(rnd.sample(targets, k)))
    return pg.Game(prio, owner, succ)


def corpus(outdir, count, seed, nmin=1, nmax=60):
    """Varied parameters drawn from a master seed; each game records its own parameters and seed."""
    os.makedirs(outdir, exist_ok=True)
    rnd = Rng(f"corpus|{seed}")
    rows = []
    for i in range(count):
        n = rnd.randint(nmin, nmax)
        d = rnd.choice([1, 2, 3, 4, max(1, n // 4), max(1, n // 2), n, n + 3])
        dmin = rnd.choice([1, 1, 2, 3])
        dmax = dmin + rnd.choice([0, 1, 2, 5, n])
        peven = rnd.choice([0.0, 0.2, 0.5, 0.5, 0.8, 1.0])
        sl = rnd.random() < 0.7 or n == 1
        gseed = rnd.randrange(2**31)
        g = random_game(n, d, dmin, dmax, gseed, peven, sl)
        name = f"r{i:05d}_n{n}_d{d}_deg{dmin}-{dmax}_pe{peven}_sl{int(sl)}_s{gseed}.pg"
        pg.write(g, os.path.join(outdir, name))
        rows.append(dict(file=name, n=n, d=d, dmin=dmin, dmax=dmax, peven=peven, selfloops=int(sl), seed=gseed, m=g.m))
    with open(os.path.join(outdir, "manifest.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)
    return rows


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "corpus":
        ap = argparse.ArgumentParser()
        ap.add_argument("cmd"); ap.add_argument("dir"); ap.add_argument("count", type=int); ap.add_argument("seed", type=int)
        ap.add_argument("--nmin", type=int, default=1); ap.add_argument("--nmax", type=int, default=60)
        a = ap.parse_args()
        rows = corpus(a.dir, a.count, a.seed, a.nmin, a.nmax)
        print(f"wrote {len(rows)} games to {a.dir} (master seed {a.seed})")
    else:
        ap = argparse.ArgumentParser()
        for k in ("n", "d", "dmin", "dmax", "seed"):
            ap.add_argument(k, type=int)
        ap.add_argument("--peven", type=float, default=0.5)
        ap.add_argument("--no-self-loops", action="store_true")
        ap.add_argument("-o")
        a = ap.parse_args()
        g = random_game(a.n, a.d, a.dmin, a.dmax, a.seed, a.peven, not a.no_self_loops)
        if a.o:
            pg.write(g, a.o)
        else:
            sys.stdout.write(pg.dumps(g))
