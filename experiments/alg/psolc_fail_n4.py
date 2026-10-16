#!/usr/bin/env python3
"""Regenerate the list of canonical n-vertex games psolC (experiments/attr/psolc.py, literal reading) leaves partly
undecided (A3 results: 1,380 games at n = 4). experiments/attr/out/ is gitignored, so L-ALG recomputes it once; the
candidates are tested on this list first (every candidate's decided set contains psolC's, so these are the only n = 4
games where a candidate can still fail). Output: out/psolc_fail_n{n}.jsonl (one game per line) and a count line.
Usage: psolc_fail_n4.py [n] [--workers K]"""
import sys, os, json, time
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "attr"))
sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import a1lib, pg, zielonka
from psolc import PsolC


def work(task):
    cfg, m, n = task
    fails, total = [], 0
    for g in a1lib.games_on(cfg, n):
        total += 1
        wc, _, rc, _ = PsolC(g, strat=None).run()
        if rc:
            ref = zielonka.solve(g)
            assert all(wc[v] is None or wc[v] == ref[v] for v in range(n)), "psolC unsound?!"
            fails.append(dict(n=n, m=m, prio=g.prio, owner=g.owner, succ=[sorted(set(s)) for s in g.succ], ref=ref,
                              c_undec=len(rc)))
    return total, fails


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    n = int(args[0]) if args else 4
    workers = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 3
    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    t0 = time.time()
    orbits = sorted(((cfg, m) for cfg, m in a1lib.succ_orbits(n)), key=lambda x: (x[1], x[0]))
    tasks = [(cfg, m, n) for cfg, m in orbits]
    total, nf = 0, 0
    with Pool(workers) as pool, open(os.path.join(HERE, "out", f"psolc_fail_n{n}.jsonl"), "w") as ff:
        for i, (t, f) in enumerate(pool.imap(work, tasks, chunksize=1)):
            total += t
            for rec in f:
                ff.write(json.dumps(rec) + "\n"); nf += 1
            if (i + 1) % 100 == 0 or i + 1 == len(tasks):
                print(f"  {i+1}/{len(tasks)} orbits, {time.time()-t0:.0f}s, games {total}, psolC-partial {nf}", flush=True)
    print(f"n={n}: games={total} psolC-partial={nf} time={time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
