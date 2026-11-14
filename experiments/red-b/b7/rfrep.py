#!/usr/bin/env python3
"""L-RED-B B7: RF with a REPAIRED dependency (the Lead's question of 2026-11-14 15:20Z, item 4), on K^s_n and on Friedmann's G_n.
Reading A ("every Even vertex with a choice on the two plays"): CH := the Even vertices with at least two successors.
  For v in CH: D'(v) := (pi(sigma(v)) u U_{w in T(v)} pi(w)) n CH minus {v}   (T(v) empty if v is not improvable).
  Delta' := (CH, D').  A component of Delta' is ACTIVE if it holds an improvable vertex.  S' := the improvable vertices of the
  active components from which no OTHER active component can be reached in Delta'.  Every v in S' moves to its best target.
  (So v waits for every improvable vertex it can reach through chains of choice vertices on plays, improvable or not: the
  transitive form; without «active» the rule would stall whenever a sink component holds no improvable vertex.)
Reading B ("a fixed point of the sink selection"): S_0 := RF's set S. Repeat: let sigma' := sigma with S_k switched; drop from
  S_k every v that has, under sigma', an improvable vertex u != v outside S_k on the play from its new target (it would have
  waited had it seen the others' switches); stop when nothing is dropped (if everything would be dropped, keep the vertices
  dropped last). The survivors move.
Usage: rfrep.py A|B ks NMIN NMAX | A|B lmcs NMIN NMAX"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
for p in (HERE, os.path.join(HERE, "..", "..", "..", "b7")):
    sys.path.insert(0, p)
sys.dont_write_bytecode = True
import rfc2, gens7
from si7 import Engine, root_first, play_vertices, sccs, rf_dependency, EVEN


def rule_A(tie="high"):
    def rule(E, sigma, val, tau, imp, kv):
        CH = [v for v in E.evens if len(E.succ[v]) >= 2]; chs = set(CH); memo = {}
        adj = {}
        for v in CH:
            d = set(play_vertices(E, sigma, tau, sigma[v], memo))
            for w in imp.get(v, []):
                d |= play_vertices(E, sigma, tau, w, memo)
            d &= chs; d.discard(v); adj[v] = d
        comp, nc = sccs(CH, adj)
        active = [False] * nc
        for v in imp: active[comp[v]] = True
        cadj = [set() for _ in range(nc)]
        for v in CH:
            for u in adj[v]:
                if comp[u] != comp[v]: cadj[comp[v]].add(comp[u])
        reach_active = [None] * nc
        def ra(c):                       # does c reach an active component other than itself?
            if reach_active[c] is None:
                reach_active[c] = False
                reach_active[c] = any(active[x] or ra(x) for x in cadj[c])
            return reach_active[c]
        new = list(sigma)
        for v in imp:
            if not ra(comp[v]): new[v] = E.best_target(v, sigma, kv, tie)
        return new
    return rule


def rule_B(tie="high"):
    def rule(E, sigma, val, tau, imp, kv):
        adj = rf_dependency(E, sigma, tau, imp); comp, nc = sccs(list(imp), adj)
        sink = [True] * nc
        for v in imp:
            for u in adj[v]:
                if comp[u] != comp[v]: sink[comp[v]] = False
        S = [v for v in imp if sink[comp[v]]]; best = {v: E.best_target(v, sigma, kv, tie) for v in S}
        while True:
            s2 = list(sigma)
            for v in S: s2[v] = best[v]
            val2, tau2 = E.evaluate(s2); imp2, _ = E.improving(s2, val2); memo = {}; Sset = set(S)
            drop = [v for v in S if any(u != v and u not in Sset and u in imp2 for u in play_vertices(E, s2, tau2, best[v], memo))]
            if not drop: break
            if len(drop) == len(S): S = drop; break
            S = [v for v in S if v not in drop]
        new = list(sigma)
        for v in S: new[v] = best[v]
        return new
    return rule


if __name__ == "__main__":
    mk = {"A": rule_A, "B": rule_B}[sys.argv[1]]; fam = sys.argv[2]
    for n in range(int(sys.argv[3]), int(sys.argv[4]) + 1):
        g, s0 = rfc2.build(n, True) if fam == "ks" else gens7.lmcs(n, "fig4")
        E = Engine(g); k, sg, val, tau = E.run(s0, mk(), maxit=200000)
        E2 = Engine(g); k0 = E2.run(s0, root_first("high"))[0]
        print(f"B7 repair {sys.argv[1]} {fam} n {n} |V| {g.n}: iterations {k} (RF {k0}; law {7 * 2 ** (n - 1) - 2 * n - 3 if fam == 'ks' else 3 * n + 3}) odd-won {E.regions(val).count(1) if val else -1}", flush=True)
