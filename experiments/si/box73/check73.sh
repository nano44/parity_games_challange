#!/usr/bin/env bash
# L-SI box 73 self-check (~60 s): the m = 2 frame tables (pinned) give the frame maxima and Theorem FRONT-2' (max post = min(b, 5 - pre)
# in every (T_0^pre-bit, T_0^post-bit) = (a, b) cell, except (a, b, pre) = (4, 2, 3): post 1); the realised m = 3 genome pq_8_1 replays with L-NEW's Gen (pre 8, post 1) and
# flipdp gives T_0, T_1 = 8, 9; frame pq mode m = 2 controls (needs python-sat; skipped without it).
set -euo pipefail
cd "$(dirname "$0")"
sha1sum -c --quiet pins.sha1
t=$(mktemp -d)
python3 -I dyn2.py > "$t/dyn2"
diff -q "$t/dyn2" dyn2.out
python3 -I mine2.py > "$t/mine2"
diff -q "$t/mine2" mine2.out
rm -rf "$t"
python3 -I - <<'PY'
import re, ast
def front(cap):
    bad = 0
    for l in open('mine2.out'):
        a, b = map(int, re.findall(r'bit\) (\d+)', l)); d = ast.literal_eval(l.split('by pre ')[1].strip())
        bad += sum(1 for p, q in d.items() if q != min(b, cap - p) - ((a, b, p) == (4, 2, 3)))   # the one sub-cap junction loss
    return bad
assert front(5) == 0, "FRONT-2' fails"
assert front(6) > 0, "negative control did not fire"
PY
for g in out/pq_8_1_m3_s1.json out/pq_4_6_m3_s1.json out/pq_7_2_m3_s2.json; do python3 -I replaypq.py "$g" > /dev/null; done
python3 -I - <<'PY'
import sys, json; sys.path.insert(0, '../box64'); from flipdp import analyse
r = analyse(json.load(open('out/pq_8_1_m3_s1.json')), K=1); assert r['T'] == [8, 9] and not r['bad'], r
r = analyse(json.load(open('out/pq_7_2_m3_s2.json')), K=1); assert r['T'] == [7, 9] and not r['bad'], r
r = analyse(json.load(open('out/pq_4_6_m3_s1.json')), K=1); assert r['T'][1] == 10 and not r['bad'], r
PY
echo "box 73 FRONT-2' + pq_8_1 pin: PASS"
python3 -I -c "import pysat" 2>/dev/null || { echo "box 73: python-sat missing, frame controls skipped"; exit 0; }
r() { local o; o=$(PRE=$1 python3 -I ../box70/frame.py 2 pq 1 $2); printf '%s\n' "$o" | grep -o -- "-> [A-Z]*" | head -n 1; }
[ "$(r 2 5)" = "-> SAT" ]; [ "$(r 3 6)" = "-> UNSAT" ]; [ "$(r 4 5)" = "-> SAT" ]; [ "$(r 4 6)" = "-> UNSAT" ]
echo "box 73 frame pq controls: PASS"
