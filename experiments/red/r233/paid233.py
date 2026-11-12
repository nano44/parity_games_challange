#!/usr/bin/env python3
"""L-RED 65 R233b: INDEPENDENT counter for L-NEW 71's Lemma PAID (box 207 Addendum A, claude/l-new b72411cf) on L-RED's own IDEAL-CYC
engine (r221q/own.py; no L-NEW code). For EVERY single feedback vertex R (window233.fvs1), every state t and every gate g with
sigma-bar_t(g) = e_g: DIRECT iff R lies on the play of e_g or of beta_g. If not DIRECT: must-0 counters
  notK1 (Lambda(e_g) != K1 or Lambda(beta_g) != K1), nonext (beta_g's play has no e-vertex), notE (next(g) = h not at its e-face),
  lexfail (not E(e_g) <lex E(e_h)), nochain (the chain g -> next -> ... does not reach a DIRECT gate within M steps).
Control PAID_CTRL=1: R replaced by a mover that is NOT a feedback vertex (the first one in index order).
Usage: paid233.py G.json ... | paid233.py rand SEED COUNT (k = 1 genomes from r231/dep231.rgen)"""
import sys, os, json, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r221q"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r231"))
import own
from window233 import fvs1
from blk231 import xi_k
from dep231 import rgen
KEYS = ("cases", "direct", "notK1", "nonext", "notE", "lexfail", "nochain", "maxchain")
def measure(G):
    out, V, O, ow = own.run(G, 20000); n, prio, _, succ, _, _ = own.build(G); N = G["N"]; rk = own.VJ(prio).rk
    evs = {V[("e", q)] for q in O}; gate_of = {V[("e", q)]: V[("g", q)] for q in O}; K1 = V["K1"]
    Rs = fvs1(G)
    if os.environ.get("PAID_CTRL") == "1": Rs = [next(x for x in range(N) if x not in Rs)]
    c = {k: 0 for k in KEYS}
    for R in Rs:
        for s, vals, tau in out:
            nxt = [(s[v] if v < N else succ[v][0]) if ow[v] == 0 else tau[v] for v in range(n)]
            def play(v):
                p = []; seen = set()
                while v not in seen: seen.add(v); p.append(v); v = nxt[v]
                return p
            def E(v): return frozenset(u for u in vals[v][1] if u in evs)
            def lt(A, B): d = A ^ B; return bool(d) and max(d, key=lambda u: rk[u]) in B
            def direct(g): q = [u for u in succ[g]]; return any(R in play(u) for u in q)
            for q in O:
                g, e, b = V[("g", q)], V[("e", q)], V[("b", q)]
                if tau[g] != e: continue
                c["cases"] += 1
                if direct(g): c["direct"] += 1; continue
                if vals[e][0] != K1 or vals[b][0] != K1: c["notK1"] += 1
                cur = g; L = 0; ok = True
                while not direct(cur):
                    eb = [u for u in play(succ[cur][1] if succ[cur][0] in evs else succ[cur][0]) if u in evs]
                    bface = [u for u in succ[cur] if u not in evs][0]; eb = [u for u in play(bface) if u in evs]
                    if not eb: c["nonext"] += 1; ok = False; break
                    h = gate_of[eb[0]]
                    if tau[h] != eb[0]: c["notE"] += 1; ok = False; break
                    ecur = [u for u in succ[cur] if u in evs][0]
                    if not lt(E(ecur), E(eb[0])): c["lexfail"] += 1; ok = False; break
                    cur = h; L += 1
                    if L > len(O): c["nochain"] += 1; ok = False; break
                c["maxchain"] = max(c["maxchain"], L)
    return c
if __name__ == "__main__":
    tot = {k: 0 for k in KEYS}; tot["genomes"] = 0
    if sys.argv[1] == "rand":
        rng = random.Random(int(sys.argv[2])); Gs = []
        while len(Gs) < int(sys.argv[3]):
            G = rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.choice([2, 3]))
            if xi_k(G) == 1: Gs.append((f"r{len(Gs)}", G))
    else: Gs = [(os.path.basename(f), json.load(open(f))) for f in sys.argv[1:]]
    for tag, G in Gs:
        c = measure(G); tot["genomes"] += 1
        for k in KEYS: tot[k] = max(tot[k], c[k]) if k == "maxchain" else tot[k] + c[k]
        if sys.argv[1] != "rand" or any(c[k] for k in ("notK1", "nonext", "notE", "lexfail", "nochain")): print(tag, c, flush=True)
    print("TOTAL", tot, flush=True)
