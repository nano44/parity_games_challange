"""Independent strategy verifier (D2 change 5). Max-parity, owner 0 = Even.

check(g, win, strat) -> list of error strings ([] = verified). win[v] in {0,1}; strat[v] = successor or None.
For each player p and its region W_p:
  closure: every v in W_p owned by p has strat[v] in E(v) and in W_p; every v in W_p owned by 1-p has E(v) within W_p;
  winning: in the graph on W_p where p's vertices keep only the strategy edge, there is no cycle whose highest
           priority has the opponent's parity (one-player game check; closure makes "reachable inside W_p" automatic).
Cycle test: recursive SCC decomposition: in each nontrivial SCC the top priority q must have p's parity; then the
q-vertices are removed and the rest of the SCC is decomposed again."""
import sys


def sccs(nodes, succ):
    """Tarjan, iterative. nodes: iterable; succ(v) -> successors (already restricted to the node set)."""
    index, low, on, st, out, cnt = {}, {}, set(), [], [], [0]
    for root in nodes:
        if root in index:
            continue
        work = [(root, iter(succ(root)))]
        index[root] = low[root] = cnt[0]; cnt[0] += 1; st.append(root); on.add(root)
        while work:
            v, it = work[-1]
            pushed = False
            for w in it:
                if w not in index:
                    index[w] = low[w] = cnt[0]; cnt[0] += 1; st.append(w); on.add(w)
                    work.append((w, iter(succ(w)))); pushed = True; break
                elif w in on:
                    low[v] = min(low[v], index[w])
            if pushed:
                continue
            work.pop()
            if work:
                low[work[-1][0]] = min(low[work[-1][0]], low[v])
            if low[v] == index[v]:
                comp = []
                while True:
                    w = st.pop(); on.discard(w); comp.append(w)
                    if w == v:
                        break
                out.append(comp)
    return out


def check(g, win, strat):
    errs = []
    n = g.n
    for v in range(n):
        p = win[v]
        if g.owner[v] == p:
            s = strat[v] if strat is not None else None
            if s is None:
                errs.append(f"v{v}: winner {p} owns it but no strategy"); continue
            if s not in g.succ[v]:
                errs.append(f"v{v}: strategy {s} is not an edge"); continue
            if win[s] != p:
                errs.append(f"v{v}: strategy leaves the region of {p}")
        else:
            out = [w for w in g.succ[v] if win[w] != p]
            if out:
                errs.append(f"v{v}: opponent of {p} escapes to {out[0]}")
    if errs:
        return errs
    for p in (0, 1):
        W = [v for v in range(n) if win[v] == p]
        restricted = {v: ([strat[v]] if g.owner[v] == p else list(set(g.succ[v]))) for v in W}
        stack = [set(W)]
        while stack:
            part = stack.pop()
            for comp in sccs(part, lambda v: [w for w in restricted[v] if w in part]):
                if len(comp) == 1 and comp[0] not in restricted[comp[0]]:
                    continue  # trivial SCC, no cycle
                q = max(g.prio[v] for v in comp)
                if q % 2 != p:
                    v = next(v for v in comp if g.prio[v] == q)
                    errs.append(f"region of {p}: opponent cycle with top priority {q} through v{v}")
                    return errs
                rest = {v for v in comp if g.prio[v] != q}
                if rest:
                    stack.append(rest)
    return errs


def read_strategy(text, n):
    strat = [None] * n
    for line in text.splitlines():
        line = line.strip().rstrip(";").strip()
        if not line or line.startswith("paritysol"):
            continue
        parts = line.split()
        if len(parts) >= 3:
            strat[int(parts[0])] = int(parts[2])
    return strat


if __name__ == "__main__":
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import pg
    g = pg.read(sys.argv[1]); text = open(sys.argv[2]).read()
    e = check(g, pg.read_sol(text, g.n), read_strategy(text, g.n))
    print("strategy verified" if not e else "FAILED: " + "; ".join(e[:5]))
    sys.exit(1 if e else 0)
