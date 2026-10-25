#!/usr/bin/env python3
"""REFEREE succ. 11 probe for the K note (docs/si/N5-KW-box15.md, sha1 5ebbb3b6...; packet P-N5-KW when pinned).
Own engine (rl_engine, rl_probe.states; no lane code). C^1O asserted per game. R := rl_probe's Rb (o included).
Phase = maximal run with (lambda_Xi, tau) constant; stretch = maximal run of a phase with R, theta = Xi(o), w = W(o) constant;
run = maximal run of consecutive non-fallback transitions inside a stretch (states k0..kT). m* = more relevant of c_theta, c_w
(c_theta if equal); kappa(rho) = rho above m* (rank). pi_v = route of v before o.
 WONCE   x, x+1 non-fallback in one phase, Xi_{x+1} = Xi_x  =>  W_{x+2} = W_{x+1}
 FA      Fact A (A-Xi), (A-W): cycle nodes c_theta / c_w on R; path sets above m* = kappa(pi_v) + C (C per H1 / H2)
 FB      Fact B: kappa(pi_y) != kappa(pi_z) => Xi order = W order = kappa order (strict)
 MON     kappa_k(x) <= kappa_{k+1}(x) along every run (kappa-order)
 FRZ     kappa_t(v) = kappa_{k0+r-1}(v) for t >= k0 + r - 1 in a run; FRZD = largest actual freeze delay seen
 LEN     post-freeze: m* frame's path set constant on R; per-vertex changes of that frame <= r - 2; per run <= (r-1)^2
 KIND    c_w > c_theta, not H2, c_w != o: post-freeze kind changes <= 1 per vertex, direction B->A iff Omega(c_w) even
 CWINT   on windows of a run with no kind change and no kind-B switch: c_w switches <= deg(c_w) - 1 (any run, not only post-freeze)
 CASCB   W-flat segment, kind-stable sub-run: a kind-B Even v switches only at sub-run steps <= |pi_v| - 2
 RUN     per run: Xi-changing transitions on R <= the note's case bound (E-SEG computed from the run's own e, N_B, E_cw)
 corner counters: selfloop_o, o_eq_ct, r2, cw_eq_ct (runs and post-freeze states touched)
Usage: kw_probe.py lib | rand N nmin nmax seed | files...   (env RANDSTARTS=N)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, rho_probe as RP
EX = []


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def kle(g, A, B):
    """A <= B in the kappa-order (sets of vertices)"""
    if A == B: return True
    t = max(A ^ B, key=lambda u: g.rank[u])
    ev = g.prio[t] % 2 == 0
    return (t in B) == ev


def mask(g, S):
    m = 0
    for u in S: m |= 1 << g.rank[u]
    return m


def above(g, m, rk):
    return m & ~((1 << (rk + 1)) - 1)


def run_game(g, cnt, name):
    o, st = P.states(g); n = g.n; T = len(st) - 1
    sl = o in g.succ[o]
    phases, k = [], 0
    while k <= T:
        j = k
        while j < T and st[j]["key"] == st[j + 1]["key"]: j += 1
        phases.append((k, j)); k = j + 1
    for (p0, p1) in phases:
        # WONCE
        for x in range(p0, p1 - 1):
            if st[x]["fb"] or st[x + 1]["fb"]: continue
            if st[x]["Xi"] == st[x + 1]["Xi"]:
                cnt["WONCE_chk"] += 1
                if st[x + 1]["W"] != st[x + 2]["W"]: fail(cnt, "WONCE", name, x)
        # stretches
        sts, t = [], p0
        while t <= p1:
            u = t
            while u < p1 and st[u + 1]["Rb"] == st[t]["Rb"] and st[u + 1]["Xi"][o] == st[t]["Xi"][o] and st[u + 1]["W"][o] == st[t]["W"][o]:
                u += 1
            sts.append((t, u)); t = u + 1
        for (s0, s1) in sts:
            R = st[s0]["Rb"]; r = len(R); H1, H2 = st[s0]["H1"], st[s0]["H2"]
            th, w = st[s0]["Xi"][o], st[s0]["W"][o]; ct, cw = th[0], w[0]
            ms = ct if g.rank[ct] >= g.rank[cw] else cw; rk = g.rank[ms]
            CX = above(g, th[1], rk) if H1 else 0
            CW = above(g, w[1], rk) if H2 else 0
            routes = {x: {v: P.route(st[x]["nx"], v, o) for v in R} for x in range(s0, s1 + 1)}
            kap = {x: {v: frozenset(u for u in routes[x][v] if g.rank[u] > rk) for v in R} for x in range(s0, s1 + 1)}
            for x in range(s0, s1 + 1):
                a = st[x]
                for v in R:
                    km = mask(g, kap[x][v])
                    if a["Xi"][v][0] != ct or above(g, a["Xi"][v][1], rk) != km | CX: fail(cnt, "FA_Xi", name, x, v)
                    if a["W"][v][0] != cw or above(g, a["W"][v][1], rk) != km | CW: fail(cnt, "FA_W", name, x, v)
                    cnt["FA_chk"] += 1
                Rl = sorted(R)
                for i, y in enumerate(Rl):
                    for z in Rl[i + 1:]:
                        if kap[x][y] == kap[x][z]: continue
                        cnt["FB_chk"] += 1
                        kz = kle(g, kap[x][y], kap[x][z])
                        xo = g.key(a["Xi"][y]) < g.key(a["Xi"][z]); wo = g.key(a["W"][y]) < g.key(a["W"][z])
                        if not (kz == xo == wo): fail(cnt, "FB", name, x, y, z)
            # runs
            runs, x = [], s0
            while x < s1:
                if st[x]["fb"]: x += 1; continue
                y = x
                while y < s1 and not st[y]["fb"]: y += 1
                runs.append((x, y)); x = y
            for (k0, kT) in runs:
                cnt["runs"] += 1
                tags = []
                if sl: tags.append("selfloop_o")
                if ct == o: tags.append("o_eq_ct")
                if r == 2: tags.append("r2")
                if cw == ct: tags.append("cw_eq_ct")
                f0 = k0 + r - 1
                for tg in tags:
                    cnt["corner_runs_" + tg] += 1
                    if kT > f0: cnt["corner_postfrz_runs_" + tg] += 1
                for x in range(k0, kT):
                    for v in R:
                        cnt["MON_chk"] += 1
                        if not kle(g, kap[x][v], kap[x + 1][v]): fail(cnt, "MON", name, x, v)
                # actual freeze delay
                last = k0
                for x in range(k0, kT):
                    if kap[x] != kap[x + 1]: last = x + 1
                if last - k0 > cnt["FRZD_max"]: EX.append(("FRZD", name, k0, last - k0, r, kT - k0))
                cnt["FRZD_max"] = max(cnt["FRZD_max"], last - k0)
                cnt["FRZD_hist_%02d" % min(last - k0, 99)] += 1
                if last > max(k0, f0): fail(cnt, "FRZ", name, k0, last, r)
                cnt["FRZ_chk"] += max(0, kT - f0)
                post = range(max(k0, f0), kT)
                # LEN
                fr = "Xi" if ms == ct else "W"
                if kT > f0:
                    for v in R:
                        if len({st[x][fr][v][1] for x in range(f0, kT + 1)}) > 1: fail(cnt, "LEN_P", name, k0, v)
                        ch = sum(st[x][fr][v] != st[x + 1][fr][v] for x in post)
                        if v in (o, ms) and ch: fail(cnt, "LEN_fix", name, k0, v)
                        if ch > max(0, r - 2): fail(cnt, "LEN_v", name, k0, v, ch)
                tot = sum(any(st[x][fr][v] != st[x + 1][fr][v] for v in R) for x in range(k0, kT))
                if tot > (r - 1) ** 2: fail(cnt, "LEN_run", name, k0, tot)
                # U3 / U23 machinery
                u3 = ms == cw and cw != ct and (not H2) and cw != o
                kind = {x: {v: (cw in routes[x][v]) for v in R if v != o} for x in range(k0, kT + 1)}
                sw = lambda x, v: g.owner[v] == 0 and st[x]["s"][v] != st[x + 1]["s"][v]
                eQ = NB = Ecw = 0
                if u3:
                    cnt["u3_runs"] += 1
                    for v in R - {o}:
                        seq = [kind[x][v] for x in range(max(k0, f0), kT + 1)]
                        chg = sum(seq[i] != seq[i + 1] for i in range(len(seq) - 1))
                        if chg:
                            cnt["KIND_postfrz_changes"] += chg
                            if chg > 1: fail(cnt, "KIND_once", name, k0, v)
                            to_a = seq[-1]
                            if to_a != (g.prio[cw] % 2 == 0): fail(cnt, "KIND_dir", name, k0, v)
                    # CWINT windows (whole run)
                    cut = [any(kind[x][v] != kind[x + 1][v] for v in R - {o}) or
                           any(sw(x, v) and not kind[x][v] for v in R - {o} if v != cw) for x in range(k0, kT)]
                    cs = 0
                    for i, x in enumerate(range(k0, kT)):
                        if cut[i]: cs = 0; continue
                        if sw(x, cw):
                            cs += 1; cnt["CWINT_switches"] += 1
                            if cs > len(g.succ[cw]) - 1: fail(cnt, "CWINT", name, x)
                    # W-flat segments, kind-stable sub-runs, CASC-B (whole run, as the lemma has no freeze hypothesis)
                    x = k0
                    while x < kT:
                        y = x
                        while y < kT and all(st[y]["W"][v] == st[y + 1]["W"][v] for v in R): y += 1
                        # [x, y) are W-flat transitions
                        z = x
                        while z < y:
                            e = z
                            while e < y and not any(kind[e][v] != kind[e + 1][v] for v in R - {o}): e += 1
                            for j, xx in enumerate(range(z, e)):
                                for v in R - {o, cw}:
                                    if sw(xx, v) and not kind[xx][v]:
                                        cnt["CASCB_switches"] += 1
                                        if j > len(routes[xx][v]) - 2: fail(cnt, "CASCB", name, xx, v, j)
                            z = e + 1 if e < y else y
                        x = y + 1 if y < kT else kT
                    for xx in post:
                        if any(kind[xx][v] != kind[xx + 1][v] for v in R - {o}): eQ += 1
                        elif any(sw(xx, v) and not kind[xx][v] for v in R - {o, cw}): NB += 1
                        if sw(xx, cw): Ecw += 1
                NX = sum(any(st[x]["Xi"][v] != st[x + 1]["Xi"][v] for v in R) for x in range(k0, kT))
                Dl = max(len(g.succ[v]) for v in range(n))
                if ms == ct: B = (r - 1) ** 2
                elif not u3: B = (r - 1) ** 2 + ((r - 1) * (r - 2) + 1) * (r - 2)
                else:
                    segs = (r - 1) * (r - 2) + 1
                    E = eQ + Ecw  # E-SEG: sum over segments of E(Q) + (E(Q) + 1)(2r - 4), events from the run's own counts
                    B = (r - 1) ** 2 + E + (E + segs) * (2 * r - 4)
                B = max(B, 0)
                cnt["RUN_chk"] += 1
                cnt["RUN_maxNX"] = max(cnt["RUN_maxNX"], NX)
                if NX > B: fail(cnt, "RUN", name, k0, NX, B)


def main(a):
    if a and a[0] == "rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        gs = [("rand%d" % i, P.rand_c1o(rng, rng.randint(lo, hi))) for i in range(N)]
    else:
        files = RP.lib() if a == ["lib"] else a
        gs = [(os.path.relpath(f, P.ROOT), RE.parse(f)) for f in files]
    cnt = Counter()
    for name, g in gs:
        try: P.assert_c1o(g)
        except AssertionError: cnt["skip_not_c1o"] += 1; continue
        cnt["games"] += 1
        try: run_game(g, cnt, name)
        except RuntimeError: cnt["maxit"] += 1
        nr = int(os.environ.get("RANDSTARTS", "0"))
        if nr:
            rng = random.Random(name); orig = RE.best_reward_start
            for _ in range(nr):
                s0 = [rng.choice(g.succ[v]) if g.owner[v] == 0 else None for v in range(g.n)]
                t0 = [rng.choice(g.succ[v]) if g.owner[v] == 1 else None for v in range(g.n)]
                RE.best_reward_start = lambda h, s0=s0, t0=t0: (s0, t0)
                cnt["runs_randstart"] += 1
                try: run_game(g, cnt, name + "@rand")
                except RuntimeError: cnt["maxit"] += 1
            RE.best_reward_start = orig
    for k in sorted(cnt): print("%-34s %d" % (k, cnt[k]))
    print("FAILS", sum(v for k, v in cnt.items() if k.endswith("_FAIL")))
    for e in EX[:40]: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
