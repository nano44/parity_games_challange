#!/usr/bin/env python3
"""Box 212 RF-LEVEL (L-NEW successor 74): the RULE-FREE part of P-N5-LEVEL, checked on runs of IDEAL-CYC(G) under ANY improving rule.
An improving rule: at every state t (Odd answering with a pointwise-optimal sigma-bar_t), switch a NON-EMPTY set of movers, each to a gate
of strictly larger value Omega_t than its current gate; stop at the first state where no mover has a strictly better gate.
Builder, valuation, order and Odd's reply are rv208.py's (experiments/new/box208/rv208.py, imported, not copied, not edited).
Rules (RULE=...): howard (rv208's: best gate, keep current if best, ties to the larger index), allrand (every improvable mover to a random
strictly better gate), allleast (every improvable mover to its LEAST strictly better gate), onebest (one random improvable mover to its best
gate), onerand (one random improvable mover, random strictly better gate), oneleast (the improvable mover of least index, to its least
strictly better gate), subrand (a random non-empty subset of the improvable movers, each to a random strictly better gate).
Must-0 counters (a VIOLATION line names the first three of each; a counter that is 0 is not printed):
  the run: IMP (a step that is not a non-empty set of strictly improving mover switches), CAP (run hit the cap)
  box 212 (a), static lemmas at EVERY visited state: CN2, CN2pi, BONLY, NOTIE, LOCGATE, LOCK2;  R15 (a): F1
  RF-A class facts: K1, K2 (sampled pairs), K3a, K3b, K3c, K3d, K3e, K4, K5new (class_(t+1)(x) >= class_t(sigma_(t+1)(x)))
  RF-A LEVEL per (b, t): L1sub, L1stall, L1rise, L1stallempty, L1lagback, L2, L3, L3alpha_m, L3beta_kind, L3beta_m, L5set, L5phi,
    NSP (more than P = 2M(N + 2M) non-stall steps for one reference state b)
  RF-B per (b, plateau [u, v]): P1, P2, P4, P4K2, PHclosed, PHval (own valuation of H_Y differs from Omega_s on Y), PHimp (a switch of a
    mover of Y that is not strictly improving in H_Y), PHout (a mover of Y switches to a gate outside Y)
  RF-C per b: C4 (a class changes after LAG is empty), DECOMP (b != non-stall steps + plateau steps + tail)
Descriptive: runs, Tmax, Tsum, bchecked, lagstates, stalls, nonstalls, nsmax (max non-stall steps for one b), nspctP (its max % of P),
  plateaus, platmax, plat_gt_movers, platidle (plateau steps that move no mover of Y), platexit ((plateau state, mover of Y) with a
  strictly better gate OUTSIDE Y, not taken), tailmax, tail_gt_N, K5how ((t, x, y) where Howard's K5 class_(t+1)(x) >= class_t(y) fails:
  the Howard-only fact), K2tested.
Control RF_CTRL=1: FRONT := the lagging vertices of the HIGHEST lagging class (L-counters must fire).
Usage: rf212.py [--T] G.json ...            (RULE from the environment; every b when T <= BALL, else b = T and BSAMP random b)
       rf212.py --rand SEED COUNT MODES      (rv208's generator; MODES as rv208)
       rf212.py --rstart SEED COUNT G.json ... (COUNT random mover start states per genome)
Environment: RULE (default howard), SEED (rule randomness, default 1), CAP (default 20000), BALL (default 80), BSAMP (default 30)."""
import sys, os, json, random, collections, itertools, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("rv208", os.path.join(HERE, "..", "box208", "rv208.py"))
rv = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(rv)

RULE = os.environ.get("RULE", "howard"); CAP = int(os.environ.get("CAP", "20000"))
BALL = int(os.environ.get("BALL", "80")); BSAMP = int(os.environ.get("BSAMP", "30")); RF_CTRL = os.environ.get("RF_CTRL") == "1"
RULES = ("howard", "allrand", "allleast", "onebest", "onerand", "oneleast", "subrand")

def run(B, rule, rng, start=None):
    n, own, succ, N = B["n"], B["own"], B["succ"], B["N"]; E = rv.Val(n, B["prio"], own, succ)
    sigma = [succ[v][0] if own[v] == 0 else -1 for v in range(n)]
    for x in range(N): sigma[x] = (start or B["start"])[x]
    hist = []; tau = None; capped = False
    while True:
        val, tau, nxt = E.best_response(sigma, tau)
        hist.append(dict(sigma=list(sigma), val=val, tau=dict(tau), nxt=nxt))
        better = {}
        for x in range(N):
            bx = [w for w in succ[x] if E.cmp(val[w], val[sigma[x]]) > 0]
            if bx: better[x] = bx
        if not better: break
        if len(hist) > CAP: capped = True; break
        def best(x):
            cur = sigma[x]; bst = cur
            for w in succ[x]:
                c = E.cmp(val[w], val[bst])
                if c > 0: bst = w
                elif c == 0 and w != bst and bst != cur and w > bst: bst = w
            return cur if E.cmp(val[bst], val[cur]) == 0 else bst
        def least(x):
            bx = better[x]; lo = bx[0]
            for w in bx[1:]:
                if E.cmp(val[w], val[lo]) < 0: lo = w
            return lo
        ns = list(sigma); xs = sorted(better)
        if rule == "howard":
            for x in range(N): ns[x] = best(x)
        elif rule == "allrand":
            for x in xs: ns[x] = rng.choice(better[x])
        elif rule == "allleast":
            for x in xs: ns[x] = least(x)
        elif rule == "onebest":
            x = rng.choice(xs); ns[x] = best(x)
        elif rule == "onerand":
            x = rng.choice(xs); ns[x] = rng.choice(better[x])
        elif rule == "oneleast":
            x = xs[0]; ns[x] = least(x)
        elif rule == "subrand":
            k = rng.randint(1, len(xs))
            for x in rng.sample(xs, k): ns[x] = rng.choice(better[x])
        else: raise SystemExit("unknown RULE " + rule)
        sigma = ns
    return E, hist, capped

def check(G, c, rule, rng, allb=True, k2pairs=3000, start=None, tag=""):
    B = rv.build(G); n, N, M, kind, own, succ = B["n"], B["N"], B["M"], B["kind"], B["own"], B["succ"]
    E, hist, capped = run(B, rule, rng, start); T = len(hist) - 1; rank, rew = E.rank, E.rew
    K0, K1, K2, K3 = B["K"]; cW, cX = B["cW"], B["cX"]; P = 2 * M * (N + 2 * M)
    core = set(B["K"]); movers = list(range(N)); gates = [v for v in range(n) if kind[v] == "g"]
    evs = [v for v in range(n) if kind[v] == "e"]; emask = sum(1 << rank[v] for v in evs); minE = min(rank[v] for v in evs)
    xgmask = sum(1 << rank[u] for u in range(n) if kind[u] in ("x", "g"))
    val = [h["val"] for h in hist]; nxt = [h["nxt"] for h in hist]; sig = [h["sigma"] for h in hist]; tau = [h["tau"] for h in hist]
    cls = [[(rew[val[t][v][0]], val[t][v][1] & emask) for v in range(n)] for t in range(T + 1)]
    c["runs"] += 1; c["Tmax"] = max(c["Tmax"], T); c["Tsum"] += T
    def bad(name, info=None):
        c[name] += 1
        if c[name] <= 3: print("VIOLATION", name, rule, tag, info, flush=True)
    if capped: bad("CAP", T)
    # ---- the run is an improving run; (a) static lemmas at every visited state; F1
    for t in range(T + 1):
        if t < T:
            ch = [x for x in movers if sig[t + 1][x] != sig[t][x]]
            if not ch or any(E.cmp(val[t][sig[t + 1][x]], val[t][sig[t][x]]) <= 0 for x in ch): bad("IMP", t)
        for v in range(n):
            lam = val[t][v][0]
            if B["prio"][lam] < 2: bad("CN2", (t, v))
            if val[t][v][1] & xgmask: bad("CN2pi", (t, v))
            if not (v == cW or (kind[v] == "e" and succ[v][0] == cW)) and rank[lam] >= minE: bad("BONLY", (t, v))
        for g in gates:
            e, b = B["face"][g]
            if E.cmp(val[t][e], val[t][b]) == 0: bad("NOTIE", (t, g))
            a = tau[t][g]; o = b if a == e else e
            if E.cmp(val[t][a], val[t][o]) >= 0: bad("LOCGATE", (t, g))
        if tau[t][K2] != K1: bad("LOCK2", t)
        if t < T:
            for v in range(n):
                if E.cmp(val[t][v], val[t + 1][v]) > 0: bad("F1", (t, v))
    # ---- class facts
    for t in range(T + 1):
        for v in range(n):
            w = nxt[t][v]
            if val[t][v][0] != val[t][w][0]: bad("K3a", (t, v))
            if kind[v] == "e":
                if kind[w] == "x" and not (cls[t][v] == (cls[t][w][0], cls[t][w][1] | (1 << rank[v])) and not (cls[t][w][1] >> rank[v]) & 1):
                    bad("K3d", (t, v))
            elif cls[t][v] != cls[t][w]: bad("K3c", (t, v))
        for e in evs:
            u = nxt[t][e]; seen = set()
            while u != e and u not in seen: seen.add(u); u = nxt[t][u]
            if u == e: bad("K3b", (t, e))
        for v in list(core) + [cW, cX] + [e for e in evs if succ[e][0] == cW]:
            if cls[t][v] != cls[0][v]: bad("K3e", (t, v))
        for g in gates:
            e, b = B["face"][g]
            if cls[t][g] != min(cls[t][e], cls[t][b]): bad("K4", (t, g))
        if t < T:
            for v in range(n):
                if cls[t + 1][v] < cls[t][v]: bad("K1", (t, v))
            for x in movers:
                if cls[t + 1][x] < cls[t][sig[t + 1][x]]: bad("K5new", (t, x))
                for y in succ[x]:
                    if cls[t + 1][x] < cls[t][y]: c["K5how"] += 1
    items = [(t, v) for t in range(T + 1) for v in range(n) if v not in core]
    for _ in range(k2pairs):
        (t1, v1), (t2, v2) = rng.choice(items), rng.choice(items)
        cm = E.cmp(val[t1][v1], val[t2][v2]); c["K2tested"] += 1
        if (cm <= 0 and cls[t1][v1] > cls[t2][v2]) or (cm >= 0 and cls[t1][v1] < cls[t2][v2]): bad("K2", (t1, v1, t2, v2))
    # ---- LEVEL, PLATEAU, tail for the reference states b
    if T <= BALL and allb: bs = list(range(1, T + 1))
    else: bs = sorted(set([T] + ([rng.randint(1, T) for _ in range(BSAMP)] if allb and T else []))) if T else []
    for b in bs:
        c["bchecked"] += 1
        gatecls_b = set(cls[b][g] for g in gates); betacls = set((rew[v], 0) for v in range(n) if kind[v] == "b")
        fr = []
        for t in range(b + 1):
            lag = [v for v in range(n) if cls[t][v] != cls[b][v]]
            if not lag: fr.append(None); continue
            m = (max if RF_CTRL else min)(cls[t][v] for v in lag); fr.append((set(lag), m, frozenset(v for v in lag if cls[t][v] == m)))
        phis = set(); ns_b = 0
        for t in range(b):
            if fr[t] is None:
                if fr[t + 1] is not None: bad("L1lagback", (b, t))
                if cls[t + 1] != cls[t]: bad("C4", (b, t))
                continue
            lag, m, F = fr[t]; phis.add((m, -len(F))); c["lagstates"] += 1
            stall = all(cls[t + 1][v] == cls[t][v] for v in F)
            if fr[t + 1] is not None:
                lag2, m2, F2 = fr[t + 1]
                if not lag2 <= lag: bad("L1sub", (b, t))
                p1, p2 = (m, -len(F)), (m2, -len(F2))
                if stall and not (F2 == F and p1 == p2): bad("L1stall", (b, t))
                if not stall and not p2 > p1: bad("L1rise", (b, t))
            elif stall: bad("L1stallempty", (b, t))
            for v in F:
                if not (kind[v] in ("x", "g") or (kind[v] == "b" and succ[v][0] < N)): bad("L2", (b, t, v, kind[v]))
            alpha = [z for z in F if kind[z] == "x" and nxt[t][z] not in lag]
            for z in alpha:
                if m != cls[b][nxt[t][z]]: bad("L3alpha_m", (b, t, z))
            beta = False
            for v0 in F:
                seen = {}; v = v0
                while v not in seen: seen[v] = len(seen); v = nxt[t][v]
                cyc = [u for u, i in seen.items() if i >= seen[v]]
                if all(u in F for u in cyc):
                    beta = True
                    if not all(kind[u] in ("x", "g", "b") for u in cyc): bad("L3beta_kind", (b, t))
                    lam = val[t][v0][0]
                    if kind[lam] != "b" or m != (rew[lam], 0): bad("L3beta_m", (b, t))
            if not alpha and not beta: bad("L3", (b, t))
            if alpha and m not in gatecls_b: bad("L5set", (b, t))
            if not alpha and beta and m not in betacls: bad("L5set", (b, t))
            if stall: c["stalls"] += 1
            else: c["nonstalls"] += 1; ns_b += 1
        if len(phis) > P: bad("L5phi", b)
        if ns_b > P: bad("NSP", (b, ns_b, P))
        c["nsmax"] = max(c["nsmax"], ns_b); c["nspctP"] = max(c["nspctP"], 100 * ns_b // P)
        # plateaus
        t = 0; platsteps = 0; bprime = b
        while t < b:
            if fr[t] is None: bprime = min(bprime, t); t += 1; continue
            u = t
            while t + 1 < b and fr[t + 1] is not None and (fr[t + 1][1], fr[t + 1][2]) == (fr[u][1], fr[u][2]): t += 1
            v = t; t += 1
            if v == u: continue
            c["plateaus"] += 1; platsteps += v - u
            m = fr[u][1]; Y = set(x for x in range(n) if cls[u][x] <= m)
            for s in range(u, v + 1):
                for x in range(n):
                    if (x in Y) != (cls[s][x] <= m) or (x in Y and cls[s][x] != cls[u][x]): bad("P1", (b, u, v, s, x))
                    if x in Y and nxt[s][x] not in Y: bad("P2", (b, u, v, s, x))
                for g in gates:
                    if g in Y and (tau[s][g] != tau[u][g] or tau[s][g] not in Y): bad("P4", (b, u, v, s, g))
                if K2 in Y and tau[s][K2] != K1: bad("P4K2", (b, u, v, s))
                for x in movers:
                    if x in Y and any(y not in Y and E.cmp(val[s][y], val[s][sig[s][x]]) > 0 for y in succ[x]): c["platexit"] += 1
            # H_Y: movers of Y keep their gates IN Y; every other vertex of Y keeps s_u(x)
            Yl = sorted(Y); idx = {x: i for i, x in enumerate(Yl)}; hsucc = []
            for x in Yl:
                if kind[x] == "x": ss = [w for w in succ[x] if w in Y]
                else:
                    ss = [nxt[u][x]]
                    if nxt[u][x] not in Y: bad("PHclosed", (b, u, v, x)); ss = [x]
                if not ss: bad("PHclosed", (b, u, v, x)); ss = [x]
                hsucc.append([idx[w] for w in ss])
            EH = rv.Val(len(Yl), [B["prio"][x] for x in Yl], [own[x] for x in Yl], hsucc)
            for s in range(u, v + 1):
                hs = [(idx[sig[s][x]] if sig[s][x] in Y else idx[x]) if kind[x] == "x" else hsucc[idx[x]][0] for x in Yl]
                hv = EH.playvals(hs)
                for x in Yl:
                    a = hv[idx[x]]; o = val[s][x]
                    pa = frozenset(Yl[i] for i in range(len(Yl)) if (a[1] >> EH.rank[i]) & 1)
                    po = frozenset(w for w in range(n) if (o[1] >> rank[w]) & 1)
                    if Yl[a[0]] != o[0] or pa != po or a[2] != o[2]: bad("PHval", (b, u, v, s, x))
                if s < v:
                    moved = False
                    for x in Yl:
                        if kind[x] != "x" or sig[s + 1][x] == sig[s][x]: continue
                        moved = True; w = sig[s + 1][x]
                        if w not in Y: bad("PHout", (b, u, v, s, x)); continue
                        if EH.cmp(hv[idx[w]], hv[idx[sig[s][x]]]) <= 0: bad("PHimp", (b, u, v, s, x))
                    if not moved: c["platidle"] += 1
            nm = sum(1 for x in Y if kind[x] == "x")
            if v - u > nm: c["plat_gt_movers"] += 1
            c["platmax"] = max(c["platmax"], v - u)
        if all(f is not None for f in fr[:b]): bprime = b
        tail = b - bprime
        if bprime != ns_b + platsteps: bad("DECOMP", (b, bprime, ns_b, platsteps))
        c["tailmax"] = max(c["tailmax"], tail)
        if tail > N: c["tail_gt_N"] += 1
    return T

def out(label, c):
    print(label, "RULE", RULE, " ".join("%s %d" % kv for kv in sorted(c.items())), flush=True)

if __name__ == "__main__":
    a = sys.argv[1:]; seed = int(os.environ.get("SEED", "1"))
    if RULE not in RULES: raise SystemExit("RULE must be one of " + ",".join(RULES))
    if a[0] == "--rand":
        s, cnt = int(a[1]), int(a[2]); modes = a[3].split(","); rg = random.Random(s); rr = random.Random(seed); c = collections.Counter()
        for i in range(cnt):
            G = rv.rgen(rg, rg.choice(modes)); check(G, c, RULE, rr, tag="seed %d #%d" % (s, i))
        out("rand %d %d %s" % (s, cnt, a[3]), c)
    elif a[0] == "--rstart":
        s, cnt = int(a[1]), int(a[2])
        for fn in a[3:]:
            G = json.load(open(fn)); G = G.get("genome", G); rg = random.Random(s); rr = random.Random(seed); c = collections.Counter()
            for i in range(cnt):
                st = [rg.randrange(len(o)) for o in G["opts"]]
                check(dict(G, start=st), c, RULE, rr, tag="%s rstart %d" % (os.path.basename(fn), i))
            out("rstart %s %d %d" % (os.path.basename(fn), s, cnt), c)
    else:
        allb = a[0] != "--T"
        for fn in (a if allb else a[1:]):
            G = json.load(open(fn)); G = G.get("genome", G); c = collections.Counter()
            check(G, c, RULE, random.Random(seed), allb=allb, tag=os.path.basename(fn))
            out(os.path.basename(fn), c)
