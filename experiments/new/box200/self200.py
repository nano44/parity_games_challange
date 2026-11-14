#!/usr/bin/env python3
"""Box 200 (L-NEW successor 67): the TIME charge of a y-top at v to a Howard step of its split vertex u (Lemma SELF).
Engine: box 196-199's (gamma3.build with pads, n5v.step mode xi from S3, up to the first fallback), as split199.py.
For a change t-1 -> t of E(v) inside a Lambda-interval I of v (node w) with top y entering, u is the split (first departure of the plays)
and b := nx_t(u) its new successor. Lemma SELF: the same step is a change of E(u) with the same symmetric difference and Lambda(u) = w
at t-1, t (TRANSFER), and u itself switches at t (its own split is u, with the same b). So the y-top of v is a y-top of u AT A STEP WHERE
u SWITCHES INTO b. S_y(u, b, w) := #{t : nx_(t-1)(u) != nx_t(u) = b, Lambda_(t-1)(u) = Lambda_t(u) = w, top of E(u)'s change = y entering}.
Counters (must be 0):
  selffail : a y-top of v (split u, new b) that is not counted in S_y(u, b, w)                       [Lemma SELF]
  tcfail   : (v, I, y) with c_y(v, I) > sum over its split pairs (u, b) of S_y(u, b, w)               [Corollary TIME-CHARGE]
  swfail   : (u, b, w) with sum_y S_y(u, b, w) > #switches of u into b while Lambda(u) = w           [distinct Howard steps]
  leapfail : consecutive switches of u into b at t < t' (Lambda(u) = w fixed), a := nx_(t'-1)(u), with not
             (Om_(t'-1)(a) > Om_t(b) and Om_(t'-1)(b) > Om_(t'-1)(a))                                  [Lemma LEAP]
Descriptive (maxima over the genome): maxc (C), maxS (max S_y(u, b, w)), maxsumS (max over (v, I, y) of sum_(u,b) S_y), maxsw (max #switches
of one u into one b in one Lambda-interval), maxsumD (max over (v, I, y) of sum_(u,b) Dhi_y(b, J_b), L-RED's sumD), maxDhib (L-RED's Dhib),
maxused (max over (v, I, y, (u, b)) of #y-tops of v through (u, b): the Lead's «used» changes + 1).
Controls (S200_CTRL): 1 S counted only when u = v (no TRANSFER): selffail, tcfail fire; 2 b taken as the OLD successor: selffail fires;
3 swfail with #switches := 0: swfail fires;
4 LEAP direction reversed (a better than b at t'-1): leapfail fires.
Usage: self200.py G.json ...  (ROOT: repo root, default from this file's place)."""
import sys, os, collections
ROOT = os.environ.get("ROOT") or os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
os.environ.setdefault("EG195_ROOT", ROOT)
sys.path[:0] = [os.path.join(ROOT, p) for p in ("experiments/new/box195", "experiments/new/box191", "experiments/new/box189",
                "experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
import json, eg195, gamma3, n5v, n5x
CTRL = os.environ.get("S200_CTRL", "0")

def run(G, cap=20000):
    g0, _, _, V = gamma3.build(G, eg195.PADS); g = eg195.topg(g0); n = g.n; name = {v: k for k, v in V.items()}
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None)
    evs = [v for v in range(n) if isinstance(name[v], tuple) and name[v][0] == "e"]; ES = sum(E.bit[v] for v in evs)
    H = []
    while len(H) <= cap:
        vs, tb = E.evaluate(tuple(sigma)); H.append((tuple(sigma), vs, tb))
        res = n5v.step(g, E, Ed, sigma, tau, "xi")
        if res is None or res[4]: break
        sigma, tau = res[0], res[1]
    T = len(H)
    def nx(t, x): s, _, tb = H[t]; return s[x] if g.owner[x] == 0 else tb[x]
    def play(t, v):
        P = [v]; seen = {v}
        while True:
            y = nx(t, P[-1])
            if y in seen: return P
            P.append(y); seen.add(y)
    def top(a, b): return max((f for f in evs if (a ^ b) & E.bit[f]), key=lambda f: E.rank[f])
    hi = {y: sum(E.bit[f] for f in evs if E.rank[f] > E.rank[y]) for y in evs}
    Lam = lambda t, x: H[t][1][x][0]
    Es = lambda t, x: H[t][1][x][1] & ES
    # S_y(u, b, w) and switch counts, at every vertex with >= 2 successors (movers, gates)
    S = collections.Counter(); SW = collections.Counter()
    for t in range(1, T):
        for u in range(n):
            if len(g.succ[u]) < 2: continue
            o, b = nx(t - 1, u), nx(t, u)
            if o == b or Lam(t - 1, u) != Lam(t, u): continue
            w = Lam(t, u); SW[(u, b, w)] += 1
            a0, a1 = Es(t - 1, u), Es(t, u)
            if a0 != a1:
                y = top(a0, a1)
                if a1 & E.bit[y]: S[(y, u, b, w)] += 1
    c = collections.Counter()
    K = lambda t, x: E.key(H[t][1][x])
    # LEAP: consecutive switches of u into b at t < t' (Lambda(u) = w at both), a := nx_(t'-1)(u)
    sws = collections.defaultdict(list)
    for t in range(1, T):
        for u in range(n):
            if len(g.succ[u]) >= 2 and nx(t - 1, u) != nx(t, u) and Lam(t - 1, u) == Lam(t, u):
                sws[(u, nx(t, u), Lam(t, u))].append(t)
    for (u, b, w), ts in sws.items():
        for t, t2 in zip(ts, ts[1:]):
            a = nx(t2 - 1, u); c["returns"] += 1
            ok = K(t2 - 1, a) > K(t, b) and K(t2 - 1, b) > K(t2 - 1, a)
            if CTRL == "4": ok = K(t2 - 1, a) > K(t2 - 1, b)
            if not ok: c["leapfail"] += 1
    for (y, u, b, w), k in S.items(): c["maxS"] = max(c["maxS"], k)
    for k in SW.values(): c["maxsw"] = max(c["maxsw"], k)
    tot = collections.Counter()
    for (y, u, b, w), k in S.items(): tot[(u, b, w)] += k
    for key, k in tot.items():
        if k > (SW[key] if CTRL != "3" else 0): c["swfail"] += 1
    # Lambda-intervals of b (for Dhi_y(b, J_b))
    def interval(x, t):
        s = t
        while s > 0 and Lam(s - 1, x) == Lam(t, x): s -= 1
        e = t
        while e + 1 < T and Lam(e + 1, x) == Lam(t, x): e += 1
        return s, e
    for v in range(n):
        t = 0
        while t < T:
            s = t
            while t + 1 < T and Lam(t + 1, v) == Lam(s, v): t += 1
            w = Lam(s, v); ytops = collections.defaultdict(list)
            for q in range(s + 1, t + 1):
                a, b_ = Es(q - 1, v), Es(q, v)
                if a == b_: continue
                y = top(a, b_)
                if not b_ & E.bit[y]: continue
                P0, P1 = play(q - 1, v), play(q, v); i = 0
                while i + 1 < min(len(P0), len(P1)) and P0[i + 1] == P1[i + 1]: i += 1
                u = P1[i]; bb = P1[i + 1] if CTRL != "2" else P0[i + 1]
                c["ytops"] += 1; ytops[y].append((q, u, bb))
                if CTRL == "1" and u != v: c["selffail"] += 1; continue
                # SELF: u switches into bb at q, Lambda(u) = w at q-1, q, u's change has top y entering
                ok = nx(q - 1, u) != nx(q, u) == bb and Lam(q - 1, u) == w == Lam(q, u)
                if ok:
                    a0, a1 = Es(q - 1, u), Es(q, u); ok = a0 != a1 and top(a0, a1) == y and bool(a1 & E.bit[y])
                if not ok: c["selffail"] += 1
            for y, L in ytops.items():
                c["maxc"] = max(c["maxc"], len(L)); pairs = collections.Counter((u, bb) for _, u, bb in L)
                for k in pairs.values(): c["maxused"] = max(c["maxused"], k)
                sumS = sum(S[(y, u, bb, w)] for (u, bb) in pairs) if CTRL != "1" else sum(S[(y, u, bb, w)] for (u, bb) in pairs if u == v)
                c["maxsumS"] = max(c["maxsumS"], sumS)
                if len(L) > sumS: c["tcfail"] += 1
                sumD = 0
                for (u, bb) in pairs:
                    q0 = next(q for q, uu, b2 in L if (uu, b2) == (u, bb)); j0, j1 = interval(bb, q0)
                    d = len({Es(q, bb) & hi[y] for q in range(j0, j1 + 1)}); sumD += d; c["maxDhib"] = max(c["maxDhib"], d)
                c["maxsumD"] = max(c["maxsumD"], sumD)
            t += 1
    c["T3"] = T - 1
    return c

if __name__ == "__main__":
    must = ("selffail", "tcfail", "swfail", "leapfail")
    for f in sys.argv[1:]:
        G = json.load(open(f)); c = run(G)
        print(os.path.basename(f), "T3", c["T3"], " ".join(f"{k} {c[k]}" for k in must), "|",
              " ".join(f"{k} {c[k]}" for k in ("ytops", "returns", "maxc", "maxused", "maxS", "maxsumS", "maxsw", "maxDhib", "maxsumD")), flush=True)
