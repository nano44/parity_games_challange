#!/usr/bin/env python3
"""L-RED 68 R239: adversary against L-NEW 74 box 212 RF-LEVEL (claude/l-new 5fa64fe6, docs/new/N5-RFLEVEL-box212.md), RF-A / RF-B / RF-C,
on L-RED's OWN IDEAL-CYC engine (experiments/red/r221q/own.py: Gamma(G) from R104's description, own VJ values, Odd's optimal reply by
own one-player SI; no code from rf212 / rv208 / level208 / si.py), under ANY improving rule at the movers.
Definitions (P-N5-LEVEL l-new 1e6df499 §2, §4, §7, quoted in box 212 §3-§5): class_t(v) = (Lambda_t(v), E_t(v)), E = the e-vertices of
Pi_t(v); order: reward(Lambda), then the most relevant element of E ^ E' lies in the larger. Reference b: LAG_t = {v : class_t(v) !=
class_b(v)}; m_t = min class on LAG_t; FRONT_t = {v in LAG_t : class m_t}; Phi_t = (m_t, -|FRONT_t|); a step t -> t+1 (t < b, LAG_t
non-empty) is a STALL iff every v in FRONT_t keeps its class. P = 2M(N + 2M).
IMPROVING RUN: every step changes sigma exactly at a non-empty set of movers, each to a gate of strictly larger value Omega_t.
RULES (env RULE): howard (best, keep current if best, ties larger index; own.py's), allleast (every improvable mover to its LEAST
strictly better gate), allworst (every improvable mover to the strictly better gate with the LARGEST gate number = the worst key),
allrand, subrand (random non-empty subset, random better gates), onebest / onerand / oneleast (one random improvable mover), onefirst
(the lowest-numbered improvable mover to its least better gate), oneworst (one random mover to its largest-gate-number better gate).
MUST-0 counters (rule-free claims of box 212):
 imp      a step that is not improving (checks my own rules)
 f1       (state t, v): Omega_(t+1)(v) strictly below Omega_t(v)                                         [F1 = R15 (a)]
 cn2      (state, v): the cycle node of v's play has priority < 2                                     [CN2]
 k1       (step, v): class falls                                                                       [RF-A (i) (K1)]
 k2       (pair of values of vertices outside the core, at one or two states; ALL pairs when (T + 1)·#outside <= K2ALL (700), else 1,500 sampled): Theta <= Theta' but class > class'  [(K2)]
 k3       (state, v): (K3) (a), (c), (d) or (e) fails                                                   [(K3)]
 k4       (state, gate): class(g) != min(face classes), or the chosen face lacks that class              [(K4)]
 k5new    (step, mover x): class_(t+1)(x) < class_t(sigma_(t+1)(x))                                    [RF-A (iv)]
 l1       (b, step): LAG grows, or a stall changes FRONT / Phi or empties LAG, or a non-stall keeps LAG non-empty without Phi rising  [(L1)]
 l2       (b, state, v in FRONT): v is not a mover, a gate or a beta-vertex with a mover successor         [(L2)]
 l3       (b, state): neither (alpha) nor (beta) holds                                                  [(L3)]
 l5       (b): Phi takes more than P values, or some m_t is neither class_b of a gate nor (c, {}) for a beta-vertex c  [(L5)]
 nsp      (b): more than P non-stall steps with LAG non-empty                                          [RF-A (iii)]
 p1, p2, p4, p5   (b, plateau): (P1), (P2) («no vertex of Y leaves Y»: s_s(x) in Y, sigma_s(x) in Y), (P4), (P5') (values on Y =
          the values of H_Y; each moved mover of Y moves inside Y to a strictly H_Y-better gate)          [RF-B]
 tail     (b = T): on [b', T] some class changes, some gate of Y changes its face, or sigma-bar(K2) != K1   [RF-C tail clause]
DESCRIPTIVE (Howard-only facts; box 212 says they FAIL for other rules): k5how (K5 for every gate), p3 (P3), p6idle (P6), p7
(v - u > movers of Y), tailN (tail > N). Also T, nonstall max, plateau max, stalls.
CTRL (must fire): 1 = the e-set order reversed in the class order; 2 = the rule takes a strictly WORSE gate at one step (imp fires
and F1 / K1 usually do); 3 = Phi's second coordinate +|FRONT| (l1 fires).
Usage: rf239.py rand SEED COUNT NMAX DMAX DEGMAX [RULES]   |   rf239.py json RULES FILE.json ...   (RULES comma-separated; default all)"""
import sys, os, json, random, functools, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [os.path.join(HERE, "..", "r221q"), os.path.join(HERE, "..", "r230")]
import own as OWN
CTRL = int(os.environ.get("CTRL", "0")); BMAX = int(os.environ.get("BMAX", "12")); CAP = int(os.environ.get("CAP", "3000")); K2ALL = int(os.environ.get("K2ALL", "700"))
RULES = ("howard", "allleast", "allworst", "allrand", "subrand", "onebest", "onerand", "oneleast", "onefirst", "oneworst")
MUST0 = ("imp", "f1", "cn2", "k1", "k2", "k3", "k4", "k5new", "l1", "l2", "l3", "l5", "nsp", "p1", "p2", "p4", "p5", "tail")
DESC = ("k5how", "p3", "p6idle", "p7", "tailN")

def rand_genome(rng, nmax, dmax, degmax):
    N = rng.randint(2, nmax); D = rng.randint(1, min(dmax, N)); lev = list(range(D)) + [rng.randrange(D) for _ in range(N - D)]
    rng.shuffle(lev)
    by = {}
    for x in range(N): by.setdefault(lev[x], []).append(x)
    opts = []; i = 0
    for x in range(N):
        o = []
        for _ in range(rng.randint(1, degmax)):
            o.append([rng.choice(by[lev[x] - 1]) if lev[x] else -1, -1 if rng.random() < 0.15 else rng.randrange(N), i]); i += 1
        opts.append(o)
    M = i; gp = list(range(M)); rng.shuffle(gp); it = iter(gp); gate = [[next(it) for _ in o] for o in opts]
    br = list(range(M)); rng.shuffle(br)
    return dict(N=N, lev=lev, opts=opts, gate=gate, br=br, bp=[rng.randint(0, 1) for _ in range(M)], start=[rng.randrange(len(o)) for o in opts])

def run(G, rule, rng):
    n, prio, ow, succ, V, O = OWN.build(G); vj = OWN.VJ(prio); N = G["N"]; key = functools.cmp_to_key(vj.cmp)
    sig = [succ[v][0] if ow[v] == 0 else None for v in range(n)]
    for x in range(N): sig[x] = V[("g", (x, G["start"][x]))]
    tau = {v: succ[v][0] for v in range(n) if ow[v] == 1}; out = []; imp = 0; gnum = {V[("g", q)]: G["gate"][q[0]][q[1]] for q in O}
    ctrl_t = rng.randrange(4) if CTRL == 2 else -1
    while len(out) <= CAP:
        vals, tau = OWN.evaluate(n, ow, succ, vj, sig, tau); out.append((tuple(sig), vals, dict(tau)))
        better = {x: [w for w in succ[x] if vj.cmp(vals[w], vals[sig[x]]) > 0] for x in range(N)}
        I = [x for x in range(N) if better[x]]
        if not I: break
        ns = list(sig)
        least = lambda x: min(better[x], key=lambda w: (key(vals[w]), w))
        if rule == "howard":
            for x in range(N): ns[x] = max(succ[x], key=lambda w: (key(vals[w]), w == sig[x], w))
        elif rule in ("allleast", "allworst", "allrand"):
            for x in I: ns[x] = least(x) if rule == "allleast" else (max(better[x], key=lambda w: gnum[w]) if rule == "allworst" else rng.choice(better[x]))
        elif rule == "subrand":
            for x in rng.sample(I, rng.randint(1, len(I))): ns[x] = rng.choice(better[x])
        else:
            x = min(I) if rule == "onefirst" else rng.choice(I)
            ns[x] = {"onebest": lambda: max(better[x], key=lambda w: (key(vals[w]), w)), "onerand": lambda: rng.choice(better[x]),
                     "oneleast": lambda: least(x), "onefirst": lambda: least(x), "oneworst": lambda: max(better[x], key=lambda w: gnum[w])}[rule]()
        if len(out) - 1 == ctrl_t:                       # CTRL=2: one step to a strictly worse gate where one exists
            for x in range(N):
                worse = [w for w in succ[x] if vj.cmp(vals[w], vals[sig[x]]) < 0]
                if worse: ns[x] = worse[0]; break
        ch = [x for x in range(N) if ns[x] != sig[x]]
        imp += int(not ch or any(vj.cmp(vals[ns[x]], vals[sig[x]]) <= 0 for x in ch))
        sig = ns
    return out, (n, prio, ow, succ, V, O, vj), imp

def analyse(G, rule, rng, k2pairs=1500):
    out, (n, prio, ow, succ, V, O, vj), imp = run(G, rule, rng); N = G["N"]; M = len(O); T = len(out) - 1; rk = vj.rk
    c = {k: 0 for k in MUST0 + DESC}; c["imp"] = imp; P = 2 * M * (N + 2 * M)
    E = {V[("e", q)] for q in O}; gates = {V[("g", q)]: q for q in O}; betas = {V[("b", q)]: q for q in O}
    core = {V["K0"], V["K1"], V["K2"], V["K3"]}; movers = set(range(N)); K2, K1 = V["K2"], V["K1"]
    face = {V[("g", q)]: (V[("e", q)], V[("b", q)]) for q in O}
    def cls(val):
        return (vj.rew(val[0]), tuple(sorted((rk[u] for u in val[1] if u in E), reverse=True)))
    def lt(a, b):
        if a[0] != b[0]: return a[0] < b[0]
        d = set(a[1]) ^ set(b[1])
        return bool(d) and ((max(d) in b[1]) != (CTRL == 1))
    def le(a, b): return a == b or lt(a, b)
    C = [[cls(vals[v]) for v in range(n)] for (_, vals, _) in out]
    def nxt(t, v): sig, _, tau = out[t]; return sig[v] if ow[v] == 0 else tau[v]
    # static facts at every state
    for t, (sig, vals, tau) in enumerate(out):
        for v in range(n):
            lam = vals[v][0]; c["cn2"] += int(prio[lam] < 2); w = nxt(t, v)
            if vals[v][0] != vals[w][0]: c["k3"] += 1                                          # (a)
            if v in E:
                if w < N:                                                                       # (d)
                    exp = (C[t][w][0], tuple(sorted(set(C[t][w][1]) | {rk[v]}, reverse=True)))
                    c["k3"] += int(C[t][v] != exp or rk[v] in C[t][w][1])
                else: c["k3"] += int(C[t][v] != C[t][V["cW"]])                                   # (e): e -> c_W has c_W's class
            elif C[t][v] != C[t][w]: c["k3"] += 1                                               # (c)
        for g, (fe, fb) in face.items():
            mn = C[t][fe] if le(C[t][fe], C[t][fb]) else C[t][fb]
            c["k4"] += int(C[t][g] != mn or C[t][nxt(t, g)] != mn)
        c["k3"] += int(any(C[t][v] != C[0][v] for v in core | {V["cW"], V["cX"]}))              # (e)
    for t in range(T):
        sb, vb, _ = out[t + 1]; sa, va, _ = out[t]
        for v in range(n):
            c["f1"] += int(vj.cmp(vb[v], va[v]) < 0); c["k1"] += int(lt(C[t + 1][v], C[t][v]))
        for x in range(N):
            c["k5new"] += int(lt(C[t + 1][x], C[t][sb[x]]))
            c["k5how"] += int(any(lt(C[t + 1][x], C[t][y]) for y in succ[x]))
    outside = [v for v in range(n) if v not in core]
    if (T + 1) * len(outside) <= K2ALL:                           # (K2) exhaustively over all pairs (vertex, state) x (vertex, state)
        pts = [(t, v) for t in range(T + 1) for v in outside]
        pairs = ((p1, p2) for p1 in pts for p2 in pts)
    else:
        pairs = (((rng.randint(0, T), rng.choice(outside)), (rng.randint(0, T), rng.choice(outside))) for _ in range(k2pairs))
    for (t1, v1), (t2, v2) in pairs:
        if lt(C[t2][v2], C[t1][v1]) and vj.cmp(out[t1][1][v1], out[t2][1][v2]) <= 0: c["k2"] += 1
    # LEVEL / PLATEAU / tail for reference states b
    Bs = list(range(T + 1)) if T + 1 <= BMAX else sorted({T} | set(rng.sample(range(T), BMAX - 1)))
    maxns = 0; maxplat = 0; stalls = 0
    for b in Bs:
        lag = [[v for v in range(n) if C[t][v] != C[b][v]] for t in range(b + 1)]
        def phi(t):
            L = lag[t]
            if not L: return None, None
            m = L[0]
            for v in L:
                if lt(C[t][v], C[t][m]): m = v
            fr = [v for v in L if C[t][v] == C[t][m]]
            return C[t][m], fr
        PH = [phi(t) for t in range(b + 1)]; ns = 0; vals_phi = set(); allowed = {C[b][g] for g in gates} | {(vj.rew(bv), ()) for bv in betas}
        for t in range(b + 1):
            m, fr = PH[t]
            if m is None: continue
            vals_phi.add((m, len(fr))); c["l5"] += int(m not in allowed)
            for v in fr: c["l2"] += int(not (v in movers or v in gates or (v in betas and nxt(t, v) < N)))
            sig = out[t][0]; L = set(lag[t])
            alpha = any(z in fr and z in movers and sig[z] not in L and m == C[b][sig[z]] for z in fr)
            beta = False
            for v in fr:                                       # (beta): the play of v closes a cycle inside FRONT of movers / gates / betas
                seen = []; w = v
                while w not in seen: seen.append(w); w = nxt(t, w)
                cyc = seen[seen.index(w):]
                if all(u in fr for u in cyc) and all(u in movers or u in gates or u in betas for u in cyc) and m == (vj.rew(max(cyc, key=lambda u: rk[u])), ()) and max(cyc, key=lambda u: rk[u]) in betas:
                    beta = True; break
            c["l3"] += int(not (alpha or beta))
            if t < b:
                m2, fr2 = PH[t + 1]; stall = all(C[t + 1][v] == C[t][v] for v in fr)
                c["l1"] += int(not set(lag[t + 1]) <= L)
                k1_, k2_ = len(fr), (None if fr2 is None else len(fr2))
                sec = (lambda k: -k) if CTRL != 3 else (lambda k: k)
                if stall:
                    stalls += 1; c["l1"] += int(m2 is None or sorted(fr2) != sorted(fr))
                else:
                    ns += 1
                    if m2 is not None and not (lt(m, m2) or (m2 == m and sec(k2_) > sec(k1_))): c["l1"] += 1
        c["l5"] += int(len(vals_phi) > P); c["nsp"] += int(ns > P); maxns = max(maxns, ns)
        t = 0
        while t <= b:                                          # plateaus: maximal intervals of constant Phi, u < v
            if PH[t][0] is None: t += 1; continue
            u = t
            while t + 1 <= b and PH[t + 1][0] == PH[u][0] and len(PH[t + 1][1]) == len(PH[u][1]): t += 1
            v = t; t += 1
            if v == u: continue
            m = PH[u][0]; maxplat = max(maxplat, v - u); Y = {x for x in range(n) if le(C[u][x], m)}; Ymov = [x for x in Y if x < N]
            for s in range(u, v + 1):
                c["p1"] += int({x for x in range(n) if le(C[s][x], m)} != Y or any(C[s][x] != C[u][x] for x in Y))
                c["p2"] += int(any(nxt(s, x) not in Y for x in Y))
                for g in gates:
                    if g in Y: c["p4"] += int(nxt(s, g) != nxt(u, g) or nxt(s, g) not in Y)
                if K2 in Y: c["p4"] += int(nxt(s, K2) != K1)
                c["p3"] += int(any(y not in Y for x in Ymov for y in succ[x]))
                # (P5'): values on Y in H_Y (every non-mover keeps s_u; movers follow sigma_s); Odd has one strategy
                hn = [nxt(u, x) if x >= N else out[s][0][x] for x in range(n)]
                for x in Y:
                    if hn[x] not in Y: c["p5"] += 1; continue
                    c["p5"] += int(vj.val(x, hn) != out[s][1][x])
                if s < v:
                    moved = [x for x in Ymov if out[s + 1][0][x] != out[s][0][x]]
                    c["p6idle"] += int(not moved)
                    for x in moved:
                        y = out[s + 1][0][x]
                        if y not in Y: c["p5"] += 1; continue
                        c["p5"] += int(vj.cmp(vj.val(y, hn), vj.val(out[s][0][x], hn)) <= 0)
            c["p7"] += int(v - u > len(Ymov))
        if b == T:                                             # RF-C tail clause
            bp = next((tt for tt in range(T + 1) if not lag[tt]), T)
            c["tailN"] += int(T - bp > N)
            for s in range(bp, T + 1):
                c["tail"] += int(any(C[s][x] != C[bp][x] for x in range(n)) or any(nxt(s, g) != nxt(bp, g) for g in gates) or nxt(s, K2) != K1)
    return c, dict(T=T, N=N, M=M, n=n, P=P, maxns=maxns, maxplat=maxplat, stalls=stalls)

if __name__ == "__main__":
    mode = sys.argv[1]; t0 = time.time()
    if mode == "rand":
        seed, cnt, nmax, dmax, degmax = map(int, sys.argv[2:7]); rules = sys.argv[7].split(",") if len(sys.argv) > 7 else RULES
        rng = random.Random(seed); gens = [rand_genome(rng, nmax, dmax, degmax) for _ in range(cnt)]; names = [f"rand{seed}_{i}" for i in range(cnt)]
    else:
        rules = sys.argv[2].split(","); gens = []; names = []
        for fn in sys.argv[3:]:
            G = json.load(open(fn)); G = G.get("genome", G); G.pop("_evals", None); gens.append(G); names.append(os.path.basename(fn))
        rng = random.Random(239)
    for rule in rules:
        tot = {k: 0 for k in MUST0 + DESC}; mx = dict(T=0, maxns=0, maxplat=0, n=0); st = 0; first = None
        for G, nm in zip(gens, names):
            c, d = analyse(G, rule, rng)
            for k in tot: tot[k] += c[k]
            for k in mx: mx[k] = max(mx[k], d[k])
            st += d["stalls"]
            if first is None and sum(c[k] for k in MUST0): first = (nm, {k: v for k, v in c.items() if v and k in MUST0})
        print(f"RF239 {mode} {' '.join(sys.argv[2:7]) if mode == 'rand' else len(gens)} rule {rule}" + (f" CTRL {CTRL}" if CTRL else "")
              + ": must0 " + " ".join(f"{k} {tot[k]}" for k in MUST0) + " | desc " + " ".join(f"{k} {tot[k]}" for k in DESC)
              + f" | max T {mx['T']} max nonstall {mx['maxns']} max plateau {mx['maxplat']} stalls {st} max |V| {mx['n']} | {time.time() - t0:.0f} s"
              + (f" | first nonzero {first}" if first else ""), flush=True)
