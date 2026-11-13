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
# §2a kill search (frozen outputs, when present): 40 chunks, every best L* 5; every best genome replayed on N5 with six counters 0
if [ -f out/climbval106.out ]; then
  [ "$(grep -c "^MG106 climb seed [0-9]* restarts 10 steps 5000: best L\* 5 | " out/climb106.out)" = 40 ] && [ "$(wc -l < out/climb106.out)" = 40 ] || bad "climb rows"
  [ "$(grep -c "L\* 5 (search: 5) Xi-graph cyclic | s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0$" out/climbval106.out)" = 40 ] || bad "climb replays"
fi
# §3b audit of cnf106.py (frozen out/aud106.out): CNF = mg106 on 2,340 genomes (incl. the 40 climbed L* = 5 genomes), every bit determined
#   on the --full sets, the three encoder mutations fire
if [ -f out/aud106.out ]; then
  [ "$(grep -c ": (genome, state, mover) units [0-9]* avfail 0 avfree [0-]* runfail 0 unsat 0 | " out/aud106.out)" = 3 ] || bad "cnf audit"
  grep -q "^AUD106 seed json genomes 40 full: .* avfail 0 avfree 0 runfail 0 unsat 0 | max L\* 5$" out/aud106.out || bad "cnf audit long runs"
  for c in 1 2 3; do grep -q "^AUD106 seed 1067 genomes 100 CTRL $c: .*| first " out/aud106.out || bad "cnf control $c"; done
fi
# §3c controls (frozen out/solve106.out): c5, g5 SAT with N5 replays clean; g6, c9 UNSAT, both checkers VERIFIED, regenerated equal
if [ -f out/solve106.out ]; then
  for t in c5 g5; do grep -q "^SOLVE106 $t L\* >= 5.*: SAT | .* decoded L\* (mg106) 5 | model run = mg106 run prefix True$" out/solve106.out && grep -q "^N5REPLAY106 $t: .* L\* 5 .* | s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0$" out/solve106.out || bad "control $t"; done
  for t in g6 c9; do grep -q "^SOLVE106 $t .*: UNSAT | " out/solve106.out && [ "$(grep -c "^CHECK106 $t [a-z_]*: s VERIFIED" out/solve106.out)" = 2 ] && grep -q "^REGEN106 $t cnf equal yes proof equal yes$" out/solve106.out || bad "control $t"
    f=dump/$t.drup.gz; [ -f $f ] && grep -q "^PROOF106 $t $f bytes $(stat -c %s $f) sha1 $(sha1sum < $f | cut -c1-40)$" out/solve106.out || bad "proof file $t"; done
fi
[ $fail = 0 ] && echo "BOX106 checks: PASS"
exit $fail
