#!/usr/bin/env python3
"""L-NEW box 185: trace of one mover z on an L^R_d run (box150 Gen): per state t the position s_t(z), pi_t = Xi-preferred option of z
under s_t, c_t = c_l(s_t) (the key-preferred option, ALIGN (a)), the value difference D_t = v(z,0) - v(z,1), and which movers on the
chains of (z,0), (z,1) moved. Usage: trace.py genome.json start(bitstring) z"""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__)); P0 = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P0, "__name__": "lib"}; exec(open(P0).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
G = json.load(open(sys.argv[1])); g = Gen(G); st = tuple(int(c) for c in sys.argv[2]); z = int(sys.argv[3])
S, _ = g.run(st); T = len(S) - 1; l = G["lev"][z]
def cl(s):
    K = g.keys(s); return 0 if K[2 * l - 2] < K[2 * l - 1] else 1
print("z", z, "level", l, "xt", [G["opts"][z][k][1] for k in range(2)], "T", T)
for t in range(T + 1):
    s = S[t]; v0, v1 = g.face(s, z, 0), g.face(s, z, 1); pi = 0 if v0 > v1 else 1
    mv = [x for x in range(G["N"]) if t and S[t][x] != S[t - 1][x]]
    ch = [g.play(s, z, k) for k in range(2)]
    print("t %2d s %s pos %d pi %d c %s %s moved %s chain0 %s chain1 %s" % (t, "".join(map(str, s)), s[z], pi, cl(s) if l else "-",
          "MOVE" if t and S[t][z] != S[t-1][z] else "    ", mv, ch[0], ch[1]))
