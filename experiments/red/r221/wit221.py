#!/usr/bin/env python3
"""L-RED 56 R221: (1) WITNESS: at every (t, v) and every e_g of seq_t(v) that is followed in seq_t(v) by a more relevant e (a climbing e),
classify why Odd's gate g is on e at t: LAM (Lambda(beta_g) != Lambda(e_g)), RET (the beta-play passes g), EST (equal Lambda, not RET:
E(beta_g) >lex E(e_g), FLIP-E). For EST, record whether the top of E(e_g) xor E(beta_g) is more relevant than every e of seq_t(v) after e_g
(ABOVE: the witness sees above the climb's rest). (2) DROP: per (v, Lambda-interval), #changes of seq(v) whose FIRST e is less relevant
than the previous first e (a re-entry from below = re-climb), and #lex decreases of E(v) (E-MON check). Unit/scope in the header line.
Usage: wit221.py G.json ..."""
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import own
def lexgt(A, B, rk):
    d = A ^ B
    if not d: return False
    return max(d, key=lambda u: rk[u]) in A
for f in sys.argv[1:]:
    G = json.load(open(f)); N = G["N"]; out, V, O, o_ = own.run(G); n, prio, _, succ, _, _ = own.build(G); rk = own.VJ(prio).rk
    evs = {V[("e", q)]: q for q in O}; cnt = {"LAM": 0, "RET": 0, "EST": 0, "EST_ABOVE": 0, "EST_bad": 0}; rows = []
    for t, (s, vals, tau) in enumerate(out):
        nxt = lambda v: (s[v] if v < N else (tau[v] if o_[v] == 1 else succ[v][0])); r = []
        def seqof(v):
            Pi = vals[v][1]; seq = []; seen = []; u = v
            while u not in seen:
                seen.append(u)
                if u in evs and u in Pi: seq.append(u)
                u = nxt(u)
            return seq, seen
        for v in range(n):
            seq, _ = seqof(v); r.append((vals[v][0], tuple(seq)))
            for i in range(len(seq) - 1):
                if seq[i] == v or not any(rk[w] > rk[seq[i]] for w in seq[i + 1:]): continue   # v = e_g itself: g not on the play
                q = evs[seq[i]]; e, b, g = V[("e", q)], V[("b", q)], V[("g", q)]
                if vals[e][0] != vals[b][0]: cnt["LAM"] += 1; continue
                if g in seqof(b)[1]: cnt["RET"] += 1; continue
                Ee, Eb = set(seqof(e)[0]), set(seqof(b)[0]); cnt["EST"] += 1
                if not lexgt(Eb, Ee, rk): cnt["EST_bad"] += 1; continue
                z = max(Eb ^ Ee, key=lambda u: rk[u])
                if all(rk[z] > rk[w] for w in seq[i + 1:]): cnt["EST_ABOVE"] += 1
        rows.append(r)
    drops = 0; mxdrop = 0; dec = 0
    for v in range(n):
        t = 0
        while t < len(rows):
            u = t
            while u + 1 < len(rows) and rows[u + 1][v][0] == rows[t][v][0]: u += 1
            dv = 0
            for i in range(t + 1, u + 1):
                a, b = rows[i - 1][v][1], rows[i][v][1]
                if a != b:
                    if lexgt(set(a), set(b), rk): dec += 1
                    if a and b and rk[b[0]] < rk[a[0]]: dv += 1
            drops += dv; mxdrop = max(mxdrop, dv); t = u + 1
    print(f"{f.split('/')[-1]} N {N} T {len(out) - 1} climbing-e (t,v,e) triples: {cnt} | re-entries total {drops} max per (v,interval) {mxdrop} | E lex decreases {dec}", flush=True)
