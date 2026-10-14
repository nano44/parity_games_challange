#!/usr/bin/env bash
# Fast self-check (< 2 min) run by scripts/verify.sh.  Needs python-sat (pip install python-sat).
set -euo pipefail
cd "$(dirname "$0")"
python3 -c "import pysat" 2>/dev/null || { echo "python-sat missing: pip install python-sat"; exit 1; }
python3 selfcheck.py
