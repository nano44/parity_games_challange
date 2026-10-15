#!/usr/bin/env python3
"""A1 exhaustive enumeration (statement section 5 step 4). Every parity game with n vertices up to isomorphism of the
successor structure and order-and-parity equivalence of priorities (a1lib.succ_orbits x owners x priority_patterns),
classified by psolQ and by Algorithm 1 (a1lib.classify). Strahler number computed for every failure (and for every game
with --all-strahler). Failures are written one per line to OUT/fail_n{n}.jsonl; a summary to OUT/summary_n{n}.txt.
Usage: exhaustive.py n [--mmax M] [--mmin M] [--workers K] [--all-strahler] [--stop-first]
Exit 0; counts in the summary. Deterministic (orbit order, owner order, pattern order)."""
import sys, os, json, time, itertools
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import a1lib, pg

OUT = os.path.join(HERE, "out")


def work(task):
    cfg, m, n, all_str = task
    counts, fails = {}, []
    for g in a1lib.games_on(cfg, n):
        r = a1lib.classify(g, want_strahler=all_str)
        key = (m, r["psolq"], r["avh"])
        counts[key] = counts.get(key, 0) + 1
        bad = r["psolq"] != "solved" or r["avh"] != "solved"
        if bad or all_str:
            if not all_str:
                r2 = a1lib.classify(g, ref=r["ref"], want_strahler=True)
                r.update({k: r2[k] for k in ("str", "strE", "strO", "height", "leaves", "treeE", "treeO")})
            skey = (m, r["str"], r["psolq"], r["avh"])
            counts[("S",) + skey] = counts.get(("S",) + skey, 0) + 1
            if bad:
                fails.append(dict(n=n, m=m, prio=g.prio, owner=g.owner, succ=[sorted(set(s)) for s in g.succ],
                                  ref=r["ref"], psolq=r["psolq"], psolq_undecided=r["psolq_undecided"], avh=r["avh"],
                                  avh_undecided=r["avh_undecided"], str=r["str"], strE=r["strE"], strO=r["strO"],
                                  height=r["height"], leaves=r["leaves"], treeE=str(r["treeE"]), treeO=str(r["treeO"]),
                                  oneplayer=len(set(g.owner)) == 1))
    return counts, fails


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    n = int(args[0])
    opt = lambda k, d: int(sys.argv[sys.argv.index(k) + 1]) if k in sys.argv else d
    mmax, mmin, workers = opt("--mmax", 10**9), opt("--mmin", 0), opt("--workers", 3)
    all_str = "--all-strahler" in sys.argv
    os.makedirs(OUT, exist_ok=True)
    t0 = time.time()
    orbits = [(cfg, m) for cfg, m in a1lib.succ_orbits(n) if mmin <= m <= mmax]
    orbits.sort(key=lambda x: (x[1], x[0]))
    npat = sum(1 for _ in a1lib.priority_patterns(n))
    print(f"n={n}: {len(orbits)} successor orbits with {mmin}<=m<={mmax}, {2**n} owner vectors, {npat} priority patterns "
          f"-> {len(orbits) * 2**n * npat} games; {workers} workers", flush=True)
    tasks = [(cfg, m, n, all_str) for cfg, m in orbits]
    counts, fails = {}, []
    tag = f"n{n}" + (f"_m{mmin}-{mmax}" if (mmin or mmax < 10**9) else "")
    with Pool(workers) as pool, open(os.path.join(OUT, f"fail_{tag}.jsonl"), "w") as ff:
        done = 0
        for c, f in pool.imap(work, tasks, chunksize=1):
            for k, v in c.items():
                counts[k] = counts.get(k, 0) + v
            for rec in f:
                ff.write(json.dumps(rec) + "\n")
            fails += f
            done += 1
            if done % 50 == 0 or done == len(tasks):
                print(f"  {done}/{len(tasks)} orbits, {time.time()-t0:.0f}s, failures so far {len(fails)}", flush=True)
            if "--stop-first" in sys.argv and fails:
                pool.terminate(); break
    lines = [f"n={n} games={sum(v for k, v in counts.items() if k[0] != 'S')} time={time.time()-t0:.0f}s",
             "m, psolq, avh : count"]
    for k in sorted(k for k in counts if k[0] != "S"):
        lines.append(f"{k} : {counts[k]}")
    lines.append("m, Strahler, psolq, avh : count" + ("" if all_str else "  (failures only)"))
    for k in sorted(k for k in counts if k[0] == "S"):
        lines.append(f"{k[1:]} : {counts[k]}")
    if fails:
        mins = {}
        for rec in fails:
            for solver, st in (("psolq", rec["psolq"]), ("avh", rec["avh"])):
                if st != "solved":
                    key = (solver, rec["str"])
                    if key not in mins or (rec["m"], rec["str"]) < (mins[key]["m"], mins[key]["str"]):
                        mins[key] = rec
        lines.append("minimal failures (solver, Strahler) -> smallest m:")
        for key in sorted(mins):
            rec = mins[key]
            lines.append(f"  {key}: n={rec['n']} m={rec['m']} prio={rec['prio']} owner={rec['owner']} succ={rec['succ']} "
                         f"ref={rec['ref']} psolq={rec['psolq']} avh={rec['avh']} trees E{rec['treeE']} O{rec['treeO']}")
    text = "\n".join(lines)
    open(os.path.join(OUT, f"summary_{tag}.txt"), "w").write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
