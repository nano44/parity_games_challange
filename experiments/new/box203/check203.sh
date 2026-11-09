#!/usr/bin/env bash
# Box 203 check (L-NEW successor 68): gfc203.py (GATE-CLASS / GATE-FLIP / QUIET-N counters on IDEAL-CYC) on MWR4_2, MWR8_2, k1fail_202,
# C4_NM50, its three controls on MWR4_2, and rnd203.py on 100 random + 100 k = 1 genomes; output must equal box203/check203.out.
set -u
cd "$(dirname "$0")"
{
  python3 -I gfc203.py inst/MWR4_2.json inst/MWR8_2.json ../box202/k1fail_202.json ../box202/inst/C4_NM50_184a739c.json
  for k in 1 2 3; do GFC_CTRL=$k python3 -I gfc203.py inst/MWR4_2.json | sed "s/^/ctrl$k /"; done
  python3 -I rnd203.py rand 2 100
  python3 -I rnd203.py k1 202 100
}
