#!/usr/bin/env python3
"""L-RED box 9 (produced on Opus 5.5): per transition of each phase, where the first difference e* lies, by the same rule as
L-ALG's dtl_rootmono.py (dtl_rootmono.RM and dtl_fdlcheck.reduce_log imported UNMODIFIED from LALGR_DIR; first differing
non-extract/pass log entry, compared on its first 4 fields; context = the best_vertices record containing it, else "T" =
search_rec -1 attractor). Prints caller, context (depth, |R|) and a short id per distinct R. Usage: ctxtrace.py G.pg"""
import sys, os
sys.path.insert(0, os.path.join(os.environ["LALGR_DIR"], "experiments", "alg"))
sys.path.insert(0, os.path.join(os.environ["LALGR_DIR"], "experiments", "harness"))
import pg, dtl_rootmono as RMo
FD = RMo.FD; FC = RMo.FC
sys.setrecursionlimit(100000)
g = pg.read(sys.argv[1]); order = os.environ.get("DTL_ORDER", "stable")
d0 = FD.P.X.build(g); d = RMo.RM(d0.pr, d0.ow, d0.outs, ins_desc=(order == "oink")); d.idx = d0.idx; d.run()
st = {"dropped": 0, "kept: differs": 0, "kept: identical but extracts": 0}
for phn, ph in enumerate(FD.phase_rows(d)):
    for r in ph: r["log"] = FC.reduce_log(r["log"], st)
    ids = {}; out = []
    for a, b in zip(ph, ph[1:]):
        la = [i for i, e in enumerate(a["log"]) if e[0] not in ("extract", "pass")]
        lb = [i for i, e in enumerate(b["log"]) if e[0] not in ("extract", "pass")]
        k = 0
        while k < min(len(la), len(lb)) and a["log"][la[k]][:4] == b["log"][lb[k]][:4]: k += 1
        if k == min(len(la), len(lb)): out.append("none"); continue
        pos = lb[k]; rb = next((r_ for r_ in b["recs"] if r_["start"] <= pos < r_["end"]), None)
        if rb is None: out.append(f"T({b['log'][pos][0]})"); continue
        key = rb["key"]; ids.setdefault(key, len(ids))
        out.append(f"C{ids[key]}[d{key[0]},|R|{len(key[1])},{b['log'][pos][0]}]")
    if len(ph) > 1: print(f"phase {phn}: S {len(ph)} |G'| {len(ph[0]['G'])} distinct bv contexts {len(ids)}:", " ".join(out), flush=True)
