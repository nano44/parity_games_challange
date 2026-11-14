#!/usr/bin/env python3
"""L-RED 71 R246 (question SCHEME-TIE): TIE CENSUS of a run of the scheme SPEC S1-S5 (FIX 1-4) from S3.
At every iteration, S4a computes a pointwise optimum of the one-player arena H (Even y keeps A(y) = {sigma(y)} + I_sigma(y), Odd follows
tau; value W*). For an Even vertex v with |A(v)| >= 2 the set of S4a-BEST options is
   BEST(v) := {w in A(v) : W*(v) = v (+) W*(w)}                           if v is not its own W*-cycle node   («path» case), and
   BEST(v) := {w in A(v) : w reaches v in H through vertices of rank < rank(v)}   if it is                    («cycle» case;
                                                                              any such w closes a cycle whose node is v).
A TIE is a pair (iteration, v) with |BEST(v)| >= 2: only there can a tie rule of S4a matter. If no tie is met in a run, the pointwise
optimum is unique at every iteration and every S4a tie rule gives the same run. The same census is taken for S4b (Odd's arena H': Odd keeps
{tau(y)} + I_tau(y), Even follows sigma), since a scheme could change that tie rule too.
UNIT «S4a ties met» := number of pairs (iteration, Even vertex v) with |A(v)| >= 2 and |BEST(v)| >= 2 (ptie = path case, ctie = cycle case).
Engines:
  s   own: n5s237 (SPEC-exact, written from the SPEC text; experiments/red/r237), values by its vjproc; transitions recomputed here with the
      same lines as n5s237.run and asserted equal to n5s237.run's iteration / fallback counts.
  v   L-NEW's: transitions by box 190 n5v.step, arena values by si.Engine exactly as n5v.step computes them (env LNEW = a tree with
      claude/l-new's experiments/new, experiments/si/si.py, experiments/harness); an independent implementation of the valuations.
Counters per game (one line):
  its, fb        iterations to the stop, fallbacks
  a_steps        iterations at which S4a ran (I_sigma nonempty)
  choice         sum over iterations of #{Even v : |A(v)| >= 2}
  ptie, ctie     «S4a ties met», path and cycle case; tie = ptie + ctie; tie_mov = those at vertices of index < NMOV (movers of Gamma3(G))
  tie_its        iterations with at least one S4a tie; tie_max = most ties in one iteration
  refuse         pairs (iteration, v) with |A(v)| >= 2 and sigma_new(v) = sigma(v) (an improving switch refused);
  refuse_strict  those with |BEST(v)| = 1 (refused by the arena's STRICT preference, not by a tie rule)
  b_steps, bchoice, btie   the same for S4b (I_tau nonempty; Odd v with >= 2 kept options; ties)
  opt_bad        #(iteration, v) where the engine's own choice is not in BEST(v) (must be 0: sanity of the census)
  fbtie          at a fallback (S4c): vertices whose Xi-best improving option is not unique (the fallback's own index tie-break is used)
Controls: TIE246_CTRL=1 (engine s) compares the options with the P-SETS IGNORED (same cycle node and length = «tied»): on the tie-free
games ptie must rise to the count of the R104 games; the frozen Gamma3(G_k) games themselves are the positive control (ties at every
iteration, equal to the IDEAL model's count, trace246.py).
Usage: tie246.py ENGINE MODE NMOV [--per FILE] GAME.pg ...     (MODE spec | xi; NMOV = number of movers, 0 if unknown)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [HERE, os.path.join(HERE, "..", "r237")]
CTRL = os.environ.get("TIE246_CTRL", "0")

def reach_low(v, w, hs, rk):
    """w reaches v in the graph hs through vertices of rank < rank(v) (w itself included)"""
    if w == v: return True
    if rk[w] >= rk[v]: return False
    seen = {w}; st = [w]
    while st:
        x = st.pop()
        for y in hs[x]:
            if y == v: return True
            if rk[y] < rk[v] and y not in seen: seen.add(y); st.append(y)
    return False

def census_own(prio, owner, succ, mode, nmov, per=None, cap=10 ** 7, rows=None, states=None):
    import n5s237 as E
    n = len(prio); order = sorted(range(n), key=lambda v: (prio[v], v)); rk = [0] * n
    for r, v in enumerate(order): rk[v] = r
    ev = [p % 2 == 0 for p in prio]; evd = [not e for e in ev]; O, Od = E.Ord(rk, ev), E.Ord(rk, evd)
    succ = [sorted(set(s)) for s in succ]; isE = [o == 0 for o in owner]; isO = [o == 1 for o in owner]
    r_ = lambda p: p if p % 2 == 0 else -p
    sigma = {v: max(succ[v], key=lambda w: (r_(prio[w]), w if prio[w] % 2 == 0 else -w)) for v in range(n) if isE[v]}
    tau = {v: max(succ[v], key=lambda w: (r_(prio[w] + 1), w if (prio[w] + 1) % 2 == 0 else -w)) for v in range(n) if isO[v]}
    def ext(v, w):
        return E.ext(rk, v, w)
    def same(v, w, Wv, Ww):
        if CTRL == "1": return Ww[0] == Wv[0] and Ww[2] + 1 == Wv[2]
        return ext(v, Ww) == Wv
    C = dict(its=0, fb=0, a_steps=0, choice=0, ptie=0, ctie=0, tie_mov=0, tie_its=0, tie_max=0, refuse=0, refuse_strict=0,
             b_steps=0, bchoice=0, btie=0, opt_bad=0, fbtie=0)
    if states is not None: states.append(dict(sigma))
    while C["its"] < cap:
        vs, _ = E.vjproc(n, rk, ev, [[sigma[v]] if isE[v] else succ[v] for v in range(n)], isO)
        vt, _ = E.vjproc(n, rk, evd, [[tau[v]] if isO[v] else succ[v] for v in range(n)], isE)
        Is = {v: [w for w in succ[v] if w != sigma[v] and O.better(vs[w], vs[sigma[v]])] for v in sigma}; Is = {v: ws for v, ws in Is.items() if ws}
        It = {v: [w for w in succ[v] if w != tau[v] and Od.better(vt[w], vt[tau[v]])] for v in tau}; It = {v: ws for v, ws in It.items() if ws}
        if not Is and not It: break
        ns, nt = dict(sigma), dict(tau); row = dict(it=C["its"] + 1, nIs=len(Is), nIt=len(It), choice=0, ptie=0, ctie=0, refuse=0, refuse_strict=0, bchoice=0, btie=0, fb=0)
        if Is:
            C["a_steps"] += 1
            A = {v: sorted({sigma[v]} | set(Is.get(v, []))) for v in sigma}
            hs = [A[v] if isE[v] else [tau[v]] for v in range(n)]
            W, ch = E.vjproc(n, rk, evd, hs, isE)
            for v in sigma: ns[v] = ch[v]
            best = {}
            for v in sigma:
                if len(A[v]) < 2: continue
                row["choice"] += 1
                if W[v][0] != v:
                    b = [w for w in A[v] if same(v, w, W[v], W[w])]; kind = "ptie"
                else:
                    b = [w for w in A[v] if reach_low(v, w, hs, rk)]; kind = "ctie"
                best[v] = b
                if ch[v] not in b: C["opt_bad"] += 1
                if len(b) >= 2:
                    row[kind] += 1
                    if v < nmov: C["tie_mov"] += 1
            if mode == "xi":
                for v in sigma:
                    if len(A[v]) >= 2 and W[v][0] != v:
                        tie = [w for w in A[v] if E.ext(rk, v, W[w]) == W[v]]
                        if tie:
                            b = tie[0]
                            for w in tie[1:]:
                                if O.better(vs[w], vs[b]): b = w
                                elif not O.better(vs[b], vs[w]) and ((w == ch[v]) > (b == ch[v]) or ((w == ch[v]) == (b == ch[v]) and w > b)): b = w
                            ns[v] = b
            for v, b in best.items():
                if ns[v] == sigma[v]:
                    row["refuse"] += 1
                    if len(b) == 1: row["refuse_strict"] += 1
        if It:
            C["b_steps"] += 1
            A = {v: sorted({tau[v]} | set(It.get(v, []))) for v in tau}
            hs = [A[v] if isO[v] else [sigma[v]] for v in range(n)]
            W, ch = E.vjproc(n, rk, ev, hs, isO)
            for v in tau: nt[v] = ch[v]
            for v in tau:
                if len(A[v]) < 2: continue
                row["bchoice"] += 1
                if W[v][0] != v: b = [w for w in A[v] if same(v, w, W[v], W[w])]
                else: b = [w for w in A[v] if reach_low(v, w, hs, rk)]
                if ch[v] not in b: C["opt_bad"] += 1
                if len(b) >= 2: row["btie"] += 1
        if ns == sigma and nt == tau:
            C["fb"] += 1; row["fb"] = 1
            if Is:
                for v, ws in Is.items():
                    b = ws[0]
                    for w in ws[1:]:
                        if O.better(vs[w], vs[b]) or (not O.better(vs[b], vs[w]) and w > b): b = w
                    ns[v] = b
                    if sum(1 for w in ws if not O.better(vs[b], vs[w])) >= 2: C["fbtie"] += 1
            else:
                for v, ws in It.items():
                    b = ws[0]
                    for w in ws[1:]:
                        if Od.better(vt[w], vt[b]) or (not Od.better(vt[b], vt[w]) and w > b): b = w
                    nt[v] = b
                    if sum(1 for w in ws if not Od.better(vt[b], vt[w])) >= 2: C["fbtie"] += 1
        sigma, tau = ns, nt; C["its"] += 1
        t = row["ptie"] + row["ctie"]
        for k in ("choice", "ptie", "ctie", "refuse", "refuse_strict", "bchoice", "btie"): C[k] += row[k]
        C["tie_its"] += t > 0; C["tie_max"] = max(C["tie_max"], t)
        if per is not None: per.write(" ".join(f"{k} {row[k]}" for k in row) + "\n")
        if rows is not None: rows.append(row)
        if states is not None: states.append(dict(sigma))
    it0, fb0, _, _, _ = E.run(prio, owner, succ, mode)
    assert (it0, fb0) == (C["its"], C["fb"]), ("census loop differs from n5s237.run", it0, fb0, C["its"], C["fb"])
    return C

def census_lnew(fn, mode, nmov, per=None, cap=10 ** 7):
    LNEW = os.environ["LNEW"]
    sys.path[:0] = [os.path.join(LNEW, p) for p in ("experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
    import n5v, n5x, pg
    from si import Engine
    g = n5x.load(fn); n = g.n; E, Ed = Engine(g), Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None)
    order = sorted(range(n), key=lambda v: (g.prio[v], v)); rk = [0] * n
    for r, v in enumerate(order): rk[v] = r
    C = dict(its=0, fb=0, a_steps=0, choice=0, ptie=0, ctie=0, tie_mov=0, tie_its=0, tie_max=0, refuse=0, refuse_strict=0,
             b_steps=0, bchoice=0, btie=0, opt_bad=0, fbtie=0)
    while C["its"] < cap:
        res = n5v.step(g, E, Ed, sigma, tau, mode)
        if res is None: break
        ns, nt, Is, It, fb = res
        if fb: vs, _ = E.evaluate(tuple(sigma)); vt, _ = Ed.evaluate(tuple(tau))
        row = dict(it=C["its"] + 1, nIs=len({v for v, _ in Is}), nIt=len({v for v, _ in It}), choice=0, ptie=0, ctie=0, refuse=0, refuse_strict=0, bchoice=0, btie=0, fb=fb)
        if Is:
            C["a_steps"] += 1
            opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
            for v, w in Is: opt[v].add(w)
            hs = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
            Er = Engine(n5v.dual(pg.Game(list(g.prio), list(g.owner), hs)))
            vh, best = Er.evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] != 0 or len(opt[v]) < 2: continue
                row["choice"] += 1
                if vh[v][0] != v: b = [w for w in opt[v] if Er.extend(v, vh[w]) == vh[v]]; kind = "ptie"
                else: b = [w for w in opt[v] if reach_low(v, w, hs, rk)]; kind = "ctie"
                if best[v] not in b: C["opt_bad"] += 1
                if len(b) >= 2:
                    row[kind] += 1
                    if v < nmov: C["tie_mov"] += 1
                if not fb and ns[v] == sigma[v]:
                    row["refuse"] += 1
                    if len(b) == 1: row["refuse_strict"] += 1
                elif fb and best[v] == sigma[v]:
                    row["refuse"] += 1
                    if len(b) == 1: row["refuse_strict"] += 1
        if It:
            C["b_steps"] += 1
            opt = {v: {tau[v]} for v in range(n) if g.owner[v] == 1}
            for v, w in It: opt[v].add(w)
            hs = [sorted(opt[v]) if g.owner[v] == 1 else [sigma[v]] for v in range(n)]
            Er = Engine(pg.Game(list(g.prio), list(g.owner), hs))
            vh, best = Er.evaluate(tuple(sigma[v] if g.owner[v] == 0 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] != 1 or len(opt[v]) < 2: continue
                row["bchoice"] += 1
                if vh[v][0] != v: b = [w for w in opt[v] if Er.extend(v, vh[w]) == vh[v]]
                else: b = [w for w in opt[v] if reach_low(v, w, hs, rk)]
                if best[v] not in b: C["opt_bad"] += 1
                if len(b) >= 2: row["btie"] += 1
        if fb:
            if Is:
                for v in {v for v, _ in Is}:
                    ws = [w for x, w in Is if x == v]; kb = max(E.key(vs[w]) for w in ws)
                    if sum(1 for w in ws if E.key(vs[w]) == kb) >= 2: C["fbtie"] += 1
            else:
                for v in {v for v, _ in It}:
                    ws = [w for x, w in It if x == v]; kb = max(Ed.key(vt[w]) for w in ws)
                    if sum(1 for w in ws if Ed.key(vt[w]) == kb) >= 2: C["fbtie"] += 1
        C["fb"] += fb; sigma, tau = list(ns), list(nt); C["its"] += 1
        t = row["ptie"] + row["ctie"]
        for k in ("choice", "ptie", "ctie", "refuse", "refuse_strict", "bchoice", "btie"): C[k] += row[k]
        C["tie_its"] += t > 0; C["tie_max"] = max(C["tie_max"], t)
        if per is not None: per.write(" ".join(f"{k} {row[k]}" for k in row) + "\n")
    return C

if __name__ == "__main__":
    a = sys.argv[1:]; eng, mode, nmov = a[0], a[1], int(a[2]); a = a[3:]; perfn = None
    if a[0] == "--per": perfn = a[1]; a = a[2:]
    for fn in a:
        per = open(perfn, "w") if perfn else None
        if eng == "s":
            import n5s237
            prio, owner, succ = n5s237.parse(fn); C = census_own(prio, owner, succ, mode, nmov, per); n = len(prio)
        else:
            C = census_lnew(fn, mode, nmov, per); n = sum(1 for l in open(fn)) - 1
        if per: per.close()
        C["tie"] = C["ptie"] + C["ctie"]
        keys = ("its", "fb", "a_steps", "choice", "tie", "ptie", "ctie", "tie_mov", "tie_its", "tie_max", "refuse", "refuse_strict", "b_steps", "bchoice", "btie", "fbtie", "opt_bad")
        print("TIE246", os.path.basename(fn), "n", n, "eng", eng, "mode", mode, "ctrl", CTRL, " ".join(f"{k} {C[k]}" for k in keys), flush=True)
