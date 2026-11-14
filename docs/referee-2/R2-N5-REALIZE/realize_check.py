#!/usr/bin/env python3
r"""REFEREE-2 successor 26 (Opus 5.5, D15): my own check of P-N5-REALIZE (docs/red/P-N5-REALIZE.md, sha1 067f06b6 @ l-red e609c5d2).
I did not import the lane's code: no r178/fastcyc, r187/stab, r187/ideal, r189/lemck and no new/box21/n5x.
- The game Gamma(G) is built from the genome JSON by MY builder, written from packet §3.1. BUILD compares it byte-for-byte with the
  pinned .pg/.start files, when given.
- The IDEAL run is MY implementation of packet §2: X-chains, Fact X order, availability, level-by-level keys, opt/stuck.
- The state loop is SPEC S1-S5 on si.py's Engine (the fleet's reference S1, read-only), as in my R2-N5-DUAL Runner. It records S4a's
  sigma_new BEFORE S4c, so the stop transition L+1 can be checked.
Genome JSON (R178 format): N, lev[x], opts[x][k] = [wt, xt, b] (wt / xt = -1 for none / X), gate[x][k], br[b], bp[b], start[x].
Checks at every state j = 0..L and at transition L+1 (each count must be 0):
  BUILD  my build equals the pin bytes (.pg, .start)        SIZE  n = N+3M+6, edges <= 6M+10, max Omega <= 4M+9
  STD    state j = standard state (sigma^{s_j}, tau_0)     FB    transitions 1..L: no fallback, tau kept, sigma changed, W kept; L+1 fallback
  SBAR   sbar = beta at every gate and K2 -> K1          PLAY  Xi(g) = (K1, B(g)+{K0,K3}, .); Xi(e_g): lev 0 (c_W, 0, 1), lev>=1 K1 with e_g in P
  KA     Xi on K = Lemma K (a) exactly                     KB    I_sigma restricted to K = {(K0, K1)}
  TAU    I_tau is empty                                     KC    Xi_tau(K1) reward >= reward(K0)
  ESC    sigma_new = sigma on beta and K (j <= L)       W1    W = Lemma W (i) formulas; W_j = W_0
  W2     W' := play value of (sigma_new, tau_0) = (c_W, 0, 3l+2) at gates and (c_W, 0, 3l+3) at movers
  TIE    every y in R(x) is fully W'-optimal and no corner     FX    Fact X: B_s(x,k) != B_s(x,k') for all k != k'
  AV     R(x) = gates of A_s(x)                             KEYB  for every pair in R(x): kappa order under (sigma_new, tau_0) = IDEAL key order under s_{j+1}
  RULE   sigma_new(x) = the kappa-least gate of R(x)          IDEAL sigma_new at movers = s_{j+1} (j < L), = s_L (j = L)
Controls: MUT=noesc (Remark of Lemma TAU: expect TAU violations), MUT=eorder (expect IDEAL/KEYB violations, RULE still 0),
  MUT=eprio (the line's looser e-priority description: any even priorities above every beta; expect 0).
BF=m: at states of genomes with M <= m, Xi = pointwise min over ALL positional Odd strategies and rho is the UNIQUE optimum.
Usage: realize_check.py GENOME.json [PIN_PREFIX] ...   |   perturb COUNT SEED GENOME.json ...   |   random COUNT N_MAX D SEED [cyc]
   cyc: random genomes with ANY Xi-graph (scope control: mismatches are expected and counted, not violations)."""
import sys, os, json, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
for p in ("experiments/si", "experiments/harness"): sys.path.insert(0, os.path.join(ROOT, p))
import pg
from si import Engine

def dual(h): return pg.Game([p + 1 for p in h.prio], [1 - o for o in h.owner], [list(s) for s in h.succ])

class St:
    def __init__(s): s.c = {}; s.ex = {}
    def inc(s, k, v=1): s.c[k] = s.c.get(k, 0) + v
    def bad(s, k, msg):
        s.inc("VIOL_" + k)
        if k not in s.ex: s.ex[k] = msg

# ---------------- builder (packet §3.1) ----------------
MUT = os.environ.get("MUT", ""); BF = int(os.environ.get("BF", "0"))   # controls: noesc (drop beta -> u), eorder (e indices by reversed gate order)

def build(G, esc=None):
    if esc is None: esc = MUT != "noesc"
    N, lev, opts, gate, br, bp = G["N"], G["lev"], G["opts"], G["gate"], G["br"], G["bp"]
    faces = [(x, k) for x in range(N) for k in range(len(opts[x]))]; M = len(faces)
    gv = {f: N + gate[f[0]][f[1]] for f in faces}
    bv = {f: N + M + i for i, f in enumerate(faces[::-1] if MUT == "border" else faces)}   # MUT=border: beta indices reversed (L-1 leaves the beta order to §3.1)
    byg = sorted(faces, key=lambda f: gate[f[0]][f[1]], reverse=(MUT == "eorder"))
    ev = {f: N + 2 * M + i for i, f in enumerate(byg)}
    cX, cW = N + 3 * M, N + 3 * M + 1; K = [N + 3 * M + 2 + i for i in range(4)]; n = N + 3 * M + 6
    prio, own, succ = [0] * n, [0] * n, [None] * n
    for f in faces:
        x, k = f; wt, xt, b = opts[x][k]
        prio[gv[f]] = 1; own[gv[f]] = 1; succ[gv[f]] = sorted([ev[f], bv[f]])
        prio[bv[f]] = 6 + 2 * br[b] + bp[b]
        succ[bv[f]] = sorted([xt, K[0]]) if (xt >= 0 and esc) else ([xt] if xt >= 0 else [K[0]])
        succ[ev[f]] = [wt if wt >= 0 else cW]
    for x in range(N): succ[x] = sorted(gv[(x, k)] for k in range(len(opts[x])))
    bmax = max(prio[bv[f]] for f in faces); eb = bmax + 1 if (bmax + 1) % 2 == 0 else bmax + 2
    for i, f in enumerate(sorted(faces, key=lambda f: (lev[f[0]], gate[f[0]][f[1]]))): prio[ev[f]] = eb + 2 * i
    if MUT == "eprio":   # the line's looser form: ANY even priorities above every beta (here random, repeats allowed)
        rr = random.Random(sum(gate[0]) + N)
        for f in faces: prio[ev[f]] = eb + 2 * rr.randrange(M)
    prio[cX] = 2; succ[cX] = [cX]
    top = 2 + max(prio); top += top % 2; prio[cW] = top; succ[cW] = [cW]
    K0, K1, K2, K3 = K
    prio[K0], prio[K1], prio[K2], prio[K3] = top + 2, 5, 3, top + 3; own[K2] = 1
    succ[K0], succ[K1], succ[K2], succ[K3] = [K1, K3], [K0, K1], [K1, K2], [K1, K2]
    g = pg.Game(prio, own, succ)
    sig = [-1] * n; tau = [-1] * n
    for v in range(n):
        if own[v] == 0: sig[v] = succ[v][0]
        else: tau[v] = succ[v][0]
    for f in faces:
        if opts[f[0]][f[1]][1] >= 0: sig[bv[f]] = opts[f[0]][f[1]][1]
        tau[gv[f]] = ev[f]
    sig[K0], sig[K1], sig[K3] = K3, K1, K2; tau[K2] = K2
    for x in range(N): sig[x] = gv[(x, G["start"][x])]
    return g, sig, tau, dict(faces=faces, gv=gv, bv=bv, ev=ev, cX=cX, cW=cW, K=K, M=M)

def dumps(g, sig, tau):
    pgt = f"parity {g.n - 1};\n" + "".join(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n" for v in range(g.n))
    st = ("SIGMA0 " + " ".join(f"{v}:{sig[v]}" for v in range(g.n) if g.owner[v] == 0) + "\n" +
          "TAU0 " + " ".join(f"{v}:{tau[v]}" for v in range(g.n) if g.owner[v] == 1) + "\n")
    return pgt, st

# ---------------- IDEAL (packet §2) ----------------
def chain(G, s, x, k):
    out = []; seen = set()
    while True:
        if (x, k) in seen: return None   # Xi-cycle: chain infinite
        seen.add((x, k)); out.append(G["opts"][x][k][2]); xt = G["opts"][x][k][1]
        if xt < 0: return frozenset(out)
        x, k = xt, s[xt]

def better(G, A, B):
    """IDEAL: option with beta-set A strictly better for Even than option with set B (Fact X form)."""
    D = A ^ B
    if not D: return False
    t = max(D, key=lambda b: G["br"][b])
    return (G["bp"][t] == 0) == (t in A)

def ideal_run(G, cap=100000):
    N, lev, opts = G["N"], G["lev"], G["opts"]
    s = list(G["start"]); states = [tuple(s)]; avail = []
    while len(states) <= cap:
        A = []
        for x in range(N):
            cur = chain(G, s, x, s[x]); a = {s[x]}
            for k in range(len(opts[x])):
                if k != s[x]:
                    ck = chain(G, s, x, k)
                    if cur is None or ck is None: return None, None, "cyclic"
                    if better(G, ck, cur): a.add(k)
            A.append(a)
        avail.append(A)
        if all(len(a) == 1 for a in A): return states, avail, "opt"
        ns = list(s); key = {}
        for l in sorted(set(lev)):
            for x in range(N):
                if lev[x] != l: continue
                def kk(k):
                    wt = opts[x][k][0]; gi = (G["gate"][x][k],)
                    return gi if wt < 0 else key[wt] + gi
                ns[x] = min(A[x], key=kk); key[x] = kk(ns[x])
        if ns == s: return states, avail, "stuck"
        s = ns; states.append(tuple(s))
    return states, avail, "cap"

def ideal_keys(G, s):
    N, lev, opts = G["N"], G["lev"], G["opts"]; key = {}
    for l in sorted(set(lev)):
        for x in range(N):
            if lev[x] == l:
                for k in range(len(opts[x])):
                    wt = opts[x][k][0]; key[(x, k)] = (G["gate"][x][k],) if wt < 0 else key[(wt, s[wt])] + (G["gate"][x][k],)
    return key

# ---------------- N5 (SPEC S1-S5) with sigma_new recorded ----------------
def pval(E, nx, v):
    seen, path, x = {}, [], v
    while x not in seen: seen[x] = len(path); path.append(x); x = nx[x]
    j = seen[x]; c = max(path[j:], key=lambda y: E.pp[y]); i = path.index(c); m = 0
    for y in path[:i]:
        if E.rank[y] > E.rank[c]: m |= E.bit[y]
    return (c, m, i), path

def step(g, E, Ed, sg, tu):
    n = g.n
    vs, sb = E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
    Is = E.improving(tuple(sg), vs)
    vt, tb = Ed.evaluate(tuple(tu[v] if g.owner[v] == 1 else -1 for v in range(n)))
    It = Ed.improving(tuple(tu), vt)
    info = dict(xi=vs, sbar=sb, Is=Is, xt=vt, It=It)
    if not Is and not It: return None, info
    ns, nt = list(sg), list(tu)
    if Is:
        opt = {v: {sg[v]} for v in range(n) if g.owner[v] == 0}
        for v, w in Is: opt[v].add(w)
        succ = [sorted(opt[v]) if g.owner[v] == 0 else [tu[v]] for v in range(n)]
        _, best = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ))).evaluate(tuple(tu[v] if g.owner[v] == 1 else -1 for v in range(n)))
        for v in range(n):
            if g.owner[v] == 0: ns[v] = best[v]
        info["R"] = opt
    if It:
        opt = {v: {tu[v]} for v in range(n) if g.owner[v] == 1}
        for v, w in It: opt[v].add(w)
        succ = [sorted(opt[v]) if g.owner[v] == 1 else [sg[v]] for v in range(n)]
        _, best = Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
        for v in range(n):
            if g.owner[v] == 1: nt[v] = best[v]
    info["snew"], info["tnew"] = list(ns), list(nt)
    fb = 0
    if ns == list(sg) and nt == list(tu):
        fb = 1
        if Is:
            for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
        else:
            for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
    info["fb"] = fb
    return (ns, nt), info

# ---------------- the check ----------------
def check(G, st, name, pin=None, scope=False):
    N, lev, opts = G["N"], G["lev"], G["opts"]
    g, sig0, tau0, D = build(G)
    faces, gv, bv, ev, cW, K, M = D["faces"], D["gv"], D["bv"], D["ev"], D["cW"], D["K"], D["M"]
    K0, K1, K2, K3 = K; n = g.n
    st.inc("games")
    if pin:
        a, b = dumps(g, sig0, tau0)
        if open(pin + ".pg").read() != a: st.bad("BUILD", name + " .pg")
        if open(pin + ".start").read() != b: st.bad("BUILD", name + " .start")
        st.inc("pins_compared")
    if n != N + 3 * M + 6 or sum(len(s) for s in g.succ) > 6 * M + 10 or max(g.prio) > 4 * M + 9: st.bad("SIZE", name)
    states, avail, how = ideal_run(G) if acyclic(G) else (None, None, "cyclic")
    if states is None:
        st.inc("IDEAL_cyclic_genomes")
        if not scope: st.bad("ACYC", name)
        # scope control: does the real run follow the IDEAL-style beta reply at all?  count first-state sbar mismatch
        E = Engine(g); vs, sb = E.evaluate(tuple(sig0[v] if g.owner[v] == 0 else -1 for v in range(n)))
        if any(sb[gv[f]] != bv[f] for f in faces): st.inc("SCOPE_cyclic_sbar_not_beta_at_state0")
        Ed = Engine(dual(g)); vt, _ = Ed.evaluate(tuple(tau0[v] if g.owner[v] == 1 else -1 for v in range(n)))
        if Ed.improving(tuple(tau0), vt): st.inc("SCOPE_cyclic_Itau_nonempty_at_state0")
        return
    L = len(states) - 1; st.inc("IDEAL_steps", L); st.inc("IDEAL_" + how)
    if L == 0: st.inc("BND_L0_games")
    if G["N"] == 1: st.inc("BND_N1_games")
    E, Ed = Engine(g), Engine(dual(g))
    Ev = [g.owner[v] == 0 for v in range(n)]
    def W_of(sg, tu): return [pval(E, [sg[v] if Ev[v] else tu[v] for v in range(n)], v)[0] for v in range(n)]
    sg, tu = list(sig0), list(tau0); W0 = W_of(sg, tu)
    def lemma_W1(W):
        for x in range(N):
            if W[x] != (cW, 0, 3 * lev[x] + 3): return False
        for f in faces:
            l = lev[f[0]]
            if W[gv[f]] != (cW, 0, 3 * l + 2) or W[ev[f]] != (cW, 0, 3 * l + 1): return False
            xt = opts[f[0]][f[1]][1]
            if xt >= 0 and W[bv[f]] != (cW, 0, 3 * lev[xt] + 4): return False
        return True
    if not lemma_W1(W0): st.bad("W1", name + "@0")
    for j in range(L + 1):
        s = states[j]
        std = list(sig0)
        for x in range(N): std[x] = gv[(x, s[x])]
        if [sg[v] for v in range(n) if Ev[v]] != [std[v] for v in range(n) if Ev[v]] or tu != tau0:
            st.bad("STD", f"{name}@{j}"); return
        nxt, info = step(g, E, Ed, sg, tu)
        if nxt is None: st.bad("FB", f"{name}@{j} N5 stopped"); return
        xi, sb = info["xi"], info["sbar"]
        if BF and M <= BF:   # P1 probe, independent of si.py: every positional Odd strategy (gates x K2)
            import itertools
            odd = [gv[f] for f in faces] + [K2]; best = None; cnt = 0; nxs = [sg[v] if Ev[v] else -1 for v in range(n)]
            vals = []
            for ch in itertools.product(*[g.succ[o] for o in odd]):
                for o, w in zip(odd, ch): nxs[o] = w
                vals.append((ch, [pval(E, nxs, v)[0] for v in range(n)]))
            mn = [min((vv[v] for _, vv in vals), key=E.key) for v in range(n)]
            if [tuple(z) for z in xi] != mn: st.bad("BF", f"{name}@{j} Xi != pointwise min")
            opt = [ch for ch, vv in vals if vv == mn]
            if opt != [tuple(bv[f] for f in faces) + (K1,)]: st.bad("BF", f"{name}@{j} optimum not unique rho")
            st.inc("BF_states"); st.inc("BF_strategies", len(vals))
        # SBAR
        if any(sb[gv[f]] != bv[f] for f in faces) or sb[K2] != K1: st.bad("SBAR", f"{name}@{j}")
        # PLAY at gates and e
        for f in faces:
            x, k = f; Bs = chain(G, s, x, k)
            want = sum(E.bit[bv[(y, kk)]] for (y, kk) in faces if opts[y][kk][2] in Bs) | E.bit[K0] | E.bit[K3]
            if xi[gv[f]][0] != K1 or xi[gv[f]][1] != want: st.bad("PLAY", f"{name}@{j} gate {f}")
            if lev[x] == 0:
                if tuple(xi[ev[f]]) != (cW, 0, 1): st.bad("PLAY", f"{name}@{j} e lev0 {f}")
            elif xi[ev[f]][0] != K1 or not (xi[ev[f]][1] & E.bit[ev[f]]): st.bad("PLAY", f"{name}@{j} e {f}")
        # K (a), (b)
        ka = {K1: (K1, 0, 0), K2: (K1, 0, 1), K3: (K1, E.bit[K3], 2), K0: (K1, E.bit[K0] | E.bit[K3], 3)}
        if any(tuple(xi[v]) != ka[v] for v in ka): st.bad("KA", f"{name}@{j}")
        if {(v, w) for (v, w) in info["Is"] if v in K} != {(K0, K1)}: st.bad("KB", f"{name}@{j}")
        # TAU, K (c)
        if info["It"]: st.bad("TAU", f"{name}@{j} {info['It'][:3]}")
        if E.rew[info["xt"][K1][0]] < E.rew[K0]: st.bad("KC", f"{name}@{j}")
        # Fact X, AV
        for x in range(N):
            for k in range(len(opts[x])):
                for k2 in range(k + 1, len(opts[x])):
                    if chain(G, s, x, k) == chain(G, s, x, k2): st.bad("FX", f"{name}@{j} x={x}")
            Rx = {w for (v, w) in info["Is"] if v == x} | {sg[x]}
            if Rx != {gv[(x, k)] for k in avail[j][x]}: st.bad("AV", f"{name}@{j} x={x}")
        snew = info["snew"]; R = info["R"]
        # ESC
        for f in faces:
            if snew[bv[f]] != sg[bv[f]]: st.bad("ESC", f"{name}@{j} beta {f}")
        if any(snew[v] != sg[v] for v in (K0, K1, K3)): st.bad("ESC", f"{name}@{j} K")
        # W', TIE, KEY (b), RULE, IDEAL choice
        nx = [snew[v] if Ev[v] else tu[v] for v in range(n)]
        Wp = {}; pth = {}
        for v in range(n): Wp[v], pth[v] = pval(E, nx, v)
        for x in range(N):
            if Wp[x] != (cW, 0, 3 * lev[x] + 3): st.bad("W2", f"{name}@{j} x={x}")
            for y in R[x]:
                if Wp[y] != (cW, 0, 3 * lev[x] + 2): st.bad("W2", f"{name}@{j} y={y}")
                if E.extend(x, Wp[y]) != Wp[x] or x in pth[y][:pth[y].index(cW)]: st.bad("TIE", f"{name}@{j} x={x} y={y}")
        sn = states[j + 1] if j < L else states[L]
        ik = ideal_keys(G, sn)
        for x in range(N):
            def kap(y): p = pth[y]; return tuple(reversed(p[:p.index(cW)]))
            Rl = sorted(R[x]); fk = {gv[(x, k)]: k for k in range(len(opts[x]))}
            for a in Rl:
                for b in Rl:
                    if a < b and ((kap(a) < kap(b)) != (ik[(x, fk[a])] < ik[(x, fk[b])])): st.bad("KEYB", f"{name}@{j} x={x}")
            if snew[x] != min(Rl, key=kap): st.bad("RULE", f"{name}@{j} x={x}")
            if snew[x] != gv[(x, sn[x])]: st.bad("IDEAL", f"{name}@{j} x={x}")
            st.inc("mover_checks"); st.inc("mover_checks_multi" if len(Rl) > 1 else "mover_checks_single")
        # transition j+1
        nsg, ntu = nxt
        if j < L:
            if info["fb"] or ntu != tu or nsg == sg: st.bad("FB", f"{name}@{j+1}")
            if W_of(nsg, ntu) != W0: st.bad("W1", f"{name}@{j+1} W changed")
        else:
            if not info["fb"]: st.bad("FB", f"{name}@{L+1} no fallback")
            st.inc("stop_fallbacks")
        sg, tu = nsg, ntu
        st.inc("states")

def rand_genome(rng, Nmax, dmax, acyclic=True, upward=True):
    d = rng.randint(1, dmax); N = rng.randint(max(1, d), max(d, Nmax))
    lev = [i % d for i in range(N)] if N >= d else [0] * N
    rng.shuffle(lev)
    if 0 not in lev: lev[0] = 0
    lev = [min(l, max(lev)) for l in lev]
    # graded: each level >= 1 needs a mover one level down
    levels = sorted(set(lev)); fix = {l: i for i, l in enumerate(levels)}; lev = [fix[l] for l in lev]
    order = list(range(N)); rng.shuffle(order); pos = {x: i for i, x in enumerate(order)}   # Xi-edges go to LATER movers (acyclic)
    opts = []; M = 0
    for x in range(N):
        deg = rng.choice([1, 2, 2, 3, 3, 4]); o = []
        for k in range(deg):
            wt = -1 if lev[x] == 0 else rng.choice([y for y in range(N) if lev[y] == lev[x] - 1])
            if acyclic: cand = [y for y in range(N) if pos[y] > pos[x]]
            else: cand = list(range(N))
            if not upward: cand = [y for y in cand if lev[y] <= lev[x]]
            xt = rng.choice(cand) if cand and rng.random() < 0.75 else -1
            o.append([wt, xt, M]); M += 1
        opts.append(o)
    bids = list(range(M)); rng.shuffle(bids)
    for o in opts:
        for f in o: f[2] = bids.pop()
    gperm = list(range(M)); rng.shuffle(gperm); it = iter(gperm)
    gate = [[next(it) for _ in o] for o in opts]
    br = list(range(M)); rng.shuffle(br); bp = [rng.randint(0, 1) for _ in range(M)]
    start = [rng.randrange(len(o)) for o in opts]
    return dict(N=N, lev=lev, opts=opts, gate=gate, br=br, bp=bp, start=start)

def acyclic(G):
    N = G["N"]; adj = [{f[1] for f in G["opts"][x] if f[1] >= 0} for x in range(N)]; col = [0] * N
    def dfs(x):
        col[x] = 1
        for y in adj[x]:
            if col[y] == 1 or (col[y] == 0 and not dfs(y)): return False
        col[x] = 2; return True
    return all(col[x] or dfs(x) for x in range(N))

def perturb(G, rng):
    H = json.loads(json.dumps(G)); N = H["N"]; M = sum(len(o) for o in H["opts"])
    for _ in range(rng.randint(1, 6)):
        r = rng.randrange(5); x = rng.randrange(N); k = rng.randrange(len(H["opts"][x]))
        if r == 0: H["opts"][x][k][1] = rng.choice([-1] + list(range(N)))
        elif r == 1:
            b1, b2 = rng.randrange(M), rng.randrange(M); H["br"][b1], H["br"][b2] = H["br"][b2], H["br"][b1]
        elif r == 2: b = rng.randrange(M); H["bp"][b] ^= 1
        elif r == 3:
            y = rng.randrange(N); k2 = rng.randrange(len(H["opts"][y])); H["gate"][x][k], H["gate"][y][k2] = H["gate"][y][k2], H["gate"][x][k]
        else: H["start"][x] = rng.randrange(len(H["opts"][x]))
    return H

def main():
    st = St(); a = sys.argv[1:]
    if a and a[0] == "perturb":
        cnt, seed = int(a[1]), int(a[2]); rng = random.Random(seed); base = [json.load(open(f)) for f in a[3:]]; done = 0; tries = 0
        while done < cnt and tries < 100 * cnt:
            tries += 1; H = perturb(rng.choice(base), rng)
            if acyclic(H): check(H, st, f"pert{seed}_{done}"); done += 1
        st.inc("perturb_tries", tries)
    elif a and a[0] == "random":
        cnt, Nmax, dmax, seed = map(int, a[1:5]); cyc = len(a) > 5 and a[5] == "cyc"; rng = random.Random(seed)
        for i in range(cnt): check(rand_genome(rng, Nmax, dmax, acyclic=not cyc), st, f"rand{seed}_{i}", scope=cyc)
    else:
        i = 0
        while i < len(a):
            G = json.load(open(a[i])); pin = None
            if i + 1 < len(a) and not a[i + 1].endswith(".json"): pin = a[i + 1]; i += 1
            check(G, st, os.path.basename(a[i] if not pin else a[i - 1]), pin); i += 1
    viol = {k: v for k, v in st.c.items() if k.startswith("VIOL_")}
    print("REALIZE-CHECK", " ".join(f"{k} {v}" for k, v in sorted(st.c.items()) if not k.startswith("VIOL_")))
    print("VIOLATIONS", sum(viol.values()), " ".join(f"{k[5:]} {v}" for k, v in sorted(viol.items())))
    for k, m in st.ex.items(): print("  first", k, m)

if __name__ == "__main__":
    main()
