#!/usr/bin/env bash
# L-SI box 109 (design day 2026-11-14): regenerates every table of docs/si/box109-design.md into out/ (about 12 minutes, one core).
# External trees (read-only, by git archive; fetch the two branches first): claude/l-lit 5c53efbd (T66's transcription of Friedmann's
# G_n) and claude/l-red-b 10dfedb6 (gk.py, for the «gkeq» comparison only). Everything else is read from this repository.
set -eu
cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1
TOP=${TOP:-$(git -C "${ROOT109:-.}" rev-parse --show-toplevel)}
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT; mkdir -p out "$T/lit" "$T/redb"
git -C "$TOP" archive 5c53efbd2d8401dc056e575fa42e49b50a265a0c docs/lit/T66-depth-check.py | tar -x -C "$T/lit"
git -C "$TOP" archive 10dfedb6574c9291011a5a7fbbdff261fe312d91 experiments/red-b | tar -x -C "$T/redb"
export LLIT="$T/lit" REDB="$T/redb"
strip() { sed -E 's/ secs [0-9.]+$//'; }                      # timings are not frozen
python3 fam109.py gkeq 3 4 5 6 7 8 9 10 11 12 > out/gkeq.out
python3 fam109.py table gk 3 4 5 6 7 8 9 10 11 12 -- xi h1 h3 howard h4 nh rf rf2 --check | strip > out/gk.out
python3 fam109.py table gk 3 4 5 6 7 8 -- spec --check | strip >> out/gk.out
python3 fam109.py table wl 1 2 3 4 5 6 7 8 -- spec h1 h3 howard h4 nh rf rf2 --check | strip > out/wl.out
python3 fam109.py table wl 1 2 3 4 5 6 -- xi --check | strip >> out/wl.out
python3 fam109.py table du 3 4 5 6 7 -- spec xi h1 h3 howard h4 nh rf rf2 --check | strip > out/du.out
python3 fam109.py table fr 1 2 3 4 5 6 7 8 -- spec xi h1 h3 howard h4 nh rf rf2 --check | strip > out/fr.out
python3 fam109.py table fr 9 10 12 14 16 -- spec nh rf rf2 --check | strip >> out/fr.out
python3 fam109.py table sae 1 2 3 4 5 6 7 8 -- spec xi h1 h3 howard h4 nh rf rf2 --check | strip > out/sae.out
python3 fam109.py table sae 9 10 12 14 16 -- spec nh rf rf2 --check | strip >> out/sae.out
python3 fam109.py table sbe 1 2 3 4 5 6 7 -- spec xi h1 h3 howard h4 nh rf rf2 --check | strip > out/sbe.out
python3 fam109.py table sbe 8 9 10 12 14 -- spec rf rf2 --check | strip >> out/sbe.out
for f in rfs zad cun dlb; do python3 fam109.py table $f 2 3 4 5 6 7 8 -- howard rf rf2 --check | strip; done > out/ports.out
{ python3 fam109.py sinks fr 2 4 6 8 12 16; python3 fam109.py sinks sae 4 8 12 16; python3 fam109.py sinks sbe 4 8 12; python3 fam109.py sinks gk 4 8 12; python3 fam109.py sinks wl 4 8; } > out/sinks.out
python3 rand109.py 109 10000 40 rf rf2 nh h3 h4 h1 howard > out/rand.out
CTRL=1 python3 rand109.py 109 100 12 rf > out/rand_ctrl.out
echo DONE
# Not re-run here (minutes to an hour each; outputs frozen in out/climb.out, out/climb_rf_10.json, out/starts.out, out/famsearch.out):
#   for N in 6 7 8 9 10 12; do python3 climb109.py rf $N 7 8 30000; done;  python3 climb109.py rf 16 1 6 4000
#   ONEP=1 python3 climb109.py rf 8 7 8 30000;  ONEP=1 python3 climb109.py rf 12 7 8 30000;  python3 climb109.py howard 12 1 6 4000
#   python3 starts109.py fr 6 200 5;  python3 starts109.py sae 6 200 5;  python3 starts109.py sbe 4 200 5        (need LLIT for fr)
#   python3 famrf109.py --G 4 --K 6 --restarts 12 --steps 1200 --seed 1;  python3 famrf109.py --G 3 --K 7 --restarts 16 --steps 1500 --seed 2 --desc
# Addendum A (frozen in out/ks.out, stale.out, decoy.out, variants.out, rand_variants.out, m1.out, gate.out, gbland.out, bits.out, union.out):
#   python3 ks109.py 1 2 3 4 5 6 7 8 -- rf howard rfp rfa rfa1 rfr rfd spec nh; python3 ks109.py 9 10 12 -- rfa rfr; python3 ks109.py 2 3 4 5 6 --noskip -- rf
#   python3 stale109.py 2 3 4 5 6 7;  python3 fam109.py table dsae 1 2 3 4 5 -- howard rf rfa rfa1 rfr --check  (rfd: 1..4);  dfr 1..4 the same (rfd: 1..5)
#   python3 fam109.py table {gk,wl,fr,sae,sbe} .. -- rfa rfr [rfp] --check;  python3 rand109.py 109 10000 40 rfa rfr rfd
#   python3 m1_109.py FAMILY N.. -- rf --secs 200 (Oink built);  python3 gate109.py FAMILY N DEPTH MODE [--order ..];  python3 gate109.py bland N..;  python3 bits109.py n..
