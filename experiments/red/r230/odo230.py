#!/usr/bin/env python3
"""L-RED 64 R230 item 6: HAND-BUILT ODOMETER attempt ODO(k, m) against L-SI 50 BOX 98 CONJECTURE U-FREE (T3 <= N + M + 4).
Design (U(G) = 2; e-priorities PERMUTED by "ekey", i.e. [E-LEV] violated unless EORD=lev):
  g       level 0, one option (wt -1, xt -1): value = escape (E = {})                         ground
  h       level 1 HUB, options X_1..X_k: wt g, xt u   (b-face observes the domino's top through u)
  S       level 1 RIVAL, options Y_1..Y_k: wt g, xt u2
  u, u2   level 1, one option each: wt g, xt z_m (the two UPWARD Xi-edges: U = 2); e_u most relevant, so V(u) = b-face
  z_1     level 2, options H (wt h) and Q_1 (wt S); z_i (i >= 2, level i + 1): P_i (wt z_(i-1)) and Q_i (wt rho_(i-1))
  rho_i   level i + 1 relays toward S (rho_1: wt S), one option
  every z / rho option: xt = itself with an EVEN beta (Odd then takes the e-face; a non-current option is improving iff its a-face
  beats the current value, and Howard picks among improving options by beta rank).
  item order (ekey, low = less relevant): chain e's < X_1 < Y_1 < X_2 < Y_2 < ... < X_k < Y_k < e_u, e_u2.
Intended run: rounds j = 1..k, each a domino of m switches toward h then a 1-step knock-off toward S: T3 ~ k*m with N + M = O(k + m).
Env YLOW=1: rival items below the hub's (0.3 + 0.02 l). DOM=1: see DOM below.
Prints T3, total, the hub's and rival's option sequences, and per-iteration #switches. Usage: odo230.py K M [EORD=lev]"""
import sys, os, json
from elev230 import measure, U
DOM = os.environ.get("DOM") == "1"     # variant: X_1 un-gated (xt self) and chain order e_Q > e_P (domino test)
def odo(k, m):
    lev = []; opts = []; nm = {}
    def mover(name, l): nm[name] = len(lev); lev.append(l); opts.append([])
    mover("g", 0); mover("h", 1); mover("S", 1); mover("u", 1); mover("u2", 1)
    for i in range(1, m + 1): mover(f"z{i}", i + 1)
    for i in range(1, m): mover(f"r{i}", i + 1)
    keys = []; even = []; rank = []
    def opt(x, wt, xt, key, bpar, brk):
        opts[nm[x]].append([nm[wt] if wt else -1, (nm[xt] if xt != "self" else nm[x]) if xt else -1, 0]); keys.append((nm[x], key)); even.append(bpar); rank.append(brk)
    opt("g", None, None, 0.0, 1, 0)
    for l in range(1, k + 1): opt("h", "g", "self" if DOM and l == 1 else "u", 0.5 + 0.02 * l, 0, 100 - l)        # beta rank: X_(j+1) beats X_(j+2) ...
    for l in range(1, k + 1): opt("S", "g", "u2", (0.3 if os.environ.get("YLOW") else 0.51) + 0.02 * l, 0, 100 - l)
    opt("u", "g", f"z{m}", 0.99, 0, 1); opt("u2", "g", f"z{m}", 0.995, 0, 1)
    opt("z1", "h", "self", 0.01, 0, 50); opt("z1", "S", "self", 0.02 if DOM else 0.005, 0, 49)
    for i in range(2, m + 1):
        opt(f"z{i}", f"z{i - 1}", "self", 0.01 + 0.001 * i, 0, 50); opt(f"z{i}", f"r{i - 1}", "self", (0.02 if DOM else 0.005) + 0.001 * i, 0, 49)
    for i in range(1, m): opt(f"r{i}", "S" if i == 1 else f"r{i - 1}", "self", 0.001 * i, 0, 10)
    N = len(lev); M = sum(map(len, opts)); i = 0; gate = []
    for x in range(N):
        gate.append([])
        for o in opts[x]: o[2] = i; gate[x].append(i); i += 1
    order = sorted(range(M), key=lambda b: rank[b]); br = [0] * M
    for r, b in enumerate(order): br[b] = r
    ek = [[0.0] * len(opts[x]) for x in range(N)]; c = {}
    for b, (x, key) in enumerate(keys): j = c.get(x, 0); ek[x][j] = key; c[x] = j + 1
    start = [len(opts[x]) - 1 if x >= nm["z1"] and x < nm["z1"] + m else 0 for x in range(N)]   # z's start on Q (knocked off)
    G = {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": list(even), "start": start, "ekey": ek}
    return G, nm
if __name__ == "__main__":
    k, m = int(sys.argv[1]), int(sys.argv[2]); G, nm = odo(k, m)
    if len(sys.argv) > 3 and sys.argv[3] == "EORD=lev": G.pop("ekey")
    import ret230
    r = ret230.run(G); c = measure(G)
    print(f"ODO k {k} m {m}: N {c['N']} M {c['M']} U {c['U']} inv {c['inv']} T3 {c['T3']} total {c['total']} fb {c['fb']} nstd {c['nstd']} returns {r['R']}")
    seq = r["seq"]; h, S = nm["h"], nm["S"]; zs = [nm[f"z{i}"] for i in range(1, m + 1)]
    for t, s in enumerate(seq):
        sw = sum(1 for x in range(G["N"]) if t and s[x] != seq[t - 1][x])
        print(t, "h", s[h], "S", s[S], "z", "".join("P" if s[z] == 0 else "Q" for z in zs), "switches", sw)
    json.dump(G, open(os.environ.get("SAVE", "/dev/null"), "w"))
