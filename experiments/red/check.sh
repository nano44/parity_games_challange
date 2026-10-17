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
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/ctx13_n40.pg --quiet 2>&1 | sed -n 1p)   # box 7: 13 distinct first-difference contexts in one phase (CTX+), both orders
[[ "$out" == "n=40 tangles=91 dominions=1 iterations=29" ]] || { echo "ctx13_n40 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/ctx12_n40.pg --quiet 2>&1 | sed -n 1p)   # box 7: 12 distinct first-difference contexts in one phase (CTX+), both orders
[[ "$out" == "n=40 tangles=65 dominions=1 iterations=26" ]] || { echo "ctx12_n40 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/fall4_n116.pg --quiet 2>&1 | sed -n 1p)   # box 7 R31 §2: 4 descents of Π_R at one context (FALL), both orders
[[ "$out" == "n=116 tangles=82 dominions=6 iterations=13" ]] || { echo "fall4_n116 drifted: $out"; exit 1; }
out=$(python3 -I dtl/dtl_flipflop.py carry/instances/fall3_n76.pg --quiet 2>&1 | sed -n 1p)   # box 7 R31: 3 descents of Π_R at one context (FALL), both orders
[[ "$out" == "n=76 tangles=56 dominions=3 iterations=10" ]] || { echo "fall3_n76 drifted: $out"; exit 1; }
if [[ -x ../../tools/oink/build/oink ]] && command -v g++ > /dev/null; then
  meet/oinkmeet.sh carry/instances/meet_viol_n17.pg | grep -q "^MEET FAILS at search 0" || { echo "meet_viol_n17: pinned Oink no longer shows the (MEET) failure (R30)"; exit 1; }
else echo "meet_viol_n17 pinned-Oink check skipped (no oink build or no g++)"; fi
TMPDIR="$t" python3 correspond.py 2 3 4 5 6 > "$t/corr.log" || { cat "$t/corr.log"; exit 1; }
python3 xcheck.py --games 150 --nmax 7 --seed 7 > "$t/x.log" || { cat "$t/x.log"; exit 1; }
echo "red check: r2_check PASS (R11), bsolo 4 = 4 tangles/7 iterations (R10); dtl_flipflop F8 = 36/1/5 (R9), Claim P/Q 0 violations; zadeh_lb N2 = 43 (no fixed order, R7); fhz_padded 2 S7 = 16 (R5 kill);  friedmann_Gn 2 S7 = 15; fhz lockstep3/relation/export OK; gated_bland 6 = 63 MSF iterations (regions = Zielonka, strategies verified); Claim F instances; MSF == Bland N<=6; $(tail -1 "$t/x.log")"
