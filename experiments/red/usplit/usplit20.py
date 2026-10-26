#!/usr/bin/env python3
"""Box 47 (L-RED successor 20): own exact checker of CONJECTURE U-SPLIT (docs/si/N5-RUND-box17.md §17, l-si 5402151c / 873c8e71),
written from §14 / §16 / §17's text, not from L-SI's sched.py. Trace = o1_19.trace (own SPEC S1-S5 loop).
  RUN S: maximal run of consecutive states inside one phase ((λ_Ξ, τ) constant), every transition S4a (no fallback), λ_W constant.
  FORBIDDEN at k (L = −1): Even x, z ∈ succ(x), z ≠ σ_k(x), COARSE W_k(z) ≻ COARSE W_k(σ_k x) (COARSE = (reward of the cycle node, path
    weight), lengths dropped), and NOT Ξ_k(z) ▷ Ξ_k(σ_k x) (S1's full order).
  U EVENT (k, (y, z)): an S4a transition k -> k+1 of S with σ_k(y) ≠ z = σ_{k+1}(y), and (y, z) forbidden at some f ∈ [k − n + 1, k − 1] ∩ S.
  (h3_D) at k: λ_Ξ(u) = λ_W(u) for every u ∈ D_k (D_k = Odd u with σ̄_k(u) ≠ τ(u)).  Offset Δ_k(v) := w(P^W_k(v)) − w(P^Ξ_k(v)) (one cycle node).
  UP: Δ_{k+1}(y) > Δ_k(y).  BD: D, or some gate's (Ξ, W) value (u ∈ D), differs at two states of [f, k + 1].
  U-SPLIT: under (h3_D) on S, every U event has UP or BD for EVERY forbidden f in the window (a kill needs one f with neither; the
  latest f is the hardest for BD, so it is the one tested).
Usage: usplit20.py game.pg start.json [--oink]"""
import sys, os, json, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "o1")); sys.path.insert(0, os.path.join(HERE, "..", "rec0"))
import o1_19 as O, pg, verify, rec0_20 as R0

def analyse(g, start=None, use_oink=False):
    n = g.n; S, FB, E = O.trace(g, start)
    ev = [E.evaluate(s) for s, _ in S]; Xi = [X for X, _ in ev]; SB = [B for _, B in ev]
    W = [[R0.playval(g, E, s, t, x) for x in range(n)] for s, t in S]
    lam = [tuple(x[0] for x in X) for X in Xi]; lamW = [tuple(x[0] for x in w) for w in W]
    co = lambda v: (E.rew[v[0]], E.weight(v[1])); K = E.key
    D = [frozenset(u for u in range(n) if g.owner[u] == 1 and SB[k][u] != S[k][1][u]) for k in range(len(S))]
    off = lambda k, v: E.weight(W[k][v][1]) - E.weight(Xi[k][v][1])
    def forb(k, x, z):
        a = S[k][0][x]
        return z != a and co(W[k][z]) > co(W[k][a]) and not K(Xi[k][z]) > K(Xi[k][a])
    r = dict(n=n, ITER=len(FB), runs=0, U=0, U_h3=0, UP=0, BD=0, neither=0, events=[], fails=[])
    N = len(S); i = 0
    while i < N:
        j = i
        while j + 1 < N and lam[j + 1] == lam[i] and S[j + 1][1] == S[i][1] and FB[j] == 0 and lamW[j + 1] == lamW[i]: j += 1
        r["runs"] += 1
        h3 = all(lam[k][u] == lamW[k][u] for k in range(i, j + 1) for u in D[k])
        for k in range(i, j):
            for y in range(n):
                if g.owner[y] != 0 or S[k][0][y] == S[k + 1][0][y]: continue
                z = S[k + 1][0][y]
                fs = [f for f in range(max(i, k - n + 1), k) if forb(f, y, z)]
                if not fs: continue
                r["U"] += 1
                if not h3: continue
                r["U_h3"] += 1; f = max(fs)
                up = off(k + 1, y) > off(k, y)
                gates = lambda q: (D[q], tuple((u, K(Xi[q][u]), K(W[q][u])) for u in sorted(D[q])))
                bd = len({gates(q) for q in range(f, k + 2)}) > 1
                r["UP"] += up; r["BD"] += bd
                if not up and not bd:
                    r["neither"] += 1
                    r["events"].append(dict(run=[i, j], k=k, f=f, y=y, z=z, a=S[k][0][y], off_y=[off(k, y), off(k + 1, y)], D=sorted(D[k])))
                    r["fails"].append(f"USPLIT k={k} f={f} y={y} z={z}")
        i = j + 1
    win, ws = E.regions(S[-1][0])
    e = verify.check(g, win, ws)
    if e: r["fails"].append("OUT_STRAT " + e[0])
    if use_oink:
        oc = O.oink_check(g, win, ws, tempfile.mkdtemp())
        r["oink"] = oc
        if oc != "OK": r["fails"].append("OUT_OINK " + oc)
    return r

if __name__ == "__main__":
    a = sys.argv
    g = pg.parse("".join(l for l in open(a[1]) if not l.lstrip().startswith("%")))
    st = json.load(open(a[2]))["start"] if len(a) > 2 and a[2].endswith(".json") else None
    print(json.dumps(analyse(g, st, "--oink" in a)))
