#!/usr/bin/env python3
"""L-SI box 55: random / targeted search for a RET event (box 54 §3), i.e. a counterexample to Lemma NO-RET (note
docs/si/N5-FSEG-box55.md §1) = unconditional ODD-STEP: at an N5 transition k -> k + 1, an Odd o whose Xi changes while
Xi(sigmabar_k(o)) does not. Checked at EVERY transition (S4a or fallback; R15 (d)). RETX counts violations; ONPLAY counts the
transitions where o lies on sigmabar_k(o)'s new Xi-play (the case NO-RET had to exclude by proof) whatever Xi does.
Random games: n vertices, random owners / priorities, out-degree 1..DMAX, random start pair. BIAS=1: vertex 0 Odd with the top EVEN
priority (the subcase «o even above the cycle»); BIAS=2: vertex 0 Odd with the top odd priority. Saves violating games to OUT/.
MUT=1 (control): Xi(sigmabar_k(o)) is compared with a wrong state (k + 1 vs k + 1), so RETX must bite.
Usage: retsearch.py SEED COUNT N DMAX BIAS OUT"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import step, start_pair, Engine, dual
import pg
seed, cnt, N, DMAX, BIAS, OUT = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
MUT = os.environ.get("MUT") == "1"
rng = random.Random(seed)
tot = dict(GAMES=0, ITERS=0, ODDCH=0, ONPLAY=0, RETX=0, BAD=0)
for i in range(cnt):
    n = N; own = [rng.randint(0, 1) for _ in range(n)]; pr = [rng.randint(0, n) for _ in range(n)]
    if BIAS == 1: own[0] = 1; pr[0] = (max(pr) + 2) & ~1
    if BIAS == 2: own[0] = 1; pr[0] = (max(pr) + 1) | 1
    succ = [rng.sample(range(n), rng.randint(1, DMAX)) for _ in range(n)]
    g = pg.Game(pr, own, succ)
    st = ({v: rng.choice(succ[v]) for v in range(n) if own[v] == 0}, {v: rng.choice(succ[v]) for v in range(n) if own[v] == 1})
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); S = [tuple(s)]; TA = list(t)
    while len(S) < 400:
        r = step(g, E, Ed, list(S[-1]), TA)
        if r is None: break
        S.append(tuple(r[0])); TA = list(r[1])
    EV = [E.evaluate(x) for x in S]; bad = 0
    for k in range(len(S) - 1):
        (X0, b0), (X1, b1) = EV[k], EV[k + 1]
        for o in range(n):
            if own[o] != 1 or X0[o] == X1[o]: continue
            tot['ODDCH'] += 1; x = b0[o]
            y, seen = x, set()
            while y not in seen and y != o: seen.add(y); y = S[k + 1][y] if own[y] == 0 else b1[y]
            tot['ONPLAY'] += y == o
            same = (X1[x] == X1[x]) if MUT else (X0[x] == X1[x])
            if same: tot['RETX'] += 1; bad += 1
    tot['GAMES'] += 1; tot['ITERS'] += len(S) - 1
    if bad:
        tot['BAD'] += 1; os.makedirs(OUT, exist_ok=True); f = os.path.join(OUT, f"ret_{seed}_{i}")
        if not MUT:
            with open(f + ".pg", "w") as h:
                h.write(f"parity {n - 1};\n" + "".join(f"{v} {pr[v]} {own[v]} {','.join(map(str, succ[v]))};\n" for v in range(n)))
            with open(f + ".start", "w") as h:
                h.write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in st[0].items()) + "\nTAU0 " + " ".join(f"{v}:{w}" for v, w in st[1].items()) + "\n")
            print("BAD", f, flush=True)
print(f"RETSEARCH seed {seed} n {N} dmax {DMAX} bias {BIAS} mut {int(MUT)} " + " ".join(f"{k} {v}" for k, v in tot.items()))
