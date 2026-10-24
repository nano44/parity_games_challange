# R2-N5-X: second-referee check of packet P-N5-X (L-NEW box 28: N5 inside a joint λ-phase is controlled by crossings and OTHER states). REFEREE-2 (successor 4), 2026-10-24 18:34Z (date -u)
Signature: (Opus 5.5, D15). Packet P-N5-X (Lead 18:1xZ), pinned at trunk claude/vibrant-johnson-nxvvxo afc88b0 (an ancestor of my merged tree).
Object: docs/new/P-N5-X-box28.md, sha1 b21d2d0638d08d750f26ae4dda2faaca7891fa23 (checked at the pin; L-NEW successor 10, l-new 23e8f93).
Background read: docs/new/N5-NH-box28.md §5c; docs/new/P-N5-XA-fixes-box28.md §5-§6; RESULTS R15, R17, R18 (c)-(d), R19, R20; the SPEC.
Independence: I have not read docs/referee/R-N5-X.md. I did not run the lane's box 28 scripts. The lane's and L-RED's instances were used
as inputs only.
Tools (docs/referee-2/R2-N5-X/, own code on my R2-N5-RE/re_check.py definitions and own N5 with random tie-breaks; "spec" mode = n5.py's
state sequence): x_check.py, dump_tf.py, run_all.sh, logs/ (41 logs), ext/fbref_cex_n32.pg (copied from claude/l-red, sha1 901674dc…).
Instances cited are re-run with experiments/new/n5.py and experiments/new/check_sol2.py (Oink zlk @ 8fbf0a7, built here by
scripts/setup_oink.sh): fbref_n48 60 iterations, 9 fallbacks; fbref_cex_n32 56 iterations, 8 fallbacks. Both: "zielonka(oink zlk) OK
strategies verified".

## Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| (1) Lemma F1 (§5) | SIGN | N-X-1: step 2 needs only Lemma G (a), which holds at every state (EQ, THR and OTHER alike) |
| (2) Lemma NF (§4) | SIGN | — |
| (3) Theorem X (§7) | SIGN WITH GAPS | G-X-1: step 4 cites PIECE "θ free" (R19 (f), my N-RE-4). With θ varying, Ξ changes on R at a θ-change without a route change, and R19 (f)'s per-part count "≤ \|R\| − 1 on R" is then FALSE if Ξ on R is counted (instance below). The total ≤ \|R\| − 1 + \|F\| − 1 survives by Lemma TF (proved here, §3.2): under (h) at both ends, a θ-change is an F-value change. CLOSED by TF. N-X-2, N-X-3: two citations used slightly outside their signed form, both covered (§3.3) |
| (4) Lemma XW (§1) | SIGN | — |
| (4) Lemma EQ (§2) | SIGN | — |
| (4) Lemma FBL-N (§3) | SIGN | — |
| (4) Lemma F2 (§6) | SIGN | — |
| (4) Lemma FB-W (§9) | SIGN (given the CR row of §8) | DATA vacuous: the hypothesis (a w-status direct eviction at L ≥ k_0 + n − 1) never occurred in my runs |
| (5) (w, u*)-run table (§8) | agree (READING) | every row checked against the proofs of R20; data on 198 θ-varying runs for the Lemma C and CR rows |
Context, as the Lead says: (X), (NH') and G-N5-TIME stay OPEN. Theorem X does NOT use (FBRE-F) (§3.4). FBRE-F's failure is confirmed in
my data (50 θ-status re-entries after post-freeze evictions).
Correction to a signed result (my own): R19 (f)'s clause "θ constant not needed (N-RE-4)" is right for the total count only if Lemma TF is
added. Its per-part reading fails when Ξ on R is counted. §3.2 has the instance and the repair. The Lead should amend R19 (f).

## 1. Lemma F1: SIGN (N-X-1)
- Step 1 ✓. F is closed under σ_k and τ, contains no Odd choice, and Ξ = W on F (Lemma G (a), no (h)).
- Step 2 ✓. For x, z ∈ F, (x, z) ∈ Iσ_k iff Ξ_k(z) ▷ Ξ_k(σ_k x) iff W_k(z) ▷ W_k(σ_k x) (σ_k x ∈ F), i.e. 𝓕-improving. N-X-1: this
  is Lemma G (a) alone and holds at EVERY state, (h) or not. The EQ/THR split in the text is unnecessary. EQ states without (h) are
  covered.
- Step 3 ✓. No crossing, so x ∈ F keeps σ_{k+1}(x) ∈ F. Every 𝓕-arena strategy, extended by σ_{k+1} on R, is an S4a-arena strategy.
  (F1) in G_τ makes σ_{k+1}|F a pointwise 𝓕-arena optimum.
  - The transitions are S4a or S4c only: τ is constant in a phase, so S4b and the Odd fallback do not occur.
- Step 4 ✓ by Lemma NF. F-intervals exclude crossings and OTHER-touching transitions, so every fallback inside is value-preserving.
  Lemma P's invariant is about current values and survives (the R20 (f) argument: its induction step never uses how σ_k arose).
- Steps 5-6 ✓. λ on F is λ_Ξ, constant in the phase. R17 Lemma P and Theorem PH hold from any start (R17 (e)), with forced Odd vertices
  (XA-4). This gives ≤ |F| − 1 transitions that change Ξ on F.
- Neither θ nor w enters. The note against R19 (f) is right.

## 2. Lemma NF: SIGN
- k EQ: Lemma EQ's fallback argument makes the transition value-preserving. So a value-changing fallback has k THR.
- With R_{k+1} = R_k, the switched edges are classified correctly:
  - F → F flat (FBL-N (ii));
  - R → R impossible (Lemma G (c) at the arena optimum, R18 (c); λ_W(x) ≠ x on R by H2);
  - R → F and F → R impossible, since R is unchanged.
- The Claim (Ω_{σ,e} unchanged for every exit e) ✓:
  - F-plays avoid o, and flat switches with disjoint regions keep G_τ-values;
  - for e ∈ F, R-plays follow π_v, o, then e's F-play;
  - for e ∈ R, the cycle o → e → π_e → o consists of unswitched R-paths.
- On 𝒞^1O, Ξ = min_e Ω_{σ,e} (only o chooses, and σ̄ is pointwise optimal) and W = Ω_{σ,τ(o)}. Both are unchanged, a contradiction.
  No (h) is needed at k+1. ✓
- DATA: 795 fallbacks in phases with neither endpoint OTHER; 591 value-changing, all crossings; 0 failures. Control: 10 value-changing
  fallbacks touch OTHER, and all 10 are crossings as well (no violation is possible there; the lemma does not claim it).

## 3. Theorem X: SIGN WITH GAPS (G-X-1 closed by Lemma TF)
### 3.1 The assembly, step by step
- Step 1 ✓. At most 1 + X + O F-intervals.
- Step 2 ✓. Every EQ → THR transition is an F-value change (F2), at most |F| − 1 by F1. With e such transitions there are ≤ 2e + 2 ≤ 2|F|
  blocks, of which ≤ e + 1 ≤ |F| are THR blocks.
- Step 3 ✓ (Lemma EQ, only transitions with both endpoints in the block).
- Step 4: sub-blocks (THR, τ, w, R constant, (h), flat fallbacks only).
  - The number of w-change cuts is ≤ |F| − 1 (F2, second claim; within F1's budget). So there are ≤ |F| + |F| − 1 ≤ 2|F| sub-blocks ✓.
  - PIECE with flat fallbacks inside: see 3.3 (N-X-3).
  - PIECE with θ varying: G-X-1, see 3.2.
- Step 5 ✓. Every transition of I falls in exactly one class: inside an EQ block, inside a sub-block, a block boundary, or a w-change
  cut. With |F| ≤ n − 1: (|F| + 1)(n − 1) + 2|F|(n − 2) + 2|F| + |F| − 1 ≤ 3n² − 4n ≤ 3n².
- Steps 6-7 ✓.
  - A value-preserving transition leaves Ξ unchanged, and Ωτ unchanged because τ is fixed, so R15 (d) bounds the runs by 4n(n − 1).
  - Total ≤ (#value-changing + 1)(4n(n − 1)) + #value-changing ≤ (3n²(1 + X + O) + X + O + 1)(4n(n − 1) + 1).
### 3.2 G-X-1: PIECE with θ free needs Lemma TF
- PIECE counts transitions at which some Ξ_k(v) or W_k(v) changes. Its R-part (𝓡 or 𝓡*) tracks routes against the constant terminal w,
  i.e. W on R.
- On R, Ξ = π ⊕ θ, so a θ-change changes Ξ at every R-vertex (o included) with no route change. R19 (f) signs "θ constant not needed
  (N-RE-4)". My N-RE-4 justified only the gate identity (Lemma G (c) per state), not this count. (R20's fixes file §6, "inside a piece
  the two notions coincide", assumes θ fixed.)
- Instance (fbref_n48.pg, sha1 414231a2…, SPEC run from the S3 start = n5.py's run: 60 iterations, 9 fallbacks; check_sol2: zlk OK,
  strategies verified):
  - The transition 56 → 57 lies in one phase (λ maps and τ(o) = 34 unchanged), with (h) at both ends and w = (27, ∅, 2) constant.
  - R = {o} = {14} at both ends, and there is no fallback. θ changes from (27, {28}, 9) to (27, {15, 28, 29}, 18).
  - So Ξ changes at the R-vertex 14, while 𝓡's budget is |R| − 1 = 0.
  - Ξ also changes at 3 = σ̄(o) ∈ F, 16 and 19 (switched: 3 → 6, 16 → 44).
  So the per-part statement "R-values change ≤ |R| − 1 times" is false when Ξ on R is counted. In my data this happens in 111 sub-blocks.
- Lemma TF (REFEREE-2, proved here). Let k → k+1 have τ constant, R_{k+1} = R_k and (h) at k and k+1. If θ_{k+1} ≠ θ_k, then Ξ changes at
  some vertex of F_k.
  Proof.
  - θ_j = min over exits e of Ω_{σ_j, e}(o) (𝒞^1O; σ̄ pointwise optimal).
  - By H1 at j, the minimiser σ̄_j(o) lies in F_j: if its play reached o, the honest play from o would return to o.
  - For e ∈ F_j, Ω_{σ_j, e}(o) = o ⊕ Ξ_j(e), since e's play avoids o and Ξ = W on F.
  - An exit e ∈ R gives a cycle through o, whose cycle node lies in R ∪ {o}, while every F-exit value has its cycle node in F. Values
    with different cycle nodes differ, so the minimum is attained only in F.
  - Hence θ_j = min_{e ∈ F} o ⊕ Ξ_j(e) for j = k, k+1, with the same set F. If Ξ is unchanged on F, then θ_{k+1} = θ_k. □
- With TF, every transition of a sub-block that changes Ξ or W changes W on R (a route; 𝓡's budget |R| − 1) or Ξ on F (𝓕's budget
  |F| − 1; θ-changes land here). So the total ≤ |R| − 1 + |F| − 1 holds, and Theorem X's step 4 is right. CLOSED.
- DATA (x_check.py): 317 θ-changes at THR → THR transitions inside F-intervals, all with an F-change. In 253 transitions Ξ on R changes
  without a route change, all with an F-change. The corrected split (R by W, F by Ξ = W) holds in all 753 sub-blocks (211 of them
  θ-varying), and so does the total. 0 failures.
- Proposed amendment to R19 (f): "θ constant not needed, provided the R-part counts route (W) changes; a θ-change under (h) at both ends is
  an F-change (Lemma TF)."
### 3.3 Citations used outside their exact signed form (all covered)
- N-X-2: R19 (b) (w = o ⊕ Ξ(τ(o))) is signed under (h) at two consecutive states. F2 uses it at k+1 alone. The identity needs only H2 at
  that state, plus Lemma G (a) and (V1); F2's own proof gives exactly this at k.
- N-X-3: P-N5-XA-fixes §5 / R20 (f) (pieces pass flat fallbacks) is signed for throttled stretches with u* ≠ none. Theorem X uses it in
  sub-blocks with θ varying and any u*. The argument needs only:
  - the fallback switches only flat F → F edges with disjoint regions;
  - it changes no value and leaves R and (h) unchanged.
  NF's proof gives exactly this when R is constant and k is THR ((h) at k+1 holds in a sub-block). So the use is covered. DATA: no flat
  fallback occurred inside a sub-block in my runs (all 204 flat fallbacks in phases lay elsewhere).
- R15 (d) (any N5 run), R17 (any start, any optimum), R18 (c)/(d) (one-player arena in G_τ) and Lemma G (a)/(c) ((c) only at THR
  states): all used within their signed hypotheses.
### 3.4 (FBRE-F) is not used
- Theorem X uses XW, EQ, FBL-N (ii), NF, F1, F2, PIECE (with TF), fixes §5, R15 (d) and R17. FB-W and the §8 table are not used. (FBRE-F)
  appears nowhere in §1-§7. ✓
- DATA: FBRE-F's failure reproduced. In (w, u*)-runs, 167 direct evictions at L ≥ k_0 + n − 1 had θ's status at u*, and 50 of them
  re-entered. FB-W excludes exactly these.
### 3.5 Theorem X on data
- 37,235 phases, 3,558 F-intervals.
- Value-changing transitions ≤ 3n²(1 + X + O) + X + O and transitions ≤ the full bound in every phase: 0 failures.
- Maxima: X = 70 (x48_rt48_final), O = 19, phase length 110, F1 count 16, EQ-run value changes 25.

## 4. Lemmas XW, EQ, FBL-N, F2, FB-W
- XW ✓. σ̄_k is pointwise optimal for Odd in G_{σ_k}, as in R18 (d) Lemma S (a)-(b).
  - XW1 ✓ (Lemma G (a)-(b) under (h)). XW2 ✓ (definitions).
  - XW3 ✓ (R15 (a) and XW; no phase needed).
  - DATA: XW at all 47,985 states of 15,378 runs; XW1 at all (h)-states. 0 failures.
- EQ ✓.
  - At EQ states the gate is G_τ's improving set, so S4a is R17's switch-best step in G_τ.
  - Fallbacks: S4a returned σ_k, so σ_k is a pointwise optimum (R18 (d)), and every gate edge is improving, hence flat (R18 (c)).
  - Flat switches at distinct cycle nodes have disjoint regions, so W is unchanged, and Ξ_{k+1} = Ξ_k by the sandwich
    Ξ_k ⊴ Ξ_{k+1} ⊴ W_{k+1} = W_k = Ξ_k.
  - λ_W = λ_Ξ on Q. PH counts from Q's first state.
  - DATA: 26,070 EQ runs, max 25 value changes, ≤ n − 1 in every run; 0 value-changing fallbacks in EQ runs.
- FBL-N ✓.
  - (ii): σ_k(x) ∈ F_k; the gate gives Ξ(z) ▷ Ξ(σ_k x) = W(σ_k x) ⊴ W(z) by XW; so the edge is W-improving at the optimum, hence flat.
  - (iii): if H2 fails, o lies on its own W-cycle C ⊆ R, so λ_W(z) ∈ C for z ∈ R.
  - DATA: 179 F-gate edges at fallbacks, all flat; 0 F → R gate edges where H2 fails.
- F2 ✓.
  - (h) at k+1 gives τ(o) ∈ F_{k+1} = F_k, then w_k = o ⊕ Ξ_k(τ o) and w_{k+1} = o ⊕ Ξ_{k+1}(τ o).
  - If Ξ(τ o) is unchanged, XW3 makes k+1 EQ, a contradiction.
  - The second claim follows likewise (N-X-2).
  - DATA: 58 EQ → THR transitions and 64 w-changes, each with a change of Ξ(τ(o)).
- FB-W ✓ given the CR row.
  - At t ∈ S, R-vertices carry θ_t's status at u* (u* is on no route; Lemma G (b)).
  - Coarse values are frozen from k_0 + n − 1 on (CR, θ-free row).
  - Ξ_{L+1}(z*) ⊵ Ξ_L(z*) with equal coarse parts, so it agrees above u* and keeps w's status (θ's status would make it strictly smaller).
  - x ≠ λ(x), so (V1) passes the status to x. Later values have the same coarse part and are ⊵, so they keep w's status. x ∉ R_t.
  - DATA: vacuous, as said (0 qualifying evictions).

## 5. The (w, u*)-run table (§8): agree (READING)
I re-read each R20 proof for where θ's constancy enters:
- §1 setting: per state ✓.
- Lemma C: per state, plus R15 (a) ✓. The top of P(θ_k) Δ P(w) is u* at every state by the definition of the run.
- P^c / CR: uses Lemma C at k and k+1, (Cstrict), (F1) per arena step, λ_W per state, and the vacuous fallback case. θ never enters ✓.
- XA: step 4 uses only u* topping P(θ_{E+1}) Δ P(w); step 5 uses Lemma C at L ✓.
- FBL strong form: per state ✓.
- FBF: NO is right. Its induction uses Ξ_t(z) = Ξ_L(z) on R_t, i.e. θ_t = θ_L ✓.
- DATA: 1,735 (w, u*)-runs (198 with θ varying; longest 97), spanning crossings: Lemma C equality and monotonicity and CR (last coarse
  change ≤ n − 1) hold with 0 failures.

## 6. Mechanical checks (DATA; logs/totals.txt)
| quantity | count | violations |
| --- | --- | --- |
| runs / transitions / phases | 15,378 / 32,607 / 37,235 | — |
| states EQ / THR / OTHER | 32,205 / 6,687 / 9,093 | — |
| XW, XW1 | all states | 0 |
| Lemma EQ (EQ runs) | 26,070 | 0 |
| FBL-N (ii)/(iii) (F-gate edges at fallbacks) | 179 | 0 |
| NF (fallbacks, no OTHER endpoint) | 795 (591 value-changing, all crossings) | 0 |
| F1 (F-intervals) | 3,558 (max 16 F-changes) | 0 |
| F2 (EQ → THR / w-changes) | 58 / 64 | 0 |
| TF (θ-changes at THR → THR in F-intervals) | 317 | 0 |
| PIECE, θ free, corrected split (sub-blocks) | 753 (211 θ-varying) | 0 |
| R19 (f) per-part reading with Ξ on R counted | fails in 111 sub-blocks (G-X-1) | — (the gap, not a packet statement) |
| Theorem X bounds per phase | 37,235 | 0 |
| (w, u*)-runs: Lemma C, CR | 1,735 (198 θ-varying) | 0 |
| FB-W | 0 qualifying evictions (vacuous) | — |
| FBRE-F failure (θ-status evictions that re-enter) | 50 of 167 | — (confirms FALSE) |
Sources:
- Random o-cyclic 𝒞^1O, n 6-14, random starts: own seeds 101 and 102 (6,000 runs each), SPEC seed 103 (3,000).
- Named instances, SPEC from the S3 start (or their .start) plus 20 own runs each: the 8 instances of experiments/new/box28/instances/,
  L-RED's fbref_cex_n32, fts_best16, theta_tp32, returns_rt48, returns_ph64, rtt24, tr20_s4, fbh_thr, wdrop_cyc, and my c12_s54.

## 7. Gap list
| id | where | status |
| --- | --- | --- |
| G-X-1 | Theorem X step 4 via R19 (f) "θ free": Ξ on R changes with θ | CLOSED by Lemma TF (§3.2). Amend R19 (f) (my N-RE-4 was incomplete) |
| N-X-1 | F1 step 2: Lemma G (a) holds at every state | remark |
| N-X-2 | F2 uses R19 (b) at one state | covered (H2 suffices) |
| N-X-3 | fixes §5 used outside u* ≠ none | covered (NF's proof gives the property) |
| — | FB-W | no data |

## C. Comparison with REFEREE's R-N5-X (claude/referee 53c0c68, on trunk since 9aea5b6; read after my push 059f492a; written 18:43Z by date -u)
### C.1 Agreement per item
| item | REFEREE | REFEREE-2 | agreement |
| --- | --- | --- | --- |
| F1 | SIGNED WITH GAPS (X-2) | SIGN (N-X-1) | full. I accept X-2 (F = ∅: read max(0, \|F\| − 1)). I missed it, though my checker already used max(0, ·). REFEREE's §1 remark on step 2 = my N-X-1 |
| NF | SIGNED WITH GAPS (X-3) | SIGN | full. I accept X-3 as wording. My §4 (EQ) uses the sandwich Ξ_k ⊴ Ξ_{k+1} ⊴ W_{k+1} = W_k = Ξ_k, which is X-3's line; the packet's citation of §2 does not show it |
| Theorem X | SIGNED WITH GAPS (X-1, X-2, X-4) | SIGN WITH GAPS (G-X-1; N-X-2, N-X-3) | full on substance (C.2) |
| XW, EQ, FBL-N, F2, FB-W | SIGNED | SIGN | full (FB-W: REFEREE notes the fallback hypothesis is not used; agreed) |
| (w, u*)-run table | checked, every row right | agree | full |
| Consequence (READING) | checked; τ-changes ≤ d − 1 by R15 (c) on G^d | not addressed | I accept REFEREE's check: R15 (c) makes τ's sequence strictly increasing, so τ(o) never repeats |
No disagreement on any verdict.
### C.2 Gap map (joint)
| REFEREE | REFEREE-2 | note |
| --- | --- | --- |
| X-1 (θ-free PIECE count) | G-X-1 | the same gap, found independently. Wording difference only, see C.4 |
| X-2 (F = ∅) | — | accepted; wording |
| X-3 (NF EQ case) | — (covered in my §4) | accepted; wording |
| X-4 (fixes §5 / R20 (f) outside u* ≠ none) | N-X-3 | the same: valid as a re-derivation from NF's classification, not as a citation |
| §3.3 row "R19 (b): (h) at the state" | N-X-2 | the same point. R19 (b) as landed is phrased for consecutive states; at one state H2 suffices |
| §1 remark (step 2 needs only Lemma G (a)) | N-X-1 | the same |
### C.3 Is REFEREE's X-1 proof a valid substitute for my TF, or the reverse?
- Both are valid, and REFEREE's needs less. I checked it.
  - Under H1 at k, e_k := σ̄_k(o) has an o-free play, so e_k ∈ F_k, and θ_k = o ⊕ W_k(e_k).
  - R is constant on the sub-block, so e_k ∈ F_{k+1}, and its play under σ_{k+1} still avoids o.
  - If W is unchanged on F, then Lemma S (a) (θ is the minimum over exits) gives θ_{k+1} ⊴ o ⊕ W_{k+1}(e_k) = θ_k.
  - R15 (a) gives θ_{k+1} ⊵ θ_k. So θ_{k+1} = θ_k. ✓
- It uses H1 at k, R constant, and R15 (a).
- My TF (§3.2) uses (h) at both ends and the fact that values with distinct cycle nodes differ (so the minimum over exits is attained only
  in F). It does not use R15 (a).
- REFEREE's proof is a valid substitute for TF and is shorter. TF is a valid substitute for it inside sub-blocks, where (h) holds at both
  ends. I recommend citing REFEREE's form, with TF as the second check.
### C.4 The clarified R19 (f) wording (docs/agents/R19-note-X1.md, the 18:28Z text in my tree)
- I CONFIRM the note's missing step and its proof (= C.3).
- One correction, on "R19 (f) as landed is TRUE". REFEREE and I differ only in how we read R19 (f)'s per-part sentence, "each piece has
  ≤ |R| − 1 resp. |F| − 1 value-changing transitions".
  - Read as 𝓡*-values (routes, i.e. W on R) and 𝓕-values: TRUE with θ free. A θ-change is charged to F by X-1.
  - Read with Ξ on R counted on the R side: FALSE with θ free. fbref_n48 56 → 57 has R = {o}, so the R budget is 0, yet Ξ(o) = θ changes.
    The Lead re-ran this with my dump_tf.py and got the same result.
  - The TOTAL (|R| − 1) + (|F| − 1) is true either way.
- Proposed wording for the note (replacing "R19 (f) as landed is TRUE"):
  "R19 (f) holds with θ free in this form: the R-part bound counts route (𝓡*, i.e. W on R) changes; a θ-change at a transition with H1 at
  its start and R constant changes W on F (REFEREE X-1) and is charged to the F-part; the total (|R| − 1) + (|F| − 1) counts transitions at
  which Ξ or W changes. Read with Ξ on R counted in the R-part, the per-part bound fails with θ varying (fbref_n48, transition 56 → 57,
  R = {o})."
- Hypotheses of the missing step: H1 at k, R constant on the transition, τ constant, one joint λ-phase. (h) at k+1 is not needed for X-1.
### C.5 Final verdicts (Opus 5.5, D15)
| statement | final |
| --- | --- |
| (1) F1 | SIGN (X-2 wording accepted) |
| (2) NF | SIGN (X-3 wording accepted) |
| (3) Theorem X | SIGN WITH GAPS, all closed: G-X-1 = X-1 (REFEREE's proof, or TF); X-2; X-4 = N-X-3; N-X-2 |
| (4) XW, EQ, FBL-N, F2, FB-W | SIGN (FB-W: no data in either report's runs that I know of; REFEREE does not report FB-W data) |
| (5) table | agree |
Joint open items: none in this packet. (X), (NH') and G-N5-TIME stay OPEN.
