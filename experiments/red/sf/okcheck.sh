#!/bin/bash
# L-RED: correctness check of sf2.py on a game: sf2 regions == Oink zlk regions (tl if zlk aborts), and sf2's strategies pass
# experiments/harness/verify.py. Usage: okcheck.sh GAME.pg   prints "OK n" or "FAIL ...".
G=$1; T=$(mktemp -d); R=$(cd "$(dirname "$0")/../../.." && pwd)
python3 "$R/experiments/red/sf/sf2.py" "$G" --sol "$T/sf.sol" > "$T/sf.out" || { echo "FAIL sf2"; exit 1; }
"$R/tools/oink/build/oink" --zlk "$G" "$T/ok.sol" > /dev/null 2>&1 || "$R/tools/oink/build/oink" --tl "$G" "$T/ok.sol" > /dev/null 2>&1 || { echo "FAIL oink"; exit 1; }
python3 -c "
import sys; sys.path.insert(0, '$R/experiments/harness'); import pg
g = pg.read('$G'); a = pg.read_sol(open('$T/sf.sol').read(), g.n); b = pg.read_sol(open('$T/ok.sol').read(), g.n)
d = [v for v in range(g.n) if a[v] != b[v]]
print('REGIONS', 'OK' if not d else 'DIFF %s' % d[:10])"
python3 "$R/experiments/harness/verify.py" "$G" "$T/sf.sol" 2>&1 | tail -1
cat "$T/sf.out"; rm -rf "$T"
