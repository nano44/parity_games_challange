#!/usr/bin/env python3
"""L-RED 62 R228: INDEPENDENT census for L-NEW 67 BOX 200 (claude/l-new f24113f0) on R221 own.py (IDEAL-CYC Howard, pad-free Γ, the
genome's start, cap 3000). No L-NEW code. In my Γ a mover's successors are its gates (one per option) and a gate's are its two faces.
  selffail (Lemma SELF; unit y-top of (v, I)): with split u and new successor b, NOT (u switches into b at t, Λ_(t-1)(u) = Λ_t(u) = w and
           u's own change has top y)
  tcfail (TIME-CHARGE; unit (v, I, y)): c_y(v, I) > Σ_(u,b) |S_y(u, b, w)|
  leapfail (LEAP; unit couple of consecutive switches t < t' of u into b with Λ(u) = w): not (val_(t'-1)(a) > val_t(b) and, for a mover,
           val_(t'-1)(b) > val_(t'-1)(a)), tested in that form for movers and gates alike
  R      = max over (u, b, w) of #switches of u into b at steps with Λ_(t-1)(u) = Λ_t(u) = w (a PER-TUPLE MAXIMUM; u mover or gate)
  Rmov   = the same over movers only;  reqfail: T > N(2M + 2) + M(2M + 3)·Rmov  (R-EQUIV's bound, with my Γ's M mover edges)
  sumS   = max over (v, I, y) of Σ_(u,b) |S_y(u, b, w)|;  C = max c_y.   returns / ytops are TOTALS.
Controls: CTRL=old (b := u's OLD successor) -> selffail, tcfail fire; CTRL=leap (both LEAP inequalities reversed) -> leapfail fires.
Usage: self228.py G.json ..."""
import sys, os, json, collections
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r221")]
import own
CTRL = os.environ.get("CTRL", "")
def census(G, cap=3000):
    out, V, O, ow = own.run(G, cap); n, prio, o_, succ, _, _ = own.build(G); vj = own.VJ(prio); rk = vj.rk; N = G["N"]; M = len(O)
    evs = {V[("e", q)] for q in O}; gates = {V[("g", q)] for q in O}; T = len(out) - 1
    nx = [[s[u] if u < N else (tau[u] if o_[u] == 1 else succ[u][0]) for u in range(n)] for (s, vals, tau) in out]
    lam = lambda t, v: out[t][1][v][0]
    E = lambda t, v: frozenset(e for e in out[t][1][v][1] if e in evs)
    def play(t, v):
        p = []; seen = set(); u = v
        while u not in seen: seen.add(u); p.append(u); u = nx[t][u]
        return p
    c = collections.Counter(T=T)
    for k in ("selffail", "tcfail", "leapfail", "R", "Rmov", "reqfail", "sumS", "C", "returns", "ytops"): c[k] = 0
    sw = collections.defaultdict(list); S = collections.defaultdict(set)      # (u, b, w) -> steps;  (y, u, b, w) -> steps
    for u in list(range(N)) + sorted(gates):
        for t in range(1, T + 1):
            if nx[t][u] != nx[t - 1][u] and lam(t - 1, u) == lam(t, u):
                w = lam(t, u); b = nx[t][u]; sw[(u, b, w)].append(t)
                A, B = E(t - 1, u), E(t, u)
                if A != B: S[(max(A ^ B, key=lambda e: rk[e]), u, b, w)].add(t)
    for (u, b, w), ts in sw.items():
        c["R"] = max(c["R"], len(ts))
        if u < N: c["Rmov"] = max(c["Rmov"], len(ts))
        for t1, t2 in zip(ts, ts[1:]):
            c["returns"] += 1; a = nx[t2 - 1][u]
            sg = -1 if CTRL == "leap" else 1
            ok = sg * vj.cmp(out[t2 - 1][1][a], out[t1][1][b]) > 0 and sg * vj.cmp(out[t2 - 1][1][b], out[t2 - 1][1][a]) > 0
            if not ok: c["leapfail"] += 1
    if T > N * (2 * M + 2) + M * (2 * M + 3) * c["Rmov"]: c["reqfail"] += 1
    for v in range(n):
        t = 0
        while t <= T:
            u_ = t
            while u_ + 1 <= T and lam(u_ + 1, v) == lam(t, v): u_ += 1
            w = lam(t, v); cnt = collections.Counter(); pairs = collections.defaultdict(set)
            for i in range(t + 1, u_ + 1):
                A, B = E(i - 1, v), E(i, v)
                if A == B: continue
                y = max(A ^ B, key=lambda e: rk[e]); cnt[y] += 1; c["ytops"] += 1
                uu = next(x for x in play(i, v) if nx[i][x] != nx[i - 1][x]); b = nx[i - 1][uu] if CTRL == "old" else nx[i][uu]; pairs[y].add((uu, b))
                if i not in S.get((y, uu, b, w), ()): c["selffail"] += 1
            for y, k in cnt.items():
                s = sum(len(S.get((y, uu, b, w), ())) for uu, b in pairs[y]); c["sumS"] = max(c["sumS"], s); c["C"] = max(c["C"], k)
                if k > s: c["tcfail"] += 1
            t = u_ + 1
    return c
K = ("T", "C", "sumS", "R", "Rmov", "returns", "ytops", "selffail", "tcfail", "leapfail", "reqfail")
if __name__ == "__main__":
    print("instance N+M", " ".join(K))
    for f in sys.argv[1:]:
        G = json.load(open(f)); G = G.get("genome", G); c = census(G)
        print(os.path.basename(f), G["N"] + sum(len(o) for o in G["opts"]), " ".join(str(c[k]) for k in K), flush=True)
