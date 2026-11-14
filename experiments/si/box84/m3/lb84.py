#!/usr/bin/env python3
"""L-SI box 84 milestone 3: machine check of Lemma LOWER-BLIND (KEEP form: only states with sigma_t(B) = S; the ADOPTION form is false
(HIDE-BUSY: a hidden S shows its beta-face, and adoption then needs the current option to beat the others, which lower e's can decide)) (docs/si/box84-hubpair.md §5). For every SET-type option S = (w, Xi-target
B, even beta) of a mover B and every step t -> t+1 inside an interval with every cycle node constant and Lambda(B) in {K1, K2}, at which
PRIV holds at t (no play from w or from any other gate of B passes B): predict [sigma_(t+1)(B) = S] as «U(S) >lex U(g_o) for every other
option o whose gate has cycle node Lambda(B)», where U(.) = the e-vertices of the play that are at least as relevant as e_S (U(S) =
{e_S} u U(w)), and compare with Howard's actual choice. Also counts how often the FULL e-sets would disagree with U (lower e's present).
Usage: lb84.py BOX81DIR GENOME.json ..."""
import sys, os, json
B81 = sys.argv[1]
sys.path[:0] = [B81, os.path.join(B81, "ref", "experiments", "new", "box191"), os.path.join(B81, "ref", "experiments", "new", "box189")]
import idealcyc, gamma3
for f in sys.argv[2:]:
    G = json.load(open(f)); h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G, cap=3000)
    _, _, _, V = gamma3.build(G, set()); N = G["N"]; ev = {V[("e", (x, k))] for x in range(N) for k in range(len(G["opts"][x]))}
    K12 = {V[("K", 1)], V[("K", 2)]}; rank = lambda v: (h.prio[v], v)
    units = [(x, k) for x in range(N) for k, o in enumerate(G["opts"][x]) if o[1] == x and G["bp"][o[2]] == 0]
    states = []
    for s in st:
        cur = list(s0)
        for x in range(N): cur[movers[x]] = V[("g", (x, s[x]))]
        vs, sb = E.evaluate(tuple(cur)); states.append((s, cur, sb, tuple(vs[v][0] for v in range(h.n))))
    checked = wrong = lowerpresent = 0
    for t in range(len(states) - 1):
        s, cur, sb, lam = states[t]; s1 = states[t + 1][0]
        if lam != states[t + 1][3]: continue
        nxt = lambda v: cur[v] if h.owner[v] == 0 else sb[v]
        def walk(v, stop):
            seen = set(); es = []; hit = False
            while v not in seen:
                if v == stop: hit = True
                seen.add(v)
                if v in ev: es.append(v)
                v = nxt(v)
            return es, hit
        for (x, k) in units:
            B = movers[x]
            if lam[B] not in K12: continue
            eS = V[("e", (x, k))]; w = h.succ[eS][0]; Ew, pw = walk(w, B)
            others = []; priv = not pw
            for k2 in range(len(G["opts"][x])):
                if k2 == k: continue
                g = V[("g", (x, k2))]; Eg, pg = walk(g, B); priv = priv and not pg
                if lam[g] == lam[B]: others.append(Eg)
            if not priv or s[x] != k: continue
            up = lambda es: sorted((rank(v) for v in es if rank(v) >= rank(eS)), reverse=True)
            US = up(Ew + [eS]); pred = all(US > up(Eg) for Eg in others)   # lists sorted by relevance: lex = numeric word order
            checked += 1; wrong += pred != (s1[x] == k)
            lowerpresent += any(rank(v) < rank(eS) for Eg in others + [Ew] for v in Eg)
    print(os.path.basename(f), "checked", checked, "LOWER-BLIND mispredictions", wrong, "steps with lower e's present", lowerpresent)
