#!/usr/bin/env bash
# L-SI box 106 check (< 1 s): layer 1 (skel106.py, exact enumeration of the adversarial KEY runs on the depth-2 ladder) is re-run and must
# reproduce the frozen summary line and the frozen list of the 1,488 runs of length >= 6 byte for byte; the §2 audit lines (frozen).
set -u
cd "$(dirname "$0")"
fail=0
bad() { echo "BOX106 FAIL $1"; fail=1; }
T=$(mktemp); trap 'rm -f "$T"' EXIT
[ "$(python3 -I skel106.py 6 "$T")" = "$(cat out/skel106.out)" ] || bad "skel106 summary"
cmp -s "$T" out/skel106_ge6.txt || bad "skel106 list"
grep -q "^SKEL106 max length over 24 gate orders x 16 starts: 8 | .* 6:1072 7:352 8:64 | lines written (length >= 6) 1488$" out/skel106.out || bad "skel106 numbers"
# §2 audit (mg106.py, frozen out/mg106.out): the mover-game availability equals SPEC's on 2 x 300 random genomes (every state), the
#   control fires, and the abstract KEY run equals key105.py's on 1,000 genomes
[ "$(grep -c "^MG106 rand seed 106[24] genomes 300: (genome, state, mover) units 19200 mgfail 0$" out/mg106.out)" = 2 ] || bad "mg audit"
grep -q "^MG106 rand seed 1061 genomes 20 CTRL 1: .* mgfail [1-9]" out/mg106.out || bad "mg control"
grep -q "^MG106 xrun seed 1063 genomes 1000: runfail 0 " out/mg106.out || bad "mg xrun"
[ $fail = 0 ] && echo "BOX106 checks: PASS"
exit $fail
