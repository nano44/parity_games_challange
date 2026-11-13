#!/usr/bin/env bash
# The gate. Every step prints PASS, FAILED or NOT RUN; exit 1 if any step FAILED.
# Usage: scripts/verify.sh   (from anywhere). Push only if it passes: scripts/verify.sh && git push -u origin <branch>
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; cd "$ROOT"
declare -a RES=(); FAIL=0
step() { local name="$1"; shift; echo "== $name"; local out; out="$("$@" 2>&1)"; local rc=$?
  if [ $rc -eq 0 ]; then RES+=("PASS     $name"); elif [ $rc -eq 77 ]; then RES+=("NOT RUN  $name ($out)"); out="";
  else RES+=("FAILED   $name"); FAIL=1; fi; [ -n "$out" ] && echo "$out" | tail -40; }

docs()   { python3 scripts/check_docs.py; }
lean()   { ls lean/lakefile.* >/dev/null 2>&1 || { echo "no lean/lakefile"; return 77; }
           command -v lake >/dev/null || { echo "lake not installed"; return 1; }
           (cd lean && lake build) || return 1
           if grep -rnw --include=*.lean -e sorry -e admit lean --exclude-dir=.lake; then echo "sorry/admit found"; return 1; fi
           if [ -f lean/Axioms.lean ]; then
             (cd lean && lake env lean Axioms.lean) | grep -o "\[.*\]" | tr -d '[]' | tr ',' '\n' | sed 's/ //g' | grep -v '^$' \
               | grep -vxE 'propext|Classical.choice|Quot.sound' && { echo "disallowed axiom"; return 1; }
           fi; return 0; }
# L55 (Lead, 2026-11-13): container restarts kill 60-min runs. If experiments/ and scripts/ are byte-identical (same git tree)
# to origin/<branch>, which was pushed through this gate and whose CI re-runs the full suite, the self-checks are reported
# NOT RUN with the tree ids; CI (.github/workflows/verify.yml) stays the full run of record. Any change there, a dirty tree,
# a missing origin branch or VERIFY_FULL=1 forces the full run.
same_as_origin() { [ "${VERIFY_FULL:-0}" = 1 ] && return 1
           local b; b="$(git branch --show-current 2>/dev/null)"; [ -n "$b" ] || return 1
           git rev-parse -q --verify "origin/$b" >/dev/null || return 1
           [ -z "$(git status --porcelain -- experiments scripts)" ] || return 1
           for d in experiments scripts; do
             [ "$(git rev-parse "HEAD:$d" 2>/dev/null)" = "$(git rev-parse "origin/$b:$d" 2>/dev/null)" ] || return 1; done
           echo "experiments/ and scripts/ trees equal origin/$b ($(git rev-parse --short HEAD:experiments), $(git rev-parse --short HEAD:scripts)); full run is CI's (L55)"; }
exps()   { same_as_origin && return 77
           local n=0; for c in experiments/*/check.sh; do [ -f "$c" ] || continue; n=$((n+1)); echo "-- $c"; bash "$c" || return 1; done
           [ $n -gt 0 ] || { echo "no experiments/*/check.sh"; return 77; }; }
oink()   { local b=tools/oink/build; [ -x $b/oink ] || { echo "Oink not built; run scripts/setup_oink.sh"; return 77; }
           local g; g="$(mktemp)"; $b/tc 6 > "$g" && $b/oink --zlk -v "$g" 2>&1 | grep -q "solution verified"; local r=$?; rm -f "$g"; return $r; }

step "doc shape (scripts/check_docs.py)" docs
step "lean build, no sorry, allowed axioms" lean
step "experiment self-checks (experiments/*/check.sh)" exps
step "oink smoke (tc 6, zlk, verified)" oink
echo; echo "== verify summary"; printf '%s\n' "${RES[@]}"
[ $FAIL -eq 0 ] && echo "VERIFY PASS" || echo "VERIFY FAILED"
exit $FAIL
