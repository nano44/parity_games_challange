#!/usr/bin/env python3
"""L-SI box 16 (successor 11): DATA for P-N5-1E. N5 (experiments/new/n5.py run(), read-only import) from the S3 start and random start
pairs; at the stop, check SPEC S5's output from definitions on EVERY game class:
  (Z)  W (Even iff the cycle node of Xi_sigma has even priority) = own Zielonka's W_E;
  (SE) Even's output strategy (sigma on Even vertices of W) wins every vertex of W: in G with Even fixed to it on W, no Odd edge leaves W,
       no Even choice leaves W, and no odd-priority t in W lies on a cycle of the subgraph of W on priorities <= prio(t);
  (SO) the same for Odd's output strategy (sigma-bar on Odd vertices of V \\ W), with even t;
  (B)  on C^1E (exactly one Even choice vertex e): ITER <= (n(n-1)+d_e)(T*(n,m,Delta,d_e)+1), T* as in RESULTS R51 (a) with f := 2n^2.
MUT=1 reads the output at the start pair instead (a mutation control; it must FAIL).
Usage: outcheck.py --rand COUNT NMIN NMAX SEED CLASS   (CLASS: any | 1E | 1O)   |   outcheck.py --list FILELIST [--starts K]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "new")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg, n5

def attr(g, S, pl, sub):
    A = set(S); ch = True
    while ch:
        ch = False
        for v in sub:
            if v in A: continue
            s = [w for w in g.succ[v] if w in sub]
            if (g.owner[v] == pl and any(w in A for w in s)) or (g.owner[v] != pl and s and all(w in A for w in s)):
                A.add(v); ch = True
    return A

def zielonka(g, sub):
    if not sub: return set(), set()
    p = max(g.prio[v] for v in sub); pl = p % 2
    A = attr(g, {v for v in sub if g.prio[v] == p}, pl, sub)
    W = zielonka(g, sub - A)
    if not W[1 - pl]:
        r = [None, None]; r[pl] = set(sub); r[1 - pl] = set(); return tuple(r)
    B = attr(g, W[1 - pl], 1 - pl, sub)
    W2 = zielonka(g, sub - B)
    r = [None, None]; r[pl] = W2[pl]; r[1 - pl] = W2[1 - pl] | B; return tuple(r)

def wins(g, region, pl, strat):
    """pl's positional strat (on pl's vertices of region) wins every vertex of region: plays stay in region, no cycle of the other parity."""
    R = set(region)
    succ = {}
    for v in R:
        if g.owner[v] == pl:
            if strat[v] is None or strat[v] not in R or strat[v] not in g.succ[v]: return False
            succ[v] = [strat[v]]
        else:
            if any(w not in R for w in g.succ[v]): return False
            succ[v] = list(set(g.succ[v]))
    for t in R:
        if g.prio[t] % 2 == pl: continue
        lo = {v for v in R if g.prio[v] <= g.prio[t]}
        st, seen = [w for w in succ[t] if w in lo], set()
        while st:
            x = st.pop()
            if x == t: return False
            if x in seen: continue
            seen.add(x); st.extend(w for w in succ[x] if w in lo)
    return True

def tstar(n, m, D, d):
    F = 2 * n * n; TH = n * n + 2 * n - 1
    XSN = 13 * (d + 1) * n ** 3 * (F + 1 + TH) + TH; X = (F + 1) * (n - 1) + F + XSN
    Th = (n - 1) + n * (X + 1) + X; So = d * (Th + 1); Wch = (F + X + 1) * n * n; Nst = 1 + X + Th + Wch
    NXi = F + Nst + (X + 1) * (n - 1) + (Nst + F) * 3 * D * n ** 4
    return (m - n + 1) * (So + NXi + 1)

def choice(g, pl): return [v for v in range(g.n) if g.owner[v] == pl and len(set(g.succ[v])) > 1]

def randgame(rng, n, cls):
    while True:
        owner = [rng.randint(0, 1) for _ in range(n)]
        prio = [rng.randint(0, n) for _ in range(n)]
        succ = []
        one = {"1E": 0, "1O": 1}.get(cls)
        cands = [v for v in range(n) if owner[v] == one] if one is not None else []
        if one is not None and not cands: continue
        c = rng.choice(cands) if cands else None
        for v in range(n):
            k = 1 if (one is not None and owner[v] == one and v != c) else rng.randint(2 if v == c else 1, min(n, 4))
            succ.append(sorted(rng.sample(range(n), k)))
        g = pg.Game(prio, owner, succ)
        if one is None or len(choice(g, one)) == 1: return g

def randstart(rng, g):
    return ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1})

MUT = os.environ.get("MUT") == "1"   # mutation control: read the output at the START pair (cap 0), not at the stop

def check(g, start, tag, tot):
    it, fb, win, ws, _ = n5.run(g, "n5", start)
    if MUT: _, _, win, ws, _ = n5.run(g, "n5", start, cap=0)
    WE, WO = zielonka(g, set(range(g.n)))
    W = {v for v in range(g.n) if win[v] == 0}
    ok = {"Z": W == WE, "SE": wins(g, W, 0, ws), "SO": wins(g, set(range(g.n)) - W, 1, ws)}
    es = choice(g, 0)
    if len(es) == 1:
        e = es[0]; D = max(len(set(s)) for s in g.succ); de = len(set(g.succ[e]))
        bnd = (g.n * (g.n - 1) + de) * (tstar(g.n, g.m, D, de) + 1)
        ok["B"] = it <= bnd; tot["1E"] += 1; tot["maxit1E"] = max(tot["maxit1E"], it)
    tot["runs"] += 1; tot["maxit"] = max(tot["maxit"], it)
    for k, v in ok.items():
        if not v: tot["viol"] += 1; print(f"VIOLATION {k} {tag}", flush=True)

def main():
    a = sys.argv[1:]; tot = {"runs": 0, "viol": 0, "1E": 0, "maxit": 0, "maxit1E": 0}
    if a[0] == "--rand":
        cnt, lo, hi, seed, cls = int(a[1]), int(a[2]), int(a[3]), int(a[4]), a[5]
        rng = random.Random(seed)
        for i in range(cnt):
            g = randgame(rng, rng.randint(lo, hi), cls)
            check(g, None if i % 2 == 0 else randstart(rng, g), f"rand{cls} seed {seed} game {i}", tot)
    else:
        K = int(a[a.index("--starts") + 1]) if "--starts" in a else 1
        rng = random.Random(16)
        root = os.path.join(HERE, "..", "..", "..")
        for line in open(a[1]):
            f = line.strip()
            if not f: continue
            g = pg.parse("".join(l for l in open(os.path.join(root, f)) if not l.lstrip().startswith("%")))
            for j in range(K):
                check(g, None if j == 0 else randstart(rng, g), f"{f} start {j}", tot)
    print(f"runs {tot['runs']}: violations {tot['viol']}; C^1E runs {tot['1E']} (max ITER {tot['maxit1E']}); max ITER {tot['maxit']}")
    print("OUTCHECK PASS" if tot["viol"] == 0 else "OUTCHECK FAIL")

if __name__ == "__main__":
    main()
