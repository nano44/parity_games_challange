#!/usr/bin/env python3
"""L-RED box 10 (produced on Opus 5.5): print each best_vertices round (regions per top, candidates removed) for calls with
|R| in BV_R (comma list), search <= BV_S, using the reference model's own code (dtl_pyref UNMODIFIED, re-run on a copy of
the state). Input ids. Usage: BV_R=14 BV_S=0 bvtrace.py G.pg"""
import sys, os, copy
A = os.path.join(os.environ["LALG_DIR"], "experiments", "alg"); sys.path.insert(0, A); sys.path.insert(0, os.path.join(A, "..", "harness"))
import pg, dtl_deficit as X
D = X.D; g = pg.read(sys.argv[1]); d0 = X.build(g); I = d0.idx
RS = {int(x) for x in os.environ.get("BV_R", "").split(",") if x}; MS = int(os.environ.get("BV_S", "0"))
nm = lambda S_: "{" + ",".join(str(I[v]) for v in sorted(S_, key=lambda v: I[v])) + "}"
class L(D.DTL):
    ns = 0
    def search(s, p): s.ns += 1; return D.DTL.search(s, p)
    def best_vertices(s, V, R, p):
        if s.ns - 1 <= MS and (not RS or len(R) in RS):
            Vc = set(v for v in R if s.pr[v] % 2 == p); rnd = 0; saveQ = s.Q; savestr = list(s.str)
            while Vc and rnd < 6:
                rnd += 1; Z = set(); CurR = set(R); regs = []
                for top in range(s.n - 1, -1, -1):
                    if top not in Vc or top in Z: continue
                    CurZ = {top}; s.Q = [top]; s.tattr(p, CurZ, CurR, CurR, s.pr[top], CurR); Z |= CurZ; regs.append(f"{I[top]}:{nm(CurZ)}")
                cand = [v for v in sorted(Vc, reverse=True) if not s.attracts(p, v, Z, R)]
                print(f"   [s{s.ns-1} |R|{len(R)} round {rnd}] regions", " ".join(regs), "| not attracted:", nm(cand))
                if not cand: break
                for t in [0] + [q for q in s.prios if q > 0 and q <= s.maxpr]:
                    s.Q = sorted(Z); s.tattr(p, Z, R, R, t, None)
                    keep = []
                    for i, u in enumerate(cand):
                        if s.pr[u] <= t: keep += cand[i:]; break
                        if not s.attracts(p, u, Z, R): keep.append(u)
                    cand = keep
                print("      removed", nm(cand)); Vc -= set(cand)
                if not cand: break
            s.Q = saveQ; s.str = savestr
        return D.DTL.best_vertices(s, V, R, p)
d = L(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = I; d.tkeys = []
sys.setrecursionlimit(100000); d.run()
