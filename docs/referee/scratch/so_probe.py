#!/usr/bin/env python3
"""REFEREE probe for P-N5-SO (pin 1ef02bb): per phase (lambda_Xi, tau) on C^1O with lambda(o) != o: Theta (theta-changes), S_o (relevant
sigmabar(o) changes), TH bound, SO bound, "at a relevant change with theta fixed the old choice leaves T", sigmabar(o) a full minimiser.
Usage: so_probe.py game.pg ... | so_probe.py rand N nmin nmax seed"""
import sys, os, random, glob
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u1_probe as U

def run(g, cnt):
    o = U.assert_c1o(g); E, Ed, out, it, fb = U.trace(g); n = g.n; do = len(set(g.succ[o]))
    st = []
    for (s, t, f, Is, a) in out:
        Xi, sb = E.evaluate(s); R = frozenset(v for v in range(n) if U.reaches(U.nxt_of(g, s, t), v, o))
        st.append(dict(Xi=Xi, sb=sb[o], R=R, ph=(tuple(x[0] for x in Xi), t)))
    i = 0
    while i < len(st):
        j = i
        while j + 1 < len(st) and st[j + 1]["ph"] == st[i]["ph"]: j += 1
        P = st[i:j + 1]; i = j + 1
        if len(P) < 2 or P[0]["Xi"][o][0] == o: continue
        cnt["phases"] += 1
        for r in P:
            mn = min(E.key(r["Xi"][x]) for x in g.succ[o])
            if E.key(r["Xi"][r["sb"]]) != mn: cnt["MIN_FAIL"] += 1
        Th = sum(P[k]["Xi"][o] != P[k + 1]["Xi"][o] for k in range(len(P) - 1))
        X = sum(P[k]["R"] != P[k + 1]["R"] for k in range(len(P) - 1))
        So = sum(P[k]["sb"] != P[k + 1]["sb"] for k in range(len(P) - 1))
        for k in range(len(P) - 1):
            a, b = P[k], P[k + 1]
            if a["sb"] != b["sb"] and a["Xi"][o] == b["Xi"][o]:
                cnt["SO_fixed_theta_changes"] += 1
                if E.key(b["Xi"][a["sb"]]) == min(E.key(b["Xi"][x]) for x in g.succ[o]): cnt["SO_old_stays_FAIL"] += 1
        if Th > (n - 1) + n * (X + 1) + X: cnt["TH_FAIL"] += 1
        if So > Th + (do - 1) * (Th + 1): cnt["SO_FAIL"] += 1
        cnt["max_So"] = max(cnt["max_So"], So); cnt["max_Th"] = max(cnt["max_Th"], Th)

if __name__ == "__main__":
    a = sys.argv[1:]; cnt = Counter()
    if a[0] == "rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for _ in range(N):
            g = U.rand_c1o(rng, lo, hi)
            if g is not None: run(g, cnt)
    elif a[0] == "lib":
        for p in sorted(glob.glob("experiments/**/*.pg", recursive=True)):
            try: g = U.load(p)
            except Exception: continue
            if sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1) != 1 or g.n > 64: continue
            c = Counter(); run(g, c); cnt["files"] += 1
            if any("FAIL" in k for k in c): print(p, dict(c))
            for k, v in c.items(): cnt[k] = max(cnt[k], v) if "max" in k else cnt[k] + v
    print(dict(sorted(cnt.items())))
