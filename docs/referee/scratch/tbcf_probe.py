#!/usr/bin/env python3
"""REFEREE successor 22: own DATA for the L44 question on RESULTS R24 (a) Lemma R and (b) TB's choice form, on games OUTSIDE C^1O.
Own engine rl_engine (written from SPEC only); no lane code. At every fallback-free transition k -> k+1 with I_sigma_k != {}:
  H := S4a's arena (Even v keeps A(v) = {sigma_k(v)} u I_sigma_k(v), Odd keeps tau_k(v)); W' := play values of (sigma_(k+1), tau_k) in G.
  For every Even h with |A(h)| > 1 that is not the cycle node c of W'(h) and not on its own W'-cycle (else a corner, counted, skipped):
    FO(h) := {y in A(h) : h not on y's W'-play and h (+) W'(y) = W'(h) in all three components}   (fully optimal options)
    SEL   sigma_(k+1)(h) in FO(h)
    ODD   c odd:  sigma_(k+1)(h) = min FO(h)                                 (TB's choice rule, longest-path mode in the dual)
    EVEN  c even: sigma_(k+1)(h) = the y in FO(h) with lex-least root-first key kappa(y) (indices of y's play, c excluded, read from c)
    BRIDGE at a FLAT non-corner move (o := sigma_k(h) != w := sigma_(k+1)(h), W'(o) = W'(w), h on neither play): o in FO(h)
MUT 1: ODD/EVEN rules swapped (must bite). CORNER=pre: a corner is h on y's play before y's cycle node (h on its own W'-cycle tested). Usage: tbcf_probe.py N seed   (random games, n 4-14, 2-5 Odd choice vertices, random start)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE
import dual_probe as D
MUT = int(os.environ.get("MUT", "0")); PRE = os.environ.get("CORNER") == "pre"
EX = []


def play(nx, v):
    seq, seen = [], set()
    while v not in seen: seen.add(v); seq.append(v); v = nx[v]
    return seq


def analyse(cnt, g, start, name):
    st = RE.run(g, start); n = g.n
    for k in range(len(st) - 1):
        S = st[k]
        if S["fb"] or not S["Is"]: continue
        s, t, s1 = S["s"], S["t"], st[k + 1]["s"]
        A = {v: {s[v]} for v in range(n) if g.owner[v] == 0}
        for v, w in S["Is"]: A[v].add(w)
        nx = [s1[v] if g.owner[v] == 0 else t[v] for v in range(n)]
        Wp = [RE.play_value(g, nx, v) for v in range(n)]
        for h in A:
            if len(A[h]) < 2: continue
            c = Wp[h][0]
            if h == c: continue
            w = s1[h]
            if PRE:   # corner = h occurs on y's play BEFORE y's cycle node (s22, R-N5-ANCHOR ANC-1); h on its own W'-cycle is tested
                def passes(y):
                    p = play(nx, y); return h in p[:p.index(c)] if c in p else h in p
                if h in play(nx, w): cnt["on_own_cycle_tested"] += 1
            else:
                def passes(y): return h in play(nx, y)
                if h in play(nx, w): cnt["corner_own_cycle"] += 1; continue   # h on its own W'-cycle: skipped (first reading)
            FO = [y for y in sorted(A[h]) if not passes(y) and g.ext(h, Wp[y]) == Wp[h]]
            cnt["movers"] += 1   # every checked Even h with >= 2 options («movers» is a misnomer: non-movers included, counted below)
            if w == s[h]: cnt["nonmovers"] += 1
            if w not in FO: fail(cnt, "SEL", name, k, h); continue
            def kappa(y):
                p = play(nx, y); return list(reversed(p[:p.index(c)]))
            odd = g.prio[c] % 2 == 1
            if len(FO) > 1: cnt["ties_odd" if odd else "ties_even"] += 1
            if len(FO) > 1 and not odd and min(FO, key=kappa) != min(FO): cnt["ties_even_kappa_ne_index"] += 1
            if MUT == 1: odd = not odd
            if odd:
                cnt["odd"] += 1
                if w != min(FO): fail(cnt, "ODD", name, k, h)
            else:
                cnt["even"] += 1
                if w != min(FO, key=kappa): fail(cnt, "EVEN", name, k, h)
            o = s[h]
            if o != w and Wp[o] == Wp[w] and h not in play(nx, o) and h not in play(nx, w):
                cnt["flat_nc"] += 1
                if o not in FO: fail(cnt, "BRIDGE", name, k, h)


def fail(cnt, tag, *a):
    cnt[tag + "_V"] += 1
    if len(EX) < 20: EX.append((tag,) + a)


def main(a):
    N, seed = int(a[0]), int(a[1]); r = random.Random(seed); cnt = Counter()
    for i in range(N):
        nn = r.randint(4, 14); k = r.randint(2, min(5, nn - 1))
        g = D.rand_ck(r, nn, k); cnt["GAMES"] += 1
        try: analyse(cnt, g, D.rand_start(g, r), "rand%d" % i)
        except RuntimeError: cnt["maxit"] += 1
    for x in sorted(cnt): print(x, cnt[x])
    print("VIOLATIONS", sum(v for x, v in cnt.items() if x.endswith("_V")))
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
