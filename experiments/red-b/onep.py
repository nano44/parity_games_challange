#!/usr/bin/env python3
"""L-RED-B B6 attempt 2: own implementation of the one-player model 1P(G) of box 217 §1 / §6.1 (claude/l-new a143d406,
docs/new/N5-QUIETKEY-box217.md), written from the text of §6.1, not from one217.py.

Genome (R104 JSON format): N, lev[x], opts[x] = [[wt, xt, b], ...], gate[x][k] (the index eps), br[b], bp[b], start[x].
  value   V_s(exit) = (0, 0); Xi_s(x, k) = (omega(b), 1) + V_s(xt); omega(b) = +-2^rank(b), sign + iff priority 6 + 2 br + bp is even,
          rank by (priority, b); pairs compared lexicographically, larger better.
  A_s(x)  = {s(x)} + {k : Xi_s(x, k) > Xi_s(x, s(x))}
  KEY     by increasing level, s'(x) = argmin over A_s(x) of key_s'(x, k) = key_s'(wt(x, k), s'(wt)) ++ (eps(x, k)); (eps) at level 0
  HOWARD  s'(x) = the Xi_s-best option
Run: from start; stop at the first s' = s (also when no option is strictly better anywhere).

Functions: load(fn), OneP(G).run(rule) -> list of states; stats(G, S) -> per-mover switch counts, |K|, enumeration depth k(G).
CLI: onep.py [--trace] G.json ...   prints N, M, T_key, T_howard, k(G) (largest k with a level-(k-1) mover at sw = |K| - 1; 0 if none),
     kh(G) (same with sw >= |K|/2 - 1 and sw >= 1), max sw; --trace prints the movers switching at every step."""
import sys, json


def load(fn):
    G = json.load(open(fn))
    return G.get("genome", G)


class OneP:
    def __init__(self, G):
        self.G = G
        N = self.N = G["N"]
        self.lev = G["lev"]
        self.opts = G["opts"]
        pr = {}
        for x in range(N):
            for (_, _, b) in self.opts[x]:
                pr[b] = 6 + 2 * G["br"][b] + G["bp"][b]
        order = sorted(pr, key=lambda b: (pr[b], b))
        self.rank = {b: r for r, b in enumerate(order)}
        self.om = {b: (1 << self.rank[b]) * (1 if pr[b] % 2 == 0 else -1) for b in pr}
        self.eps = G["gate"]
        # Xi-topological order, targets first (iterative DFS; raises on a cycle)
        state = [0] * N
        topo = []
        for r in range(N):
            if state[r]:
                continue
            stack = [(r, 0)]
            state[r] = 1
            while stack:
                x, i = stack.pop()
                if i < len(self.opts[x]):
                    stack.append((x, i + 1))
                    y = self.opts[x][i][1]
                    if y >= 0:
                        if state[y] == 1:
                            raise ValueError("Xi-graph has a cycle")
                        if state[y] == 0:
                            state[y] = 1
                            stack.append((y, 0))
                else:
                    state[x] = 2
                    topo.append(x)
        self.topo = topo
        self.bylev = sorted(range(N), key=lambda x: (self.lev[x], x))

    def values(self, s):
        mv = [None] * self.N
        ov = [None] * self.N
        for x in self.topo:
            row = []
            for (_, y, b) in self.opts[x]:
                w, h = (0, 0) if y < 0 else mv[y]
                row.append((w + self.om[b], h + 1))
            ov[x] = row
            mv[x] = row[s[x]]
        return mv, ov

    def improving(self, s):
        _, ov = self.values(s)
        return [[k for k in range(len(self.opts[x])) if k == s[x] or ov[x][k] > ov[x][s[x]]] for x in range(self.N)], ov

    def step(self, s, rule="key"):
        A, ov = self.improving(s)
        if rule == "howard":
            return tuple(max(A[x], key=lambda k: ov[x][k]) for x in range(self.N))
        new = list(s)
        key = [None] * self.N
        for x in self.bylev:
            best = None
            for k in A[x]:
                wt = self.opts[x][k][0]
                kk = (key[wt] if self.lev[x] > 0 else ()) + (self.eps[x][k],)
                if best is None or kk < best[0]:
                    best = (kk, k)
            key[x], new[x] = best
        return tuple(new)

    def keys(self, s):
        key = [None] * self.N
        for x in self.bylev:
            wt = self.opts[x][s[x]][0]
            key[x] = (key[wt] if self.lev[x] > 0 else ()) + (self.eps[x][s[x]],)
        return key

    def run(self, rule="key", cap=10 ** 7):
        s = tuple(self.G["start"])
        S = [s]
        while len(S) <= cap:
            t = self.step(s, rule)
            if t == s:
                break
            s = t
            S.append(s)
        return S

    def nkeys(self):
        """|K(x)|: number of root-first W-paths from x to level 0 (one option per level)"""
        nk = [0] * self.N
        for x in self.bylev:
            nk[x] = len(self.opts[x]) if self.lev[x] == 0 else sum(nk[o[0]] for o in self.opts[x])
        return nk


def stats(G, S=None):
    P = OneP(G)
    if S is None:
        S = P.run("key")
    N = P.N
    sw = [0] * N
    for a, b in zip(S, S[1:]):
        for x in range(N):
            if a[x] != b[x]:
                sw[x] += 1
    nk = P.nkeys()
    k = 0
    kh = 0
    for x in range(N):
        if sw[x] >= 1 and sw[x] == nk[x] - 1:
            k = max(k, P.lev[x] + 1)
        if sw[x] >= 1 and 2 * (sw[x] + 1) >= nk[x]:
            kh = max(kh, P.lev[x] + 1)
    return {"T": len(S) - 1, "sw": sw, "nk": nk, "k": k, "kh": kh, "P": P}


if __name__ == "__main__":
    a = sys.argv[1:]
    trace = "--trace" in a
    a = [x for x in a if x != "--trace"]
    for fn in a:
        G = load(fn)
        P = OneP(G)
        S = P.run("key")
        H = P.run("howard")
        st = stats(G, S)
        M = sum(len(o) for o in G["opts"])
        print(f"{fn.split('/')[-1]} N {G['N']} M {M} key {len(S) - 1} howard {len(H) - 1} k {st['k']} khalf {st['kh']} maxsw {max(st['sw'])}", flush=True)
        if trace:
            for t, (p, q) in enumerate(zip(S, S[1:]), 1):
                print(t, [x for x in range(G["N"]) if p[x] != q[x]])
