#!/usr/bin/env python3
"""L-NEW box 174: RE-TRIGGER checks. For a run, tau = top level; blocks of top-only steps [a, b].
 RETRIG: if b < T, every least-level mover h of step b + 1 moves to w with some z in Mv_b (a top mover) on the chain of (h, w) under
         s_(b-1), z a strict Xi-descendant of h.
 BOUNDA: I <= [a_1 = 1 block ends at T] ... checked as: #blocks with b < T <= #lower steps moving a lower Xi-ancestor of a top mover.
 BOUNDD: #blocks with a >= 2 <= #lower steps moving a strict Xi-descendant of a top mover.
 TOPSINK: if no lower mover has a top mover as strict Xi-descendant, then I <= 1 and the only block ends at T.
Prints per-file detail with -v. Usage: retrig.py [-v] [-r nrand] files..."""
import os, sys, json, random, itertools
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P, "__name__": "lib"}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
K = {"__file__": os.path.join(H, "..", "box172", "keycheck.py"), "__name__": "lib"}
exec(open(K["__file__"]).read().split("\nC = {")[0], K); xdesc, valid, rand_gen, is_lr = K["xdesc"], K["valid"], K["rand_gen"], K["is_lr"]
C = dict(runs=0, blocks=0, retrig=0, RETRIG=0, BOUNDA=0, BOUNDD=0, TOPSINK=0, sinkruns=0)
def check(G, start, v=False, name=""):
    g = Gen(G); S, _ = g.run(start); T = len(S) - 1; N = G["N"]; tau = max(G["lev"]); D = xdesc(G); C["runs"] += 1
    if tau == 0: return
    top = [x for x in range(N) if G["lev"][x] == tau]; low = [x for x in range(N) if G["lev"][x] < tau]
    anc = set(x for x in low if any(z in D[x] for z in top)); dlow = set(x for x in range(N) if any(x in D[z] for z in top))   # strict Xi-descendants of top movers, any level
    Mv = [None] + [set(x for x in range(N) if S[t][x] != S[t - 1][x]) for t in range(1, T + 1)]
    TO = [None] + [all(G["lev"][x] == tau for x in Mv[t]) for t in range(1, T + 1)]
    blocks = []; t = 1
    while t <= T:
        if TO[t]:
            a = t
            while t + 1 <= T and TO[t + 1]: t += 1
            blocks.append((a, t))
        t += 1
    C["blocks"] += len(blocks)
    for a, b in blocks:
        if b == T: continue
        C["retrig"] += 1; m = min(G["lev"][x] for x in Mv[b + 1])
        for h in Mv[b + 1]:
            if G["lev"][h] != m: continue
            w = S[b + 1][h]; ch = g.play(S[b - 1], h, w)
            if not any(z in Mv[b] and z in D[h] for z in ch): C["RETRIG"] += 1
    nA = sum(1 for t in range(1, T + 1) if not TO[t] and Mv[t] & anc); nD = sum(1 for t in range(1, T + 1) if not TO[t] and Mv[t] & dlow)
    if sum(1 for a, b in blocks if b < T) > nA: C["BOUNDA"] += 1
    if sum(1 for a, b in blocks if a >= 2) > nD: C["BOUNDD"] += 1
    if not anc:
        C["sinkruns"] += 1
        if len(blocks) > 1 or (blocks and blocks[-1][1] != T): C["TOPSINK"] += 1
    if v:
        pat = "".join("T" if TO[t] else "L" for t in range(1, T + 1))
        print("%-26s d %d T %2d I %d %s anc %s (levels %s) nA %d dlow %s nD %d" % (name[:26], tau + 1, T, len(blocks), pat, sorted(anc),
              sorted(G["lev"][x] for x in anc), nA, sorted(dlow), nD))
if __name__ == "__main__":
    args = sys.argv[1:]; v = "-v" in args; args = [a for a in args if a != "-v"]; nr = 0
    if args and args[0] == "-r": nr = int(args[1]); args = args[2:]
    for f in args:
        try: G = json.load(open(f)); assert valid(G) and "start" in G
        except Exception: continue
        try: check(G, G["start"], v, os.path.basename(f))
        except RuntimeError: C["skipped"] = C.get("skipped", 0) + 1
    rng = random.Random(174); k = 0
    while k < nr:
        G = rand_gen(rng)
        if not valid(G): continue
        k += 1; sizes = [len(o) for o in G["opts"]]
        for st in (itertools.product(*[range(s) for s in sizes]) if eval("*".join(map(str, sizes))) <= 64 else [G["start"]]): check(G, list(st))
    print(" ".join("%s %d" % kv for kv in C.items()))
