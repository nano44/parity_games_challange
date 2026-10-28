#!/usr/bin/env bash
# L-NEW box 49 (successor 30): the named dressings of docs/new/N5-READER-box49.md §1-§2, rebuilt and compared (log out/dress_named.txt).
set -euo pipefail
cd "$(dirname "$0")"
B=../box48/instances/long121_n40; S=0,1,2,6,7,8,17,20,22,23,24,30,36,39
{
echo "== l121_a: Odd reader o (L-SI's l121reader_n41, rebuilt)";                  python3 -I dress.py $B.pg $B.start inst/l121_a "1:0:$S:0"
echo "== l121_b: + Even forced e -> o";                                            python3 -I dress.py $B.pg $B.start inst/l121_b "1:0:$S:0" "0:0:h0:h0"
echo "== l121_c: Even CHOICE e -> {o, e2}, e2 Even forced -> o, start e -> o";     python3 -I dress.py $B.pg $B.start inst/l121_c "1:0:$S:0" "0:0:h0,h2:h0" "0:0:h0:h0"
echo "== l121_d29: o with S ∪ succ(29), and an edge 29 -> o at the OLD Even vertex 29"
python3 -I dress.py $B.pg $B.start inst/l121_d29 "1:0:0,1,2,5,6,7,8,17,20,22,23,24,30,36,39:5" "EDGE:29:h0"
echo "== l121_e100: o <-> e (o -> S ∪ {e}, e Even forced -> o, priority 100): both new vertices have a predecessor"
python3 -I dress.py $B.pg $B.start inst/l121_e100 "1:0:$S,h1:0" "0:100:h0:h0"
echo "== l121_er19: Even reader e on S' (best of two hill climbs, search.py evenreader seeds 1, 2)"
python3 -I dress.py $B.pg $B.start inst/l121_er19 "0:0:6,8,17,19,25,27,34:6"
echo "== l121_er_6_19: Even reader on the most-flipping pair {6, 19} (22 order flips in the phase)"
python3 -I dress.py $B.pg $B.start inst/l121_er_6_19 "0:0:6,19:6"
} 2>&1
