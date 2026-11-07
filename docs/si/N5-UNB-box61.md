# N5-UNB (box 61): every unblock of a gated edge happens at the same transition as a rise of Ξ at its target, at a key at least the unblock key (Lemma UNBLOCK-KEY, PROVED). But inconsistent steps cannot be charged one-to-one to unblocks (12,433 inconsistent steps, 6,889 unblocks in the corpus), and one (edge, key) pair re-unblocks K times in one τ-stretch on fbg_K. The reachable charge is the landed R95 [SUB] + RSTAR-PCH, and it composes through the targets' Ξ-rises
L-SI successor 38 (Opus 5.5; D18). Lead 2026-10-31 23:15Z, BOX 61: «what makes an edge blocked (in IW, not in Is) and later unblocked? …
Prove a lemma that charges each inconsistent step to an unblock event at a distinct (edge, key) pair, ideally with a per-edge bound that
does not compose across levels. Or show by instance why it must compose.» Written 2026-10-31 from 23:1xZ (date -u; see commit).
- Labels: PROVED (lane) / DATA / READING / DEAD. Not a TARGET.md claim. G-N5-TIME stays OPEN. Not a packet.
- Sources opened: docs/new/N5-GATE-box118.md §§0-5 (claude/l-new 5ea2e738: τ-stretch, Is_k, IW_k, INC, Lemma CONSISTENT-RED);
  docs/RESULTS.md R95 (l. 7476: Lemma SUB [SUB], Lemma GAP-DEV, Theorem RSTAR-PCH, blocked edges and R*_F as in R88 / R89);
  docs/si/N5-ANC-box58.md §§1-2 (ULT, INT, SUCC-MONO); docs/si/N5-RET-box60.md §1 (KEY-RETURN).
- Notation (box 118): in a τ-stretch, Is_k = N5's improving edges (SPEC S2, by Ξ), IW_k = G_τ's improving edges of σ_k (by W against τ).
  An Even edge e = (y, z) is BLOCKED at k if e ∈ IW_k \ Is_k; it is UNBLOCKED at k + 1 if blocked at k and e ∈ Is_(k+1). The unblock key
  is key(Ξ_(k+1)(z), Ξ_(k+1)(σ_(k+1)(y))). A transition is inconsistent if Is_k ≠ IW_k or it is a fallback; INC counts them.
- Premises: [IMP], [R15a], SUCC-MONO (box 58 §2), INT. No W-run hypothesis, no S4a optimality.

## 1. Lemma UNBLOCK-KEY (PROVED, lane)
- Statement. If e = (y, z) satisfies e ∉ Is_k and z ≠ σ_k(y) (in particular if e is blocked at k), and e ∈ Is_(k+1), then Ξ(z) changes at
  k, and its key κ_k(z) ≥ key(Ξ_(k+1)(σ_(k+1)(y)), Ξ_(k+1)(z)), the unblock key.
- Proof. e ∉ Is_k with z ≠ σ_k(y) gives Ξ_k(z) ⊴ Ξ_k(σ_k(y)) (S2). e ∈ Is_(k+1) gives Ξ_(k+1)(z) ▷ Ξ_(k+1)(σ_(k+1)(y)). SUCC-MONO
  (one step) gives Ξ_k(σ_k(y)) ⊴ Ξ_(k+1)(σ_(k+1)(y)). So Ξ_k(z) ⊴ Ξ_(k+1)(σ_(k+1)(y)) ◁ Ξ_(k+1)(z). Hence Ξ(z) changes at k, and INT gives
  key(Ξ_(k+1)(σ_(k+1)(y)), Ξ_(k+1)(z)) ≤ key(Ξ_k(z), Ξ_(k+1)(z)) = κ_k(z). □
- So an unblock is never caused by the source side: y's target only rises in Ξ (SUCC-MONO), which can only re-block. It is always a Ξ-rise
  of the target, at the same transition, at least as significant as the level at which z now beats y's target.
- Corollary. In any interval, the unblocks of (y, z) at key ≥ κ number at most the changes of Ξ(z) at key ≥ κ in that interval. Summed over
  edges this is R95's RSTAR-PCH charge R*_F ≤ Σ_(y, z) ΞCH_F(z), now with the key level and the simultaneity made explicit.
- DATA (experiments/si/anc58/unblock.py; corpus output anc58/unblock_corpus.txt, 1,132 games): 17,841 τ-stretch steps and INC 12,433
  (identical to box 118's corpus counts, a cross-check of the two tools); 6,889 unblocks, all with Ξ(z) changing at k (XIUP 6,889,
  SRCDN 0), and 0 with a key below the unblock key (UNBKCH 0).

## 2. The one-to-one charge fails (DATA)
- Inconsistent steps outnumber unblocks: corpus INC 12,433 against 6,889 unblocks. 9,404 inconsistent steps have NO unblock at the next
  state (NOUNB).
  | instance (box 116 / R167 starts) | stretch steps | INC | unblocks | distinct (edge, key) | longest gap without an unblock |
  | --- | --- | --- | --- | --- | --- |
  | sr_K2_m6_m4 (R167) | 22 | 20 | 5 | 5 | 8 |
  | fbA_K4_m8_m8 | 44 | 43 | 9 | 9 | 8 |
  | fbA_K8_m8_m8 | 88 | 87 | 17 | 17 | 8 |
  | fbg_K4_m6_m24 | 139 | 131 | 109 | 43 | 26 |
  | fbg_K8_m6_m24 | 271 | 263 | 217 | 63 | — |
  | fbg_K12_m6_m24 | 403 | 395 | 325 | 83 | — |
  - On fbA_K the unblocks are 2K + 1 and the gaps between them stay ≤ 8: the stretch is (unblocks) × (a constant).
  - Corpus maximum gap: 68 (red/usplit gate_K64_n581).
- So any charge of inconsistent steps to unblocks is many-to-one. The landed many-to-one charge is R95's Lemma SUB (signed by both
  referees): in every sub-interval F′ of a W-run, at most (n − 1)(R*_T(F′) + 1) transitions change W, where R*_T(F′) counts adoptions of
  edges blocked earlier in F′. With FL_F (W-flat transitions) this gives |F| ≤ (n − 1)(R*_F + 1) + FL_F (R95 FREE-RED). Inside a
  τ-stretch the W-runs are separated by λ_W changes and fallbacks.

## 3. The per-(edge, key) bound fails, linearly in K (DEAD for the explicit form; DATA for the growth)
- DEAD: «inside one τ-stretch, each (edge, key) pair is unblocked at most once». Instance experiments/new/box116/inst/fbg_K4_m6_m24.pg
  (sha1 456d12b0…) with the repaired start fbg_K4_m6_m24_fixed.start (sha1 463fb03b…): edge (124, 126) unblocks 4 times at key (1, 145)
  in the stretch 1 … 139. Faithfulness (this box): startcheck OK; n5b (red/seg/xeng.py) state sequence identical (140 iterations, 0
  fallbacks); n5.py's solution = Oink zlk, both strategies verified.
- DATA (growth): MAXREP, the most unblocks of one (edge, key) in one stretch, is 4 / 8 / 12 on fbg_K4 / K8 / K12_m6_m24 (edges (124, 126),
  (192, 194), (266, 268); keys (1, 145), (1, 169), (1, 193)). fbg_K4_m6_m48 also has 4. Corpus maximum 5 (red/so rise_thin51_n40).
  - So the number of (edge, key) charges is polynomial (≤ m_E(n + 3)), but a single pair is re-used K times. The ideal charge «each
    inconsistent step to a DISTINCT (edge, key)» cannot hold even after dividing by a constant.
- Why it composes (READING, from UNBLOCK-KEY). Each of the K unblocks of (266, 268) needs its own rise of Ξ(268) at key ≥ (1, 193) at that
  same transition. Between two of them the edge is re-blocked, so y's target rose past Ξ(268) again. The per-edge count is therefore
  the target's count of rises above the unblock level, which is set by the levels below (XI-CH-POLY). That is the composition. One rise
  of Ξ(z) also unblocks every blocked edge into z at once (fan-out d_E(z), as box 60 §3).
- NOT shown: a family where the per-pair repeats grow faster than linearly in n. On fbg the repeats are K and n = 178 + 14K (178, 234,
  290), so the data is consistent with a polynomial bound. «Must compose» is shown for the charge's FORM (a per-edge bound has to count
  the target's Ξ-rises). A super-polynomial instance is not given.

## 4. Answer to the Lead, and overlap with L-NEW box 119
- What makes an edge blocked: (y, z) ∈ IW \ Is means W(z) ▷ W(σ(y)) but Ξ(z) ⊴ Ξ(σ(y)). By R18 (d) Lemma S (b) (quoted in box 118 §4),
  z then has Ξ(z) ◁ W(z), so z is in the gap set. What unblocks it: ONLY a rise of Ξ(z) at that transition, at key ≥ the unblock key
  (UNBLOCK-KEY). The source side never unblocks.
- Charging: one-to-one is false (§2). Per distinct (edge, key) is false (§3). The true charge is many-to-one with factor n − 1 (R95
  [SUB]) onto adoptions of previously blocked edges, and per edge onto the target's Ξ-rises (RSTAR-PCH, sharpened by UNBLOCK-KEY). It
  composes across levels through XI-CH.
- Overlap: L-NEW box 119 (not yet pushed at claude/l-new 5ea2e738) attacks INC from the blocked-edge side. This box covers the UNBLOCK side
  (cause, key, counts, the fbg repeat instance). I suggest that L-NEW take the BLOCKING side: what re-blocks (y, z) between two unblocks
  (a rise of y's target past Ξ(z), i.e. a switch of y or a rise of Ξ(σ(y))), and whether re-blocks are bounded.

## DONE / FINDINGS / NEEDS
- DONE: this note; anc58/unblock.py (+ rununblock.sh, unblock_corpus.txt); check.sh «box 61».
- FINDINGS:
  - PROVED (lane): UNBLOCK-KEY (an unblock = a simultaneous Ξ-rise of the target at key ≥ the unblock key). It sharpens R95 RSTAR-PCH.
  - DATA: INC 12,433 vs unblocks 6,889 (one-to-one fails); fbA stretch ≈ unblocks × ≤ 8.
  - DEAD (explicit): «each (edge, key) unblocks at most once per τ-stretch» (fbg_K4_m6_m24: 4; n5b identical, Oink OK). DATA: repeats = K on fbg_K.
  - READING: the charge composes through the targets' Ξ-rises (XI-CH-POLY). No super-polynomial instance.
- NEEDS: none from the owner.
