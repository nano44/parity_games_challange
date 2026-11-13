#!/usr/bin/env python3
"""L-SI box 104: FREE genomes. A free genome is an R104 genome whose beta- and e-vertices carry ARBITRARY distinct priorities in
[6, top) of either parity (R104's [DEF] has every e even and above every beta: E-DOM). Gamma3*(G) is L-NEW's box189 gamma3.build(G,
all four pad kinds) with those priorities; c_W = top, K0 = top + 2, K3 = top + 3 are re-computed above them; K1 5, K2 3, c_X 2, pads,
movers and gates are unchanged.
F_n := Gamma3* of L-RED 54's comp.py genome of PGSolver's switchallexp_n (Friedmann's G_n, arXiv 0901.2731), every carrier ranked by
the ORIGINAL priority it carries (beta: its key; e of a CycleCenter gate: pr(CycleLeaver), own parity; all other e's lowest, even).
Engines (read-only archives, see run104.sh): env LNEW = claude/l-new fcba92fc (experiments/new, experiments/si/si.py,
experiments/harness, experiments/hard-families, experiments/n5-second); env LRED = claude/l-red 8c01d40e (experiments/red/r217).
Usage: free104.py run MODE ALG n...      MODE free|edom, ALG xi|spec: one line per n (engine 1 = box190 n5v.py from S3)
       free104.py pg n OUT.pg            write F_n
       free104.py prio n                 priority facts of F_n (E-DOM violations)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); LNEW = os.environ["LNEW"]; LRED = os.environ["LRED"]
os.environ["WTT"] = LNEW; os.environ["WT3"] = LNEW
sys.path[:0] = [HERE, os.path.join(LRED, "experiments/red/r217")] + [os.path.join(LNEW, p) for p in (
    "experiments/new/box190", "experiments/new/box189", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
import gdsl
KEYS = {}
_orig = gdsl.Gen.genome
def _genome(s, start=None):
    """gdsl.Gen.genome, also recording each option's beta key and gate key (flat option order)."""
    G, ix = _orig(s, start); bk = []; gk = []
    for x in s.names:
        for (wt, xt, b, par, g) in s.opts[x]: bk.append(b); gk.append(g)
    KEYS["bk"] = bk; KEYS["gk"] = gk; return G, ix
gdsl.Gen.genome = _genome
import comp, fried, pg, n5v, gamma3
PADS = {"K", "pe", "pb", "m"}

def options(G): return [(x, k) for x in range(G["N"]) for k in range(len(G["opts"][x]))]

def build_free(G, pb, pe):
    """Gamma3*(G): pb[q], pe[q] = the priorities of beta_q and e_q (distinct integers >= 6). Returns (game, sigma0, tau0, V)."""
    gm, sig, tau, V = gamma3.build(G, PADS); prio = list(gm.prio); O = options(G)
    vals = [pb[q] for q in O] + [pe[q] for q in O]
    assert len(set(vals)) == len(vals) and min(vals) >= 6, "carrier priorities must be distinct and >= 6"
    for q in O: prio[V[("b", q)]] = pb[q]; prio[V[("e", q)]] = pe[q]
    top = max(vals) + 2; top += top % 2
    K0, K1, K2, K3 = (V[("K", i)] for i in range(4))
    prio[V["cW"]] = top; prio[K0], prio[K1], prio[K2], prio[K3] = top + 2, 5, 3, top + 3
    assert all(prio[v] <= 2 for kk, v in V.items() if not (isinstance(kk, tuple) and kk[0] in ("b", "e", "K")) and kk != "cW")
    return pg.Game(prio, list(gm.owner), [list(s) for s in gm.succ]), sig, tau, V

def friedmann_prios(G, bk, gk):
    """one common order of the 2M carriers by the original priority they carry; priorities 6, 7, ... with the carrier's own parity."""
    car = []
    for q in options(G):
        b = G["opts"][q[0]][q[1]][2]; k = bk[b]; g = gk[b]
        car.append(((k[0], 1, k[1] if isinstance(k[1], int) else 0, q), "b", q, G["bp"][b]))
        real = len(g) == 2 and g[0] > 0
        car.append(((g[0] if real else -2, 0, g[1] if real else 0, q), "e", q, (g[0] % 2) if real else 0))
    car.sort(key=lambda c: c[0]); pb = {}; pe = {}; p = 5
    for (_, kind, q, par) in car:
        p += 1
        if p % 2 != par: p += 1
        (pb if kind == "b" else pe)[q] = p
    return pb, pe

def F(n, mode="free"):
    """(game, sigma0, tau0, V, G, ix) for Friedmann's switchallexp_n; mode edom = R104's priorities (the genome game Gamma3(G))."""
    G, ix = comp.compile_(n)
    if mode == "edom": g, sig, tau, V = gamma3.build(G, PADS)
    else: g, sig, tau, V = build_free(G, *friedmann_prios(G, KEYS["bk"], KEYS["gk"]))
    return g, sig, tau, V, G, ix

def prio_facts(g, V, G):
    O = options(G); pb = [g.prio[V[("b", q)]] for q in O]; pe = [g.prio[V[("e", q)]] for q in O]
    below = sum(1 for e in pe if any(e < b for b in pb)); odd_e = sum(1 for e in pe if e % 2)
    odd_b_above = sum(1 for b in pb if b % 2 and any(b > e for e in pe))
    return below, odd_e, odd_b_above, min(pb + pe), max(pb + pe), g.prio[V["cW"]]

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "run":
        mode, alg = sys.argv[2], sys.argv[3]
        for n in map(int, sys.argv[4:]):
            Vf = fried.game(n); T, _ = fried.howard(Vf); g, sig, tau, V, G, ix = F(n, mode)
            states, fb, E = n5v.run(g, alg, None, cap=10 ** 6); s0 = states[0]
            std = all(s0[0][v] == sig[v] for v in sig) and all(s0[1][v] == tau[v] for v in tau)
            win, _ = n5v.solution(g, states, E)
            print(f"F104 n {n} mode {mode} alg {alg}: |G_n| {len(Vf)} Howard T {T} | N {G['N']} M {len(options(G))} |V| {g.n} m {sum(len(s) for s in g.succ)} "
                  f"maxprio {max(g.prio)} | iterations {len(states) - 1} fallbacks {fb} | iterations - T = {len(states) - 1 - T} | S3 = standard start {std} | "
                  f"Even wins {win.count(0)}/{g.n}", flush=True)
    elif cmd == "pg":
        g = F(int(sys.argv[2]))[0]; pg.write(g, sys.argv[3])
    elif cmd == "prio":
        for n in map(int, sys.argv[2:]):
            for mode in ("free", "edom"):
                g, sig, tau, V, G, ix = F(n, mode); f = prio_facts(g, V, G)
                print(f"PRIO104 n {n} mode {mode}: e-vertices below some beta {f[0]} of {len(options(G))}; odd e {f[1]}; odd betas above some e {f[2]}; "
                      f"carrier priorities {f[3]}..{f[4]}; c_W {f[5]}", flush=True)
