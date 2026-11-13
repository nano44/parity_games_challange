#!/usr/bin/env python3
"""L-RED 69 R243: GREEDY SIGNAL SYNTHESIS on a ladder genome. Round r: over every candidate new mover y at level L (W-targets = the
two ORIGINAL level-(L-1) movers; Ξ-targets (u, v) over all movers incl. earlier additions or -1; own β's at the two lowest ranks with
parities p0, p1; gate order g0; start st) pick the one with the largest sw(y) (signal243's exact screen), ADD it to the genome
(ranks shifted), re-run the genome with r187 ideal.traj and check that the run of every earlier mover is unchanged and that y's sw equals
the screen's (exact: nothing points to y). Stops after R rounds or when sw(y) = 2^(j+1) - 1 (full; j = L - base). Writes the genome.
Usage: greedy243.py G.json L R OUT.json [BASE]   (BASE = the full block's base level, default 0)"""
import sys, os, json, itertools, copy, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(HERE, "..", "r187")]
import ideal
G = json.load(open(sys.argv[1])); G = G.get("genome", G); L, R, OUTF = int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
BASE = int(sys.argv[5]) if len(sys.argv) > 5 else 0; FULL = 2 ** (L - BASE + 1) - 1
P = [x for x in range(G["N"]) if G["lev"][x] == L - 1][:2]
def run(G):
    S, why = ideal.traj(G, cap=500000); return S
def screen(G, S):
    N, lev, opts, gate, br, bp = G["N"], G["lev"], G["opts"], G["gate"], G["br"], G["bp"]; T = len(S) - 1
    order = sorted(range(N), key=lambda v: (lev[v], v)); pr = lambda b: 4 + 2 * br[b] + bp[b]
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
    KA = [kap(s) for s in S]; CH = [chains(s) for s in S]; gmax = max(max(g) for g in gate); E = frozenset(); best = (-1, None)
    for u, v in itertools.product([-1] + list(range(N)), repeat=2):
        if u == v: continue
        sig = [cmp(CH[t][u] if u >= 0 else E, CH[t][v] if v >= 0 else E) for t in range(T + 1)]
        for p0, p1, g0, st in itertools.product((0, 1), repeat=4):
            tie = 1 if (p0, p1) == (0, 1) else (-1 if (p0, p1) == (1, 0) else 0); s = st; sw = 0
            for t in range(T):
                k0 = KA[t + 1][P[0]] + (gmax + 1 + g0,); k1 = KA[t + 1][P[1]] + (gmax + 2 - g0,); kp = 0 if k0 < k1 else 1
                if kp != s:
                    c = sig[t] or tie
                    if (c > 0 and kp == 0) or (c < 0 and kp == 1): s = kp; sw += 1
            if sw > best[0]: best = (sw, (u, v, p0, p1, g0, st))
    return best
def add(G, prm):
    u, v, p0, p1, g0, st = prm; G = copy.deepcopy(G); gmax = max(max(g) for g in G["gate"])
    G["br"] = [r + 2 for r in G["br"]]; b0 = len(G["br"]); G["br"] += [0, 1]; G["bp"] += [p0, p1]
    G["opts"].append([[P[0], u, b0], [P[1], v, b0 + 1]]); G["gate"].append([gmax + 1 + g0, gmax + 2 - g0]); G["lev"].append(L); G["start"].append(st); G["N"] += 1
    return G
S = run(G); log = []
for r in range(R):
    sw, prm = screen(G, S); H = add(G, prm); S2 = run(H); y = H["N"] - 1
    same = all(S2[t][:G["N"]] == S[t] for t in range(len(S))) and len(S2) == len(S)
    swy = sum(S2[t][y] != S2[t - 1][y] for t in range(1, len(S2)))
    print(f"GREEDY243 round {r}: added mover {y} level {L} Ξ-targets {prm[:2]} parities {prm[2:4]} g0 {prm[4]} start {prm[5]}: screen sw {sw}, re-run sw {swy}, earlier run unchanged {same} (full = {FULL})", flush=True)
    G, S = H, S2
    if swy >= FULL: break
json.dump(G, open(OUTF, "w")); print("GREEDY243 wrote", OUTF, hashlib.sha1(open(OUTF, "rb").read()).hexdigest())
