#!/usr/bin/env bash
# L-RED self-check (run by scripts/verify.sh). Pins: gated_bland N=6 -> 63 MSF iterations (both the generator and the
# committed instance), the two Claim F counterexamples (1 escaped switch each), MSF == Bland correspondence N=2..6,
# and a small engine validation (brute force, Zielonka, verify.py).  ~20 s.
set -euo pipefail
cd "$(dirname "$0")"
t=$(mktemp -d); trap 'rm -rf "$t"' EXIT
python3 gens_red.py gated_bland 6 > "$t/g6.pg"
cmp -s "$t/g6.pg" instances/gated_bland_N6.pg || { echo "generator drifted from instances/gated_bland_N6.pg"; exit 1; }
out=$(python3 vj.py msf "$t/g6.pg" 2>&1 >"$t/g6.sol" | head -1)
[[ "$out" == "solved with 63 iterations,"* ]] || { echo "gated_bland 6: expected 63 iterations, got: $out"; exit 1; }
python3 ../harness/zielonka.py "$t/g6.pg" > "$t/g6.zlk"
python3 - "$t" <<'PY'
import sys; sys.path.insert(0, "../harness"); import pg, verify
t = sys.argv[1]; g = pg.read(f"{t}/g6.pg"); s = open(f"{t}/g6.sol").read()
assert pg.read_sol(s, g.n) == pg.read_sol(open(f"{t}/g6.zlk").read(), g.n), "regions differ from Zielonka"
e = verify.check(g, pg.read_sol(s, g.n), verify.read_strategy(s, g.n)); assert not e, e
PY
for f in claimF_len_cf1 claimF_bit_cf2; do
  out=$(python3 vj.py msf instances/$f.pg --start spec:2:1 2>&1 >/dev/null | head -1)
  [[ "$out" == "solved with 1 iterations,"*"escapes 1"* ]] || { echo "$f: expected 1 escaped switch, got: $out"; exit 1; }
done
TMPDIR="$t" python3 correspond.py 2 3 4 5 6 > "$t/corr.log" || { cat "$t/corr.log"; exit 1; }
python3 xcheck.py --games 150 --nmax 7 --seed 7 > "$t/x.log" || { cat "$t/x.log"; exit 1; }
echo "red check: gated_bland 6 = 63 MSF iterations (regions = Zielonka, strategies verified); Claim F instances; MSF == Bland N<=6; $(tail -1 "$t/x.log")"
