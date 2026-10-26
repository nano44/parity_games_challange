#!/usr/bin/env python3
"""REFEREE successor 8 probe for packet P-N5-RL (docs/si/P-N5-RL-box10.md, pin 2fb698d, sha1 0a3c70cb...).
Own engine rl_engine.py (SPEC S1-S5 from the text; no lane code). Every game is asserted to be in C^1O: exactly one Odd vertex
with out-degree > 1. Definitions from P-N5-FBW §0 / P-N5-RL §0: R-bar = {o} + vertices whose (sigma, tau)-play reaches o; F = rest;
H1 o not on the (sigma, sigmabar)-cycle of o; H2 o not on its (sigma, tau)-cycle; H3 cycle node of theta = that of w; phase key =
(lambda_Xi, tau); scope run = maximal run of in-phase transitions k with (h) at k, H2 at k+1, w_{k+1} = w_k.
Checks (counters; *_FAIL must be 0 for the packet's claims):
 BLF     BL-FORM (a)-(c) and Lemma G form at every blocked edge of every (h) state
 BL      at in-phase THR fallbacks with (h): (a), (b), (c) (Opt of G_tau[F] by own VJ on the dual), (d) incl. all deficient exits,
         (e) for the computed optimum; F1 sampled
 FF      FREE-FREEZE for every (k0, t, z)
 EQ      EQ-END: <= 1 fallback after theta = w in S, and it ends the phase; EQ_END_NOTH counts scope runs whose last state is not (h)
 MG      MERGE (a)-(c) at every window gate of every (h) state
 TEV     after an in-scope fallback k0 with L = M_{k0} >= 0, states t in (k0, next fallback of S] with r > L on [k0+1, t]:
         x_t's play meets Ev; Ev on the cycle; TEV-RED (1)-(3) with e = the last Ev vertex in lasso order; post-rise (4);
         ENT setting count, EV / EV+ when it occurs
Usage: rl_probe.py file.pg ... | lib | named | rand N nmin nmax seed"""
import sys, os, random, glob
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
BOT, INF = -2, 10 ** 6
EX = []


def lev(x, y):
    if x == y: return BOT
    if x[0] != y[0]: return INF
    d = x[1] ^ y[1]
    return d.bit_length() - 1 if d else -1


def coarse(x, L):
    if L >= INF: return 0
    if L <= BOT: return x
    return (x[0], x[1] & ~((1 << (L + 1)) - 1))


def assert_c1o(g):
    odd = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1]
    assert len(odd) == 1, "not C^1O: %d Odd choice vertices" % len(odd)
    return odd[0]


def returns(nx, o):
    pre, cyc = RE.lasso(nx, o)
    return o in cyc


def route(nx, v, o):
    """vertices of v's play before o (v's play reaches o)"""
    out, x = [], v
    while x != o: out.append(x); x = nx[x]; assert len(out) <= len(nx)
    return out


def extp(g, path, x):
    for u in reversed(path): x = g.ext(u, x)
    return x


def states(g):
    o = assert_c1o(g); n = g.n; run = RE.run(g); st = []
    for a in run:
        s, t, Xi, sb = a["s"], a["t"], a["Xi"], a["sb"]
        nx = [s[v] if g.owner[v] == 0 else t[v] for v in range(n)]
        hg = [s[v] if g.owner[v] == 0 else sb[v] for v in range(n)]
        W = [RE.play_value(g, nx, v) for v in range(n)]
        Rb = set()
        for v in range(n):
            pre, cyc = RE.lasso(nx, v)
            if o in pre or o in cyc: Rb.add(v)
        F = set(range(n)) - Rb
        H1, H2, H3 = not returns(hg, o), not returns(nx, o), Xi[o][0] == W[o][0]
        gl = [lev(Xi[s[y]], Xi[z]) for y, z in a["Is"]]
        st.append(dict(s=s, t=t, Is=a["Is"], It=a["It"], fb=a["fb"], Xi=Xi, sb=sb, Ut=a["Ut"], W=W, nx=nx, hg=hg, Rb=Rb, F=F, H1=H1, H2=H2,
                       H3=H3, h=H1 and H2 and H3, r=lev(Xi[o], W[o]) if H3 else INF, M=max(gl, default=BOT),
                       key=(tuple(x[0] for x in Xi), tuple(t))))
    return o, st


def K(g, x): return g.key(x)


def opt_one_player(g, keep, fixed_odd):
    """optimal valuation of the one-player game with successor lists keep (Odd vertices keep one edge): own VJ procedure on the
    dual with the Odd side fixed. Returns (val, strategy)."""
    h = g.restrict(keep); hd = h.dual()
    val, ch = RE.evaluate(hd, [fixed_odd[v] if g.owner[v] == 1 else None for v in range(g.n)])
    strat = [ch[v] if g.owner[v] == 0 else None for v in range(g.n)]
    nx = [strat[v] if g.owner[v] == 0 else keep[v][0] for v in range(g.n)]
    pv = [RE.play_value(g, nx, v) for v in range(g.n)]
    return val, strat, pv


def check_state_blf(g, o, a, cnt, name, k):
    Xi, W, s, nx, Rb, F = a["Xi"], a["W"], a["s"], a["nx"], a["Rb"], a["F"]
    th, w = Xi[o], W[o]; c = th[0]
    blocked = []
    for v in range(g.n):
        if g.owner[v] != 0: continue
        for u in g.succ[v]:
            if u == s[v]: continue
            wimp = K(g, W[u]) > K(g, W[s[v]]); gate = K(g, Xi[u]) > K(g, Xi[s[v]])
            if wimp and not gate:
                blocked.append((v, u)); cnt["BLF_edges"] += 1
                okA = s[v] in F and v in F and u in Rb
                pu = route(nx, u, o) if u in Rb else None
                okB = pu is not None and K(g, extp(g, pu, th)) <= K(g, Xi[s[v]]) < K(g, extp(g, pu, w))
                okC = Xi[s[v]][0] == c
                okG = pu is not None and Xi[u] == extp(g, pu, th) and W[u] == extp(g, pu, w)
                for ok, lab in ((okA, "a"), (okB, "b"), (okC, "c"), (okG, "G")):
                    if not ok: cnt["BLF_%s_FAIL" % lab] += 1; EX.append((name, "BLF" + lab, k, v, u))
    return blocked


def check_merge(g, o, a, cnt, name, k):
    Xi, s, nx, Rb, F, sb = a["Xi"], a["s"], a["nx"], a["Rb"], a["F"], a["sb"]
    th = Xi[o]; c = th[0]; x0 = sb[o]
    for y, z in a["Is"]:
        if not (y in Rb and y != o and z in F): continue
        l = lev(Xi[s[y]], Xi[z])
        if l >= INF:
            cnt["MG_gates_levINF"] += 1
            zs = set(sum(RE.lasso(nx, z), [])); xs0 = set(sum(RE.lasso(nx, x0), []))
            if not (zs & xs0): cnt["MG_levINF_plays_disjoint"] += 1; EX.append((name, "MG_INF_disjoint", k, y, z))
            continue
        cnt["MG_gates"] += 1
        top = max(l, g.rank[c]); Hs = {v for v in range(g.n) if g.rank[v] > top}
        pi = route(nx, s[y], o)
        okA = not (set(pi) & Hs) and coarse(Xi[z], l) == coarse(extp(g, pi, th), l)
        okB = o not in Hs
        pz, cz = RE.lasso(nx, z); px, cx = RE.lasso(nx, x0)
        zp, xp = pz + cz, px + cx; xs = set(xp)
        m = next(v for v in zp if v in xs)
        okC = not (set(zp[:zp.index(m)]) & Hs) and not (set(xp[:xp.index(m)]) & Hs)
        for ok, lab in ((okA, "a"), (okB, "b"), (okC, "c")):
            if not ok: cnt["MG_%s_FAIL" % lab] += 1; EX.append((name, "MG" + lab, k, y, z))


def check_bl(g, o, st, k, cnt, name, rng):
    a = st[k]; Xi, W, s, t, F, Rb, nx = a["Xi"], a["W"], a["s"], a["t"], a["F"], a["Rb"], a["nx"]
    n = g.n; th, w = Xi[o], W[o]; x0 = a["sb"][o]; cnt["BL_fb"] += 1
    keep = [g.succ[v] if g.owner[v] == 0 else [t[v]] for v in range(n)]
    Ws, ss, pv = opt_one_player(g, keep, t)
    if pv != Ws: cnt["BL_OPTPLAY_FAIL"] += 1; EX.append((name, "optplay", k))
    for _ in range(10):  # F1 sampled: W* dominates random strategies (own VJ optimum, not (P))
        sr = [rng.choice(g.succ[v]) if g.owner[v] == 0 else None for v in range(n)]
        nr = [sr[v] if g.owner[v] == 0 else t[v] for v in range(n)]
        cnt["BL_F1_chk"] += 1
        if any(K(g, RE.play_value(g, nr, v)) > K(g, Ws[v]) for v in range(n)): cnt["BL_F1_FAIL"] += 1
    if any(K(g, W[v]) > K(g, Ws[v]) for v in range(n)): cnt["BL_F1cur_FAIL"] += 1
    # Step 0: Odd's dual valuation of tau equals W* (as triples), and (o, x) in I_tau iff W*(x) < W*(e*)
    if a["Ut"] != Ws: cnt["BL_step0_U_FAIL"] += 1; EX.append((name, "step0U", k))
    es = t[o]; Ito = {x for (v, x) in a["It"] if v == o}
    for x in g.succ[o]:
        if x == es: continue
        cnt["BL_step0_chk"] += 1
        if (x in Ito) != (K(g, Ws[x]) < K(g, Ws[es])): cnt["BL_step0_I_FAIL"] += 1; EX.append((name, "step0I", k, x))
    if W == Ws: cnt["BL_a_FAIL"] += 1; EX.append((name, "BLa", k))
    blocked = check_state_blf(g, o, a, Counter(), name, k)
    if not blocked: cnt["BL_b_FAIL"] += 1; EX.append((name, "BLb", k))
    # (c)
    for v in F:
        if g.owner[v] == 1 and t[v] not in F: cnt["BL_c_CLOSED_FAIL"] += 1
    keepF = [([u for u in g.succ[v] if u in F] if g.owner[v] == 0 else [t[v]]) if v in F else [v] for v in range(n)]
    Wf, sf, pvf = opt_one_player(g, keepF, [t[v] if v in F else v for v in range(n)])
    if any(Wf[v] != W[v] for v in F): cnt["BL_c_FAIL"] += 1; EX.append((name, "BLc", k))
    if any(K(g, Wf[v]) < K(g, W[v]) for v in F): cnt["BL_c_F1_FAIL"] += 1
    # (d)
    if not K(g, W[x0]) < K(g, Ws[x0]): cnt["BL_d_FAIL"] += 1; EX.append((name, "BLd", k))
    for x in g.succ[o]:
        if x in F and K(g, g.ext(o, Xi[x])) < K(g, w):
            cnt["BL_d_exits"] += 1
            if not K(g, W[x]) < K(g, Ws[x]): cnt["BL_d_exit_FAIL"] += 1; EX.append((name, "BLd2", k, x))
    # (e) for the computed optimum
    nxs = [ss[v] if g.owner[v] == 0 else t[v] for v in range(n)]
    pre, cyc = RE.lasso(nxs, x0); seq = pre + cyc
    if all(v in F for v in seq): cnt["BL_e_FAIL"] += 1; EX.append((name, "BLe", k))
    else:
        i = next(i for i, v in enumerate(seq) if v not in F)
        if g.owner[seq[i - 1]] != 0: cnt["BL_e_exit_FAIL"] += 1
    cnt["BL_blocked_on_x0play"] += any(v in RE.lasso(nx, x0)[0] + RE.lasso(nx, x0)[1] for v, u in blocked)


def scope_runs(st):
    T = len(st) - 1
    inph = [st[k]["key"] == st[k + 1]["key"] for k in range(T)]
    ok = [inph[k] and st[k]["h"] and st[k + 1]["H2"] and st[k]["W"][OO[0]] == st[k + 1]["W"][OO[0]] for k in range(T)]
    runs, k = [], 0
    while k < T:
        if ok[k]:
            j = k
            while j < T and ok[j]: j += 1
            runs.append(list(range(k, j)))  # transitions k..j-1, states k..j
            k = j
        else: k += 1
    return inph, runs


OO = [None]


def run(g, cnt, name, rng=None):
    rng = rng or random.Random(1)
    o, st = states(g); OO[0] = o; T = len(st) - 1; cnt["games"] += 1; cnt["states"] += len(st)
    inph, runs = scope_runs(st)
    for k, a in enumerate(st):
        if a["h"]:
            cnt["h_states"] += 1
            Rl = sorted(a["Rb"])
            for i1 in range(len(Rl)):
                for i2 in range(i1 + 1, len(Rl)):
                    u1, u2 = Rl[i1], Rl[i2]; cnt["RSAME_chk"] += 1
                    sx = (K(g, a["Xi"][u1]) > K(g, a["Xi"][u2])) - (K(g, a["Xi"][u1]) < K(g, a["Xi"][u2]))
                    sw = (K(g, a["W"][u1]) > K(g, a["W"][u2])) - (K(g, a["W"][u1]) < K(g, a["W"][u2]))
                    if sx != sw: cnt["RSAME_FAIL"] += 1; EX.append((name, "RSAME", k, u1, u2))
            check_state_blf(g, o, a, cnt, name, k); check_merge(g, o, a, cnt, name, k)
    # phases
    ph = [0] * len(st)
    for k in range(T): ph[k + 1] = ph[k] if inph[k] else ph[k] + 1
    blfb = []
    for k in range(T):
        a = st[k]
        if a["fb"] and inph[k] and a["h"] and K(g, a["Xi"][o]) < K(g, a["W"][o]):
            check_bl(g, o, st, k, cnt, name, rng); blfb.append(k)
    # FREE-FREEZE
    for k0 in blfb:
        F0 = st[k0]["F"]
        for t in range(k0 + 1, len(st)):
            if ph[t] != ph[k0]: break
            b = st[t]
            if not b["h"]: continue
            for z in b["F"]:
                pre, cyc = RE.lasso(b["nx"], z)
                if all(v in F0 for v in pre + cyc):
                    cnt["FF_chk"] += 1
                    if b["Xi"][z] != st[k0]["Xi"][z]: cnt["FF_FAIL"] += 1; EX.append((name, "FF", k0, t, z))
    # EQ-END and TEV
    for S in runs:
        sts = S + [S[-1] + 1]; w = st[S[0]]["W"][o]
        cnt["EQ_runs"] += 1
        teq = next((t for t in sts if st[t]["Xi"][o] == w), None)
        if teq is not None:
            cnt["EQ_runs_eq"] += 1
            fbs = [k for k in S if k >= teq and st[k]["fb"]]
            if len(fbs) > 1: cnt["EQ_MANY_FAIL"] += 1; EX.append((name, "EQmany", S[0], fbs))
            for k in fbs:
                cnt["EQ_fb_after"] += 1
                if not (k + 1 == T or not inph[k + 1]): cnt["EQ_LAST_FAIL"] += 1; EX.append((name, "EQlast", k))
            if any(st[t]["Xi"][o] != w for t in sts if t >= teq): cnt["EQ_THETA_FAIL"] += 1
            end = sts[-1]
            if not st[end]["h"]:
                cnt["EQ_END_NOTH"] += 1; EX.append((name, "EQ_end_not_h", S[0], end, st[end]["H1"], st[end]["H3"]))
        tev(g, o, st, S, cnt, name)


def tev(g, o, st, S, cnt, name):
    fbs = [k for k in S if st[k]["fb"]]
    for i, k0 in enumerate(fbs):
        L = st[k0]["M"]
        if L < 0: continue
        cnt["TEV_k0"] += 1
        F0, F1 = st[k0]["F"], st[k0 + 1]["F"]; Ev = F1 - F0; c = st[k0]["Xi"][o][0]
        cnt["TEV_k0_Ev_nonempty"] += bool(Ev)
        Hs = {v for v in range(g.n) if g.rank[v] > max(L, g.rank[c])}
        A = {v for v in Hs if st[k0]["Xi"][o][1] >> g.rank[v] & 1}
        cnt["TEV_k0_A_empty"] += not A
        cnt["TEV_k0_Ev_classc0"] += any(coarse(st[k0]["Xi"][v], L) == (c, 0) for v in Ev)
        k1 = fbs[i + 1] if i + 1 < len(fbs) else None
        last = k1 if k1 is not None else S[-1]
        risen = False
        for t in range(k0 + 1, last + 1):
            b = st[t]
            if not (b["r"] > L and b["r"] < INF): break
            if coarse(b["Xi"][o], L) != coarse(st[k0]["Xi"][o], L): risen = True
            if not b["h"]: break
            cnt["TEV_states"] += 1; cnt["TEV_states_post"] += risen
            xt = b["sb"][o]; pre, cyc = RE.lasso(b["nx"], xt); seq = pre + cyc
            Cc = RE.lasso(b["nx"], c)[1]
            if set(Cc) & Ev: cnt["TEV_Ev_on_c_cycle"] += 1; EX.append((name, "Ev_on_c_cycle", k0, t))
            if not (set(seq) & Ev): continue
            cnt["TEV_meet"] += 1; cnt["TEV_meet_post"] += risen
            if set(cyc) & Ev: cnt["TEV_Ev_on_xt_cycle"] += 1; EX.append((name, "Ev_on_xt_cycle", k0, t))
            e = [v for v in seq if v in Ev][-1]; f = b["nx"][e]
            fpre, fcyc = RE.lasso(b["nx"], f)
            ok1 = g.owner[e] == 0 and all(v in F0 for v in fpre + fcyc) and b["Xi"][f] == st[k0]["Xi"][f]
            if not ok1: cnt["TEVRED1_FAIL"] += 1; EX.append((name, "TEVRED1", k0, t, e, e in cyc))
            if not ok1: continue
            ue = st[k0]["s"][e]
            pu = route(st[k0]["nx"], ue, o)
            ok2 = not (set(pu) & Hs) and coarse(st[k0]["Xi"][ue], L) == coarse(st[k0]["Xi"][o], L) and o not in Hs
            if not ok2: cnt["TEVRED2_FAIL"] += 1; EX.append((name, "TEVRED2", k0, t, e))
            Bt = {v for v in Hs if b["Xi"][o][1] >> g.rank[v] & 1}
            before = set(seq[:seq.index(e)]) & Hs
            if Bt != A | before:
                if Bt == A | before | ({e} & Hs): cnt["TEVRED3_E_IN_H"] += 1; EX.append((name, "TEVRED3_eH", k0, t, e))
                else: cnt["TEVRED3_FAIL"] += 1; EX.append((name, "TEVRED3", k0, t, e))
            cnt["TEV_e_in_H"] += e in Hs
            if risen and ue in b["Rb"]:
                cnt["TEVRED4_chk"] += 1
                gate = K(g, b["Xi"][ue]) > K(g, b["Xi"][f]) and lev(b["Xi"][f], b["Xi"][ue]) > L
                if not gate: cnt["TEVRED4_FAIL"] += 1; EX.append((name, "TEVRED4", k0, t, e))
        if k1 is not None and st[k1]["M"] == L and risen and all(st[t]["r"] > L for t in range(k0 + 1, k1 + 1)):
            cnt["ENT_SETTING"] += 1; EX.append((name, "ENT", k0, k1))


def lib():
    out = []
    for l in open(os.path.join(ROOT, "experiments/new/box33/lib.txt")):
        if l.strip(): out.append(os.path.join(ROOT, l.split()[0]))
    return out


def named():
    out = [os.path.join(ROOT, l.split()[0]) for l in open(os.path.join(ROOT, "experiments/si/coarse/named.txt")) if l.strip()]
    out += sorted(glob.glob(os.path.join(ROOT, "experiments/si/coarse/instances/*.pg")))
    out += sorted(glob.glob(os.path.join(ROOT, "experiments/si/coarse/instances/box9/*.pg")))
    out += sorted(glob.glob(os.path.join(ROOT, "experiments/si/riselast/instances/*.pg")))
    return out


def rand_c1o(rng, n):
    while True:
        prio = rng.sample(range(n * 2), n); owner = [rng.random() < 0.5 for _ in range(n)]
        owner = [1 if x else 0 for x in owner]; o = rng.randrange(n); owner[o] = 1
        succ = []
        for v in range(n):
            if v == o: succ.append(rng.sample(range(n), rng.randint(2, min(5, n))))
            elif owner[v] == 1: succ.append([rng.randrange(n)])
            else: succ.append(rng.sample(range(n), rng.randint(1, min(4, n))))
        g = RE.Game(prio, owner, succ)
        try: assert_c1o(g)
        except AssertionError: continue
        return g


def main(argv):
    cnt = Counter()
    if argv[0] in ("lib", "named"):
        files = lib() if argv[0] == "lib" else named()
        for f in files:
            g = RE.parse(f)
            try: assert_c1o(g)
            except AssertionError: cnt["skip_not_c1o"] += 1; continue
            if g.n > 64: cnt["skip_big"] += 1; continue
            run(g, cnt, os.path.relpath(f, ROOT))
    elif argv[0] == "rand":
        N, lo, hi, seed = map(int, argv[1:5]); rng = random.Random(seed)
        for i in range(N): run(rand_c1o(rng, rng.randint(lo, hi)), cnt, "rand%d_%d" % (seed, i), rng)
    else:
        for f in argv: run(RE.parse(f), cnt, f)
    for kk in sorted(cnt): print("%-24s %d" % (kk, cnt[kk]))
    fails = sum(v for kk, v in cnt.items() if kk.endswith("_FAIL"))
    print("FAILS", fails)
    seen = Counter()
    for e in EX:
        seen[e[1]] += 1
        if seen[e[1]] <= 6: print("EX", e)
    for kk, v in seen.items(): print("EXCOUNT", kk, v)


if __name__ == "__main__":
    main(sys.argv[1:])
