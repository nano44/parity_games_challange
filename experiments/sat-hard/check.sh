#!/usr/bin/env bash
# Fast self-check (< 2 min). Needs python-sat (pip install python-sat); cadical binary optional (apt install cadical).
set -euo pipefail
cd "$(dirname "$0")"
python3 -c "import pysat" 2>/dev/null || { echo "python-sat missing: pip install python-sat"; exit 1; }
timeout 110 python3 selfcheck.py
