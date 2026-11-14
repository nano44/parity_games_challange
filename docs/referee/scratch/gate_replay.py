"""REFEREE successor 31: P-N5-GATE replay with own code (xicyc_replay.howard on own Γ / Γ3 builder; no lane code).
Engine: 'cyc' = IDEAL-CYC Howard on Γ(G); 'g3' = HOW3 (Howard on Γ3(G), states 0..T3, i.e. up to N5′-xi's first fallback).
Ties among best mover successors: keep current, else larger index (HOW3 allows any rule).
Counters (unit in brackets; all must be 0 except controls c* and sizes):
  grfail  flip at t whose LEFT face p has Ω_t(p) = Ω_(t-1)(p) (GATE-RACE (a))                         [flips]
  gr2fail gates with flips > min(ch_p + ch_q, 2 min(ch_p, ch_q) + 1) (GATE-RACE (b))                   [gates]
  trfail  left-face change inside a Λ-interval with E changed whose top leaves or is not on P_t(p)      [flips]
  glnfail LAM ∧ PRIV ∧ e_o∈E(p_e) states where the ⊴-order of the faces ≠ π-lex order, or π's equal  [(gate,state)]
  glnb    flips with LAM∧PRIV∧UP at t-1 and t and both π's unchanged (GATE-LOW-NULL (b))             [flips]
  glnb2   such flips with the same Λ at t-1, t where the face named by (b′) does not rise in π        [flips]
  k10     LAM ∧ PRIV ∧ not UP states (K10; 0 expected on both engines: R123 B-ONLY / CHAIN B-ONLY3)     [(gate,state)]
  npfail  NP states with σ̄(o) ≠ p_e, or P(p_b) ≠ A·o·P(p_e), or Λ unequal, or E(p_e) ⊄ E(p_b)        [(gate,state)]
  npboth  flips with NP on both sides; npkind  flips with NP before that are not relocks / after not unlocks [flips]
  relfail gates with relocks > ch_pe; unlfail gates with unlocks > 1 + relocks or unlocks > ch_pb      [gates]
  dpass   (gate, state) with e_o on P_t(D) (PROVISO; 0 expected on both engines)                      [(gate,state)]
  dexact  steps with e_o ∉ P(D) at t-1, t where (Ω(p_e) changes) ≠ (Ω(D) changes) (E-FACE-PAYS (b))     [(gate,step)]
  dfail   gates whose D avoids e_o all run and unlocks > 1 + ch_D (E-FACE-PAYS (c), first inequality)   [gates]
  cfail2  gates with ch_D > 2M+2 + Σ_J #E-changes of D in J + gam(D) (E-FACE-PAYS (c), second)          [gates]
  dflip   gates with flips > 2 lamch + 2 min_f nl_f + 1 (E-FACE-PAYS (d))                                [gates]
  sbfail  (x, t) with Ω_t(x) ≠ Ω_(t-1)(x) and no vertex of P_(t-1)(x) changing successor (STEP-BOUND)   [(vertex,step)]
  parfail changes of H = E(b) ∩ U_y (inside a Λ-interval of b, y ∈ {w} ∪ e-letters ≻ w) violating PARALLEL (i)-(iii) [changes]
  pefail  same-pair couples of expulsions of z at (b, J) where E(b′) ∩ U_z does not strictly lex-rise (PAIR-EXPEL) [couples]
  pjfail  same-pair expulsions not in one Λ-interval of b′                                              [pairs]
  ecfail  (b, J, z) with a_z > 1 + Σ_pairs Dhi_z(b′, J_b′) (EXPEL-COUNT, first inequality)             [tuples]
  plfail  runs with more than 3M distinct split pairs                                                   [runs]
  cfail   (v, I, y) with c_y(v, I) > a_y(v, I) (C ≤ A*_all, pointwise)                                  [tuples]
  afail   runs with A*_all > 1 + M·C;  a3fail runs with C > 3M (1 + M·A*_route)                          [runs]
Controls (must fire somewhere): cJoin flips whose JOINED face q is unchanged (the left-face test is not vacuous); cLow states where
the order disagrees with π taken BELOW e_o (π⁻ := E minus π); cNP NP states with σ̄(o) = p_b tested (= every NP state); cD steps where
(Ω(p_e) changes) ≠ (Ω(p_b) changes); cU couples tested with U_z := ∅ (= every couple).
Usage: gate_replay.py ENGINE CAP F.json ...   (ENGINE cyc | g3)"""
import sys, os, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xicyc_replay import howard

KEYS = ("grfail gr2fail trfail glnfail glnb glnb2 k10 npfail npboth npkind relfail unlfail dpass dexact dfail cfail2 dflip sbfail "
        "parfail pefail pjfail ecfail plfail cfail afail a3fail cJoin cLow cNP cD cU T gates flips couples parch maxC maxAall maxAroute "
        "maxflips").split()

def play(st, v):
    out, seen = [], set()
    while v not in seen: seen.add(v); out.append(v); v = st[v]
    return out, v            # path (prefix + cycle, each vertex once) and the re-entry vertex

def one(G, eng, cap, C):
    pad = eng == "g3"
    E, lab, ties, states, movers, idx = howard(G, pad, cap)
    n = E.n; N = G["N"]; rk = E.rk
    O = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]; M = len(O)
    evs = frozenset(idx[("e", q)] for q in O); gates = {idx[("g", q)]: q for q in O}
    T = len(states) - 1; C["T"] = max(C["T"], T)
    V = [s[2] for s in states]; ST = [s[1] for s in states]
    L = [[V[t][v][0] for v in range(n)] for t in range(T + 1)]
    Es = [[frozenset(V[t][v][1]) & evs for v in range(n)] for t in range(T + 1)]
    PL = {}
    def P(t, v):
        if (t, v) not in PL: PL[(t, v)] = play(ST[t], v)[0]
        return PL[(t, v)]
    ch = lambda v, t: E.cmp(V[t][v], V[t - 1][v]) != 0
    def top(S): return max(S, key=lambda z: rk[z])
    def lexgt(A, B):
        d = A ^ B
        return bool(d) and top(d) in A
    def ivl(v, t):
        a = t
        while a > 0 and L[a - 1][v] == L[t][v]: a -= 1
        b = t
        while b < T and L[b + 1][v] == L[t][v]: b += 1
        return a, b
    # ---- per gate
    for g, q in gates.items():
        C["gates"] += 1
        e = idx[("e", q)]; D = E.succ[e][0]
        pe, pb = (idx[("pe", q)], idx[("pbeta", q)]) if pad else (e, idx[("b", q)])
        pi = lambda S: frozenset(z for z in S if rk[z] >= rk[e])
        chp = {f: sum(ch(f, t) for t in range(1, T + 1)) for f in (pe, pb, D)}
        lamf = {f: sum(L[t][f] != L[t - 1][f] for t in range(1, T + 1)) for f in (pe, pb)}
        lamch = sum(L[t][pe] != L[t - 1][pe] or L[t][pb] != L[t - 1][pb] for t in range(1, T + 1))
        rel = unl = 0; davoid = True
        for t in range(T + 1):
            lam = L[t][pe] == L[t][pb]; priv = e not in Es[t][pb]; up = rk[e] > rk[L[t][pe]]
            if lam and priv and not up: C["k10"] += 1
            if lam and priv and e in Es[t][pe]:
                c = E.cmp(V[t][pe], V[t][pb]); a, b = pi(Es[t][pe]), pi(Es[t][pb])
                if a == b or (c > 0) != lexgt(a, b): C["glnfail"] += 1
                a2, b2 = Es[t][pe] - a, Es[t][pb] - b
                if a2 == b2 or (c > 0) != lexgt(a2, b2): C["cLow"] += 1
            if not priv:   # NP
                C["cNP"] += 1
                pp, pq = P(t, pb), P(t, pe)
                ok = ST[t][g] == pe and L[t][pe] == L[t][pb] and Es[t][pe] <= Es[t][pb] and g in pp
                if ok:
                    i = pp.index(g); ok = pp[i + 1:] == pq
                C["npfail"] += not ok
            if e in P(t, D): C["dpass"] += 1; davoid = False
        for t in range(1, T + 1):
            a0, a1 = e not in P(t - 1, D), e not in P(t, D)
            if a0 and a1 and ch(pe, t) != ch(D, t): C["dexact"] += 1
            if ch(pe, t) != ch(pb, t): C["cD"] += 1
            s0, s1 = ST[t - 1][g], ST[t][g]
            if s0 == s1: continue
            C["flips"] += 1; p, qf = s0, s1
            if s0 == pe: rel += 1
            else: unl += 1
            if not ch(p, t): C["grfail"] += 1
            if not ch(qf, t): C["cJoin"] += 1
            if L[t][p] == L[t - 1][p] and Es[t][p] != Es[t - 1][p]:
                x = top(Es[t][p] ^ Es[t - 1][p])
                if x not in Es[t][p] or x not in P(t, p): C["trfail"] += 1
            npb, npa = e in Es[t - 1][pb], e in Es[t][pb]
            if npb and npa: C["npboth"] += 1
            if (npb and s0 != pe) or (npa and s1 != pe): C["npkind"] += 1
            def lpu(s): return L[s][pe] == L[s][pb] and e not in Es[s][pb] and rk[e] > rk[L[s][pe]]
            if lpu(t - 1) and lpu(t):
                if pi(Es[t][pe]) == pi(Es[t - 1][pe]) and pi(Es[t][pb]) == pi(Es[t - 1][pb]): C["glnb"] += 1
                if L[t][pe] == L[t - 1][pe]:
                    f = pe if s0 == pe else pb
                    if not lexgt(pi(Es[t][f]), pi(Es[t - 1][f])): C["glnb2"] += 1
        fl = rel + unl; C["maxflips"] = max(C["maxflips"], fl)
        cp, cq = chp[pe], chp[pb]
        if fl > min(cp + cq, 2 * min(cp, cq) + 1): C["gr2fail"] += 1
        if rel > cp: C["relfail"] += 1
        if unl > 1 + rel or unl > cq: C["unlfail"] += 1
        if davoid and unl > 1 + chp[D]: C["dfail"] += 1
        if fl > 2 * lamch + 2 * min(cp - lamf[pe], cq - lamf[pb]) + 1: C["dflip"] += 1
        # (c) second inequality, read on D over the run
        lamD = sum(L[t][D] != L[t - 1][D] for t in range(1, T + 1))
        eD = sum(1 for t in range(1, T + 1) if L[t][D] == L[t - 1][D] and Es[t][D] != Es[t - 1][D])
        gam = sum(1 for t in range(1, T + 1) if ch(D, t) and L[t][D] == L[t - 1][D] and Es[t][D] == Es[t - 1][D])
        if lamD > 2 * M + 2 or chp[D] > lamD + eD + gam: C["cfail2"] += 1
    # ---- STEP-BOUND
    for t in range(1, T + 1):
        moved = {v for v in range(n) if ST[t][v] != ST[t - 1][v]}
        for x in range(n):
            if ch(x, t) and not (set(P(t - 1, x)) & moved): C["sbfail"] += 1
    # ---- PARALLEL, PAIR-EXPEL, EXPEL-COUNT, A*-EQUIV
    def split(b, t):        # first vertex of P_t(b) whose successor differs at t-1; its new successor
        for u in P(t, b):
            if ST[t][u] != ST[t - 1][u]: return u, ST[t][u]
        return None, None
    cmax = 0; aall = 0; aroute = 0; pairs_all = set(); ctab = {}
    route = set()
    for v in range(n):
        a = 0
        while a <= T:
            _, b_ = ivl(v, a); w = L[a][v]
            letters = sorted({z for t in range(a, b_ + 1) for z in Es[t][v]}, key=lambda z: rk[z])
            ys = [w] + [y for y in evs if rk[y] > rk[w]]
            # tops and runs
            cy = collections.Counter(); exps = collections.defaultdict(list)
            for t in range(a + 1, b_ + 1):
                if Es[t][v] != Es[t - 1][v]:
                    d = Es[t][v] ^ Es[t - 1][v]; cy[top(d)] += 1
                    u, nb = split(v, t)
                    if u is not None:
                        pairs_all.add((u, nb)); route.add(nb)
                    for z in Es[t - 1][v] - Es[t][v]: exps[z].append((t, u, nb))
            for y in ys:
                Uy = frozenset(z for z in evs if rk[z] > rk[y])
                for t in range(a + 1, b_ + 1):
                    H0, H1 = Es[t - 1][v] & Uy, Es[t][v] & Uy
                    if H0 == H1: continue
                    C["parch"] += 1; x = top(H0 ^ H1); u, _ = split(v, t)
                    p0, p1 = P(t - 1, v), P(t, v); bad = x not in H1 or x not in p1 or x in p0 or u is None
                    if not bad:
                        i1 = p1.index(u); bad = x not in p1[i1 + 1:]
                        i0 = p0.index(u) if u in p0 else None
                        for z in H0 - H1:
                            if z in p1 or z not in p0 or rk[z] >= rk[x] or i0 is None or z not in p0[i0 + 1:]: bad = True
                    C["parfail"] += bad
            for z in letters:
                runs = sum(1 for t in range(a, b_ + 1) if z in Es[t][v] and (t == a or z not in Es[t - 1][v]))
                aall = max(aall, runs)
                if cy[z] > runs: C["cfail"] += 1
                Uz = frozenset(y for y in evs if rk[y] > rk[z]); byp = collections.defaultdict(list)
                for (t, u, nb) in exps[z]: byp[(u, nb)].append(t)
                tot = 0
                for (u, nb), ts in byp.items():
                    J = {ivl(nb, t) for t in ts}
                    if len(J) > 1: C["pjfail"] += 1
                    ja, jb = min(J); tot += len({Es[s][nb] & Uz for s in range(ja, jb + 1)})
                    for i in range(len(ts)):
                        for j in range(i + 1, len(ts)):
                            C["couples"] += 1; C["cU"] += 1
                            if not lexgt(Es[ts[j]][nb] & Uz, Es[ts[i]][nb] & Uz): C["pefail"] += 1
                if runs > 1 + tot: C["ecfail"] += 1
            for y, c in cy.items(): cmax = max(cmax, c)
            a = b_ + 1
    for b in route:
        a = 0
        while a <= T:
            _, b_ = ivl(b, a)
            for z in {z for t in range(a, b_ + 1) for z in Es[t][b]}:
                aroute = max(aroute, sum(1 for t in range(a, b_ + 1) if z in Es[t][b] and (t == a or z not in Es[t - 1][b])))
            a = b_ + 1
    if len(pairs_all) > 3 * M: C["plfail"] += 1
    if aall > 1 + M * cmax: C["afail"] += 1
    if cmax > 3 * M * (1 + M * aroute): C["a3fail"] += 1
    C["maxC"] = max(C["maxC"], cmax); C["maxAall"] = max(C["maxAall"], aall); C["maxAroute"] = max(C["maxAroute"], aroute)
    return T

if __name__ == "__main__":
    eng, cap = sys.argv[1], int(sys.argv[2]); tot = collections.Counter()
    for f in sys.argv[3:]:
        C = collections.Counter(); one(json.load(open(f)), eng, cap, C)
        print(eng, os.path.basename(f), " ".join(f"{k} {C[k]}" for k in KEYS), flush=True)
        for k in KEYS:
            if k.startswith("max") or k == "T": tot[k] = max(tot[k], C[k])
            else: tot[k] += C[k]
    print(eng, "TOTAL", " ".join(f"{k} {tot[k]}" for k in KEYS), flush=True)
