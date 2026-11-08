#!/usr/bin/env bash
# Box 197 check (L-NEW successor 65): a fixed subset of sweep197 (deep seed 1971 × 30, TC3, rd2_d9, the four controls); run from
# experiments/new; the output must equal box197/check197.out.
set -u
cd "$(dirname "$0")"
{
  python3 -I asc197.py deep 1971 30
  python3 -I asc197.py --files ../box196/inst_si85/TC3.json ../box192/inst/rd2_d9.json
  for k in 1 2 3; do A197_CTRL=$k python3 -I asc197.py deep 1973 30 | sed "s/^/ctrl$k /"; done
  A197_CTRL=4 python3 -I asc197.py --files ../box196/inst_si85/TC3.json | sed "s/^/ctrl4 /"
}
