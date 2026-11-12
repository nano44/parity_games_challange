#!/usr/bin/env bash
# L-SI box 104 check (~1 s, no engine, no git): the frozen outputs of run104.sh, runw104.sh (and replay209.sh when present).
# WRAP (wrap104.py): (1) random games: the six counters 0 (xi: two sets; spec: one), controls fire, the frozen 300 replay with 0
#   differing rows; (2) W(G_n, iota) of arXiv 1106.0778v2, both priority versions, n = 1..6: Fact 6.1's node and edge counts, Howard
#   T = 9 * 2^n - 10 with 0 tie events, N5'-xi = T + 3, counters 0; N5 (spec) counters 0; (3) W(switchallexp_n), n = 2..6: T + 3 with
#   the listed counts, counters 0; no tie event on Howard's run, n = 2..8; (4) two engines AGREE+CORRECT on 7 wrapped games;
#   (5) the long rows (out/wrap_long.out), when present.
# FREE genomes (free104.py): (6) F_n, N5'-xi from S3: iterations = Howard T + 3, 1 fallback, n = 2..8; E-DOM build and N5 (spec)
#   controls; (7) two engines AGREE+CORRECT at n = 2..5; (8) state for state: mism 0 at n = 2..6, control fires; (9) Lemma FREE-REACH
#   counters 0 on random free genomes, controls fire; (10) F_n is outside E-DOM, the E-DOM build is inside.
# (11) instance sha1; (12) quotes: 0 FAIL at the sources, and every quoted string stands in docs/si/box104-map.md.
set -u
cd "$(dirname "$0")"
fail=0
bad() { echo "BOX104 FAIL $1"; fail=1; }
Z="s3fail 0 nonstd 0 nohoward 0 fbwrong 0 endwrong 0 wrong 0"
# (1)
[ "$(grep -c ": $Z | " out/wrap_rand.out)" = 3 ] && [ "$(wc -l < out/wrap_rand.out)" = 3 ] || bad "wrap random"
grep -q "CTRL 1: s3fail 0 nonstd 0 nohoward [1-9]" out/wrap_ctrl.out || bad "wrap control 1"
grep -q "CTRL 2: .* fbwrong 100 endwrong 100 " out/wrap_ctrl.out || bad "wrap control 2"
grep -q "games 300: $Z | rows differing from the frozen (T, iterations, |W|) 0$" out/wrap_json.out || bad "wrap frozen 300"
# (2)
for v in fig4 table4; do for p in "1 8" "2 26" "3 62" "4 134" "5 278" "6 566"; do
  set -- $p
  grep -q "^WRAP104 alg xi lmcs $v n $1: .* Fact 6.1 (nodes, edges) True .* Howard T (own howard) $2 tie events 0 | .* | T $2 iterations $(($2 + 3)) | iterations - Howard T = 3 | 2^n = $((1 << $1)) | $Z$" out/wrap_lmcs_xi.out || bad "wrap lmcs $v xi n $1"
done; done
[ "$(grep -c "lmcs fig4 n [1-6]: .* distinct priorities \([0-9]*\) | .*" out/wrap_lmcs_xi.out)" = 6 ] || bad "wrap lmcs rows"
[ "$(grep -c "| $Z$" out/wrap_lmcs_spec.out)" = 6 ] || bad "wrap lmcs spec"
# (3)
for p in "2 30 33" "3 70 73" "4 150 153" "5 310 313" "6 630 633"; do
  set -- $p
  grep -q "^WRAP104 alg xi switchallexp n $1: .* Howard T (fried.howard) $2 | .* | T $2 iterations $3 | iterations - Howard T = 3 | $Z$" out/wrap_fried_xi.out || bad "wrap xi n $1"
done
[ "$(grep -c "| $Z$" out/wrap_fried_spec.out)" = 5 ] || bad "wrap spec"
[ "$(grep -c "; tie events 0$" out/wrap_ties.out)" = 7 ] || bad "wrap ties"
# (4)
[ "$(grep -c "impl1 iterations \([0-9]*\) fallbacks 1; impl2 iterations \1 fallbacks 1; regions equal True; vs Zielonka True/True; verify errors 0/0; AGREE+CORRECT$" out/wrap_xck.out)" = 7 ] || bad "wrap xck"
# (5)
if [ -f out/wrap_long.out ]; then
  for p in "lmcs fig4 n 7: .* Howard T (own howard) 1142 tie events 0 | .* iterations 1145 " "lmcs fig4 n 8: .* Howard T (own howard) 2294 tie events 0 | .* iterations 2297 " \
           "switchallexp n 7: .* Howard T (fried.howard) 1243 | .* iterations 1246 " "switchallexp n 8: .* Howard T (fried.howard) 2486 | .* iterations 2489 "; do
    grep -q "^WRAP104 alg xi $p| iterations - Howard T = 3 | .*$Z$" out/wrap_long.out || bad "wrap long: $p"
  done
  [ "$(grep -c "AGREE+CORRECT$" out/wrap_long.out)" = 2 ] || bad "wrap long xck"
fi
# (6)
for p in "2 30 33" "3 70 73" "4 150 153" "5 310 313" "6 630 633" "7 1243 1246" "8 2486 2489"; do
  set -- $p
  grep -q "^F104 n $1 mode free alg xi: .* Howard T $2 | .* | iterations $3 fallbacks 1 | iterations - T = 3 | S3 = standard start True" out/free_xi.out || bad "free xi n $1"
done
for p in "2 17" "3 19" "4 21" "5 23" "6 25"; do
  set -- $p
  grep -q "^F104 n $1 mode edom alg xi: .* | iterations $2 fallbacks 1 | .* S3 = standard start True" out/edom_xi.out || bad "edom xi n $1"
done
for p in "2 5" "3 5" "4 5" "5 5" "6 6"; do
  set -- $p
  grep -q "^F104 n $1 mode free alg spec: .* | iterations $2 fallbacks 1 | " out/free_spec.out || bad "free spec n $1"
done
# (7)
[ "$(grep -c "impl1 iterations \([0-9]*\) fallbacks 1; impl2 iterations \1 fallbacks 1; regions equal True; vs Zielonka True/True; verify errors 0/0; AGREE+CORRECT$" out/xck.out)" = 4 ] || bad "xck"
# (8)
[ "$(grep -c "; mism 0$" out/xtraj.out)" = 5 ] && [ "$(wc -l < out/xtraj.out)" = 5 ] || bad "xtraj"
[ "$(grep -c "CTRL: .*; mism [1-9]" out/xtraj_ctrl.out)" = 2 ] || bad "xtraj control"
# (9)
[ "$(grep -c ": $Z | " out/freereach.out)" = 3 ] && [ "$(wc -l < out/freereach.out)" = 3 ] || bad "freereach"
grep -q "CTRL 1: s3fail 0 nonstd 0 nohoward [1-9]" out/freereach_ctrl.out || bad "freereach control 1"
grep -q "CTRL 2: .* fbwrong 100 endwrong 100 " out/freereach_ctrl.out || bad "freereach control 2"
# (10)
[ "$(grep -c "mode free: .*; odd betas above some e [1-9]" out/prio.out)" = 7 ] || bad "prio free"
[ "$(grep -c "mode edom: e-vertices below some beta 0 of .*; odd e 0; odd betas above some e 0;" out/prio.out)" = 7 ] || bad "prio edom"
# (11), (12)
(cd inst && sha1sum -c --quiet SHA1SUMS) || bad "instance sha1"
grep -q "^QUOTES104 total [0-9]* fail 0$" out/quotes104.out || bad "quotes at source"
python3 -I quotes104.py doc ../../../docs/si/box104-map.md > /dev/null || bad "quotes in the doc"
if [ -f out/replay209_level.out ]; then python3 -I replay209sum.py > /dev/null || bad "replay209 counters"; fi
[ $fail = 0 ] && echo "BOX104 checks: PASS"
exit $fail
