#!/usr/bin/env python3
"""L-RED-B B6 attempt 2 (for the referees of P-N5-EXP): R117's own side conditions, checked on Gamma3(G_k).

Corollary EXP-N5 uses RESULTS R117's Theorem REACH3 as landed. R117 states two lemmas inside it that a referee may want tested on
THESE games, whose shape (two options on one W-target, Xi-target X at positive levels, all parities even, up to 9 movers on a
level) is unusual: «S3's start pair equal to R104's stated start transported through the pads (Lemma S3-START)» and «no pad is ever
a cycle node or in a P-set (Lemma PAD)».
Must-0 counters, per genome (pads = the 4M + 4 vertices pA, s, q, r, pe, pbeta, pb, m of R117's list):
  startdiff (unit vertices): SPEC's S3 start pair (n5x.start_pair) differs from R104's stated start transported through the pads
            (what gamma3.build returns), on Even's vertices or on Odd's
  padcyc    (unit (state, vertex)): the cycle node of some vertex's value is a pad, at some state of the run
  padp      (unit (state, vertex)): the P-set of some vertex's value contains a pad, at some state of the run
  fbpos     1 if the mover states 0..F are not the model's run, or the first fallback is not at transition L(G) + 1
Descriptive: n, its (iterations to N5's stop), L (the model's run length), states checked.
Control B6R_CTRL=1: padcyc / padp are counted for the two NON-pad vertices K1 and s... (K1 is the common cycle node, so padcyc
must fire).
Usage: b6reach.py LNEW G.json ..."""
import sys, os
LNEW = os.path.abspath(sys.argv[1])
sys.path[:0] = [os.path.join(LNEW, p) for p in ("experiments/new/box195", "experiments/new/box189", "experiments/new/box190",
                                               "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("EG195_ROOT", LNEW)
import gamma3, eg195, n5v, n5x
import onep
CTRL = os.environ.get("B6R_CTRL", "0")
PADKINDS = ("pA", "s", "q", "r", "pe", "pbeta", "pb", "m")

for fn in sys.argv[2:]:
    G = onep.load(fn)
    g0, sig0, tau0, V = gamma3.build(G, eg195.PADS)
    g = eg195.topg(g0)
    pads = set()
    for key, v in V.items():
        kind = key[0] if isinstance(key, tuple) else key
        if kind in PADKINDS:
            pads.add(v)
    if CTRL == "1":
        pads = {V[("K", 1)], V["s"]}
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g))
    sigma, tau = n5x.start_pair(g, E, Ed, None)
    startdiff = sum(1 for v in range(g.n) if g.owner[v] == 0 and sig0[v] != sigma[v]) \
        + sum(1 for v in range(g.n) if g.owner[v] == 1 and tau0.get(v, tau[v]) != tau[v])
    R = onep.OneP(G).run("key")
    L = len(R) - 1
    S = [gamma3.mover_state(G, V, sigma, eg195.PADS)]
    padcyc = padp = states = its = 0
    F = None
    while its < 10 ** 7:
        vs, _ = E.evaluate(tuple(sigma))
        states += 1
        for v in range(g.n):
            cyc, path, _ = vs[v]
            padcyc += int(cyc in pads)
            padp += int(any((path >> E.rank[p]) & 1 for p in pads))
        res = n5v.step(g, E, Ed, sigma, tau, "spec")
        if res is None:
            break
        its += 1
        if res[4] and F is None:
            F = its - 1
        if F is None:
            S.append(gamma3.mover_state(G, V, res[0], eg195.PADS))
        sigma, tau = list(res[0]), list(res[1])
    if F is None:
        F = its
    fbpos = int(F != L or [tuple(s) for s in S] != [tuple(s) for s in R])
    print(f"{os.path.basename(fn)[:-5]} ctrl {CTRL} n {g.n} pads {len(pads)} its {its} L {L} states {states} "
          f"startdiff {startdiff} padcyc {padcyc} padp {padp} fbpos {fbpos}", flush=True)
