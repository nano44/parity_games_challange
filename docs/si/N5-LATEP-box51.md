# N5-LATEP (box 51): TIED-RB is DEAD; LATE′ (forget a block at each adoption) keeps FW-R* verbatim and removes stale and W-silent repeats; every LATE′ adoption pays a distinct (edge, gap Ξ-climb of its target) token
L-SI successor 32 (Opus 5.5), D15 / D18, Lead reading L40. Lead 2026-10-30 05:28Z: «GO, BOX 51: 1. Prove or kill TIED-RB … 2. The stale
REPEATs. Prefer the redefinition: forget a block at each adoption. Check whether GP*-RUN / FW-R* (R88/R89) survive it … If TIED-RB holds,
your TXC_F(z) and its GXC should be the same object, or one bounded by the other; state the relation exactly.» Working note, unrefereed,
not a TARGET.md claim. G-N5-TIME OPEN. Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
- Tools (experiments/si/odd/):
  - tied.py (box 50 §6; now importable: run());
  - tiedmut.py (mutation search: add / drop an edge, shift a priority, change a start choice);
  - tiedfuzz.py (random games; found nothing: runs too short);
  - latep.py (LATE′ counters and the GAP-CLIMB check).
  - Outputs: odd/out/latep_corpus.txt, tiedmut_*.txt. Pins: si/check.sh «box 51».
- Symbols as in box 50 (docs/si/N5-ADD-box50.md) and R88 / R89. Z_t := {v : Ξ_t(v) ≠ W_t(v)} (P-N5-GAP §1). XW: Ξ_t ⊴ W_t pointwise
  (RESULTS R88 Lemma XW, any t). W-MON on a W-run (R89 GP*-RUN).

## 1. DEAD: CONJECTURE TIED-RB (box 50 §6)
- Statement killed: «every re-blocked REPEAT of (y, z) has a tied Ξ-climb of z on [k, u − 1]», tied meaning Ξ_{s+1}(z) ▷ Ξ_s(z) and
  W_{s+1}(z) = W_s(z).
- Instance: odd/inst/si51/tiedmut_so_th_n32_11.pg / .start (sha1 4ce2df57… / c3430f63…; found by tiedmut.py seed 11 as out/tiedmut_so_th_n32_11).
  - It is so_th_n32 (L-RED, red/so/instances) with one added edge 24 → 29, from start σ(11) = 25, all other choices best-reward.
  - The .start file lists every vertex.
  - n = 32; 34 iterations, 0 fallbacks.
  - Second engine: red/seg/xeng.py (L-NEW's n5.py on si.py vs L-COMP's n5b SPEC): «state sequences identical: True».
  - Oink: NOT RUN (Oink not built in this container). The claim is about the dynamics, not the solution.
- The repeat, in global state indices (the W-run starts at state 1; τ is constant from state 1):
  - y = 0 (Even, successors 10 and 15) and z = 10 (Even, successors 22 and 24);
  - y leaves z at transition 11 → 12;
  - (y, z) is BLOCKED at state 13 (W(z) ▷ W(σ y), not improving);
  - (y, z) is improving at state 14, and y re-adopts z at transition 14 → 15.
  - Ξ(z) changes only at transitions 12 → 13 (z itself switches 22 → 24) and 13 → 14. W(z) changes at both of them too.
  - So no Ξ-climb of z on [11, 14] has W(z) fixed. At state 13, z ∈ Z: W_13(z) ≠ Ξ_13(z). At state 14, Ξ_14(z) = W_14(z).
- Mutation statistics (tiedmut.py; each run stops at its first counterexample). SKIPPED: a switchbestexp_5 run (1,500 trials) and two
  further wdepth seeds (21, 22) were stopped unfinished at ~05:35Z to land the box; no output kept.

| base | mutations / trial | trials | REPEATs | re-blocked | untied | untied AND re-blocked |
| --- | --- | --- | --- | --- | --- | --- |
| so_th_n32 (seed 11) | 3 | 1,755 | 827 | 302 | 170 | 1 |
| so_th_n32 (seed 12) | 8 | 739 | 54 | 16 | 13 | 1 |
| wdepth_K4_m16 (seed 14) | 4 | 173 | 1,207 | 1,192 | 12 | 2 |

- READING: an untied re-blocked repeat is rare (4 in 1,510), but it exists. The climb that pays is an own switch of the target (or a
  change on the shared prefix of z's τ-play and σ̄-play), which raises W(z) and Ξ(z) together. TXC alone does not pay all repeats.

## 2. LATE′: forget a block at each adoption (PROVED, lane): FW-R* and GP*-RUN survive verbatim
- Definition (LATE′). In a W-run F = [a, b] (R89), an adoption of the Even edge (y, z) at the transition u → u + 1 (σ_{u+1}(y) = z ≠ σ_u(y))
  is LATE′ if (y, z) is BLOCKED (R88 §3: W_t(z) ▷ W_t(σ_t y) and (y, z) ∉ Iσ_t) at some state t with p + 1 ≤ t < u, where p is the previous
  adoption transition of (y, z) in F (t ≥ a if there is none). R*′_T(F) := the transitions of F containing a LATE′ adoption.
- Diff against R88 §4 (P-N5-GP §4, l. 144-145): R88 reads «… to an edge (y, z) that was blocked at some state t ∈ [a, τ)». LATE′ replaces
  «t ∈ [a, τ)» by «t ∈ [max(a, p + 1), τ), p the previous adoption transition of (y, z) in F». Nothing else changes. Every LATE′ adoption
  is R88-late, so R*′_T ≤ R*_T.
- Corollary FW-R*′. Every W-run F has WCH ≤ (n − 1)(R*′_T(F) + 1).
- Proof. FW-R*'s proof, verbatim, up to «y_i adopts (y_i, y_{i+1}) at some transition τ → τ + 1 with t < τ ≤ k». Take τ to be the FIRST
  adoption of (y_i, y_{i+1}) after t. The proof shows ρ_{t+1}(y_i) ≠ y_{i+1}, so the previous adoption p of that edge has p ≠ t. It has
  p ∉ (t, τ) by the choice of τ, so p < t, i.e. p + 1 ≤ t. The edge is therefore blocked at a state t ∈ [p + 1, τ): the adoption at τ is
  LATE′. The charging (k − τ ≤ n − 2) is unchanged. □ The same holds on W-runs (R89 GP*-RUN: the proof does not use σ̄ or λ_Ξ constancy).
  Lemma GP* is untouched: it never used the late-adoption definition.
- Consequences (PROVED, lane):
  - (a) A LATE′ REPEAT (LATE′ adoption of an edge adopted before in F) is exactly a box-50 RE-BLOCKED REPEAT: t ≥ p + 1 forces t after y's
    last leave k of z, because σ_t(y) ≠ z = σ_{p+1}(y).
  - (b) LATE-SPLIT′. Every LATE′ REPEAT of (y, z) at u, with y not its own W-cycle node on [k + 1, t_b], has a strict W(z)-rise on
    [k + 1, t_b] ⊆ [k + 1, u − 1], where t_b is a blocked state ≥ k + 1. This is box 42 §1 (ii) in its original form: (OPT) at k + 1,
    W-SUCC to t_b, blocked at t_b. So W-silent and SELF repeats do not exist under LATE′, and X′_F = own-cycle repeats only.
  - (c) STALE REPEATs (box 50 §6) are not LATE′ adoptions. They leave R*′_T and need no count.
  - (d) Theorem CIRCLE (box 50 §2) holds with primes: REP′ ≤ n_E R*′_T, R*′_T ≤ m_E + REP′, REP′ ≤ X′ + Σ_z d_E(z) WCH_F(z),
    WT_F ≤ (n − 1)(R*′_T + 1).
  - (e) Downstream: every R88-late adoption used in a proof that only needs FW-R*'s charge can be read as LATE′. In particular, box 40's
    LATE re-entries are LATE′: the edge is blocked at j − 2, and the previous adoption p has p + 1 ≤ j − 2 because σ_{j−1}(v) ≠ c. So
    P-N5-CUT's LATE term and R90's REP* may be read with LATE′. This is a READING for the referees to check against the frozen packet;
    it is not a change to R90's signed text.

## 3. Lemma GAP-CLIMB (PROVED, lane): every LATE′ adoption pays a distinct (edge, gap Ξ-climb of its target) token
- Definition. ZXC_F(z) := the transitions s → s + 1 of F with z ∈ Z_s and Ξ_{s+1}(z) ▷ Ξ_s(z) (a Ξ-climb of z while z is a gap vertex).
- Lemma GAP-CLIMB. Let the LATE′ adoption of (y, z) at u have last blocked state t_b (p + 1 ≤ t_b < u). Let s be the first transition of
  [t_b, u − 1] at which Ξ(z) changes. Then s exists, z ∈ Z_s, and Ξ_{s+1}(z) ▷ Ξ_s(z). For one edge, distinct LATE′ adoptions give
  distinct s. Hence LATE′_F(y, z) ≤ ZXC_F(z), and the LATE′ adoptions of F number at most Σ_z d_E(z)·ZXC_F(z).
- Proof.
  - (y, z) ∉ Iσ_{t_b} (blocked) and (y, z) ∈ Iσ_u ([S4a]: σ_{u+1}(y) = z ∈ A_u(y), z ≠ σ_u(y)). R89 Lemma LATE-RISE gives
    Ξ_u(z) ▷ Ξ_{t_b}(z), so s exists. Ξ is non-decreasing along S4a steps (R15), so the first change is a strict rise.
  - Ξ_s(z) = Ξ_{t_b}(z) ⊴ Ξ_{t_b}(σ_{t_b} y) (not improving, [S2]) ⊴ W_{t_b}(σ_{t_b} y) (XW) ◁ W_{t_b}(z) (blocked) ⊴ W_s(z) (W-MON). So
    Ξ_s(z) ≠ W_s(z): z ∈ Z_s.
  - Distinctness: for consecutive LATE′ adoptions u′ < u of the same edge, t_b(u) ≥ u′ + 1, so the intervals [t_b, u − 1] are disjoint. □
- This is R89's R*-RISE (late adoptions of an edge ≤ Ξ-changes of its target) sharpened in two ways. The climb is at a GAP state of z.
  The intervals are taken after the last block, so they are disjoint per edge without R89's argument.

## 4. TXC, GXC and ZXC: the exact relation (PROVED, lane, from the definitions)
- Definitions:
  - TXC_F(z) := the tied Ξ-climbs of z in F (box 50 §6);
  - GXC (L-NEW box 70 §3): the pairs (v, t) with v Even, σ_{t+1}(v) ≠ σ_t(v), τ_{t+1} = τ_t, λ_Ξ unchanged at t, v ∈ Z_t,
    Ξ_{t+1}(v) ▷ Ξ_t(v), and W_{t+1}(v) ⊴ W_t(v).
- Inside a W-run F, as sets of (vertex, transition) pairs: GXC_F ⊆ TXC_F ⊆ ZXC_F.
  - GXC ⊆ TXC: on F, W-MON gives W_{t+1}(v) ⊵ W_t(v), so with ⊴ it is equality.
  - TXC ⊆ ZXC: z ∈ Z_s is automatic, since Ξ_s(z) ◁ Ξ_{s+1}(z) ⊴ W_{s+1}(z) = W_s(z) by XW.
- Both inclusions are strict in general:
  - GXC also needs v Even, v switching, and λ_Ξ fixed;
  - ZXC also allows climbs where W(z) rises (§1's instance: transitions 12 → 13 and 13 → 14 are in ZXC_F(10), not in TXC_F(10)).
- So ZXC_F(z) = TXC_F(z) + WZ_F(z), where WZ_F(z) := the ZXC transitions at which W(z) also changes, and WZ_F(z) ≤ WCH_F(z).
- Composition (PROVED, lane): LATE′ adoptions of F ≤ Σ_z d_E(z)·(TXC_F(z) + WZ_F(z)). The WZ part is the circle again (W-changes), but
  only at gap states that coincide with a Ξ-climb. The TXC part is GXC-type.
- What would close it (OPEN):
  - (i) TXC_F(z) ≤ poly·(GXC + 1) (a tied climb at a non-switching z must descend along z's Ξ-play to a switching vertex; at an Odd vertex
    the descent can leave the τ-play, so W need not stay fixed below: not proved);
  - (ii) WZ polynomial per W-run.

## 5. DATA (latep.py; corpus 719 games + latew)
| set | max WCH | max R*_T | max R*′_T | max REP′ | LATE′ adoptions (sum) | GAP-CLIMB tied (W(z) fixed) | X′ (W-silent / SELF) | FW-R*′ violations | GAP-CLIMB violations / repeated tokens |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| corpus (719; per-W-run maxima, sums over games) | 159 | 17 | 17 | 9 | 1,104 | 1,003 | 0 | 0 | 0 / 0 |
| latew_K20_m32 (n 538) | 700 | 640 | 640 | 570 | 641 | 639 | 0 | 0 | 0 / 0 |
| wdepth_K4_m16 (n 146) | 76 | 36 | 36 | 21 | 37 | 35 | 0 | 0 | 0 / 0 |
| TIED-RB instance (n 32) | 19 | 4 | 4 | 1 | 6 | 4 | 0 | 0 | 0 / 0 |
- Every LATE′ adoption is R88-late (RSUB_V 0). The corpus has 1,104 LATE′ adoptions against 1,141 R88-late ones (box 42); the 37
  dropped are the stale repeats.
- Of the GAP-CLIMB tokens, 91 % in the corpus (1,003 / 1,104) and all but 2 on latew / wdepth are tied (TXC). The rest are WZ.
- FW-R*′ holds on every W-run (FWV 0), as §2 proves.

## DONE / FINDINGS / NEEDS
- DONE: odd/latep.py, tiedmut.py, tiedfuzz.py, tied.py (importable); corpus, latew; counterexample pinned with two engines; si/check.sh
  «box 51»; this note.
- FINDINGS:
  1. DEAD: CONJECTURE TIED-RB (tiedmut_so_th_n32_11, n 32: re-blocked REPEAT of (0, 10) whose only Ξ(z)-climbs also raise W(z); two
     engines agree). Rare: 4 untied re-blocked in 1,510 re-blocked REPEATs over the mutation runs.
  2. PROVED (lane): LATE′ (forget a block at each adoption). FW-R*′ holds with FW-R*'s proof verbatim; GP* is untouched. Stale and
     W-silent / SELF repeats vanish (X′ = own-cycle only); CIRCLE holds with primes.
  3. PROVED (lane): Lemma GAP-CLIMB. LATE′ adoptions ≤ Σ_z d_E(z)·ZXC_F(z), one distinct (edge, gap Ξ-climb of target) token each.
  4. PROVED (lane): GXC_F ⊆ TXC_F ⊆ ZXC_F inside a W-run, both inclusions strict; ZXC = TXC + WZ with WZ ≤ WCH.
  5. READING: R90's REP* and P-N5-CUT's LATE term can be read with LATE′ (for the referees to check).
- NEEDS: none from the owner.
