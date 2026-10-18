"""L-ALG succ. 10 (box 13, produced on Opus 5.5), GAP-A-M §34: the transitions whose depth-0 states (R_j, rank_j, V_j) are IDENTICAL in
consecutive searches (88-104 on the two-player library, 0 on 𝒞^1P). For each, the first differing best_vertices call over ALL depths
(calls listed in execution order with (depth, R, result, rounds, V)): its depth, whether the call itself differs (outcome) or only its
context R (the difference arose in a piece, a recursion input or sptl), and the transition's phase length. Also: whether the two
searches have the same call sequence entirely (then the difference is in tangle extraction only).
TREE=1 also tests (TREE-NEW): every transition gives some vertex a new key (v, depth, rank, |R|, |V|) over the contexts of ALL
calls containing it, and (TREE-PIECE): the same with the call's PIECE and its position in the parent call (b12_pot's full key,
at every depth).
Usage: DTL_ORDER=stable|oink [NMAX=n | CLASS=1 DIST=1] [TREE=1] b12_ident.py G.pg ...
   or: DTL_ORDER=... b12_ident.py climb START.pg STEPS SEED OUTDIR   (two-player climb against (TREE-PIECE))"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, fixd_stealentry as SE, b12_pot as B
from b12_fdkey import plain
from b12_topchain import classgames


class AC(B.CH):
    def best_vertices(self, V, R, p):
        Rk = frozenset(R); res = B.CH.best_vertices(self, V, R, p)
        if hasattr(self, "calls"):
            if not hasattr(self, "allc"): self.allc = {}
            self.allc.setdefault(id(self.calls), []).append((getattr(self, "_dep", 0), Rk, res, len(self._vr) if res else 0, frozenset(V)))
        return res


def run(g, order):
    saved = SE.SE; SE.SE = AC
    try:
        return SE.run(g, order)
    finally:
        SE.SE = saved


def treekeys(calls, n):
    """keys (v, depth, rank, |R|, |V|) for every vertex v of every best_vertices call's context, all depths."""
    return {(v, dep, n + 2 if res == 1 else (e if res == -1 else 0), len(R), len(V)) for dep, R, res, e, V in calls for v in R}


def treepieces(calls, n):
    """keys (v, depth, position within the parent call, rank, |R|, |V|) for v in the call's PIECE: R minus the context of the next
    call at the same depth before the recursion returns to a shallower depth (all of R if there is none)."""
    out = set(); pos = {}
    for i, (dep, R, res, e, V) in enumerate(calls):
        for dd in [x for x in pos if x > dep]: del pos[dd]
        j = pos.get(dep, -1) + 1; pos[dep] = j
        nxt = next((calls[k][1] for k in range(i + 1, len(calls)) if calls[k][0] <= dep), None)
        nxt = nxt if nxt is not None and next(calls[k][0] for k in range(i + 1, len(calls)) if calls[k][0] <= dep) == dep else frozenset()
        r = n + 2 if res == 1 else (e if res == -1 else 0)
        out |= {(v, dep, j, r, len(R), len(V)) for v in R - nxt}
    return out


def treenew(d, n, keyf=None):
    """(transitions, transitions with no new tree key, first)"""
    log = getattr(d, "log", []); allc = getattr(d, "allc", {}); tr = bad = 0; ex = None; seen = None; prev = None
    for ph, calls in log:
        k = (keyf or treekeys)(allc.get(id(calls), []), n)
        if prev is not None and prev == ph:
            tr += 1
            if not (k - seen): bad += 1; ex = ex or ph
        if prev != ph: seen = set()
        seen |= k; prev = ph
    return tr, bad, ex


def tp_score(g, order):
    """(transitions without a new TREE-PIECE key, −(fewest vertices with a new key at one transition), transitions, searches).
    With PLUS=1 ((TREE-PIECE⁺)): transitions whose call sequence (depth, R, rank, V) is identical are skipped (§34c)."""
    d = run(g, order); log = getattr(d, "log", []); allc = getattr(d, "allc", {}); bad = tr = 0; marg = g.n + 1; seen = set(); prev = None
    plus = os.environ.get("PLUS") == "1"; pcalls = None
    for ph, calls in log:
        A = allc.get(id(calls), []); k = treepieces(A, g.n)
        if prev == ph and not (plus and A == pcalls):
            tr += 1; nv = len({x[0] for x in k - seen}); marg = min(marg, nv); bad += (nv == 0)
        elif prev != ph:
            seen = set()
        seen |= k; prev = ph; pcalls = A
    return (bad, -marg, tr, d.iterations)


def tp_climb(start_file, steps, seed, out, order):
    """class-free climb (fixd_oneplayer.mutate with ONEP_ANY=1, two-player games, priorities as mutated) on tp_score."""
    import random
    os.environ["ONEP_ANY"] = "1"
    from fixd_oneplayer import mutate
    rnd = random.Random(seed); g = pg.read(start_file); P = max(g.prio) + 1; sg = tp_score(g, order); os.makedirs(out, exist_ok=True)
    print("start", sg, flush=True)
    for it in range(steps):
        h = mutate(g, 0, P, rnd)
        if h is None: continue
        try:
            sh = tp_score(h, order)
        except RecursionError:
            continue
        if sh >= sg:
            if sh > sg: print(it, sh, flush=True)
            g, sg = h, sh
            if sg[0] >= 1:
                fn = os.path.join(out, f"treepiece_viol_n{g.n}_s{seed}.pg"); pg.write(g, fn); print("VIOLATION", sg, fn, flush=True); return
    fn = os.path.join(out, f"treepiece_final_n{g.n}_s{seed}.pg"); pg.write(g, fn); print("final", sg, fn)


if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "climb":
    sys.setrecursionlimit(100000)
    import importlib; M = importlib.import_module("b12_ident")
    M.tp_climb(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5], os.environ.get("DTL_ORDER", "stable")); sys.exit(0)

if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable")
    tot = ident = 0; kinds = {}; ex = {}
    src = lambda: classgames(sys.argv[1:], 3, 2, 200) if os.environ.get("CLASS") == "1" else plain(sys.argv[1:], int(os.environ.get("NMAX", "100")))
    for name, g in src():
        try:
            d = run(g, order)
        except RecursionError:
            continue
        log = getattr(d, "log", []); allc = getattr(d, "allc", {})
        for (pa, ca), (pb, cb) in zip(log, log[1:]):
            if pa != pb: continue
            tot += 1
            if B.sig(B.chain(ca, g.n)) != B.sig(B.chain(cb, g.n)): continue
            ident += 1; A = allc.get(id(ca), []); Bc = allc.get(id(cb), [])
            k = next((i for i in range(min(len(A), len(Bc))) if A[i] != Bc[i]), None)
            if k is None:
                kind = "same call sequence" if len(A) == len(Bc) else "one sequence is a prefix"
            else:
                a, b = A[k], Bc[k]
                kind = f"depth {b[0]}: " + ("context differs" if a[:2] != b[:2] else "outcome differs")
            kinds[kind] = kinds.get(kind, 0) + 1; ex.setdefault(kind, (name, g.n))
    print("order", order, "transitions", tot, "identical depth-0 states", ident)
    if os.environ.get("TREE") == "1":
        T = [0, 0]; first = None; T2 = [0, 0]; first2 = None
        for name, g in src():
            try:
                d = run(g, order)
            except RecursionError:
                continue
            tr, bad, e = treenew(d, g.n); T[0] += tr; T[1] += bad
            if e and first is None: first = (name, g.n, e)
            tr, bad, e = treenew(d, g.n, treepieces); T2[0] += tr; T2[1] += bad
            if e and first2 is None: first2 = (name, g.n, e)
        print("  TREE-NEW (v, depth, rank, |R|, |V|) over all calls' contexts: transitions", T[0], "without a new key", T[1], "first", first)
        print("  TREE-PIECE (v, depth, position, rank, |R|, |V|) over all calls' pieces: transitions", T2[0], "without a new key", T2[1], "first", first2)
    for k in sorted(kinds): print(f"  {k:32s} {kinds[k]:5d}  first {ex[k]}")

