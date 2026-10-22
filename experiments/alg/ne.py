#!/usr/bin/env python3
"""C1: NE(k), nested-escape fatal attractors (docs/alg/candidates/C1.md). Max-parity, owner 0 = Even, 1 = Odd.
NE(0) is literal psolC (DTR15-4 Fig. 5; cross-checked against experiments/attr/psolc.py). NE(k) adds, to the target of
psolC's product attractor, the states of the escape game Esc_p(G, A, X) that NE(k-1) decides for p.

API: solve(g, k) -> (win, decisions, stats); win[v] in {0, 1, None}.
     solve_with_strategy(g, k, strat="oracle"|"zlk"|None) -> (win, strat, residual, info)
CLI: ne.py game.pg [solution.sol] [-k K] [--strat oracle|zlk|none] [--partial] [--trace]
Exit 3 'UNDECIDED r of n' if the residual is non-empty and --partial is not given."""
import sys, os
from collections import deque
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg

sys.setrecursionlimit(10000)

MODE = "esc"   # "esc": C1 (escape game on (A \ X) x C with sinks TOP/BOT); "h": C2 (full product game H with Good sinks)


class Stats:
    def __init__(self):
        self.calls = [0] * 64        # NE calls per level (index = k)
        self.product_states = 0
        self.esc_states = 0
        self.fixpoint_iters = 0
        self.decisions = 0


def attractor(owner, succ, pred, alive, target, p):
    """Attractor of `target` (iterable of vertices in alive) for player p inside `alive` (a set)."""
    A = set(target)
    cnt, q = {}, deque(A)
    while q:
        w = q.popleft()
        for v in pred[w]:
            if v not in alive or v in A:
                continue
            if owner[v] == p:
                A.add(v); q.append(v)
            else:
                if v not in cnt:
                    cnt[v] = sum(1 for x in succ[v] if x in alive)
                cnt[v] -= 1
                if cnt[v] == 0:
                    A.add(v); q.append(v)
    return A


def ne(n, prio, owner, succ, k, stats, trace=False, depth=0):
    """NE_k on the game (prio, owner, succ) with vertex set range(n). Returns win list and decisions list."""
    stats.calls[k] += 1
    pred = [[] for _ in range(n)]
    for v in range(n):
        for w in succ[v]:
            pred[w].append(v)
    win = [None] * n
    decisions = []
    alive = set(range(n))
    while alive:
        removed = False
        for p in (0, 1):
            X = gfp(prio, owner, succ, pred, alive, p, k, stats, trace, depth)
            if X:
                D = attractor(owner, succ, pred, alive, X, p)
                for v in D:
                    win[v] = p
                decisions.append((p, len(X), len(D)))
                stats.decisions += 1
                if trace:
                    print(f"{'  '*depth}NE_{k}: player {p} gfp X={sorted(X)} Attr |{len(D)}|", file=sys.stderr)
                alive = alive - D
                removed = True
                break
        if not removed:
            break
    return win, decisions


def gfp(prio, owner, succ, pred, alive, p, k, stats, trace, depth):
    X = {v for v in alive if prio[v] % 2 == p}
    while X:
        stats.fixpoint_iters += 1
        W = w_level(prio, owner, succ, alive, X, p, k, stats, trace, depth)
        if trace:
            print(f"{'  '*depth}  gfp_{k} p={p}: X={sorted(X)} -> W={sorted(W)}", file=sys.stderr)
        if X <= W:
            return X
        X = X & W
    return set()


def w_level(prio, owner, succ, alive, X, p, k, stats, trace, depth):
    """W_k(G, A, X, p): the x in X whose entry state (x, pr(x)) lies in the p-attractor, inside the product Pi, of
    Good ∪ R, where R = the states of the escape game decided for p by NE_{k-1} (R = {} when k = 0)."""
    # product Pi: reachable part from the entry states (x, START); state = (v, c); c = max priority since the start,
    # the start's own priority included (DTR15-4 Def. 2 edge (1), first line); the start visit itself is not a target.
    START = -1
    entries = [(x, START) for x in X]
    nodes = {}
    out = []
    pn_succ = []
    q = deque()
    for e in entries:
        nodes[e] = len(out); out.append(e); q.append(e)
    while q:
        v, c = q.popleft()
        s = []
        if c != START and v in X and c % 2 == p:
            pn_succ.append(s)      # Good: target of the attractor, never expanded
            continue
        base = prio[v] if c == START else c
        for w in succ[v]:
            if w not in alive:
                continue
            node = (w, max(base, prio[w]))
            if node not in nodes:
                nodes[node] = len(out); out.append(node); q.append(node)
            s.append(nodes[node])
        pn_succ.append(s)
    N = len(out)
    stats.product_states += N
    good = {i for i, (v, c) in enumerate(out) if c != START and v in X and c % 2 == p}
    R = set()
    if k >= 1 and MODE == "esc":
        # C1: escape game on the product states with v not in X, plus TOP (index N) and BOT (index N + 1)
        esc_idx = {}
        esc_nodes = []
        for i, (v, c) in enumerate(out):
            if v not in X:
                esc_idx[i] = len(esc_nodes); esc_nodes.append(i)
        if esc_nodes:
            TOP, BOT = len(esc_nodes), len(esc_nodes) + 1
            e_prio = [prio[out[i][0]] for i in esc_nodes] + [p, 1 - p]
            e_owner = [owner[out[i][0]] for i in esc_nodes] + [p, p]
            e_succ = []
            for i in esc_nodes:
                s = []
                for j in pn_succ[i]:
                    w, c2 = out[j]
                    if w in X:
                        s.append(TOP if c2 % 2 == p else BOT)
                    else:
                        s.append(esc_idx[j])
                e_succ.append(sorted(set(s)))
            e_succ += [[TOP], [BOT]]
            stats.esc_states += len(e_succ)
            ewin, _ = ne(len(e_succ), e_prio, e_owner, e_succ, k - 1, stats, trace, depth + 1)
            R = {esc_nodes[a] for a in range(len(esc_nodes)) if ewin[a] == p}
    elif k >= 1 and MODE == "h":
        # C2: the whole product game H: every Pi state, Good states made p-winning sinks (self-loop of p's parity),
        # bad visits to X continue as in Pi; priority of (v, c) is pr(v). NE_{k-1} decides p's region R of H.
        h_prio = [(p if i in good else prio[v]) for i, (v, c) in enumerate(out)]
        h_owner = [owner[v] for (v, c) in out]
        h_succ = [([i] if i in good else sorted(set(pn_succ[i]))) for i in range(N)]
        stats.esc_states += N
        hwin, _ = ne(N, h_prio, h_owner, h_succ, k - 1, stats, trace, depth + 1)
        R = {i for i in range(N) if hwin[i] == p}
    # attractor of good ∪ R for p in the product
    T = good | R
    pn_pred = [[] for _ in range(N)]
    for i in range(N):
        for j in pn_succ[i]:
            pn_pred[j].append(i)
    A = set(T)
    cnt, q = {}, deque(A)
    while q:
        w = q.popleft()
        for i in pn_pred[w]:
            if i in A:
                continue
            if owner[out[i][0]] == p:
                A.add(i); q.append(i)
            else:
                if i not in cnt:
                    cnt[i] = len(pn_succ[i])
                cnt[i] -= 1
                if cnt[i] == 0:
                    A.add(i); q.append(i)
    return {x for x in X if nodes[(x, START)] in A}


# ---------------------------------------------------------------------------------------------------- public API
def solve(g, k, trace=False):
    stats = Stats()
    succ = [sorted(set(s)) for s in g.succ]
    win, decisions = ne(g.n, list(g.prio), list(g.owner), succ, k, stats, trace)
    return win, decisions, stats


def oracle_strategy(g, k, D, p):
    """Positional strategy for p on a closed region D won by p (its final region), by oracle extraction with NE(k)
    itself: restrict each p-vertex of D to one successor inside D, keep the first choice for which NE(k) still decides
    all of G[D] for p. Returns (strat dict, failed list of vertices for which no edge was accepted)."""
    Dl = sorted(D)
    idx = {v: i for i, v in enumerate(Dl)}
    succ = [[idx[w] for w in sorted(set(g.succ[v])) if w in D] for v in Dl]
    prio = [g.prio[v] for v in Dl]
    owner = [g.owner[v] for v in Dl]
    strat, failed = {}, []
    for i, v in enumerate(Dl):
        if owner[i] != p:
            continue
        if len(succ[i]) == 1:
            strat[v] = Dl[succ[i][0]]; continue
        chosen = None
        for w in list(succ[i]):
            saved = succ[i]
            succ[i] = [w]
            st = Stats()
            ww, _ = ne(len(Dl), prio, owner, succ, k, st)
            if all(x == p for x in ww):
                chosen = w
                break
            succ[i] = saved
        if chosen is None:
            failed.append(v)
        else:
            strat[v] = Dl[chosen]
    return strat, failed


def closed(g, D, p):
    """D is closed for p: p's vertices keep a successor in D, q's vertices have all successors in D."""
    for v in D:
        s = set(g.succ[v])
        if g.owner[v] == p:
            if not (s & D):
                return False
        elif not s <= D:
            return False
    return True


def solve_with_strategy(g, k, strat="oracle", trace=False):
    """Returns (win, strat, residual, info). Positional strategies on each player's final decided region when it is
    closed (always, when the game is completely solved): 'oracle' = extraction with NE(k) itself (C1.md section 1), with
    Zielonka fallback on the region if extraction fails for some vertex (recorded in info['strat_fail']);
    'zlk' = Zielonka on the region (verification aid only); None = regions only. info['nonclosed'] lists the players
    whose partial decided region is not closed (no strategy produced there)."""
    win, decisions, stats = solve(g, k, trace)
    st = [None] * g.n
    info = dict(decisions=decisions, stats=stats, strat_fail=[], nonclosed=[], strat_mode=strat)
    residual = {v for v in range(g.n) if win[v] is None}
    if strat:
        for p in (0, 1):
            D = {v for v in range(g.n) if win[v] == p}
            if not D:
                continue
            if not closed(g, D, p):
                info["nonclosed"].append(p)
                continue
            if strat == "oracle":
                sd, failed = oracle_strategy(g, k, D, p)
                if failed:
                    info["strat_fail"].append((p, sorted(failed)))
                    sd = zlk_strategy(g, D, p)
            else:
                sd = zlk_strategy(g, D, p)
            for v, w in sd.items():
                st[v] = w
    return win, st, residual, info


def zlk_strategy(g, D, p):
    import zielonka
    Dl = sorted(D)
    idx = {v: i for i, v in enumerate(Dl)}
    succ = [[idx[w] for w in sorted(set(g.succ[v])) if w in D] for v in Dl]
    sub = pg.Game([g.prio[v] for v in Dl], [g.owner[v] for v in Dl], succ)
    w, s = zielonka.solve_with_strategy(sub)
    assert all(x == p for x in w), "Zielonka disagrees: decided region is not won by its player (UNSOUND)"
    return {v: Dl[s[i]] for i, v in enumerate(Dl) if g.owner[v] == p}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    opt = lambda key, d: sys.argv[sys.argv.index(key) + 1] if key in sys.argv else d
    k = int(opt("-k", 1))
    global MODE
    MODE = opt("--mode", "esc")
    mode = opt("--strat", "oracle")
    mode = None if mode == "none" else mode
    g = pg.read(args[0])
    win, strat, residual, info = solve_with_strategy(g, k, mode, trace="--trace" in sys.argv)
    s = info["stats"]
    print(f"NE({k}): {len(info['decisions'])} decisions, calls per level {s.calls[:k+1]}, product states {s.product_states}, "
          f"escape states {s.esc_states}, fixpoint iterations {s.fixpoint_iters}, strat-fail {info['strat_fail']}, "
          f"nonclosed {info['nonclosed']}", file=sys.stderr)
    if residual and "--partial" not in sys.argv:
        print(f"UNDECIDED {len(residual)} of {g.n}: {sorted(residual)[:20]}", file=sys.stderr)
        sys.exit(3)
    text = f"paritysol {g.n};\n" + "".join(
        f"{v} {w if w is not None else '?'}{'' if strat[v] is None else ' ' + str(strat[v])};\n" for v, w in enumerate(win))
    if len(args) > 1:
        open(args[1], "w").write(text)
    else:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
