#!/usr/bin/env python3
"""REFEREE succ. 12 probe for packet P-N5-FBK (docs/new/P-N5-FBK-box44.md, pin 5d723af6, sha1 afd7c65a...). Own engine (rl_engine via
dual_probe.run5; kappa / kwt from fbred_probe; helpers from twot_probe). Any game; per phase, per class U_c, Q_c := (Q n U_c) - {c}.
 ROUTE  ROUTE-k: at every state, q -> par_t(q) (first vertex of Q_c - {q} on q's honest play, q not direct) has no cycle; depth <= m_c - 1
 SATK   SAT-k: q not direct, p = par_t(q), t in p-run Theta_p, t > f^{Theta_p}_{w_c} => kappa_t(q) in S_{q,p} + kappa_t(p)   [n <= PATHN]
        (the packet's extra hypothesis t > g_{w_c} is NOT imposed here: the proof does not use it; counted separately as SATK_g)
 FBKT   Theorem FB-kT: N_late <= 1 + sum_q (V_q - 1) and V_q <= sum_h D_c ((m_c - 1) D_c)^h  (phases with a late fallback)
 ALT    Lemma ALT: every in-phase change of sigma-bar(q), q in Q_c, q != c: CLEAN => kappa_{t+1}(q) >= kappa_t(q), equality only at a tie
 NEP    Corollary: N_ep <= 1 + sum_q (rho_q + tie_q + nc_q + cyc_q)
 MUT    env FBK_MUT=1: SAT-k with S_{q,p} shifted by the smallest nonzero kwt step (must bite where SAT-k is exercised)
Usage: fbk_probe.py lib | rand N nmin nmax k seed | list file | files...   (env RANDSTARTS=N, PATHN=14)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, rho_probe as RP, dual_probe as D, fbred_probe as F, twot_probe as TT
EX = []
PATHN = int(os.environ.get("PATHN", "14"))
MUT = os.environ.get("FBK_MUT", "") == "1"


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def run_check(g, start, cnt, name):
    A = D.run5(g, start); n = g.n; small = n <= PATHN
    Q = {v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1}
    info = []
    for a in A:
        Xi, sb = RE.evaluate(g, a["s"])
        info.append(dict(Xi=Xi, sb=sb, hg=[a["s"][v] if g.owner[v] == 0 else sb[v] for v in range(n)]))
    T_ = len(A) - 1
    key = [(tuple(x[0] for x in info[k]["Xi"]), tuple(A[k]["t"])) for k in range(T_ + 1)]
    k = 0
    while k <= T_:
        j = k
        while j < T_ and key[j] == key[j + 1]: j += 1
        p0, p1 = k, j; k = j + 1
        lam = key[p0][0]; C = set(lam); T = C | Q
        U = {c: {v for v in range(n) if lam[v] == c} for c in C}
        fbs = [x for x in range(p0, p1) if A[x]["fb"]]; f = len(fbs)
        Qc = {c: (Q & U[c]) - {c} for c in C}
        cnt["phases"] += 1
        def kap(t, z): return F.kap(g, info[t]["Xi"][z], lam[z])
        def play(t, v):
            seq, seen = [], set()
            while v not in seen: seen.add(v); seq.append(v); v = info[t]["hg"][v]
            return seq, v
        def on_cycle(t, q): return play(t, q)[1] == q
        def par(t, q, c):
            """None if direct, else first vertex of Qc - {q} on q's play"""
            if on_cycle(t, q): return None
            for v in play(t, q)[0][1:]:
                if v == c: return None
                if v in Qc[c]: return v
            return None
        def qruns(q):
            runs, cur = [], []
            for t in range(p0, p1 + 1):
                if cur and info[t]["Xi"][q] != info[cur[-1]]["Xi"][q]: runs.append(cur); cur = []
                cur.append(t)
            runs.append(cur); return runs
        if small:
            kopt_q = {}
            for c in C:
                for q in Qc[c]:
                    nodes = U[c] - (T - {q})
                    kopt_q[q] = {z: TT.best(TT.spaths(g, nodes, q, z, c)) for z in U[c]}
        for c in C:
            w = len(U[c]) - 1
            for t in range(p0, p1 + 1):
                # ROUTE-k
                pr = {q: par(t, q, c) for q in Qc[c]}
                for q in Qc[c]:
                    seen, x, d = {q}, q, 0
                    while pr.get(x) is not None:
                        x = pr[x]; d += 1
                        if x in seen: fail(cnt, "ROUTE", name, t, q); break
                        seen.add(x)
                    cnt["ROUTE_chk"] += 1
                    if d > max(len(Qc[c]) - 1, 0): fail(cnt, "ROUTE_depth", name, t, q, d)
                    cnt["max_depth"] = max(cnt["max_depth"], d)
            if not small: continue
            runmap = {}
            for p in Qc[c]:
                for Th in qruns(p):
                    for t in Th: runmap[(p, t)] = Th
            for t in range(p0, p1 + 1):
                for q in Qc[c]:
                    p = par(t, q, c)
                    if p is None: continue
                    Th = runmap[(p, t)]; fTh = [x for x in fbs if x in Th]
                    if not (w <= 0 or (len(fTh) >= w and t > fTh[w - 1])): continue
                    S = set()
                    for y in g.succ[q]:
                        if y not in U[c]: continue
                        if y == p: S.add(F.kwt(g, q, c))
                        elif y not in T and kopt_q[p][y] is not None: S.add(F.add(F.kwt(g, q, c), kopt_q[p][y]))
                    if MUT: S = {(a + 1, b) for a, b in S}
                    cnt["SATK_chk"] += 1
                    cnt["SATK_g"] += bool(w <= 0 or (f >= w and t > fbs[w - 1]))
                    if F.add(kap(t, q), (-kap(t, p)[0], -kap(t, p)[1])) not in S: fail(cnt, "SATK", name, t, q, p)
        # ALT and N_ep
        tie = nc = cyc = rho = 0; ep = 1
        for t in range(p0, p1):
            rho += sum(1 for q in Q if info[t]["Xi"][q] != info[t + 1]["Xi"][q])
            ch = [q for q in Q if info[t]["sb"][q] != info[t + 1]["sb"][q]]
            if ch: ep += 1
            for q in ch:
                c = lam[q]
                if q == c: cyc += 1; continue
                y1, y2 = info[t]["sb"][q], info[t + 1]["sb"][q]
                clean = (not on_cycle(t, q)) and (not on_cycle(t + 1, q)) and q not in play(t, y2)[0]
                cnt["ALT_changes"] += 1
                if not clean: nc += 1; cnt["ALT_nonclean"] += 1; continue
                k0, k1 = kap(t, q), kap(t + 1, q)
                if k1 < k0: fail(cnt, "ALT", name, t, q)
                elif k1 == k0:
                    istie = kap(t, y2) == kap(t, y1) and kap(t + 1, y2) == kap(t, y2)
                    cnt["ALT_tie"] += 1
                    if not istie: fail(cnt, "ALT_eq", name, t, q)
                    tie += 1
                else: cnt["ALT_strict"] += 1
        cnt["NEP_chk"] += 1; cnt["max_epochs"] = max(cnt["max_epochs"], ep)
        if ep > 1 + rho + tie + nc + cyc: fail(cnt, "NEP", name, p0, ep)
        # FB-kT
        late = [x for jj, x in enumerate(fbs, 1) if jj >= n]
        if late:
            cnt["FBKT_chk"] += 1
            Nl = len({tuple(info[x]["Xi"][q] for q in sorted(Q)) for x in late})
            b = 1
            for c in C:
                mc = len(Qc[c]); w = len(U[c]) - 1
                if not mc: continue
                Dc = max(len([y for y in g.succ[q] if y in U[c]]) for q in Qc[c]) + w
                Vq = sum(Dc * ((mc - 1) * Dc) ** h for h in range(mc))
                b += mc * (Vq - 1)
            if Nl > b: fail(cnt, "FBKT", name, p0, Nl, b)


def main(a):
    nr = int(os.environ.get("RANDSTARTS", "0")); cnt = Counter()
    if a and a[0] == "rand":
        N, lo, hi, kk, seed = map(int, a[1:6]); rng = random.Random(seed)
        gs = [("rand%d_%d" % (seed, i), D.rand_ck(rng, rng.randint(lo, hi), kk)) for i in range(N)]
    elif a and a[0] == "list":
        gs = [(l.split()[0], RE.parse(os.path.join(P.ROOT, l.split()[0]))) for l in open(a[1]) if l.strip()]
    else:
        gs = [(os.path.relpath(f, P.ROOT), RE.parse(f)) for f in (RP.lib() if a == ["lib"] else a)]
    for name, g in gs:
        if g.n > int(os.environ.get("MAXN", "64")): cnt["skip_big"] += 1; continue
        cnt["games"] += 1
        for i, st in enumerate([RE.best_reward_start(g)] + [D.rand_start(g, random.Random(name + str(i))) for i in range(nr)]):
            try: run_check(g, st, cnt, name + ("@r%d" % i if i else ""))
            except RuntimeError: cnt["maxit"] += 1
    for k in sorted(cnt): print("%-26s %d" % (k, cnt[k]))
    print("FAILS", sum(v for k, v in cnt.items() if k.endswith("_FAIL")))
    for e in EX[:40]: print("EX (", e)


if __name__ == "__main__":
    main(sys.argv[1:])
