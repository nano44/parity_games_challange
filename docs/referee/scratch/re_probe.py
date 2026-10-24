#!/usr/bin/env python3
"""REFEREE probe for packet P-N5-RE (docs/new/P-N5-RE-box26.md, pin 52c7261). Uses n5x.step (N5 SPEC S4 loop, engine code-linked
by RESULTS R15 G-N1) read-only. Checks, at every N5 transition k -> k+1:
 SW   every Even y with sigma_{k+1}(y) != sigma_k(y), lam_k(y) != y and lam_{k+1}(y) != y has Xi_{k+1}(y) > Xi_k(y) strictly
      (the referee's (NC)-free form of RE step 2; no phase, no (h), no class assumption).
      Sub-counts: NC   = the packet's excluded case: lam constant, y on its new honest cycle, Xi_k(y) has empty path set;
                  NCR/CAVR = the same restricted to RE's setting (y in R_k, joint lambda and tau constant, (h) at k);
                  CAV  = the caveat case of RE step 2: z's k-path passes y while y is NOT on its new cycle.
 FLAT switched y that is its own cycle node at k or k+1 (no strictness claimed; counted only).
 RE3  on C^1O games: a LEAVE of Even x from R at k->k+1 inside a joint lambda-phase, (h) at k: Xi_{k+1}(x) > Xi_k(x) strictly.
 PSPLIT on C^1O games: inside a PIECE (as piececheck.py: joint lambda, tau, theta, w constant, (h) both ends, no fallback, R constant)
      the number of transitions changing a value on R is <= |R| - 1 and on F is <= |F| - 1, separately (the referee's R* count).
Usage: re_probe.py N nmin nmax seed [c1o|gen] [--randstart]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments/new/box25"))
from common import *
from thtrace import Rset
from wdrop_h import oncycle
from collections import Counter

def honest_cycle_has(g, s, sb, y):
    nxt = [s[v] if g.owner[v] == 0 else sb[v] for v in range(g.n)]; x, seen = nxt[y], set()
    while x not in seen:
        if x == y: return True
        seen.add(x); x = nxt[x]
    return False

def passes(g, s, sb, z, y):
    nxt = [s[v] if g.owner[v] == 0 else sb[v] for v in range(g.n)]; x, seen = z, set()
    while x not in seen:
        if x == y: return True
        seen.add(x); x = nxt[x]
    return False

def rand_gen(rng, lo, hi):
    n = rng.randint(lo, hi)
    return pg.Game([rng.randrange(n + 2) for _ in range(n)], [rng.randrange(2) for _ in range(n)],
                   [sorted(set(rng.sample(range(n), min(n, rng.choice((1, 2, 2, 3)))))) for _ in range(n)])

def run(g, start, cnt, c1o):
    assert not c1o or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1) == 1, "not in C^1O: exactly one Odd choice vertex required"
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); o = odd_choice(g) if c1o else None
    rows = []
    while True:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t))
        row = dict(s=tuple(s), t=tuple(t), Xi=Xi, sb=sb, lam=(tuple(x[0] for x in Xi), tuple(y[0] for y in U)))
        if c1o:
            _, W = wvals(g, s, t)
            row.update(W=W, R=Rset(g, s, t, o), th=E.key(Xi[o]), w=E.key(W[o]),
                       h=not oncycle(g, s, sb, o) and not oncycle(g, s, t, o) and Xi[o][0] == W[o][0])
        rows.append(row); r = step(g, E, Ed, s, t)
        if r is None: break
        row["fb"] = r[4]; s, t = list(r[0]), list(r[1])
    rows[-1]["fb"] = 0
    for k in range(len(rows) - 1):
        a, b = rows[k], rows[k + 1]
        for y in range(g.n):
            if g.owner[y] != 0 or a["s"][y] == b["s"][y]: continue
            la, lb = a["Xi"][y][0], b["Xi"][y][0]
            if la == y or lb == y: cnt["FLAT_cyclenode_switch"] += 1; continue
            cnt["SW_checks"] += 1
            strict = E.key(b["Xi"][y]) > E.key(a["Xi"][y])
            if not strict: cnt["SW_VIOLATION"] += 1
            if la == lb and honest_cycle_has(g, b["s"], b["sb"], y) and a["Xi"][y][1] == 0:
                cnt["NC_case"] += 1; cnt["NC_case_strict"] += strict
            z = b["s"][y]
            if passes(g, a["s"], a["sb"], z, y) and not honest_cycle_has(g, b["s"], b["sb"], y):
                cnt["CAV_case"] += 1; cnt["CAV_case_strict"] += strict
                if c1o and a["lam"] == b["lam"] and a["t"] == b["t"] and a["h"] and y in a["R"]:
                    cnt["CAVR_case"] += 1; cnt["CAVR_case_strict"] += strict
                    if not hasattr(run, "ex"): run.ex = (g.n, k, y, z); print("CAVR example: n", g.n, "transition", k, "y", y, "z", z, file=sys.stderr)
            if c1o and la == lb and a["t"] == b["t"] and a["h"] and y in a["R"] and honest_cycle_has(g, b["s"], b["sb"], y) and a["Xi"][y][1] == 0:
                cnt["NCR_case"] += 1; cnt["NCR_case_strict"] += strict
        if c1o and a["lam"] == b["lam"] and a["t"] == b["t"] and a["h"]:
            for x in range(g.n):
                if g.owner[x] == 0 and x != o and x in a["R"] and x not in b["R"]:
                    cnt["RE3_checks"] += 1
                    if not E.key(b["Xi"][x]) > E.key(a["Xi"][x]): cnt["RE3_VIOLATION"] += 1
    if c1o:
        pr = pf = 0
        for k in range(len(rows) - 1):
            a, b = rows[k], rows[k + 1]
            ok = (a["lam"] == b["lam"] and a["t"] == b["t"] and a["th"] == b["th"] and a["w"] == b["w"] and a["h"] and b["h"]
                  and not a["fb"] and a["R"] == b["R"])
            if not ok: pr = pf = 0; continue
            R = a["R"]; F = set(range(g.n)) - R
            chR = any(E.key(a["Xi"][v]) != E.key(b["Xi"][v]) or E.key(a["W"][v]) != E.key(b["W"][v]) for v in R)
            chF = any(E.key(a["Xi"][v]) != E.key(b["Xi"][v]) or E.key(a["W"][v]) != E.key(b["W"][v]) for v in F)
            pr += chR; pf += chF; cnt["PSPLIT_transitions"] += 1
            cnt["PSPLIT_maxR_slack"] = min(cnt.get("PSPLIT_maxR_slack", 99), len(R) - 1 - pr)
            cnt["PSPLIT_maxF_slack"] = min(cnt.get("PSPLIT_maxF_slack", 99), len(F) - 1 - pf)
            if pr > len(R) - 1: cnt["PSPLIT_R_VIOLATION"] += 1
            if pf > len(F) - 1: cnt["PSPLIT_F_VIOLATION"] += 1

if __name__ == "__main__":
    a = sys.argv[1:]; cnt = Counter()
    if a[0].endswith(".pg"):
        g = load(a[0]); st = readstart(a[1]) if len(a) > 1 and not a[1].startswith("-") else None
        run(g, st, cnt, True); print(a[0], dict(sorted(cnt.items()))); sys.exit()
    N, lo, hi, seed = map(int, a[0:4]); mode = a[4] if len(a) > 4 else "c1o"; RS = "--randstart" in a; rng = random.Random(seed)
    for i in range(N):
        g = rand_c1o(rng, lo, hi, forced=0.1) if mode == "c1o" else rand_gen(rng, lo, hi)
        if g is None: continue
        st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
              {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
        cnt["runs"] += 1; run(g, st, cnt, mode == "c1o")
    print(dict(sorted(cnt.items())))
