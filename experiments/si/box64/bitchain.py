#!/usr/bin/env python3
"""L-SI box 64: (1) check of Lemma BIT-CHAIN (docs/si/N5-FLIPOR-box64.md §2): on an R197 2-wide degree-2 ladder the IDEAL step
above level 0 is determined by the Xi-data, the bit b_0 and two bits per level c_l(k) = [gate(A_l, k) < gate(B_l, k)] (A_l = mover 2l,
B_l = mover 2l + 1); b_l = b_(l-1) if (s(A_l), s(B_l)) = (0, 1), not b_(l-1) if (1, 0), c_l(k) if both = k; a level-(l+1) mover's
key-preferred option is 0 iff b_l = 1; a degree-2 mover moves iff its other option is strictly Xi-better and key-preferred (keys of
the NEW state). Independent re-implementation, compared with flipdp.Ext.step on every state and both b (BITC violations).
(2) restart measurements (warm-start test, §3): for every start u and bit b: seg = length of the H_b run from u, e = its end state,
R = length of the H_(1-b) run from e (restart after a flip at the stuck state). Reports max R, max seg + R, T_0(G) = max over starts
and b of the flip-free run, whether some restart reaches T_0(G) (R = T0), and the warm-start inequality W1 «L_(1-b)(s) <= L_b(s) + C»
as the largest gap max_s (L_(1-b)(s) - L_b(s)).
Usage: bitchain.py genome.json ...   or   bitchain.py --random m count seed"""
import sys, os, json, itertools, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from flipdp import Ext

def bc_step(E, up, b0):
    G = E.G; m = max(G["lev"]); st = E.full(up, b0)
    C = {v: (1 - st[v]) if E.better(st, v) else st[v] for v in E.UP}  # Xi-better option (or current if none), OLD state
    new = dict((v, st[v]) for v in range(E.N)); b = b0
    for l in range(1, m + 1):
        kp = 0 if b == 1 else 1
        if os.environ.get("BC_NEG") and l == 2: kp = 1 - kp  # negative control: wrong carry at level 2
        for v in (2 * l, 2 * l + 1):
            if C[v] != st[v] and kp == C[v]: new[v] = C[v]
        a, bb = new[2 * l], new[2 * l + 1]
        if (a, bb) == (0, 1): b = b
        elif (a, bb) == (1, 0): b = 1 - b
        else: b = int(G["gate"][2 * l][a] < G["gate"][2 * l + 1][a])
    return tuple(new[v] for v in E.UP)

def run(E, u, b):
    n = 0
    while True:
        w = E.step(u, b)
        if w == u: return n, u
        u, n = w, n + 1

def analyse(G):
    E = Ext(G); states = list(itertools.product(*[range(len(E.opts[v])) for v in E.UP]))
    bitc = sum(1 for u in states for b in (0, 1) if bc_step(E, u, b) != E.step(u, b))
    L = {(u, b): run(E, u, b) for u in states for b in (0, 1)}
    T0 = max(L[k][0] for k in L)
    best = None; gapW1 = -10 ** 9
    for (u, b), (seg, e) in L.items():
        R = L[(e, 1 - b)][0]
        if best is None or (R, seg) > (best[0], best[1]): best = (R, seg, u, b)
        gapW1 = max(gapW1, L[(u, 1 - b)][0] - L[(u, b)][0])
    segR = max(L[(u, b)][0] + L[(L[(u, b)][1], 1 - b)][0] for (u, b) in L)
    return {"BITC": bitc, "T0": T0, "maxR": best[0], "segAtMaxR": best[1], "maxSegPlusR": segR, "W1gap": gapW1,
            "arg": (list(best[2]), best[3])}

if __name__ == "__main__":
    tot = 0
    if sys.argv[1] == "--random":
        sys.path.insert(0, HERE); from climb import rand_iso
        m, cnt, seed = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); rng = random.Random(seed); agg = {}
        done = 0
        while done < cnt:
            G = rand_iso(m + 1, rng)
            try: r = analyse(G)
            except AssertionError: continue
            done += 1; tot += r["BITC"]
            for k in ("T0", "maxR", "maxSegPlusR", "W1gap"): agg[k] = max(agg.get(k, -99), r[k])
        print("random m", m, "genomes", cnt, "BITC", tot, "max", agg)
    else:
        for p in sys.argv[1:]:
            r = analyse(json.load(open(p))); tot += r["BITC"]; print(os.path.basename(p), r)
    print("TOTAL BITC", tot); sys.exit(1 if tot else 0)
