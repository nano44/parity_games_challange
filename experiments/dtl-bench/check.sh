#!/usr/bin/env bash
# DTL bench self-check (< 1 min; run by scripts/verify.sh). prints SKIPPED and exits 0 if Oink is not built (CI has no Oink).
# 1. pinned DTL and IDTL agree with brute force + py-zlk, strategies verified, on all 324 games n=2, P=2;
# 2. a planted region flip is reported MISMATCH and a planted losing strategy BADSTRAT by the bench's judge.
set -euo pipefail
cd "$(dirname "$0")"
[ -x ../../tools/oink/build/oink ] || { echo "DTL-BENCH CHECK SKIPPED: Oink not built (scripts/setup_oink.sh)"; exit 0; }
T="$(mktemp -d)"; trap 'rm -rf "$T"' EXIT
python3 bench.py exhaustive 2 2 --csv "$T/x.csv" --jobs 2 | tail -1
python3 - "$T" <<'PY'
import sys, os, glob
sys.path.insert(0, "."); sys.path.insert(0, "../harness")
import bench
bench.FAILDIR = os.path.join(sys.argv[1], "fail")
games = sorted(glob.glob("../alg/instances/dtl_proof_c*.pg"))
for kind, want in (("region", "MISMATCH"), ("strategy", "BADSTRAT")):
    bench.PIN = {kind: ["python3", "plant.py", kind, "{in}", "{out}"]}
    sts = [r["status"] for gp in games for r in bench.one((gp, 30, 400, None, None)) if r["solver"] == kind]
    # region: every game; strategy: only games with a losing deviation (the rest stay ok, never MISMATCH)
    assert sts.count(want) >= (len(games) if kind == "region" else 1) and set(sts) <= {want, "ok"}, (kind, sts)
    print(f"planted {kind} defect reported as {want} on {sts.count(want)}/{len(games)} games")
PY
echo "DTL-BENCH CHECK PASS"
