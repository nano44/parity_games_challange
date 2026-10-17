#!/usr/bin/env python3
"""Lower bound on w(n,d) (weak separator, convention E) by pairwise-inconsistent words.

If words u, v reach the same state q of a deterministic safety automaton A, then for every infinite word y:
u.y accepted <=> v.y accepted. A weak (n,d)-separator accepts every infinite path label of an even graph with <= n
vertices and rejects every infinite path label of an odd graph with <= n vertices. Hence u, v need distinct
(non-bottom) states if some infinite y has u.y = label of an infinite path of an even graph H and v.y = label of an
infinite path of an odd graph H' (or the same with u, v swapped).
With E(u) = {(H,a): a reachable in H by a path labelled u from some vertex} and O(u) likewise for odd graphs, this
holds iff some (H,a) in E(u), (H',b) in O(v) have a common infinite path from (a,b) in the label-synchronised product
H x H' (or swapped). A clique of pairwise-inconsistent words gives w(n,d) >= clique size (all members are non-bottom:
each has an accepted infinite continuation, which forces E(u) non-empty and the state non-bottom).
Signatures (E(u), O(u)) are explored exhaustively from the empty word, so every word class is considered.
Usage: clique.py n d [--words-out FILE]"""
import sys, os, json, itertools, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import graphs
import networkx as nx


def analyse(n, d, log=print):
    ev, od = graphs.family(n, d, 0), graphs.family(n, d, 1)
    # node ids
    enodes = [(gi, a) for gi in range(len(ev)) for a in range(n)]
    onodes = [(gi, b) for gi in range(len(od)) for b in range(n)]
    eid = {x: i for i, x in enumerate(enodes)}; oid = {x: i for i, x in enumerate(onodes)}
    def succ_table(fam, ids):
        T = [[set() for _ in range(d + 1)] for _ in range(len(ids))]
        for gi, (nn, E) in enumerate(fam):
            for (u, p, v) in E:
                T[ids[(gi, u)]][p].add(ids[(gi, v)])
        return T
    Te, To = succ_table(ev, eid), succ_table(od, oid)
    # C[e] = set of o with a common infinite path from (e, o)
    C = [set() for _ in enodes]
    for gi in range(len(ev)):
        for gj in range(len(od)):
            nodes = [(a, b) for a in range(n) for b in range(n)]
            succ = {}
            for a, b in nodes:
                ea, ob = eid[(gi, a)], oid[(gj, b)]
                succ[(a, b)] = [(x, y) for p in range(1, d + 1) for x in Te[ea][p] for y in To[ob][p]]
            alive = set(nodes)
            changed = True
            while changed:  # prune nodes without a successor inside alive: survivors have infinite paths
                changed = False
                for x in list(alive):
                    if not any(y in alive for y in succ[x]):
                        alive.discard(x); changed = True
            for (a, b) in alive:
                C[eid[(gi, a)]].add(oid[(gj, b)])
    # exhaustive signature exploration
    start = (frozenset(range(len(enodes))), frozenset(range(len(onodes))))
    sigs = {start: ()}
    frontier = [start]
    while frontier:
        nxt = []
        for s in frontier:
            for p in range(1, d + 1):
                t = (frozenset(y for x in s[0] for y in Te[x][p]), frozenset(y for x in s[1] for y in To[x][p]))
                if t not in sigs:
                    sigs[t] = sigs[s] + (p,); nxt.append(t)
        frontier = nxt
    cand = [s for s in sigs if s[0]]  # non-bottom candidates (E non-empty)
    log(f"(n,d)=({n},{d}): {len(ev)} even, {len(od)} odd graphs; {len(sigs)} word signatures, {len(cand)} with E != {{}}")
    reachO = [set().union(*[C[e] for e in s[0]]) if s[0] else set() for s in cand]
    G = nx.Graph(); G.add_nodes_from(range(len(cand)))
    for i in range(len(cand)):
        for j in range(i + 1, len(cand)):
            if (reachO[i] & cand[j][1]) or (reachO[j] & cand[i][1]):
                G.add_edge(i, j)
    log(f"  inconsistency graph: {G.number_of_edges()} edges")
    clique, size = nx.max_weight_clique(G, weight=None)
    words = [list(sigs[cand[i]]) for i in clique]
    return size, words, (ev, od)


def certify(n, d, words, ev, od):
    """Re-check a clique independently of the signature machinery: for each pair search a lasso y = x.z^w that is an
    infinite path label after u in some even graph and after v in some odd graph (or swapped), by product search."""
    def ends(fam, w):
        out = []
        for gi, (nn, E) in enumerate(fam):
            cur = set(range(nn))
            for p in w:
                cur = {v for (u, q, v) in E if q == p and u in cur}
            out += [(gi, a) for a in cur]
        return out
    def common_inf(ga, a, gb, b):
        Ea, Eb = ev[ga][1], od[gb][1]
        seen, st = set(), [(a, b)]
        while st:
            x = st.pop()
            if x in seen:
                continue
            seen.add(x)
            st += [(v1, v2) for (u1, p, v1) in Ea if u1 == x[0] for (u2, q, v2) in Eb if u2 == x[1] and q == p]
        # infinite path exists iff the reachable product contains a cycle
        sub = {x: [(v1, v2) for (u1, p, v1) in Ea if u1 == x[0] for (u2, q, v2) in Eb if u2 == x[1] and q == p] for x in seen}
        alive = set(seen)
        while True:
            dead = [x for x in alive if not any(y in alive for y in sub[x])]
            if not dead:
                break
            alive -= set(dead)
        return bool(alive)
    for i, j in itertools.combinations(range(len(words)), 2):
        ok = False
        for u, v in ((words[i], words[j]), (words[j], words[i])):
            for (ga, a) in ends(ev, u):
                for (gb, b) in ends(od, v):
                    if common_inf(ga, a, gb, b):
                        ok = True; break
                if ok: break
            if ok: break
        if not ok:
            return False, (words[i], words[j])
    return True, None


if __name__ == "__main__":
    n, d = int(sys.argv[1]), int(sys.argv[2])
    t = time.time()
    size, words, (ev, od) = analyse(n, d)
    ok, bad = certify(n, d, words, ev, od)
    print(f"  max clique {size} (lower bound w({n},{d}) >= {size}); certified by lasso search: {ok} {bad or ''}; {time.time()-t:.0f}s")
    if "--words-out" in sys.argv:
        json.dump({"n": n, "d": d, "bound": size, "words": words}, open(sys.argv[sys.argv.index("--words-out") + 1], "w"))
