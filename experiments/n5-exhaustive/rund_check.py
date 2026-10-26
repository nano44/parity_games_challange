#!/usr/bin/env python3
"""Box 11 item 2 (Lead 2026-10-26 07:15Z): independent check of L-SI's PROVED box-17 lemmas from the note's text (docs/si/N5-RUND-box17.md
§5, l-si d61b3cf0 / 27d47226): Lemma OFFSET (a)-(c) and Theorem TWIN-GAP (i)-(iii). L-SI's experiments/si/rund/ scripts NOT opened.
Machinery: gdnc_check.state_info (my own D_k, u(v), pi_v, (h3_D), M_D) on REFEREE-2's fb_check run and valuations. Own code below:
  w(P) := sum over ranks r in P of eps * 2^r, eps = +1 (even priority) / -1 (odd);  s^Xi_k(v) := w(P(Xi_k v)), s^W_k(v) := w(P(W_k v));
  Delta_k(v) := s^W - s^Xi;  delta_k(u) := w(P(W_k u)) - w(P(Xi_k u)) for u in D_k.
  S := every MAXIMAL fallback-free run of transitions inside one phase (key (lambda_Xi, tau)) with (h3_D) at every state (>= 1 transition);
  L* := max(max_S M_D, -1);  U_S := union over k in S, u in D_k of P(Xi_k u) symdiff P(W_k u) (ranks);  l_S := min U_S;  B := L* - l_S + 1.
Checks:
  OFFa  lambda_Xi(v) = lambda_W(v) for all v at every state of S, constant on S; s^Xi(v) and s^W(v) non-decreasing along S.
  OFFb  Delta(v) = 0 if v in F_D, or v in R_D with lambda(v) in pi_v; else Delta(v) = delta(u(v)).
  OFFc  every rank of P(Xi u) symdiff P(W u) (u in D_k, k in S) lies in [l_S, L*]; every offset on S is a multiple of 2^l_S; U_S empty =>
        every offset on S is 0.
  TGi   at each transition of S where Delta(v) changes by d != 0: d > 0 => s^W(v) rises by >= d; d < 0 => s^Xi(v) rises by >= -d.
  TGii  per v: changes at transitions from states >= k_0 + n - 1 (0-based, as FRZ-U_H3) <= (2^(L*+2) - 2) / 2^l_S.
  TGiii per v: N_v <= (n - 1) + 2^(B+1).
Records: B, l_S, L*, max N_v, offset changes at states >= k_0 + n - 1 (TGii exercised or not).
Mutation control RUND_MUT=b: OFFb with delta's sign flipped (must fail where offsets are nonzero).
Usage: rund_check.py rand N NMIN NMAX K SEED | files LIST.txt [STARTS]   (rand: C^KO games, canonical + one random start pair each)"""
import os
import random
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gdnc_check as G  # noqa: E402

F = G.F; BOT = G.BOT
MUT = os.environ.get("RUND_MUT", "")   # mutation control only: 'b' = OFFb with the offset's sign flipped


def wP(E, mask):
    s, r = 0, 0
    while mask:
        if mask & 1:
            v = E.vert[r]; s += (-1 if E.par[v] else 1) << r
        mask >>= 1; r += 1
    return s


def ranks(mask):
    return {r for r in range(mask.bit_length()) if mask >> r & 1}


def check_run(g, s, t, c, mx, bad, name):
    states, fbs, E, Ed = F.run_n5(g, s, t)
    if not hasattr(E, "vert"):
        E.vert = {E.rank[v]: v for v in range(g.n)}
    A = [G.state_info(g, E, a, b) for a, b in states]
    n = g.n; T = len(fbs); c["runs"] += 1
    for S in A:
        S["sX"] = [wP(E, x[1]) for x in S["Xi"]]; S["sW"] = [wP(E, x[1]) for x in S["W"]]
        S["delta"] = {u: wP(E, S["W"][u][1]) - wP(E, S["Xi"][u][1]) for u in S["D"]}
    ok = [not fbs[j] and A[j]["lam"] == A[j + 1]["lam"] and states[j][1] == states[j + 1][1] and A[j]["h3"] and A[j + 1]["h3"]
          for j in range(T)]
    k = 0
    while k < T:
        if not ok[k]:
            k += 1; continue
        j = k
        while j < T and ok[j]:
            j += 1
        run(g, A, list(range(k, j + 1)), c, mx, bad, f"{name}[{k},{j}]")
        k = j


def run(g, A, Sx, c, mx, bad, name):
    n = g.n; k0 = Sx[0]; c["S_runs"] += 1
    Ls = max(max(A[x]["MD"] for x in Sx), -1)
    U = set()
    for x in Sx:
        for u in A[x]["D"]:
            U |= ranks(A[x]["Xi"][u][1] ^ A[x]["W"][u][1])
    lS = min(U) if U else None
    B = (Ls - lS + 1) if U else 0
    mx["max_B"] = max(mx["max_B"], B); c["S_runs_U_nonempty"] += bool(U)
    lam0 = A[k0]["lam"]
    for x in Sx:
        S = A[x]
        # OFFa (first sentence) and constancy
        c["OFFa_states"] += 1
        if any(S["Xi"][v][0] != S["W"][v][0] for v in range(n)) or S["lam"] != lam0:
            bad(f"{name} OFFa lambda at {x}")
        # OFFb
        for v in range(n):
            Dv = S["sW"][v] - S["sX"][v]; c["OFFb_checks"] += 1
            if v not in S["uv"]:
                exp = 0
            else:
                u = S["uv"][v]; exp = 0 if S["lam"][v] in S["pi"][v] else S["delta"][u] * (-1 if MUT == "b" else 1)
            if Dv != exp:
                bad(f"{name} OFFb v={v} at {x}: Delta {Dv} expected {exp}")
            # OFFc: multiples of 2^l_S; zero if U empty
            c["OFFc_checks"] += 1
            if (lS is None and Dv != 0) or (lS is not None and Dv % (1 << lS) != 0):
                bad(f"{name} OFFc v={v} at {x}: Delta {Dv} l_S {lS}")
        for u in S["D"]:
            rr = ranks(S["Xi"][u][1] ^ S["W"][u][1])
            if rr and (min(rr) < lS or max(rr) > Ls):
                bad(f"{name} OFFc ranks of u={u} at {x}: {sorted(rr)} not in [{lS},{Ls}]")
    # OFFa monotone scores, TGi-iii
    for v in range(n):
        Nv = Nlate = 0
        for a, b in zip(Sx, Sx[1:]):
            A0, A1 = A[a], A[b]; c["OFFa_mono_checks"] += 1
            if A1["sX"][v] < A0["sX"][v] or A1["sW"][v] < A0["sW"][v]:
                bad(f"{name} OFFa monotone v={v} at {a}")
            d = (A1["sW"][v] - A1["sX"][v]) - (A0["sW"][v] - A0["sX"][v])
            if d:
                Nv += 1; c["TGi_checks"] += 1
                if d > 0 and A1["sW"][v] - A0["sW"][v] < d: bad(f"{name} TGi v={v} at {a} d={d}")
                if d < 0 and A1["sX"][v] - A0["sX"][v] < -d: bad(f"{name} TGi v={v} at {a} d={d}")
                if a - k0 >= n - 1:
                    Nlate += 1
        if Nv:
            c["vertices_with_offset_changes"] += 1
        mx["max_N_v"] = max(mx["max_N_v"], Nv); mx["max_N_v_late"] = max(mx["max_N_v_late"], Nlate)
        c["TGii_exercised(late changes)"] += Nlate
        if lS is not None and Nlate > ((1 << (Ls + 2)) - 2) // (1 << lS): bad(f"{name} TGii v={v}: {Nlate}")
        if Nv > (n - 1) + (1 << (B + 1)): bad(f"{name} TGiii v={v}: N_v {Nv} > {(n - 1) + (1 << (B + 1))}")
        c["TG_vertex_checks"] += 1


def main():
    c, mx, viol = Counter(), Counter(), []
    if sys.argv[1] == "rand":
        N, lo, hi, K, seed = map(int, sys.argv[2:7]); rng = random.Random(seed)
        for i in range(N):
            n = rng.randint(lo, hi); g = G.rand_ckO(rng, n, min(K, n - 1))
            E, Ed = F.Engine(g), F.Engine(F.n5.dual(g))
            check_run(g, list(E.initial("best")), list(Ed.initial("best")), c, mx, viol.append, f"r{seed}#{i}c")
            s, t = G.rand_start(g, rng); check_run(g, s, t, c, mx, viol.append, f"r{seed}#{i}r")
    else:
        for path in [l.strip() for l in open(sys.argv[2]) if l.strip()]:
            g = F.lpg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%")))
            E, Ed = F.Engine(g), F.Engine(F.n5.dual(g)); rng = random.Random(7); nm = os.path.basename(path)
            check_run(g, list(E.initial("best")), list(Ed.initial("best")), c, mx, viol.append, nm)
            for r in range(int(sys.argv[3]) if len(sys.argv) > 3 else 0):
                s, t = G.rand_start(g, rng); check_run(g, s, t, c, mx, viol.append, f"{nm}#{r}")
    G.report(c, mx, viol)


if __name__ == "__main__":
    main()
