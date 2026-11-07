#!/usr/bin/env python3
"""L-NEW box 166: exact composition test of the 64 winning 2-bit patterns (out/patterns2.json) against REAL clock key orders.
Clock C (corpus genome + start) runs unaffected by V. A bit = the order of two clock movers p, q of one level under the NEW clock
state (bit_t = [key_t(p) < key_t(q)]); a V-mover reading bit i with sign sg sits one level above (p, q) and W-points its option 0
to p and option 1 to q (sg 0) or reversed (sg 1); a constant reader W-points both options to one mover (gates decide).
V-run: s_t(x) = KP_t(x) if x unhappy at s_(t-1); stop when nothing changes after the clock has stopped (clock frozen after its end).
Any composed moves(x0) > 5 is rebuilt as one IDEAL genome (box165 build) and re-verified by the plain simulator (box150 Gen).
Usage: compose2.py vfile x0 nstarts clockfile ..."""
import os, sys, json, itertools, random
H = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(H, "..", "box165", "permover.py")).read().split("\nif __name__")[0])
V = json.load(open(sys.argv[1])); x0 = int(sys.argv[2]); NS = int(sys.argv[3]); gv = Gen(V); NV = V["N"]
pats = json.load(open(os.path.join(H, "out", "patterns2.json")))
vstates = list(itertools.product((0, 1), repeat=NV)); unh = {s: [x for x in range(NV) if len(gv.avail(s, x)) == 2] for s in vstates}
rng = random.Random(7)

def vrun(bitseq, pat, s):
    mv = 0; t = 0; Tc = len(bitseq[0])
    while t < 500:
        t += 1; n = list(s); u = min(t, Tc) - 1
        for x in unh[s]:
            a = pat[x]; n[x] = a[1] if a[0] == "c" else (1 - bitseq[a[1]][u]) ^ a[2]   # bit 1 = option 0 preferred
        n = tuple(n)
        if n == s:
            if t >= Tc: return mv
            continue
        mv += n[x0] != s[x0]; s = n
    return mv

def build(Cg, cs, pr, lv, pat, vs):
    NC = Cg["N"]; M0 = sum(len(o) for o in Cg["opts"]); opts = [list(map(list, o)) for o in Cg["opts"]]
    gate = [list(gg) for gg in Cg["gate"]]; mg = max(x for gg in gate for x in gg) + 1
    br = list(Cg["br"]) + [0] * (2 * NV); bp = list(Cg["bp"]) + [0] * (2 * NV); topr = max(Cg["br"]) + 1; lev = list(Cg["lev"])
    for x in range(NV):
        a = pat[x]
        if a[0] == "c": p = q = pr[0][0]; L = lv[0]; gs = [mg + 2 * x, mg + 2 * x + 1] if a[1] == 0 else [mg + 2 * x + 1, mg + 2 * x]
        else:
            p, q = pr[a[1]]; L = lv[a[1]]
            if a[2]: p, q = q, p
            gs = [mg + 2 * x, mg + 2 * x + 1]
        o = []
        for k in range(2):
            xt = V["opts"][x][k][1]; m = M0 + 2 * x + k
            o.append([(p, q)[k], xt + NC if xt >= 0 else -1, m]); br[m] = topr + V["br"][V["opts"][x][k][2]]; bp[m] = V["bp"][V["opts"][x][k][2]]
        opts.append(o); gate.append(gs); lev.append(L + 1)
    return {"N": NC + NV, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": bp, "start": list(cs) + list(vs), "deg": [len(o) for o in opts]}

best = 0
for cf in sys.argv[4:]:
    try: Cg = json.load(open(cf)); assert "N" in Cg; gc = Gen(Cg)
    except Exception: continue
    NC = Cg["N"]; starts = [tuple(Cg["start"])] + [tuple(rng.randrange(len(o)) for o in Cg["opts"]) for _ in range(NS)]; fb = 0; kill = None
    for cs in starts:
        try: S, _ = gc.run(list(cs))
        except RuntimeError: continue
        if len(S) < 5: continue
        keys = [gc.keys(S[t]) for t in range(1, len(S))]; seq = {}
        for L in sorted(set(Cg["lev"])):
            ms = [v for v in range(NC) if Cg["lev"][v] == L]
            for p, q in itertools.combinations(ms, 2):
                sq = tuple(int(k[p] < k[q]) for k in keys)
                if sum(a != b for a, b in zip(sq, sq[1:])) >= 1 and sq not in seq and tuple(1 - b for b in sq) not in seq: seq[sq] = ((p, q), L)
        D = list(seq.items())
        for (A, (pa, la)), (B, (pb, lb)) in itertools.permutations(D, 2):
            for pat in pats:
                for vs in vstates:
                    m = vrun((A, B), pat, vs)
                    if m > fb: fb = m
                    if m > 5 and kill is None:
                        G = build(Cg, cs, (pa, pb), (la, lb), pat, vs); r = measure(G); xr = NC + x0
                        kill = (m, r["mv"][xr], r["desc"][xr], r["T"]); fn = os.path.join(H, "out", "KILL_PM_compose_%s.json" % os.path.basename(cf)[:-5])
                        json.dump(G, open(fn, "w"))
                        print("CANDIDATE KILL", os.path.basename(cf), "composed", m, "| plain re-run: moves", r["mv"][xr], "desc", r["desc"][xr], "T", r["T"],
                              "KILL" if r["mv"][xr] > 1 + r["desc"][xr] else "MISMATCH", fn, flush=True)
            if kill: break
        if kill: break
    best = max(best, fb); print("clock", os.path.basename(cf), "N", NC, "max composed moves(x0)", fb, flush=True)
print("BEST", best)
