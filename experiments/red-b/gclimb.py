#!/usr/bin/env python3
"""B3 (L-RED-B successor 3): GUIDE-RULE kill attempt on N5 itself. Hill climb of N5's iteration count (SPEC S1-S5, mode "spec" of
L-NEW's box190/n5v.py, run through L-SI's box 104 tool gscan104.py: the guided wrapper Wg(H, s0, rho0) with face targets gamma)
over small parity games H, Even starts s0, frozen Odd faces rho0 and face targets gamma (the fixed face of the Even edge (v, w) leads
to gamma(v, w), which may differ from w: «frozen faces that disagree with Odd's true reply»). Every candidate is also checked for
correctness (regions of N5's output = harness Zielonka on Wg, inside gscan104.run). Tools are READ from git archives (not copied):
  B3ROOT/lnew  = claude/l-new 069c888b (experiments/new, box189, box190, box21, si, harness, hard-families)
  B3ROOT/lred  = claude/l-red 2d290a15 (experiments/red/r217)
  B3ROOT/lsi   = claude/l-si 2051a0ee (experiments/si/box104)
Usage: gclimb.py B3ROOT <obj> <seed> <iters> <nH> [copy]     obj: its (iterations) | perv (1000 iterations / |Wg|) | pre (iterations
before the first fallback). Resumable: work/gclimb_<tag>.json. Prints improvements; final line GCLIMB ...; a candidate whose output
is NOT correct is written to work/gwrong_<tag>.jsonl at once."""
import sys, os, json, random, time
root = os.path.abspath(sys.argv[1])
os.environ["LNEW"] = os.path.join(root, "lnew"); os.environ["LRED"] = os.path.join(root, "lred")
sys.path.insert(0, os.path.join(root, "lsi/experiments/si/box104"))
import gscan104 as GS
from wrap104 import pg

def rand_H(rng, n):
    prio = list(range(n)); rng.shuffle(prio)
    own = [rng.randrange(2) for _ in range(n)]
    succ = []
    for v in range(n):
        k = rng.randint(1, 3); succ.append(sorted(set(rng.randrange(n) for _ in range(k))))
    return {"prio": prio, "own": own, "succ": succ}

def complete(rng, D):
    """Fill s0 (Even), rho0 (Odd), gamma (Even edges) consistently with succ; drop stale entries."""
    n = len(D["prio"]); succ = D["succ"]
    s0 = D.get("s0", {}); rho = D.get("rho", {}); gam = D.get("gam", {})
    s0 = {str(v): s0[str(v)] for v in range(n) if D["own"][v] == 0 and str(v) in s0 and s0[str(v)] in succ[v]}
    for v in range(n):
        if D["own"][v] == 0 and str(v) not in s0: s0[str(v)] = rng.choice(succ[v])
    rho = {str(v): rho[str(v)] for v in range(n) if D["own"][v] == 1 and str(v) in rho and 0 <= rho[str(v)] < n}
    for v in range(n):
        if D["own"][v] == 1 and str(v) not in rho: rho[str(v)] = rng.choice(succ[v])
    gam = {k: t for k, t in gam.items() if D["own"][int(k.split(",")[0])] == 0 and int(k.split(",")[1]) in succ[int(k.split(",")[0])] and 0 <= t < n}
    D["s0"], D["rho"], D["gam"] = s0, rho, gam
    return D

def run(D, copy):
    n = len(D["prio"])
    H = pg.Game(D["prio"], D["own"], D["succ"])
    s0 = [D["s0"][str(v)] if D["own"][v] == 0 else -1 for v in range(n)]
    rho0 = {v: D["rho"][str(v)] for v in range(n) if D["own"][v] == 1}
    gamma = {tuple(map(int, k.split(","))): t for k, t in D["gam"].items()}
    return GS.run(H, s0, rho0, cap=20000, gamma=gamma, copy=copy)

def mutate(rng, D):
    D = json.loads(json.dumps(D)); n = len(D["prio"]); v = rng.randrange(n)
    op = rng.choice(["prio", "own", "edge+", "edge-", "retarget", "s0", "rho", "gam", "gam", "gamdel"])
    if op == "prio":
        u = rng.randrange(n); D["prio"][v], D["prio"][u] = D["prio"][u], D["prio"][v]
    elif op == "own": D["own"][v] ^= 1
    elif op == "edge+":
        if len(D["succ"][v]) < 4: D["succ"][v] = sorted(set(D["succ"][v] + [rng.randrange(n)]))
    elif op == "edge-":
        if len(D["succ"][v]) > 1: D["succ"][v].remove(rng.choice(D["succ"][v]))
    elif op == "retarget":
        s = D["succ"][v]; s[rng.randrange(len(s))] = rng.randrange(n); D["succ"][v] = sorted(set(s))
    elif op == "s0":
        if D["own"][v] == 0: D["s0"][str(v)] = rng.choice(D["succ"][v])
    elif op == "rho":
        if D["own"][v] == 1: D["rho"][str(v)] = rng.randrange(n)
    elif op == "gam":
        if D["own"][v] == 0:
            w = rng.choice(D["succ"][v]); D["gam"]["%d,%d" % (v, w)] = rng.randrange(n)
    elif op == "gamdel":
        if D["gam"]: del D["gam"][rng.choice(list(D["gam"]))]
    return complete(rng, D)

def score(d, obj):
    if obj == "its": return d["its"] * 10000 - d["W"]
    if obj == "perv": return (1000000 * d["its"]) // d["W"]
    if obj == "pre": return (d["F1"] or d["its"]) * 10000 - d["W"]
    raise ValueError(obj)

def main():
    obj, seed, iters, nH = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    copy = (sys.argv[6] == "1") if len(sys.argv) > 6 else True
    tag = "%s_s%d_n%d_c%d" % (obj, seed, nH, int(copy)); os.makedirs("work", exist_ok=True)
    sf = "work/gclimb_%s.json" % tag; wf = open("work/gwrong_%s.jsonl" % tag, "a")
    rng = random.Random(seed)
    if os.path.exists(sf):
        S = json.load(open(sf)); D = S["D"]; it0 = S["it"]; rng.seed(seed * 7919 + it0)
    else:
        D = complete(rng, rand_H(rng, nH)); it0 = 0
    d = run(D, copy); best = score(d, obj); t0 = time.time(); nwrong = 0
    for it in range(it0, iters):
        E = D
        for _ in range(rng.randint(1, 3)): E = mutate(rng, E)
        try:
            d2 = run(E, copy)
        except Exception as ex:
            continue
        if not d2["ok"]:
            nwrong += 1; wf.write(json.dumps({"D": E, "copy": copy, "d": d2}) + "\n"); wf.flush()
            print("WRONG it %d its %d |Wg| %d" % (it, d2["its"], d2["W"]), flush=True)
        s = score(d2, obj)
        if s >= best:
            if s > best:
                print("it %d its %d F1 %s fbs %d |Wg| %d hsteps %d hmoves %d tauch %d" % (it, d2["its"], d2["F1"], d2["fbs"], d2["W"],
                      d2["hsteps"], d2["hmoves"], d2["tauch"]), flush=True)
            D, best, d = E, s, d2
        if it % 50 == 0: json.dump({"D": D, "it": it + 1, "d": d}, open(sf, "w"))
    json.dump({"D": D, "it": iters, "d": d}, open(sf, "w"))
    print("GCLIMB %s its %d F1 %s fbs %d |Wg| %d hsteps %d wrong %d %.0fs" % (tag, d["its"], d["F1"], d["fbs"], d["W"], d["hsteps"],
          nwrong, time.time() - t0), flush=True)

if __name__ == "__main__":
    main()
