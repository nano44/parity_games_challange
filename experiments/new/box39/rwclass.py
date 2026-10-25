#!/usr/bin/env python3
"""Box 39 (1): classes of R̄-rises with θ fixed, and a direct check of Lemma BF-M (docs/new/N5-RW-box39.md).
A BLOCK is a maximal run of consecutive in-phase HN states (H1 ∧ ¬H2) with θ, R̄ and c_w constant. T* := max(rank c_θ, rank c_w).
M_k(z) := signed weight of the P-bits of Ξ_k(z) above T* (z ∈ R̄). Per transition of a block, for z ∈ R̄ ∖ {o}:
  rise class M (lev > T*), BAND (rank c_θ < lev ≤ T*), LEN (lev = −1); W changed on R̄ or not; fallback or S4a.
Check BFM: for every Even v ∈ R and successor x ∈ R̄: M_{k+1}(v) ≥ wt(v) + M_k(x), wt(v) = ±2^rank(v) if rank(v) > T* else 0.
Check FREEZE: no M-rise after the first n − 1 transitions of a block (consequence of BFM when no positive M-cycle; else the block
is short). DATA only. Usage: rwclass.py game.pg [game.state] ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "box38"))
sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from neb_run import *
from rwcount import cw_of
from h1 import wvals
from mono import lev

def blocks(g, s0):
    rows, o, E = trace(g, s0); N = len(rows)
    for r in rows: r["cw"] = cw_of(g, r, o, E) if (r["h1"] and not r["h2"]) else None
    HN = [r["h1"] and not r["h2"] for r in rows]
    def same(a, b): return (rows[b]["ph"] == rows[a]["ph"] and rows[b]["th"] == rows[a]["th"] and rows[b]["R"] == rows[a]["R"]
                            and rows[b]["cw"] == rows[a]["cw"])
    out = []; a = 0
    while a < N:
        if not HN[a]: a += 1; continue
        b = a
        while b + 1 < N and HN[b + 1] and same(a, b + 1): b += 1
        out.append((a, b)); a = b + 1
    return rows, o, E, out

def analyse(g, s0, acc, name):
    rows, o, E, bl = blocks(g, s0); n = g.n
    for a, b in bl:
        if b == a: continue
        bump(acc, "blocks"); bump(acc, "block_transitions", b - a)
        Rb = set(rows[a]["R"]) | {o}; ct = E.rank[rows[a]["Xi"][o][0]]; Ts = max(ct, E.rank[rows[a]["cw"]])
        hi = ~((1 << (Ts + 1)) - 1)
        def M(val): return E.weight(val[1] & hi)
        def wt(v): return (E.weight(E.bit[v]) if E.rank[v] > Ts else 0)
        Wk = wvals(g, rows[a]["s"], rows[a]["t"])[1]
        lastM = -1; tie = 0
        for k in range(a, b):
            X0, X1 = rows[k]["Xi"], rows[k + 1]["Xi"]; Wk1 = wvals(g, rows[k + 1]["s"], rows[k + 1]["t"])[1]
            fb = "fb" if rows[k]["fb"] else "s4a"
            wch = any(Wk[z] != Wk1[z] for z in Rb)
            cls = set()
            for z in Rb - {o}:
                if E.key(X0[z]) < E.key(X1[z]):
                    L = lev(X0[z], X1[z])
                    cls.add("M" if L > Ts else ("BAND" if L > ct else ("LEN" if L == -1 else "LOW")))
                elif E.key(X0[z]) > E.key(X1[z]): bump(acc, "FAIL_monotone"); print("MONO", name, k, z)
            for c in cls: bump(acc, f"rise_{c}_{fb}_{'Wch' if wch else 'Wsame'}")
            if cls: bump(acc, f"rise_tr_{fb}_{'Wch' if wch else 'Wsame'}")
            if cls and fb == "s4a" and not wch: tie += 1
            if fb == "s4a" and any(E.key(Wk[z]) > E.key(Wk1[z]) for z in range(n)): bump(acc, "FAIL_F1_Wmono"); print("F1", name, k)
            if "M" in cls: lastM = k - a
            for v in Rb - {o}:
                if g.owner[v] != 0: continue
                for x in set(g.succ[v]):
                    if x in Rb and M(X1[v]) < wt(v) + M(X0[x]):
                        bump(acc, "FAIL_BFM"); print("BFM", name, a, k, v, x, fb)
            Wk = Wk1
        mx(acc, "max_last_M_rise_index", lastM, n, name, a, b)
        mx(acc, "max_TIE_per_block", tie, n, name, a, b); bump(acc, "TIE_total", tie); acc.setdefault("_ties", []).append(tie)
        if lastM >= n - 1: bump(acc, "FAIL_FREEZE"); print("FREEZE", name, a, b, lastM)

def rand_main(N, lo, hi, seed):
    import random
    sys.path.insert(0, os.path.join(HERE, "..", "box25")); from common import rand_c1o
    rng = random.Random(seed); acc = {}
    for i in range(N):
        g = rand_c1o(rng, lo, hi)
        if g is None: continue
        bump(acc, "games"); analyse(g, None, acc, f"rand{seed}_{i}")
    for key in sorted(acc):
        if not key.startswith('_'): print(key, acc[key])

if __name__ == "__main__" and sys.argv[1:2] == ["--rand"]:
    rand_main(*map(int, sys.argv[2:6])); sys.exit(0)
if __name__ == "__main__":
    acc = {}; args = sys.argv[1:]; i = 0
    while i < len(args):
        f = args[i]; s0 = None
        if i + 1 < len(args) and args[i + 1].endswith(".state"): s0 = list(map(int, open(args[i + 1]).read().split())); i += 1
        try: g = load(f)
        except Exception: bump(acc, "load_fail"); i += 1; continue
        if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1: analyse(g, s0, acc, f)
        else: bump(acc, "skipped_not_C1O")
        i += 1
    for key in sorted(acc):
        if not key.startswith('_'): print(key, acc[key])
