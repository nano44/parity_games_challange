#!/usr/bin/env bash
# tools/lanecheck.sh: the lane's own self-check (experiments/red-b/check.sh) in a git archive of the l-red-b commit
# of cfg.json, with one negative control (one byte appended to the pinned out/n5_k13.out). Works only under
# docs/agents/tools/r131/tmp/ (removed afterwards). Deterministic output on stdout; exit 1 if the check does not
# pass or the control does not fire. Nothing of the repository is touched.
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ROOT="$(git -C "$HERE" rev-parse --show-toplevel)"
C="$(python3 -B -c "import json,sys; print(json.load(open(sys.argv[1],encoding='utf-8'))['heads']['l-red-b'])" "$HERE/cfg.json")"
A="$HERE/tmp/arch"
rm -rf "$A"; mkdir -p "$A"
git -C "$ROOT" archive "$C" experiments/red-b docs/red-b experiments/new/box203/inst | tar -x -C "$A"
n=$(find "$A" -type f | wc -l)
echo "archive of claude/l-red-b ${C:0:8}: experiments/red-b, docs/red-b, experiments/new/box203/inst: $n files"
fail=0
( cd "$A/experiments/red-b" && bash check.sh > "$A/check.out" 2>&1 ); rc=$?
last="$(tail -n 1 "$A/check.out")"
echo "check.sh: rc $rc ; last line: $last"
{ [ $rc -eq 0 ] && [ "$last" = "red-b check PASS" ]; } || fail=1
P="$A/experiments/red-b/data/b6b/out/n5_k13.out"
cp "$P" "$A/n5_k13.keep"; printf 'x' >> "$P"
( cd "$A/experiments/red-b" && bash check.sh > "$A/check_neg.out" 2>&1 ); rcn=$?
lastn="$(tail -n 1 "$A/check_neg.out")"
msg="$(grep -c 'red-b: data/b6b fixes3 SHA1SUMS mismatch' "$A/check_neg.out")"
echo "negative control (one byte appended to data/b6b/out/n5_k13.out): rc $rcn ; mismatch line printed $msg ; last line: $lastn"
{ [ "$lastn" = "red-b check FAILED" ] && [ "$msg" -ge 1 ]; } || fail=1
cp "$A/n5_k13.keep" "$P"
( cd "$A/experiments/red-b" && bash check.sh > "$A/check2.out" 2>&1 ); rc2=$?
echo "restored: rc $rc2 ; last line: $(tail -n 1 "$A/check2.out")"
[ $rc2 -eq 0 ] || fail=1
rm -rf "$A"
[ $fail -eq 0 ] && echo "lanecheck: PASS" || echo "lanecheck: FAILED"
exit $fail
