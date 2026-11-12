#!/usr/bin/env python3
"""L-COMP box 44 item 1: classification of count differences on W(H, s0), as L-RED 66 classified n5x236 / n5v in R236 (claude/l-red
7317ed4c notes: «start 0, fallback 0, real divergence 0; ALL tie rule. At the first differing state ... every differing choice is
optimal ... in BOTH engines»).
Two runs of N5'-xi from S3 on two builds / tie rules of the SAME (H, s0) are compared through their H-parts (the Even strategy of H at
every state before the first fallback):
  start    : the H-parts differ at state 0;
  tie      : at the first differing state t, every vertex where they differ chose, in BOTH runs, a ⊴-best successor by H's own valuation
             at state t − 1 (so the two runs are two Howard runs of H that resolve a tie differently);
  real     : at the first differing state some differing choice is not a best successor in one of the runs;
  fallback : the H-parts are equal state for state but the fallback position, the number of fallbacks or the iterations differ;
  same     : nothing differs.
Configurations: A = my vertex order and tie rule (ORDER=mine); B one of: rev, rand:<seed> (the new vertices of W in another index
order), tiemin (TIE ties to the smaller index, SPEC's choice ignored: N5XI44_CTRL=1), howard (no W at all: MY Howard run of H with the
rule «keep a best current successor, else the largest index among the best»; then only start / tie / real / same are possible, and
«same» also needs equal length).
Usage: cls44.py RAND300.json B [first last]  -> one line per differing game and a summary line."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import wrap44, n5xi44, val44, wchk44
from wchk44 import pg, SpecSI
EVEN = 0


def hrun(h, s0, order, xctrl):
    wrap44.ORDER = order; n5xi44.XCTRL = xctrl
    g, V = wrap44.wrap(h, s0); run = []
    def hook(t, sigma, tau, vs, Is, It, F):
        if F == 0: run.append(wrap44.hpart(h, sigma, V))
    r = n5xi44.run(g, "xi", hook=hook)
    return run, (r["Ttot"], r["F"], r["first"])


def classify(h, A, B, ca, cb):
    if A[0] != B[0]: return "start", 0
    si = SpecSI(h)
    for t in range(1, min(len(A), len(B))):
        if A[t] == B[t]: continue
        val = si.evaluate(list(A[t - 1])); ok = True
        for v in range(h.n):
            if h.owner[v] == EVEN and A[t][v] != B[t][v]:
                best = val44.bestset(h, val, v)
                if A[t][v] not in best or B[t][v] not in best: ok = False
        return ("tie" if ok else "real"), t
    if len(A) != len(B): return "real", min(len(A), len(B))       # one run stops where the other goes on from the same state
    return ("same" if ca == cb else "fallback"), -1


if __name__ == "__main__":
    D = json.load(open(sys.argv[1])); mode = sys.argv[2]
    lo = int(sys.argv[3]) if len(sys.argv) > 3 else 0; hi = int(sys.argv[4]) if len(sys.argv) > 4 else len(D["games"])
    tot = dict(same=0, start=0, tie=0, real=0, fallback=0); cdiff = 0
    for i in range(lo, hi):
        G = D["games"][i]; h = pg.Game(G["prio"], G["owner"], G["succ"]); s0 = G["s0"]
        A, ca = hrun(h, s0, "mine", "0")
        if mode == "howard":
            st, T, ties, sw = val44.howard(h, s0); B = st; cb = ca if len(B) == len(A) else None
        elif mode == "tiemin": B, cb = hrun(h, s0, "mine", "1")
        else: B, cb = hrun(h, s0, mode, "0")
        k, t = classify(h, A, B, ca, cb); tot[k] += 1; cdiff += (len(A) != len(B)) or (cb is not None and ca != cb)
        if k != "same": print("CLS44 %s game %d: %s at state %d | A: T %d (iterations, fallbacks, first) %s | B: T %d %s" % (mode, i, k, t, len(A) - 1, ca, len(B) - 1, cb if mode != "howard" else "-"))
    print("CLS44 %s vs mine, games %d-%d of %s: %s | games whose counts differ %d" % (mode, lo, hi - 1, os.path.basename(sys.argv[1]), " ".join("%s %d" % kv for kv in tot.items()), cdiff))
