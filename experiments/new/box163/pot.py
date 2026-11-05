#!/usr/bin/env python3
"""L-NEW box 163 (DATA): screen Xi-side candidate potentials Phi(u) on forced c-steps of ISO R197 ladders (box 162 cstep).
Requirement checked: at every frame with a move, Phi(new) < Phi(old) (a no-flip step must strictly decrease Phi; c is the frame's bit).
Exhaustive over all states u and both c of random genomes; a violation is a kill instance (written to out/)."""
import os, sys, json, random
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, "..", "box162", "flipcheck.py")
ns = {"__file__": P, "__name__": "lib"}; exec(open(P).read(), ns)
Gen, cstep, rand_lr, allstates = ns["Gen"], ns["cstep"], ns["rand_lr"], ns["allstates"]
def unhappy(g, u): return [x for x in range(2, g.N) if len(g.avail(u, x)) > 1]
CANDS = {
  "U":   lambda g, u: len(unhappy(g, u)),                                   # number of Xi-unhappy movers
  "UW":  lambda g, u: sum(2 ** (g.N // 2 - g.lev[x]) for x in unhappy(g, u)),  # unhappy, weighted toward low levels
  "UWT": lambda g, u: sum(2 ** g.lev[x] for x in unhappy(g, u)),            # unhappy, weighted toward high levels
  "CNT": lambda g, u: sum(g.cnt(u, x) for x in range(2, g.N)),              # number of strictly better options (deg 2: = U)
  "RINF": None,                                                             # exact max over key schedules (sanity: always decreases)
}
def rinf(g, u, memo):
    if u in memo: return memo[u]
    best = 0
    for c in (0, 1):
        u2 = cstep(g, u, c)
        if u2[2:] != u[2:]: best = max(best, 1 + rinf(g, u2, memo))
    memo[u] = best; return best
rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 163); n = int(sys.argv[2]) if len(sys.argv) > 2 else 300
viol = {k: 0 for k in CANDS}; first = {}; frames = 0
for i in range(n):
    d = 3 + i % 2; G = rand_lr(d, rng, True); g = Gen(G); memo = {}
    for u in allstates(g.N):
        if u[:2] != (0, 0): continue
        for c in (0, 1):
            u2 = cstep(g, u, c)
            if u2 == u: continue
            frames += 1
            for k, f in CANDS.items():
                a, b = (rinf(g, u, memo), rinf(g, u2, memo)) if f is None else (f(g, u), f(g, u2))
                if b >= a:
                    viol[k] += 1
                    if k not in first: first[k] = (i, d, u, c, a, b); G["start"] = list(u); os.makedirs(os.path.join(H, "out"), exist_ok=True); json.dump(G, open(os.path.join(H, "out", f"kill_{k}.json"), "w"))
print(f"POT frames {frames} " + " ".join(f"{k} {v}" for k, v in viol.items()))
for k, v in first.items(): print("first", k, v)
