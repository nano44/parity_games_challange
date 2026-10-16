#!/usr/bin/env bash
# The only sanctioned way to push (CLAUDE.md). Runs the gate and pushes the current branch only if it passes.
# Never pipe verify's output: a pipe replaces its exit code with the last command's.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
branch="$(git branch --show-current)"
log="$(mktemp)"
if scripts/verify.sh >"$log" 2>&1; then
  tail -6 "$log"
  git push -u origin "$branch"
else
  cat "$log"
  echo "push.sh: VERIFY FAILED, nothing pushed" >&2
  exit 1
fi
