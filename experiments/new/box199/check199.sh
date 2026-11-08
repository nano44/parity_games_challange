#!/usr/bin/env bash
# Box 199 check (L-NEW successor 66): split199.py on CX4_n21, GROW7_n34, NK6_cl21, ROUTELOW_n21 and its six controls on CX4_n21; output must equal box199/check199.out.
set -u
cd "$(dirname "$0")"
{
  python3 -I split199.py inst/CX4_n21.json inst/GROW7_n34.json inst/NK6_cl21.json inst/ROUTELOW_n21.json
  for k in 1 2 3 4 5 6; do S199_CTRL=$k python3 -I split199.py inst/CX4_n21.json | sed "s/^/ctrl$k /"; done
}
