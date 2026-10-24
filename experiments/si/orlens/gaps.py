#!/usr/bin/env python3
"""Gap levels and action elimination along N5 runs (docs/si/N5-OR-lens.md §2-§4).
Usage: gaps.py game.pg [start] [--verbose]
Per joint lambda-phase with target T = Xi at the phase's last state:
  E1  g_{k+1}(v) <= g_k(v) for every v (ultrametric monotonicity)                       -> violations counted
  E2  sigma_k(x) = z, x not a cycle node  =>  g_k(x) >= s(x,z) = lev(T(x), x+T(z))       -> violations counted
  E2' sbar_k(y) = e, y Odd not a cycle node =>  g_k(e) >= sbar(y,e) = lev(y+T(e), T(y))  -> violations counted
  flat = transition k -> k+1 with g_{k+1} == g_k pointwise; longest run of consecutive flat transitions;
  Gmax = max_v g_k(v); longest run with Gmax constant; total level drops sum_v (number of strict decreases of g(v)).
  returns: an Even vertex re-uses an edge it left earlier in the phase (count; slack level of the returned edge vs g)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortrace as OT

def analyse(path, start=None, verbose=False, check=True):
    g, st = OT.load(path, start)
    E, Ed, states, fbf, (it, fb) = OT.run_states(g, st)
    if check:
        it2, fb2, *_ = OT.N5.run(g, "n5", st)
        assert (it, fb) == (it2, fb2), (it, fb, it2, fb2)
    L = OT.Lex(E); n = g.n
    res = dict(n=n, it=it, fb=fb, phases=[])
    for ph in OT.phases(E, Ed, states):
        T = states[ph[-1]][2]
        lam = [T[v][0] for v in range(n)]
        G = [[L.lev(T[v], states[k][2][v]) for v in range(n)] for k in ph]
        e1 = e2 = e2o = 0; flat = []; drops = 0
        for i in range(len(ph)):
            sig, tau, vs, sbar = states[ph[i]][:4]
            for x in range(n):
                if lam[x] == x: continue
                if g.owner[x] == 0:
                    z = sig[x]; a = L.pre(x, T[z])
                    if L.le(a, T[x]) and G[i][x] < L.lev(T[x], a): e2 += 1
                else:
                    e = sbar[x]; a = L.pre(x, T[e])
                    if L.le(T[x], a) and G[i][e] < L.lev(a, T[x]): e2o += 1
            if i + 1 < len(ph):
                for v in range(n):
                    if G[i + 1][v] > G[i][v]: e1 += 1
                    if G[i + 1][v] < G[i][v]: drops += 1
                flat.append(G[i + 1] == G[i])
        def longest(bs):
            best = cur = 0
            for b in bs:
                cur = cur + 1 if b else 0; best = max(best, cur)
            return best
        gm = [max(r) for r in G]
        gmflat = [gm[i + 1] == gm[i] for i in range(len(gm) - 1)]
        # returns
        rets = 0; retinfo = []
        left = {}
        for i in range(1, len(ph)):
            s0, s1 = states[ph[i - 1]][0], states[ph[i]][0]
            for x in range(n):
                if g.owner[x] == 0 and s0[x] != s1[x]:
                    left.setdefault(x, set()).add(s0[x])
                    if s1[x] in left[x]:
                        rets += 1
                        a = L.pre(x, T[s1[x]])
                        retinfo.append((ph[i], x, s1[x], L.lev(T[x], a) if L.le(a, T[x]) else 'neg', G[i][x]))
        res["phases"].append(dict(states=(ph[0], ph[-1]), trans=len(ph) - 1, E1=e1, E2=e2, E2o=e2o, drops=drops,
                                  flat=sum(flat), flatrun=longest(flat), gmaxrun=longest(gmflat), returns=rets,
                                  fallbacks=sum(fbf[k] for k in ph[:-1] if k < len(fbf))))
        if verbose:
            print(f"phase {ph[0]}..{ph[-1]}")
            for i, k in enumerate(ph):
                print(f"  k={k:3d} fb={fbf[k] if k < len(fbf) else '-'} g=" + " ".join('.' if x < 0 else str(x) for x in G[i]))
            for r in retinfo: print("  return", r)
    return res

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    r = analyse(args[0], args[1] if len(args) > 1 else None, "--verbose" in sys.argv)
    print(f"{os.path.basename(args[0])} n={r['n']} iterations={r['it']} fallbacks={r['fb']}")
    for p in r["phases"]:
        if p["trans"] == 0: continue
        print("  phase", p)
