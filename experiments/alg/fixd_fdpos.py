"""L-ALG succ. 9 (box 11, produced on Opus 5.5), GAP-A-M §28: where the first differences of a phase sit on the depth-0 chain.
For each transition s -> s+1 of a phase (reduced logs, first difference e* as in dtl_ctxclimb.fitness) print the first-difference
context's depth and, for the depth-0 context R_j(s+1) that contains e* or calls the deeper call holding it, the chain
position j. A RESET at transition s is a position j(s) < j(s-1): the rise at j re-cuts the chain below it. The RESET DEPTH of a
phase is the longest chain of positions p_1 < p_2 < ... < p_k such that the transitions at p_i happen between two resets at
p_{i-1} (a nested counter); here it is computed as the length of the longest strictly increasing run between resets to a
position <= its start, a cheap proxy: max over s of #{distinct positions seen since the last transition at a position <= j(s)}.
Usage: RM_DV=0 RM_LIGHT=1 DTL_ORDER=oink|stable fixd_fdpos.py G.pg ..."""
import sys, os
os.environ.setdefault("RM_DV", "0"); os.environ.setdefault("RM_LIGHT", "1")
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_rootmono as RMo, dtl_step5stats as ST
FD = RMo.FD


def fdpos(g):
    d0 = FD.P.X.build(g); d = RMo.RM(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
    st = {"dropped": 0, "kept: differs": 0, "kept: identical but extracts": 0}; out = []
    for ph in FD.phase_rows(d):
        for r in ph: r["log"] = RMo.FC.reduce_log(r["log"], st)
        seq = []
        for a, b in zip(ph, ph[1:]):
            la = [i for i, e in enumerate(a["log"]) if e[0] not in ("extract", "pass")]
            lb = [i for i, e in enumerate(b["log"]) if e[0] not in ("extract", "pass")]
            k = 0
            while k < min(len(la), len(lb)) and a["log"][la[k]][:4] == b["log"][lb[k]][:4]: k += 1
            if k == min(len(la), len(lb)): seq.append(("none", None)); continue
            pos = lb[k]
            rec = next((r_ for r_ in b["recs"] if r_["start"] <= pos < r_["end"]), None)
            if rec is None: seq.append(("outside", None)); continue
            dep, R = rec["key"]
            # depth-0 chain position: the last depth-0 context of b that contains R (R itself if depth 0)
            c0 = b["ctx0"]; j = max((i for i, C in enumerate(c0) if R <= C), default=None)
            seq.append((dep, j))
        out.append((len(ph), len(ph[0]["G"]), seq))
    return out


def reset_depth(js):
    best = 0
    for s in range(len(js)):
        seen = set()
        for t in range(s, -1, -1):
            if js[t] is None: break
            if t < s and js[t] <= js[s]: break
            seen.add(js[t])
        best = max(best, len(seen))
    return best


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f, g in ST.games(sys.argv[1:]):
        for S, nG, seq in fdpos(g):
            if S < 3: continue
            js = [j for _, j in seq]
            resets = sum(1 for a, b in zip(js, js[1:]) if a is not None and b is not None and b < a)
            print(os.path.basename(f), "S", S, "|G'|", nG, "resets", resets, "reset-depth proxy", reset_depth(js),
                  "positions", js, "depths", [dp for dp, _ in seq], flush=True)
