#!/usr/bin/env python3
"""L-RED R143: check Lemma SETTLE on real N5 (n5b SPEC) traces. For every W-constant interval I (wint.py definition): layer(v) := length
of W(v) (fixed on I); U_k := {sigmabar_k(g) : Odd g, sigmabar_k(g) != tau(g)} + {Xi-successor of every W-cycle node}. A transition
k -> k+1 of I is an EVENT if sigmabar changes, sigma changes at a W-cycle node, or Xi changes on U_k + U_(k+1). WINDOW = maximal run of
states of I with no event inside. Claim (per window starting at state k0): a vertex of layer d switches only at transitions k with
k - k0 <= d - 1. Hence |I| <= (D + 1)(E_I + 1), D = max layer. Prints per game: intervals, max |I|, max E_I, violations (VIOL).
Usage: settle.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.abspath(os.path.join(HERE, "..", ".."))
for p in ("n5-second", "harness", "hard-families"): sys.path.insert(0, os.path.join(EXP, p))
import n5b
pg = n5b.pg
def analyse(g, s0=None, t0=None, max_iter=5000):
    N = n5b.N5(g); N.mode = "spec"; tr, fb = [], []
    try: N.run(s0, t0, trace=tr, fbtrace=fb, max_iter=max_iter)
    except Exception as e: return None
    SG = n5b.SpecSI(g); Wc = {}
    def W(s, t):
        if t not in Wc:
            h = pg.Game(list(g.prio), list(g.owner), [[t[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(g.n)])
            Wc[t] = n5b.SpecSI(h)
        return Wc[t].evaluate(list(s))
    flat = [i for i in range(len(tr) - 1) if tr[i][1] == tr[i + 1][1] and not fb[i] and tr[i][0] != tr[i + 1][0]
            and W(*tr[i]) == W(tr[i + 1][0], tr[i][1])]
    ivs = []; 
    for i in flat:
        if ivs and ivs[-1][1] == i: ivs[-1][1] = i + 1
        else: ivs.append([i, i + 1])
    out = []
    for p, q in ivs:
        t = tr[p][1]; Wv = W(tr[p][0], t); lay = [Wv[v][2] for v in range(g.n)]
        cyc = [v for v in range(g.n) if Wv[v][0] == v]
        X = [SG.evaluate_choice(list(tr[k][0])) for k in range(p, q + 1)]
        def U(k):
            s = tr[k][0]; xi, sb = X[k - p]; u = set()
            for v in range(g.n):
                if g.owner[v] == 1 and sb[v] != t[v]: u.add(sb[v])
            for c in cyc: u.add(s[c] if g.owner[c] == 0 else sb[c])
            return u
        ev = []
        for k in range(p, q):
            s, s2 = tr[k][0], tr[k + 1][0]; (x1, b1), (x2, b2) = X[k - p], X[k + 1 - p]
            e = any(b1[v] != b2[v] for v in range(g.n) if g.owner[v] == 1) or any(s[c] != s2[c] for c in cyc if g.owner[c] == 0) \
                or any(x1[u] != x2[u] for u in U(k) | U(k + 1))
            ev.append(e)
        viol = 0; k0 = p; D = 0; nw = 0; inwin = False
        for k in range(p, q):
            if ev[k - p]: k0 = k + 1; inwin = False; continue
            if not inwin: nw += 1; inwin = True
            for v in range(g.n):
                if g.owner[v] == 0 and tr[k][0][v] != tr[k + 1][0][v]:
                    D = max(D, lay[v])
                    if k - k0 > lay[v] - 1: viol += 1
        E = sum(ev); out.append(dict(LEN=q - p, E=E, D=D, NW=nw, VIOL=viol, BOUND=(D + 1) * (E + 1)))
    return out, len(tr) - 1
if __name__ == "__main__":
    g = pg.read(sys.argv[1]); st = n5b.read_start(sys.argv[2], g) if len(sys.argv) > 2 else (None, None)
    r = analyse(g, *st)
    if r is None: print(f"SETTLE {os.path.basename(sys.argv[1])} n {g.n} RUN-ERROR"); sys.exit(0)
    out, it = r
    ml = max([o["LEN"] for o in out], default=0); me = max([o["E"] for o in out], default=0); v = sum(o["VIOL"] for o in out)
    over = sum(1 for o in out if o["LEN"] > o["BOUND"])
    print(f"SETTLE {os.path.basename(sys.argv[1])} n {g.n} it {it} intervals {len(out)} maxLEN {ml} maxE {me} VIOL {v} OVERBOUND {over} "
          + "maxNW " + str(max([o["NW"] for o in out], default=0)) + " " + " ".join(f"[{o['LEN']},{o['E']},{o['D']},{o['NW']}]" for o in out if o["LEN"] >= 2))
