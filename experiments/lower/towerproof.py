#!/usr/bin/env python3
"""T-L2 step 2: readable refutation attempt in TYPE form. Variables x[j][t] = [depth-(j-1) type t is accepted by gate j]
(j = 1..k); s_j(v) = OR/AND over successors w of x[j][type_{j-1}(w)]; the output must be a function of the k-profile.
Top-down DPLL with unit propagation; prints the derivation (branch decisions and the forced literals with their reasons)
so that its size can be judged. Usage: towerproof.py core.json k [maxdepth]"""
import sys, os, json, time, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pysat.solvers import Cadical153, Glucose4
from levels import load_core, types
from coremin import struct_only


class Inst:
    def __init__(self, core, k):
        S, W = struct_only(core)
        self.owner = [int(o) for o in S.owner]; self.p2 = [int(p == 2) for p in S.prio]
        self.succ = [[int(w) for w in S.indices[S.indptr[v]:S.indptr[v + 1]]] for v in range(S.N)]
        self.W = [bool(w) for w in W]; self.N = S.N; self.k = k
        self.T = types(self.owner, self.p2, self.succ, k)
        self.var = {}; self.name = {}
        def new(nm):
            i = len(self.var) + 1; self.var[nm] = i; self.name[i] = nm; return i
        # x[j][t] for occurring successor types
        for j in range(1, k + 1):
            for t in sorted(set(self.T[j - 1][w] for v in range(self.N) for w in self.succ[v])):
                new(("x", j, t))
        # s_j(v): one variable per (j, depth-j type of v) since s_j is constant on depth-j types
        for j in range(1, k + 1):
            for t in sorted(set(self.T[j])):
                new(("s", j, t))
        self.cl = []
        for j in range(1, k + 1):
            done = set()
            for v in range(self.N):
                t = self.T[j][v]
                if t in done: continue
                done.add(t)
                sv = self.var[("s", j, t)]
                xs = sorted(set(self.var[("x", j, self.T[j - 1][w])] for w in self.succ[v]))
                if self.owner[v] == 0:
                    self.cl.append([-sv] + xs); [self.cl.append([sv, -x]) for x in xs]
                else:
                    self.cl.append([sv] + [-x for x in xs]); [self.cl.append([-sv, x]) for x in xs]
        # output: for every pair (u winning, u' losing) with the same base labels, some s_j differs; one clause per type pair
        # d[j][(t,t')] = [s_j differs on depth-j types t, t'] encoded via XOR of the two s variables
        self.pairs = set()
        for u in range(self.N):
            for u2 in range(self.N):
                if self.W[u] and not self.W[u2] and self.p2[u] == self.p2[u2] and self.owner[u] == self.owner[u2]:
                    self.pairs.add((self.T[k][u], self.T[k][u2]))
        self.pairs = sorted(self.pairs)
        # depth-k type -> its depth-j types
        rep = {}
        for v in range(self.N): rep.setdefault(self.T[k][v], v)
        for (t, t2) in self.pairs:
            u, u2 = rep[t], rep[t2]
            lits = []
            for j in range(1, k + 1):
                a, b = self.var[("s", j, self.T[j][u])], self.var[("s", j, self.T[j][u2])]
                if a == b: continue
                d = new(("d", j, self.T[j][u], self.T[j][u2]))
                # d -> (a xor b)
                self.cl.append([-d, a, b]); self.cl.append([-d, -a, -b]); lits.append(d)
            self.cl.append(lits)   # may be empty: then the pair is unseparable at depth k (W not a function of depth-k types)


if __name__ == "__main__":
    core = load_core(sys.argv[1]); k = int(sys.argv[2])
    I = Inst(core, k)
    nx = sum(1 for nm in I.var if nm[0] == "x"); ns = sum(1 for nm in I.var if nm[0] == "s")
    print(f"type-form instance: {nx} x-variables (gate, type), {ns} s-variables, {len(I.pairs)} W-pairs of depth-{k} types, {len(I.cl)} clauses")
    for Sv in (Cadical153, Glucose4):
        t0 = time.time(); s = Sv(bootstrap_with=I.cl, with_proof=(Sv is Glucose4)); r = s.solve()
        pf = s.get_proof() if Sv is Glucose4 else None; s.delete()
        print(f"{Sv.__name__}: {'SAT' if r else 'UNSAT'} [{time.time()-t0:.1f}s]" + (f"; DRUP proof: {len(pf)} lines, {sum(1 for l in pf if l.startswith('d'))} deletions" if pf is not None else ""))
