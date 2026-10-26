#!/usr/bin/env python3
"""L-SI box 17: DATA for Lemma PIECE_D and Corollary SPLIT-RED (docs/si/N5-RUND-box17.md §11). At a state k, an Even edge (x, z),
z != a := sigma_k(x), is SPLIT if it is improving in exactly one frame: [Xi_k(z) > Xi_k(a)] != [W_k(z) > W_k(a)] (S1 order, strict).
A state is SPLIT if it has a split edge; FORBIDDEN if some edge is W-improving but not Xi-improving (IW ⊄ IX); EXTRA if IX ⊄ IW. Split edges are classed: cyc (different cycle nodes in a frame), offset (same cycle node,
Delta(z) != Delta(a)), length (same cycle node, equal offsets: the path-set comparison agrees, so lengths decide).
Along every maximal fallback-free in-phase run S (n5x.py step, read-only) with (h3_D) at every state it checks:
  ARENA_V  at a non-split state k, Iσ_k (SPEC S2 on Xi) != the improving set of sigma_k in G_tau (W): PIECE_D's first step predicts 0
  BLOCK_V  a maximal block of consecutive transitions with non-split source states has >= n + m transitions (R17 (c) predicts 0)
  RED_V    |S| > N_split + (N_split + 1)(n + m - 1) (Corollary SPLIT-RED predicts 0)
and reports N_split per run, the split-edge classes, and the share of split states. MUT=1: the block bound n + m is replaced by 2
(control; must fail on long blocks). Usage: piece.py --list FILE [KMIN] | --rand COUNT NLO NHI SEED | --one GAME [START]  (NMAX, RS env)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "fb2o"))
from n5x import step, start_pair, Engine, dual, load, readstart
from tcdir import lasso, wval
MUT = os.environ.get("MUT") == "1"
C = Counter(); VIOL = []; TOP = []

def check(g, name, start=None):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    m = sum(len(set(x)) for x in g.succ)
    while len(rows) <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        D = [u for u in range(g.n) if g.owner[u] == 1 and sb[u] != t[u]]
        wn = (lambda s, t: (lambda v: s[v] if g.owner[v] == 0 else t[v]))(list(s), tuple(t))
        W = [wval(E, wn, v) for v in range(g.n)]
        h3 = all(vs[u][0] == W[u][0] for u in D)
        off = [E.weight(W[v][1]) - E.weight(vs[v][1]) for v in range(g.n)]
        IX, IW, cls = set(), set(), Counter()
        for x in range(g.n):
            if g.owner[x] != 0: continue
            a = s[x]
            for z in set(g.succ[x]):
                if z == a: continue
                ix = E.key(vs[z]) > E.key(vs[a]); iw = E.key(W[z]) > E.key(W[a])
                if ix: IX.add((x, z))
                if iw: IW.add((x, z))
                if ix != iw:
                    if vs[z][0] != vs[a][0] or W[z][0] != W[a][0]: cls["cyc"] += 1
                    elif off[z] != off[a]: cls["offset"] += 1
                    else: cls["length"] += 1
        Is = set(r[2]) if r else set()
        rows.append(dict(key=(tuple(x[0] for x in vs), tuple(t)), h3=h3, split=IX != IW, forb=not IW <= IX, extra=not IX <= IW, IX=IX, IW=IW, Is=Is, cls=cls,
                         fb=r[4] if r else 0, D=len(D)))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and not rows[j]["fb"] and rows[j + 1]["key"] == rows[i]["key"]: j += 1
        if j > i and all(rows[x]["h3"] for x in range(i, j + 1)): run(g, m, name, rows, i, j)
        i = j + 1

def run(g, m, name, rows, i, j):
    T = j - i; C["runs"] += 1; C["trans"] += T
    srcs = range(i, j)                                          # source states of the run's transitions
    nsplit = sum(rows[k]["split"] for k in srcs)
    C["split_states"] += nsplit; C["runs_with_split"] += nsplit > 0
    nforb = sum(rows[k]["forb"] for k in srcs); C["forb_states"] += nforb; C["extra_states"] += sum(rows[k]["extra"] for k in srcs)
    C["max_forb_run"] = max(C["max_forb_run"], nforb); C["runs_with_forb"] += nforb > 0
    for k in srcs:
        for c, v in rows[k]["cls"].items(): C["edges_" + c] += v
        if rows[k]["IX"] != rows[k]["Is"]: C["SPEC_MISMATCH"] += 1     # sanity: our Xi-improving set is n5x's Is
        if not rows[k]["split"] and rows[k]["IX"] != rows[k]["IW"]: C["ARENA_V"] += 1; VIOL.append(("ARENA", name, k))
    blk, cap = 0, (2 if MUT else g.n + m)
    for k in srcs:
        if rows[k]["split"]: blk = 0; continue
        blk += 1; C["max_block"] = max(C["max_block"], blk)
        if blk >= cap: C["BLOCK_V"] += 1; VIOL.append(("BLOCK", name, i, k, blk, cap)); blk = 0
    if T > nsplit + (nsplit + 1) * (g.n + m - 1): C["RED_V"] += 1; VIOL.append(("RED", name, i, j))
    C["max_split_run"] = max(C["max_split_run"], nsplit)
    if T >= C["max_T"]: C["max_T"] = T; TOP.append((name, i, j, g.n, "T", T, "split", nsplit, "maxD", max(rows[x]["D"] for x in range(i, j + 1))))

def main():
    a = sys.argv[1:]
    if a[0] == "--one":
        g = load(a[1]); check(g, a[1], readstart(a[2]) if len(a) > 2 else None)
    elif a[0] == "--rand":
        sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box43")); from multi import rand_ckO
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); i = 0; K = int(os.environ.get("K", "0"))
        while i < cnt:
            g = rand_ckO(rng, lo, hi, K or rng.choice((2, 2, 3, 4)))
            if g is None: continue
            i += 1
            st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1})
            check(g, f"rand seed {seed} #{i}", None if i % 2 else st)
    else:
        kmin = int(a[2]) if len(a) > 2 else 2
        for line in open(a[1]):
            f = line.strip()
            if not f: continue
            g = load(os.path.join(ROOT, f))
            if g.n > int(os.environ.get("NMAX", "48")) or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin:
                continue
            check(g, f); rng = random.Random(f)
            for _ in range(int(os.environ.get("RS", "0"))):
                check(g, f + " rs", ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                     {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}))
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for x in TOP[-6:]: print("TOP", x)
    for v in VIOL[:10]: print("VIOLATION", v)
    print("PIECE PASS" if not VIOL else "PIECE FAIL")

if __name__ == "__main__":
    main()
