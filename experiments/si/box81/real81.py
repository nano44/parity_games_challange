#!/usr/bin/env python3
"""L-SI box 81: the REAL algorithms on Gamma3(G) from the default start S3 (byte copies of L-NEW's runners in ref/: box190 n5v.py,
box21 n5x.py, n5.py, box189 gamma3.py with pads {K, pe, pb, m}), and, with --stated, N5 on Gamma(G) (no pads) from R104's STATED start.
With --stated also: R104's IDEAL run (box80 sim80.Sim) T and whether N5's mover-phase states equal it (Theorem REALIZE).
Per genome and mode (xi = N5'-xi, spec = N5) prints: iterations, fallbacks, T3 = transitions before the first one that changes tau or a
non-mover/non-beta Even vertex or is a fallback (the mover phase), whether the mover-phase states equal IDEAL-CYC Howard's states
(idealcyc.run, R118 / REACH3-CYC), and the number of distinct mover states.
Usage: real81.py [--stated] [--modes xi,spec] FILES.json"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); RN = os.path.join(HERE, "ref", "experiments", "new")
sys.path[:0] = [os.path.join(RN, "box190"), os.path.join(RN, "box191"), os.path.join(RN, "box189")]
import n5v, gamma3, idealcyc
PADS = {"K", "pe", "pb", "m"}


def real(G, mode, stated=False, cap=10 ** 4):
    pads = set() if stated else PADS
    g, sig0, tau0, V = gamma3.build(G, pads); N = G["N"]
    start = None
    if stated:
        start = ({v: w for v, w in sig0.items() if g.owner[v] == 0}, {v: w for v, w in tau0.items() if g.owner[v] == 1})
        os.environ["N5X_STRICT_START"] = "1"
    states, fbs, E = n5v.run(g, mode, start, cap)
    s0, t0 = states[0]
    keep = {V[("x", x)] for x in range(N)} | {V[("b", (x, k))] for x in range(N) for k in range(len(G["opts"][x]))}
    T3 = 0
    for t in range(1, len(states)):
        s, ta = states[t]
        if ta != t0 or any(s[v] != s0[v] for v in range(g.n) if g.owner[v] == 0 and v not in keep): break
        T3 = t
    ms = [gamma3.mover_state(G, V, s, pads) for s, _ in states]
    how = [tuple(z) for z in idealcyc.run(G)]
    eq = ms[:T3 + 1] == how[:T3 + 1]
    extra = {}
    if stated:
        sys.path.insert(0, os.path.join(HERE, "..", "box80")); import sim80
        S = [tuple(z) for z in sim80.Sim(G).run()]
        extra = dict(idealT=len(S) - 1, moverphase_eq_ideal=int(ms[:T3 + 1] == S[:T3 + 1]), T3_eq_idealT=int(T3 == len(S) - 1))
    return dict(**extra, iters=len(states) - 1, fallbacks=fbs, T3=T3, howardT=len(how) - 1, moverphase_eq_howard=int(eq),
                full_eq_howard=int(ms[:len(how)] == how), distinct_mover_states=len(set(ms)))


if __name__ == "__main__":
    a = sys.argv[1:]; stated = "--stated" in a; a = [z for z in a if z != "--stated"]; modes = ["xi", "spec"]
    if "--modes" in a:
        i = a.index("--modes"); modes = a[i + 1].split(","); del a[i:i + 2]
    for f in a:
        G = json.load(open(f))
        for m in modes:
            r = real(G, m, stated)
            print(os.path.basename(f), "mode", m, "start", "stated" if stated else "S3", " ".join(f"{k} {v}" for k, v in r.items()), flush=True)
