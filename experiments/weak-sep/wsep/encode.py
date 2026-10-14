"""SAT encoding: 'is there a deterministic safety automaton with k (non-bottom) states that is a weak / strong
(n,d)-separator?'  See docs/struct/S1-statement.md D4-D5 and docs/lit/T4-weak-separators.md §3(b) for the sketch.

Variables
  t[q][a][q2]   delta(q, a+1) = q2, q2 in 0..k-1 or k (= bottom); exactly one per (q, a).  State 0 is initial.
Per even graph H (W1):   R[v][q] over-approximates the reachable product states from V(H) x {0}: R[v][0];
                         R[v][q] & t[q][a][q2] -> R[v2][q2] for (v,a+1,v2) in E(H);   R[v][q] -> not t[q][a][bottom].
Per odd graph H (W2):    same R; plus a rank r(v,q) in [0, N), N = n*k, in thermometer encoding u[x][j] = (r(x) >= j),
                         with R[v][q] & t[q][a][q2] -> r(v,q) > r(v2,q2).  Acyclic reachable product <=> rejection of all
                         infinite paths of H (KV 1902.07175 App. A gives the same characterisation).
Strong (S2):             for every odd letter p, a rank on Q (thermometer, range [0,k]) non-increasing on letters < p and
                         decreasing on letter p: no cycle of A with odd maximum.  All states are reachable (symmetry
                         breaking below), so this is 'L(A) subset of LimsupEven'.
Symmetry breaking:       BFS numbering of states (Heule-Verwer 2010): state j >= 1 has parent par(j) = least i with an
                         edge i -> j; par is non-decreasing in j; for equal parents the least letter i -> j is smaller
                         than the least letter i -> j+1.  This forces every state reachable, so k is the exact state count
                         of a reachable automaton; the search over k = 1, 2, ... stops at the first SAT k, which is w or s
                         because a minimum-size separator has all states reachable.
Soundness of the over-approximation: the least closed R is contained in any closed R, so a solution with any closed R
certifies the property; conversely the exact reachable set plus a topological order is a solution.  Every automaton the
solver returns is re-checked by wsep.automata (independent code path) before it is reported.
"""
from __future__ import annotations
import itertools
from pysat.solvers import Solver
from .graphs import Graph


class Encoder:
    def __init__(self, n, d, k, strong, solver_name='cadical153'):
        self.solver_name = solver_name
        self.n, self.d, self.k, self.strong = n, d, k, strong
        self.nv = 0
        self.solver = Solver(name=solver_name)
        self.nclauses = 0
        self.t = [[[self.new() for _ in range(k + 1)] for _ in range(d)] for _ in range(k)]
        for q in range(k):
            for a in range(d):
                self.exactly_one(self.t[q][a])
        self.symmetry_breaking()
        if strong:
            self.strong_condition()

    def new(self):
        self.nv += 1
        return self.nv

    def add(self, cl):
        self.solver.add_clause(cl)
        self.nclauses += 1

    def exactly_one(self, xs):
        self.add(list(xs))
        for i in range(len(xs)):
            for j in range(i + 1, len(xs)):
                self.add([-xs[i], -xs[j]])

    # --- Heule-Verwer BFS symmetry breaking ---
    def symmetry_breaking(self):
        k, d, t = self.k, self.d, self.t
        e = [[None] * k for _ in range(k)]  # e[i][j]: some letter i -> j
        for i in range(k):
            for j in range(k):
                e[i][j] = self.new()
                self.add([-e[i][j]] + [t[i][a][j] for a in range(d)])
                for a in range(d):
                    self.add([-t[i][a][j], e[i][j]])
        par = [[None] * k for _ in range(k)]  # par[j][i], i < j
        for j in range(1, k):
            for i in range(j):
                p = par[j][i] = self.new()
                # p <-> e[i][j] & AND_{i'<i} not e[i'][j]
                self.add([-p, e[i][j]])
                for i2 in range(i):
                    self.add([-p, -e[i2][j]])
                self.add([p, -e[i][j]] + [e[i2][j] for i2 in range(i)])
            self.add([par[j][i] for i in range(j)])  # every state j >= 1 has a parent (hence reachable)
        for j in range(1, k - 1):  # parents non-decreasing
            for i in range(j):
                for i2 in range(i):
                    self.add([-par[j][i], -par[j + 1][i2]])
        m = {}  # m[i][j][a]: a is the least letter with i -> j
        for i in range(k):
            for j in range(k):
                for a in range(d):
                    v = m[i, j, a] = self.new()
                    self.add([-v, t[i][a][j]])
                    for b in range(a):
                        self.add([-v, -t[i][b][j]])
                    self.add([v, -t[i][a][j]] + [t[i][b][j] for b in range(a)])
        for j in range(1, k - 1):
            for i in range(j):
                for a in range(d):
                    for b in range(a + 1):
                        self.add([-par[j][i], -par[j + 1][i], -m[i, j, a], -m[i, j + 1, b]])

    # --- thermometer ranks ---
    def thermo(self, N):
        """returns u with u[j] = (r >= j) for j in 0..N; u[0] = True, u[N] = False, chained."""
        u = [None] * (N + 1)
        for j in range(1, N):
            u[j] = self.new()
        for j in range(1, N - 1):
            self.add([-u[j + 1], u[j]])
        return u

    def greater(self, ux, uy, N, cond):
        """cond -> r(x) > r(y), i.e. for all j: r(y) >= j -> r(x) >= j+1."""
        for j in range(N):
            cl = list(cond)
            if j > 0:
                cl.append(-uy[j])
            if j + 1 < N:
                cl.append(ux[j + 1])
            self.add(cl)  # (not cond) or not uy[j] or ux[j+1]; uy[0]=True, ux[N]=False omitted

    def strong_condition(self):
        k, d, t = self.k, self.d, self.t
        for p in range(1, d + 1, 2):
            N = k + 1
            u = [self.thermo(N) for _ in range(k)]
            for q in range(k):
                for q2 in range(k):
                    for a in range(p):  # letters 1..p
                        if a + 1 < p:  # non-increasing: r(q) >= r(q2)
                            for j in range(1, N):
                                self.add([-t[q][a][q2], -u[q2][j], u[q][j]])
                        else:  # letter p: strictly decreasing
                            self.greater(u[q], u[q2], N, [-t[q][a][q2]])

    # --- per-graph constraints ---
    def reach_vars(self, g: Graph):
        k, t = self.k, self.t
        R = [[self.new() for _ in range(k)] for _ in range(g.n)]
        for v in range(g.n):
            self.add([R[v][0]])
        for (v, p, v2) in g.edges:
            for q in range(k):
                for q2 in range(k):
                    self.add([-R[v][q], -t[q][p - 1][q2], R[v2][q2]])
        return R

    def add_even(self, g: Graph):
        R = self.reach_vars(g)
        for (v, p, v2) in g.edges:
            for q in range(self.k):
                self.add([-R[v][q], -self.t[q][p - 1][self.k]])

    def add_odd(self, g: Graph):
        k, t = self.k, self.t
        R = self.reach_vars(g)
        N = g.n * k
        u = [[self.thermo(N) for _ in range(k)] for _ in range(g.n)]
        for (v, p, v2) in g.edges:
            for q in range(k):
                for q2 in range(k):
                    self.greater(u[v][q], u[v2][q2], N, [-R[v][q], -t[q][p - 1][q2]])

    def require_odd_cycle_max_at_most(self, pmax):
        """Add: the transition graph has a closed walk (hence a simple cycle) whose letters are <= pmax and whose maximum
        is odd (some step uses an odd letter p with every letter on the walk <= p; we fix p = pmax, caller loops over odd
        pmax).  Walk of length k with pauses: positions 0..k (pos k = pos 0), one-hot states; each step pauses or follows
        a transition with letter <= pmax; at least one step uses letter pmax."""
        k, t = self.k, self.t
        L = k
        x = [[self.new() for _ in range(k)] for _ in range(L + 1)]
        for i in range(L + 1):
            self.exactly_one(x[i])
        for q in range(k):
            self.add([-x[L][q], x[0][q]]); self.add([x[L][q], -x[0][q]])
        step = {}
        for i in range(L):
            opts = []
            pause = self.new(); opts.append(pause)
            for q in range(k):
                self.add([-pause, -x[i][q], x[i + 1][q]])
            for a in range(pmax):
                s = step[i, a] = self.new(); opts.append(s)
                for q in range(k):
                    for q2 in range(k):
                        self.add([-s, -x[i][q], -x[i + 1][q2], t[q][a][q2]])
            self.add(opts)
        self.add([step[i, pmax - 1] for i in range(L)])

    def solve(self):
        if not self.solver.solve():
            return None
        model = set(x for x in self.solver.get_model() if x > 0)
        delta = []
        for q in range(self.k):
            row = []
            for a in range(self.d):
                q2 = [x for x in range(self.k + 1) if self.t[q][a][x] in model]
                assert len(q2) == 1
                row.append(None if q2[0] == self.k else q2[0])
            delta.append(row)
        return {'k': self.k, 'd': self.d, 'delta': delta}

    def delete(self):
        self.solver.delete()
