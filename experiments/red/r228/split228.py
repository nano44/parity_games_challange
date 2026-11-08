#!/usr/bin/env python3
"""L-RED 62 R228 item 1: INDEPENDENT all-pairs census for L-NEW 66 BOX 199 Addenda 2-3 (claude/l-new 91ed2f3f, 42e9c728) on R221 own.py
(IDEAL-CYC Howard, my own Gamma: gate g = (x, k) Odd with faces e(g), b(g); no pads; the genome's start). No L-NEW code.
Per (v, maximal Lambda-interval I), each change t-1 -> t of E(v) (e-vertices of Pi(v)) has a top (most relevant changed e) and a split pair
(u, b): u = first vertex of the play at t whose successor differs from t-1, b = its new successor. For a letter y: U_y(S) = S ∩ {e more
relevant than y}; wt(y) = the successor of the e-vertex y (a mover, or c_W). For EVERY pair t < t' of y-tops of (v, I) with equal split
pair (u, b) (a "same-pair couple"; a := u's successor at t' - 1):
  dn2  (PAIR-SPLIT (a')): not val_(t'-1)(a) > val_t(b)                      rh2 (PAIR-SPLIT (c')): not U_y(E_t'(b)) >lex U_y(E_t(b))
  rw2  (CONJECTURE RW-WT*, strong form): U_y(E_t(wt(y))) == U_y(E_t'(wt(y)))
  rw2w (weak form): U_y(E(wt(y))) takes < 2 values on [t, t']
  b0s  (CONJECTURE RW-B0*): b's play at t or at t' holds a U_y-letter before y
Per (v, I, y) with c_y >= 1 tops:
  sp   (Corollary SPLIT-COUNT): c_y > sum over its split pairs (u, b) of Dhi_y(b, J_b), J_b = b's maximal Lambda-interval holding the first
       y-top through (u, b), Dhi = #distinct U_y(E(b)) on J_b;     jbfail: a later y-top through (u, b) outside J_b (must be 0, F1/F2)
  spw  (C-WT, first inequality): c_y > sum over (u, b) of #values of U_y(E(wt(y))) on the span of the y-tops through (u, b)
  spl3m: #split pairs > 3M;   nspl = max #split pairs per (v, I, y);  C = max c_y.
  Dwt  := max over (v, I, y) of Dhi_y(wt(y), J), J = wt(y)'s maximal Lambda-interval holding y's first top (the open core of Add. 2 A2.4);
  DwtJ := the same over ALL Lambda-intervals J of wt(y) for every letter y that is a top somewhere (context, not a claim).
Units: couple (dn2, rh2, rw2, rw2w, b0s), triple (v, I, y) (sp, spw, jbfail, spl3m); couples = #same-pair couples; all counters are TOTALS,
C / nspl / Dwt / DwtJ are per-unit MAXIMA. Control CTRL=uy (U_y := empty set): rh2 must fire on every couple.
Usage: split228.py G.json ...   (census(G, cap) for climbs)"""
import sys, os, json, collections
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r221")]
import own
CTRL = os.environ.get("CTRL", "")
def census(G, cap=3000):
    out, V, O, ow = own.run(G, cap); n, prio, o_, succ, _, _ = own.build(G); vj = own.VJ(prio); rk = vj.rk; N = G["N"]
    M = len(O); evs = {V[("e", q)] for q in O}; T = len(out) - 1
    nx = [[s[u] if u < N else (tau[u] if o_[u] == 1 else succ[u][0]) for u in range(n)] for (s, vals, tau) in out]
    def play(t, v):
        p = []; seen = set(); u = v
        while u not in seen: seen.add(u); p.append(u); u = nx[t][u]
        return p
    Ec = {}
    def E(t, v):
        k = (t, v)
        if k not in Ec: Ec[k] = frozenset(e for e in out[t][1][v][1] if e in evs)
        return Ec[k]
    lam = lambda t, v: out[t][1][v][0]
    def interval(v, t):                     # maximal Lambda-interval of v holding t
        a = t
        while a > 0 and lam(a - 1, v) == lam(t, v): a -= 1
        b = t
        while b < T and lam(b + 1, v) == lam(t, v): b += 1
        return a, b
    def lexgt(A, B):
        d = A ^ B
        return bool(d) and max(d, key=lambda e: rk[e]) in A
    c = collections.Counter(T=T)
    for k in ("couples", "dn2", "rh2", "rw2", "rw2w", "b0s", "sp", "spw", "jbfail", "spl3m", "C", "nspl", "Dwt", "DwtJ"): c[k] = 0
    topletters = set()
    for v in range(n):
        t = 0
        while t <= T:
            u_ = t
            while u_ + 1 <= T and lam(u_ + 1, v) == lam(t, v): u_ += 1
            tops = []; split = {}
            for i in range(t + 1, u_ + 1):
                A, B = E(i - 1, v), E(i, v)
                if A == B: continue
                z = max(A ^ B, key=lambda e: rk[e]); tops.append((i, z))
                uu = next(x for x in play(i, v) if nx[i][x] != nx[i - 1][x]); split[i] = (uu, nx[i][uu])
            t = u_ + 1
            by = collections.defaultdict(list)
            for i, z in tops: by[z].append(i)
            for y, ts in by.items():
                topletters.add(y); wty = nx[0][y]
                Uy = (lambda S: frozenset()) if CTRL == "uy" else (lambda S, y=y: frozenset(e for e in S if rk[e] > rk[y]))
                c["C"] = max(c["C"], len(ts))
                grp = collections.defaultdict(list)
                for i in ts: grp[split[i]].append(i)
                c["nspl"] = max(c["nspl"], len(grp)); c["spl3m"] += len(grp) > 3 * M
                s_sp = 0; s_spw = 0
                for (uu, b), L in grp.items():
                    ja, jb = interval(b, L[0])
                    if any(not (ja <= i <= jb) for i in L): c["jbfail"] += 1
                    s_sp += len({Uy(E(s, b)) for s in range(ja, jb + 1)})
                    s_spw += len({Uy(E(s, wty)) for s in range(L[0], L[-1] + 1)})
                    for x in range(len(L)):
                        for w_ in range(x + 1, len(L)):
                            t1, t2 = L[x], L[w_]; a = nx[t2 - 1][uu]; c["couples"] += 1
                            if not vj.cmp(out[t2 - 1][1][a], out[t1][1][b]) > 0: c["dn2"] += 1
                            if not lexgt(Uy(E(t2, b)), Uy(E(t1, b))): c["rh2"] += 1
                            if Uy(E(t1, wty)) == Uy(E(t2, wty)): c["rw2"] += 1
                            if len({Uy(E(s, wty)) for s in range(t1, t2 + 1)}) < 2: c["rw2w"] += 1
                            for tt in (t1, t2):
                                pb = play(tt, b); pre = pb[:pb.index(y)] if y in pb else pb
                                if any(e in evs and rk[e] > rk[y] for e in pre): c["b0s"] += 1; break
                c["sp"] += len(ts) > s_sp; c["spw"] += len(ts) > s_spw
                ja, jb = interval(wty, ts[0])
                c["Dwt"] = max(c["Dwt"], len({Uy(E(s, wty)) for s in range(ja, jb + 1)}))
    for y in topletters:
        wty = nx[0][y]; s = 0
        while s <= T:
            a, b = interval(wty, s)
            c["DwtJ"] = max(c["DwtJ"], len({frozenset(e for e in E(r, wty) if rk[e] > rk[y]) for r in range(a, b + 1)})); s = b + 1
    return c
K = ("T", "couples", "dn2", "rh2", "rw2", "rw2w", "b0s", "sp", "spw", "jbfail", "spl3m", "C", "nspl", "Dwt", "DwtJ")
if __name__ == "__main__":
    print("instance N+M", " ".join(K))
    for f in sys.argv[1:]:
        G = json.load(open(f)); G = G.get("genome", G); c = census(G)
        print(os.path.basename(f), G["N"] + sum(len(o) for o in G["opts"]), " ".join(str(c[k]) for k in K), flush=True)
