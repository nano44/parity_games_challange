#!/usr/bin/env bash
# Box 200 check (L-NEW successor 67): self200.py on CX4_n21, RWX_n95, C6G8_n54 and its four controls on CX4_n21; output must equal box200/check200.out.
set -u
cd "$(dirname "$0")"
{
  python3 -I self200.py inst/CX4_n21.json inst/RWX_n95.json inst/C6G8_n54.json
  for k in 1 2 3 4; do S200_CTRL=$k python3 -I self200.py inst/CX4_n21.json | sed "s/^/ctrl$k /"; done
}
