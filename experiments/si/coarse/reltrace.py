#!/usr/bin/env python3
"""L-SI box 9: DATA for the per-level count (docs/si/N5-C-box9.md §4). Inside each scope run S of an o-cyclic 𝒞^1O game (rfinv.py
scope: in-phase, (h) at k and k+1, w constant), the event sequence: fallbacks F(M, r, released exits, evicted tails at level M),
θ-changes T(level, absorbed exit or '-'), and per level M >= 0 the BLOCK = the fallbacks of S at level M (contiguous by CLS1).
Per block: N = #fallbacks, A = #θ-changes above M strictly inside the block (between its first and last fallback), Rel = #exit
releases at the block's fallbacks, tails = #distinct level-M tails, rep = #(tail, fallback) repeats, and whether r_j > M throughout.
Checks (DATA): (ABS-L') A <= (d_o - 1)·(N - 1) when r_j > M on the block; (REL-A) every re-absorption of an exit inside a block is
preceded by its release at a fallback of the block; with b_k(y) := Ξ_k(σ_k y): (FB-FLAT) at an in-scope THR fallback k with u* ≠ none,
COARSE_{M_k}(b(y)) is unchanged at k -> k+1 for every Even y; (ONE-RISE) for consecutive level-M fallbacks f < f' of a block with
r_j > M on (f, f'], every level-M tail y at f' has COARSE_M(b_{f'}(y)) = COARSE_M(b_{f+1}(y)); (CONSEC) their level-M tail sets are
disjoint. (FB-RE) per scope run, #fallbacks of level >= 0 <= n·n_E + RE(S), RE(S) := #(y, j): j an S4a step of S, y ∈ F_j ∩ R_{j+1},
y evicted (R -> F as a tail) at an earlier fallback of S; and per level-M block N <= |tails| + RE inside the block (PL-RED). Usage: reltrace.py [-v] game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rfinv import *
from collections import Counter, defaultdict

def runs_of(g, name):
    E, out = states(g); n = g.n; o = odd_choice(g); assert o is not None, f"{name}: not one-Odd-choice"
    Ed = n5.Engine(n5.dual(g)); exits = sorted(set(g.succ[o]))
    for a in out:
        a["key"] = (tuple(x[0] for x in a["Xi"]), a["t"], tuple(x[0] for x in Ed.evaluate(tuple(a["t"]))[0]))
        _, W = wvals(g, a["s"], a["t"]); a["W"] = W; a["R"] = reach(g, a["s"], a["t"], o)
        a["h"] = (not oncycle(g, a["s"], a["sb"], o)) and (not oncycle(g, a["s"], a["t"], o)) and a["Xi"][o][0] == W[o][0]
        a["gl"] = [(y, z, lev(a["Xi"][a["s"][y]], a["Xi"][z])) for y, z in a["Is"]]
        a["M"] = max([l for *_, l in a["gl"]] or [-3])
    runs = []; cur = None
    for i in range(len(out) - 1):
        a, b = out[i], out[i + 1]
        if not (a["key"] == b["key"] and a["h"] and b["h"] and a["W"][o] == b["W"][o]): cur = None; continue
        if cur is None: cur = []; runs.append(cur)
        r = lev(a["Xi"][o], a["W"][o]); lt = lev(a["Xi"][o], b["Xi"][o])
        rel = [x for x in exits if x != o and x in a["R"] and x not in b["R"]]
        ent = [x for x in exits if x != o and x not in a["R"] and x in b["R"]]
        if a["fb"]:
            tails = sorted({y for y, z, l in a["gl"] if l == a["M"]})
            cur.append(dict(k="F", i=i, M=a["M"], r=r, rel=rel, ent=ent, tails=tails, lt=lt))
        else:
            cur.append(dict(k="S", i=i, r=r, rel=rel, ent=ent, lt=lt, x0=a["sb"][o], x1=b["sb"][o],
                            enter=[y for y in range(n) if g.owner[y] == 0 and y not in a["R"] and y in b["R"]]))
    return runs, len([x for x in exits if x != o]), exits, out

def scan_rel(g, name, verbose=False):
    runs, d_o, exits, out = runs_of(g, name); C = Counter(); ex = []
    b = lambda k, y: out[k]["Xi"][out[k]["s"][y]]
    Ev = [y for y in range(g.n) if g.owner[y] == 0]
    for S in runs:
        if verbose: print(name, "RUN", " ".join((f"F{e['M']}/r{e['r']}" + (f"-{e['rel']}" if e['rel'] else "") + (f"+{e['ent']}" if e['ent'] else ""))
                                               if e["k"] == "F" else (f"T{e['lt']}" + (f"+{e['ent']}" if e['ent'] else "") + (f"-{e['rel']}" if e['rel'] else "")
                                                if e["lt"] > -2 or e["ent"] or e["rel"] else ".") for e in S))
        fbs = [t for t, e in enumerate(S) if e["k"] == "F"]
        evicted = set(); RE = 0; reent = []
        for t, e in enumerate(S):
            if e["k"] == "F" and e["M"] >= 0: evicted |= set(e["tails"])
            if e["k"] == "S":
                hit = [y for y in e["enter"] if y in evicted]; RE += len(hit); reent += [t] * len(hit)
        nfb = sum(1 for t in fbs if S[t]["M"] >= 0); nE = sum(1 for y in range(g.n) if g.owner[y] == 0)
        C["RE"] += RE; C["max_RE_run"] = max(C["max_RE_run"], RE); C["fb_ge0"] += nfb
        if nfb > g.n * nE + RE: C["fbre_viol"] += 1; ex.append((name, "FB-RE", nfb, RE))
        for t in fbs:
            e = S[t]; k = e["i"]
            if e["r"] >= 0 and e["M"] >= 0:
                C["flat_chk"] += 1
                if any(coarse(b(k + 1, y), e["M"]) != coarse(b(k, y), e["M"]) for y in Ev): C["flat_viol"] += 1; ex.append((name, "FB-FLAT", k))
        for t, t2 in zip(fbs, fbs[1:]):              # (NJ-INT) consecutive fallbacks k0 < k, L = M_k0, r > L on (k0, k]: θ-changes above L
            L = S[t]["M"]
            if all(S[u]["r"] > L for u in range(t + 1, t2 + 1)):
                C["int_chk"] += 1; up = sum(1 for u in range(t + 1, t2) if S[u]["lt"] > L)
                if up: C["int_up"] += 1; ex.append((name, "NJ-INT", L, up))
        for M in sorted({S[t]["M"] for t in fbs if S[t]["M"] >= 0}):
            blk = [t for t in fbs if S[t]["M"] == M]; t0, t1 = blk[0], blk[-1]; N = len(blk)
            A = sum(1 for t in range(t0 + 1, t1) if S[t]["lt"] > M)
            rabove = all(S[t]["r"] > M for t in range(t0 + 1, t1 + 1))
            Rel = sum(len(S[t]["rel"]) for t in blk)
            for t, t2 in zip(blk, blk[1:]):
                f, f2 = S[t]["i"], S[t2]["i"]
                C["consec_chk"] += 1
                if set(S[t]["tails"]) & set(S[t2]["tails"]): C["consec_viol"] += 1; ex.append((name, "CONSEC", M, f, f2))
                if all(S[u]["r"] > M for u in range(t + 1, t2 + 1)):
                    for y in S[t2]["tails"]:
                        C["onerise_chk"] += 1
                        if coarse(b(f2, y), M) != coarse(b(f + 1, y), M): C["onerise_viol"] += 1; ex.append((name, "ONE-RISE", M, f, f2, y))
            tl = Counter(y for t in blk for y in S[t]["tails"])
            REb = sum(1 for t in reent if t0 < t < t1)
            BM = 0; brk_fb = 0                       # (PL) breaks: steps inside the block where COARSE_M(Ξ) changes somewhere
            for t in range(t0, t1):
                k = S[t]["i"]
                if any(coarse(out[k + 1]["Xi"][v], M) != coarse(out[k]["Xi"][v], M) for v in range(g.n)):
                    if S[t]["k"] == "F": brk_fb += 1
                    else: BM += 1
            hiM = sum(1 for t in range(t0 + 1, t1) if out[S[t]["i"]]["M"] > M)
            C["blk_hiM"] += hiM
            if hiM: ex.append((name, "hiM", M, hiM, [out[S[t]["i"]]["M"] for t in range(t0 + 1, t1) if out[S[t]["i"]]["M"] > M][:5]))
            C["blk_B"] += BM; C["max_B"] = max(C["max_B"], BM); C["brk_at_fb"] += brk_fb
            if rabove and N > nE * (1 + BM): C["pl_viol"] += 1; ex.append((name, "PL", M, N, BM))
            for t in blk[:-1]:                       # (EV-FRZ) a tail evicted at a block fallback: COARSE_M(b(y)) to the block's end
                f = S[t]["i"]; fend = S[t1]["i"]
                for y in S[t]["tails"]:
                    C["evfrz_chk"] += 1
                    if coarse(b(fend, y), M) != coarse(b(f + 1, y), M): C["evfrz_rise"] += 1
            if N > len(tl) + REb: C["plred_viol"] += 1; ex.append((name, "PL-RED", M, N, len(tl), REb))
            C["blocks"] += 1; C["blk_fb"] += N; C["blk_A"] += A; C["blk_rel"] += Rel
            C["max_N"] = max(C["max_N"], N); C["max_A"] = max(C["max_A"], A); C["max_rep"] = max(C["max_rep"], max(tl.values()))
            if rabove:
                C["blk_rabove"] += 1
                if A > (d_o - 1) * (N - 1): C["absl_viol"] += 1; ex.append((name, "ABS-L'", M, N, A, d_o))
            # (REL-A): inside the block, an exit absorbed twice is released at a block fallback in between
            last_abs = {}
            for t in range(t0, t1 + 1):
                e = S[t]
                if e["k"] == "S" and e["lt"] > M:
                    for x in e["ent"]:
                        if x in last_abs:
                            C["reabs"] += 1
                            if not any(x in S[u]["rel"] and S[u]["k"] == "F" for u in range(last_abs[x], t)): C["rela_viol"] += 1; ex.append((name, "REL-A", M, x))
                        last_abs[x] = t
            C["Nmax_vs_tails"] = max(C["Nmax_vs_tails"], N - len(tl))
    return C, ex

if __name__ == "__main__":
    v = "-v" in sys.argv; T = Counter(); X = []
    for p in [a for a in sys.argv[1:] if a != "-v"]:
        c, e = scan_rel(load(p), os.path.basename(p), v); X += e
        for k, val in c.items(): T[k] = max(T[k], val) if k.startswith("max") or k.startswith("Nmax") else T[k] + val
    print("TOTAL", dict(T))
    for e in X[:20]: print("  ", e)
