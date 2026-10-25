# R-N5-NEEDB: REFEREE report on packet P-N5-NEEDB (L-SI box 13: XG, ANTI (+ ANTI-Ξ / ANTI-W), NEED-β incl. A2*, OLD-THREAT, INTO ⇒ no case-(i) fallback)
Referee: REFEREE (successor 10, session_01J4kmfDqtZdanh3RSCxChyD), Opus 5.5 (owner ruling D15, Lead reading L37).
- Routing: the Lead's message of 18:10Z (Lead's stamp).
- Object: docs/si/P-N5-NEEDB-box13.md at trunk e6ee613, sha1 7471aef37f9ad2a746dbc63451a5543b3917a443 (checked with
  `git show e6ee613:docs/si/P-N5-NEEDB-box13.md | sha1sum`; identical on my tree), 253 lines. Authors: L-SI successors 7 and 8.
- Written 2026-10-25T18:45Z-18:51Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: I did not read any docs/referee-2/R2-N5-NEEDB* file. I read REFEREE-2's R2-N5-LV2 addendum (f2209fa4)
  only for its witness game and start pair (data). D1: each statement treated as wrong until its proof was checked.
- Premises re-read: P-N5-RL §0-§2 (BL-FORM, BL Steps 0, 1, 2a, 2b), RESULTS R37 (a)-(c), R41 (a) LV-SHAPE, R29 (a) (C5)-(C7), (c) OFFGATE,
  (e) NL (i)-(iii), R20 (b) FBL, R31 (d) FLAT-ALL, R40 (b) FZ, P-N5-FB §0 (C1)-(C4).
- Tools: own engine (scratch/rl_engine.py) and a new probe, scratch/needb_probe.py; no lane code (xg.py, a2star.py, oldthreat.py not run).

## Verdicts
| § | statement | label | verdict (Opus 5.5, D15) |
| --- | --- | --- | --- |
| §1 | Lemma XG | PROVED | SIGNED (note NEEDB-N1, wording) |
| §2 | Lemma ANTI (any one-player game); instances ANTI-Ξ, ANTI-W | PROVED | SIGNED |
| §3 | Corollary NEED-β, cases (B), (A1), (A2′), (A2″) | PROVED | SIGNED |
| §3 | Corollary NEED-β, case (A2*) | PROVED | SIGNED |
| §4.1 | Lemma OLD-THREAT | PROVED | SIGNED |
| §4.2 | Reduction: INTO ⇒ no case-(i) fallback | PROVED | SIGNED (note NEEDB-N2, precision; NEEDB-N3, notation) |
| §5 | CONJECTURE INTO, "THR ⇒ M ≥ 0", case (ii), the reading, dead conjectures | not to sign | not signed |
- No (P) beyond R36. Landed premises only: R15, R17 (a) F1, R18 (d), R19 (a), R20 (b), R29 (a), (c), (e), R31 (d), R36, R37 (a), (b),
  R40 (b), R41 (a). The labels are exact.
- No gaps. Notes NEEDB-N1..N4.
- IN DATA (lesson N-ENT-2; my data, §6):
  - XG's hypothesis never occurs (0 cases).
  - Setting (LV+) occurs exactly once, on REFEREE-2's witness block_9501.pg from its start pair: NEED-β case (B), and the σ*-play from x0
    uses the (β) gate (10, 8). The packet's "vacuous" line for (LV+) is out of date since REFEREE-2's addendum f2209fa4 (18:02Z).
  - NEED-β's proof gives a stronger, testable statement (§3 below), which holds at every THR fallback with r ≥ 0 that I tested (1,817 checks
    over three overlapping runs, §6).
  - A2″ and A2* never occur.
  - ANTI: 100,000 random one-player checks.
  - OLD-THREAT: post-rise states as counted in §6.

## 1. XG: checked
- (i):
  - The strategy "σ* on z's play, σ_k elsewhere on F_k" is a G_τ[F_k]-strategy with the same play from z. So U(z) ⊴ Opt(G_τ[F_k])(z) =
    W(z) (BL (c); unconditional by R36).
  - F1 gives U(z) ⊵ W(z), and Lemma G gives W(z) = Ξ(z). Correct.
- (ii):
  - y ∈ R, and H2 keeps o off its W-cycle. So y is not on its own W-cycle: if it were, o's W-play would reach y and then o. Hence
    W(y) = y ⊕ W(s).
  - z's σ*-play stays in F, so it avoids y ∈ R, and U(y) = y ⊕ U(z).
  - F1 gives y ⊕ U(z) ⊵ y ⊕ W(s). y lies on neither play, so (C7) cancels it. Correct.
- (iii):
  - Lemma G and (C7) give π_s ⊕ w ▷ π_s ⊕ θ at level exactly r. π_s ⊆ R is disjoint from P(θ), P(w) ⊆ {o} ∪ F and from c.
    If s = o, π_s = ∅.
  - So Ξ(z) ⊵ W(s) ▷ Ξ(s): a gate. (C5) with a = Ξ(s) ◁ b = W(s) ⊴ c = Ξ(z) gives level ≥ r. Correct.
- NEEDB-N1 (wording): "In particular M_k ≥ r_k" holds only when an Even y as in the hypothesis exists. The note after the proof says
  this, but the sentence reads as unconditional.

## 2. ANTI: checked
- Step 1, V_{σ_ex} = V:
  - V(z_c) = (c, ∅, ·), so z_c's σ-play reaches c through vertices ranked below c. This includes z_c = σ(c), on c's own cycle.
  - It cannot first meet another c′ ∈ T. c′'s σ-play is its own cycle, so the play would stay there and never reach c (c ≠ c′).
  - Hence every σ_ex-play keeps its prefix up to the first T-vertex c met, and then runs on a cycle through c topped by c. The value,
    measured to the first visit of the cycle node, is unchanged. Correct.
- Step 2:
  - σ_ex is a strategy of H′, and V has no improving edge in H′. At v ∉ T, H′ allows only u with V(u) ⊴ V(σ v), since v has no
    exceptional edge. At c ∈ T, everything allowed is ⊴ V(z_c).
  - R36 Lemma P1 applies to the one-player game H′, so σ_ex is H′-optimal. σ′ is an H′-strategy, so F1 in H′ gives V_{σ′} ⊴ V. Correct.
- ANTI-Ξ:
  - Gates are the Ξ-improving edges, so non-gates are allowed.
  - An (α) gate (LV-SHAPE: y is its own Ξ-cycle node) at level −1 has Ξ(σ y) = (y, ∅, ·), hence Ξ(z) = (y, ∅, ·): Ξ-exceptional.
  - G_σ̄'s only Odd choice is fixed to o → x0, and Ξ_k is σ_k's valuation there (SPEC S1). Correct.
- ANTI-W: BL Step 2a's exceptional W-improving gates match the definition. Correct.
- Data: 100,000 random one-player checks (n 3-9, five random σ′ per (H, σ)), 21,235 vertex instances with an exceptional edge,
  0 failures (needb_logs/anti.log).

## 3. NEED-β: checked
- (F-a):
  - x0 ∈ F (H1) is a free exit with o ⊕ Ξ(x0) = θ ◁ w (THR). So (o, x0) ∉ Iτ_k by BL Step 1, and U(x0) ⊵ U(t) by Step 0.
  - x0 ≠ t: x0 = t would give θ = o ⊕ Ξ(t) = o ⊕ W(t) = w.
- (F-b), (F-c): (C7) through o, then (C5) with Ξ(x0) ◁ W(t) ⊴ U(x0). Correct.
- The case split is exhaustive, as stated. (A2″) is applied whenever rank m_K > rank m′, wherever m′ lies.
- (B): 𝒫 avoids o, so it is a G_σ̄-play. ANTI-Ξ for σ′ gives U(x0) ⊴ Ξ(x0), against (F-c). Correct.
- (A1):
  - 𝒬 avoids λ ∪ {o}: otherwise o would lie on 𝒫's cycle.
  - U(t) = W(t) by ANTI-Ξ on 𝒬 and F1.
  - σ″'s G_σ̄-play from x0 is the cycle K = λ ∪ {o}, through σ̄'s edge o → x0. So rew(m_K) ≤ rew(c).
  - m_K ≠ c: c ∈ λ would make 𝒬 (cycle node c, by H3) meet λ. And o ≠ c by H1.
  - U(x0) = K ⊕ W(t), because K is disjoint from 𝒬 ⊇ P(W t). (F-a) then forces rew(m_K) > rew(c), in both sub-cases (a high vertex
    in K, or a length-only comparison). Contradiction. Correct.
- (A2′):
  - m′ ∈ K, so rank m_K ≥ rank m′.
  - If m_K = m′, the two reward inequalities force m′ = c ∈ λ. Then
    - U(t) = (c, ∅, ·) ⊵ W(t), so wt(P(W t)) ≤ 0;
    - σ″ gives wt(P(Ξ x0)) ≥ 0;
    - and (F-b) at level r ≥ 0 gives wt(P(W t)) > wt(P(Ξ x0)), because a level ≥ 0 is a path-set difference.
    Contradiction. Correct.
- (A2″):
  - m_K lies on λ before the re-entry vertex.
  - P(U x0) has top m_K and P(U t) = ∅, so (F-a) makes m_K even.
  - rew(m_K) ≤ rew(c) then forces c even with rank c ≥ rank m_K > rank m′, against rew(m′) ≥ rew(c). Correct (also when m_K = c).
- (A2*):
  - Step 1: both values have cycle node m′ and empty path sets. ℓ_{x0} = |λ| + 1 + ℓ_t > ℓ_t, so the longer one is ⊵ only if m′ is odd.
  - Step 2: if m′ ≠ c, rew(c) < rew(m′) = −pp(m′) forces c odd and above m′.
  - Step 3: σ″ gives rew(m_K) ≤ rew(c). But m_K < m′ ≤ c in rank and c is odd, so rew(m_K) > rew(c).
  - Correct. The Remark is right: the "no (β) gate" assumption enters only through σ″ and ANTI-Ξ.
- NEEDB-N4 (a stronger statement the proof already gives; DATA, not a requested change). The proof uses M_k = −1 only to know that every
  gate is (α) or (β) (LV-SHAPE).
  - Read with "non-gate or Ξ-exceptional gate" in place of "non-gate or (α) gate", the same proof gives this. At every in-phase THR S4c
    fallback with (h) and r_k ≥ 0, 𝒫 uses an edge (y, σ*(y)) that is a gate and not Ξ-exceptional.
  - Every step goes through: (F-a)-(F-c) need only THR with r ≥ 0 and BL Steps 0-1; ANTI-Ξ allows exactly those edges.
  - In (LV+) this is NEED-β.
  - Unlike (LV+), this statement is exercised in data: §6.

## 4. OLD-THREAT and the reduction: checked
- OLD-THREAT, FREEZE:
  - (h) at every source in S.
  - (A_{k0+1}) by OFFGATE (gates at k0 + 1 into F have level ≤ M_{k0} = L), then NL (iii) at each S4a step with r_s > L.
  - NL (ii) (R_s ⊆ R̄_{s+1}) gives F_{s+1} ⊆ F_s, so x ∈ F_t puts x in F_s for s ∈ [k0 + 1, t].
  - FLAT-ALL (iii) across k0: M_{k0} = L ≥ 0, and (h) at k0 + 1, because k0 + 1 ≤ j < t is a source in S. Also THR at k0, because
    r_{k0} ≥ r_{k0+1} > L (Fact R).
  - NL (i) at each step. This is FZ's chain with the end state t. Correct.
- OLD-THREAT, SANDWICH and MONOTONICITY:
  - x's play avoids o at t, so it is the same under every Odd choice. Lemma S (a) with o → x gives θ_t ⊴ o ⊕ Ξ_t(x).
  - (C1) and (C4) (or (C7) with (C2)) give COARSE_L(θ_t) ⊴_L COARSE_L(θ_{k0}).
  - The rise at j < t is strict ((C1), (C3)), and monotone ever after. Contradiction. Correct.
  - The k0-threat qualifies because θ_{k0} = o ⊕ Ξ_{k0}(x_{k0}) ((V1) at o, H1).
- Reduction:
  - A case-(i) fallback k has (h), r_k > L ≥ 0: THR with u* ≠ none. FBL (R20 (b), strong form) excludes every gate into R̄_k, so INTO
    fails at k.
  - Correct, with two notes:
    - NEEDB-N2 (precision): "k is a post-rise state" needs every transition strictly between k0 and k to be an S4a step. So k must be
      the FIRST fallback of S after k0 (it is after j, since the rise setting has no fallback in (k0, j)). The reduction still covers
      every case-(i) fallback: if any later fallback has r > L on [k0 + 1, k], so does the first one, and that one is post-rise. One
      line in the fixes file.
    - NEEDB-N3 (notation): R20 (b) states FBL as "no F→R and no R→R gate edge" in R19's notation, where R = "the vertices whose current
      play reaches o", o included, i.e. today's R̄. So the packet's "no F → R̄ and no R → R̄" is the landed statement. It holds at a
      single THR state with r ≥ 0 (as in R29 (f)'s CLS-3 note).

## 5. Not signed
- §5: CONJECTURE INTO (my data: 52 post-rise states with r > L, 0 violations; 0 case-(i) fallbacks), CONJECTURE "THR ⇒ M ≥ 0", case (ii), the reading, and the FALSE conjectures RISE-DROP,
  GATE-ABOVE, FEED (instances not re-run here; not used above).
- Nothing here is a running-time bound for N5, a TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN.

## 6. Data (DATA, not proof; scratch/needb_probe.py on rl_engine, logs scratch/needb_logs/)
File sets:
- (L) P-N5-RHO's 412-file list: 253 𝒞^1O games. Run from SPEC S3's start, then with 4 uniformly random start pairs per game (RANDSTARTS=4;
  1,012 extra runs).
- (R2) the 145 𝒞^1O game files under docs/referee-2/*/climb/ (REFEREE-2's climb outputs, used as inputs), from SPEC S3's start.
- (W) REFEREE-2's R2-N5-LV2/climb/{block_9501, best_*}.pg and experiments/red/so/instances/beta2_n11.pg, with 200 random start pairs
  each (1,400 runs).
- block_9501.pg (sha1 1b5b76fd) from its own start pair (block_9501.txt).

| check | (L) + 4 random starts | (R2) | (W) random starts | block_9501 own start | failures |
| --- | --- | --- | --- | --- | --- |
| THR in-scope fallbacks with r ≥ 0 (F-a, F-c checked at each) | 985 | 398 | 434 | 1 | 0 |
| NEED-β general form (NEEDB-N4): σ*-play from x0 uses a non-exceptional gate; cases B / A1 / A2′ / A2″ / A2* | 473 / 361 / 151 / 0 / 0 | 274 / 93 / 31 / 0 / 0 | 434 / 0 / 0 / 0 / 0 | 1 / 0 / 0 / 0 / 0 | 0 |
| setting (LV+) (M = −1, r ≥ 0): NEED-β with a (β) gate on 𝒫 | 0 | 0 | 0 | 1 (gate (10, 8)) | 0 |
| XG hypothesis (y ∈ R, σ*(y) ∈ F with its play in F; also the alternative optimal choices) | 0 | 0 | 0 | 0 | — |
| rises; post-rise states; OLD-THREAT exit checks | 62; 75; 377 | 17; 56; 133 | — | — | 0 |
| INTO (counted, conjecture): post-rise states with r > L; violations | 13; 0 | 39; 0 | — | — | — |
| case-(i) fallbacks (FBL checked there) | 0 | 0 | — | — | — |

- ANTI: 100,000 random checks, 0 failures (§2).
- Logs: needb_logs/{anti, lib, lib_rand4, r2climbs, W_rand200, block_9501_ownstart}.log.
- Thin:
  - XG's hypothesis is VACUOUS in my data too.
  - (LV+) occurs once, case (B) only.
  - A2″ and A2* never occur, even in the general form. So the A2 sub-arguments rest on their proofs, which I checked line by line.
  - My OLD-THREAT sample (131 post-rise states) is smaller than the lane's (562).

## §C. Comparison with REFEREE-2 (R2-N5-NEEDB.md, referee-2 ef433d32, REFEREE-2 successor 12) (Opus 5.5, D15)
Written 2026-10-25T22:08Z by date -u, by REFEREE successor 11 (session_01VH2ckvgGP9CGkb8Suno5f1). Routing: the Lead's message of 22:04Z
(Lead's stamp). My report above (successor 10, referee 008ad8ab) was pushed before I opened R2-N5-NEEDB.md. Object unchanged: both
reports checked docs/si/P-N5-NEEDB-box13.md, sha1 7471aef3, at the pin e6ee613(0).

### C.1 Verdicts: identical
| statement | REFEREE | REFEREE-2 |
| --- | --- | --- |
| §1 Lemma XG | SIGNED (NEEDB-N1 wording) | SIGN (N-NEEDB-4 DATA) |
| §2 Lemma ANTI; ANTI-Ξ, ANTI-W | SIGNED | SIGN |
| §3 NEED-β (B), (A1), (A2′), (A2″) | SIGNED | SIGN (N-NEEDB-1 status) |
| §3 NEED-β (A2*) | SIGNED | SIGN |
| §4.1 OLD-THREAT | SIGNED | SIGN (N-NEEDB-3 citation) |
| §4.2 INTO ⇒ no case-(i) fallback | SIGNED (NEEDB-N2, NEEDB-N3) | SIGN (N-NEEDB-2 wording) |
| §5 | not signed | not signed (N-NEEDB-5 FINDING on a §5 CONJECTURE) |
Neither report has a gap. No statement is NOT SIGNED by either.

### C.2 Joint note map (one fixes-file line per row)
| REFEREE | REFEREE-2 | ruling |
| --- | --- | --- |
| NEEDB-N2 (the case-(i) fallback must be the FIRST fallback of S after k0; a later one implies the first is case (i)) | N-NEEDB-2 (read "case (i)" as the NEXT fallback of S after k0) | SAME finding. Fixes line: "k := the next fallback of S after k0". |
| "IN DATA" line: (LV+) occurs once, block_9501 from its start pair; the packet's "vacuous" row is out of date since f2209fa4 | N-NEEDB-1 (status: (LV+) is non-empty, witness exercised) | SAME. Fixes line: replace the "vacuous" row by the witness (block_9501.pg sha1 1b5b76fd + block_9501.txt). |
| NEEDB-N3 (FBL's landed R is today's R̄; the packet's "no F → R̄, R → R̄" is the landed statement) | stated in R2's background (P-N5-XA's R_k contains o) and used in §4.2 | SAME reading; wording only. |
| NEEDB-N1 ("In particular M_k ≥ r_k" holds only when such a y exists) | — | REFEREE only; wording. Stands. |
| NEEDB-N4 (general form: at every THR in-scope fallback with r ≥ 0 the σ*-play from x0 uses a non-exceptional gate; 1,818 checks, 0 failures) | RECORD in §3 DATA: at all M ≥ 0 in-scope THR r ≥ 0 fallbacks the σ*-play from x0 uses an R → F gate | Compatible; REFEREE-2's record is a stronger data statement (an R → F gate is in particular not Ξ-exceptional). Neither is a signed claim. |
| — | N-NEEDB-3 ((C4), not (C7), passes equal COARSE_L values through o ⊕ in the sandwich) | ACCEPTED. (C4) (P-N5-FB §1; R-N5-FB §1.1) says COARSE_L(u ⊕ x) is a function of u and COARSE_L(x), which is the step used. Citation only. |
| XG vacuous in my data (0) | N-NEEDB-4 (DATA: XG's hypothesis reached 7 times in climb 12004; witness_xg_12004.pg sha1 89d9085b) | ACCEPTED as REFEREE-2's data, NOT REPRODUCED by me (C.4). |
| — | N-NEEDB-5 (FINDING: §5 CONJECTURE "in scope, THR ⇒ M ≥ 0" FALSE on block_9501 from its saved start pair) | CONFIRMED on my engine (C.3). |

### C.3 N-NEEDB-5 re-checked on my own engine: the CONJECTURE "in scope, THR ⇒ M ≥ 0" is FALSE as stated
- Tool: scratch/needb5_check.py (rl_engine / rl_probe only; no REFEREE-2 or lane code). Log: scratch/needb_logs/needb5_check.log.
- Game docs/referee-2/R2-N5-LV2/climb/block_9501.pg, sha1 1b5b76fd986487549fe0a35da79f68f5f0d19b3f (checked), o = 7. Start pair from
  block_9501.txt: σ0 = [9, 2, 9, 1, 0, 5, 2, 8, 3, 5, 7], τ0 = [9, 2, 9, 1, 0, 5, 2, 5, 0, 5, 3]. 5 states, one fallback, at state 1.
- State 1, on my engine: (h) holds; θ = (5, {9}, 3) (mask 1024 = rank 10) ◁ w = (5, ∅, 1): THR; r = 10 ≥ 0; M = −1; in phase with
  state 2, H2 at 2, w_2 = w_1: in scope. Its gates are (10, 1), (10, 3), (10, 8), all of level −1, all with y ∈ R and z ∈ F: (β).
  rank o = 2 < rank c = 9 (c = 5). This is exactly the counterexample shape that N5-LV3-box12.md §4 (sha1 20ba05d7) writes down.
- The CONJECTURE (N5-LV3 l.157, P-N5-NEEDB §5) has no start-pair restriction. SPEC S3 reads "Start (unless a start pair is given)",
  and N5-LV3 §5's own data use perturbed start pairs ("SPEC allows a start pair"). So the conjecture as stated is FALSE.
- From SPEC S3's own start the same game has 4 states, one fallback at state 0, and no in-scope THR fallback with r ≥ 0 and M < 0.
  A "from the S3 start" form is not refuted by this instance (REFEREE-2 says the same). That form is not what the lane stated.
- Nothing signed depends on the conjecture: P-N5-NEEDB §5 is not signed by either referee, and NEED-β holds at this state (case B, the
  σ*-play from x0 uses the (β) gate (10, 8): my predecessor's run, §6 table, needb_logs/block_9501_ownstart.log).
- Recommended record (the Lead's call): DEAD (L-SI docs/si/DEAD.md) for "in scope, THR ⇒ M ≥ 0" as stated, with this instance and start
  pair; the S3-start form, if the lane keeps it, as a new CONJECTURE.

### C.4 N-NEEDB-4's witness does not reproduce on my engine as saved
- witness_xg_12004.txt gives the start pair of the climb SEED (block_9501's). It is NOT a strategy pair of witness_xg_12004.pg: 10 of the
  11 entries are not successors of their vertex (e.g. vertex 1 Even, σ0(1) = 2 ∉ succ(1) = {5, 7}). My probe cannot run from it.
- On my engine, witness_xg_12004.pg from 2,000 uniformly random start pairs (needb_probe.py RANDSTARTS=2000; log
  needb_logs/witness_xg_12004_rand2000.log): XG's hypothesis 0 times (XG and XGalt); (LV+) 219 times, all case B; 0 failures.
- REFEREE-2 says its count needs the climb's own evaluate(…, "lv", 12004) (its rng and its choice among optima). XG's hypothesis depends
  on which optimal σ* is taken, so a mismatch is possible without either engine being wrong. Not a gap: XG is SIGNED by both on its proof.
- Fixes-file line asked: save the start pair actually used for the 7 XG cases (or the optimum chosen), so the witness can be re-run.

### C.5 Result
- P-N5-NEEDB: every statement to sign is SIGNED by both referees, no gaps. Notes for the fixes file: NEEDB-N2 = N-NEEDB-2 (next
  fallback), N-NEEDB-1 (witness replaces "vacuous"), N-NEEDB-3 ((C4)), NEEDB-N1, NEEDB-N3 (wording), C.4 (witness start pair).
- FINDING outside the signed set: the §5 CONJECTURE "in scope, THR ⇒ M ≥ 0" is FALSE as stated (C.3), confirmed by both referees on
  independent engines.
- Not a running-time bound, not a TARGET.md claim, not a step-4 pass. G-N5-TIME stays OPEN.
