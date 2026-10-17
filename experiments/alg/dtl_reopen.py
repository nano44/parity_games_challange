"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), queue item (2): resets. For consecutive searches s, s+1 of a phase,
idx0 (dtl_idx0.py) per vertex; OPENED = vertices whose depth-0 removal index increases (moved to a later piece), CLOSED =
decreases. For opened v: RELEARN if v lies in a tangle learned in a later search of the phase. Per phase: totals of opened,
closed, relearned, and S, |G'|. DTL_ORDER=oink | stable. Usage: dtl_reopen.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_absorb as AB, dtl_idx0 as I0

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = AB.SL.P.X.build(g)
        d = AB.AB(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
        rows, cur = [], []
        for t in d.trace:
            if cur and (t["p"] != cur[-1]["p"] or t["dom"] != cur[-1]["dom"]): rows.append(cur); cur = []
            cur.append(t)
        if cur: rows.append(cur)
        for ph in rows:
            if len(ph) < 4: continue
            G = ph[0]["G"]; ix = [I0.idx0(tr["calls"], G) for tr in ph]
            learned = [set().union(*[C for _, C in tr.get("learn", [])]) if tr.get("learn") else set() for tr in ph]
            op = cl = rl = 0; per = []
            for s in range(len(ph) - 1):
                O = {v for v in G if ix[s + 1].get(v, 0) > ix[s].get(v, 0)}; Cc = {v for v in G if ix[s + 1].get(v, 0) < ix[s].get(v, 0)}
                later = set().union(*learned[s + 1:]) if s + 1 < len(ph) else set()
                R = O & later; op += len(O); cl += len(Cc); rl += len(R); per.append(f"{len(Cc)}/{len(O)}/{len(R)}")
            print(os.path.relpath(f), f"p={ph[0]['p']} S={len(ph)} |G'|={len(G)} closed {cl} opened {op} opened-then-relearned {rl}  per transition closed/opened/relearned:", " ".join(per))

def fullpos(calls, G):
    """Position of v = tree position (tuple) of the last best_vertices call (call order) whose context contains v."""
    lab = {}
    for pos, R, res, V in calls:
        for v in R: lab[v] = pos
    return lab

def closings(f):
    """(CL) per transition: vertices whose full tree position moves lexicographically EARLIER (closed) / LATER (opened)."""
    g = pg.read(f); d0 = AB.SL.P.X.build(g)
    d = AB.AB(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
    rows, cur = [], []
    for t in d.trace:
        if cur and (t["p"] != cur[-1]["p"] or t["dom"] != cur[-1]["dom"]): rows.append(cur); cur = []
        cur.append(t)
    if cur: rows.append(cur)
    out = []
    for ph in rows:
        G = ph[0]["G"]; L = [fullpos(tr["calls"], G) for tr in ph]
        for s in range(len(ph) - 1):
            a, b = L[s], L[s + 1]
            out.append((sum(1 for v in G if b.get(v, ()) < a.get(v, ())), sum(1 for v in G if b.get(v, ()) > a.get(v, ()))))
    return out
