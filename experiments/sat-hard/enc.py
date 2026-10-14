"""SAT encoding of 'a deterministic safety automaton with k non-bottom states is a weak (n,d)-separator for the given
even / odd graphs' (convention E). Written from L-STRUCT's specification (claude/l-struct 42dbbc2,
experiments/weak-sep/wsep/encode.py docstring) but implemented independently, with two changes:
  * odd-graph ranks use a shared 'successor rank' auxiliary: y[v2,p,q][j] <-> rank(v2, delta(q,p)) >= j, so each
    product edge costs N clauses instead of k*N (N = rank range);
  * ranks are only needed inside strongly connected components of the odd graph (a product cycle projects to a closed
    walk of H, hence stays inside one SCC of H); N = |SCC| * k.
Variables: t[q][a][x] (x in 0..k, k = bottom), exactly one per (q,a); state 0 initial; BFS symmetry breaking
(Heule-Verwer 2010: parents non-decreasing, equal parents ordered by least letter) so all states are reachable.
Even graph H: R[v][q] for all v: R[v][0]; R[v][q] & t[q][p][q2] -> R[v2][q2]; R[v][q] -> -t[q][p][bottom].
Odd graph H: same R; rank u[v][q] (thermometer) with R[v][q] & t[q][p][q2] -> r(v,q) > r(v2,q2) inside SCCs.
Sound and complete for the given graph set: any model is a separator for those graphs (the checker re-verifies against
the full family); conversely a separator gives a model (exact reachable set + topological ranks)."""
from __future__ import annotations


class CNF:
    def __init__(self):
        self.nv, self.clauses = 0, []

    def new(self):
        self.nv += 1
        return self.nv

    def add(self, c):
        self.clauses.append(c)

    def exactly_one(self, xs):
        self.add(list(xs))
        for i in range(len(xs)):
            for j in range(i + 1, len(xs)):
                self.add([-xs[i], -xs[j]])

    def dimacs(self, path):
        with open(path, "w") as f:
            f.write(f"p cnf {self.nv} {len(self.clauses)}\n")
            for c in self.clauses:
                f.write(" ".join(map(str, c)) + " 0\n")


def sccs(n, edges):
    adj = [[] for _ in range(n)]
    for (u, p, v) in edges:
        adj[u].append(v)
    reach = [set() for _ in range(n)]
    for s in range(n):
        st, seen = [s], {s}
        while st:
            x = st.pop()
            for y in adj[x]:
                if y not in seen:
                    seen.add(y); st.append(y)
        reach[s] = seen
    comp = [-1] * n
    c = 0
    for v in range(n):
        if comp[v] < 0:
            for w in range(n):
                if w in reach[v] and v in reach[w]:
                    comp[w] = c
            c += 1
    return comp


class Encoding(CNF):
    def __init__(self, n, d, k, symmetry=True):
        super().__init__()
        self.n, self.d, self.k = n, d, k
        self.t = [[[self.new() for _ in range(k + 1)] for _ in range(d)] for _ in range(k)]
        for q in range(k):
            for a in range(d):
                self.exactly_one(self.t[q][a])
        if symmetry:
            self._bfs()

    def _bfs(self):
        k, d, t = self.k, self.d, self.t
        e = [[self.new() for _ in range(k)] for _ in range(k)]
        for i in range(k):
            for j in range(k):
                self.add([-e[i][j]] + [t[i][a][j] for a in range(d)])
                for a in range(d):
                    self.add([-t[i][a][j], e[i][j]])
        par = {}
        for j in range(1, k):
            for i in range(j):
                p = par[j, i] = self.new()
                self.add([-p, e[i][j]])
                for i2 in range(i):
                    self.add([-p, -e[i2][j]])
                self.add([p, -e[i][j]] + [e[i2][j] for i2 in range(i)])
            self.add([par[j, i] for i in range(j)])
        for j in range(1, k - 1):
            for i in range(j):
                for i2 in range(i):
                    self.add([-par[j, i], -par[j + 1, i2]])
        m = {}
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
                        self.add([-par[j, i], -par[j + 1, i], -m[i, j, a], -m[i, j + 1, b]])

    def _reach(self, g):
        n, E = g
        k, t = self.k, self.t
        R = [[self.new() for _ in range(k)] for _ in range(n)]
        for v in range(n):
            self.add([R[v][0]])
        for (v, p, v2) in E:
            for q in range(k):
                for q2 in range(k):
                    self.add([-R[v][q], -t[q][p - 1][q2], R[v2][q2]])
        return R

    def add_even(self, g):
        n, E = g
        R = self._reach(g)
        for (v, p, v2) in E:
            for q in range(self.k):
                self.add([-R[v][q], -self.t[q][p - 1][self.k]])

    def add_odd(self, g):
        if getattr(self, "binary", False):
            return self.add_odd_binary(g)
        n, E = g
        k, t = self.k, self.t
        R = self._reach(g)
        comp = sccs(n, E)
        size = {c: comp.count(c) for c in set(comp)}
        inner = [(v, p, v2) for (v, p, v2) in E if comp[v] == comp[v2]]
        u = {}
        for v in range(n):
            N = size[comp[v]] * k
            for q in range(k):
                # thermometer u[v,q][j] = rank >= j, j = 1..N-1 (rank in [0, N))
                u[v, q] = [None] + [self.new() for _ in range(N - 1)]
                for j in range(1, N - 1):
                    self.add([-u[v, q][j + 1], u[v, q][j]])
        y = {}
        for (v, p, v2) in inner:
            N = size[comp[v]] * k
            for q in range(k):
                key = (v2, p, q)
                if key not in y:  # y[j] >= rank(v2, delta(q,p)) >= j for successor states inside the SCC
                    yy = [None] + [self.new() for _ in range(N - 1)]
                    for q2 in range(k):
                        for j in range(1, N):
                            self.add([-t[q][p - 1][q2], -u[v2, q2][j], yy[j]])
                    y[key] = yy
                yy = y[key]
                # R[v][q] -> rank(v,q) > rank(succ): rank(v,q) >= 1 always (succ >= 0), and >= j+1 if y[j]
                # successor (non-bottom) exists -> rank(v,q) >= 1
                self.add([-R[v][q], t[q][p - 1][k]] + ([u[v, q][1]] if N > 1 else []))
                for j in range(1, N):
                    self.add([-R[v][q], -yy[j]] + ([u[v, q][j + 1]] if j + 1 < N else []))
        # a product edge inside an SCC whose successor rank would need to be < 0 is impossible: covered above.

    def decode(self, model):
        pos = set(x for x in model if x > 0)
        delta = []
        for q in range(self.k):
            row = []
            for a in range(self.d):
                xs = [x for x in range(self.k + 1) if self.t[q][a][x] in pos]
                assert len(xs) == 1
                row.append(None if xs[0] == self.k else xs[0])
            delta.append(row)
        return {"k": self.k, "d": self.d, "delta": delta}


def add_reject_lasso(e, u, v):
    """Constraint: the automaton rejects u.v^w, i.e. its run on u.v^k hits bottom (k = number of states: if the run
    survives |u| + k|v| letters, two v-boundary states repeat and the run never rejects)."""
    k, t = e.k, e.t
    word = list(u) + list(v) * k
    x = [e.new() for _ in range(k + 1)]
    e.add([x[0]])
    for p in word:
        y = [e.new() for _ in range(k + 1)]
        for q in range(k):
            for q2 in range(k + 1):
                e.add([-x[q], -t[q][p - 1][q2], y[q2]])
        e.add([-x[k], y[k]])
        x = y
    e.add([x[k]])


def _bits(N):
    b = 1
    while (1 << b) < N:
        b += 1
    return b


def add_odd_binary(self, g):
    """Odd graph with BINARY ranks: r(v,q) in [0, 2^B), B = bits(|SCC|*k); successor rank bits z[v2,p,q] are tied to
    r(v2, delta(q,p)) by t[q][p][q2] -> (z = r(v2,q2)); then R[v][q] & (successor non-bottom) -> r(v,q) > z via a
    lexicographic comparator (MSB first) with auxiliary 'equal so far' variables."""
    n, E = g
    k, t = self.k, self.t
    R = self._reach(g)
    comp = sccs(n, E)
    size = {c: comp.count(c) for c in set(comp)}
    inner = [(v, p, v2) for (v, p, v2) in E if comp[v] == comp[v2]]
    r = {}
    for v in range(n):
        B = _bits(size[comp[v]] * k)
        for q in range(k):
            r[v, q] = [self.new() for _ in range(B)]  # r[..][0] = MSB
    z = {}
    for (v, p, v2) in inner:
        B = len(r[v, 0])
        for q in range(k):
            key = (v2, p, q)
            if key not in z:
                zz = [self.new() for _ in range(B)]
                for q2 in range(k):
                    for b in range(B):
                        self.add([-t[q][p - 1][q2], -r[v2, q2][b], zz[b]])
                        self.add([-t[q][p - 1][q2], r[v2, q2][b], -zz[b]])
                z[key] = zz
            zz, a = z[key], r[v, q]
            # cond = R[v][q] & not t[q][p][bottom];  cond -> a > zz (lexicographic, MSB first)
            cond = [-R[v][q], t[q][p - 1][k]]
            eq = []  # eq[i]: a and zz agree on bits 0..i-1 (eq[0] = true)
            gt = []  # gt_i: first difference at bit i with a=1, zz=0
            prev_eq = None
            for b in range(B):
                gb = self.new()  # gb -> prefix equal and a_b=1 and zz_b=0
                self.add([-gb, a[b]]); self.add([-gb, -zz[b]])
                if prev_eq is not None:
                    self.add([-gb, prev_eq])
                gt.append(gb)
                if b < B - 1:
                    e2 = self.new()  # e2 -> prefix equal through bit b
                    if prev_eq is not None:
                        self.add([-e2, prev_eq])
                    self.add([-e2, -a[b], zz[b]]); self.add([-e2, a[b], -zz[b]])
                    prev_eq = e2
            self.add(cond + gt)


Encoding.add_odd_binary = add_odd_binary
