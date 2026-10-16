#!/usr/bin/env python3
"""L-RED successor 3 (Opus 5.5), 2026-10-16: REPLAY depth (GAP-A-M §6.3/§20; L-ALG dtl_pieces.replays2, read-only via
LALG_DIR >= c7fc7cb) measured on A_DTL itself (not C6), in the order given by DTL_ORDER (oink: Oink's exact order as in
dtl_deficit.build; stable: (priority, id)). Fitness: 10000 x replay depth + 100 x replays + longest phase + searches/1000.
Usage: DTL_ORDER=oink LALG_DIR=.. replay.py G.pg ... ; --c6 measures C6 instead (stable order only, as L-ALG)."""
import sys, os

def _mods():
    ld = os.environ["LALG_DIR"]
    for q in (os.path.join(ld, "experiments", "alg"), os.path.join(ld, "experiments", "harness"), os.path.join(ld, "experiments", "dtl-bench")):
        if q not in sys.path: sys.path.insert(0, q)
    import dtl_pieces as P, dtl_pyref as D, pg
    return P, D, pg

def run(path, c6=False):
    P, D, pg = _mods(); g = pg.read(path)
    if c6:
        from dtl_c6proto import C6
        base, kw = C6, {}; idx = sorted(range(g.n), key=lambda v: (g.prio[v], v))
    elif os.environ.get("DTL_ORDER") == "oink":
        from stdsort import oink_order
        idx = oink_order(g.prio); D.TV_SORTED = True; D.PEARCE = True; kw = {"ins_desc": True}; base = D.DTL
    else:
        idx = sorted(range(g.n), key=lambda v: (g.prio[v], v)); kw = {}; base = D.DTL
    new = {v: i for i, v in enumerate(idx)}
    d = P.mk(base)([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx], **kw)
    d.run(); rep, dep = P.replays2(d); ph = P.level_seqs(d)
    return dict(depth=dep, replays=rep, longest=max((len(x) for x in ph), default=0), searches=d.iterations, n=g.n,
                phases=[x for x in ph if x])

def score(path):
    r = run(path)
    return 10000 * r["depth"] + 100 * r["replays"] + r["longest"] + r["searches"] / 1000.0

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    c6 = "--c6" in sys.argv
    for f in [a for a in sys.argv[1:] if a != "--c6"]:
        r = run(f, c6)
        print(f"== {os.path.basename(f)} {'C6' if c6 else 'A_DTL'} order={'stable' if c6 else os.environ.get('DTL_ORDER', 'stable')} n={r['n']} searches={r['searches']} depth={r['depth']} replays={r['replays']} longest={r['longest']} levels={r['phases']}")

def score_phase(path):
    """successor 3: longest phase (transitions within one phase, A_DTL) first, then searches."""
    r = run(path)
    return 100 * r["longest"] + r["searches"] + r["depth"] / 10.0
