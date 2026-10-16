#!/usr/bin/env python3
"""L-ALG (produced on Opus 5.5, 2026-10-16): reproduces the violation of fixed-context monotonicity (M) (= Claim P, = the
first-call distance monotonicity of GAP-A-data F5) in an ACTUAL A_DTL run (docs/alg/GAP-A-M.md §4b).
Instance experiments/alg/instances/dtl_mviol_n20.pg (vertex ids already in Oink's std::sort order, labels "origK" = ids in
the climb's file). (1) Python: L-COMP's dtl_py (copy dtl_pyref.py) with Oink's order data (identity index order, ins lists
descending, tangle vertices sorted, Pearce SCC order) + dtl_ideal.pq_violations. (2) Oink (if tools/oink/build/oink exists):
pinned command with `-t -t`; the "distance k:" lines of the FIRST best_vertices call of consecutive same-player iterations
with no dominion in between; a vertex whose distance decreases is a violation. Exit 1 if (1), or (2) when run, does not
reproduce."""
import sys, os, re, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_pyref as D, dtl_ideal as I

GAME = os.path.join(HERE, "instances", "dtl_mviol_n20.pg")
g = pg.read(GAME)
lab = lambda v: g.labels[v] if g.labels else str(v)
ok = True

# (1) Python run with Oink's order data (the file is already in Oink's index order)
D.TV_SORTED, D.PEARCE = True, True
d = I.Ctx(list(g.prio), list(g.owner), [list(s) for s in g.succ], ins_desc=True)
d.run()
viol = sorted({(p, s1, s2, lab(v), a, b) for p, s1, s2, v, a, b in I.pq_violations(d)})
print(f"python: tangles {d.tangles}, dominions {d.dominions}, searches {d.nsearch}; Claim-P violations "
      f"(player, search, later search, vertex, round, later round): {viol}")
ok &= any(v[3] == "orig16" for v in viol) and any(v[3] == "orig1" for v in viol)

# (2) Oink's own trace
oink = os.path.join(HERE, "..", "..", "tools", "oink", "build", "oink")
if os.path.exists(oink):
    out = subprocess.run([oink, "--dtl", "--no-single", "--no-wcwc", "--no-loops", "-t", "-t", GAME],
                         capture_output=True, text=True).stdout + ""
    out = re.sub(r"\x1b\[[0-9;]*m", "", out)
    iters, cur, first = [], None, False
    for line in out.splitlines():
        m = re.search(r"iteration (\d+)-(even|odd)", line)
        if m:
            cur = {"it": int(m.group(1)), "p": m.group(2), "dist": {}, "dominion_before": False}
            iters.append(cur); first = True; continue
        if cur is None:
            continue
        if "dominion" in line and "dominions" not in line:
            cur["dominion_after"] = True
        if first:
            m = re.search(r"distance (\d+): (.*)$", line)
            if m:
                for v in m.group(2).split():
                    cur["dist"][v] = int(m.group(1))
            if "best vertices" in line:
                first = False
    found = []
    for a, b in zip(iters, iters[1:]):
        if a["p"] == b["p"] and not a.get("dominion_after"):
            for v, k in a["dist"].items():
                if v in b["dist"] and b["dist"][v] < k:
                    found.append((a["it"], b["it"], v, k, b["dist"][v]))
    print("oink: first-call distance decreases (iteration, next same-player iteration, vertex, distance, later distance):",
          found)
    ok &= any(f[2] == "orig16" for f in found) and any(f[2] == "orig1" for f in found)
else:
    print("oink: NOT RUN (tools/oink/build/oink absent; scripts/setup_oink.sh)")
print("M-VIOLATION", "REPRODUCED" if ok else "NOT REPRODUCED")
sys.exit(0 if ok else 1)
