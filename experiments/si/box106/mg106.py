#!/usr/bin/env python3
"""L-SI box 106, §2 audit: the MOVER GAME M_s (docs/si/box106-exact2.md §2) against SPEC's own valuation on Gamma3*(G*).
For a free depth-2 ladder genome G* (box 105 ladder105.py's shape and generator) and EVERY mover state s (16), the availability bit of
every mover x («the other option's pad value is strictly better than the current one's», SPEC S1 / S2) is computed twice:
  (1) by si.Engine on Gamma3*(G*) in the standard state of s (as box 105 key105.py does);
  (2) by mg106's abstract evaluator: Odd's optimum, by brute force over Odd's face choices at the 4 active gates and the valued gate,
      of the VJ value of the play in M_s; lengths counted in Gamma3*'s edges (mover -> pad -> gate -> pe | pbeta -> carrier -> next).
Counter mgfail (unit (genome, state, mover)): the two bits differ. CTRL=1: the abstract evaluator flips the parity of every e-carrier
(must fire). Usage: mg106.py rand SEED COUNT | xrun SEED COUNT (abstract KEY run vs key105's, counter runfail) | climb SEED RESTARTS STEPS [OUT.json]
(env LNEW, LRED, BOX104 as box 105's tools)"""
import sys, os, random, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box105"))
import ladder105 as LD
import key105 as K
from si import Engine
CTRL = int(os.environ.get("CTRL", "0"))
CW, K1 = "cW", "K1"

def mg_values(G, pb, pe, s):
    """abstract value of the gate of every option (x, k) under state s: dict (x, k) -> comparable key"""
    N = G["N"]; top = max(list(pb.values()) + list(pe.values())) + 2; top += top % 2
    pri = {}
    for q in pb: pri[("b",) + q] = pb[q]
    for q in pe: pri[("e",) + q] = pe[q] ^ (1 if CTRL == 1 else 0)
    pri[CW] = top; pri[K1] = 5; pri["K0"] = top + 2; pri["K3"] = top + 3
    def edges(x, k):   # (carrier, target, edges from the gate to the target vertex)
        wt, xt, _ = G["opts"][x][k]
        e = (("e", x, k), wt if wt >= 0 else CW, 3)            # g -> pe -> e -> (mover | c_W)
        b = (("b", x, k), xt if xt >= 0 else K1, 3 if xt >= 0 else 9)   # g -> pbeta -> beta -> mover ; or beta -> pb -> K0 -> pA -> K3 -> K2 -> r -> K1
        return e, b
    def play_value(start, rho):
        """start = (x, k) (its gate); rho: dict mover -> 0 (e-face) / 1 (beta-face) at the active gates, plus the start gate's face"""
        seq = []; pos = 0; seen = {}
        node = start; face = rho["start"]
        if start[1] == s[start[0]]: seen[start[0]] = 0     # the valued gate is the mover's active gate: a return to the mover closes here
        while True:
            x, k = node
            carr, tgt, ln = edges(x, k)[face]
            seq.append((carr, pos, ln)); pos += ln
            if tgt == CW: path = [c for c, _, _ in seq]; cyc_node = CW; length = pos; break
            if tgt == K1:
                path = [c for c, _, _ in seq] + ["K0", "K3"]; cyc_node = K1; length = pos; break
            if tgt in seen:     # cycle closes at mover tgt: cycle = edges from seen[tgt] on
                i0 = seen[tgt]; cyc = [c for c, _, _ in seq[i0:]]; cyc_node = max(cyc, key=lambda c: pri[c])
                j = [c for c, _, _ in seq].index(cyc_node, i0); path = [c for c, _, _ in seq[:j]]
                length = seq[j][1] + 2     # the carrier sits 2 edges after the gate where its edge starts (g -> pe | pbeta -> carrier)
                break
            seen[tgt] = len(seq); pos += 2     # mover -> pad -> gate of the next active option
            node = (tgt, s[tgt]); face = rho[tgt]
        P = frozenset(c for c in path if pri[c] > pri[cyc_node])
        return cyc_node, P, length
    def key(v):
        c, P, ln = v; p = pri[c]; r = p if p % 2 == 0 else -p
        w = sum((1 if pri[u] % 2 == 0 else -1) * (2 ** rk[u]) for u in P)
        return (r, w, -ln if p % 2 == 0 else ln)
    allc = sorted(pri, key=lambda c: pri[c]); rk = {c: i for i, c in enumerate(allc)}
    out = {}
    for x in range(N):
        for k in range(2):
            best = None
            for bits in itertools.product((0, 1), repeat=N + 1):
                rho = {z: bits[z] for z in range(N)}; rho["start"] = bits[N]
                if k == s[x]: rho["start"] = rho[x]
                kv = key(play_value((x, k), rho))
                if best is None or kv < best: best = kv
            out[(x, k)] = best
    return out

def abstract_run(G, pb, pe):
    """KEY(G*) on the depth-2 ladder with the mover-game availability: returns the list of states (L* = len - 1)"""
    tab = {}
    def avail(s):
        if s not in tab:
            mg = mg_values(G, pb, pe, s); tab[s] = [mg[(x, 1 - s[x])] > mg[(x, s[x])] for x in range(4)]
        return tab[s]
    gate = G["gate"]; s = tuple(G["start"]); states = [s]
    while True:
        a = avail(s); t = list(s)
        for x in (0, 1):
            if a[x] and gate[x][1 - s[x]] < gate[x][s[x]]: t[x] = 1 - s[x]
        pref = 0 if gate[0][t[0]] < gate[1][t[1]] else 1
        for x in (2, 3):
            if a[x] and s[x] != pref: t[x] = pref
        t = tuple(t)
        if t == s: return states
        s = t; states.append(s)

def climb(seed, restarts, steps):
    rng = random.Random(seed); best = -1; bst = None; hist = []
    for r in range(restarts):
        st = LD.init(rng, 2); sc = len(abstract_run(*gp(st))) - 1
        for _ in range(steps):
            t = LD.mutate(rng, st, 2); v = len(abstract_run(*gp(t))) - 1
            if v >= sc: st, sc = t, v
        hist.append(sc)
        if sc > best: best, bst = sc, st
    return best, bst, hist

def gp(st):
    G = LD.genome(st, 2); pb, pe = LD.prios(st, G, "free"); return G, pb, pe

def main():
    if sys.argv[1] == "xrun":     # abstract run vs key105 (SPEC engine) on random genomes: counter runfail (unit genomes)
        seed, count = int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); bad = 0; mx = 0
        for i in range(count):
            st = LD.init(rng, 2); G, pb, pe = gp(st); a = abstract_run(G, pb, pe); b, c, *_ = K.key_run(G, pb, pe)
            bad += int([tuple(x) for x in a] != [tuple(x) for x in b]); mx = max(mx, len(a) - 1)
        print("MG106 xrun seed %d genomes %d: runfail %d | max L* %d" % (seed, count, bad, mx)); return
    if sys.argv[1] == "climb":    # MG106 climb SEED RESTARTS STEPS [OUT.json]
        seed, R, S = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); best, bst, hist = climb(seed, R, S)
        print("MG106 climb seed %d restarts %d steps %d: best L* %d | per restart %s" % (seed, R, S, best, sorted(hist, reverse=True)), flush=True)
        if len(sys.argv) > 5:
            import json; json.dump({"mode": "free", "d": 2, "state": bst, "L": best}, open(sys.argv[5], "w"))
        return
    seed, count = int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); fails = 0; units = 0; firstbad = None
    for i in range(count):
        st = LD.init(rng, 2); G = LD.genome(st, 2); pb, pe = LD.prios(st, G, "free")
        g, sig, tau, V = K.F.build_free(G, pb, pe); E = Engine(g)
        for s in itertools.product((0, 1), repeat=4):
            vs, _ = E.evaluate(tuple(K.standard(G, g, sig, V, list(s)))); kv = [E.key(vs[v]) for v in range(g.n)]
            mg = mg_values(G, pb, pe, s)
            for x in range(4):
                o = 1 - s[x]
                a1 = kv[V[("m", (x, o))]] > kv[V[("m", (x, s[x]))]]
                a2 = mg[(x, o)] > mg[(x, s[x])]
                units += 1
                if a1 != a2:
                    fails += 1
                    if firstbad is None: firstbad = (i, s, x)
    print("MG106 rand seed %d genomes %d%s: (genome, state, mover) units %d mgfail %d%s" % (seed, count, " CTRL %d" % CTRL if CTRL else "",
          units, fails, "" if firstbad is None else " | first %s" % (firstbad,)))

if __name__ == "__main__":
    main()
