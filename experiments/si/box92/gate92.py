#!/usr/bin/env python3
"""L-SI box 92: Lemma GATE-LOW-NULL (box 85's FLIP-U / LOW-NULL at an Odd gate), on two engines (engines of box91/mult91.py).
Unit: an Odd vertex o with two successors (faces) p_e, p_b, where p_e's play starts at o's e-vertex e_o (own: p_e = e_o; g3: the pad
pe_o -> e_o); a time t of the whole run. LAM_t := Lambda_t(p_e) == Lambda_t(p_b); PRIV_t := e_o not in E_t(p_b).
pi(X) := {f in X : f at least as relevant as e_o}.  Counters (TOTALS; must be 0):
  decfail : at a t with LAM_t and PRIV_t and e_o in E_t(p_e): the most relevant element of E_t(p_e) ^ E_t(p_b) is less relevant than e_o
            (or the difference is empty)                                                         [(PROJ): the decider is >= e_o]
  glnfail : a flip of o at t with LAM_(t-1), LAM_t, PRIV_(t-1), PRIV_t, where neither pi(E(p_e)) nor pi(E(p_b)) changed at t
                                                                                                  [Lemma GATE-LOW-NULL]
Records (TOTALS): flips, f_lam (a Lambda differs at t-1 or t), f_np (not PRIV at t-1 or t), f_up (decided by a change of pi, the lemma's
case); lowch = #(o, t) with E(p_e) or E(p_b) changing only BELOW e_o (pi unchanged) on LAM/PRIV steps: changes the gate cannot see;
lowflip = flips at such steps (must be 0: = glnfail restricted). Control CTRL=low: pi := the part strictly LESS relevant than e_o
(glnfail / decfail fire).
Usage: gate92.py own|g3 G.json ...   (OWN_DIR / ROOT as for mult91.py)"""
import sys, os, json, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box91"))
import mult91
CTRL = os.environ.get("CTRL", "")
def run(T, n, nx, lam, E, rk, evs, odd2, val):
    c = collections.Counter()
    for k in ("gates", "flips", "f_lam", "f_np", "f_up", "lowch", "lowflip", "decfail", "glnfail"): c[k] = 0
    for (o, p, q) in odd2:
        pe = pb = eo = None
        for f, g in ((p, q), (q, p)):
            if f in evs: pe, pb, eo = f, g, f
            elif nx(0, f) in evs and all(nx(t, f) == nx(0, f) for t in range(T + 1)): pe, pb, eo = f, g, nx(0, f)
        if pe is None: continue
        c["gates"] += 1; r0 = rk[eo]
        pi = (lambda X: frozenset(f for f in X if rk[f] < r0)) if CTRL == "low" else (lambda X: frozenset(f for f in X if rk[f] >= r0))
        LP = lambda t: lam(t, pe) == lam(t, pb) and eo not in E(t, pb)
        for t in range(T + 1):
            if LP(t) and eo in E(t, pe):
                d = E(t, pe) ^ E(t, pb)
                c["decfail"] += (not d) or rk[max(d, key=lambda f: rk[f])] < r0
            if t == 0: continue
            fl = nx(t, o) != nx(t - 1, o); c["flips"] += fl
            if lam(t, pe) != lam(t, pb) or lam(t - 1, pe) != lam(t - 1, pb): c["f_lam"] += fl; continue
            if not (LP(t) and LP(t - 1)): c["f_np"] += fl; continue
            up = pi(E(t, pe)) != pi(E(t - 1, pe)) or pi(E(t, pb)) != pi(E(t - 1, pb))
            anych = E(t, pe) != E(t - 1, pe) or E(t, pb) != E(t - 1, pb)
            if fl and up: c["f_up"] += 1
            if fl and not up: c["glnfail"] += 1
            if anych and not up: c["lowch"] += 1; c["lowflip"] += fl
    return c
K = ("gates", "flips", "f_lam", "f_np", "f_up", "lowch", "lowflip", "decfail", "glnfail")
if __name__ == "__main__":
    eng = sys.argv[1]; print("engine", eng, "instance N+M", " ".join(K), flush=True)
    for f in sys.argv[2:]:
        G = json.load(open(f)); G = G.get("genome", G)
        c = run(*(mult91.eng_own(G) if eng == "own" else mult91.eng_g3(G)))
        print(eng, os.path.basename(f), G["N"] + sum(len(o) for o in G["opts"]), " ".join(str(c[k]) for k in K), flush=True)
