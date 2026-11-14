#!/usr/bin/env python3
"""L-RED R187 STAB: a fastcyc IDEAL genome (R178 format) -> a REAL parity game whose gates are stabilised:
  mover x_v (Even, prio 0) -> its gates; gate (v,k) (Odd, prio 1) -> {e_(v,k), beta_(v,k)};
  W-face: e_(v,k) (Even, EVEN priority above every beta, rank rising with the owner's level) -> PAD vertices (Even, prio 0) -> W-target
          (mover of level - 1, or c_W = top even self-loop);
  Xi-face: beta_(v,k) (Even, prio 4 + 2 br + bp) -> X-target (mover, or c_X = even self-loop prio 2).
Indices: movers 0..N-1, gates N + gate[v][k], betas, then e/pads allocated in gate-index order, c_X, c_W.
START: sigma = genome start at movers, the single edge elsewhere; tau = W-face (e) at every gate.
run(G, pad) returns (game, start dict, gates, e-of-gate, beta-of-gate). Usage: stab.py genome.json PAD out_prefix"""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r170"), os.path.join(H, "..", "..", "new", "box21"), os.path.join(H, "..", "r183")]
from n5x import load
import pg

def build(G, pad=0, epar=0, kgad=False, esc=False):
    N, lev, opts, gate, br, bp = G["N"], G["lev"], G["opts"], G["gate"], G["br"], G["bp"]
    M = sum(len(o) for o in opts)
    gv = {(v, k): N + gate[v][k] for v in range(N) for k in range(len(opts[v]))}
    bv = {}; nxt = N + M
    for v in range(N):
        for k in range(len(opts[v])): bv[(v, k)] = nxt; nxt += 1
    padk = pad if isinstance(pad, (list, tuple)) else [pad] * (max(lev) + 2)
    ev, chain = {}, {}
    for (v, k) in sorted(gv, key=lambda q: gv[q]):
        ev[(v, k)] = nxt; nxt += 1; chain[(v, k)] = list(range(nxt, nxt + padk[lev[v]])); nxt += padk[lev[v]]
    cX = nxt; cW = nxt + 1; n = nxt + 2
    if kgad: K = list(range(n, n + 4)); n += 4
    prio = [0] * n; own = [0] * n; succ = [None] * n
    bb = 6 if kgad else 4
    bmax = max(bb + 2 * br[b] + bp[b] for b in range(len(br)))
    erank = sorted(gv, key=lambda q: (lev[q[0]], gv[q]))
    eb = bmax + 1 + (bmax + 1) % 2
    for i, q in enumerate(erank): prio[ev[q]] = eb + 2 * i + epar
    for v in range(N): succ[v] = sorted(gv[(v, k)] for k in range(len(opts[v])))
    for (v, k), g in gv.items():
        wt, xt, b = opts[v][k]
        prio[g] = 1; own[g] = 1; succ[g] = sorted([ev[(v, k)], bv[(v, k)]])
        prio[bv[(v, k)]] = bb + 2 * br[b] + bp[b]; succ[bv[(v, k)]] = [(K[0] if kgad else cX) if xt < 0 else xt] if not (esc and kgad and xt >= 0) else sorted([xt, K[0]])
        path = [ev[(v, k)]] + chain[(v, k)] + [cW if wt < 0 else wt]
        for a, c in zip(path, path[1:]): succ[a] = [c]
    prio[cX] = 2; succ[cX] = [cX]
    top = max(prio) + 2; top += top % 2; prio[cW] = top; succ[cW] = [cW]
    if kgad:   # FINDK gadget (findk.py 4 3000 1): prio [4,3,1,5] own [E,E,O,E] succ 0->{1,3} 1->{0,1} 2->{1,2} 3->{1,2}; stuck at
               # sigma (0->3, 1->1, 3->2), tau (2->2); u = K0: Xi_sigma cycle node K1 (odd, low band), Xi_tau cycle node K0 (even, above c_W)
        a, b_, c, d = K
        prio[c] = 3; prio[b_] = 5; prio[a] = top + 2; prio[d] = top + 3; own[c] = 1
        succ[a] = [b_, d]; succ[b_] = [a, b_]; succ[c] = [b_, c]; succ[d] = [b_, c]
    g = pg.Game(prio, own, succ)
    sig = {v: succ[v][0] for v in range(n) if own[v] == 0}
    for (v, k), b in bv.items():
        if opts[v][k][1] >= 0: sig[b] = opts[v][k][1]
    if kgad: sig[K[0]] = K[3]; sig[K[1]] = K[1]; sig[K[3]] = K[2]
    for v in range(N): sig[v] = gv[(v, G["start"][v])]
    tau = {gv[q]: ev[q] for q in gv}
    if kgad: tau[K[2]] = K[2]
    return g, sig, tau, gv, ev, bv

def write(g, sig, tau, pre):
    with open(pre + ".pg", "w") as f:
        f.write(f"parity {g.n - 1};\n")
        for v in range(g.n): f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")
    with open(pre + ".start", "w") as f:
        f.write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in sorted(sig.items())) + "\n")
        f.write("TAU0 " + " ".join(f"{v}:{w}" for v, w in sorted(tau.items())) + "\n")

if __name__ == "__main__":
    G = json.load(open(sys.argv[1])); g, sig, tau, *_ = build(G, int(sys.argv[2]), kgad=os.environ.get("KGAD", "1") == "1", esc=os.environ.get("ESC", "1") == "1"); write(g, sig, tau, sys.argv[3]); print("n", g.n)
