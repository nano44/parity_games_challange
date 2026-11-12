"""REFEREE successor 31: P-N5-BONLY3 replay with own code (my lane's Γ3 builder xicyc_replay.build(pad=True) and VJ best_reply; no lane code).
For each genome: (1) the HOW3 run (xicyc_replay.howard, states 0..T3); (2) R random mover strategies σ in [FRAME3] (frame = the builder's
frozen start off the movers: K0 → pA → K3, K1 → s → K1, K3 → K2, β → Ξ-target or pb; a uniformly random option at every mover), each with
its optimal σ̄ = best_reply. Counters (unit (pair, vertex) for bonly, (pair, gate) for the rest; must be 0):
  bonly   v not an exception (c_W, e with successor c_W, their pe pads) with Λ(v) at least as relevant as the least e-vertex  [B-ONLY3]
  ecyc    an e-vertex on the cycle of some play                                                                       [NO-E-CYCLE3]
  dpass   e_o on P(D), D := e_o's successor                                                                           [PROVISO3]
  lamup   Λ(pe_o) = Λ(pβ_o) and e_o not more relevant than Λ(pe_o)                                                    [LAM-UP3]
  transp  a single-successor vertex v with Λ(v) ≠ Λ(succ v)                                                           [face transport, §4]
Controls (must fire): cNopad = bonly with the pe-pad exceptions dropped; cAnti = bonly under Odd's anti strategy (e-face at every gate,
σ̄(K2) kept) in place of σ̄ (non-optimal Odd).
Usage: bonly3_replay.py R SEED F.json ..."""
import sys, os, json, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xicyc_replay import build, howard
from xicyc_vj import VJ

def lam_of(st, v):
    seen = []; pos = {}
    while v not in pos: pos[v] = len(seen); seen.append(v); v = st[v]
    return seen, seen[pos[v]:]

def check(E, idx, O, st, C, tag, prio):
    rk = E.rk; n = E.n; cW = idx["cW"]
    evs = [idx[("e", q)] for q in O]; emin = min(rk[e] for e in evs)
    exc = {cW}; excnp = {cW}
    for q in O:
        e = idx[("e", q)]
        if E.succ[e][0] == cW: exc |= {e, idx[("pe", q)]}; excnp.add(e)
    for v in range(n):
        path, cyc = lam_of(st, v); w = max(cyc, key=lambda z: rk[z])
        if rk[w] >= emin:
            if v not in exc: C[tag + "bonly"] += 1
            if v not in excnp: C[tag + "cNopad"] += 1
        if tag == "" and any(z in evs for z in cyc): C["ecyc"] += 1
        if tag == "" and len(E.succ[v]) == 1:
            _, c2 = lam_of(st, E.succ[v][0])
            if max(c2, key=lambda z: rk[z]) != w: C["transp"] += 1
    if tag: return
    for q in O:
        e = idx[("e", q)]; D = E.succ[e][0]
        if e in lam_of(st, D)[0]: C["dpass"] += 1
        pe, pb = idx[("pe", q)], idx[("pbeta", q)]
        _, c1 = lam_of(st, pe); _, c2 = lam_of(st, pb)
        w1, w2 = max(c1, key=lambda z: rk[z]), max(c2, key=lambda z: rk[z])
        if w1 == w2 and not rk[e] > rk[w1]: C["lamup"] += 1
        C["gatepairs"] += 1

def one(G, R, rng, C):
    prio, own, fsucc, sig, movers, idx, _ = build(G, True); E = VJ(prio, own, fsucc)
    O = [(x, k) for x in range(G["N"]) for k in range(len(G["opts"][x]))]
    _, _, _, states, _, _ = howard(G, True)
    for (s, st, val) in states: check(E, idx, O, st, C, "", prio); C["pairs"] += 1
    gates = [idx[("g", q)] for q in O]
    for _ in range(R):
        s = [sig.get(v) for v in range(E.n)]
        for x in movers: s[x] = rng.choice(E.succ[x])
        st, val = E.best_reply(s); check(E, idx, O, st, C, "", prio); C["pairs"] += 1
        an = list(st)
        for q in O: an[idx[("g", q)]] = idx[("pe", q)]
        check(E, idx, O, an, C, "a_", prio)

if __name__ == "__main__":
    R, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed); T = collections.Counter()
    for f in sys.argv[3:]:
        C = collections.Counter(); one(json.load(open(f)), R, rng, C)
        print(os.path.basename(f), " ".join(f"{k} {C[k]}" for k in ("pairs", "gatepairs", "bonly", "ecyc", "dpass", "lamup", "transp", "cNopad", "a_bonly")), flush=True)
        T.update(C)
    print("TOTAL", " ".join(f"{k} {T[k]}" for k in ("pairs", "gatepairs", "bonly", "ecyc", "dpass", "lamup", "transp", "cNopad", "a_bonly")), flush=True)
