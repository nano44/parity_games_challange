#!/usr/bin/env bash
# L-SI box 107 self-check (fast, deterministic): the ABANDON / ONE-AHEAD counters on the five towers equal the frozen output and are 0 with
# a firing control; the committed k = 2 model replays on L-NEW's one217.OneP; the small SAT answers (d = 2 ladder, bi-ladder d <= 4,
# pair networks P <= 3) are re-derived and equal the frozen lines. The long SAT answers (d = 3, 4; bi-ladder d >= 5; pair networks
# P >= 4) are NOT re-run here: they are frozen lines of run107.sh, labelled «search answer, uncertified» in the doc.
set -eu
cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
TOP=${TOP:-$(git rev-parse --show-toplevel)}
git -C "$TOP" archive a143d4060 experiments/new/box217/one217.py experiments/new/box212/inst | tar -x -C "$T"
[ "$(sha1sum < "$T/experiments/new/box217/one217.py" | cut -c1-40)" = "$(cat one217.sha1)" ]
ONE="$T/experiments/new/box217"; INST="$T/experiments/new/box212/inst"
python3 -I abandon107.py "$ONE" --lmax 7 "$INST"/DBL4_d20_F30.json "$INST"/RECF4_d20_F60.json "$INST"/H5_d20_F62.json "$INST"/H6_d24_F126.json "$INST"/HIT7_d28_F254.json > "$T/ab.out"
cmp "$T/ab.out" out/abandon107.out
grep -q "^TOTAL bad_i 0 viol_ii 0 viol_iii 0 viol_iv 0$" out/abandon107.out
if grep -q "CONTROL-SILENT" out/abandon107.out; then echo "control silent"; exit 1; fi
[ "$(grep -c " ctrl [1-9]" out/abandon107.out)" = 5 ]
python3 -I replay107.py "$ONE" out/k2_d2.json > "$T/rp.out"; cmp "$T/rp.out" out/replay107.out
grep -q "replay_equals_model 1 sw \[1, 1, 3, 1\] full \[0, 1, 2\]" out/replay107.out
chk() { local f=$1 key=$2; shift 2; "$@" > "$T/l" 2>&1; a=$(grep -- "^$key " "$T/l"); b=$(grep -- "^$key " "$f"); [ -n "$a" ] && [ "$a" = "$b" ] || { echo "MISMATCH $key"; exit 1; }; }
python3 -I replay107.py "$ONE" ctrl/lead_bil4.json > "$T/c.out"
for T_ in 7 8; do python3 syn107.py 4 $T_ len --fix ctrl/lead_bil4.json --notime | grep "^SYN107" >> "$T/c.out"; done
cmp "$T/c.out" out/ctrl107.out
grep -q "lead_bil4.json N 8 T_key 7 " out/ctrl107.out
grep -q "SYN107 d 4 T 7 goal len extra \[\] FIXED ctrl/lead_bil4.json solver cadical195 answer SAT" out/ctrl107.out
grep -q "SYN107 d 4 T 8 goal len extra \[\] FIXED ctrl/lead_bil4.json solver cadical195 answer UNSAT" out/ctrl107.out
chk out/syn107.out "SYN107 d 2 T 6 goal full:2" python3 syn107.py 2 6 full:2 --notime
chk out/syn107.out "SYN107 d 2 T 8 goal len" python3 syn107.py 2 8 len --notime
for dT in "2 2" "2 3" "3 3" "3 4" "4 6" "4 7"; do set -- $dT; chk out/bil107.out "BIL107 d $1 T $2 full None" python3 bil107.py $1 $2 --notime; done
for PT in "1 1" "1 2" "2 2" "2 3" "3 4" "3 5"; do set -- $PT; chk out/pn107.out "PN107 P $1 T $2 chain 0 full None" python3 pn107.py $1 $2 --notime; done
for dT in "2 3" "2 4" "3 5" "3 6"; do set -- $dT; chk out/up107.out "UP107 d $1 T $2 goal len" python3 up107.py $1 $2 len --notime; done
python3 -I replay107.py "$ONE" out/up_k2_d4.json out/up_k3_d6.json > "$T/rpu.out"; cmp "$T/rpu.out" out/replay107_up.out
[ "$(grep -c "replay_equals_model 1" out/replay107_up.out)" = 2 ]
grep -q "up_k3_d6.json N 12 T_key 8 replay_equals_model 1 sw \[1, 1, 3, 3, 7, 1, 3, 3, 3, 2, 1, 1\] full \[0, 1, 2, 3, 4\]" out/replay107_up.out
python3 -I fill107.py check
chk out/pn107.out "PN107 P 3 T 22 chain 1 full \[(2, 0)\]" python3 pn107.py 3 22 --chain --full 2:0 --notime
if grep -rn "/hom[e]/user" *.py *.sh > /dev/null; then echo "absolute path in a tool"; exit 1; fi
echo "box 107 check OK"
