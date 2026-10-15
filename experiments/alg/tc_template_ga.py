#!/usr/bin/env python3
"""GA over uniform per-bit templates of Two-Counters-like games, fitness = Oink dtl tangle count at N = NFIT.
A template fixes, for every bit i of both counters: which of a menu of edge types exist and the priorities of the
auxiliary vertices; it is applied uniformly, so a template is a family parametrised by N. Vertex roles per bit (player pl,
bit i): H (high, pl), T (tangle, 1-pl), L (gate, 1-pl), Z (pl), chain S_j/A_j/B_j (j < i) as in tc, plus optional
extras E1 (pl) and E2 (1-pl). Edge menu (each on/off): tc's own edges are always on; optional: T->E1, E1->T, E1->L_own(i-1),
E2->T, L->E2, E2->H, Z->L_own(i-1), H->L_opp(i), T->L_opp(i-1), E1->Z, A_j->E1, Z->E2, H->E2, E2->L_opp(i+1).
Priorities: pr(T) in {lopr, lopr+2}, pr(Z) in {lopr-1, lopr+1, lopr+2}, pr(E1) in {0..3}, pr(E2) in {0..3} (parity by role),
pr(L) in {inpr, inpr-2}. Usage: tc_template_ga.py GENS SEED [--nfit 5] [--pop 40] [--ngrow 9]"""
import sys, os, json, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, oink_fit, zielonka

EDGES = ["T>E1", "E1>T", "E1>Lown-1", "E2>T", "L>E2", "E2>H", "Z>Lown-1", "H>Lopp", "T>Lopp-1", "E1>Z", "A>E1", "Z>E2", "H>E2", "E2>Lopp+1", "E1>E2", "E2>E1", "E1>H"]


def build(tpl, n):
    on, prT, prZ, prE1, prE2, prL = tpl
    prio, owner, succ, names = [], [], [], []
    def new(p, o, nm): prio.append(p); owner.append(o); succ.append([]); names.append(nm); return len(prio) - 1
    def edge(a, b):
        if b not in succ[a]: succ[a].append(b)
    V = {}
    toppo = (n + 3) * n + 6 * n
    for i in range(n):
        for pl, hipr, inpr, lopr in ((0, toppo - 2, toppo - 2 * n - 3, 2), (1, toppo - 1, toppo - 2 * n - 2, 1)):
            tag = f"{'Odd' if pl else 'Even'}-{i}"
            h = new(hipr, pl, tag + "-H"); t = new(lopr + prT, 1 - pl, tag + "-T"); l = new(inpr + prL, 1 - pl, tag + "-L")
            z = new(lopr - 1 + prZ, pl, tag + "-Z")
            e1 = new(2 * prE1 + pl, pl, tag + "-E1"); e2 = new(2 * prE2 + (1 - pl), 1 - pl, tag + "-E2")   # parity of owner
            V[(pl, i)] = dict(H=h, T=t, L=l, Z=z, E1=e1, E2=e2, lopr=lopr)
            edge(l, t); edge(t, h); edge(z, t)
        toppo -= 2
    for (pl, i), d in V.items():
        tag = f"{'Odd' if pl else 'Even'}-{i}"; lopr = d["lopr"]
        prev = (d["T"],); chainA = []
        for j in range(i):
            s = new(lopr - 1, pl, f"{tag}-S-{j}"); a = new(lopr - 1, 1 - pl, f"{tag}-A-{j}"); b = new(lopr - 1, 1 - pl, f"{tag}-B-{j}")
            for p_ in prev: edge(p_, s)
            edge(s, a); edge(s, b); edge(a, V[(pl, j)]["L"]); edge(b, V[(1 - pl, j)]["L"]); prev = (a, b); chainA.append(a)
        for p_ in prev: edge(p_, d["Z"])
        for j in range(i + 1 - pl, n): edge(d["Z"], V[(1 - pl, j)]["L"])
        edge(d["H"], V[(pl, (i + n - 1) % n)]["L"])
        own_prev = V[(pl, (i + n - 1) % n)]; opp = V[(1 - pl, i)]; opp_prev = V[(1 - pl, (i + n - 1) % n)]; opp_next = V[(1 - pl, (i + 1) % n)]
        E = dict(zip(EDGES, on))
        if E["T>E1"]: edge(d["T"], d["E1"])
        if E["E1>T"]: edge(d["E1"], d["T"])
        if E["E1>Lown-1"]: edge(d["E1"], own_prev["L"])
        if E["E2>T"]: edge(d["E2"], d["T"])
        if E["L>E2"]: edge(d["L"], d["E2"])
        if E["E2>H"]: edge(d["E2"], d["H"])
        if E["Z>Lown-1"]: edge(d["Z"], own_prev["L"])
        if E["H>Lopp"]: edge(d["H"], opp["L"])
        if E["T>Lopp-1"]: edge(d["T"], opp_prev["L"])
        if E["E1>Z"]: edge(d["E1"], d["Z"])
        if E["A>E1"]:
            for a in chainA: edge(a, d["E1"])
        if E["Z>E2"]: edge(d["Z"], d["E2"])
        if E["H>E2"]: edge(d["H"], d["E2"])
        if E["E2>Lopp+1"]: edge(d["E2"], opp_next["L"])
        if E["E1>E2"]: edge(d["E1"], d["E2"])
        if E["E2>E1"]: edge(d["E2"], d["E1"])
        if E["E1>H"]: edge(d["E1"], d["H"])
        # every vertex needs a successor: give isolated extras a self-loop (owner's opponent parity makes it harmless? no: a
        # self-loop is a cycle of the vertex's own priority; E1 has pl's parity (winning for pl), E2 has 1-pl's parity)
        for x in (d["E1"], d["E2"]):
            if not succ[x]: edge(x, x)
    return pg.Game(prio, owner, [sorted(s) for s in succ], names)


def rand_tpl(rnd):
    return ([rnd.random() < 0.25 for _ in EDGES], rnd.choice([0, 2]), rnd.choice([0, 2, 3]), rnd.randrange(4), rnd.randrange(4), rnd.choice([0, -2]))


def mutate(t, rnd):
    on, a, b, c, d, e = list(t[0]), t[1], t[2], t[3], t[4], t[5]
    r = rnd.random()
    if r < 0.6: i = rnd.randrange(len(on)); on[i] = not on[i]
    elif r < 0.68: a = rnd.choice([0, 2])
    elif r < 0.76: b = rnd.choice([0, 2, 3])
    elif r < 0.84: c = rnd.randrange(4)
    elif r < 0.92: d = rnd.randrange(4)
    else: e = rnd.choice([0, -2])
    return (on, a, b, c, d, e)


def fit(t, n, solver="dtl"):
    g = build(t, n)
    return oink_fit.work(g, solver, raw=True, timeout=60)


def main():
    gens, seed = int(sys.argv[1]), int(sys.argv[2])
    opt = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
    nfit = int(opt("--nfit", 5)); pop_n = int(opt("--pop", 40)); ngrow = int(opt("--ngrow", 9)); solver = opt("--solver", "dtl")
    rnd = random.Random(seed)
    pop = sorted(((fit(t, nfit, solver), t) for t in (rand_tpl(rnd) for _ in range(pop_n))), key=lambda x: -x[0])
    t0 = time.time()
    for g in range(gens):
        elite = pop[:pop_n // 4]
        kids = [mutate(rnd.choice(elite)[1], rnd) for _ in range(pop_n - len(elite))]
        pop = sorted(elite + [(fit(t, nfit, solver), t) for t in kids], key=lambda x: -x[0])
        if g % 10 == 0 or g == gens - 1:
            print(f"gen {g}: best {solver} work at N={nfit}: {pop[0][0]} (plain tc: {2*nfit+1}); {time.time()-t0:.0f}s", flush=True)
    seen = set()
    for (f_, t) in pop[:5]:
        if str(t) in seen: continue
        seen.add(str(t))
        curve = []
        for N in range(2, ngrow + 1):
            g_ = build(t, N); w = oink_fit.work(g_, solver, raw=True, timeout=120); curve.append((N, g_.n, w))
            if w >= 10**9: break
        print(f"template on={[e for e, b in zip(EDGES, t[0]) if b]} prT={t[1]} prZ={t[2]} prE1={t[3]} prE2={t[4]} prL={t[5]}: (N, n, {solver}) = {curve}", flush=True)
        pg.write(build(t, 4), os.path.join(HERE, "out", f"tc_template_{solver}_s{seed}_{f_}.pg"))
    json.dump([dict(fit=f_, tpl=t) for (f_, t) in pop[:5]], open(os.path.join(HERE, "out", f"tc_template_{solver}_s{seed}.json"), "w"))


if __name__ == "__main__":
    main()
