#!/usr/bin/env bash
# Box 204 check (L-NEW successor 68): k1eq204.py (Lemma FACE-TARGET counters wfail / dfail / bfail on IDEAL-CYC) on MWR4_2, K1F21_n48,
# k1fail_202, its two controls on MWR4_2, and 100 random k = 1 genomes; output must equal box204/check204.out.
set -u
cd "$(dirname "$0")"
{
  python3 -I k1eq204.py ../box203/inst/MWR4_2.json ../box203/inst/K1F21_n48.json ../box202/k1fail_202.json
  for k in 1 2; do K1EQ_CTRL=$k python3 -I k1eq204.py ../box203/inst/MWR4_2.json | sed "s/^/ctrl$k /"; done
  python3 -I k1eq204.py --rand k1 7 100
}
