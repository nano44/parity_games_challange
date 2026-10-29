# R2-N5-CORE: REFEREE-2 report on packet P-N5-CORE (box 23): (C1) EVERY-SWITCH, (C2) PHASE-SW, (C3) RISE-SW, (C4) RISE-GATE-CLEAN, (C5) FRESH-RED, (C6) FRESH3-COUNT
Referee: REFEREE-2 successor 19 (session_01V5yGRZzoAVpZvqB1LedCVF), Opus 5.5 (D15, L37). Written 2026-10-28 from 23:35Z (date -u).
Object: docs/si/P-N5-CORE-box23.md, sha1 7b66f1bae1a1b675c0fda0af1e5eaabf13f128a0 (measured with `git show <ref>:<path> | sha1sum` at l-si
081ae740, on origin/claude/l-si and on trunk 908e4333: all three equal the pin), 111 lines, frozen. Author L-SI successor 19.
INDEPENDENCE: I have not opened any file under docs/referee/ and have not run `git log` on origin/claude/referee. The only command run on that
branch is the name count `git ls-tree --name-only -r origin/claude/referee docs/referee/ | grep -ic core`: 16 at 2026-10-28 23:29:20Z (handover
check), 16 at 2026-10-28 23:44:25Z (push turn, after `git fetch origin claude/referee`). Names only. No exposure to declare.
Lane tools (experiments/si/root/corecheck.py, experiments/si/rund/quotecheck.py, experiments/si/check.sh) NOT run or imported.
Checker: docs/referee-2/R2-N5-CORE/core_check.py and qcheck.py (own; run_all.sh; logs/).
- N5 on G: my lane's SPEC loop (R2-N5-DUAL/dual_check.Runner on si.py, which is SPEC S1's own implementation, imported read-only, as in every
  REFEREE-2 checker since successor 13).
- Ξ: my own play value of (σ, σ̄) (R2-N5-RUND/rund_check.state_info), compared with the engine's valuation at every state (ENGXI, 0 differences).
- κ, κwt_c, Q, U_c, Y^q_t, A_t, D_t, DD_t, Δ, fresh edges and global C-intervals are written from the packet's §1 definitions.
- Phases: maximal runs with (λ_Ξ, τ) constant (RESULTS R38 (a)).
Scope (D1): CORE bounds nothing by itself; no bound on switches, Ξ-changes or return-only transitions per vertex or per phase is claimed.
Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Verdicts (all "(Opus 5.5, D15)")
| item | statement | verdict |
| --- | --- | --- |
| (C1) EVERY-SWITCH | every in-phase transition changes σ | SIGN |
| (C2) PHASE-SW | \|P\| ≤ Σ_w SW_P(w) | SIGN |
| (C3) RISE-SW | an Even switch at w, w off honest cycles at t and t + 1, strictly raises Ξ(w); and its Consequence | SIGN. Also true at every N5 transition, not only in-phase ones (N-CORE-1) |
| (C4) RISE-GATE-CLEAN | a clean σ̄ change y1 → y2 at u raises κ(y1), strictly unless κ_{t+1}(y1) = κ_{t+1}(y2) | SIGN. The tie exception is needed: it is used at nep22f_n64 (N-CORE-2) |
| (C5) FRESH-RED | \|I\| ≤ m_E + NOFRESH(I) | SIGN (m_E − n_E also holds, N-CORE-3) |
| (C6) FRESH3-COUNT | on a global C-interval: fresh-Even-edge ≤ m_E, fresh-Odd-option ≤ Σ (deg − 1), A-shrink ≤ Σ_c \|A_a(U_c)\| ≤ n | SIGN. Its premise is a definition from GCX, which has not landed yet (N-CORE-4) |
| quotes | 10 [Q] tags | 10/10 VERBATIM in the tagged lines (own qcheck.py; shifted-line control SHIFT=1: 0/10) |
| §6 | DATA, pointers | not reviewed for signature (not to sign); my counts are in §2, with differences noted (N-CORE-5, N-CORE-6) |
No gap. Notes N-CORE-1..6.

## 1. Proof check
### 1.1 Premises
- Every quote is checked verbatim against its tagged lines (logs/quotes.txt).
  - RESULTS @33f43c20 l. 1825-1826 (R38 (a) KEY), 631, 640 (R15 (a), (d)), 2851, 2858-2859 (R56 (a), (d)), 3768-3769 ((SW) in R72's premises).
  - SPEC @33f43c20 l. 47 (S2), 50, 56-57 (S4, S4c).
  - P-N5-FBRED-box44 @3732ab55 l. 49-50 ((Aκ)).
- I also read the cited items in context: R15 (a)-(d), R38 (a), R56's setting line and (a)-(d), FBRED §0-§1 (κ, κwt_c, Q, U_c, (Aκ), (M1κ), (M2κ)),
  P-N5-GCX-fixes F2, and SPEC S1-S5 with FIX 1-4.
- (V1) (RESULTS R17 (a)) is not in the (C3) premise list. The step Ξ(w) = w ⊕ Ξ(next w) is the definition of a valuation as a play value
  (SPEC S1 "valuation of v under (σ, σ̄)"), so nothing is missing. My data confirm the engine's Ξ equals the play value at every state (ENGXI).

### 1.2 (C1), (C2)
- (C1).
  - τ_{t+1} = τ_t inside a phase.
  - A non-fallback iteration has (σ_new, τ_new) ≠ (σ, τ), so σ_new ≠ σ.
  - An Even fallback (Iσ ≠ ∅; FIX 3: τ is kept) moves every vertex that has an improving edge to some w ≠ σ(v). Such a vertex exists.
  - An Odd fallback changes τ, so it cannot occur inside a phase.
  - Correct. The phase hypothesis is used: control X1 (σ unchanged at a transition that leaves the phase) bites 435 / 939 / 2,789 times
    (alt_all / lib41 / random k2).
- (C2): immediate from (C1). Correct. Tight (equality) in 151 of 458 phases of alt_all.

### 1.3 (C3) RISE-SW, line by line
- y ∈ Iσ_t(w) by (SW); S2 gives Ξ_t(y) ▷ Ξ_t(σ_t w). Checked as C3a and C3a2.
- Ξ_{t+1}(y) ⊵ Ξ_t(y): R15 (a) with (d). σ_{t+1} is Switch_I(σ_t) with ∅ ≠ I ⊆ Iσ_t, an unambiguous set since one edge per vertex. Checked as
  C3b, and pointwise as MONO.
- Neither play passes through w.
  - y's honest (t+1)-play: w ∉ it, because w is off the cycle of its own (t+1)-play, whose tail after w is y's play.
  - σ_t(w)'s honest t-play: the same argument at t.
  - Checked as C3c.
- The cycle nodes are equal to λ(w) at t and at t + 1, since λ_Ξ is constant on the phase. Checked as C3d.
- w ⊕ is strictly monotone on w-free values with the same cycle node c:
  - w ∉ P on either side;
  - adding w (when rank(w) > rank(c)) to both sets leaves their symmetric difference unchanged;
  - both lengths grow by 1, compared in the direction fixed by c's parity.
  - Correct.
- The Remark (the order of the steps) is right: Ξ_t(y) itself may be the value of a play through w, so the chain must compare values first
  and apply w ⊕ only to the two w-free values.
- Consequence |P| ≤ Σ_w XR_P(w) + #{on-cycle switch pairs}: correct. Each transition has a switching w by (C1). If w is off-cycle at t and t + 1,
  Ξ(w) changes, by (C3). Checked as C3cons on every phase.
- The hypothesis "off honest cycles" is needed: control X3cyc (C3's conclusion fails at on-cycle switches) bites 38 / 89 / 328 times.
- Control X3y (strict rise demanded of Ξ(y), the new successor) bites at 14,480 of 16,896 switches in alt_all. This matches the lane's MUT=1 control.

### 1.4 (C4) RISE-GATE-CLEAN, line by line
- At t, (Aκ) with next_t(u) = y1, and κ-Y-FORM_D (u ∈ Q ∩ U_c, u ≠ c, off honest cycles at t) give κ_t(y1) = min over Y^u_t of κ_t.
  - The cancellation is valid: κ takes values in Z² ordered lexicographically, an ordered group.
  - y1 ∈ Y^u_t holds automatically (u is off the cycle, so y1's t-play avoids u).
  - So CLEAN's real content is y2 ∈ Y^u_t and y1 ∈ Y^u_{t+1}.
- The same argument at t + 1 gives κ_{t+1}(y2) ⪯ κ_{t+1}(y1), using y1 ∈ Y^u_{t+1}.
- (M2κ) gives κ_t(y2) ⪯ κ_{t+1}(y2), with y2 ∈ U_c because Y ⊆ U_c.
- The chain is right, and the conclusion is exactly what it proves.
- Data: premises AK and YF checked at every state of every phase (YF 45,577 checks in alt_all); chain steps C4a-C4c; C4X (a strict κ-rise is a
  strict Ξ-rise of y1, (M1κ)). 0 violations.
- The tie exception is needed (N-CORE-2).
- (M1κ) consequence sentence and the charging remark ("at most the number of Odd u with σ̄_t(u) = y1"): correct (one rise of y1 can serve every
  u that leaves y1 at t).

### 1.5 (C5), (C6)
- (C5): fresh transitions inject into Even edges (the first switch into an edge not held at an earlier state of I, the first state included).
  - The parenthetical (non-fresh = every switching Even vertex returns to an edge held before; with (C1) there is a switching vertex) is
    checked as C5p.
  - Correct.
- (C6):
  - (a), (b): injections into (vertex, option) pairs not held at a. For Odd u there are deg(u) − 1 such options (distinct successors).
  - (c): on good transitions A_{t+1} ⊆ A_t for every class, so a vertex leaves A at most once. U_c partitions V, so Σ_c |A_a(U_c)| ≤ n.
  - Correct.
  - None of the three uses maximality of the interval, fallback-freeness or λ_W. They hold on every run of good transitions inside one phase.
    I checked both readings: maximal runs of good transitions in the phase (C6), and inside each fallback-free λ_W-constant sub-run S as in
    GCX (C6S).
  - The good-transition hypothesis is needed:
    - control X6A (A-shrink transitions over a whole phase > Σ_c |A_a|) bites 26 / 34 times (alt_all / lib41);
    - control X6Ax (A not monotone over the phase) bites 201 / 472 times.

## 2. Data (own checker; every run 0 violations)
| corpus | runs | phases | in-phase transitions (fallbacks) | (C3) checks | (C4) clean / unclean | (C5) intervals | (C6) intervals (C6S) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| alt_all (413 games, given start else S3) | 413 | 458 | 8,048 (729) | 16,825 | 3,071 / 1,075 | 86,519 | 1,187 (1,172) |
| lib41_noref × 3 starts (S3 + 2 random) | 1,230 | 1,163 | 12,135 (988) | 22,591 | 1,590 / 2,349 | 134,769 | 2,097 (2,012) |
| named (si/root/instances 7, nep90_n40) | 8 | 11 | 537 (37) | 1,160 | 396 / 33 | 2,145 | 107 (105) |
| random k2, n 6-16 (3,000 games × 3) | 9,000 | 1,467 | 1,587 (242) | 1,486 | 109 / 44 | 1,711 | 1,317 (1,120) |
| random kO, n 8-20 (1,500 × 3) | 4,500 | 753 | 824 (147) | 752 | 68 / 29 | 896 | 671 (547) |
| random k5, n 20-36 (400 × 2) | 800 | 191 | 213 (37) | 240 | 36 / 5 | 237 | 160 (130) |
| lib41 × 3, RULE=rand (random non-empty subset of Iσ, τ fixed) | 1,230 | 2,071 | 14,822 (–) | 35,118 | 9,274 / 4,090 | 166,215 | not run |
- Vacuity:
  - (C6) (b) is non-zero in 207 intervals of alt_all, (c) in 424; nearest to the bounds: Odd-option 19 of 22 (so_sorl_n32), A-shrink 40 of 46
    (xsn43_n48).
  - (C5): fresh transitions up to 0.5·m_E (b5_o11).
- Robustness under RULE=rand: (C3), (C4), (C5) hold under a random selection rule (any non-empty subset of Iσ, random improving successor),
  0 violations. They depend on no tie rule of S4. This rules out the "any deterministic rule" failure mode of G-GCX-1 / ABS-DEPTH-TIE for this
  packet.
- Unclean changes (not claimed): the conclusion of (C4) also held at every unclean change: X4u = 0 at 1,075 (alt_all) + 2,349 (lib41) + 33 (named) + 78 (random) + 4,090 (RULE=rand)
  unclean changes.

## 3. Notes (not gaps)
- N-CORE-1 ((C3) is wider than stated). (C3) holds at every N5 transition, in-phase or not.
  - (SW) and R15 (a), (d) apply at every iteration. A τ-only change leaves σ, hence Ξ, unchanged.
  - If the cycle nodes at t and t + 1 differ, the two values compare by the reward of the cycle node, which w ⊕ does not change.
  - Data: XC3, 6,863 + 21,269 + 7,392 + 5,993 + 2,626 off-cycle switches at phase-leaving transitions, 0 failures.
  - The packet's claim (in-phase) is a special case; nothing needs changing.
- N-CORE-2 (the tie exception of (C4) is used). nep22f_n64 (experiments/n5-epoch/instances, its .start), transition 8 → 9, class c = 18.
  - Clean changes at u = 9 (57 → 30) and at u = 56 (6 → 1), with all four κ-values equal to (0, 4) at t and t + 1.
  - So κ(y1) does not rise there, and (C4) without the exception would be FALSE. Under RULE=rand: 9 such cases.
  - Ties at t + 1 with a strict rise anyway: 16 (alt_all), 17 (lib41).
- N-CORE-3 ((C5)/(C6) (a) constant). Each Even vertex holds one edge at the first state, so fresh transitions number ≤ m_E − n_E. Cosmetic.
  - The bound cannot be lowered to n_E: control X5nE bites 344 times in alt_all.
  - "Held at no earlier state of I" cannot be replaced by "not held at the previous state": X5loc bites 12 times.
- N-CORE-4 ((C6)'s premise has not landed).
  - §0 heads the premise column "(all LANDED)". (C6)'s entry is "P-N5-GCX §1 (transition-local reading)", i.e. P-N5-GCX-fixes F2.
  - GCX is R76, at CHECKER (C85) and not in docs/RESULTS.md on trunk 908e4333, whose last entry is R75.
  - (C6) uses only that definition, and (§1.5) holds for every run of good transitions inside one phase, so its truth does not depend on the
    landing.
  - The packet should say "(definition from P-N5-GCX-fixes F2, signed by both referees, landing)" and "inside one phase": the classes U_c need
    a phase, and §1 does not say "of S".
- N-CORE-5 (counts differ from §6; not to sign).
  - On alt_all my in-phase transitions number 8,048, against §6's 8,084. Similarly (C3) checks 16,825 vs 16,883 and clean / unclean
    3,071 / 1,075 vs 3,077 / 1,165.
  - The cause is unknown (lane code not run; possible causes are the phase cut or the start used per game).
  - Every count is ≥ 99.5 % of the lane's except the unclean one (92 %). Neither side found a violation.
- N-CORE-6 (§6 "NOFRESH ≤ 22 per run"). Over whole phases, NOFRESH reaches 90 (long121_n40 [1, 122]; l121ereader_n41 [1, 122]).
  - So §6's "run" must be a smaller unit than a phase, e.g. a fallback-free run. This is not stated; not to sign.

## 4. DONE / FINDINGS / NEEDS
- DONE: report (this file), checker docs/referee-2/R2-N5-CORE/{core_check.py, qcheck.py, run_all.sh, named.lst, logs/}.
- FINDINGS: (C1)-(C6) all SIGN, no gap. (C3) also holds off-phase (N-CORE-1). (C4)'s tie exception is necessary (nep22f_n64, N-CORE-2).
  (C6)'s GCX premise has not landed and its scope needs "inside one phase" (N-CORE-4). The §6 counts differ slightly from mine (N-CORE-5, -6).
- NEEDS: Lead: the §C word (REFEREE's R-N5-CORE.md exists; I have not opened it); route N-CORE-1..6 to L-SI.

## §C. Comparison with REFEREE's report (written on the Lead's word of 2026-10-28 23:54Z; from 23:55Z by date -u)
Object: docs/referee/R-N5-CORE.md at origin/claude/referee 9d831869 (sha1 0e1480a3709671f395a8813fcafa6e464fd2ffd4), REFEREE successor 17.
Opened for the first time after my report was pushed (2ed8d3fb).
### C.1 Verdicts: IDENTICAL
| item | REFEREE | REFEREE-2 | joint |
| --- | --- | --- | --- |
| (C1) | SIGNED | SIGN | SIGN |
| (C2) | SIGNED, \|P\| = number of transitions (CORE-N1) | SIGN (my checker used the transition count without saying so) | SIGN, with CORE-N1's wording |
| (C3) + Remark + Consequence | SIGNED | SIGN | SIGN |
| (C4) | SIGNED; tie clause needed (CORE-N4) | SIGN; tie clause needed (N-CORE-2) | SIGN |
| (C5) | SIGNED | SIGN | SIGN |
| (C6) | SIGNED in either scope (CORE-N3) | SIGN in either scope (N-CORE-4) | SIGN |
| quotes | 10/10 | 10/10 | 10/10 |
### C.2 Joint gap map: EMPTY
Neither report has a gap.
### C.3 Notes, side by side
- CORE-N1 (|P| read as a state count makes (C2) false): ACCEPTED, MISSED by me.
  - My check compared Σ SW with b − a, the transition count, and skipped one-state phases. I never noticed the packet does not define |P|.
  - Reproduced on my engine: alt_all has 2,098 one-state phases, each with |P| = 1 > 0 = Σ SW under the state reading (counter phases_one_state
    in core_check.py, logs/alt_all.txt).
  - Joint wording: "|P| := the number of transitions of P".
- CORE-N2 (citations):
  - (a) ACCEPTED, MISSED. The R15 (d) quote at l. 640 stops at "to Even's σ"; the sentence continues at l. 640-641 «(on G) and/or with ∅ ≠ I ⊆
    Iτ to Odd's τ (on G^d)». The packet's in-phase use is right.
  - (b) AGREED. My §1.1 noted (V1) missing from the (C3) premise list but judged S1's definition sufficient. REFEREE's citation of R17 (a)
    (V1) for the recursion is the better one; I adopt it.
  - (c) AGREED, and CONTAINED in my N-CORE-1, which goes further. (C3) holds at every N5 transition, including ones where λ_Ξ changes, since
    differing cycle nodes compare by reward, which w ⊕ keeps. REFEREE notes only that the τ clause is not needed (its step 4 still uses λ
    constant). N-CORE-1 is mine alone; it is an extension and changes no verdict.
- CORE-N3 = my N-CORE-4.
  - Both reports find the scope (S dropped) and "all LANDED" points: GCX is not in RESULTS; only a definition is used.
  - REFEREE adds that the D-, DD- and Δ-clauses of goodness are unused; only "A non-increasing" is. ACCEPTED; I said only that maximality,
    fallback-freeness and λ_W are unused.
- CORE-N4 = my N-CORE-2: same instance, transition and vertices (nep22f_n64, 8 → 9, c = 18, u = 9 (57 → 30), u = 56 (6 → 1), κ = (0, 4)), found
  independently.
  - REFEREE adds that 8 → 9 is a fallback: CONFIRMED on my engine (Runner fallback flag 2 = Even fallback with Iτ ≠ ∅).
- CORE-N5 (invalid start files in alt_all.lst): ACCEPTED, MISSED by me, and it touched my data.
  - My reader (rund_check.read_start) does not validate. comp54_n80.start gives forced Odd vertex 11 the non-edge 11 → 51, and my alt_all run
    used it.
  - Re-run with validation (non-edge → first successor; counter INVALID_START_ENTRIES = 1, comp54_n80 only): every count in my §2 alt_all row
    is IDENTICAL, 0 violations. The pre-validation log is kept as logs/alt_all_v1_unvalidated.txt.
  - n3cov_lean.start has entries for the wrong owner and non-edges, overwritten or ignored. n3cov_lean and n3cov_phi leave 22 / 12 choice
    vertices unset, which my reader sets to the first successor. So those two runs are from valid but partly default starts, not the "given"
    ones.
  - Joint: route to the owners of experiments/red/n3/instances/.
- CORE-N6 (FRESH3 data): not reviewed by me (not to sign). No conflict.
- Notes of mine REFEREE does not have:
  - N-CORE-1 (above);
  - N-CORE-3 (m_E − n_E): REFEREE has the same remark inside §4, "not needed";
  - N-CORE-5 (my counts below §6's);
  - N-CORE-6 (NOFRESH 90 per phase vs "≤ 22 per run"): REFEREE's max NOFRESH is also 90, so the numbers agree.
- Controls compared:
  - REFEREE's MUT4 (goodness necessity) and MUT5 (injectivity) did not bite. My X6A bites: in 26 alt_all phases, the transitions with an
    A-shrink exceed Σ_c |A_a(U_c)|. My X5loc also bites: fresh-vs-previous-state transitions exceed m_E 12 times.
  - REFEREE's MUT6 (|I| ≤ m_E without NOFRESH) bites 40 times on l121reader_n41.
  - So the necessity of the C-interval hypothesis and of the NOFRESH term is now exhibited in data, by one referee each.
- Data scale: REFEREE ran more runs (best-reward + 1 random on alt_all, lib1140, 48,000 random); I ran given starts, RULE=rand robustness and
  random k2/kO/k5. Disjoint additions, 0 violations on both sides.
### C.4 Joint list for the lane's fixes file
CORE-N1 (|P| wording), CORE-N2 (a)-(c), CORE-N3 = N-CORE-4, CORE-N4 = N-CORE-2, CORE-N5 (start files; route to experiments/red/n3 owners),
N-CORE-1, N-CORE-3, N-CORE-5, N-CORE-6. No verdict changes.
### C.5 DONE / FINDINGS / NEEDS
- DONE: this §C; core_check.py updated (start validation, phases_one_state); logs/alt_all.txt re-run (identical counts).
- FINDINGS: verdicts identical, joint gap map empty. I missed CORE-N1, CORE-N2 (a) and CORE-N5; CORE-N5 touched my alt_all data, re-run shows no
  change. N-CORE-1 (C3 at every transition) is mine alone.
- NEEDS: Lead: route the joint list (C.4) to L-SI and CORE-N5 to experiments/red/n3's owner; word on P-N5-FBCK when REFEREE has reported.
