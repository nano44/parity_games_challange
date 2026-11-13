#!/usr/bin/env python3
"""Box 108 (L-SI 56): own IDEAL simulator, written from RESULTS R104's definition only.
State s: one option per mover.  Xi-value of option (x, o) under s: the SET of beta's on the chain (x, o), (xt, s(xt)), ... up to the
exit; compared by the beta of largest rank in the symmetric difference (better if that beta's parity is even, worse if odd).
IDEAL step: every mover moves to the lexicographically least key (gate indices of the chain of W-targets under the NEW state, lowest
level first) among its current option and the options with a strictly better Xi-value under the OLD state.  Stop when nothing is
available or nothing changes.  L(G) = number of steps."""
import sys, json

class Ideal:
    def __init__(self, G):
        self.G = G; self.N = G["N"]; self.lev = G["lev"]; self.opts = G["opts"]; self.gate = G["gate"]
        self.rank = {}; self.par = {}
        for x in range(self.N):
            for (_, _, b) in self.opts[x]:
                self.rank[b] = 6 + 2 * G["br"][b] + G["bp"][b]; self.par[b] = G["bp"][b] % 2
        assert len(set(self.rank.values())) == len(self.rank)
        self.bylev = sorted(range(self.N), key=lambda x: self.lev[x])
    def chain(self, s, x, o):
        """the beta set of option (x, o) under s"""
        B = []
        while True:
            _, y, b = self.opts[x][o]; B.append(b)
            if y < 0: return frozenset(B)
            x, o = y, s[y]
    def better(self, A, B):
        """A strictly better than B"""
        D = A ^ B
        if not D: return False
        b = max(D, key=lambda c: self.rank[c])
        return (b in A) == (self.par[b] == 0)
    def avail(self, s):
        out = []
        for x in range(self.N):
            cur = self.chain(s, x, s[x])
            out.append([o for o in range(len(self.opts[x])) if o == s[x] or self.better(self.chain(s, x, o), cur)])
        return out
    def step(self, s):
        """returns (new state, availability sets) or (None, A) at the stop"""
        A = self.avail(s)
        if all(len(a) == 1 for a in A): return None, A
        new = list(s); key = {}
        for x in self.bylev:
            def kk(o):
                w = self.opts[x][o][0]
                return (key[w] if w >= 0 else ()) + (self.gate[x][o],)
            new[x] = min(A[x], key=kk); key[x] = kk(new[x])
        new = tuple(new)
        return (None, A) if new == tuple(s) else (new, A)
    def run(self, cap=10 ** 7):
        s = tuple(self.G["start"]); S = [s]
        while len(S) <= cap:
            t, _ = self.step(s)
            if t is None: break
            s = t; S.append(s)
        return S

if __name__ == "__main__":
    for fn in sys.argv[1:]:
        G = json.load(open(fn)); S = Ideal(G).run(); print(fn, "N", G["N"], "L", len(S) - 1)
