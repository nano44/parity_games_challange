"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5): mechanical check of the First-Difference Lemma (GAP-A-M §21d) on
DTL runs. For consecutive searches s, s+1 of a phase, with every tattr call and every extraction logged in call order:
 (ii) the first tattr whose output differs has the same caller, depth, input Z and threshold, and a strictly larger output;
 (iv) search s+1 creates no tangle before that call;
 (iii) some tangle attracted there was created by s at or after the position of that call in s's log.
DTL_ORDER=oink | stable. Usage: dtl_fdlcheck.py G.pg ...   (exit 1 on any violation)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_firstdiff as FD
D = FD.D

class CK(FD.FD):
    def tattr(s, p, Z, R, Gx, maxpr, consume):
        FD.FD.tattr(s, p, Z, R, Gx, maxpr, consume)
        s.log[-1] = s.log[-1] + (len(s.tv),)                  # tangles existing when this call ended
    def extractTangles(s, top, R):
        k = len(s.tv); r = D.DTL.extractTangles(s, top, R)
        for t in range(k, len(s.tv)): s.log.append(("extract", t))
        return r

if __name__ == "__main__":
    sys.setrecursionlimit(100000); n = bad = 0
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = FD.P.X.build(g); d = CK(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
        for ph in FD.phase_rows(d):
            for a, b in zip(ph, ph[1:]):
                la = [e for e in a["log"] if e[0] != "extract"]; lb = [e for e in b["log"] if e[0] != "extract"]
                k = 0
                while k < min(len(la), len(lb)) and la[k][:4] == lb[k][:4]: k += 1
                if k == min(len(la), len(lb)): continue
                n += 1; x, y = la[k], lb[k]
                ok2 = x[0] == y[0] and x[1] == y[1] and x[2] == y[2] and x[4] == y[4] and y[3] > x[3]
                # position of the k-th tattr in b's full log; extractions before it in b?
                full_b = b["log"]; cnt = -1; pos_b = None
                for i, e in enumerate(full_b):
                    if e[0] != "extract":
                        cnt += 1
                        if cnt == k: pos_b = i; break
                ok4 = not any(e[0] == "extract" for e in full_b[:pos_b])
                full_a = a["log"]; cnt = -1; pos_a = None
                for i, e in enumerate(full_a):
                    if e[0] != "extract":
                        cnt += 1
                        if cnt == k: pos_a = i; break
                later_a = {e[1] for e in full_a[pos_a:] if e[0] == "extract"}
                ok3 = bool(set(y[5]) & later_a)
                if not (ok2 and ok3 and ok4):
                    bad += 1; print("VIOLATION", os.path.relpath(f), f"p={a['p']}", {"ii": ok2, "iii": ok3, "iv": ok4}, flush=True)
    print(f"First-Difference Lemma check: {n} transitions, violations {bad}"); sys.exit(1 if bad else 0)
