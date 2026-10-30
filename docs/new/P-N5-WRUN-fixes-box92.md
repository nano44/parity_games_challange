# P-N5-WRUN fixes (box 92; APPEND-ONLY). Frozen packet docs/new/P-N5-WRUN-box92.md (sha1 fae68aa0…) and line docs/new/P-N5-WRUN-box92-line.txt (sha1 0faa5b80…) at l-new 7668bc9b are NOT edited; errata and cross-reads are given here.
L-NEW successor 39 (Opus 5.5), D14 / D18. Newest entry last.

## Entry 1 (2026-10-30 16:34Z by date -u): CONJECTURE BIP-REL-1 DEAD (L-RED successor 34, R143 §5, l-red 717f407a, docs/red/R143-settle.md). Lead 16:34Z: «Open docs/new/P-N5-WRUN-fixes-box92.md (append-only) with an erratum: BIP-REL-1 DEAD (instance, SHA).»
### L-RED's text (verbatim, R143-settle.md l. 121-130)
> - DATA (strictrel.py = L-RED R142b; relpe.py STRICT=1 = L-NEW box 89's own counter on its n5x engine; xeng; Oink zlk + verify):
> 
>   | pin | n | iterations | strict releases of (y, z) in one frozen stretch | relpe frozen_edge | xeng | Oink |
>   | --- | --- | --- | --- | --- | --- | --- |
>   | rel2/instances/rel2_R2_n82 | 82 | 10 | 2 | 2 | identical | OK |
>   | rel2/instances/rel2_R4_n322 | 322 | 22 | 4 | 4 | identical | OK |
>   | (generator only) R = 3, 6 | 183, 714 | 16, 34 | 3, 6 | — | — | — |
> 
> - DEAD: CONJECTURE BIP-REL-1 (≤ 1 strict release per edge per frozen stretch). Instance rel2_R2_n82, edge (y, oz).
>   - The family gives R strict releases of ONE edge in ONE stretch at n ≈ 20R², so R° ≥ ⌊√(n/20)⌋.
### Reproduction (L-NEW, own counter)
- experiments/red/rel2/instances/rel2_R2_n82.pg sha1 064a8309e6fe1052a09c929f5f02d5118de7731d, .start sha1 2988324fb0f300b4407bc076e1473d5ce16deb7e
  (read from l-red 717f407a; sha1s equal L-RED's pins.sha1). `STRICT=1 python3 -I new/box89/relpe.py rel2_R2_n82.pg rel2_R2_n82.start`
  (from experiments/): «RELPE n 82 mE 55 runs 1 maxima {'late_edge': 2, 'rstar': 2, 'F': 10, 'frozen_edge': 2} argmax-edge (81, 80)».
  One W-run, two strict releases of edge (81, 80) in one frozen stretch: BIP-REL-1 is DEAD. Obstruction (L-RED): box 90's one-line
  obstruction realised with one-player delay chains as a clock (τ-branch climb, then ρ-branch climb, twice).
### Errata to the frozen packet
- §12: CONJECTURE BIP-REL-1 is DEAD (instance above; family R strict releases at n ≈ 20R², so R° ≥ ⌊√(n/20)⌋ there).
- §3.3 row E10 («BIP-REL-1 ∧ SB-POLY ∧ FL-POLY ⇒ WRUN-POLY (under [SUB])»): still a true implication, now VACUOUS (its premise is false).
- §9 last bullet («With CONJECTURE BIP-REL-1 (§12) R° ≤ m_E»): void. BIP-RED itself is unaffected; it needs R°-POLY (R° ≤ p(n)), not
  R° ≤ m_E. Row E8 (WRUN-POLY ⇔ SB-POLY ∧ R°-POLY ∧ FL-POLY under [SUB]) is unaffected. R143's family has R° ≈ √(n/20): polynomial.
- §13 DATA «BIP-REL-1 0 violations (box89/relpe.py STRICT=1)» holds for the 1132-run corpus only; DEAD row to add: BIP-REL-1, rel2_R2_n82.
- The line (0faa5b80) does not state BIP-REL-1 as a hypothesis or conclusion except in «BIP-REL-1 … are open» (the status parenthesis):
  read «BIP-REL-1 is DEAD (L-RED R143)». A revised line will be issued if the Lead asks.
- CONJECTURE BIP-POLY is NOT killed (R143's runs are short: 10 / 22 iterations).

## Cross-reads (lane level; NOT packet changes) — Lead 16:34Z: «Note these in the fixes file as cross-reads, not packet changes.»
### L-SI successor 33, l-si 78788761, docs/si/N5-GATE-box51b.md §11 (verbatim, l. 308-318)
> - Lemma RETURN-CHARGE′ (PROVED, lane). In ANY stretch of an N5 run (S4a steps, τ-changes and S4c fallbacks alike), let Even v leave d at k1
>   and re-adopt d at k2 > k1. Then Ξ_{k2}(d) ▷ Ξ_{k1}(d).
>   - The hypotheses of §10.3 (λ_Ξ fixed, v not its own Ξ-cycle node) are dropped.
>   - Proof. Every Even switch at j goes to an edge of Iσ_j: S4a's arena is σ_j ∪ Iσ_j, and S4c picks from Iσ_j (n5x.py step()). So the
>     sequence j ↦ Ξ_j(σ_j(v)) is non-decreasing.
>     - Without a switch at j, it is one vertex, and Ξ is pointwise non-decreasing (R15 (a), (d)).
>     - With a switch a → b at j: Ξ_{j+1}(b) ⊵ Ξ_j(b) ▷ Ξ_j(a).
>   - Hence Ξ_{k2}(d) ▷ Ξ_{k2}(σ_{k2}(v)) ⊵ Ξ_{k1+1}(σ_{k1+1}(v)) ▷ Ξ_{k1}(d). □ (This replaces §10.3's reflection through v ⊕ ·.)
> - Corollary SEG-XCH (PROVED, lane). For every segment [p, q] of a run, let SWT := the transitions of [p, q] that switch some Even vertex.
>   Then SWT ≤ m_E + Σ_d d_E(d)·XCH_{[p,q]}(d).
>   - A switch either adopts an edge v has not held in [p, q] (≤ deg(v) − 1 per v), or is a return.
- L-NEW reading: RETURN-CHARGE′ is the no-hypothesis form of RET-ΞRISE (packet §5.1) and of landed R86 SW-RETURN's chain; Corollary
  SEG-XCH (i) is packet §3.2 XI-RUN, derived independently (L-SI via a direct return count, L-NEW via R86 SW-RETURN). RX = 0 in both. Two
  independent derivations of the same bound; the packet's form needs only landed lemmas.
### L-RED successor 34, R143 §1, l-red 717f407a (verbatim, R143-settle.md l. 39-47)
> - (C) Count. Every transition of I switches some Even vertex. Inside a window only vertices outside C switch (a CN switch is an event).
>   So a window has at most D := max{layer(v) : v switches in I} transitions, and |I| ≤ E_I + (E_I + 1)·D = (D + 1)(E_I + 1) − 1. □
> - Corollary INT-LIN-EF (PROVED, lane). An event-free W-constant interval has |I| ≤ D ≤ n − 1. That covers in particular every interval
>   with σ̄ frozen, no CN switch and every upward head's Ξ constant.
> - Corollary SETTLE-RED (PROVED, lane). E_I ≤ SBF_I + CN_I + Σ_(u ∈ U*) XCH_I(u), where U* := ∪_k U_k (|U_k| ≤ #Odd + |C|), SBF_I is the
>   number of σ̄-changing transitions and CN_I the number of CN switches. Hence [P-INT] ⇐ «in-interval Ξ-changes at upward heads, σ̄-flips
>   and CN switches are polynomial».
>   - This sharpens L-SI's INT-XCH (Σ over EVERY vertex d, weighted by its in-degree) to the heads alone.
>   - It replaces CONJECTURE LAYER-RESET's mixed-radix bound Π_d(1 + m_d) by a product (D + 1)(E_I + 1).
- L-NEW reading: Lemma SETTLE (lane, modulo L-SI's Claim RG and L-LIT's LEX-BFS / IDX-MONO) sharpens packet §11 INT-XCH⁰ (all vertices,
  in-degree weights) to E_I (σ̄ flips, CN switches, Ξ-changes at upward heads). It bears on row E11 ([P-INT] ⇐ …) only; not in the packet.
