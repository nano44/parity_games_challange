#!/usr/bin/env python3
"""B5 (L-RED-B successor 4; docs/red-b/B5-second-fb.md §4): hill climb of the number of fallbacks k and of the iterations after the
first fallback (P1 = I - f_1) of N5 (SPEC, L-NEW's box190/n5v.py mode spec) from S3, on wrappers OUTSIDE Lemma ONE-FB's hypothesis:
L-SI's gscan104.wrapg wrappers (claude/l-si 2051a0ee, git archive) plus FREE Odd faces (b5lemma.build: o -> f1 .. f5 -> t, a second
non-valve successor of o in V_O; (A1) of ONE-FB fails there). Every candidate's output is checked against harness Zielonka; a wrong one
is written at once to work/b5wrong_<tag>.jsonl.
Modes:  rand nH  (H random with nH vertices and mutated, as gclimb.py; plus s0, rho0, gamma, free)
        fam NAME n  (H = a family member, fixed: fried | lmcs | hn; start = its own, rho0 = Odd's optimal counterstrategy; mutated:
                     s0, rho0, gamma, free)
Objectives: k (k, then P1, then I) | p1 (P1, then k, then I) | its (I).
Usage: b5climb.py B3ROOT OBJ SEED ITERS (rand nH | fam NAME n) [copy]   env CORE. Resumable: work/b5c_<tag>.json. Final line B5CLIMB."""
import sys, os, json, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import b5lemma as L
from b5lemma import GS, pg, n5v, n5, n5x, zielonka, Engine

def frun(g, cap=200000):
    E, Ed = Engine(g), Engine(n5.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None); its = 0; fl = []; tch = 0
    while its < cap:
        r = n5v.step(g, E, Ed, sigma, tau, "spec")
        if r is None: break
        ns, nt, _, _, fb = r; its += 1; tch += int(nt != list(tau))
        if fb: fl.append(its)
        sigma, tau = ns, nt
    vs, _ = E.evaluate(tuple(sigma)); win = [0 if g.prio[vs[v][0]] % 2 == 0 else 1 for v in range(g.n)]
    return dict(I=its, fl=fl, k=len(fl), P1=(its - fl[0]) if fl else 0, tch=tch, W=g.n, ok=(win == zielonka.solve(g)))

def game_of(D, Hfix):
    H = Hfix or pg.Game(D["prio"], D["own"], D["succ"]); n = H.n
    s0 = [D["s0"][str(v)] if H.owner[v] == 0 else -1 for v in range(n)]
    rho0 = {v: D["rho"][str(v)] for v in range(n) if H.owner[v] == 1}
    gamma = {tuple(map(int, k.split(","))): t for k, t in D["gam"].items()}
    free = {int(o): t for o, t in D["free"].items()}
    return L.build(H, s0, rho0, gamma, D["copy"], free or None)[0]

def fixup(rng, D, H):
    n = H.n; succ = H.succ
    D["s0"] = {str(v): D["s0"][str(v)] if str(v) in D["s0"] and D["s0"][str(v)] in succ[v] else rng.choice(succ[v]) for v in range(n) if H.owner[v] == 0}
    D["rho"] = {str(v): D["rho"][str(v)] if str(v) in D["rho"] and 0 <= D["rho"][str(v)] < n else rng.choice(succ[v]) for v in range(n) if H.owner[v] == 1}
    D["gam"] = {k: t for k, t in D["gam"].items() if H.owner[int(k.split(",")[0])] == 0 and int(k.split(",")[1]) in succ[int(k.split(",")[0])] and 0 <= t < n}
    D["free"] = {o: t for o, t in D["free"].items() if H.owner[int(o)] == 1 and 0 <= t < n}
    return D

def mutate(rng, D, Hfix):
    D = json.loads(json.dumps(D))
    ops = ["s0", "rho", "gam", "gamdel", "free", "free", "freedel"] + ([] if Hfix else ["prio", "own", "edge+", "edge-", "retarget"])
    op = rng.choice(ops)
    H = Hfix or pg.Game(D["prio"], D["own"], D["succ"]); n = H.n; v = rng.randrange(n)
    if op == "prio": u = rng.randrange(n); D["prio"][v], D["prio"][u] = D["prio"][u], D["prio"][v]
    elif op == "own": D["own"][v] ^= 1
    elif op == "edge+":
        if len(D["succ"][v]) < 4: D["succ"][v] = sorted(set(D["succ"][v] + [rng.randrange(n)]))
    elif op == "edge-":
        if len(D["succ"][v]) > 1: D["succ"][v].remove(rng.choice(D["succ"][v]))
    elif op == "retarget": s = D["succ"][v]; s[rng.randrange(len(s))] = rng.randrange(n); D["succ"][v] = sorted(set(s))
    elif op == "s0":
        if H.owner[v] == 0: D["s0"][str(v)] = rng.choice(H.succ[v])
    elif op == "rho":
        if H.owner[v] == 1: D["rho"][str(v)] = rng.choice(H.succ[v]) if rng.random() < 0.5 else rng.randrange(n)
    elif op == "gam":
        if H.owner[v] == 0: D["gam"]["%d,%d" % (v, rng.choice(H.succ[v]))] = rng.randrange(n)
    elif op == "gamdel":
        if D["gam"]: del D["gam"][rng.choice(list(D["gam"]))]
    elif op == "free":
        if H.owner[v] == 1: D["free"][str(v)] = rng.randrange(n)
    elif op == "freedel":
        if D["free"]: del D["free"][rng.choice(list(D["free"]))]
    H2 = Hfix or pg.Game(D["prio"], D["own"], D["succ"])
    return fixup(rng, D, H2)

def score(d, obj):
    if obj == "k": return (d["k"], d["P1"], d["I"], -d["W"])
    if obj == "p1": return (d["P1"], d["k"], d["I"], -d["W"])
    if obj == "its": return (d["I"], -d["W"])
    raise ValueError(obj)

def main():
    obj, seed, iters, mode = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    rng = random.Random(seed)
    if mode == "rand":
        nH = int(sys.argv[6]); rest = sys.argv[7:]; Hfix = None; tag = "%s_rand_n%d_s%d" % (obj, nH, seed)
    else:
        name, nH = sys.argv[6], int(sys.argv[7]); rest = sys.argv[8:]; Hfix, s0b = L.fam(name, nH); tag = "%s_%s_n%d_s%d" % (obj, name, nH, seed)
    copy = (rest[0] == "1") if rest else True; tag += "_c%d_%s" % (int(copy), L.CORE)
    os.makedirs("work", exist_ok=True); sf = "work/b5c_%s.json" % tag; wf = open("work/b5wrong_%s.jsonl" % tag, "a")
    if os.path.exists(sf):
        S = json.load(open(sf)); D = S["D"]; it0 = S["it"]; rng.seed(seed * 7919 + it0)
    elif Hfix:
        _, cs = Engine(Hfix).evaluate(tuple(s0b[v] if Hfix.owner[v] == 0 else -1 for v in range(Hfix.n)))
        D = {"s0": {str(v): s0b[v] for v in range(Hfix.n) if Hfix.owner[v] == 0},
             "rho": {str(v): cs[v] for v in range(Hfix.n) if Hfix.owner[v] == 1}, "gam": {}, "free": {}, "copy": copy}; it0 = 0
    else:
        H = L.rand_H(rng, nH); D = {"prio": list(H.prio), "own": list(H.owner), "succ": [list(s) for s in H.succ], "s0": {}, "rho": {},
                                    "gam": {}, "free": {}, "copy": copy}; D = fixup(rng, D, H); it0 = 0
    d = frun(game_of(D, Hfix)); best = score(d, obj); t0 = time.time(); nwrong = 0
    print("start I %d k %d P1 %d |Wg| %d" % (d["I"], d["k"], d["P1"], d["W"]), flush=True)
    for it in range(it0, iters):
        E = D
        for _ in range(rng.randint(1, 3)): E = mutate(rng, E, Hfix)
        try: d2 = frun(game_of(E, Hfix))
        except Exception as ex: continue
        if not d2["ok"]:
            nwrong += 1; wf.write(json.dumps({"D": E, "d": d2}) + "\n"); wf.flush(); print("WRONG it %d" % it, flush=True)
        s = score(d2, obj)
        if s >= best:
            if s[:3] > best[:3]:
                print("it %d I %d k %d P1 %d fallbacks %s tau-changes %d |Wg| %d free %d" % (it, d2["I"], d2["k"], d2["P1"], d2["fl"][:10],
                      d2["tch"], d2["W"], len(E["free"])), flush=True)
            D, best, d = E, s, d2
        if it % 20 == 0: json.dump({"D": D, "it": it + 1, "d": d}, open(sf, "w"))
    json.dump({"D": D, "it": iters, "d": d}, open(sf, "w"))
    print("B5CLIMB %s I %d k %d P1 %d fallbacks %s tau-changes %d |Wg| %d free %d wrong %d %.0fs" % (tag, d["I"], d["k"], d["P1"],
          d["fl"][:12], d["tch"], d["W"], len(D["free"]), nwrong, time.time() - t0), flush=True)

if __name__ == "__main__":
    main()
