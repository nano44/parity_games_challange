#!/usr/bin/env python3
"""L-SI succ. 7, box 12: DATA search for an in-scope THR fallback with M = -1 (setting (LV) of P-N5-LV), and for a (β) gate there.
A state k is counted when: S4a and S4b both return (σ_k, τ_k) (fallback, Even switches), (h) at k and k+1, k -> k+1 in phase
(λ_Ξ, τ, λ of the dual valuation unchanged, as reltrace.runs_of), w_{k+1} = w_k, θ_k ◁ w_k (THR), and every gate has level -1.
Gate kinds as LV-SHAPE: (β) y ∈ R_k, z ∈ F_k; (α) s, z ∈ F_k; (γ) s ∈ F_k, z ∈ R̄_k; other.
Modes:
  betasearch.py states SEED COUNT NMIN NMAX   random 𝒞^1O games, random (σ, τ) as the state k (not necessarily reachable from S3)
  betasearch.py runs   SEED COUNT NMIN NMAX   random 𝒞^1O games, every state of the N5 run from S3's start (reltrace.runs_of)
  betasearch.py corpus SEED PERT FILE...      every transition of the N5 run of each game, plus PERT random perturbations of each run
                                              state (σ changed at 1-3 Even vertices, τ(o) changed with prob. 1/3), each perturbed state
                                              taken as a start pair (SPEC allows one) and tested as the state k
Prints counters and the first examples (game in pgsolver format + σ, τ)."""
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "coarse"))
from reltrace import *
from mono import lev, INF

def rand_game(rng, n):
    """Random 𝒞^1O game: exactly one Odd vertex (o = 0 here, relabelled by rank only) with out-degree > 1."""
    while True:
        prio = [rng.randrange(n + 2) for _ in range(n)]
        owner = [0] * n
        for v in range(1, n):
            if rng.random() < 0.3: owner[v] = 1
        owner[0] = 1
        succ = []
        for v in range(n):
            if owner[v] == 1 and v != 0: succ.append([rng.randrange(n)])
            else:
                k = rng.choice((1, 2, 2, 3)) if v else rng.choice((2, 2, 3))
                succ.append(sorted(set(rng.sample(range(n), min(k, n)))))
        if len(set(succ[0])) < 2: continue
        return pg.Game(prio, owner, succ)

def tailored_game(rng, n):
    """𝒞^1O game for the (β) shape: o = 0 of priority 0; mostly low priorities (0-3); a few high ones (n..n+4) so that rank o < rank c."""
    while True:
        prio = [rng.choice((0, 1, 2, 3, 0, 1)) for _ in range(n)]; prio[0] = 0
        for v in rng.sample(range(1, n), rng.randint(1, 3)): prio[v] = n + rng.randrange(5)
        owner = [0] * n
        for v in range(1, n):
            if rng.random() < 0.25: owner[v] = 1
        owner[0] = 1; succ = []
        for v in range(n):
            if owner[v] == 1 and v != 0: succ.append([rng.randrange(n)])
            else:
                k = rng.choice((1, 2, 2, 3)) if v else rng.choice((2, 2, 3))
                succ.append(sorted(set(rng.sample(range(n), min(k, n)))))
        if len(set(succ[0])) < 2: continue
        return pg.Game(prio, owner, succ)

def step(g, E, Ed, sigma, tau):
    """One N5 iteration from (sigma, tau): returns (vs, sb, Is, It, fb, sigma', tau')."""
    n = g.n
    vs, sb = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
    vt, tb = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
    if not Is and not It: return vs, sb, Is, It, None, None, None
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
    fb = ns == list(sigma) and nt == list(tau)
    if fb:
        if Is:
            for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
        else:
            for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
    return vs, sb, Is, It, fb, tuple(ns), tuple(nt)

def info(g, E, Ed, o, s, t):
    vs, sb, Is, It, fb, ns, nt = step(g, E, Ed, s, t)
    _, W = wvals(g, s, t); R = reach(g, s, t, o)
    h = (not oncycle(g, s, sb, o)) and (not oncycle(g, s, t, o)) and vs[o][0] == W[o][0]
    key = (tuple(x[0] for x in vs), tuple(t), tuple(x[0] for x in Ed.evaluate(tuple(t))[0]))
    return dict(s=s, t=t, Xi=vs, sb=sb, Is=Is, It=It, fb=fb, ns=ns, nt=nt, W=W, R=R, h=h, key=key)

def classify(g, o, a, b):
    """None unless a -> b is an in-scope THR Even fallback; else (r, M, kinds)."""
    if not a["fb"] or not a["Is"]: return "nofb"
    if not a["h"]: return "fb_noh"
    if not b["h"] or a["key"] != b["key"] or a["W"][o] != b["W"][o]: return "fb_h_notscope"
    r = lev(a["Xi"][o], a["W"][o])
    if r <= -2: return "EQ"
    if E_key(a["Xi"][o]) >= E_key(a["W"][o]): return "theta>=w"
    Rb = a["R"] | {o}; kinds = []; M = -3
    for y, z in a["Is"]:
        l = lev(a["Xi"][a["s"][y]], a["Xi"][z]); M = max(M, l)
        sy = a["s"][y]
        if y in a["R"] and z not in Rb: kinds.append("beta")
        elif sy not in Rb and z not in Rb: kinds.append("alpha")
        elif sy not in Rb and z in Rb: kinds.append("gamma")
        else: kinds.append("other")
    return r, M, kinds

E_key = None

def dump(g, a):
    lines = [f"parity {g.n - 1};"] + [f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};" for v in range(g.n)]
    return "\n".join(lines) + f"\n% sigma {list(a['s'])}\n% tau {list(a['t'])}"

def main(mode, seed, count, nmin, nmax):
    global E_key
    rng = random.Random(seed); C = Counter(); ex = {}
    for it in range(count):
        n = rng.randint(nmin, nmax); g = rand_game(rng, n); o = 0
        E, Ed = n5.Engine(g), n5.Engine(n5.dual(g)); E_key = E.key
        if mode in ("starts", "tstarts"):
            if mode == "tstarts": g = tailored_game(rng, n); E, Ed = n5.Engine(g), n5.Engine(n5.dual(g)); E_key = E.key
            st = ({v: rng.choice(g.succ[v]) for v in range(n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(n) if g.owner[v] == 1})
            try: _, out = states(g, st)
            except AssertionError: C["assert"] += 1; continue
            pairs = []
            for i in range(len(out) - 1):
                if not out[i]["fb"]: continue
                a = info(g, E, Ed, o, out[i]["s"], out[i]["t"]); b = info(g, E, Ed, o, out[i + 1]["s"], out[i + 1]["t"])
                pairs.append((a, b))
        elif mode == "states":
            s = tuple(rng.choice(g.succ[v]) if g.owner[v] == 0 else -1 for v in range(n))
            t = tuple(rng.choice(g.succ[v]) if g.owner[v] == 1 else -1 for v in range(n))
            a = info(g, E, Ed, o, s, t)
            if a["fb"] is None or not a["fb"]: C["notfb"] += 1; continue
            b = info(g, E, Ed, o, a["ns"], a["nt"]); pairs = [(a, b)]
        else:
            try: _, out = states(g)
            except AssertionError: C["assert"] += 1; continue
            pairs = []
            for i in range(len(out) - 1):
                a = info(g, E, Ed, o, out[i]["s"], out[i]["t"]); b = info(g, E, Ed, o, out[i + 1]["s"], out[i + 1]["t"])
                pairs.append((a, b))
        for a, b in pairs:
            c = classify(g, o, a, b)
            C["pairs"] += 1
            if isinstance(c, str): C[c] += 1; continue
            r, M, kinds = c; C["THR"] += 1
            rk = sorted(range(g.n), key=lambda u: (g.prio[u], u)); rk = {v: i for i, v in enumerate(rk)}
            if rk[o] < rk[a["Xi"][o][0]]: C["THR_rank_o<c"] += 1
            if M >= 0: C["THR_M>=0"] += 1; continue
            tag = "LV_r>=0" if r >= 0 else "LV_r=-1"; C[tag] += 1
            for kd in set(kinds): C[f"{tag}_{kd}"] += 1
            key = tag + ("_beta" if "beta" in kinds else "")
            if key not in ex: ex[key] = (dump(g, a), r, M, kinds, a["Is"])
    print("TOTAL", dict(C))
    for k, v in ex.items(): print("EXAMPLE", k, "r", v[1], "M", v[2], v[3], v[4]); print(v[0])

def corpus(seed, pert, files):
    global E_key
    rng = random.Random(seed); C = Counter(); ex = {}
    for p in files:
        g = load(p); o = odd_choice(g)
        if o is None or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1) != 1: C["skip_class"] += 1; continue
        E, Ed = n5.Engine(g), n5.Engine(n5.dual(g)); E_key = E.key
        try: _, out = states(g)
        except AssertionError: C["assert"] += 1; continue
        ev = [v for v in range(g.n) if g.owner[v] == 0 and len(set(g.succ[v])) > 1]
        cands = []
        for i in range(len(out) - 1): cands.append(("run", out[i]["s"], out[i]["t"]))
        for i in range(len(out)):
            for _ in range(pert):
                s, t = list(out[i]["s"]), list(out[i]["t"])
                for v in rng.sample(ev, min(len(ev), rng.randint(1, 3))): s[v] = rng.choice(g.succ[v])
                if rng.random() < 1 / 3: t[o] = rng.choice(g.succ[o])
                cands.append(("pert", tuple(s), tuple(t)))
        for src, s, t in cands:
            a = info(g, E, Ed, o, s, t)
            if not a["fb"]: C[src + "_nofb"] += 1; continue
            b = info(g, E, Ed, o, a["ns"], a["nt"]); c = classify(g, o, a, b)
            if isinstance(c, str): C[src + "_" + c] += 1; continue
            r, M, kinds = c; C[src + "_THR"] += 1
            rk = sorted(range(g.n), key=lambda u: (g.prio[u], u)); rk = {v: i for i, v in enumerate(rk)}
            if rk[o] < rk[a["Xi"][o][0]]: C[src + "_THR_rank_o<c"] += 1
            if any(y in a["R"] and z not in (a["R"] | {o}) for y, z in a["Is"]): C[src + "_THR_hasRF"] += 1
            if M >= 0: C[src + "_THR_M>=0"] += 1; continue
            tag = src + ("_LV_r>=0" if r >= 0 else "_LV_r=-1"); C[tag] += 1
            for kd in set(kinds): C[f"{tag}_{kd}"] += 1
            key = tag + ("_beta" if "beta" in kinds else "")
            if key not in ex: ex[key] = (os.path.basename(p) + "\n" + dump(g, a), r, M, kinds, a["Is"])
    print("TOTAL", dict(sorted(C.items())))
    for k, v in ex.items(): print("EXAMPLE", k, "r", v[1], "M", v[2], v[3], v[4]); print(v[0])

if __name__ == "__main__":
    if sys.argv[1] == "corpus": corpus(int(sys.argv[2]), int(sys.argv[3]), sys.argv[4:]); sys.exit()
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
