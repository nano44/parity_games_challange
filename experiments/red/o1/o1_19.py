#!/usr/bin/env python3
"""Box 45 (L-RED successor 19): adversary on P-N5-1O (docs/si/P-N5-1O-box15.md, sha1 2cf5e672), written from the packet text.
Per run of N5 (SPEC S1-S5, own copy of n5.py's loop) on a 𝒞^1O game from a start pair (None = SPEC S3 start, Engine.initial("best")):
  ITER   number of iterations (= transitions, R15 (d)); bound ITER* = (n(n−1)+d_o)(T*+1), T* from §2's chain with F = 2n².
  PH     phases (maximal runs with (λ, τ) constant; λ(v) = cycle node of Ξσ(v)); bound R47 (b): n(n−1)+d_o.
  TAU    τ changes; bound R47 (a): d_o − 1.
  f      in-phase Even fallbacks per phase; bound R48 (i): o ≠ c_θ: 1+(|U|−2)(|succ(o)∩Û|+|U|) [deg_U(o) = |succ(o) ∩ U| as in P-N5-FBPOLY; the
         RESULTS R48 / P-N5-1O §1 wording |succ(o) ∩ Û|, Û = U ∖ {o}, as FB_R48hat; F = 2n² as FB_F]; |U| = 2: 1; o = c_θ: |U|.
  T      transitions with both ends in one phase; bound T* (R50 (h) at f = F; per phase also at the phase's own f).
  OUT    Lemma OUT: W = {v : Ω(λ(v)) even} at the stop equals Oink's (--zlk; --tl fallback) W_E; σ on W and σ̄ on V∖W are winning
         (harness/verify.py, closure + one-player cycle test) and Oink's own `-v --sol` accepts the written solution.
Mode "of": N5^OF (P-N5-DUAL §0: at an S4c fallback Odd falls back first if Iτ ≠ ∅). Counted as data for box 45 (2).
Usage: o1_19.py rand seed secs nmin nmax R OUT [--of] [--nooink]  |  o1_19.py file game.pg [start.json] [--of]"""
import sys, os, json, random, time, subprocess, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
for p in ("../so", "../../new", "../../si", "../../harness"): sys.path.insert(0, os.path.join(HERE, p))
import pg, n5, verify
from si import Engine
OINK = os.path.join(HERE, "..", "..", "..", "tools", "oink", "build", "oink")

def trace(g, start=None, mode="n5", cap=10 ** 6):
    n = g.n; E, Ed = Engine(g), Engine(n5.dual(g))
    sigma, tau = list(E.initial("best")), list(Ed.initial("best"))
    if start is not None:
        for v in range(n):
            if g.owner[v] == 0: sigma[v] = start[v]
            else: tau[v] = start[v]
    S = [(tuple(sigma), tuple(tau))]; FB = []
    while len(FB) < cap:
        vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        vt, tbar = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
        if not Is and not It: break
        ns, nt = list(sigma), list(tau)
        if Is:
            opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
            for v, w in Is: opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
            _, best = Engine(n5.dual(pg.Game(list(g.prio), list(g.owner), succ))).evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] == 0: ns[v] = best[v]
        if It:
            opt = {v: {tau[v]} for v in range(n) if g.owner[v] == 1}
            for v, w in It: opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 1 else [sigma[v]] for v in range(n)]
            _, best = Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(tuple(sigma[v] if g.owner[v] == 0 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] == 1: nt[v] = best[v]
        fb = 0
        if ns == sigma and nt == tau:
            even = bool(Is) if mode == "n5" else not It
            if even:
                fb = 1
                for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
            else:
                fb = 2
                for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
        sigma, tau = ns, nt; S.append((tuple(sigma), tuple(tau))); FB.append(fb)
    return S, FB, E

def bounds(n, m, d, D, F=None):
    F = 2 * n * n if F is None else F
    TH = n * n + 2 * n - 1; XSN = 13 * (d + 1) * n ** 3 * (F + 1 + TH) + TH; X = (F + 1) * (n - 1) + F + XSN
    Th = (n - 1) + n * (X + 1) + X; So = d * (Th + 1); Wch = (F + X + 1) * n * n; Nst = 1 + X + Th + Wch
    NXi = F + Nst + (X + 1) * (n - 1) + (Nst + F) * 3 * D * n ** 4; Ts = (m - n + 1) * (So + NXi + 1)
    return Ts, (n * (n - 1) + d) * (Ts + 1)

def oddchoice(g): return [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1]

def oink_check(g, win, ws, tmp):
    gp, sp, rp = (os.path.join(tmp, x) for x in ("g.pg", "a.sol", "r.sol"))
    pg.write(g, gp); pg.write_sol(win, sp, ws)
    for solver in ("--zlk", "--tl"):
        try:
            subprocess.run([OINK, solver, gp, rp], capture_output=True, timeout=120, check=True); break
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired): continue
    else: return "NOREF"
    ref = pg.read_sol(open(rp).read(), g.n)
    if ref != win: return "MISMATCH"
    r = subprocess.run([OINK, "--no", "-v", "--sol", sp, gp], capture_output=True, text=True, timeout=120)
    if r.returncode != 0 or "verified" not in (r.stdout + r.stderr).lower(): return "OINKV " + (r.stdout + r.stderr)[-200:].replace("\n", " | ")
    return "OK"

def analyse(g, start=None, mode="n5", tmp=None, use_oink=True):
    oc = oddchoice(g); assert len(oc) == 1, "not C^1O"; o = oc[0]; n = g.n; m = sum(len(set(s)) for s in g.succ)
    d = len(set(g.succ[o])); D = max(len(set(s)) for s in g.succ)
    S, FB, E = trace(g, start, mode)
    ev = [E.evaluate(s) for s, _ in S]; lam = [tuple(x[0] for x in X) for X, _ in ev]
    Xi = [X for X, _ in ev]; SB = [B for _, B in ev]
    r = dict(n=n, m=m, d=d, ITER=len(FB), fb_even=sum(1 for x in FB if x == 1), fb_odd=sum(1 for x in FB if x == 2))
    Ts, IT = bounds(n, m, d, D); r["ITERb"] = IT; r["PHb"] = n * (n - 1) + d
    r["TAU"] = sum(1 for k in range(len(FB)) if S[k][1] != S[k + 1][1])
    ph = []; a = 0; N = len(S)
    while a < N:
        b = a
        while b + 1 < N and lam[b + 1] == lam[a] and S[b + 1][1] == S[a][1]: b += 1
        ct = lam[a][o]; U = {z for z in range(n) if lam[a][z] == ct}; u = len(U); dU = len(set(g.succ[o]) & U); dUh = len(set(g.succ[o]) & (U - {o}))
        f = sum(1 for k in range(a, b) if FB[k] == 1); fo = sum(1 for k in range(a, b) if FB[k] == 2)
        fbd = u if o == ct else (1 if u == 2 else 1 + (u - 2) * (dU + u))       # P-N5-FBPOLY (a): deg_U(o) = |succ(o) ∩ U|
        fbh = u if o == ct else (1 if u == 2 else 1 + (u - 2) * (dUh + u))      # RESULTS R48 / P-N5-1O §1 wording: |succ(o) ∩ Û|
        Th = sum(1 for k in range(a, b) if Xi[k][o] != Xi[k + 1][o])                         # Θ: θ = Ξ(o) changes (R27)
        So = sum(1 for k in range(a, b) if SB[k][o] != SB[k + 1][o] and lam[k][o] != o)     # S_o: relevant σ̄(o) changes (R27)
        ph.append(dict(T=b - a, f=f, fo=fo, u=u, oc=o == ct, fbd=fbd, fbh=fbh, Th=Th, So=So, Tb=bounds(n, m, d, D, f)[0])); a = b + 1
    r["PH"] = len(ph); r["Tmax"] = max(p["T"] for p in ph); r["fmax"] = max(p["f"] for p in ph)
    r["fslack"] = max(p["f"] - p["fbd"] for p in ph); r["fslackhat"] = max(p["f"] - p["fbh"] for p in ph)
    r["fcap"] = max(p["f"] - max(1, p["u"] - 2) for p in ph); r["fF"] = r["fmax"] - 2 * n * n; r["Tslack"] = max(p["T"] - p["Tb"] for p in ph)
    r["fo_inphase"] = sum(p["fo"] for p in ph)
    r["Thmax"] = max(p["Th"] for p in ph); r["Somax"] = max(p["So"] for p in ph)
    r["Th_oc"] = max([p["Th"] for p in ph if p["oc"]] + [0]); r["So_oc"] = max([p["So"] for p in ph if p["oc"]] + [0])
    r["So_slack"] = max(p["So"] - d * (p["Th"] + 1) for p in ph)
    r["Tn"] = r["Tmax"] / (m - n + 1)
    fails = []
    if r["ITER"] > IT: fails.append("ITER")
    if r["PH"] > r["PHb"]: fails.append("PHASES_R47b")
    if r["TAU"] > d - 1: fails.append("TAU_R47a")
    if r["fslack"] > 0: fails.append("FB_R48")
    if r["fslackhat"] > 0: fails.append("FB_R48hat")
    if r["fF"] > 0: fails.append("FB_F")
    if r["Th_oc"] or r["So_oc"]: fails.append("OC_THETA_SO")
    if r["So_slack"] > 0: fails.append("SO_R27g")
    if r["Tslack"] > 0: fails.append("T_R50h")
    if mode == "n5" and r["fo_inphase"]: fails.append("ODDFB_INPHASE")
    win, ws = E.regions(S[-1][0])
    lamf = lam[-1]; W = [E.par[lamf[v]] for v in range(n)]
    if W != win: fails.append("OUT_W_formula")
    e = verify.check(g, win, ws)
    if e: fails.append("OUT_STRAT " + e[0])
    if use_oink:
        oc_ = oink_check(g, win, ws, tmp)
        if oc_ != "OK": fails.append("OUT_OINK " + oc_)
    r["fails"] = fails
    return r

def randgame(rng, nmin, nmax):
    while True:
        n = rng.randint(nmin, nmax)
        prio = [rng.randrange(2 * n) for _ in range(n)]; owner = [0 if rng.random() < 0.7 else 1 for _ in range(n)]
        succ = [sorted(set(rng.sample(range(n), 1 if owner[v] else rng.choice((1, 2, 2, 3))))) for v in range(n)]
        o = rng.randrange(n); owner[o] = 1; succ[o] = sorted(set(rng.sample(range(n), rng.randint(2, max(2, n // 2)))))
        g = pg.Game(prio, owner, succ)
        if len(oddchoice(g)) == 1: return g

if __name__ == "__main__":
    a = sys.argv; mode = "of" if "--of" in a else "n5"; uo = "--nooink" not in a
    tmp = tempfile.mkdtemp()
    if a[1] == "file":
        g = pg.parse("".join(l for l in open(a[2]) if not l.lstrip().startswith("%")))
        st = json.load(open(a[3]))["start"] if len(a) > 3 and a[3].endswith(".json") else None
        print(json.dumps(analyse(g, st, mode, tmp, uo))); sys.exit()
    seed, secs, nmin, nmax, R, out = int(a[2]), float(a[3]), int(a[4]), int(a[5]), int(a[6]), a[7]
    rng = random.Random(seed); t0 = time.time(); best = {}; runs = 0; fails = {}
    keys = ("ITER", "PH", "Tmax", "fmax", "fslack", "fslackhat", "fcap", "TAU", "ITERn", "Thmax", "Somax", "Tn")
    while time.time() - t0 < secs:
        g = randgame(rng, nmin, nmax)
        for k in range(R + 1):
            st = None if k == 0 else [rng.choice(g.succ[v]) for v in range(g.n)]
            r = analyse(g, st, mode, tmp, uo); runs += 1; r["ITERn"] = r["ITER"] / g.n
            for f in r["fails"]:
                fails[f.split()[0]] = fails.get(f.split()[0], 0) + 1
                if fails[f.split()[0]] <= 3:
                    json.dump(dict(prio=g.prio, owner=g.owner, succ=g.succ, start=st, r=r), open(f"{out}_FAIL_{f.split()[0]}_{fails[f.split()[0]]}.json", "w"))
                    print("FAIL", f, r, flush=True)
            for kk in keys:
                if kk not in best or r[kk] > best[kk][0]:
                    best[kk] = (r[kk], dict(prio=g.prio, owner=g.owner, succ=g.succ, start=st, r=r))
    json.dump({k: v[1] for k, v in best.items()}, open(out + "_best.json", "w"))
    print("RUNS", runs, "FAILS", fails, {k: v[0] for k, v in best.items()}, flush=True)
