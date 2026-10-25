#!/usr/bin/env python3
"""Box 41 (L-RED successor 17): own checker of CONJECTURE INTO and case (ii) (docs/si/N5-RISE-box13.md, sha1 3b8fea13, §0, §2), written
from the text. Machinery (scope runs, (h), W, r = lev(θ, w), M, COARSE_L) as in experiments/red/so/rx16.py (own, box 39). Trace =
ex16.trace (start pair optional; None = SPEC S3 start, = sox.trace = n5.run).
RISE SETTING: k0 an in-scope Even S4c fallback with L := M_k0 >= 0; j = the first transition after k0 with: every transition s in
(k0, j] in scope, no fallback, r_s > L, and j the first S4a step changing COARSE_L(θ). POST-RISE STATE: t > j such that every
transition s -> s+1, k0 < s < t, is an in-scope S4a step with r_s > L.
  INTO:   at a post-rise state t with r_t > L some gate (y, z) ∈ Iσ_t has z ∈ R̄_t. Failures split: INTO_FAIL_NOGATE (Iσ_t = ∅) and
          INTO_FAIL (gates exist, all into F_t) — the latter is the kill shape; at a fallback state it is case (i).
  CASE1:  a post-rise state t with r_t > L at which an in-scope Even fallback t -> t+1 is taken.
  CASE2:  after the rise, the scope run continues (in scope, any steps) and a later Even fallback occurs in the same scope run after
          some state with r <= L (REFEREE-2's observation excludes it).
Usage: into17.py game.pg [start.json] ..."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "so"))
import sox, pg, ex16
from si import Engine
from sox import BOT, INF, lev, coarse

def analyse(g, start=None, cap=3000):
    o = sox.oddchoice(g); assert len(o) == 1, "not C^1O"; o = o[0]; n = g.n
    S, FB, E = ex16.trace(g, start, cap); N = len(S)
    ev = [E.evaluate(s) for s, _ in S]; Xi = [e[0] for e in ev]; sb = [e[1] for e in ev]; lam = [tuple(x[0] for x in X) for X in Xi]
    Wv = []
    for s, t in S:
        succ = [list(g.succ[v]) if g.owner[v] == 0 else [t[v]] for v in range(n)]
        Wv.append(Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(s)[0])
    def play(k, v, odd):
        x, seen, out = v, set(), []
        while x not in seen:
            seen.add(x); out.append(x); x = S[k][0][x] if g.owner[x] == 0 else (S[k][1][x] if odd == "tau" else sb[k][x])
        return out
    R = [frozenset({o} | {v for v in range(n) if o in play(k, v, "tau")}) for k in range(N)]
    H1 = [o not in play(k, sb[k][o], "sbar") for k in range(N)]; H2 = [o not in play(k, S[k][1][o], "tau") for k in range(N)]
    H3 = [Wv[k][o][0] == lam[k][o] for k in range(N)]
    gates = [E.improving(S[k][0], Xi[k]) for k in range(N)]
    def M(k): return max((lev(Xi[k][S[k][0][y]], Xi[k][z]) for y, z in gates[k]), default=BOT)
    inph = [lam[k] == lam[k + 1] and S[k][1] == S[k + 1][1] for k in range(N - 1)]
    efb = [FB[k] and S[k][0] != S[k + 1][0] for k in range(N - 1)]
    scope = [inph[k] and H1[k] and H2[k] and H3[k] and H2[k + 1] and Wv[k + 1][o] == Wv[k][o] for k in range(N - 1)]
    th = [Xi[k][o] for k in range(N)]; r = [lev(Xi[k][o], Wv[k][o]) for k in range(N)]
    C = {}; ex = []
    def bump(k, v=1): C[k] = C.get(k, 0) + v
    for k0 in range(N - 1):
        if not (scope[k0] and efb[k0]): continue
        L = M(k0)
        if L == INF or L < 0: continue
        j = None; s = k0 + 1
        while s < N - 1 and scope[s] and not FB[s] and r[s] > L:
            if coarse(th[s + 1], L) != coarse(th[s], L): j = s; break
            s += 1
        if j is None: continue
        bump("rises")
        t = j + 1
        while True:
            if r[t] > L:
                bump("post_states_r>L"); into = [(y, z) for y, z in gates[t] if z in R[t]]
                C["min_into"] = min(C.get("min_into", 10 ** 6), len(into))
                if into: bump("INTO_ok")
                elif not gates[t]: bump("INTO_FAIL_NOGATE"); ex.append(("NOGATE", k0, j, t, L, r[t], t < N - 1 and scope[t]))
                else: bump("INTO_FAIL"); ex.append(("INTO", k0, j, t, L, r[t], gates[t][:6]))
                if t < N - 1 and scope[t] and efb[t]: bump("CASE1"); ex.append(("CASE1", k0, j, t, L))
            if t >= N - 1 or not scope[t] or FB[t] or r[t] <= L: break
            t += 1
        # case (ii): continue along the scope run from t (any in-scope steps) looking for a later Even fallback after an r <= L state
        drop = r[t] <= L; s = t
        while s < N - 1 and scope[s]:
            if r[s] <= L: drop = True
            if efb[s] and s > j:
                bump("FB_after_rise"); ex.append(("FB_AFTER_RISE", k0, j, s, L, r[s], "case2" if drop else "case1"))
                if drop: bump("CASE2")
                break
            s += 1
    return C, ex, N

if __name__ == "__main__":
    tot = {}; args = sys.argv[1:]; i = 0
    while i < len(args):
        f = args[i]; st = None
        if i + 1 < len(args) and args[i + 1].endswith(".json"): st = json.load(open(args[i + 1]))["start"]; i += 1
        i += 1
        try: g = sox.load(f)
        except Exception: continue
        if len(sox.oddchoice(g)) != 1: continue
        C, ex, N = analyse(g, st)
        for k, v in C.items(): tot[k] = tot.get(k, 0) + v
        tot["files"] = tot.get("files", 0) + 1
        if C: print(os.path.basename(f), C, [e for e in ex if e[0] != "x"][:4], flush=True)
    print("TOTAL", tot)
