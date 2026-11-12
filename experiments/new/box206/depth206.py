#!/usr/bin/env python3
"""Box 206 (L-NEW successor 70): CHANGE DEPTH of class changes on IDEAL-CYC(G) (box191 idealcyc via box203 gfc203.hist_ideal).
For a vertex v and a step t with Lambda_(t-1)(v) = Lambda_t(v) and E_(t-1)(v) != E_t(v) (E = the e-vertices of Pi, R118/R121):
  z := the most relevant element of E_(t-1) Δ E_t;  depth := #elements of E_(t-1) ∪ E_t more relevant than z (0 = the top changes).
Lemma DEPTH-COUNT (box 206 §1): on an interval of states with Lambda(v) fixed, if every change has depth <= c, the set P_t of the
c + 1 most relevant elements of E_t strictly rises (lexicographically) at every change, so #changes <= sum_(j=0..c+1) C(m, j) - 1.
Counters (TOTALS, unit (vertex, step) unless stated): lam (Lambda changes), ch (E changes at fixed Lambda), d0..d9 (by depth, 9 = 9+),
maxdepth (max depth over all changes), elfall (E falls at fixed Lambda: must be 0, RESULTS R121 E-MON), topfall (top of E falls at fixed
Lambda: must be 0), pfail (P_t, c := max depth on the vertex's Lambda-interval, does not strictly rise at a change: must be 0),
ufail (unconditional form, c0 = 0, 1, 2: P^(c0) does not strictly
rise at a change of depth <= c0, or changes at a change of depth > c0; unit (change, c0): must be 0), cfail (unit (vertex, Lambda-interval): #changes > sum_(j<=c+1) C(m, j) - 1: must be 0); maxdeep_v (max over vertices of the number of
changes of depth >= 1), loud (unit: steps at which some vertex changes class), L-1/L0/L1.. (loud steps by their LOUD DEPTH := the least
change depth over the vertices changing class at that step, -1 if some Lambda changes), maxloud (max loud depth), maxDE (max over vertices and Lambda-intervals of the number of distinct E). Scope: movers (default) or all
vertices (DEP_ALL=1). Control DEP_CTRL=1: relevance reversed (least relevant element first): elfall and topfall must fire.
Usage: depth206.py G.json ... | depth206.py --rand {k1,k2,rand} SEED COUNT [dump.json: first genome with maxdepth >= DEP_DUMP]"""
import sys, os, json, collections, random
from math import comb
ROOT = os.environ.get("ROOT") or os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path[:0] = [os.path.join(ROOT, p) for p in ("experiments/new/box203", "experiments/new/box202", "experiments/new/box191")]
import gfc203
CTRL = os.environ.get("DEP_CTRL", "0"); ALL = os.environ.get("DEP_ALL") == "1"

def census(G, c=None):
    c = collections.Counter() if c is None else c
    H, n, E, V, gates = gfc203.hist_ideal(G); T = len(H) - 1
    ebits = sorted(E.rank[v] for k, v in V.items() if isinstance(k, tuple) and k[0] == "e"); m = len(ebits)
    pos = {r: i for i, r in enumerate(ebits)}                       # e-vertex rank -> position 0..m-1 (relevance order)
    def es(mask):                                                  # E as an int over positions (bit i = i-th least relevant e)
        x = 0
        for r in ebits:
            if (mask >> r) & 1: x |= 1 << (pos[r] if CTRL != "1" else m - 1 - pos[r])
        return x
    who = range(n) if ALL else [V[("x", x)] for x in range(G["N"])]
    gmax = 0; stepmin = [None] * (T + 1)          # per step: min over vertices of the change depth (-1: some Lambda change)
    def note(t, d): stepmin[t] = d if stepmin[t] is None else min(stepmin[t], d)
    for v in who:
        seq = [(H[t][0][v][0], es(H[t][0][v][1])) for t in range(T + 1)]
        ivs = []; cur = [0]
        for t in range(1, T + 1):
            if seq[t][0] != seq[t - 1][0]: c["lam"] += 1; ivs.append(cur); cur = [t]; note(t, -1)
            else: cur.append(t)
        ivs.append(cur); deep = 0
        for iv in ivs:
            dep = []
            for a, b in zip(iv, iv[1:]):
                e0, e1 = seq[a][1], seq[b][1]
                if e0 == e1: continue
                z = (e0 ^ e1).bit_length() - 1
                if (e0 >> z) & 1: c["elfall"] += 1
                if e1.bit_length() < e0.bit_length(): c["topfall"] += 1
                d = bin((e0 | e1) >> (z + 1)).count("1"); dep.append((a, b, d)); note(b, d); c["ch"] += 1; c["d%d" % min(d, 9)] += 1
                gmax = max(gmax, d); deep += d >= 1
            c["maxDE"] = max(c["maxDE"], len({seq[t][1] for t in iv}))
            if not dep: continue
            cc = max(d for _, _, d in dep)
            def top(x, k):
                out = 0
                while x and k: hb = 1 << (x.bit_length() - 1); out |= hb; x ^= hb; k -= 1
                return out
            for a, b, d in dep:
                pa, pb = top(seq[a][1], cc + 1), top(seq[b][1], cc + 1)
                zz = (pa ^ pb).bit_length() - 1
                if pa == pb or not (pb >> zz) & 1: c["pfail"] += 1
            if len(dep) > sum(comb(m, j) for j in range(cc + 2)) - 1: c["cfail"] += 1
            for c0 in range(3):                    # unconditional form: P^(c0) rises strictly at depth <= c0, is unchanged at depth > c0
                for a, b, d in dep:
                    pa, pb = top(seq[a][1], c0 + 1), top(seq[b][1], c0 + 1)
                    zz = (pa ^ pb).bit_length() - 1
                    if (d <= c0 and (pa == pb or not (pb >> zz) & 1)) or (d > c0 and pa != pb): c["ufail"] += 1
        c["maxdeep_v"] = max(c["maxdeep_v"], deep)
    for t in range(1, T + 1):
        if stepmin[t] is not None: c["loud"] += 1; c["L%d" % min(stepmin[t] + 1, 9)] += 1; c["maxloud"] = max(c["maxloud"], stepmin[t])
    c["maxdepth"] = max(c["maxdepth"], gmax); c["T"] = max(c["T"], T); c["sumT"] += T
    return c, gmax

KEYS = ("sumT", "T", "lam", "ch", "elfall", "topfall", "pfail", "cfail", "ufail", "maxdepth", "maxdeep_v", "maxDE", "loud", "maxloud")
def show(name, c):
    print(name, "ctrl", CTRL, "all" if ALL else "movers", " ".join(f"{k} {c[k]}" for k in KEYS), "|",
          " ".join(f"d{i} {c['d%d' % i]}" for i in range(10) if c["d%d" % i]), "|",
          " ".join(f"L{i - 1} {c['L%d' % i]}" for i in range(10) if c["L%d" % i]), flush=True)

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--rand":
        mode, seed, cnt = a[1], int(a[2]), int(a[3]); dump = a[4] if len(a) > 4 else None
        rng = random.Random(seed); c = collections.Counter(); hist = collections.Counter()
        import rand191, fvs202
        os.environ["K1_MODE"] = "2" if mode == "k2" else "1"
        import k1srch202
        while c["genomes"] < cnt:
            if mode == "rand": G = rand191.rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3))
            else:
                G = k1srch202.mk(rng)
                if G is None or fvs202.kfvs(G)[0] != (2 if mode == "k2" else 1): continue
            c["genomes"] += 1; _, g = census(G, c); hist[g] += 1
            if dump and g >= int(os.environ.get("DEP_DUMP", "99")) and not os.path.exists(dump): json.dump(G, open(dump, "w"))
        show(f"{mode} seed {seed} genomes {c['genomes']}", c)
        print("  genomes by maxdepth:", dict(sorted(hist.items())), flush=True)
    else:
        for f in a: c, _ = census(json.load(open(f))); show(os.path.basename(f), c)
