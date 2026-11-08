#!/usr/bin/env python3
"""L-SI box 91: the expulsion structure of the high parts at SPLIT-COUNT's route vertices b, on two engines.
Setting (L-NEW box 199 Add. 2, claude/l-new 91ed2f3f): per (v, maximal Lambda-interval I) each change of E(v) has a top and a split pair
(u, b) (u = first vertex of v's play at t whose successor changed, b = its new successor); for a letter y with tops at (v, I), J_b = b's
maximal Lambda-interval holding the first y-top through (u, b); H_s := E_s(b) ∩ U_y (U_y = e-vertices more relevant than y), s in J_b.
Dhi_y(b, J_b) = #distinct H_s (SPLIT-COUNT's summand).
Box 91 objects at one tuple (b, J, y) (cached; every b, J, y reached from some (v, I, y, (u, b))):
  a change s-1 -> s of H; x := its top (most relevant e of the symmetric difference); Z := H_(s-1) \\ H_s (EXPELLED letters).
  x EXPELS z when z in Z.  X(z) := the letters that expel z somewhere in J.  a_z := #maximal runs of s in J with z in H_s (presences).
  P_X(z) := 1 + sum_(x in X(z)) P_X(x) (paths in the expulsion DAG; edges z -> x go up in relevance).
Counters (must be 0; unit: change of H for par*, tuple (b, J, y) for the rest; all TOTALS):
  par1 : an expelled z lies on b's NEW play at s, or x lies on b's OLD play at s-1      [Lemma PARALLEL (i)]
  par2 : an expelled z is not less relevant than x                                         [Lemma PARALLEL (ii)]
  par3 : an expelled z lies on the common prefix (up to and including b's split u')      [Lemma PARALLEL (iii)]
  lexfail: x not in H_s (top must enter)                                                   [E-MON3]
  afail: a_z > 1 + sum_(x in X(z)) a_x                                                     [Corollary EXP-PATHS (a)]
  pxfail: Dhi > 1 + sum_z (P_X(z) restricted to a_z >= 1)                                  [Corollary EXP-PATHS (b)]
  dhifail: Dhi - 1 != #changes of H on J                                                   [lex-monotone; E-MON3]
  spfail: c_y(v, I) > sum_(u,b) Dhi_y(b, J_b)                                              [SPLIT-COUNT, box 199 Add. 2]
Records (per-tuple MAXIMA over the genome unless said): C = max c_y(v, I); Dhib = max Dhi; sumD = max_(v,I,y) sum_(u,b) Dhi (= L-RED R228's);
  maxa = max a_z; Xdep = longest chain in the expulsion DAG; Xfan = max |X(z)|; maxPX = max P_X(z); mexp = max #expulsions of one z by one x;
  nexp = max #expulsions at one tuple; seg2 = TOTAL changes whose expelled letters are not all on the first divergent segment of the old play
  (multi-switch Howard steps; DATA, no claim); tuples = TOTAL distinct (b, J, y) analysed.
Lemma GATE-RACE (unit: Odd vertex o with two successors p, q; whole run; TOTALS): flips = #t with o's choice changed; ch_p, ch_q = #t with
  the value of p / q changed.  grfail: flips > ch_p + ch_q;  gr2fail: flips > 2 min(ch_p, ch_q) + 1;  grwhy: a flip at t where the face
  Odd LEAVES did not change value at t (the proof's step).
  Lemma TRIGGER (same unit; TOTALS over flips): the left face L's change at t is a Lambda change (fl_lam), else an e-set change (fl_e), else
  length only (fl_len); trfail: an fl_e flip whose top x is not on L's play at t (or not in E_t(L)); maxlamfl = max fl_lam at one o.  maxflip = max flips (maximum); gtight = #o with flips >= 2 at the bound.
Lemma PAIR-EXPEL / Corollary EXPEL-COUNT (unit: couple s < s' of expulsions of one z at (b, J) through the same split pair (u', b') of b's
  plays, u' = b's split at the expulsion, b' its new successor; TOTALS): pefail: E_s'(b') ∩ U_z not >lex E_s(b') ∩ U_z;
  ecfail (unit (b, J, y, z)): a_z > 1 + sum over z's expulsion pairs of Dhi_z(b', J_b'); pelam: an expulsion pair with Lambda(b') != Lambda(b)
  (must be 0: b' lies on b's play); nexpl = max #expulsion split pairs of one z (maximum); pecouples = #couples.
Controls (CTRL env): "uz" sets U_z := empty in PAIR-EXPEL (pefail fires on every couple); "gr" lowers gr2fail's bound by 1 (fires where the bound is tight); "a0" drops the 1 in afail's bound (a_z <= sum a_x: fires at every first presence); "pre" counts par3 on the WHOLE old
play instead of the prefix (fires at every expulsion).
Engines (read-only pinned copies, see pins.txt): own = L-RED R221 own.py ($OWN_DIR); g3 = L-NEW's Gamma3 N5'-xi run from S3 ($ROOT tree).
Usage: mult91.py own|g3 G.json ..."""
import sys, os, json, collections
CTRL = os.environ.get("CTRL", "")

def eng_own(G, cap=3000):
    sys.path.insert(0, os.environ["OWN_DIR"]); import own
    out, V, O, _ = own.run(G, cap); n, prio, o_, succ, _, _ = own.build(G); rk = own.VJ(prio).rk; N = G["N"]
    evs = {V[("e", q)] for q in O}; T = len(out) - 1
    nx = [[s[u] if u < N else (tau[u] if o_[u] == 1 else succ[u][0]) for u in range(n)] for (s, vals, tau) in out]
    lam = lambda t, v: out[t][1][v][0]
    Ec = {}
    def E(t, v):
        k = (t, v)
        if k not in Ec: Ec[k] = frozenset(e for e in out[t][1][v][1] if e in evs)
        return Ec[k]
    odd2 = [(u, succ[u][0], succ[u][1]) for u in range(N, n) if o_[u] == 1 and len(succ[u]) == 2]
    return T, n, (lambda t, x: nx[t][x]), lam, E, rk, evs, odd2, (lambda t, v: out[t][1][v])

def eng_g3(G, cap=20000):
    R = os.environ["ROOT"]; os.environ.setdefault("EG195_ROOT", R)
    sys.path[:0] = [os.path.join(R, p) for p in ("experiments/new/box195", "experiments/new/box191", "experiments/new/box189",
                    "experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
    import eg195, gamma3, n5v, n5x
    g0, _, _, V = gamma3.build(G, eg195.PADS); g = eg195.topg(g0); n = g.n; name = {v: k for k, v in V.items()}
    E_, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E_, Ed, None)
    evs = {v for v in range(n) if isinstance(name[v], tuple) and name[v][0] == "e"}; bit = {E_.bit[f]: f for f in evs}
    ES = sum(bit); H = []
    while len(H) <= cap:
        vs, tb = E_.evaluate(tuple(sigma)); H.append((tuple(sigma), vs, tb))
        res = n5v.step(g, E_, Ed, sigma, tau, "xi")
        if res is None or res[4]: break
        sigma, tau = res[0], res[1]
    T = len(H) - 1
    nx = lambda t, x: H[t][0][x] if g.owner[x] == 0 else H[t][2][x]
    lam = lambda t, v: H[t][1][v][0]
    Ec = {}
    def E(t, v):
        k = (t, v)
        if k not in Ec:
            m = H[t][1][v][1] & ES; Ec[k] = frozenset(f for b, f in bit.items() if m & b)
        return Ec[k]
    odd2 = [(x, g.succ[x][0], g.succ[x][1]) for x in range(n) if g.owner[x] == 1 and len(g.succ[x]) == 2]
    return T, n, nx, lam, E, E_.rank, evs, odd2, (lambda t, v: E_.key(H[t][1][v]))

def census(T, n, nx, lam, E, rk, evs, odd2, val):
    def play(t, v):
        p = []; seen = set(); u = v
        while u not in seen: seen.add(u); p.append(u); u = nx(t, u)
        return p
    def interval(v, t):
        a = t
        while a > 0 and lam(a - 1, v) == lam(t, v): a -= 1
        b = t
        while b < T and lam(b + 1, v) == lam(t, v): b += 1
        return a, b
    top = lambda d: max(d, key=lambda e: rk[e])
    c = collections.Counter(T=T)
    for k in ("par1", "par2", "par3", "lexfail", "afail", "pxfail", "dhifail", "spfail", "C", "Dhib", "sumD", "maxa", "Xdep", "Xfan",
              "maxPX", "mexp", "nexp", "seg2", "tuples", "grfail", "gr2fail", "grwhy", "maxflip", "gtight",
              "fl_lam", "fl_e", "fl_len", "trfail", "maxlamfl", "pecouples", "pefail", "ecfail", "pelam", "nexpl"): c[k] = 0
    lamfl = collections.Counter()
    for (o, p, q) in odd2:                              # Lemma GATE-RACE (whole run)
        fl = chp = chq = 0; why = 0
        for t in range(1, T + 1):
            dp, dq = val(t, p) != val(t - 1, p), val(t, q) != val(t - 1, q); chp += dp; chq += dq
            if nx(t, o) != nx(t - 1, o):
                fl += 1; left = nx(t - 1, o)              # the face Odd leaves must have changed value at t
                if not (dp if left == p else dq): why += 1
                if lam(t, left) != lam(t - 1, left): c["fl_lam"] += 1; lamfl[o] += 1
                elif E(t, left) != E(t - 1, left):
                    c["fl_e"] += 1; x = top(E(t, left) ^ E(t - 1, left))
                    if x not in E(t, left) or x not in set(play(t, left)): c["trfail"] += 1
                else: c["fl_len"] += 1
        bound = 2 * min(chp, chq) + 1 - (1 if CTRL == "gr" else 0)
        c["grfail"] += fl > chp + chq; c["gr2fail"] += fl > bound; c["grwhy"] += why
        c["maxflip"] = max(c["maxflip"], fl); c["gtight"] += fl >= 2 and fl == 2 * min(chp, chq) + 1
    c["maxlamfl"] = max(lamfl.values(), default=0)
    cache = {}
    def tuple_(b, J, y):
        key = (b, J, y)
        if key in cache: return cache[key]
        ja, jb = J; ry = rk[y]
        Hs = [frozenset(e for e in E(s, b) if rk[e] > ry) for s in range(ja, jb + 1)]
        dhi = len(set(Hs)); nch = 0; X = collections.defaultdict(set); mex = collections.Counter(); nexp = 0
        ex = collections.defaultdict(list)
        for i in range(1, len(Hs)):
            A, B = Hs[i - 1], Hs[i]
            if A == B: continue
            nch += 1; s = ja + i; x = top(A ^ B); Z = A - B
            if x not in B: c["lexfail"] += 1
            if Z:
                P0, P1 = play(s - 1, b), play(s, b); S1 = set(P1); S0 = set(P0)
                if any(z in S1 for z in Z) or x in S0: c["par1"] += 1
                if any(rk[z] >= rk[x] for z in Z): c["par2"] += 1
                j = 0
                while j + 1 < min(len(P0), len(P1)) and P0[j + 1] == P1[j + 1]: j += 1
                pre = set(P0) if CTRL == "pre" else set(P0[:j + 1])
                if any(z in pre for z in Z): c["par3"] += 1
                k = j + 1                                   # first divergent old segment: P0[j+1 .. first vertex also on P1)
                while k < len(P0) and P0[k] not in S1: k += 1
                seg = set(P0[j + 1:k])
                if any(z not in seg for z in Z): c["seg2"] += 1
                for z in Z: X[z].add(x); mex[(z, x)] += 1; ex[z].append((s, (P1[j], P1[j + 1] if j + 1 < len(P1) else None)))
                nexp += len(Z)
        if dhi - 1 != nch: c["dhifail"] += 1
        letters = set().union(*Hs) if Hs else set()
        a = {}
        for z in letters:
            runs = 0; prev = False
            for h in Hs:
                cur = z in h
                if cur and not prev: runs += 1
                prev = cur
            a[z] = runs
        one = 0 if CTRL == "a0" else 1
        for z in letters:
            if a[z] > one + sum(a.get(x, 0) for x in X[z]): c["afail"] += 1
        PX = {}; dep = {}
        for z in sorted(letters | set(X), key=lambda e: -rk[e]):
            PX[z] = 1 + sum(PX[x] for x in X[z]); dep[z] = 1 + max((dep[x] for x in X[z]), default=0)
        if dhi > 1 + sum(PX[z] for z in letters if a[z] >= 1): c["pxfail"] += 1
        for z, L in ex.items():                         # Lemma PAIR-EXPEL / Corollary EXPEL-COUNT
            rz = rk[z]; Uz = (lambda S: frozenset()) if CTRL == "uz" else (lambda S, rz=rz: frozenset(e for e in S if rk[e] > rz))
            grp = collections.OrderedDict()
            for s_, pr in L: grp.setdefault(pr, []).append(s_)
            tot = 0
            for (u2, b2), ss in grp.items():
                if b2 is None or lam(ss[0], b2) != lam(ss[0], b) or any(lam(s_, b2) != lam(ss[0], b2) for s_ in ss): c["pelam"] += 1; continue
                ja2, jb2 = interval(b2, ss[0]); tot += len({Uz(E(r, b2)) for r in range(ja2, jb2 + 1)})
                for i1 in range(len(ss)):
                    for i2 in range(i1 + 1, len(ss)):
                        c["pecouples"] += 1; A2, B2 = Uz(E(ss[i2], b2)), Uz(E(ss[i1], b2))
                        d = A2 ^ B2
                        if not (d and top(d) in A2): c["pefail"] += 1
            if a[z] > 1 + tot: c["ecfail"] += 1
            c["nexpl"] = max(c["nexpl"], len(grp))
        c["tuples"] += 1; c["Dhib"] = max(c["Dhib"], dhi); c["maxa"] = max([c["maxa"]] + list(a.values()))
        c["Xdep"] = max([c["Xdep"]] + [dep[z] - 1 for z in letters]); c["Xfan"] = max([c["Xfan"]] + [len(X[z]) for z in letters])
        c["maxPX"] = max([c["maxPX"]] + [PX[z] for z in letters]); c["mexp"] = max([c["mexp"]] + list(mex.values()))
        c["nexp"] = max(c["nexp"], nexp)
        cache[key] = dhi
        return dhi
    for v in range(n):
        t = 0
        while t <= T:
            u_ = t
            while u_ + 1 <= T and lam(u_ + 1, v) == lam(t, v): u_ += 1
            by = collections.defaultdict(list)
            for i in range(t + 1, u_ + 1):
                A, B = E(i - 1, v), E(i, v)
                if A == B: continue
                y = top(A ^ B); uu = next(q for q in play(i, v) if nx(i, q) != nx(i - 1, q)); by[y].append((i, (uu, nx(i, uu))))
            t = u_ + 1
            for y, L in by.items():
                c["C"] = max(c["C"], len(L)); grp = collections.OrderedDict()
                for i, pr in L: grp.setdefault(pr, []).append(i)
                s_sp = 0
                for (uu, b), ts in grp.items(): s_sp += tuple_(b, interval(b, ts[0]), y)
                c["sumD"] = max(c["sumD"], s_sp); c["spfail"] += len(L) > s_sp
    return c

K = ("T", "C", "Dhib", "sumD", "maxa", "Xdep", "Xfan", "maxPX", "mexp", "nexp", "seg2", "tuples",
     "par1", "par2", "par3", "lexfail", "afail", "pxfail", "dhifail", "spfail", "maxflip", "gtight", "grfail", "gr2fail", "grwhy",
     "fl_lam", "fl_e", "fl_len", "maxlamfl", "trfail", "pecouples", "nexpl", "pefail", "ecfail", "pelam")
if __name__ == "__main__":
    eng = sys.argv[1]; print("engine", eng, "instance N+M", " ".join(K), flush=True)
    for f in sys.argv[2:]:
        G = json.load(open(f)); G = G.get("genome", G)
        c = census(*(eng_own(G) if eng == "own" else eng_g3(G)))
        print(eng, os.path.basename(f), G["N"] + sum(len(o) for o in G["opts"]), " ".join(str(c[k]) for k in K), flush=True)
