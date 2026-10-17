#!/usr/bin/env python3
"""Template GA on the tc+ base (van Dijk's own rtl killer): per bit (pl, i) two extra vertices E1 (pl's parity) and E2
(opponent parity) and a menu of edges among the bit's H/T/I/Z, the extras, and the neighbouring bits' roles (found by
vertex labels of tcvar.tcplus). Fitness = Oink dtl tangles at N = NFIT with growth tie-break. Usage: tcplus_template_ga.py GENS SEED [--nfit 6] [--pop 36] [--ngrow 9]"""
import sys, os, json, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, oink_fit, tcvar

EDGES = ["T>E1", "E1>T", "E1>Iown-1", "E2>T", "I>E2", "E2>H", "Z>Iown-1", "H>Iopp", "T>Iopp-1", "E1>Z", "Z>E2", "H>E2", "E2>Iopp+1",
         "E1>E2", "E2>E1", "E1>H", "E1>Topp", "E1>Zopp", "E2>Zown-1", "T>Zopp", "Z>Topp", "I>Iopp", "E2>Iown", "Z>Zopp-1", "E1>Iopp+1", "Zk>E1", "E2>Zk"]


def build(tpl, n):
    on, prE1, prE2 = tpl
    g = tcvar.tcplus(n)
    prio, owner, succ, names = list(g.prio), list(g.owner), [sorted(set(s)) for s in g.succ], list(g.labels)
    idx = {nm: v for v, nm in enumerate(names)}
    def new(p, o, nm): prio.append(p); owner.append(o); succ.append([]); names.append(nm); return len(prio) - 1
    def edge(a, b):
        if b not in succ[a]: succ[a].append(b)
    E = dict(zip(EDGES, on))
    R = {}
    for i in range(n):
        for pl in (0, 1):
            tag = f"{'Odd' if pl else 'Even'}-{i}"
            R[(pl, i)] = dict(H=idx[tag + "-H"], T=idx[tag + "-T"], I=idx[tag + "-I0"], Z=idx[tag + "-Z"],
                              Zk=[idx[f"{tag}-{k}-Z"] for k in range(i + 1, n)],
                              E1=new(2 * prE1 + pl, pl, tag + "-E1"), E2=new(2 * prE2 + (1 - pl), 1 - pl, tag + "-E2"))
    for (pl, i), d in R.items():
        own_prev = R[(pl, (i - 1) % n)]; opp = R[(1 - pl, i)]; opp_prev = R[(1 - pl, (i - 1) % n)]; opp_next = R[(1 - pl, (i + 1) % n)]
        if E["T>E1"]: edge(d["T"], d["E1"])
        if E["E1>T"]: edge(d["E1"], d["T"])
        if E["E1>Iown-1"]: edge(d["E1"], own_prev["I"])
        if E["E2>T"]: edge(d["E2"], d["T"])
        if E["I>E2"]: edge(d["I"], d["E2"])
        if E["E2>H"]: edge(d["E2"], d["H"])
        if E["Z>Iown-1"]: edge(d["Z"], own_prev["I"])
        if E["H>Iopp"]: edge(d["H"], opp["I"])
        if E["T>Iopp-1"]: edge(d["T"], opp_prev["I"])
        if E["E1>Z"]: edge(d["E1"], d["Z"])
        if E["Z>E2"]: edge(d["Z"], d["E2"])
        if E["H>E2"]: edge(d["H"], d["E2"])
        if E["E2>Iopp+1"]: edge(d["E2"], opp_next["I"])
        if E["E1>E2"]: edge(d["E1"], d["E2"])
        if E["E2>E1"]: edge(d["E2"], d["E1"])
        if E["E1>H"]: edge(d["E1"], d["H"])
        if E["E1>Topp"]: edge(d["E1"], opp["T"])
        if E["E1>Zopp"]: edge(d["E1"], opp["Z"])
        if E["E2>Zown-1"]: edge(d["E2"], own_prev["Z"])
        if E["T>Zopp"]: edge(d["T"], opp["Z"])
        if E["Z>Topp"]: edge(d["Z"], opp["T"])
        if E["I>Iopp"]: edge(d["I"], opp["I"])
        if E["E2>Iown"]: edge(d["E2"], d["I"])
        if E["Z>Zopp-1"]: edge(d["Z"], opp_prev["Z"])
        if E["E1>Iopp+1"]: edge(d["E1"], opp_next["I"])
        if E["Zk>E1"]:
            for z in d["Zk"]: edge(z, d["E1"])
        if E["E2>Zk"]:
            for z in d["Zk"]: edge(d["E2"], z)
        for x in (d["E1"], d["E2"]):
            if not succ[x]: edge(x, x)
    return pg.Game(prio, owner, [sorted(s) for s in succ], names)


def fit(t, n):
    w = oink_fit.work(build(t, n), "dtl", raw=True, timeout=60)
    if w <= 0: return w
    w0 = max(1, oink_fit.work(build(t, max(2, n - 3)), "dtl", raw=True, timeout=60))
    return w * 1000 + min(999, int(1000 * w / w0 / 50))


def main():
    gens, seed = int(sys.argv[1]), int(sys.argv[2])
    opt = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
    nfit = int(opt("--nfit", 6)); pop_n = int(opt("--pop", 36)); ngrow = int(opt("--ngrow", 9))
    rnd = random.Random(seed)
    rand_tpl = lambda: ([rnd.random() < 0.2 for _ in EDGES], rnd.randrange(4), rnd.randrange(4))
    def mutate(t):
        on, a, b = list(t[0]), t[1], t[2]; r = rnd.random()
        if r < 0.75: i = rnd.randrange(len(on)); on[i] = not on[i]
        elif r < 0.87: a = rnd.randrange(4)
        else: b = rnd.randrange(4)
        return (on, a, b)
    pop = sorted(((fit(t, nfit), t) for t in (rand_tpl() for _ in range(pop_n))), key=lambda x: -x[0]); t0 = time.time()
    for g in range(gens):
        elite = pop[:pop_n // 4]
        kids = [mutate(rnd.choice(elite)[1]) for _ in range(pop_n - len(elite))]
        pop = sorted(elite + [(fit(t, nfit), t) for t in kids], key=lambda x: -x[0])
        if g % 10 == 0 or g == gens - 1:
            print(f"gen {g}: best fitness at N={nfit}: {pop[0][0]} (plain tc+ dtl at N={nfit}: {oink_fit.work(tcvar.tcplus(nfit), 'dtl')}); {time.time()-t0:.0f}s", flush=True)
    seen = set()
    for (f_, t) in pop[:4]:
        if str(t) in seen: continue
        seen.add(str(t)); curve = []
        for N in range(2, ngrow + 1):
            g_ = build(t, N); w = oink_fit.work(g_, "dtl", raw=True, timeout=120); curve.append((N, g_.n, w))
            if w >= 10**9: break
        print(f"template on={[e for e, b in zip(EDGES, t[0]) if b]} prE1={t[1]} prE2={t[2]}: (N, n, dtl) = {curve}", flush=True)
        pg.write(build(t, 4), os.path.join(HERE, "out", f"tcplus_template_s{seed}_{f_}.pg"))
    json.dump([dict(fit=f_, tpl=t) for (f_, t) in pop[:4]], open(os.path.join(HERE, "out", f"tcplus_template_s{seed}.json"), "w"))


if __name__ == "__main__":
    main()
