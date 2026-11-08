#!/usr/bin/env python3
"""Box 193 (L-NEW successor 61): e-sequences of plays on IDEAL-CYC (box191 idealcyc.py and box189 gamma3.py, both unmodified).
Per state t and vertex v: the play from v under (sigma_t, sigma-bar_t); seq(v) := its e-vertices that lie in Pi_t(v), in play order.
Records (counts over all (state, vertex) pairs unless said otherwise):
  edomfail E-DOM-ALL-d: vertices other than c_W, K0, K3 and the e's that are more relevant than the least relevant e (must be 0)
  decfail  CHAIN-DECOMP: seq(v) = (f, ...) must give e-part(v) = {f} + e-part(y_f) and Lambda(y_f) = Lambda(v)
  tmonfail TAIL-MON: e-part(y) lex-nondecreasing between consecutive states with Lambda(y) fixed, at every W-target / c_W successor y
  ascstates (state, vertex) pairs whose seq has an ascent (consecutive a, b with rank(b) > rank(a)); maxasc = max ascents in one seq
  maxDE    max over (v, Lambda) of the number of distinct e-parts of v while Lambda(v) = that cycle node; M = number of e-vertices
  Ascent gates, for each ascent (a, b) of a mover's seq with Lambda below every e (cases of Lemma ASC-GATE, box 193 doc §4):
  edomunits / decunits / tmonunits: the number of units checked by edomfail (vertices) / decfail ((state, vertex) pairs with a
           nonempty e-sequence) / tmonfail ((consecutive state pair, W-target or c_W successor y with Lambda(y) fixed) pairs)
  asc      ascents examined; upfail = ascents whose segment y_a .. b has no beta whose Xi-target has level >= lev(a) (UP-JUMP)
  gates    gates on the segment where Odd takes beta; ci = Lambda(e_h) != w; con = b on e_h's play; chi = e_h's pre-merge part has
           an e more relevant than b; gfail = none of the three (would contradict ASC-GATE)
Usage: asc193.py FILES.json"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [os.path.join(HERE, "..", "box191"), os.path.join(HERE, "..", "box189")]
import idealcyc, gamma3


def run_states(G):
    h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G)
    _, _, _, V = gamma3.build(G, set()); name = {v: k for k, v in V.items()}
    gi = {}
    for x in range(G["N"]):
        for v in h.succ[movers[x]]: gi[(x, inv[v])] = v
    out = []
    for s in st:
        cur = list(s0)
        for x in range(G["N"]): cur[movers[x]] = gi[(x, s[x])]
        vals, sb = E.evaluate(tuple(cur))
        out.append((vals, [cur[v] if h.owner[v] == 0 else sb[v] for v in range(h.n)]))
    return h, E, V, name, out


def play(nxt, v):
    path, vis = [], set()
    while v not in vis: vis.add(v); path.append(v); v = nxt[v]
    return path


def analyse(G):
    h, E, V, name, ev = run_states(G)
    evs = [v for v in range(h.n) if name[v][0] == "e"]; ES = 0
    for v in evs: ES |= 1 << E.rank[v]
    emin = min(E.rank[v] for v in evs)
    top = {V["cW"], V[("K", 0)], V[("K", 3)]}
    edomfail = sum(1 for v in range(h.n) if v not in top and name[v][0] != "e" and E.rank[v] > emin)
    W = {v: ev[0][1][v] for v in evs}            # e -> its only successor (W-target mover or c_W), frozen
    lev = lambda v: G["lev"][name[v][1]]          # level of a mover
    r = dict(T=len(ev) - 1, M=len(evs), edomfail=edomfail, decfail=0, tmonfail=0, ascstates=0, maxasc=0, maxDE=0,
             asc=0, upfail=0, gates=0, ci=0, con=0, chi=0, gfail=0, edomunits=0, decunits=0, tmonunits=0)
    r["edomunits"] = sum(1 for v in range(h.n) if v not in top and name[v][0] != "e")
    prev, seen = {}, {}
    for t, (vals, nxt) in enumerate(ev):
        for v in range(h.n):
            lam = vals[v][0]; path = play(nxt, v)
            seq = [y for y in path if y in W and (vals[v][1] >> E.rank[y]) & 1]
            epart = vals[v][1] & ES
            assert sum(1 << E.rank[y] for y in seq) == epart, (t, v)
            na = sum(1 for p, q in zip(seq, seq[1:]) if E.rank[q] > E.rank[p])
            if na: r["ascstates"] += 1
            r["maxasc"] = max(r["maxasc"], na)
            if seq:
                r["decunits"] += 1; y = W[seq[0]]
                if not (vals[y][0] == lam and (vals[y][1] & ES) | (1 << E.rank[seq[0]]) == epart): r["decfail"] += 1
            seen.setdefault((v, lam), set()).add(epart)
            if v in prev and prev[v][0] == lam and v in W.values():
                r["tmonunits"] += 1; d = prev[v][1] ^ epart
                if d and not (epart >> (d.bit_length() - 1)) & 1: r["tmonfail"] += 1
            prev[v] = (lam, epart)
            if name[v][0] != "x" or E.rank[lam] >= emin: continue
            for a, b in zip(seq, seq[1:]):
                if E.rank[b] <= E.rank[a]: continue
                r["asc"] += 1; seg = path[path.index(a) + 1: path.index(b)]
                la = lev(V[("x", name[a][1][0])])
                up = any(name[z][0] == "b" and name[nxt[z]][0] == "x" and lev(nxt[z]) >= la
                         and lev(nxt[z]) > lev(V[("x", name[z][1][0])]) for z in seg)   # strictly upward Xi-edge (fixes entry 2, W-4)
                if not up: r["upfail"] += 1
                for g in seg:
                    if name[g][0] != "g" or name[nxt[g]][0] != "b": continue
                    r["gates"] += 1; eh = V[("e", name[g][1])]
                    if vals[eh][0] != lam: r["ci"] += 1; continue
                    pe, pb = play(nxt, eh), play(nxt, nxt[g])
                    if b in pe: r["con"] += 1; continue
                    sb = set(pb); Ap = []
                    for z in pe:
                        if z in sb: break
                        Ap.append(z)
                    if any(z in W and E.rank[z] > E.rank[b] for z in Ap): r["chi"] += 1
                    else: r["gfail"] += 1
    r["maxDE"] = max(len(s) for s in seen.values())
    return r


if __name__ == "__main__":
    for f in sys.argv[1:]:
        G = json.load(open(f)); a = analyse(G)
        print(os.path.basename(f), "N", G["N"], " ".join(f"{k} {v}" for k, v in a.items()))
