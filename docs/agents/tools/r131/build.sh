#!/usr/bin/env bash
# build.sh: builds docs/agents/R131-draft.md and REPORT.txt from cfg.json. Reads ONLY cfg.json and fetch.txt (the
# record of fetch.sh) and git objects; it never fetches unless called as `bash build.sh --fetch`, which runs the
# clearly separate fetch.sh first. It starts from a clean state every time (out/, tmp/, REPORT.txt and the draft are
# removed first), writes nothing outside docs/agents/tools/r131/ and docs/agents/R131-draft.md, runs no git add /
# commit / merge / push, and exits non-zero if any check fails. Outputs of the checks are redirected to files and
# their exit codes read directly (no pipe hides one).
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(git -C "$HERE" rev-parse --show-toplevel)"
cd "$HERE" || exit 1
export PYTHONDONTWRITEBYTECODE=1
if [ "${1:-}" = "--fetch" ]; then
  bash fetch.sh > fetch.log 2>&1; rc=$?
  echo "fetch.sh rc $rc"; [ $rc -ne 0 ] && { echo "BUILD FAILED (fetch)"; exit 1; }
  rm -f fetch.log
fi
[ -f fetch.txt ] || { echo "BUILD FAILED: no fetch.txt (run: bash fetch.sh)"; exit 1; }
rm -rf out tmp REPORT.txt "$ROOT/docs/agents/R131-draft.md"
mkdir -p out tmp
fail=0
step() {
  name="$1"; shift
  "$@" > "out/$name.out" 2>&1; rc=$?
  last="$(tail -n 1 "out/$name.out")"
  echo "$name: rc $rc: ${last:0:150}"
  echo "$name rc $rc ${last:0:150}" >> out/steps.txt
  [ $rc -ne 0 ] && fail=1
  return 0
}
step lanecheck bash tools/lanecheck.sh
step fill python3 -B fill131.py
if [ ! -f out/draft.p1.md ]; then
  head -n 40 out/fill.out | cut -c1-300
  echo "BUILD FAILED: fill131.py wrote no draft"; rm -rf tmp; exit 1
fi
step upd python3 -B tools/upd.py
step data python3 -B tools/data.py
step prem python3 -B tools/prem.py
step shape python3 -B tools/shape.py out/draft.p1.md
step lp python3 -B tools/lp.py out/draft.p1.md
step sweep python3 -B tools/sweep.py out/draft.p1.md
step landtest python3 -B tools/landtest.py out/draft.p1.md
step mkadd python3 -B tools/mkadd.py
if [ -f "$ROOT/docs/agents/R131-draft.md" ]; then
  step post_shape python3 -B tools/shape.py "$ROOT/docs/agents/R131-draft.md"
  step post_lp python3 -B tools/lp.py "$ROOT/docs/agents/R131-draft.md"
  step post_sweep python3 -B tools/sweep.py "$ROOT/docs/agents/R131-draft.md"
  step post_landtest python3 -B tools/landtest.py "$ROOT/docs/agents/R131-draft.md"
else
  fail=1
fi
python3 -B tools/report.py "$fail" > REPORT.txt 2> out/report.err; rc=$?
[ $rc -ne 0 ] && { fail=1; echo "report.py rc $rc"; }
rm -rf tmp
if [ -f "$ROOT/docs/agents/R131-draft.md" ]; then
  echo "draft: docs/agents/R131-draft.md sha1 $(sha1sum < "$ROOT/docs/agents/R131-draft.md" | cut -d' ' -f1) lines $(wc -l < "$ROOT/docs/agents/R131-draft.md")"
fi
[ $fail -eq 0 ] && echo "BUILD PASS" || echo "BUILD FAILED"
exit $fail
