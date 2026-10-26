#!/usr/bin/env python3
"""REFEREE succ. 12 probe for packet P-N5-H3 (docs/si/P-N5-H3-box16.md, pin d096e404, sha1 680e4528...). Own engine (rl_engine via
dual_probe.run5). Any game. W_k := (sigma_k, tau_k) play values; D_k := {Odd u : sigma-bar_k(u) != tau_k(u)}; u(v) := first D-vertex on v's
(sigma_k, tau_k)-play (v included); pi_v := that path, u(v) excluded. lev / COARSE_L on (c, mask, len) values.
 BP     G_D-NC (b'): at states with (NC) (no u in D on its own honest cycle nor on its own W-cycle): Xi(v) = pi_v (+) Xi(u), W(v) = pi_v (+) W(u)
 TCC    TC-CLASS: lambda_Xi(v) = lambda_Xi(u(v)), lambda_W(v) = lambda_W(u(v)) for v in R_D; terminal changes stay inside one honest class
 C2H3   C2-H3: at (h3_D) states, COARSE_L(Xi(v)) = COARSE_L(W(v)) for all v, L = max(M_D, -1)
 WMG    WM-G: W_{k+1} >= W_k at in-phase non-fallback transitions
 FRZ    FRZ-U_H3: on maximal fallback-free in-phase runs with (h3_D) at every state, with L = max(max_S M_D, -1): COARSE_L(W) constant from
        state k0 + n - 1 on (counts FRZ_nonvacuous runs reaching that length)
 MUT    env H3_MUT=1: C2-H3 checked at L = M_D - 1 (must bite where M_D >= 0)
Usage: h3_probe.py lib | rand N nmin nmax kmin kmax seed | list file | files...  (a file X.pg with X.start also runs from that start pair)   (env RANDSTARTS=N, MAXN=64; starts seeded by relative path / fixed seed)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, rho_probe as RP, dual_probe as D
EX = []
MUT = os.environ.get("H3_MUT", "") == "1"


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def lev(x, y):
    if x == y: return -2                     # bottom
    if x[0] != y[0]: return 10 ** 6          # infinity
    d = x[1] ^ y[1]
    return d.bit_length() - 1 if d else -1


def coarse(x, L):
    return (x[0], x[1] & ~((1 << (L + 1)) - 1)) if L >= 0 else (x[0], x[1])


def prefix(g, path, x):
    for u in reversed(path): x = g.ext(u, x)
    return x


def state_info(g, a):
    n = g.n
    Xi, sb = RE.evaluate(g, a["s"])
    nxw = [a["s"][v] if g.owner[v] == 0 else a["t"][v] for v in range(n)]
    nxh = [a["s"][v] if g.owner[v] == 0 else sb[v] for v in range(n)]
    W = [RE.play_value(g, nxw, v) for v in range(n)]
    Dk = {u for u in range(n) if g.owner[u] == 1 and sb[u] != a["t"][u]}
    uv, pi = {}, {}
    for v in range(n):
        x, path, seen = v, [], set()
        while x not in seen:
            if x in Dk: uv[v] = x; pi[v] = path; break
            seen.add(x); path.append(x); x = nxw[x]
    def on_own_cycle(nx, u):
        x, seen = nx[u], set()
        while x not in seen:
            if x == u: return True
            seen.add(x); x = nx[x]
        return False
    NC = all(not on_own_cycle(nxh, u) and not on_own_cycle(nxw, u) for u in Dk)
    h3 = all(Xi[u][0] == W[u][0] for u in Dk)
    MD = max((lev(Xi[u], W[u]) for u in Dk), default=-2)
    return dict(Xi=Xi, W=W, D=Dk, uv=uv, pi=pi, NC=NC, h3=h3, MD=MD)


def run_check(g, start, cnt, name):
    A = D.run5(g, start); n = g.n
    st = [state_info(g, a) for a in A]
    for k, s in enumerate(st):
        cnt["states"] += 1; cnt["states_h3"] += s["h3"]; cnt["states_h3_notNC"] += s["h3"] and not s["NC"]
        for v, u in s["uv"].items():
            cnt["TCC_chk"] += 1
            if s["Xi"][v][0] != s["Xi"][u][0] or s["W"][v][0] != s["W"][u][0]: fail(cnt, "TCC", name, k, v)
            if s["NC"]:
                cnt["BP_chk"] += 1
                if s["Xi"][v] != prefix(g, s["pi"][v], s["Xi"][u]) or s["W"][v] != prefix(g, s["pi"][v], s["W"][u]): fail(cnt, "BP", name, k, v)
        if s["h3"]:
            L = max(s["MD"], -1) - (1 if MUT else 0)
            if MUT and s["MD"] < 0: continue
            for v in range(n):
                cnt["C2H3_chk"] += 1
                if coarse(s["Xi"][v], L) != coarse(s["W"][v], L): fail(cnt, "C2H3", name, k, v, L)
    T_ = len(A) - 1
    key = [(tuple(x[0] for x in st[k]["Xi"]), tuple(A[k]["t"])) for k in range(T_ + 1)]
    k = 0
    while k <= T_:
        j = k
        while j < T_ and key[j] == key[j + 1]: j += 1
        p0, p1 = k, j; k = j + 1
        cnt["phases"] += 1
        for s in range(p0, p1):
            # terminal changes stay in one honest class
            for v in st[s]["uv"]:
                if v in st[s + 1]["uv"] and st[s]["uv"][v] != st[s + 1]["uv"][v]:
                    cnt["TC_changes"] += 1
                    if st[s]["Xi"][st[s]["uv"][v]][0] != st[s + 1]["Xi"][st[s + 1]["uv"][v]][0]: fail(cnt, "TCC_class", name, s, v)
            if A[s]["fb"]: continue
            for v in range(n):
                cnt["WMG_chk"] += 1
                if g.key(st[s + 1]["W"][v]) < g.key(st[s]["W"][v]): fail(cnt, "WMG", name, s, v)
        # maximal fallback-free runs with (h3_D) at every state
        runs, cur = [], []
        for s in range(p0, p1 + 1):
            ok = st[s]["h3"] and (not cur or not A[s - 1]["fb"])
            if ok: cur.append(s)
            else:
                if cur: runs.append(cur)
                cur = [s] if st[s]["h3"] else []
        if cur: runs.append(cur)
        for R in runs:
            cnt["FRZ_runs"] += 1
            cnt["max_run_transitions"] = max(cnt["max_run_transitions"], len(R) - 1)
            L = max(max(st[s]["MD"] for s in R), -1)
            cw = lambda s: [coarse(st[s]["W"][v], L) for v in range(n)]
            if len(R) >= n and n >= 2:
                # the stronger (1-based) reading: no coarse change at the transition into state k0 + n - 1 (R[n-1] from R[n-2])
                cnt["FRZ1B_chk"] += 1
                if cw(R[n - 2]) != cw(R[n - 1]): cnt["FRZ1B_violated"] += 1; EX.append(("FRZ1B", name, R[0], len(R), n))
            if len(R) < n + 1: continue          # the proof's reading: freeze from state k0 + n - 1; content needs >= n + 1 states
            cnt["FRZ_nonvacuous"] += 1
            base = cw(R[n - 1])
            for s in R[n - 1:]:
                if cw(s) != base: fail(cnt, "FRZ", name, s)


def main(a):
    nr = int(os.environ.get("RANDSTARTS", "0")); cnt = Counter(); maxn = int(os.environ.get("MAXN", "64"))
    if a and a[0] == "rand":
        N, lo, hi, kl, kh, seed = map(int, a[1:7]); rng = random.Random(seed)
        gs = [("rand%d_%d" % (seed, i), D.rand_ck(rng, rng.randint(lo, hi), rng.randint(kl, kh))) for i in range(N)]
    elif a and a[0] == "list":
        gs = [(l.split()[0], RE.parse(os.path.join(P.ROOT, l.split()[0]))) for l in open(a[1]) if l.strip()]
    else:
        gs = [(os.path.relpath(f, P.ROOT), RE.parse(f)) for f in (RP.lib() if a == ["lib"] else a)]
    for name, g in gs:
        if g.n > maxn: cnt["skip_big"] += 1; continue
        cnt["games"] += 1
        starts = [RE.best_reward_start(g)] + [D.rand_start(g, random.Random(name + str(i))) for i in range(nr)]
        sf = os.path.join(P.ROOT, name[:-3] + ".start") if name.endswith(".pg") else ""
        if sf and os.path.exists(sf):  # a given start pair (SIGMA0 / TAU0 lines, v:w)
            s0, t0 = [None] * g.n, [None] * g.n
            for l in open(sf):
                p_ = l.split()
                if p_ and p_[0] in ("SIGMA0", "TAU0"):
                    for vw in p_[1:]:
                        v, w = map(int, vw.split(":")); (s0 if p_[0] == "SIGMA0" else t0)[v] = w
            b0 = RE.best_reward_start(g)  # vertices the .start file omits keep the S3 choice
            s0 = [b0[0][v] if (g.owner[v] == 0 and s0[v] is None) else s0[v] for v in range(g.n)]
            t0 = [b0[1][v] if (g.owner[v] == 1 and t0[v] is None) else t0[v] for v in range(g.n)]
            starts.append((s0, t0)); cnt["given_starts"] += 1
        for i, stt in enumerate(starts):
            try: run_check(g, stt, cnt, name + ("@r%d" % i if i else ""))
            except RuntimeError: cnt["maxit"] += 1
    for k in sorted(cnt): print("%-26s %d" % (k, cnt[k]))
    print("FAILS", sum(v for k, v in cnt.items() if k.endswith("_FAIL")))
    for e in EX[:40]: print("EX (", e)


if __name__ == "__main__":
    main(sys.argv[1:])
