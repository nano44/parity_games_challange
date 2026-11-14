#!/usr/bin/env python3
"""Box 206 Addendum E (L-NEW successor 71): own-engine check of L-RED 65's corrected CWR obstruction (claude/l-red 2c5e558b,
docs/red/R231-cwr.md §2). For a carry genome (CW / CWR, carry206.py) and a high bit qh_K (default K = 3), per state t of the
IDEAL-CYC run: c_K's chosen Xi-target, Q's and R's gate faces (e/b), Lambda (vertex, priority) of R, Q, qh_K, c_K, the values of
qh_K's two faces (Lambda priority, |E|), and CLOSE := 1 iff the play from e_qh_K, with qh_K's gate forced to its e-face and every
other vertex on the state's strategy pair, returns to e_qh_K (Addendum D's claimed cycle). Totals: closed (unit: states; must be
read, not must-0), raceTop (states at which Lambda(R) is the beta vertex of R's chosen option with even priority).
Usage: ediag206.py G.json NAMES.json [K]   (NAMES = the MWR names file the genome was built from)"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(HERE, "..", "box203"), os.path.join(HERE, "..", "box191")]
import gfc203, idealcyc
G = json.load(open(sys.argv[1])); nm = json.load(open(sys.argv[2])); K = int(sys.argv[3]) if len(sys.argv) > 3 else 3
H, n, E, V, gates = gfc203.hist_ideal(G); ST = idealcyc.run(G); h, s0, movers, inv = idealcyc.build(G)
N0 = max(nm.values()) + 1; qhK = nm["qh%d" % K]; cK = N0 + K - 1; R, Q = nm["R"], nm["Q"]
prio = h.prio
def succ_at(t):
    s = list(s0)
    for x in range(G["N"]): s[movers[x]] = V[("g", (x, ST[t][x]))]
    sb = H[t][1]
    return lambda v: (s[v] if h.owner[v] == 0 else sb[v])
def lam(t, v): return H[t][0][v][0]
def nE(t, v):
    m = H[t][0][v][1]; return sum(1 for k, w in V.items() if isinstance(k, tuple) and k[0] == "e" and (m >> E.rank[w]) & 1)
def face(t, x):
    g = V[("g", (x, ST[t][x]))]; return "e" if H[t][1][g] == V[("e", (x, ST[t][x]))] else "b"
closed = 0; racetop = 0
print("genome", os.path.basename(sys.argv[1]), "qh%d" % K, "=", qhK, "c%d" % K, "=", cK, "R", R, "Q", Q, "T", len(H) - 1)
for t in range(len(H)):
    f = succ_at(t); q = (qhK, ST[t][qhK]); ev = V[("e", q)]; bv = V[("b", q)]
    seen = set(); v = ev; ok = 0
    while True:
        v = f(v)
        if v == ev: ok = 1; break
        if v in seen: break
        seen.add(v)
    closed += ok
    lr = lam(t, R); bR = V[("b", (R, ST[t][R]))]
    rt = int(lr == bR and prio[lr] % 2 == 0); racetop += rt
    cx = G["opts"][cK][ST[t][cK]][1] if cK < G["N"] else None
    print(t, "c%d->%s" % (K, cx), "Qface", face(t, Q), "Rface", face(t, R),
          "Lam R/Q/qh/c", "/".join("%d:%d" % (lam(t, w), prio[lam(t, w)]) for w in (V[("x", R)], V[("x", Q)], V[("x", qhK)], V[("x", cK)])),
          "| qh faces e(%d,%d) b(%d,%d)" % (prio[lam(t, ev)], nE(t, ev), prio[lam(t, bv)], nE(t, bv)), "qhface", face(t, qhK), "CLOSE", ok, "raceTop", rt)
print("TOTALS closed", closed, "raceTop", racetop, "states", len(H))
