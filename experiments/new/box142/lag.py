#!/usr/bin/env python3
"""L-NEW box 142 LAG: on a 2-wide deg-2 IDEAL ladder (R178 §1 rule; Xi-graph any, values = box139/fastcyc_r178.py), find LAG events:
a step s at which L_(l-1) changes (l >= 1) and BOTH level-l movers then point away from the new L_(l-1) at state s - 1 ... more precisely:
let R = the level-l movers whose option at state s-1 does not target L_(l-1)(s) (released by the carry); a LAG event is |R| = 2 and the two
move at different steps before the next change of L_(l-1) (or both move, at steps s1 != s2). LAGMAX = max |s1 - s2|. Also counts
FLIPSTEP: steps at which L_l changes (at most one change per step by definition) and DOUBLE: carries after which L_l changes twice
before the next carry. DELAY[l]: released level-l movers that do not move at the carry step but move later before the next carry; DELVIOL counts levels
with flips(L_l) > flips(L_(l-1)) + 2 + DELAY[l] (Lemma DELAY-CHARGE).
Usage: lag.py genome.json ... | --rand d trials seed"""
import sys, os, json, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box139"))
src = open(os.path.join(HERE, "..", "box139", "paths.py")).read().split("def vx(G):")[0]
ns = {"__file__": os.path.join(HERE, "..", "box139", "paths.py")}; exec(src, ns); run = ns["run"]
def analyse(G):
    S, CUR, KEY, why = run(G, cap=3000); N, opts = G["N"], G["opts"]; d = N // 2
    T = len(S) - 1
    def L(t, l): return 2 * l if KEY[min(t, len(KEY) - 1)][2 * l] < KEY[min(t, len(KEY) - 1)][2 * l + 1] else 2 * l + 1
    lag = 0; lagmax = 0; double = 0; ex = None; delay = [0] * d; F = [0] * d; viol = 0
    for l in range(d): F[l] = sum(1 for t in range(1, T + 1) if L(t, l) != L(t - 1, l))
    for l in range(1, d):
        carries = [s for s in range(1, T + 1) if L(s, l - 1) != L(s - 1, l - 1)]
        for i, s in enumerate(carries):
            nxt = carries[i + 1] if i + 1 < len(carries) else T + 1
            Lm = L(s, l - 1); R = [x for x in (2 * l, 2 * l + 1) if opts[x][S[s - 1][x]][0] != Lm]
            if len(R) == 2:
                mt = [[t for t in range(s, nxt) if S[t][x] != S[t - 1][x]] for x in R]
                if mt[0] and mt[1] and mt[0][0] != mt[1][0]:
                    lag += 1; g = abs(mt[0][0] - mt[1][0]); lagmax = max(lagmax, g)
                    if ex is None: ex = (l, s, R, mt[0][0], mt[1][0])
            delay[l] += sum(1 for x in R if any(S[t][x] != S[t - 1][x] for t in range(s + 1, nxt)) and S[s][x] == S[s - 1][x])
            fl = sum(1 for t in range(s, nxt) if L(t, l) != L(t - 1, l))
            double += fl >= 2
    viol = sum(1 for l in range(1, d) if F[l] > F[l - 1] + 2 + delay[l])
    return T, why, lag, lagmax, double, ex, delay, F, viol
if sys.argv[1] == "--rand":
    sys.path.insert(0, os.path.join(HERE, "..", "box140"))
    src2 = open(os.path.join(HERE, "..", "box140", "upclimb.py")).read().split("def score(G):")[0].split("def rand(d, rng):")[1]
    exec("def rand(d, rng):" + src2.split("def mut(G, rng):")[0], globals())
    d, trials, seed = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); rng = random.Random(seed); best = None
    for i in range(trials):
        G = rand(d, rng)
        # allow ANY acyclic Xi-target (mover of a different level in a fixed topological order: higher index) for generality
        if os.environ.get("ANY"):
            for v in range(G["N"]):
                for k in range(2): G["opts"][v][k][1] = rng.choice([u for u in range(G["N"]) if u > v] + [-1])
        T, why, lag, lagmax, double, ex, delay, F, viol = analyse(G)
        if lag and (best is None or T < best[0]):
            best = (T, G, ex); print("LAGFOUND trial", i, "steps", T, "lag events", lag, "max", lagmax, "ex (level, carry step, movers, s1, s2)", ex, flush=True)
            json.dump(G, open(os.path.join(HERE, f"lag_min_d{d}.json"), "w"))
    print("DONE", "found" if best else "none")
else:
    for p in sys.argv[1:]:
        T, why, lag, lagmax, double, ex, delay, F, viol = analyse(json.load(open(p)))
        print(f"LAG {os.path.basename(p)} STEPS {T} STOP {why} LAGEVENTS {lag} LAGMAX {lagmax} DOUBLE {double} DELAY {delay} LFLIPS {F} DELVIOL {viol} EX {ex}")
