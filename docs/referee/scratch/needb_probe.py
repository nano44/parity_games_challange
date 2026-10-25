#!/usr/bin/env python3
"""REFEREE succ. 10 probe for packet P-N5-NEEDB (docs/si/P-N5-NEEDB-box13.md, pin e6ee613, sha1 7471aef3...).
Own engine (rl_engine, rl_probe.states / scope_runs / opt_one_player; no lane code). C^1O asserted per game.
At every in-scope Even S4c fallback k with (h), THR and r_k >= 0 (u* != none); U := Opt(G_tau), sigma* := the engine's optimum:
 XG    every Even y in R_k with z := sigma*(y) in F_k and z's sigma*-play in F_k: (y, z) is a gate of level >= r_k;
       XGalt: also every successor z in F_k of y with y (+) U(z) = U(y) whose sigma*-play stays in F_k
 FAC   (F-a) U(x0) >= U(t), (F-c) U(x0) > Xi(x0) with lev >= r
 NB    NEED-beta in its general form (proof never uses M = -1 beyond LV-SHAPE): the sigma*-play P from x0 uses an edge (y, sigma* y) that
       is a gate and NOT Xi-exceptional; in setting (LV+) (M_k = -1) that gate must be (beta) (y in R_k, z in F_k). Case counts B/A1/A2'/A2''/A2*
At every RISE (k0 in-scope fallback, L = M_k0 >= 0, j = first S4a step changing COARSE_L(theta), no fallback in between, r > L):
 OT    OLD-THREAT at every post-rise state t: every exit x != o of o with x in F_k0 and COARSE_L(o + Xi_k0 x) = COARSE_L(theta_k0) is in R_t
 INTO  (conjecture, counted) post-rise t with r_t > L: some gate into R-bar_t;  CASEI: case (i) fallbacks (counted) and FBL there
ANTI on random one-player games (mode anti N seed): sigma' using only V-non-improving or V-exceptional edges has V_sigma' <= V.
Usage: needb_probe.py lib | files... | anti N seed"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, rho_probe as RP
EX = []


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def play(nx, v):
    pre, cyc = RE.lasso(nx, v)
    return pre, cyc


def run(g, cnt, name):
    o, st = P.states(g); P.OO[0] = o; n = g.n; T = len(st) - 1
    K = lambda x: g.key(x)
    inph, runs = P.scope_runs(st)
    for S in runs:
        cnt["scope_runs"] += 1
        Sset = set(S)
        for k in S:
            a = st[k]
            if not (a["fb"] and a["Is"]): continue
            if a["Xi"][o] == a["W"][o] or a["r"] < 0: continue
            cnt["THR_fb_r_ge0"] += 1
            r = a["r"]; t = a["t"][o]; x0 = a["sb"][o]; Rk = a["Rb"] - {o}; Fk = a["F"]
            keep = [g.succ[v] if g.owner[v] == 0 else [a["t"][v]] for v in range(n)]
            _, sstar, U = P.opt_one_player(g, keep, a["t"])
            gates = set(a["Is"]); Xi = a["Xi"]
            nxs = [sstar[v] if g.owner[v] == 0 else keep[v][0] for v in range(n)]
            # XG
            for y in Rk:
                if g.owner[y] != 0: continue
                s = a["s"][y]
                cands = [sstar[y]] + [z for z in g.succ[y] if z != sstar[y] and K(g.ext(y, U[z])) == K(U[y])]
                for i, z in enumerate(cands):
                    if z not in Fk: continue
                    pre, cyc = play(nxs, z)
                    if not set(pre + cyc) <= Fk: continue
                    tag = "XG" if i == 0 else "XGalt"
                    cnt[tag + "_chk"] += 1
                    if (y, z) not in gates or P.lev(Xi[s], Xi[z]) < r: fail(cnt, tag, name, k, y, z)
            # F-a, F-c
            cnt["FAC_chk"] += 1
            if not (K(U[x0]) >= K(U[t]) and K(U[x0]) > K(Xi[x0]) and P.lev(Xi[x0], U[x0]) >= r): fail(cnt, "FAC", name, k)
            # NEED-beta, general form
            pre, cyc = play(nxs, x0)
            Pv = pre + cyc
            good = []
            for y in Pv:
                if g.owner[y] != 0: continue
                z = sstar[y]
                if (y, z) not in gates: continue
                exc = Xi[y][0] == y and Xi[z][0] == y and Xi[z][1] == 0
                if not exc: good.append((y, z))
            if o not in Pv: case = "B"
            elif o not in cyc: case = "A1"
            else:
                lam = pre[:pre.index(o)] if o in pre else cyc[:0]
                if o in pre: lam = pre[:pre.index(o)]
                else: lam = pre + cyc[:cyc.index(o)]
                mprime = max(cyc, key=lambda v: g.rank[v])
                mK = max(lam + [o], key=lambda v: g.rank[v])
                if mprime in lam + [o]: case = "A2p"
                elif g.rank[mK] > g.rank[mprime]: case = "A2pp"
                else: case = "A2star"
            cnt["NB_case_" + case] += 1
            cnt["NB_chk"] += 1
            if not good: fail(cnt, "NB", name, k, case)
            if a["M"] == -1:
                cnt["LVplus"] += 1
                if not any(y in Rk and z in Fk for (y, z) in good): fail(cnt, "NB_beta", name, k, case)
        # rises
        for k0 in S:
            a0 = st[k0]
            if not (a0["fb"] and a0["Is"]): continue
            L = a0["M"]
            if L < 0 or L >= P.INF: continue
            th0 = P.coarse(a0["Xi"][o], L)
            s = k0 + 1; j = None
            while s in Sset and not st[s]["fb"] and st[s]["r"] > L:
                if P.coarse(st[s]["Xi"][o], L) != P.coarse(st[s + 1]["Xi"][o], L): j = s; break
                s += 1
            if j is None: continue
            if not all(st[x]["r"] > L for x in range(k0 + 1, j + 1)): continue
            cnt["rises"] += 1
            exits = [x for x in g.succ[o] if x != o and x in a0["F"] and P.coarse(g.ext(o, a0["Xi"][x]), L) == th0]
            if a0["sb"][o] not in exits: fail(cnt, "OT_threat_not_listed", name, k0)
            t = j + 1
            while True:
                cnt["OT_states"] += 1
                for x in exits:
                    cnt["OT_chk"] += 1
                    if x not in st[t]["Rb"] - {o}: fail(cnt, "OT", name, k0, j, t, x)
                if st[t]["r"] > L and st[t]["r"] < P.INF:
                    cnt["INTO_states"] += 1
                    if not any(z in st[t]["Rb"] for (y, z) in st[t]["Is"]): cnt["INTO_viol"] += 1; EX.append(("INTO_viol", name, k0, t))
                    if st[t]["fb"] and st[t]["Is"] and t in Sset:
                        cnt["CASEI"] += 1
                        if any(z in st[t]["Rb"] for (y, z) in st[t]["Is"]): fail(cnt, "CASEI_FBL", name, t)
                if t in Sset and not st[t]["fb"] and st[t]["r"] > L: t += 1
                else: break


def anti(N, seed):
    rng = random.Random(int(seed)); cnt = Counter()
    for _ in range(int(N)):
        n = rng.randint(3, 9)
        owner = [rng.randint(0, 1) for _ in range(n)]
        prio = list(range(n)); rng.shuffle(prio)
        succ = [rng.sample(range(n), rng.randint(1, min(3, n))) if owner[v] == 0 else [rng.randrange(n)] for v in range(n)]
        g = RE.Game(prio, owner, succ)
        sig = [rng.choice(g.succ[v]) if owner[v] == 0 else g.succ[v][0] for v in range(n)]
        V = [RE.play_value(g, sig, v) for v in range(n)]
        for _ in range(5):
            sp = list(sig)
            for v in range(n):
                if owner[v] != 0: continue
                ok = [u for u in g.succ[v] if g.key(V[u]) <= g.key(V[sig[v]])
                      or (V[v][0] == v and u != sig[v] and V[u][0] == v and V[u][1] == 0)]
                sp[v] = rng.choice(ok)
                if V[v][0] == v and any(u != sig[v] and V[u][0] == v and V[u][1] == 0 for u in g.succ[v]): cnt["exc_vertices"] += 1
            V2 = [RE.play_value(g, sp, v) for v in range(n)]
            cnt["ANTI_chk"] += 1
            if any(g.key(V2[v]) > g.key(V[v]) for v in range(n)): cnt["ANTI_FAIL"] += 1
    for k in sorted(cnt): print("%-30s %d" % (k, cnt[k]))
    print("FAILS", sum(v for k, v in cnt.items() if k.endswith("_FAIL")))


def main(a):
    if a and a[0] == "anti": return anti(a[1], a[2])
    if os.environ.get("START"):
        # START="s0,s1,...;t0,t1,..." : run N5 from this start pair instead of SPEC S3's (owner-irrelevant entries ignored)
        sp, tp = os.environ["START"].split(";")
        s0 = [int(x) for x in sp.split(",")]; t0 = [int(x) for x in tp.split(",")]
        RE.best_reward_start = lambda g: ([s0[v] if g.owner[v] == 0 else None for v in range(g.n)],
                                          [t0[v] if g.owner[v] == 1 else None for v in range(g.n)])
    files = RP.lib() if a == ["lib"] else a
    cnt = Counter()
    for f in files:
        g = RE.parse(f)
        try: P.assert_c1o(g)
        except AssertionError: cnt["skip_not_c1o"] += 1; continue
        if g.n > 64: cnt["skip_big"] += 1; continue
        cnt["games"] += 1
        try: run(g, cnt, os.path.relpath(f, P.ROOT))
        except RuntimeError: cnt["maxit"] += 1
        # RANDSTARTS=N: also N uniformly random start pairs (own rng, seeded by the file name)
        nr = int(os.environ.get("RANDSTARTS", "0"))
        if nr:
            rng = random.Random(f); orig = RE.best_reward_start
            for _ in range(nr):
                s0 = [rng.choice(g.succ[v]) if g.owner[v] == 0 else None for v in range(g.n)]
                t0 = [rng.choice(g.succ[v]) if g.owner[v] == 1 else None for v in range(g.n)]
                RE.best_reward_start = lambda h, s0=s0, t0=t0: (s0, t0)
                cnt["runs_randstart"] += 1
                try: run(g, cnt, os.path.relpath(f, P.ROOT) + "@rand")
                except RuntimeError: cnt["maxit"] += 1
            RE.best_reward_start = orig
    for k in sorted(cnt): print("%-30s %d" % (k, cnt[k]))
    print("FAILS", sum(v for k, v in cnt.items() if k.endswith("_FAIL")))
    for e in EX[:40]: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
