#!/bin/bash
# Box 216 worker A (resumable): V2/V3 xflip216 and V1 gate216 (N5 spec mode) on the frozen set; then gate216 in xi mode (reference).
cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1
bash run216.sh out/xflip_frozen.out python3 -I xflip216.py
G216_MODE=spec bash run216.sh out/gate_frozen_spec.out python3 -I gate216.py
G216_MODE=xi bash run216.sh out/gate_frozen_xi.out python3 -I gate216.py
