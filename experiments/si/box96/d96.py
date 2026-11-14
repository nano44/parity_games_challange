#!/usr/bin/env python3
"""L-SI box 96: Lemma D-AVOID (E-FACE-PAYS (b)'s proviso «D's play avoids e_o») and the B-ONLY form it uses, on two engines
(engines of box91/mult91.py). Unit gate: an Odd vertex o with two successors (faces) p_e, p_b, p_e's play starting at o's e-vertex e_o
(as box93/np93.py); D := e_o's single successor (W-target, or c_W); t a state of the whole run (own: IDEAL-CYC to the cap 3000; g3:
Gamma3 N5'-xi from S3 to the first fallback or the cap 20000).
Counters (TOTALS; must be 0):
  dpass  : (gate, t) with e_o on P_t(D)                                                            [Lemma D-AVOID]
  lamD   : (gate, t), D not c_W, with Lambda_t(D) at least as relevant as e_o                       [D-AVOID's proof: B-ONLY at D]
  bonly  : (t, v), v not an exception, with Lambda_t(v) at least as relevant as some e-vertex; exceptions = c_W, the e-vertices whose
           successor is c_W, and (Gamma3) the single-successor vertices whose successor is an exception (the pads of those e's)  [B-ONLY / B-ONLY3]
  sfail  : gate with S(p_e) != S(D) (the step sets of value changes; whole run)                     [E-FACE-PAYS (b) with D-AVOID]
  relD   : gate with relocks(o) > ch_D;  unlD: gate with unlocks(o) > 1 + ch_D                      [E-FACE-PAYS (a) + (b)]
Records: gates, states (T + 1), pairs (gate, t), Dcw (gates with D = c_W), tight (gates with relocks = ch_D, ch_D >= 1).
Control CTRL=nopad: the exceptions WITHOUT the pads of the level-0 e's (bonly fires on Gamma3 only: the pad clause of B-ONLY3 is needed).
Control CTRL=anti (fires on Xi-cyclic genomes): Odd's choice replaced by «e-face at o, beta-face at every other gate» (K2 kept); counts
  aptpass = (gate, t) with e_o on D's play under (sigma_t, that strategy): optimality of Odd is what D-AVOID uses.
Usage: d96.py own|g3 G.json ...   (OWN_DIR / ROOT as for box91/mult91.py)"""
import sys, os, json, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box91"))
import mult91
CTRL = os.environ.get("CTRL", "")
K = ("states", "gates", "pairs", "Dcw", "dpass", "lamD", "bonly", "sfail", "relD", "unlD", "tight", "aptpass")

def run(T, n, nx, lam, E, rk, evs, odd2, val):
    c = collections.Counter({k: 0 for k in K}); c["states"] = T + 1
    nsucc = {}
    for t in range(T + 1):
        for v in range(n):
            nsucc.setdefault(v, set()).add(nx(t, v))
    # c_W: the e-vertices' successors that are self-loops more relevant than every e-vertex
    emin = min(rk[e] for e in evs)
    cw = {nx(0, e) for e in evs if nx(0, nx(0, e)) == nx(0, e) and rk[nx(0, e)] > emin}
    gates = []
    for (o, p, q) in odd2:
        pe = pb = eo = None
        for f, g in ((p, q), (q, p)):
            if f in evs: pe, pb, eo = f, g, f
            elif nx(0, f) in evs and all(nx(t, f) == nx(0, f) for t in range(T + 1)): pe, pb, eo = f, g, nx(0, f)
        if pe is not None: gates.append((o, pe, pb, eo, nx(0, eo)))
    gateset = {g[0] for g in gates}
    exc = set(cw) | {e for e in evs if nx(0, e) in cw}
    grow = CTRL != "nopad"
    while grow:
        grow = False
        for v in range(n):
            if v not in exc and v not in gateset and len(nsucc[v]) == 1 and next(iter(nsucc[v])) in exc and v not in evs:
                exc.add(v); grow = True
    def play(t, v, ch=None):
        p = []; seen = set(); u = v
        while u not in seen:
            seen.add(u); p.append(u); u = ch(u) if ch else nx(t, u)
        return p
    for t in range(T + 1):
        for v in range(n):
            if v not in exc and rk[lam(t, v)] >= emin: c["bonly"] += 1
    for (o, pe, pb, eo, D) in gates:
        c["gates"] += 1; c["Dcw"] += D in cw
        SD = SE = 0; rel = unl = 0; sd = []; se = []
        for t in range(T + 1):
            c["pairs"] += 1
            if eo in play(t, D): c["dpass"] += 1
            if D not in cw and rk[lam(t, D)] >= rk[eo]: c["lamD"] += 1
            if CTRL == "anti":
                g2 = {gg[0]: gg for gg in gates}
                def ch(u, t=t):
                    if u == o: return pe
                    if u in g2: return g2[u][2]
                    return nx(t, u)
                if eo in play(t, D, ch): c["aptpass"] += 1
            if t == 0: continue
            if val(t, D) != val(t - 1, D): sd.append(t)
            if val(t, pe) != val(t - 1, pe): se.append(t)
            if nx(t, o) != nx(t - 1, o):
                if nx(t - 1, o) == pe: rel += 1
                else: unl += 1
        c["sfail"] += sd != se; c["relD"] += rel > len(sd); c["unlD"] += unl > 1 + len(sd)
        c["tight"] += rel == len(sd) >= 1
    return c

if __name__ == "__main__":
    eng = sys.argv[1]; print("engine", eng, "instance N+M", " ".join(K), flush=True)
    for f in sys.argv[2:]:
        G = json.load(open(f)); G = G.get("genome", G)
        c = run(*(mult91.eng_own(G) if eng == "own" else mult91.eng_g3(G)))
        print(("ctrl=" + CTRL + " " if CTRL else "") + eng, os.path.basename(f), G["N"] + sum(len(o) for o in G["opts"]),
              " ".join(str(c[k]) for k in K), flush=True)
