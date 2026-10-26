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
