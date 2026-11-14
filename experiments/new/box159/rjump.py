#!/usr/bin/env python3
"""L-NEW box 159, DATA: potential R(s) := number of steps of the run of H_s (every level-0 mover frozen at its option in s) from s.
By SEG, R(s_t) = R(s_(t-1)) - 1 at every step without a level-0 move. At a level-0 step t: JUMP_t := R(s_t) - (R(s_(t-1)) - 1).
T = R(s_0) + sum of JUMP_t + (number of level-0 steps) - ... (exact identity checked: T = R(s_0) + sum_t JUMP_t).
Prints per run: R0, the jumps, T. ALL=1: all starts (N <= ALLN). Usage: rjump.py genome.json ..."""
import sys, os, json, itertools
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box150", "check.py")
ns = {"__file__": P}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]; restrict = ns["restrict"]
def R(G, s):
    keep = [v for v in range(G["N"]) if G["lev"][v] == 0]; H = restrict(G, keep, list(s)); S, _ = Gen(H).run(H["start"]); return len(S) - 1
agg = dict(runs=0, IDENT=0, maxjump=-99, maxjump_file=None, maxR0=0); quiet = os.environ.get("Q")
for f in sys.argv[1:]:
    G = json.load(open(f)); g = Gen(G); N = g.N
    if max(len(o) for o in G["opts"]) > 2: continue
    starts = [G["start"]]
    if os.environ.get("ALL") and N <= int(os.environ.get("ALLN", "8")): starts = [list(x) for x in itertools.product(*[range(len(o)) for o in G["opts"]])]
    for st in starts:
        S, _ = g.run(st); T = len(S) - 1; agg["runs"] += 1
        Rs = [R(G, s) for s in S]
        jumps = []
        for t in range(1, T + 1):
            lv0 = any(g.lev[v] == 0 and S[t][v] != S[t - 1][v] for v in range(N))
            if lv0: jumps.append(Rs[t] - (Rs[t - 1] - 1))
            elif Rs[t] != Rs[t - 1] - 1: agg["IDENT"] += 1      # SEG says this cannot happen
        if T != Rs[0] + sum(jumps) and Rs[-1] == 0: agg["IDENT"] += 1
        for j in jumps:
            if j > agg["maxjump"]: agg["maxjump"], agg["maxjump_file"] = j, (os.path.basename(f), st, T, Rs[0], jumps)
        agg["maxR0"] = max(agg["maxR0"], Rs[0])
        if not quiet: print(f"{os.path.basename(f)} d {max(g.lev)+1} T {T} R0 {Rs[0]} jumps {jumps}")
print("RJUMP", agg)
