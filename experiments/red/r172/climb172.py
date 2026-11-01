#!/usr/bin/env python3
"""L-RED R172: hill-climb against L-NEW's CONJECTURE TF-PH (box 122): inside a TWO-FIX window, a lambda_W-phase intersected with a
fallback-free run has at most n - 1 W-changing transitions. PHNF is computed exactly as in L-NEW's experiments/new/box122/windows.py
(W := the valuation of sigma in G_tau; in-phase := lambda_W equal at both states; PHNF resets at lambda_W changes and at fallbacks).
Score = (max PHNF over windows with ODIFF >= MINODIFF (env, default 1), its window L). Genome / mutations as climb170 (KO Odd choice
vertices, so ODIFF <= KO by FREEZE). Usage: climb172.py N KO SEED ITERS OUT_PREFIX [SEED_PG SEED_START|-]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "r170")); sys.path.insert(0, os.path.join(HERE, "..", "r171"))
from climb170 import rand_game, mutate, write
from climb171 import load_genome
from n5x import step, Engine, dual
import pg
MINOD = int(os.environ.get("MINODIFF", "1"))

def phnf_windows(g, s, t, cap=3000):
    n, own = g.n, g.owner; E, Ed = Engine(g), Engine(dual(g)); S, T, FBL = [tuple(s)], [tuple(t)], []
    while len(S) - 1 < cap:
        r = step(g, E, Ed, list(S[-1]), list(T[-1]))
        if r is None: break
        S.append(tuple(r[0])); T.append(tuple(r[1])); FBL.append(r[4])
    K = len(S) - 1; SB = [tuple(-1 if own[v] == 0 else E.evaluate(x)[1][v] for v in range(n)) for x in S]
    out = []; k = 0
    while k < K:
        if T[k + 1] != T[k] or SB[k + 1] != SB[k]: k += 1; continue
        a = k
        while k < K and T[k + 1] == T[k] and SB[k + 1] == SB[k]: k += 1
        b = k; tau = T[a]; od = sum(1 for v in range(n) if own[v] == 1 and SB[a][v] != tau[v])
        et = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
        Ws = [et.evaluate(S[j])[0] for j in range(a, b + 1)]; lam = [tuple(w[0] for w in x) for x in Ws]
        pn = mpn = 0
        for j in range(a, b):
            i = j - a
            if lam[i] != lam[i + 1]: pn = 0; continue
            if i > 0 and lam[i] != lam[i - 1]: pn = 0
            if FBL[j]: pn = 0
            else: pn += Ws[i + 1] != Ws[i]; mpn = max(mpn, pn)
        out.append(dict(a=a, b=b, L=b - a, ODIFF=od, FB=sum(FBL[a:b]), PHNF=mpn))
    return out, K

def score(G):
    g = pg.Game(G["prio"], G["own"], G["succ"])
    try: W, K = phnf_windows(g, G["s"], G["t"])
    except Exception: return (-1, 0), None
    W = [w for w in W if w["ODIFF"] >= MINOD]
    if not W: return (0, 0), None
    w = max(W, key=lambda w: (w["PHNF"], w["L"])); return (w["PHNF"], w["L"]), w

def main():
    n, ko, seed, iters, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    rng = random.Random(seed)
    G = load_genome(sys.argv[6], sys.argv[7]) if len(sys.argv) > 7 else rand_game(n, ko, n // 6, rng)
    n = len(G["prio"]); sc, w = score(G); print(f"start PHNF {sc[0]} {w}", flush=True)
    for i in range(iters):
        if i % 400 == 399 and sc[0] < 2 and len(sys.argv) <= 7: G = rand_game(n, ko, n // 6, rng); sc, w = score(G)
        H = mutate(G, rng)
        if H is None: continue
        H["ch"] = [v for v in range(n) if H["own"][v] == 1 and len(H["succ"][v]) > 1]
        s2, w2 = score(H)
        if s2 >= sc:
            if s2 > sc: print(f"it {i} PHNF {s2[0]} L {s2[1]} {w2}", flush=True)
            G, sc, w = H, s2, w2
    write(G, out); print(f"BEST n {n} KO {ko} PHNF {sc[0]} (n-1 = {n - 1}) {w}")

if __name__ == "__main__":
    main()
