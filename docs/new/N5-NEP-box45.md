# Epochs per phase (N_ep) and the restricted one-player games (box 45)
L-NEW successor 24 (Opus 5.5), D14 / D18, Lead reading L40; Lead's item (3), 07:11Z (Lead's stamp): "can the number of epochs in a phase be
bounded by the number of distinct one-player optima the restricted games G′_E can produce? Or show instance-style why not." Written
2026-10-26 07:27Z (date -u). Working doc, unrefereed. Labels: PROVED / CONJECTURE / OPEN / DATA / READING.
Not a TARGET.md claim; G-N5-TIME stays open.

## 0. Setting
Notation of docs/new/P-N5-EPR-box45.md §0: phase (λ_Ξ, τ constant), epoch E (σ̄|Q constant), its CONFIGURATION C_E := σ̄_E|Q, D_E, G′_E.
The honest frame of E is the one-player game H_E := G_{σ̄_E} (Odd fixed to σ̄_E; Even free); O_E := Even's optimal valuation of H_E (its
"one-player optimum"). On E, Ξ_k = V_{σ_k,σ̄_E} ⊴ O_E (R17 (F1)). Distinct configurations give distinct H_E; equal configurations give the same
H_E, G′_E and O_E.

## 1. Answer: NO, not by the number of distinct optima, and not by the number of distinct configurations (DATA, instance-style)
- Configurations RECUR inside a phase (already P-N5-ACCEL §4: lap_n6_s1_110421, σ̄(2) = 0, 4, 0). So N_ep can exceed the number of distinct
  configurations, hence the number of distinct H_E, hence the number of distinct optima O_E.
- Many epochs, ONE optimum: experiments/red/so/instances/so_th_n32.pg (n 32, sha1 ae9126ad1bf963114bdd56b6e50c8c1cc571779e), from S3: a phase with
  N_ep = 31 epochs and 18 distinct configurations, all of whose one-player games H_E have the SAME optimum valuation O_E (1 distinct optimum);
  one configuration recurs 5 times. Every epoch of that phase has |D_E| ≤ 1.
- Many epochs, many recurrences: experiments/si/orlens/instances/lev_l_x.pg (n 32, sha1 6c365ff7207e92eeaa64a78c0b0220e228cb2963), from S3:
  a phase with N_ep = 50, 14 distinct configurations, one configuration recurring 10 times, 11 distinct optima; every epoch has |D_E| ≤ 1.
- Why distinct optima cannot count epochs (READING): an epoch ends when σ̄|Q changes, i.e. when Odd's best reply to the CURRENT σ changes. O_E
  is about Even's best reply to σ̄_E, a different object: Odd can alternate between replies whose one-player games share Even's optimum
  (so_th_n32), and N5's σ, which is far from that optimum, keeps moving Odd's best reply. The relevant progress measure is Ξ (honest values),
  as in ALT (P-N5-FBK §4: a clean change of σ̄(q) raises Ξ(q) unless it is a tie), not O_E.
- experiments/new/box45/nep.py; outputs out/nep_lib41_k2.txt, out/nep_rand3000.txt, out/nep_named.txt:
| sample | runs | phases | phases with a recurring configuration | max N_ep (n) | max distinct configurations | max recurrences of one configuration (|D| = 1 / |D| = 0) | max N_ep / distinct optima | phases with every epoch |D| ≤ 1 (their max N_ep) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lib41 (n ≤ 64), S3 + 2 random starts, seed 7 | 1,101 | 5,377 | 189 | 50 (32) | 23 | 10 (10 / 5) | 31.0 | 3,814 (50) |
| 3,000 random 𝒞^kO (k 2-4, n 5-18), S3 + 4 random, seed 8 | 15,000 | 40,203 | 2 | 3 (17) | 3 | 2 (2 / 2) | 3.0 | 30,360 (3) |
| lap_n6_s1_110421 and so_th_n32, S3 | 2 | 4 | 2 | 31 (32) | 18 | 5 (3 / 5) | 31.0 | 4 (31) |
- Reading of the data: the phases with the most epochs (50, 31) consist ONLY of epochs with |D_E| ≤ 1. So EP-0 / EP-1 (P-N5-EPR) bound each of
  their epochs, and what is left in them is purely N_ep, i.e. how often Odd's best reply alternates at one vertex at a time.

## 2. What would bound such phases (CONJECTURE REC, and its consequence)
- Configurations with |D| ≤ 1 number at most 1 + Σ_{q ∈ Q} (deg(q) − 1) ≤ m (τ|Q itself, and one deviation at one q).
- CONJECTURE REC: in every phase, every configuration C recurs at most poly(n) times (as the configuration of distinct epochs). DATA: max 10
  recurrences (n 32-40), max 5 for C = τ|Q (D = ∅).
- Consequence (PROVED from REC, EP-0, EP-1): in a phase whose epochs all have |D_E| ≤ 1, N_ep ≤ m·poly(n), so the phase has at most
  m·poly(n)·(T*(G′) + 1) transitions (EP-1 under (Στ) / P-N5-STAU), with no ρ term.
- Why REC is plausible and where it stalls (READING). Fix C. All C-epochs of the phase use the SAME restricted game G′_C and the same honest
  frame H_C; on them Ξ_k = V_{σ_k,σ̄_C}, non-decreasing along the phase (R15 (a)). Their states form a "pseudo-run" of N5^τ on G′_C: runs of
  N5^τ transitions (P-N5-EPR REPRO) separated by jumps that only raise Ξ. A per-phase bound for N5^τ on G′_C that is proved by a MONOTONE
  POTENTIAL in Ξ (a lower bound that only grows) would survive the jumps and bound all C-epochs together. Two obstacles:
  - S4a optimises against τ (in G_τ, the W-frame), not in H_C, so its progress is in W, and W can DROP at fallbacks; for C = τ|Q (D = ∅) the two
    frames coincide (H_C = G_τ), and R17's Lemma P progress (W ⪰ the best simple-path values with ≤ j edges) is gained at every S4a step taken at
    a D = ∅ state whose successor state is also D = ∅; it is not gained at an EXIT step (the next state has D ≠ ∅ and Ξ ⊴ W there), and
    single-state D = ∅ epochs make no Ξ-progress by this argument.
  - The landed 𝒞^1O chain (R48, R50) counts per phase with window inductions that START at a state of the phase; a pseudo-run restarts its
    windows at every jump. Whether the counts are monotone-potential counts (and so survive jumps) is a statement about each lemma, not checked.
- OPEN: REC, even for C = τ|Q.

## 3. What this does not give
- No bound on N_ep. No statement about phases with an epoch of |D_E| ≥ 2 (1,628 of 8,727 lib41 epochs, all short, len ≤ 27 + 1; P-N5-EPR §5).
- The instances of §1 are not counterexamples to any conjecture of the fleet; they refute only the proposed shape "N_ep ≤ #distinct optima".

## 4. Recurrence climbs (DATA; experiments/new/box45/recclimb.py; added 07:35Z by date -u)
Hill climbs (box43 climb.mutate, S3 start) maximising (max recurrences of one configuration in a phase, max N_ep); --d0: recurrences of
C = τ|Q only. Outputs out/recclimb*.txt, best games in out/climb/.
| run | best (recurrences, N_ep) | n |
| --- | --- | --- |
| k 2, n ≤ 12, 3,000 steps, seed 31 | (1, 2) | 9 |
| k 3, n ≤ 16, 3,000 steps, seed 32 | (2, 4) | 15 |
| --d0, k 2, n ≤ 12, 3,000 steps, seed 33 | (1, 4) (no D = ∅ recurrence) | 11 |
| seeded from so_th_n32 (n 32), 2,000 steps, seed 34 | (5, 32) | 32 |
Reading (DATA): random mutation does not grow recurrences beyond what the library already shows (max 10, lev_l_x); no evidence against REC.

## 5. Lemma REC-0: epochs with D = ∅ per phase (PROVED by the lane, unrefereed; Lead's GO 07:36Z, item (1); written 07:49Z by date -u)
Statement (every game). In every phase P of N5, with f := its in-phase fallbacks, the number N_0 of epochs E of P with D_E = ∅ satisfies
    N_0 ≤ (f + 1)(n + 1) + 4n(n − 1) + 1.
With EP-0 (RESULTS R64: len(E) ≤ n + m), the D = ∅ epochs of a phase hold at most N_0·(n + m) transitions.
Premises: R17 (b) Lemma P (its induction step, below), R17 (F1)/(F2); R23 (g) WM (game-general, P-N5-XEP fixes XEP-N2); R21 (a) XW (Ξ ⊴ W);
R15 (a) (Ξ non-decreasing), R15 (d) (≤ 4n(n − 1) consecutive iterations with Ωσ = Ξ and Ωτ unchanged); P-N5-XEP §2 (a) SN-PREFIX_D (a)
(signed by both: along an S4a run, each vertex's unsplit states form a prefix); SPEC S4a; R18 (d) Lemma S (c) (S4a's output is optimal in its
arena against τ).
Setting. τ and λ := λ_Ξ are constant on P. The W-frame is the FIXED one-player game G_τ (Odd fixed to τ); W_k = σ_k's valuation there. A state is
ALL-UNSPLIT if λ_W = λ there. At a D = ∅ state, σ̄ = τ on Q, so Ξ = W, and the state is all-unsplit. For j ≥ 0, LEVEL j at a state k means:
W_k(x) ⪰ value(r) for every vertex x and every simple path r of G_τ with ≤ j edges from x to a cycle node u of λ (value(r) := (u, P(r), |r|),
as in R17 Lemma P). B := the pointwise maximum of value(r) over all such r (any length ≤ n − 1).
Proof.
1. (Lemma P step, reused.) If k is a D = ∅ state with level j, k → k+1 is an S4a step, and k + 1 is all-unsplit, then k + 1 has level j + 1.
   At k, Ξ_k = W_k, so the gates Iσ_k are exactly the W-improving edges of G_τ, and S4a's arena (Even: {σ_k(v)} ∪ Iσ_k(v); Odd: τ) is the
   switch-best arena H_k of G_τ; S4a's output is an optimum of it (Lemma S (c)). λ_W is λ at k and at k + 1. R17 Lemma P's induction step uses
   exactly these facts (the hypothesis at k, the arena, (F1)/(F2), and that the step stays in the λ_W-phase), and R17 (d) notes that it holds for
   every pointwise-optimal choice. So level j + 1 at k + 1.
2. (Persistence.) If k → k+1 is an S4a step with k, k + 1 all-unsplit, level j at k gives level j at k + 1: WM (W_{k+1} ⊵ W_k), and the cycle nodes
   of λ are unchanged. Level 0 holds at every all-unsplit state (Ω(u) = (u, ∅, 0) for a cycle node u of λ = λ_W).
3. (Runs.) Split the phase at its f fallback transitions into ≤ f + 1 fallback-free runs R. By SN-PREFIX_D (a) for every vertex, the all-unsplit
   states of R form a prefix U(R) of R. So inside U(R) the level only grows (2), by one at each S4a step from a D = ∅ state to a state of U(R) (1).
4. (Saturation.) Call a D = ∅ state t SATURATED if W_t = B. At an all-unsplit state, W_t(x) is the value of x's play, i.e. value(r) for the simple
   path r from x to λ(x), a cycle node of λ; so W_t ⊴ B. Hence a D = ∅ state with level n − 1 (every simple path has ≤ n − 1 edges) is saturated.
   Let t be the first saturated D = ∅ state of P (if any) and t* the last D = ∅ state of P. For every D = ∅ state t′ ≥ t: Ξ_{t′} = W_{t′} ⊴ B = Ξ_t
   and Ξ_{t′} ⊵ Ξ_t (R15 (a)), so Ξ_{t′} = B. By R15 (a) again Ξ is constant (= B) on [t, t*]; τ is constant, so Ωσ and Ωτ are unchanged on
   every transition there, and R15 (d) gives t* − t ≤ 4n(n − 1). So at most 4n(n − 1) + 1 D = ∅ epochs meet [t, t*].
5. (Before saturation.) Every D = ∅ epoch E = (x, …, y) with y < t (or every D = ∅ epoch, if no state is saturated), except possibly the last epoch
   of P, has an in-phase last transition y → y + 1 from the D = ∅ state y; these transitions are distinct for distinct epochs. Each is
   (i) a fallback (≤ f), or (ii) an S4a step that leaves U(R) of its run (≤ 1 per run, ≤ f + 1), or (iii) an S4a step from a D = ∅ state into
   U(R). By 1-3, after n − 1 steps of kind (iii) in one run, the next D = ∅ state of U(R) has level n − 1, hence is saturated (4); so before t,
   kind (iii) occurs ≤ n − 1 times per run, ≤ (n − 1)(f + 1) in all. Total before t: ≤ f + (f + 1) + (n − 1)(f + 1) + 1 = (f + 1)(n + 1).
6. Sum: N_0 ≤ (f + 1)(n + 1) + 4n(n − 1) + 1. □
- What it does NOT give: a bound free of f. The W-level is lost at fallbacks (W may drop there) and at a split; the Ξ-level (permanent) grows
  only at D = ∅ → D = ∅ steps, so single-state D = ∅ epochs are charged to W-progress, hence to f. With RESULTS R56 (f ≤ 1 + (n − 1)(2 + ρ)),
  N_0 = O(n²(1 + ρ)); on 𝒞^kO with FB-kT (P-N5-FBK, both referees signed, conditional on R56 and P-N5-2T), f = O(n^{k+1}) and N_0 = O(n^{k+2}).
  So REC for C = τ|Q is REDUCED to f (fallbacks per phase), not proved outright.
- DATA (experiments/new/box45/rec0.py; out/rec0_*.txt): lib41 × 3 starts (1,101 runs, 5,377 phases) and 3,000 random 𝒞^kO × 5 (15,000 runs,
  40,203 phases): 0 violations of REC-0; max N_0 = 5 (n 24) and 2; max N_0 / (f + 1) = 5.0; kind-(iii) steps per run ≤ 4 (n − 1 predicted).
- Adversarial climbs on N_0 (recclimb.py --d0; out/recclimb0_*.txt, best games out/climb/): seeded from so_th_n32 (1,500 steps, seed 41):
  (N_0 5, N_ep 31), no growth; k 3, n ≤ 20, 4,000 steps, seed 42: (2, 7); k 2, n ≤ 16, 4,000 steps, seed 43: (2, 3). No instance beyond the
  library's N_0 = 5; REC-0's bound is far above every observed N_0.
