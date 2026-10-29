# R-N5-REL: REFEREE report on packet P-N5-REL (L-SI box 25: Lemma GATE-RISE and its Count, Theorem STATIC-DEPTH-REL, Corollary REL-SPLIT)
Referee: REFEREE (successor 17), Opus 5.5 (owner ruling D15). FIRST referee (Lead message of 2026-10-29 04:41Z by date -u).
- Object and pin: docs/si/P-N5-REL-box25.md, sha1 f79300a2d01cfb0aa27ad7214bcefbd84eafd7bb, 128 lines, author L-SI successor 21: the same sha1
  at l-si 07f19760 (an ancestor of origin/claude/l-si) and at the l-si head. Quote base b28123a58.
- Probe and data runs 2026-10-29 (date -u) between my SDPRIME §C push (04:48Z) and the report; report written 2026-10-29T04:56Z by date -u. Every
  verdict is labelled (Opus 5.5, D15).
- Independence: I opened no docs/referee-2/ file on REL. Names matching "N5-REL" at 04:53Z, in the same turn as the fetch: 0 on my tree,
  2 on origin/claude/referee-2, 0 on trunk. Names only. No lane code run or imported (experiments/si/grun/gaterise.py, relseg.py, n5x,
  quotecheck.py untouched; only the data files grun/out/rdr_K10, anc_K10 were copied, by git show at 07f19760).
- Premises read against their text: SPEC S1 (valuation, total order, Ξσ against σ̄), S2, S4a, S4c; RESULTS R15 (a), (d); R17 (a) (V1)/(V2);
  R57 (a) (VJ); R18 (d) Lemma S (a) with P2; (SW); R77 (c)'s W-MONO, Ξ-SUCC, GEN_W; R80 (a). For comparison only: RESULTS R61 (e) Lemma ALT.
- Quotes: 17 [Q path@commit:lines] passages, all in their cited ranges (own scratch/flip_quotes.py: QUOTES 17 FAILED 0, "…" read as a
  separator). Strictly 16/17 verbatim: the (SW) quote again carries a "…" for a mere line break (as N-SD-1 / SDP-N3).
- Tool: scratch/rel_probe.py (sha1 4b35aabd…; own engine rl_engine; cycles / play from depth_probe.py; start parsing from core_probe.py).
  Logs scratch/rel_logs/; inputs scratch/rel_inputs/ (rdr_K10, anc_K10).

## Verdicts (sign-off line per item)
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 | Lemma GATE-RISE: (i) u off honest cycles at t and t + 1, (ii) y2's honest t-play avoids u, (iii) Ξ_t(y1) ≠ Ξ_t(y2) ⇒ Ξ_{t+1}(u) ▷ Ξ_t(u) | SIGNED |
| §1 | its Count: CH_S(u) ≤ XR_S(u) + TIE_S(u) + CYC_S(u) + THRU_S(u); G(S) ≤ Σ_u (…) | SIGNED |
| §2 | Theorem STATIC-DEPTH-REL (REL-admissible [a, b], (H4′_rel), GEN_W): settling on V^W_b / V^H_b; σ_t = σ_b on [a + max_{Q∖T} d, b]; b − a ≤ max_{Q∖T} d ≤ |Even ∖ T| ≤ n − 1 | SIGNED, including the domain-closure sentences of the definitions |
| §3 | Corollary REL-SPLIT: |S| = Σ(b_i − a_i) + SEG − 1 ≤ SEG·n − 1 under (H4′_rel), GEN_W at every b_i; each cut is a σ̄ change on RO_{b_i} or a CW ∪ CH appearance; SEG − 1 ≤ G(S) + CF(S) | SIGNED (a REDUCTION: SEG unbounded) |
| §2 | Remark (contains STATIC-DEPTH′) | not to sign; true as stated (§2 below; data REMK) |
| §4 | data, readers, CONJECTURE SEG-RUN, READING | not signed; the reader figures reproduced (§4) |
No gap. Notes REL-N1..N5. Nothing here bounds SEG, G or CF; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays OPEN.

## 1. GATE-RISE re-derived
1. (V1) with (i) at t and at t + 1: Ξ_t(u) = u ⊕ Ξ_t(y1), Ξ_{t+1}(u) = u ⊕ Ξ_{t+1}(y2) ✓; both y1's t-play and y2's (t + 1)-play avoid u (u off its cycle) ✓.
2. τ′ := σ̄_t with u ↦ y2. By (ii) y2's honest t-play is also its (σ_t, τ′)-play, and u's is u followed by it, not returning to u; so
   V_{σ_t,τ′}(u) = u ⊕ Ξ_t(y2) ✓. (VJ) (R57 (a): Ξσ ⊴ V_{σ,τ′} for every positional τ′) gives u ⊕ Ξ_t(y1) ⊴ u ⊕ Ξ_t(y2) ✓.
3. On values of plays avoiding u, x ↦ u ⊕ x is strictly monotone and order-reflecting: same cycle node, u added to both path sets or to none
   (u ∉ either set), length + 1 on both, so the comparison is unchanged; different cycle nodes compare by reward, unchanged ✓. All values used
   here (Ξ_t(y1), Ξ_t(y2), Ξ_{t+1}(y2)) are of u-free plays ✓. With (iii) and totality: Ξ_t(y1) ◁ Ξ_t(y2) ✓.
4. R15 (a), (d): Ξ_{t+1}(y2) ⊵ Ξ_t(y2) ✓; chain ✓.
- Count ✓: the four kinds cover every σ̄(u)-change (CYC if (i) fails; THRU if (i) holds and (ii) fails; TIE if (i), (ii) hold and (iii) fails;
  else clean); a clean change is a transition at which Ξ(u) changes, counted in XR_S(u) ✓; every σ̄-changing transition has a changing u of
  out-degree ≥ 2 ✓.
- REL-N1 (relation to landed text): GATE-RISE is the strict form of RESULTS R61 (e) Lemma ALT (q ∈ Q_c, q ≠ c; "clean ... κ_{t+1}(q) ≥
  κ_t(q), with equality only if κ_t(y2) = κ_t(y1) and κ_{t+1}(y2) = κ_t(y2)"), restated in Ξ for every off-cycle Odd u and proved from R57 (a),
  R17 (a) and R15 directly. R61's entry is headed "CONDITIONAL on RESULTS R56 and R58", so a self-contained proof is useful. The packet does
  not cite ALT; it should. R61 (e)'s referees found its "q on no honest cycle at t + 1" unused. For GATE-RISE the same holds when u ≠ λ(u):
  then Ξ_{t+1}(u) = u ⊕ Ξ_{t+1}(y2) with y2's path to λ(u) avoiding u, even if u lies on the cycle (S1 measures the play up to its first visit
  of the cycle node). Not needed for any signed statement. Data: 4 changes with (i) failing only at t + 1 and (ii), (iii) holding, all with a
  strict rise (GR_CYC1).

## 2. STATIC-DEPTH-REL re-derived
- Definitions ✓. X_b is closed under "Even vertex on a member's b-play" (either frame), so every Even vertex of V^W_b ∪ V^H_b is in X_b ✓, and
  V^W_b (V^H_b) is closed under the W- (honest) successor at b ✓. T_W ⊆ V^W_b, T_H ⊆ V^H_b ✓. The recursion stays in its domains (the
  packet's sentence) ✓: for Even v ∉ T in either domain, v ∈ X_b, so both of v's b-plays are in the domains, and y = σ_b(v) lies on both ✓.
- Items 1-3 ✓ as in STATIC-DEPTH′ (my R-N5-SDPRIME §1), with two REL-specific points, both correct:
  - item 2, honest frame: an Odd v ∈ V^H_b ∖ T_H lies on the honest b-play of a member of X_b, so v ∈ RO_b, and REL-admissibility fixes
    σ̄(v) on [a, b] ✓. This is the only use of σ̄, so σ̄ may move elsewhere (data: REL_sigmabar_moves_off_RO).
  - item 1: only the cycles of CW_b / CH_b are kept, and they are exactly the cycles the domains' plays end in ✓.
- Item 4 ✓: v ∈ X_b (v ∉ T in a domain); y ∈ V^W_b ∩ V^H_b is W- and H-settled by induction; (A) uses H-settledness of y and Ξ-SUCC;
  (B) uses (A) at v, S4a elsewhere, W-settledness of y and v ∉ T_W; (C) uses that v's W-cycle at b is in CW_b (v ∈ X_b) and GEN_W at v, then
  H-settledness of y and v ∉ T_H ✓. (A)'s out-degree-1 remark ✓.
- Item 5 ✓: every v ∈ Q ∖ T is in X_b ⊆ V^W_b and settles by a + d(v) ≤ a + max_{Q∖T} d; v ∈ Q ∩ T by item 1; Even vertices outside Q have one
  successor; so σ_t = σ_b and R80 (a) gives b − a ≤ max_{Q∖T} d ✓. Distinct Even vertices outside T on a recursion path (an Even v ∉ T is one
  recursion node, dW(v) = dH(v) = d(v), so a revisit would be a cycle) ✓; T ≠ ∅ when Q ≠ ∅ ✓; Q = ∅ ⇒ no in-phase S4a step, b = a ✓.
- W-MONO and Ξ-SUCC are used on runs where λ_W may change, as in SDPRIME; settled there as a signed proof step by both referees (R-N5-SDPRIME
  §C). The same step is needed here (REL-N2).
- Remark (not to sign) ✓: σ̄ constant on all Odd vertices and all end cycles persisting ⇒ REL-admissible; the depths coincide on the domains
  (an Even vertex of V^W_b on an honest cycle is in X_b, so that cycle is its honest play's cycle, in CH_b). Data: REL's least a is never later
  than STATIC-DEPTH′'s (REMK 0 failures), and earlier in 789 (alt_all) + 495 (lib41) + 1,122 (lib1140) + 175 (readers) intervals.

## 3. REL-SPLIT re-derived
- REL-admissibility of [x, b_i] is monotone in x (for fixed b_i's sets), so a_i is well defined; the segments tile S; e − s = Σ(b_i − a_i) +
  SEG − 1 ✓; STATIC-DEPTH-REL per segment (b_i − a_i ≤ n − 1) gives ≤ SEG(n − 1) + SEG − 1 = SEG·n − 1 ✓.
- Cut a_i − 1 → a_i (i ≥ 2): [a_i − 1, b_i] fails admissibility but [a_i, b_i] passes. So either some u ∈ RO_{b_i} has σ̄_{a_i−1}(u) ≠ σ̄_{b_i}(u)
  = σ̄_{a_i}(u), a σ̄ change at that transition, or a cycle of CW_{b_i} ∪ CH_{b_i} is one at a_i but not at a_i − 1, an appearance ✓. Distinct
  transitions ✓. So SEG − 1 ≤ G(S) + CF(S) ✓.

## 4. Data (scratch/rel_logs/; 0 failures in every MUT=0 run)
| corpus | runs (fallback-free runs S) | GATE-RISE clean / TIE / CYC / THRU | REL intervals (σ̄ moves off RO_b) | SPLIT runs with hypotheses / all | cuts checked | max SEG / n |
| --- | --- | --- | --- | --- | --- | --- |
| alt_all (413 games, n ≤ 600, given start else S3) | 413 (3,286) | 3,700 / 82 / 10 / 118 | 5,385 (789) | 3,029 / 3,286 | 1,951 | 0.79 |
| lib41 (n ≤ 48; given + S3 + 1 random) | 727 (4,353) | 2,438 / 129 / 15 / 13 | 5,814 (495) | 4,279 / 4,353 | 2,210 | 0.83 |
| lib1140 (n ≤ 40; given + S3 + 1 random; two halves) | 1,857 (11,445) | 4,063 / 169 / 68 / 91 | 8,741 (1,122) | 11,229 / 11,445 | 3,077 | 0.83 (n ≥ 2) |
| readers: rdr_K10, anc_K10, runfam_K10 (given starts) | 3 (6) | 445 / 22 / 0 / 0 | 273 (175) | 6 / 6 | 24 | 0.18 |
- Per-vertex settling (SDV), σ_t = σ_b (SIG), the length (LEN) and the cap (LENcap), the Count (CNT, CNTG), REL-SPLIT's sum, cuts and
  SEG − 1 ≤ G + CF: 0 failures. Where GEN_W's used form fails (34 / 52 / 76 intervals), the conclusions still held (no overrun counters).
- §4's reader figures reproduced: runfam_K10 (n 49), rdr_K10 (n 74), anc_K10 (n 99) each run 99 transitions in one fallback-free run with
  SEG = 9; G inside the run is 9 on runfam_K10 and 91 on rdr_K10 and anc_K10 (92 σ̄-changing transitions in the whole run, one of them the
  phase-leaving transition 0 → 1). So the readers inflate G tenfold and leave SEG unchanged, as the READING says (not signed).
- §4 says "SEG ≤ 0.79n in the library": my alt_all maximum is 0.79 n, as stated; lib1140 reaches 0.83 n (REL-N4).

## 5. Mutation controls (scratch/rel_logs/mut*_lib41.txt)
| MUT | change | result |
| --- | --- | --- |
| 1 | settling demanded from a + d − 1 | BITES: SDV 15,442 |
| 2 | GATE-RISE demanded also for THRU changes ((ii) dropped) | does NOT bite (13 THRU changes, all rising) |
| 3 | GATE-RISE demanded also for TIE changes ((iii) dropped) | BITES: 128 of 129 ties without a rise |
| 4 | REL-admissible without "σ̄ constant on RO_b" | BITES: SDV 26,383, SIG 1,274, LEN 283, SPLIT 3. The σ̄ condition is needed |
| 5 | X_b := Q (no closure) | does NOT bite on lib41 (only H4rel counts change, 62 → 75) |
- Controls 2 and 5 do not bite: (ii) and the closure of X_b rest on the proof (§1 step 2; §2 item 4 needs y ∈ V^W_b ∩ V^H_b), not on data.

## 6. Notes (for L-SI's fixes file; none changes a verdict)
- REL-N1: GATE-RISE = the strict form of RESULTS R61 (e) Lemma ALT, now self-contained; cite it. (i) at t + 1 can be weakened to u ≠ λ(u)
  (§1, last bullet; 4 data cases).
- REL-N2: W-MONO and Ξ-SUCC are used beyond R77 (c)'s (H1) (λ_W may change on a run); the landing entry should carry the same signed proof step as
  SDPRIME's (R-N5-SDPRIME §C).
- REL-N3: notation clash. §2's Q := the Even vertices of out-degree ≥ 2, while elsewhere in RESULTS (R56, R71, R81) Q is the Odd choice
  vertices (and R81's K is generated by these Even vertices). Rename (e.g. Q_E) before landing.
- REL-N4 (§4, not signed): alt_all's max SEG / n is 0.79, as §4 states. On lib1140 the max over n ≥ 2 is 0.83 (si/orlens/instances/
  run_m_n24, SEG 20 at n 24); the only SEG = n case is the one-vertex game alg/instances/strfam_S1_n1 (SEG 1, trivial). The lane should name
  the library its 0.79 refers to.
- REL-N5 (quotes): the (SW) quote's "…" (as N-SD-1); 16/17 strictly verbatim.

## DONE / FINDINGS / NEEDS
- DONE: R-N5-REL.md (this file), scratch/rel_probe.py, scratch/rel_logs/, scratch/rel_inputs/.
- FINDINGS: GATE-RISE with its Count, STATIC-DEPTH-REL and REL-SPLIT all SIGNED, no gap; the σ̄-on-RO_b condition and (iii) are needed (MUT 4,
  3 bite); (ii) and X_b's closure rest on proof; GATE-RISE is R61 (e) ALT's strict form, self-contained (REL-N1); notation clash Q (REL-N3).
- NEEDS: Lead: the REL §C word when REFEREE-2 reports; route REL-N1..N5 to L-SI's fixes file.
