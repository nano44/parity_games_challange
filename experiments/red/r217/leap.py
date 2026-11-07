#!/usr/bin/env python3
"""L-RED 54 R217: hand-built LEAPFROG gadget (d 2) in R104's genome format (IDEAL-CYC / box 191).
Parameters: k taps per side. Design (all plays end at u -> K0 -> K3 -> K2 -> K1, so Lambda = K1 throughout and every face flip is an
R-flip candidate):
- FUSE: level-0 movers c_0..c_{L-1}, L = 2k. c_i has option EXIT (beta odd-low -> u) [start] and CHAIN (beta odd-HIGH -> c_{i+1});
  c_{L-1}'s CHAIN goes to TOP (a level-1 self-loop bit whose forced escape e is the highest e). The improvement (TOP's e) travels
  back along the fuse one mover per step (PATH lemma), reaching c_i at step about L - i.
- TAPS: level-1 self-loop bits T_j (one option: gate with xt = T_j itself, beta even, so Odd must escape through e(T_j)), W-target the
  fuse mover c_{p_j}. Tap j's e has rank j. Taps alternate sides in activation order: activation order = decreasing fuse position.
- Y (level 0): options -> taps of side Y (beta -> T_j).  X' (level 0): options -> taps of side X.
- Z (level 1): one option, gate g: W-target Y, Xi-target X'; e_g is the lowest level-1 e. g is the measured gate.
Usage: leap.py k [out.json]"""
import sys, json
def build(k):
    L = 2 * k; movers = []; lev = []; opts = []
    def mv(level):
        movers.append(len(movers)); lev.append(level); opts.append([]); return movers[-1]
    c = [mv(0) for _ in range(L)]
    TOP = mv(1)
    T = [mv(1) for _ in range(2 * k)]          # tap j activates j-th (j = 0 first)
    Y = mv(0); X = mv(0); Z = mv(1)
    betas = []                                   # (owner-option, rank-key, parity)
    gates = {}                                   # (x,k) -> gate key for e order within level
    def opt(x, wt, xt, bkey, par, gkey=0):
        b = len(betas); betas.append((bkey, par)); opts[x].append([wt, xt, b]); gates[(x, len(opts[x]) - 1)] = gkey
    # fuse
    for i in range(L):
        opt(c[i], -1, -1, ("exit", i), 1)                                 # EXIT: odd, low
        opt(c[i], -1, c[i + 1] if i + 1 < L else TOP, ("chain", i), 1)    # CHAIN: odd, high
    opt(TOP, c[0] if False else -2, TOP, ("bit", -1), 0, gkey=10 ** 6)   # placeholder wt fixed below
    opts[TOP][0][0] = None
    # tap j sits at fuse position p_j = L - 1 - j (activated j-th); its e rank = j
    for j in range(2 * k):
        opt(T[j], None, T[j], ("bit", j), 0, gkey=1000 + j)
        opts[T[j]][0][0] = c[L - 1 - j]
    # TOP's escape: a level-0 sink mover s that goes to u
    s = mv(0); opt(s, -1, -1, ("sink", 0), 1)
    opts[TOP][0][0] = s
    for j in range(2 * k):
        side = Y if j % 2 == 0 else X
        opt(side, -1, T[j], ("tap", j), 0)
    opt(Z, Y, X, ("g", 0), 0, gkey=0)
    N = len(movers)
    # beta ranks: exit < tap < sink < bit < chain  (chain odd and highest: an inactive CHAIN is worse than EXIT)
    order = {"exit": 0, "tap": 1, "sink": 2, "g": 3, "bit": 4, "chain": 5}
    idx = sorted(range(len(betas)), key=lambda b: (order[betas[b][0][0]], betas[b][0][1]))
    br = [0] * len(betas)
    for r, b in enumerate(idx): br[b] = r
    bp = [betas[b][1] for b in range(len(betas))]
    gate = [[0] * len(opts[x]) for x in range(N)]
    allq = sorted(((x, kk) for x in range(N) for kk in range(len(opts[x]))), key=lambda q: (gates[q], q))
    for i, q in enumerate(allq): gate[q[0]][q[1]] = i
    start = [0] * N
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": bp, "start": start}, dict(Z=Z, Y=Y, X=X, c=c, T=T, TOP=TOP)
if __name__ == "__main__":
    G, info = build(int(sys.argv[1]))
    s = json.dumps(G)
    if len(sys.argv) > 2: open(sys.argv[2], "w").write(s + "\n")
    else: print(s)
    print("Z", info["Z"], "Y", info["Y"], "X", info["X"], file=sys.stderr)
