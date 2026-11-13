#!/usr/bin/env python3
"""L-SI box 105, D2 validation (Lead 17:27Z: «D2 checks regions and S3-standardness on every genome»): each best ladder genome of
run105d2.sh (best/ladder_<mode>_d<d>.json, ladder105.py's state) is rebuilt as Gamma3*(G*) and run by N5 (box190 n5v.py mode spec) from
S3 through key105.validate: s3fail, keyfail (N5's states 0..L* carry KEY's state at the movers; first fallback at L* + 1), endfail
(1 fallback, L* + 3 iterations), wrong (regions != harness Zielonka), keymono, valmono; and whether the Xi-graph is cyclic
(self-loops count; R104's IDEAL-ACYC test). One line per file.
Usage: val105.py FILE.json...   (env LNEW, LRED, BOX104 as key105.py)"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import ladder105 as LD
import key105 as K
def xi_cyclic(G):
    """True iff the Xi-graph (x -> Xi-target of each option, movers only; self-loops count) has a cycle (R104's IDEAL-ACYC test)"""
    N = G["N"]; E = {x: {o[1] for o in G["opts"][x] if o[1] >= 0} for x in range(N)}; col = {}
    def dfs(u):
        col[u] = 1
        for w in E[u]:
            if col.get(w) == 1 or (w not in col and dfs(w)): return True
        col[u] = 2; return False
    return any(dfs(x) for x in range(N) if x not in col)
for f in sys.argv[1:]:
    b = json.load(open(f)); G = LD.genome(b["state"], b["d"]); pb, pe = LD.prios(b["state"], G, b["mode"])
    c, L, n = K.validate(G, pb, pe)
    print("VAL105 %s mode %s d %d: |V| %d L* %d (search: %d) Xi-graph %s | %s" % (os.path.basename(f), b["mode"], b["d"], n, L, b["L"],
          "cyclic" if xi_cyclic(G) else "acyclic",
          " ".join("%s %d" % (k, c[k]) for k in ("s3fail", "keyfail", "endfail", "wrong", "keymono", "valmono"))), flush=True)
