#!/usr/bin/env bash
# L-SI box 108 self-check (deterministic, about 45 s) for docs/si/box108-gk-proof.md (Theorem GK: L(G_k) = 2^k - 2 on R104's IDEAL model):
# 1. check108.py on G_3..G_12 (four sha1; run length and stop; closed form; latch form; static lemmas on run states and random states;
#    one bit per level; switch counts; one table row per phase class): fresh output = frozen out/check108.out;
# 2. the 32 table rows of §5 of the proof file equal the generated rows, line by line; the hand tables of §3-§4, parsed out of the
#    proof file, equal the observed signals (counter DOC), with a control (one wrong Q must be reported);
# 3. the R104 quotes of the proof file occur in docs/red/P-N5-REALIZE.md (quotes108.py), with a control;
# 4. the 19 controls fire as frozen (out/ctrl108.out);
# 5. L-NEW's one217.OneP (claude/l-new a143d4060) gives the same state sequences for k = 3..10 (out/one217.out);
# 6. the abstract latch network (abs108.py) equals the closed form for k = 3..11 (out/abs108.out). k = 12..17 of out/abs108_long.out
#    are frozen lines, not re-run here (about 4 minutes).
set -eu
cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
TOP=${TOP:-$(git rev-parse --show-toplevel)}; DOC=${DOC:-"$TOP/docs/si/box108-gk-proof.md"}
python3 check108.py 3 12 --table --doc "$DOC" > "$T/c.out"
cmp "$T/c.out" out/check108.out
grep -q "^CHECK108 PASS k 3..12 rand 200$" out/check108.out
grep -q "^TABLE classes 32 multi-row 0 missing 0 unexpected 0$" out/check108.out
grep -q "^DOC positions 23 doc-positions 23 fails DOC=0$" out/check108.out
[ "$(grep -c " fails SHA=0 RUN=0 CLOSED=0 LATCH=0 STATIC=0 SIG=0 SW=0$" out/check108.out)" = 10 ]
grep -E "^(bot|mid|top) [AST]" "$T/c.out" > "$T/rows"
[ "$(wc -l < "$T/rows")" = 32 ]
while IFS= read -r line; do grep -qxF -- "$line" "$DOC" || { echo "table row missing in the doc: $line"; exit 1; }; done < "$T/rows"
[ "$(grep -cE "^(bot|mid|top) [AST]" "$DOC")" = 32 ]
sed 's/^| 3h+1 | S9 | 1 0 0 1 1 0 1 | yb |/| 3h+1 | S9 | 1 0 0 1 1 0 1 | y |/' "$DOC" > "$T/bad.md"; ! cmp -s "$DOC" "$T/bad.md"
if python3 check108.py 3 5 --rand 0 --doc "$T/bad.md" > "$T/d.out"; then echo "DOC control silent"; exit 1; fi
grep -q "^DOC mismatch at S9 " "$T/d.out"
python3 quotes108.py "$DOC" "$TOP/docs/red/P-N5-REALIZE.md" > "$T/q.out"; cmp "$T/q.out" out/quotes108.out
grep -q "^QUOTES108 quotes 13 pieces 22 fail 0$" out/quotes108.out
if QUOTES108_CTRL=1 python3 quotes108.py "$DOC" "$TOP/docs/red/P-N5-REALIZE.md" > /dev/null; then echo "quote control silent"; exit 1; fi
CTRLS="H-off eps-wv eps-wu eps-uv eps-v0 dl-y dl-y2 dl-yp dl-yp2 dl-uv dl-uvtop dl-v0 dl-u0 dl-w dep-yb start-yb start-ypb form-kmin-yp form-Q"
for c in $CTRLS; do python3 check108.py 4 6 --rand 50 --ctrl "$c"; done > "$T/k.out"
cmp "$T/k.out" out/ctrl108.out
[ "$(grep -c ": fired on 3 of 3 k " out/ctrl108.out)" = 19 ]
git -C "$TOP" archive a143d4060 experiments/new/box217/one217.py | tar -x -C "$T"
[ "$(sha1sum < "$T/experiments/new/box217/one217.py" | cut -c1-40)" = "$(cat "$TOP/experiments/si/box107/one217.sha1")" ]
python3 -I -B replay108.py "$T/experiments/new/box217" 3 10 > "$T/r.out"
cmp "$T/r.out" out/one217.out
grep -q "^REPLAY108 PASS$" out/one217.out
python3 abs108.py 3 11 > "$T/a.out"; cmp "$T/a.out" out/abs108.out
[ "$(grep -c " closed_form_mismatches 0$" out/abs108.out)" = 9 ]
[ "$(grep -c " closed_form_mismatches 0$" out/abs108_long.out)" = 6 ]
echo "check108: PASS"
