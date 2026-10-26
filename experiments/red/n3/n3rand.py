#!/usr/bin/env python3
"""Random search for N3-LEVEL / FLIP-COST / SG violations with n3x.py's exact checker, biased to many Odd choice vertices.
Usage: n3rand.py SEED SECONDS NMIN NMAX OUTDIR. Writes OUTDIR/viol_<seed>_<i>.pg (+ .start) on a violation; prints counters."""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import n3x
import pg

def rgame(rng, n):
    prio = [rng.randrange(n) for _ in range(n)]
    owner = [rng.randrange(2) for _ in range(n)]
    succ = []
    for v in range(n):
        d = rng.choice([1, 2, 2, 3]) if owner[v] == 1 else rng.choice([1, 2, 3])
        succ.append(sorted(set(rng.randrange(n) for _ in range(d))))
    return pg.Game(prio, owner, succ)

def main():
    seed, secs, nmin, nmax, out = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    os.makedirs(out, exist_ok=True); rng = random.Random(seed); t0 = time.time(); i = 0
    while time.time() - t0 < secs:
        i += 1; g = rgame(rng, rng.randint(nmin, nmax)); before = len(n3x.VIOL)
        st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
              {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if i % 2 else None
        n3x.check(g, f"r{seed}_{i}", st); n3x.C["games"] += 1
        if len(n3x.VIOL) > before:
            p = os.path.join(out, f"viol_{seed}_{i}.pg"); pg.write(g, p)
            with open(p[:-3] + ".start", "w") as f:
                s = st or ({}, {})
                f.write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in s[0].items()) + "\nTAU0 " + " ".join(f"{v}:{w}" for v, w in s[1].items()) + "\n")
    print(" ".join(f"{k}={v}" for k, v in sorted(n3x.C.items())))
    for v in n3x.VIOL[:10]: print("VIOLATION", v)
    print("N3X PASS" if not n3x.VIOL else "N3X FAIL")

if __name__ == "__main__":
    main()
