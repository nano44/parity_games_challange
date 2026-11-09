#!/usr/bin/env bash
# Box 203 check (L-NEW successor 68): gfc203.py (GATE-CLASS / GATE-FLIP / QUIET-N counters on IDEAL-CYC) on MWR4_2, MWR8_2, k1fail_202,
# C4_NM50, its three controls on MWR4_2, and rnd203.py on 100 random + 100 k = 1 genomes; part 2: asc203.py on the staircases ST4, ST8
# (the DEAD-ascent witness: ST8 maxasc 7 at k 1) and MWR4_2, lam203.py ((k+1)-Lambda) on ST8, MWR4_2, MW4_2, 100 k = 1 genomes and
# its control; output must equal box203/check203.out.
set -u
cd "$(dirname "$0")"
{
  python3 -I gfc203.py inst/MWR4_2.json inst/MWR8_2.json ../box202/k1fail_202.json ../box202/inst/C4_NM50_184a739c.json
  for k in 1 2 3; do GFC_CTRL=$k python3 -I gfc203.py inst/MWR4_2.json | sed "s/^/ctrl$k /"; done
  python3 -I rnd203.py rand 2 100
  python3 -I rnd203.py k1 202 100
  python3 -I asc203.py inst/ST4_k1.json inst/ST8_k1.json inst/MWR4_2.json
  python3 -I lam203.py inst/ST8_k1.json inst/MWR4_2.json ../box202/inst/MW4_2.json
  python3 -I lam203.py --rand k1 7 100
  LAM_CTRL=1 python3 -I lam203.py --rand k1 7 100 | sed "s/^/ctrl4 /"
}
