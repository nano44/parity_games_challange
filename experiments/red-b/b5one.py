#!/usr/bin/env python3
"""B5 §6 (L-RED-B successor 4): the post-fallback phase in isolation. By Lemma ONE-FB′ the run after a guided wrapper's close is a
ONE-PLAYER run (Odd fixed at tau0): S4a = Even's optimum inside {current} ∪ improving edges. Here N5 itself (SPEC, L-NEW's box190/n5v.py
mode spec) runs from its default start S3 on one-player parity games H (every Odd vertex has exactly one successor; Odd vertices are
allowed as pass-through vertices), and a hill climb maximises the iteration count I. A family on which I grows super-polynomially
would be a family of parity games on which N5 from S3 is super-polynomial. Every candidate's output is checked against harness
Zielonka (wrong -> work/b5one_wrong_<tag>.jsonl at once). Moves: swap priorities, retarget / add / remove an Even edge, flip an owner
(an Odd vertex keeps only its first successor).
Usage: b5one.py B3ROOT SEED ITERS n [maxdeg]     Resumable: work/b5one_<tag>.json. Final line B5ONE ...
       b5one.py B3ROOT --verify OUTDIR STATEFILE...  (best on n5b --mode spec + Zielonka, .pg with sha1)"""
import sys, os, json, random, time, re, hashlib, subprocess
sys.argv, rest = sys.argv[:2], sys.argv[2:]
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import b5lemma as L
from b5lemma import pg, n5v, n5, n5x, zielonka, Engine

def game(D):
    succ = [list(s) if D["own"][v] == 0 else [s[0]] for v, s in enumerate(D["succ"])]
    return pg.Game(list(D["prio"]), list(D["own"]), succ)

def frun(g, cap=10 ** 6):
    E, Ed = Engine(g), Engine(n5.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None); its = 0; fl = []
    while its < cap:
        r = n5v.step(g, E, Ed, sigma, tau, "spec")
        if r is None: break
        sigma, tau, _, _, fb = r; its += 1
        if fb: fl.append(its)
    vs, _ = E.evaluate(tuple(sigma)); win = [0 if g.prio[vs[v][0]] % 2 == 0 else 1 for v in range(g.n)]
    return dict(I=its, fl=fl, ok=(win == zielonka.solve(g)))

def rand_D(rng, n, maxdeg):
    prio = list(range(n)); rng.shuffle(prio); own = [int(rng.random() < 0.2) for _ in range(n)]
    succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, maxdeg)))) for _ in range(n)]
    return {"prio": prio, "own": own, "succ": succ}

def mutate(rng, D, maxdeg):
    D = json.loads(json.dumps(D)); n = len(D["prio"]); v = rng.randrange(n)
    op = rng.choice(["prio", "prio", "edge+", "edge-", "retarget", "retarget", "own"])
    if op == "prio": u = rng.randrange(n); D["prio"][u], D["prio"][v] = D["prio"][v], D["prio"][u]
    elif op == "edge+":
        if len(D["succ"][v]) < maxdeg: D["succ"][v] = sorted(set(D["succ"][v] + [rng.randrange(n)]))
    elif op == "edge-":
        if len(D["succ"][v]) > 1: D["succ"][v].remove(rng.choice(D["succ"][v]))
    elif op == "retarget": s = D["succ"][v]; s[rng.randrange(len(s))] = rng.randrange(n); D["succ"][v] = sorted(set(s))
    elif op == "own": D["own"][v] ^= 1
    return D

def verify(out, files):
    os.makedirs(out, exist_ok=True); tw = te = 0
    for sf in files:
        tag = os.path.basename(sf)[len("b5one_"):-len(".json")]; g = game(json.load(open(sf))["D"])
        path = os.path.join(out, "one_" + tag + ".pg"); pg.write(g, path); sha = hashlib.sha1(open(path, "rb").read()).hexdigest()
        d = frun(g); r = subprocess.run([sys.executable, L.N5B, path, "--mode", "spec"], capture_output=True, text=True)
        m = re.search(r"iterations (\d+) fallbacks (\d+)", r.stdout)
        w = int(not d["ok"]); e = int(not m or (int(m.group(1)), int(m.group(2))) != (d["I"], len(d["fl"]))); tw += w; te += e
        print("B5ONEVERIFY %s n %d sha1 %s | n5v I %d k %d | n5b %s | wrong %d engdiff %d" % (tag, g.n, sha, d["I"], len(d["fl"]),
              ("I %s k %s" % m.groups()) if m else "FAILED", w, e), flush=True)
    print("B5ONEVERIFY SUMMARY games %d wrong %d engdiff %d" % (len(files), tw, te), flush=True)

def main():
    if rest[0] == "--verify": return verify(rest[1], rest[2:])
    seed, iters, n = int(rest[0]), int(rest[1]), int(rest[2]); maxdeg = int(rest[3]) if len(rest) > 3 else 3
    tag = "n%d_d%d_s%d" % (n, maxdeg, seed); os.makedirs("work", exist_ok=True); sf = "work/b5one_%s.json" % tag
    wf = open("work/b5one_wrong_%s.jsonl" % tag, "a"); rng = random.Random(seed)
    if os.path.exists(sf): S = json.load(open(sf)); D = S["D"]; it0 = S["it"]; rng.seed(seed * 7919 + it0)
    else: D = rand_D(rng, n, maxdeg); it0 = 0
    d = frun(game(D)); best = d["I"]; t0 = time.time(); nw = 0
    for it in range(it0, iters):
        E = D
        for _ in range(rng.randint(1, 3)): E = mutate(rng, E, maxdeg)
        d2 = frun(game(E))
        if not d2["ok"]: nw += 1; wf.write(json.dumps({"D": E, "d": d2}) + "\n"); wf.flush(); print("WRONG it %d" % it, flush=True)
        if d2["I"] >= best:
            if d2["I"] > best: print("it %d I %d k %d" % (it, d2["I"], len(d2["fl"])), flush=True)
            D, best, d = E, d2["I"], d2
        if it % 50 == 0: json.dump({"D": D, "it": it + 1, "d": d}, open(sf, "w"))
    json.dump({"D": D, "it": iters, "d": d}, open(sf, "w"))
    print("B5ONE %s I %d k %d fallbacks %s wrong %d %.0fs" % (tag, d["I"], len(d["fl"]), d["fl"][:8], nw, time.time() - t0), flush=True)

if __name__ == "__main__":
    main()
