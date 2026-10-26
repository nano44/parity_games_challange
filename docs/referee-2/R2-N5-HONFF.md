# R2-N5-HONFF: REFEREE-2 report on packet P-N5-HONFF (FB-RISE; HON-FF: W-honest states per phase ≤ 4n² − 3n with no fallback term)
Referee: REFEREE-2 successor 16 (session_01R1scbTA9MiKutHRhRdi3zh), Opus 5.5 (D15, L37). Written 2026-10-26 13:06Z (date -u).
Object: docs/new/P-N5-HONFF-box47.md, sha1 98101d1fe723a570f3c79085b929a456ebb7dff5 (`git show 4a0a8aba:… | sha1sum` and the same at l-new
2fca63b8), 141 lines, pinned at trunk 4a0a8aba, frozen. Author L-NEW successor 26. Reviewed as a new object (my R2-N5-HON is a reference).
Independence: written before opening any REFEREE file on HONFF; `git fetch origin claude/referee` + `git ls-tree --name-only -r
origin/claude/referee docs/referee/ | grep -ic honff` gave 0 at 12:24Z and 1 at 13:06Z (same turn as the push). (REFEREE's R-N5-HON.md,
quoted by the packet, is the finished HON review, read at the HON §C.) The lane's tools (experiments/new/box47/*.py) were NOT run or imported.
Checker: docs/referee-2/R2-N5-HONFF/honff_check.py (own; on my R2-N5-HON/hon_check.py and succ. 13's SPEC loop; Ξ, W my own play values;
LEV and LEV_odd exact by enumeration of all simple paths of G_τ, with a per-phase budget).
Scope (D1): HON-FF counts one kind of state; it does NOT bound f. Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Verdicts
| item | verdict | premises (checked) |
| --- | --- | --- |
| §1 Lemma FB-RISE (a) general form | SIGN | SPEC S2, S4c, FIX 3; (MON) = R15 (a), (d) via (VJ) (P1); R17 (V1), (V2); Lemma P Case A (Q-A) |
| §1 Lemma FB-RISE (b) honest form | SIGN | (a); (MON); SAT0's Odd case (with N-HON-1's wording), which uses only (V1), (V2) |
| §2 Theorem HON-FF (≤ 4n² − 3n) | SIGN | FB-RISE (b); Lemma HON steps 0-3 (step 1 for fallback-free gaps: WM and S (c), P2) |
| §2 Corollary HON-0-FF (a)-(c) | SIGN | HON-FF; HON-0's proof |
| §2 REC-0 difference f(n + 1) + 2 | CHECKED (algebra; per phase in data) | — |
| §2 Corollary REC-1-FF (a) | SIGN | HON-0-FF (a); REC-1 (a)'s proof |
| §2 Corollary REC-1-FF (c), (d) | SIGN as IMPLICATIONS from (Στ) (which holds at R65's audit strength) | via EP-1u |
| Q-A (Lemma P's Case A with Ω := Ξ_t) | YES (§1) | — |
| §5 quotes (17) | all VERBATIM (my own substring check against the six named files at l-new 0238b1cb) | — |
No gap. Notes N-HONFF-1..4 (§3). Not reviewed (as briefed): §3 (DATA), §4 (OPEN / READING), the READING in §1.

## 1. Proof check, and Q-A
- Q-A: YES. Lemma P's Case A (box 10 §2, A1, A2) reads, about Ω and ρ: (i) the Case-A inequality Ω(z) ⪯ Ω(ρ(x)); (ii) the bound Ω(z) ⪰
  value(r′); (iii) A1: (V1) at x, Ω(x) = x ⊕ Ω(ρ(x)), with ρ(x)'s path to λ(x) avoiding x (when x is on its own cycle below its node, the
  arc from ρ(x) reaches the node before returning to x), and x ∉ r′; then (V2); (iv) A2: Ω(x) = (x, ∅, 0) at an own cycle node, and Ω(ρ(x))
  has cycle node x because ρ(x) lies on x's cycle. All four are facts about the VALUE OF A PLAY of a positional strategy pair: the
  one-player hypothesis of R17 is not used. Ξ_t is the play value of (σ_t, σ̄_t) (§0), so Case A holds with Ω := Ξ_t, ρ := σ_t, and S2's Iσ_t
  as the improving set (Case A's hypothesis "(x, z) ∉ I" is exactly "Ξ_t(z) ⪯ Ξ_t(σ_t x)"). No optimality premise (P1 or P2) is needed for
  Case A itself. Data: QA, the pointwise form (every state, Even x, non-improving z, simple path x z r′ with Ξ_t(z) ⪰ value(r′) ⇒ value(r) ⪯
  Ξ_t(x)), 661,000,000+ checks, 0 failures (§4).
- FB-RISE (a). The fallback is in-phase, hence Even's (FIX 3: τ kept), and switches exactly the x with Iσ_t(x) ≠ ∅ to z*(x) (S4c); λ fixed.
  For r = x → z → r′, |r| ≤ j: |r′| ≤ j − 1 ≤ LEV(t). (1) Odd x: |r| ≤ LEV_odd(t) and (MON). (2) Even x, z non-improving (any x, switched or
  not): Case A at t, then (MON). (3) z improving: x switched; Ξ_t(z*) ⪰ Ξ_t(z) ⪰ value(r′) (z* is the Ξ_t-maximum over Iσ_t(x) ∋ z), (MON)
  to t + 1; 3a λ(x) ≠ x: (V1) at t + 1 (x's honest play is x then z*'s) and (V2) (r′ avoids x; z*'s path to λ(x) avoids x); 3b λ(x) = x:
  z* is on x's cycle at t + 1, so λ(z*) = x (phase) and Ξ_t(z*) has node x ≠ u, hence x beats u and (x, ∅, 0) ≻ value(r). CORRECT. It uses no
  arena optimality (no P2) and no W.
- FB-RISE (b). LEV(h) = n − 1: (MON). Otherwise, for Odd x every simple r of G_τ starts x → τ(x); at the W-honest h, W_h(τ x) = Ξ_h(τ x) ⪰
  value(r′) and λ_W = λ; SAT0's Odd case (not its own W-cycle node: (V1), (V2), with τ(x)'s PATH to its node avoiding x, N-HON-1; own node:
  rewards) gives W_h(x) ⪰ value(r); Ξ_t(x) ⪰ Ξ_h(x) = W_h(x) (MON over [h, t], any transitions). So LEV_odd(t) ≥ LEV(h) + 1 and LEV(t) ≥ LEV(h);
  (a) closes. SAT0's Odd case does not use SAT0's hypothesis "no W-improving edge" (that is for Even vertices). CORRECT.
- HON-FF. Gaps between consecutive unsaturated W-honest states: fallback-free ⇒ step 1 (as signed in HON); with a fallback t ∈ [h_i, h_{i+1} − 1]
  ⇒ FB-RISE (b) with h := h_i ≤ t, then (MON) to h_{i+1}. Every one of the s − 1 gaps rises, 0 ≤ LEV(h_1), LEV(h_s) ≤ n − 2: s ≤ n − 1; the
  saturated tail ≤ 4n(n − 1) + 1 (HON step 3, R15 (d)). (n − 1) + 4n(n − 1) + 1 = 4n² − 3n. CORRECT. The "What is replaced" bullet is right:
  a gap with a fallback reads no W value after h (both uses named in HON-N3 are avoided), so the fallback-free hypothesis is needed only
  where step 1 is used.
- HON-0-FF, REC-1-FF (a): the HON proofs with HON-FF in place of HON (f enters REC-1 (a) only through HON-0 (a)). CORRECT. (c), (d): REC-1 (c),
  (d) with f deleted, through EP-1u; implications. CORRECT as implications.
- REC-0 comparison: (f + 1)(n + 1) + 4n(n − 1) + 1 − (4n² − 3n) = f(n + 1) + 2. CORRECT.

## 2. Premises, complete list
SPEC S2, S4c, FIX 3 (in-phase fallback is Even's); phase (R38 (a)); (MON) = R15 (a), (d) on SPEC's Ξ via (VJ) under P1; R17 (V1), (V2) and
Lemma P Case A (Q-A: play-value facts); P-N5-HON (to land as R68): Lemma HON steps 0-3 (step 1 uses WM = R23 (g) and Lemma S (c), i.e. P2),
SAT0's Odd case with N-HON-1, HON-0's and REC-1's proofs; (Στ) (R64 (e); R65) for REC-1-FF (c), (d) only. The packet's list is complete and
slightly over-complete (N-HONFF-1).

## 3. Notes (no gap)
- N-HONFF-1 (premise line). "RESULTS R21 (a) XW and R23 (g) WM enter only through HON step 1": WM does; XW does NOT enter HON-FF at all (in
  P-N5-HON, XW is used only in HON-FB (iv), which HON-FF does not cite). Over-complete, not wrong; suggest "WM (and Lemma S (c)) enter only
  through HON step 1; XW is not used".
- N-HONFF-2 (premise forms). FB-RISE (a), (b) need P1 only (through (MON)); P2 enters HON-FF only through HON step 1 on fallback-free gaps.
  Worth stating, since FB-RISE is the new ingredient and is free of the arena-optimality premise.
- N-HONFF-3 (data where it matters, thin). Exact LEV reached 5 of the 6 known gaps with an inside fallback (j10_n24, ffin5_n32, ffin4_n24
  at budget 3·10⁶; j8_n32 and ffin12_n32 at 1.5·10⁸), with 24 non-W-honest in-phase fallbacks after a W-honest state, all with FB-RISE (a)
  and (b) holding and every gap rising; j7_n32 stays over budget even at 1.5·10⁸ paths per phase (UNK). The library runs (overlapping sets) have 3 such
  fallbacks; random runs none. FB-RISE (a) itself is exercised at 1,642 in-phase fallbacks (1,084 at non-honest states).
- N-HONFF-4 (control). Dropping the LEV_odd term ("LEV(t + 1) ≥ min(LEV(t) + 1, n − 1)") fails 152 times on lib41 (one start), as the packet's
  CTRL_T reports for its samples: the Odd term is needed, and the checker sees failed rises.

## 4. Data (DATA, not proof)
| set | N5 runs | states | phases with exact LEV (UNK) | in-phase fallbacks (non-honest; after an honest state) | FB-RISE (b) checks | gaps (with an inside fallback) | Q-A checks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| gap instances j10_n24, j7_n32, j8_n32 (S3), ffin12_n32, ffin5_n32, ffin4_n24 (+ .start), b5_o11, immp_cex_n11 (+ .start); budget 3·10⁶ | 8 | 227 | 6 (6) | 14 (13; 10) | 39 | 24 (3) | 2,988,812 |
| j8_n32, ffin12_n32 at budget 1.5·10⁸ | 2 | 89 | 4 (0) | 15 (14; 14) | 86 | 18 (2) | 105,864,852 |
| j7_n32 at budget 1.5·10⁸ | 1 | 51 | 0 (2) | — | — | — | — |
| lib41 minus referee games × 3 starts; budget 3·10⁶ | 1,230 | 19,562 | 417 (314) | 433 (395; 1) | 138 | 1,653 (1) | 218,336,197 |
| my 503 𝒞^1O files × 2 starts; budget 3·10⁶ | 1,006 | 17,710 | 526 (308) | 709 (660; 2) | 145 | 1,818 (1) | 334,513,822 |
| random 2 Odd choices, n 5-12 (3,000 × 3) | 9,000 | 21,090 | 1,148 (0) | 292 (1; 0) | 332 | 860 (0) | 27,787 |
| random 4 Odd choices, n 6-14 (2,000 × 3) | 6,000 | 16,464 | 614 (0) | 179 (1; 0) | 193 | 438 (0) | 18,349 |
0 violations of FB-RISE (a), (b) (and its step LEV_odd(t) ≥ LEV(h) + 1), Q-A, every gap's rise, HON-FF's bound, HON-0-FF (a)-(c), the REC-0
difference and REC-1-FF (a) in every set. Max W-honest states in a phase: 57 (x32_rand64, n = 64; bound 4n² − 3n = 16,192). Mutations (must
fail): ctrl (no LEV_odd term) 152 FAIL on lib41; b2 ((b) with LEV(h) + 2) 1 FAIL on lib41 (thin: 68 checks with one start). Logs: R2-N5-HONFF/logs/; reproduce `run_all.sh`.

## 5. Signatures
FB-RISE (a), (b), Theorem HON-FF, Corollary HON-0-FF (a)-(c), Corollary REC-1-FF (a): SIGN, on every game, under the standing SPEC premise
1E-N3 (P1 for FB-RISE; P1 and P2 for HON-FF through HON step 1). REC-1-FF (c), (d): SIGN as IMPLICATIONS from (Στ). Q-A: YES. No gap; notes
N-HONFF-1..4. REFEREE-2 successor 16 (Opus 5.5, D15).

## Addendum (13:10Z, date -u): independence record, corrected
- The independence count at the push was 1, not 0: REFEREE's docs/referee/R-N5-HONFF.md (claude/referee cce5ea5e, committed 12:39Z) was
  already on its branch when I fetched in the push turn. My commit message (05e7663c) says "0 HONFF files … at 13:06Z"; that is WRONG,
  the report's header line ("1 at 13:06Z") is right. No rebase or amend: this addendum is the correction.
- What I saw of it, and when: its file NAME (in that listing) and, AFTER my report was committed and pushed, its commit SUBJECT line in a
  `git log -1` I ran to explain the count (it summarises REFEREE's verdicts). I did not open the file. My report text, verdicts and notes
  were final at the push and are unchanged. The §C will be written only on the Lead's word.
- Log fix: logs/big_j7.txt now holds the 3·10⁷-budget run of j7_n32 (UNK 2, as the report says); logs/huge_j7.txt the 1.5·10⁸ run (UNK 2).
