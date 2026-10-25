#!/usr/bin/env python3
"""Box 42 (L-RED successor 18): K survey (wakes per phase), from the definition in RESULTS R27 (setting paragraph; = P-N5-LP §3):
  RELEVANT CHANGE at k → k+1: Even y with σ_{k+1}(y) ≠ σ_k(y) and λ_k(y) ≠ y, or Odd u with σ̄_{k+1}(u) ≠ σ̄_k(u) and λ_k(u) ≠ u.
  L_k := max lev(Ξ_k(old), Ξ_k(new)) over relevant changes (⊥ if none); NU if L_k = ⊥, RELEVANT otherwise.
  WAKE at k′: a relevant Even switch at k′ of level > L_k, where k < k′ are consecutive relevant transitions of the phase (only NU
  between), no fallback in [k, k′] (transitions k..k′), and R constant on [k, k′+1].
Counts per phase: Kt = #transitions with a wake (LEDGER-v2 §3 wording), Ks = #wake switches (R27 "K := #wakes"); wakes split by the
state type at k′ (H1/H2 flags: U1 = H1∧H2, U2 = ¬H1∧H2, U3 = H1∧¬H2, U23 = ¬H1∧¬H2).
Usage: k18.py [--start f.json] game.pg ...   one line per file: n, iterations, phases, max Kt / Ks per phase, total, by type."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "so"))
import sox, ex16
from sox import lev, BOT

def analyse(g, st=None, cap=2000):
    o = sox.oddchoice(g)[0]; n = g.n
    S, FB, E = (ex16.trace(g, st, cap=cap) if st is not None else sox.trace(g, cap=cap))
    N = len(S); ev = [E.evaluate(tuple(s)) for s, _ in S]; Xi = [e[0] for e in ev]; SB = [e[1] for e in ev]
    lam = [tuple(x[0] for x in X) for X in Xi]
    def oncyc(t, odd):
        seen, x = [], o
        while x not in seen: seen.append(x); x = S[t][0][x] if g.owner[x] == 0 else (SB[t][x] if odd == "sb" else S[t][1][x])
        return o in seen[seen.index(x):]
    def R(t):
        r = set()
        for v in range(n):
            seen, x = set(), v
            while x not in seen and x != o: seen.add(x); x = S[t][0][x] if g.owner[x] == 0 else S[t][1][x]
            if x == o and v != o: r.add(v)
        return frozenset(r)
    Rs = [R(t) for t in range(N)]
    def used(k):
        L, ew = BOT, []
        for v in range(n):
            if lam[k][v] == v: continue
            a, b = (S[k][0][v], S[k + 1][0][v]) if g.owner[v] == 0 else (SB[k][v], SB[k + 1][v])
            if a != b:
                l = lev(Xi[k][a], Xi[k][b]); L = max(L, l)
                if g.owner[v] == 0: ew.append(l)
        return L, ew
    phases = []; a = 0
    while a < N - 1:
        b = a
        while b + 1 < N and lam[b + 1] == lam[a] and S[b + 1][1] == S[a][1]: b += 1
        Kt = Ks = 0; typ = {}; prev = None
        for k in range(a, b):
            L, ew = used(k)
            if L == BOT: continue
            if prev is not None:
                pk, pL = prev
                if not any(FB[i] for i in range(pk, k + 1)) and all(Rs[i] == Rs[pk] for i in range(pk, k + 2)):
                    w = sum(1 for l in ew if l > pL)
                    if w:
                        Kt += 1; Ks += w
                        h1, h2 = not oncyc(k, "sb"), not oncyc(k, "tau")
                        tn = {(1, 1): "U1", (0, 1): "U2", (1, 0): "U3", (0, 0): "U23"}[(int(h1), int(h2))]; typ[tn] = typ.get(tn, 0) + w
            prev = (k, L)
        phases.append(dict(a=a, b=b, Kt=Kt, Ks=Ks, typ=typ)); a = b + 1
    return dict(n=n, it=len(FB), fb=sum(FB), phases=phases)

if __name__ == "__main__":
    args = sys.argv[1:]; st = None
    if args and args[0] == "--start": st = json.load(open(args[1])); st = st.get("start", st); args = args[2:]
    for f in args:
        try: g = sox.load(f)
        except Exception: continue
        if len(sox.oddchoice(g)) != 1: continue
        r = analyse(g, st); ph = r["phases"]; typ = {}
        for p in ph:
            for k, v in p["typ"].items(): typ[k] = typ.get(k, 0) + v
        print(os.path.basename(f), "n", r["n"], "it", r["it"], "fb", r["fb"], "phases", len(ph), "maxKt", max((p["Kt"] for p in ph), default=0),
              "maxKs", max((p["Ks"] for p in ph), default=0), "totKs", sum(p["Ks"] for p in ph), "types", typ, flush=True)
