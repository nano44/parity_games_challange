#!/usr/bin/env python3
"""L-SI box 7: DATA check of Lemma MONO (docs/si/N5-C-box7.md §2). For every transition j -> j+1 of an N5 run:
  M_j  = max level of a gate edge (Ξ_j-improving Even edge) at j, lev(Ξ_j(σ_j y), Ξ_j(z)) (INF = cycle nodes differ, -1 length only;
  box 9: INF was 99, which misread ranks >= 99 at n >= 100);
  NC_j = every cycle of the (σ_{j+1}, σ̄_j)-graph has its top vertex (largest rank) a cycle node of the (σ_j, σ̄_j)-graph.
Checks: NC_j  =>  COARSE_{M_j}(Ω_{σ_{j+1}, σ̄_j}) = COARSE_{M_j}(Ξ_j) = COARSE_{M_j}(Ξ_{j+1}) pointwise, and M_{j+1} <= M_j.
Also: NC fails exactly when COARSE(Ω_{σ_{j+1}, σ̄_j}) differs (the converse half of COARSE-SI), and, on one-Odd-choice games, every
NC failure inside a joint λ-phase has a new cycle through o. Runs are asserted equal to experiments/new/n5.py run().
Usage: mono.py game.pg ...   |   mono.py --random SEED COUNT NMIN NMAX   (random games, any class, phase-free checks only)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments/new")); sys.path.insert(0, os.path.join(ROOT, "experiments/si"))
sys.path.insert(0, os.path.join(ROOT, "experiments/harness"))
import pg, n5
from si import Engine

INF = 10 ** 6      # the level ∞ (cycle nodes differ); above every rank

def lev(a, b):
    if a[0] != b[0]: return INF
    d = a[1] ^ b[1]
    if not d: return -1 if a[2] != b[2] else -2
    return d.bit_length() - 1

def coarse(val, L):
    if L >= INF: return ()
    return (val[0], val[1] >> (L + 1)) if L >= -1 else (val[0], val[1], val[2])

def states(g, start=None):
    """σ_0, σ_1, ... of n5.run (same loop; asserted against n5.run's (iterations, fallbacks))."""
    E, Ed = n5.Engine(g), n5.Engine(n5.dual(g)); n = g.n
    sigma, tau = list(E.initial("best")), list(Ed.initial("best"))
    if start:
        for v, w in start[0].items(): sigma[v] = w
        for v, w in start[1].items(): tau[v] = w
    out = []; fb = 0
    while True:
        vs, sb = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        vt, tb = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
        out.append(dict(s=tuple(sigma), t=tuple(tau), Xi=vs, sb=sb, Is=Is, fb=False))
        if not Is and not It: break
        ns, nt = list(sigma), list(tau)
        if Is:
            opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
            for v, w in Is: opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
            Er = Engine(n5.dual(pg.Game(list(g.prio), list(g.owner), succ)))
            _, best = Er.evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] == 0: ns[v] = best[v]
        if It:
            opt = {v: {tau[v]} for v in range(n) if g.owner[v] == 1}
            for v, w in It: opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 1 else [sigma[v]] for v in range(n)]
            Er = Engine(pg.Game(list(g.prio), list(g.owner), succ))
            _, best = Er.evaluate(tuple(sigma[v] if g.owner[v] == 0 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] == 1: nt[v] = best[v]
        if ns == sigma and nt == tau:
            fb += 1; out[-1]["fb"] = True
            if Is:
                for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
            else:
                for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
        sigma, tau = ns, nt
    it, fb2 = n5.run(g, "n5", start)[:2]
    assert (it, fb2) == (len(out) - 1, fb), ((it, fb2), (len(out) - 1, fb))
    return E, out

def cycles(g, s, sb):
    """cycles of the functional graph v -> s[v] (Even) / sb[v] (Odd), as vertex lists."""
    nxt = lambda v: s[v] if g.owner[v] == 0 else sb[v]
    col = [0] * g.n; cyc = []
    for v in range(g.n):
        p = []; u = v
        while col[u] == 0: col[u] = 1; p.append(u); u = nxt(u)
        if col[u] == 1:
            c = p[p.index(u):]; cyc.append(c)
        for x in p: col[x] = 2
    return cyc

def scan(g, start=None, oc=None):
    E, out = states(g, start); rk = E.rank; c = dict(tr=0, nc=0, ncfail=0, viol_coarse=0, viol_M=0, viol_conv=0,
                                                   ncfail_inphase=0, ncfail_inphase_no_o=0, Mdown=0, Mup=0)
    ex = []
    for j in range(len(out) - 1):
        a, b = out[j], out[j + 1]; c["tr"] += 1
        gl = [lev(a["Xi"][a["s"][y]], a["Xi"][z]) for y, z in a["Is"]]; M = max(gl) if gl else -3
        lam = [a["Xi"][v][0] for v in range(g.n)]
        cyc = cycles(g, b["s"], a["sb"]); tops = [max(C, key=lambda v: rk[v]) for C in cyc]
        nc = all(lam[t] == t for t in tops)
        Ve = E.evaluate(tuple(b["s"]))  # (Ξ_{j+1}, σ̄_{j+1})
        # Ω_{σ_{j+1}, σ̄_j}: evaluate the one-player game with Odd fixed to σ̄_j
        G1 = pg.Game(list(g.prio), list(g.owner), [[a["sb"][v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(g.n)])
        E1 = Engine(G1); V, _ = E1.evaluate(tuple(b["s"][v] if g.owner[v] == 0 else -1 for v in range(g.n)))
        L = M
        eqV = all(coarse(V[v], L) == coarse(a["Xi"][v], L) for v in range(g.n))
        eqX = all(coarse(b["Xi"][v], L) == coarse(a["Xi"][v], L) for v in range(g.n))
        gl1 = [lev(b["Xi"][b["s"][y]], b["Xi"][z]) for y, z in b["Is"]]; M1 = max(gl1) if gl1 else -3
        if nc:
            c["nc"] += 1
            if not (eqV and eqX): c["viol_coarse"] += 1; ex.append(("coarse", j))
            if M1 > M: c["viol_M"] += 1; ex.append(("M", j, M, M1))
        else:
            c["ncfail"] += 1
            if eqV and M < INF: c["viol_conv"] += 1; ex.append(("conv", j))
            if oc is not None and a["Xi"] is not None:
                same_phase = [x[0] for x in a["Xi"]] == [x[0] for x in b["Xi"]] and a["t"] == b["t"]
                if same_phase:
                    c["ncfail_inphase"] += 1
                    bad = [C for C, t in zip(cyc, tops) if lam[t] != t]
                    if not all(oc in C for C in bad): c["ncfail_inphase_no_o"] += 1; ex.append(("no-o", j))
        if M1 < M: c["Mdown"] += 1
        if M1 > M: c["Mup"] += 1
    return c, ex

def load(path): return pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%")))

def odd_choice(g):
    oc = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1]
    return oc[0] if len(oc) == 1 else None

if __name__ == "__main__":
    T = {}
    if sys.argv[1] == "--random":
        seed, cnt, a, b = map(int, sys.argv[2:6]); rnd = random.Random(seed); EX = []
        for i in range(cnt):
            n = rnd.randint(a, b)
            prio = [rnd.randrange(n) for _ in range(n)]; own = [rnd.randrange(2) for _ in range(n)]
            succ = [sorted(set(rnd.sample(range(n), rnd.randint(1, min(3, n))))) for _ in range(n)]
            g = pg.Game(prio, own, succ); c, ex = scan(g, oc=odd_choice(g))
            for k, v in c.items(): T[k] = T.get(k, 0) + v
            EX += ex
        print("random", seed, cnt, T, EX[:5])
    else:
        for p in sys.argv[1:]:
            g = load(p); oc = odd_choice(g); assert oc is not None, f"{p}: not one-Odd-choice"; c, ex = scan(g, oc=oc)
            for k, v in c.items(): T[k] = T.get(k, 0) + v
            print(f"{os.path.basename(p):22s} n {g.n:3d} 1O {oc is not None}", c, ex[:3])
        print("TOTAL", T)
