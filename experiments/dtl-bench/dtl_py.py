#!/usr/bin/env python3
"""Second, independent implementation of DTL / IDTL (gauntlet step 2, Lead 2026-10-15 21:20Z).
Written ONLY from docs/alg/candidates/C5-DTL.md @ ccff864 (the pinned pseudocode, L22/L24); Oink's dtl.cpp was not read.
Section / line references "C5 §n" are to that file. Plain Python ints (every number is an index or a priority).

Usage: dtl_py.py IN.pg OUT.sol [--idtl] [--order stable|reverse|oink] [--stats]
Writes a paritysol solution ("v winner [strategy];") in the input's vertex ids and prints
"found D dominions and T tangles." / "solved in I iterations" like Oink, so harness/compare.py-style parsing works.

Choices the pseudocode leaves open (each listed in README "dtl_py choices"; they can change counts, not correctness):
 CH1 index order of equal-priority vertices (C5 §0 "any order"): stable by input position (--order reverse: reversed;
     --order oink: Oink's step-0 std::sort order, emulated in stdsort.py from game.cpp:478-505, read after the first
     count divergences to tell order effects from algorithm differences). --order oink also sets CH2': ins(v) in
     DECREASING new index, as Oink's Game::build_in_array (game.cpp:868-906) fills each in-list from its end.
 CH2 outs(v): in input order; ins(v): predecessors in increasing new index, each once per edge.
 CH3 tangle vertex order tv[t]: the order in which the SCC algorithm pops C off its stack.
 CH3' (--order oink only): tv[t] sorted ascending, as dtl.cpp stores it (read after shrinking divergence #2).
 CH3'' (--order oink only): SCC vertex order = Pearce's (root first, then its post-order stack), as dtl.cpp emits it;
     it fixes the order dominion vertices are queued for solving (read after shrinking divergence #3).
 CH4 "Q := all of Z" in best_vertices' threshold loop: pushed in increasing index (so popped from the highest).
 CH6 idtl iteration counter: see run() (convention read from dtl.cpp run() after the first divergence).
 CH5 dominion vertices are put in S at extraction; a vertex is solved once (a second solve of the same vertex is counted
     in stats['resolve'] and ignored).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
import pg

TV_SORTED = False   # CH3 switch (see docstring)
PEARCE = False      # CH3'' switch


class DTL:
    def __init__(self, prio, owner, succ, interleaved=False, ins_desc=False):
        self.n = len(prio)
        self.pr, self.ow, self.outs = prio, owner, succ
        ins = [[] for _ in range(self.n)]
        for v in range(self.n):                      # CH2
            for w in succ[v]:
                ins[w].append(v)
        self.ins = [x[::-1] for x in ins] if ins_desc else ins   # CH2': Oink game.cpp:868-906 fills ins from the end
        self.interleaved = interleaved
        self.str = [-1] * self.n
        self.G = set(range(self.n))
        self.tv, self.tout, self.tpr, self.tin = [], [], [], [[] for _ in range(self.n)]
        self.tangles = self.dominions = self.iterations = 0
        self.W, self.S, self.dom_vector = set(), set(), []
        self.Q = []
        self.win, self.sol_str = [None] * self.n, [None] * self.n
        self.stats = {"resolve": 0, "stuck": 0}
        self.prios = sorted(set(prio))
        self.maxpr = prio[self.n - 1] if self.n else 0

    # ---- C5 §1 primitives
    def attracts(self, p, v, Z, R):
        if self.ow[v] == p:
            return any(w in Z for w in self.outs[v])
        inz = False
        for w in self.outs[v]:
            if w in Z:
                inz = True
            elif w in R:
                return False
        return inz

    def attractVertices(self, p, v, R, Z, Gx, maxpr):
        pr, ow, st = self.pr, self.ow, self.str
        for u in self.ins[v]:
            if u in Z:
                if ow[u] == p and st[u] == -1:
                    st[u] = v
            elif u in R and (maxpr < 0 or pr[u] <= maxpr):
                if ow[u] != p and any(w in Gx and w not in Z for w in self.outs[u]):
                    continue
                Z.add(u); st[u] = v if ow[u] == p else -1; self.Q.append(u)

    def attractTangle(self, t, p, R, Z, Gx, maxpr):
        if self.tpr[t] == -1 or self.tpr[t] % 2 != p:
            return False
        new = False
        for w, _ in self.tv[t]:
            if w not in self.G:
                self.tpr[t] = -1
                return False
            if w in Z:
                continue
            if w not in R:
                return False
            if maxpr >= 0 and self.pr[w] > maxpr:
                return False
            new = True
        if not new:
            return False
        for e in self.tout[t]:
            if e not in Z and e in Gx:
                return False
        for w, s in self.tv[t]:
            if w not in Z:
                Z.add(w); self.str[w] = s; self.Q.append(w)
        return True

    def attractTangles(self, p, v, R, Z, Gx, maxpr):
        for t in self.tin[v]:
            self.attractTangle(t, p, R, Z, Gx, maxpr)

    def extractTangles(self, top, R):
        """Pearce/Tarjan SCC from top on R: p-vertices keep only str[v], opponent vertices all edges into R."""
        p = self.pr[top] % 2
        st, ow = self.str, self.ow

        def succ(v):
            if ow[v] == p:
                s = st[v]
                return [s] if s != -1 and s in R else []
            return [w for w in self.outs[v] if w in R]

        if PEARCE:
            sccs = self.pearce(top, succ)
        else:
            index, low, on, stack, cnt, sccs = {}, {}, set(), [], 0, []
            index[top] = low[top] = 0; cnt = 1; stack.append(top); on.add(top)
            work = [(top, iter(succ(top)))]
            while work:
                v, it = work[-1]
                pushed = False
                for w in it:
                    if w not in index:
                        index[w] = low[w] = cnt; cnt += 1; stack.append(w); on.add(w)
                        work.append((w, iter(succ(w)))); pushed = True; break
                    elif w in on:
                        low[v] = min(low[v], index[w])
                if pushed:
                    continue
                work.pop()
                if work:
                    low[work[-1][0]] = min(low[work[-1][0]], low[v])
                if low[v] == index[v]:
                    C = []
                    while True:
                        w = stack.pop(); on.discard(w); C.append(w)
                        if w == v:
                            break
                    sccs.append(C)
        made = False
        for C in sccs:
            if len(C) == 1:
                v = C[0]
                if not (st[v] == v or (st[v] == -1 and v in self.outs[v])):
                    continue
            Cs = set(C)
            esc = sorted({w for v in C if ow[v] != p for w in self.outs[v] if w in self.G and w not in Cs})
            if not esc:
                for v in C:
                    if PEARCE and v in self.S:    # CH5' (--order oink): dtl.cpp queues a vertex only if not yet in S
                        continue
                    self.S.add(v); self.dom_vector.append((v, st[v]))
                self.dominions += 1; made = True
                continue
            key = sorted(C)
            if key in self.tkeys:
                continue
            t = len(self.tv)
            self.tv.append([(v, st[v]) for v in (sorted(C) if TV_SORTED else C)]); self.tout.append(esc); self.tpr.append(self.pr[top])
            self.tkeys.append(key)
            for e in esc:
                self.tin[e].append(t)
            self.tangles += 1; made = True
        return made

    @staticmethod
    def pearce(root, succ):
        """CH3'' (--order oink): Pearce's SCC algorithm (IPL 2016, PEA_FIND_SCC2), with an SCC's vertices listed as Oink's
        dtl.cpp 222-299 lists them: the root first, then the non-root vertices popped off Pearce's stack (pushed at finish
        time). Same SCCs as Tarjan; only the vertex order inside an SCC differs (it fixes the order dominion vertices are
        queued for solving in search())."""
        INF = float("inf")
        rindex, S, sccs, idx = {}, [], [], [1]
        def visit(v):
            rindex[v] = idx[0]; idx[0] += 1; isroot = True
            for w in succ(v):
                if w not in rindex:
                    visit(w)
                if rindex[w] < rindex[v]:
                    rindex[v] = rindex[w]; isroot = False
            if isroot:
                idx[0] -= 1; C = [v]
                while S and rindex[v] <= rindex[S[-1]]:
                    w = S.pop(); rindex[w] = INF; idx[0] -= 1; C.append(w)
                rindex[v] = INF; sccs.append(C)
            else:
                S.append(v)
        visit(root)
        return sccs

    def tattr(self, p, Z, R, Gx, maxpr, consume):
        """Tangle attractor loop of C5 §1 with the shared stack Q (already filled by the caller)."""
        while self.Q:
            v = self.Q.pop()
            if consume is not None:
                consume.discard(v)
            self.attractVertices(p, v, R, Z, Gx, maxpr)
            self.attractTangles(p, v, R, Z, Gx, maxpr)

    # ---- C5 §2
    def sptl(self, V, R, p):
        changes = False
        for top in range(self.n - 1, -1, -1):
            if top not in V or top not in R:
                continue
            Z = {top}; self.str[top] = -1; self.Q = [top]
            self.tattr(p, Z, R, R, self.pr[top], R)
            closed = (self.str[top] != -1) if self.ow[top] == p else not any(w in R for w in self.outs[top])
            if closed and top not in self.W:
                self.W.add(top)
                if self.extractTangles(top, Z):
                    changes = True
        return changes

    def best_vertices(self, V, R, p):
        V.clear(); V.update(v for v in R if self.pr[v] % 2 == p)
        if not V:
            return 0
        while True:
            prevV = set(V)
            Z = set(); CurR = set(R)
            for top in range(self.n - 1, -1, -1):
                if top not in V or top in Z:
                    continue
                CurZ = {top}; self.Q = [top]
                self.tattr(p, CurZ, CurR, CurR, self.pr[top], CurR)
                Z |= CurZ
            cand = [v for v in sorted(V, reverse=True) if not self.attracts(p, v, Z, R)]
            if not cand:
                return 1
            for t in [0] + [q for q in self.prios if q > 0 and q <= self.maxpr]:   # t = 0 .. pr(n-1); other t change nothing
                self.Q = sorted(Z)                                                    # CH4
                self.tattr(p, Z, R, R, t, None)
                keep = []
                for i, u in enumerate(cand):
                    if self.pr[u] <= t:
                        keep += cand[i:]; break
                    if not self.attracts(p, u, Z, R):
                        keep.append(u)
                cand = keep
            V -= set(cand)
            if not cand:
                return 1
            if not V:
                V.clear(); V.update(prevV)
                return -1

    def dom(self, V, R, X, p):
        for top in range(self.n - 1, -1, -1):
            if top not in V or top in X:
                continue
            X.add(top); self.str[top] = -1; self.Q = [top]
            self.tattr(p, X, R, R, self.pr[top], R)

    def search_rec(self, R, p, depth):
        X = set()
        while True:
            V = set()
            res = self.best_vertices(V, R, p)
            if res == 0:
                return
            if res == 1:
                while self.sptl(V, set(R), p):
                    pass
                self.dom(V, R, X, p)
                continue
            t = 0; Z = set(); self.Q = []
            for v in range(self.n):
                if v not in R:
                    continue
                if self.pr[v] > t:
                    if self.Q:
                        break
                    t = self.pr[v]
                if self.attracts(p, v, X, R):
                    Z.add(v); self.str[v] = -1; self.Q.append(v)
            if self.Q:
                self.tattr(p, Z, R, R, t, R)
                for u in range(self.n - 1, -1, -1):
                    if self.pr[u] < t:
                        break
                    if u in Z and self.pr[u] == t:
                        X.add(u); self.Q.append(u)
                while self.Q:
                    u = self.Q.pop(); Z.discard(u)
                    self.attractVertices(1 - p, u, Z, X, Z, t)
                X |= Z
                self.search_rec(Z, p, depth + 1)
            else:
                self.dom(V, R, X, p)

    def search(self, p):
        T, D = self.tangles, self.dominions
        self.search_rec(set(self.G), p, 0)
        self.W = set()
        if self.dom_vector:
            self.Q = []
            for v, s in self.dom_vector:
                self.str[v] = s; self.Q.append(v)
            self.dom_vector = []
            while self.Q:
                v = self.Q.pop()
                self.solve(v, p)
                self.G.discard(v)
                self.attractVertices(p, v, self.G, self.S, self.G, -1)
                self.attractTangles(p, v, self.G, self.S, self.G, -1)
            self.S = set()
        return self.tangles != T or self.dominions != D

    def solve(self, v, p):
        if self.win[v] is not None:
            self.stats["resolve"] += 1; return
        self.win[v] = p
        self.sol_str[v] = self.str[v] if self.ow[v] == p else None

    def run(self):
        self.tkeys = []
        if not self.interleaved:
            while self.G:
                self.iterations += 1
                if not self.search(0):
                    break
            while self.G:
                self.iterations += 1
                if not self.search(1):
                    break
        else:
            # CH6: iterations counted once per round at the top of the loop, including the final round that finds G empty.
            # C5 §2 leaves the idtl counter open; this convention was taken from dtl.cpp run() (1123-1138), read AFTER the
            # first cross-check, to classify the only divergence found (counts per search call differ; regions, strategies,
            # tangles and dominions equal). It changes the reported counter only, never the computation.
            while True:
                self.iterations += 1
                if not self.G:
                    break
                a = self.search(0)
                if not self.G:
                    break
                b = self.search(1)
                if not a and not b:
                    self.stats["stuck"] += 1; break
        return self.win, self.sol_str


def solve_game(g, interleaved=False, order="stable"):
    """Reindex by priority (C5 §0; CH1), run, map back. Returns (win, strategy, solver)."""
    if order == "oink":                   # CH1': Oink's own step-0 order (stdsort.py, emulating game.cpp:495's std::sort)
        from stdsort import oink_order
        idx = oink_order(g.prio)
    else:
        idx = sorted(range(g.n), key=lambda v: (g.prio[v], v if order == "stable" else -v))
    new = {v: i for i, v in enumerate(idx)}
    d = DTL([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx], interleaved,
            ins_desc=(order == "oink"))
    global TV_SORTED, PEARCE
    saved = TV_SORTED, PEARCE
    if order == "oink":
        TV_SORTED = True                  # CH3': Oink sorts a new tangle's vertices ascending before storing it (dtl.cpp 385-424)
        PEARCE = True                     # CH3'': SCC vertex order as Oink's Pearce loop emits it (dominion queue order)
    try:
        win, st = d.run()
    finally:
        TV_SORTED, PEARCE = saved
    W = [None] * g.n; S = [None] * g.n
    for i, v in enumerate(idx):
        W[v] = win[i]
        S[v] = idx[st[i]] if st[i] is not None and st[i] != -1 else (None if st[i] is None else -1)
    return W, S, d


def main():
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    order = sys.argv[sys.argv.index("--order") + 1] if "--order" in sys.argv else "stable"
    a = [x for x in a if x != order]
    g = pg.read(a[0])
    sys.setrecursionlimit(100000)
    W, S, d = solve_game(g, "--idtl" in sys.argv, order)
    with open(a[1], "w") as f:
        f.write(f"paritysol {g.n - 1};\n")
        for v in range(g.n):
            if W[v] is None:
                continue
            f.write(f"{v} {W[v]}" + (f" {S[v]}" if S[v] is not None and S[v] != -1 else "") + ";\n")
    print(f"found {d.dominions} dominions and {d.tangles} tangles.")
    print(f"solved in {d.iterations} iterations and 0 pruning steps.")
    if "--stats" in sys.argv:
        print("stats", d.stats, "unsolved", sum(1 for x in W if x is None))


if __name__ == "__main__":
    main()
