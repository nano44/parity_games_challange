"""Shared code for A1: classify one game under psolQ and under Algorithm 1 of arXiv 2511.03752 (experiments/m2/avh.py),
check soundness against harness Zielonka and positional strategies with harness verify.py (restricted to the decided
region for partial outputs), canonical enumeration of small games, random games, shrinking."""
import sys, os, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "harness"))
sys.path.insert(0, os.path.join(HERE, "..", "m2"))
import pg, zielonka, verify
import avh
from psolq import PsolQ
from psolb import PsolB, Psol
from strahler import strahler, tree_height, tree_leaves


def check_partial(g, win, strat):
    """verify.py on the decided part: for each player p, the region D_p = {v : win[v] = p} must be closed under p's
    strategy and the opponent's edges, and contain no opponent-parity dominant cycle. Returns [] or error strings."""
    errs = []
    for p in (0, 1):
        D = [v for v in range(g.n) if win[v] == p]
        if not D:
            continue
        idx = {v: i for i, v in enumerate(D)}
        succ = []
        for v in D:
            if g.owner[v] == p:
                s = strat[v]
                if s is None or s not in g.succ[v]:
                    errs.append(f"v{v}: no/invalid strategy"); succ.append([]); continue
                if win[s] != p:
                    errs.append(f"v{v}: strategy leaves region of {p}"); succ.append([]); continue
                succ.append([idx[s]])
            else:
                out = [w for w in set(g.succ[v]) if win[w] != p]
                if out:
                    errs.append(f"v{v}: opponent of {p} escapes to {out[0]}"); succ.append([]); continue
                succ.append([idx[w] for w in set(g.succ[v])])
        if errs:
            return errs
        sub = pg.Game([g.prio[v] for v in D], [g.owner[v] for v in D], succ)
        errs += verify.check(sub, [p] * len(D), [succ[i][0] if g.owner[v] == p else None for i, v in enumerate(D)])
    return errs


def classify(g, ref=None, want_strahler=False, others=False):
    """Returns dict: ref (Zielonka winners), psolq: 'solved'|'undecided'|'UNSOUND'|'BADSTRAT', psolq_undecided (count),
    avh: 'solved'|'stuck'|'WRONG'|'BADSTRAT', avh_undecided, and if want_strahler: str, strE, strO, height, leaves."""
    ref = zielonka.solve(g) if ref is None else ref
    out = dict(ref=ref)
    win, strat, residual, _ = PsolQ(g).run()
    bad = [v for v in range(g.n) if win[v] is not None and win[v] != ref[v]]
    if bad:
        out["psolq"] = "UNSOUND"
    elif check_partial(g, win, strat):
        out["psolq"] = "BADSTRAT"
    else:
        out["psolq"] = "solved" if not residual else "undecided"
    out["psolq_undecided"] = len(residual)
    if others:
        for name, cls in (("psolb", PsolB), ("psol", Psol)):
            w2, s2, res2, _ = cls(g).run()
            if any(w2[v] is not None and w2[v] != ref[v] for v in range(g.n)):
                out[name] = "UNSOUND"
            elif check_partial(g, w2, s2):
                out[name] = "BADSTRAT"
            else:
                out[name] = "solved" if not res2 else "undecided"
            out[name + "_undecided"] = len(res2)
    s = avh.Solver(g)
    try:
        awin, astrat = s.solve()
        if awin != ref:
            out["avh"] = "WRONG"
        elif verify.check(g, awin, astrat):
            out["avh"] = "BADSTRAT"
        else:
            out["avh"] = "solved"
        out["avh_undecided"] = 0
    except avh.Stuck:
        dec = [v for v in range(g.n) if s.win[v] is not None]
        if any(s.win[v] != ref[v] for v in dec):
            out["avh"] = "WRONG"           # wrong on the part it did decide
        elif check_partial(g, s.win, s.strat):
            out["avh"] = "BADSTRAT"
        else:
            out["avh"] = "stuck"
        out["avh_undecided"] = g.n - len(dec)
    if want_strahler:
        st, info = strahler(g, win=ref)
        out.update(str=st, strE=info["E"][0], strO=info["O"][0],
                   height=max(tree_height(info["E"][1]), tree_height(info["O"][1])),
                   leaves=max(tree_leaves(info["E"][1]), tree_leaves(info["O"][1])),
                   treeE=info["E"][1], treeO=info["O"][1])
    return out


# ---- canonical enumeration -------------------------------------------------------------------------------------
def priority_patterns(n):
    """Every priority vector on n vertices up to order-and-parity-preserving relabelling, exactly once:
    a surjective rank map V -> {0..r-1} and a parity bit per rank; pr(v) = 2 rank(v) + bit(rank(v))."""
    for r in range(1, n + 1):
        for ranks in itertools.product(range(r), repeat=n):
            if len(set(ranks)) != r:
                continue
            for bits in itertools.product((0, 1), repeat=r):
                yield tuple(2 * ranks[v] + bits[ranks[v]] for v in range(n))


def succ_configs(n):
    succsets = [frozenset(s) for r in range(1, n + 1) for s in itertools.combinations(range(n), r)]
    return itertools.product(succsets, repeat=n)


def canon_succ(cfg, perms):
    """Canonical representative of a successor configuration under vertex permutations (lexicographically least)."""
    best = None
    for p in perms:
        img = [None] * len(cfg)
        for v, s in enumerate(cfg):
            img[p[v]] = tuple(sorted(p[w] for w in s))
        t = tuple(img)
        if best is None or t < best:
            best = t
    return best


def succ_orbits(n):
    """One representative per isomorphism class of successor configurations (self-loops allowed), with its edge count."""
    perms = list(itertools.permutations(range(n)))
    seen = set()
    for cfg in succ_configs(n):
        c = canon_succ(cfg, perms)
        if c in seen:
            continue
        seen.add(c)
        yield c, sum(len(s) for s in c)


def games_on(cfg, n):
    """All games on a fixed successor configuration: every owner vector and every canonical priority pattern."""
    succ = [list(s) for s in cfg]
    for owners in itertools.product((0, 1), repeat=n):
        for prio in priority_patterns(n):
            yield pg.Game(prio, owners, succ)


def compress(g):
    """TARGET.md section 1 compression: priorities sorted, consecutive same-parity values merged, result in {0..n}."""
    vals = sorted(set(g.prio))
    new, cur = {}, None
    for v in vals:
        if cur is None:
            cur = v % 2
        elif v % 2 != cur % 2:
            cur += 1
        new[v] = cur
    return pg.Game([new[p] for p in g.prio], g.owner, g.succ)


# ---- shrinking -------------------------------------------------------------------------------------------------
def shrink(g, pred):
    """Greedy: delete an edge or a vertex (with its incident edges, if every vertex keeps a successor) while pred(g)."""
    changed = True
    while changed:
        changed = False
        for v in range(g.n):
            for w in sorted(set(g.succ[v])):
                if len(set(g.succ[v])) < 2:
                    continue
                succ = [list(set(s)) for s in g.succ]
                succ[v].remove(w)
                h = pg.Game(g.prio, g.owner, succ)
                if pred(h):
                    g = h; changed = True
        for v in range(g.n):
            keep = [u for u in range(g.n) if u != v]
            idx = {u: i for i, u in enumerate(keep)}
            succ = [[idx[w] for w in set(g.succ[u]) if w != v] for u in keep]
            if g.n < 2 or any(not s for s in succ):
                continue
            h = pg.Game([g.prio[u] for u in keep], [g.owner[u] for u in keep], succ)
            if pred(h):
                g = h; changed = True
                break
    return g
