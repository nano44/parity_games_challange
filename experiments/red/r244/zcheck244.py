#!/usr/bin/env python3
"""L-RED 70 R244: N5 itself on the kill candidate, run to its END, against Zielonka. Game: Γ3(G) (R117) built by box 189's gamma3.build with
all pads (an OBJECT of claude/l-new, env LNEW; L-RED has no Γ3 builder of its own: said in the verdict). N5: L-RED's n5s237.run (SPEC-exact,
written from the SPEC text by L-RED 67), default start S3, mode spec. Zielonka: written here (recursive, max-parity, attractors).
Checks per genome: iterations, fallbacks; winners of N5 = winners of Zielonka (wrong = number of vertices that differ, must be 0);
Even's final strategy wins from every vertex N5 gives to Even (Zielonka on the game with Even's edges cut to σ; bad_E must be 0) and Odd's
reply strategy wins from every vertex N5 gives to Odd (Odd's edges cut to σ̄; bad_O must be 0).
Control ZCTRL=1: the priorities of the game given to Zielonka are shifted by one (parities flipped): wrong must be > 0.
Usage: zcheck244.py G.json ...   (env LNEW)"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); LNEW = os.environ["LNEW"]
sys.path[:0] = [os.path.join(HERE, "..", "r237")] + [os.path.join(LNEW, p) for p in ("experiments/new/box195", "experiments/new/box190", "experiments/new/box189", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
import n5s237 as S
import gamma3
sys.setrecursionlimit(100000)
def attr(V, pred, owner, succ, A, p):
    A = set(A); out = {v: sum(1 for w in succ[v] if w in V) for v in V}; q = list(A)
    while q:
        w = q.pop()
        for v in pred[w]:
            if v in V and v not in A:
                if owner[v] == p: A.add(v); q.append(v)
                else:
                    out[v] -= 1
                    if out[v] == 0: A.add(v); q.append(v)
    return A
def zielonka(V, prio, owner, succ, pred):
    if not V: return set(), set()
    m = max(prio[v] for v in V); p = m % 2; U = {v for v in V if prio[v] == m}
    A = attr(V, pred, owner, succ, U, p); W = zielonka(V - A, prio, owner, succ, pred)
    if not W[1 - p]: return (V, set()) if p == 0 else (set(), V)
    B = attr(V, pred, owner, succ, W[1 - p], 1 - p); W2 = zielonka(V - B, prio, owner, succ, pred)
    res = [None, None]; res[p] = W2[p]; res[1 - p] = W2[1 - p] | B; return res[0], res[1]
def solve(prio, owner, succ):
    n = len(prio); pred = [[] for _ in range(n)]
    for v in range(n):
        for w in succ[v]: pred[w].append(v)
    return zielonka(set(range(n)), prio, owner, succ, pred)
CTRL = os.environ.get("ZCTRL") == "1"
for f in sys.argv[1:]:
    G = json.load(open(f)); G = G.get("genome", G)
    g, sig0, tau0, V = gamma3.build(G, {"K", "pe", "pb", "m"}); n = g.n; prio = list(g.prio); owner = list(g.owner); succ = [sorted(set(s)) for s in g.succ]
    it, fb, win, sigma, sbar = S.run(prio, owner, succ)
    WE, WO = solve([p + 1 for p in prio] if CTRL else prio, owner, succ)
    wrong = sum(1 for v in range(n) if win[v] != (v in WE))
    sE = [[sigma[v]] if owner[v] == 0 else succ[v] for v in range(n)]; E2, _ = solve(prio, owner, sE); badE = sum(1 for v in range(n) if win[v] and v not in E2)
    sO = [[sbar[v]] if owner[v] == 1 else succ[v] for v in range(n)]; _, O2 = solve(prio, owner, sO); badO = sum(1 for v in range(n) if not win[v] and v not in O2)
    print(f"ZCHECK244 {os.path.basename(f)}: N {G['N']} n {n} m {sum(len(s) for s in succ)} N5 iterations {it} fallbacks {fb} | Even wins {sum(win)} of {n} | wrong {wrong} bad_E {badE} bad_O {badO} | ctrl {int(CTRL)}", flush=True)
