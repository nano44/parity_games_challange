#!/usr/bin/env python3
"""L-NEW box 143: per-mover / per-option delay counts (cause.py analyse). Prints MAXDELAY_OPT = max over (x, k) of the delays of x into
option k, MAXDELAY_X, MAXMOVES_X, MAXBFLIPS_X, and the per-level moves. Usage: perx.py genome.json ..."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
src = open(os.path.join(HERE, "cause.py")).read().split('if __name__ == "__main__":')[0]
ns = {"__file__": os.path.join(HERE, "cause.py")}; exec(src, ns); analyse = ns["analyse"]; run = ns["run"]
for p in sys.argv[1:]:
    G = json.load(open(p)); r = analyse(G); S = run(G, cap=5000)[0]; N = G["N"]
    opt = {}; px = {}
    for (x, l, s, sp, zs, cl) in r["dl"]:
        k = S[sp][x]; opt[(x, k)] = opt.get((x, k), 0) + 1; px[x] = px.get(x, 0) + 1
    mv = [sum(S[t][x] != S[t - 1][x] for t in range(1, len(S))) for x in range(N)]
    print(f"PERX {os.path.basename(p)} d {N//2} STEPS {r['T']} SUMDELAY {r['D']} MAXDELAY_OPT {max(opt.values(), default=0)} MAXDELAY_X {max(px.values(), default=0)} "
          f"MAXMOVES_X {max(mv)} MOVES_PER_LEVEL {[mv[2*l]+mv[2*l+1] for l in range(N//2)]} DELAY_PER_LEVEL {[sum(v for x,v in px.items() if x//2==l) for l in range(N//2)]}")
