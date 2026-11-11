#!/usr/bin/env python3
"""REFEREE-2 successor 35: own replay of packet P-N5-CHAIN (L-NEW 64, claude/l-new 93531b03) on Γ3(G). Shares no code with L-NEW,
L-RED, REFEREE or L-SI: Γ3 builder, SPEC S1, VJ values / order, S3 and N5′-xi's S4a are REFEREE-2's own R2-P-N5-END/r2end.py
(successor 34). The xi run is re-stepped here so that every state can be inspected; counters are written from the packet's TEXT.
Per pre-fallback state t (states 0..T3) and step t → t+1 (t < T3):
  nonstd    state is not the standard state (σ(β)=xt or pb, σ(K0)=pA, σ(K1)=s, σ(K3)=K2, τ(g)=pe, τ(K2)=K2)        REACH3-ALL
  nohow     (step, mover): new σ(x) not ⊴-best under Ω_t, or σ(x) best and changed; nonmov: a non-mover Even σ changed
  t3def     states where «some mover has a strictly better successor» disagrees with «not the last pre-fallback state»
  fbidx     runs whose first fallback is not iteration T3 + 1; tot3     runs with iterations ≠ T3 + 3 (ENDGAME-3 / CHAIN3)
  cnlow     (state, v ≠ c_X): priority(Λ) < 3, or a mover / gate / pad in Π                                          CN2-3
  loc / tie (state, gate): σ̄(g) not the strictly smaller face / faces equal                                LOC-GATE3 / NO-TIE3
  k2        states: σ̄(K2) ≠ r or not Ω(r) ◁ Ω(K2)                                                                  LOC-K2-3
  bonly     (state, v outside the exclusions): Λ(v) not less relevant than every e                                   B-ONLY3
  f1 / dom / strict   F1 pointwise; DOM at every (mover, successor); STRICT at every changed mover
  emon      (step, v) with Λ equal: E_t(v) > E_(t+1)(v) lex                                                          E-MON3
  cdec      (state, v) with seq ≠ (): CHAIN-DECOMP3 fails                                                          CHAIN-DECOMP3
  upfail    (state, v): ascents of seq_t(v) > U(G); maxasc                                                             UP-B3
  wfail     quiet windows > L3; Tfail runs T3 > Q + (Q+1)·L3; TQfail runs T3 > (1 + Σ_v (D^tot_E(v) − 1))(L3 + 1)    QUIET3 / T-QUIET3
  civ       (run, v): some class of v occupied in two separate intervals (F-cls3 per vertex)
  bound     runs with T3 + 3 > CHAIN3's bound (F′ of P-N5-ASC §4 with B = U(G))
  nonconv   states where a value of class (K1, ∅) lies strictly below a value of class (K1, S≠∅) which lies strictly below another
            value of class (K1, ∅) (record: F-cls3's «each class is a convex set of values», read over ALL vertices; my W-1)
--ctrlX: every other fail counter's condition inverted or tightened (nonstd/nohow/fbidx/tot3 negated, cnlow threshold 7, bonly no
  exclusions, loc order reversed, tie = equal nodes, k2 expects K2, upfail bound −1, cdec mover test negated, f1/dom/strict/emon
  reversed, civ any class change, bound := 3, nonmov negated, TQfail bound 0): each must fire.
Usage: r2chain.py [--ctrl0] [--ctrlX] [--gen COUNT SEED KIND]... FILES...   (--ctrl0: L3 := 0 and U(G) := −1, wfail / Tfail / upfail must fire)"""
import sys, json, random, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2-P-N5-END"))
import r2end as R
from functools import cmp_to_key

CAP = 10 ** 40
def Fp(B, M):
    f = 1 + M * (M + 1) // 2
    for _ in range(B):
        f = (M * M + 3 * M + 1) * (1 + M * f * f)
        if f > CAP: return CAP        # saturated: the bound is then > 10^40, far above any iteration count here
    return f

def lexle(od, S, T):              # S ≤ T: equal or most relevant of S Δ T in T
    d = S ^ T
    if not d: return True
    return max(d, key=lambda u: od.pp[u]) in T

def run(G, C, ctrl0=False, X=False):
    g = R.build(G, "lev"); n, pr, ow, E, V = g["n"], g["pr"], g["ow"], g["E"], g["V"]
    od = R.Order(pr); dpr, dow = R.dual(pr, ow); dod = R.Order(dpr)
    N, M, O = g["N"], g["M"], g["O"]
    movers = [V[("x", x)] for x in range(N)]; gates = {V[("g", o)]: o for o in O}
    evs = {V[("e", o)] for o in O}; emin = min(od.pp[e] for e in evs)
    pads = {V[k] for k in ("pA", "s", "q", "r")} | {V[(t, o)] for t in ("pe", "pB", "pb", "m") for o in O}
    nopi = set(movers) | set(gates) | pads
    excl = {V["cW"]} | {V[("e", o)] for o in O if G["opts"][o[0]][o[1]][0] < 0} | {V[("pe", o)] for o in O if G["opts"][o[0]][o[1]][0] < 0}
    lev = G["lev"]
    U = sum(1 for (x, k) in O if G["opts"][x][k][1] >= 0 and lev[G["opts"][x][k][1]] > lev[x])
    L3 = (M + 1) * (2 * M + 1) * (N + 1) + N * (n - 1)
    if ctrl0: L3, Ub = 0, -1
    else: Ub = U
    st = R.s3(g); sig = [st[v] if ow[v] == 0 else None for v in range(n)]; tau = [st[v] if ow[v] == 1 else None for v in range(n)]
    def standard(sig, tau):
        for o in O:
            xt = G["opts"][o[0]][o[1]][1]; b = V[("b", o)]
            if sig[b] != (V[("x", xt)] if xt >= 0 else V[("pb", o)]): return False
            if tau[V[("g", o)]] != V[("pe", o)]: return False
        return sig[V["K0"]] == V["pA"] and sig[V["K1"]] == V["s"] and sig[V["K3"]] == V["K2"] and tau[V["K2"]] == V["K2"]
    it = 0; F = None; hist = []      # hist: (val, sbar) per pre-fallback state
    while True:
        val, sbar = R.s1(pr, ow, E, sig, od)
        Is = {v: [w for w in E[v] if w != sig[v] and od.cmp(val[w], val[sig[v]]) > 0] for v in range(n) if ow[v] == 0}
        Is = {v: l for v, l in Is.items() if l}
        dval, tbar = R.s1(dpr, dow, E, tau, dod)
        It = {v: [w for w in E[v] if w != tau[v] and dod.cmp(dval[w], dval[tau[v]]) > 0] for v in range(n) if ow[v] == 1}
        It = {v: l for v, l in It.items() if l}
        if F is None:
            hist.append((val, sbar, list(sig)))
            if (not standard(sig, tau)) != X: C["nonstd"] += 1
        if not Is and not It: break
        it += 1
        if it > 100000: C["capped"] += 1; break
        snew = list(sig); tnew = list(tau)
        if Is:
            A = {v: sorted(set([sig[v]] + Is.get(v, []))) if ow[v] == 0 else None for v in range(n)}
            HE = [A[v] if ow[v] == 0 else [tau[v]] for v in range(n)]
            _, hch = R.s1(dpr, dow, HE, tau, dod)
            for v in range(n):
                if ow[v] == 0: snew[v] = hch[v] if hch[v] is not None else HE[v][0]
            fx = [None if ow[v] == 0 else tau[v] for v in range(n)]; ch0 = [v for v in range(n) if ow[v] == 0]
            fw, W = R.one_player_opt(od, HE, fx, ch0, sig)
            for v in ch0:
                if len(A[v]) >= 2 and W[v][0] != v:
                    TIE = [w for w in A[v] if R.oplus(od, v, W[w]) == W[v]]
                    if not TIE: C["emptytie"] += 1; continue
                    best = [w for w in TIE if all(od.cmp(val[w], val[u]) >= 0 for u in TIE)]
                    snew[v] = snew[v] if snew[v] in best else max(best)
        if It:
            HE2 = [[sig[v]] if ow[v] == 0 else sorted(set([tau[v]] + It.get(v, []))) for v in range(n)]
            _, hc2 = R.s1(pr, ow, HE2, sig, od)
            for v in range(n):
                if ow[v] == 1: tnew[v] = hc2[v]
        isfb = snew == sig and tnew == tau
        if isfb:
            if Is:
                for v, l in Is.items():
                    bw = l[0]
                    for w in l[1:]:
                        c = od.cmp(val[w], val[bw])
                        if c > 0 or (c == 0 and w > bw): bw = w
                    snew[v] = bw
            else:
                for v, l in It.items():
                    bw = l[0]
                    for w in l[1:]:
                        c = dod.cmp(dval[w], dval[bw])
                        if c > 0 or (c == 0 and w > bw): bw = w
                    tnew[v] = bw
            if F is None: F = it
        elif F is None:   # a pre-fallback step: Howard check at the movers, nothing else changes
            for x in movers:
                bset = [w for w in E[x] if all(od.cmp(val[w], val[u]) >= 0 for u in E[x])]
                if (snew[x] not in bset or (sig[x] in bset and snew[x] != sig[x])) != X: C["nohow"] += 1
            for v in range(n):
                if ow[v] == 0 and v not in movers and (snew[v] != sig[v]) != X: C["nonmov"] += 1
        sig, tau = snew, tnew
    # T3's own definition (HOW3): the first state at which no mover has a strictly better successor; it must be the last
    # pre-fallback state (independent of how the loop stopped)
    for t, (val, sbar, sg) in enumerate(hist):
        imp = any(od.cmp(val[w], val[sg[x]]) > 0 for x in movers for w in E[x])
        if imp == (t == len(hist) - 1) or (X and t == len(hist) - 1): C["t3def"] += 1
    T3 = len(hist) - 1; C["runs"] += 1; C["maxT3"] = max(C["maxT3"], T3)
    if (F != T3 + 1) != X: C["fbidx"] += 1
    if (it != T3 + 3) != X: C["tot3"] += 1
    # ---- per state
    def play(f, v):
        seq = []; seen = set()
        while v not in seen: seen.add(v); seq.append(v); v = f[v]
        return seq
    cls = []
    for t, (val, sbar, sg) in enumerate(hist):
        f = [sg[v] if ow[v] == 0 else sbar[v] for v in range(n)]
        for v in range(n):
            c, P, k = val[v]
            if v != V["cX"] and (pr[c] < (7 if X else 3) or P & nopi): C["cnlow"] += 1
            if (v not in excl or X) and od.pp[c] >= emin: C["bonly"] += 1
        for gv, o in gates.items():
            a, b = sbar[gv], (V[("pB", o)] if sbar[gv] == V[("pe", o)] else V[("pe", o)])
            if (val[a] == val[b]) or (X and val[a][0] == val[b][0]): C["tie"] += 1
            elif od.cmp(val[a], val[b]) * (-1 if X else 1) > 0: C["loc"] += 1
        if sbar[V["K2"]] != (V["K2"] if X else V["r"]) or od.cmp(val[V["r"]], val[V["K2"]]) >= 0: C["k2"] += 1
        seqs = []
        for v in range(n):
            c = val[v][0]; pl = play(f, v)
            seq = [u for u in pl if u in evs and u in val[v][1]]
            seqs.append(seq)
            asc = sum(1 for i in range(len(seq) - 1) if od.pp[seq[i + 1]] > od.pp[seq[i]])
            C["maxasc"] = max(C["maxasc"], asc)
            if asc > (Ub if not X else -1): C["upfail"] += 1
            if seq:
                ff = seq[0]; y = f[ff]
                if (y not in movers) != X or val[y][0] != c or set(seq) != {ff} | (val[y][1] & evs): C["cdec"] += 1
        cl = [(val[v][0], frozenset(val[v][1] & evs)) for v in range(n)]; cls.append(cl)
        # record: non-convexity of class (K1, ∅) over all vertices
        K1 = V["K1"]; a0 = [val[v] for v in range(n) if cl[v] == (K1, frozenset())]; a1 = [val[v] for v in range(n) if cl[v][0] == K1 and cl[v][1]]
        if a0 and a1:
            lo = min(a0, key=cmp_to_key(od.cmp)); hi = max(a0, key=cmp_to_key(od.cmp))
            if any(od.cmp(lo, y) < 0 and od.cmp(y, hi) < 0 for y in a1): C["nonconv"] += 1
    for t in range(T3):
        v0, v1 = hist[t][0], hist[t + 1][0]; sg0, sg1 = hist[t][2], hist[t + 1][2]
        for v in range(n):
            if od.cmp(v1[v], v0[v]) * (-1 if X else 1) < 0: C["f1"] += 1
            if v0[v][0] == v1[v][0] and not (lexle(od, v1[v][1] & evs, v0[v][1] & evs) if X else lexle(od, v0[v][1] & evs, v1[v][1] & evs)): C["emon"] += 1
        for x in movers:
            for y in E[x]:
                if od.cmp(v1[x], R.oplus(od, x, v0[y])) * (-1 if X else 1) < 0: C["dom"] += 1
            if sg1[x] != sg0[x] and od.cmp(v1[x], v0[x]) * (-1 if X else 1) <= 0: C["strict"] += 1
    # ---- classes, windows
    loud = [any(cls[t][v] != cls[t + 1][v] for v in range(n)) for t in range(T3)]
    Q = sum(loud); w = best = 0
    for l in loud:
        if l: w = 0
        else:
            w += 1; best = max(best, w)
            if w > L3: C["wfail"] += 1   # counted per step beyond L3 (a window over L3 fires at least once)
    C["maxwin"] = max(C["maxwin"], best)
    D = []
    for v in range(n):
        seqc = [cls[t][v] for t in range(T3 + 1)]; blocks = [seqc[0]] + [seqc[t] for t in range(1, T3 + 1) if seqc[t] != seqc[t - 1]]
        if len(blocks) != len(set(blocks)) or (X and len(blocks) > 1): C["civ"] += 1
        D.append(len(set(seqc)))
    if T3 > Q + (Q + 1) * L3: C["Tfail"] += 1
    if T3 > (0 if X else (1 + sum(d - 1 for d in D)) * (L3 + 1)): C["TQfail"] += 1
    if not ctrl0:
        bnd = (1 + n * ((2 * M + 3) * Fp(U, M) - 1)) * (L3 + 1) + 3
        if it > (3 if X else bnd): C["bound"] += 1
    C["maxU"] = max(C["maxU"], U)
    return T3, it, F, U

KEYS = ["runs", "t3def", "nonstd", "nohow", "nonmov", "fbidx", "tot3", "capped", "emptytie", "cnlow", "loc", "tie", "k2", "bonly", "f1", "dom",
        "strict", "emon", "cdec", "upfail", "wfail", "Tfail", "TQfail", "civ", "bound", "nonconv", "maxasc", "maxwin", "maxT3", "maxU"]

def main(a):
    gens, files, ctrl0, X, i = [], [], False, False, 0
    while i < len(a):
        if a[i] == "--gen": gens.append((int(a[i + 1]), int(a[i + 2]), a[i + 3])); i += 4
        elif a[i] == "--ctrl0": ctrl0 = True; i += 1
        elif a[i] == "--ctrlX": X = True; i += 1
        else: files.append(a[i]); i += 1
    Gs = []
    for f in files:
        if f.endswith(".jsonl"): Gs += [(f"{f.split('/')[-1]}#{j}", json.loads(l)) for j, l in enumerate(open(f))]
        else:
            G = json.load(open(f))
            if isinstance(G, dict) and "genome" in G: G = G["genome"]
            if not (isinstance(G, dict) and "opts" in G and "start" in G): print(f.split("/")[-1], "skipped (not a genome)"); continue
            Gs.append((f.split("/")[-1], G))
    for cnt, seed, kind in gens:
        rng = random.Random(seed); Gs += [(f"gen{kind}{seed}#{j}", R.gen(rng, kind)) for j in range(cnt)]
    C = {k: 0 for k in KEYS}
    for name, G in Gs:
        T3, it, F, U = run(G, C, ctrl0, X)
        if not name.startswith("gen"): print(f"{name} T3 {T3} iters {it} F {F} U {U}")
    print("TOTAL" + (" CTRL0" if ctrl0 else "") + (" CTRLX" if X else "") + ": " + " ".join(f"{k} {C[k]}" for k in KEYS))

if __name__ == "__main__":
    main(sys.argv[1:])
