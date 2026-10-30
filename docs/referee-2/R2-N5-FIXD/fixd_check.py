#!/usr/bin/env python3
r"""REFEREE-2 successor 23 (Opus 5.5, D15): own check of P-N5-FIXD (L-NEW box 91: FIX-DEPTH, FIXD-MON, PHASE-RED with FLATTR,
PHASE-RED' given CONJECTURE FLAT-SW). Pre-freeze version written from docs/new/N5-FIXD-box77.md and N5-FLATSRC-box79.md.
N5 loop: my R2-N5-DUAL/dual_check.Runner (SPEC S1-S5 on si.py's Engine, read-only); N5-LZC loop: my R2-N5-WCH/wch_check.LZRunner
(LZC=1). Coordinate sequence: my wch_check.CS (reward of c; per rank n-1..0: +1 / -1 / 0; length, negated when c is even). The lane's
experiments/new/box77/*.py and box79/*.py are NOT imported.
Phase := maximal run of consecutive states with (lambda_Xi, tau) constant (RESULTS R38 (a) KEY). fin := Xi_b for the phase [a, b].
DEPTH_t(v) := length of the common prefix of CS(Xi_t(v)) and CS(fin(v)) (n + 2 if equal). K_t := sum_v DEPTH_t(v).
Checks (each must be 0):
  XMON   Xi_t(v) ⊴ Xi_{t+1}(v) at every in-phase transition and every v (the R15 (a) premise, read on the run)
  LEXK   SPEC key order = lexicographic order of CS on all pairs (Xi_t(v), fin(v)) met (sampled)
  MON    FIXD-MON: DEPTH_{t+1}(v) >= DEPTH_t(v) for every v, every in-phase transition
  KR     K-rise transitions <= n(n+2) per phase (and K in [0, n(n+2)])
  CH     CH_P <= n(n+2) + FLATTR_P <= n(n+2) + sum_v FLAT_P(v)
  STALL  consecutive in-phase Xi-unchanged transitions <= 4n(n-1) (R15 (d) reading)
  PR     PHASE-RED |P| <= (4n(n-1)+1)(CH_P + 1) and <= (4n(n-1)+1)(n(n+2) + sum FLAT + 1)
  FSW    CONJECTURE FLAT-SW: every flat transition (Xi changes, no DEPTH rise) has a switched Even x with Xi(x) changed
  PR2    PHASE-RED': |P| <= (4n(n-1)+1)(n(n+2) + sum_x FLATSW_P(x) + 1)
  OWNC   my Lemma (L) (not in the packet): an in-phase transition all of whose switched Even vertices are their own Xi-cycle node at k
         leaves Xi unchanged
  SWS    an in-phase switched Even x that is not its own Xi-cycle node at k or k+1 has Xi_{k+1}(x) ▷ Xi_k(x)
Controls (expected > 0): X_MON_cross (DEPTH w.r.t. fin_P read from P's last state to the next phase's first state with the next phase's
fin falls somewhere: monotonicity is a per-phase fact), X_OWNC (transitions to which (L) applies), X_KSTALL (no K-rise for > 1 step).
Usage: fixd_check.py random N nmin nmax seed [starts] | files list.txt [runs [prefix]]   (LZC=1: N5-LZC)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-WCH"))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FRAME"))
import wch_check as W
F = W.F; DC, pg, Engine, dual = F.DC, F.pg, F.Engine, F.dual
MAXT = int(os.environ.get("MAXT", "5000")); LZC = os.environ.get("LZC") == "1"
VERB = os.environ.get("VERB") == "1"


def depth(A, B):
    for i in range(len(A)):
        if A[i] != B[i]: return i
    return len(A)


def run_game(g, s, t, st, name, rng):
    n = g.n
    if LZC: states, fbs = W.LZRunner(g).run(list(s), list(t), cap=MAXT)
    else: states, fbs = DC.Runner(g).run(list(s), list(t), cap=MAXT)
    E = Engine(g); K = E.key
    Even = [v for v in range(n) if g.owner[v] == 0]
    Xi = [E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))[0] for sg, _ in states]
    lam = [tuple(x[v][0] for v in range(n)) for x in Xi]
    tau = [tuple(tu[v] for v in range(n) if g.owner[v] == 1) for _, tu in states]
    CSx = [[W.CS(E, g, x[v]) for v in range(n)] for x in Xi]
    st.inc("runs"); st.inc("transitions", len(states) - 1)
    T = len(states); a = 0; phases = []
    while a < T:
        b = a
        while b + 1 < T and lam[b + 1] == lam[a] and tau[b + 1] == tau[a]: b += 1
        phases.append((a, b)); a = b + 1
    L4 = 4 * n * (n - 1); NN = n * (n + 2)
    for pi, (a, b) in enumerate(phases):
        st.inc("phases")
        fin = CSx[b]
        D = [[depth(CSx[t][v], fin[v]) for v in range(n)] for t in range(a, b + 1)]
        Ks = [sum(d) for d in D]
        if any(k < 0 or k > NN for k in Ks): st.bad("KR", f"{name} P[{a},{b}] K out of range")
        for v in range(n):
            if rng.random() < 0.05:
                x, y = Xi[a][v], Xi[b][v]
                if x != y and ((K(x) < K(y)) != (CSx[a][v] < fin[v])): st.bad("LEXK", f"{name} v={v}")
                st.inc("LEXK_checks")
        CH = KR = FLATTR = 0; FLAT = [0] * n; FLATin = [0] * n; FSW = [0] * n; stall = kst = 0; mstall = mkst = 0
        for k in range(a, b):
            i = k - a; sw = [x for x in Even if states[k + 1][0][x] != states[k][0][x]]
            for v in range(n):
                if K(Xi[k + 1][v]) < K(Xi[k][v]): st.bad("XMON", f"{name}@{k} v={v}")
                if D[i + 1][v] < D[i][v]: st.bad("MON", f"{name}@{k} v={v} {D[i][v]}->{D[i+1][v]}")
            # SWS and Lemma (L)
            for x in sw:
                if lam[k][x] != x and lam[k + 1][x] != x and not K(Xi[k + 1][x]) > K(Xi[k][x]): st.bad("SWS", f"{name}@{k} x={x}")
            if sw and all(lam[k][x] == x for x in sw):
                st.inc("X_OWNC")
                if Xi[k + 1] != Xi[k]: st.bad("OWNC", f"{name}@{k} sw={sw}")
            chg = Xi[k + 1] != Xi[k]
            for v in range(n):   # FLAT_P(v) per its definition: Xi(v) changes, DEPTH(v) does not (any transition)
                if Xi[k + 1][v] != Xi[k][v] and D[i + 1][v] == D[i][v]: FLAT[v] += 1
            krise = Ks[i + 1] > Ks[i]
            if chg:
                CH += 1; stall = 0
                if krise: KR += 1
                else:
                    FLATTR += 1
                    fl = [v for v in range(n) if Xi[k + 1][v] != Xi[k][v]]
                    for v in fl: FLATin[v] += 1
                    fs = [x for x in sw if Xi[k + 1][x] != Xi[k][x]]
                    if not fs: st.bad("FSW", f"{name}@{k} P[{a},{b}] sw={sw} fl={fl}")
                    for x in fs: FSW[x] += 1
            else:
                stall += 1; mstall = max(mstall, stall)
                if krise: st.bad("KR", f"{name}@{k} K rises without Xi change")
            kst = 0 if krise else kst + 1; mkst = max(mkst, kst)
        Lp = b - a
        if KR > NN: st.bad("KR", f"{name} P[{a},{b}] KR {KR}")
        if not (CH <= NN + FLATTR <= NN + sum(FLAT)): st.bad("CH", f"{name} P[{a},{b}] CH {CH} FLATTR {FLATTR} sumFLAT {sum(FLAT)}")
        if mstall > L4: st.bad("STALL", f"{name} P[{a},{b}] stall {mstall}")
        if Lp > (L4 + 1) * (CH + 1) or Lp > (L4 + 1) * (NN + sum(FLAT) + 1): st.bad("PR", f"{name} P[{a},{b}]")
        if Lp > (L4 + 1) * (NN + sum(FSW) + 1): st.bad("PR2", f"{name} P[{a},{b}]")
        if mkst > 1: st.inc("X_KSTALL")
        st.inc("n_Krise", KR); st.inc("n_FLATTR", FLATTR); st.inc("n_CH", CH); st.inc("Xi_flat_tr", Lp - CH)
        st.mxu("max_phase_len", (Lp, name)); st.mxu("max_FLAT_v", (max(FLAT), name)); st.mxu("max_FLATTR", (FLATTR, name))
        st.mxu("max_FLATSW_x", (max(FSW), name)); st.mxu("max_Kstall", (mkst, name)); st.mxu("max_Xi_unchanged_run", (mstall, name))
        st.mxu("max_FLAT_over_n", (round(max(FLAT) / n, 3), name)); st.mxu("max_FLATin_v", (max(FLATin), name))
        if sum(FLATin) > sum(FLAT): st.bad("CH", f"{name} P[{a},{b}] FLATin > FLAT")
        if VERB: print("PHASE", name, a, b, "len", Lp, "Krise", KR, "FLATTR", FLATTR, "maxFLAT", max(FLAT), "v", FLAT.index(max(FLAT)),
                       "maxFSW", max(FSW), "Kstall", mkst, flush=True)
        if pi + 1 < len(phases):   # control: monotonicity across the boundary fails somewhere
            a2, b2 = phases[pi + 1]
            if any(depth(CSx[b][v], CSx[b2][v]) > depth(CSx[a2][v], CSx[b2][v]) for v in range(n)): st.inc("X_MON_cross")


def main():
    st = F.St(); a = sys.argv[1:]; rng = random.Random(9191)
    st.mxu = lambda k, v: st.mx.__setitem__(k, v) if (k not in st.mx or v > st.mx[k]) else None
    if a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); ns = int(a[5]) if len(a) > 5 else 2; rng = random.Random(seed)
        for i in range(N):
            g = DC.rand_game(rng, rng.randint(nmin, nmax), "kO")
            for r in range(ns + 1):
                if r == 0: s, t = Engine(g).initial("best"), Engine(dual(g)).initial("best")
                else: s, t = [rng.choice(g.succ[v]) for v in range(g.n)], [rng.choice(g.succ[v]) for v in range(g.n)]
                run_game(g, list(s), list(t), st, f"rand{seed}:{i}#{r}", rng)
    else:
        runs = int(a[2]) if len(a) > 2 else 1; pre = a[3] if len(a) > 3 else ""
        for line in [l.split() for l in open(a[1]) if l.strip() and not l.startswith("#")]:
            g = pg.read(os.path.join(DC.ROOT, pre + line[0]))
            if len(line) > 1:
                s, t, ok = W.read_start(g, os.path.join(DC.ROOT, pre + line[1]))
                if ok: st.inc("starts_valid"); run_game(g, s, t, st, f"{line[0]}#start", rng)
                else: st.inc("starts_INVALID_skipped")
            for r in range(runs):
                if r == 0: s, t = Engine(g).initial("best"), Engine(dual(g)).initial("best")
                else: s, t = [rng.choice(g.succ[v]) for v in range(g.n)], [rng.choice(g.succ[v]) for v in range(g.n)]
                run_game(g, list(s), list(t), st, f"{line[0]}#{r}", rng)
            if os.environ.get("PROGRESS"): print("DONE-FILE", line[0], flush=True)
    print("MODE", " ".join(a), "MAXT", MAXT, "LZC", LZC)
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"max {k}: {st.mx[k]}")
    keys = ("XMON", "LEXK", "MON", "KR", "CH", "STALL", "PR", "FSW", "PR2", "OWNC", "SWS")
    bad = sum(st.c.get(k, 0) for k in keys)
    print("RESULT", "PASS" if bad == 0 else "FAIL", "violations", bad)


if __name__ == "__main__":
    main()
