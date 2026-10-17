"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5): (SPP-sharp) "S <= max(1, |G'| - 1)" on EVERY game with n vertices,
owners in {0,1}, priorities 0..P and every non-empty successor set (harness/exhaustive.py), in order datum DTL_ORDER.
Usage: dtl_sppexh.py n P"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import exhaustive, dtl_spp as P
n, Pm = int(sys.argv[1]), int(sys.argv[2]); cnt = viol = 0; best = (0,)
for g in exhaustive.iter_games(n, Pm):
    d = P.build(g); d.run(); cnt += 1
    for r in P.phases(d):
        if r["S"] > max(1, r["G"] - 1): viol += 1
        best = max(best, (r["S"] - r["G"], r["S"], r["G"]))
print(f"n={n} P={Pm} order={os.environ.get('DTL_ORDER', 'stable')}: {cnt} games, (SPP-sharp) violations {viol}, max (S-|G'|, S, |G'|) = {best}")
