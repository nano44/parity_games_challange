#!/usr/bin/env python3
"""L-NEW box 165: per-mover moves(x) and key flips KF_x on real IDEAL runs (RESULTS R104 model; simulator box150/check.py Gen).
KP_s(x) := the option of x with the least key under the keys of s (R105 KEYFLIP); KF_x := #{t in [1, T] : KP_(s_t)(x) != KP_(s_(t-1))(x)}.
Positions: desc(x) = #movers reachable from x along Xi-edges of ANY option (strict Xi-descendants), anc(x) = #strict Xi-ancestors.
Prints per file: T, N, max degree, max moves, max KF, KEYFLIP check (moves <= 1 + KF at degree <= 2), and the profile
«max moves / max KF over movers with desc = j» for j = 0.. ; with -v the per-mover table.
Usage: permover.py [-v] file.json ..."""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]

def reach(G):
    N = G["N"]; adj = [set(o[1] for o in G["opts"][x] if o[1] >= 0) for x in range(N)]; R = []
    for x in range(N):
        seen, st = set(), list(adj[x])
        while st:
            y = st.pop()
            if y not in seen: seen.add(y); st.extend(adj[y])
        R.append(seen)
    return R

def kp(g, key, x):
    return min(range(len(g.opts[x])), key=lambda k: g.optkey(key, x, k))

def measure(G, start=None):
    g = Gen(G); S, _ = g.run(start if start is not None else G["start"]); N = g.N
    mv = [0] * N; kf = [0] * N
    prev = [kp(g, g.keys(S[0]), x) for x in range(N)]
    for t in range(1, len(S)):
        key = g.keys(S[t]); cur = [kp(g, key, x) for x in range(N)]
        for x in range(N):
            mv[x] += S[t][x] != S[t - 1][x]; kf[x] += cur[x] != prev[x]
        prev = cur
    R = reach(G); desc = [len(R[x]) for x in range(N)]; anc = [sum(x in R[y] for y in range(N)) for x in range(N)]
    return dict(T=len(S) - 1, mv=mv, kf=kf, desc=desc, anc=anc, lev=G["lev"], deg=max(len(o) for o in G["opts"]))

if __name__ == "__main__":
    v = "-v" in sys.argv; files = [f for f in sys.argv[1:] if f != "-v"]
    for f in files:
        try: G = json.load(open(f)); assert "N" in G and "opts" in G; r = measure(G)
        except Exception as e: continue
        N = G["N"]; bad = [x for x in range(N) if r["deg"] <= 2 and r["mv"][x] > 1 + r["kf"][x]]
        prof = {}
        for x in range(N):
            j = r["desc"][x]; a, b = prof.get(j, (0, 0)); prof[j] = (max(a, r["mv"][x]), max(b, r["kf"][x]))
        print("%-34s T %3d N %2d deg %d maxmv %2d maxkf %2d KEYFLIPviol %d | desc:mv/kf %s" % (os.path.basename(f)[:34], r["T"], N,
              r["deg"], max(r["mv"]), max(r["kf"]), len(bad), " ".join("%d:%d/%d" % (j, *prof[j]) for j in sorted(prof))), flush=True)
        if v:
            for x in sorted(range(N), key=lambda x: r["desc"][x]):
                print("   x %2d lev %d desc %2d anc %2d moves %2d KF %2d" % (x, r["lev"][x], r["desc"][x], r["anc"][x], r["mv"][x], r["kf"][x]))
