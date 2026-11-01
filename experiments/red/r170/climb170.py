#!/usr/bin/env python3
"""L-RED R170: hill-climb for long TWO-FIX windows (L-NEW box 121) on games with exactly KO Odd choice vertices (every other Odd
vertex has one edge), so every window has ODIFF <= KO (FREEZE, docs/red/R170-twofix.md section 1).
Genome: a game (n vertices, distinct priorities, owners, edges) and a valid start pair. Score: the longest TWO-FIX window L
(tau and si.Engine's sbar constant), then the run length K. Engine: n5x.step (SPEC S1-S5).
Usage: climb170.py N KO SEED ITERS OUT_PREFIX   (writes OUT_PREFIX.pg / .start for the best genome; prints progress lines)
Env: FBFREE=1 scores only windows without S4c fallbacks; MAXDEG (default 5) caps Even out-degree; MINODIFF=d scores only windows with ODIFF >= d; ODD=<count of single-edge Odd vertices> (default n // 6)."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import step, Engine, dual
import pg

FBFREE = os.environ.get("FBFREE") == "1"; MINOD = int(os.environ.get("MINODIFF", "0")); MAXDEG = int(os.environ.get("MAXDEG", "5"))

def score(G, cap=4000):
    g = pg.Game(G["prio"], G["own"], G["succ"]); n = g.n
    E, Ed = Engine(g), Engine(dual(g)); s, t = list(G["s"]), list(G["t"])
    S, T, F = [tuple(s)], [tuple(t)], [0]
    while len(S) - 1 < cap:
        r = step(g, E, Ed, list(S[-1]), list(T[-1]))
        if r is None: break
        S.append(tuple(r[0])); T.append(tuple(r[1])); F.append(r[4])
    SB = [tuple(E.evaluate(x)[1][v] if g.owner[v] == 1 else -1 for v in range(n)) for x in S]
    K = len(S) - 1; best = 0; bw = None; k = 0
    while k < K:
        if T[k + 1] != T[k] or SB[k + 1] != SB[k]: k += 1; continue
        a = k
        while k < K and T[k + 1] == T[k] and SB[k + 1] == SB[k]: k += 1
        fb = sum(F[a + 1:k + 1])
        if FBFREE and fb: continue
        if MINOD and sum(1 for v in range(n) if g.owner[v] == 1 and SB[a][v] != T[a][v]) < MINOD: continue
        if k - a > best: best, bw = k - a, (a, k, fb)
    return (best, K), bw

def rand_game(n, ko, nodd, rng):
    own = [0] * n
    odd = rng.sample(range(n), ko + nodd); ch = odd[:ko]
    for v in odd: own[v] = 1
    prio = list(range(n)); rng.shuffle(prio)
    succ = []
    for v in range(n):
        d = rng.choice([2, 3]) if v in ch else (1 if own[v] else rng.choice([1, 2, 2, 3, 3, 4]))
        succ.append(sorted(rng.sample(range(n), d)))
    G = {"prio": prio, "own": own, "succ": succ, "ch": ch}
    G["s"] = [rng.choice(succ[v]) if own[v] == 0 else -1 for v in range(n)]
    G["t"] = [rng.choice(succ[v]) if own[v] == 1 else -1 for v in range(n)]
    return G

def mutate(G, rng):
    n = len(G["prio"]); H = {k: (list(v) if isinstance(v, list) else v) for k, v in G.items()}
    H["succ"] = [list(s) for s in G["succ"]]
    op = rng.randrange(6)
    if op == 0:  # swap two priorities
        a, b = rng.sample(range(n), 2); H["prio"][a], H["prio"][b] = H["prio"][b], H["prio"][a]
    elif op in (1, 2):  # retarget an edge of an Even vertex or an Odd choice vertex
        cand = [v for v in range(n) if H["own"][v] == 0 or v in H["ch"]]; v = rng.choice(cand)
        i = rng.randrange(len(H["succ"][v])); w = rng.randrange(n)
        if w in H["succ"][v]: return None
        old = H["succ"][v][i]; H["succ"][v][i] = w; H["succ"][v].sort()
        for key in ("s", "t"):
            if H[key][v] == old: H[key][v] = w
    elif op == 3:  # add / remove an Even edge
        v = rng.choice([v for v in range(n) if H["own"][v] == 0])
        if len(H["succ"][v]) > 1 and rng.random() < 0.5:
            w = rng.choice(H["succ"][v]); H["succ"][v].remove(w)
            if H["s"][v] == w: H["s"][v] = rng.choice(H["succ"][v])
        else:
            w = rng.randrange(n)
            if w in H["succ"][v] or len(H["succ"][v]) >= MAXDEG: return None
            H["succ"][v].append(w); H["succ"][v].sort()
    elif op == 4:  # change a start choice
        v = rng.randrange(n); key = "s" if H["own"][v] == 0 else "t"; H[key][v] = rng.choice(H["succ"][v])
    else:  # retarget a single-edge Odd vertex
        c = [v for v in range(n) if H["own"][v] == 1 and v not in H["ch"]]
        if not c: return None
        v = rng.choice(c); w = rng.randrange(n); H["succ"][v] = [w]; H["t"][v] = w
    return H

def write(G, prefix):
    n = len(G["prio"])
    with open(prefix + ".pg", "w") as f:
        f.write(f"parity {n - 1};\n")
        for v in range(n): f.write(f"{v} {G['prio'][v]} {G['own'][v]} {','.join(map(str, G['succ'][v]))};\n")
    with open(prefix + ".start", "w") as f:
        f.write("SIGMA0 " + " ".join(f"{v}:{G['s'][v]}" for v in range(n) if G["own"][v] == 0) + "\n")
        f.write("TAU0 " + " ".join(f"{v}:{G['t'][v]}" for v in range(n) if G["own"][v] == 1) + "\n")

def main():
    n, ko, seed, iters, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    rng = random.Random(seed); nodd = int(os.environ.get("ODD", n // 6))
    G = rand_game(n, ko, nodd, rng); sc, bw = score(G)
    for i in range(iters):
        if i % 400 == 399 and sc[0] < 3:  # restart dead starts
            G = rand_game(n, ko, nodd, rng); sc, bw = score(G)
        H = mutate(G, rng)
        if H is None: continue
        s2, b2 = score(H)
        if s2 >= sc:
            if s2 > sc: print(f"it {i} L {s2[0]} K {s2[1]} window {b2}", flush=True)
            G, sc, bw = H, s2, b2
    write(G, out); print(f"BEST n {n} KO {ko} seed {seed} L {sc[0]} K {sc[1]} window {bw}")

if __name__ == "__main__":
    main()
