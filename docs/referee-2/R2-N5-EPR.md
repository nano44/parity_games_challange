# R2-N5-EPR: second-referee check of packet P-N5-EPR (L-NEW box 45: RESTRICT_E, REPRO, EP-0, EP-k, EP-1 ⇐ (Στ), X_SN^pre(E) ≤ len(E); every game). REFEREE-2 (successor 14), written 2026-10-26 06:4xZ-06:5xZ (date -u)
Signature: (Opus 5.5, D15). Lead's order 06:38Z (its stamp).
Object: docs/new/P-N5-EPR-box45.md, `git show a3b1cff3:docs/new/P-N5-EPR-box45.md | sha1sum` -> 8fecca797478d1a77564ac1c5b82d11e952559e0
(= the Lead's pin; = my tree), 160 lines (L-NEW successor 24, frozen l-new 08abd9cb). No fixes file.
Background read (texts): SPEC S1-S5 with FIX 3; RESULTS R17 (c), (e), R18 (d) Lemma S (a), R51 (a), (b), R56 (N-FBRED-3 landing note), R57;
P-N5-XEP §0, §4 (X_SN^pre); P-N5-ACCEL §0 (epochs).
Independence: no docs/referee/ EPR file (trunk and origin/claude/referee, name listing: none); none opened. The lane's
experiments/new/box45/eprestrict.py, itcheck.py not run or imported.
Tools (own code, docs/referee-2/R2-N5-EPR/): epr_check.py (N5 on G: succ. 13's SPEC loop; N5 / N5^τ on G′_E: my own one-step function
transcribed from the same loop, checked against it at every step (SELF)); twin_search.py (DIV search); run_all.sh; logs/; climb/;
instances/. Random start pairs throughout, as the Lead asked.
Labels: PROVED / IMPLICATION (L-NEW 24). Per-epoch bounds; nothing bounds the number of epochs; G-N5-TIME stays OPEN.

## Verdicts (Opus 5.5, D15)
| statement | verdict | notes |
| --- | --- | --- |
| §1 RESTRICT_E (i)-(iv) | SIGN | N-EPR-1 (standing SPEC premise in (i)) |
| §2 REPRO: reproduction of the pairs and fallback types | SIGN | — |
| §2 REPRO: "all of these states lie in ONE phase of that N5^τ run" | NOT SIGNED as stated: FALSE at y′ = y + 1 | GAP G-EPR-1 (repair below) |
| §3 EP-0 (len(E) ≤ n + m if D_E = ∅) | SIGN (statement); proof needs the G-EPR-1 case | G-EPR-1 |
| §3 EP-k (Σ_E len(E); len(E) ≤ transitions of one N5^τ phase on G′_E) | SIGN the sum; the second part only with "+ 1" (or "transitions with source in that phase") | G-EPR-1 |
| §3 EP-1 ((Στ) ⇒ len(E) ≤ T*(G′_E)) | SIGN as an implication with the bound T*(G′_E) + 1; as stated (no + 1) NOT proved | G-EPR-1 |
| §3 Consequence X_SN^pre(E) ≤ len(E) | SIGN | — |
| §4, §5, §6 | not signed (as briefed) | DIV = 0 confirmed independently; DIV > 0 NOT found (§5) |
One gap, G-EPR-1, with a counterexample to the stated clause and a one-line repair; the orders of every bound are unchanged. No (P).
TARGET.md diff: no TARGET.md object claimed.

## 1. RESTRICT_E: SIGN (the Lead's item: identity of Ξ / W / Iσ / S4a / S4c on G and G′_E)
- Setting ✓: G′_E keeps G's vertices, priorities, owners and Even lists; Odd v ∉ D_E gets {τ(v)} (= {σ̄_E(v)}); u ∈ D_E gets {τ(u), σ̄_E(u)}.
- (i) ✓. Every Odd strategy of G′_E is one of G; Lemma S (a) on G (game-general: R56's N-FBRED-3; (VJ) of R57) gives Ξ_k ⊴ V_{σ_k,σ̄′_k} = Ξ′_k;
  Lemma S (a) on G′_E gives Ξ′_k ⊴ V_{σ_k,σ̄_E} = Ξ_k (σ̄_E = σ̄_k on E is a strategy of G′_E); the order is antisymmetric on value triples
  (injective rewards, injective signed weights, then length) ✓. W: G_τ = (G′_E)_τ as games ✓.
  N-EPR-1: "Ξ′_k is S1's valuation on G′_E" uses SPEC's standing requirement that S1's procedure returns an optimal counterstrategy (as in
  every N5 result; 1E-N3, H3-N1). Name it in the landing entry.
- (ii) ✓: Iσ (S2) reads Ξ and Even's lists; S4a's arena (Even v: {σ_k(v)} ∪ Iσ_k(v); Odd v: {τ(v)}) is the same game for G and G′_E, so the
  deterministic S1 run on its dual returns the same σ_new; S4c's switch-all reads Iσ, Ξ's keys and vertex ids ✓. DATA: RII 0 failures.
- (iii) ✓: the dual valuation of τ is S1 on the graph "Odd keeps τ, Even keeps all" — the same for G and G′_E; so Iτ′ = Iτ ∩ E(G′_E) ✓.
- (iv) ✓: Iτ′ ≠ ∅ ⇒ Iτ ≠ ∅ ⇒ S4b ran on G; in-phase ⇒ τ_{k+1} = τ and no Odd fallback ⇒ S4b's output on G was τ; so V_{σ_k,τ} is the
  pointwise minimum over H′_G's Odd strategies (Lemma S (a)); G′_E's arena allows a subset containing τ, so τ is value-optimal there ✓.

## 2. REPRO
- N5^τ's definition (the Lead's item) ✓: S4b^τ keeps τ iff Iτ ≠ ∅ and V_{σ,τ} on S4b's arena H′ equals S1's valuation on H′ against σ; all
  other steps are SPEC's. It is well defined; it differs from N5 only where SPEC's S4b returns a τ_new ≠ τ of the same valuation.
- Reproduction ✓ (induction): in-phase ⇒ Iσ_k ≠ ∅ (else σ_new = σ_k and N5 stops, S4b changes τ, or Odd falls back (FIX 3), each leaving
  the phase); Iσ′_k = Iσ_k; S4a outputs agree; S4b^τ returns τ (Iτ′ = ∅, or (iv)); so the fallback fires on both or neither, is Even's on
  both, and switches the same vertices to the same targets ((ii)) ✓. DATA: REP 0 failures; my step function = the Runner at every step.
- G-EPR-1 (GAP: the "one phase" clause). The proof says "The cycle-node maps agree at every visited pair (RESTRICT_E (i))". RESTRICT_E (i)
  holds for k ∈ E. The last visited pair y′ = y + 1 (when y → y + 1 is in-phase on G) is NOT in E: σ̄|Q changes there, so σ̄_{y+1} ≠ σ̄_E,
  and Ξ′_{y+1} (Odd restricted to G′_E) can have a different cycle node from Ξ_{y+1}. Then the N5^τ run on G′_E LEAVES its λ′-phase at the
  transition y → y + 1, while N5 on G stays in its phase.
  - Counterexample (smallest found): docs/referee-2/R2-N5-EPR/instances/lamend_D0.pg (n 5) from lamend_D0.start. N5 on G: states 1, 2 form one
    phase (λ ≡ 1, τ = (3, 0) on the Odd vertices 1, 3). σ̄ at the Odd vertices: (3, 0) at state 1, (3, 1) at state 2, so E = {1}, len(E) = 1,
    D_E = ∅, G′_E = G_τ. At state 2, λ′ = λ_W ≡ 4 ≠ λ ≡ 1: on G′_E the transition 1 → 2 changes every cycle node, i.e. it is NOT an in-phase
    transition of the N5^τ (= N5) run on G′_E. A |D_E| = 1 instance: instances/lamend_D1.pg (n 7) from lamend_D1.start.
  - Not a corner case: LAMEND (λ′ ≠ λ at y′) in 396 of 3,420 in-phase epoch ends on lib41, 536 of 4,421 on the 𝒞^1O list, 1,063 of 8,436 in all
    (§5), with |D_E| = 0 and 1 both frequent.
  - What survives: the states x … y lie in one phase of the N5^τ run (RESTRICT_E (i) holds there: LAM 0 failures), and the reproduced
    transitions are exactly the len(E) transitions with source in x … y. The last of them may be that phase's exit transition.
  - Repair: REPRO: "… the states (σ_x, τ), …, (σ_y, τ) lie in one phase of that N5^τ run; its len(E) transitions are the transitions of that
    run whose source lies in that phase (the last one may leave it)". EP-k: "len(E) ≤ (in-phase transitions of one N5^τ phase on G′_E) + 1".
    EP-1: "len(E) ≤ T*(G′_E) + 1" — R51 (a)'s T* counts the in-phase transitions of a phase, the boundary transition being the "+ 1" of
    (T* + 1); every order is unchanged.

## 3. EP-0, EP-k, EP-1, and the consequence
- EP-0 ✓ as a statement; its proof needs the G-EPR-1 case. G′_E is one-player (D_E = ∅), Iτ′ = ∅, N5^τ = N5 on G′_E. The y − x transitions
  among x … y are inside one λ′-phase (RESTRICT_E (i)); by R17 (e) at most one of them is a fallback, and a fallback leaves no improving
  edge, so if it occurs it is the last transition of E and y → y + 1 is not in-phase on G (len(E) = y − x ≤ (n + m′ − 1) + 1); otherwise
  y − x ≤ n + m′ − 1 switch-best steps (R17 (c)) plus possibly the exit transition y → y + 1: len(E) ≤ n + m′ ≤ n + m ✓. DATA: EP0 0 failures
  (max len 56 with D_E = ∅).
- EP-k: the sum part ✓ (every in-phase transition has its source in exactly one epoch); the second part with the G-EPR-1 repair.
- EP-1 ✓ as an implication, with the bound T*(G′_E) + 1. (Στ)'s list (the Lead's item) is R48 (i) with R38, R39, R44, R45, R49 and R50 (h) with
  R15, R17, R18 (d), R19, R21 (a), R22, R23 (g), R24, R26, R27, R30 (c), R34 (e), (f), R38 (a): it is the landed per-phase chain of R51 (a) and
  matches R51 (a)'s citation list (R18 (d) S (a), R21 (a), R36 (c), R47 (b), R48 (i), R50 (h)) for the per-phase part; R36 (c), R47 (b) are
  not per-phase and are rightly absent. G′_E ∈ 𝒞^1O with o := u, d_o = 2, n′ = n, m′ ≤ m, Δ′ ≤ Δ ✓; start pairs allowed (R51 (b)) ✓; under
  (Στ), the N5^τ phase containing x … y has f ≤ 2n² and ≤ T*(G′_E) in-phase transitions, so len(E) ≤ T*(G′_E) + 1 = O(m·Δ·n¹¹) ✓. (Στ) is
  NOT claimed, and I do not sign the §4 audit (a text search).
- Consequence ✓: X_SN^pre(E) counts crossings with both ends in E (P-N5-XEP §4), each an in-phase transition with source in E, so
  X_SN^pre(E) ≤ len(E); hence ≤ n + m if D_E = ∅, and O(m·Δ·n¹¹) under (Στ) if |D_E| = 1 (the + 1 does not change the order).

## 4. DIV (the Lead's item: an instance where SPEC's S4b moves τ on G′_E inside an epoch)
- NOT FOUND. DIV = 0 on every sample (§5, 38,834 runs), on 4 hill climbs (objective 1000·DIV + #RIV states, 1,500 steps each, n 5-9) and on
  72,000 runs of twin_search.py (random games with "twin" low-priority successor pairs a, b → w added at Odd choice vertices, to create
  ties). In-phase states with Iτ′ ≠ ∅ (where DIV can happen) are rare: 107 in the natural samples, ≤ 13 per climb / twin batch.
- Why it is narrow (READING, from TIE-W): with |D_E| = 1, Iτ′ ≠ ∅ forces (u, σ̄_E(u)) ∈ Iτ, so W_k = Ξ_k (TIE-W); S4b's arena on G′_E is then
  G′_E itself with Even fixed, so SPEC's S4b output there is S1's own counterstrategy σ̄′_k on G′_E, and DIV happens iff S1's tie-break gives
  σ̄′_k(u) = σ̄_E(u) although on G's (larger) S4b arena it returned τ(u). Not shown impossible; not observed. (Στ) stays unexercised.

## 5. DATA (epr_check.py; own definitions; S3 and random start pairs)
| set | runs | epochs | RI / RII / RIII / RIV checks | REP steps | EP0 checks (max len, D_E = ∅) | LAMEND differs / checks | max len (\|D_E\| = 1) | DIV | violations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lib41.txt (n ≤ 64), S3 + 2 random | 1,101 | 8,770 | 17,522 / 12,172 / 12,172 / 81 | 12,172 | 2,034 (56) | 396 / 3,420 | 92 | 0 | 0 |
| R2-N5-KW/files.lst, S3 + 2 random | 1,509 | 10,677 | 24,630 / 18,374 / 18,374 / 0 | 18,374 | 3,153 (56) | 536 / 4,421 | 92 | 0 | 0 |
| lib2o_noref.lst, S3 + 3 random | 164 | 545 | 1,061 / 584 / 584 / 0 | 584 | 219 (10) | 22 / 68 | 32 | 0 | 0 |
| box-43/44, S3 + 5 random | 60 | 363 | 582 / 272 / 272 / 0 | 272 | 81 (11) | 5 / 53 | 7 | 0 | 0 |
| random 𝒞^kO n 4-12, 3 random pairs | 30,000 | 74,476 | 78,459 / 4,392 / 4,392 / 23 | 4,392 | 35,450 (4) | 83 / 409 | 2 | 0 | 0 |
| random 𝒞^kO n 4-8, 2 random pairs | 6,000 | 13,517 | 14,269 / 817 / 817 / 3 | 817 | 7,268 (2) | 21 / 65 | 2 | 0 | 0 |
- The lane's maxima are reproduced: longest epochs 92 with |D_E| = 1 (returns_ph64) and 56 with D_E = ∅ (x32_rand64) (the lane: 91 / 56 counted
  as y − x; mine count len(E)).
- Mutation control d1 (u ∈ D_E keeps only τ(u) in G′_E): RI 6,403, RII 1,646, REP 1,615, LAM 811 failures on lib41 S3 — the checks bite.
- Reproduce: `sh docs/referee-2/R2-N5-EPR/run_all.sh` (≈ 80 s); `python3 epr_check.py start instances/lamend_D0.pg instances/lamend_D0.start`
  (the G-EPR-1 witness; LAMEND_differs 1); twin_search.py and climb mode as in §4.

## 6. Notes
- G-EPR-1 (gap, minor): REPRO's "one phase" clause is false at y′ (witness lamend_D0.pg, n 5); repair as in §2; EP-k and EP-1 take "+ 1"; EP-0's
  statement stands, its proof needs the exit case.
- N-EPR-1: RESTRICT_E (i) rests on SPEC's standing requirement (S1 returns an optimal counterstrategy), as every N5 result.
- DATA: RESTRICT_E (i)-(iv) and the reproduction hold everywhere; DIV = 0 everywhere; no DIV > 0 instance found (§4).
