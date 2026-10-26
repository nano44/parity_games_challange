# R93: CONJECTURE C-ONCE_X is DEAD (a direct-gate ladder; k X-migrations of one vertex in one PURE C-interval)
L-RED successor 22 (Opus 5.5; D14/D15/D18, Lead 16:34Z target (1b)). Written 2026-10-26 ~18:1xZ (date -u). Labels (D18 / L40): DEAD / DATA.
Target: docs/si/N5-GCX-box21.md §4 (l-si f984baa0), quoted:
> Survives (DATA only, thin): the X_u form C-ONCE_X (migrations INTO a D-direct gate): migx_per_vertex_max = 1 on every set of §2 and on the
> climbs […] I expect C-ONCE_X to die to a better climb. Not proposed for proof.
An X-MIGRATION into u at t → t+1 is defined in P-N5-GCX-box21.md §1 (trunk sha1 5a91bebb): a vertex z ∈ R_u(t+1) ∖ (R_u(t) ∪ A_t), with
u ∈ DD_t ∩ DD_{t+1}.

## 1. Result (DEAD, verified)
Family cxmig_k (experiments/red/ul/mkcx.py k). One vertex x makes k X-migrations into D-direct gates inside ONE C-interval [0, k + 7] of
class b. The interval is PURE: D ∩ U = DD, every gate is D-direct, with constant offsets. It has no fallback, λ_W is constant, and it is
one phase.

| instance (experiments/red/ul/instances/) | sha1 game | sha1 start | n | iterations n5 / n5b (fb) | C-interval | X-migrations of x |
| --- | --- | --- | --- | --- | --- | --- |
| cxmig_k4_n54 | a3893ea4… | d0c8d8ed… | 54 | 12 / 12 (0) | [0, 11] | 4 (x = 17) |
| cxmig_k8_n82 | 4fa6ee8f… | a8d3c8e8… | 82 | 16 / 16 (0) | [0, 15] | 8 (x = 25) |
| cxmig_k16_n138 | 9f29476d… | a5e2b99b… | 138 | 24 / 24 (0) | [0, 23] | 16 (x = 41) |

Evidence:
- experiments/red/ul/vrun.sh: n5.py (SPEC) = n5b --mode spec. check_sol2 prints "zielonka(oink zlk) OK strategies verified" for both.
- My checker ulx.py (XMIG_PER_VERTEX, written from P-N5-GCX §1) gives 4, 8, 16.
- L-SI's gcx.py (reference, l-si 721de60a, unmodified) prints MIG2X_cint = 1 and migx_per_vertex_max = 4, 8, 16.
- Control: ulx.py with MUT=1 on nep90_n40 (whole run as one interval) finds vertices 1, 26, 28 X-migrating twice in run [0, 14]. That is
  L-SI's own control result. Unmutated, nep90 gives none.

## 2. The construction
- Clock C1: mkreader's Bellman-Ford chain v_0 … v_L (L = k + 1). The wave reaches v_L, v_{L−1}, … at ticks 1, 2, ….
- Rungs j = 0 … k:
  - Each rung is an Odd gate d_j → {h_j, h′_j}, with h_j → {w_j, u_0} and h′_j → w_j. Here w_j = v_{L+1−j} (w_0 = p0).
  - rank(h′_j) > rank(h_j), so σ̄(d_j) = h_j and τ(d_j) = h′_j. Both exits are in A and both read w_j, so the offset
    Δ(d_j) = w(h′_j) − w(h_j) is constant: every d_j is D-direct for the whole interval.
- x → {d_0 … d_k}:
  - Ξ(x via d_j) jumps when the wave reaches w_j, and the rung weights rise with j. So x moves to the newest rung at each tick.
  - Each move takes x from R_{d_{j−1}} into R_{d_j}, i.e. one X-migration.
  - In this pure interval W = Ξ + Δ_j on each region, so the climb is Ξ-driven.
- τ is Odd-optimal (I_τ = ∅):
  - Even's best reply from h_j escapes to u_0 of a slower chain C2 (u_0 … u_{k+6}). C2's top G2 ranks above every h′.
  - C2's early values (the o′-level) sit below C1's, so (h_j, u_0) is not Ξ-improving during the run.

## 3. Scope
- DEAD: C-ONCE_X, in a PURE interval, with migrations per vertex growing linearly in n.
- Not touched: UL_C on pure intervals. This run has no U events: every move is Ξ-improving and W-best at once.
- Also, the X_u per gate here is 1. The growth is per VERTEX, not per gate.
