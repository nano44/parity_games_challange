#!/usr/bin/env python3
"""L-RED 64 R230 item 7 (stall / recursion after DEAD ODO-2SRC, docs/red/R230-odo.md): RING oscillator RING(k, m).
Two sources at level 1: hub h (X_1..X_k) and rival S (Y_1..Y_k). Two chains of m movers each:
  chain A (z_1..z_m): P_i toward h (z_1: wt h; z_i: wt z_(i-1)), Q_i via relays ra toward S          (domino toward h, reset to S)
  chain B (y_1..y_m): P'_i toward S (y_1: wt S; y_i: wt y_(i-1)), Q'_i via relays rb toward h        (domino toward S, reset to h)
Observers (the only upward Xi-edges, U = 2): u -> y_m (h's options X_2.. observe chain B's top), u2 -> z_m (S's options Y_1..
observe chain A's top). X_1 is un-gated (xt self), so h leads at the start. Every chain / relay option: even Xi self-loop.
Intended ring: A completes toward h -> S observes h through A (superset) and overtakes -> B runs toward S, A resets -> B completes
-> h observes S through B and overtakes -> ... ; target T3 ~ (#overtakes) * m with N + M = O(k + m).
e-order permuted (ekey): chain e's < sources' items (X_l, Y_l interleaved: X_l = 0.5 + 0.02 l, Y_l = 0.51 + 0.02 l) < e_u, e_u2;
within a chain e_Q > e_P (env QP=0 flips it). Usage: ring230.py K M  (env SAVE=path, EORD=lev to drop ekey)."""
import sys, os, json
from elev230 import measure, U
QP = os.environ.get("QP", "1") == "1"
def ring(k, m):
    lev = []; opts = []; nm = {}; keys = []; par = []; rank = []
    def mover(n, l): nm[n] = len(lev); lev.append(l); opts.append([])
    def opt(x, wt, xt, key, bpar, brk):
        opts[nm[x]].append([nm[wt] if wt else -1, (nm[x] if xt == "self" else nm[xt]) if xt else -1, 0]); keys.append((nm[x], key)); par.append(bpar); rank.append(brk)
    mover("g", 0); mover("h", 1); mover("S", 1); mover("u", 1); mover("u2", 1)
    for c in "zy":
        for i in range(1, m + 1): mover(f"{c}{i}", i + 1)
        for i in range(1, m): mover(f"r{c}{i}", i + 1)
    opt("g", None, None, 0.0, 1, 0)
    for l in range(1, k + 1): opt("h", "g", "self" if l == 1 else "u", 0.5 + 0.02 * l, 0, 100 - l)
    for l in range(1, k + 1): opt("S", "g", "u2", 0.51 + 0.02 * l, 0, 100 - l)
    opt("u", "g", f"y{m}", 0.99, 0, 1); opt("u2", "g", f"z{m}", 0.995, 0, 1)
    qa, pa = (0.02, 0.01) if QP else (0.01, 0.02)
    for c, home, away in (("z", "h", "S"), ("y", "S", "h")):
        for i in range(1, m + 1):
            opt(f"{c}{i}", home if i == 1 else f"{c}{i - 1}", "self", pa * 0.5 + 0.0005 * i, 0, 50)
            opt(f"{c}{i}", away if i == 1 else f"r{c}{i - 1}", "self", qa * 0.5 + 0.0005 * i, 0, 49)
        for i in range(1, m): opt(f"r{c}{i}", away if i == 1 else f"r{c}{i - 1}", "self", 0.0001 * i, 0, 10)
    N = len(lev); M = sum(map(len, opts)); i = 0; gate = []
    for x in range(N):
        gate.append([])
        for o in opts[x]: o[2] = i; gate[x].append(i); i += 1
    br = [0] * M
    for r, b in enumerate(sorted(range(M), key=lambda b: rank[b])): br[b] = r
    ek = [[0.0] * len(opts[x]) for x in range(N)]; cnt = {}
    for b, (x, key) in enumerate(keys): j = cnt.get(x, 0); ek[x][j] = key; cnt[x] = j + 1
    start = [0] * N
    for c in "zy":
        for i in range(1, m + 1): start[nm[f"{c}{i}"]] = 1          # chains start on Q (reset)
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": par, "start": start, "ekey": ek}, nm
if __name__ == "__main__":
    k, m = int(sys.argv[1]), int(sys.argv[2]); G, nm = ring(k, m)
    if os.environ.get("EORD") == "lev": G.pop("ekey")
    if os.environ.get("SAVE"): json.dump(G, open(os.environ["SAVE"], "w"))
    import ret230
    r = ret230.run(G); c = measure(G)
    print(f"RING k {k} m {m}: N {c['N']} M {c['M']} U {c['U']} inv {c['inv']} T3 {c['T3']} total {c['total']} fb {c['fb']} nstd {c['nstd']} returns {r['R']}", flush=True)
    if os.environ.get("TRACE"):
        seq = r["seq"]; z = [nm[f"z{i}"] for i in range(1, m + 1)]; y = [nm[f"y{i}"] for i in range(1, m + 1)]
        for t, s in enumerate(seq):
            print(t, "h", s[nm["h"]], "S", s[nm["S"]], "A", "".join("P" if s[v] == 0 else "Q" for v in z), "B", "".join("P" if s[v] == 0 else "Q" for v in y))
