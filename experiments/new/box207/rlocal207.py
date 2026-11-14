#!/usr/bin/env python3
"""Box 207 (L-NEW successor 71): the feedback vertex R at Xi-feedback number k = 1 on IDEAL-CYC (box203 gfc203.hist_ideal).
For each feedback vertex R (a mover whose removal makes the Xi-graph acyclic; fvs202), the R-INTERVALS are the maximal runs of states with
class(R) = (Lambda(R), E(R)) constant; the step that changes class(R) is counted in the interval it ends. Reported for the feedback vertex
with the smallest (cint, loudint) (DATA, descriptive): DR = D^tot(R) (= number of intervals), cint (max over intervals and vertices of
the vertex's class changes in the interval), loudint (max loud steps in one interval), flipint (max flips of one gate in one interval),
Rint (max R-labelled steps of R118 in one interval), deepnoR (loud steps of loud depth > 1 at which class(R) does not change; the naive
race-flip charge), efail (steps with no Lambda change at which some gate flips to its e-face and class(R) does not change; EFLIP-R),
pR (p-steps of R118 at which class(R) changes).
Must-0 counters: rrep (class(R) takes a value it had before and left: (C1) of P-N5-QN, R118 (e) + R121 E-MON), ifail (#intervals != DR),
qfail (Lemma R-LOCAL's bound T <= Q + (Q + 1) * N with Q := sum of loud steps over the intervals <= DR * loudint fails).
Control RL_CTRL=1: the face of the gate with most flips replaces class(R) (it alternates, so rrep must fire).
Usage: rlocal207.py G.json ... | rlocal207.py --rand SEED COUNT"""
import sys, os, json, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(HERE, "..", d) for d in ("box203", "box202", "box191")]
import gfc203, fvs202
CTRL = os.environ.get("RL_CTRL") == "1"

def fvsets(G):
    adj = fvs202.xigraph(G); nodes = set(adj); out = []
    for x in sorted(nodes):
        rest = nodes - {x}
        if not fvs202.cyclic_parts({a: [b for b in adj[a] if b in rest] for a in rest}, rest): out.append(x)
    return out

def census(G):
    H, n, E, V, gates = gfc203.hist_ideal(G); T = len(H) - 1
    import idealcyc
    ST = idealcyc.run(G)
    ebits = sorted(E.rank[v] for k, v in V.items() if isinstance(k, tuple) and k[0] == "e"); pos = {r: i for i, r in enumerate(ebits)}
    em = 0
    for r in ebits: em |= 1 << r
    def es(mask):
        x = 0
        for r in ebits:
            if (mask >> r) & 1: x |= 1 << pos[r]
        return x
    cls = [[(H[t][0][v][0], es(H[t][0][v][1])) for t in range(T + 1)] for v in range(n)]
    ch = [[v for v in range(n) if cls[v][t] != cls[v][t - 1]] for t in range(1, T + 1)]
    lam = [any(cls[v][t][0] != cls[v][t - 1][0] for v in range(n)) for t in range(1, T + 1)]
    fl = [[g for g in gates if H[t][1][g] != H[t - 1][1][g]] for t in range(1, T + 1)]
    lab = ["C" if lam[t - 1] else ("R" if fl[t - 1] else "p") for t in range(1, T + 1)]
    ld = [None] * (T + 1)                                      # loud depth per step (-1: some Lambda changes)
    for t in range(1, T + 1):
        for v in ch[t - 1]:
            a, b = cls[v][t - 1], cls[v][t]
            d = -1 if a[0] != b[0] else bin((a[1] | b[1]) >> ((a[1] ^ b[1]).bit_length())).count("1")
            ld[t] = d if ld[t] is None else min(ld[t], d)
    best = None
    for R in fvsets(G):
        r = V[("x", R)]
        gm = max(gates, key=lambda g: sum(g in f for f in fl)) if gates else None
        rc = [H[t][1][gm] for t in range(T + 1)] if CTRL else cls[r]
        chg = [rc[t] != rc[t - 1] for t in range(1, T + 1)]
        iv = 0; cv = collections.Counter(); li = collections.Counter(); fi = collections.Counter(); ri = collections.Counter()
        for t in range(1, T + 1):
            for v in ch[t - 1]: cv[(iv, v)] += 1
            if ch[t - 1]: li[iv] += 1
            for g in fl[t - 1]: fi[(iv, g)] += 1
            if lab[t - 1] == "R": ri[iv] += 1
            if chg[t - 1]: iv += 1
        seen = set(); rrep = 0
        for t in range(T + 1):
            if t and rc[t] != rc[t - 1] and rc[t] in seen: rrep += 1
            seen.add(rc[t])
        DR = len(set(rc)); Q = sum(li.values())
        r_ = dict(R=R, DR=DR, cint=max(cv.values(), default=0), loudint=max(li.values(), default=0), flipint=max(fi.values(), default=0),
                  Rint=max(ri.values(), default=0),
                  deepnoR=sum(1 for t in range(1, T + 1) if ld[t] is not None and ld[t] > 1 and not chg[t - 1]),
                  efail=sum(1 for t in range(1, T + 1) if not lam[t - 1] and not chg[t - 1] and any(H[t][1][g] == gates[g][1] for g in fl[t - 1])),
                  pR=sum(1 for t in range(1, T + 1) if lab[t - 1] == "p" and chg[t - 1]),
                  rrep=rrep, ifail=int(iv + 1 != DR), qfail=int(T > Q + (Q + 1) * G["N"] or Q > DR * max(li.values(), default=0)))
        key = (r_["cint"], r_["loudint"])
        if best is None or key < best[0]: best = (key, r_)
    return T, best[1] if best else None

KEYS = ("R", "DR", "cint", "loudint", "flipint", "Rint", "deepnoR", "efail", "pR", "rrep", "ifail", "qfail")
if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--rand":
        os.environ["K1_MODE"] = "1"; import k1srch202
        rng = random.Random(int(a[1])); cnt = int(a[2]); g = 0; mx = collections.Counter(); tot = collections.Counter()
        while g < cnt:
            G = k1srch202.mk(rng)
            if G is None or fvs202.kfvs(G)[0] != 1: continue
            g += 1; T, r = census(G)
            for k in ("DR", "cint", "loudint", "flipint", "Rint"): mx[k] = max(mx[k], r[k])
            for k in ("deepnoR", "efail", "pR", "rrep", "ifail", "qfail"): tot[k] += r[k]
            mx["T"] = max(mx["T"], T)
        print("rand k1 seed", a[1], "genomes", g, "max", dict(mx), "TOTALS", " ".join("%s %d" % (k, tot[k]) for k in ("deepnoR", "efail", "pR", "rrep", "ifail", "qfail")), flush=True)
    else:
        for f in a:
            T, r = census(json.load(open(f)))
            print(os.path.basename(f), "T", T, " ".join("%s %s" % (k, r[k]) for k in KEYS), flush=True)
