#!/usr/bin/env python3
"""L-RED R158: hill-climb over the FEEDBACK superset gadget on span/mkrw.py K m (engine E1).
Added to mkrw: riders d_j (Odd) -> {md_j -> r_j (tau), mq_j -> hp (route 2, toggle R2)}; Even selectors hs (odd j), hps (even j);
E2 chain rr_1..rr_m2 (Even: aa_i -> rr_(i-1) | hs, bb_i -> hps); gates (toggle GATE): a_j (j >= 2) Odd -> {r_(j-1) (tau), g_j -> rr_m2};
b_j -> be_j -> hp. Markers BA2_i, MU_j (md), MQ_j (mq), GM_j (g), BE_j (be): each either inert (priority below z) or placed in the
band between E1's a-markers and the pivot ladder, at a searched rank and parity. Objective: longest W-run |F| (n5b SPEC).
Usage: fbsearch.py K m m2 iters seed [OUTPREFIX]"""
import sys, os, random, re, subprocess, tempfile, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xcn"))
import xcn, n5b
pg = xcn.pg
K, m, m2, IT, seed = map(int, sys.argv[1:6]); OUT = sys.argv[6] if len(sys.argv) > 6 else None
td = tempfile.mkdtemp()
subprocess.run([sys.executable, os.path.join(HERE, "..", "span", "mkrw.py"), str(K), str(m), f"{td}/b.pg", f"{td}/b.start"], check=True, capture_output=True)
rows = []
for line in open(f"{td}/b.pg"):
    mm = re.match(r'\s*(\d+)\s+(\d+)\s+([01])\s+([\d,]+)\s*"([^"]*)"', line)
    if mm: rows.append([int(mm.group(1)), int(mm.group(2)), int(mm.group(3)), [int(a) for a in mm.group(4).split(",")], mm.group(5)])
rows.sort(); base = {r[4]: r for r in rows}
st = open(f"{td}/b.start").read().split("\n")
S0 = dict(tuple(map(int, x.split(":"))) for x in st[0].split()[1:]); T0 = dict(tuple(map(int, x.split(":"))) for x in st[1].split()[1:])
Z = base["z"][1]; BAmax = max(base[f"a{j}"][1] for j in range(1, m + 1)); LADmin = min(r[1] for r in rows if r[1] > BAmax)
MK = [f"BA2_{i}" for i in range(1, m2 + 1)] + [f"MU{j}" for j in range(1, m + 1)] + [f"MQ{j}" for j in range(1, m + 1)] + [f"GM{j}" for j in range(2, m + 1)] + [f"BE{j}" for j in range(1, m + 1)]
def build(gen):
    R2, GATE = gen["R2"], gen["GATE"]
    pr = {r[4]: 1000 * r[1] + (r[1] % 2) for r in rows}; own = {r[4]: r[2] for r in rows}
    succ = {r[4]: [rows[w][4] for w in r[3]] for r in rows}; order = [r[4] for r in rows]
    sig = {rows[v][4]: rows[w][4] for v, w in S0.items()}; tau = {rows[v][4]: rows[w][4] for v, w in T0.items()}
    placed = sorted((gen["mk"][k][0], k) for k in MK if gen["mk"][k] is not None)
    lo, hi = 1000 * BAmax + 2, 1000 * LADmin - 2; step = max(4, (hi - lo) // (len(placed) + 2) // 2 * 2)
    mp = {}
    for i, (_, k) in enumerate(placed):
        p = lo + 2 * i * 2 + (gen["mk"][k][1]); mp[k] = p
    low = iter(range(2, 1000 * Z, 2))
    def P(k): return mp[k] if k in mp else next(low)
    def add(name, o, p, s): order.append(name); own[name] = o; pr[name] = p; succ[name] = list(s)
    for j in range(1, m + 1):
        add(f"d{j}", 1, next(low), [f"md{j}"] + ([f"mq{j}"] if R2 else [])); tau[f"d{j}"] = f"md{j}"
        add(f"md{j}", 1, P(f"MU{j}"), [f"r{j}"])
        if R2: add(f"mq{j}", 1, P(f"MQ{j}"), ["hp"])
        add(f"be{j}", 1, P(f"BE{j}"), ["hp"]); succ[f"b{j}"] = [f"be{j}"]
        if GATE and j >= 2:
            succ[f"a{j}"] = [f"r{j - 1}", f"g{j}"]; tau[f"a{j}"] = f"r{j - 1}"; add(f"g{j}", 1, P(f"GM{j}"), [f"rr{m2}"])
    od = [f"d{j}" for j in range(1, m + 1, 2)]; ev = [f"d{j}" for j in range(2, m + 1, 2)]
    add("hs", 0, next(low), od); sig["hs"] = od[gen["s0"] % len(od)]; add("hps", 0, next(low), ev); sig["hps"] = ev[gen["s0"] % len(ev)]
    for i in range(1, m2 + 1):
        add(f"rr{i}", 0, next(low), [f"aa{i}", f"bb{i}"]); sig[f"rr{i}"] = f"bb{i}"
        add(f"aa{i}", 1, P(f"BA2_{i}"), ["hs" if i == 1 else f"rr{i - 1}"]); add(f"bb{i}", 1, next(low), ["hps"])
    ix = {v: i for i, v in enumerate(order)}
    g = pg.Game([pr[v] for v in order], [own[v] for v in order], [[ix[w] for w in succ[v]] for v in order])
    s0 = [ix[sig.get(v, succ[v][0])] if own[v] == 0 else -1 for v in order]; t0 = [ix[tau.get(v, succ[v][0])] if own[v] == 1 else -1 for v in order]
    return g, s0, t0, order
def score(gen):
    g, s0, t0, _ = build(gen)
    try:
        tr, fb = xcn.trace(g, s0, t0, cap=20000); runs, W = xcn.wruns(g, tr, fb)
    except Exception as e: return -1, 0
    return max(len(F) for F in runs) - 1, len(tr) - 1
def rnd(rng):
    return {"R2": rng.random() < 0.5, "GATE": True, "s0": rng.randrange(4), "mk": {k: (None if rng.random() < 0.2 else (rng.random(), rng.randrange(2))) for k in MK}}
def mutate(gen, rng):
    g2 = json.loads(json.dumps(gen)); g2["mk"] = {k: (tuple(v) if v else None) for k, v in g2["mk"].items()}
    for _ in range(rng.randrange(1, 4)):
        r = rng.random()
        if r < 0.05: g2["R2"] = not g2["R2"]
        elif r < 0.08: g2["s0"] = rng.randrange(4)
        else:
            k = rng.choice(MK); v = g2["mk"][k]
            if v is None or rng.random() < 0.15: g2["mk"][k] = None if v is not None and rng.random() < 0.5 else (rng.random(), rng.randrange(2))
            elif rng.random() < 0.5: g2["mk"][k] = (v[0], 1 - v[1])
            else: g2["mk"][k] = (min(1, max(0, v[0] + rng.gauss(0, 0.15))), v[1])
    return g2
if __name__ == "__main__":
    rng = random.Random(seed)
    nog = {"R2": False, "GATE": False, "s0": 0, "mk": {k: None for k in MK}}
    print("baseline (no gates, inert):", score(nog), flush=True)
    best = rnd(rng); bs = score(best)
    for it in range(IT):
        if it % 200 == 199 and bs[0] <= 0: best = rnd(rng); bs = score(best)
        c = mutate(best, rng); cs = score(c)
        if cs[0] >= bs[0]:
            if cs[0] > bs[0]: print(it, "best |F|", cs, "R2", c["R2"], flush=True)
            best, bs = c, cs
    print("FINAL", bs)
    if OUT:
        json.dump(best, open(OUT + ".json", "w"))
        g, s0, t0, order = build(best)
        with open(OUT + ".pg", "w") as f:
            f.write(f"parity {g.n - 1};\n")
            for v in range(g.n): f.write(f'{v} {g.prio[v]} {g.owner[v]} {",".join(map(str, g.succ[v]))} "{order[v]}";\n')
        with open(OUT + ".start", "w") as f:
            f.write("SIGMA0 " + " ".join(f"{v}:{s0[v]}" for v in range(g.n) if g.owner[v] == 0) + "\n")
            f.write("TAU0 " + " ".join(f"{v}:{t0[v]}" for v in range(g.n) if g.owner[v] == 1) + "\n")
