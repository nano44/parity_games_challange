#!/usr/bin/env python3
"""Box 194: CONJECTURE IN-BOUND data. Per run and vertex v: IN(v) = max number of value changes of v inside one maximal stretch with
(cycle node, e-part of Pi) constant (as box192/dv192.py), split into k-only changes (Pi equal) and beta-part changes (Pi differs).
Also IN_B(v) = max number of distinct beta-parts inside one such stretch.
Modes: in194.py FILES.json | rand COUNT SEED | climb d w D seed iters OUT.json (hill-climb max IN; mutation = box191 climb191.mut,
exec'd from the unmodified file; resumable via OUT.json). Imports relative to this file."""
import sys, os, json, random, copy
HERE = os.path.dirname(os.path.abspath(__file__)); B191 = os.path.join(HERE, "..", "box191"); B192 = os.path.join(HERE, "..", "box192")
sys.path[:0] = [B192, B191]
import rpot192, rand191

def analyse(G):
    h, E, V, name, movers, ev = rpot192.states(G)
    ES = 0
    for v in range(h.n):
        if name[v][0] == "e": ES |= 1 << E.rank[v]
    r = dict(T=len(ev) - 1, n=h.n, IN=0, INk=0, INb=0, INB=0, who="")
    for v in range(h.n):
        vals = [ev[t][0][v] for t in range(len(ev))]
        tot = kk = bb = 0; bset = {vals[0][1]}
        for t in range(1, len(vals)):
            a, b = vals[t - 1], vals[t]
            if (a[0], a[1] & ES) != (b[0], b[1] & ES): tot = kk = bb = 0; bset = {b[1]}; continue
            if a == b: continue
            tot += 1
            if a[1] == b[1]: kk += 1
            else: bb += 1
            bset.add(b[1])
            if tot > r["IN"]: r["IN"], r["who"] = tot, f"{name[v]}"
            r["INk"] = max(r["INk"], kk); r["INb"] = max(r["INb"], bb); r["INB"] = max(r["INB"], len(bset))
    return r

def fmt(r): return " ".join(f"{k} {v}" for k, v in r.items())

if __name__ == "__main__":
    if sys.argv[1] == "rand":
        cnt, seed = int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); best = None
        for i in range(cnt):
            a = analyse(rand191.rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3)))
            if best is None or (a["IN"], a["INB"]) > (best["IN"], best["INB"]): best = a
        print(f"rand count {cnt} seed {seed} max:", fmt(best))
    elif sys.argv[1] == "climb":
        d, w, D, seed, iters = map(int, sys.argv[2:7]); out = sys.argv[7]; rng = random.Random(seed)
        src = open(os.path.join(B191, "climb191.py")).read(); i0 = src.index("def mut(G):"); i1 = src.index("\ncur = ")
        exec(src[i0:i1])
        cur = json.load(open(out)) if os.path.exists(out) else rand191.rgen(rng, d, w, D)
        sc = lambda G: (lambda a: (a["IN"], a["INB"], a["T"]))(analyse(G)); cs = sc(cur)
        for it in range(iters):
            G = mut(json.loads(json.dumps(cur)))
            try: s = sc(G)
            except Exception: continue
            if s >= cs:
                cur, cs = G, s
                json.dump(cur, open(out, "w"))
        print(f"climb d {d} w {w} D {D} seed {seed} iters {iters}:", fmt(analyse(cur)))
    else:
        for f in sys.argv[1:]: print(os.path.basename(f), fmt(analyse(json.load(open(f)))))
