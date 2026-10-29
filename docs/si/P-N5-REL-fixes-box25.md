# P-N5-REL fixes (box 25): repairs only, after both reports on P-N5-REL-box25 (no gap; joint gap map EMPTY)
L-SI successor 21 (Opus 5.5; D18, Lead reading L40). Object: the frozen packet docs/si/P-N5-REL-box25.md, sha1
f79300a2d01cfb0aa27ad7214bcefbd84eafd7bb (l-si 07f19760), UNCHANGED (sha1 pinned in experiments/si/check.sh). This file changes NO signed
statement: it records the referees' notes and the lane's repairs of citations, notation and wording, as the Lead's message of 2026-10-29 05:27Z
asked («write docs/si/P-N5-REL-fixes-box25.md (repairs only, quotes pinned)»). Reports: REFEREE docs/referee/R-N5-REL.md (report 69b12910,
§C a343d6b4); REFEREE-2 docs/referee-2/R2-N5-REL.md (report eb5aa2b5, §C b6811cf1). Every [Q path@commit:lines] «…» below is a contiguous,
strictly verbatim span of its source (experiments/si/rund/quotecheck.py, pinned with a shifted-line control). Scope (D1) unchanged: structural
lemmas and a reduction inside one phase; SEG is not bounded; G-N5-TIME stays OPEN.

## Joint list (Lead 05:27Z) and repairs
| fix | note(s) | kind | repair |
| --- | --- | --- | --- |
| F1 | REL-N1 | citation | GATE-RISE is the strict Ξ-form of landed RESULTS R61 (e) Lemma ALT; cited. Hypothesis (i) at t + 1 may be weakened to u ≠ λ(u) (remark, not signed) |
| F2 | REL-N2 = N-REL-6 | citation; signed proof step | W-MONO, Ξ-SUCC at every in-phase S4a transition, λ_W not used (as P-N5-SDPRIME-fixes F1) |
| F3 | REL-N3 = N-REL-4 | notation | §2's Q (Even vertices of out-degree ≥ 2) renamed E_2 |
| F4 | REL-N5 = N-REL-1 | quote | the (SW) quote without "…" |
| F5 | REL-N4 ~ N-REL-7 | §4 data (not signed) | the start set of "SEG ≤ 0.79n" stated; higher with random starts |
| F6 | N-REL-2 | wording | step 3's injectivity is used on u-free values with a fixed cycle node |
| F7 | N-REL-3 | thin spot | hypothesis (ii) not shown necessary in data; stays a proof hypothesis |
| F8 | N-REL-5 | Remark (not signed) | "contains STATIC-DEPTH′'s length bound and its settling on V^W_b ∪ V^H_b" |
| F9 | N-REL-8 | record only | coverage beyond STATIC-DEPTH′ |

## F1 (REL-N1). GATE-RISE and RESULTS R61 (e) Lemma ALT
- Landed text: [Q docs/RESULTS.md@ab545081b:3128-3130] «(e) Lemma ALT: for an in-phase transition t → t+1 and q ∈ Q_c, q ≠ c, with y1 := σ̄_t(q) ≠ y2 := σ̄_{t+1}(q), call the change CLEAN if q
      lies on no honest cycle at t and at t + 1 and y2's honest play at t avoids q; then a clean change has κ_{t+1}(q) ≥ κ_t(q), with
      equality only if κ_t(y2) = κ_t(y1) and κ_{t+1}(y2) = κ_t(y2) (a TIE at t).» R61 is headed CONDITIONAL on RESULTS R56 and R58.
- REFEREE: [Q docs/referee/R-N5-REL.md@a343d6b4:39-41] «REL-N1 (relation to landed text): GATE-RISE is the strict form of RESULTS R61 (e) Lemma ALT (q ∈ Q_c, q ≠ c; "clean ... κ_{t+1}(q) ≥
  κ_t(q), with equality only if κ_t(y2) = κ_t(y1) and κ_{t+1}(y2) = κ_t(y2)"), restated in Ξ for every off-cycle Odd u and proved from R57 (a),
  R17 (a) and R15 directly.»
- REPAIR (citation): add to §1 "GATE-RISE is the strict form, in Ξ and for every Odd u (not only u ∈ Q_c), of RESULTS R61 (e) Lemma ALT; its
  proof here uses only R57 (a), R17 (a) and R15 (a), (d), so it does not inherit R61's conditionality on R56 and R58."
- Remark (NOT to sign): (i) at t + 1 can be weakened to u ≠ λ(u), as R61 (e)'s referees found for ALT. REFEREE: [Q docs/referee/R-N5-REL.md@a343d6b4:42-45] «For GATE-RISE the same holds when u ≠ λ(u):
  then Ξ_{t+1}(u) = u ⊕ Ξ_{t+1}(y2) with y2's path to λ(u) avoiding u, even if u lies on the cycle (S1 measures the play up to its first visit
  of the cycle node). Not needed for any signed statement. Data: 4 changes with (i) failing only at t + 1 and (ii), (iii) holding, all with a
  strict rise (GR_CYC1).» (i) at t stays: REFEREE-2's cyc control (8 of 23 CYC changes without a rise) shows it is needed.

## F2 (REL-N2 = N-REL-6). W-MONO and Ξ-SUCC where λ_W changes
- [Q docs/referee-2/R2-N5-REL.md@b6811cf1:124-125] «W-MONO and Ξ-SUCC are cited from R77 (c), landed under R77's (H1), which includes λ_W constancy. REL's runs do not fix λ_W.»
- REPAIR: identical to P-N5-SDPRIME-fixes-box25 F1 (sha1 f0bc5f45…): "Facts used as proof steps (signed by both referees): (W-MONO) W_{t+1} ⊵ W_t
  at every in-phase S4a transition (P2; R18 (d) Lemma S (a)); (Ξ-SUCC) Ξ_t(σ_t v) non-decreasing along in-phase S4a transitions (R15 (a), (d)
  and (SW)); λ_W is not used." The packet already quotes R15 (a), (d) and (SW) in its premise list.

## F3 (REL-N3 = N-REL-4). Notation: Q → E_2
- [Q docs/referee-2/R2-N5-REL.md@b6811cf1:115-116] «§2 sets "Q := the Even vertices of out-degree ≥ 2". The fleet's landed texts use Q for the ODD vertices of out-degree ≥ 2: RESULTS R56, R71,
    R80, R81, P-N5-FBC, P-N5-FBCK.»
- REPAIR: in §2-§3 read E_2 for Q throughout ("E_2 := the Even vertices of out-degree ≥ 2"; X_b is the closure of E_2; the length bound is
  max_{v ∈ E_2 ∖ T} d(v)). §1's Count sums over the Odd vertices of out-degree ≥ 2, as the fleet's Q. In the lane's tools (grun/relseg.py and
  others) the variable stays named Q; it means E_2.

## F4 (REL-N5 = N-REL-1). The (SW) quote
- [Q docs/referee-2/R2-N5-REL.md@b6811cf1:108] «The same cosmetic point as P-N5-SDPRIME (N-SD-1 = SDP-N3). 16/17 strictly verbatim.»
- REPAIR: the quote reads, strictly verbatim, [Q docs/RESULTS.md@b28123a58:3768-3769] «(SW): every Even switch of N5 is to an edge of Iσ».

## F5 (REL-N4 ~ N-REL-7). §4's SEG figure (DATA, not signed): the start set
- [Q docs/referee-2/R2-N5-REL.md@b6811cf1:127-128] «N-REL-7 (§4's SEG figure, not to sign). SEG reaches 0.95·n on lib41 with random starts (lev_l_n20), above §4's "≤ 0.79n in the library". The
  start sets differ.»
- REPAIR: §4's "SEG ≤ 0.79n in the library" means: the corpus experiments/si/runlin/out/alt_all_root.lst (413 files), default S3 starts
  (grun/relseg_alt.txt) and, separately, its pinned starts where given (grun/relseg_alt_start.txt); both give max SEG / n = 0.79. With other
  starts it is higher: REFEREE 0.83 (lib41 and lib1140 run_m_n24, SEG 20 at n 24), REFEREE-2 0.95 (lib41 lev_l_n20, random start), and the
  lane's climb 1.00 (grun/out/sg_2, SEG 29 at n 29). The DATA bound for CONJECTURE SEG-RUN is therefore SEG ≤ 1.00n (any start, all data).

## F6 (N-REL-2). GATE-RISE step 3, wording
- [Q docs/referee-2/R2-N5-REL.md@b6811cf1:109-110] «State "for u-free x with a fixed cycle node" in the injectivity sentence, and note the case of different cycle
  nodes (order kept, since u ⊕ keeps the cycle node).»
- REPAIR: step 3 reads "x ↦ u ⊕ x is strictly monotone on the values of plays avoiding u: monotone by (V2); for two such x with the same cycle
  node c it adds u to both path sets or to neither and 1 to both lengths, so the comparison is unchanged and x is recovered; for different
  cycle nodes u ⊕ keeps each cycle node, so the order (decided by the cycle nodes) is kept." Both values it is applied to, Ξ_t(y1) and Ξ_t(y2),
  are values of plays avoiding u, by (i) and (ii).

## F7 (N-REL-3). Hypothesis (ii), thin spot
- [Q docs/referee-2/R2-N5-REL.md@b6811cf1:111-112] «N-REL-3 (thin spot: (ii) unexercised as a necessity). All 239 THRU changes in my data (125 + 109 + 3 + 2) still raised Ξ(u).
  - (ii) is used in the proof (step 2's τ′-play), so it stays a hypothesis.» Recorded (lane data: 73 + 176 + 56 THRU changes, all rising).

## F8 (N-REL-5). The Remark (not signed)
- [Q docs/referee-2/R2-N5-REL.md@b6811cf1:121-122] «STATIC-DEPTH′'s per-vertex settling at vertices outside V^W_b ∪ V^H_b (e.g. a reader) is NOT a conclusion of STATIC-DEPTH-REL. The Remark
    should say "contains its length bound".»
- REPAIR (with REFEREE's §C correction): the Remark reads "STATIC-DEPTH-REL contains STATIC-DEPTH′'s length bound and its per-vertex settling on
  V^W_b ∪ V^H_b; it does not give STATIC-DEPTH′'s settling at other vertices."

## F9 (N-REL-8). Record only
- [Q docs/referee-2/R2-N5-REL.md@b6811cf1:129-131] «REL-admissible intervals outside STATIC-DEPTH′'s hypotheses, where σ̄ moves at an Odd vertex off RO_b:
  4,094 + 3,281 + 539 + 2,947 + 192. On the lane's reader instances almost every interval is of this kind (2,947 of 3,012).»

## DONE / FINDINGS / NEEDS
- DONE: this fixes file (repairs only); check.sh pins its quotes and the packet's sha1.
- FINDINGS: no signed statement changes. GATE-RISE is now tied to landed R61 (e) ALT (strict, unconditional form). The SEG data bound for SEG-RUN
  is 1.00n over all starts.
- NEEDS: none from the owner.
