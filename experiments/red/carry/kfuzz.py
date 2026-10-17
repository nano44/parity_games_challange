#!/usr/bin/env python3
"""L-RED (box 6, produced on Opus 5.5): in-process random fuzz of L-ALG's GAP-C statements (K-in), (K-first), (K4-B) and
run completeness, both order data, on L-ALG's unmodified classes (dtl_kin.KI, dtl_whichpiece.WP, dtl_k4b.K4B), imported
read-only from LALG5_DIR (>= 31fdd98). Writes every violating game to OUTDIR. Usage:
  kfuzz.py SEED COUNT OUTDIR [--nmin 4] [--nmax 12] [--deg 3] [--prmax K]"""
import sys, os, random, argparse
ld = os.path.join(os.environ["LALG5_DIR"], "experiments", "alg")
sys.path.insert(0, ld); sys.path.insert(0, os.path.join(ld, "..", "harness"))
import pg, dtl_k4b as KB, dtl_whichpiece as WPm

def rgame(rng, n, deg, prmax):
    pr = [rng.randint(0, prmax) for _ in range(n)]; ow = [rng.randint(0, 1) for _ in range(n)]
    succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, deg)))) for _ in range(n)]
    return pg.Game(pr, ow, succ)

def check(g, order):
    """Returns list of violation tags for game g under order ('oink'|'stable')."""
    ins = order == "oink"; bad = []
    d0 = KB.K.P.build(g); d = KB.K4B(d0.pr, d0.ow, d0.outs, ins_desc=ins); d.run()
    if d.G: bad.append("INCOMPLETE")
    for tr in d.trace:
        W = tr["Wp"]
        if not W or tr["d1"] > tr["dom"]: continue
        bad.append("_checked")
        if any(t != W for t in [set(tr["G"])]): bad.append("_mixed")
        if not any(C <= W for C in tr["newt"]): bad.append("K-in")
        if "first" in tr:
            V, Z, R = tr["first"]
            if not Z <= W or not V <= W: bad.append("K4-B")
    d0 = WPm.L.K.P.build(g); d = WPm.WP(d0.pr, d0.ow, d0.outs, ins_desc=ins); d.run()
    for tr in d.trace:
        W = tr["Wp"]
        if not W or tr["d1"] > tr["dom"]: continue
        pcs, passes = tr["pieces"], tr["passes"]
        if not pcs: bad.append("nostable"); continue
        hi = pcs[1]["passes_from"] if len(pcs) > 1 else len(passes)
        ok = any(tops and tops[-1] in W and any(top == tops[-1] and C <= W for top, C in ev) for tops, ev in passes[pcs[0]["passes_from"]:hi])
        if not ok: bad.append("K-first")
    return bad

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    a = argparse.ArgumentParser(); a.add_argument("seed", type=int); a.add_argument("count", type=int); a.add_argument("outdir")
    a.add_argument("--nmin", type=int, default=4); a.add_argument("--nmax", type=int, default=12); a.add_argument("--deg", type=int, default=3)
    a.add_argument("--prmax", type=int, default=-1); o = a.parse_args()
    rng = random.Random(o.seed); os.makedirs(o.outdir, exist_ok=True); tot = {}
    for i in range(o.count):
        n = rng.randint(o.nmin, o.nmax); g = rgame(rng, n, o.deg, o.prmax if o.prmax >= 0 else rng.randint(1, n))
        for order in ("oink", "stable"):
            try: bad = check(g, order)
            except RecursionError: bad = ["recursion"]
            for b in bad:
                if b.startswith("_"): tot[b] = tot.get(b, 0) + 1
            for b in set(bad):
                if b.startswith("_"): continue
                tot[b] = tot.get(b, 0) + 1
                fn = os.path.join(o.outdir, f"kf_{o.seed}_{i}_{order}_{b}.pg")
                with open(fn, "w") as f: f.write(pg.dumps(g))
                print("VIOLATION", b, order, fn, flush=True)
    print("done", o.count, "games x 2 orders", tot)
