#!/usr/bin/env python3 -I
"""REFEREE scratch tool for R-L1b (docs/lower/L1-statement.md v2 and L1-report.md at claude/l-lower b1abae0).
One-player Büchi games (all vertices Even, priorities {1,2}), all games with <= n vertices, as one big disjoint union.
(1) Winning status W per pointed game (vertex): reachable P_2 vertex on a cycle (independent of Zielonka; cross-checked).
(2) Depth-k bisimulation types by k rounds of refinement; the least k with no type mixing winning and losing vertices is the
    minimal depth of a correct program (Theorem B claims <= 2n-1; Lemma 2.1' claims >= 2n-2).
(3) Lemma 2.1' lasso pair: regions and the depth at which the types first differ, n = 2..7.
(4) Full quotient Q_n; exhaustive search over ALL programs with c Cpre gates (gate i = Cpre of any Boolean function of
    P_2 and the previous Cpre outputs; output = any function of all of them) for small c (B_1 lower bounds, n <= 3).
(5) The lane's witness programs min_b1_n{2,3,4}.json evaluated on Q_n with my interpreter (cost and correctness).
Usage: python3 -I l1bcheck.py [path-to-experiments/lower] [nmax]"""
import sys, os, json, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slpcheck import Game, WE

def union_games(n):
    """All one-player Büchi games with k <= n vertices. Returns flat arrays: pr (1/2), indptr, indices, gameid, W."""
    pr, indptr, indices, W, gid = [], [0], [], [], []
    g = 0
    for k in range(1, n + 1):
        succs = list(range(1, 1 << k))
        for prs in itertools.product((1, 2), repeat=k):
            for succ in itertools.product(succs, repeat=k):
                base = len(pr)
                # winning: reach a P_2 vertex that lies on a cycle (reaches itself)
                reach = [0] * k
                for v in range(k):
                    r = succ[v]
                    while True:
                        nr = r
                        for w in range(k):
                            if (r >> w) & 1: nr |= succ[w]
                        if nr == r: break
                        r = nr
                    reach[v] = r
                good = sum(1 << u for u in range(k) if prs[u] == 2 and (reach[u] >> u) & 1)
                for v in range(k):
                    pr.append(prs[v]); gid.append(g)
                    for w in range(k):
                        if (succ[v] >> w) & 1: indices.append(base + w)
                    indptr.append(len(indices))
                    W.append(1 if (reach[v] & good) else 0)
                g += 1
    return pr, indptr, indices, W, gid

def refine_rounds(pr, indptr, indices, W, kmax):
    """Returns list cls_k (type ids after k rounds) for k = 0..kmax, and per k whether some type is mixed."""
    N = len(pr)
    cls = [p for p in pr]
    out = []
    for k in range(kmax + 1):
        mixed = {}
        for v in range(N):
            t = cls[v]
            m = mixed.get(t, 0)
            mixed[t] = m | (2 if W[v] else 1)
        nmixed = sum(1 for m in mixed.values() if m == 3)
        out.append((cls, len(mixed), nmixed))
        if k == kmax: break
        ids = {}; new = [0] * N
        for v in range(N):
            key = (cls[v], frozenset(cls[w] for w in indices[indptr[v]:indptr[v + 1]]))
            i = ids.get(key)
            if i is None: i = ids[key] = len(ids)
            new[v] = i
        cls = new
    return out

def quotient(pr, indptr, indices, W):
    N = len(pr); cls = [p for p in pr]
    while True:
        ids = {}; new = [0] * N
        for v in range(N):
            key = (cls[v], frozenset(cls[w] for w in indices[indptr[v]:indptr[v + 1]]))
            i = ids.get(key)
            if i is None: i = ids[key] = len(ids)
            new[v] = i
        if len(ids) == len(set(cls)): cls = new; break
        cls = new
    Q = len(set(cls)); qpr = [0] * Q; qsucc = [set() for _ in range(Q)]; qW = [None] * Q
    for v in range(N):
        c = cls[v]; qpr[c] = pr[v]
        for w in indices[indptr[v]:indptr[v + 1]]: qsucc[c].add(cls[w])
        assert qW[c] in (None, W[v]), "W not bisimulation invariant?!"
        qW[c] = W[v]
    return qpr, [sorted(s) for s in qsucc], qW

def diamond(qsucc, X):
    return [1 if any(X[w] for w in qsucc[v]) else 0 for v in range(len(qsucc))]

def exhaustive(qpr, qsucc, qW, c):
    """Is there a program with c Cpre gates solving all of Q? Chain: s_i = <>f_i(P2, s_1..s_{i-1}), f_i any Boolean function."""
    Q = len(qpr); P2 = [1 if p == 2 else 0 for p in qpr]
    def rec(i, feats):   # feats: list of bit-vectors available (P2, s_1..s_{i-1})
        # output test
        table = {}
        ok = True
        for v in range(Q):
            key = tuple(f[v] for f in feats)
            if table.setdefault(key, qW[v]) != qW[v]: ok = False; break
        if ok: return True
        if i > c: return False
        m = len(feats)
        for tt in range(1 << (1 << m)):            # truth table of f_i over m inputs
            arg = [ (tt >> sum(feats[j][v] << j for j in range(m))) & 1 for v in range(Q)]
            s = diamond(qsucc, arg)
            if rec(i + 1, feats + [s]): return True
        return False
    return rec(1, [P2])

def run_json(path, qpr, qsucc, qW):
    prog = json.load(open(path))["program"]
    Q = len(qpr); val = []
    cost = 0
    for gte in prog:
        k = gte[0]
        if k == "P": val.append([1 if p == gte[1] else 0 for p in qpr])
        elif k == "VE": val.append([1] * Q)
        elif k == "EMPTY": val.append([0] * Q)
        elif k == "or": val.append([a | b for a, b in zip(val[gte[1]], val[gte[2]])])
        elif k == "and": val.append([a & b for a, b in zip(val[gte[1]], val[gte[2]])])
        elif k == "not": val.append([1 - a for a in val[gte[1]]])
        elif k == "cpre": val.append(diamond(qsucc, val[gte[1]])); cost += 1
        else: raise ValueError(gte)
    bad = sum(1 for v in range(Q) if val[-1][v] != qW[v])
    return cost, bad

def lasso_pair(n):
    # G^cyc: a_1..a_n cycle, pr(a_{n-1}) = 2; G^tail: a_1..a_{n-1} -> z -> z, pr(z) = 1
    prc = [1] * n; prc[n - 2] = 2; succ_c = [1 << ((i + 1) % n) for i in range(n)]
    prt = [1] * n; prt[n - 2] = 2; succ_t = [1 << (i + 1) for i in range(n - 1)] + [1 << (n - 1)]
    gc, gt = Game(n, (1 << n) - 1, prc, succ_c), Game(n, (1 << n) - 1, prt, succ_t)
    assert WE(gc) == gc.ALL and not (WE(gt) & 1), "regions"
    # types on the union of the two games
    pr = prc + prt; indptr = [0]; indices = []
    for i in range(n):
        indices += [j for j in range(n) if (succ_c[i] >> j) & 1]; indptr.append(len(indices))
    for i in range(n):
        indices += [n + j for j in range(n) if (succ_t[i] >> j) & 1]; indptr.append(len(indices))
    W = [1] * n + [0] * n
    rounds = refine_rounds(pr, indptr, indices, W, 2 * n)
    first_differ = next(k for k, (cls, _, _) in enumerate(rounds) if cls[0] != cls[n])
    return first_differ

def main():
    lane = sys.argv[1] if len(sys.argv) > 1 else None
    nmax = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    for n in range(2, 8):
        print(f"Lemma 2.1' pair n={n}: regions OK; depth-k types of the roots first differ at k = {lasso_pair(n)} (claim: 2n-2 = {2*n-2})")
    for n in range(1, nmax + 1):
        pr, indptr, indices, W, gid = union_games(n)
        # cross-check W against Zielonka on all games (n <= 3) / every 97th game (n = 4)
        bad = 0; g = -1; checked = 0
        for v in range(len(pr)):
            if gid[v] == g: continue
            g = gid[v]
            if n == 4 and g % 97: continue
            vs = [u for u in range(v, len(pr)) if gid[u] == g]; k = len(vs)
            game = Game(k, (1 << k) - 1, [pr[u] for u in vs], [sum(1 << (w - v) for w in indices[indptr[u]:indptr[u + 1]]) for u in vs])
            we = WE(game); checked += 1
            if any(((we >> i) & 1) != W[vs[i]] for i in range(k)): bad += 1
        rounds = refine_rounds(pr, indptr, indices, W, 2 * n)
        mind = next((k for k, (_, _, nm) in enumerate(rounds) if nm == 0), None)
        print(f"n={n}: {len(pr)} pointed games; W vs Zielonka mismatches {bad} on {checked} games; types per depth "
              f"{[t for _, t, _ in rounds]}; mixed per depth {[nm for _, _, nm in rounds]}; minimal depth = {mind} "
              f"(Lemma 2.1': >= {2*n-2}; Theorem B: <= {2*n-1})", flush=True)
        qpr, qsucc, qW = quotient(pr, indptr, indices, W)
        print(f"  quotient Q_{n}: {len(qpr)} classes (lane: 2, 14, 442, 48062)")
        if n <= 3:
            for c in range(0, 2 * n - 2):   # UNSAT side only; SAT at 2n-2 is the lane witness
                print(f"  exhaustive: program with {c} Cpre gates solving Q_{n}? {exhaustive(qpr, qsucc, qW, c)}", flush=True)
        if lane:
            path = os.path.join(lane, f"min_b1_n{n}.json")
            if os.path.exists(path):
                cost, bad = run_json(path, qpr, qsucc, qW)
                print(f"  lane witness {os.path.basename(path)}: cost {cost}, mismatches on Q_{n}: {bad}")

if __name__ == "__main__":
    main()
