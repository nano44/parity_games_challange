#!/usr/bin/env python3
"""L-RED 62 R228 (A): INDEPENDENT census for L-SI 48 BOX 91 (claude/l-si c59e3182) on R221 own.py (IDEAL-CYC Howard, pad-free Γ, the
genome's start, cap 3000). No L-SI / L-NEW code. For every vertex b and maximal Λ-interval J of b (Λ = w), E_r(b) = e-vertices of b's
play more relevant than w (own.py's value set). At each change r-1 -> r of E(b) in J: top x (most relevant of the difference), expelled
Z = E_(r-1)(b) \\ E_r(b), b's split u' (first vertex of the play at r whose successor differs) and its new successor b'.
  par1 (PARALLEL (i)): x not on b's new play, or x on the old play, or some z in Z on the new play / not on the old play
  par2 (PARALLEL (ii)): some z in Z not less relevant than x
  par3 (PARALLEL (iii)): some z in Z not strictly after u' on the old play, or x not strictly after u' on the new play
  pefail (PAIR-EXPEL): for ANY two expulsions s < s' of the same z at (b, J) through the same split pair (u', b'):
          not  U_z(E_s'(b')) >lex U_z(E_s(b'))   (U_z = e-vertices more relevant than z);   pelam: Λ(b') differs at s and s'
  ecfail (EXPEL-COUNT): a_z(b, J) > 1 + Σ_(u',b') Dhi_z(b', J_b')  (Dhi over b''s full Λ-interval holding its first expulsion of z)
  Astar := max over (b, J, z) of a_z(b, J) = #maximal presence runs of z in E(b) on J (a PER-TUPLE MAXIMUM; U := all letters above w)
  C (max c_y per (v, I, y), own census), couples / expulsions are TOTALS.
Control CTRL=uz (U_z := ∅): pefail must fire on every couple.  Usage: expel228.py G.json ...   (census(G, cap) for climbs)"""
import sys, os, json, collections
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r221")]
import own
CTRL = os.environ.get("CTRL", "")
def census(G, cap=3000):
    out, V, O, ow = own.run(G, cap); n, prio, o_, succ, _, _ = own.build(G); rk = own.VJ(prio).rk; N = G["N"]
    evs = {V[("e", q)] for q in O}; T = len(out) - 1
    nx = [[s[u] if u < N else (tau[u] if o_[u] == 1 else succ[u][0]) for u in range(n)] for (s, vals, tau) in out]
    def play(t, v):
        p = []; seen = set(); u = v
        while u not in seen: seen.add(u); p.append(u); u = nx[t][u]
        return p
    Ec = {}
    def E(t, v):
        if (t, v) not in Ec: Ec[(t, v)] = frozenset(e for e in out[t][1][v][1] if e in evs)
        return Ec[(t, v)]
    lam = lambda t, v: out[t][1][v][0]
    def interval(v, t):
        a = t
        while a > 0 and lam(a - 1, v) == lam(t, v): a -= 1
        b = t
        while b < T and lam(b + 1, v) == lam(t, v): b += 1
        return a, b
    def lexgt(A, B):
        d = A ^ B
        return bool(d) and max(d, key=lambda e: rk[e]) in A
    c = collections.Counter(T=T)
    for k in ("par1", "par2", "par3", "pefail", "pelam", "ecfail", "couples", "expulsions", "Astar", "C"): c[k] = 0
    for b in range(n):
        t = 0
        while t <= T:
            a_, b_ = interval(b, t); t = b_ + 1
            runs = collections.Counter(); prev = frozenset(); exp = collections.defaultdict(list)
            for r in range(a_, b_ + 1):
                cur = E(r, b)
                for z in cur - prev: runs[z] += 1
                if r > a_ and cur != prev:
                    x = max(cur ^ prev, key=lambda e: rk[e]); Z = prev - cur
                    pn, po = play(r, b), play(r - 1, b)
                    uu = next(q for q in pn if nx[r][q] != nx[r - 1][q]); bb = nx[r][uu]
                    if x not in pn or x in po or any(z in pn or z not in po for z in Z): c["par1"] += 1
                    if any(rk[z] >= rk[x] for z in Z): c["par2"] += 1
                    iu_o, iu_n = po.index(uu), pn.index(uu)
                    if any(z in po and po.index(z) <= iu_o for z in Z) or (x in pn and pn.index(x) <= iu_n): c["par3"] += 1
                    for z in Z: exp[z].append((r, uu, bb)); c["expulsions"] += 1
                prev = cur
            if runs: c["Astar"] = max(c["Astar"], max(runs.values()))
            for z, L in exp.items():
                Uz = (lambda S: frozenset()) if CTRL == "uz" else (lambda S, z=z: frozenset(e for e in S if rk[e] > rk[z]))
                grp = collections.defaultdict(list)
                for r, uu, bb in L: grp[(uu, bb)].append(r)
                bound = 1
                for (uu, bb), rs in grp.items():
                    ja, jb = interval(bb, rs[0]); bound += len({Uz(E(s, bb)) for s in range(ja, jb + 1)})
                    for i in range(len(rs)):
                        for j in range(i + 1, len(rs)):
                            s1, s2 = rs[i], rs[j]; c["couples"] += 1
                            if lam(s1, bb) != lam(s2, bb): c["pelam"] += 1
                            if not lexgt(Uz(E(s2, bb)), Uz(E(s1, bb))): c["pefail"] += 1
                if runs[z] > bound: c["ecfail"] += 1
    # C: max c_y over (v, I, y) (tops = most relevant element of each change)
    for v in range(n):
        t = 0
        while t <= T:
            a_, b_ = interval(v, t); t = b_ + 1; cnt = collections.Counter()
            for r in range(a_ + 1, b_ + 1):
                A, B = E(r - 1, v), E(r, v)
                if A != B: cnt[max(A ^ B, key=lambda e: rk[e])] += 1
            if cnt: c["C"] = max(c["C"], max(cnt.values()))
    return c
K = ("T", "C", "Astar", "expulsions", "couples", "par1", "par2", "par3", "pefail", "pelam", "ecfail")
if __name__ == "__main__":
    print("instance N+M", " ".join(K))
    for f in sys.argv[1:]:
        G = json.load(open(f)); G = G.get("genome", G); c = census(G)
        print(os.path.basename(f), G["N"] + sum(len(o) for o in G["opts"]), " ".join(str(c[k]) for k in K), flush=True)
