#!/usr/bin/env python3
"""L-RED successor 30: exact per-state check of Lemma MG (R119 §1) on N5 runs (n5b SPEC).
At state (sigma, tau): T = tau-bar (Even's optimal counter to tau, SPEC S1 on G^d), sbar = Odd's optimal counter to sigma.
For every vertex u, pi = (sigma, sbar)-play from u. Hypotheses: (i) every Even w on pi has sigma(w) = T(w); (ii) every Odd p on pi
with sbar(p) != tau(p) has (p, sbar(p)) not in I_tau; (iii) no such p on pi's cycle, and for each such p the (T, tau)-play from
tau(p) avoids pi's prefix up to p. Claim: Xi_sigma(u) = value of the (T, tau)-play from u. Counts hits / violations, plus the
'reads' (u with Xi_sigma(u) != (sigma, tau)-value: a free-Odd lock) and which hypothesis each such u fails.
Control: u failing only (i) with Xi_sigma(u) != (T, tau)-value (shows (i) is needed and the test can fire).
Also asserts that the play values reproduce n5b's valuations (sanity). Usage: mgcheck.py GAME.pg [START]"""
import sys, os
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.insert(0, R + "/experiments/n5-second"); sys.path.insert(0, R + "/experiments/hard-families"); sys.path.insert(0, R + "/experiments/harness")
import n5b, pg

def playval(g, nxt, u, rank):
    seq = []; pos = {}
    x = u
    while x not in pos:
        pos[x] = len(seq); seq.append(x); x = nxt(x)
    cyc = seq[pos[x]:]; c = max(cyc, key=lambda y: rank[y])
    pre = seq[:seq.index(c)] if c in seq[:pos[x]] else seq[:seq.index(c)]
    P = frozenset(y for y in pre if rank[y] > rank[c])
    return (c, P, len(pre)), seq, cyc

def check(g, sigma0=None, tau0=None, out=None):
    N = n5b.N5(g, mode="spec"); tr = []
    N.run(sigma0, tau0, trace=tr)
    rank = {v: r for r, v in enumerate(sorted(range(g.n), key=lambda v: (g.prio[v], v)))}
    hits = viol = reads = ctrl = 0; fails = {"i": 0, "ii": 0, "iii": 0}
    for (sig, tau) in tr:
        sig = list(sig); tau = list(tau)
        vs, sbar = N.opt(N.SG, sig)
        vt, tbd = N.opt(N.SD, tau)
        It = N.improving(N.SD, tau, vt)
        T = [tbd[v] if g.owner[v] == 0 else -1 for v in range(g.n)]
        fs = lambda x: sig[x] if g.owner[x] == 0 else sbar[x]
        ft = lambda x: T[x] if g.owner[x] == 0 else tau[x]
        fst = lambda x: sig[x] if g.owner[x] == 0 else tau[x]
        for u in range(g.n):
            val, seq, cyc = playval(g, fs, u, rank)
            assert val == vs[u], ("sanity", u, val, vs[u])
            vT, _, _ = playval(g, ft, u, rank)
            vST, _, _ = playval(g, fst, u, rank)
            lock = val != vST
            f = []
            if any(g.owner[w] == 0 and sig[w] != T[w] for w in seq): f.append("i")
            devs = [k for k, p in enumerate(seq) if g.owner[p] == 1 and sbar[p] != tau[p]]
            if any(sbar[seq[k]] in It.get(seq[k], []) for k in devs): f.append("ii")
            bad = False
            for k in devs:
                p = seq[k]
                if p in cyc: bad = True; break
                _, s2, _ = playval(g, ft, tau[p], rank)
                if set(s2) & set(seq[:k + 1]): bad = True; break
            if bad: f.append("iii")
            if lock:
                reads += 1
                for h in f: fails[h] += 1
            if f == ["i"] and val != vT: ctrl += 1
            if not f:
                hits += 1
                if val != vT:
                    viol += 1
                    if out is not None: out.append((sig, tau, u, val, vT))
    return len(tr), hits, viol, reads, fails, ctrl

if __name__ == "__main__":
    g = pg.read(sys.argv[1])
    s0, t0 = n5b.read_start(sys.argv[2], g) if len(sys.argv) > 2 else (None, None)
    o = []
    print(sys.argv[1], "states %d hits %d violations %d locks %d lock-fails %s control(only (i) fails, claim false) %d" % check(g, s0, t0, o))
    for x in o[:3]: print("VIOL", x)
