# R-N5-FIXD-C: REFEREE §C on P-N5-FIXD: cross-map against REFEREE-2 (R2-N5-FIXD, claude/referee-2 4a960ef9), and my check of its FLAT-SW proof
Referee: REFEREE (successor 20), Opus 5.5 (D15).
- The Lead gave the §C word at 16:34Z (read 16:44Z by date -u). I opened docs/referee-2/R2-N5-FIXD.md @ 4a960ef9 (143 lines) only after that
  word, and after my report R-N5-FIXD.md (2c9d8040) was pushed.

## 1. Cross-map
| item | REFEREE (R-N5-FIXD) | REFEREE-2 (R2-N5-FIXD) | joint reading |
| --- | --- | --- | --- |
| §2 FIX-DEPTH / FIXD-MON | SIGNED | SIGNED | agree |
| §3 PHASE-RED | SIGNED | SIGNED | agree |
| §4 PHASE-RED′ (implication) | SIGNED | SIGNED | agree |
| line: k unbound in the PHASE-RED′ hypothesis | FIXD-N1 | L-1 (REQUIRED) | same finding, same fix |
| line: P bound inside the hypothesis's parenthesis, used in the conclusion | MISSED | L-2 (REQUIRED) | I agree; I missed it. This is my handover's "binder in another clause" pattern again |
| line: standing SPEC premise of R57 absent | FIXD-N2 | not raised | I keep it. R92 and R93 carry the clause verbatim, and MON / SW-KEEP use Ξ_σ = Ωσ. REFEREE-2 treats the gloss «Odd's optimal counterstrategy σ̄_t» as enough (its L-3 discusses that gloss) |
| line: τ → τ_t | not raised | L-3 (optional) | agree, optional |
| line: cite R93 (a) | FIXD-N4 | not raised | wording only |
| DATA label «6568 of 16183 Ξ-changing» | FIXD-N3 | N-2 | same finding |
| sharper constants: n(n + 1) K-rises (λ_Ξ constant ⇒ DEPTH ≥ 1), 2n(n − 1) Ξ-unchanged run via R15 (c) | not raised | N-3 | both are correct (I re-derived them). Precision only |
| comp54_n80.start | totals unreconciled | N-1: «invalid start», corrected totals 6475 / 9596 | see §2 |
| FLAT-SW | proved (SW-KEEP: R15 (a) + R57 pointwise optimum + a lasso argument) | proved (§5: Lemma OWN + R91 SW-IN's argument) | two independent proofs; §3 |

## 2. DATA: the comp54_n80 start, and my totals
- comp54_n80.start gives «11:51». Vertex 11 is ODD (owner 1; «11 134 1 11;»), so this is τ(11), not σ(11). Its only edge is 11 → 11.
- My parser (core_probe.parse_start) prints «NOTE … forced vertex 11 -> 51; using 11» and runs from the repaired start: τ(11) := 11, every
  other entry as given. That is a valid start pair.
- From it my engine gives 55 iterations, K-rise 22 and FLATTR 32: the lane's numbers exactly. So the lane's comp54 run coincides with a
  genuine N5 run from the repaired start, and the lane's totals (9615 / 6503) are totals of genuine runs.
- REFEREE-2's corrected totals (9596 / 6475) use a different valid choice: the default start for comp54. Both are right for their run sets.
  N-1 is a start-FILE defect, not invalid data. Either way FLAT-SW has 0 exceptions.
- My own gap of 6460 vs 6503: fixd_probe.py's default MAXN 200 skipped 4 games (switchbestexp_8, fc_8, leanT_N32, n3cov_phi) whose FLATTR
  totals 15 + 13 + 4 + 7 + 4 = 43. leanT_N32 sits in both lists, so it is counted twice. 6503 − 43 = 6460. Per game, every other run equals
  the lane's count (box79/flatsrc_*.txt). R-N5-FIXD §5's run-set note is hereby resolved.

## 3. REFEREE-2 §5: Lemma OWN and Corollary FLAT-SW (strong form): my independent check
- Lemma OWN: SIGNED (Opus 5.5, D15). I checked it against the procedure text of SPEC S1 (docs/new/N5-ssi-global.md l. 33-44).
  - Fact 0 ✓: a vertex is its own cycle node iff it is alive at its own turn and passes (i).
  - Fact 1 ✓: an alive x ∈ X ∖ {v} that reaches a cycle node v would be put in R(v) with cycle node v.
  - (ii) ✓: walks to v stop at the first visit, so they never use v's out-edges, and avoid X ∖ {v}.
  - (iii)-(iv) ✓: M for Even u (reaching v without u) and for Odd u (reaching u without v) never use v's out-edges. The longest / shortest
    recursions are anchored at v.
  - (vi) ✓.
  - Note FIXD-C1 (exposition, not a gap): in (i) and (v), DFS from v may enter some x ∈ X, and x's subtree is explored differently in the
    two runs. The conclusion still holds: every vertex reachable from x fails to reach v through allowed vertices (else x would, against
    Fact 1). So the visited marks left by x's subtree never block a walk to v, and «the first successor on a DFS-found cycle» is in both runs
    the first successor in list order from which v is reachable. The report states only «avoids the out-edges of X»; this sentence closes it.
  - Independent DATA (own S1 implementation rl_engine.evaluate; docs/referee/scratch/own_check.py, seeds 1, 2, 6000 trials each):
    1963 pairs satisfying the hypothesis, 0 violations, Odd choices included. Control «own cycle node under σ only»: 3927 / 3927 pairs differ.
- Corollary FLAT-SW (strong form, in-phase): SIGNED.
  - λ_Ξ is constant on the phase (R38 (a)), so each switched x is its own Ξ-cycle node at both states or at neither.
  - All at both: OWN gives Ξ_{k+1} = Ξ_k.
  - Otherwise some x is at neither. Its new target w has (x, w) ∈ Iσ_k (S4a / S4c). x ⊕ · is strictly monotone on values with the common
    cycle node λ_Ξ(x), and x is in neither path set. So Ξ_{k+1}(x) = x ⊕ Ξ_{k+1}(w) ⊵ x ⊕ Ξ_k(w) ▷ x ⊕ Ξ_k(σ_k x) = Ξ_k(x) (MON at w; the
    improvement).
  - This is the argument of R91 (i) SW-IN, as REFEREE-2 says. The cycle node of Ξ_k(w) is λ_Ξ(w) at k, which equals the one at k + 1.
- Comparison with my SW-KEEP:
  - SW-KEEP holds at EVERY σ-changing transition (it does not need λ_Ξ constant) and proves only Ξ-equality, through pointwise optimality.
  - OWN is a statement about S1's procedure. It gives equal Odd choices too, needs no improvement hypothesis, and does not use the R57
    premise for that step.
  - Both give FLAT-SW. REFEREE-2's strong form also gives a strict rise of some switched x at every Ξ-changing in-phase transition.
    SW-KEEP's step (1) gives the same strict rise for the non-own-cycle-node switch (by injectivity, plus R15 (a) at the successor).
- So FLAT-SW now has two independent proofs, each checked by the other referee once REFEREE-2 reports on SW-KEEP. PHASE-RED′ can be stated
  unconditionally in a revised line. That line must carry FIXD-N2's premise clause: SW-KEEP uses it, and so does SW-IN's R15 (a) step.

## 4. Line revision L-2 (l-new 9460f011, docs/new/P-N5-FIXD-box91-line-L2.txt, sha1 d553bbba9a996d5d400efa0bdd53947785ffd5f7)
- Word-diff against the frozen line ba09dd26 (`git diff --no-index --word-diff=porcelain`). The changed tokens are exactly:
  - «revision L-2» in the label;
  - «, under the standing SPEC premise of RESULTS R57» (my N2);
  - «R93 (a) (Fact LEX, COMMON PREFIX)» (my N4);
  - «τ_t» (REFEREE-2 L-3);
  - «every transition k → k + 1 counted in FLATTR_P … has an Even vertex x switched at k» (my N1 = REFEREE-2 L-1);
  - «then every phase P has» (REFEREE-2 L-2).
  Nothing else changed.
- Strict symbol test on the new tokens: k bound by «k → k + 1»; P in the conclusion bound by «every phase P»; R57 and R93 (a) are landed
  labels; τ_t bound by «states (σ_t, τ_t)». No free symbol remains.
- Verdict: L-2 MATCHES §2-§4 and every note of both referees (Opus 5.5, D15).
- Open for a later revision, not a defect of L-2: once REFEREE-2 signs SW-KEEP, FLAT-SW is two-referee proved. Then «(CONJECTURE FLAT-SW,
  not proved here)» and «FLAT-SW is a conjecture» become stale, and PHASE-RED′ can be stated unconditionally, as the Lead planned.

## 5. Line revision L-3 (l-new 59d58d0d, docs/new/P-N5-FIXD-box91-line-L3.txt, sha1 7d22165a7e0cbd1a556cb546d8d3c53efa640956; fixes file sha1 eb3bd874bb91da35a901a14d1bfadb496c2c34f9)
- Word-diff against L-2 (d553bbba). The changed tokens are exactly:
  - the label «L-3»;
  - «(Corollary PHASE-RED′, an implication) if» → «(Theorem FLAT-SW, proof of record Theorem SW-KEEP (REFEREE R-N5-FIXD §4b, claude/referee
    2c9d8040; signed by REFEREE-2 R2-N5-FIXD-C §C.4, claude/referee-2 73d44f3b), from RESULTS R15 (a), (d), the standing SPEC premise of
    RESULTS R57 and R93 (a))»;
  - «every transition k → k + 1 of every N5 run at which Ξ changes at some vertex, in particular every transition counted in FLATTR_P for
    any phase P, has an Even vertex x switched at k with Ξ_{k+1}(x) ≠ Ξ_k(x); and (Corollary PHASE-RED′) every phase P has …»;
  - the tail «FLAT-SW is proved by a referee-originated proof, SW-KEEP, signed by both referees».
  Nothing else changed.
- (b) The clause states exactly what SW-KEEP gives, and no more.
  - It claims only transitions at which Ξ changes. Ξ_t := Ξ_{σ_t} (bound in the line), so every such transition has σ_{k+1} ≠ σ_k.
  - By R15 (d), every σ-change of N5 is Switch_I with ∅ ≠ I ⊆ Iσ_k, one edge per vertex (S4a's σ_new, or the S4c fallback). That is
    SW-KEEP's hypothesis, and the clause is SW-KEEP's contrapositive.
  - A transition that changes only τ leaves Ξ unchanged, so it is not claimed. No transition without a σ-change is claimed.
  - «in particular every transition counted in FLATTR_P» ✓: FLATTR transitions are Ξ-changing by definition.
- The premises named in the clause are exactly SW-KEEP's:
  - R15 (a), in (1b) and (4);
  - R15 (d), for the form of N5's switches;
  - the R57 premise, in (4) and in Fact F's realising strategy;
  - R93 (a) COMMON PREFIX, in (2).
- REFEREE-2's signature exists: R2-N5-FIXD-C.md @ 73d44f3b, §C.4 «Theorem SW-KEEP (REFEREE §4b): SIGNED (Opus 5.5, D15)» (l. 58).
- Strict symbol test on the new tokens:
  - k is bound by «k → k + 1»; P by «for any phase P» in FLAT-SW and by «every phase P» in PHASE-RED′;
  - «switched at k» is defined in the parenthesis; FLATSW_P(x) is unchanged;
  - SW-KEEP, R2-N5-FIXD-C and the two SHAs are references, not symbols.
  - No free symbol.
- PHASE-RED′ is now a corollary of PHASE-RED and FLAT-SW. The packet's §4 proof applies verbatim with the hypothesis discharged.
- Verdict: L-3 MATCHES the packet's §2-§4 plus the two-referee-signed FLAT-SW (Opus 5.5, D15). No required change.

## DONE / FINDINGS / NEEDS
- DONE: this §C; own_check.py.
- FINDINGS:
  1. FIXD: both referees SIGN §2-§4; joint line fixes L-1 (= N1) and L-2 (my miss), plus my N2 (premise) and N4. REFEREE-2's L-3 and N-3
     are optional.
  2. REFEREE-2's Lemma OWN and its FLAT-SW strong form are SIGNED by me (exposition note FIXD-C1).
  3. comp54: the lane's run equals a genuine run from the repaired start (τ(11) := 11). My 6460 is fully explained (MAXN skipped 43).
- NEEDS: Lead: L-2 MATCHES (§4). The next revision (unconditional PHASE-RED′, after REFEREE-2 signs SW-KEEP) needs a word-diff from me
  when it is frozen.
