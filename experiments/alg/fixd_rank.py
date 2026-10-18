"""L-ALG succ. 9 (box 11, produced on Opus 5.5), GAP-A-M §27d: (RANK-MONO) toward (CTX⁺). For a search s of a phase let
ctx0(s) = R_0 ⊋ R_1 ⊋ ... be its depth-0 best_vertices contexts (dtl_rootmono.RM, as in dtl_ctxpieces.py) and
rank_s(v) = max{ j : v ∈ R_j(s) } (the depth-0 position at which v is removed). (RANK-MONO): rank_{s+1}(v) ≤ rank_s(v) for every
v ∈ G′ and consecutive searches s, s+1 of a phase. With it, the depth-0 contexts change only at rank drops, so a phase has at
most (n+1)(n² + 1) distinct depth-0 contexts. Also printed: the number of distinct depth-0 contexts and the depth of the
first-difference contexts is not computed here. Usage: RM_DV=0 RM_LIGHT=1 DTL_ORDER=oink|stable fixd_rank.py G.pg ..."""
import sys, os
os.environ.setdefault("RM_DV", "0"); os.environ.setdefault("RM_LIGHT", "1")
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_rootmono as RMM, dtl_step5stats as ST
FD = RMM.FD
POS = []   # (pair index, pairs in the phase, #vertices whose rank rose, chain sizes before, after)


def check(g):
    d0 = FD.P.X.build(g); d = RMM.RM(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
    inc = not all(w is not None for w in d.win); viol = 0; pairs = 0; first = None; nctx = 0
    for ph in FD.phase_rows(d):
        G = ph[0]["G"]; ctxs = set()
        ranks = []
        for r in ph:
            c0 = r["ctx0"]; ctxs.update(c0)
            ranks.append({v: max((j for j, R in enumerate(c0) if v in R), default=-1) for v in G})
        nctx = max(nctx, len(ctxs))
        for k, (a, b) in enumerate(zip(ranks, ranks[1:])):
            pairs += 1
            bad = [v for v in G if b[v] > a[v]]
            if bad:
                viol += 1
                if first is None: first = (len(ph), sorted(d.idx[v] for v in bad)[:6])
                POS.append((k, len(ph) - 1, len(bad), [len(R) for R in ph[k]["ctx0"]], [len(R) for R in ph[k + 1]["ctx0"]]))
    return inc, pairs, viol, first, nctx


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f, g in ST.games(sys.argv[1:]):
        inc, pairs, viol, first, nctx = check(g)
        print(os.path.basename(f), "INCOMPLETE" if inc else "complete", "pairs", pairs, "RANK-MONO violations", viol,
              "first", first, "max distinct depth-0 contexts", nctx, flush=True)
        for p in POS: print("   violation at pair", p[0], "of", p[1], "| rank rose for", p[2], "vertices | chain sizes", p[3], "->", p[4])
        POS.clear()
