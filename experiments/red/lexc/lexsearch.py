#!/usr/bin/env python3
"""L-RED R143 (a): structured search for a long W-constant interval with an EVEN W-cycle node and a width-2 tight DAG (L-LIT T54 §4.4
LEX-ARENA template), run by the real N5 (n5b SPEC). Template: c = 0 (Even, even prio PC, self-loop); layers 1..L of two Even vertices
(low prio); an Odd gadget o_(x,y) on every tight edge x -> y (tau0(o) = y; layer 1 -> c); markers (prio > PC) and free vertices X; the
search mutates deviation edges of gadgets, markers, X and sigma0. Objective: (longest W-constant interval, max in-interval Xi-changes of
one vertex, returns). Reports per interval: LEN, XCI, RET, SBF (sigma-bar flips).
Usage: lexsearch.py --search SEED L NMARK NX SECONDS OUT.pg   |   lexsearch.py GAME.pg START"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.abspath(os.path.join(HERE, "..", ".."))
for p in ("n5-second", "harness", "hard-families"): sys.path.insert(0, os.path.join(EXP, p))
import n5b
pg = n5b.pg

def intervals(g, s0, t0, max_iter=400):
    N = n5b.N5(g); N.mode = "spec"; tr, fb = [], []
    try: N.run(s0, t0, trace=tr, fbtrace=fb, max_iter=max_iter)
    except Exception: return [], tr
    Wc = {}; SG = n5b.SpecSI(g)
    def W(s, t):
        if t not in Wc:
            h = pg.Game(list(g.prio), list(g.owner), [[t[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(g.n)])
            Wc[t] = n5b.SpecSI(h)
        return Wc[t].evaluate(list(s))
    out = []; cur = None
    for i in range(len(tr) - 1):
        (s, t), (s2, t2) = tr[i], tr[i + 1]
        if t == t2 and not fb[i] and s != s2 and W(s, t) == W(s2, t):
            if cur is None: cur = [i, i + 1]
            else: cur[1] = i + 1
        else:
            if cur: out.append(tuple(cur))
            cur = None
    if cur: out.append(tuple(cur))
    res = []
    for (p, q) in out:
        X = [SG.evaluate_choice(list(tr[k][0])) for k in range(p, q + 1)]
        xi = [x[0] for x in X]; sb = [x[1] for x in X]
        xc = [sum(1 for k in range(len(xi) - 1) if xi[k][v] != xi[k + 1][v]) for v in range(g.n)]
        sbf = sum(1 for k in range(len(sb) - 1) for v in range(g.n) if g.owner[v] == 1 and sb[k][v] != sb[k + 1][v])
        ret = 0
        for v in range(g.n):
            if g.owner[v] != 0: continue
            held = {tr[p][0][v]}
            for k in range(p, q):
                a, b = tr[k][0][v], tr[k + 1][0][v]
                if a != b:
                    if b in held: ret += 1
                    held.add(b)
        res.append(dict(p=p, q=q, LEN=q - p, XCI=max(xc), XV=xc.index(max(xc)), RET=ret, SBF=sbf, lam=xi[0][xc.index(max(xc))][0]))
    return res, tr

class T:
    """template: L layers, NM markers, NX free vertices."""
    def __init__(s, rng, L, NM, NX):
        s.L, s.NM, s.NX = L, NM, NX; s.rng = rng
        s.PC = 4 * (NM + NX) + 10                       # c priority (even); markers above it
        s.lay = [[0]]; nid = 1
        for j in range(1, L + 1): s.lay.append([nid, nid + 1]); nid += 2
        s.gad = {}
        for j in range(1, L + 1):
            for x in s.lay[j]:
                for y in s.lay[j - 1]:
                    s.gad[(x, y)] = nid; nid += 1
        s.mk = list(range(nid, nid + NM)); nid += NM
        s.xv = list(range(nid, nid + NX)); nid += NX; s.n = nid
        s.dev = {o: [] for o in s.gad.values()}
        s.mprio = {m: rng.randrange(s.PC + 1, s.PC + 2 * NM + 2) for m in s.mk}
        s.msucc = {m: [rng.randrange(s.n)] for m in s.mk}; s.mown = {m: rng.randrange(2) for m in s.mk}
        s.xprio = {x: rng.randrange(0, s.PC + 2 * NM + 2) for x in s.xv}; s.xown = {x: rng.randrange(2) for x in s.xv}
        s.xsucc = {x: sorted(set(rng.sample(range(s.n), 2))) for x in s.xv}
        s.sig0 = {x: rng.choice(s.lay[j - 1]) for j in range(2, L + 1) for x in s.lay[j]}
        for _ in range(rng.randint(1, 2 * L)): s.mut_dev()
    def mut_dev(s):
        o = s.rng.choice(list(s.dev)); pool = s.mk + s.xv + [v for j in range(1, s.L + 1) for v in s.lay[j]]
        if s.dev[o] and s.rng.random() < 0.4: s.dev[o].pop(s.rng.randrange(len(s.dev[o])))
        else: s.dev[o] = sorted(set(s.dev[o] + [s.rng.choice(pool)]))
    def mutate(s):
        r = s.rng.random(); rng = s.rng
        if r < 0.35: s.mut_dev()
        elif r < 0.5 and s.mk: m = rng.choice(s.mk); s.mprio[m] = rng.randrange(s.PC + 1, s.PC + 2 * s.NM + 2)
        elif r < 0.6 and s.mk: m = rng.choice(s.mk); s.msucc[m] = sorted(set(rng.sample(range(s.n), rng.randint(1, 2)))); s.mown[m] = rng.randrange(2)
        elif r < 0.8 and s.xv:
            x = rng.choice(s.xv); k = rng.random()
            if k < 0.5: s.xsucc[x] = sorted(set(rng.sample(range(s.n), rng.randint(1, 3))))
            elif k < 0.8: s.xprio[x] = rng.randrange(0, s.PC + 2 * s.NM + 2)
            else: s.xown[x] ^= 1
        else:
            j = rng.randrange(2, s.L + 1) if s.L >= 2 else 1
            if s.L >= 2: x = rng.choice(s.lay[j]); s.sig0[x] = rng.choice(s.lay[j - 1])
    def game(s):
        prio = [0] * s.n; own = [0] * s.n; succ = [None] * s.n
        prio[0] = s.PC; own[0] = 0; succ[0] = [0]
        for j in range(1, s.L + 1):
            for i, x in enumerate(s.lay[j]):
                prio[x] = 2 * j + i % 2 if 2 * j + 1 < s.PC else 1; own[x] = 0; succ[x] = sorted(s.gad[(x, y)] for y in s.lay[j - 1])
        for (x, y), o in s.gad.items():
            prio[o] = 1; own[o] = 1; succ[o] = sorted(set([y] + s.dev[o]))
        for m in s.mk: prio[m] = s.mprio[m]; own[m] = s.mown[m]; succ[m] = s.msucc[m]
        for x in s.xv: prio[x] = s.xprio[x]; own[x] = s.xown[x]; succ[x] = s.xsucc[x]
        return pg.Game(prio, own, succ)
    def start(s, g):
        sig = [-1] * s.n; tau = [-1] * s.n
        for v in range(s.n):
            if g.owner[v] == 0: sig[v] = g.succ[v][0]
            else: tau[v] = g.succ[v][0]
        for x, y in s.sig0.items(): sig[x] = s.gad[(x, y)]
        for (x, y), o in s.gad.items(): tau[o] = y
        return sig, tau

def score(res):
    if not res: return (0, 0, 0)
    b = max(res, key=lambda r: (r["LEN"], r["XCI"], r["RET"]))
    return (b["LEN"], b["XCI"], b["RET"])

def write(g, sig, tau, out):
    with open(out, "w") as fo:
        fo.write(f"parity {g.n - 1};\n" + "".join(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n" for v in range(g.n)))
    with open(out[:-3] + ".start", "w") as fo:
        fo.write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in enumerate(sig) if w >= 0) + "\n")
        fo.write("TAU0 " + " ".join(f"{v}:{w}" for v, w in enumerate(tau) if w >= 0) + "\n")

if __name__ == "__main__" and sys.argv[1] == "--search":
    import copy
    seed, L, NM, NX, secs, out = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), float(sys.argv[6]), sys.argv[7]
    rng = random.Random(seed); t = T(rng, L, NM, NX); g = t.game(); f = score(intervals(g, *t.start(g))[0]); best = (f, copy.deepcopy(t))
    end = time.time() + secs; it = 0
    while time.time() < end:
        it += 1; h = copy.deepcopy(h0 := t); h.rng = rng
        for _ in range(rng.randint(1, 3)): h.mutate()
        gh = h.game(); fh = score(intervals(gh, *h.start(gh))[0])
        if fh >= f: t, f = h, fh
        if fh > best[0]: best = (fh, copy.deepcopy(h)); print("improve", it, fh, flush=True)
    f, t = best; g = t.game(); sig, tau = t.start(g); write(g, sig, tau, out)
    print(f"LEXSEARCH seed {seed} L {L} NM {NM} NX {NX} n {g.n} best (LEN, XCI, RET) {f} tries {it} -> {out}")
elif __name__ == "__main__":
    g = pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g)
    res, tr = intervals(g, s0, t0)
    print(f"LEXC {os.path.basename(sys.argv[1])} n {g.n} iterations {len(tr) - 1}")
    for r in res: print("  interval", r)
