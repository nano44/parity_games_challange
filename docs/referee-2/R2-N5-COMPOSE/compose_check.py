#!/usr/bin/env python3
r"""REFEREE-2 successor 20 (Opus 5.5, D15): own check of P-N5-COMPOSE (docs/si/P-N5-COMPOSE-box28.md, sha1 e1b977aa @ l-si 3ca0932d).
State loop: R2-N5-DUAL/dual_check.Runner (my lane's SPEC loop on si.py = SPEC S1's own implementation, read-only). Xi_t = S1 on sigma_t (G),
U_t = S1 on tau_t (G^d); lambda, lambda^U their cycle-node maps. The lane's chg/compose.py is NOT imported (run only as the pinned re-run).
MATCHED test: my lane's R2-N5-MATCHPHI/mphi_check.matched (own Mendelsohn-Dulmage matcher). Everything else from the packet's §1 definitions.
Checks (each must be 0; "side" E = Even with Xi on lambda-runs, O = Odd with U on G^d on lambda^U-runs):
  FSW    every switch of sigma (tau) at t goes along I_sigma_t (I_tau_t)                              (F-SW)
  FMON   Xi_{t+1} >= Xi_t (G's key) and U_{t+1} >=_d U_t (G^d's key) at every vertex                (F-MON)
  SWR    ENT_R(v, c) <= 1 + RISE_R(c) on: every lambda-run (lambda^U-run), every phase, the whole run, and RSUB random stretches
  LEN    RISE_R(c) <= n PCH_R(c) + n - 1 on every lambda-run / lambda^U-run and every phase; LENB: each P-value is one contiguous block;
         LEND: inside a block every change is l-only and strictly in S1's direction for Omega(c0) (on G^d: G^d's parity)
  CMP    Theorem COMPOSE chain on every lambda-run R and every phase: sum SW <= sum_{(v,c), SW(v)>0} (1 + RISE(c)) <= sum n (PCH(c)+1)
         <= m_side n (P*_R + 1); phase: |P| <= sum_v SW_P(v)
  RUN    Corollary COMPOSE-RUN: every transition is of kind (i)-(iv); #(i), #(iii) <= n(n-1); (ii) has an Even switch, (iv) an Odd
         switch and sigma unchanged; T <= 2n(n-1) + sum SW_E + sum SW_O <= 2n(n-1) + (n(n-1)+1) n (m_E (P*+1) + m_O (P*^U + 1))
  NM     §6 implication on every lambda-run (lambda^U-run), MATCHED read with the side's parities: PCH_R(c) <= (K(K+1)/2)(NM_R(c)+1) + NM_R(c)
Controls (counted, expected to bite somewhere; NOT violations): X_SWR0 ENT <= RISE (the "+1" dropped); X_LEN0 RISE <= PCH (length-only
rises exist); X_LENfull RISE <= n PCH + n - 1 on the WHOLE run (lambda not constant; did not bite in my data); X_RUN0 T <= sum SW_E +
sum SW_O (kinds (i), (iii) dropped).
Usage: compose_check.py random N nmin nmax seed [starts] | files list.txt [runs [prefix]]  (list lines: game.pg [game.start], start VALIDATED)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-DUAL")); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-MATCHPHI"))
import dual_check as DC
from mphi_check import matched, wfun
pg, Engine = DC.pg, DC.Engine
RSUB = int(os.environ.get("RSUB", "20"))


class St:
    def __init__(s): s.c, s.mx = {}, {}
    def inc(s, k, d=1): s.c[k] = s.c.get(k, 0) + d
    def mxu(s, k, v):
        if v > s.mx.get(k, -1): s.mx[k] = v
    def bad(s, k, msg):
        s.inc(k)
        if s.c[k] <= 5: print("VIOLATION", k, msg, flush=True)


def runs_of(keys):
    """maximal runs [a, b] of equal keys."""
    out, a = [], 0
    for k in range(1, len(keys) + 1):
        if k == len(keys) or keys[k] != keys[a]: out.append((a, k - 1)); a = k
    return out


def side_check(g, side, Eng, vals, strat, owner_side, R, st, name, lamrun, msg):
    """R = (a, b) a stretch of states. vals[t][v] = (c, mask, l); strat[t] = the side's strategy. Returns sum SW."""
    a, b = R; n = g.n
    rise = [0] * n; pch = [0] * n; ent = {}
    for t in range(a, b):
        for c in range(n):
            if vals[t + 1][c] != vals[t][c]: rise[c] += 1
            if vals[t + 1][c][1] != vals[t][c][1]: pch[c] += 1
        for v in range(n):
            if g.owner[v] == owner_side and strat[t][v] != strat[t + 1][v]:
                ent[(v, strat[t + 1][v])] = ent.get((v, strat[t + 1][v]), 0) + 1
    for (v, c), k in ent.items():
        st.inc(f"SWR_{side}_checks")
        if k > 1 + rise[c]: st.bad("SWR", f"{name} {msg} side {side} v={v} c={c} ENT={k} RISE={rise[c]}")
        if k > rise[c]: st.inc(f"X_SWR0_{side}")
    sw = {}
    for (v, c), k in ent.items(): sw[v] = sw.get(v, 0) + k
    if not lamrun: return sum(sw.values())
    for c in range(n):
        st.inc(f"LEN_{side}_checks")
        if rise[c] > n * pch[c] + n - 1: st.bad("LEN", f"{name} {msg} {side} c={c}")
        if rise[c] > pch[c]: st.inc(f"X_LEN0_{side}")
        # blocks and l-direction
        seen, cur = set(), None
        for t in range(a, b + 1):
            m = vals[t][c][1]
            if m != cur:
                if m in seen: st.bad("LENB", f"{name} {msg} {side} c={c}")
                seen.add(m); cur = m
            elif t > a and vals[t][c] != vals[t - 1][c]:
                c0 = vals[t][c][0]; l0, l1 = vals[t - 1][c][2], vals[t][c][2]
                good = (l1 < l0) if Eng.par[c0] == 0 else (l1 > l0)
                if vals[t][c][0] != vals[t - 1][c][0] or not good: st.bad("LEND", f"{name} {msg} {side} c={c}")
    # COMPOSE chain
    S1 = sum(sw.values())
    S2 = sum(1 + rise[c] for v in sw for c in set(g.succ[v]))
    S3 = sum(n * (pch[c] + 1) for v in sw for c in set(g.succ[v]))
    mside = sum(len(g.succ[v]) for v in range(n) if g.owner[v] == owner_side)
    S4 = mside * n * (max(pch) + 1)
    st.inc(f"CMP_{side}_checks")
    if not (S1 <= S2 <= S3 <= S4): st.bad("CMP", f"{name} {msg} {side} {S1} {S2} {S3} {S4}")
    st.mxu(f"S1/S2_{side}", round(S1 / S2, 3) if S2 else 0)
    # §6 implication: per vertex v, P-changes vs carries, MATCHED with the side's parities (Eng = the side's engine)
    for v in range(n):
        c0 = vals[a][v][0]; rc = Eng.rank[c0]
        inv = {Eng.rank[u]: u for u in range(n)}
        Rc = list(range(rc + 1, n)); K = len(Rc)
        if K == 0: continue
        par = [Eng.par[inv[r]] for r in Rc]; w = wfun(par)
        toset = lambda m: frozenset(j for j, r in enumerate(Rc) if m >> r & 1)
        p = nm = 0
        for t in range(a, b):
            A, B = toset(vals[t][v][1]), toset(vals[t + 1][v][1])
            if A == B: continue
            p += 1
            if not matched(A, B, par, w): nm += 1
        if p == 0: continue
        st.inc(f"NM_{side}_checks"); st.mxu(f"maxNM_{side}", nm); st.mxu(f"maxPCH_{side}", p)
        if p > (K * (K + 1) // 2) * (nm + 1) + nm: st.bad("NM", f"{name} {msg} {side} v={v} PCH={p} NM={nm} K={K}")
    return S1


def run_game(g, s, t, st, name, rng):
    n = g.n; E, Ed = Engine(g), Engine(DC.dual(g))
    states, fbs = DC.Runner(g).run(s, t)
    T = len(states) - 1; st.inc("runs"); st.inc("transitions", T); st.mxu("maxT", T)
    sg = [a for a, _ in states]; tu = [b for _, b in states]
    Xi, U, Is, It = [], [], [], []
    for a, b in states:
        x, _ = E.evaluate(tuple(a[v] if g.owner[v] == 0 else -1 for v in range(n))); Xi.append([tuple(z) for z in x])
        u, _ = Ed.evaluate(tuple(b[v] if g.owner[v] == 1 else -1 for v in range(n))); U.append([tuple(z) for z in u])
        Is.append(set(E.improving(tuple(a), x))); It.append(set(Ed.improving(tuple(b), u)))
    lam = [tuple(x[0] for x in X) for X in Xi]; lamU = [tuple(x[0] for x in X) for X in U]
    # F-SW, F-MON, RUN classification
    kinds = {1: 0, 2: 0, 3: 0, 4: 0}
    for k in range(T):
        for v in range(n):
            if g.owner[v] == 0 and sg[k][v] != sg[k + 1][v] and (v, sg[k + 1][v]) not in Is[k]: st.bad("FSW", f"{name}@{k} E v={v}")
            if g.owner[v] == 1 and tu[k][v] != tu[k + 1][v] and (v, tu[k + 1][v]) not in It[k]: st.bad("FSW", f"{name}@{k} O v={v}")
            if E.key(Xi[k + 1][v]) < E.key(Xi[k][v]) or Ed.key(U[k + 1][v]) < Ed.key(U[k][v]): st.bad("FMON", f"{name}@{k} v={v}")
        if lam[k + 1] != lam[k]: kinds[1] += 1
        elif sg[k + 1] != sg[k]: kinds[2] += 1
        elif lamU[k + 1] != lamU[k]: kinds[3] += 1
        elif tu[k + 1] != tu[k]: kinds[4] += 1
        else: st.bad("RUN", f"{name}@{k}: unclassified (nothing changes)")
    for i in kinds: st.inc(f"kind{i}", kinds[i])
    if kinds[1] > n * (n - 1) or kinds[3] > n * (n - 1): st.bad("RUN", f"{name}: lambda / lambda^U changes {kinds[1]} {kinds[3]}")
    sumE = sum(side_check(g, "E", E, Xi, sg, 0, R, st, name, True, f"lrun{R}") for R in runs_of(lam))
    sumO = sum(side_check(g, "O", Ed, U, tu, 1, R, st, name, True, f"lUrun{R}") for R in runs_of(lamU))
    nl, nlu = len(runs_of(lam)), len(runs_of(lamU)); st.mxu("max_lruns", nl); st.mxu("max_lUruns", nlu)
    if nl > n * (n - 1) + 1 or nlu > n * (n - 1) + 1: st.bad("RUN", f"{name}: runs {nl} {nlu}")
    # kinds (ii) / (iv) are charged to distinct in-run switches
    if kinds[2] > sumE or kinds[4] > sumO: st.bad("RUN", f"{name}: kind (ii) {kinds[2]} > SW_E {sumE} or (iv) {kinds[4]} > SW_O {sumO}")
    mE = sum(len(g.succ[v]) for v in range(n) if g.owner[v] == 0); mO = sum(len(g.succ[v]) for v in range(n) if g.owner[v] == 1)
    def pstar(vals, keys):
        best = 0
        for a, b in runs_of(keys):
            for c in range(n): best = max(best, sum(vals[t + 1][c][1] != vals[t][c][1] for t in range(a, b)))
        return best
    Ps, PsU = pstar(Xi, lam), pstar(U, lamU)
    bound = 2 * n * (n - 1) + (n * (n - 1) + 1) * n * (mE * (Ps + 1) + mO * (PsU + 1))
    st.inc("RUN_checks")
    if not (T <= 2 * n * (n - 1) + sumE + sumO <= bound): st.bad("RUN", f"{name}: T {T} sums {sumE} {sumO} bound {bound}")
    if T > sumE + sumO: st.inc("X_RUN0")
    # phases ((lambda, tau) constant): |P| <= sum SW_P and the COMPOSE chain with R := phase
    for a, b in runs_of([(lam[k], tu[k]) for k in range(T + 1)]):
        if b == a: continue
        st.inc("phases"); S1 = side_check(g, "E", E, Xi, sg, 0, (a, b), st, name, True, f"phase{(a, b)}")
        if b - a > S1: st.bad("CMP", f"{name} phase {(a, b)}: |P| {b - a} > sum SW {S1}")
    # SW-RETURN on the whole run and random stretches (any stretch; LEN not claimed there)
    side_check(g, "E", E, Xi, sg, 0, (0, T), st, name, False, "whole"); side_check(g, "O", Ed, U, tu, 1, (0, T), st, name, False, "whole")
    for _ in range(RSUB if T > 1 else 0):
        a = rng.randrange(T); b = rng.randrange(a + 1, T + 1)
        side_check(g, "E", E, Xi, sg, 0, (a, b), st, name, False, "sub"); side_check(g, "O", Ed, U, tu, 1, (a, b), st, name, False, "sub")
    # controls on the whole run
    for c in range(n):
        r = sum(Xi[t + 1][c] != Xi[t][c] for t in range(T)); p = sum(Xi[t + 1][c][1] != Xi[t][c][1] for t in range(T))
        if r > n * p + n - 1: st.inc("X_LENfull")


def main():
    st = St(); a = sys.argv[1:]; rng = random.Random(2828)
    if a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); ns = int(a[5]) if len(a) > 5 else 2; rng = random.Random(seed)
        for i in range(N):
            g = DC.rand_game(rng, rng.randint(nmin, nmax), "kO")
            for r in range(ns + 1):
                if r == 0: s, t = Engine(g).initial("best"), Engine(DC.dual(g)).initial("best")
                else: s, t = [rng.choice(g.succ[v]) for v in range(g.n)], [rng.choice(g.succ[v]) for v in range(g.n)]
                run_game(g, list(s), list(t), st, f"rand{seed}:{i}#{r}", rng)
    elif a[0] in ("files", "pairs"):
        runs = int(a[2]) if len(a) > 2 else 2; pre = a[3] if len(a) > 3 else ""
        sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RUND")); import rund_check as RC
        for line in [l.split() for l in open(a[1]) if l.strip()]:
            g = pg.read(os.path.join(DC.ROOT, pre + line[0]))
            if len(line) > 1:
                s, t = RC.read_start(g, os.path.join(DC.ROOT, pre + line[1]))
                if all((s if g.owner[v] == 0 else t)[v] in g.succ[v] for v in range(g.n)):
                    st.inc("starts_valid"); run_game(g, list(s), list(t), st, f"{line[0]}#start", rng)
                else: st.inc("starts_INVALID_skipped")
            for r in range(runs):
                if r == 0: s, t = Engine(g).initial("best"), Engine(DC.dual(g)).initial("best")
                else: s, t = [rng.choice(g.succ[v]) for v in range(g.n)], [rng.choice(g.succ[v]) for v in range(g.n)]
                run_game(g, list(s), list(t), st, f"{line[0]}#{r}", rng)
    print("MODE", " ".join(a), "RSUB", RSUB)
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"max {k}: {st.mx[k]}")
    bad = sum(st.c.get(k, 0) for k in ("FSW", "FMON", "SWR", "LEN", "LENB", "LEND", "CMP", "RUN", "NM"))
    print("RESULT", "PASS" if bad == 0 else "FAIL", "violations", bad)


if __name__ == "__main__":
    main()
