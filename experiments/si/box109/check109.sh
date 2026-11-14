#!/usr/bin/env bash
# L-SI box 109 self-check (deterministic, about 40 s) for docs/si/box109-design.md (hybrids h1-h4, candidate S8 = RF):
# 1. every row that tab109.py generates from the frozen out/*.out is in the design file, line by line;
# 2. fresh runs on the families that need no external tree (gk, sae, sbe, ports) reproduce the frozen lines: N5's 2^k + 1 on
#    Gamma3(G_3), Gamma3(G_4); RF, Howard, NH, h1 on small sizes; a control (a wrong frozen count must be reported);
# 3. RF (rf109.py's own run) equals n6.py's mode rf on those games, and its .sol passes harness verify on one game;
# 4. 300 random games: RF's regions equal harness Zielonka's, strategies verified; control: a flipped winner is reported on every game;
# 5. Addendum A: K^s_n (n = 1..6) and the decoyed switchallexp (N = 1, 2): fresh lines equal the frozen ones; RF's closed form; RFA = Howard.
set -eu
cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
TOP=${TOP:-$(git rev-parse --show-toplevel)}; DOC=${DOC:-"$TOP/docs/si/box109-design.md"}
strip() { sed -E 's/ secs [0-9.]+$//'; }
python3 tab109.py > "$T/rows"
[ "$(wc -l < "$T/rows")" -ge 60 ]
while IFS= read -r line; do grep -qxF -- "$line" "$DOC" || { echo "table row missing in the doc: $line"; exit 1; }; done < "$T/rows"
{ python3 fam109.py table gk 3 4 -- spec xi h1 h3 howard h4 nh rf rf2 --check
  python3 fam109.py table gk 5 6 -- xi h1 howard rf --check
  python3 fam109.py table sae 1 2 3 4 5 -- spec h1 howard nh rf rf2 --check
  python3 fam109.py table sbe 1 2 3 4 -- spec howard nh rf --check
  python3 fam109.py table cun 2 3 4 -- howard rf --check; } | strip > "$T/fresh"
[ "$(wc -l < "$T/fresh")" = 78 ]
cat out/gk.out out/sae.out out/sbe.out out/ports.out > "$T/frozen"
while IFS= read -r line; do grep -qxF -- "$line" "$T/frozen" || { echo "fresh line not in the frozen output: $line"; exit 1; }; done < "$T/fresh"
grep -q "^T109 gk 3 mode spec n 175 m 228 iterations 9 fallbacks 1 " "$T/fresh"
grep -q "^T109 gk 4 mode spec n 310 m 404 iterations 17 fallbacks 1 " "$T/fresh"
grep -q "^T109 sbe 4 mode nh n 110 m 250 iterations 286 " "$T/fresh"
sed 's/^T109 gk 4 mode rf n 310 m 404 iterations 6 /T109 gk 4 mode rf n 310 m 404 iterations 7 /' "$T/fresh" > "$T/bad"; ! cmp -s "$T/fresh" "$T/bad"
if ( while IFS= read -r line; do grep -qxF -- "$line" "$T/frozen" || exit 1; done < "$T/bad" ); then echo "control silent"; exit 1; fi
python3 "$TOP/experiments/hard-families/pgsolver_port.py" switchallexp 4 > "$T/s4.pg"
o=$(python3 rf109.py "$T/s4.pg" "$T/s4.sol"); grep -q "^RF n 63 m 143 iterations 27 switches 103 capped 0 maxsink 7 " <<<"$o"
grep -q "^T109 sae 4 mode rf n 63 m 143 iterations 27 fallbacks 0 switches 103 capped 0 wrong 0 badstrat 0$" out/sae.out
python3 "$TOP/experiments/harness/verify.py" "$T/s4.pg" "$T/s4.sol" > "$T/v.out" 2>&1 || { cat "$T/v.out"; exit 1; }
o=$(python3 rand109.py 7 300 16 rf); grep -q "^R109 mode rf seed 7 games 300 n<=16: wrong 0 badstrat 0 capped 0 " <<<"$o"
o=$(CTRL=1 python3 rand109.py 7 300 16 rf); grep -q "^R109 mode rf seed 7 games 300 n<=16 CTRL 1: wrong 300 " <<<"$o"
# Addendum A: the kill family K^s_n (rebuilt), n = 1..6: RF's count is 7 * 2^(n-1) - 2n - 3, RFA's is polynomial; fresh lines = frozen lines
python3 ks109.py 1 2 3 4 5 6 -- rf rfa howard > "$T/ks"
[ "$(wc -l < "$T/ks")" = 18 ]
while IFS= read -r line; do grep -qxF -- "$line" out/ks.out || { echo "fresh K^s line not in out/ks.out: $line"; exit 1; }; done < "$T/ks"
for n in 1 2 3 4 5 6; do grep -q "^KS109 n $n mode rf .* iterations $((7 * 2 ** (n - 1) - 2 * n - 3)) switches .* wrong 0 badstrat 0 " "$T/ks"; done
grep -q "^KS109 n 6 mode rfa |V| 127 |E| 236 iterations 25 " "$T/ks"
# Addendum A: decoyed switchallexp: RFA's count equals Howard's, RF's does not
python3 fam109.py table dsae 1 2 -- howard rfa rf --check | strip > "$T/dec"
[ "$(wc -l < "$T/dec")" = 6 ]
while IFS= read -r line; do grep -qxF -- "$line" out/decoy.out || { echo "fresh decoy line not in out/decoy.out: $line"; exit 1; }; done < "$T/dec"
grep -q "^T109 dsae 2 mode howard n 497 m [0-9]* iterations 30 " "$T/dec"; grep -q "^T109 dsae 2 mode rfa n 497 m [0-9]* iterations 30 " "$T/dec"
grep -q "^T109 dsae 2 mode rf n 497 m [0-9]* iterations 21 " "$T/dec"
echo "CHECK109 PASS"
