#!/usr/bin/env bash
# L-RED box 16 (produced on Opus 5.5): check a NEST* candidate. sha1; both order data through L-ALG's unmodified b12_pot.run/chain
# + b12_core.states (via ../xctx/nestclass.py positions); NEST* (../xctx/comb/neststar.py); pinned Oink A_DTL with --verify
# (iteration counts per parity, to compare with the Python q-phase lengths).
cd "$(dirname "$0")"; OINK=../../../tools/oink/build/oink
for f in "$@"; do
  echo "== $f sha1 $(sha1sum "$f" | cut -c1-40)"
  for o in stable oink; do DTL_ORDER=$o python3 starclimb.py "$f"; done
  "$OINK" --dtl --no-single --no-wcwc --no-loops -v "$f" 2>&1 | grep -E "found|solved in|iterations:|verified|ERROR|error" | sed 's/^\[ *[0-9.]*\] /  oink: /'
done
