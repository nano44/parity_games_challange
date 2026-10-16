#!/usr/bin/env python3
"""L-RED successor 3 (Opus 5.5), 2026-10-16, queue item 3: r0 dips at one IDEAL-STABLE context, DEF-filtered.
Per (player, context) key of L-ALG's dtl_regvec.py (read-only via LALG_DIR): successive depth-0 calls with the SAME ideal
(C6) result, ideal STABLE, actual round sets different (a DEF step at that context). r0 = first round where the actual
round sets differ; M = actual nonempty rounds after the step (as in L-ALG dtl_crm.py). A DIP = r0 smaller than at the
previous DEF step of the same context while M does not rise. Order from DTL_ORDER. Usage: r0d.py G.pg ..."""
import sys, os

def _rv():
    ld = os.environ["LALG_DIR"]
    for q in (os.path.join(ld, "experiments", "alg"), os.path.join(ld, "experiments", "harness")):
        if q not in sys.path: sys.path.insert(0, q)
    import dtl_regvec as RV, pg
    return RV, pg

def measure(path):
    RV, pg = _rv(); g = pg.read(path); d = RV.build(g); d.run()
    res = []
    for key, occ in d.calls.items():
        seq = []
        for (s1, r1, v1, h1, _), (s2, r2, v2, h2, _) in zip(occ, occ[1:]):
            if h1 != h2 or r1 == r2 or h1[0] != 1: continue
            pick = lambda r, i: r[i] if i < len(r) else frozenset()
            r0 = next(i for i in range(1, max(len(r1), len(r2)) + 1) if pick(r1, i) != pick(r2, i))
            seq.append((s2, r0, len([x for x in r1 if x]), len([x for x in r2 if x])))
        if not seq: continue
        dips = sum(1 for a, b in zip(seq, seq[1:]) if b[1] < a[1] and b[3] <= a[3])
        res.append(dict(p=key[0], ctx=len(key[1]), steps=len(seq), dips=dips, seq=seq))
    return res, d

def score(path):
    res, d = measure(path)
    if not res: return d.ns / 1000.0
    return 1000 * max(r["dips"] for r in res) + 100 * max(r["steps"] for r in res) + sum(r["dips"] for r in res) + d.ns / 1000.0

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f in sys.argv[1:]:
        res, d = measure(f)
        print(f"== {os.path.basename(f)} order={os.environ.get('DTL_ORDER', 'stable')} searches={d.ns}")
        for r in sorted(res, key=lambda r: -r["steps"])[:5]:
            print(f"   player {r['p']} |ctx| {r['ctx']} DEF steps {r['steps']} dips {r['dips']} (s, r0, M before, M after): {r['seq']}")
