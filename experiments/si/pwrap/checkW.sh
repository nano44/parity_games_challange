#!/usr/bin/env bash
# L-SI packet P-N5-WRAP check (~1 s, no engine, no git): (1) the 30 [Q] items were found at their pinned sources (frozen out/qwrap.out)
# and each stands in docs/si/P-N5-WRAP.md (qwrap.py doc reads out/qwrap.json); (2) the frozen instances of experiments/si/box104/inst
# (sha1); (3) the DATA lines of the packet's §9, re-read from experiments/si/box104/out; (4) once frozen, the packet's sha1.
set -u
cd "$(dirname "$0")"
fail=0
bad() { echo "PWRAP FAIL $1"; fail=1; }
[ "$(grep -c "^QWRAP [A-Za-z0-9-]* OK " out/qwrap.out)" = 30 ] && [ "$(wc -l < out/qwrap.out)" = 30 ] || bad "quotes at source"
python3 -I qwrap.py doc ../../../docs/si/P-N5-WRAP.md > /dev/null || bad "quotes in the packet"
(cd ../box104/inst && sha1sum -c --quiet SHA1SUMS) || bad "instance sha1"
O=../box104/out
Z="s3fail 0 nonstd 0 nohoward 0 fbwrong 0 endwrong 0 wrong 0"
for p in "1 8 211" "2 26 395" "3 62 600" "4 134 826" "5 278 1073" "6 566 1341"; do
  set -- $p
  grep -q "^WRAP104 alg xi lmcs fig4 n $1: .* Howard T (own howard) $2 tie events 0 | |W| $3 | T $2 iterations $(($2 + 3)) | .*$Z$" $O/wrap_lmcs_xi.out || bad "W^L_$1"
  [ "$2" = $((9 * (1 << $1) - 10)) ] || bad "T formula n $1"
done
for p in "7 1142 1630" "8 2294 1940"; do
  set -- $p
  grep -q "^WRAP104 alg xi lmcs fig4 n $1: .* Howard T (own howard) $2 tie events 0 | |W| $3 | T $2 iterations $(($2 + 3)) | .*$Z$" $O/wrap_long.out || bad "W^L_$1 long"
  [ "$2" = $((9 * (1 << $1) - 10)) ] || bad "T formula n $1"
done
for n in 1 2 3 4 5 6 7 8; do [ $((21 * n * n + 305 * n + 96)) = $((2 * $(grep -h "lmcs fig4 n $n:" $O/wrap_lmcs_xi.out $O/wrap_long.out | head -1 | sed 's/.*|W| \([0-9]*\) .*/\1/'))) ] || bad "|W| formula n $n"; done
[ "$(grep -c "^WRAP104 alg spec lmcs fig4 n [1-4]: .* F 4 iterations 6 | .*$Z$" $O/wrap_lmcs_spec.out)" = 4 ] || bad "N5 on W^L_n"
[ "$(grep -c ": $Z | " $O/wrap_rand.out)" = 3 ] || bad "random sets"
grep -q "CTRL 1: s3fail 0 nonstd 0 nohoward 405 " $O/wrap_ctrl.out || bad "control 1"
grep -q "CTRL 2: .* fbwrong 100 endwrong 100 " $O/wrap_ctrl.out || bad "control 2"
if [ -f out/P-N5-WRAP.sha1 ]; then (cd ../../.. && sha1sum -c --quiet experiments/si/pwrap/out/P-N5-WRAP.sha1) || bad "packet sha1"; fi
# (5) fixes entry 1: L-2 and the fixes file at their pinned sha1 (built by fix1/mkL2.py from L-1 and the two referee reports; mkL2.out
#   records the check stage be7da8f3 = L-1 + LW-1)
if [ -f fix1/SHA1SUMS ]; then
  (cd ../../.. && sha1sum -c --quiet experiments/si/pwrap/fix1/SHA1SUMS) || bad "fixes entry 1 sha1"
  grep -q "^L-1 + LW-1 sha1 be7da8f3a98e4c5a26158eae9aa2766c56531222 3190 B; .*: True$" fix1/mkL2.out || bad "fix1 check stage"
fi
[ $fail = 0 ] && echo "PWRAP checks: PASS"
exit $fail
