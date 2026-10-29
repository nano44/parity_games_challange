#!/usr/bin/env bash
# The only sanctioned way to push (CLAUDE.md). Runs the gate and pushes the current branch only if it passes.
# Never pipe verify's output: a pipe replaces its exit code with the last command's.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
branch="$(git branch --show-current)"
# Push exactly the commit that was verified: a commit made while verify runs must not go out unverified.
sha="$(git rev-parse HEAD)"
log="$(mktemp)"
if scripts/verify.sh >"$log" 2>&1; then
  tail -6 "$log"
  now="$(git rev-parse HEAD)"
  [ "$now" = "$sha" ] || echo "push.sh: HEAD moved during verify ($sha -> $now); pushing the verified commit $sha only" >&2
  git push origin "$sha:refs/heads/$branch"
  git branch -u "origin/$branch" >/dev/null 2>&1 || true
else
  cat "$log"
  echo "push.sh: VERIFY FAILED, nothing pushed" >&2
  exit 1
fi
