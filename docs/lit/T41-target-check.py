# L-LIT T41 (docs/lit/T41-moving-target.md). Reads L-SI's helpers read-only (experiments/si/root/common.py -> experiments/new/box21/n5x.py, si.py).
# Usage (repo root): python3 -I docs/lit/T41-target-check.py GAME.pg [START]
# Per phase P = [i, j] of the N5 run (λ_Ξ and τ constant, R38 (a), as common.phases), the FIXED TARGET c := σ^c_τ = Even's optimal
# counterstrategy to τ in the full game G (the S1 procedure on G^d, Ed.evaluate(τ); the same procedure S4a runs on the arena), constant on P.
# Per switching Even vertex v (σ_t(v) ≠ σ_{t+1}(v), t ∈ [i, j)):
#   MISS   σ_{t+1}(v) ≠ c(v)  (S4a's choice is not the target);  AVAIL  c(v) ∈ H_t(v) = {σ_t(v)} ∪ Iσ_t(v) (the target was in the arena)
#   AWAY   switches of v FROM c(v) to another successor (leaving the target); AWAY_MAX the most by one vertex in one phase
#   VMISS  W_{t+1}(v) ◁ W^c(v) (the switch does not reach the target's VALUE; W^c = W of (c, τ), pointwise maximal in G_τ)
#   per phase: WEND_EQ = Even vertices with W_j(v) = W^c(v) at the phase's last state (of EV_PH = Even vertices summed over phases)
#   per vertex: REACH (σ_k(v) = c(v) for some k after its first switch), END (σ_j(v) = c(v)), LEAVE (v starts the phase at c(v) and switches away),
#   SBR = switches of v up to and including the one that lands on c(v) (only for REACH vertices), SW = all switches of v in P.
# Prints one line per game: totals over phases with ≥ 1 Even switch, split fallback / S4a transitions for MISS, and maxima.
import os, sys
ROOT = os.getcwd(); sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
from common import rows, phases, load, readstart, wplay
from n5x import Engine, dual
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None
E, R = rows(g, st, cap=20000); n = g.n; Ed = Engine(dual(g))
EV = [v for v in range(n) if g.owner[v] == 0]
S = dict(ph=0, sw=0, sw_fb=0, miss=0, miss_fb=0, miss_avail=0, miss_unavail=0, verts=0, reach=0, end=0, leave=0, never=0,
         sbr_max=0, sw_max=0, sbr_gt1=0, sw_ph_max=0, vmiss=0, wend_eq=0, ev_ph=0, away=0, away_max=0)
worst = None
for i, j in phases(R):
    tau = R[i]["t"]; assert all(R[k]["t"] == tau for k in range(i, j + 1))
    c = Ed.evaluate(tuple(tau))[1]; Wc = wplay(E, g, [c[v] if g.owner[v] == 0 else -1 for v in range(n)], tau)[0]
    cnt = {}; first_hit = {}; sw_ph = 0; aw = {}
    for t in range(i, j):
        A, B = R[t], R[t + 1]; fb = bool(A["fb"]); imp = None
        for v in EV:
            if A["s"][v] == B["s"][v]: continue
            if A["s"][v] == c[v]: aw[v] = aw.get(v, 0) + 1; S["away"] += 1
            sw_ph += 1; S["sw"] += 1; S["sw_fb"] += fb; cnt[v] = cnt.get(v, 0) + 1
            if E.key(B["W"][v]) < E.key(Wc[v]): S["vmiss"] += 1
            if B["s"][v] != c[v]:
                S["miss"] += 1; S["miss_fb"] += fb
                if imp is None: imp = set(E.improving(tuple(A["s"]), A["vs"]))
                if c[v] == A["s"][v] or (v, c[v]) in imp: S["miss_avail"] += 1
                else: S["miss_unavail"] += 1
            elif v not in first_hit: first_hit[v] = cnt[v]
    if not cnt: continue
    S["ev_ph"] += len(EV); S["wend_eq"] += sum(1 for v in EV if E.key(R[j]["W"][v]) == E.key(Wc[v]))
    S["away_max"] = max([S["away_max"]] + list(aw.values()))
    S["ph"] += 1; S["sw_ph_max"] = max(S["sw_ph_max"], sw_ph)
    for v, k in cnt.items():
        S["verts"] += 1; S["sw_max"] = max(S["sw_max"], k)
        if R[i]["s"][v] == c[v]: S["leave"] += 1
        if v in first_hit:
            S["reach"] += 1; S["sbr_max"] = max(S["sbr_max"], first_hit[v]); S["sbr_gt1"] += first_hit[v] > 1
        else: S["never"] += 1
        if R[j]["s"][v] == c[v]: S["end"] += 1
        if worst is None or k > worst[0]: worst = (k, v, i, j, first_hit.get(v), R[j]["s"][v] == c[v])
print(f"{os.path.basename(sys.argv[1])}: n={n} " + " ".join(f"{k}={v}" for k, v in S.items()) + f" | max-switch vertex (SW, v, i, j, SBR, END): {worst}")
