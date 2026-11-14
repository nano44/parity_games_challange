#!/usr/bin/env python3
"""L-RED 71 R247: RF and Howard with a SECOND valuation engine: L-NEW's si.Engine (claude/l-new a143d406, env LNEW) supplies Xi_sigma, Odd's
optimal counterstrategy and the improving edges; the dependency digraph and the sink components are rf247's (the rule itself has one
implementation in this lane). Checks the iteration counts of si247.py (values by n5s237.vjproc) on the same games and starts.
Usage: rfv247.py RULE GAME.pg [s3|file]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); LNEW = os.environ["LNEW"]
sys.path[:0] = [HERE, os.path.join(HERE, "..", "r237")] + [os.path.join(LNEW, p) for p in ("experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
import si247, rf247, pg
from si import Engine

class Shim:
    """the part of si247.SI that rf247.dep / rule_rf use, on top of si.Engine"""
    def __init__(s, prio, owner, succ):
        s.n = len(prio); s.isE = [o == 0 for o in owner]; s.succ = succ; s.E = Engine(pg.Game(list(prio), list(owner), [list(x) for x in succ]))
    def best(s, val, ws): return max(ws, key=lambda w: (s.E.key(val[w]), w))

if __name__ == "__main__":
    rule, fn = sys.argv[1], sys.argv[2]; st = sys.argv[3] if len(sys.argv) > 3 else "s3"
    prio, owner, succ = si247.parse(fn); e0 = si247.SI(prio, owner, succ); sigma = e0.s3()
    if st == "file": sigma.update(si247.read_start(fn))
    sh = Shim(prio, owner, e0.succ); n = sh.n; it = 0
    while True:
        tup = tuple(sigma.get(v, -1) for v in range(n)); val, sbar = sh.E.evaluate(tup); I = {}
        for v, w in sh.E.improving(tup, val): I.setdefault(v, []).append(w)
        if not I: break
        full = {v: (sbar[v] if not sh.isE[v] else None) for v in range(n)}
        ch = rf247.rule_rf(sh, sigma, val, full, I) if rule == "rf" else {v: sh.best(val, ws) for v, ws in I.items()}
        for v, w in ch.items(): sigma[v] = w
        it += 1
    print("RFV247", os.path.basename(fn), "n", n, "rule", rule, "start", st, "iterations", it, flush=True)
