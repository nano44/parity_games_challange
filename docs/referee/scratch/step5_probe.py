"""REFEREE probe (R-STEP5): independent instrumentation of dtl_pyref (via dtl_step5.S5) for
 TPR  : every stored tangle contains its top and tpr == max priority of its vertices (DTL-proof Lemma 1.5a, used by NT-f (D));
 NTF  : the final round of every -1 best_vertices call accepts no tangle in its region loop;
 FM   : Z_f subset of Z^r for every round r of a -1 call;
 YZ   : at P pieces, Dom(prevV) removes exactly Z_f; also counts straddling Dom acceptances;
 C1Z  : number of -1 calls whose f == 1 (NT-f trivial case).
Usage: DTL_ORDER=oink|stable ref_probe.py G.pg ..."""
import sys, os
A = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "experiments", "alg")
sys.path.insert(0, A); sys.path.insert(0, os.path.join(A, "..", "harness"))
import pg, dtl_step5 as S5
D = S5.D
C = dict(tangles=0, tpr_bad=0, top_missing=0, calls=0, ntf_bad=0, fm_bad=0, f1=0, P=0, yz_bad=0, strad=0, rounds=0)

class R(S5.S5):
    in_reg = False; acc = 0; in_dom = False; xb = None; lastZf = None
    def extractTangles(s, top, Rg):
        k = len(s.tv); r = S5.S5.extractTangles(s, top, Rg)
        for t in range(k, len(s.tv)):
            vs = [v for v, _ in s.tv[t]]; C["tangles"] += 1
            if top not in vs: C["top_missing"] += 1
            if s.tpr[t] != max(s.pr[v] for v in vs): C["tpr_bad"] += 1
        return r
    def attractTangle(s, t, p, Rg, Z, Gx, maxpr):
        r = D.DTL.attractTangle(s, t, p, Rg, Z, Gx, maxpr)
        if r and s.in_reg: s.acc += 1
        if r and s.in_dom and any(w in s.xb for w, _ in s.tv[t]): C["strad"] += 1
        return r
    def best_vertices(s, V, Rg, p):
        V.clear(); V.update(v for v in Rg if s.pr[v] % 2 == p)
        s.lastZf = None
        if not V: return 0
        Zs = []
        while True:
            prevV = set(V); Z = set(); CurR = set(Rg); s.acc = 0; s.in_reg = True
            for top in range(s.n - 1, -1, -1):
                if top not in V or top in Z: continue
                CurZ = {top}; s.Q = [top]
                s.tattr(p, CurZ, CurR, CurR, s.pr[top], CurR)
                Z |= CurZ
            s.in_reg = False; acc = s.acc; Zs.append(frozenset(Z)); C["rounds"] += 1
            cand = [v for v in sorted(V, reverse=True) if not s.attracts(p, v, Z, Rg)]
            if not cand: return 1
            for t in [0] + [q for q in s.prios if q > 0 and q <= s.maxpr]:
                s.Q = sorted(Z); s.tattr(p, Z, Rg, Rg, t, None)
                keep = []
                for i, u in enumerate(cand):
                    if s.pr[u] <= t: keep += cand[i:]; break
                    if not s.attracts(p, u, Z, Rg): keep.append(u)
                cand = keep
            V -= set(cand)
            if not cand: return 1
            if not V:
                V.clear(); V.update(prevV); C["calls"] += 1
                if acc: C["ntf_bad"] += 1
                Zf = Zs[-1]
                if len(Zs) == 1: C["f1"] += 1
                if any(not Zf <= Zr for Zr in Zs): C["fm_bad"] += 1
                s.lastZf = Zf
                return -1
    def dom(s, V, Rg, X, p):
        P = s.lastZf is not None
        R0 = set(Rg)
        s.in_dom = P
        for top in range(s.n - 1, -1, -1):
            if top not in V or top in X: continue
            s.xb = set(X)
            X.add(top); s.str[top] = -1; s.Q = [top]
            s.tattr(p, X, Rg, Rg, s.pr[top], Rg)
        s.in_dom = False
        if P:
            C["P"] += 1
            if R0 - set(Rg) != s.lastZf: C["yz_bad"] += 1
        s.lastZf = None

for f in sys.argv[1:]:
    try: g = pg.read(f)
    except Exception as e: continue
    if g.n > 80: continue
    try: pass
    except Exception as e: continue
    d0 = S5.X.build(g); d = R(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.trace = []
    d.run()
print(os.environ.get("DTL_ORDER", "stable"), C)
