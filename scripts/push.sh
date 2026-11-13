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
  # A push counts only when origin shows the verified commit: git push has been seen to print
  # "RPC failed; HTTP 503" and still let this script exit 0 (L-COMP 22, 2026-11-13). Retry, then fail loudly.
  ok=0
  for attempt in 1 2 3 4; do
    if git push origin "$sha:refs/heads/$branch"; then
      remote="$(git ls-remote origin "refs/heads/$branch" 2>/dev/null | cut -f1 || true)"
      if [ "$remote" = "$sha" ]; then ok=1; break; fi
      echo "push.sh: git push returned 0 but origin/$branch is ${remote:-missing}, not $sha (attempt $attempt)" >&2
    else
      echo "push.sh: git push failed (attempt $attempt)" >&2
    fi
    sleep $((attempt * 15))
  done
  if [ "$ok" != 1 ]; then
    echo "push.sh: PUSH FAILED after VERIFY PASS: origin/$branch is not $sha" >&2
    exit 2
  fi
  echo "push.sh: origin/$branch = $sha (checked with git ls-remote)"
  git branch -u "origin/$branch" >/dev/null 2>&1 || true
else
  cat "$log"
  echo "push.sh: VERIFY FAILED, nothing pushed" >&2
  exit 1
fi
