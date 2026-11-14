#!/usr/bin/env bash
# Box 198 check (L-NEW successor 65): pair198.py on NK6_cl21 and TC3, and its two controls; output must equal box198/check198.out.
set -u
cd "$(dirname "$0")"
{
  python3 -I pair198.py inst/NK6_cl21.json ../box196/inst_si85/TC3.json
  for k in 1 2; do P198_CTRL=$k python3 -I pair198.py inst/NK6_cl21.json | sed "s/^/ctrl$k /"; done
}
