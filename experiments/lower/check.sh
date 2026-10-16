#!/usr/bin/env bash
# L-LOWER fast regression (< 2 min, deterministic). Run by scripts/verify.sh.
# 1. evaluator: unfolded Büchi SLP and ANP's symmetric SLP agree with Zielonka on all games with n <= 3;
# 2. exact minima on the bisimulation quotient: B_1(2) = 2, B_1(3) = 4 (SAT), and the minimal depth 2n-2 for n <= 3;
# 3. the vectorized n=5 reference agrees with Zielonka on all one-player Büchi games with <= 3 vertices.
set -euo pipefail
cd "$(dirname "$0")"
python3 -c "import pysat" 2>/dev/null || { echo "python-sat not installed (pip install python-sat); SAT checks skipped"; SKIP=1; }
timeout 110 python3 -I - <<'PY'
import sys; sys.path.insert(0, "../harness"); sys.path.insert(0, ".")
import numpy as np, zielonka
from slp import buchi_unfold, anp_symmetric, eval_struct, cost
from games import iter_raw, to_game, pack
from quotient import build
from depthneeded import depth_needed
import vec5
def run(prog, n, prios, owners):
    raws = [r for k in range(1, n + 1) for r in iter_raw(k, prios, owners)]
    S, off = pack(raws); out = eval_struct(prog, S)
    ref = np.concatenate([np.array(zielonka.solve(to_game(r))) == 0 for r in raws])
    assert (out == ref).all(), "mismatch"; return len(raws)
print("buchi_unfold(3) == Zielonka on", run(buchi_unfold(3), 3, (1, 2), (0, 1)), "games (n<=3, two-player)")
print("anp_symmetric(3,2) == Zielonka on", run(anp_symmetric(3, 2), 3, (0, 1, 2), (0, 1)), "games (n<=3, priorities 0..2)")
for n, d in ((1, 0), (2, 2), (3, 4)):
    q = build(n); assert depth_needed(q) == d, (n, depth_needed(q)); print(f"minimal depth for n={n}: {d} (= 2n-2)")
try:
    import satsearch
    for n, b in ((2, 2), (3, 4)):
        q = build(n); k, prog = satsearch.minimum(q, kmax=b, verbose=False)
        assert k == b and (eval_struct(prog, q.S) == q.W).all(), (n, k); print(f"B_1({n}) = {b} (SAT, witness verified on Q_{n})")
except ImportError:
    print("python-sat missing: B_1 checks skipped")
for k in (1, 2, 3):
    S = vec5.all_succ(k)
    for pm in range(2 ** k):
        W = vec5.ref_W(S, pm, k); prio = [2 if (pm >> v) & 1 else 1 for v in range(k)]
        for gi in range(len(S)):
            succ = [[w for w in range(k) if (S[gi, v] >> w) & 1] for v in range(k)]
            z = zielonka.solve(__import__("pg").Game(prio, [0] * k, succ))
            assert sum(1 << v for v in range(k) if z[v] == 0) == W[gi]
print("vec5.ref_W == Zielonka on all one-player Büchi games with k <= 3 vertices")
print("L-LOWER CHECK PASS")
PY
