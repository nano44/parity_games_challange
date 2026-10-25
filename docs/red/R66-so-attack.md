# R66: adversary on P-N5-SO and P-N5-LP §4 (J ≤ S_o, K) (L-RED successor 15, box 36; GO 2026-10-25 01:22Z, date -u)
Targets (Lead 01:22Z): docs/new/P-N5-SO-box32.md (sha1 deb5ee44, pinned at trunk 1ef02bb: Lemma TH, Lemma SO, Corollary XJ) and
docs/new/P-N5-LP-box32.md (sha1 d2c8121a) §4, read with its fixes file docs/new/P-N5-LP-fixes-box32.md (DF FALSE, DF′ replaces it).
In order: (1) S_o > d_o(Θ+1) in one phase; (2) Θ > (n−1) + n(X+1) + X; (3) J > S_o; (4) K (wakes) growth per phase.
𝒞^1O only: one Odd vertex with out-degree > 1, asserted in the checker. Referees were not contacted. Labels per L40. G-N5-TIME stays
OPEN.

## 0. Result in one line
NO KILL. 0 failures of TH, SO, J ≤ S_o and of every sub-claim of their proofs, over 230 library files, 2,000 random games and
about 2.6 M climb evaluations. Three things are new (DATA):
- the (d_o − 1)(Θ + 1) term of SO is needed;
- J = S_o is attained;
- K = 2 occurs.

## 1. Checker: experiments/red/so/sox.py, written from the frozen text
I wrote the checker myself; L-NEW's box32/socheck.py was read but not used.
- Trace: its own copy of experiments/new/n5.py run(). On every file it is asserted equal to n5.run in iterations and fallbacks.
- Engine: L-SI experiments/si/si.py, read-only.
- Definitions (P-N5-LP §0-§1, P-N5-SO header):
  - Phase: a maximal run of transitions with λ_Ξ (all vertices) and τ constant.
  - R_k := {o} ∪ {v : the (σ_k, τ_k)-play from v reaches o}. A crossing is a transition with R_k ≠ R_{k+1}.
  - θ = Ξ(o) and Θ := the number of θ-changes. d_o := |succ(o)|.
  - S_o := the number of transitions with σ̄(o) changed and λ(o) ≠ o.
  - J := the number of non-tame transitions: COARSE_{M_k}(Ξ_{k+1}) ≠ COARSE_{M_k}(Ξ_k), where M_k is the max gate level (R25).
  - K := the number of transitions with a wake (LP §3 definition).
    - Consecutive relevant transitions k < k′ (L_k ≠ ⊥), with no fallback in [k, k′] and R constant on [k, k′+1].
    - A wake is a relevant Even switch at k′ of level > L_k.
- Checked per phase: TH, SO and J ≤ S_o, exactly as stated.
- Checked at every in-phase transition, each with its own counter:
  - CAP1: σ̄(o) is a full Ξ-minimiser, and θ = o ⊕ Ξ(σ̄ o).
  - TIE: at a relevant σ̄(o) change with θ unchanged, the old choice is not in T_{k+1}.
  - TSHRINK: T_{k+1} ⊆ T_k on a θ-run.
  - RUN: at most d_o − 1 θ-fixed changes per θ-run.
  - KEY: for x ∈ T_k ∩ T_{k+1}, the H-path to c is unchanged. This is the proof's "keys are frozen" step.
  - H1C: H1 is constant on crossing-free intervals.
  - THH1: under H1, at a crossing-free θ-change, x0 = σ̄_k(o) is in F and Ξ(x0) changes.
  - THN: under ¬H1, θ = (c, ∅, d).
  - J1: at a non-tame transition, σ̄(o) changes at a level > M_k.
- Trap 3 (a checker that tests less than the packet): every statement and proof step listed above is tested at its own threshold.
- Trap 2 (degenerate maxima): the J − S_o fitness counts only phases with J ≥ 1. A first j climb had settled on J = S_o = 0; it was
  killed and restarted.

## 2. Reading of the proofs against the code (READING, L-RED)
These are the steps a kill would have to break.
- **SO, the tie-break.**
  - Even cycle node (longest-path mode): si.py l.154-171. `longest` keeps the first successor in hs[o] (ascending ids) with a
    strictly larger distance, so the choice is the least id in T. The key is the vertex id itself, fixed.
  - Odd cycle node (BFS mode): si.py l.172-180. Layer order is (position of the parent in the previous layer, id in hp[parent]). hp
    lists are built in ascending id order, and restrict only deletes from them. So the discovery order is the length-lexicographic
    order of root-first id sequences of the tree path: a function of the path alone.
  - Every non-o vertex on the path of x ∈ T has one successor in hs (Even: σ; Odd: forced on 𝒞^1O). So the key of x depends only on
    x's H-path, which is the proof's claim.
- **SO, the strictness of ⊕ at the first switching vertex p.** The fixes file (§4, N-LP-1) notes that ⊕ need not keep strictness in
  general. Here it does, because neither Ξ_k(old successor of p) nor Ξ_{k+1}(new successor of p) contains p:
  - λ_{k+1}(p) = c ≠ p, so the new play from p does not return to p;
  - the old successor lies on p's own path.
  With p in neither value, adding p keeps the top difference, or lengths +1 on both.
- **TH and J ≤ S_o:** no gap found. The ¬H1 count uses only that θ is monotone (R15 (a)) and that d ∈ [0, n − 1]. J ≤ S_o is J1
  plus the relevance of the σ̄(o) change.

## 3. Data (DATA; all 0 failures)
| set | files / games | phases | max Θ | max S_o | max X | max J | max K | max θ-fixed changes in a θ-run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LIB: c1o_list.py 48 (every 𝒞^1O .pg with n ≤ 48 in experiments/) | 230 | 280 | 51 (lev_l_x) | 49 (lev_l_x) | 84 (b6_xl_n48) | 18 (rel2_x31_rx48) | 1 (nowake_cex_n32) | 1 |
| RAND: sorand.py 2000 8 24 3601 | 2,000 | 420 | 2 | 1 | 3 | 0 | 0 | 1 |
| 8 climbs, soclimb.py, 40-50 min each | ≈ 2.6 M evaluations | — | 33 | 22 | 31 | 19 | 2 | 15 |
- Climbs (soclimb.py; fitness = failures first, then the mode's measure):
  - tie, from a random game (n 24) and from lev_l_x (n 32);
  - sor (θ-runs with ≥ 2 θ-fixed changes), from a random game (n 24) and from the tie best (n 32);
  - j (J − S_o), from rel2_x31_rx48;
  - k: two rounds from nowake_cex_n32;
  - th (Θ), from a random game (n 32).

## 4. Instances: experiments/red/so/instances/
Each one passed experiments/red/so/vrun.sh:
- 𝒞^1O asserted;
- n5.py = n5b.py in iterations and fallbacks;
- `check_sol2.py` "zielonka(oink zlk) OK strategies verified";
- sox 0 failures.

| file | sha1 | n | o | it / fb | phase: Θ, S_o, X, J, K, d_o | point |
| --- | --- | --- | --- | --- | --- | --- |
| so_tie13_n24.pg | 0ff10c906ad3fc5f8c6348e77da5e8f4d905c570 | 24 | 0 | 16 / 0 | 1, 15, 14, 0, 0, 15 | 13 θ-fixed changes in one θ-run (cap d_o − 1 = 14); SO bound 29 |
| so_tie15_n32.pg | ccfeed8908870e134a30d80dc24511836b7401fb | 32 | 13 | 20 / 0 | 1, 18, 0, 0, 0, 21 | 15 in one θ-run (cap 20), crossing-free (X = 0); SO bound 41 |
| so_sor5_n24.pg | 42f9fa79bbd3cf1762220acbd42b296454097312 | 24 | 2 | 23 / 0 | 6, 22, 18, 1, 0, 19 | 6 θ-runs with ≥ 2 θ-fixed changes; 16 pure tie-break moves; SO bound 132 |
| so_sorl_n32.pg | ce8f7013eb1d17bf03604d9e0afcec7c639cdb8d | 32 | 13 | 22 / 0 | 4, 22, 0, 0, 0, 23 | S_o = 22 with Θ = 4 and X = 0; SO bound 114 |
| so_j19_n48.pg | eb7e232bf0abe2c20acc2d0cb8f26554640937cb | 48 | 0 | 25 / 1 | 19, 19, 20, 19, 0, 21 | J = S_o = 19 (equality) |
| so_k2_n32.pg | fb3d3c0c99a5c0402d0d4950819d0d0b879db766 | 32 | 27 | 20 / 2 | first phase: 0, 0, 0, 0, 2, 13 | first K > 1 |
| so_th_n32.pg | ae9126ad1bf963114bdd56b6e50c8c1cc571779e | 32 | 3 | 36 / 0 | 33, 30, 31, 3, 0, 18 | Θ climb; TH bound 1,086 |
- Side observation: on nowake_cex_n32 (L-NEW, not mine), n5b.py from its default start makes 3 iterations, against n5.py's 9.
  The two start rules are not the same object, so this is not a finding against either; n5.py = n5b.py on all 7 of my instances.

## 5. Findings (labels)
- (1) DATA: SO is not refuted. Its d_o-term is genuinely used.
  - A single θ-run can carry Θ-free σ̄(o) changes up to 15 of the d_o − 1 = 20 allowed (so_tie15_n32), and several runs can carry them
    in one phase (so_sor5_n24: 6 runs).
  - So "S_o ≤ Θ + O(1)", which LIB suggested (S_o ≤ Θ there), is FALSE on climbed data: S_o 18 with Θ 1. SO's statement allows this.
  - Every such change was a pure tie-break move (old and new choice both in T_k). In every one, the old choice left T, as SO's proof
    says; TIE and KEY had 0 failures.
- (2) DATA: TH is not refuted and is far from tight: max Θ / bound = 51 / 756 (lev_l_x, n 32, X 21) and 33 / 1,086 (so_th_n32, n 32, X 31).
  Θ can exceed X (so_sorl_n32: Θ 4, X 0; lev_l_x: 51 vs 21), so the n(X + 1) term is not vacuous, but no phase came near it.
- (3) DATA: J ≤ S_o is attained with equality: J = S_o = 19 at n 48 (so_j19_n48). The climb never got J − S_o above 0.
- (4) DATA: K reached 2 per phase (so_k2_n32) and stayed at 2 through two climbs (≈ 460 k evaluations). No growth seen.
- OPEN: X per phase, K per phase, G-N5-TIME.

## 6. Reproduce
- `python3 experiments/new/box32/c1o_list.py 48 | awk '{print $1}' | xargs python3 experiments/red/so/sox.py` (LIB)
- `python3 experiments/red/so/sorand.py 2000 8 24 3601` (RAND)
- `python3 experiments/red/so/soclimb.py tie|sor|j|k|th seed secs OUT (seed.pg | --rand n)` (climbs)
- `experiments/red/so/vrun.sh experiments/red/so/instances/<file>` (verification; needs scripts/setup_oink.sh)

## 7. Correction (box 37, 2026-10-25 ~04:10Z, date -u)
- The §4 side observation (n5b 3 vs n5.py 9 iterations on nowake_cex_n32) was an artefact of n5b's default `--mode orig`, which uses
  L-COMP's own A5 tie-break. With `--mode spec`, n5b gives 9 / 2 = n5.py there.
- vrun.sh now runs n5b with `--mode spec`. All instances in experiments/red/so/instances/ agree with n5.py in that mode (R67 §4).
