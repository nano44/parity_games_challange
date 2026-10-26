#!/usr/bin/env python3
"""Box 48 DATA (docs/new/N5-NCONF-box48.md): distinct Odd configurations sigma-bar|Q per phase, on every phase (fallbacks or not).
A phase = maximal run of states with (lambda, tau) constant (as box47/fbconf.py). Per phase: L = transitions, EPQ = sigma-bar|Q changes + 1,
EPD = D changes + 1 (D = {q in Q: sigma-bar(q) != tau(q)}), NCONF = distinct sigma-bar|Q, ND = distinct D, REV = EPQ - NCONF (returns to an
earlier configuration), f = in-phase fallbacks, NCF = distinct configurations at fallback sources (fbconf's NCONF).
Usage: nconf.py STARTS SEED (--list FILE | --rand C LO HI GSEED | files) [--nmax N] [--start F] [--minlen L]; VERB=1 prints a row per phase
with L >= minlen; TRACE=1 also prints the configuration sequence of those phases."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
for p in ("../box43", "../box21"): sys.path.insert(0, os.path.join(HERE, p))
from multi import load, step, start_pair, Engine, dual, rand_ckO
from n5x import readstart
C = {}; M = {}
def inc(k, v=1): C[k] = C.get(k, 0) + v
def mx(k, v, tag=None):
    if v > M.get(k, (-1,))[0]: M[k] = (v, tag)
VERB = os.environ.get("VERB") == "1"; TRACE = os.environ.get("TRACE") == "1"; MINLEN = 0
def run(g, start, nm, cap=5000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []; inc("runs")
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        conf = tuple(sb[q] for q in Q)
        rows.append(dict(lam=tuple(x[0] for x in vs), t=tuple(t), fb=r[4] if r else 0, conf=conf,
                         D=frozenset(q for q in Q if sb[q] != t[q])))
        if r is None: break
        s, t = r[0], r[1]
    if len(rows) > cap: inc("CAP")
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and (rows[j + 1]["lam"], rows[j + 1]["t"]) == (rows[i]["lam"], rows[i]["t"]): j += 1
        phase(g, rows, i, j, Q, nm, start)
        i = j + 1
def phase(g, rows, a, b, Q, nm, start):
    L = b - a; confs = [rows[k]["conf"] for k in range(a, b + 1)]; Ds = [rows[k]["D"] for k in range(a, b + 1)]
    epq = 1 + sum(1 for k in range(L) if confs[k] != confs[k + 1]); epd = 1 + sum(1 for k in range(L) if Ds[k] != Ds[k + 1])
    nconf = len(set(confs)); nd = len(set(Ds)); f = sum(1 for k in range(a, b) if rows[k]["fb"])
    ncf = len({rows[k]["conf"] for k in range(a, b) if rows[k]["fb"]})
    vis = {}
    for k in range(L + 1):
        if k == 0 or confs[k] != confs[k - 1]: vis[confs[k]] = vis.get(confs[k], 0) + 1
    vmax = max(vis.values())
    # a return without a fallback in between: config c's epochs E1 < E2 with no in-phase fallback between E1's end and E2's start
    lastend = {}; ret_nofb = 0; fbpos = [k - a for k in range(a, b) if rows[k]["fb"]]
    for k in range(L + 1):
        c = confs[k]
        if (k == 0 or confs[k - 1] != c) and c in lastend:
            if not any(lastend[c] <= x < k for x in fbpos): ret_nofb += 1
        if k == L or confs[k + 1] != c: lastend[c] = k
    inc("RET_NOFB", ret_nofb)
    inc("phases"); inc("sum_L", L); inc("sum_epq", epq); inc("sum_nconf", nconf)
    if epd != epq: inc("EPD_NE_EPQ")
    if epq > nconf: inc("phases_with_return")
    tag = (nm, g.n, len(Q))
    for k, v in (("L", L), ("EPQ", epq), ("NCONF", nconf), ("ND", nd), ("REV", epq - nconf), ("VIS", vmax), ("RET_NOFB", ret_nofb), ("f", f), ("NCF", ncf),
                 ("NCONF_minus_n", nconf - g.n), ("NCONF_over_n", round(nconf / g.n, 3))):
        mx(k + "_max", v, tag)
    if VERB and L >= MINLEN:
        print(f"PHASE {nm} n={g.n} |Q|={len(Q)} {'S3' if start is None else 'start'} [{a},{b}] L={L} EPQ={epq} EPD={epd} NCONF={nconf} ND={nd} "
              f"REV={epq - nconf} VIS={vmax} RET_NOFB={ret_nofb} f={f} NCF={ncf} |D|max={max(len(d) for d in Ds)}", flush=True)
        if TRACE:
            ids = {}; seq = [ids.setdefault(c, len(ids)) for c in confs]
            print("  CONFSEQ " + " ".join(map(str, seq)), flush=True)
            print("  DSEQ " + " ".join("{" + ",".join(map(str, sorted(d))) + "}" for d in Ds), flush=True)
if __name__ == "__main__":
    a = sys.argv[1:]; nmax = 64; fixed = None
    if "--nmax" in a: i = a.index("--nmax"); nmax = int(a[i + 1]); del a[i:i + 2]
    if "--minlen" in a: i = a.index("--minlen"); MINLEN = int(a[i + 1]); del a[i:i + 2]
    if "--start" in a: i = a.index("--start"); fixed = readstart(a[i + 1]); del a[i:i + 2]
    K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    if a[0] == "--list":
        R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [(l.split()[0], load(os.path.join(R0, l.split()[0]))) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    elif a[0] == "--rand":
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        gs = [(f"rand{i}", g) for i, g in enumerate(rand_ckO(rng, lo, hi, rng.randint(2, 4)) for _ in range(cnt)) if g is not None]
    else: gs = [(f, load(f)) for f in a]
    for nm, g in gs:
        if g.n > nmax: continue
        sts = [fixed] if fixed else [None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                                {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]
        for st in sts:
            try: run(g, st, nm)
            except RecursionError: inc("RECERR")
    print(" ".join(f"{k} {v}" for k, v in sorted(C.items())))
    print(" ".join(f"{k} {v[0]} {v[1]}" for k, v in sorted(M.items())))
