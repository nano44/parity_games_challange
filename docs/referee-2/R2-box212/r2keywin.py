#!/usr/bin/env python3
"""REFEREE-2 40: DATA probe for gap G-1 of my box 212 pre-read (RF-D's window clause). Own engine: R2-P-N5-END/r2end.py's SPEC
primitives (s1, dual, Order, s3, build; successor 34, from SPEC's text), not the lane's n5v / arena213.
N5 from S3 on Γ3(G) (e-order lev) up to its first fallback. At every state t before it, with σ̄_t from S1:
  N5's Even step  : S4a = Even's optimum in the arena H (Even v keeps A(v) = {σ(v)} ∪ Iσ(v)), Odd fixed at N5's τ   (SPEC l. 51-53)
  window step     : the same S4a with Odd fixed at σ̄_t instead of τ, and every non-mover Even vertex kept at σ_t (H_V's single
                    successor s_u; RF-B: «every other vertex x of Y keeps the single successor s_u(x)»). On a class-frozen window with Y = V (the tail; on the five towers
                    the whole run, box 212 §6 / §7) the window game H_V of RF-B has Odd's single strategy σ̄_u = σ̄_t, so SPEC's key step
                    ON THE WINDOW GAME is exactly this (Iσ is the same: same values, same gates).
Counters (unit in brackets): states [t], moved [(t, mover) N5 changes], notbest [(t, mover) N5's new gate not Ξσ-best: box 213's
notbest, second engine], diff [(t, mover) N5's choice ≠ the window step's], diffstates [t with some diff], taudiff [(t, gate) τ(g) ≠
σ̄_t(g)], itfail [t with Iτ ≠ ∅ before the fallback]; first_diff t:mover(vertex index):σ_t:N5's:window's (vertex indices of r2end.build). F = iteration of the first fallback (r2end's count; T_key = F − 1, my tkey check).
--ctrl: the window step uses τ (non-movers still kept): isolates τ versus σ̄; expected diff 0 (ESC3-ALL: S4a keeps σ at non-movers).   Usage: r2keywin.py [--ctrl] FILES..."""
import sys, os, json
sys.path.insert(0, os.path.join(os.environ["R2DIR"], "R2-P-N5-END"))
from r2end import build, s1, dual, Order, s3
ctrl = "--ctrl" in sys.argv; files = [a for a in sys.argv[1:] if a != "--ctrl"]
TOT = dict(runs=0, states=0, moved=0, notbest=0, diff=0, diffstates=0, taudiff=0, gatestates=0, itfail=0, nofb=0)
for fn in files:
    G = json.load(open(fn)); G = G.get("genome", G)
    g = build(G, "lev"); n, pr, ow, E, V = g["n"], g["pr"], g["ow"], g["E"], g["V"]
    od = Order(pr); dpr, dow = dual(pr, ow); dod = Order(dpr)
    st = s3(g); sig = [st[v] if ow[v] == 0 else None for v in range(n)]; tau = [st[v] if ow[v] == 1 else None for v in range(n)]
    movers = {V[("x", x)] for x in range(g["N"])}; gates = [V[("g", o)] for o in g["O"]]
    c = dict(states=0, moved=0, notbest=0, diff=0, diffstates=0, taudiff=0, gatestates=0, itfail=0); F = None
    for it in range(1, 100000):
        val, sbar = s1(pr, ow, E, sig, od)
        Is = {v: [w for w in E[v] if w != sig[v] and od.cmp(val[w], val[sig[v]]) > 0] for v in range(n) if ow[v] == 0}
        Is = {v: l for v, l in Is.items() if l}
        dval, _ = s1(dpr, dow, E, tau, dod)
        It = {v: [w for w in E[v] if w != tau[v] and dod.cmp(dval[w], dval[tau[v]]) > 0] for v in range(n) if ow[v] == 1}
        It = {v: l for v, l in It.items() if l}
        if not Is and not It: break
        snew = list(sig)
        if Is:
            HE = [sorted(set([sig[v]] + Is.get(v, []))) if ow[v] == 0 else [tau[v]] for v in range(n)]
            _, hch = s1(dpr, dow, HE, tau, dod)
            for v in range(n):
                if ow[v] == 0: snew[v] = hch[v] if hch[v] is not None else HE[v][0]
        if snew == sig and not It: F = it; break                     # first fallback (Iσ ≠ ∅, σ_new = σ, τ unchanged)
        if It: c["itfail"] += 1; F = it; break                       # not expected before the fallback on Γ3 (box 104 §8): counted, stop
        c["states"] += 1
        for gv in gates: c["gatestates"] += 1; c["taudiff"] += tau[gv] != sbar[gv]
        odd = sbar if not ctrl else tau
        HW = [(sorted(set([sig[v]] + Is.get(v, []))) if v in movers else [sig[v]]) if ow[v] == 0 else [odd[v]] for v in range(n)]
        _, wch = s1(dpr, dow, HW, odd, dod)
        wnew = [(wch[v] if wch[v] is not None else HW[v][0]) if ow[v] == 0 else None for v in range(n)]
        d = 0
        for x in movers:
            if snew[x] != sig[x]:
                c["moved"] += 1
                if any(od.cmp(val[w], val[snew[x]]) > 0 for w in E[x]): c["notbest"] += 1
            if wnew[x] != snew[x]:
                d += 1
                if "first" not in c: c["first"] = f"t{it - 1}:mover{x}:sig{sig[x]}:N5{snew[x]}:win{wnew[x]}"
        c["diff"] += d; c["diffstates"] += d > 0
        sig = snew
    TOT["runs"] += 1; TOT["nofb"] += F is None
    first = c.pop("first", "-")
    for k in c: TOT[k] += c[k]
    print(os.path.basename(fn), "F", F, " ".join(f"{k} {v}" for k, v in c.items()), "first_diff", first, flush=True)
print("TOTAL ctrl", int(ctrl), " ".join(f"{k} {v}" for k, v in TOT.items()), flush=True)
