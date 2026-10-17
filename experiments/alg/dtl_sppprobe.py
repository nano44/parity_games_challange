"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), queue item (2): per-phase candidate potentials, tested per search.
For each phase (dtl_spp.py convention) and each search s but the last, with T_s the tangles stored before s:
  UNION: the union of the vertex sets of the phase player's tangles strictly grows in s;
  TOPS:  the set of tops (vertices at which a tangle was extracted) strictly grows;
  PAIRS: the set of (top, vertex) incidences strictly grows;
  NEWV:  some tangle learned in s contains a vertex in no earlier tangle of the same TOP.
Counts searches where each fails. DTL_ORDER=oink | stable. Usage: dtl_sppprobe.py G.pg ... (PROBE_V=1 prints failures)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_spp as P

class PR(P.PS):
    def extractTangles(s, top, R):
        k = len(s.tv); r = P.X.D.DTL.extractTangles(s, top, R)
        for t in range(k, len(s.tv)): s.trace[-1].setdefault("new", []).append((top, frozenset(v for v, _ in s.tv[t])))
        return r

def probe(d):
    rows, cur = [], []
    for t in d.trace:
        if cur and (t["p"] != cur[-1]["p"] or t["dom"] != cur[-1]["dom"]): rows.append(cur); cur = []
        cur.append(t)
    if cur: rows.append(cur)
    res = []
    for ph in rows:
        p = ph[0]["p"]; U = set(); tops = set(); pairs = set(); bytop = {}
        # tangles of p stored before the phase
        for (top, C) in [x for tr in d.trace[:d.trace.index(ph[0])] for x in tr.get("new", []) if d.pr[x[0]] % 2 == p]:
            U |= C; tops.add(top); pairs |= {(top, v) for v in C}; bytop.setdefault(top, set()).update(C)
        fail = {"UNION": [], "TOPS": [], "PAIRS": [], "NEWV": []}
        for i, tr in enumerate(ph[:-1]):
            new = tr.get("new", [])
            U2 = U | set().union(*[C for _, C in new]) if new else set(U)
            if not U2 > U: fail["UNION"].append(i)
            T2 = tops | {t for t, _ in new}
            if not T2 > tops: fail["TOPS"].append(i)
            P2 = pairs | {(t, v) for t, C in new for v in C}
            if not P2 > pairs: fail["PAIRS"].append(i)
            if not any(C - bytop.get(t, set()) for t, C in new): fail["NEWV"].append(i)
            U, tops, pairs = U2, T2, P2
            for t, C in new: bytop.setdefault(t, set()).update(C)
        res.append((p, len(ph), fail))
    return res

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    tot = {}; nph = 0; ns = 0
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = P.X.build(g); d = PR(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
        for p, S, fail in probe(d):
            if S < 2: continue
            nph += 1; ns += S - 1
            for k, v in fail.items():
                tot[k] = tot.get(k, 0) + len(v)
                if v and os.environ.get("PROBE_V"): print(f"{os.path.relpath(f)} p={p} S={S} {k} fails at searches {v}")
    print(f"phases(S>=2)={nph} non-last searches={ns} failures:", tot)
