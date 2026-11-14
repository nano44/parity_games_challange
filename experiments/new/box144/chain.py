#!/usr/bin/env python3
"""L-NEW box 144 CHAIN-BACK on 2-wide deg-2 IDEAL-ACYC ladders. For each DELSTEP t (least mover h_t delayed, box 143) with new
option k: the cause set Z_t = movers on the WHOLE Xi-play of (h_t, k) at state t-2 that move at step t-1 (non-empty: box 142
DELAY-CAUSE). t is CHAINED if h_(t-1) is in Z_t (then pi(h_t) < pi(h_(t-1)) in every topological order of the Xi-graph).
Prints DELSTEPS, CHAINED, UNCHAINED, NOCAUSE (Z_t empty; must be 0), PIVIOL (chained with h_t not a Xi-ancestor of h_(t-1); must be
0), MAXCHAIN (longest run of consecutive chained DELSTEPS + 1), and the classes of the first cause of UNCHAINED DELSTEPS
(CAR = moved at a carry step of its own level - 1, DEL, PRE), with their level relative to h_(t-1) (UNLEV).
Usage: chain.py genome.json ... [VERB=1]"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "..", "box143", "cause.py")).read().split('if __name__ == "__main__":')[0]
ns = {"__file__": os.path.join(HERE, "..", "box143", "cause.py")}; exec(src, ns); run = ns["run"]
VERB = os.environ.get("VERB")
def analyse(G):
    S, CUR, KEY, why = run(G, cap=5000); N, opts, lev = G["N"], G["opts"], G["lev"]; d = N // 2; T = len(S) - 1
    def L(t, l):
        K = KEY[min(t, len(KEY) - 1)]; return 2 * l if K[2 * l] < K[2 * l + 1] else 2 * l + 1
    carry = {(l, t) for l in range(d) for t in range(1, T + 1) if L(t, l) != L(t - 1, l)}
    mv = lambda t, x: S[t][x] != S[t - 1][x]
    def play(t, x, k):
        out = []; y = opts[x][k][1]
        while y >= 0: out.append(y); y = opts[y][S[t][y]][1]
        return out
    reach = {}
    def desc(x):  # all movers Xi-reachable from x (any options)
        if x not in reach:
            r = set()
            for (wt, xt, b) in opts[x]:
                if xt >= 0: r |= {xt} | desc(xt)
            reach[x] = r
        return reach[x]
    def cls(t, x):
        l = lev[x]
        if l > 0 and (l - 1, t) in carry: return "CAR"
        cs = [s for s in range(1, t + 1) if l > 0 and (l - 1, s) in carry]
        if not cs: return "PRE"
        return "DEL" if all(not mv(u, x) for u in range(cs[-1], t)) else "OTHER"
    least = {}
    for t in range(1, T + 1):
        ms = [x for x in range(N) if mv(t, x)]
        if ms: least[t] = min(ms, key=lambda x: lev[x])
    ds = ch = noc = piv = 0; run_ = 0; mx = 0; ucls = {}; ulev = {}; prev_ch = False
    for t in range(1, T + 1):
        isdel = t >= 2 and t in least and cls(t, least[t]) == "DEL"
        if not isdel: run_ = 0; continue
        ds += 1; x = least[t]; k = S[t][x]; Z = [y for y in play(t - 2, x, k) if mv(t - 1, y)]
        if not Z: noc += 1
        if least.get(t - 1) in Z:
            ch += 1; run_ += 1
            if least[t - 1] not in desc(x): piv += 1
        else:
            run_ = 0
            if Z:
                c = Z[0]; cc = cls(t - 1, c); ucls[cc] = ucls.get(cc, 0) + 1
                dl = lev[c] - lev[least[t - 1]] if t - 1 in least else None; ulev[dl] = ulev.get(dl, 0) + 1
            if VERB: print(f"  UNCHAINED t {t} h {x} lev {lev[x]} Z {Z} classes {[cls(t-1, z) for z in Z]} h_(t-1) {least.get(t-1)}")
        mx = max(mx, run_ + 1)
    # ALL steps t >= 2 (R178 XI-NEW form): cause set of the least mover's new option; chained if h_(t-1) is in it
    au = 0; anoc = 0; apiv = 0; blk = 0; amx = 0
    for t in range(1, T + 1):
        if t not in least: continue
        if t == 1 or (t - 1) not in least: blk = 1; amx = max(amx, blk); continue
        x = least[t]; k = S[t][x]; Z = [y for y in play(t - 2, x, k) if mv(t - 1, y)] if t >= 2 else []
        if not Z: anoc += 1
        if least[t - 1] in Z:
            blk += 1
            if least[t - 1] not in desc(x): apiv += 1
        else: au += 1; blk = 1
        amx = max(amx, blk)
    abound = N * (1 + au)
    return dict(au=au, anoc=anoc, apiv=apiv, amx=amx, abound=abound, aok=T <= abound, T=T, d=d, ds=ds, ch=ch, un=ds - ch, noc=noc, piv=piv, mx=mx if ds else 0, ucls=ucls, ulev=dict(sorted(ulev.items(), key=str)))
if __name__ == "__main__":
    for p in sys.argv[1:]:
        r = analyse(json.load(open(p)))
        print(f"CHAIN {os.path.basename(p)} d {r['d']} STEPS {r['T']} DELSTEPS {r['ds']} CHAINED {r['ch']} UNCHAINED {r['un']} NOCAUSE {r['noc']} PIVIOL {r['piv']} "
              f"MAXCHAIN {r['mx']} UNCLS {r['ucls']} UNLEV {r['ulev']} | ALL: UNCH {r['au']} NOCAUSE {r['anoc']} PIVIOL {r['apiv']} MAXBLOCK {r['amx']} BOUND N(1+U) {r['abound']} OK {r['aok']}")
