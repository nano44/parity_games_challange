#!/usr/bin/env python3
r"""REFEREE-2 successor 20 (Opus 5.5, D15): own check of P-N5-GP (docs/si/P-N5-GP-box31.md, sha1 cd4866df @ l-si d072bb28).
State loop: my lane's R2-N5-DUAL/dual_check.Runner (SPEC N5 on si.py, read-only). Xi_t, sbar_t, I_sigma_t from si.py's engine; W_t := my own
play value of the (sigma_t, tau_t)-plays (R2-N5-RUND play_value). The lane's core/gp.py is NOT imported (run only as the pinned re-run).
Phase = maximal run with (lambda_Xi, tau) constant; frozen W-phase F = [a, b] = maximal run inside a phase whose transitions are no S4c
fallback, change no lambda_W and no sbar (§1 [FRZ]).
Checks (each must be 0):
  WMON   every in-phase non-fallback transition: W_{t+1} >= W_t pointwise, and W_{t+1} >= the W-value of RANDH random strategies of H_t
  XW     Xi_t <= W_t everywhere; Xi_t = W_t where the W-play meets no vertex of D_t
  GPS    Lemma GP*: every k in F, every x, every path r of G_tau unblocked at state k (simple; ends at a W cycle node; L <= k - a; Even edge i
         not blocked at state k-1-i), at most PCAP per (k, x), DFS in index order: W_k(x) >= value(r). NODECAP (0 = none) bounds the DFS
         nodes per (k, x); truncations are counted (GPS_dfs_truncated)
  F1H    every k -> k+1 in F, every (x, z) in I_sigma_k: W_{k+1}(x) >= val_rhohat(x), rhohat = rho_k[x -> z] (F1 in H_k, Case B's first line)
  IMP    the Case B sub-cases the proof calls impossible inside F never occur: B1'(ii) (x not in pi, x on c's cycle, top of P(pi) even) and
         B2b (i) (top of D' even) / (iii) with c odd. Counted per sub-case: B1, B1'(i), B1'(iii), B2a, B2b(ii), B2b(iii) c even.
  NOTBL  GP / GP+ core: no edge to z in ALLOWED+(x, t) (rho_t(x), I_sigma_t, U_t, same basin of a same-pair tail-disjoint gate) is blocked
  FWR    Corollary FW-R*: WCH <= (n - 1)(R*_T + 1) per frozen W-phase
Controls (counted, expected to bite somewhere): X_GPall = GP* with the blocked restriction dropped (plain W-frame Lemma P) fails;
X_FW0 = WCH > n - 1 (the R*_T term is used); X_BLK = blocked edges exist.
Usage: gp_check.py random N nmin nmax seed [starts] | files list.txt [runs [prefix]]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-DUAL"))
import dual_check as DC
pg, Engine, dual = DC.pg, DC.Engine, DC.dual
PCAP = int(os.environ.get("PCAP", "300")); NODECAP = int(os.environ.get("NODECAP", "0")); RANDH = int(os.environ.get("RANDH", "3")); MAXF = int(os.environ.get("MAXF", "400"))


class St:
    def __init__(s): s.c, s.mx = {}, {}
    def inc(s, k, d=1): s.c[k] = s.c.get(k, 0) + d
    def mxu(s, k, v):
        if v > s.mx.get(k, -1): s.mx[k] = v
    def bad(s, k, msg):
        s.inc(k)
        if s.c[k] <= 5: print("VIOLATION", k, msg, flush=True)


def play(nx, v):
    seen, path, x = {}, [], v
    while x not in seen: seen[x] = len(path); path.append(x); x = nx[x]
    return path, seen[x]


def pval(E, nx, v):
    path, j = play(nx, v)
    c = max(path[j:], key=lambda y: E.pp[y]); i = path.index(c); m = 0
    for y in path[:i]:
        if E.rank[y] > E.rank[c]: m |= E.bit[y]
    return (c, m, i)


def run_game(g, s, t, st, name, rng):
    n = g.n; E = Engine(g); K = E.key
    states, fbs = DC.Runner(g).run(list(s), list(t))
    T = len(states) - 1; st.inc("runs"); st.inc("transitions", T)
    info = []
    for sg, tu in states:
        xe, sb = E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
        xi = [tuple(z) for z in xe]; Is = set(E.improving(tuple(sg), xe))
        nxW = [sg[v] if g.owner[v] == 0 else tu[v] for v in range(n)]
        W = [pval(E, nxW, v) for v in range(n)]
        sbar = tuple(sb[v] if g.owner[v] == 1 else -1 for v in range(n))
        D = frozenset(u for u in range(n) if g.owner[u] == 1 and sb[u] != tu[u])
        nxX = [sg[v] if g.owner[v] == 0 else sb[v] for v in range(n)]
        info.append(dict(sg=sg, tu=tu, xi=xi, Is=Is, W=W, nxW=nxW, nxX=nxX, sbar=sbar, D=D,
                         lam=tuple(z[0] for z in xi), lamW=tuple(z[0] for z in W)))
    for I in info:   # XW
        for v in range(n):
            st.inc("XW_checks")
            if K(I["xi"][v]) > K(I["W"][v]): st.bad("XW", f"{name} v={v}")
            if not (set(play(I["nxW"], v)[0]) & I["D"]) and I["xi"][v] != I["W"][v]: st.bad("XW", f"{name} v={v} (D-free play)")
    # phases and frozen W-phases
    k0 = 0; nF = 0
    while k0 <= T:
        k1 = k0
        while k1 + 1 <= T and (info[k1 + 1]["lam"], info[k1 + 1]["tu"]) == (info[k0]["lam"], info[k0]["tu"]): k1 += 1
        for t in range(k0, k1):   # WMON
            if fbs[t]: continue
            st.inc("WMON_checks"); A, B = info[t], info[t + 1]
            if any(K(B["W"][v]) < K(A["W"][v]) for v in range(n)): st.bad("WMON", f"{name}@{t}")
            arena = {v: [A["sg"][v]] + [w for x, w in A["Is"] if x == v] for v in range(n) if g.owner[v] == 0}
            for _ in range(RANDH):
                nx = list(A["nxW"])
                for v in arena: nx[v] = rng.choice(arena[v])
                if any(K(B["W"][v]) < K(pval(E, nx, v)) for v in range(n)): st.bad("WMON", f"{name}@{t}: H_t strategy beats rho_t+1")
        a = k0
        for t in range(k0, k1 + 1):
            if t == k1 or fbs[t] or info[t + 1]["lamW"] != info[t]["lamW"] or info[t + 1]["sbar"] != info[t]["sbar"]:
                if nF < MAXF: frozen(g, E, info, fbs, a, t, st, name)
                nF += 1; a = t + 1
        k0 = k1 + 1
    st.inc("frozen_phases", nF)


def blocked_at(g, E, I):
    K = E.key; out = set()
    for x in range(g.n):
        if g.owner[x] != 0: continue
        rx = I["sg"][x]
        for z in set(g.succ[x]):
            if z != rx and (x, z) not in I["Is"] and K(I["W"][z]) > K(I["W"][rx]): out.add((x, z))
    return out


def frozen(g, E, info, fbs, a, b, st, name):
    n = g.n; K = E.key; st.inc("F_checked"); st.mxu("maxF", b - a)
    BL = {t: blocked_at(g, E, info[t]) for t in range(a, b)}
    if any(BL.values()): st.inc("X_BLK")
    lamW = info[a]["lamW"]; tu = info[a]["tu"]
    # GP*: path enumeration (and the MUT=all control)
    for k in range(a, b + 1):
        Wk = info[k]["W"]
        for x in range(n):
            cnt = [0]; worst = [None]; nodes = [0]
            def dfs(y, path, vis, mut):
                if cnt[0] >= PCAP: return
                nodes[0] += 1
                if NODECAP and nodes[0] > NODECAP:
                    if nodes[0] == NODECAP + 1: st.inc("GPS_dfs_truncated")
                    return
                L = len(path) - 1
                if lamW[y] == y:
                    cnt[0] += 1
                    u = y; m = 0
                    for r in path[:-1]:
                        if E.rank[r] > E.rank[u]: m |= E.bit[r]
                    if K(Wk[x]) < K((u, m, L)):
                        if mut: st.inc("X_GPall")
                        else: st.bad("GPS", f"{name} F[{a},{b}] k={k} x={x} path={path}")
                if L >= k - a: return
                nxt = [tu[y]] if g.owner[y] == 1 else sorted(set(g.succ[y]))
                for z in nxt:
                    if z in vis: continue
                    if g.owner[y] == 0 and not mut and (y, z) in BL[k - 1 - L]: continue
                    vis.add(z); path.append(z); dfs(z, path, vis, mut); path.pop(); vis.discard(z)
            dfs(x, [x], {x}, False); st.inc("GPS_paths", cnt[0])
            if BL and any(BL.values()):
                cnt[0] = 0; nodes[0] = 0; dfs(x, [x], {x}, True)
    # F1H and the Case B sub-case census, per transition k -> k+1 in F
    for k in range(a, b):
        A, B = info[k], info[k + 1]
        for x, z in A["Is"]:
            nx = list(A["nxW"]); nx[x] = z; vh = pval(E, nx, x)
            st.inc("F1H_checks")
            if K(B["W"][x]) < K(vh): st.bad("F1H", f"{name}@{k} x={x} z={z}")
            c = lamW[z]; pi = [z]
            while pi[-1] != c: pi.append(A["nxW"][pi[-1]])
            cyc, j = play(A["nxW"], c); cycle = set(cyc[j:])
            hi = [y for y in pi[:-1] if E.rank[y] > E.rank[c]]
            if x not in pi:
                if x not in cycle: st.inc("B1")
                elif not hi: st.inc("B1p_i")
                else:
                    top = max(hi, key=lambda y: E.rank[y])
                    if g.prio[top] % 2 == 0: st.bad("IMP", f"{name}@{k} B1'(ii) x={x} z={z}")
                    else: st.inc("B1p_iii")
            elif x == c: st.inc("B2a")
            else:
                Dp = [y for y in pi[:pi.index(x)] if E.rank[y] > E.rank[c]] + ([x] if E.rank[x] > E.rank[c] else [])
                if Dp:
                    top = max(Dp, key=lambda y: E.rank[y])
                    if g.prio[top] % 2 == 0: st.bad("IMP", f"{name}@{k} B2b(i) x={x} z={z}")
                    else: st.inc("B2b_ii")
                elif g.prio[c] % 2 == 1: st.bad("IMP", f"{name}@{k} B2b(iii) c odd x={x} z={z}")
                else: st.inc("B2b_iii_even")
    # NOTBL (GP / GP+)
    for t in range(a, b):
        I = info[t]; D = I["D"]
        meetW = {v: play(I["nxW"], v)[0] for v in range(n)}
        U = {v for v in range(n) if not (set(meetW[v]) & D)}
        first = {}
        for v in range(n):
            for y in meetW[v]:
                if y in D: first[v] = y; break
        Sd = {}
        for v, d in first.items(): Sd.setdefault(d, set()).add(v)
        good = set()
        for d, S in Sd.items():
            if info[a]["lam"][d] != lamW[d]: continue
            pw = meetW[d][1:]; px = play(I["nxX"], d)[0][1:]
            if not (set(pw) & S) and not (set(px) & S): good.add(d)
        for x in range(n):
            if g.owner[x] != 0: continue
            allowed = {I["sg"][x]} | {w for y, w in I["Is"] if y == x} | {z for z in g.succ[x] if z in U}
            if x in first and first[x] in good: allowed |= {z for z in g.succ[x] if first.get(z) == first[x]}
            for z in allowed:
                st.inc("NOTBL_checks")
                if (x, z) in BL[t]: st.bad("NOTBL", f"{name}@{t} x={x} z={z}")
    # FW-R*
    WCH = sum(info[t + 1]["W"] != info[t]["W"] for t in range(a, b))
    everbl = set(); RT = 0
    for t in range(a, b):
        ad = [(y, info[t + 1]["sg"][y]) for y in range(n) if g.owner[y] == 0 and info[t + 1]["sg"][y] != info[t]["sg"][y]]
        if any(e in everbl for e in ad): RT += 1
        everbl |= BL[t]
    st.inc("FWR_checks"); st.mxu("maxRT", RT); st.mxu("maxWCH", WCH)
    if RT == 0: st.inc("F_RT0")
    if WCH > (n - 1) * (RT + 1): st.bad("FWR", f"{name} F[{a},{b}] WCH {WCH} RT {RT} n {n}")
    if WCH > n - 1: st.inc("X_FW0")


def main():
    st = St(); a = sys.argv[1:]; rng = random.Random(3131)
    if a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); ns = int(a[5]) if len(a) > 5 else 2; rng = random.Random(seed)
        for i in range(N):
            g = DC.rand_game(rng, rng.randint(nmin, nmax), "kO")
            for r in range(ns + 1):
                if r == 0: s, t = Engine(g).initial("best"), Engine(dual(g)).initial("best")
                else: s, t = [rng.choice(g.succ[v]) for v in range(g.n)], [rng.choice(g.succ[v]) for v in range(g.n)]
                run_game(g, s, t, st, f"rand{seed}:{i}#{r}", rng)
    elif a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 2; pre = a[3] if len(a) > 3 else ""
        for line in [l.split() for l in open(a[1]) if l.strip()]:
            g = pg.read(os.path.join(DC.ROOT, pre + line[0]))
            if len(line) > 1:   # start files: unlisted vertices from S3 (the lanes' convention); validated
                s, t = list(Engine(g).initial("best")), list(Engine(dual(g)).initial("best"))
                for l2 in open(os.path.join(DC.ROOT, pre + line[1])):
                    ps = l2.split()
                    if ps and ps[0] in ("SIGMA0", "TAU0"):
                        for kv in ps[1:]:
                            v, w = map(int, kv.split(":")); (s if ps[0] == "SIGMA0" else t)[v] = w
                if all((s if g.owner[v] == 0 else t)[v] in g.succ[v] for v in range(g.n)):
                    st.inc("starts_valid"); run_game(g, s, t, st, f"{line[0]}#start", rng)
                else: st.inc("starts_INVALID_skipped")
            for r in range(runs):
                if r == 0: s, t = Engine(g).initial("best"), Engine(dual(g)).initial("best")
                else: s, t = [rng.choice(g.succ[v]) for v in range(g.n)], [rng.choice(g.succ[v]) for v in range(g.n)]
                run_game(g, list(s), list(t), st, f"{line[0]}#{r}", rng)
            if os.environ.get("PROGRESS"): print("DONE-FILE", line[0], flush=True)
    print("MODE", " ".join(a), "PCAP", PCAP, "RANDH", RANDH, "MAXF", MAXF)
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"max {k}: {st.mx[k]}")
    bad = sum(st.c.get(k, 0) for k in ("WMON", "XW", "GPS", "F1H", "IMP", "NOTBL", "FWR"))
    print("RESULT", "PASS" if bad == 0 else "FAIL", "violations", bad)


if __name__ == "__main__":
    main()
