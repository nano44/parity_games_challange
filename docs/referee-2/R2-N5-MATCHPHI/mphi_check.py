#!/usr/bin/env python3
r"""REFEREE-2 successor 19 (Opus 5.5, D15): independent check of P-N5-MATCHPHI (docs/lit/P-N5-MATCHPHI.md, sha1 544705b7 @ l-lit 12b7d12a).
Own code; the lane's T33-match-phi-check.py is run only as the pinned re-run the Lead asked for (logs/pinned_check.txt), never imported.
MATCHED test: OWN polynomial matcher (Mendelsohn-Dulmage: a bipartite graph has a matching covering X (left) and Y (right) iff it has one
covering X and one covering Y; each found by augmenting paths), cross-checked against brute force over all matchings for |A Δ B| <= BF.
Modes:
  comb Kmax      every K <= Kmax, every parity pattern, every ordered pair (A, B), A != B:
                 F1   Fact 1: for o != i: w(i) > w(o) <=> weight({i}) > weight({o}); additivity weight(S - o + i) - weight(S) = weight({i}) - weight({o})
                 F1b  MATCHED => weight(B) > weight(A) (Fact 1's reading)
                 MP   Lemma MATCH-Phi: MATCHED => Phi(B) - Phi(A) >= 1 (every pair, improving or not)
                 MM   own matcher == brute force (|A Δ B| <= BF)
                 TIGHT  longest MATCHED-only chain (a DAG: Phi rises) vs W = K(K+1)/2 (the Corollary at NM = 0)
  seq N K L seed random sequences of subsets of K ranks (ANY sequence, no monotonicity: the Remark): COR  PCH <= W (NM + 1) + NM
  n5 ...         N5 data (files / pairs / random as in my other checkers): per (v, phase) PCH, NM, the Corollary (COR, CORn), and MP at every MATCHED
                 P-change; max NM, NM/n, carry share.
Controls (counted CTL_*, expected nonzero): CTL_noM2 (an uncovered ODD incoming rank allowed: Lemma fails?), CTL_noM1 (pairs need not
satisfy (M1)), CTL_W_K (Corollary with W := K instead of K(K+1)/2), CTL_carry_rise (carries that RAISE weight: carries are not just falls).
Usage: mphi_check.py comb Kmax | seq N K L seed | n5 files list [runs] | n5 pairs list prefix | n5 random N nmin nmax seed k [starts]"""
import sys, os, random, itertools
BF = int(os.environ.get("BF", "8"))


class St:
    def __init__(s): s.c, s.mx, s.viol = {}, {}, []
    def inc(s, k, v=1): s.c[k] = s.c.get(k, 0) + v
    def bad(s, k, m): s.inc("VIOLATIONS"); s.inc("V_" + k); s.viol.append(f"{k}: {m}")
    def mxr(s, k, v):
        if k not in s.mx or v > s.mx[k]: s.mx[k] = v


def wfun(par):   # par: list of parities of the K positions (index = pos - 1)
    return [(k + 1) if par[k] == 0 else -(k + 1) for k in range(len(par))]


def weight(A, par): return sum((1 if par[r] == 0 else -1) << r for r in A)


def phi(A, w): return sum(w[r] for r in A)


def can_cover(L, R, adj, must):
    """is there a matching covering every vertex of `must` (subset of L)? adj: L -> list of R."""
    match = {}
    def aug(u, seen):
        for v in adj[u]:
            if v in seen: continue
            seen.add(v)
            if v not in match or aug(match[v], seen):
                match[v] = u; return True
        return False
    return all(aug(u, set()) for u in must)


def matched(A, B, par, w, relax=""):
    outs, ins = sorted(A - B), sorted(B - A)
    ok = (lambda o, i: True) if relax == "noM1" else (lambda o, i: w[i] > w[o])
    must_o = [o for o in outs if par[o] == 0]
    must_i = [i for i in ins if par[i] == 1] if relax != "noM2" else []
    adjO = {o: [i for i in ins if ok(o, i)] for o in outs}
    adjI = {i: [o for o in outs if ok(o, i)] for i in ins}
    return can_cover(outs, ins, adjO, must_o) and can_cover(ins, outs, adjI, must_i)


def matched_bf(A, B, par, w):
    outs, ins = sorted(A - B), sorted(B - A)
    for k in range(min(len(outs), len(ins)) + 1):
        for so in itertools.combinations(outs, k):
            for si in itertools.permutations(ins, k):
                if not all(w[i] > w[o] for o, i in zip(so, si)): continue
                if all(par[o] == 1 for o in outs if o not in so) and all(par[i] == 0 for i in ins if i not in si): return True
    return False


def comb(Kmax, st):
    for K in range(1, Kmax + 1):
        W = K * (K + 1) // 2
        subs = [frozenset(c) for k in range(K + 1) for c in itertools.combinations(range(K), k)]
        for pat in range(2 ** K):
            par = [(pat >> k) & 1 for k in range(K)]; w = wfun(par)
            for o in range(K):
                for i in range(K):
                    if o == i: continue
                    st.inc("F1_checks")
                    if (w[i] > w[o]) != (weight({i}, par) > weight({o}, par)): st.bad("F1", f"K{K} pat{pat} o{o} i{i}")
                    for S in subs:
                        if o in S and i not in S and weight((S - {o}) | {i}, par) - weight(S, par) != weight({i}, par) - weight({o}, par):
                            st.bad("F1add", f"K{K}")
            succ = {A: [] for A in subs}
            for A in subs:
                for B in subs:
                    if A == B: continue
                    m = matched(A, B, par, w)
                    st.inc("pairs")
                    if len(A ^ B) <= BF:
                        st.inc("MM_checks")
                        if m != matched_bf(A, B, par, w): st.bad("MM", f"K{K} pat{pat} {sorted(A)}->{sorted(B)}")
                    if m:
                        st.inc("matched_pairs"); succ[A].append(B)
                        if phi(B, w) - phi(A, w) < 1: st.bad("MP", f"K{K} pat{pat} {sorted(A)}->{sorted(B)}")
                        if not weight(B, par) > weight(A, par): st.bad("F1b", f"K{K} pat{pat}")
                    else:
                        if weight(B, par) > weight(A, par): st.inc("CTL_carry_rise")
                    if not m and matched(A, B, par, w, "noM2") and phi(B, w) - phi(A, w) < 1: st.inc("CTL_noM2")
                    if not m and matched(A, B, par, w, "noM1") and phi(B, w) - phi(A, w) < 1: st.inc("CTL_noM1")
            # longest MATCHED-only chain (Phi strictly rises along it, so the graph is acyclic)
            memo = {}
            order = sorted(subs, key=lambda A: -phi(A, w))
            for A in order:
                memo[A] = max([1 + memo[B] for B in succ[A]], default=0)
            L = max(memo.values())
            if L > W: st.bad("TIGHT", f"K{K} pat{pat}: chain {L} > W {W}")
            st.mxr(f"TIGHT_K{K}", (L, W, pat))


def seq(N, K, Ln, seed, st):
    rng = random.Random(seed); W = K * (K + 1) // 2
    for _ in range(N):
        par = [rng.randint(0, 1) for _ in range(K)]; w = wfun(par)
        A = frozenset(r for r in range(K) if rng.random() < 0.5)
        pch = nm = 0; nmW = 0
        for _ in range(Ln):
            if rng.random() < 0.7:   # small local move (often matched) or a random jump
                r = rng.randrange(K); B = A ^ {r}
                if rng.random() < 0.5:
                    r2 = rng.randrange(K); B = B ^ {r2}
            else:
                B = frozenset(r for r in range(K) if rng.random() < 0.5)
            if B == A: continue
            pch += 1
            if not matched(A, B, par, w): nm += 1
            A = B
        st.inc("COR_checks")
        if pch > W * (nm + 1) + nm: st.bad("COR", f"K{K} pch {pch} nm {nm}")
        if pch > K * (nm + 1) + nm: st.inc("CTL_W_K")
        st.mxr("seq_max_ratio", (round(pch / (W * (nm + 1) + nm), 3), K, pch, nm))


def n5(args, st):
    HERE = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RUND"))
    import rund_check as R
    DC, pg = R.DC, R.pg
    rng = random.Random(1933)
    def run_game(gp, s, t, name):
        states, fbs = DC.Runner(gp).run(s, t)
        ctx = R.Ctx(gp); g, n, E = gp, gp.n, ctx.E
        S2 = R.Stats()
        I = [R.state_info(ctx, a, b, S2, name) for a, b in states]
        if S2.c.get("VIOLATIONS"): st.bad("ENGXI", name)
        st.inc("runs")
        inv = {E.rank[v]: v for v in range(n)}
        key = [(I[k]["lamX"], I[k]["tu"]) for k in range(len(I))]
        k0 = 0
        while k0 < len(I):
            k1 = k0
            while k1 + 1 < len(I) and key[k1 + 1] == key[k0]: k1 += 1
            if k1 > k0:
                st.inc("phases")
                for v in range(n):
                    c = I[k0]["lamX"][v]; rc = E.rank[c]
                    Rc = list(range(rc + 1, n)); K = len(Rc)
                    if K == 0: continue
                    par = [g.prio[inv[r]] % 2 for r in Rc]; w = wfun(par)
                    toset = lambda m: frozenset(j for j, r in enumerate(Rc) if m >> r & 1)
                    pch = nm = 0; crise = 0
                    for k in range(k0, k1):
                        A, B = toset(I[k]["xi"][v][1]), toset(I[k + 1]["xi"][v][1])
                        if I[k]["xi"][v][1] >> (rc + 1) << (rc + 1) != I[k]["xi"][v][1]: st.bad("RC", f"{name}@{k} v={v}: P not inside R_c")
                        if A == B: continue
                        pch += 1; st.inc("Pchanges")
                        if matched(A, B, par, w):
                            st.inc("matched")
                            if phi(B, w) - phi(A, w) < 1: st.bad("MP", f"{name}@{k} v={v}")
                        else: nm += 1
                    if pch == 0: continue
                    W = K * (K + 1) // 2
                    st.inc("COR_checks")
                    if pch > W * (nm + 1) + nm: st.bad("COR", f"{name} [{k0},{k1}] v={v}")
                    if pch > (n * n / 2) * (nm + 1) + nm: st.bad("CORn", f"{name} [{k0},{k1}] v={v}")
                    st.mxr("max_NM", (nm, name, k0, k1, v, n, pch))
                    st.mxr("max_NM_over_n", (round(nm / n, 3), name, k0, k1, v, n, pch))
                    st.mxr("max_PCH", (pch, name, k0, k1, v, n, nm))
                    st.mxr("max_PCH_over_bound", (round(pch / (W * (nm + 1) + nm), 4), name, k0, k1, v, pch, nm, K))
                    st.inc("NM_total", nm)
            k0 = k1 + 1
    a = args
    if a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 3
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            gp = pg.read(os.path.join(DC.ROOT, path))
            for r in range(runs):
                s, t = R.starts(gp, r, rng); run_game(gp, s, t, f"{path}#{r}")
    elif a[0] == "pairs":
        for line in [l.split() for l in open(a[1]) if l.strip()]:
            gp = pg.read(os.path.join(a[2], line[0]))
            if len(line) > 1:
                s, t = R.read_start(gp, os.path.join(a[2], line[1]))
                for v in range(gp.n):
                    x = s if gp.owner[v] == 0 else t
                    if x[v] not in gp.succ[v]: st.inc("INVALID_START_ENTRIES"); x[v] = gp.succ[v][0]
            else: s, t = R.starts(gp, 0, None)
            run_game(gp, s, t, line[0] + ("#start" if len(line) > 1 else "#S3"))
    elif a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); k = int(a[5]) if len(a) > 5 else 2; ns = int(a[6]) if len(a) > 6 else 2
        rng2 = random.Random(seed)
        sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-H3")); import h3_check as H
        for i in range(N):
            nn = rng2.randint(nmin, nmax)
            gp = DC.rand_game(rng2, nn, "kO") if k == 0 else H.rand_kO(rng2, nn, k)
            for r in range(ns):
                s, t = R.starts(gp, r, rng2); run_game(gp, s, t, f"random{seed}:{i}#{r}")


def main():
    st = St(); a = sys.argv[1:]
    if a[0] == "comb": comb(int(a[1]), st)
    elif a[0] == "seq": seq(int(a[1]), int(a[2]), int(a[3]), int(a[4]), st)
    elif a[0] == "n5": n5(a[1:], st)
    print("MODE", " ".join(a), "BF", BF)
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol[:40]: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")


if __name__ == "__main__":
    main()
