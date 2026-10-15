#!/usr/bin/env bash
# L-ALG regression (< 1 min, run by scripts/verify.sh): NE(0) equals psolC on the instance library; NE(1) (C1) and
# NE'(1) (C2) solve the psolC killers with verified oracle strategies; the recorded C1 killers still fail at their k and
# are solved one level up; everything sound against Zielonka.
set -euo pipefail
cd "$(dirname "$0")"
python3 -I - <<'PY'
import sys, glob; sys.path.insert(0, "."); sys.path.insert(0, "../harness"); sys.path.insert(0, "../attr")
import pg, ne, zielonka, verify, alglib
from psolc import PsolC
files = sorted(glob.glob("../attr/instances/*.pg")) + sorted(glob.glob("../m2/counterexamples/*.pg")) + sorted(glob.glob("../harness/bench/*.pg"))
for f in files:
    g = pg.read(f); ref = zielonka.solve(g)
    wc, _, rc, _ = PsolC(g, strat=None).run()
    w0, _, _ = ne.solve(g, 0)
    assert w0 == wc, (f, "NE(0) != psolC")
    for mode in ("esc", "h"):
        ne.MODE = mode
        win, strat, res, info = ne.solve_with_strategy(g, 1, "oracle")
        assert alglib.status(win, ref) == "solved", (f, mode, alglib.status(win, ref), len(res))
        assert not verify.check(g, win, strat) and not info["strat_fail"], (f, mode, info)
print(f"library: NE(0) == psolC on {len(files)} games; C1 and C2 at k=1 solve all, strategies verified")
exp = {"instances/c1_k1_min_n7_m10.pg": 1, "instances/c1_k2_min_n11_m15.pg": 2}
for f, kf in exp.items():
    g = pg.read(f); ref = zielonka.solve(g)
    ne.MODE = "esc"; k, undec, verd = alglib.k_needed(g, ref, kf + 1, with_strat=True)
    assert k == kf + 1 and undec[kf] == g.n and not verd["verify"], (f, k, undec, verd)
    ne.MODE = "h"; k2, undec2, verd2 = alglib.k_needed(g, ref, 1, with_strat=True)
    assert k2 == 1 and not verd2["verify"], (f, k2, undec2)
    print(f"{f}: C1 undecided at k={kf} ({undec[kf]}/{g.n}), solved at k={kf+1}; C2 solves at k=1; strategies verified")
print("ALG-CHECK PASS")
PY
