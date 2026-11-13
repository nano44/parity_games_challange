#!/usr/bin/env python3
"""L-RED 68 R239: box 212 §2's READING («at every state» in R123 means every state of IDEAL-CYC, whatever the rule) tested directly: the five
landed static lemmas of R123, checked at EVERY state visited by every improving rule of rf239 (own engine, own Odd reply), on random
genomes. Statements (quoted in box 212 §2 / P-N5-LEVEL §1):
 cn2     «the cycle node of v's play has priority >= 2» (every vertex, every state)
 bonly   «for every vertex v other than c_W and the e-vertices whose successor is c_W, Lambda_t(v) is less relevant than every e-vertex»
 notie   «At every state and every gate g, Omega_t(e_g) != Omega_t(beta_g).»
 locgate LOC-GATE's conclusion as P-N5-LEVEL (K4)'s proof uses it: the chosen face a = sigma-bar_t(g) has Omega_t(a) strictly below
         Omega_t(b) for the other face b
 lock2   «At every state sigma-bar_t(K2) = K1 and Omega_t(K1) < Omega_t(K2).»
 opt     Odd's reply is pointwise optimal: no Odd vertex has a successor of strictly smaller value ([OPT], own SI fixpoint)
CTRL=1: bonly's comparison reversed (must fire). Usage: static239.py SEED COUNT NMAX DMAX DEGMAX [RULES]"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import rf239
KEYS = ("cn2", "bonly", "notie", "locgate", "lock2", "opt"); CTRL = os.environ.get("CTRL") == "1"
if __name__ == "__main__":
    seed, cnt, nmax, dmax, degmax = map(int, sys.argv[1:6]); rules = sys.argv[6].split(",") if len(sys.argv) > 6 else rf239.RULES
    rng = random.Random(seed); gens = [rf239.rand_genome(rng, nmax, dmax, degmax) for _ in range(cnt)]; t0 = time.time()
    for rule in rules:
        tot = {k: 0 for k in KEYS}; states = 0
        for G in gens:
            out, (n, prio, ow, succ, V, O, vj), _ = rf239.run(G, rule, random.Random(rng.random()))
            rk = vj.rk; E = [V[("e", q)] for q in O]; emin = min(rk[e] for e in E); cW = V["cW"]
            exc = {cW} | {V[("e", q)] for q in O if succ[V[("e", q)]] == [cW]}
            for sig, vals, tau in out:
                states += 1
                for v in range(n):
                    tot["cn2"] += int(prio[vals[v][0]] < 2)
                    if v not in exc: tot["bonly"] += int((rk[vals[v][0]] < emin) == CTRL)
                    if ow[v] == 1: tot["opt"] += int(any(vj.cmp(vals[w], vals[tau[v]]) < 0 for w in succ[v]))
                for q in O:
                    g, e, b = V[("g", q)], V[("e", q)], V[("b", q)]
                    tot["notie"] += int(vals[e] == vals[b]); a = tau[g]; o = b if a == e else e
                    tot["locgate"] += int(not vj.cmp(vals[a], vals[o]) < 0)
                K1, K2 = V["K1"], V["K2"]; tot["lock2"] += int(tau[K2] != K1 or not vj.cmp(vals[K1], vals[K2]) < 0)
        print(f"STATIC239 seed {seed} genomes {cnt} N<={nmax} d<={dmax} deg<={degmax} rule {rule}" + (" CTRL 1" if CTRL else "") + ": "
              + " ".join(f"{k} {tot[k]}" for k in KEYS) + f" | states {states} | {time.time() - t0:.0f} s", flush=True)
