#!/usr/bin/env python3
"""Box 34: Theorem FREEZE (docs/new/N5-REL-box34.md). In a phase on 𝒞^1O, if states k0 .. k0 + n - 1 all have (h) and r_k <= ℓ, then
COARSE_ℓ(Ξ) is constant at every state from k0 + n - 1 to the phase's last state with H2, and COARSE_ℓ(W) is constant at those of them
with H2. Then (BLOCKS) for ℓ >= 0: at the later H1 ∧ H2 states, COARSE_{ℓ-1}(θ) takes <= 2 d_o values and COARSE_{ℓ-1}(w) <= 2;
and (X2) inside a fallback-free run of consecutive (h) states after k0 + n - 1 with (COARSE_{ℓ-1} θ, COARSE_{ℓ-1} w) constant and
different, each vertex crosses R at most twice. Checks all three for every phase and every ℓ. Env MODE=H3: FREEZE′ (§10). Usage: freeze.py game.pg ... | --rand"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from relfr import *
from mono import coarse

def bump(acc, k, d=1): acc[k] = acc.get(k, 0) + d

def check(g, acc, name):
    rows, o = rows_w(g); n = g.n; d_o = len(set(g.succ[o]))
    H2 = [h2(r["nxt"], o) for r in rows]
    hh = [r["h1"] and H2[i] and r["Xi"][o][0] == r["W"][o][0] for i, r in enumerate(rows)]
    if os.environ.get("MODE") == "H3":   # FREEZE′ (N5-REL-box34.md §10): windows of H3 states, (b) at states with H2 or H3
        hh = [r["Xi"][o][0] == r["W"][o][0] for r in rows]; H2 = [H2[i] or hh[i] for i in range(len(rows))]
    rr = [lev(r["Xi"][o], r["W"][o]) if hh[i] else None for i, r in enumerate(rows)]
    ph = []; i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1]["ph"] == rows[i]["ph"]: j += 1
        ph.append((i, j)); i = j + 1
    for a, b in ph:
        lastH2 = max([k for k in range(a, b + 1) if H2[k]], default=None)
        if lastH2 is None: continue
        for l in range(-2, n):
            k0 = None
            for s in range(a, b - n + 2):
                if all(hh[k] and rr[k] <= l for k in range(s, s + n)): k0 = s; break
            if k0 is None: continue
            F = k0 + n - 1; bump(acc, "freezes")
            for t in range(F + 1, lastH2 + 1):
                for v in range(n):
                    if coarse(rows[t]["Xi"][v], l) != coarse(rows[F]["Xi"][v], l): bump(acc, "FREEZE_Xi_FAIL"); acc.setdefault("ex_fx", (name, a, l, F, t, v)); break
                if H2[t]:
                    for v in range(n):
                        if coarse(rows[t]["W"][v], l) != coarse(rows[F]["W"][v], l): bump(acc, "FREEZE_W_FAIL"); acc.setdefault("ex_fw", (name, a, l, F, t, v)); break
                bump(acc, "freeze_state_checks")
            if l < 0: continue
            ths = set(); ws = set()
            for t in range(F, lastH2 + 1):
                if rows[t]["h1"] and H2[t]: ths.add(coarse(rows[t]["Xi"][o], l - 1)); ws.add(coarse(rows[t]["W"][o], l - 1))
            if len(ths) > 2 * d_o: bump(acc, "BLOCKS_theta_FAIL"); acc.setdefault("ex_bt", (name, a, l, len(ths), d_o))
            if len(ws) > 2: bump(acc, "BLOCKS_w_FAIL"); acc.setdefault("ex_bw", (name, a, l, len(ws)))
            if len(ths) > acc.get("max_theta_vals", (0,))[0]: acc["max_theta_vals"] = (len(ths), d_o, name, l)
            # X2: fallback-free (h) intervals with the pair constant and different
            t = F
            while t < lastH2:
                if not hh[t]: t += 1; continue
                key = (coarse(rows[t]["Xi"][o], l - 1), coarse(rows[t]["W"][o], l - 1)); u = t; cnt = {}
                while u < lastH2 and hh[u] and hh[u + 1] and not rows[u]["fb"] and rows[u]["ph"] == rows[u + 1]["ph"] and \
                        (coarse(rows[u + 1]["Xi"][o], l - 1), coarse(rows[u + 1]["W"][o], l - 1)) == key:
                    for v in set(rows[u]["R"]) ^ set(rows[u + 1]["R"]): cnt[v] = cnt.get(v, 0) + 1
                    u += 1
                if key[0] != key[1] and cnt:
                    bump(acc, "X2_intervals")
                    if max(cnt.values()) > 2: bump(acc, "X2_FAIL"); acc.setdefault("ex_x2", (name, t, u, l, max(cnt.values())))
                t = u + 1

if __name__ == "__main__":
    acc = {}; a = sys.argv[1:]
    if a and a[0] == "--rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); d = 0
        while d < N:
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            check(g, acc, f"rand{seed}_{d}"); d += 1
    else:
        for f in a:
            g = load(f)
            if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) != 1: continue
            check(g, acc, os.path.basename(f))
    for k in sorted(acc): print(k, acc[k])
