#!/usr/bin/env python3
"""L-COMP box 47: table of the search lanes (out/lanes/<LANE>.state of search47): iterations, the lane's best (score decoded: k_A6,
kfront = the largest sw of a level-k mover, T) and its size; the best genome is written to out/lanes/<LANE>_cur_best.txt / .json (gen47 text
/ JSON), and its k_A6 / khalf / T are RE-MEASURED by the C port (bin/one47 + a Python count of sw and |K| on its key states).
Usage: lanes47.py [LANE ...]  (default: every *.state)"""
import sys, os, glob, json, subprocess
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H); import gen47
def kk(G, S):
    N, lev = G["N"], G["lev"]; T = len(S) - 1; sw = [sum(1 for t in range(T) if S[t + 1][x] != S[t][x]) for x in range(N)]; P = [0] * N
    for l in range(max(lev) + 1):
        for x in range(N):
            if lev[x] == l: P[x] = sum(1 if l == 0 else P[o[0]] for o in G["opts"][x])
    k = max([lev[x] + 1 for x in range(N) if sw[x] == P[x] - 1], default=0)
    kh = max([lev[x] for x in range(N) if P[x] >= 2 and sw[x] >= P[x] // 2 - 1], default=-1)
    kf = max([sw[x] for x in range(N) if lev[x] == k], default=0)
    return T, k, kh, kf
lanes = sys.argv[1:] or sorted(os.path.basename(p)[:-6] for p in glob.glob(os.path.join(H, "out", "lanes", "*.state")))
print("| lane | iters | best k_A6 | kfront | T (score) | re-measured T / k_A6 / khalf / kfront | d | N | N + M |")
print("| --- | --- | --- | --- | --- | --- | --- | --- | --- |")
for L in lanes:
    st = open(os.path.join(H, "out", "lanes", L + ".state")).read().split("\n"); it, rs, tc, tb = st[0].split()
    w = " ".join(st[1:]).split(); N0, M0 = int(w[0]), int(w[1]); n0 = 2 + N0 + 7 * M0 + N0; best = " ".join(w[n0:])
    tb = int(tb); log = os.path.join(H, "out", "lanes", L + ".log"); l0 = open(log).readline(); kmode = "SCORE K" in l0; kd = "SCORE KD" in l0
    k, f, t = (tb >> 40, (tb >> 20) & ((1 << 20) - 1), tb & ((1 << 20) - 1)) if kmode else (-1, -1, tb)
    if kd: f = "%d (deficit)" % (f - (1 << 19))
    bt = os.path.join(H, "out", "lanes", L + "_cur_best.txt"); open(bt, "w").write(best + "\n"); G = gen47.t2j(best)
    json.dump(G, open(bt[:-4] + ".json", "w"), sort_keys=True)
    o = subprocess.run([os.path.join(H, "bin", "one47"), bt, "key", "--states"], capture_output=True, text=True).stdout
    S = [tuple(map(int, l.split()[3:])) for l in o.splitlines() if l.startswith("S ")]; T2, k2, kh2, kf2 = kk(G, S)
    print("| %s | %s | %s | %s | %d | %d / %d / %d / %d | %d | %d | %d |" % (L, it, k if kmode else "—", f if kmode else "—", t, T2, k2, kh2, kf2, max(G["lev"]) + 1, G["N"], G["N"] + sum(len(o) for o in G["opts"])))
