"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), GAP-C: completeness of A_DTL (Python emulation, order datum
DTL_ORDER) on EVERY game with n vertices, priorities 0..P (harness/exhaustive.py): the run must solve every vertex, and
the regions must equal Zielonka's. Usage: dtl_gapc_exh.py n P"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
sys.path.insert(0, os.path.join(HERE, "..", "dtl-bench"))
import exhaustive, zielonka, dtl_pyref as D
n, Pm = int(sys.argv[1]), int(sys.argv[2]); order = os.environ.get("DTL_ORDER", "stable"); cnt = inc = wrong = 0
for g in exhaustive.iter_games(n, Pm):
    W, S, d = D.solve_game(g, order=order); cnt += 1
    if any(w is None for w in W): inc += 1; print("INCOMPLETE", g.prio, g.owner, g.succ, flush=True); continue
    z = zielonka.solve(g)
    zw = z[0] if isinstance(z, tuple) else z
    if list(W) != list(zw): wrong += 1
print(f"n={n} P={Pm} order={order}: {cnt} games, incomplete {inc}, region mismatches vs Zielonka {wrong}")
