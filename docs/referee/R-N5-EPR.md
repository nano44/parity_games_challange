# R-N5-EPR: REFEREE report on packet P-N5-EPR (L-NEW box 45: RESTRICT_E, REPRO, EP-0, EP-k, EP-1 under (Στ); every game)
Referee: REFEREE (successor 12, session_01KNDBjZvPFLaNjEdCmEWBcN), Opus 5.5 (owner ruling D15).
- Routing: the Lead's message of 06:38Z (Lead's stamp).
- Object: docs/new/P-N5-EPR-box45.md at trunk a3b1cff3, sha1 8fecca797478d1a77564ac1c5b82d11e952559e0 (checked with
  `git show a3b1cff3:docs/new/P-N5-EPR-box45.md | sha1sum`; identical on my tree), 160 lines, frozen at l-new 08abd9cb. Author: L-NEW successor 24.
- Written 2026-10-26T06:39Z-06:44Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/ EPR file on my tree; none opened. No lane code run (experiments/new/box45/eprestrict.py,
  itcheck.py). D1.
- Premises checked: SPEC S1-S5 (S4b: "τ_new = Odd's optimal counterstrategy (S1 procedure on H', not dual) to σ"; S4c; S4d); R18 (d) Lemma S
  (a) on every game (my R-N5-1E §1, from VJ00's text; signed on every game as (VJ) in P-N5-1E); R17 (c), (e) (landed text, RESULTS R17);
  R48 (i), R50 (h), R51 (a), (b) for EP-1.
- Tool: scratch/epr_probe.py (own engine; N5^τ written from SPEC with S4b^τ; random start pairs). Logs scratch/epr_logs/ (run_all.sh).

## Verdicts
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 | RESTRICT_E (i)-(iv) | SIGNED |
| §2 | REPRO: N5^τ on G′_E from (σ_x, τ) visits (σ_x, τ), …, (σ_{y′}, τ) with the same fallback types | SIGNED |
| §2 | REPRO's last clause: "all of these states lie in ONE phase of that N5^τ run (λ′ = λ on them, by RESTRICT_E (i))" | SIGNED WITH GAP EPR-1: true for x..y; FALSE in general for y′ = y + 1 (counterexample below); repair stated |
| §3 | EP-0: D_E = ∅ ⇒ len(E) ≤ n + m | SIGNED (the bound survives EPR-1; proof wording note EPR-N1) |
| §3 | EP-k (reduction) | SIGNED WITH GAP EPR-1 (len(E) ≤ 1 + the in-phase transitions of one N5^τ phase on G′_E) |
| §3 | EP-1 as an IMPLICATION from (Στ) | SIGNED WITH GAP EPR-1 (len(E) ≤ T*(G′_E) + 1; the order O(m·Δ·n¹¹) is unchanged) |
| §3 | Consequence: every count inside one epoch, in particular X_SN^pre(E), is ≤ len(E) | SIGNED |
| §4-§6 | (Στ) audit, TIE-W, data, combination | not signed (as briefed) |
One gap, EPR-1 (an off-by-one at the epoch's last transition; asymptotics unchanged). Not a running-time bound (no bound on N_ep; |D_E| ≥ 2
open). Not a TARGET.md claim; G-N5-TIME stays OPEN.

## 1. RESTRICT_E (the Lead's first point)
- (i) Every Odd strategy of G′_E is one of G. Lemma S (a) on G: Ξ_k ⊴ V_{σ_k,σ̄′_k} = Ξ′_k. Lemma S (a) on G′_E: Ξ′_k ⊴ V_{σ_k,σ̄_E}, and σ̄_E is a
  strategy of G′_E (off D it equals τ, on D it is one of the two kept edges) with V_{σ_k,σ̄_E} = Ξ_k (σ̄_k = σ̄_E on E) ✓. The order is
  antisymmetric on play values (injective rewards; distinct path sets have distinct signed weights; then length), so Ξ′_k = Ξ_k ✓. W: G_τ and
  (G′_E)_τ are the same one-player game ✓. Both uses of Lemma S (a) are on positional strategies, within its scope ✓.
- (ii) Iσ is read from Ξ and Even's (unchanged) lists ✓. S4a's arena (Even: {σ_k(v)} ∪ Iσ_k(v), Odd: τ(v)) is literally the same game,
  successor lists in the same order, and S1 is deterministic ✓. S4c's Even switch-all reads Iσ, Ξ, indices ✓.
- (iii) The dual S1 run for τ is on the graph where Odd keeps τ only and Even keeps its lists: the same for G and G′_E; Iτ′ = Iτ ∩ E(G′_E) ✓.
- (iv) Iτ′ ≠ ∅ ⇒ Iτ ≠ ∅, so S4b runs on G; in-phase ⇒ τ_{k+1} = τ; if S4b's output were τ_new ≠ τ, S4d would set τ := τ_new; so S4b's output
  on G is τ, i.e. τ is S1's counterstrategy on H′_G and V_{σ_k,τ} is the pointwise minimum there (Lemma S (a)). G′_E's arena is a sub-arena
  containing τ, so τ is value-optimal there too ✓.
- Standing premise (as 1E-N3): Lemma S (a) for "S1's valuation" assumes S1's procedure returns an optimal counterstrategy.
- VERDICT: RESTRICT_E (i)-(iv) SIGNED. "Ξ, W, Iσ, S4a's output and S4c's Even switch identical on G and G′_E at every state of the epoch":
  yes, at every k ∈ E.

## 2. REPRO (the Lead's second point) and gap EPR-1
- N5^τ's definition (§0): SPEC S1-S5 with S4b replaced by S4b^τ ("if Iτ ≠ ∅ and τ is value-optimal against σ in S4b's arena H′, τ_new := τ;
  otherwise SPEC's S4b output"); S1, S2, S3, S4a, S4c, S4d, S5 are SPEC's. So it differs from SPEC exactly in keeping a value-optimal τ ✓.
  It still changes σ or τ at every iteration (a kept τ with S4a's output σ triggers S4c), so R15 (d)'s termination argument applies.
- The induction over k ∈ [x, y′ − 1]: in-phase ⇒ Iσ_k ≠ ∅ (otherwise N5 stops, or τ changes by S4b or by Odd's fallback) ✓; Iσ′_k = Iσ_k (ii) ✓;
  S4a's output the same (ii) ✓; S4b^τ returns τ (SPEC if Iτ′ = ∅, else (iv)) ✓; on G, S4b's output is τ (in-phase) ✓; so the fallback fires
  on both or neither, is Even's on both, and switches the same vertices to the same targets ✓. Every k used is in E (y′ − 1 ≤ y) ✓. So the
  state sequence and fallback types are reproduced ✓.
- EPR-1 (GAP). The last clause, "all of these states lie in ONE phase of that N5^τ run (λ′ = λ on them, by RESTRICT_E (i))", includes the
  state y′ = y + 1 when y → y + 1 is in-phase on G. But y + 1 ∉ E (σ̄|Q changed there), so RESTRICT_E (i) does not apply at y + 1: on G′_E
  the Odd vertices outside D_E are forced to τ, and Odd may have lost the choice that gave λ_{y+1}. Then λ′ at (σ_{y+1}, τ) ≠ λ, and the
  transition y → y + 1 LEAVES the N5^τ phase on G′_E.
  - Counterexample: experiments/new/box44/instances/fb17_n32.pg (sha1 398e23e2eb18aac3c75af0b500a5d292f57a1d1e), from S3. Q = {11, 23},
    τ|Q = (6, 4). Epoch E = (26) (x = y = 26), D_E = {11}; at 27, σ̄(23) changes 4 → 18 (a new epoch), τ and λ unchanged on G (same
    phase). N5^τ on G′_E moves 26 → 27 to exactly σ_27 (no fallback), as REPRO says; but λ′ at 27 ≠ λ_27 (vertices 0, 1, 4, 5, 7, 8, 9, 10, …:
    cycle node 18 on G, 12 on G′_E, where 23 is forced to τ(23) = 4). So state 27 is in a different phase of the N5^τ run.
  - Frequency (my data): of the epochs ending at an in-phase transition, λ′ at y + 1 differs from λ in 491 of 3,791 (lib41: 403 of 3,358; 240
    of them with |D_E| = 1).
  - Repair: "the states (σ_x, τ), …, (σ_y, τ) lie in one phase of the N5^τ run; the transition y → y′ has its source in that phase and may
    leave it". Then the transitions of E are the in-phase transitions of one N5^τ phase plus at most one transition leaving it.
- VERDICT: REPRO SIGNED (state sequence, fallback types, states x..y in one phase); its last clause at y′ WITH GAP EPR-1.

## 3. EP-0, EP-k, EP-1, the consequence
- EP-0: the bound holds despite EPR-1. G′_E is one-player (D_E = ∅), so N5^τ = N5 on G′_E and N5's Even step is switch-best with a fallback
  only in the value-flat situation, after which no improving edge is left and the run stops (R17 (e)). R17 (c): a λ-phase has fewer than
  n + m′ in-phase steps. The states x..y lie in one λ′-phase; the transitions of E are its in-phase steps plus, at most, one final
  transition (the exit to y + 1, or a fallback, which ends the run; not both). So len(E) ≤ (n + m′ − 1) + 1 ≤ n + m ✓. EPR-N1 (wording):
  the proof's "len(E) consecutive N5 iterations on G′_E inside one λ-phase" should say "the last one may leave it"; the arithmetic already
  allows it.
- EP-k: the sum identity is correct ✓. Its second part, "len(E) is at most the number of transitions of one phase of an N5^τ run on G′_E",
  holds if a phase's transitions include the one leaving it; in the convention of R51 (a) (T* bounds the in-phase transitions; leaving
  transitions are counted separately) it needs "+ 1" (EPR-1).
- EP-1 (the implication): G′_E ∈ 𝒞^1O with o = u, d_o = 2, n′ = n, m′ ≤ m, Δ′ ≤ Δ ✓; start pairs allowed (R51 (b)) ✓; under (Στ), the N5^τ phase has
  f ≤ 2n² and ≤ T*(G′_E) in-phase transitions (R48 (i), R50 (h), monotone in f as R51 (a) uses) ✓. With EPR-1, len(E) ≤ T*(G′_E) + 1, not
  ≤ T*(G′_E). The order O(m·Δ·n¹¹) is unaffected.
- (Στ)'s list (the Lead's third point): it names R48 (i) and R50 (h) with the per-phase statements they cite and "their own landed chains",
  for every N5^τ phase on 𝒞^1O from every start pair. That covers everything EP-1's proof uses (R48 (i), R50 (h) and its monotonicity in f,
  start-freeness), so it is complete for EP-1, by construction (the catch-all "own landed chains"). Being a catch-all, it is also exactly as
  strong as "the whole 𝒞^1O per-phase chain holds for N5^τ"; the §4 audit that would discharge it is a text search, not signed.
- Consequence: every count with both ends of its transitions in E (or with source in E) is ≤ len(E) ✓, in particular X_SN^pre(E) (crossings with
  both ends in E) ✓. Unaffected by EPR-1 (len(E) is defined on G).
- VERDICT: EP-0 SIGNED; EP-k and EP-1 SIGNED WITH GAP EPR-1 (repair: "+ 1"); the consequence SIGNED.

## 4. Data (DATA, not proof; scratch/epr_probe.py, own engine; logs scratch/epr_logs/)
Checks per epoch: R1-R4 (RESTRICT_E (i)-(iv)) at every k ∈ E; REP (my own N5^τ on G′_E reproduces σ and the fallback flags through y′); EP0;
counts DIV (SPEC's own S4b on G′_E would move τ inside the window) and EXITLAM (λ′ at y + 1 ≠ λ, EPR-1).
| set | runs | epochs (by \|D\|: 0 / 1 / 2 / ≥3) | max len(E) by \|D\| | R1-R4 / REP / EP0 failures | EXITLAM / exits checked | DIV |
| --- | --- | --- | --- | --- | --- | --- |
| lib41, n ≤ 64, S3 + 2 random | 1,101 | 8,751 (2,053 / 5,045 / 295 / 1,358) | 56 / 92 / 28 / 18 | 0 | 403 / 3,358 (240 with one D-vertex) | 0 |
| box-43/44 instances, S3 + 4 random | 55 | 336 (65 / 94 / 114 / 63) | 5 / 14 / 18 / 10 | 0 | 3 / 46 (all with one D-vertex, fb17_n32) | 0 |
| 3,000 random 𝒞^kO (k 2-4), n 5-18, seed 92, S3 + 4 random | 15,000 | 43,544 | 4 / 3 / 2 / 2 | 0 | 85 / 387 | 0 |
- RESTRICT_E and REPRO's state / fallback reproduction: 64,331 state checks, 52,631 epochs, 0 failures; my N5^τ agrees with the packet's.
- DIV = 0 in my data too: premise (Στ) is never exercised here (N5^τ and SPEC's N5 coincide on G′_E inside each epoch window).
- EXITLAM: 491 epochs (263 with |D_E| = 1) whose last transition leaves the N5^τ phase on G′_E — the EPR-1 counterexample is common, not
  rare. The lane's REP_V checks σ and fallback flags (which hold), not λ′ at y′.
- Reproduce (from docs/referee/scratch): `sh epr_logs/run_all.sh` (fixed seed; file starts seeded by the RELATIVE path).

## 5. Notes for the fixes file
- EPR-1 (gap): REPRO's last clause holds for x..y only; the transition y → y′ may leave the N5^τ phase (fb17_n32, S3, epoch (26)). Repairs:
  REPRO "states x..y in one phase; the last transition has its source there"; EP-k "len(E) ≤ 1 + in-phase transitions of one N5^τ phase";
  EP-1 "len(E) ≤ T*(G′_E) + 1".
- EPR-N1: EP-0's proof wording (the last transition may leave the λ-phase; the bound n + m already allows it).
