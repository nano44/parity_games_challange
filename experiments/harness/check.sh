#!/usr/bin/env bash
# Harness self-test (< 2 min, deterministic). Run by scripts/verify.sh.
set -euo pipefail
cd "$(dirname "$0")"
timeout 110 python3 -I selftest.py
