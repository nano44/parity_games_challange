# C14: landing gate for RESULTS R14 (packet 11: Lemma CHANGE-NEW, F_R ≤ 3·#fired⁺(R), GAP-A ⇔ (CTX⁺) ∧ (FIRED⁺-R)) — CHECKER, 2026-10-18

Target: docs/agents/R14-draft.md at trunk f4a2439 (not edited). Branch: origin/claude/checker confirmed an ancestor of the
local branch, then trunk f4a2439 merged by merge commit.
Sources (all ancestors of f4a2439):
- GAP-A-M.md §23s (line 3313) at the pin 5909724.
- The imports, §23v (l-alg 510cb18).
- docs/referee/R-P11.md: f953548 (draft, 00:56:31Z), fc86762 (final, 01:01:19Z), and §C at abc5185 (01:14:23Z).
- docs/referee-2/R2-P11.md: aeedd00 (00:55:28Z) and §5 at bb8a625 (01:01:34Z).
- Code: Oink 8fbf0a7.

## Verdict: FAIL on one clause in (c) (E-1); everything else PASS (recommended N-1; notes N-2..N-4)
| check | verdict |
| --- | --- |
| 1 statement diff (a)-(d): "NO premise", EQUIVALENCE, (a)'s line cites | (a), (b), (d) PASS; (c) FAIL on E-1 |
| 2 gap union G-R14-1..6; G-R14-3 / §23v signature status | PASS (N-2, N-3) |
| 3 re-run (d): dtl_changenew.py both orders, pinned Oink on spp_chain_up_n43 | PASS, reproduced exactly |
| 4 against TARGET.md | PASS once E-1 is fixed |

## E-1 (required): (c) "At G′ alone (FIRED⁺-R) is implied by GAP-A but does not imply it; it is (SPP) there (GAP-A-M §23s end)"
- What both referees signed about G′:
  - REFEREE (c): "At G′ alone it is not GAP-A, but it bounds only the root's own transitions ... S can be driven by deep
    contexts with few root firings, so FIRED⁺(G′) alone does not imply GAP-A ... On chain families ... #fired⁺(G′) = S − 1,
    so at G′ it IS the search count".
  - REFEREE-2 §3: "At G′ alone, (FIRED⁺-R) is necessary and bounds the root-e* transitions ... On families where every
    transition's first difference is at the root ... it is the whole count".
  - Neither report says "(SPP)".
- The source the draft cites, "GAP-A-M §23s end", is the "Note (00:46Z)" added by l-alg 3b5c9ac ("§23s note (root FIRED+ =
  SPP)").
  - It is NOT at the pin 5909724: the pin's §23s ends at "... with no steal bookkeeping".
  - It is not refereed.
  - It is itself data-conditional: "D_{G′} ... is about S − 1 in the data ... So (FIRED⁺ ≤ |R|) at the root would give
    S ≤ |G′| + 1 per phase, which is (SPP) itself (DATA, tight ...)".
- The clause is also inconsistent within (c).
  - (SPP) gives GAP-A (R5 (k): "if (SPP) ... then A_DTL makes ≤ n(n + 2) ...").
  - So "does not imply [GAP-A]" and "it is (SPP) there" cannot both hold as identities.
- Fix: replace "; it is (SPP) there (GAP-A-M §23s end)" by the signed reading, e.g. "; on chain families where every first
  difference is at the root (spp_chain_up_n43) it equals S − 1 (both referees)". Optionally add "(L-ALG's unrefereed note,
  §23s, 3b5c9ac, relates its ≤ |R| form to (SPP) on data)".
- G-R14-4's "at G′ it is (SPP)" needs the same treatment.

## 1. Statement diff
| draft | §23s (5909724) | signed | |
| --- | --- | --- | --- |
| Object: D_R, #fired⁺(R) (region AND threshold firings), ntv(x) | §23s Setting | both | OK |
| (a) CHANGE-NEW and its proof: function of (R, p, alive T, order datum); T only appended; first differing tattr; region step by EXACT/EXACT*; threshold step by DTL-proof Lemma 1.2 | §23s Lemma; its step 1 cites STR-DET (N11-a1 fixes this); its step 3 cites the §22r Corollary (G11-a1 fixes this) | REFEREE SWG (N11-a1, G11-a1 closed); REFEREE-2 SIGN (N11-a1) | OK. The corrected proof is used |
| (b) D_R ≤ #fired⁺(R); N*_R ≤ D_R; "F_R ≤ 3·#fired⁺(R) with NO premise"; GAP-A ⇐ (CTX⁺) ∧ (FIRED⁺-R), given STR-DET | §23s Corollary | REFEREE (b) SIGN "with no premise. ✓"; REFEREE-2 (b) SIGN "with no steal premise"; joint "F_R ≤ 3·#fired⁺(R) holds unconditionally" | OK. "NO premise" is exactly what both signed (STR-DET enters only the GAP-A conditional, via R9) |
| (c) tight (41 = 41, both orders); "an EQUIVALENCE: GAP-A ⇔ (CTX⁺) ∧ (FIRED⁺-R) up to polynomial factors, given STR-DET ...; a reformulation, not a reduction to something easier" | §23s HONEST LIMIT ("close to GAP-A's core") | REFEREE (c) "That is an equivalence, not a reduction to something easier"; REFEREE-2 (c) "a reformulation of GAP-A, not a reduction of it"; joint "This is an equivalence, not a reduction" | OK on the equivalence. **E-1** on the G′ clause |
| (d) data | §23s DATA; 37,361 = 14,008 + 14,202 + 9,151 | REFEREE (d), REFEREE-2 (d) | OK (N-1) |

(a)'s line citations against the reports:
| draft | REFEREE (a) | REFEREE-2 §1 | |
| --- | --- | --- | --- |
| V rebuilt from R 648/662-667 | "asserted empty on entry (648) and rebuilt from R (662-667)" | "(852, asserted at 648) ... recomputed from R (662-667)" | OK |
| Candidates written at 714 before read at 735 | "written (714) before it is read (735)" | "written before it is read in each round (712-714)" | OK |
| Q empty on entry | drain list 488, 697, 727, 883, 918, 944, 967, 1032 | 697, 727, 883, 918, 944, 1032 | OK |
| str read only at 73 | "read only at 73" | "read only at 73" | OK |
| this->G read only at 132, changed only at 1035 | "read only at 132, and changes only at 1035" | "read at 132 ... assigned only at 1082 (start) and 1035" | OK. Within a phase only 1035 applies |
| stored 440/458-461 | "stored at 440 (tidx = tpr.size()) and 461 (tpr.push_back)" | "added only at 458-461 (push_back)" | OK. A union of both |
| tpr = −1 only at 134 | "only at 134" | "only at 134" | OK |
| G changes only at 1035, ending the phase | same | same | OK |
| threshold step: all of Z pushed at 724, Gx = R | G11-a1 "Q = all of Z (724), Gx = R" | "all of Z pushed at 724" | OK |
All match both reports.

The Lead's named points:
- "F_R ≤ 3·#fired⁺(R) with NO premise": exact.
- (c) says EQUIVALENCE / reformulation, not reduction: yes. The heading and Scope agree ("a reformulation of GAP-A, not a
  bound"). The G′ clause is E-1.
- (a)'s line cites: all match (table).

## 2. Verdict quotes, independence, gap union
- REFEREE (table plus §C): (a) SWG closed; (b) SIGN; (c) CONFIRMED; (d) CONFIRMED. This equals the draft.
- REFEREE-2 (table plus §5): (a) SIGN (N11-a1); (b) SIGN (N11-b1); (c) CONFIRMED; (d) probe. This equals the draft.
- Independence:
  - REFEREE: "docs/referee-2/R2-P11.md was not read"; §C after.
  - REFEREE-2: "not read before this report was pushed"; §5 read f953548 "after aeedd00 was pushed".
  - No REJECT.
| referee item | draft |
| --- | --- |
| N11-a1 (both) | G-R14-1 |
| REFEREE G11-a1 (= REFEREE-2 §1 in substance) | G-R14-2 |
| REFEREE-2 N11-b1, CONFIRMED by REFEREE §C | G-R14-3 |
| (FIRED⁺-R) OPEN | G-R14-4 (E-1 applies to its "(SPP)" phrase) |
| (CTX⁺) OPEN | G-R14-5 (N-4) |
| dependencies; (ACYC) | G-R14-6 |
- "Closed" applies only to G-R14-1..3; G-R14-4..5 are OPEN; G-R14-6 lists dependencies. Correct.
- G-R14-3 is checked against REFEREE §C: "R2's N11-b1 is CONFIRMED. It is the strongest consequence of the packet ...
  #(e*-at-R transitions) ≤ D_R ≤ #fired⁺(R) given STR-DET, and ≤ 2·D_R without it ... S − 1 ≤ Σ_{R∈C_bv} #fired⁺(R) +
  n(|C_T| + |C_Dom|) + 1". The draft's G-R14-3 matches. Two signatures.
- N-2 (the Lead's question on §23v). §23v (510cb18, 01:19Z) says "N11-b1 (REFEREE-2 only; REFEREE's §C pending, so ONE
  signature)". REFEREE §C (abc5185, 01:14:23Z) was on claude/referee 5 minutes earlier but not on the trunk §23v read
  (3572651), so §23v was accurate for its source.
  - R14's G-R14-3 already says so explicitly ("which marks N11-b1 as one signature, written before REFEREE §C confirmed
    it").
  - For R14 nothing more is needed.
  - For the L-ALG file, recommend that L-ALG add a one-line update to §23v (or the next import section) that §C confirms
    N11-b1, so GAP-A-M does not carry a stale "ONE signature" that a later result might cite. That is L-ALG's lane; it does
    not block R14.
- N-3. §23v's header says "its §C comparison is still pending" for REFEREE. This is the same staleness, with the same remedy.

## 3. Re-run (d)
- Pinned Oink on experiments/alg/instances/spp_chain_up_n43.pg (sha1 b9b0fd2087e13dee...): "found 1 dominions and 41
  tangles", "solved in 43 iterations", "solution verified (42 strategies)".
- experiments/alg/dtl_changenew.py, unmodified (f6a5a2d, before the pin), RM_EXCL=1 RM_LIGHT=1 RM_DV=0, on spp_chain_up_n43
  plus stealonce_viol_n76:
  | | stable | Oink | REFEREE (d) |
  | --- | --- | --- | --- |
  | CHANGE-NEW holds | 89 / 89 | 49 / 49 | 89 / 89, 49 / 49 |
  | D_R ≤ #fired⁺(R) holds; N*_R ≤ D_R holds | 53 / 53; 53 / 53 | 19 / 19; 19 / 19 | 53 / 53, 19 / 19 |
  | max D_R (#fired⁺) | 41 (41), spp_chain_up_n43 depth 0, \|R\| 43, 42 visits | 41 (41), same | 41 = 41 |
  | max D_R / #fired⁺ | 1.0 | 1.0 | — |
  Identical. "D_R ≤ #fired⁺ everywhere, root D = #fired⁺ = 41" is confirmed in both orders.

## 4. Against TARGET.md
- Heading: "partial step-4 reformulation (not M3, not a step-4 pass)".
- Scope: "an unconditional per-context bound ... and a reformulation of GAP-A, not a bound ... Gauntlet step 4 stays open".
- The only overstatement is E-1's "(SPP) there", which equates a G′-level data statement with the core conjecture as if
  proved. With E-1 fixed there is no overstatement.

## Notes
- N-1 (recommended, data line). "REFEREE p11probe.py (corpus 138 files + 2 instances, both orders, AT the first differing
  tattr) 1,160/1,160 and 1,231/1,231".
  - REFEREE's 1,160 / 1,231 are the 138-file corpus alone ("My probe on the corpus (experiments/alg/instances, 138 files)").
  - Its two-instance run is separate: 89 / 49 pairs.
  - Suggest "(corpus 138 files ...) 1,160/1,160 and 1,231/1,231; the two instances 89/89 and 49/49".
- N-4. G-R14-5's "|C_bv| ≤ S − 1 per phase, best contexts/transitions ≈ 0.5 at n = 20, 30, 40 (L-RED box 9, unpinned, in
  progress)" has no source on trunk except LEAD-STATE line 556 (an L-RED check-in). It is labelled "unpinned, in progress",
  which is honest. Fine as status.

## Fix list
Required:
- E-1: (c) replace "it is (SPP) there (GAP-A-M §23s end)" with the signed G′ reading; same in G-R14-4.
Recommended:
- N-1: data attribution.
- N-2: L-ALG to note in GAP-A-M that §C confirms N11-b1 (not blocking).
With E-1, R14 passes. I re-diff the text only.
