#!/usr/bin/env python3
"""L-RED 69 R241: attack on L-NEW box 213 KEY-TAU (i), (ii), (iii) (claude/l-new 14340979, docs/new/N5-KEYWIN-box213.md §3) and box 215
KEYSIDE-ALL (claude/l-new cd4f7f4d, docs/new/N5-KEYSIDE-box215.md §2) with L-RED's OWN engine: n5s237.py (SPEC-exact N5, L-RED 67, written
from the SPEC text), run from S3 on Γ3(G) to its first fallback. Box 213 / 215 tools were NOT read before the verdict (R241 rule).
Objects borrowed (OBJECTS only): box 189 gamma3.build(G, all pads) (claude/l-new fcba92fc; env LNEW), as in L-RED R239's imp239.py.
What is L-RED's own: the run (n5s237), the keys (computed by a level-order DP over the genome's W-graph, NOT by S1's BFS), the plays
(followed vertex by vertex in the game graph under (σ_t, τ_t)), every counter, the controls and the second-engine replay.

Definitions used (read from box 213 §3 / box 215 §1-§2; e-index = the Γ3 vertex index of e_(x,k); gate index g(x,k) from the genome):
  A_t(x) = {σ_t(x)} ∪ Iσ_t(x) (pads m_(x,k)), Iσ from Ξσ_t = n5s237.vjproc on G_σt (SPEC S2);
  ekey_t(y, k) = ekey-prefix of wt(y,k) + (e-index of e_(y,k)), root-first; κ_t(y) = min over k ∈ A_t(y) of κ-prefix(wt) + (e(y,k),);
  μ_t(x) = the e-indices met on x's play under (σ_t, τ_t), read from the cycle end (root-first); the play must end in c_W's self-loop;
  key_s(x, k) (box 215, P-IDEAL-KEYS) = key_s(wt, s(wt)) + (g(x,k),); KP_s(x) = argmin_k key_s(x, k) over ALL options of x.
Must-0 counters (unit: one (state, mover) unless said):
  std     state t <= F1-1 with σ_t ≠ σ_0 off the movers                                                   ([STD], box 213 §1)
  tau3    state t <= F1-1 with τ_t ≠ TAU3 (pe at every gate, K2 -> K2)                                     (box 213 (K2))
  w3      option pad m_(x,k) of a level-ℓ mover whose S4a-arena value is not (c_W, ∅, 5ℓ+4), or a mover that is its own arena
          cycle node (R125 W3-ALL, as box 213 uses it); arena = SPEC S4a's H (Even keeps A_t, Odd keeps τ_t), S1 on the dual
  lenvar  mover with two τ-paths of different lengths in the W-graph (static)
  kp      transition t -> t+1 <= F1-1 (non-fallback): σ_(t+1)(x) ≠ the option of A_t(x) with the least ekey (κ DP)      KEY-TAU (i)
  kpf     the fallback state F1-1: the κ-DP choice ≠ σ_(F1-1)(x) (S4a returned σ itself there)                      KEY-TAU (i) at F1
  kpa     any state t <= F1-1: S4a's arena choice (vjproc on the dual of H, before S4c) ≠ the κ-DP choice                KEY-TAU (i) direct
  unreach x's play under (σ_t, τ_t) does not end in c_W's self-loop
  mukappa μ_(t+1)(x) ≠ κ_t(x); muinc μ_(t+1)(x) > μ_t(x); muflat σ_(t+1)(x) ≠ σ_t(x) and μ_(t+1)(x) = μ_t(x)       KEY-TAU (ii)
  mulen   two keys of one mover compared with different lengths
  kviol   (per mover) switches(x) > |K(x)| - 1, |K(x)| = number of τ-paths of x in the W-graph                      KEY-TAU (iii)
  nomove  non-fallback transition that switches no mover                                                         [NE]
  eord    (static) e-index order ≠ gate-index order on the options (box 215 §1's identification)
  kpg     [M] in gate keys: s_(t+1)(x) ≠ argmin over A_t(x) of key_(s_(t+1))(x, ·)                                  box 215 [M]
  lkp     Mv_t ∩ W(x) = ∅ but some option's key_s changes or KP changes (W(x) = movers below x in the W-graph)      LOCAL-KP
  pkf     deg-2 mover, level >= 1, targets a ≠ b: KF_x ≠ flips(a, b); pkfa: targets a = b (or level 0): KF_x ≠ 0     PAIR-KF
  kflip   deg-2 mover moving at t with s_t(x) ≠ KP_(s_t)(x); kflipm: moves(x) > 1 + KF_x                            KEYFLIP′
  casc    a flip of a same-level pair (p, q) at step t with neither moving and NOT (l >= 1, w_p ≠ w_q, (w_p, w_q) flips at t)  CASCADE
  ftt     flips(p, q) > T (T = non-fallback steps)                                                                 F <= T
  ladder  on 𝓛^R_d-shaped genomes (movers 2l, 2l+1 at level l, degree 2, targets {2l-2, 2l-1}): F(0) > 2, F(l) > moves(2l) +
          moves(2l+1) + F(l-1), moves(x) > 1 + F(lev(x)-1), or F(l) > 3^(l+1) - 1                                LADDER
  *_e     the same nine box 215 counters with e-index keys instead of gate keys (the numbering-free form; = the gate form when
          e-order = gate order, i.e. eord 0)
Descriptive: T (non-fallback steps), switches, nlk (moves to a non-global-least key option: σ_(t+1)(x) ≠ KP_(s_(t+1))(x)), maxsw, maxK,
  xicyc (genome has a Ξ-cycle), essential-Ξ statistics are NOT computed here.
Controls (must fire): KT_MODE=xi (N5′-xi, Howard's tie rule): kp / kflip; KT_CTRL=1: κ DP takes the MOST key (kp fires);
  KT_CTRL=2: μ read leaf-first instead of root-first (muinc / mukappa fire); KT_CTRL=3: gate keys with gate indices permuted (kpg / kflip fire).
Second engine (env SECOND=1: every genome; XEVERY=k: every k-th generated genome; json mode: always): box 190's n5v mode spec from box 21's S3 pair, σ compared state by state to F1 (xdiff).
Scope check (not a control): KT_PERM=e|all, KT_PSEED: Γ3 renumbered (isomorphic copy); keys still read as the e-vertices' (new) indices.
Usage: kt241.py json FILE.json ... | kt241.py gen MODE SEED COUNT | kt241.py ladder SEED COUNT DMAX | kt241.py rand SEED COUNT NMAX DMAX DEGMAX [XRATE]   (env LNEW; LRED unset)"""
import sys, os, json, random, time, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); LNEW = os.environ["LNEW"]
sys.path[:0] = [HERE, os.path.join(HERE, "..", "r237")] + [os.path.join(LNEW, p) for p in ("experiments/new/box195", "experiments/new/box190", "experiments/new/box189", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
import n5s237 as S
import gamma3
PADS = {"K", "pe", "pb", "m"}
MODE = os.environ.get("KT_MODE", "spec"); CTRL = int(os.environ.get("KT_CTRL", "0"))
PERM = os.environ.get("KT_PERM", "none"); PSEED = int(os.environ.get("KT_PSEED", "1"))   # renumber Γ3: none | e (e-vertices among themselves) | all

class _G:
    def __init__(s, prio, owner, succ): s.prio, s.owner, s.succ, s.n = prio, owner, succ, len(prio)

def renumber(g, V, how, seed):
    """an isomorphic copy of Γ3 with vertex indices permuted (how = e: the e-vertices among themselves; all: every vertex)"""
    n = g.n; rr = random.Random(seed); pi = list(range(n))
    if how == "e":
        es = sorted(v for k, v in V.items() if isinstance(k, tuple) and k[0] == "e"); sh = es[:]; rr.shuffle(sh)
        for a, b in zip(es, sh): pi[a] = b
    elif how == "all": rr.shuffle(pi)
    prio = [0] * n; owner = [0] * n; succ = [None] * n
    for v in range(n): prio[pi[v]] = g.prio[v]; owner[pi[v]] = g.owner[v]; succ[pi[v]] = sorted(pi[w] for w in g.succ[v])
    return _G(prio, owner, succ), {k: pi[v] for k, v in V.items()}
KEYS = ("std", "tau3", "w3", "lenvar", "kp", "kpf", "kpa", "unreach", "mukappa", "muinc", "muflat", "mulen", "kviol", "nomove",
        "eord", "kpg", "lkp", "pkf", "pkfa", "kflip", "kflipm", "casc", "ftt", "ladder",
        "kpg_e", "lkp_e", "pkf_e", "pkfa_e", "kflip_e", "kflipm_e", "casc_e", "ftt_e", "ladder_e")
DESC = ("T", "switches", "nlk", "maxsw", "maxK", "ladders")

def ladder_shape(G):
    N, lev, opts = G["N"], G["lev"], G["opts"]
    if N < 2 or N % 2: return False
    for x in range(N):
        if lev[x] != x // 2 or len(opts[x]) != 2: return False
        l = lev[x]; ws = sorted(o[0] for o in opts[x])
        if l == 0 and ws != [-1, -1]: return False
        if l >= 1 and ws != [2 * l - 2, 2 * l - 1]: return False
    return True

def analyse(G, second=False):
    g, sig0, tau0, V = gamma3.build(G, PADS)
    if PERM != "none": g, V = renumber(g, V, PERM, PSEED)
    n = g.n; prio = list(g.prio); owner = list(g.owner); succ = [sorted(set(s)) for s in g.succ]
    N, lev, opts, gate = G["N"], G["lev"], G["opts"], G["gate"]
    order = sorted(range(n), key=lambda v: (prio[v], v)); rk = [0] * n
    for r, v in enumerate(order): rk[v] = r
    ev = [p % 2 == 0 for p in prio]; evd = [not e for e in ev]; O = S.Ord(rk, ev)
    isE = [o == 0 for o in owner]; isO = [o == 1 for o in owner]
    cW = V["cW"]; K2 = V[("K", 2)]; mvv = [V[("x", x)] for x in range(N)]; mvset = set(mvv)
    pad = {V[("m", (x, k))]: (x, k) for x in range(N) for k in range(len(opts[x]))}
    eid = {(x, k): V[("e", (x, k))] for x in range(N) for k in range(len(opts[x]))}
    eset = set(eid.values())
    gidx = {(x, k): gate[x][k] for x in range(N) for k in range(len(opts[x]))}
    if CTRL == 3:
        rr = random.Random(5); vals = list(gidx.values()); rr.shuffle(vals); gidx = dict(zip(gidx.keys(), vals))
    lorder = sorted(range(N), key=lambda x: (lev[x], x))
    c = {k: 0 for k in KEYS}; d = {k: 0 for k in DESC}
    # static: path counts, lengths, e/gate order
    npath = {}; lens = {}
    for x in lorder:
        npath[x] = 0; ls = set()
        for k, o in enumerate(opts[x]):
            wt = o[0]; npath[x] += npath[wt] if wt >= 0 else 1
            ls |= {l + 1 for l in lens[wt]} if wt >= 0 else {1}
        lens[x] = ls; c["lenvar"] += int(len(ls) > 1)
    qs = sorted(eid); c["eord"] = int(sorted(qs, key=lambda q: eid[q]) != sorted(qs, key=lambda q: gate[q[0]][q[1]]))
    d["maxK"] = max(npath.values())
    below = {}
    for x in lorder:
        b = set()
        for o in opts[x]:
            if o[0] >= 0: b |= {o[0]} | below[o[0]]
        below[x] = b
    # the run
    tr = []; fbt = []
    its, fbs, win, _, _ = S.run(prio, owner, succ, MODE, trace=tr, fbtrace=fbt)
    F1 = fbt[0] if fbt else len(tr)
    states = [tr[t] for t in range(min(F1, len(tr)))]                          # states 0..F1-1
    sopt = [tuple(pad[st[0][mvv[x]]][1] if st[0][mvv[x]] in pad else -1 for x in range(N)) for st in states]
    s0, t0 = states[0]
    tau_ok = all(t0[V[("g", q)]] == V[("pe", q)] for q in eid) and t0[K2] == K2
    def play_key(sg, tu, x):
        v = mvv[x]; seen = {}; es = []; path = []
        while v not in seen:
            seen[v] = len(path); path.append(v)
            if v in eset: es.append(v)
            v = sg[v] if isE[v] else tu[v]
        cyc = path[seen[v]:]
        ok = (cyc == [cW])
        return (tuple(es) if CTRL == 2 else tuple(reversed(es))), ok
    def kdp(choicesets, key_of):
        """level-order DP: for each mover, argmin over its allowed options of prefix(wt) + (key_of(x,k),)"""
        kap = {}; ch = {}
        for x in lorder:
            best = None
            for k in choicesets[x]:
                wt = opts[x][k][0]; kk = (kap[wt] if wt >= 0 else ()) + (key_of(x, k),)
                if best is None or ((kk > best[0]) if CTRL == 1 else (kk < best[0])): best = (kk, k)
            kap[x], ch[x] = best
        return kap, ch
    def keys_under(s, key_of):
        """box 215's key_s(x, k) for every option, and KP_s(x)"""
        own = {}; allk = {}; KP = {}
        for x in lorder:
            allk[x] = []
            for k, o in enumerate(opts[x]):
                wt = o[0]; allk[x].append((own[wt] if wt >= 0 else ()) + (key_of(x, k),))
            own[x] = allk[x][s[x]]; KP[x] = min(range(len(opts[x])), key=lambda k: allk[x][k])
        return own, allk, KP
    ekey = lambda x, k: eid[(x, k)]; gkey = lambda x, k: gidx[(x, k)]
    mu = []; kap = []; Aset = []
    for t, (sg, tu) in enumerate(states):
        c["std"] += int(any(sg[v] != s0[v] for v in sg if v not in mvset))
        c["tau3"] += int(tu != t0 or not tau_ok)
        vs, _ = S.vjproc(n, rk, ev, [[sg[v]] if isE[v] else succ[v] for v in range(n)], isO)
        Is = {v: [w for w in succ[v] if w != sg[v] and O.better(vs[w], vs[sg[v]])] for v in sg}
        A = {v: sorted({sg[v]} | set(Is[v])) for v in sg}
        Am = {x: sorted(pad[w][1] for w in A[mvv[x]]) for x in range(N)}; Aset.append(Am)
        W, ch = S.vjproc(n, rk, evd, [A[v] if isE[v] else [tu[v]] for v in range(n)], isE)   # SPEC S4a arena (dual of H)
        for x in range(N):
            c["w3"] += int(W[mvv[x]][0] == mvv[x])
            for k in range(len(opts[x])):
                c["w3"] += int(W[V[("m", (x, k))]] != (cW, frozenset(), 5 * lev[x] + 4))
        kp_t, chk = kdp(Am, ekey); kap.append(kp_t)
        for x in range(N):
            c["kpa"] += int(pad.get(ch[mvv[x]], (None, None))[1] != chk[x])
        mk = {}
        for x in range(N):
            mk[x], ok = play_key(sg, tu, x); c["unreach"] += int(not ok)
        mu.append(mk)
        if t == F1 - 1 and fbt:
            c["kpf"] += sum(int(chk[x] != sopt[t][x]) for x in range(N))
    T = len(states) - 1; d["T"] = T
    sw = [0] * N
    for t in range(T):
        mv = [x for x in range(N) if sopt[t + 1][x] != sopt[t][x]]
        c["nomove"] += int(not mv); d["switches"] += len(mv)
        _, chk = kdp(Aset[t], ekey)
        for x in range(N):
            c["kp"] += int(sopt[t + 1][x] != chk[x])
            a, b, kk = mu[t + 1][x], mu[t][x], kap[t][x]
            c["mulen"] += int(len(a) != len(b) or len(a) != len(kk))
            c["mukappa"] += int(a != kk); c["muinc"] += int(a > b); c["muflat"] += int(x in mv and a == b)
        for x in mv: sw[x] += 1
    c["kviol"] = sum(int(sw[x] > npath[x] - 1) for x in range(N)); d["maxsw"] = max(sw) if sw else 0
    # box 215 ([M] and the key-side lemmas), once with gate keys (box 215 as stated, sfx "") and once with e-index keys (sfx "_e")
    bylev = {}
    for x in range(N): bylev.setdefault(lev[x], []).append(x)
    def side(key_of, sfx):
        KS = [keys_under(s, key_of) for s in sopt]
        for t in range(T):
            own1, allk1, KP1 = KS[t + 1]
            for x in range(N):
                ak = [k for k in Aset[t][x]]
                c["kpg" + sfx] += int(sopt[t + 1][x] != min(ak, key=lambda k: allk1[x][k]))
                if not sfx: d["nlk"] += int(sopt[t + 1][x] != sopt[t][x] and sopt[t + 1][x] != KP1[x])
        KF = [0] * N; moves = [0] * N
        for t in range(1, T + 1):
            own0, allk0, KP0 = KS[t - 1]; own1, allk1, KP1 = KS[t]; Mv = {x for x in range(N) if sopt[t][x] != sopt[t - 1][x]}
            for x in range(N):
                KF[x] += int(KP1[x] != KP0[x]); moves[x] += int(x in Mv)
                if not (Mv & below[x]): c["lkp" + sfx] += int(allk1[x] != allk0[x] or KP1[x] != KP0[x])
                if len(opts[x]) == 2 and x in Mv: c["kflip" + sfx] += int(sopt[t][x] != KP1[x])
        def flips(p, q):
            f = 0; at = []
            for t in range(1, T + 1):
                if (KS[t][0][p] < KS[t][0][q]) != (KS[t - 1][0][p] < KS[t - 1][0][q]): f += 1; at.append(t)
            return f, at
        fl = {}
        for l, xs in bylev.items():
            for p, q in itertools.combinations(xs, 2):
                fl[(p, q)] = fl[(q, p)] = flips(p, q)
        for x in range(N):
            if len(opts[x]) == 2:
                a, b = opts[x][0][0], opts[x][1][0]
                if a == b or lev[x] == 0: c["pkfa" + sfx] += int(KF[x] != 0)
                else: c["pkf" + sfx] += int(KF[x] != fl[(a, b)][0])
                c["kflipm" + sfx] += int(moves[x] > 1 + KF[x])
        for l, xs in bylev.items():
            for p, q in itertools.combinations(xs, 2):
                f, at = fl[(p, q)]; c["ftt" + sfx] += int(f > T)
                for t in at:
                    if sopt[t][p] != sopt[t - 1][p] or sopt[t][q] != sopt[t - 1][q]: continue
                    wp, wq = opts[p][sopt[t][p]][0], opts[q][sopt[t][q]][0]
                    ok = l >= 1 and wp != wq and t in fl[(wp, wq)][1]
                    c["casc" + sfx] += int(not ok)
        if ladder_shape(G):
            d["ladders"] = 1 if not sfx else d["ladders"]; L = max(lev) + 1; F = [fl[(2 * l, 2 * l + 1)][0] for l in range(L)]
            c["ladder" + sfx] += int(F[0] > 2)
            for l in range(1, L):
                c["ladder" + sfx] += int(F[l] > moves[2 * l] + moves[2 * l + 1] + F[l - 1]) + int(F[l] > 3 ** (l + 1) - 1)
                for x in (2 * l, 2 * l + 1): c["ladder" + sfx] += int(moves[x] > 1 + F[l - 1])
        return KF, moves
    side(ekey, "_e"); KF, moves = side(gkey, "")
    xd = None
    if second: xd = second_engine(g, [st[0] for st in states], F1)
    xc = xi_cyc_opts(G); allopt = {x: list(range(len(opts[x]))) for x in range(N)}; kglob, _ = kdp(allopt, ekey)
    slack = sum(moves[x] - KF[x] for x in range(N) if len(opts[x]) == 2)
    cyc = sum(int((x, sopt[t][x]) in xc) for t in range(len(sopt)) for x in range(N))
    muroom = sum(int(mu[t][x] != kglob[x]) for t in range(len(mu)) for x in range(N))
    return c, d, dict(F1=F1, its=its, fbs=fbs, n=n, N=N, xd=xd, slack=slack, cyc=cyc, muroom=muroom, xicyc=int(bool(xc)))

def xi_cyc_opts(G):
    """options whose Ξ-edge x -> xt lies on a Ξ-cycle (xt a mover that reaches x in the Ξ-graph; self-loops included); L-COMP's cycopt"""
    N = G["N"]; adj = [set(o[1] for o in G["opts"][x] if o[1] >= 0) for x in range(N)]; reach = []
    for s0 in range(N):
        seen = {s0}; st = [s0]
        while st:
            v = st.pop()
            for w in adj[v]:
                if w not in seen: seen.add(w); st.append(w)
        reach.append(seen)
    return {(x, k) for x in range(N) for k, o in enumerate(G["opts"][x]) if o[1] >= 0 and x in reach[o[1]]}

def second_engine(g, sigmas, F1):
    import n5v, n5x, n5
    from si import Engine
    import eg195
    g2 = eg195.topg(g); E, Ed = Engine(g2), Engine(n5.dual(g2)); sigma, tau = n5x.start_pair(g2, E, Ed, None); xd = 0
    for t in range(len(sigmas)):
        xd |= int(any(sigma[v] != w for v, w in sigmas[t].items()))
        r = n5v.step(g2, E, Ed, sigma, tau, "spec")
        if r is None: break
        sigma, tau = r[0], r[1]
    return xd

def rand_genome(rng, nmax, dmax, degmax, xrate=0.15, selfl=0.0):
    N = rng.randint(2, nmax); D = rng.randint(1, min(dmax, N)); lev = list(range(D)) + [rng.randrange(D) for _ in range(N - D)]
    rng.shuffle(lev); by = {}
    for x in range(N): by.setdefault(lev[x], []).append(x)
    opts = []; i = 0
    for x in range(N):
        o = []
        for _ in range(rng.randint(1, degmax)):
            xt = x if rng.random() < selfl else (-1 if rng.random() < xrate else rng.randrange(N))
            o.append([rng.choice(by[lev[x] - 1]) if lev[x] else -1, xt, i]); i += 1
        opts.append(o)
    M = i; gp = list(range(M)); rng.shuffle(gp); it = iter(gp); gate = [[next(it) for _ in o] for o in opts]
    br = list(range(M)); rng.shuffle(br)
    return dict(N=N, lev=lev, opts=opts, gate=gate, br=br, bp=[rng.randint(0, 1) for _ in range(M)], start=[rng.randrange(len(o)) for o in opts])

def ladder_genome(rng, dmax, xrate=0.1, selfl=0.1):
    """𝓛^R_d-shaped genome (movers 2l, 2l+1 at level l, two options each, targets 2l-2 and 2l-1) with RANDOM Ξ-targets (cycles allowed),
    random gate order, β ranks / parities and start: the Ξ-cyclic ladders box 215 §4 says no generator in the tree produces"""
    d = rng.randint(1, dmax); N = 2 * d; lev = [x // 2 for x in range(N)]; opts = []; i = 0
    for x in range(N):
        l = lev[x]; wts = [-1, -1] if l == 0 else [2 * l - 2, 2 * l - 1]; rng.shuffle(wts); o = []
        for w in wts:
            r = rng.random(); xt = x if r < selfl else (-1 if r < selfl + xrate else rng.randrange(N))
            o.append([w, xt, i]); i += 1
        opts.append(o)
    M = i; gp = list(range(M)); rng.shuffle(gp); it = iter(gp); gate = [[next(it) for _ in o] for o in opts]
    br = list(range(M)); rng.shuffle(br)
    return dict(N=N, lev=lev, opts=opts, gate=gate, br=br, bp=[rng.randint(0, 1) for _ in range(M)], start=[rng.randrange(2) for _ in range(N)])

def load(fn):
    G = json.load(open(fn))
    if isinstance(G, dict) and "genome" in G: G = G["genome"]
    G = {k: v for k, v in G.items() if k in ("N", "lev", "opts", "gate", "br", "bp", "start")}
    return G

def fmt(c, d, info):
    return " ".join(f"{k} {c[k]}" for k in KEYS) + " | " + " ".join(f"{k} {d[k]}" for k in DESC) + f" | N {info['N']} n {info['n']} F1 {info['F1']} its {info['its']} fb {info['fbs']} xicyc {info['xicyc']} cycuse {info['cyc']} slack {info['slack']} muroom {info['muroom']}" + (f" xdiff {info['xd']}" if info['xd'] is not None else "")

if __name__ == "__main__":
    t0 = time.time(); sec = os.environ.get("SECOND", "0") == "1"; XEVERY = int(os.environ.get("XEVERY", "0"))
    tag = f"KT241 mode {MODE}" + (f" CTRL {CTRL}" if CTRL else "") + (f" PERM {PERM} {PSEED}" if PERM != "none" else "")
    tot = {k: 0 for k in KEYS}; dt = {k: 0 for k in DESC}; mx = {"T": 0, "maxsw": 0, "maxK": 0}; xs = xd = 0; first = None; cnt = 0
    if sys.argv[1] == "json":
        items = [(os.path.basename(f), load(f)) for f in sys.argv[2:]]
    elif sys.argv[1] == "gen":                                       # box 195's eg195.gen families (object): rand dense deep noesc esc acyc lvl0
        import eg195
        md, seed, k = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]); rng = random.Random(seed)
        items = ((f"{md}{seed}_{i}", eg195.gen(rng, md)) for i in range(k))
    elif sys.argv[1] == "ladder":
        seed, k, dmax = map(int, sys.argv[2:5]); rng = random.Random(seed)
        items = ((f"lad{seed}_{i}", ladder_genome(rng, dmax)) for i in range(k))
    else:
        seed, k, nmax, dmax, degmax = map(int, sys.argv[2:7]); xr = float(sys.argv[7]) if len(sys.argv) > 7 else 0.15
        sl = float(sys.argv[8]) if len(sys.argv) > 8 else 0.0
        rng = random.Random(seed); items = ((f"r{seed}_{i}", rand_genome(rng, nmax, dmax, degmax, xr, sl)) for i in range(k))
    for name, G in items:
        c, d, info = analyse(G, sec or sys.argv[1] == "json" or (XEVERY > 0 and cnt % XEVERY == 0 and not CTRL and MODE == "spec")); cnt += 1
        for k in KEYS: tot[k] += c[k]
        for k in DESC: dt[k] += d[k]
        for k in mx: mx[k] = max(mx[k], d[k])
        if info["xd"] is not None: xs += 1; xd += info["xd"]
        if first is None and sum(c.values()): first = (name, {k: v for k, v in c.items() if v})
        if sys.argv[1] == "json": print(f"{tag} {name}: " + fmt(c, d, info), flush=True)
    print(f"{tag} TOTAL {sys.argv[1]} {' '.join(sys.argv[2:9]) if sys.argv[1] != 'json' else cnt}: genomes {cnt} " + " ".join(f"{k} {tot[k]}" for k in KEYS)
          + " | " + " ".join(f"{k} {dt[k]}" for k in ("T", "switches", "nlk", "ladders")) + f" max T {mx['T']} maxsw {mx['maxsw']} maxK {mx['maxK']}"
          + f" | second engine sampled {xs} xdiff {xd} | {time.time() - t0:.0f} s" + (f" | first nonzero {first}" if first else ""), flush=True)
