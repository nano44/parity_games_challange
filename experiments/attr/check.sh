#!/usr/bin/env bash
# A1 regression (fast, < 1 min): psolQ/psolB/psol and the Strahler DP reproduce the published outcomes on HKP's figures
# and on the M2 counterexamples (validate.py --quick); the minimal instances of docs/attr/A1-results.md still fail as
# recorded; every game with n = 2 is solved by psolQ and by Algorithm 1 (regions).
set -euo pipefail
cd "$(dirname "$0")"
python3 -I validate.py --quick | tail -1 | grep -q "VALIDATE PASS"
echo "validate --quick: PASS"
python3 -I a3_validate.py --quick | tail -1 | grep -q "A3-VALIDATE PASS"
echo "a3_validate --quick: PASS"
python3 -I - <<'PY'
import sys; sys.path.insert(0, "."); sys.path.insert(0, "../harness")
import pg, a1lib
exp = {  # file: (psolq, psolb, psol, avh, Strahler)
    "instances/psolq_min_n3_m4.pg": ("undecided", "undecided", "undecided", "solved", 1),
    "instances/alg1_min_n4_m5.pg": ("undecided", "undecided", "solved", "WRONG", 1),
    "instances/psolq_str2_n4_m6.pg": ("undecided", "undecided", "undecided", "solved", 2),
    "instances/psolq_pd_n3_m4.pg": ("undecided", "undecided", "undecided", "solved", 1),
    "instances/avh_badstrat_n3_m4.pg": ("solved", "solved", "solved", "BADSTRAT", 1),
}
import os
for f, e in exp.items():
    if not os.path.exists(f):
        print(f"{f}: not written yet, skipped"); continue
    r = a1lib.classify(pg.read(f), want_strahler=True, others=True)
    got = (r["psolq"], r["psolb"], r["psol"], r["avh"], r["str"])
    assert got == e, (f, got, e)
    print(f"{f}: psolq/psolb/psol/alg1/Str = {got}")
import peeling
for f, (ps, p2) in {"instances/llit_witness_buchi_n3.pg": (True, True), "instances/psolq_min_n3_m4.pg": (False, False),
                    "instances/alg1_min_n4_m5.pg": (False, False), "../harness/bench/hkp_fig4a.pg": (False, False),
                    "../harness/bench/hkp_fig4b.pg": (True, True)}.items():
    g = pg.read(f); r = a1lib.classify(g, others=True)
    got = (peeling.both(g, r["ref"], peeling.peeling), peeling.both(g, r["ref"], peeling.pa2))
    assert got == (ps, p2) and (r["psolb"] == "solved") == p2, (f, got, r["psolb"])
    print(f"{f}: PA* {ps}, PA** {p2} = psolB-complete")
from psolc import PsolC
for f, (undec, b, q) in {"instances/psolc_min_n4_m6.pg": (4, "undecided", "undecided"),
                         "instances/tc2_psolc_nothing_n9_m11.pg": (9, "undecided", "undecided"),
                         "instances/dtr_fig4.pg": (0, "undecided", "solved"),
                         "../harness/bench/hkp_fig6.pg": (0, "undecided", "undecided")}.items():
    g = pg.read(f); r = a1lib.classify(g, others=True)
    w, st, res, _ = PsolC(g).run()
    assert len(res) == undec and (r["psolb"], r["psolq"]) == (b, q), (f, len(res), r["psolb"], r["psolq"])
    print(f"{f}: psolC undecided {len(res)}, psolB {b}, psolQ {q}")
n2 = 0
for cfg, m in a1lib.succ_orbits(2):
    for g in a1lib.games_on(cfg, 2):
        r = a1lib.classify(g); n2 += 1
        assert r["psolq"] == "solved" and r["avh"] in ("solved", "BADSTRAT"), (pg.dumps(g), r)
print(f"n=2: all {n2} canonical games solved by psolQ; Algorithm 1 regions right on all")
PY
