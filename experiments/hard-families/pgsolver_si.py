#!/usr/bin/env python3
"""Python port of PGSolver's strategy improvement with the "switchall" policy (Voege-Jurdzinski valuations).

Source: github.com/tcsprojects/pgsolver @ d3cd624, src/lib/solvers/stratimpralgs.ml:
  56-74 orderings, 76-87 initial strategies, 89-128 valuation ordering / best decision / improvable,
  130-145 winning regions and strategies, 147-199 evaluate_strategy, 441-597 strategy_improvement main loop,
  659-669 improvement_policy_optimize_all_locally + strategy_improvement_optimize_all_locally_policy (registered as
  "switchall", line 694-696, with initial_strategy_by_best_reward and node_total_ordering_by_position).
Helpers: paritygame.ml:120 ns_max, :473 reward, :1229 paritygame_to_dynamic_paritygame_by_strategy;
  tcslib @ 6778419 src/data/tcsgraph.ml: GraphUtils (iterate_with_minimal_distance, ..._maximal_distance_single_loop,
  build_reachability_set), DynamicGraph (sub_graph_by_node_closure, depth_find, iter_by); TreeSet.choose = min_elt,
  fold ascending (tcsset.ml).
DEVIATION: PGSolver runs "switchall" inside universal_solve (global preprocessing, SCC decomposition); this port runs
the strategy improvement loop directly on the whole game. Iteration counts are therefore those of the bare algorithm.
switchbest: switch_globally_best.ml:13-104 (policy) and :107-108 (strategy_improvement_by_policy: alternating
  transformation + cheap escape cycles, transformations.ml:271-320, 338-394, 397-413; initial_strategy_by_last_edge).
Usage: pgsolver_si.py game.pg [out.sol] [--switchbest]   (logs 'solved with K iterations.'; K = PGSolver's counter, line 595-598)"""
import sys, os, functools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
import pg

sys.setrecursionlimit(1000000)
EVEN, ODD = 0, 1


def cmp(a, b):
    return (a > b) - (a < b)


class SI:
    def __init__(self, g):
        self.g = g
        self.pr, self.pl = g.prio, g.owner
        self.succ = [sorted(set(s)) for s in g.succ]

    # stratimpralgs.ml:66-67
    def rel(self, i, j):
        return cmp((self.pr[i], i), (self.pr[j], j))

    # paritygame.ml:473
    @staticmethod
    def reward(player, prio):
        return -prio if (prio % 2 != player) and prio >= 0 else prio

    # stratimpralgs.ml:69-74
    def rew(self, i, j):
        ri, rj = self.reward(EVEN, self.pr[i]), self.reward(EVEN, self.pr[j])
        c = cmp(ri, rj)
        if c != 0:
            return c
        # OCaml: ri mod 2 = 0 (sign of mod follows the dividend; -3 mod 2 = -1)
        return cmp(i, j) if ri % 2 == 0 else cmp(j, i)

    # paritygame.ml:120 ns_max: fold ascending from choose (= min element); keep acc unless lessf acc x
    @staticmethod
    def ns_max(ns, lessf):
        acc = ns[0]
        for x in ns:
            if lessf(acc, x):
                acc = x
        return acc

    # stratimpralgs.ml:85-87
    def initial_strategy_by_best_reward(self):
        return [-1 if self.pl[i] == ODD else self.ns_max(self.succ[i], lambda a, b: self.rew(a, b) <= 0)
                for i in range(self.g.n)]

    # stratimpralgs.ml:92-107
    def nvo(self, a, b):
        (u, p, e), (v, q, f) = a, b
        c = self.rew(u, v)
        if c != 0:
            return c
        r = p ^ q
        if r:
            w = max(r, key=lambda x: (self.pr[x], x))  # min_elt under flip(relevance) = most relevant
            c = -1 if ((self.pr[w] % 2 == 0 and w in q) or (self.pr[w] % 2 == 1 and w in p)) else 1
            return c
        if e == f:
            return 0
        return -1 if ((self.pr[v] % 2 == 1 and e < f) or (self.pr[v] % 2 == 0 and e > f)) else 1

    # stratimpralgs.ml:109-112
    def nvto(self, valu, x, y):
        c = self.nvo(valu[x], valu[y])
        return c if c != 0 else cmp(x, y)

    # stratimpralgs.ml:114-121
    def best(self, valu, v):
        o = lambda x, y: self.nvto(valu, x, y) >= 0
        if self.pl[v] == ODD:
            return self.ns_max(self.succ[v], lambda a, b: o(a, b))
        return self.ns_max(self.succ[v], lambda a, b: o(b, a))

    # stratimpralgs.ml:147-199
    def evaluate(self, strat):
        n = self.g.n
        gs = {i: set(self.succ[i]) if strat[i] == -1 else {strat[i]} for i in range(n)}   # paritygame.ml:1229
        gp = {i: set() for i in range(n)}
        for i in range(n):
            for j in gs[i]:
                gp[j].add(i)
        asc = sorted(range(n), key=functools.cmp_to_key(self.rew))                       # add_cmp snapshot
        valu = [(-1, frozenset(), 0)] * n
        for v in asc:
            if valu[v][0] != -1 or v not in gs:
                continue
            # DynamicGraph.depth_find v (fun u -> rel u v <= 0) (fun u -> has_edge u v graph) graph
            seen, found = set(), False

            def process(u):
                if u in seen:
                    return False
                seen.add(u)
                r = False
                for w in sorted(gs[u]):        # TreeSet.fold ascending, r || (...) short-circuits
                    r = r or (self.rel(w, v) <= 0 and (v in gs[w] or process(w)))
                return r
            if not process(v):
                continue
            # sub_graph_by_node_closure v (preds): nodes reaching v, with all their edges among themselves
            nodes, st = set(), [v]
            while st:
                w = st.pop()
                if w in nodes:
                    continue
                nodes.add(w)
                st.extend(gp[w])
            hs = {w: {u for u in gs[w] if u in nodes} for w in nodes}
            hp = {w: {u for u in gp[w] if u in nodes} for w in nodes}
            paths = {u: set() for u in nodes}

            def del_other_edges(x, m):
                for y in list(hs[x]):
                    if y not in m:
                        hs[x].discard(y); hp[y].discard(x)

            def reach(start, excl):  # build_reachability_set over preds filtered (!= excl)
                s, st2 = set(), [start]
                while st2:
                    x = st2.pop()
                    if x in s:
                        continue
                    s.add(x)
                    st2.extend(y for y in hp[x] if y != excl)
                return s
            for u in sorted(nodes, key=lambda x: (self.pr[x], x), reverse=True):  # iter_by des_rel (snapshot)
                if self.rel(u, v) > 0:
                    if self.pr[u] % 2 == 0:
                        m = reach(v, u)
                        for q in nodes:
                            if q not in m:
                                paths[q].add(u)
                        del_other_edges(u, m)
                        for q in m:
                            del_other_edges(q, m)
                    else:
                        m = reach(u, v)
                        for q in m:
                            paths[q].add(u)
                        for x in m:
                            if x != u:
                                del_other_edges(x, m)
            dist = {}
            if self.pr[v] % 2 == 0:
                cache = {}

                def get_dist(x):  # 1 + max over successors; 0 at v (RecursiveFunctionCache)
                    if x in cache:
                        return cache[x]
                    r = 0 if x == v else 1 + max(get_dist(y) for y in hs[x])
                    cache[x] = r
                    return r
                occ, st = set(), [v]
                while st:                     # reach_next: visit v then preds; order irrelevant for values
                    x = st.pop()
                    if x in occ:
                        continue
                    occ.add(x); dist[x] = get_dist(x)
                    st.extend(hp[x])
            else:
                occ, layer, i = set(), [v], 0   # iterate_with_minimal_distance: BFS over preds
                while layer:
                    nxt = []
                    for x in layer:
                        if x in occ:
                            continue
                        occ.add(x); dist[x] = i
                        nxt.extend(hp[x])
                    layer, i = nxt, i + 1
            for u in nodes:
                valu[u] = (v, frozenset(paths[u]), dist.get(u, 0))
            for u in nodes:                     # del_node u graph
                for y in gs.pop(u):
                    if y in gp: gp[y].discard(u)
                for y in gp.pop(u):
                    if y in gs: gs[y].discard(u)
        return valu

    # stratimpralgs.ml:82-83 initial_strategy_by_last_edge (ns_last = max successor)
    def initial_strategy_by_last_edge(self):
        return [-1 if self.pl[i] == ODD else max(self.succ[i]) for i in range(self.g.n)]

    def policy_switchall(self, strat, valu):  # improvement_policy_optimize_all_locally, line 659-666
        new = list(strat)
        for i, j in enumerate(strat):
            if j == -1:
                continue
            k = self.best(valu, i)
            if self.nvo(valu[j], valu[k]) < 0:
                new[i] = k
        return new

    def policy_switchbest(self, old, valu):
        """switch_globally_best.ml:13-104 improvement_policy_optimize_all_globally."""
        n = self.g.n
        vo = self.nvo
        # pruned copy: Even keeps edges w with valu(w) >= valu(old(i))  (lines 14-21)
        psucc = [list(self.succ[i]) if self.pl[i] == ODD else
                 [w for w in self.succ[i] if vo(valu[w], valu[old[i]]) >= 0] for i in range(n)]
        ppred = [set() for _ in range(n)]
        for i in range(n):
            for w in psucc[i]:
                ppred[w].add(i)
        strategy = list(old)
        valu2 = list(valu)
        valued = [False] * n
        # graph' (lines 29-42)
        g2s = {i: set(psucc[i]) for i in range(n)}
        g2p = {i: set(ppred[i]) for i in range(n)}

        def del_node(v):
            if v not in g2s:
                return
            for w in g2s.pop(v):
                if w in g2p: g2p[w].discard(v)
            for w in g2p.pop(v):
                if w in g2s: g2s[w].discard(v)
        check = set()
        for v in range(n):
            edges = psucc[v]
            if self.pl[v] == ODD:
                # best_decision_by_valuation_ordering game ... (Odd's edges are not pruned)
                reference = valu[self.best_in(valu, v, psucc[v])]
                for u in edges:
                    if vo(valu[u], reference) > 0 and v in g2s and u in g2s:   # del_edge: no-op unless both exist
                        g2s[v].discard(u); g2p[u].discard(v)
                check.add(v)
            elif len(edges) > 1:
                del_node(v)
            else:
                check.add(v)
        while check:                                   # lines 43-50
            v = min(check); check.discard(v)
            if not g2s[v]:
                check |= g2p[v]
                del_node(v)
        for v in g2s:
            valued[v] = True
        todo, rest = set(), set()
        for v in range(n):                             # lines 55-59
            if valued[v]:
                todo |= ppred[v]
            else:
                rest.add(v)

        def cu1(v, u):
            a, b, c = valu2[u]
            return (a, b | {v}, c + 1)

        def cu(v):                                     # lines 62-67
            p = sorted(u for u in psucc[v] if valued[u])
            if self.pl[v] == EVEN:
                c = lambda x, y: vo(valu2[x], valu2[y])
            else:
                c = lambda x, y: vo(valu2[y], valu2[x])
            mx = p[0]
            for u in p:
                if c(u, mx) > 0:
                    mx = u
            return mx
        while rest:                                    # lines 69-101
            while todo:
                v = min(todo); todo.discard(v)
                succs = psucc[v]
                if not valued[v]:
                    if all(valued[u] for u in succs):
                        valued[v] = True
                        u = cu(v)
                        valu2[v] = cu1(v, u)
                        if self.pl[v] == EVEN:
                            strategy[v] = u
                    elif self.pl[v] == ODD and any(valued[u] and vo(cu1(v, u), valu2[v]) == 0 for u in succs):
                        raise RuntimeError("impossible")
                    if valued[v]:
                        todo |= ppred[v]
                        rest.discard(v)
            if rest:
                temp = sorted(v for v in rest if self.pl[v] == ODD and any(valued[u] for u in psucc[v]))
                if not temp:
                    raise RuntimeError("crap")
                l = [(v, cu1(v, cu(v))) for v in reversed(temp)]   # fold ascending, prepend -> descending
                best_v, best_va = l[0]
                for v, va in l[1:]:                    # list_max ... (fun a b -> valu_ord a b > 0): first minimum
                    if vo(best_va, va) > 0:
                        best_v, best_va = v, va
                todo |= ppred[best_v]
                rest.discard(best_v)
                valu2[best_v] = best_va
                valued[best_v] = True
        return strategy

    def best_in(self, valu, v, succs):
        o = lambda x, y: self.nvto(valu, x, y) >= 0
        if self.pl[v] == ODD:
            return self.ns_max(succs, lambda a, b: o(a, b))
        return self.ns_max(succs, lambda a, b: o(b, a))

    def solve(self, max_iter=None, policy="switchall"):
        strat = self.initial_strategy_by_best_reward() if policy == "switchall" else self.initial_strategy_by_last_edge()
        pol = self.policy_switchall if policy == "switchall" else self.policy_switchbest
        valu = self.evaluate(strat)
        counter = 0
        improvable = lambda: any(self.pl[i] == EVEN and self.nvo(valu[strat[i]], valu[self.best(valu, i)]) < 0
                                 for i in range(self.g.n))
        while improvable():
            counter += 1
            if max_iter and counter > max_iter:
                raise RuntimeError("iteration cap")
            strat = pol(strat, valu)
            valu = self.evaluate(strat)
        counter += 1
        win = [self.pr[valu[i][0]] % 2 for i in range(self.g.n)]
        ws = [strat[i] if (win[i] == self.pl[i] == EVEN) else (self.best(valu, i) if win[i] == self.pl[i] else None)
              for i in range(self.g.n)]
        return win, ws, counter


def alternating_transformation(g):
    """transformations.ml:338-394 with total = true (every vertex here has a successor)."""
    n = g.n
    counter, ptr = n, -1
    altmap = [(-1, -1)] * n
    succ = [sorted(set(s)) for s in g.succ]
    for i in range(n):
        for j in succ[i]:
            if g.owner[i] == g.owner[j] and altmap[j] == (-1, -1):
                altmap[j] = (counter, ptr); counter += 1; ptr = j
    prio, owner, nsucc = [0] * counter, [0] * counter, [[] for _ in range(counter)]
    for i in range(n):
        prio[i], owner[i] = g.prio[i], g.owner[i]
        nsucc[i] = sorted({altmap[j][0] if g.owner[i] == g.owner[j] else j for j in succ[i]})
    while ptr != -1:
        ind, prev = altmap[ptr]
        prio[ind], owner[ind], nsucc[ind] = 0, 1 - g.owner[ptr], [ptr]
        ptr = prev
    return pg.Game(prio, owner, nsucc)


def cheap_escape_cycles_transformation(g):
    """transformations.ml:271-320 with keep_scc = false."""
    n = g.n
    prio = [p + 2 for p in g.prio] + [1, 0, 0, 0]
    owner = list(g.owner) + [ODD, EVEN, EVEN, ODD]
    succ = [sorted(set(g.succ[i]) | {n if g.owner[i] == EVEN else n + 1}) for i in range(n)]
    succ += [[n + 2], [n + 3], [n], [n + 1]]
    return pg.Game(prio, owner, succ)


def solve_switchbest(g, max_iter=None):
    """strategy_improvement_by_policy (stratimpralgs.ml:636-637) -> strategy_improvement' (600-616):
    alternating transformation, cheap escape cycles, SI from the last edge, then restrict back."""
    g1 = alternating_transformation(g)
    g2 = cheap_escape_cycles_transformation(g1)
    win2, ws2, k = SI(g2).solve(max_iter, policy="switchbest")
    win = win2[:g.n]
    ws = []
    for i in range(g.n):
        s = ws2[i]
        if s is None or win[i] != g.owner[i]:
            ws.append(None)
        elif s < g.n:
            ws.append(s)
        else:
            ws.append(g1.succ[s][0] if s < g1.n else None)  # alternating_revertive_restriction: dummy -> its successor
    return win, ws, k


if __name__ == "__main__":
    g = pg.read(sys.argv[1])
    if "--switchbest" in sys.argv:
        sys.argv.remove("--switchbest")
        win, ws, k = solve_switchbest(g)
    else:
        win, ws, k = SI(g).solve()
    print(f"solved with {k} iterations.", file=sys.stderr)
    if len(sys.argv) > 2:
        pg.write_sol(win, sys.argv[2], ws)
    else:
        sys.stdout.write(f"paritysol {g.n};\n" + "".join(f"{v} {w}{'' if ws[v] is None else ' ' + str(ws[v])};\n" for v, w in enumerate(win)))
