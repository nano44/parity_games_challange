#!/usr/bin/env python3
"""L-SI box 81 XCHECK: an INDEPENDENT implementation of IDEAL-CYC(G) Howard (no code shared with ref/ or experiments/si/si.py).
- Gamma(G) built from RESULTS R104's text (vertex order: movers, gates by gate index, beta by option (x, k), e by gate index, unused
  loop cX (2), c_W, K0..K3; beta priority 6 + 2 br + bp; e priorities even, above every beta, ordered by (level, gate index); c_W = least
  even >= 2 above all; K0 top+2, K1 5, K2 (Odd) 3, K3 top+3). Frozen (IDEAL-CYC, R118 (a)): beta -> Xi-target (u = K0 if X), K0 -> K3,
  K1 -> K1, K3 -> K2, e -> its one successor; movers free (Howard), Odd free.
- Relevance: rank by (priority, index). Value (cycle node L, set P of path vertices more relevant than L, length k); order: reward of L
  (even: higher better; odd: higher worse), then P by its most relevant element of the symmetric difference (even: in the larger set),
  then k (longer better iff L odd).
- Odd's optimal counterstrategy: Odd switch-all policy iteration against fixed sigma (switch to a successor of strictly smaller value),
  plays evaluated explicitly on the functional graph; final Odd choice = smallest-value successor, ties to the current, then smaller index.
- Howard at movers: successor of largest value; ties keep current, then larger index (R118 / idealcyc tie rule).
Compares, per instance, with the reference (census81 / idealcyc): the game (prio, owner, succ), the whole state sequence, every value at
every state, and the ascent histogram (box 193 definition) computed from MY plays. R (labels C/R/p) is printed from my sigma-bar choice;
R depends on the deterministic choice (R118: «any fixed deterministic choice»), so R is compared and a difference is reported, not failed.
Usage: xchk81.py FILES.json"""
import sys, os, json
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))


def build(G):
    N, lev, opts, gate, br, bp = G["N"], G["lev"], G["opts"], G["gate"], G["br"], G["bp"]
    O = [(x, k) for x in range(N) for k in range(len(opts[x]))]
    byg = sorted(O, key=lambda q: gate[q[0]][q[1]])
    idx = {}; n = 0
    for x in range(N): idx["x", x] = n; n += 1
    for q in byg: idx["g", q] = n; n += 1
    for q in O: idx["b", q] = n; n += 1
    for q in byg: idx["e", q] = n; n += 1
    cX, cW, K0, K1, K2, K3 = n, n + 1, n + 2, n + 3, n + 4, n + 5; n += 6
    pr = [0] * n; ow = [0] * n; sc = [[] for _ in range(n)]
    for x in range(N): sc[x] = [idx["g", (x, k)] for k in range(len(opts[x]))]
    bpr = {q: 6 + 2 * br[opts[q[0]][q[1]][2]] + bp[opts[q[0]][q[1]][2]] for q in O}
    top_b = max(bpr.values()); e0 = top_b + 1 if (top_b + 1) % 2 == 0 else top_b + 2
    for i, q in enumerate(sorted(O, key=lambda q: (lev[q[0]], gate[q[0]][q[1]]))): pr[idx["e", q]] = e0 + 2 * i
    for q in O:
        x, k = q; wt, xt, _ = opts[x][k]; g, b, e = idx["g", q], idx["b", q], idx["e", q]
        pr[g] = 1; ow[g] = 1; sc[g] = [e, b]
        pr[b] = bpr[q]; sc[b] = [xt, K0] if xt >= 0 else [K0]
        sc[e] = [wt if wt >= 0 else cW]
    pr[cX] = 2; sc[cX] = [cX]
    top = max(pr) + 2; top += top % 2
    pr[cW] = top; sc[cW] = [cW]
    pr[K0], pr[K1], pr[K2], pr[K3] = top + 2, 5, 3, top + 3; ow[K2] = 1
    sc[K0] = [K1, K3]; sc[K1] = [K0, K1]; sc[K2] = [K1, K2]; sc[K3] = [K1, K2]
    froz = {}
    for q in O:
        xt = opts[q[0]][q[1]][1]; froz[idx["b", q]] = xt if xt >= 0 else K0
    froz[K0] = K3; froz[K1] = K1; froz[K3] = K2
    return pr, ow, sc, froz, idx, N


class Val:
    def __init__(s, pr, ow, sc):
        n = s.n = len(pr); s.pr, s.ow, s.sc = pr, ow, sc
        order = sorted(range(n), key=lambda v: (pr[v], v)); s.rk = [0] * n
        for r, v in enumerate(order): s.rk[v] = r
        s.ev = [pr[v] % 2 == 0 for v in range(n)]
    def reward(s, v): return s.rk[v] if s.ev[v] else -s.rk[v]
    def setcmp(s, A, B):            # +1 if A better for Even than B, -1 worse, 0 equal (A, B: bitmasks over ranks)
        d = A ^ B
        if not d: return 0
        r = d.bit_length() - 1; inA = (A >> r) & 1
        evr = s.evrank[r]
        return (1 if inA else -1) * (1 if evr else -1)
    def cmp(s, a, b):
        if a[0] != b[0]: return 1 if s.reward(a[0]) > s.reward(b[0]) else -1
        c = s.setcmp(a[1], b[1])
        if c: return c
        if a[2] == b[2]: return 0
        longer_better = not s.ev[a[0]]
        return (1 if a[2] > b[2] else -1) * (1 if longer_better else -1)
    def plays(s, nxt):
        n = s.n; val = [None] * n; state = [0] * n
        for v0 in range(n):
            if state[v0]: continue
            path = []; v = v0
            while state[v] == 0: state[v] = 1; path.append(v); v = nxt[v]
            if state[v] == 1:                       # new cycle, starting at v
                i = path.index(v); cyc = path[i:]; L = max(cyc, key=lambda u: s.rk[u])
                j = cyc.index(L); m = len(cyc)
                for t in range(m):
                    u = cyc[(j - t) % m]; val[u] = (L, 0, t)     # u is t steps before L on the cycle; no vertex above L
                for u in cyc: state[u] = 2
                path = path[:i]
            for u in reversed(path):
                w = val[nxt[u]]; L = w[0]
                val[u] = (L, w[1] | ((1 << s.rk[u]) if s.rk[u] > s.rk[L] else 0), w[2] + 1); state[u] = 2
        return val
    def evaluate(s, sig, tau0=None):
        n = s.n; tau = list(tau0) if tau0 else [s.sc[v][0] if s.ow[v] == 1 else None for v in range(n)]
        while True:
            nxt = [sig[v] if s.ow[v] == 0 else tau[v] for v in range(n)]; val = s.plays(nxt); ch = False
            for v in range(n):
                if s.ow[v] != 1: continue
                best = tau[v]
                for w in s.sc[v]:
                    if s.cmp(val[w], val[best]) < 0: best = w
                if best != tau[v]: tau[v] = best; ch = True
            if not ch: break
        fin = list(tau)               # deterministic final choice: min value, ties current then smaller index
        for v in range(n):
            if s.ow[v] != 1: continue
            best = tau[v]
            for w in sorted(s.sc[v]):
                if s.cmp(val[w], val[best]) < 0: best = w
            fin[v] = best
        return val, fin


def run(G, cap=10 ** 5):
    pr, ow, sc, froz, idx, N = build(G); V = Val(pr, ow, sc)
    V.evrank = [0] * V.n
    for v in range(V.n): V.evrank[V.rk[v]] = V.ev[v]
    inv = {}
    for x in range(N):
        for k in range(len(G["opts"][x])): inv[idx["g", (x, k)]] = k
    sig = [None] * V.n
    for v in range(V.n):
        if ow[v] == 0: sig[v] = froz.get(v, sc[v][0])
    for x in range(N): sig[x] = idx["g", (x, G["start"][x])]
    states = []; tau = None
    while len(states) <= cap:
        val, tau = V.evaluate(sig, tau)
        states.append((tuple(inv[sig[x]] for x in range(N)), val, list(tau), list(sig)))
        ns = list(sig)
        for x in range(N):
            b = sig[x]
            for w in sc[x]:
                c = V.cmp(val[w], val[b])
                if c > 0 or (c == 0 and w != sig[x] and b != sig[x] and w > b): b = w
            ns[x] = b
        if ns == sig: break
        sig = ns
    return (pr, ow, sc), V, idx, states


def ascents(G, V, idx, states):
    name = {v: k for k, v in idx.items()}; evs = {v for v in range(V.n) if name.get(v, ("?",))[0] == "e"}
    hist = Counter(); lab = []; prev = None
    for sig_s, val, tau, sig in states:
        nxt = [sig[v] if V.ow[v] == 0 else tau[v] for v in range(V.n)]
        lam = [val[v][0] for v in range(V.n)]; sb = [tau[v] for v in range(V.n) if V.ow[v] == 1]
        if prev is not None: lab.append("C" if lam != prev[0] else ("R" if sb != prev[1] else "p"))
        prev = (lam, sb)
        for v in range(V.n):
            path = []; seen = set(); u = v
            while u not in seen: seen.add(u); path.append(u); u = nxt[u]
            seq = [y for y in path if y in evs and (val[v][1] >> V.rk[y]) & 1]
            hist[sum(1 for a, b in zip(seq, seq[1:]) if V.rk[b] > V.rk[a])] += 1
    return hist, "".join(lab)


if __name__ == "__main__":
    sys.path[:0] = [HERE, os.path.join(HERE, "ref", "experiments", "new", "box191"), os.path.join(HERE, "ref", "experiments", "new", "box189")]
    import idealcyc, census81
    for f in sys.argv[1:]:
        G = json.load(open(f)); game, V, idx, states = run(G)
        h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); rst = idealcyc.run(G)
        hg = (list(h.prio), list(h.owner)) == (game[0], game[1]) and all(sorted(a) == sorted(b) for a, b in zip(h.succ_full if hasattr(h, "succ_full") else [], []))
        import gamma3
        g0, _, _, _ = gamma3.build(G, set())
        same_game = (list(g0.prio), list(g0.owner)) == (game[0], game[1]) and all(sorted(a) == sorted(b) for a, b in zip(g0.succ, game[2]))
        same_states = [s[0] for s in states] == [tuple(s) for s in rst]
        gi = {}
        for x in range(G["N"]):
            for v in h.succ[movers[x]]: gi[(x, inv[v])] = v
        vbad = 0
        for (st, val, _, _), rs in zip(states, rst):
            cur = list(s0)
            for x in range(G["N"]): cur[movers[x]] = gi[(x, rs[x])]
            rv, _ = E.evaluate(tuple(cur))
            vbad += sum(1 for v in range(V.n) if (rv[v][0], rv[v][1], rv[v][2]) != val[v])
        hist, lab = ascents(G, V, idx, states)
        ref, _, _ = census81.census(G)
        print(os.path.basename(f), "game", "SAME" if same_game else "DIFF", "states", "SAME" if same_states else "DIFF",
              "T", len(states) - 1, "/", len(rst) - 1, "valuediffs", vbad,
              "hist", "SAME" if dict(hist) == ref["hist"] else f"DIFF {dict(sorted(hist.items()))} vs {ref['hist']}",
              "R", lab.count("R"), "/", ref["R"], "labels", "SAME" if lab == ref["labels"] else f"DIFF {lab} vs {ref['labels']}")
