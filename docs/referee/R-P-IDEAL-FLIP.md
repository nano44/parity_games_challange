# R-P-IDEAL-FLIP: REFEREE report on P-IDEAL-FLIP (L-NEW successor 53, box 162)
REFEREE successor 23 (Opus 5.5, D15), 2026-11-05T11:14Z by date -u. Independent: I did not read docs/referee-2/.
- Stale-clone check: HEAD = ls-remote = e51a0b37, and ff-only had nothing to merge.
- Object: claude/l-new 9effea1f, an ancestor of origin/claude/l-new. I re-measured every file:
  - packet 92803bd5 (236 lines);
  - L-1 36418d16 (1 line, 0 «|»);
  - iso_d4_st9 7ca1e68c, kf0_d2_t2 c2233e05, kf1_d2_t3 d368d441.

## 0. Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §2 | W-ONLY (a), (b), (c), (d) | SIGN |
| §3 | NOW-ONCE (a), (b), (c) | SIGN (note FL-N1: (b) does not need ISO) |
| §4 | SWAP | SIGN |
| §4 | SWAP-RUN | SIGN (note FL-N2: the «no such q» caveat is removable) |
| §5 | FLIP-1: T_0(1) = 2, T_k(1) = 3 (k ≥ 1) | SIGN |
| §6 | DEAD SC-ISO | SIGN AS CONDITIONAL, gap FL-G1 (machine premise T^R(3) ≤ 8). The unconditional part, «SC-ISO at d = 4 ⇒ T^R(3) ≥ 9», is SIGNED |
| §7 | DATA, checks, exclusions, TARGET diff | not to sign; w162 and pin162 MATCH; diff agreed |
| line | L-1 | NOT YET: REQUIRED FL-L1, FL-L2, FL-L3 |

## 1. Premise route
- Premises:
  - R104's definition. §0 is the P-IDEAL-SLOT §0 restatement, with facts (F1) and (F2) immediate from it.
  - R109 SEG-ONCE at l = −1. The quote is FOUND verbatim in the landed R109 line (trunk 42c7711b, RESULTS l. 11030; grep -F: 1 hit).
    It is used in §2 (d) and §3 (c) only, for «each level-0 mover of a degree-≤-2 genome moves at most once».
- No R105 (E-2 irrelevant), R106 to R108, docs/lit or docs/sources. T* is named but never used. I checked that no proof uses a value of
  T* or of T^R, except the DEAD item's machine premise.
- The SC-ISO quote is a prefix of docs/new/N5-SLOT-box160.md l. 50 (the source continues «…, and DEAD at d = 4 for ISO»). The precise
  W-channel form is the packet's.

## 2. Proof checks
- W-ONLY (a): SIGN.
  - Level 1. The real key (g(w, s″(w)), g(o)) and the c-key (κ^c_w, g(o)) tie on the first entry iff w = w′. For w ≠ w′, both orders
    are «0 first iff b_0(s″) = 1 iff c = 1».
  - Level ≥ 2. The prefixes are the same option p (by agreement at level l − 1). (F1) makes distinct prefixes differ, and the order
    claim at l − 1 transfers.
  - Both systems pick from the same A_s(x).
  - Uses only that the level-0 movers are exactly {0, 1}. No ISO is needed.
- W-ONLY (b): SIGN. Under ISO, no chain of a U-option passes 0 or 1, and key^c never reads 0 or 1.
- W-ONLY (c): SIGN.
  - H_q is valid and lies in 𝓦_d, and b_0 is constant = b_0(q).
  - A-sets on U are those of G (by (b)); keys are (a) applied to H_q.
  - Stop rule: the all-singleton case gives Step^c(s) = s.
- W-ONLY (d): SIGN.
  - The induction u_t|U = s_t|U goes through by (b) then (a).
  - c changes only at steps that move 0 or 1. SEG-ONCE (all degree 2) gives ≤ 2 such steps, so flips ≤ 2.
  - The non-counted steps move only level-0 movers, which gives + 2.
- NOW-ONCE: SIGN.
  - KP at level 1: option 0 iff b_0 = 1 (real) / iff c = 1 (forced).
  - (a) uses (F2) and needs no ISO. (b) is the same argument with key^c. (c) combines SEG-ONCE (l = −1) with (a).
  - FL-N1: the proof of (b) uses no ISO. The c-step is defined for every G ∈ 𝓦_d, so (b) holds for every G ∈ 𝓛^R_d. The packet states
    (b) only under ISO, because forced runs are defined only for ISO genomes.
- SWAP: SIGN.
  - κ^c_(1−k) = κ^(1−c)_k (checked for k = 0, 1).
  - Levels ≥ 2 have the same W-targets, so by induction the keys are equal. The Ξ-data and A-sets are equal.
- SWAP-RUN: SIGN.
  - Blocks of constant c: Step^(c*)_G or, by SWAP, Step^(c*)_(G^swap). W-ONLY (b) and (c) turn each block into a prefix of an IDEAL run
    of G_q or (G^swap)_q from the block's start state, followed by idle frames.
  - FL-N2: the caveat «if no q with b_0(q) = c* exists» is not needed.
    - b_0 takes at least one value on the four level-0 configurations.
    - If every q has b_0(q) = 1 − c*, then:
      - blocks with c = 1 − c* are runs of G_q (b_0(q) = 1 − c*);
      - blocks with c = c* use Step^(c*)_G = Step^(1−c*)_(G^swap) (SWAP with c := 1 − c*), so they are runs of (G^swap)_q.
    - So in every case a forced run with k flips is a concatenation of ≤ k + 1 runs of the two fixed IDEAL genomes G_q and (G^swap)_q.
  - I checked this argument. It is not in the packet's text (see FL-L2).
- FLIP-1: SIGN.
  - Upper.
    - v exists, because the Ξ-graph is acyclic and ISO holds.
    - v's two values are state-independent singletons, so v changes at most once.
    - u's two values depend only on v's option and always differ. Two consecutive u-changes need a v-change in between, so u changes at
      most twice, and moves ≤ 3.
    - k = 0: NOW-ONCE (b) gives ≤ 2.
  - Lower: the two instances, re-run below.
- DEAD SC-ISO: SIGN AS CONDITIONAL, gap FL-G1.
  - The instance is checked (§3): 𝓛^R_4, ISO, T 11, level-0 steps 7 and 8, seg1 6 + tail 3 = 9.
  - So «SC-ISO at d = 4 ⇒ T^R(3) ≥ 9» is PROVED (by the instance alone). That part I SIGN.
  - The DEAD conclusion needs T^R(3) ≤ 8. That is a CaDiCaL UNSAT on L-RED's xcnf encoding: not landed, not Lean, not refereed, and I did
    not check the encoding.
  - My ruling, asked by the Lead:
    - The DEAD cannot be signed unconditionally now. L43 needs a refereed proof or an instance beyond an EXPLICIT ESTABLISHED bound,
      and here the bound itself is the open premise.
    - Under Lead reading L42 (an uncovered premise is stated as an explicit hypothesis, labelled CONDITIONAL), it CAN be signed now as
      «CONDITIONAL DEAD (premise: T^R(3) ≤ 8, machine)», with the gap listed.
  - To drop «CONDITIONAL», the premise must itself become an established result. I recommend:
    - L-COMP 9's independent encoding and cube UNSAT agreeing with L-RED's;
    - a referee check that each encoding is faithful to R104's step rule (as for any machine claim);
    - the premise landed as its own RESULTS entry, cited by the DEAD line.

## 3. Independent checks (scratch/flip_probe.py; β-set simulator written from R104's text; c-step and forced runs from §1's text)
- Log: xinew_logs/flip_probe.txt.
- iso_d4_st9:
  - in 𝓛^R_4 (lev ⌊x/2⌋, degree 2, wt = 2(l − 1) + k), and ISO;
  - T = 11, the 12 states EQUAL §6's list, level-0 steps [7, 8], seg1 6, tail 3.
- I-0 (kf0_d2_t2): ISO, in 𝓛^R_2. The forced run with c ≡ 0 has U-frames (0,0) → (0,1) → (1,1) → (1,1): moves 2, as in §5.
  - My exhaustive V_k (max moves over all bit sequences with ≤ k changes): V_0 = V_1 = V_6 = 2.
- I-1 (kf1_d2_t3): with c = (0, 1, 1), the frames are (1,0) → (1,1) → (0,1) → (0,0): moves 3, as in §5.
  - V_0 = 1, V_1 = V_6 = 3.
- FLIP-1 bounds, exhaustive per (genome, start): 400 random ISO genomes of 𝓛^R_2 × 16 starts = 6,400 pairs. max V_0 = 2, max V_6 = 3:
  0 violations, and both bounds are reached.
- W-ONLY (a) on 367 real steps of 400 random 𝓛^R_3 genomes (ISO not required): 0 violations.
- Not checked by me: T^R(3) ≤ 8. A brute force over 𝓛^R_3 is out of reach here, and I did not audit xcnf.py.

## 4. Machine checks at 9effea1f (detached worktree, 17 s)
- w162:
  - «… WONLY 0 ISOA 0 FROZ 0 CONS 0 SWAP 0 SWAPNEG 12594 NOWONCE 0 NOWCTRL 307 FLIP1 0»;
  - «INST iso_d4_st9 LR True ISO True d 4 T 11 level-0 steps [7, 8] seg1 6 tail 3»;
  - «WIT kf0_d2_t2.json … V_0 2» and «WIT kf1_d2_t3.json … V_1 3»;
  - the box 150 checker on the instance: «TOTAL genomes 1 runs 1 steps 11 … VIOL 0».
  - All match check.sh's patterns.
- The CHECKED counts equal the line's DATA (44,084 / 31,320 / 1,044 / 28,896 / 307 / 15,660 / 1,312).
- pin162: all five sha1s EQUAL.

## 5. Diff against TARGET.md
- No statement concerns parity games, regions, running time or the cost model. Each is about R104's IDEAL model, or the forced run
  defined from it.
- Agreed with §7: not M4, not M3, not a gauntlet step. G-N5-TIME OPEN.

## 6. Line L-1 (definitions diffed; DATA scoped per C120)
- Definitions MATCH §1:
  - 𝓦_d;
  - 𝓛^R_d (movers 2l, 2l + 1 on level l, degree 2, no other movers, wt = 2(l − 1) + k);
  - T^R(d) (kept apart from T*; T^R ≤ T* since 𝓛^R_d ⊆ 𝓛_d);
  - ISO; b_0;
  - the c-step (A-sets old, keys new, 0 and 1 kept, level-1 key (κ^c_w, gate), κ^c_0 = 1 − c, κ^c_1 = c);
  - T_k(m) (sup over ISO genomes of 𝓛^R_(m+1), starts, bit sequences with ≤ k changes, of the U-changing frames).
- Claims MATCH: W-ONLY (a)-(d) with their hypotheses; NOW-ONCE (a); SWAP; FLIP-1 with instance sha1s.
- DATA: every count is scoped to its statement and equals my w162 re-run, and the unsupported items are named («NOW-ONCE for c_t-step
  sequences and the T_k(m) values for m ≥ 2: no signed DATA»). This MEETS C120.
- REQUIRED FL-L1 (NOW-ONCE (b) hypothesis). The line states the c_t-step half «on 𝓛^R_d» without ISO, while the signed (b) is
  [forced runs, ISO]. It is true without ISO (FL-N1), but the line must match a signed statement. Either:
  - add «(ISO)» to that half; or
  - add a fixes entry extending (b) to every G ∈ 𝓛^R_d, with the one-sentence note that the proof uses no ISO.
- REQUIRED FL-L2 (SWAP-RUN scope). «so under ISO a c_t-step sequence with k changes is a concatenation of at most k + 1 runs of two fixed
  IDEAL genomes» is unconditional. The packet signs it only when some q has b_0(q) = c_1, and says the reading «needs such a q». It is
  true in general (FL-N2), but that argument is not in the packet. Either:
  - a fixes entry adds FL-N2's role exchange; or
  - the line adds «(when some level-0 options q have b_0(q) = c_1)».
- REQUIRED FL-L3 (DEAD label).
  - «DEAD: the lane conjecture SC-ISO (…) is false, by … together with the machine premise T^R(3) ≤ 8 (…)» → «CONDITIONAL DEAD
    (premise T^R(3) ≤ 8, machine; …): the lane conjecture SC-ISO (…) is false under that premise, by …».
  - Keep the existing parenthesis «without it the instance shows that SC-ISO at d = 4 forces T^R(3) ≥ 9». That is the signed
    unconditional part.
- VERDICT: line L-1 NOT YET. It matches once FL-L1, FL-L2 and FL-L3 are applied.

## DONE / FINDINGS / NEEDS
- DONE:
  - this report;
  - w162 and pin162 MATCH;
  - all three instances recomputed;
  - FLIP-1 bounds exhaustively checked on 6,400 pairs;
  - definitions diffed; DATA scoping checked.
- FINDINGS:
  - W-ONLY, NOW-ONCE, SWAP, SWAP-RUN and FLIP-1: SIGN.
  - DEAD SC-ISO: CONDITIONAL on the machine premise T^R(3) ≤ 8 (FL-G1). The implication «SC-ISO at d = 4 ⇒ T^R(3) ≥ 9» is SIGNED.
  - Line L-1 NOT YET: FL-L1, FL-L2, FL-L3.
- NEEDS:
  - Lead: route FL-L1 to L3 (fixes entry or line) to L-NEW 53.
  - Lead: forward L-COMP 9's independent T^R(3) ≤ 8 result. Dropping «CONDITIONAL» needs that plus a faithfulness check of the encodings
    and a landed premise. The Lead or CHECKER decides the route.

## §C (2026-11-05T12:55Z by date -u, successor 23; Opus 5.5, D15): fixes entry 1 and line L-2
- Object: claude/l-new 4c2e5124, an ancestor of origin/claude/l-new. I re-measured every file:
  - fixes f8d3677e, 57 lines;
  - L-2 8099415b, 1 line, 0 «|»;
  - packet 92803bd5 / 236 and L-1 36418d16: unchanged.
- F-a, NOW-ONCE (b′) without ISO (new signed content): SIGN.
  - The c_t-step sequence is defined on any G ∈ 𝓛^R_d via the c-step of 𝓦_d, and 0 and 1 are kept.
  - KP^c(x) = 0 iff c = 1: key^c(x, k) = (κ^c_k, g(x, k)), and the first entries differ. This holds for every state.
  - A change at frame t takes an option of A_(u_(t−1))(x) other than the current one. At degree 2 both options are then available, so
    the new option is KP^(c_t)(x).
  - Two consecutive changes in a constant-c interval give u_(t2)(x) = u_(t1)(x) = u_(t2−1)(x), a contradiction.
  - No Ξ-value and no ISO is used. Correct; it closes FL-L1 by extension.
- F-b, SWAP-RUN for ANY q (exchange argument): SIGN.
  - Put v := b_0(q).
  - Blocks with c = v are runs of H_q (W-ONLY (c) for G).
  - Blocks with c = 1 − v use Step^(1−v)_G = Step^v_(G^swap) (SWAP with c := v), and are runs of (G^swap)_q (W-ONLY (c) for G^swap,
    which is ISO with the same level-0 gates, so its b_0(q) = v).
  - Once a step is idle it stays idle.
  - Correct. It is the same argument as my FL-N2, in a cleaner form (no c* needed). It closes FL-L2, and the caveat paragraph is
    superseded.
- F-c (REFEREE-2 F-1, unsigned remark): CORRECT.
  - H_q and (G^swap)_q have degree-1 level-0 movers, so they are not in 𝓛_d.
  - R109 SHIFT applies (the quote's two pieces are verbatim in the landed R109 line). The shifted genome lies in 𝓛_(d−1): its new level
    0 holds the two degree-2 movers of old level 1 plus two degree-1 movers, and every higher level holds two degree-2 movers.
  - So each piece is ≤ T*(d − 1). The remark stays outside the signed text.
- L-2: my own word diff (git diff --word-diff) finds exactly 3 hunks, equal to entry 1's list.
  - «CONDITIONAL DEAD (premise T^R(3) ≤ 8, machine):»: FL-L3 is MET. The clause «without it … forces T^R(3) ≥ 9» is kept.
  - «whose run from any state with q at 0 and 1 is the iterated b_0(q)-step»: this is W-ONLY (c)'s statement. Correct.
  - «every start)»: §7 says every start for d ≤ 4, and every checked genome has d ≤ 4 (random d = 2, 3, 4; corpus d ≤ 4). Correct.
  - NOW-ONCE's c_t-step half and SWAP-RUN's unconditional form now match signed statements ((b′), F-b).
  - All other definitions and clauses are unchanged from L-1, which I diffed in §6.
- VERDICT: line L-2 MATCHES.
  - Signed: W-ONLY, NOW-ONCE (incl. (b′)), SWAP, SWAP-RUN (F-b form) and FLIP-1.
  - SC-ISO is CONDITIONAL DEAD (gap FL-G1), and its implication «SC-ISO at d = 4 ⇒ T^R(3) ≥ 9» is signed.
- FL-G1 status (FYI from the Lead): L-COMP 9 reports T^R(3) = 8 by an independent encoding (claude/l-comp 6f19564f), and REFEREE-2 is
  auditing it. I have not audited either encoding.
  - The label can lose «CONDITIONAL» only when the premise is established as its own landed item (as said in §2). That is a new
    line, not this one.

## §C add. 1 (2026-11-05T17:05Z by date -u, successor 24; Opus 5.5, D15): line L-3 byte test
- Object: claude/l-new 47b4e165 (ancestor of origin head a9851eba; the L-3 file is identical at both), docs/new/P-IDEAL-FLIP-line-L3.txt
  sha1 4089bd73baf65929cf5b6094ef31882df817fd53 (with newline), 4,715 bytes; fixes entry 2 in docs/new/P-IDEAL-FLIP-fixes.md (file
  sha1 4220c44e…).
- Test (scratch/flip_l3_bytetest.py): expected = L-2 (l-new 4c2e5124, sha1 8099415b…) with exactly CHECKER C122 §5's R1-R4, the old and
  new strings parsed from the CHECKER file itself (claude/checker 80ed31a6, docs/checker/C122.md; wrapped lines joined with single
  spaces). Each old string occurs exactly once in L-2. My rebuild was made BEFORE L-3 was pushed and already gave sha1 4089bd73….
- Result: L-3 EQUALS the expected bytes (sha1 4089bd73…, 4,715 bytes, one line). 53 «(» / 53 «)», depth never negative, 0 «|»,
  one « — », «2026» once. The unclosed DATA parenthesis of L-2 (C122 G-0) is closed by R4.
- Packet: docs/new/P-IDEAL-FLIP.md unchanged 4c2e5124 → 47b4e165. Fixes entry 2 states DATA scope / source-note changes only, and its
  word diff equals R1-R4; no signed statement, definition or premise changes.
- Verdict: L-3 MATCHES (L-2 + C122 §5 R1-R4, nothing else). All signatures of this report carry over unchanged; DEAD SC-ISO stays
  CONDITIONAL (FL-G1), see R-T3R-audit.md for the premise.
