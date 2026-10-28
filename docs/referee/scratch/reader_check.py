#!/usr/bin/env python3
"""REFEREE succ. 16: own check of the READER device (L-SI, docs/si/N5-ALT-box23.md §8). Own engine rl_engine (SPEC S1-S5); no lane code.
Runs N5 on a base game G (with its start) and on G' = G + reader vertex o (with its start), and compares state by state on the old vertices:
sigma, tau, sigmabar, the fallback flag, the phase cut ((lambda_Xi, tau) constant), and Xi as (cycle node, path set as a VERTEX set, length).
On G' it also reports, per state: Itau(o) (o's improving edges on G^d), whether tau(o) moves, and whether Xi(o) = o (+) min_{y in S} Xi(y).
Usage: reader_check.py base.pg base.start reader.pg reader.start o [phase_a phase_b]"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE
from gcx_probe import load_start


def vset(g, mask): return frozenset(g.byrank[r] for r in range(g.n) if (mask >> r) & 1)


def main(a):
    gb, gr = RE.parse(a[0]), RE.parse(a[2]); o = int(a[4])
    sb, sr = RE.run(gb, load_start(gb, a[1])), RE.run(gr, load_start(gr, a[3]))
    n = gb.n; S = gr.succ[o]
    print("states base / reader:", len(sb), len(sr), "| o =", o, "S =", S, "| rank(o) =", gr.rank[o],
          "| old vertices with priority <= prio(o):", sum(1 for v in range(n) if gb.prio[v] <= gr.prio[o]))
    same = len(sb) == len(sr); first = None
    for k in range(min(len(sb), len(sr))):
        x, y = sb[k], sr[k]
        ok = (x["s"][:n] == y["s"][:n] and x["t"][:n] == y["t"][:n] and x["sb"][:n] == y["sb"][:n] and x["fb"] == y["fb"]
              and all((x["Xi"][v][0], vset(gb, x["Xi"][v][1]), x["Xi"][v][2]) == (y["Xi"][v][0], vset(gr, y["Xi"][v][1]), y["Xi"][v][2]) for v in range(n)))
        if not ok and first is None: first = k
    same = same and first is None
    print("SAME on old vertices:", same, "" if same else "(first difference at state %s)" % first)
    def phases(st, nn):
        cut = []; k = 0
        while k < len(st):
            j = k; key = lambda q: (tuple(v[0] for v in st[q]["Xi"][:nn]), tuple(st[q]["t"]))
            while j + 1 < len(st) and key(j + 1) == key(k): j += 1
            cut.append((k, j)); k = j + 1
        return cut
    pb, pr = phases(sb, n), phases(sr, gr.n)
    print("phases equal:", pb == pr, "| base phases:", pb, "" if pb == pr else "| reader phases: %s" % pr)
    gd = gr.dual(); moves = 0; itau = 0; minok = 0
    for k, y in enumerate(sr):
        if any(v == o for v, w in y["It"]): itau += 1
        if k + 1 < len(sr) and sr[k + 1]["t"][o] != y["t"][o]: moves += 1
        best = min((y["Xi"][s] for s in S), key=lambda v: gr.key(v))
        if y["Xi"][o] == gr.ext(o, best): minok += 1
    print("states with Itau(o) != {}:", itau, "| tau(o) moves:", moves, "| Xi(o) = o (+) min_S Xi at", minok, "of", len(sr), "states")
    if len(a) > 6:
        pa, pb_ = int(a[5]), int(a[6])
        ch = sum(1 for k in range(pa, pb_) if sr[k]["Xi"][o] != sr[k + 1]["Xi"][o])
        D = sum(1 for k in range(pa, pb_ + 1) if sr[k]["sb"][o] != sr[k]["t"][o])
        sbc = sum(1 for k in range(pa, pb_) if sr[k]["sb"][o] != sr[k + 1]["sb"][o])
        fbs = sum(1 for k in range(pa, pb_) if sr[k]["fb"])
        print("phase [%d, %d]: Xi(o) changes %d (2n = %d); o in D at %d states; sigmabar(o) changes %d; fallbacks %d"
              % (pa, pb_, ch, 2 * gr.n, D, sbc, fbs))


if __name__ == "__main__":
    main(sys.argv[1:])
