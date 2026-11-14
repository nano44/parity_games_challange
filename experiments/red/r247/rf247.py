#!/usr/bin/env python3
"""L-RED 71 R247: candidate RF («ROOT-FIRST»; L-SI 57), OWN implementation from the rule as the Lead relayed it (2026-11-14 14:06Z):
  «one-sided, memoryless, inside the classical VJ scheme: in the play graph of (sigma, sigma-bar), an improvable Even vertex v DEPENDS on an
   improvable u != v iff u lies on the play from sigma(v) or from one of v's improving targets; switch-best exactly at the improvable
   vertices in the SINK strongly connected components of the dependency digraph.»
Readings made here (each a parameter, so that a difference from L-SI's counts can be located; defaults = the plain reading):
  R1 the play from w is w, nxt(w), nxt(nxt(w)), ... with nxt = sigma at Even and sigma-bar at Odd vertices, the WHOLE play: path and cycle,
     w itself included (INCL_W = True);
  R2 «improving targets» = every w in I(v) (ALL_TARGETS = True; False: only the Xi-best one);
  R3 a sink component is a strongly connected component of the dependency digraph with no edge into another component; a single vertex
     with no dependency is a sink component;
  R4 switch-best: the Xi-best improving successor, ties to the larger index (as si247's howard).
The rule is registered in si247.RULES as «rf». dep(e, sigma, sbar, I) returns the dependency digraph (dict v -> set of u)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE]
import si247
INCL_W = True; ALL_TARGETS = True

def dep(e, sigma, val, sbar, I):
    n = e.n; nxt = [sigma[v] if e.isE[v] else sbar[v] for v in range(n)]
    imp = set(I); memo = {}
    def onplay(w):
        """improvable vertices on the play from w (w included)"""
        if w in memo: return memo[w]
        path = []; pos = {}; x = w
        while x not in pos and x not in memo:
            pos[x] = len(path); path.append(x); x = nxt[x]
        if x in memo: tail = memo[x]
        else:
            cyc = path[pos[x]:]; tail = frozenset(y for y in cyc if y in imp)
            for y in cyc: memo[y] = tail
            path = path[:pos[x]]
        for y in reversed(path):
            tail = tail | {y} if y in imp else tail
            memo[y] = frozenset(tail)
        return memo[w]
    D = {}
    for v, ws in I.items():
        targets = [sigma[v]] + (list(ws) if ALL_TARGETS else [e.best(val, ws)])
        s = set()
        for t in targets:
            s |= onplay(t) if INCL_W else onplay(nxt[t])
        s.discard(v); D[v] = s
    return D

def sinks(D):
    """vertices of the sink strongly connected components of the digraph D (Tarjan, iterative)"""
    index = {}; low = {}; onst = set(); st = []; comp = {}; cid = 0; counter = 0
    for root in D:
        if root in index: continue
        work = [(root, iter(sorted(D[root])))]; index[root] = low[root] = counter; counter += 1; st.append(root); onst.add(root)
        while work:
            v, it = work[-1]; adv = False
            for u in it:
                if u not in index:
                    index[u] = low[u] = counter; counter += 1; st.append(u); onst.add(u); work.append((u, iter(sorted(D[u])))); adv = True; break
                elif u in onst: low[v] = min(low[v], index[u])
            if adv: continue
            work.pop()
            if work: low[work[-1][0]] = min(low[work[-1][0]], low[v])
            if low[v] == index[v]:
                while True:
                    u = st.pop(); onst.discard(u); comp[u] = cid
                    if u == v: break
                cid += 1
    nonsink = {comp[v] for v in D for u in D[v] if comp[u] != comp[v]}
    return {v for v in D if comp[v] not in nonsink}, comp

def rule_rf(e, sigma, val, sbar, I):
    D = dep(e, sigma, val, sbar, I); S, _ = sinks(D)
    return {v: e.best(val, I[v]) for v in S}

si247.RULES["rf"] = rule_rf
