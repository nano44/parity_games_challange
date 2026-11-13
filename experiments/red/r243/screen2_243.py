#!/usr/bin/env python3
"""L-RED 69 R243: TWO-MOVER SIGNAL SCREEN (exact). Fix a genome's run (r187 ideal.traj). Add an auxiliary mover z at level LZ (W-targets
= that level-(LZ-1) pair) with Ξ-targets (u, v), own β's at the two HIGHEST ranks ('high': z is a signal bit, a comparison against z's
chain is decided by z's own β) or the two LOWEST ('low': z is a Ξ-MUX: its chain is u's or v's chain by z's state), parities, gate
order, start; z is simulated exactly (nothing points to z except y). Then a target mover y at level L (W-targets the level-(L-1) pair)
with Ξ-targets (z, w) or (w, z), w any mover or -1, own β's lowest, parities, gate order, start; sw(y) computed for all y-choices at once
(numpy). Reports the best sw(y) per z-level and mode, and the best overall, against full = 2^(L - BASE + 1) - 1.
Usage: screen2_243.py G.json L LZLIST [BASE] [ZSAMPLE]   (ZSAMPLE: number of (u, v) pairs sampled per z-level/mode; 0 = all)"""
import sys, os, json, itertools, random, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(HERE, "..", "r187")]
import ideal
G = json.load(open(sys.argv[1])); G = G.get("genome", G); L = int(sys.argv[2]); LZS = [int(v) for v in sys.argv[3].split(",")]
BASE = int(sys.argv[4]) if len(sys.argv) > 4 else 0; ZS = int(sys.argv[5]) if len(sys.argv) > 5 else 0; FULL = 2 ** (L - BASE + 1) - 1
N, lev, opts, gate, br, bp = G["N"], G["lev"], G["opts"], G["gate"], G["br"], G["bp"]
S, why = ideal.traj(G); T = len(S) - 1; order = sorted(range(N), key=lambda v: (lev[v], v)); pr = lambda b: 4 + 2 * br[b] + bp[b]
gmax = max(max(g) for g in gate)
def kap(s):
    own = {}
    for x in order:
        o = opts[x][s[x]]; own[x] = (own[o[0]] if o[0] >= 0 else ()) + (gate[x][s[x]],)
    return own
def chains(s):
    C = {}
    def ch(u):
        if u in C: return C[u]
        b = opts[u][s[u]][2]; y = opts[u][s[u]][1]; C[u] = frozenset([b]) | (ch(y) if y >= 0 else frozenset()); return C[u]
    for u in range(N): ch(u)
    return C
def cmp(A, B):
    d = A ^ B
    if not d: return 0
    z = max(d, key=pr); return 1 if ((z in A) == (bp[z] == 0)) else -1
KA = [kap(s) for s in S]; CH = [chains(s) for s in S]; E = frozenset()
def kp_seq(Lv, g0):
    Pp = [x for x in range(N) if lev[x] == Lv - 1][:2]
    return np.array([0 if KA[t + 1][Pp[0]] + (gmax + 1 + g0,) < KA[t + 1][Pp[1]] + (gmax + 2 - g0,) else 1 for t in range(T)], dtype=np.int8)
KPY = {g0: kp_seq(L, g0) for g0 in (0, 1)}
CMPW = {}                                                     # cmp(C[a], C[w]) for movers a, w, per t (cached lazily)
def sim_scalar(kp, sig, tie, st):
    s = st; sw = 0; out = [s]
    for t in range(T):
        if kp[t] != s:
            c = sig[t] or tie
            if (c > 0 and kp[t] == 0) or (c < 0 and kp[t] == 1): s = int(kp[t]); sw += 1
        out.append(s)
    return sw, out
def y_best(sigmat):
    """sigmat: array (Wn, T) of cmp(chain(z), chain(w)) for z on option 0's side; y tries both sides, parities (ties), g0, start"""
    best = (-1, None)
    for side in (1, -1):
        sg = sigmat * side
        for tie in (0,):
            for g0 in (0, 1):
                kp = KPY[g0]
                for st in (0, 1):
                    s = np.full(sg.shape[0], st, dtype=np.int8); sw = np.zeros(sg.shape[0], dtype=np.int32)
                    for t in range(T):
                        c = sg[:, t].copy(); c[c == 0] = tie
                        mv = (kp[t] != s) & (((c > 0) & (kp[t] == 0)) | ((c < 0) & (kp[t] == 1)))
                        s = np.where(mv, kp[t], s); sw += mv
                    i = int(sw.argmax())
                    if sw[i] > best[0]: best = (int(sw[i]), (side, tie, g0, st, i))
    return best
t0 = time.time(); rng = random.Random(1); overall = (-1, None); Wl = [-1] + list(range(N))
CW = [[CH[t][w] if w >= 0 else E for t in range(T + 1)] for w in Wl]
for LZ in LZS:
    KPZ = {g0: kp_seq(LZ, g0) for g0 in (0, 1)}
    pairs = [(u, v) for u in Wl for v in Wl if u != v]
    if ZS: pairs = rng.sample(pairs, min(ZS, len(pairs)))
    for mode in ("low",):          # 'high' is degenerate: z's own β's then decide z's own comparison, so z switches at most once
        bestm = (-1, None)
        for (u, v) in pairs:
            for (pz0, pz1), gz, stz in itertools.product(((0, 1), (1, 0)), (0, 1), (0, 1)):
                if mode == "high": sigz = [cmp(CH[t][u] if u >= 0 else E, CH[t][v] if v >= 0 else E) for t in range(T)]
                else: sigz = [cmp(CH[t][u] if u >= 0 else E, CH[t][v] if v >= 0 else E) for t in range(T)]
                tiez = 1 if (pz0, pz1) == (0, 1) else (-1 if (pz0, pz1) == (1, 0) else 0)
                if mode == "high":   # z's own β's are the top ranks: z's comparison of its own options is decided by its own β's
                    sigz = [tiez * 0 + (1 if pz0 == 0 and pz1 == 1 else -1 if pz0 == 1 and pz1 == 0 else 0)] * T
                swz, sz = sim_scalar(KPZ[gz], sigz, tiez, stz)
                if swz == 0 and mode == "high": pass
                # z's chain per t, and y's signal against every w
                if mode == "high":
                    # comparison chain(z) vs chain(w): decided by z's current β (top rank): + if that β is even
                    par = [pz0, pz1]; row = np.array([[1 if par[sz[t]] == 0 else -1 for t in range(T)]], dtype=np.int8)
                    sigmat = np.repeat(row, len(Wl), axis=0)
                else:
                    sigmat = np.zeros((len(Wl), T), dtype=np.int8)
                    for t in range(T):
                        a = (u if sz[t] == 0 else v); A = CH[t][a] if a >= 0 else E
                        for j, w in enumerate(Wl):
                            sigmat[j, t] = cmp(A, CW[j][t])
                    # ties (equal chains): the only difference left is z's current own β (present on z's side only)
                    for t in range(T):
                        col = sigmat[:, t]; col[col == 0] = 1 if [pz0, pz1][sz[t]] == 0 else -1
                b = y_best(sigmat)
                if b[0] > bestm[0]: bestm = (b[0], dict(LZ=LZ, mode=mode, u=u, v=v, pz=(pz0, pz1), gz=gz, stz=stz, swz=swz, y=b[1], w=Wl[b[1][4]]))
                if mode == "high": break          # in 'high' mode z's run does not depend on (u, v) beyond its own β's: one (u, v) suffices
            if mode == "high": break
        print(f"SCREEN2 {os.path.basename(sys.argv[1])} L {L} z-level {LZ} mode {mode}: best sw(y) {bestm[0]} (full {FULL}) at {bestm[1]} | pairs {len(pairs)} | {time.time() - t0:.0f} s", flush=True)
        overall = max(overall, bestm, key=lambda q: q[0])
print(f"SCREEN2 BEST {os.path.basename(sys.argv[1])} L {L}: sw(y) {overall[0]} of {FULL} at {overall[1]}", flush=True)
ADDZ = os.environ.get("ADDZ")      # write G + the best z (own β's at the two lowest ranks) to this file, for an iterated screen
if ADDZ:
    import copy
    b = overall[1]; H = copy.deepcopy(G); Pz = [x for x in range(N) if lev[x] == b["LZ"] - 1][:2]
    H["br"] = [r + 2 for r in H["br"]]; b0 = len(H["br"]); H["br"] += [0, 1]; H["bp"] += list(b["pz"])
    H["opts"].append([[Pz[0], b["u"], b0], [Pz[1], b["v"], b0 + 1]]); H["gate"].append([gmax + 1 + b["gz"], gmax + 2 - b["gz"]])
    H["lev"].append(b["LZ"]); H["start"].append(b["stz"]); H["N"] += 1
    S2, _ = ideal.traj(H); zz = H["N"] - 1
    same = len(S2) == len(S) and all(S2[t][:N] == S[t] for t in range(len(S)))
    print(f"SCREEN2 ADDZ wrote {ADDZ}: z = mover {zz}, sw(z) {sum(S2[t][zz] != S2[t - 1][zz] for t in range(1, len(S2)))} (screen {b['swz']}), earlier run unchanged {same}", flush=True)
    json.dump(H, open(ADDZ, "w"))
