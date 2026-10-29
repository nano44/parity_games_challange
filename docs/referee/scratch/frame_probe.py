#!/usr/bin/env python3
"""REFEREE successor 18: own control for packet P-N5-FRAME (L-NEW box 65, l-new 938d8796, sha1 ce8c4803).
Own engine rl_engine (SPEC S1-S5 from the text; no lane code). Per N5 run:
  FRT   FRAME-tau (ii) tau_{t+1}(o) in {tau_t(o)} u I_tau_t(o); (iii) no tau repeats
  DUAL  DUAL-ORDER: G^d's key order is the exact reverse of G's on the values met (random pairs per state)
  OFZ   ODD-FREEZE / ENT-FREEZE: at every state, every Odd o, e in succ(o), e != tau(o), every simple path P_e from e to o (Odd vertices
        other than o follow tau, Even vertices free; = an (H1') witness) with (H2) and (H3): assert (o, e) not in I_tau and tau_{t+1}(o) != e
  SUCC  SUCC-MON: Xi_t(sigma_t(y)) non-decreasing;  LATE  LATE-RISE on every pair t < u (runs up to 150 transitions)
  GPR   GP*-RUN on W-runs (tau-stretch, no S4c, lambda_W constant; sigma-bar and lambda_Xi free): GP* by capped DFS, FW-R*
  RRS   R*-RISE: late adoptions of each Even edge (y, z) in a W-run <= RISE_F(z) (Xi-changes of z in F)
  STR   STRETCH-RED per tau-stretch: |S| <= Q + (Q+1)((n-1)(R*_S+1) + FL_S), Q <= fb_S + n(n-1)(fb_S+1), fb_S <= n(n-1) + (n(n-1)+1)(1+(n-1)(2+rho_S))
        (rho_S taken in its smallest reading: transitions of the phase at which some Odd choice vertex's Xi changes)
MUT: 1 drop (H3)'s "more relevant than w"; 2 drop (H2); 3 drop (H3)'s "even"; 4 GP* on W-runs without the blocked condition.
Usage: frame_probe.py rand N lo hi seed | FILES...  (env MAXN, RANDSTARTS, CAP)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE
MUT = int(os.environ.get("MUT", "0")); CAP = int(os.environ.get("CAP", "4000"))
EX = []


def fail(cnt, tag, *a):
    cnt[tag + "_V"] += 1
    if len(EX) < 30: EX.append((tag,) + a)


def stretches(keys, cut=lambda t: False):
    out, i, T = [], 0, len(keys) - 1
    while i <= T:
        j = i
        while j < T and keys[j + 1] == keys[i] and not cut(j): j += 1
        out.append((i, j)); i = j + 1
    return out


def analyse(cnt, g, start, name):
    n = g.n; gd = g.dual(); st = RE.run(g, start); T = len(st) - 1
    cnt["RUNS"] += 1; cnt["TRANS"] += T
    S = [x["s"] for x in st]; Tt = [x["t"] for x in st]; key = g.key; keyd = gd.key
    nxs = [[S[t][v] if g.owner[v] == 0 else Tt[t][v] for v in range(n)] for t in range(T + 1)]
    W = [[RE.play_value(g, nx, v) for v in range(n)] for nx in nxs]
    Xi = [x["Xi"] for x in st]; U = [x["Ut"] for x in st]
    tbar = [RE.evaluate(gd, [Tt[t][v] if g.owner[v] == 1 else None for v in range(n)])[1] for t in range(T + 1)]
    It = [set(x["It"]) for x in st]; Is = [set(x["Is"]) for x in st]
    oddv = [v for v in range(n) if g.owner[v] == 1]
    # FRT
    seen = set()
    for t in range(T + 1):
        k = tuple(Tt[t][o] for o in oddv)
        if t == 0 or k != tuple(Tt[t - 1][o] for o in oddv):
            if k in seen: fail(cnt, "FRT_rep", name, t)
            seen.add(k)
        if t < T:
            for o in oddv:
                cnt["FRT_chk"] += 1
                if Tt[t + 1][o] != Tt[t][o] and (o, Tt[t + 1][o]) not in It[t]: fail(cnt, "FRT", name, t, o)
    # DUAL-ORDER on values met
    rng = random.Random(name)
    for t in range(T + 1):
        for _ in range(5):
            a, b = W[t][rng.randrange(n)], Xi[t][rng.randrange(n)]
            cnt["DUAL_chk"] += 1
            if a != b and ((key(a) < key(b)) != (keyd(a) > keyd(b))): fail(cnt, "DUAL", name, t)
    # ODD-FREEZE / ENT-FREEZE
    for t in range(T + 1):
        nxU = [tbar[t][v] if g.owner[v] == 0 else Tt[t][v] for v in range(n)]
        for o in oddv:
            if len(g.succ[o]) < 2: continue
            h = Tt[t][o]; pre, cy = RE.lasso(nxU, h); rho = set(pre) | set(cy)
            w = max(cy, key=lambda u: g.rank[u])
            for e in g.succ[o]:
                if e == h: continue
                cnt["OFZ_pairs"] += 1
                budget = CAP; stack = [[e]]; hit = None
                while stack and budget > 0 and hit is None:
                    path = stack.pop(); budget -= 1; y = path[-1]
                    if y == o:
                        P = set(path); top = max(path, key=lambda u: g.rank[u])
                        h2 = not (rho & P)
                        h3a = g.prio[top] % 2 == 0; h3b = g.rank[top] > g.rank[w]
                        if (h2 or MUT == 2) and (h3a or MUT == 3) and (h3b or MUT == 1): hit = path
                        continue
                    succ = g.succ[y] if g.owner[y] == 0 else [Tt[t][y]]
                    for z in succ:
                        if z not in path: stack.append(path + [z])
                if hit is None: continue
                cnt["OFZ_hits"] += 1; cnt["OFZ_hitlen_max"] = max(cnt["OFZ_hitlen_max"], len(hit))
                tag = "OFZ" + ("_MUT%d" % MUT if MUT in (1, 2, 3) else "")
                if (o, e) in It[t]: fail(cnt, tag, name, t, o, e, hit)
                if t < T and Tt[t + 1][o] == e: fail(cnt, tag + "_ENT", name, t, o, e)
    # SUCC-MON, LATE-RISE
    for t in range(T):
        for y in range(n):
            if g.owner[y] == 0:
                cnt["SUCC_chk"] += 1
                if key(Xi[t + 1][S[t + 1][y]]) < key(Xi[t][S[t][y]]): fail(cnt, "SUCC", name, t, y)
    if T <= 150:
        for y in range(n):
            if g.owner[y] != 0: continue
            for z in g.succ[y]:
                notin = [t for t in range(T + 1) if (y, z) not in Is[t]]
                for u in range(T + 1):
                    if (y, z) in Is[u]:
                        for t in notin:
                            if t < u:
                                cnt["LATE_chk"] += 1
                                if not key(Xi[u][z]) > key(Xi[t][z]): fail(cnt, "LATE", name, t, u, y, z)
    # W-runs inside tau-stretches; STRETCH-RED
    lamW = [tuple(v[0] for v in w) for w in W]; lamX = [tuple(v[0] for v in x) for x in Xi]
    tauk = [tuple(Tt[t][o] for o in oddv) for t in range(T + 1)]

    def blocked(t, x, z): return key(W[t][z]) > key(W[t][nxs[t][x]]) and (x, z) not in Is[t]

    for (sa, sb_) in stretches(tauk):
        L = sb_ - sa; cnt["STRETCHES"] += 1
        fbS = sum(1 for t in range(sa, sb_) if st[t]["fb"])
        Q = sum(1 for t in range(sa, sb_) if st[t]["fb"] or lamW[t + 1] != lamW[t])
        FL = sum(1 for t in range(sa, sb_) if S[t + 1] != S[t] and W[t + 1] == W[t])
        # phases (lambda_Xi constant) inside S; rho in its smallest reading
        rhoS = 0
        for (pa, pb) in stretches(lamX[sa:sb_ + 1]):
            pa += sa; pb += sa
            r = sum(1 for t in range(pa, pb) if any(Xi[t + 1][o] != Xi[t][o] for o in oddv if len(g.succ[o]) > 1))
            rhoS = max(rhoS, r)
        RS = 0
        for (a, b) in stretches(lamW[sa:sb_ + 1], cut=lambda j: st[j + sa]["fb"]):
            a += sa; b += sa
            cnt["WRUNS"] += 1
            if any(lamX[t + 1] != lamX[t] for t in range(a, b)): cnt["WRUN_lamXi_changes"] += 1
            if any(tuple(st[t + 1]["sb"][o] for o in oddv) != tuple(st[t]["sb"][o] for o in oddv) for t in range(a, b)): cnt["WRUN_sbar_changes"] += 1
            cyc = {u for u in range(n) if lamW[a][u] == u}
            for t in range(a, b):
                for v in range(n):
                    cnt["WMON_chk"] += 1
                    if key(W[t + 1][v]) < key(W[t][v]): fail(cnt, "WMON", name, a, b, t, v)
            # GP* (capped DFS)
            for k in range(a, b + 1):
                budget = [CAP]
                for x in range(n):
                    wk = key(W[k][x]); stack = [[x]]
                    while stack and budget[0] > 0:
                        path = stack.pop(); budget[0] -= 1; y = path[-1]; Lp = len(path) - 1
                        if y in cyc:
                            P = 0
                            for q in path[:-1]:
                                if g.rank[q] > g.rank[y]: P |= 1 << g.rank[q]
                            cnt["GPR_chk"] += 1
                            if key((y, P, Lp)) > wk: fail(cnt, "GPR" + ("_MUT4" if MUT == 4 else ""), name, a, b, k, x, path)
                        if Lp >= k - a or Lp >= n - 1: continue
                        tt = k - 1 - Lp
                        succ = g.succ[y] if g.owner[y] == 0 else [Tt[k][y]]
                        for z in succ:
                            if z in path: continue
                            if g.owner[y] == 0 and MUT != 4 and blocked(tt, y, z): continue
                            stack.append(path + [z])
            # FW-R*, R*-RISE
            WCH = sum(1 for t in range(a, b) if W[t + 1] != W[t])
            blk = set(); RT = 0; late = Counter()
            for t in range(a, b):
                lt = False
                for y in range(n):
                    if g.owner[y] == 0 and S[t + 1][y] != S[t][y] and (y, S[t + 1][y]) in blk:
                        lt = True; late[(y, S[t + 1][y])] += 1
                RT += lt
                for y in range(n):
                    if g.owner[y] == 0:
                        for z in g.succ[y]:
                            if blocked(t, y, z): blk.add((y, z))
            cnt["FWR_chk"] += 1; RS = max(RS, RT)
            if WCH > (n - 1) * (RT + 1): fail(cnt, "FWR", name, a, b, WCH, RT)
            for (y, z), c in late.items():
                rise = sum(1 for t in range(a, b) if Xi[t + 1][z] != Xi[t][z])
                cnt["RRS_chk"] += 1
                if c > rise: fail(cnt, "RRS", name, a, b, y, z, c, rise)
            cnt["RT_max"] = max(cnt["RT_max"], RT)
        N2 = n * (n - 1)
        cnt["STR_chk"] += 1
        ok = (L <= Q + (Q + 1) * ((n - 1) * (RS + 1) + FL) and Q <= fbS + N2 * (fbS + 1)
              and fbS <= N2 + (N2 + 1) * (1 + (n - 1) * (2 + rhoS)))
        if not ok: fail(cnt, "STR", name, sa, sb_, L, Q, RS, FL, fbS, rhoS)
        cnt["stretch_max"] = max(cnt["stretch_max"], L); cnt["fbS_max"] = max(cnt["fbS_max"], fbS)


def main(a):
    import core_probe as CP, dual_probe as D
    cnt = Counter(); nst = int(os.environ.get("RANDSTARTS", "1"))
    def do(g, name, extra=None):
        r = random.Random(name)
        starts = ([extra] if extra else []) + [RE.best_reward_start(g)] + [D.rand_start(g, r) for _ in range(nst)]
        for s0 in starts:
            try: analyse(cnt, g, s0, name)
            except RuntimeError: cnt["maxit"] += 1
    if a[0] == "rand":
        N, lo, hi, seed = map(int, a[1:5]); r2 = random.Random(seed)
        for i in range(N):
            nn = r2.randint(lo, hi)
            do(D.rand_ck(r2, nn, r2.randint(0, min(5, nn - 1))), "rand%d" % i)
    else:
        for path in a:
            if path.endswith(".start"): continue
            try: g = RE.parse(path)
            except Exception: cnt["parse_err"] += 1; continue
            if g.n > int(os.environ.get("MAXN", "40")): cnt["skip_big"] += 1; continue
            sp = path[:-3] + ".start"; ex = None
            if os.path.exists(sp):
                try: ex = CP.parse_start(g, sp)
                except Exception: cnt["start_err"] += 1
            cnt["GAMES"] += 1; do(g, os.path.relpath(path), ex)
    for k in sorted(cnt): print(k, cnt[k])
    print("VIOLATIONS", sum(v for k, v in cnt.items() if k.endswith("_V")))
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
