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
# L55 (Lead, 2026-11-13), narrowed by L56 after CHECKER 24's finding (CI skipped the self-checks: in the Actions checkout
# origin/<branch> IS the pushed commit). The self-checks are reported NOT RUN, with the tree ids, ONLY when: not in CI
# (GITHUB_ACTIONS unset), VERIFY_FULL != 1, the tree is clean, experiments/ and scripts/ equal origin/<branch>, every path
# changed since origin/<branch> is under docs/agents/, and no check script (*.sh, *.py, *.pins) under experiments/ mentions «docs/agents». Otherwise full run.
same_as_origin() { [ "${VERIFY_FULL:-0}" = 1 ] && return 1; [ -n "${GITHUB_ACTIONS:-}" ] && return 1
           local b; b="$(git branch --show-current 2>/dev/null)"; [ -n "$b" ] || return 1
           git rev-parse -q --verify "origin/$b" >/dev/null || return 1
           [ -z "$(git status --porcelain)" ] || return 1
           for d in experiments scripts; do
             [ "$(git rev-parse "HEAD:$d" 2>/dev/null)" = "$(git rev-parse "origin/$b:$d" 2>/dev/null)" ] || return 1; done
           local ch; ch="$(git diff --name-only "origin/$b" HEAD)" || return 1
           [ -n "$ch" ] || return 1
           ! printf '%s\n' "$ch" | grep -qv '^docs/agents/' || return 1
           ! grep -rqI --include=*.sh --include=*.py --include=*.pins 'docs/agents' experiments 2>/dev/null || return 1
           echo "only docs/agents/ changed since origin/$b; experiments/ and scripts/ trees equal ($(git rev-parse --short HEAD:experiments), $(git rev-parse --short HEAD:scripts)); CI runs the full suite (L55/L56)"; }
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
