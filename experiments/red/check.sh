#!/usr/bin/env bash
# L-RED self-check (run by scripts/verify.sh). Pins: gated_bland N=6 -> 63 MSF iterations (both the generator and the
# committed instance), the two Claim F counterexamples (1 escaped switch each), MSF == Bland correspondence N=2..6,
# and a small engine validation (brute force, Zielonka, verify.py).  ~20 s.
set -euo pipefail
cd "$(dirname "$0")"
t=$(mktemp -d); trap 'rm -rf "$t"' EXIT
python3 gens_red.py gated_bland 6 > "$t/g6.pg"
cmp -s "$t/g6.pg" instances/gated_bland_N6.pg || { echo "generator drifted from instances/gated_bland_N6.pg"; exit 1; }
out=$(python3 vj.py msf "$t/g6.pg" 2>&1 >"$t/g6.sol" | sed -n 1p)
[[ "$out" == "solved with 63 iterations,"* ]] || { echo "gated_bland 6: expected 63 iterations, got: $out"; exit 1; }
python3 ../harness/zielonka.py "$t/g6.pg" > "$t/g6.zlk"
python3 - "$t" <<'PY'
import sys; sys.path.insert(0, "../harness"); import pg, verify
t = sys.argv[1]; g = pg.read(f"{t}/g6.pg"); s = open(f"{t}/g6.sol").read()
assert pg.read_sol(s, g.n) == pg.read_sol(open(f"{t}/g6.zlk").read(), g.n), "regions differ from Zielonka"
e = verify.check(g, pg.read_sol(s, g.n), verify.read_strategy(s, g.n)); assert not e, e
PY
for f in claimF_len_cf1 claimF_bit_cf2; do
  out=$(python3 vj.py msf instances/$f.pg --start spec:2:1 2>&1 >/dev/null | sed -n 1p)
  [[ "$out" == "solved with 1 iterations,"*"escapes 1"* ]] || { echo "$f: expected 1 escaped switch, got: $out"; exit 1; }
done
python3 gate.py 4 | grep -q "lsf on gate(G_4, labels Bland): n=22 switches=15" || { echo "gate.py drifted"; exit 1; }
python3 fhz.py lockstep3 3 1 1 1 1 | grep -q "all three models agree" || { echo "fhz lockstep3 failed"; exit 1; }
python3 fhz.py relation 4 2 2 2 40 | grep -q "differ in 0" || { echo "fhz relation check failed"; exit 1; }
python3 fhz.py export 4 1 1 1 "$t/f4.pg" >/dev/null && cmp -s "$t/f4.pg" instances/fhz_n4_r1s1t1.pg || { echo "fhz export drifted"; exit 1; }
python3 gens_red.py friedmann_Gn 2 > "$t/G2.pg"; st=$(grep "^% start" "$t/G2.pg" | sed "s/% start //")
out=$(python3 vj.py most-improved "$t/G2.pg" --start "spec:$st" 2>&1 >/dev/null | sed -n 1p)
[[ "$out" == "solved with 15 iterations,"* ]] || { echo "friedmann_Gn 2 under S7: expected 15, got: $out"; exit 1; }
python3 antichain_check.py "$t/G2.pg" most-improved --start "spec:$st" | grep -q "at 0 steps" || { echo "antichain_check: S7 must be downstream-first"; exit 1; }
python3 gens_red.py fhz_padded 4 | grep -v "^%" > "$t/fp4.pg"; cmp -s "$t/fp4.pg" instances/fhz_padded_n4.pg || { echo "fhz_padded generator drifted from instances/fhz_padded_n4.pg"; exit 1; }
python3 gens_red.py fhz_padded 2 | grep -v "^%" > "$t/fp2.pg"; out=$(python3 vj.py most-improved "$t/fp2.pg" 2>&1 >/dev/null | sed -n 1p)
[[ "$out" == "solved with 16 iterations,"* ]] || { echo "fhz_padded 2 under S7: expected 16, got: $out"; exit 1; }
python3 zadeh_lb.py instances/zadehexp_N2_labelled.pg --tie lb | grep -q "43 switches, 38 tie steps, 131 'chosen before competitor' constraints; fixed total order exists: False" || { echo "zadeh_lb drifted (R7)"; exit 1; }
python3 zadeh_lb.py instances/zadehexp_N2_labelled.pg --tie index | grep -q "41 switches" || { echo "zadeh_lb index drifted (R7)"; exit 1; }
if [[ -x ../../tools/oink/build/oink ]]; then
  python3 dtl/gens_dtl.py chain 10 > "$t/chain10.pg"; ../../tools/oink/build/oink --dtl --no-single --no-wcwc "$t/chain10.pg" 2>&1 | grep -q "found 1 dominions and 8 tangles" || { echo "dtl chain 10 drifted (R8)"; exit 1; }
  python3 dtl/gens_dtl.py counter_odftl 3 > "$t/odftl3.pg"; ../../tools/oink/build/oink --dtl --no-single --no-wcwc "$t/odftl3.pg" 2>&1 | grep -q "and 9 tangles" || { echo "dtl counter_odftl 3 drifted (R8)"; exit 1; }
else echo "dtl chain check skipped (no oink build)"; fi
# R9 (2026-10-16): the instrumented DTL tracer (built on dtl-bench/dtl_py.py) reproduces L-ALG's F8 instance exactly and
# Claim P/Q hold on it; when Oink is built the tracer's counts are cross-checked against the pinned binary.
out=$(python3 -I dtl/dtl_flipflop.py dtl/instances/lalg_dtl_restart8_n20.pg --quiet 2>&1 | sed -n 1p)
[[ "$out" == "n=20 tangles=36 dominions=1 iterations=5" ]] || { echo "dtl_flipflop drifted on lalg_dtl_restart8_n20: $out"; exit 1; }
out=$(python3 -I dtl/dtl_ctxmono.py dtl/instances/lalg_dtl_restart8_n20.pg dtl/instances/lalg_dtl_pertop31_n18.pg 2>&1 | grep -c "ClaimP violations 0 ClaimQ violations 0")
[[ "$out" == "2" ]] || { echo "dtl_ctxmono: Claim P/Q pins changed"; exit 1; }
if [[ -x ../../tools/oink/build/oink ]]; then
  python3 -I dtl/dtl_flipflop.py dtl/instances/lalg_dtl_restart8_n20.pg --quiet --oink ../../tools/oink/build/oink 2>&1 | grep -q "MATCH" || { echo "dtl_flipflop vs oink: DIFFER"; exit 1; }
fi
# R11 (2026-10-16, Opus 5.5): (r2) counter-instance on L-ALG's real run; bsolo fast level = 4 searches one tangle each (R10).
python3 -I carry/r2_check.py carry/instances/lalg_dtl_mviol_n20.pg > "$t/r2.log" 2>&1 || { cat "$t/r2.log"; echo "r2_check FAILED"; exit 1; }
python3 -I carry/bsolo.py 4 2 "$t/bsolo.pg" 2>/dev/null
out=$(python3 -I dtl/dtl_flipflop.py "$t/bsolo.pg" --quiet 2>&1 | sed -n 1p)
[[ "$out" == "n=16 tangles=4 dominions=2 iterations=7" ]] || { echo "bsolo drifted: $out"; exit 1; }
python3 -I carry/liftmod.py 3 "$t/lift3.pg"
out=$(python3 -I dtl/dtl_flipflop.py "$t/lift3.pg" --quiet 2>&1 | sed -n 1p)
[[ "$out" == "n=30 tangles=3 dominions=1 iterations=3" ]] || { echo "liftmod 3 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/h4_notweaker_n20.pg --quiet 2>&1 | sed -n 1p)   # R15 instance
[[ "$out" == "n=20 tangles=12 dominions=1 iterations=7" ]] || { echo "h4_notweaker_n20 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/h4_disjoint_n20.pg --quiet 2>&1 | sed -n 1p)   # R15 instance 2
[[ "$out" == "n=20 tangles=21 dominions=2 iterations=10" ]] || { echo "h4_disjoint_n20 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/lemmaS_viol_n20.pg --quiet 2>&1 | sed -n 1p)   # R16 Lemma S violation
[[ "$out" == "n=20 tangles=18 dominions=1 iterations=8" ]] || { echo "lemmaS_viol_n20 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/lemmaS_Mdrop_n20.pg --quiet 2>&1 | sed -n 1p)   # R16 Lemma S, M drops
[[ "$out" == "n=20 tangles=15 dominions=1 iterations=7" ]] || { echo "lemmaS_Mdrop_n20 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/h4_def2ctx_n20.pg --quiet 2>&1 | sed -n 1p)   # R15: 2 DEF in one context
[[ "$out" == "n=20 tangles=12 dominions=2 iterations=7" ]] || { echo "h4_def2ctx_n20 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/h4_def7_n28.pg --quiet 2>&1 | sed -n 1p)   # R15: 7 DEF in one context
[[ "$out" == "n=28 tangles=18 dominions=3 iterations=13" ]] || { echo "h4_def7_n28 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/h4_compound_n44.pg --quiet 2>&1 | sed -n 1p)   # R15: compounding
[[ "$out" == "n=44 tangles=25 dominions=3 iterations=13" ]] || { echo "h4_compound_n44 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/h4_compound2x2_n44.pg --quiet 2>&1 | sed -n 1p)   # R15: 2-level replay
[[ "$out" == "n=44 tangles=30 dominions=2 iterations=13" ]] || { echo "h4_compound2x2_n44 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/cm_mdrop_oink_n28.pg --quiet 2>&1 | sed -n 1p)   # successor 3: (CM) M 13->1 (Oink order)
[[ "$out" == "n=28 tangles=12 dominions=1 iterations=7" ]] || { echo "cm_mdrop_oink_n28 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/cm_mdrop_both_n28.pg --quiet 2>&1 | sed -n 1p)   # successor 3: (CM) M 8->7 (both orders)
[[ "$out" == "n=28 tangles=24 dominions=1 iterations=9" ]] || { echo "cm_mdrop_both_n28 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/lex_viol_inj_n28.pg --quiet 2>&1 | sed -n 1p)   # successor 3 R18: (LEX)/(NR) false, injective
[[ "$out" == "n=28 tangles=23 dominions=1 iterations=8" ]] || { echo "lex_viol_inj_n28 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/lex_viol_tie_n28.pg --quiet 2>&1 | sed -n 1p)   # successor 3 R18: same, priority ties (Oink order)
[[ "$out" == "n=28 tangles=23 dominions=1 iterations=8" ]] || { echo "lex_viol_tie_n28 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/f1_twofall_n48.pg --quiet 2>&1 | sed -n 1p)   # successor 3 R19: two fall steps at one context
[[ "$out" == "n=48 tangles=32 dominions=2 iterations=8" ]] || { echo "f1_twofall_n48 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/replay4_n32.pg --quiet 2>&1 | sed -n 1p)   # successor 3 R20: replay depth 4 at n = 32
[[ "$out" == "n=32 tangles=38 dominions=2 iterations=13" ]] || { echo "replay4_n32 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/f1_twodef_n48.pg --quiet 2>&1 | sed -n 1p)   # successor 3 R20: two DEF fall steps at one context
[[ "$out" == "n=48 tangles=41 dominions=1 iterations=11" ]] || { echo "f1_twodef_n48 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/spp19_oink_n30.pg --quiet 2>&1 | sed -n 1p)   # successor 3 R21: 19 searches in one phase (Oink order)
[[ "$out" == "n=30 tangles=30 dominions=2 iterations=21" ]] || { echo "spp19_oink_n30 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/spp19_stable_n30.pg --quiet 2>&1 | sed -n 1p)   # successor 3 R21: 19 searches in one phase (both orders)
[[ "$out" == "n=30 tangles=40 dominions=3 iterations=23" ]] || { echo "spp19_stable_n30 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/absmono_viol_n44.pg --quiet 2>&1 | sed -n 1p)   # box 5 R22: (ABS-mono) and (ABS-mono-pw) FALSE
[[ "$out" == "n=44 tangles=34 dominions=1 iterations=5" ]] || { echo "absmono_viol_n44 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/gapb_dup_n20.pg --quiet 2>&1 | sed -n 1p)   # box 5 R23: orphan + duplicate-check hit (GAP-beta), run complete
[[ "$out" == "n=20 tangles=26 dominions=1 iterations=14" ]] || { echo "gapb_dup_n20 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/gapbW_dup_n20.pg --quiet 2>&1 | sed -n 1p)   # box 5 R23 s6: orphan + duplicate INSIDE W_p (NO-ORPHAN-W false), run complete
[[ "$out" == "n=20 tangles=8 dominions=2 iterations=6" ]] || { echo "gapbW_dup_n20 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/spp22_oink_n40.pg --quiet 2>&1 | sed -n 1p)   # box 5 R24: 22 searches in one phase at |G'| = 38 (both orders)
[[ "$out" == "n=40 tangles=41 dominions=3 iterations=28" ]] || { echo "spp22_oink_n40 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/kfirst_viol_n13.pg --quiet 2>&1 | sed -n 1p)   # box 6 R25: (K-first) and (K4-B) FALSE, both orders, run complete
[[ "$out" == "n=13 tangles=6 dominions=2 iterations=5" ]] || { echo "kfirst_viol_n13 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/pk_viol_n20.pg --quiet 2>&1 | sed -n 1p)   # box 6 R27: (P-K) and (K-STEP-first) FALSE, both orders, run complete
[[ "$out" == "n=20 tangles=4 dominions=1 iterations=2" ]] || { echo "pk_viol_n20 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/spp25_oink_n40.pg --quiet 2>&1 | sed -n 1p)   # box 6 R24 addendum: 25 searches in one phase at |G'| = 38 (Oink order)
[[ "$out" == "n=40 tangles=56 dominions=3 iterations=31" ]] || { echo "spp25_oink_n40 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/tstep_near_n20.pg --quiet 2>&1 | sed -n 1p)   # box 6 R27 §5: (T-STEP) near miss (KT broken by T, barren, 1 D-tangle before)
[[ "$out" == "n=20 tangles=19 dominions=1 iterations=10" ]] || { echo "tstep_near_n20 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/kin_viol_n29.pg --quiet 2>&1 | sed -n 1p)   # box 6 R29: (K-in), (K-low), (TW), (S-LOW tight), KT-STEP FALSE, both orders, run complete
[[ "$out" == "n=29 tangles=15 dominions=2 iterations=8" ]] || { echo "kin_viol_n29 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/meet_viol_n17.pg --quiet 2>&1 | sed -n 1p)   # box 7 R30: (MEET) of GAP-C §18r FALSE, both orders, run complete
[[ "$out" == "n=17 tangles=4 dominions=2 iterations=6" ]] || { echo "meet_viol_n17 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/meet_viol_n29.pg --quiet 2>&1 | sed -n 1p)   # box 7 R30: (MEET) FALSE (unshrunk climb hit from kin_viol_n29)
[[ "$out" == "n=29 tangles=17 dominions=2 iterations=9" ]] || { echo "meet_viol_n29 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/ctx11_n40.pg --quiet 2>&1 | sed -n 1p)   # box 7: 11 distinct first-difference contexts in one phase (CTX+), both orders
[[ "$out" == "n=40 tangles=48 dominions=1 iterations=24" ]] || { echo "ctx11_n40 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/fallv_viol_n28.pg --quiet 2>&1 | sed -n 1p)   # box 7 R32: (FALL-V) FALSE, vertex 14 falls twice at the root context, both orders
[[ "$out" == "n=28 tangles=17 dominions=1 iterations=7" ]] || { echo "fallv_viol_n28 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/stealer_viol_n76.pg --quiet 2>&1 | sed -n 1p)   # box 7 R34: (STEALER-MONO) FAILS 3x in stable order (Oink order holds)
[[ "$out" == "n=76 tangles=47 dominions=1 iterations=7" ]] || { echo "stealer_viol_n76 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/stealonce_viol_n76.pg --quiet 2>&1 | sed -n 1p)   # box 8 R35: (STOLEN-PERM), (STAYS-MET), (NO-REFIRE) FAIL 7x and (STEAL-ONCE*) max 2, stable order (Oink order holds)
[[ "$out" == "n=76 tangles=50 dominions=1 iterations=7" ]] || { echo "stealonce_viol_n76 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/stealonce_core_n76.pg --quiet 2>&1 | sed -n 1p)   # box 8 R36: edge-minimised R35 core (101 edges), STEAL-ONCE* k 2 twice, depth 1, stable
[[ "$out" == "n=76 tangles=15 dominions=5 iterations=4" ]] || { echo "stealonce_core_n76 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/stealonce_both_n45.pg --quiet 2>&1 | sed -n 1p)   # box 8 R36 §5: STEAL-ONCE* k 2 in BOTH order data (vertex-minimised R35 core)
[[ "$out" == "n=45 tangles=17 dominions=2 iterations=6" ]] || { echo "stealonce_both_n45 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/firedstep13_n76.pg --quiet 2>&1 | sed -n 1p)   # box 8 R36: 13 distinct tangles fired at one step (dtl_firedlong2 FL_ALL=1, stable)
[[ "$out" == "n=76 tangles=38 dominions=5 iterations=4" ]] || { echo "firedstep13_n76 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/firedlong667_n43.pg --quiet 2>&1 | sed -n 1p)   # box 8 R36 §4: long-phase FIRED-R 4 fired at |R| 6, S 14 (root/firedlong.py, both orders)
[[ "$out" == "n=43 tangles=22 dominions=2 iterations=16" ]] || { echo "firedlong667_n43 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/firedlong667_n20.pg --quiet 2>&1 | sed -n 1p)   # box 8 R36 §4: long-phase FIRED-R 4 fired at |R| 6, S 12 (both orders)
[[ "$out" == "n=20 tangles=26 dominions=1 iterations=14" ]] || { echo "firedlong667_n20 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/ctx6_n20.pg --quiet 2>&1 | sed -n 1p)   # box 9 R38: (CTX+) curve, 6/13 first-difference contexts/transitions (stable)
[[ "$out" == "n=20 tangles=24 dominions=1 iterations=14" ]] || { echo "ctx6_n20 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/ctx7_n30.pg --quiet 2>&1 | sed -n 1p)   # box 9 R38: (CTX+) curve, 7/15 first-difference contexts/transitions (stable)
[[ "$out" == "n=30 tangles=29 dominions=1 iterations=14" ]] || { echo "ctx7_n30 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/ctx6_n56.pg --quiet 2>&1 | sed -n 1p)   # box 9 R38: (CTX+) curve, 6/12 first-difference contexts/transitions (stable)
[[ "$out" == "n=56 tangles=56 dominions=1 iterations=15" ]] || { echo "ctx6_n56 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/fired10_n20.pg --quiet 2>&1 | sed -n 1p)   # box 7: 10 distinct tangles fired at one context of |R| 12 (FIRED-R ratio 0.83, Oink order)
[[ "$out" == "n=20 tangles=14 dominions=1 iterations=3" ]] || { echo "fired10_n20 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/ctx13_n40.pg --quiet 2>&1 | sed -n 1p)   # box 7: 13 distinct first-difference contexts in one phase (CTX+), both orders
[[ "$out" == "n=40 tangles=91 dominions=1 iterations=29" ]] || { echo "ctx13_n40 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/ctx12_n40.pg --quiet 2>&1 | sed -n 1p)   # box 7: 12 distinct first-difference contexts in one phase (CTX+), both orders
[[ "$out" == "n=40 tangles=65 dominions=1 iterations=26" ]] || { echo "ctx12_n40 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/fall4_n116.pg --quiet 2>&1 | sed -n 1p)   # box 7 R31 §2: 4 descents of Π_R at one context (FALL), both orders
[[ "$out" == "n=116 tangles=82 dominions=6 iterations=13" ]] || { echo "fall4_n116 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/fall3_n76.pg --quiet 2>&1 | sed -n 1p)   # box 7 R31: 3 descents of Π_R at one context (FALL), both orders
[[ "$out" == "n=76 tangles=56 dominions=3 iterations=10" ]] || { echo "fall3_n76 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py lag/instances/depth2_n39.pg --quiet 2>&1 | sed -n 1p)   # box 10 R39: first re-steal of DEPTH 2 (dtl_stealdepth, both order data)
[[ "$out" == "n=39 tangles=15 dominions=1 iterations=10" ]] || { echo "depth2_n39 drifted: $out"; exit 1; }
[[ "$(sha1sum lag/instances/depth2_n39.pg | cut -c1-12)" == "6200e5869e8f" ]] || { echo "depth2_n39 sha1 changed"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py lag/instances/depth3_n46.pg --quiet 2>&1 | sed -n 1p)   # box 10 R39: re-steal DEPTH 3 (both order data)
[[ "$out" == "n=46 tangles=15 dominions=1 iterations=11" ]] || { echo "depth3_n46 drifted: $out"; exit 1; }
[[ "$(sha1sum lag/instances/depth3_n46.pg | cut -c1-12)" == "54cc8526238e" ]] || { echo "depth3_n46 sha1 changed"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py lag/instances/depth4_n53.pg --quiet 2>&1 | sed -n 1p)   # box 10 R39: re-steal DEPTH 4, k 3 (both order data)
[[ "$out" == "n=53 tangles=18 dominions=1 iterations=12" ]] || { echo "depth4_n53 drifted: $out"; exit 1; }
[[ "$(sha1sum lag/instances/depth4_n53.pg | cut -c1-12)" == "40dacf0e4b6f" ]] || { echo "depth4_n53 sha1 changed"; exit 1; }
for row in "4 50 c8fd86165aba 17 12" "8 78 46ad828c7901 25 16" "12 106 0dd2899eacfe 33 20"; do   # box 10 R39 §6: UNIFORM family lagfam.py, depth = D
  set -- $row; f="lag/instances/fam_D$1_n$2.pg"
  python3 -I lag/lagfam.py "$1" "$t/fam.pg" && cmp -s "$t/fam.pg" "$f" || { echo "lagfam.py D=$1 no longer generates $f"; exit 1; }
  [[ "$(sha1sum "$f" | cut -c1-12)" == "$3" ]] || { echo "$f sha1 changed"; exit 1; }
  out=$(python3 -I dtl/dtl_flipflop.py "$f" --quiet 2>&1 | sed -n 1p)
  [[ "$out" == "n=$2 tangles=$4 dominions=1 iterations=$5" ]] || { echo "$f drifted: $out"; exit 1; }
done
for o in stable oink; do   # depth 4 / k 3 on fam_D4 by L-ALG's dtl_stealdepth.py (in-tree copy = l-alg e0fc1bb0), both order data
  out=$(cd ../alg && RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0 DTL_ORDER=$o python3 -I dtl_stealdepth.py ../red/lag/instances/fam_D4_n50.pg 2>&1 | grep '^max')
  [[ "$out" == "max k 3; max depth 4" ]] || { echo "fam_D4_n50 depth drifted ($o): $out"; exit 1; }
  out=$(cd ../alg && RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0 DTL_ORDER=$o python3 -I dtl_prefexits.py ../red/lag/instances/fam_D4_n50.pg 2>&1 | grep '^max exits' | grep -o '\[(3, 50,')
  [[ "$out" == "[(3, 50," ]] || { echo "fam_D4_n50 exits drifted ($o): expected max exits 3 (R39 §7)"; exit 1; }
done
for row in "ctxp/instances/deep1_n13.pg fa65aa1c971b 13 4 1 4" "tcpert/instances/tcL_N4.pg 37146b39a5f9 68 10 2 6" "tcpert/instances/tcL_N6.pg 93e22887e13f 138 16 2 8" "tcpert/instances/tcR4_N5.pg 665e657a7306 100 27 2 15" "tcpert/instances/leanT_N8.pg 5b5ab3eee9e5 64 44 2 10" "tcpert/instances/prod/nest4_n80.pg 31c02e548d82 80 35 1 14"; do   # box 11 R40, box 12 R41
  set -- $row
  [[ "$(sha1sum "$1" | cut -c1-12)" == "$2" ]] || { echo "$1 sha1 changed"; exit 1; }
  out=$(python3 -I dtl/dtl_flipflop.py "$1" --quiet 2>&1 | sed -n 1p)
  [[ "$out" == "n=$3 tangles=$4 dominions=$5 iterations=$6" ]] || { echo "$1 drifted: $out"; exit 1; }
done
for o in stable oink; do   # R40: depth-1 birth on deep1_n13; tcL(6) phase-0 contexts 2 (in-tree experiments/alg = l-alg 11d89e20 copies)
  out=$(LALG_DIR="$(cd ../.. && pwd)" DTL_ORDER=$o python3 -I ctxp/depthscan.py ctxp/instances/deep1_n13.pg -q)
  [[ "$out" == *"tangles-born-at-depth>=1 1 deep-bv-res1 1 FIRST-BV-1 0"* ]] || { echo "deep1_n13 depth-1 birth drifted ($o): $out"; exit 1; }
  out=$(LALG_DIR="$(cd ../.. && pwd)" DTL_ORDER=$o python3 -I ctxp/ctxfit.py tcpert/instances/tcL_N6.pg | grep '^phase 0')
  [[ "$out" == "phase 0: S 5 |G'| 138 contexts 2: 0/138/C0/bv-thr 0/138/C0/bv-thr 0/124/C1/bv-thr 0/138/C0/bv-thr" ]] || { echo "tcL_N6 contexts drifted ($o): $out"; exit 1; }
  out=$(LALG_DIR="$(cd ../.. && pwd)" DTL_ORDER=$o python3 -I ctxp/ctxfit.py tcpert/instances/tcR4_N5.pg | tail -1)   # R40 §8: e* at depth 1
  [[ "$out" == "SUMMARY transitions 12 max-contexts 7 e*-at-depth>=1 3" ]] || { echo "tcR4_N5 depth-1 first differences drifted ($o): $out"; exit 1; }
  out=$(LALG_DIR="$(cd ../.. && pwd)" DTL_ORDER=$o python3 -I ctxp/ctxfit.py tcpert/instances/leanT_N8.pg | tail -1)   # R40 §9: a new context per transition
  [[ "$out" == "SUMMARY transitions 7 max-contexts 7 e*-at-depth>=1 0" ]] || { echo "leanT_N8 contexts drifted ($o): $out"; exit 1; }
  out=$(cd ../alg && DTL_ORDER=$o python3 -I fixd_fdpos.py ../red/tcpert/instances/prod/nest4_n80.pg | grep -o "positions \[[^]]*\]" | head -1)   # R41: tail re-rise
  [[ "$out" == "positions [6, 6, 15, 15, 14, 9, 0, 3, 6, 9, 6, 3, 0]" ]] || { echo "nest4_n80 positions drifted ($o): $out"; exit 1; }
done
if [[ -x ../../tools/oink/build/tc ]]; then   # R40: tcL generator reproduces the pinned files
  for N in 4 6; do python3 -I tcpert/tcpert.py tcL $N "$t/tcl.pg" && cmp -s "$t/tcl.pg" tcpert/instances/tcL_N$N.pg || { echo "tcpert.py tcL $N no longer generates tcL_N$N.pg"; exit 1; }; done
  python3 -I tcpert/tcpert.py tcR4 5 "$t/tcr.pg" && cmp -s "$t/tcr.pg" tcpert/instances/tcR4_N5.pg || { echo "tcpert.py tcR4 5 no longer generates tcR4_N5.pg"; exit 1; }
  python3 -I tcpert/lean.py 8 "$t/lean.pg" leanT > /dev/null && cmp -s "$t/lean.pg" tcpert/instances/leanT_N8.pg || { echo "lean.py 8 leanT no longer generates leanT_N8.pg"; exit 1; }
else echo "tcL generator check skipped (no tc build)"; fi
if [[ -x ../../tools/oink/build/oink ]] && command -v g++ > /dev/null; then
  meet/oinkmeet.sh carry/instances/meet_viol_n17.pg | grep -q "^MEET FAILS at search 0" || { echo "meet_viol_n17: pinned Oink no longer shows the (MEET) failure (R30)"; exit 1; }
else echo "meet_viol_n17 pinned-Oink check skipped (no oink build or no g++)"; fi
# R42 (box 14): (XCTX@p0) kill on 𝒞^1P and the near miss; L-ALG's b12_core (in-tree copy, unmodified) in both orders.
[[ "$(sha1sum xctx/instances/xctx_viol_n20.pg | cut -c1-12)" == "742ba103cdb7" ]] || { echo "xctx_viol_n20 sha1 changed"; exit 1; }
[[ "$(sha1sum xctx/instances/xcov11_n20.pg | cut -c1-12)" == "47023109c198" ]] || { echo "xcov11_n20 sha1 changed"; exit 1; }
for o in stable oink; do
  out=$(cd ../alg && DTL_ORDER=$o MODE=core CLASS=1 DIST=1 python3 -I b12_core.py ../red/xctx/instances/xctx_viol_n20.pg | grep -o "CORE-ALL violations [0-9]*")
  [[ "$out" == "CORE-ALL violations 1" ]] || { echo "xctx_viol_n20: b12_core CORE-ALL drifted ($o): $out"; exit 1; }
  out=$(cd ../alg && DTL_ORDER=$o MODE=xcover CLASS=1 DIST=1 python3 -I b12_core.py ../red/xctx/instances/xcov11_n20.pg | grep -o "cross-context [0-9]*")
  [[ "$out" == "cross-context 1" ]] || { echo "xcov11_n20: b12_core xcover drifted ($o): $out"; exit 1; }
  out=$(cd xctx && DTL_ORDER=$o python3 -I xscore.py instances/xctx_viol_n20.pg | grep -o "score ([0-9]*")
  [[ "$out" == "score (1" ]] || { echo "xctx_viol_n20: (XCTX@p0) violation not reproduced ($o): $out"; exit 1; }
done
# R42 §5 (box 14): (VR-NEW_all) kill on 𝒞^1P; b12_pot (in-tree, unmodified) K-v-all = 1 in both orders.
[[ "$(sha1sum xctx/instances/vrall_viol_n20.pg | cut -c1-12)" == "ed5058576554" ]] || { echo "vrall_viol_n20 sha1 changed"; exit 1; }
for o in stable oink; do
  out=$(cd ../alg && DTL_ORDER=$o CLASS=1 DIST=1 python3 -I b12_pot.py ../red/xctx/instances/vrall_viol_n20.pg | grep "K-v-all" | awk '{print $3}')
  [[ "$out" == "1" ]] || { echo "vrall_viol_n20: b12_pot K-v-all violations drifted ($o): $out"; exit 1; }
done
# R43 (box 14): (TREE-PIECE⁺) kill, two-player; L-ALG's b12_ident.tp_score PLUS=1 (in-tree copy, unmodified), both orders.
[[ "$(sha1sum tpp/instances/tpp_viol_n22.pg | cut -c1-12)" == "a5088b091cbd" ]] || { echo "tpp_viol_n22 sha1 changed"; exit 1; }
[[ "$(sha1sum tpp/instances/tpp_viol_n63.pg | cut -c1-12)" == "64d0832859a4" ]] || { echo "tpp_viol_n63 sha1 changed"; exit 1; }
for o in stable oink; do
  out=$(cd ../alg && PLUS=1 python3 -I -c "import sys; sys.setrecursionlimit(100000); sys.path.insert(0, '.'); sys.path.insert(0, '../harness'); import pg, b12_ident as I; print(I.tp_score(pg.read('../red/tpp/instances/tpp_viol_n22.pg'), '$o'))")
  [[ "$out" == "(1, 0, 3, 5)" ]] || { echo "tpp_viol_n22: tp_score PLUS=1 drifted ($o): $out"; exit 1; }
done
# R44 (box 14): (NO-PRE-a) kill; L-ALG's b12_nopre.py scan (in-tree, unmodified) reports pre = 1 in both orders.
[[ "$(sha1sum nopre/instances/nopre_viol_n20.pg | cut -c1-12)" == "9a93a8e24832" ]] || { echo "nopre_viol_n20 sha1 changed"; exit 1; }
for o in stable oink; do
  out=$(cd ../alg && DTL_ORDER=$o python3 -I b12_nopre.py scan ../red/nopre/instances/nopre_viol_n20.pg | tail -1 | grep -o "\[[0-9]*,")
  [[ "$out" == "[1," ]] || { echo "nopre_viol_n20: (NO-PRE-a) precondition count drifted ($o): $out"; exit 1; }
done
# R45 (box 14): NEST 3 inside 𝒞^1P (nestclass.py on L-ALG's chain), both orders.
[[ "$(sha1sum xctx/instances/nest3_n20.pg | cut -c1-12)" == "4ac8e1f4955b" ]] || { echo "nest3_n20 sha1 changed"; exit 1; }
[[ "$(sha1sum xctx/instances/nest3_n24.pg | cut -c1-12)" == "6b039158a2d1" ]] || { echo "nest3_n24 sha1 changed"; exit 1; }
for o in stable oink; do
  out=$(cd xctx && DTL_ORDER=$o python3 -I nestclass.py instances/nest3_n20.pg | grep -o "score ([0-9]*, [0-9]*, [0-9]*")
  [[ "$out" == "score (3, 1, 11" ]] || { echo "nest3_n20: NEST drifted ($o): $out"; exit 1; }
  out=$(cd xctx && DTL_ORDER=$o python3 -I nestclass.py instances/nest3_n24.pg | grep -o "score ([0-9]*, [0-9]*, [0-9]*")
  [[ "$out" == "score (3, 3, 18" ]] || { echo "nest3_n24: NEST drifted ($o): $out"; exit 1; }
done
# R87 (successor 21): exact N3-LEVEL checker; pp_K12 hyp flips pinned, strict control must fail on the coverage pin
out=$(python3 -I n3/n3x.py --one usplit/instances/pp_K12_n161.pg | head -1)
[[ "$out" == *"hyp=60 "* ]] || { echo "n3x pp_K12 drifted: $out"; exit 1; }
python3 -I n3/n3x.py --one n3/instances/n3cov_lean.pg n3/instances/n3cov_lean_fixed.start | grep -q "N3X PASS" || { echo "n3x n3cov_lean: not PASS"; exit 1; }
MUT=1 python3 -I n3/n3x.py --one n3/instances/n3cov_lean.pg n3/instances/n3cov_lean_fixed.start | grep -q "N3X FAIL" || { echo "n3x strict control did not fail"; exit 1; }
# R91 (successor 22): UL_C reader kill pinned (sha1, U event index L = 10 > |U| - 1 = 7); lib-free control: L = 6 gives no violation
[[ "$(sha1sum ul/instances/reader_L10_n36.pg | cut -c1-12)" == "316443126793" ]] || { echo "reader_L10 sha1 changed"; exit 1; }
out=$(python3 -I ul/ulx.py --one ul/instances/reader_L10_n36.pg ul/instances/reader_L10_n36.start | head -1)
[[ "$out" == *" UL_C_VIOL=1 "* ]] || { echo "ulx reader_L10 drifted: $out"; exit 1; }
python3 -I ul/mkreader.py 6 "$t/rd6.pg" > /dev/null && out=$(python3 -I ul/ulx.py --one "$t/rd6.pg" "$t/rd6.start" | head -1)
[[ "$out" != *"UL_C_VIOL"* ]] || { echo "ulx control L=6 fired: $out"; exit 1; }
# R92 (successor 22): ladder ENT k = 12 pinned: one phase, QP 14, QP_c 12 in one class, ENT 11 (L-NEW's qp.py columns)
[[ "$(sha1sum ul/instances/ladderent_k12_n48.pg | cut -c1-12)" == "56986308e2ae" ]] || { echo "ladderent_k12 sha1 changed"; exit 1; }
out=$(python3 -I ../new/box48/qp.py 1 7 ul/instances/ladderent_k12_n48.pg --start ul/instances/ladderent_k12_n48.start | grep -A1 "^longest" | tail -1)
[[ "$out" == "   14 48 14 3 11 12 12 14 12 12 2 "* ]] || { echo "ladderent_k12 qp drifted: $out"; exit 1; }
# R93 (successor 22): C-ONCE_X kill pinned (x X-migrates 4 times in one pure C-interval)
[[ "$(sha1sum ul/instances/cxmig_k4_n54.pg | cut -c1-12)" == "a3893ea4fd89" ]] || { echo "cxmig_k4 sha1 changed"; exit 1; }
out=$(python3 -I ul/ulx.py --one ul/instances/cxmig_k4_n54.pg ul/instances/cxmig_k4_n54.start | grep "^MAX XMIG_PER_VERTEX")
[[ "$out" == "MAX XMIG_PER_VERTEX 4 "* ]] || { echo "cxmig_k4 drifted: $out"; exit 1; }
# R100 (successor 24): FB-LIN tools. Level-1 template = one detachment wave (f = m); library maxima reproduced by fbphase.py
out=$(python3 -I fb/lvl1.py 8); [[ "$out" == "m 8 n 15 f, phase, it = (8, 0, 10)" ]] || { echo "lvl1 drifted: $out"; exit 1; }
out=$(python3 -I fb/fbphase.py so/instances/rise_fb38_n48.pg S3 so/instances/farrise25_n32.pg S3 | tr '\n' ' ')
[[ "$out" == *"maxf=37 "*"maxf=25 "* ]] || { echo "fbphase drifted: $out"; exit 1; }
[[ "$(sha1sum fb/instances/fb38_n48.pg | cut -c1-12)" == "bc5858a24505" ]] || { echo "fb38_n48 sha1 changed"; exit 1; }
out=$(python3 -I fb/fbphase.py fb/instances/fb38_n48.pg fb/instances/fb38_n48.start); [[ "$out" == *"maxf=38 "* ]] || { echo "fb38_n48 drifted: $out"; exit 1; }
# R105 (successor 25): SEG-COUNT kill (designed gadget + family); generators reproduce the pins, segchk.py gives EXC 1 / 2
python3 -I seg/mk2d.py "$t/s20.pg" "$t/s20.start" > /dev/null; cmp -s "$t/s20.pg" seg/instances/segcount_kill_n20.pg && cmp -s "$t/s20.start" seg/instances/segcount_kill_n20.start || { echo "mk2d drifted from segcount_kill_n20"; exit 1; }
python3 -I seg/mkk.py 3 "$t/k3.pg" "$t/k3.start" > /dev/null; cmp -s "$t/k3.pg" seg/instances/segfam_k3_n29.pg || { echo "mkk 3 drifted from segfam_k3_n29"; exit 1; }
[[ "$(sha1sum seg/instances/segcount_kill_n20.pg | cut -c1-12)" == "2783f64d82f2" ]] || { echo "segcount_kill_n20 sha1 changed"; exit 1; }
out=$(python3 -I seg/segchk.py seg/instances/segcount_kill_n20.pg seg/instances/segcount_kill_n20.start | tail -1); [[ "$out" == *"maxEXC 1 max deadlocks/segment 2" ]] || { echo "segcount_kill_n20 drifted: $out"; exit 1; }
out=$(python3 -I seg/segchk.py seg/instances/segfam_k3_n29.pg seg/instances/segfam_k3_n29.start | tail -1); [[ "$out" == *"maxEXC 2 max deadlocks/segment 3" ]] || { echo "segfam_k3_n29 drifted: $out"; exit 1; }
# R106 (successor 25): quadratic fallback-free run = one REL segment (mkr.py); generator reproduces the pins; K 3 m 4: L 20 at n 54
python3 -I seg/mkr.py 3 4 "$t/q.pg" "$t/q.start" > /dev/null; cmp -s "$t/q.pg" seg/instances/runquad_K3_m4_n54.pg && cmp -s "$t/q.start" seg/instances/runquad_K3_m4_n54.start || { echo "mkr drifted from runquad_K3_m4_n54"; exit 1; }
python3 -I seg/mkr.py 8 30 "$t/q8.pg" "$t/q8.start" > /dev/null; cmp -s "$t/q8.pg" seg/instances/runquad_K8_m30_n192.pg || { echo "mkr drifted from runquad_K8_m30_n192"; exit 1; }
out=$(python3 -I seg/segchk.py seg/instances/runquad_K3_m4_n54.pg seg/instances/runquad_K3_m4_n54.start | head -1); [[ "$out" == "seg [0, 20] L 20 switchers 11 EXC 9 "*"FAILS" ]] || { echo "runquad_K3_m4_n54 drifted: $out"; exit 1; }
# R107 (successor 26): s3embed of runquad_K3_m4_n54 reproduces the pin; N5 from the S3 DEFAULT start (no start file) makes 21 iterations
python3 -I seg/s3embed.py seg/instances/runquad_K3_m4_n54.pg seg/instances/runquad_K3_m4_n54.start "$t/e.pg" "$t/e.start" > /dev/null; cmp -s "$t/e.pg" seg/instances/s3quad_K3_m4.pg || { echo "s3embed drifted from s3quad_K3_m4"; exit 1; }
out=$(python3 -I ../n5-second/n5b.py seg/instances/s3quad_K3_m4.pg "$t/e.sol" --mode spec); [[ "$out" == "n5b iterations 21 fallbacks 0 "* ]] || { echo "s3quad_K3_m4 drifted: $out"; exit 1; }
# R109 (successor 26): H_n with the top gate's exit removed; hnh1.py reproduces the pin; N5 from iota (+ S3 tau) makes 3n^2+13n-5 = 61 at n 3
python3 -I seg/hnh1.py 3 topfix "$t/h3.pg" "$t/h3.start" > /dev/null; cmp -s "$t/h3.pg" seg/instances/hntop_n3.pg && cmp -s "$t/h3.start" seg/instances/hntop_n3.start || { echo "hnh1 drifted from hntop_n3"; exit 1; }
out=$(python3 -I ../n5-second/n5b.py seg/instances/hntop_n3.pg "$t/h3.sol" --mode spec --start seg/instances/hntop_n3.start); [[ "$out" == "n5b iterations 61 fallbacks 0 "* ]] || { echo "hntop_n3 drifted: $out"; exit 1; }
# R111 (successor 26): dualize.py reproduces the dual pin; N5 from S3 on G^d of s3quad_K3_m4 makes 21 iterations (mirror of R107)
printf 'SIGMA0\nTAU0\n' > "$t/emp.start"; python3 -I ctl/dualize.py seg/instances/s3quad_K3_m4.pg "$t/emp.start" "$t/d.pg" "$t/d.start"; cmp -s "$t/d.pg" ctl/instances/d_s3quad_K3_m4.pg || { echo "dualize drifted"; exit 1; }
out=$(python3 -I ../n5-second/n5b.py ctl/instances/d_s3quad_K3_m4.pg "$t/d.sol" --mode spec); [[ "$out" == "n5b iterations 21 fallbacks 0 "* ]] || { echo "d_s3quad_K3_m4 drifted: $out"; exit 1; }
# R112 (successor 27): chain.py reproduces relay_L3; one joint lambda-run, 13 iterations, 6 sigma- and 7 tau-changes
python3 -I cpl/chain.py 3 "$t/r3.pg" "$t/r3.start" > /dev/null; cmp -s "$t/r3.pg" cpl/instances/relay_L3.pg && cmp -s "$t/r3.start" cpl/instances/relay_L3.start || { echo "chain.py drifted from relay_L3"; exit 1; }
out=$(python3 -I cpl/cpl.py cpl/instances/relay_L3.pg cpl/instances/relay_L3.start); [[ "$out" == "n 28 it 13 fb 0 sigma-changes 6 tau-changes 7 joint-lambda-runs 1 "* ]] || { echo "relay_L3 drifted: $out"; exit 1; }
# R113 (successor 27): ewin.py + dualize.py give the Odd clock dewin_runquad_K3_m4 (21 iterations, all tau-changes)
python3 -I cpl/ewin.py seg/instances/runquad_K3_m4_n54.pg "$t/e.pg" > /dev/null; cmp -s "$t/e.pg" cpl/instances/ewin_runquad_K3_m4.pg || { echo "ewin drifted"; exit 1; }
out=$(python3 -I cpl/cpl.py cpl/instances/dewin_runquad_K3_m4.pg cpl/instances/dewin_runquad_K3_m4.start); [[ "$out" == "n 54 it 21 fb 0 sigma-changes 0 tau-changes 21 "* ]] || { echo "dewin drifted: $out"; exit 1; }
# R114 (successor 28): N5-SF second engine sf2.py (L-COMP PGSolver-port valuations) = n5sf.py counts; snare-rule family ports
python3 -I sf/sbev.py --selftest > /dev/null || { echo "sbev selftest failed"; exit 1; }
python3 -I ../hard-families/pgsolver_port.py switchbestexp 2 > "$t/sb2.pg"; out=$(python3 -I sf/sf2.py "$t/sb2.pg"); [[ "$out" == "sf2 mode spec n 60 iterations 58 fallbacks 0 sigma_changes 58 SBC_sigma 4 "* ]] || { echo "sf2 switchbestexp 2 drifted: $out"; exit 1; }
python3 -I sf/fsubexp.py 3 > "$t/fs3.pg"; [[ "$(sha1sum "$t/fs3.pg" | cut -c1-12)" == "907738682bdb" ]] || { echo "fsubexp 3 sha1 changed"; exit 1; }
out=$(python3 -I sf/sf2.py "$t/fs3.pg"); [[ "$out" == "sf2 mode spec n 77 iterations 11 "* ]] || { echo "sf2 fsubexp 3 drifted: $out"; exit 1; }
python3 -I sf/fsubexp.py fearnley 3 > "$t/fe3.pg"; out=$(python3 -I sf/sf2.py "$t/fe3.pg"); [[ "$out" == "sf2 mode spec n 59 iterations 9 "* ]] || { echo "sf2 fearnleysubexp 3 drifted: $out"; exit 1; }
# R115 (successor 28): fcN = switchbestexp minus f_i -> c; N5-SF SBC_sigma = N^2 (N = 3: 121 iterations, SBC 9)
python3 -I sf/sbev.py 3 --drop fc > "$t/fc3.pg"; [[ "$(sha1sum "$t/fc3.pg" | cut -c1-12)" == "9af7ca12ace1" ]] || { echo "fc3 sha1 changed"; exit 1; }
out=$(python3 -I sf/sf2.py "$t/fc3.pg"); [[ "$out" == "sf2 mode spec n 85 iterations 121 fallbacks 0 sigma_changes 121 SBC_sigma 9 "* ]] || { echo "fc3 drifted: $out"; exit 1; }
# R116 (successor 29): dwN = fcN + one repeater per escape-chain edge; N5-SF iterations 19*2^N - 18, SBC_sigma 2^(N+1) - N - 2 (N = 3: 134 / 11)
python3 -I sf/dlchain.py 3 1 > "$t/dw3.pg"; cmp -s "$t/dw3.pg" sf/instances/dw_3.pg && [[ "$(sha1sum "$t/dw3.pg" | cut -c1-12)" == "e5f94c800324" ]] || { echo "dlchain drifted from dw_3"; exit 1; }
out=$(python3 -I sf/sf2.py sf/instances/dw_3.pg); [[ "$out" == "sf2 mode spec n 87 iterations 134 fallbacks 0 sigma_changes 134 SBC_sigma 11 "* ]] || { echo "dw_3 drifted: $out"; exit 1; }
out=$(python3 -I sf/sf2.py sf/instances/dw_4.pg); [[ "$out" == "sf2 mode spec n 113 iterations 286 fallbacks 0 sigma_changes 286 SBC_sigma 26 "* ]] || { echo "dw_4 drifted: $out"; exit 1; }
# R118 (successor 29): FRAME-STRETCH kill pins regenerate from mkr.py; tstretch.py on the small gate instance (tau constant, 21 sigma-changes)
python3 -I seg/mkr.py 20 80 "$t/mk.pg" "$t/mk.start" > /dev/null; cmp -s "$t/mk.pg" seg/instances/mk_20_80.pg && cmp -s "$t/mk.start" seg/instances/mk_20_80.start || { echo "mkr drifted from mk_20_80"; exit 1; }
out=$(python3 -I sf/tstretch.py seg/instances/runquad_K3_m4_n54.pg seg/instances/runquad_K3_m4_n54.start); [[ "$out" == "n 54 m 83 n+m 137 iterations 21 fb 0 tau-changes 0 max-tau-stretch 21 "* ]] || { echo "tstretch drifted: $out"; exit 1; }
# R119 (successor 30): Lemma MG per-state check on dw_3 (0 violations; control fires); mixed-frame two-level gate sampler on CDAG_3
out=$(python3 -I mix/mgcheck.py sf/instances/dw_3.pg); [[ "$out" == *"states 42 hits 1145 violations 0 locks 288 "*"control(only (i) fails, claim false) 2383" ]] || { echo "mgcheck dw_3 drifted: $out"; exit 1; }
out=$(TMPDIR="$t" python3 -I mix/mixgate.py 3 300 1 | sed -n 2p); [[ "$out" == "best stretch 2 iterations 2 fb 0" ]] || { echo "mixgate drifted: $out"; exit 1; }
# R120 (successor 30): RESET-LIN kill. mkr + wave observer (obs2.py): observer #MAT = K(m - 1) in one lambda-run (K = 4, m = 16: 60 at n 119); pin regenerates
python3 -I seg/mkr.py 8 32 "$t/mk8.pg" "$t/mk8.start" > /dev/null; python3 -I mix/obs2.py "$t/mk8.pg" "$t/mk8.start" "$t/w8.pg" "$t/w8.start" > /dev/null; cmp -s "$t/w8.pg" mix/instances/wobs_K8_m32.pg && cmp -s "$t/w8.start" mix/instances/wobs_K8_m32.start || { echo "obs2 drifted from wobs_K8_m32"; exit 1; }
python3 -I seg/mkr.py 4 16 "$t/mk4.pg" "$t/mk4.start" > /dev/null; python3 -I mix/obs2.py "$t/mk4.pg" "$t/mk4.start" "$t/w4.pg" "$t/w4.start" > /dev/null
out=$(python3 -I mix/matc.py "$t/w4.pg" "$t/w4.start" | tail -1); [[ "$out" == "  max #MAT 60  max #MAT / n 0.504" ]] || { echo "matc w4 drifted: $out"; exit 1; }
# R121 (successor 30): RESET-LIN-T kill. TARGET=1 adds Even e -> {o, d} (one switch to o); o counted as a switch target: #MAT 60 at K 4; pin tobs_K8_m32
TARGET=1 python3 -I mix/obs2.py "$t/mk8.pg" "$t/mk8.start" "$t/tg8.pg" "$t/tg8.start" > /dev/null; cmp -s "$t/tg8.pg" mix/instances/tobs_K8_m32.pg && cmp -s "$t/tg8.start" mix/instances/tobs_K8_m32.start || { echo "obs2 TARGET drifted from tobs_K8_m32"; exit 1; }
TARGET=1 python3 -I mix/obs2.py "$t/mk4.pg" "$t/mk4.start" "$t/tg4.pg" "$t/tg4.start" > /dev/null; out=$(TARGETS=1 python3 -I mix/matc.py "$t/tg4.pg" "$t/tg4.start" | tail -1); [[ "$out" == "  max #MAT 60  max #MAT / n 0.496" ]] || { echo "matc targets tg4 drifted: $out"; exit 1; }
# R122 (successor 30): FG(tau) on the wrapped switchallexp 3 with the climbed edge ranking: 119 iterations, 28 stalls (switch-all 70); wrapped-S3 start 64 / 14
out=$(python3 -I mix/fgt.py mix/instances/switchallexp_3.pg file:mix/instances/fg_sa3_best.order); [[ "$out" == *"FG iterations 119 stalls 28 switch-all 70" ]] || { echo "fgt drifted: $out"; exit 1; }
START=wbest OUT="$t/wr3.pg" python3 -I mix/fgt.py mix/instances/switchallexp_3.pg file:mix/instances/fg_sa3_best.order > /dev/null; cmp -s "$t/wr3.pg" mix/instances/fg_wrapped_sa3.pg || { echo "wrapped game drifted"; exit 1; }
# R123 (successor 31): RESET-LIN-S kill. spanobs.py adds Even e -> {o, d -> h'} (tau(o) = yh -> h): e leaves and re-enters o once per
# pivot cycle, so span(e, o) holds the observer's MATCHED P-changes, (K - 2)(m - 1) + K; K = 4: 34 at n 122; pin spanobs_K12_m48 (482 > n 346)
python3 -I span/spanobs.py "$t/w4.pg" "$t/w4.start" "$t/so4.pg" "$t/so4.start" > /dev/null
out=$(python3 -I span/spanc.py "$t/so4.pg" "$t/so4.start" | sed -n 2p); [[ "$out" == "  pair (119, 102) span [18, 58]: MAT 34 PCH 39" ]] || { echo "spanc so4 drifted: $out"; exit 1; }
python3 -I seg/mkr.py 12 48 "$t/mk12.pg" "$t/mk12.start" > /dev/null; python3 -I mix/obs2.py "$t/mk12.pg" "$t/mk12.start" "$t/w12.pg" "$t/w12.start" > /dev/null
python3 -I span/spanobs.py "$t/w12.pg" "$t/w12.start" "$t/so12.pg" "$t/so12.start" > /dev/null; cmp -s "$t/so12.pg" span/instances/spanobs_K12_m48.pg && cmp -s "$t/so12.start" span/instances/spanobs_K12_m48.start || { echo "spanobs drifted from spanobs_K12_m48"; exit 1; }
# R123 §4: CARRY-SEG-S kill. carryobs.py: Even observer (OWNER=0 ABOVE=a) + beta_j markers on the b-links + e -> {o, d -> yd -> h'}:
# every P-change of o in span(e, o) but one is a carry; SEG = (K - 1)(m + 1) + 2; K = 4: 53 at n 122; pin carryobs_K12_m48 (541 > n - 1 = 345)
OWNER=0 ABOVE=a python3 -I mix/obs2.py "$t/mk4.pg" "$t/mk4.start" "$t/oe4.pg" "$t/oe4.start" > /dev/null; python3 -I span/carryobs.py "$t/oe4.pg" "$t/oe4.start" "$t/co4.pg" "$t/co4.start" > /dev/null
out=$(python3 -I span/spanc.py "$t/co4.pg" "$t/co4.start" | sed -n 6p); [[ "$out" == "  max SEG^span 53 at pair (119, 102) span [0, 60] (MAT 1 PCH 54); CARRY-SEG-S PASS" ]] || { echo "spanc co4 drifted: $out"; exit 1; }
OWNER=0 ABOVE=a python3 -I mix/obs2.py "$t/mk12.pg" "$t/mk12.start" "$t/oe12.pg" "$t/oe12.start" > /dev/null; python3 -I span/carryobs.py "$t/oe12.pg" "$t/oe12.start" "$t/co12.pg" "$t/co12.start" > /dev/null
cmp -s "$t/co12.pg" span/instances/carryobs_K12_m48.pg && cmp -s "$t/co12.start" span/instances/carryobs_K12_m48.start || { echo "carryobs drifted from carryobs_K12_m48"; exit 1; }
# R124 (successor 31): bidirectional chain (span/mkrb.py): iterations 2K(m + 1); K 3, m 4: 30; pin bidir_K8_m32 regenerates
python3 -I span/mkrb.py 3 4 "$t/b3.pg" "$t/b3.start" > /dev/null; out=$(python3 -I ../n5-second/n5b.py "$t/b3.pg" "$t/b3.sol" --start "$t/b3.start" --mode spec); [[ "$out" == "n5b iterations 30 fallbacks 0 "* ]] || { echo "mkrb K3 drifted: $out"; exit 1; }
python3 -I span/mkrb.py 8 32 "$t/b8.pg" "$t/b8.start" > /dev/null; cmp -s "$t/b8.pg" span/instances/bidir_K8_m32.pg && cmp -s "$t/b8.start" span/instances/bidir_K8_m32.start || { echo "mkrb drifted from bidir_K8_m32"; exit 1; }
# R127 (successor 31): mkr in one W-world (span/mkrw.py) + late adopters: R* = K*m in one W-run; K 4: R* 64 (latec.py on n5b); pin latew_K8_m32
LATE=1 python3 -I span/mkrw.py 4 16 "$t/lw4.pg" "$t/lw4.start" > /dev/null; out=$(python3 -I span/latec.py "$t/lw4.pg" "$t/lw4.start"); [[ "$out" == "LATEC lw4.pg n 186 iter 76 cuts 0 fallbacks 0 R* 64 late 65 max-per-edge-Wrun 4" ]] || { echo "latec lw4 drifted: $out"; exit 1; }
LATE=1 python3 -I span/mkrw.py 8 32 "$t/lw8.pg" "$t/lw8.start" > /dev/null; cmp -s "$t/lw8.pg" span/instances/latew_K8_m32.pg && cmp -s "$t/lw8.start" span/instances/latew_K8_m32.start || { echo "mkrw drifted from latew_K8_m32"; exit 1; }
# R130 (successor 31): chained late adopters (span/mkrw.py LATE=2): box-48 window depth (m - 1)/2; K 4 m 16: depth 7, REP 21; pin wdepth_K4_m64
LATE=2 python3 -I span/mkrw.py 4 16 "$t/ch16.pg" "$t/ch16.start" > /dev/null; out=$(DEPTH=1 REP=1 python3 -I span/latec.py "$t/ch16.pg" "$t/ch16.start" | tr '\n' ' '); [[ "$out" == "DEPTH max window depth 7 LATEC ch16.pg n 146 iter 76 cuts 0 fallbacks 0 R* 36 late 37 max-per-edge-Wrun 4 REP 21 " ]] || { echo "latec depth ch16 drifted: $out"; exit 1; }
LATE=2 python3 -I span/mkrw.py 4 64 "$t/ch64.pg" "$t/ch64.start" > /dev/null; cmp -s "$t/ch64.pg" span/instances/wdepth_K4_m64.pg && cmp -s "$t/ch64.start" span/instances/wdepth_K4_m64.start || { echo "mkrw LATE=2 drifted from wdepth_K4_m64"; exit 1; }
# R131 (successor 32): CONJECTURE TIED-RB (L-SI box 50 §6) DEAD. tree/mktied.py = mkrw LATE=1 + y_J -> {v_J, z_J}, z_J (Even) -> {a_(J+1), c_(J+1)}:
# untied re-blocked REPEATs (K - 1)(m - 2) in one W-run; K 4 m 8: 18 (tree/tiedc.py on n5b); pin tiedrb_K8_m16 (98 at n 270) regenerates
python3 -I tree/mktied.py 4 8 "$t/td48.pg" "$t/td48.start" > /dev/null; out=$(python3 -I tree/tiedc.py "$t/td48.pg" "$t/td48.start" | head -1); [[ "$out" == "TIEDC td48.pg n 134 iter 45 fallbacks 0 runs 1 rep 36 tied 18 untied 18 reblk 36 untied_reblk 18" ]] || { echo "tiedc td48 drifted: $out"; exit 1; }
python3 -I tree/mktied.py 8 16 "$t/td816.pg" "$t/td816.start" > /dev/null; cmp -s "$t/td816.pg" tree/instances/tiedrb_K8_m16.pg && cmp -s "$t/td816.start" tree/instances/tiedrb_K8_m16.start || { echo "mktied drifted from tiedrb_K8_m16"; exit 1; }
# R132 (successor 32): device tree (tree/scratch/mkrt.py TREE=3) REP = (K - 1)(2^D - 1) = 21; Lemma DAG-tau* check (200 random DAG games)
TREE=3 python3 -I tree/scratch/mkrt.py 4 16 "$t/mt3.pg" "$t/mt3.start" > /dev/null; out=$(python3 -I tree/tiedlib.py "$t/mt3.pg" "$t/mt3.start"); [[ "$out" == "TIEDLIB mt3.pg n 146 it 76 runs 1 rep 21 tied 21 untied 0 reblk 21 untied_reblk 0" ]] || { echo "mkrt TREE=3 drifted: $out"; exit 1; }
out=$(python3 -I tree/scratch/dagtest.py 1 200); [[ "$out" == "done 200 max(it - height) 0" ]] || { echo "dagtest drifted: $out"; exit 1; }
# R133 (successor 32): VARIANT N5-LZC (L-NEW box 72), engine B lzc/n5lzb.py on n5b: laziness costs 3 iterations on lazyhurt_n9 (N5 3/0, N5-LZC 6/2)
out=$(python3 -I lzc/n5lzb.py lzc/instances/lazyhurt_n9.pg "$t/lh.sol" --start lzc/instances/lazyhurt_n9.start --plain); [[ "$out" == "n5lzb(plain) iterations 3 fallbacks 0" ]] || { echo "n5lzb plain drifted: $out"; exit 1; }
out=$(python3 -I lzc/n5lzb.py lzc/instances/lazyhurt_n9.pg "$t/lh.sol" --start lzc/instances/lazyhurt_n9.start); [[ "$out" == "n5lzb iterations 6 fallbacks 2" ]] || { echo "n5lzb lazy drifted: $out"; exit 1; }
# R134 (successor 32): ZXC per W-run (zxc/zxc.py): R120's Even wave observer on one-world mkr (span/mkrw.py 4 16 + mix/obs2.py OWNER=0 ABOVE=a): ZXC(obs) = Km + K + 1 = 69 of |F| = 76
python3 -I span/mkrw.py 4 16 "$t/zw.pg" "$t/zw.start" > /dev/null; OWNER=0 ABOVE=a python3 -I mix/obs2.py "$t/zw.pg" "$t/zw.start" "$t/zo.pg" "$t/zo.start" > /dev/null
out=$(python3 -I zxc/zxc.py "$t/zo.pg" "$t/zo.start" | cut -d' ' -f1-13); [[ "$out" == "ZXC zo.pg n 128 iter 76 fallbacks 0 longest-W-run 76 top obs:69/76E(TXC 0)" ]] || { echo "zxc observer drifted: $out"; exit 1; }
# R135 (successor 33): box 82's escape in real N5. dg_k (desync/mkdg.py): lateral desync gate, tau fixed, 4 iterations for every k; pins
# dg_16 / dgu_4 / dga_4 (UP=1 upward variants, Lemma WAIT-CYCLE branches); box 80 ladders: upward waits; no-upward-wait max T-rises k + 2
sha1sum -c --quiet desync/ladder.sha1 || { echo "box80 ladder copies changed"; exit 1; }
python3 -I desync/mkdg.py 16 "$t/dg16.pg" "$t/dg16.start" > /dev/null; cmp -s "$t/dg16.pg" desync/instances/dg_16.pg && cmp -s "$t/dg16.start" desync/instances/dg_16.start || { echo "mkdg drifted from dg_16"; exit 1; }
UP=1 python3 -I desync/mkdg.py 4 "$t/du.pg" "$t/du.start" > /dev/null; cmp -s "$t/du.pg" desync/instances/dgu_4.pg || { echo "mkdg UP drifted from dgu_4"; exit 1; }
UP=1 UPTO=A python3 -I desync/mkdg.py 4 "$t/da.pg" "$t/da.start" > /dev/null; cmp -s "$t/da.pg" desync/instances/dga_4.pg || { echo "mkdg UPTO=A drifted from dga_4"; exit 1; }
out=$(python3 -I desync/dgstat.py desync/instances/dg_16.pg desync/instances/dg_16.start); [[ "$out" == "DGSTAT dg_16.pg n 94 iterations 4 fallbacks 0 tau-changes 0 W-runs 1 W(T)-values 4 max-WCH-in-a-W-run 3 (B4) W-cycle-nodes ['sink'] Xi-cycle-nodes ['sink']" ]] || { echo "dgstat dg_16 drifted: $out"; exit 1; }
out=$(python3 -I desync/dgstat.py desync/instances/dga_4.pg desync/instances/dga_4.start); [[ "$out" == *"iterations 3 fallbacks 0 tau-changes 1 "*"Xi-cycle-nodes ['h3_0', 'sink']" ]] || { echo "dgstat dga_4 drifted: $out"; exit 1; }
out=$(python3 -I seg/xeng.py desync/instances/dg_16.pg desync/instances/dg_16.start | tail -1); [[ "$out" == "state sequences identical: True" ]] || { echo "xeng dg_16: $out"; exit 1; }
out=$(python3 -I desync/upwait.py desync/ladder/ladder_8.pg desync/ladder/ladder_8.seq); [[ "$out" == "UPWAIT ladder_8.pg steps 749 upward-blocked 4914 lateral-blocked 1408 vertices-with-upward-waits 14" ]] || { echo "upwait drifted: $out"; exit 1; }
out=$(python3 -I desync/noup.py desync/ladder/ladder_5.pg); [[ "$out" == "NOUP ladder_5.pg max T-rises: no-upward-waits 7, unrestricted 31" ]] || { echo "noup drifted: $out"; exit 1; }
python3 -I desync/wcrand.py 1 400 4 9 | grep -qx "WCRAND seed 1 runs 400 self-routed-blocks 360 violations 0" || { echo "wcrand drifted"; exit 1; }
OPEN0=1 python3 -I desync/mkpar.py 4 "$t/pa.pg" "$t/pa.start" > /dev/null; cmp -s "$t/pa.pg" desync/instances/par_4.pg && cmp -s "$t/pa.start" desync/instances/par_4.start || { echo "mkpar drifted from par_4"; exit 1; }
python3 -I desync/mkpar.py 4 "$t/pc.pg" "$t/pc.start" > /dev/null; cmp -s "$t/pc.start" desync/instances/parc_4.start || { echo "mkpar drifted from parc_4"; exit 1; }
# R136 (successor 33): pattern clock. pclock/patcount.py on mkrb K 4 m 8: PAT = SERVED = K = 4 (clock hp, 3 switches; PAT-SW checked online);
# shared T clock pclock/mkte.py (Lemma ALT-ESCAPE): te_8 pin, 9 iterations, 0 served waits
python3 -I span/mkrb.py 4 8 "$t/rb48.pg" "$t/rb48.start" > /dev/null; out=$(python3 -I pclock/patcount.py "$t/rb48.pg" "$t/rb48.start"); [[ "$out" == "PATCOUNT rb48.pg n 78 iterations 72 self-routed-blocks 519 served-waits 57 max-PAT 4 max-SERVED 4 at-max-PAT: busiest route vertex hp with 3 switches" ]] || { echo "patcount rb48 drifted: $out"; exit 1; }
python3 -I pclock/mkte.py 8 "$t/te8.pg" "$t/te8.start" > /dev/null; cmp -s "$t/te8.pg" pclock/instances/te_8.pg && cmp -s "$t/te8.start" pclock/instances/te_8.start || { echo "mkte drifted from te_8"; exit 1; }
out=$(python3 -I pclock/patcount.py pclock/instances/te_8.pg pclock/instances/te_8.start); [[ "$out" == "PATCOUNT te_8.pg n 82 iterations 9 self-routed-blocks 2 served-waits 0 "* ]] || { echo "patcount te_8 drifted: $out"; exit 1; }
# R137 (successor 33): FREE returns at one edge, quadratic: free/obsx.py (two interleaved R120 observers, BLK=2, + chooser X) on mkrw K m:
# returns per edge K*m/4 in one W-run (K 4 m 16: 16; pin fx_K8_m32: 64)
python3 -I span/mkrw.py 4 16 "$t/fw4.pg" "$t/fw4.start" > /dev/null; BLK=2 OWNER=0 ABOVE=a python3 -I free/obsx.py "$t/fw4.pg" "$t/fw4.start" "$t/f4.pg" "$t/f4.start" > /dev/null
out=$(python3 -I free/xret.py "$t/f4.pg" "$t/f4.start"); [[ "$out" == "XRET f4.pg n 130 iterations 76 fallbacks 0 tau-changes 0 X-switches 33 returns-per-edge [16, 16]" ]] || { echo "xret f4 drifted: $out"; exit 1; }
python3 -I span/mkrw.py 8 32 "$t/fw8.pg" "$t/fw8.start" > /dev/null; BLK=2 OWNER=0 ABOVE=a python3 -I free/obsx.py "$t/fw8.pg" "$t/fw8.start" "$t/f8.pg" "$t/f8.start" > /dev/null
cmp -s "$t/f8.pg" free/instances/fx_K8_m32.pg && cmp -s "$t/f8.start" free/instances/fx_K8_m32.start || { echo "obsx drifted from fx_K8_m32"; exit 1; }
# R138 (successor 33): R*_F = K*m in one W-run on mkrw LATE=1 (L-NEW box 85 xirise.py; latec.py second counter): K 4 m 8: R* 32; pin
# rstar/instances/latew_K16_m32 (R* 512 > n 482; regenerated and sha1-checked)
LATE=1 python3 -I span/mkrw.py 4 8 "$t/l48.pg" "$t/l48.start" > /dev/null; out=$(python3 -I span/latec.py "$t/l48.pg" "$t/l48.start"); [[ "$out" == "LATEC l48.pg n 122 iter 44 cuts 0 fallbacks 0 R* 32 late 33 max-per-edge-Wrun 4" ]] || { echo "latec l48 drifted: $out"; exit 1; }
sha1sum -c --quiet rstar/latew_K16_m32.sha1 || { echo "latew_K16_m32 pin changed"; exit 1; }
LATE=1 python3 -I span/mkrw.py 16 32 "$t/l1632.pg" "$t/l1632.start" > /dev/null; cmp -s "$t/l1632.pg" rstar/instances/latew_K16_m32.pg && cmp -s "$t/l1632.start" rstar/instances/latew_K16_m32.start || { echo "mkrw drifted from latew_K16_m32"; exit 1; }
# R139 (successor 33): XICH at ONE vertex quadratic: R120 Even wave observer on mkrw (mix/obs2.py OWNER=0 ABOVE=a): XICH(obs) = Km + K + 1
# (xich/xichc.py, n5b); K 4 m 8: 37; pin xich/instances/obs_K12_m24 (301 at n 272)
python3 -I span/mkrw.py 4 8 "$t/xw4.pg" "$t/xw4.start" > /dev/null; OWNER=0 ABOVE=a python3 -I mix/obs2.py "$t/xw4.pg" "$t/xw4.start" "$t/xo4.pg" "$t/xo4.start" > /dev/null
out=$(python3 -I xich/xichc.py "$t/xo4.pg" "$t/xo4.start"); [[ "$out" == "XICHC xo4.pg n 96 iterations 44 max-XICH 37 at obs (W-run length so far 44)" ]] || { echo "xichc drifted: $out"; exit 1; }
sha1sum -c --quiet xich/obs_K12_m24.sha1 || { echo "obs_K12_m24 pin changed"; exit 1; }
python3 -I span/mkrw.py 12 24 "$t/xw12.pg" "$t/xw12.start" > /dev/null; OWNER=0 ABOVE=a python3 -I mix/obs2.py "$t/xw12.pg" "$t/xw12.start" "$t/xo12.pg" "$t/xo12.start" > /dev/null
cmp -s "$t/xo12.pg" xich/instances/obs_K12_m24.pg && cmp -s "$t/xo12.start" xich/instances/obs_K12_m24.start || { echo "obs2 drifted from obs_K12_m24"; exit 1; }
# R140 (successor 33): Friedmann 0901.2731 / PGSolver switchallexp: switch-all V0 70 iterations at N 3, S4a arena optimum vs sigma-bar V1 8
# (fried/hybrid.py, Lemma ARENA-MAX); pins fried/instances/switchallexp_4/_6 (N5 8 / 12 iterations, xeng identical)
python3 ../hard-families/pgsolver_port.py switchallexp 3 > "$t/sa3.pg"
out=$(python3 -I fried/hybrid.py "$t/sa3.pg" V0); [[ "$out" == "HYBRID sa3.pg V0 iterations 70" ]] || { echo "hybrid V0 drifted: $out"; exit 1; }
out=$(python3 -I fried/hybrid.py "$t/sa3.pg" V1); [[ "$out" == "HYBRID sa3.pg V1 iterations 8" ]] || { echo "hybrid V1 drifted: $out"; exit 1; }
sha1sum -c --quiet fried/pins.sha1 || { echo "fried pins changed"; exit 1; }
python3 ../hard-families/pgsolver_port.py switchallexp 4 | cmp -s - fried/instances/switchallexp_4.pg || { echo "switchallexp 4 drifted"; exit 1; }
out=$(python3 -I seg/xeng.py fried/instances/switchallexp_4.pg fried/instances/switchallexp_4.start | tr '\n' ' '); [[ "$out" == "n5b: states 9 iterations 8 "*"identical: True " ]] || { echo "xeng switchallexp_4: $out"; exit 1; }
# R141 (successor 33): W-constant intervals (L-SI box 51b [P-INT]): wint/wint.py gives 8 on u23sw64_n32 (L-SI's max); idxmono: 26 of 64 upward
out=$(python3 -I wint/wint.py xing/instances/u23sw64_n32.pg); [[ "$out" == "WINT u23sw64_n32.pg n 32 longest-W-constant-interval 8 iterations 16" ]] || { echo "wint drifted: $out"; exit 1; }
out=$(python3 -I wint/idxmono.py xing/instances/u23sw64_n32.pg | cut -d' ' -f1-6); [[ "$out" == "IDXMONO u23sw64_n32.pg interval-switches 64 upward 26" ]] || { echo "idxmono drifted: $out"; exit 1; }
# R142 (successor 33): BIP(rho, tau) (L-NEW box 88). bip/bip.py (n5b) = bip/bip2.py (si.py) on the search pins: 24 steps at n 12, 13 at n 8
sha1sum -c --quiet bip/pins.sha1 || { echo "bip pins changed"; exit 1; }
for p in "bipsearch_n12 24" "bipsearch_n8 13"; do set -- $p
  a=$(python3 -I bip/bip.py bip/instances/$1.pg bip/instances/$1.start); b=$(python3 -I bip/bip2.py bip/instances/$1.pg bip/instances/$1.start)
  [[ "$a" == "BIP $1.pg n "*" steps $2" && "$b" == "BIP2 $1.pg n "*" steps $2" ]] || { echo "bip $1 drifted: $a / $b"; exit 1; }
done
# R142b (successor 33): lagged-clone fx (free/fxlag.py) against BIP-REL-1: sigma-bar re-routes (71 frozen stretches in 76 iterations), max strict
# releases of one edge in one frozen stretch 1 (bip/strictrel.py); pin free/instances/fxlag_K4_m16 (xeng identical, Oink OK)
sha1sum -c --quiet free/fxlag.sha1 || { echo "fxlag pin changed"; exit 1; }
python3 -I span/mkrw.py 4 16 "$t/fl.pg" "$t/fl.start" > /dev/null; python3 -I free/fxlag.py "$t/fl.pg" "$t/fl.start" "$t/flx.pg" "$t/flx.start" > /dev/null
cmp -s "$t/flx.pg" free/instances/fxlag_K4_m16.pg && cmp -s "$t/flx.start" free/instances/fxlag_K4_m16.start || { echo "fxlag drifted"; exit 1; }
out=$(python3 -I bip/strictrel.py free/instances/fxlag_K4_m16.pg free/instances/fxlag_K4_m16.start); [[ "$out" == "STRICTREL fxlag_K4_m16.pg n 234 iterations 76 frozen-stretches 71 max-strict-releases-one-edge-one-stretch 1 at ('w1', 'T1')" ]] || { echo "strictrel drifted: $out"; exit 1; }
# R143 (successor 34): Lemma SETTLE (lexc/settle.py: 0 violations; u23sw64 event-free 8 <= D 10; winseed_u23_n32 4 windows), model FT L - 1
# (lexc/ftmodel.py exhaustive L 3 = 2), and BIP-REL-1 DEAD (rel2/mkrel2.py: 2 strict releases of (y, oz) in one frozen stretch at n 82)
out=$(python3 -I lexc/settle.py xing/instances/u23sw64_n32.pg); [[ "$out" == "SETTLE u23sw64_n32.pg n 32 it 16 intervals 1 maxLEN 8 maxE 0 VIOL 0 OVERBOUND 0 maxNW 1 [8,0,10,1]" ]] || { echo "settle u23sw64 drifted: $out"; exit 1; }
sha1sum -c --quiet lexc/pins.sha1 || { echo "lexc pins changed"; exit 1; }
out=$(python3 -I lexc/settle.py lexc/winseed_u23_n32.pg lexc/winseed_u23_n32.start); [[ "$out" == "SETTLE winseed_u23_n32.pg n 32 it 12 intervals 1 maxLEN 7 maxE 3 VIOL 0 OVERBOUND 0 maxNW 4 [7,3,9,4]" ]] || { echo "settle winseed drifted: $out"; exit 1; }
out=$(python3 -I lexc/ftmodel.py exh 3 | cut -d" " -f1-10); [[ "$out" == "FT exh L 3 W 2 n_DAG 6 longest 2" ]] || { echo "ftmodel drifted: $out"; exit 1; }
sha1sum -c --quiet rel2/pins.sha1 || { echo "rel2 pins changed"; exit 1; }
python3 -I rel2/mkrel2.py "$t/r2.pg" "$t/r2.start" 2; cmp -s "$t/r2.pg" rel2/instances/rel2_R2_n82.pg && cmp -s "$t/r2.start" rel2/instances/rel2_R2_n82.start || { echo "mkrel2 drifted"; exit 1; }
out=$(python3 -I bip/strictrel.py rel2/instances/rel2_R2_n82.pg rel2/instances/rel2_R2_n82.start); [[ "$out" == "STRICTREL rel2_R2_n82.pg n 82 iterations 10 frozen-stretches 2 max-strict-releases-one-edge-one-stretch 2 at ('y', 'oz')" ]] || { echo "rel2 strictrel drifted: $out"; exit 1; }
out=$(python3 -I seg/xeng.py rel2/instances/rel2_R2_n82.pg rel2/instances/rel2_R2_n82.start | tail -1); [[ "$out" == "state sequences identical: True" ]] || { echo "xeng rel2: $out"; exit 1; }
if [[ -x ../../tools/oink/build/oink ]]; then out=$(bash rel2/oinkcmp.sh rel2/instances/rel2_R2_n82.pg rel2/instances/rel2_R2_n82.start); [[ "$out" == "OINK OK" ]] || { echo "rel2 oink: $out"; exit 1; }; fi
# R144 (successor 34): shared delay (rel2/mkrel3.py): R strict releases of (y, oz) in one frozen stretch at n = 54R - 20 (pin rel3_R4_n196:
# 4 at n 196, |F| 26); rel2/swcount.py time accounting (every chain vertex switches once)
python3 -I rel2/mkrel3.py 4 "$t/r3.pg" "$t/r3.start"; cmp -s "$t/r3.pg" rel2/instances/rel3_R4_n196.pg && cmp -s "$t/r3.start" rel2/instances/rel3_R4_n196.start || { echo "mkrel3 drifted"; exit 1; }
out=$(python3 -I bip/strictrel.py rel2/instances/rel3_R4_n196.pg rel2/instances/rel3_R4_n196.start); [[ "$out" == "STRICTREL rel3_R4_n196.pg n 196 iterations 26 frozen-stretches 2 max-strict-releases-one-edge-one-stretch 4 at ('y', 'oz')" ]] || { echo "rel3 strictrel drifted: $out"; exit 1; }
out=$(python3 -I rel2/swcount.py rel2/instances/rel3_R4_n196.pg rel2/instances/rel3_R4_n196.start); [[ "$out" == "SWCOUNT rel3_R4_n196.pg n 196 F 26 SW 79 sw1 61 sw2 0 sw3+ 4 maxSW 7 stretches 2 maxlen 25 meanlen 12.50" ]] || { echo "swcount rel3 drifted: $out"; exit 1; }
# R145 (successor 34): CONJECTURE FLIP-EV (L-SI box 52) DEAD: flipev_n10 (hand start) and flipevr_n10 (S3 start) each have an EXI sigma-bar flip
# at a non-cycle-node Odd vertex with no Xi-change at any head (flipev/flipev.py VIOL 1; FLIP-EV' VIOL2 0); xeng identical, Oink OK
sha1sum -c --quiet flipev/pins.sha1 || { echo "flipev pins changed"; exit 1; }
out=$(python3 -I flipev/flipev.py flipev/instances/flipev_n10.pg flipev/instances/flipev_n10.start); [[ "$out" == "FLIPEV flipev_n10.pg n 10 iterations 3 candidates 1 VIOL 1 MINHC 0 witness (k, o, old, new) (0, 8, 9, 4) VIOL2 0" ]] || { echo "flipev_n10 drifted: $out"; exit 1; }
out=$(python3 -I flipev/flipev.py flipev/instances/flipevr_n10.pg flipev/instances/flipevr_n10.start); [[ "$out" == "FLIPEV flipevr_n10.pg n 10 iterations 3 candidates 1 VIOL 1 MINHC 0 witness (k, o, old, new) (1, 9, 3, 0) VIOL2 0" ]] || { echo "flipevr_n10 drifted: $out"; exit 1; }
for f in flipev_n10 flipevr_n10; do out=$(python3 -I seg/xeng.py flipev/instances/$f.pg flipev/instances/$f.start | tail -1); [[ "$out" == "state sequences identical: True" ]] || { echo "xeng $f: $out"; exit 1; }
  if [[ -x ../../tools/oink/build/oink ]]; then out=$(bash rel2/oinkcmp.sh flipev/instances/$f.pg flipev/instances/$f.start); [[ "$out" == "OINK OK" ]] || { echo "oink $f: $out"; exit 1; }; fi; done
# R145c: sigma-bar flips K*m at ONE Odd vertex of out-degree 2 in one W-run (mkrw LATE=1 + mix/obs2.py + flipev/obs3.py; flipev/sbv.py 32 at K4 m8)
LATE=1 python3 -I span/mkrw.py 4 8 "$t/q1.pg" "$t/q1.start" > /dev/null; python3 -I mix/obs2.py "$t/q1.pg" "$t/q1.start" "$t/q2.pg" "$t/q2.start" > /dev/null
python3 -I flipev/obs3.py "$t/q2.pg" "$t/q2.start" "$t/q3.pg" "$t/q3.start" > /dev/null
out=$(python3 -I flipev/sbv.py "$t/q3.pg" "$t/q3.start"); [[ "$out" == "SBV q3.pg n 133 iterations 44 W-runs 1 longest 44 maxSB 32 at root (out-degree 2, returns 31, its W-run length 44)" ]] || { echo "sbv obs3 drifted: $out"; exit 1; }
# R146 (successor 34): ROOT-FLIP (L-SI 35) independent n5b check: tie instances BAD 0, 2000 tie-biased random games BAD 0
out=$(python3 -I flipev/rootflip.py flipev/instances/flipev_n10.pg flipev/instances/flipev_n10.start); [[ "$out" == "ROOTFLIP flipev_n10.pg TR 1 FL 2 TIE 1 BAD 0 witness None" ]] || { echo "rootflip drifted: $out"; exit 1; }
out=$(python3 -I flipev/rootflip.py --rand 1 2000 10 16 1); [[ "$out" == "ROOTFLIP-RAND seed 1 games 2000 n 10-16 bias 1 TR 500 FL 711 TIE 0 BAD 0 witness None" ]] || { echo "rootflip rand drifted: $out"; exit 1; }
# R147 (successor 35): Theorem SRC-SETTLE (source heads D u C): xcn/srcsettle.py VIOL/VIOL2/TAILV/BLKV/CNOX 0; one-vertex repeats in one
# W-run: XCN 4 at own node 0 (xcn4_n12), CN 3 at W-cycle node 1, all cosmetic, C-only tail 2, no source event (cn3_n9); xeng identical, Oink OK
sha1sum -c --quiet xcn/pins.sha1 || { echo "xcn pins changed"; exit 1; }
out=$(python3 -I xcn/xcn.py xcn/instances/xcn4_n12.pg xcn/instances/xcn4_n12.start); [[ "$out" == "XCN xcn4_n12.pg n 12 iters 5 wruns 2 maxL 4 maxCN 0 maxCNc 0 maxXCN 4 maxXCNo 4 sumCN 0 sumXCN 4" ]] || { echo "xcn4 drifted: $out"; exit 1; }
out=$(python3 -I xcn/srcsettle.py xcn/instances/cn3_n9.pg xcn/instances/cn3_n9.start); [[ "$out" == "SRC cn3_n9.pg n 9 VIOL 0 E 3 Esrc 3 CN 3 CNO 3 CNOX 0 FLIPONLY 0 maxblk 0 maxL 3 maxEsrc 3 maxE 3 maxHXS 0 VIOL2 0 TAILV 0 BLKV 0 maxblk2 3 maxtail 2 Es2 0" ]] || { echo "cn3 drifted: $out"; exit 1; }
out=$(python3 -I xcn/srcrand.py 1 300 5 10); [[ "$out" == "SRCRAND seed 1 games 300 n 5-10 VIOL 0 E 13 Esrc 8 CN 5 CNO 5 CNOX 0 FLIPONLY 0 maxblk 1 maxL 1 maxEsrc 1 maxE 1 maxHXS 1 VIOL2 0 TAILV 0 BLKV 0 maxblk2 1 maxtail 1 Es2 4 firstbad None" ]] || { echo "srcrand drifted: $out"; exit 1; }
for f in xcn4_n12 cn3_n9; do out=$(python3 -I seg/xeng.py xcn/instances/$f.pg xcn/instances/$f.start | tail -1); [[ "$out" == "state sequences identical: True" ]] || { echo "xeng $f: $out"; exit 1; }
  if [[ -x ../../tools/oink/build/oink ]]; then out=$(bash rel2/oinkcmp.sh xcn/instances/$f.pg xcn/instances/$f.start); [[ "$out" == "OINK OK" ]] || { echo "oink $f: $out"; exit 1; }; fi; done
# P-N5-SRC (FROZEN packet + line, successor 35): sha1 pinned; the frozen files are never edited (fixes go in a separate file)
echo "3caae56e3afdfaab80739c0e12e397b3d6cc7a8b  ../../docs/red/P-N5-SRC.md" | sha1sum -c --quiet || { echo "P-N5-SRC packet changed"; exit 1; }
echo "3101a0c04f7959ccd50b86f5e6fa76789bdf6995  ../../docs/red/P-N5-SRC-line.txt" | sha1sum -c --quiet || { echo "P-N5-SRC line changed"; exit 1; }
# R148 (successor 35): CONJECTURE CASCADE-LIN (L-NEW box 99) DEAD: cascl_K4_m8_N100 (mkrw LATE=1 K4 m8 + 100 passive clones of Even 63, n 222):
# one FRESH tick of clock 4 roots 121 > n/2 returns (L-NEW retcause.py, data in casc/retcause_out.txt); here: regeneration, return count, xeng, Oink.
# R148-hxs: HXS at ONE source (Odd observer, obs2) = K(m + 1) = 36 at K4 m8 (xcn/hxs.py)
sha1sum -c --quiet casc/pins.sha1 || { echo "casc pins changed"; exit 1; }
LATE=1 python3 -I span/mkrw.py 4 8 "$t/cb.pg" "$t/cb.start" > /dev/null; python3 -I casc/clone.py "$t/cb.pg" "$t/cb.start" 63 100 "$t/cc.pg" "$t/cc.start"
cmp -s "$t/cc.pg" casc/instances/cascl_K4_m8_N100.pg && cmp -s "$t/cc.start" casc/instances/cascl_K4_m8_N100.start || { echo "clone drifted from cascl_K4_m8_N100"; exit 1; }
out=$(python3 -I casc/retx.py casc/instances/cascl_K4_m8_N100.pg casc/instances/cascl_K4_m8_N100.start); [[ "$out" == "RETX cascl_K4_m8_N100.pg n 222 F 44 returns 798 topX [(63, 7), (66, 7), (69, 7), (72, 7), (75, 7), (78, 7)]" ]] || { echo "retx drifted: $out"; exit 1; }
out=$(python3 -I seg/xeng.py casc/instances/cascl_K4_m8_N100.pg casc/instances/cascl_K4_m8_N100.start | tail -1); [[ "$out" == "state sequences identical: True" ]] || { echo "xeng cascl: $out"; exit 1; }
if [[ -x ../../tools/oink/build/oink ]]; then out=$(bash rel2/oinkcmp.sh casc/instances/cascl_K4_m8_N100.pg casc/instances/cascl_K4_m8_N100.start); [[ "$out" == "OINK OK" ]] || { echo "oink cascl: $out"; exit 1; }; fi
# R148 cont.: cascl66_K4_m8_N150 (n 272, clones of 66, 2 returns per root: one FRESH root 321 > n); casctf_n10_N210 (L-NEW topfix_n10 + 210 clones
# of 193, 17 returns per root each: one FRESH root 3620 = 8.6n; CASC grows ~n^2 along topfix_N)
python3 -I casc/clone.py "$t/cb.pg" "$t/cb.start" 66 150 "$t/c6.pg" "$t/c6.start"
cmp -s "$t/c6.pg" casc/instances/cascl66_K4_m8_N150.pg && cmp -s "$t/c6.start" casc/instances/cascl66_K4_m8_N150.start || { echo "clone drifted from cascl66"; exit 1; }
python3 -I casc/clone.py ../new/box52/out/topfix_n10.pg - 193 210 "$t/tf.pg" -; python3 -I casc/defstart.py "$t/tf.pg" "$t/tf.start"
cmp -s "$t/tf.pg" casc/instances/casctf_n10_N210.pg && cmp -s "$t/tf.start" casc/instances/casctf_n10_N210.start || { echo "clone drifted from casctf"; exit 1; }
out=$(python3 -I casc/retx.py casc/instances/casctf_n10_N210.pg casc/instances/casctf_n10_N210.start); [[ "$out" == "RETX casctf_n10_N210.pg n 420 F 58 returns 3822 topX [(192, 18), (193, 17), (210, 17), (211, 17), (212, 17), (213, 17)]" ]] || { echo "retx casctf drifted: $out"; exit 1; }
for f in cascl66_K4_m8_N150 casctf_n10_N210; do out=$(python3 -I seg/xeng.py casc/instances/$f.pg casc/instances/$f.start | tail -1); [[ "$out" == "state sequences identical: True" ]] || { echo "xeng $f: $out"; exit 1; }
  if [[ -x ../../tools/oink/build/oink ]]; then out=$(bash rel2/oinkcmp.sh casc/instances/$f.pg casc/instances/$f.start); [[ "$out" == "OINK OK" ]] || { echo "oink $f: $out"; exit 1; }; fi; done
python3 -I mix/obs2.py "$t/cb.pg" "$t/cb.start" "$t/cbo.pg" "$t/cbo.start" > /dev/null
out=$(python3 -I xcn/hxs.py "$t/cbo.pg" "$t/cbo.start"); [[ "$out" == "HXS cbo.pg n 131 iters 44 F 44 ES 40 maxHXS 36 top 122(D,O,deg8):36 90(D,O,deg2):8 95(D,O,deg2):8" ]] || { echo "hxs obs drifted: $out"; exit 1; }
TMPDIR="$t" python3 correspond.py 2 3 4 5 6 > "$t/corr.log" || { cat "$t/corr.log"; exit 1; }
python3 xcheck.py --games 150 --nmax 7 --seed 7 > "$t/x.log" || { cat "$t/x.log"; exit 1; }
echo "red check: R148 CASCADE-LIN dead (121 > 111; 321 > n 272; 3620 = 8.6n), HXS(obs) 36; R147 SRC-SETTLE 0 viol, XCN 4 / CN 3 at one vertex; R146 rootflip BAD 0; R145 SB 32 at root (K4 m8), FLIP-EV dead (flipev_n10, flipevr_n10); R144 rel3 4 at n 196; R143 SETTLE 8 <= 10, FT 2, rel2 strict releases 2; R142 bip 24 at n 12; R141 wint 8 / up 26; R140 switchallexp 3 V0 70 / V1 8; R139 XICH(obs) 37 at K4 m8; R138 R* 32 at K4 m8; R137 FREE 16/edge at K4 m16; R136 rb48 PAT 4, te_8 0 served; R135 dg_16 4 iterations, noup k5 7 vs 31; R134 ZXC(obs) 69/76; R133 lazyhurt_n9 3 vs 6; R132 mkrt REP 21, DAG-tau* 200/200; R131 tiedrb_K8_m16 pin, untied re-blocked 18 at K 4 m 8; R130 wdepth_K4_m64 pin, depth 7 at m 16; R127 latew_K8_m32 pin, R* 64 at K 4; R124 mkrb K3 30, bidir_K8_m32 pin; R123 spanobs_K12_m48 pin, span(e, o) MAT 34 at K 4; carryobs_K12_m48 pin, SEG 53 at K 4; R122 FG 119/28; R121 tobs_K8_m32 pin, target #MAT 60; R120 wobs_K8_m32 pin, observer #MAT 60 at K 4; R119 mgcheck dw_3 0/1145, mixgate 3 300 1 = 2; R118 mk_20_80 pin, tstretch 21; R116 dw_3 134/11, dw_4 286/26; R114 sf2/fsubexp OK; R115 fc3 121/9; r2_check PASS (R11), bsolo 4 = 4 tangles/7 iterations (R10); dtl_flipflop F8 = 36/1/5 (R9), Claim P/Q 0 violations; zadeh_lb N2 = 43 (no fixed order, R7); fhz_padded 2 S7 = 16 (R5 kill);  friedmann_Gn 2 S7 = 15; fhz lockstep3/relation/export OK; gated_bland 6 = 63 MSF iterations (regions = Zielonka, strategies verified); Claim F instances; MSF == Bland N<=6; $(tail -1 "$t/x.log")"
