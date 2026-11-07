#!/usr/bin/env python3
"""L-RED 53 R215 (Lead 10:05Z, box 192): own labeller for IDEAL-CYC runs (trajectory from box191 idealcyc.run, env WT3; valuations
si.Engine via idealcyc.build; my own step classification, NOT subrun191.labels). Per step t -> t+1:
  C  : some vertex's VJ cycle node changes;  R : no cycle node changes and Odd's optimal counterstrategy changes somewhere;  p : neither.
  R_mov : R-steps at which sigma-bar changes at a gate whose Xi-target is a MOVER (xt >= 0);  R_X : R-steps flipping only X-target gates
  (or non-gate Odd vertices). L = sum over gates of states with Omega(e_g) == Omega(beta_g) (face ties). Also max flips at one gate.
Units: R = number of R-STEPS (transitions t -> t+1); R-flips = sum over R-steps of the number of gates whose sigma-bar face changes.
Usage: rmov.py G.json ..."""
import sys, os, json, hashlib
sys.path.insert(0, os.path.join(os.environ["WT3"], "experiments/new/box191"))
import idealcyc, gamma3
def label(G):
    h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G)
    _, _, _, V = gamma3.build(G, set()); Q = [(x, k) for x in range(G["N"]) for k in range(len(G["opts"][x]))]
    gv = {q: V[("g", q)] for q in Q}; mov = {q: G["opts"][q[0]][q[1]][1] >= 0 for q in Q}
    odd = [v for v in range(h.n) if h.owner[v] == 1]
    prev = None; C = R = Rm = p = L = RF = 0; fl = {q: 0 for q in Q}
    for s in st:
        cur = list(s0)
        for x in range(G["N"]): cur[movers[x]] = V[("g", (x, s[x]))]
        vs, sb = E.evaluate(tuple(cur)); lam = [vs[v][0] for v in range(h.n)]; br = [sb[v] for v in odd]
        L += sum(1 for q in Q if vs[V[("e", q)]] == vs[V[("b", q)]])
        if prev:
            ch = [q for q in Q if sb[gv[q]] != prev[2][gv[q]]]
            for q in ch: fl[q] += 1
            if lam != prev[0]: C += 1
            elif br != prev[1]:
                R += 1; Rm += any(mov[q] for q in ch); RF += len(ch)
            else: p += 1
        prev = (lam, br, sb)
    return dict(T=len(st) - 1, C=C, R=R, RF=RF, R_mov=Rm, p=p, L=L, maxflip=max(fl.values()))
if __name__ == "__main__":
  for f in sys.argv[1:]:
    G = json.load(open(f)); r = label(G); C, R, Rm, p, L = r["C"], r["R"], r["R_mov"], r["p"], r["L"]; T = r["T"]
    w = max(sum(1 for v in range(G["N"]) if G["lev"][v] == l) for l in set(G["lev"]))
    print(f"{os.path.basename(f)} sha1 {hashlib.sha1(open(f, 'rb').read()).hexdigest()[:8]} d {max(G['lev']) + 1} w {w} N {G['N']} "
          f"T {T} C {C} R {R} R-flips {r['RF']} R_mov {Rm} R_X {R - Rm} p {p} L {L} maxflip/gate {r['maxflip']}", flush=True)
