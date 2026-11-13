#!/bin/bash
# Box 216 worker C (resumable): DATA (vi), gate216 in modes idx and seq (other improving rules) on the frozen set.
cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1
G216_MODE=idx bash run216.sh out/gate_frozen_idx.out python3 -I gate216.py
G216_MODE=seq bash run216.sh out/gate_frozen_seq.out python3 -I gate216.py
