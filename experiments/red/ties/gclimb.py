#!/usr/bin/env python3
"""L-RED successor 22: climb for (G1) of docs/si/N5-GCILEN-box22.md §5: a global C-interval (P-N5-GCX §1; R91 §5) of a lambda_W-constant
fallback-free run that CONTAINS a sigma-bar change, as long as possible relative to n. Score = (len - (n - 1), -n). Odd choice set fixed
(box43 climb.mutate), so k is fixed. Usage: gclimb.py SEED.pg [SEED.start|-] STEPS RNGSEED NMAX OUTPREFIX"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(HERE, "..", "ul")); sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box43"))
import ulx
import climb
climb.DEG2 = False
from multi import odd_choices

def score(g, st):
    try: E, R = ulx.trace(g, st, cap=600)
    except RecursionError: return None
    n = g.n; best = None; i = 0
    while i < len(R):
        j = i
        while j + 1 < len(R) and (R[j + 1]["lam"], R[j + 1]["t"]) == (R[i]["lam"], R[i]["t"]): j += 1
        s0 = i
        for k in range(i, j + 1):                  # cut at fallbacks and at lambda_W changes
            if k == j or R[k]["fb"] or R[k + 1]["lamW"] != R[k]["lamW"]:
                best = mx(best, run(g, E, R, s0, k))
                s0 = k + 1
        i = j + 1
    return best

def mx(a, b): return b if a is None or (b is not None and b > a) else a

def run(g, E, R, s0, e0):
    if e0 <= s0: return None
    n = g.n; best = None; G = {}
    for k in range(s0, e0 + 1):
        D = {u for u in range(n) if g.owner[u] == 1 and R[k]["sb"][u] != R[k]["t"][u]}
        A = set(range(n)) - ulx.meets(R[k]["wn"], D, n); DD = {}
        for u in D:
            cu = R[k]["lam"][u]
            if R[k]["sb"][u] in A and R[k]["t"][u] in A and R[k]["lam"][R[k]["sb"][u]] == cu and R[k]["lam"][R[k]["t"][u]] == cu:
                DD[u] = E.weight(R[k]["vs"][R[k]["t"][u]][1]) - E.weight(R[k]["vs"][R[k]["sb"][u]][1])
        G[k] = (A, D, DD)
    a = s0
    for k in range(s0, e0 + 1):
        ok = k < e0 and G[k + 1][0] <= G[k][0] and G[k + 1][1] == G[k][1] and G[k + 1][2] == G[k][2]
        if not ok:
            if any(R[x]["sb"] != R[x + 1]["sb"] for x in range(a, k)): best = mx(best, ((k - a) - (n - 1), -n, a, k))
            a = k + 1
    return best

def main():
    gp, sp, steps, seed, nmax, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
    rng = random.Random(seed); g = ulx.load(gp); O = sorted(odd_choices(g))
    st = None
    if sp != "-":
        s, t = ulx.readstart(sp); st = [s.get(v, t.get(v)) for v in range(g.n)]
    cur = score(g, mkst(g, st)); print("seed score", cur, "k", len(O), "n", g.n, flush=True)
    for it in range(steps):
        r = climb.mutate(rng, g, O, nmax, st)
        if r is None: continue
        g2, O2, st2 = r
        sc = score(g2, mkst(g2, st2))
        if sc is not None and (cur is None or sc[:2] >= cur[:2]):
            if cur is None or sc[:2] > cur[:2]: print("step", it, "score", sc, "n", g2.n, flush=True); save(out, g2, st2)
            g, O, st, cur = g2, O2, st2, sc
    print("final", cur)

def mkst(g, st):
    if not st: return None
    return ({v: st[v] for v in range(g.n) if g.owner[v] == 0}, {v: st[v] for v in range(g.n) if g.owner[v] == 1})

def save(out, g, st):
    with open(out + ".pg", "w") as f:
        f.write("parity %d;\n" % (g.n - 1))
        for v in range(g.n): f.write("%d %d %d %s;\n" % (v, g.prio[v], g.owner[v], ",".join(map(str, g.succ[v]))))
    if st:
        with open(out + ".start", "w") as f:
            f.write("SIGMA0 " + " ".join("%d:%d" % (v, st[v]) for v in range(g.n) if g.owner[v] == 0) + "\n")
            f.write("TAU0 " + " ".join("%d:%d" % (v, st[v]) for v in range(g.n) if g.owner[v] == 1) + "\n")

if __name__ == "__main__":
    main()
