#!/usr/bin/env python3
"""REFEREE succ. 14 probe for packet P-N5-HON (docs/new/P-N5-HON-box46.md, pin 31835c4b, sha1 07f8e767...). Own engine only (rl_engine =
SPEC S1-S5 from the text; epr_probe's gates / s4a / s4b_arena / wval / n5tau_step, written by REFEREE succ. 12). No lane code.
Per phase P ((lambda_Xi, tau) constant) of every N5 run; W_k := sigma_k's valuation in G_tau; W-honest := Xi_k = W_k; f := in-phase fallbacks;
f_in := in-phase fallbacks at non-honest states strictly between two honest states of P; D_k := {q in Q : sigma-bar_k(q) != tau(q)}.
 HON    #honest <= f + 4n^2 - 3n          HONP   #honest <= f_in + 4n^2 - 3n        H0     #D={} states, N_0, transitions out of D={} epochs <= f_in + 4n^2 - 3n
 D0H    D={} state => honest
 Needs LEV (exact by simple-path enumeration in G_tau, only n <= LEVMAX, default 11):
 LMON   LEV non-decreasing along P (step 0)          LB0    LEV >= 0
 GAPW   fallback-free gap h < h' of consecutive honest states: W non-decreasing at every transition (WM) and lambda_W(h+1) = lambda (step 1)
 STEP1  ... LEV(h') >= min(LEV(h) + 1, n - 1)       SAT    honest h: Xi_h <= B; LEV = n-1 => Xi_h = B (step 2)
 CNT    s - 1 <= f_in + n - 2 (unsaturated honest), saturated honest states span <= 4n(n-1) transitions (step 3)
 SAT0   any state of P with no W-improving edge in G_tau: W >= value(r) for all simple r to W-cycle nodes; honest => LEV = n - 1
 HONFF  (count, OPEN conjecture, not signed) gaps with a fallback inside that do not rise
 HON-FB at an honest h whose transition is an in-phase fallback: FB1 every W-improving edge flat; FB2 W_{h+1} = W_h; FB3 no W-improving edge at
        sigma_{h+1}; FB4 h+1 honest, (LEV n-1 if computed) and the last state of P
 REC1   per phase: #{u}-intervals <= 1 + #(D={} sources) + X_dir + X_big (proof form) and <= 1 + (f_in + 4n^2 - 3n) + X_dir + X_big
 RU     RESTRICT_u (i)-(iv) at every state with D_k <= {u}, for every such u in Q (G^u := every Odd v != u cut to tau(v), u keeps all edges)
 REPU   REPRO_u: N5^tau on G^u from (sigma_x, tau) reproduces the len(J) transitions of every u-run J with the same fallback flags, and
        lambda' = lambda at x..y (one phase); EXITLAM counts the exit transition leaving it; MULTI counts u-runs spanning >= 2 epochs
 MUT=1  control: G^u with u ALSO cut to tau(u) (= G_tau): RU must fail at D = {u} states.   MUT=2 control: STEP1 asked across EVERY gap incl.
        fallbacks at honest h (not a claim; must fail only if a fallback gap fails to rise).
 MUT=3  control: STEP1 with a rise of 2: must fail.
Usage: hon_probe.py rand N nmin nmax kmax seed | files[:startfile]...   (env RANDSTARTS=N default 2, LEVMAX, MAXN, NORU=1 skips RU/REPU)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, dual_probe as D, epr_probe as E
EX = []
MUT = int(os.environ.get("MUT", "0"))


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def best_le(g, succ, cyc, n):
    """best[x][j] = max key-value over simple paths r from x with <= j edges ending at a vertex of cyc (value(r) as in R17 Lemma P)"""
    best = [[None] * n for _ in range(g.n)]
    for x in range(g.n):
        byL = [None] * n
        stack = [(x, (x,))]
        while stack:
            v, p = stack.pop()
            if v in cyc:
                val = (v, 0, 0)
                for w in reversed(p[:-1]): val = g.ext(w, val)
                L = len(p) - 1
                if byL[L] is None or g.key(val) > g.key(byL[L]): byL[L] = val
            if len(p) - 1 >= n - 1: continue
            for w in succ[v]:
                if w not in p: stack.append((w, p + (w,)))
        cur = None
        for j in range(n):
            if byL[j] is not None and (cur is None or g.key(byL[j]) > g.key(cur)): cur = byL[j]
            best[x][j] = cur
    return best


def level(g, V, best, n):
    lv = -1
    for j in range(n):
        if all(best[x][j] is None or g.key(V[x]) >= g.key(best[x][j]) for x in range(g.n)): lv = j
        else: break
    return lv


def gu_game(g, t, u):
    succ = [list(g.succ[v]) if g.owner[v] == 0 or (v == u and MUT != 1) else [t[v]] for v in range(g.n)]
    return RE.Game(list(g.prio), list(g.owner), succ)


def w_improving(g, W, s):
    return [(v, w) for v in range(g.n) if g.owner[v] == 0 for w in g.succ[v] if w != s[v] and g.key(W[w]) > g.key(W[s[v]])]


def analyse(g, start, cnt, name):
    st = RE.run(g, start)
    n, m = g.n, sum(len(x) for x in g.succ)
    Q = [v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1]
    info = []
    for x in st:
        W = E.wval(g, x["s"], x["t"])
        info.append(dict(lam=tuple(v[0] for v in x["Xi"]), t=tuple(x["t"]), W=W, hon=(list(x["Xi"]) == list(W)),
                         D=frozenset(q for q in Q if x["sb"][q] != x["t"][q]), sbQ=tuple(x["sb"][q] for q in Q), fb=x["fb"]))
    K = len(st); k = 0
    while k < K:
        j = k
        while j + 1 < K and info[j + 1]["lam"] == info[k]["lam"] and info[j + 1]["t"] == info[k]["t"]: j += 1
        phase(g, st, info, k, j, cnt, name, n, m, Q)
        k = j + 1


def phase(g, st, info, a, b, cnt, name, n, m, Q):
    cnt["PHASES"] += 1
    t = list(st[a]["t"]); lam = info[a]["lam"]
    f = sum(1 for k in range(a, b) if info[k]["fb"])
    H = [k for k in range(a, b + 1) if info[k]["hon"]]
    f_in = sum(1 for k in range(a, b) if info[k]["fb"] and not info[k]["hon"] and H and H[0] < k < H[-1])
    cnt["f_in_total"] += f_in; cnt["fb_at_honest"] += sum(1 for k in range(a, b) if info[k]["fb"] and info[k]["hon"])
    cnt["MAX_HONEST"] = max(cnt["MAX_HONEST"], len(H))
    bnd = 4 * n * n - 3 * n
    cnt["HON_chk"] += 1
    if len(H) > f + bnd: fail(cnt, "HON", name, a, len(H), f)
    if len(H) > f_in + bnd: fail(cnt, "HONP", name, a, len(H), f_in)
    d0 = [k for k in range(a, b + 1) if not info[k]["D"]]
    for k in d0:
        cnt["D0H_chk"] += 1
        if not info[k]["hon"]: fail(cnt, "D0H", name, k)
    eps = []; k = a
    while k <= b:
        j = k
        while j + 1 <= b and info[j + 1]["sbQ"] == info[k]["sbQ"]: j += 1
        eps.append((k, j)); k = j + 1
    N0 = sum(1 for (x, y) in eps if not info[x]["D"])
    tr0 = sum(1 for (x, y) in eps if not info[x]["D"] for kk in range(x, y + 1) if kk < b)
    cnt["H0_chk"] += 1
    if max(len(d0), N0, tr0) > f_in + bnd: fail(cnt, "H0", name, a, len(d0), N0, tr0, f_in)
    cnt["MAX_N0"] = max(cnt["MAX_N0"], N0)
    # HON-FB (no LEV needed for FB1-FB3, FB4 last/honest)
    succ_t = [list(g.succ[v]) if g.owner[v] == 0 else [t[v]] for v in range(n)]
    for h in range(a, b):
        if info[h]["fb"] and not info[h]["hon"]:  # control: FB1's flatness test on fallbacks it does not claim
            W = info[h]["W"]
            if any(not (W[x][0] == x and W[z][0] == x and W[z][1] == 0) for (x, z) in w_improving(g, W, st[h]["s"])): cnt["CTRL_FB1_nonhonest_nonflat"] += 1
            if info[h + 1]["W"] != W: cnt["CTRL_FB2_nonhonest_Wchange"] += 1
        if not (info[h]["hon"] and info[h]["fb"]): continue
        cnt["FB_chk"] += 1
        W = info[h]["W"]; s = st[h]["s"]
        for (x, z) in w_improving(g, W, s):
            if not (W[x][0] == x and W[z][0] == x and W[z][1] == 0): fail(cnt, "FB1", name, h, x, z)
        if info[h + 1]["W"] != W: fail(cnt, "FB2", name, h)
        if w_improving(g, info[h + 1]["W"], st[h + 1]["s"]): fail(cnt, "FB3", name, h)
        if not info[h + 1]["hon"] or h + 1 != b: fail(cnt, "FB4", name, h, info[h + 1]["hon"], h + 1 == b)
    # REC-1 (a)
    ints = []; k = a
    while k <= b:
        if len(info[k]["D"]) == 1:
            j = k
            while j + 1 <= b and info[j + 1]["D"] == info[k]["D"]: j += 1
            ints.append((k, j)); k = j + 1
        else: k += 1
    src0 = xdir = xbig = 0
    for (x, y) in ints:
        if x == a: continue
        Dk = info[x - 1]["D"]
        if not Dk: src0 += 1
        elif len(Dk) == 1: xdir += 1
        else: xbig += 1
    cnt["REC1_chk"] += 1; cnt["INTERVALS"] += len(ints); cnt["X_dir"] += xdir; cnt["X_big"] += xbig; cnt["INT_from_D0"] += src0
    if len(ints) > 1 + src0 + xdir + xbig or len(ints) > 1 + f_in + bnd + xdir + xbig: fail(cnt, "REC1", name, a, len(ints))
    # LEV-based checks
    if n <= int(os.environ.get("LEVMAX", "11")):
        cyc = {u for u in range(n) if lam[u] == u}
        best = best_le(g, succ_t, cyc, n)
        LEV = {k: level(g, st[k]["Xi"], best, n) for k in range(a, b + 1)}
        for k in range(a, b + 1):
            cnt["LB0_chk"] += 1
            if LEV[k] < 0: fail(cnt, "LB0", name, k)
            if k < b and LEV[k + 1] < LEV[k]: fail(cnt, "LMON", name, k)
        for h in H:  # control: the DEAD claims IMM / IMM' (packet §5) must be detectable by this LEV
            if h < b and not info[h]["fb"] and LEV[h + 1] < min(LEV[h] + 1, n - 1):
                cnt["CTRL_IMM_fails"] += 1
                if h + 1 != b: cnt["CTRL_IMMP_fails"] += 1; EX.append(("CTRL_IMMP", name, h, LEV[h], LEV[h + 1], LEV.get(h + 2)))
        B = [best[x][n - 1] for x in range(n)]
        for h in H:
            cnt["SAT_chk"] += 1
            if any(B[x] is not None and g.key(st[h]["Xi"][x]) > g.key(B[x]) for x in range(n)): fail(cnt, "SAT", name, h, "Xi>B")
            if LEV[h] == n - 1 and list(st[h]["Xi"]) != B: fail(cnt, "SAT", name, h, "lev n-1, Xi != B")
        for i in range(len(H) - 1):
            h, h2 = H[i], H[i + 1]
            fbs = [k for k in range(h, h2) if info[k]["fb"]]
            if not fbs or (MUT == 2):
                if not fbs:
                    cnt["GAPW_chk"] += 1
                    for k in range(h, h2):
                        if any(g.key(info[k + 1]["W"][x]) < g.key(info[k]["W"][x]) for x in range(n)): fail(cnt, "GAPW", name, k)
                    if tuple(v[0] for v in info[h + 1]["W"]) != lam: fail(cnt, "GAPW", name, h, "lamW")
                cnt["STEP1_chk"] += 1
                if LEV[h2] < min(LEV[h] + (2 if MUT == 3 else 1), n - 1): fail(cnt, "STEP1", name, h, h2, LEV[h], LEV[h2], "fbs", fbs)
            else:
                cnt["FFGAP"] += 1
                if any(k != h for k in fbs):
                    cnt["FFGAP_inside"] += 1
                    if LEV[h2] < min(LEV[h] + 1, n - 1): cnt["HONFF_norise"] += 1; EX.append(("HONFF", name, h, h2, LEV[h], LEV[h2]))
        uns = [h for h in H if LEV[h] < n - 1]; sat = [h for h in H if LEV[h] >= n - 1]
        cnt["CNT_chk"] += 1
        if uns and sat and min(sat) < max(uns): fail(cnt, "CNT", name, a, "sat before unsat")
        if len(uns) - 1 > f_in + n - 2: fail(cnt, "CNT", name, a, len(uns), f_in)
        if sat and sat[-1] - sat[0] > 4 * n * (n - 1): fail(cnt, "CNT", name, a, "tail")
        for h in range(a, b):
            if info[h]["hon"] and info[h]["fb"]:
                if LEV[h + 1] != n - 1: fail(cnt, "FB4", name, h, "LEV", LEV[h + 1])
        # SAT0 at every state of P without W-improving edges
        cache = {}
        for k in range(a, b + 1):
            W = info[k]["W"]
            if w_improving(g, W, st[k]["s"]): continue
            cw = frozenset(u for u in range(n) if W[u][0] == u)
            if cw not in cache: cache[cw] = best_le(g, succ_t, cw, n)
            bw = cache[cw]
            cnt["SAT0_chk"] += 1
            if any(bw[x][n - 1] is not None and g.key(W[x]) < g.key(bw[x][n - 1]) for x in range(n)): fail(cnt, "SAT0", name, k)
            if info[k]["hon"] and LEV[k] != n - 1: fail(cnt, "SAT0", name, k, "honest not saturated")
    # RESTRICT_u / REPRO_u
    if os.environ.get("NORU") == "1": return
    for u in Q:
        k = a
        while k <= b:
            if not info[k]["D"] <= {u}: k += 1; continue
            x = k
            while k + 1 <= b and info[k + 1]["D"] <= {u}: k += 1
            y = k; k += 1
            L = (y - x) + (1 if y < b else 0)
            gp = gu_game(g, t, u)
            nep = len({info[z]["sbQ"] for z in range(x, y + 1)})
            cnt["URUNS"] += 1; cnt["URUN_MULTI"] += nep > 1; cnt["MAX_URUN_LEN"] = max(cnt["MAX_URUN_LEN"], L)
            if nep > 1 and any(info[z]["D"] == {u} for z in range(x, y + 1)): cnt["URUN_MULTI_withU"] += 1
            for kk in range(x, y + 1):
                s = st[kk]["s"]
                Xi, sb, Is, It, _ = E.gates(g, s, t)
                Xp, sbp, Isp, Itp, _ = E.gates(gp, s, t)
                cnt["RU_chk"] += 1
                if Xp != Xi or E.wval(gp, s, t) != E.wval(g, s, t): fail(cnt, "RU1", name, kk, u, sorted(info[kk]["D"]))
                if sorted(Isp) != sorted(Is): fail(cnt, "RU2", name, kk, u)
                elif Is and E.s4a(gp, s, t, Isp) != E.s4a(g, s, t, Is): fail(cnt, "RU2out", name, kk, u)
                Eg = {(v, w) for v in range(n) for w in gp.succ[v]}
                if sorted(Itp) != sorted(e for e in It if e in Eg): fail(cnt, "RU3", name, kk, u)
                if kk < b and Itp:
                    Hh, val, _ = E.s4b_arena(gp, s, t, Itp)
                    cnt["RU4_chk"] += 1
                    if E.wval(Hh, s, t) != val: fail(cnt, "RU4", name, kk, u)
            s, tt = list(st[x]["s"]), list(t); ok = True; lamok = True
            for kk in range(x, x + L):
                if kk <= y:
                    Xp, _ = RE.evaluate(gp, s)
                    if tuple(v[0] for v in Xp) != lam: lamok = False
                r = E.n5tau_step(gp, s, tt)
                if r is None: ok = False; break
                sn, tn, fbb, dv = r; cnt["DIV"] += dv
                if sn != list(st[kk + 1]["s"]) or tn != list(t) or fbb != bool(info[kk]["fb"]): ok = False; break
                s, tt = sn, tn
            if L == 0:
                Xp, _ = RE.evaluate(gp, s)
                if tuple(v[0] for v in Xp) != lam: lamok = False
            cnt["REPU_chk"] += 1
            if not ok or not lamok: fail(cnt, "REPU", name, x, u, ok, lamok)
            if y < b:
                Xy, _ = RE.evaluate(gp, st[y + 1]["s"])
                cnt["EXIT_chk"] += 1
                if tuple(v[0] for v in Xy) != info[y + 1]["lam"]: cnt["EXITLAM"] += 1


def parse_start(g, path):
    """start file: two lines 'sigma v:w ...' / 'tau v:w ...' or a list 'v w' per line with owner deciding; accept both"""
    s = [None] * g.n; t = [None] * g.n
    for l in open(path):
        l = l.split("#")[0].strip()
        if not l: continue
        toks = l.replace(",", " ").split()
        pairs = [x for x in toks if ":" in x or "->" in x]
        if pairs:
            for p in pairs:
                v, w = p.replace("->", ":").split(":"); v, w = int(v), int(w)
                (s if g.owner[v] == 0 else t)[v] = w
        elif len(toks) == 2 and toks[0].lstrip("-").isdigit():
            v, w = int(toks[0]), int(toks[1]); (s if g.owner[v] == 0 else t)[v] = w
    assert all((s[v] if g.owner[v] == 0 else t[v]) in g.succ[v] for v in range(g.n)), "bad start file"
    return s, t


def main(a):
    cnt = Counter(); rng = random.Random(1414); nst = int(os.environ.get("RANDSTARTS", "2"))
    def do(g, name, r, extra=None):
        starts = ([extra] if extra else []) + [RE.best_reward_start(g)] + [D.rand_start(g, r) for _ in range(nst)]
        for j, s0 in enumerate(starts):
            cnt["RUNS"] += 1; analyse(g, s0, cnt, "%s/%d" % (name, j))
    if a[0] == "rand":
        N, lo, hi, km, seed = map(int, a[1:6]); r2 = random.Random(seed)
        for i in range(N):
            nn = r2.randint(lo, hi)
            g = D.rand_ck(r2, nn, r2.randint(0, min(km, nn - 1)))
            do(g, "rand%d" % i, rng)
    else:
        for f in a:
            path, _, sp = f.partition(":")
            g = RE.parse(path)
            if g.n > int(os.environ.get("MAXN", "64")): cnt["skip_big"] += 1; continue
            do(g, os.path.relpath(path), random.Random(os.path.relpath(path)), parse_start(g, sp) if sp else None)
    for k in sorted(cnt): print(k, cnt[k])
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
