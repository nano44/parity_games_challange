#!/usr/bin/env python3
r"""REFEREE-2 successor 25 (Opus 5.5, D15): own check of P-N5-GATE (docs/new/P-N5-GATE-box120.md @ l-new 516717da, sha1 ac88915d).
Engine: my lane's DC.Runner / Engine / dual (R2-N5-FRAME via R2-N5-LATEP); start files via R2-N5-WRUN/wrun_check.read_start (validated).
The lane's box117 / box118 scripts are NOT imported. LO = Xi_sigma (G), HI = dual valuation of tau (G^d) read as a G-triple (Lemma R),
W = (sigma, tau)-play valuation; order = E.key (G's S1 order); CS = R93 (a) coordinate sequence. Checks (each must be 0):
  SQZ    LO_k <= W_k <= HI_k, LO_k <= LO_(k+1), HI_(k+1) <= HI_k (every k, v)
  SET    SETTLE-MON (SET_k subset SET_(k+1); settled values frozen)      BRK  BRACKET-MON per vertex, B_k in [0, n(n+2)]
  RED    K <= (n+1)(SG+1), K <= (n(n+2)+1)(BG+1)
  CONS   every consistent transition (tau kept, no fallback, Is = IW) changes sigma; every maximal consistent window < B
  OPT    at consistent transitions: no edge of H_k improves sigma_(k+1) in G_tau at a vertex not its own W-cycle node (R91 OPT-OFF form)
  CORL   every tau-stretch length <= (INC+1)(B-1) + INC
Counters: climb (tau-kept transitions), INC, runs INC 0, maxWchPerPhase, runs exceeding n-1, SG/n, BG/n maxima.
Usage: gate_check.py files list.txt [runs [prefix]]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-LATEP")); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-WRUN"))
import latep_check as L
import wrun_check as WR
DC, pg, Engine, dual, pval = L.DC, L.pg, L.Engine, L.dual, L.pval
SHOW = int(os.environ.get("SHOW", "3")); DUMP = os.environ.get("DUMP"); shown = {}


def run_game(g, s, t, st, name):
    n = g.n; m = sum(len(set(x)) for x in g.succ); E = Engine(g); Ed = Engine(dual(g)); K_ = E.key
    def bad(key, msg):
        st.bad(key, msg)
    states, fbs = DC.Runner(g).run(list(s), list(t), cap=L.MAXT)
    K = len(states) - 1; st.inc("runs"); st.inc("transitions", K)
    def CS(x):
        c, msk, l = x
        return (E.rew[c],) + tuple((1 if E.rankpar[q] == 0 else -1) if msk >> q & 1 else 0 for q in range(n - 1, -1, -1)) + \
            (l if E.par[c] == 1 else -l,)
    def lcp(a, b):
        i = 0
        while i < len(a) and a[i] == b[i]: i += 1
        return i
    S = []
    for sg, tu in states:
        xe, _ = E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
        LO = [tuple(z) for z in xe]; Is = set(E.improving(tuple(sg), xe))
        ue, _ = Ed.evaluate(tuple(tu[v] if g.owner[v] == 1 else -1 for v in range(n)))
        HI = [tuple(z) for z in ue]
        nx = [sg[v] if g.owner[v] == 0 else tu[v] for v in range(n)]
        W = [pval(E, nx, v) for v in range(n)]
        IW = {(y, z) for y in range(n) if g.owner[y] == 0 for z in set(g.succ[y]) if z != sg[y] and K_(W[z]) > K_(W[sg[y]])}
        S.append(dict(sg=sg, tu=tu, LO=LO, HI=HI, W=W, Is=Is, IW=IW, lamW=tuple(x[0] for x in W)))
    Bk = []; SETs = []
    for k, A in enumerate(S):
        for v in range(n):
            st.inc("SQZ_checks")
            if not (K_(A["LO"][v]) <= K_(A["W"][v]) <= K_(A["HI"][v])): bad("SQZ", f"{name}@{k} v={v} sandwich")
            if k + 1 <= K:
                B_ = S[k + 1]
                if K_(B_["LO"][v]) < K_(A["LO"][v]) or K_(B_["HI"][v]) > K_(A["HI"][v]): bad("SQZ", f"{name}@{k} v={v} mono")
        SETs.append({v for v in range(n) if A["LO"][v] == A["HI"][v]})
        Bk.append([lcp(CS(A["LO"][v]), CS(A["HI"][v])) for v in range(n)])
    for k in range(K):
        if not SETs[k] <= SETs[k + 1]: bad("SET", f"{name}@{k}")
        for v in range(n):
            if Bk[k + 1][v] < Bk[k][v]: bad("BRK", f"{name}@{k} v={v}")
    for k in range(K + 1):
        if not 0 <= sum(Bk[k]) <= n * (n + 2): bad("BRK", f"{name}@{k} range")
    # settled values frozen
    for k in range(K + 1):
        for v in SETs[k]:
            a = S[k]["LO"][v]
            for j in (k, K):
                if not (S[j]["LO"][v] == S[j]["W"][v] == S[j]["HI"][v] == a): bad("SET", f"{name}@{k} v={v} not frozen at {j}")
    def gap(flags):
        best = cur = 0
        for f in flags:
            cur = 0 if f else cur + 1; best = max(best, cur)
        return best
    SG = gap([SETs[k + 1] != SETs[k] for k in range(K)]); BG = gap([sum(Bk[k + 1]) > sum(Bk[k]) for k in range(K)])
    if K > (n + 1) * (SG + 1) or K > (n * (n + 2) + 1) * (BG + 1): bad("RED", f"{name} K {K} SG {SG} BG {BG}")
    if n: st.mxu("SG_over_n", round(SG / n, 3)); st.mxu("BG_over_n", round(BG / n, 3))
    # tau-stretches, consistency, phases
    B = (n * n - n + 1) * (n + m)
    kept = [S[k]["tu"] == S[k + 1]["tu"] for k in range(K)]
    cons = [kept[k] and not fbs[k] and S[k]["Is"] == S[k]["IW"] for k in range(K)]
    INCrun = 0; maxph = 0; climb = 0
    k = 0
    while k < K:
        if not kept[k]: k += 1; continue
        a = k
        while k < K and kept[k]: k += 1
        b = k                                   # stretch = transitions a..b-1
        L_ = b - a; inc = sum(1 for t in range(a, b) if not cons[t]); INCrun += inc; climb += L_
        if L_ > (inc + 1) * (B - 1) + inc: bad("CORL", f"{name} stretch {a}-{b}")
        t = a; win = 0
        for t in range(a, b):
            if cons[t]:
                win += 1
                if S[t + 1]["sg"] == S[t]["sg"]: bad("CONS", f"{name}@{t} consistent but sigma unchanged")
                A, C = S[t], S[t + 1]
                for y in range(n):
                    if g.owner[y] != 0 or C["lamW"][y] == y: continue
                    st.inc("OPT_checks")
                    for z in set(g.succ[y]):
                        if (z == A["sg"][y] or (y, z) in A["Is"]) and K_(C["W"][z]) > K_(C["W"][C["sg"][y]]): bad("OPT", f"{name}@{t} y={y} z={z}")
                if win >= B: bad("CONS", f"{name} window >= B")
            else: win = 0
        # lambda_W-phases inside the stretch
        cnt = 0
        for t in range(a, b):
            if t > a and S[t]["lamW"] != S[t - 1]["lamW"]: cnt = 0
            if S[t]["W"] != S[t + 1]["W"] and S[t]["lamW"] == S[t + 1]["lamW"]: cnt += 1
            maxph = max(maxph, cnt)
    st.inc("climb", climb); st.inc("INC", INCrun); st.inc("fallbacks", sum(1 for f in fbs if f))
    if INCrun == 0: st.inc("runs_INC0")
    if maxph > n - 1: st.inc("runs_exceed_n-1")
    st.mxu("maxWchPerPhase", maxph)
    if DUMP: print("RUN", name, "n", n, "K", K, "fb", sum(1 for f in fbs if f), "SG", SG, "BG", BG, "climb", climb, "INC", INCrun,
                   "maxWchPerPhase", maxph, flush=True)


L.run_game = run_game; L.read_start = WR.read_start
KEYS = ("SQZ", "SET", "BRK", "RED", "CONS", "OPT", "CORL")
if __name__ == "__main__":
    import io, contextlib, re
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf): L.main()
    bad = 0
    for l in buf.getvalue().splitlines():
        if not l.startswith("RESULT"): print(l)
        m = re.match(r"(\S+): (\d+)$", l)
        if m and m[1] in KEYS: bad += int(m[2])
    print("RESULT", "PASS" if bad == 0 else "FAIL", "violations", bad)
