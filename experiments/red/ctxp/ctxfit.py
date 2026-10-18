#!/usr/bin/env python3
"""L-RED box 11 (produced on Opus 5.5): first-difference location per transition, by the rule of root/ctxtrace.py (L-ALG
dtl_rootmono.RM and dtl_fdlcheck.reduce_log imported UNMODIFIED from LALG_DIR). For each phase: list of (depth, |R|, caller,
context id) per transition (depth None for a search_rec -1 attractor 'T' entry, with the depth of its log entry).
Usage: ctxfit.py G.pg   (prints per phase; summary: transitions, distinct contexts, e* at depth >= 1)"""
import sys, os
for k, v in (("RM_LIGHT", "1"), ("RM_DV", "0")): os.environ.setdefault(k, v)
A = os.path.join(os.environ["LALG_DIR"], "experiments", "alg"); sys.path.insert(0, A); sys.path.insert(0, os.path.join(A, "..", "harness"))
import pg, dtl_rootmono as RMo
FD = RMo.FD; FC = RMo.FC
sys.setrecursionlimit(100000)
def run(g):
    order = os.environ.get("DTL_ORDER", "stable")
    d0 = FD.P.X.build(g); d = RMo.RM(d0.pr, d0.ow, d0.outs, ins_desc=(order == "oink")); d.idx = d0.idx; d.run()
    st = {"dropped": 0, "kept: differs": 0, "kept: identical but extracts": 0}; phases = []
    for ph in FD.phase_rows(d):
        for r in ph: r["log"] = FC.reduce_log(r["log"], st)
        ids = {}; out = []
        for a, b in zip(ph, ph[1:]):
            la = [i for i, e in enumerate(a["log"]) if e[0] not in ("extract", "pass")]
            lb = [i for i, e in enumerate(b["log"]) if e[0] not in ("extract", "pass")]
            k = 0
            while k < min(len(la), len(lb)) and a["log"][la[k]][:4] == b["log"][lb[k]][:4]: k += 1
            if k == min(len(la), len(lb)): out.append(None); continue
            pos = lb[k]; e = b["log"][pos]; rb = next((r_ for r_ in b["recs"] if r_["start"] <= pos < r_["end"]), None)
            if rb is None: out.append(("T", e[1] if len(e) > 1 else None, None, e[0])); continue
            key = rb["key"]; ids.setdefault(key, len(ids)); out.append((key[0], len(key[1]), ids[key], e[0]))
        phases.append((len(ph), len(ph[0]["G"]) if ph else 0, len(ids), out))
    return phases
def summary(phases):
    tr = sum(len(o) for _, _, _, o in phases); cx = max([c for _, _, c, _ in phases] or [0])
    deep = sum(1 for _, _, _, o in phases for x in o if x and ((x[0] != "T" and x[0] >= 1) or (x[0] == "T" and isinstance(x[1], int) and x[1] >= 1)))
    return tr, cx, deep
if __name__ == "__main__":
    ph = run(pg.read(sys.argv[1]))
    for i, (S, nG, c, o) in enumerate(ph):
        if S > 1: print(f"phase {i}: S {S} |G'| {nG} contexts {c}:", " ".join("none" if x is None else f"{x[0]}/{x[1]}/C{x[2]}/{x[3]}" for x in o))
    print("SUMMARY transitions %d max-contexts %d e*-at-depth>=1 %d" % summary(ph))
