"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), GAP-C (TW) on MIXED searches only (both players win something):
learned tangles inside W_p / outside / straddling. DTL_ORDER = oink | stable. Usage: dtl_twmixed.py G.pg ..."""
import sys, os
sys.path.insert(0, "/home/user/parity_games_challange/experiments/alg"); sys.path.insert(0, "/home/user/parity_games_challange/experiments/harness")
import pg, dtl_kin as K
sys.setrecursionlimit(100000); tab = {"mixed searches": 0, "inside": 0, "outside": 0, "straddle": 0}
for f in sys.argv[1:]:
    g = pg.read(f); d0 = K.P.build(g); d = K.KI(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.run()
    for tr in d.trace:
        W = tr["Wp"]; G = set(tr["G"])
        if not W or W == G: continue
        tab["mixed searches"] += 1
        for C in tr["newt"]: tab["inside" if C <= W else "straddle" if C & W else "outside"] += 1
print(tab)
