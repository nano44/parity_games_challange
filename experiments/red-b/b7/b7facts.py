#!/usr/bin/env python3
"""L-RED-B B7: must-0 counters for the facts of docs/red-b/B7-RF-sched.md, measured on the real run of RF on K^s_n.
At EVERY iteration:
  sink    vertices whose cycle node is not x                                   [Lemma SINK, gap G1]
  eqval   pairs of distinct successors of one vertex with equal valuations     [gap G5: no tie rule can matter]
  test    gates whose d is improvable although the gate is right, or not improvable although wrong, where
          wrong := (open and E > B) or (closed and B > E), E = Xi(h) + e, B = Xi(below)   [Lemma TEST]
At every STABLE state Z(t) (the state in which the next iteration is a CLOSE; t = number of closings so far):
  zclosed the set of closed gates is not CUR(t) + the stale gates that the qualification rule leaves closed
  zsel    R or a selector does not point where §4 says (R: entry of the lowest set bit's gate; g_i: f(current gate) if bit i
          is set, s(i, cx_t(i)) otherwise)
  zimp    the improvable set is not {d of the right-context gate of every unset bit} + {d of every stale closed gate}  [V1-V3]
  zsink   the set of RF's sinks is not {d(j, c)}, j the lowest unset bit                                              [ORDER]
Controls: B7F_CTRL=1: «right context» := the HIGHEST set bit above (zimp must fire for n >= 3); B7F_CTRL=2: the
qualification rule without its second clause (zclosed and zimp must fire for n >= 2).
Usage: b7facts.py NMIN NMAX"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
for p in (HERE, os.path.join(HERE, "..", "..", "..", "b7")):
    sys.path.insert(0, p)
sys.dont_write_bytecode = True
import rfc2
from si7 import Engine, root_first, rf_dependency, sccs
CTRL = int(os.environ.get("B7F_CTRL", "0"))


def run(n):
    g, s0 = rfc2.build(n, True); E = Engine(g); nm = g.names; idx = {a: k for k, a in enumerate(nm)}
    ctx = lambda i: rfc2.ctx(i, n)
    L = [(i, c) for i in range(n, 0, -1) for c in ctx(i)]; pos = {gc: k for k, gc in enumerate(L)}
    below = {L[k]: (f"C{L[k + 1][0]}.{L[k + 1][1]}" if k + 1 < len(L) else "R") for k in range(len(L))}
    V = lambda t, gc: idx[f"{t}{gc[0]}.{gc[1]}"]
    c = dict(sink=0, eqval=0, test=0, zclosed=0, zsel=0, zimp=0, zsink=0); st = dict(t=0, stale=set(), states=0, its=0)
    x = idx["x"]
    def tr(its, sigma, val, tau, imp):
        st["its"] = its
        kv = [E.key(val[v]) for v in range(E.n)]
        c["sink"] += sum(1 for v in range(E.n) if val[v][0] != x)
        for v in range(E.n):
            ks = [kv[u] for u in E.succ[v]]; c["eqval"] += len(ks) - len(set(ks))
        closed = {gc for gc in L if sigma[V("d", gc)] == V("e", gc)}
        for gc in L:
            Ev = (kv[V("h", gc)][0], kv[V("h", gc)][1] + E.sbit[V("e", gc)]); Bv = kv[idx[below[gc]]][:2]
            wrong = (Ev > Bv) if gc not in closed else (Bv > Ev)
            c["test"] += int(wrong != (V("d", gc) in imp))
        if not imp: return
        adj = rf_dependency(E, sigma, tau, imp); comp, nc = sccs(list(imp), adj); sk = [True] * nc
        for v in imp:
            for u in adj[v]:
                if comp[u] != comp[v]: sk[comp[v]] = False
        sinks = {v for v in imp if sk[comp[v]]}
        isclose = all(nm[v][0] == "d" and E.best_target(v, sigma, kv, "high") == idx["e" + nm[v][1:]] for v in sinks)
        if not isclose: return
        # stable state Z(t)
        t = st["t"]; st["states"] += 1
        bit = lambda i: (t >> (i - 1)) & 1
        def cx(i, hi=False):
            r = [j for j in range(i + 1, n + 1) if bit(j)]
            return "x" if not r else str(max(r) if hi else min(r))
        cur = {(i, cx(i)) for i in range(1, n + 1) if bit(i)}
        def qualifies(i, c1):
            return all(bit(k) for k in range(1, i)) and (CTRL == 2 or bool(bit(i)) or pos[(i, cx(i))] < pos[(i, c1)])
        st["stale"] = {gc for gc in st["stale"] | (st.get("prevcur", set()) - cur) if gc not in cur}
        st["stale"] = {gc for gc in st["stale"] if not qualifies(*gc)}
        c["zclosed"] += int(closed != cur | st["stale"])
        okR = (nm[sigma[idx["R"]]] == "x") if t == 0 else (sigma[idx["R"]] == V("f", (min(i for i in range(1, n + 1) if bit(i)), cx(min(i for i in range(1, n + 1) if bit(i))))))
        okg = all(sigma[idx[f"g{i}"]] == (V("f", (i, cx(i))) if bit(i) else V("s", (i, cx(i)))) for i in range(2, n + 1))
        c["zsel"] += int(not (okR and okg))
        pend = {V("d", (i, cx(i, CTRL == 1))) for i in range(1, n + 1) if not bit(i)}
        c["zimp"] += int(set(imp) != pend | {V("d", gc) for gc in st["stale"]})
        j = min(i for i in range(1, n + 1) if not bit(i))
        c["zsink"] += int(sinks != {V("d", (j, cx(j)))})
        st["prevcur"] = cur | {(j, cx(j))}       # after this close the new gate is current in t + 1 (recomputed there)
        st["t"] = t + 1
    E.run(s0, root_first("high"), trace=tr)
    return c, st


if __name__ == "__main__":
    bad = 0
    for n in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
        c, st = run(n)
        print(f"B7 facts n {n}: iterations {st['its']} stable states {st['states']} (2^n - 1 = {2 ** n - 1}) ctrl {CTRL}: " + " ".join(f"{k} {v}" for k, v in c.items()), flush=True)
        bad += sum(c.values()) + int(st["states"] != 2 ** n - 1)
    sys.exit(1 if bad else 0)
