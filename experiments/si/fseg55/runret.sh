#!/bin/bash
# L-SI box 55: NO-RET random / targeted search (retsearch.py), 3 biases x 3 sizes.
cd "$(dirname "$0")/../.."
D=/tmp/claude-0/-home-user-parity-games-challange/2da1fc23-6f5e-5512-95eb-3f9d4096c350/scratchpad/ret
for b in 0 1 2; do for nn in 8 12 16; do echo "$((100 * b + nn)) 100000 $nn 3 $b"; done; done | xargs -P 2 -L 1 bash -c 'timeout 3000 python3 -I si/fseg55/retsearch.py "$0" "$1" "$2" "$3" "$4" '"$D" > si/fseg55/ret_out.txt
