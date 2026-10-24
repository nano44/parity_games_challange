#!/bin/bash
# L-RED box 24 (produced on Opus 5.5): HL_k = R53's H_k (experiments/red/kl/famgen.py H k) with a z-separated delay lane of length
# L7 on node 7 (open at start, inward target 3) and one of length L8 on node 8 (closed at start, inward target 1), z priority 23,
# lane priority 1 (R56 §2). Usage: hlgen.sh k [L7 [L8]] > out.pg   (defaults L7 = 8, L8 = 4)
set -e
D=$(cd "$(dirname "$0")" && pwd); k=$1; L7=${2:-8}; L8=${3:-4}
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
python3 "$D/../kl/famgen.py" H "$k" > "$T/h.pg"
python3 "$D/lanegen.py" "$T/h.pg" 7 "$L7" 23 > "$T/h7.pg"
python3 "$D/lanegen.py" "$T/h7.pg" 8 "$L8" 23 1 1 closed
