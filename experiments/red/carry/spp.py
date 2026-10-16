#!/usr/bin/env python3
"""L-RED (box 5, Opus 5.5), 2026-10-16: searches per phase against |G'| (the game at the phase start) on A_DTL, using
L-ALG's experiments/alg/dtl_phasestats.py (read-only via LALG_DIR, l-alg >= b9b3b2b). Order datum from DTL_ORDER.
Per run: max searches in one phase (spp), its |G'|, max over phases with >= 3 searches of searches - |G'| (excess; > 0 refutes (SPP) plain
form) and of searches / |G'|. Usage: DTL_ORDER=oink LALG_DIR=.. spp.py G.pg ..."""
import sys, os

def _mods():
    ld = os.environ["LALG_DIR"]
    for q in (os.path.join(ld, "experiments", "alg"), os.path.join(ld, "experiments", "harness")):
        if q not in sys.path: sys.path.insert(0, q)
    import dtl_phasestats as PS, pg
    return PS, pg

def measure(path):
    PS, pg = _mods(); g = pg.read(path); d = PS.build(g); d.run()
    rows, cur = [], []
    for t in d.trace:
        if cur and (t["p"] != cur[-1]["p"] or t["dom"] != cur[-1]["dom"]): rows.append(cur); cur = []
        cur.append(t)
    if cur: rows.append(cur)
    best = dict(spp=0, G=0, excess=-10 ** 9, ratio=0.0, iters=d.iterations, n=g.n, ppar=0)
    for ph in rows:
        G0, p = ph[0]["G"], ph[0]["p"]
        if not G0: continue
        k = len(ph); par = sum(1 for v in G0 if d.pr[v] % 2 == p)
        if k > best["spp"] or (k == best["spp"] and len(G0) < best["G"]): best.update(spp=k, G=len(G0), ppar=par)
        if k >= 3:                                    # trivial 1-2 search phases on tiny G' would game the ratio
            best["excess"] = max(best["excess"], k - len(G0)); best["ratio"] = max(best["ratio"], k / len(G0))
    return best

def score(path):
    b = measure(path)
    return 1000 * b["ratio"] + b["spp"] + b["iters"] / 1000.0

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f in sys.argv[1:]:
        b = measure(f)
        print(f"== {os.path.basename(f)} order={os.environ.get('DTL_ORDER', 'stable')} n={b['n']} iterations={b['iters']} "
              f"max spp={b['spp']} at |G'|={b['G']} (p-parity {b['ppar']}) max ratio={b['ratio']:.3f} max excess={b['excess']}"
              + ("  ** PHASE > |G'| **" if b["excess"] > 0 else ""))
