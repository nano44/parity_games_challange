# R2-N5-WRUN-L3: word-diff of the P-N5-WRUN line, revision L-3 (REFEREE-2 successor 23, Opus 5.5, D15)
Object: docs/new/P-N5-WRUN-box92-line-L3.txt @ l-new fb976deb, sha1 cbba7a1b67340aebda613dcf8a71dc0b445f5e5a (re-hashed: match), against L-2
(85c12579, 8ab101e5). Token diff L-2 → L-3 (difflib over whitespace tokens): the global binder «for every N5 run on every game, every W-run
F = [a, b] of it, every Even edge (X, g) and every vertex v:»; GAP-DEV «the target z of every Even edge blocked at a state q of F has …»;
ΞCH-PCH «every vertex z has ΞCH_F(z) ≤ …»; PREFIX-MON «Ξ_t(v) … fixed over states t of F … Ξ_t(v)»; BIP-RED «(Theorem BIP-RED, with [SUB])»
(was «an implication from [SUB]»); REL2-WRISE (A2) «the (σ_{s+1}[y → z], τ_s)-play from z avoiding y, σ_{s+1}[y → z] being σ_{s+1} changed
at y to z». Nothing else changed.

## The Lead's three checks (my cautions of R2-N5-WRUN-L3check.md)
1. GAP-DEV and z: OK. The global binder binds v, not z. GAP-DEV binds z locally («the target z of every Even edge blocked at a state q of F»),
   and ΞCH-PCH re-binds it with «every vertex z has». No shadowing. ΞCH-PCH now holds for every z, as §6.2 and E2 need. WRUN-L3's z part:
   CLOSED.
2. Summation indices: «Σ_{(X, g)} REG_F(X, g) + Σ_{(X, g)} FREE_F(X, g)» (TRIPLE-RED) rebinds the global (X, g), «Σ RET_F» has no index at
   all, and XI-RUN's «Σ_v SW_R(v)» rebinds the global v. These are bound summation indices, so no symbol is free and the meaning is
   unambiguous. NOT REQUIRED. Optional exact text: «Σ_{(X′, g′)} RET_F(X′, g′) ≤ m_E(n + 1) + Σ_{(X′, g′)} REG_F(X′, g′) + Σ_{(X′, g′)}
   FREE_F(X′, g′)» and «Σ_{v′} SW_R(v′)».
3. PREFIX-MON «over states t of F»: §7.2 states the monotonicity «while λ(Ξ_t(v)) is constant», over any states of the run. Restricting it
   to F is a special case of the signed lemma, so it is true, and it is all LEVEL-RED uses (blocks of F with λ(Ξ(v)) constant). The line
   states less than §7.2, which is allowed. NOT REQUIRED. Optional: «over consecutive states t of the run» would match §7.2 exactly.
- WRUN-L3's F part: every formerly free F (TRIPLE-RED, RET-ΞRISE / FREE-RED, ΞCH-PCH / RSTAR-PCH, LEVEL-RED, NO-DEV, BIP-RED) is now bound
  by the global binder, and v is bound for LEVEL-RED. XI-RUN's own «every W-run F has» re-quantifies F harmlessly. CLOSED.
- WRUN-L4: (A2) now names τ_s and defines σ_{s+1}[y → z]. CLOSED.

## A new REQUIRED item: WRUN-L5 («with [SUB]»)
- L-3 changes «(Theorem BIP-RED, an implication from [SUB])» to «(Theorem BIP-RED, with [SUB])», following REFEREE's optional note. The
  line still has [SUB] only as a definition («[SUB] := for every sub-interval F′ …»), and WRUN-EQ still says «and, under [SUB], ⇔ SB-POLY ∧
  R°-POLY ∧ FL-POLY». So the line does not say whether [SUB] is claimed. «with [SUB]» can be read as «assuming [SUB]» (the old implication)
  or as «using [SUB], which holds» (an unconditional BIP-RED, which needs [SUB] stated as a claim). E8 then contradicts the second reading.
  Both referees have signed [SUB], so the unconditional form is available, but it must be stated.
- Required: ONE of the following.
  - (a) Unconditional. Replace «(Theorem BIP-RED, with [SUB])» by «(Lemma SUB, signed by both referees: REFEREE-2 docs/referee-2/SUB-check.md,
    claude/referee-2 a11c2868, and REFEREE R-N5-WRUN §9.1, claude/referee 8c0b2e69) [SUB] holds, and (Theorem BIP-RED)», and replace
    «and, under [SUB], ⇔ SB-POLY ∧ R°-POLY ∧ FL-POLY» by «and ⇔ SB-POLY ∧ R°-POLY ∧ FL-POLY».
  - (b) Conditional, as signed in the packet. Restore «(Theorem BIP-RED, an implication from [SUB])».
  (a) needs the Lead's decision that [SUB] lands in this line. The packet's §0 table already anticipates it: «if signed, BIP-RED is
  unconditional».
- Symbol test of the rest of the changed text: q (by «at a state q of F»), z (as above), t (by «over states t of F»), s, y and z in (A2)
  (bound by the clause's own «y leaves z at s»), σ_{s+1}[y → z] (defined in place). OK.

## Verdict
L-3 (cbba7a1b): **REQUIRED CHANGE WRUN-L5** (one of (a) or (b) above) (Opus 5.5, D15). WRUN-L3 and WRUN-L4 are CLOSED. The summation indices
and PREFIX-MON's range are optional precision.
