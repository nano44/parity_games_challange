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
import strfam
for s_, kf in ((2, 1), (3, 2), (4, 3)):
    g = strfam.S(s_); ref = zielonka.solve(g)
    ne.MODE = "h"; k, undec, _ = alglib.k_needed(g, ref, kf)
    assert k == kf and all(u == g.n for u in undec[:kf]), (s_, k, undec)
    print(f"sibling-trap family S_{s_} (n={g.n}): C2 decides nothing for k < {kf}, solves at k = {kf}")
PY
# every lane script must at least compile (a broken dtl_pieces.py once passed verify)
python3 -I -c "import ast, glob; [ast.parse(open(f).read(), f) for f in glob.glob('*.py')]; print('scripts compile')"
# GAP-A-M.md §4: the synthetic counter to fixed-context monotonicity (M) must keep reproducing
python3 -I dtl_m_synth.py | tail -1
# GAP-A-M.md §4b: the same failure in an actual A_DTL run (Python always; Oink trace when Oink is built)
python3 -I dtl_mviol_check.py | tail -1
# GAP-A-M.md §18: the synthetic genuine-tangle counter to candidate (LEX) must keep reproducing (exit 0 iff it does)
python3 -I dtl_lexcounter.py | tail -1
# GAP-A-M.md §18f: the synthetic pure DEF cycle (state revisit at an ideal-stable context) must keep reproducing
python3 -I dtl_staterevisit.py | tail -1
# GAP-A-M.md §18h: (LEX) fails in an actual A_DTL run (both order data)
python3 -I dtl_lexviol_check.py | tail -1
# GAP-A-M.md §18i: (CM) fails in an actual A_DTL run (both order data)
python3 -I dtl_cmviol_check.py | tail -1
# GAP-A-M.md §18k: synthetic two-fall context (L-RED's (F1) is not structural)
python3 -I dtl_twofall.py | tail -1
# GAP-A-M.md §10: the abstract barrier model APP(k) must keep satisfying its checkable axioms
python3 -I app_model.py 1 2 3 4 5 6 | tail -1
# GAP-A-M.md §21: the chain family keeps S = |G'| - 1 searches in one phase (tightness of (SPP-sharp)), both order data
python3 -I dtl_chainfam.py --check | tail -1
# GAP-A-M.md §21d: the First-Difference Lemma holds mechanically on three long phases (Oink order)
DTL_ORDER=oink python3 -I dtl_fdlcheck.py instances/spp_final_n20.pg instances/spp_chain_up_n43.pg ../red/carry/instances/spp19_oink_n30.pg | tail -1
# GAP-A-M.md §26b: lagfam collapsed to d = 3 (flat7) rebuilds bit-identically and keeps re-steal depth D = 4 (stable order)
python3 -I fixd_lagcollapse.py 4 flat7 "${TMPDIR:-/tmp}/lagflat7_chk.pg" > /dev/null
cmp "${TMPDIR:-/tmp}/lagflat7_chk.pg" instances/lagflat7_d3_D4.pg
RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0 DTL_ORDER=stable python3 -I dtl_stealdepth.py instances/lagflat7_d3_D4.pg | grep -m1 "max k" | grep -q "max depth 4"
echo "ALG-CHECK PASS"
