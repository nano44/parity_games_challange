"""L-ALG succ. 6 (produced on Opus 5.5, 2026-10-17 box 6), GAP-C §18o: is a BORN ORPHAN of search s the cause of the first
difference of s → s+1 (First-Difference Lemma (iii), logs with repeated sptl passes deleted, as dtl_fdlcheck.py)? For each
consecutive pair in a phase where s has born orphans: (C) some born orphan of s is accepted at the first differing tattr
e of s+1; (c) none is, but another tangle created by s is; (-) no tangle of s is accepted at e (FDL (iii) would fail);
(=) no difference (logs equal or prefix). DTL_ORDER = oink | stable. Usage: dtl_borncause.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_fdlcheck as FC, dtl_bornnext as BN
FD = FC.FD; tab = {}

if __name__ == "__main__":
    sys.setrecursionlimit(100000); st = {"dropped": 0, "kept: differs": 0, "kept: identical but extracts": 0}
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = FD.P.X.build(g); d = BN.BN(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
        for ph in FD.phase_rows(d):
            for r in ph: r["log"] = FC.reduce_log(r["log"], st)
            for a, b in zip(ph, ph[1:]):
                born = {t for t, _ in a.get("born", [])}
                if not born: continue
                la = [e for e in a["log"] if e[0] != "extract"]; lb = [e for e in b["log"] if e[0] != "extract"]
                k = 0
                while k < min(len(la), len(lb)) and la[k][:4] == lb[k][:4]: k += 1
                if k == min(len(la), len(lb)): tab["(=) no difference"] = tab.get("(=) no difference", 0) + 1; continue
                used = set(lb[k][5]); created = {e[1] for e in a["log"] if e[0] == "extract"}
                key = "(C) a born orphan of s is accepted at e" if used & born else "(c) another tangle of s is accepted at e" if used & created else "(-) no tangle of s at e"
                tab[key] = tab.get(key, 0) + 1
    print({k: tab[k] for k in sorted(tab)})
