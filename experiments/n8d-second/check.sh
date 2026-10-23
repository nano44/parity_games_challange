#!/usr/bin/env bash
# Fast self-check of the N8d second implementation (run by scripts/verify.sh via experiments/*/check.sh).
set -e
cd "$(dirname "$0")"
python3 selfcheck.py 300 9
