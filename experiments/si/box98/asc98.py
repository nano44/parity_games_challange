#!/usr/bin/env python3
"""L-SI box 98: ascents of the e-sequences on one run, two engines (box91/mult91.py engines). seq_t(v) := the e-vertices of P_t(v) more
relevant than Lambda_t(v), in play order; an ascent = a step to a more relevant element (RESULTS R121 / P-N5-CHAIN §7). Records per genome:
U (options with a Xi-target of higher level), T (= T3 on g3, T_CYC on own), maxasc = max over (t, v) of the ascents of seq_t(v),
Dmax = max over v of D^tot_E(v) (distinct (Lambda, E) pairs of v over the run), sumD = sum_v (D^tot_E(v) - 1), upfail = (t, v) with more
ascents than U (UP-B / UP-B3: must be 0 under [E-LEV]).
Usage: asc98.py own|g3 G.json ...   (OWN_DIR / ROOT as for box91/mult91.py)"""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box91"))
import mult91
def Uof(G):
    lev = G["lev"]; return sum(1 for x in range(G["N"]) for (wt, xt, b) in G["opts"][x] if xt >= 0 and lev[xt] > lev[x])
def run(G, T, n, nx, lam, E, rk, evs, odd2, val):
    U = Uof(G); maxasc = upfail = 0; cls = [set() for _ in range(n)]
    for t in range(T + 1):
        for v in range(n):
            p = []; seen = set(); u = v
            while u not in seen: seen.add(u); p.append(u); u = nx(t, u)
            L = lam(t, v); seq = [x for x in p if x in evs and rk[x] > rk[L]]
            a = sum(1 for i in range(1, len(seq)) if rk[seq[i]] > rk[seq[i - 1]])
            maxasc = max(maxasc, a); upfail += a > U
            cls[v].add((L, frozenset(seq)))
    D = [len(c) for c in cls]
    return dict(U=U, T=T, maxasc=maxasc, Dmax=max(D), sumD=sum(d - 1 for d in D), upfail=upfail)
if __name__ == "__main__":
    eng = sys.argv[1]; K = ("U", "T", "maxasc", "Dmax", "sumD", "upfail")
    print("engine", eng, "instance N M", " ".join(K), flush=True)
    for f in sys.argv[2:]:
        G = json.load(open(f)); G = G.get("genome", G)
        c = run(G, *(mult91.eng_own(G) if eng == "own" else mult91.eng_g3(G)))
        print(eng, os.path.basename(f), G["N"], sum(len(o) for o in G["opts"]), " ".join(str(c[k]) for k in K), flush=True)
