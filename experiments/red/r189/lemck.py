#!/usr/bin/env python3
"""L-RED R189 LEMCK: lemma-by-lemma check of Theorem REALIZE (docs/red/P-N5-REALIZE.md) at EVERY state of the real N5 run
(SPEC S1-S5 via n5x.step, the box-21 engine) on the STAB+K+ESC game of an IDEAL genome (r187/stab.py, pad 0):
  L-SBAR  Odd's optimal counterstrategy sigma-bar_j = beta-face at every gate, K2 -> K1            (Lemma SBAR)
  L-TAU   I_tau = empty (so S4b keeps tau)                                                          (Lemma TAU)
  L-ESC   (K0, K1) in I_sigma; sigma_(j+1) = sigma_j at every beta-vertex and on K                   (Lemmas ESC, K)
  L-W     W_j = W_0 at every vertex (valuation of the (sigma_j, tau_j) play)                         (Lemma W)
  L-AV    I_sigma at every mover = IDEAL availability A_j (ideal.py rule, fastcyc values)            (Lemma KEY, availability)
  L-KEY   sigma_(j+1)(x) = the least available gate of x in the ROOT-FIRST key read off the real game  (Lemma KEY, [RULE])
          (play path from c_W to the gate under (sigma_(j+1), tau), c_W excluded, indices compared lexicographically)
  L-FB    transitions 1..L are not fallbacks and change sigma; transition L+1 (IDEAL stop) is a fallback
Independent of r187/ideal.py for L-KEY (keys are read off the real game). Usage: lemck.py genome.json ... | --rand N d seed"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(H, "..")
sys.path[:0] = [os.path.join(R, "r187"), os.path.join(R, "r178"), os.path.join(R, "r170"), os.path.join(R, "..", "new", "box21")]
from n5x import Engine, dual, step
import pg, stab, ideal, fastcyc, downgen

def acyclic(G):
    N = G["N"]; adj = [{xt for (_, xt, _) in G["opts"][v] if xt >= 0} for v in range(N)]; col = [0] * N
    def dfs(v):
        col[v] = 1
        for w in adj[v]:
            if col[w] == 1 or (col[w] == 0 and not dfs(w)): return False
        col[v] = 2; return True
    return all(col[v] or dfs(v) for v in range(N))

def check(G):
    assert acyclic(G), "Xi-graph not acyclic: Theorem REALIZE does not apply"
    g, sig, tau, gv, ev, bv = stab.build(G, 0, kgad=True, esc=True)
    n = g.n; N = G["N"]; K = list(range(n - 4, n)); cW = n - 5
    s = [sig.get(v, -1) for v in range(n)]; t = [tau.get(v, -1) for v in range(n)]
    E, Ed = Engine(g), Engine(dual(g))
    WE = lambda tt: Engine(pg.Game(list(g.prio), list(g.owner), [list(g.succ[v]) if g.owner[v] == 0 else [tt[v]] for v in range(n)]))
    inv = {gv[q]: q for q in gv}; gates = sorted(gv.values()); betas = sorted(bv.values())
    S, why = ideal.traj(G); L = len(S) - 1
    W0 = None; bad = {k: 0 for k in ("SBAR", "TAU", "ESC", "W", "AV", "KEY", "FB")}
    for j in range(L + 1):
        if tuple(next(k for k in range(len(G["opts"][v])) if s[v] == gv[(v, k)]) for v in range(N)) != S[j]: bad["KEY"] += 1
        vs, sbar = E.evaluate(tuple(s))
        if any(sbar[x] != bv[inv[x]] for x in gates) or sbar[K[2]] != K[1]: bad["SBAR"] += 1
        W = WE(t).evaluate(tuple(s[v] if g.owner[v] == 0 else -1 for v in range(n)))[0]
        if W0 is None: W0 = W
        if W != W0: bad["W"] += 1
        r = step(g, E, Ed, list(s), list(t))
        ns, nt, Is, It, fb = r[0], r[1], r[2], r[3], r[4]
        if It: bad["TAU"] += 1
        if (K[0], K[1]) not in Is or (j < L and any(ns[v] != s[v] for v in betas + K if g.owner[v] == 0)): bad["ESC"] += 1
        # availability at movers vs IDEAL
        val, idx, _, _ = fastcyc.values(G, [S[j][v] for v in range(N)])
        for v in range(N):
            real = {w for x, w in Is if x == v} | {s[v]}
            cur = val(N + idx[(v, S[j][v])])
            ide = {gv[(v, k)] for k in range(len(G["opts"][v])) if k == S[j][v] or val(N + idx[(v, k)]) > cur}
            if real != ide: bad["AV"] += 1; break
        if j < L:
            if fb or ns == s or nt != t: bad["FB"] += 1
            # L-KEY: root-first key read off the real game under (ns, t)
            def path_to_cW(y):
                p = [y]; z = y
                while z != cW:
                    z = t[z] if g.owner[z] == 1 else ns[z]; p.append(z)
                    if len(p) > n: return None
                return tuple(reversed(p[:-1]))
            for v in range(N):
                av = {w for x, w in Is if x == v} | {s[v]}
                keys = {y: path_to_cW(y) for y in av}
                if None in keys.values() or min(av, key=lambda y: keys[y]) != ns[v]: bad["KEY"] += 1; break
        else:
            if not fb: bad["FB"] += 1
        s, t = ns, nt
    return L, why, bad

if __name__ == "__main__":
    if sys.argv[1] == "--rand":
        cnt, d, seed = map(int, sys.argv[2:5]); rng = random.Random(seed); tot = {}; Ls = []
        for _ in range(cnt):
            G = downgen.randacyc(d, 2, rng); L, why, bad = check(G); Ls.append(L)
            for k, x in bad.items(): tot[k] = tot.get(k, 0) + x
        print(f"LEMCK random ACYC d {d} games {cnt} L {min(Ls)}-{max(Ls)} sum {sum(Ls)} viol " + " ".join(f"{k} {x}" for k, x in tot.items()))
    elif sys.argv[1] == "--perturb":
        # champions (files after the count) mutated by fastcyc.mutate, kept only if the Xi-graph stays ACYCLIC
        cnt, seed = map(int, sys.argv[2:4]); base = [json.load(open(f)) for f in sys.argv[4:]]; rng = random.Random(seed)
        tot = {}; Ls = []; done = 0
        while done < cnt:
            G = json.loads(json.dumps(rng.choice(base)))
            for _ in range(rng.randint(1, 6)): G = fastcyc.mutate(G, rng)
            if not acyclic(G): continue
            L, why, bad = check(G); Ls.append(L); done += 1
            for k, x in bad.items(): tot[k] = tot.get(k, 0) + x
        print(f"LEMCK perturbed ACYC games {cnt} L {min(Ls)}-{max(Ls)} sum {sum(Ls)} viol " + " ".join(f"{k} {x}" for k, x in tot.items()))
    else:
        for f in sys.argv[1:]:
            L, why, bad = check(json.load(open(f)))
            print(f"LEMCK {os.path.basename(f)} L {L} {why} viol " + " ".join(f"{k} {x}" for k, x in bad.items()))
