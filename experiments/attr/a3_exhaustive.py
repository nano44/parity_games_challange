#!/usr/bin/env python3
"""A3: psolC against psolB, psolQ and PA** on every canonical game with n vertices (a1lib enumeration), with the
per-node check of DTR Thm 4 (every node psolB decides, psolC decides) and soundness against Zielonka.
PA** is taken as "psolB solves completely" (T-A1, RESULTS R2), not recomputed.
Writes OUT/a3_fail_n{n}.jsonl (games where psolC is partial, or Thm 4's node inclusion fails, or any solver is unsound)
and OUT/a3_summary_n{n}.txt. Usage: a3_exhaustive.py n [--workers K] [--variant]  (--variant: also run psolC with the
start colour excluded, docs/attr/psolC-impl.md A1)."""
import sys, os, json, time
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import a1lib, pg, zielonka
from psolb import PsolB
from psolq import PsolQ
from psolc import PsolC

OUT = os.path.join(HERE, "out")


def status(win, ref, residual):
    if any(win[v] is not None and win[v] != ref[v] for v in range(len(ref))):
        return "UNSOUND"
    return "solved" if not residual else "undecided"


def work(task):
    cfg, m, n, variant = task
    counts, fails = {}, []
    for g in a1lib.games_on(cfg, n):
        ref = zielonka.solve(g)
        wb, _, rb, _ = PsolB(g).run()
        wq, _, rq, _ = PsolQ(g).run()
        wc, _, rc, _ = PsolC(g, strat=None).run()
        sb, sq, sc = status(wb, ref, rb), status(wq, ref, rq), status(wc, ref, rc)
        rec = dict(psolb=sb, psolq=sq, psolc=sc, b_undec=len(rb), q_undec=len(rq), c_undec=len(rc))
        thm4 = all(wc[v] is not None for v in range(n) if wb[v] is not None)   # psolB-decided ⊆ psolC-decided
        rec["thm4"] = thm4
        key = (m, sb, sq, sc, thm4)
        if variant:
            wx, _, rx, _ = PsolC(g, strat=None, exclude_start=True).run()
            sx = status(wx, ref, rx); rec["psolcx"] = sx; rec["x_undec"] = len(rx)
            key = key + (sx,)
        counts[key] = counts.get(key, 0) + 1
        bad = sc != "solved" or not thm4 or "UNSOUND" in (sb, sq, sc) or (variant and sx == "UNSOUND")
        if bad:
            fails.append(dict(n=n, m=m, prio=g.prio, owner=g.owner, succ=[sorted(set(s)) for s in g.succ], ref=ref, **rec))
    return counts, fails


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    n = int(args[0])
    workers = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 3
    variant = "--variant" in sys.argv
    os.makedirs(OUT, exist_ok=True)
    t0 = time.time()
    orbits = sorted(((cfg, m) for cfg, m in a1lib.succ_orbits(n)), key=lambda x: (x[1], x[0]))
    tasks = [(cfg, m, n, variant) for cfg, m in orbits]
    counts, fails = {}, []
    with Pool(workers) as pool, open(os.path.join(OUT, f"a3_fail_n{n}.jsonl"), "w") as ff:
        done = 0
        for c, f in pool.imap(work, tasks, chunksize=1):
            for k, v in c.items():
                counts[k] = counts.get(k, 0) + v
            for rec in f:
                ff.write(json.dumps(rec) + "\n")
            fails += f
            done += 1
            if done % 100 == 0 or done == len(tasks):
                print(f"  {done}/{len(tasks)} orbits, {time.time()-t0:.0f}s, records {len(fails)}", flush=True)
    total = sum(counts.values())
    agg = {}
    for k, v in counts.items():
        m, sb, sq, sc, thm4 = k[:5]
        for name, val in (("psolB", sb), ("psolQ", sq), ("psolC", sc)):
            agg[(name, val)] = agg.get((name, val), 0) + v
        agg[("thm4", thm4)] = agg.get(("thm4", thm4), 0) + v
        agg[("B,C", sb, sc)] = agg.get(("B,C", sb, sc), 0) + v
        agg[("Q,C", sq, sc)] = agg.get(("Q,C", sq, sc), 0) + v
        if variant:
            agg[("psolCx", k[5])] = agg.get(("psolCx", k[5]), 0) + v
            agg[("C,Cx", sc, k[5])] = agg.get(("C,Cx", sc, k[5]), 0) + v
    lines = [f"n={n} games={total} time={time.time()-t0:.0f}s variant={variant}"]
    for k in sorted(agg, key=str):
        lines.append(f"{k} : {agg[k]}")
    lines.append("by m, psolB, psolQ, psolC, thm4" + (", psolCx" if variant else "") + " : count")
    for k in sorted(counts, key=str):
        lines.append(f"{k} : {counts[k]}")
    part = [r for r in fails if r["psolc"] == "undecided"]
    if part:
        mn = min(r["m"] for r in part)
        lines.append(f"smallest psolC-partial games: m={mn}, count {sum(1 for r in part if r['m'] == mn)}")
        for r in [r for r in part if r["m"] == mn][:6]:
            lines.append(f"  prio={r['prio']} owner={r['owner']} succ={r['succ']} ref={r['ref']} psolB={r['psolb']} psolQ={r['psolq']} c_undec={r['c_undec']}")
    text = "\n".join(lines)
    open(os.path.join(OUT, f"a3_summary_n{n}.txt"), "w").write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
