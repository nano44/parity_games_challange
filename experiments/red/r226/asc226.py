#!/usr/bin/env python3
"""L-RED 60 R226 item 1: INDEPENDENT census for L-NEW 65 BOX 197 (claude/l-new 2f4167cd) on R221 own.py (IDEAL-CYC Howard; my own Gamma
construction: gate g = (x, k) is Odd with faces e(g) [W-face] and b(g) [beta-face]; no pads). No L-NEW code used.
For every state t, vertex v, ascent (c_i, c_(i+1)) of seq_t(v) (e-vertices of Pi_t(v) in play order; ascent = next more relevant):
  g1 := first gate on the play after c_i;  w := Lambda_t(v).
  awA  : Odd takes g1's W-face (tau(g1) = e(g1))                                    [ASC-WIT (a): 0 under E-LEV]
  awBb : not (val(e(g1)) > val(b(g1)))                                               [ASC-WIT (b)]
  awC  : Lambda(e(g1)) = w and E(e(g1)) has no e at least as relevant as c_(i+1)     [ASC-WIT (c)]
  awD  : Lambda(e(g1)) != w and reward(Lambda(e(g1))) <= reward(w)                   [ASC-WIT (d)]
  rootfail: from v's FIRST ascent, iterate (g1 -> e(g1)) until Lambda(e(g1)) != w; fail if a step breaks lev(g1) < lev(c_i), (a), (b),
            or ends with a cycle node not strictly better, or the chain exceeds lev(c_i) steps   [ASC-ROOT]
Per (v, maximal interval I with Lambda(v) constant): D, Mact, tops, Rtop (top was in an earlier set of I), lexdec (top not in the new
  set: E-MON3), dfail (D > 1 + Mact + Rtop: RE-COUNT), maxalt (longest x y x y ... alternation of two symbols in the tops sequence).
Env EORD=rev reverses the e-order by level (own.py): [E-LEV] then FAILS, so awA must fire (natural control); RE-COUNT needs no [E-LEV].
Usage: asc226.py G.json ... | asc226.py rand SEED COUNT"""
import sys, os, json, random, collections
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r225"), os.path.join(H, "..", "r221")]
import own
def alt(tops):
    al = 0; S = set(tops)
    for x in S:
        for y in S:
            if x == y: continue
            L = 0; want = x
            for z in tops:
                if z == want: L += 1; want = y if want == x else x
            al = max(al, L)
    return al
def census(G, cap=3000):
    N = G["N"]; out, V, O, ow = own.run(G, cap); n, prio, o_, succ, _, _ = own.build(G); vj = own.VJ(prio); rk = vj.rk
    inv = {v: k for k, v in V.items()}; evs = {V[("e", q)] for q in O}; gates = {V[("g", q)]: q for q in O}
    levq = lambda q: G["lev"][q[0]]; c = collections.Counter()
    for t, (s, vals, tau) in enumerate(out):
        nxt = lambda u: (s[u] if u < N else (tau[u] if o_[u] == 1 else succ[u][0]))
        def play(v):
            p = []; seen = set(); u = v
            while u not in seen: seen.add(u); p.append(u); u = nxt(u)
            return p
        def asc_first(v):
            p = play(v); pos = [i for i, u in enumerate(p) if u in evs and u in vals[v][1]]
            for a, b in zip(pos, pos[1:]):
                if rk[p[b]] > rk[p[a]]: return p, a, b
            return p, None, None
        for v in range(n):
            p = play(v); pos = [i for i, u in enumerate(p) if u in evs and u in vals[v][1]]; w = vals[v][0]; first = True
            for a, b in zip(pos, pos[1:]):
                if rk[p[b]] <= rk[p[a]]: continue
                c["asc"] += 1; g1 = next(u for u in p[a + 1:b + 1] if u in gates); q = gates[g1]; ge, gb = V[("e", q)], V[("b", q)]
                if tau[g1] == ge: c["awA"] += 1; continue
                if not vj.cmp(vals[ge], vals[gb]) > 0: c["awBb"] += 1
                if vals[ge][0] == w:
                    if not any(e in evs and rk[e] >= rk[p[b]] for e in vals[ge][1]): c["awC"] += 1
                elif vj.rew(vals[ge][0]) <= vj.rew(w): c["awD"] += 1
                if first:
                    first = False; u = v; ci = p[a]; steps = 0; ok = True
                    while True:
                        pp, aa, bb = asc_first(u)
                        if aa is None: ok = False; break
                        ci = pp[aa]; gg = next(z for z in pp[aa + 1:bb + 1] if z in gates); qq = gates[gg]
                        if levq(qq) >= G["lev"][inv[ci][1][0]] or tau[gg] == V[("e", qq)] or not vj.cmp(vals[V[("e", qq)]], vals[V[("b", qq)]]) > 0: ok = False; break
                        steps += 1; ue = V[("e", qq)]
                        if vals[ue][0] != w:
                            ok = vj.rew(vals[ue][0]) > vj.rew(w); break
                        if steps > G["lev"][inv[p[a]][1][0]]: ok = False; break
                        u = ue
                    c["rootfail" if not ok else "rootok"] += 1; c["rootdepth"] = max(c["rootdepth"], steps)
    T = len(out) - 1
    for v in range(n):
        t = 0
        while t <= T:
            u = t
            while u + 1 <= T and out[u + 1][1][v][0] == out[t][1][v][0]: u += 1
            Es = [frozenset(e for e in out[i][1][v][1] if e in evs) for i in range(t, u + 1)]
            D = len(set(Es)); Ma = len(frozenset().union(*Es)); seen = set(Es[0]); tops = []; Rt = 0
            for i in range(1, len(Es)):
                a_, b_ = Es[i - 1], Es[i]
                if a_ == b_: continue
                top = max(a_ ^ b_, key=lambda e: rk[e]); tops.append(top)
                if top not in b_: c["lexdec"] += 1
                if top in seen: Rt += 1
                seen |= b_
            c["Rtop"] += Rt
            if D > 1 + Ma + Rt: c["dfail"] += 1
            c["maxalt"] = max(c["maxalt"], alt(tops)); c["maxtops"] = max(c["maxtops"], len(tops)); c["maxRtopI"] = max(c["maxRtopI"], Rt)
            t = u + 1
    c["T"] = T; return c
KEYS = ("asc", "awA", "awBb", "awC", "awD", "rootok", "rootfail", "lexdec", "dfail", "Rtop")
def show(name, cs):
    tot = collections.Counter()
    for x in cs:
        for k in KEYS: tot[k] += x[k]
    print(name, "runs", len(cs), " ".join("%s %d" % (k, tot[k]) for k in KEYS), "maxRtopI", max(x["maxRtopI"] for x in cs), "maxalt", max(x["maxalt"] for x in cs),
          "maxtops", max(x["maxtops"] for x in cs), "rootdepth", max(x["rootdepth"] for x in cs), "maxT", max(x["T"] for x in cs), flush=True)
if __name__ == "__main__":
    if sys.argv[1] == "rand":
        import latch225
        rng = random.Random(int(sys.argv[2])); show("rand %s" % sys.argv[2], [census(latch225.rgen(rng)) for _ in range(int(sys.argv[3]))])
    else:
        for f in sys.argv[1:]: show(os.path.basename(f), [census(json.load(open(f)))])
