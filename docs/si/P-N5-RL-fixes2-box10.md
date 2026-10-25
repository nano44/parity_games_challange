# Fixes to packet P-N5-RL, part 2: REFEREE-2's items and a concordance of both reports
L-SI successor 6 (Opus 5.5; D14, D15, D18, L37, L40). Written 2026-10-25 ~13:05Z (date -u), at the Lead's request (12:43Z).
- Object: docs/si/P-N5-RL-box10.md, sha1 0a3c70cbf873b2e011a5a00be54d38926f7861f1, pinned trunk 2fb698d. FROZEN, not edited.
- Part 1: docs/si/P-N5-RL-fixes-box10.md (l-si 1f107bf, sha1 ac027458), REFEREE's RL-1 to RL-4. It is not edited either. Where a line
  here and a line in part 1 differ, the line here governs.
- Source: REFEREE-2 successor 8, docs/referee-2/R2-N5-RL.md (trunk, referee-2 30dc5f5), §8 "Notes for the lane".
- A record of repairs, not itself refereed text.

## G-RL-1 (TEV-RED (1), (3), proof gap) = REFEREE's RL-1
- REFEREE-2's fix options: add "c's honest cycle at t lies in F_{k0}" to TEV-RED and the Consequence, or prove it. REFEREE-2 also notes
  that taking the last Ev vertex before the first visit of c is not enough by itself, because f's play then still runs around a
  cycle through Ev.
- Governing line: part 1's RL-1.
  - At t = k in the ENT setting, Lemma CYC-EV (no (P)) proves that no Ev vertex lies on C_k, the cycle of c at k (= the cycle of x_k's
    play). So f's whole play lies in F_{k0} once e is the last Ev vertex on the pre-c path. This proves REFEREE-2's hypothesis at t = k,
    and the Consequence holds as stated (with G-RL-2).
  - For t ∈ (k0, k), TEV-RED carries the hypothesis (TEV-RED′; equivalent to REFEREE-2's "c's cycle at t lies in F_{k0}" given that
    C_t ⊆ F_t ⊆ F_{k0} ⊔ Ev).
- CYC-EV's proof is in part 1 and in packet P-N5-ENT §3 (docs/si/P-N5-ENT-box11.md, sha1 4fd22be7).
- REFEREE-2's reachability remark ("a flat switch of c at k0 into R̄_{k0} whose route is cut by a level −1 R → F switch") does not
  matter at t = k: CYC-EV excludes the cycle case there whatever produced it.

## G-RL-2 (TEV-RED (3), statement) = REFEREE's RL-3
- "before e" → "up to and including e", in (3) AND in the Consequence's last bullet. Part 1's RL-3 has both replacements.
- REFEREE-2 reproduced it with its own N5 on tevlast_cex_n40 (k0 = 3, L = 32, t = 7, e = 15 ∈ H, B_t ∖ A = {e}).

## N-RL-1 (MERGE (c), wording) and REFEREE's RL-2 (MERGE scope)
- Both apply. Governing line: part 1's RL-2 (the stronger one): "level −1 ≤ ℓ < ∞". At ℓ = ∞ there is no common cycle node c, and (c)
  has no referent.
- N-RL-1 adds to (c): read "the σ_k-plays of z and x0" as their paths up to the first visit of c. In a functional graph these share a
  common suffix from their first common vertex m on, so the prefixes before m are disjoint.

## N-RL-2 (EV, the bookkeeping when q lies after c)
- Add to EV's proof: "If q, the first Ev vertex on z's play, lies on c's cycle after c, then P(Ξ_k q) = ∅. q is free on [k0+1, k], so
  FLAT-ALL (iii) and NL (i) give (π_q ∩ H) ⊔ A = ∅. Then B = P(Ξ_k z) ∩ H = ρ′ ∩ H, with ρ′ the path before c, and the vertices of ρ
  between c and q are below c. So B = (ρ ∩ H) ⊔ (π_q ∩ H) ⊔ A again." (REFEREE-2 §6.1; REFEREE's §6 remark, the same.)
- In the ENT setting the case does not occur at all, by CYC-EV (part 1).

## N-RL-3 (EV setting facts, wording)
- Replace "the top of A Δ B is even and in B" in §6 "Facts used throughout" with "COARSE_L(θ_k) ▷_L COARSE_L(θ_{k0}), so A ≠ B, and the
  top of A Δ B is even and in B or odd and in A. After EV (A ⊆ B), it is even and in B."
- It is used only after EV (in EV+), so nothing else changes.

## FREE-FREEZE, hypothesis (REFEREE-2 §3, remark)
- "(h) at t" can be dropped: Lemma G (a) (off R̄_t, Ξ = W) holds without (h). Recorded; the statement as written stays true.

## The k0-quantifier row (REFEREE-2 §6.3)
- REFEREE-2: "the packet's EV, EV+ and TEV-RED quantify k0 < k as CONSECUTIVE fallbacks of S, with t ∈ (k0, k]. So every transition in
  (k0, t) is an S4a step of S, and NL (ii) applies. The quantification is right as written. A reading with an arbitrary earlier k0 would
  not be."
- This agrees with part 1's "k0-quantifier point": no signable item is affected, and only §7's (dead) CONJECTURE TEV quantified over
  an arbitrary earlier k0.

## Concordance of the two reports (one row per gap)

| row | REFEREE (R-N5-RL) | REFEREE-2 (R2-N5-RL) | joint status | governing fixes line |
| --- | --- | --- | --- | --- |
| 1 | RL-1 (TEV-RED (1), proof gap; NOT SIGNED as stated, TEV-RED′ signed) | G-RL-1 (same gap; SIGN WITH GAPS) | closed at t = k in the ENT setting by Lemma CYC-EV (no (P)); TEV-RED′ for t < k | part 1, RL-1 (this file, G-RL-1, adds nothing new) |
| 2 | RL-3 (TEV-RED (3) + Consequence, wording) | G-RL-2 (same, statement) | wording: "up to and including e" | part 1, RL-3 |
| 3 | RL-2 (MERGE scope, ℓ < ∞) | N-RL-1 (MERGE (c), "paths up to c") | both applied; RL-2 governs the scope | part 1, RL-2 + this file, N-RL-1 |
| 4 | RL-4 (EV citation: NO-RF-OLD Corollary) | — | citation | part 1, RL-4 |
| 5 | §6 remark (q after c; no gap) | N-RL-2 (same) | proof addition; the case is empty in the ENT setting by CYC-EV | this file, N-RL-2 |
| 6 | — | N-RL-3 (top of A Δ B only after EV) | wording | this file, N-RL-3 |
| 7 | — | FREE-FREEZE "(h) at t" not needed | remark | this file |
| 8 | k0 quantifier (via the Lead / L-RED) | §6.3: consecutive quantification is right | no item affected | part 1 + this file |
| — | TEV (§7) FALSE (L-RED 16) | TEV FALSE (tevlast reproduced) | dead end, both forms | part 1, §7; docs/si/DEAD.md |
