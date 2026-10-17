"""L-ALG succ. 6 (produced on Opus 5.5, 2026-10-17 box 6), GAP-C §18h (FM): search for a best_vertices call that returns −1
while the final round's region union is NOT inside an earlier round's union, with an ARBITRARY set of genuine p-tangles
injected as the stored tangles (as dtl_m_synth.py did for (M)). A hit shows the shape L-RED must make DTL learn; it does
not by itself refute (FM) on A_DTL runs, whose tangle sets come from learning.
Usage: dtl_fmsynth.py SEED COUNT   (prints the first hits and a summary)."""
import sys, os, random, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_pyref as D


def sccs(nodes, succ):
    idx, low, on, st, out, c = {}, {}, set(), [], [], [0]
    def visit(v):
        idx[v] = low[v] = c[0]; c[0] += 1; st.append(v); on.add(v)
        for w in succ(v):
            if w not in nodes: continue
            if w not in idx: visit(w); low[v] = min(low[v], low[w])
            elif w in on: low[v] = min(low[v], idx[w])
        if low[v] == idx[v]:
            C = []
            while True:
                w = st.pop(); on.discard(w); C.append(w)
                if w == v: break
            out.append(C)
    for v in nodes:
        if v not in idx: visit(v)
    return out


def tangles(pr, ow, succ, p, kmax=4, cap=400):
    """Genuine p-tangles of size ≤ kmax: (vertex set, p-strategy) with the restricted graph strongly connected and every
    cycle of p's parity maximum; escapes = opponent edges leaving the set."""
    n = len(pr); found = []
    for k in range(1, kmax + 1):
        for S in itertools.combinations(range(n), k):
            Ss = set(S); pv = [v for v in S if ow[v] == p]
            if any(not any(w in Ss for w in succ[v]) for v in S): continue
            for choice in itertools.product(*[[w for w in succ[v] if w in Ss] for v in pv]):
                st = dict(zip(pv, choice))
                g = lambda v: [st[v]] if ow[v] == p else [w for w in succ[v] if w in Ss]
                comps = sccs(Ss, g)
                if len(comps) != 1: continue
                if k == 1 and S[0] not in g(S[0]): continue
                bad = False
                for q in {pr[v] for v in S if pr[v] % 2 != p}:
                    sub = {v for v in S if pr[v] <= q}
                    for C in sccs(sub, lambda v: [w for w in g(v) if w in sub]):
                        if any(pr[v] == q for v in C) and (len(C) > 1 or C[0] in g(C[0])): bad = True
                if bad: continue
                esc = sorted({w for v in S if ow[v] != p for w in succ[v] if w not in Ss})
                if not esc: continue                       # a dominion, not a stored tangle
                found.append(([(v, st.get(v, -1)) for v in S], esc, max(pr[v] for v in S)))
                if len(found) >= cap: return found
                break
    return found


def rounds_call(d, R, p):
    """dtl_pyref.best_vertices verbatim, returning (result, list of region unions per round)."""
    V = {v for v in R if d.pr[v] % 2 == p}; rs = []
    if not V: return 0, rs
    while True:
        prevV = set(V); Z = set(); CurR = set(R)
        for top in range(d.n - 1, -1, -1):
            if top not in V or top in Z: continue
            CurZ = {top}; d.Q = [top]; d.tattr(p, CurZ, CurR, CurR, d.pr[top], CurR); Z |= CurZ
        rs.append(frozenset(Z))
        cand = [v for v in sorted(V, reverse=True) if not d.attracts(p, v, Z, R)]
        if not cand: return 1, rs
        for t in [0] + [q for q in d.prios if 0 < q <= d.maxpr]:
            d.Q = sorted(Z); d.tattr(p, Z, R, R, t, None); keep = []
            for i, u in enumerate(cand):
                if d.pr[u] <= t: keep += cand[i:]; break
                if not d.attracts(p, u, Z, R): keep.append(u)
            cand = keep
        V -= set(cand)
        if not cand: return 1, rs
        if not V: return -1, rs


if __name__ == "__main__":
    seed, count = int(sys.argv[1]), int(sys.argv[2]); rnd = random.Random(seed); tab = {}; hits = 0
    for it in range(count):
        n = rnd.randint(5, int(os.environ.get("NMAX", "9"))); p = 0
        pr = sorted(rnd.randrange(5) for _ in range(n)); ow = [rnd.randrange(2) for _ in range(n)]
        succ = [sorted(rnd.sample(range(n), rnd.randint(1, 3))) for _ in range(n)]
        cand = tangles(pr, ow, succ, p)
        if not cand: continue
        T = [t for t in cand if rnd.random() < 0.35][:6]
        d = D.DTL(pr, ow, succ); d.tkeys = []
        for vs, esc, top in T:
            k = len(d.tv); d.tv.append(vs); d.tout.append(esc); d.tpr.append(top)
            for e in esc: d.tin[e].append(k)
        res, rs = rounds_call(d, set(range(n)), p)
        if res != -1: tab["not -1"] = tab.get("not -1", 0) + 1; continue
        fm = all(rs[-1] <= z for z in rs)
        mono = all(b <= a for a, b in zip(rs, rs[1:]))
        tab["-1 calls with a MONO failure"] = tab.get("-1 calls with a MONO failure", 0) + (0 if mono else 1)
        tab["-1 calls, FM " + ("holds" if fm else "FAILS")] = tab.get("-1 calls, FM " + ("holds" if fm else "FAILS"), 0) + 1
        if not fm and hits < 3:
            hits += 1
            print("FM FAILS: n", n, "pr", pr, "ow", ow, "succ", succ, "tangles", [(vs, esc, top) for vs, esc, top in T],
                  "rounds", [sorted(z) for z in rs], flush=True)
    print(tab)
