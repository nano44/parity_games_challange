#!/usr/bin/env python3
"""B4 (L-RED-B successor 3; docs/red-b/B4-postfb.md §2 (b)): gfam.py with the objective P1 = I - f_1 (iterations AFTER the first
fallback; 0 if none), ties by I. Otherwise as gfam.py: climb N5's (SPEC) iteration count on guided wrappers of a FIXED family member H (Friedmann's games, on
which Howard is exponential), mutating only the guide: the Even start s0, the frozen Odd faces rho0 (any vertex of H, also a vertex
that is not a successor: a face that «disagrees with Odd's true reply») and the face targets gamma of Even edges. Wrapper and run:
L-SI's gscan104.wrapg / run (claude/l-si 2051a0ee, git archive), N5 = L-NEW's box190/n5v.py mode spec; correctness against harness
Zielonka on Wg inside run. Families: fried (PGSolver switchallexp_n via L-NEW's hard-families/pgsolver_port.py, best-reward start),
lmcs (G_n of arXiv 1106.0778v2 with Figure 4 priorities, iota start; wrap104.lmcs_game; B3ROOT/llit = claude/l-lit 5c53efbd\ndocs/lit/T66-depth-check.py), hn (H_n of its Section 8.4, L-COMP's hn.py mode fig, iota; B3ROOT/lcomp = claude/l-comp aa863db5\nexperiments/friedmann-hn).
Usage: b4climb.py B3ROOT FAMILY n seed iters [copy]    Resumable: work/b4c_b4_<tag>.json. Final line B4CLIMB ..."""
import sys, os, json, random, time
root = os.path.abspath(sys.argv[1])
os.environ["LNEW"] = os.path.join(root, "lnew"); os.environ["LRED"] = os.path.join(root, "lred")
os.environ["LLIT"] = os.path.join(root, "llit"); os.environ["HN"] = os.path.join(root, "lcomp/experiments/friedmann-hn")
sys.path.insert(0, os.path.join(root, "lsi/experiments/si/box104"))
import gscan104 as GS
import wrap104 as W

def family(name, n):
    if name == "fried":
        r = W.fried_game(n); return r[0], list(r[1])
    if name == "lmcs":
        H, s0 = W.lmcs_game(n, "fig4"); return H, list(s0)
    if name == "hn":
        H, s0 = GS.fam("hn", n); return H, list(s0)
    raise ValueError(name)

def main():
    name, n, seed, iters = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    copy = (sys.argv[6] == "1") if len(sys.argv) > 6 else True
    H, s0base = family(name, n)
    from si import Engine
    EH = Engine(H); _, cs = EH.evaluate(tuple(s0base[v] if H.owner[v] == 0 else -1 for v in range(H.n)))
    tag = "b4_%s_n%d_s%d_c%d" % (name, n, seed, int(copy)); os.makedirs("work", exist_ok=True)
    sf = "work/b4c_%s.json" % tag; wf = open("work/b4cwrong_%s.jsonl" % tag, "a")
    rng = random.Random(seed)
    ev = [v for v in range(H.n) if H.owner[v] == 0]; od = [v for v in range(H.n) if H.owner[v] == 1]
    def run(G):
        s0 = [G["s0"].get(str(v), -1) if H.owner[v] == 0 else -1 for v in range(H.n)]
        rho0 = {v: G["rho"][str(v)] for v in od}
        gamma = {tuple(map(int, k.split(","))): t for k, t in G["gam"].items()}
        return GS.run(H, s0, rho0, cap=200000, gamma=gamma, copy=copy)
    if os.path.exists(sf):
        S = json.load(open(sf)); G = S["G"]; it0 = S["it"]; rng.seed(seed * 7919 + it0)
    else:
        G = {"s0": {str(v): s0base[v] for v in ev}, "rho": {str(v): cs[v] for v in od}, "gam": {}}; it0 = 0
    P1 = lambda d: (d["its"] - d["F1"]) if d["F1"] else 0
    sc = lambda d: (P1(d), d["its"])
    d = run(G); best = sc(d); t0 = time.time(); nwrong = 0
    print("start its %d F1 %s |Wg| %d" % (d["its"], d["F1"], d["W"]), flush=True)
    for it in range(it0, iters):
        E = json.loads(json.dumps(G))
        for _ in range(rng.randint(1, 3)):
            op = rng.choice(["s0", "rho", "rho", "gam", "gam", "gamdel"])
            if op == "s0" and ev:
                v = rng.choice(ev); E["s0"][str(v)] = rng.choice(H.succ[v])
            elif op == "rho" and od:
                v = rng.choice(od); E["rho"][str(v)] = rng.choice(H.succ[v]) if rng.random() < 0.5 else rng.randrange(H.n)
            elif op == "gam" and ev:
                v = rng.choice(ev); w = rng.choice(H.succ[v]); E["gam"]["%d,%d" % (v, w)] = rng.randrange(H.n)
            elif op == "gamdel" and E["gam"]:
                del E["gam"][rng.choice(list(E["gam"]))]
        try: d2 = run(E)
        except Exception: continue
        if not d2["ok"]:
            nwrong += 1; wf.write(json.dumps({"G": E, "d": d2}) + "\n"); wf.flush(); print("WRONG it %d" % it, flush=True)
        if sc(d2) >= best:
            if sc(d2) > best:
                print("it %d P1 %d its %d F1 %s fbs %d hsteps %d hmoves %d tauch %d" % (it, P1(d2), d2["its"], d2["F1"], d2["fbs"], d2["hsteps"],
                      d2["hmoves"], d2["tauch"]), flush=True)
            G, best, d = E, sc(d2), d2
        if it % 20 == 0: json.dump({"G": G, "it": it + 1, "d": d}, open(sf, "w"))
    json.dump({"G": G, "it": iters, "d": d}, open(sf, "w"))
    print("B4CLIMB %s |H| %d P1 %d its %d F1 %s fbs %d |Wg| %d hsteps %d wrong %d %.0fs" % (tag, H.n, P1(d), d["its"], d["F1"], d["fbs"], d["W"],
          d["hsteps"], nwrong, time.time() - t0), flush=True)

if __name__ == "__main__":
    main()
