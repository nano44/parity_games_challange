#!/usr/bin/env python3
"""L-RED 66 R234 item 3: CONJECTURE DEEP3 (L-SI 51 box 100 §5.2) measured exactly as WINDOW uses it. Engine: r232/how3_232 (env LNEW).
For every SCC C of D(G) with t0(C) = max f over SCCs reachable from C (box 99 §2): internal gates = gates (x, k), x in C, whose W- and
Xi-targets are both movers of C; a flip at step t -> t+1 with t >= t0(C) is charged (TWO-CROSS) to the change of the face Odd leaves;
depth as box 100 §3 (-1 Lambda; Pi: #Pi_t elements above z; length-only: |Pi_t|).
Per instance: deepC = sum over SCCs of Deep_c(C) (internal, after t0, depth > c); deepC_max = max over SCCs; intC = internal flips
after t0; allgates deep = cross100's convention (every gate, whole run, depth > c) for reproduction; dmaxC; and the per-gate profile of
the gate with most deep internal flips (gate, flips, deep). CMAX = c (default 3).  Usage: deep234.py G.json ... | deep234.py rand SEED COUNT"""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r232"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r221q"))
import how3_232 as H, own
c = int(os.environ.get("CMAX", "3"))
def depth(A, B, rk):
    if A[0] != B[0]: return -1
    D = A[1] ^ B[1]
    if not D: return len(A[1])
    z = max(D, key=lambda u: rk[u]); return sum(1 for u in A[1] if rk[u] > rk[z])
def one(G, soft=False):
    full = []; seq = H.how3(G, full=full); T = len(seq) - 1; V = full[0][2]; gm = H.build(G)[0]; rk = own.VJ(gm.prio).rk
    cs, comp, succD = H.sccs(G); K = len(cs); f = [0] * K
    for t in range(1, T + 1):
        for x in range(G["N"]):
            if seq[t][x] != seq[t - 1][x]: f[comp[x]] = t
    reach = []
    for ci in range(K):
        r = set()
        for d in succD[ci]: r |= {d} | reach[d]
        reach.append(r)
    t0 = [max((f[d] for d in reach[ci]), default=0) for ci in range(K)]
    out = dict(T3=T, deepC=0, deepC_max=0, intC=0, alldeep=0, dmaxC=-1, soft=0); perC = [0] * K; prof = {}; gs = {}
    for x in range(G["N"]):
        for k, o in enumerate(G["opts"][x]):
            g, pe, pb = V[("g", (x, k))], V[("pe", (x, k))], V[("pbeta", (x, k))]
            internal = all(y >= 0 and comp[y] == comp[x] for y in o[:2]); ci = comp[x]
            for t in range(T):
                a, b = full[t][1][g], full[t + 1][1][g]
                if a == b: continue
                d = depth(full[t][0][a], full[t + 1][0][a], rk)
                out["alldeep"] += d > c
                if internal and t >= t0[ci]:
                    out["intC"] += 1; out["dmaxC"] = max(out["dmaxC"], d); out["soft"] += max(0, d); gs[(x, k)] = gs.get((x, k), 0) + max(0, d)
                    if d > c: perC[ci] += 1; prof[(x, k)] = prof.get((x, k), 0) + 1
    out["gsoft"] = max(gs.values(), default=0); out["deepC"] = sum(perC); out["deepC_max"] = max(perC); out["top"] = sorted(prof.items(), key=lambda kv: -kv[1])[:3]
    return out
def items():
    if sys.argv[1] == "rand":
        import random; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r231")); from dep231 import rgen
        rng = random.Random(int(sys.argv[2]))
        for i in range(int(sys.argv[3])): yield "r%d" % i, rgen(rng, rng.randint(1, 5), rng.randint(1, 4), rng.choice([2, 3, 4]))
    else:
        for fn in sys.argv[1:]:
            G = json.load(open(fn)); G = G.get("genome", G); G.pop("_evals", None); yield os.path.basename(fn), G
if __name__ == "__main__":
    tot = dict(n=0, deepC=0, intC=0, alldeep=0, deepC_max=0)
    for nm, G in items():
        o = one(G); tot["n"] += 1
        for k in ("deepC", "intC", "alldeep"): tot[k] += o[k]
        tot["deepC_max"] = max(tot["deepC_max"], o["deepC_max"])
        if sys.argv[1] != "rand" or o["deepC"]: print(nm, dict(N=G["N"], M=sum(len(v) for v in G["opts"]), **o), flush=True)
    print("TOTAL", tot, flush=True)
