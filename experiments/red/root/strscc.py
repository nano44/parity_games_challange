#!/usr/bin/env python3
"""L-RED box 7 (produced on Opus 5.5), target (2e) (REFEREE-2 R2-P4 gap G-STR): consecutive searches s, s+1 of a phase
whose tattr calls agree (FDL alignment on reduced logs, as in L-ALG dtl_fdlcheck.py) up to the first difference e*, but
where an SCC extraction BEFORE e* sees a different strategy and finds different SCCs. Built on L-ALG's dtl_fdlcheck.CK and
reduce_log, UNMODIFIED (the logged run is unchanged); this subclass only records, in a side list, at every
extractTangles(top, R): the SCCs of the strategy graph (p-vertices: str[v] if in R; opponent: all edges into R) reachable
from top, non-trivial or self-looped as dtl_pyref keeps them (duplicates INCLUDED), keyed by the last tattr entry logged
before it. reduce_log keeps the tuple objects, so each record maps to a reduced position; records after a dropped
(repeated) tattr are skipped. HIT-STR = same reduced position, same (top, R), different SCC sets, before e* (or with no
e*). Also counts STR-DIFF-ONLY (str on R differs, SCCs equal). LALGC_DIR = l-alg >= c983b024; DTL_ORDER = oink | stable.
Usage: strscc.py G.pg ..."""
import sys, os
sys.path.insert(0, os.path.join(os.environ["LALGC_DIR"], "experiments", "alg"))
sys.path.insert(0, os.path.join(os.environ["LALGC_DIR"], "experiments", "harness"))
import pg, dtl_fdlcheck as FC
FD = FC.FD


class SC(FC.CK):
    def search(s, p):
        s.side = []; r = FC.CK.search(s, p); s.trace[-1]["side"] = s.side; return r

    def extractTangles(s, top, R):
        p = s.pr[top] % 2; Rs = set(R)
        def succ(v):
            if s.ow[v] == p:
                w = s.str[v]; return [w] if w != -1 and w in Rs else []
            return [w for w in s.outs[v] if w in Rs]
        reach = {top}; st = [top]
        while st:
            v = st.pop()
            for w in succ(v):
                if w not in reach: reach.add(w); st.append(w)
        sccs = set()
        for v in reach:
            fw = {v}; st = [v]
            while st:
                x = st.pop()
                for w in succ(x):
                    if w not in fw: fw.add(w); st.append(w)
            C = frozenset(u for u in fw if v in _reach(u, succ))
            if len(C) > 1 or s.str[v] == v or (s.ow[v] != p and v in s.outs[v] and v in Rs) or (s.ow[v] == p and s.str[v] == v):
                sccs.add(C)
        last = next((e for e in reversed(s.log) if e[0] not in ("extract", "pass")), None)
        strR = tuple(sorted((v, s.str[v]) for v in Rs if s.ow[v] == p))
        s.side.append((last, top, frozenset(Rs), frozenset(sccs), strR))
        return FC.CK.extractTangles(s, top, R)


def _reach(u, succ):
    fw = {u}; st = [u]
    while st:
        x = st.pop()
        for w in succ(x):
            if w not in fw: fw.add(w); st.append(w)
    return fw


def measure_game(g, order, verbose=False, name=""):
    os.environ["DTL_ORDER"] = order
    stat = {"dropped": 0, "kept: differs": 0, "kept: identical but extracts": 0}
    d0 = FD.P.X.build(g); d = SC(d0.pr, d0.ow, d0.outs, ins_desc=(order == "oink")); d.idx = d0.idx; d.run()
    m = dict(hit=0, strdiff=0, compared=0, trans=0, silent=0, incomplete=int(not all(w is not None for w in d.win)))
    for ph in FD.phase_rows(d):
        for r in ph: r["red"] = FC.reduce_log(r["log"], stat)
        for i, (a, b) in enumerate(zip(ph, ph[1:])):
            la = [e for e in a["red"] if e[0] != "extract"]; lb = [e for e in b["red"] if e[0] != "extract"]
            k = 0
            while k < min(len(la), len(lb)) and la[k][:4] == lb[k][:4]: k += 1
            m["trans"] += 1
            newt = set(range(a["k0"], b["k0"]))            # tangles created by s: SILENT = they fire before e* in s+1
            m["silent"] += sum(1 for e in lb[:k] if set(e[5]) & newt)   # with an unchanged output (the G-STR first half)
            def recs(row, L):
                pos = {id(e): j for j, e in enumerate(L)}; out = {}
                for last, top, R, sccs, strR in row["side"]:
                    if last is None: j = -1
                    elif id(last) in pos: j = pos[id(last)]
                    else: continue                          # after a dropped (repeated) tattr
                    if j < k: out.setdefault((j, top, R), []).append((sccs, strR))
                return out
            ra, rb = recs(a, la), recs(b, lb)
            for key in ra.keys() & rb.keys():
                for (sa, ta), (sb, tb) in zip(ra[key], rb[key]):
                    m["compared"] += 1
                    if sa != sb:
                        m["hit"] += 1
                        if verbose: print("HIT-STR", name, order, f"p={a['p']} pair {i}->{i + 1} pos {key[0]} (e* at {k}) top {d.idx[key[1]]}"
                                          f" |R| {len(key[2])}: s {sorted(sorted(d.idx[v] for v in C) for C in sa)}"
                                          f" s+1 {sorted(sorted(d.idx[v] for v in C) for C in sb)}", flush=True)
                    elif ta != tb: m["strdiff"] += 1
    return m


def score(path):
    """dtl_search.py --fitness strscc: 1e12 incomplete + 1e11 HIT-STR + 1e8 * STR-DIFF-ONLY + 1e5 * compared extractions
    before e* + SILENT (tattr calls before e* in s+1 where a tangle created by s fires with an unchanged output)."""
    sys.setrecursionlimit(100000); m = measure_game(pg.read(path), os.environ.get("DTL_ORDER", "stable"))
    return int(1e12 * m["incomplete"] + 1e11 * (m["hit"] > 0) + 1e8 * min(m["strdiff"], 999)
               + 1e5 * min(m["compared"], 999) + min(m["silent"], 99999))


if __name__ == "__main__":
    sys.setrecursionlimit(100000); tot = {"hit": 0, "strdiff": 0, "compared": 0, "trans": 0, "silent": 0}
    for f in sys.argv[1:]:
        try: g = pg.read(f)
        except Exception: continue
        m = measure_game(g, os.environ.get("DTL_ORDER", "stable"), True, os.path.relpath(f))
        for k in tot: tot[k] += m[k]
        if m["hit"] or m["strdiff"] or m["incomplete"] or m["silent"]: print("FILE", os.path.relpath(f), m, flush=True)
    print("totals:", tot)
