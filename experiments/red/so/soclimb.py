#!/usr/bin/env python3
"""Box 36 (L-RED): hill-climb on 𝒞^1O games against P-N5-SO / P-N5-LP §4, counter = sox.analyse (own checker).
Fitness (lexicographic, failures of any sox sub-claim first):
  tie : (fails, max θ-fixed relevant σ̄(o) changes in one θ-run, max per phase of θ-fixed changes, max pure tie-break moves)
  j   : (fails, max (J − S_o), max J)            k : (fails, max K, max J)
  th  : (fails, max Θ, max X)                    so: (fails, max S_o − Θ, max S_o)
Mutations keep exactly one Odd vertex with out-degree > 1 (others are rejected). Invalid sentinel −10^9 (trap 1).
Usage: soclimb.py mode seed secs OUT [seed.pg | --rand n]"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sox, pg
NEG = (-10 ** 9,) * 4

def mutate(rng, G):
    prio, owner, succ = [list(G[0]), list(G[1]), [list(s) for s in G[2]]]; n = len(prio)
    for _ in range(rng.choice((1, 1, 2, 3))):
        k = rng.randrange(6); v = rng.randrange(n)
        if k == 0: prio[v] = rng.randrange(n)
        elif k == 1: owner[v] ^= 1
        elif k == 2: succ[v] = sorted(set(succ[v]) | {rng.randrange(n)})
        elif k == 3 and len(succ[v]) > 1: succ[v].remove(rng.choice(succ[v]))
        elif k == 4: w = rng.randrange(n); succ[v] = sorted(set(succ[v]) - {rng.choice(succ[v])} | {w}) or [w]
        else: a, b = rng.randrange(n), rng.randrange(n); prio[a], prio[b] = prio[b], prio[a]
    return [prio, owner, succ]

def fit(G, mode):
    g = pg.Game(*G)
    if any(not s for s in G[2]) or len(sox.oddchoice(g)) != 1: return NEG, None
    try: r = sox.analyse(g, cap=3000)
    except AssertionError: raise
    except Exception: return NEG, None
    rs = r["rows"]; fails = sum(r["C"].values())
    mx = lambda f: max((f(x) for x in rs), default=-10 ** 9)
    if mode == "tie": f = (fails, mx(lambda x: x["maxrun"]), mx(lambda x: x["fixch"]), mx(lambda x: x["tiepure"]))
    elif mode == "j": f = (fails, max((x["J"] - x["So"] for x in rs if x["J"] >= 1), default=-10 ** 9), mx(lambda x: x["J"]), 0)   # trap 2: J >= 1 only
    elif mode == "k": f = (fails, mx(lambda x: x["K"]), mx(lambda x: x["J"]), 0)
    elif mode == "th": f = (fails, mx(lambda x: x["Th"]), mx(lambda x: x["X"]), 0)
    elif mode == "so": f = (fails, mx(lambda x: x["So"] - x["Th"]), mx(lambda x: x["So"]), 0)
    return f, r

def dump(G, path):
    n = len(G[0])
    open(path, "w").write(f"parity {n-1};\n" + "".join(f"{v} {G[0][v]} {G[1][v]} {','.join(map(str, G[2][v]))};\n" for v in range(n)))

if __name__ == "__main__":
    mode, seed, secs, out = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    if sys.argv[5] == "--rand":
        n = int(sys.argv[6])
        while True:
            prio = [rng.randrange(n) for _ in range(n)]; owner = [rng.randrange(2) for _ in range(n)]
            succ = [sorted(set(rng.sample(range(n), 1 if owner[v] else rng.choice((1, 2, 2, 3))))) for v in range(n)]
            o = rng.randrange(n); owner[o] = 1; succ[o] = sorted(set(rng.sample(range(n), max(2, n // 4))))
            G = [prio, owner, succ]; f, r = fit(G, mode)
            if f != NEG: break
    else:
        g = sox.load(sys.argv[5]); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f, r = fit(G, mode)
    t0 = time.time(); it = 0; print("start", f, flush=True); dump(G, out + ".pg")
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh, rh = fit(H, mode)
        if fh >= f:
            if fh > f:
                print(f"{time.time()-t0:7.0f}s it {it} fit {fh} it/fb {rh['it']}/{rh['fb']} C {rh['C']} ex {rh['ex']}", flush=True); dump(H, out + ".pg")
            G, f = H, fh
    print("FINAL", f, it, flush=True)
