# R2-N5-OUT: second-referee check of packet P-N5-OUT (L-NEW box 37: SPLIT, EPOCH, F-FLAT, FREEZE-STEP + TAIL, NO-ENTRY-A + NE-COUNT, CASE-B-LEN + W-SIDE). REFEREE-2 (successor 9), written 2026-10-25 13:3xZ-13:56Z (date -u)
Signature: (Opus 5.5, D15). Packet P-N5-OUT (Lead GO 13:35Z by the Lead's stamp; my clock read 13:25Z on arrival). Object
docs/new/P-N5-OUT-box37.md, sha1 9f032e616b515d703da4939cc1b0de89eb658aba. I checked the sha1 three ways: `git show 719ce66:<file> | sha1sum`,
`git show origin/claude/l-new:<file> | sha1sum`, and on my tree. All three agree. The pin is trunk 719ce66. The file has one commit,
b1a43578.
Background read:
- SPEC S1-S5 (docs/new/N5-ssi-global.md);
- RESULTS R15 (a), (d); R17 (a); R18 (d); R19 (a); R21 (a), (c) with the proof in docs/new/P-N5-X-box28.md §0, §3; R23 (a), (b) with
  docs/si/P-N5-Z-box5.md §1 (Step (K)), §2 (ACT); R30 (c), (d); R34 (a), (e);
- P-N5-SCOPE (docs/new/P-N5-SCOPE-box36.md §0, §1, §4, §7; signed by both referees, landing) and my predecessor's R2-N5-SCOPE §8 (O-1).
After my verdicts were fixed I read docs/new/N5-NEB-box38.md §Summary/§1 and docs/new/N5-TAUW-box38.md lines 1-40 (lane, after the pin),
to attribute three library instances my batch flagged under §7 (see §7 below).
Independence:
- I read nothing in docs/referee/ or notes/REFEREE.md. REFEREE's report on this packet (fa08687, per the Lead) is on trunk and in my
  merged tree; I did not open it.
- I did not run or import any lane script for a check. The one exception is a DATA re-run of the lane's own reproduction command
  (fbsplit.py, packet §8) to compare numbers (§8 below).
- Lane .pg files are inputs only.
Tools: docs/referee-2/R2-N5-OUT/ (own code; it builds on my lane's R2-N5-FRZ/frz_check.py and R2-N5-RE/re_check.py):
- out_check.py: the checks;
- out_climb.py: the climbs;
- spec_s3.py: the SPEC-trace attribution run;
- files.lst, run_all.sh, run_climbs.sh, totals.py, logs/, climb/, totals_logs.txt, logs_spec_s3.txt.
Every game asserts exactly one Odd vertex with out-degree > 1. The phase key is (λ_Ξ, τ).
Attribution. Every count names its trace:
- own: my N5. S4a takes an arena optimum by deterministic switch-all SI. S4b takes a pointwise-best option at o. S4c is as SPEC.
- rand: my N5 with random-subset SI and random value-preserving re-choices; any arena optimum.
- spec: the state sequence of experiments/new/n5.py (SPEC tie-breaks) via re_check.n5_spec, checked with my definitions.
Labels (D18 / L40): PROVED (L-NEW succ. 16/17) is the packet's own label. §7 is not signed, as briefed. Nothing here is a running-time
bound, a TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN.

## Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| §1 Lemma SPLIT (a), (b) and the crossing dichotomy | SIGN | N-OUT-1: in the landed FBL-N, R contains o (P-N5-X §0), so R21 (c) (iii) already excludes the target o; the "(filled in)" step re-derives this and is correct |
| §2 Corollary EPOCH (corrected form) | SIGN | It uses FB-INT (P-N5-SCOPE §4), which both referees signed (REFEREE-2 6d6e4bcf, §C fb6fa696). N-OUT-3: the dependency table's status column is stale. The corrected "+ X_S" is the O-1 repair and is needed. The superseded form is unproved, not refuted: 0 cases in data |
| §3 Lemma F-FLAT | SIGN | — |
| §4 Lemma FREEZE-STEP, Corollary TAIL | SIGN | Control: drop the hypothesis "no gate into R̄_t" and a conclusion fails at 259 / 255 / 283 of 265 / 258 / 285 such transitions (own / rand / spec) |
| §5 Theorem NO-ENTRY-A | SIGN | N-OUT-2 (citation): Step (K) (R23 (a)) is stated for "a fallback inside a phase". The statement lets a + 1 leave S, and then possibly the phase (b = a). BASE needs only FBL-N (i) (τ unchanged) with F1 (R17 (a)), which hold at every Even fallback. So the step is sound; the citation should be FBL-N (i) + F1 or Step (K)'s proof. Controls: dropping "θ constant" and dropping case A each produce violations (§9) |
| §5 Corollary NE-COUNT (a)-(c) | SIGN | — |
| §6 Lemma CASE-B-LEN, Remark W-SIDE | SIGN | The hypothesis is reached: 4 R → R̄ gates at case-B HN fallbacks in the batch (SPEC trace, nebc_cex_n14), and 1,291,962 in my climbs, with both W-SIDE cases (§9). All are level −1 with z's route longer. The "Consequence (… READING)" paragraph is a reading and is not signed |
| §7 | not signed (as briefed) | N-OUT-4 (record): CONJECTURE NO-ENTRY-B and CONJECTURE NO-ENTRY for τ(o) ≠ o are FALSE. The lane found this after the pin (box 38: nebc_cex_n14, tauw_A_cex_n24, tauw_B_cex_n24), and my checker reproduces it in all three traces (§7). The DEAD END ROUTE-FROZEN reproduces too |
No statement is NOT SIGNED, and no gap is open. No counterexample turned up in 66,655 batch runs (2,655 library + 64,000 random) or in
741,432 climb runs (4 climbs).

## 1. Lemma SPLIT: SIGN
Statement as written: for an in-phase transition k → k+1 with H1 ∧ ¬H2 at k, (a) a non-fallback has R_k ⊆ R_{k+1}, and (b) an Even S4c
fallback has R̄_{k+1} ⊆ R̄_k.
- Transition kinds. τ is constant in a phase, so an in-phase transition that is not a fallback has Iσ ≠ ∅. (If Iσ = ∅ and τ_new = τ, the
  fallback is Odd's and changes τ.) So it is an S4a step: σ_new is an arena optimum and τ_new = τ. An in-phase fallback is Even's
  (FIX 3), since an Odd fallback moves τ(o) to an improving target ≠ τ(o). ✓
- (a) Take v ∈ R_k.
  - Under ¬H2, o lies on its W-cycle C_W, and every vertex of C_W reaches o. So v's W-cycle node is c_w = top(C_W) ∈ R̄_k.
  - On 𝒞^1O, H_k and the (σ_k, τ)-graph differ only at o. So v's honest play is π_v followed by o's honest play, and λ(v) = c_θ.
  - Under H1, o's honest cycle avoids o. Each vertex on it has the same successor in both graphs, so its (σ_k, τ)-play stays on that
    cycle and never meets o. So c_θ ∈ F_k.
  - Hence c_w ≠ λ(v), and R-STICK (R30 (c): an S4a transition of a phase, no H1 needed) keeps v in R_{k+1}. ✓
- (b) If R̄ gains a vertex, ACT (i) (R23 (b), τ unchanged) gives a switched s ∈ F_k with σ_{k+1}(s) ∈ R̄_k.
  - S4c switches gate edges only, so (s, σ_{k+1}(s)) is a gate from F_k into R̄_k.
  - Landed FBL-N (iii) (R21 (c)) forbids it under ¬H2. There, R contains o (P-N5-X §0: "o ∈ R_k by convention"; F_k := V ∖ R_k, the
    packet's F_k), so the target o is already covered.
  - The packet's "(filled in)" argument for z = o is also correct: x = λ_W(o) ∈ C_W ⊆ R̄_k. N-OUT-1. ✓ (b) does not use H1.
- Dichotomy. A crossing at an S4a step has R_k ⊊ R_{k+1}: an entry. A crossing at a fallback has R̄_{k+1} ⊊ R̄_k, since o is in both:
  an eviction. ✓
- DATA: 899 / 945 / 919 S4a cases and 188 / 204 / 193 fallback cases (own / rand / spec, library). Every crossing of every HN stretch
  is an S4a entry or a fallback eviction. 0 violations.

## 2. Corollary EPOCH (corrected form): SIGN
- Segments. Cutting before each break gives B + 1 segments. Take an eviction e inside a segment and the first entry after it. Then e
  precedes it with no entry in between, so that entry is a break and starts a new segment. So inside a segment every entry precedes every
  eviction. ✓
- Before a segment's first eviction:
  - S4a steps do not shrink R (SPLIT (a));
  - a fallback that changes R is an eviction (SPLIT (b));
  - so R grows weakly, strictly at each entry, inside V ∖ {o}: at most n − 1 entries.
- After it, there are no entries. S4a steps leave R fixed (SPLIT (a) with no entry). Each eviction shrinks R̄ ⊇ {o} strictly: at most
  n − 1 evictions. So X_S ≤ 2(n − 1)(B + 1). ✓
- Fallbacks.
  - Crossing fallbacks: at most X_S.
  - The others lie in the ≤ X_S + 1 maximal crossing-free runs of S.
  - Each such run lies in one maximal crossing-free run Q of the phase, and distinct runs of S lie in distinct Q (a crossing separates
    them).
  - FB-INT (P-N5-SCOPE §4, "Q ... ≤ n_E(2n − 1) S4c fallback transitions") applies to Q verbatim.
  - So f_S ≤ K(X_S + 1) + X_S. ✓
- The "+ X_S" term is needed for the proof. In data every fallback with both ends in an HN stretch is a crossing: 184 / 198 / 189 of
  184 / 198 / 189 (own / rand / spec). The superseded f_S ≤ K(X_S + 1) never failed in data (0), because K ≥ 1 and the crossing-free
  runs of S carried no fallbacks. It is unproved, not refuted.
- DATA: max X_S 31 (all traces), max f_S 12, max breaks per stretch 2. Per-segment counts (entries / evictions ≤ n − 1 each, entries
  before evictions) and both bounds held: 0 violations. FB-INT itself (≤ K fallbacks per maximal crossing-free run of a phase): max 1
  per run in the library, 0 violations.

## 3. Lemma F-FLAT: SIGN
- Step 1. Take x ∈ F_k switched to z.
  - FBL-N (ii) (as stated in P-N5-X §3) gives x = λ_W(x) and λ_W(z) = x, and (iii) gives z ∈ F_k.
  - Plays from F avoid o, so W = Ξ there (G (a)). Hence λ_k(x) = x and λ_k(z) = x.
  - (F) (R34 (a)) with c = x gives Ξ_k(σ_k x) = (x, ∅, L_x − 1); σ_k(x) lies on x's cycle.
  - No switched x′ lies on q before x: x′ is its own cycle node, so a play through x′ ends on x′'s cycle, with cycle node x′ ≠ x.
    This includes z itself. The self-loop gate z = x gives q = (x) and the cycle x → x.
  - The new cycle x → z → q → x is forced: its Odd vertices are forced, and o is not on it.
  - In-phase means λ_{k+1}(x) = x, so x tops that cycle and P(Ξ_k z) = ∅. The gate has level −1. ✓
- Step 2. Take v ∈ F_k with c := λ_k(v), and let p be v's path to c (p ⊆ F_k).
  - p has no switched vertex before c.
  - If c is unswitched, c's cycle has no switched vertex (each x on it has λ_k(x) = c ≠ x). If c is switched, the continuation is Step
    1's cycle.
  - In both cases V_{σ_{k+1}, σ̄_k}(v) = (c, p ∩ V_{>c}, |p|) = Ξ_k(v). The play avoids o, so σ̄_k plays no role.
  - Lemma S (a) gives ⊴, and R15 (a) gives ⊵. ✓
- Step 3. Under H1, x0 = σ̄_k(o) ≠ o, and its honest play avoids o, so x0 ∈ F_k.
  - Under (σ_{k+1}, σ̄_k), o's play is o followed by x0's new play, which stays in F_k (Step 2).
  - So V(o) = o ⊕ Ξ_k(x0) = θ_k by (V1) at k.
  - Lemma S (a) and R15 (a) then give θ_{k+1} = θ_k. ✓
- DATA: 188 / 204 / 193 in-phase HN fallbacks. Ξ was unchanged on F_k and θ unchanged in every case. Every gate from F_k had z ∈ F_k,
  λ(x) = λ_W(x) = x = λ(z) = λ_W(z), and level −1. 0 violations.

## 4. Lemma FREEZE-STEP and Corollary TAIL: SIGN
- Route form. Under H1, no vertex of π_z is a cycle node: its play reaches o and never returns. So Ξ_k(z) = π_z ⊕ θ_k by (V1). ✓
- (i), S4a step.
  - Switched targets are σ_t(s) or gate targets, all in F_t. So ACT (i) excludes an entry, and SPLIT (a) gives R_{t+1} = R_t.
  - A switched v ∈ R_t would move to F_t = F_{t+1} and leave R. So no vertex of R_t switches, and routes are unchanged. ✓
- (i), fallback. SPLIT (b) gives R̄_{t+1} ⊆ R̄_t. A switched vertex on a t+1 route would point into F_t ⊆ F_{t+1}, against the route. ✓
- (ii) follows from the route form at t and at t+1 with equal routes and θ. ✓
- (iii) The chain Ξ_t(z) = Ξ_{t+1}(z) ▷ Ξ_{t+1}(σ_{t+1} y) ⊵ Ξ_t(σ_{t+1} y) ⊵ Ξ_t(σ_t y) uses (ii), R15 (a) and R15 (d). z = σ_t(y) is
  impossible. Otherwise (y, z) ∈ Iσ_t with z ∈ R̄_t, against the hypothesis. ✓
- TAIL: induction inside the stretch while θ is constant. Each step needs H1 at t+1, which holds inside the stretch. ✓
- DATA: hypothesis met at 560 / 640 / 570 transitions (162 / 185 / 170 fallbacks, the rest S4a). (i)-(iii) held in every case. TAIL:
  706 / 772 / 720 starts and 5,229 / 6,431 / 5,315 steps, 0 violations.
- Control: in-phase HN transitions with H1 at t+1 and θ equal, but with a gate into R̄_t: 265 / 258 / 285. There some conclusion fails in
  259 / 255 / 283 of them. The hypothesis is the one ROUTE-FROZEN's obstruction names, and it carries the lemma. Mutation "nohyp" flags
  wd16_s2 and rfroz_cex_n16 at once.

## 5. Theorem NO-ENTRY-A and Corollary NE-COUNT: SIGN
Setting facts.
- τ(o) = o gives w = (o, ∅, 0) and ¬H2 at every state, so HN = H1.
- At an H1 state c_θ ≠ o, and XW with distinct cycle nodes gives reward(c_θ) < reward(o). Rewards of distinct vertices differ, since p′
  is injective and its sign is the parity.
- Case A forces Ω(o) even, and case B forces Ω(c_θ) odd. Both one-line arguments are right. ✓
(T1)-(T3).
- x ≡ y means the same cycle node and the same P on ranks ≥ rank(o). It is an equivalence relation.
- (T1): the parts of P at ranks ≥ rank(o) are unchanged, so the top of the difference, its side and the cycle-node comparison are
  unchanged.
- (T2) follows from (T1) applied to (x′, y).
- (T3): ⊕ adds the same vertex to both or to neither.
- Checked mechanically (mode t123): 171,535 (T1), 17,507 (T2) and 162,147 (T3) random cases, 0 failures. ✓
SEP-o. o ∈ P(θ_t) because o is not a cycle node (H1) and rank(o) > rank(c_θ). ⊕ only adds vertices along π_z. F-plays avoid o. ✓
BASE (i) is FBL-N (iii). BASE (ii), checked line by line:
- σ_a(v) ∈ R̄_a. P(θ_a) ⊆ {o} ∪ F_a, and the routes lie in R_a. So the honest P-difference is (π_z Δ π_{σ_a v}) ∩ V_{>c_θ}, with top
  u ≠ o, so rank(u) > rank(o).
- The W-difference is (π_z Δ π_{σ_a v}) ∩ V_{>o}. Its top is the same u on the same side, because anything above u is above c_θ. So
  the W comparison gives the same verdict.
- Case 1 (v ∉ π_z): v is on neither play (its own route cannot contain it), and o's W-play is the self-loop. So the switched W at v is
  v ⊕ W_a(z) ▷ v ⊕ W_a(σ_a v) = W_a(v).
- Case 2: the honest difference is q ∪ {v} restricted above c_θ, all on z's side. So Ω(u) is even, u tops the closed cycle (everything
  else on it lies below c_θ), and p′(u) > p′(o) = reward(o) (Ω(o) even, case A).
- In both cases σ_a[v → z] has a strictly larger W at v. σ_a is a pointwise arena optimum in G_τ (FBL-N (i)), and F1 (R17 (a)) makes it
  dominate every arena strategy. Contradiction. That is Step (K)'s proof, and it needs only τ_{a+1} = τ_a (N-OUT-2). ✓
STEP, checked line by line:
- No entry: switched edges are gates, (i) at t, and ACT (i).
- The value claim, by induction on the route length at t+1:
  - d = 0 uses θ constant;
  - for d ≥ 1, (V1) at t+1 (H1, z not a cycle node), (ii) at t for a switched z (z ∈ R_{t+1} ⊆ R_t, z′ ∈ R̄_{t+1} ⊆ R̄_t, and the
    switched edge is a gate), and (T3), then (V1) at t with z ∈ R̄_t.
- (i) at t+1:
  - SEP-o at t+1, (T1), and R15 (a), (d) give a gate (y, z) at t;
  - y ∈ F_t contradicts (i) at t;
  - y ∈ R_t: (ii) at t, (T2), and o's membership in the two path sets give the contradiction.
  - The case split is complete: F_{t+1} ⊆ F_t ∪ R_t, and y ≠ o since gates start at Even vertices.
- (ii) at t+1: the value claim, (ii) at t, and (T1) give an R → R̄ gate at t of level ≥ rank(o), against (ii) at t.
Everything else in the statement follows: R̄ only shrinks, there are no entries, and the classes are frozen by transitivity of ≡. ✓
NE-COUNT.
- (a) The eviction a → a+1 is a fallback (SPLIT). If θ were constant on [a, k+1] ⊆ S, NO-ENTRY-A with b = k+1 would exclude the entry.
  F-FLAT puts the θ-change at an S4a transition j → j+1 with a < j ≤ k. The next break's eviction is after this entry, so the intervals
  are disjoint, and B ≤ θ_S. ✓
- (b) is EPOCH with (a). ✓
- (c):
  - In a τ(o) = o phase the HN stretches are the maximal H1-runs. T_ph toggles give T_ph + 1 alternating runs, so
    N_HN ≤ ⌊T_ph/2⌋ + 1 ≤ ⌊T*/2⌋ + 1 by TOGGLE-COUNT (R34 (e)).
  - An HN in-phase fallback has both ends in one stretch, or it is that stretch's exit (≤ 1 per stretch).
  - The θ_S count disjoint transitions.
  - The arithmetic: Σ_S (f_S + 1) ≤ (K + 1) Σ_S (X_S + 1) ≤ (K + 1) Σ_S (2(n − 1)(θ_S + 1) + 1) ≤
    (K + 1)(2(n − 1)θ_ph + (2n − 1)N_HN). ✓
DATA (library):
- 63 / 59 / 63 case-A τ(o) = o phases (own / rand / spec);
- SEP-o at 735 / 804 / 749 H1 states;
- 124 / 141 / 126 base fallback states, with 21 / 6 / 18 R → R̄ gates there;
- 1,070 / 1,322 / 1,077 (a, b) pairs and 4,181 / 5,133 / 4,249 value-class checks: INV held at every pair, with no entry and no class
  change;
- 12 / 12 / 12 case-A breaks, each with an S4a θ-change in (a, k] and the intervals disjoint; B ≤ θ_S in every stretch;
- (c)'s bounds held in every case-A phase (max f_HN 12 on wd16_s2, max θ_ph 11); T_ph ≤ T* everywhere;
- 0 violations.

## 6. Lemma CASE-B-LEN and Remark W-SIDE: SIGN
- The P-difference computation is §5 BASE's. Any non-empty difference has its top u above c_θ, hence above o, so §5's Cases 1-2 apply.
  Case 2 needs Ω(u) even (z's side) and gives reward(u) = p′(u) > p′(o) ≥ reward(o). This holds for either parity of o, which is all case
  B allows. So P is equal, lev = −1, and c_θ odd makes the longer route better. ✓
- W-SIDE Case 1: the W-difference lies in (rank(o), rank(c_θ)). Step (K) forbids a W-favourable top, and with an empty difference it
  forbids odd o, since the longer route would win. Case 2's statement on the closed cycle's node is Step (K) directly. ✓
- The hypothesis is reached in the batch: 4 R → R̄ gates at case-B HN fallback states, SPEC trace, on 2 library files.
  All are level −1 with z's route longer, and all are Case 1 with an empty W-difference and Ω(o) even. The own and rand traces reached
  case-B HN fallbacks (18 / 23 states) but no R → R̄ gate there.
- My caseb climbs reach it about 1.3 million times, with W-SIDE Case 2 among them (§9). 0 violations.
- The "Consequence (… READING)" paragraph is not signed. It is consistent with the lane's later nebc_cex_n14: the fallback's length-only
  R → R̄ switch 3: 7 → 6, then the F → R̄ gate 4 → 3.

## 7. §7, not signed: what my data says
- ROUTE-FROZEN (FALSE): rfroz_cex_n16 reproduces in all three traces. FREEZE's hypothesis fails at the post-fallback states, and R-values
  change after the fallback with θ constant and no entry.
- CONJECTURE NO-ENTRY-B and NO-ENTRY for τ(o) ≠ o are FALSE (N-OUT-4).
  - My checker records every break with no θ-change between its eviction and its entry. In case A it treats such a break as a
    violation; elsewhere it records it.
  - Records (own / rand / spec):
    - nebc_cex_n14 (sha1 399119af…): 1 / 1 / 1. Under the SPEC trace that break lies in a case-B τ(o) = o phase; under my own N5, in
      a τ(o) ≠ o phase.
    - tauw_A_cex_n24 (sha1 e29908d5…): 2 / 2 / 2, τ(o) ≠ o.
    - tauw_B_cex_n24 (sha1 c0ad4f0c…): 4 / 2 / 4, τ(o) ≠ o.
  - The lane reports these instances after the pin (docs/new/N5-NEB-box38.md, N5-TAUW-box38.md; l-new c7631588, 530261c2). I read
    those files only after my verdicts.
  - No case-A τ(o) = o break was ever unseparated.
- The open residual core (θ_S / θ_ph, HN stretches for τ(o) ≠ o, OTHER states) stays open. Nothing here bounds it.

## 8. The packet's §8 data
- Re-run of the lane's command (`python3 experiments/new/box38/fbsplit.py $(cat experiments/new/box37/lib37.txt) …/rfroz_cex_n16.pg`,
  exit 0). It reproduces data/fbsplit_lib.txt line for line:
  - 115 HN stretches;
  - 107 crossing, 0 non-crossing and 2 exit fallbacks;
  - breaks 8 (A) + 3 (B), all θ-separated;
  - 25 case-A / 12 case-B τ(o) = o phases;
  - max f_S 12 (wd16_s2), max X_S 31 (post31_n48).
- Its trace is the SPEC engine from the S3 start (mblock.rows_w → start_pair).
- My checker on the same trace and start (spec_s3.py, logs_spec_s3.txt) gives the same numbers:
  - 271 runs (270 lib37 files + rfroz_cex_n16), 159 non-𝒞^1O files skipped;
  - 115 HN stretches;
  - 107 fallbacks with both ends in a stretch, all 107 crossings;
  - breaks 8 (A) + 3 (B);
  - 25 / 12 phases;
  - max X_S 31, max f_S 12;
  - 0 violations of any check.
- The lane's numbers are counts on the SPEC trace from the S3 start. My batch numbers (§9) add two random starts per file and two
  other traces.

## 9. Batch, controls and climbs (DATA, not proof)
- Batch (run_all.sh, logs/, totals_logs.txt): 295 𝒞^1O library files × 3 traces × 3 starts (S3 + 2 random)
  = 2,655 runs, 50,667 states. Random 𝒞^1O games (n 4-14 and 15-30): 22,000 own + 22,000 rand + 20,000 spec runs, 156,816 states.
  - Random games give 6,703 HN stretches but only 4 in-phase HN fallbacks (2 / 1 / 1), no break and max X_S 2. The library carries the content, as
    the lane found.
  - 894 / 894 logs end "RESULT OK violations=0"; there were no timeouts.
- Mutation controls (OUT_MUT, out_check.py):
  - "theta" (NO-ENTRY-A walked past θ-changes): violations on b5_os_n16 (86), wf0_cex_n16 (222) and b5_os_n24 (261), SPEC trace.
  - "caseB" (case B treated as case A): 43 violations on nebc_cex_n14 (SEP-o, NE-COUNT (a)).
  - "nohyp" (FREEZE-STEP without its gate hypothesis): violations on wd16_s2 and rfroz_cex_n16.
  - The checker sees each hypothesis being removed.
- Climbs (run_climbs.sh, climb/): four 1200 s climbs (FIT caseb × 2, brk, nea; own and rand traces;
  mutations keep o's self-loop):
  - totals: 185,358 evaluations, 741,432 runs, 4,779,867 states, 845,231 HN stretches; 0 violations (totals_climb.txt);
  - CASE-B-LEN: 1,291,962 R → R̄ gates at case-B HN fallbacks, all level −1 with the longer route. W-SIDE: 945,586 Case 1 (404,314 with
    an empty W-difference, all with Ω(o) even) and 346,376 Case 2. So both cases of the Remark occur;
  - NO-ENTRY-A: 2,346,463 (a, b) pairs, 138,804 R → R̄ gates at base states, 9,702,716 value-class checks;
  - 27,892 case-A breaks, all θ-separated as NE-COUNT (a) requires; 33,294 case-B breaks (all θ-separated in the climbs: a record,
    not a claim);
  - FREEZE-STEP's hypothesis: 911,595 times; TAIL steps: 3,376,157;
  - climbs are not families.

## 10. Notes for the lane (none blocks a signature)
- N-OUT-1: SPLIT (b) / F-FLAT Step 1: landed FBL-N (iii) has o ∈ R, so the target o is covered by the citation. The filled-in step is
  correct and redundant.
- N-OUT-2: NO-ENTRY-A BASE and CASE-B-LEN cite Step (K), which is stated "inside a phase". Cite FBL-N (i) + F1, or require a + 1 ∈ S.
  NE-COUNT always has a + 1 ∈ S.
- N-OUT-3: the dependency table's status column for KEY / FB-INT is stale. Both referees have signed (REFEREE-2 R2-N5-SCOPE 6d6e4bcf and
  §C fb6fa696; REFEREE per the table); landing is pending (no RESULTS row yet on trunk fb1dfb92).
- N-OUT-4: §7's CONJECTURES NO-ENTRY-B and NO-ENTRY (τ(o) ≠ o) are FALSE (lane box 38). The frozen packet still lists them as
  conjectures. The RESULTS entry should carry the FALSE status.

## §C. Comparison with REFEREE's R-N5-OUT, and the lane's fixes file (written 2026-10-25 14:32Z by date -u, after my report dfcaae67 was pushed and merged)
Read: docs/referee/R-N5-OUT.md at trunk 7fc7ac9 (report fa08687, §C a8b8ef3), and docs/new/P-N5-OUT-fixes-box37.md (sha1
640a5db215e7d5e2bcdc3b335ae5e4972fed1fb2; it agrees on my tree and at origin/claude/l-new; L-NEW succ. 17, l-new dd3f780).
### C.1 Verdicts
They are identical. Both referees sign SPLIT, EPOCH (corrected; both say "+ X_S" is needed), F-FLAT, FREEZE-STEP, TAIL, NO-ENTRY-A,
NE-COUNT (a)-(c), CASE-B-LEN and W-SIDE. Neither signs §7 or W-SIDE's "Consequence" (READING). No gap in either report, so the joint
gap map is empty.
### C.2 Notes map
| REFEREE | REFEREE-2 | content | status |
| --- | --- | --- | --- |
| OUT-R1 | N-OUT-2 | (K) / Step (K) is stated "inside a phase"; BASE uses it at a only, and a+1 may leave the phase when b = a. FBL-N (i) + F1 suffices. REFEREE's §C extends it to CASE-B-LEN, as in my N-OUT-2 | agreed; citation; fixes §1 |
| OUT-N1 | N-OUT-3 | KEY / FB-INT status stale | agreed; status; fixes §2 |
| — | N-OUT-1 | FBL-N (iii) already covers the target o (o ∈ R in P-N5-X) | accepted by REFEREE's §C; record; fixes map |
| NO-ENTRY-B FALSE (in its §7 row) | N-OUT-4 | §7 conjectures FALSE: NO-ENTRY-B (nebc_cex_n14) and NO-ENTRY for τ(o) ≠ o (tauw_A/B_cex_n24) | agreed; record; fixes §3 |
Nothing is only REFEREE's that I would reject, and nothing is only mine that REFEREE rejects.
### C.3 Data, side by side (DATA, not proof)
- REFEREE's lib37 counts are counts on its own engine (rl_engine) from the canonical start: 113 stretches, 11 breaks (8 A + 3 B),
  25 / 12 τ(o) = o phases, every in-stretch fallback a crossing. They agree with the lane's §8 and with my spec_s3.py run (115 / 11 /
  25 / 12 with rfroz_cex_n16 included, and 107 / 107 crossings).
- REFEREE did not test NE-COUNT (c)'s per-phase bounds in data (its §7, "checked as arithmetic"). I did:
  - case-A τ(o) = o phases, every trace;
  - N_HN ≤ ⌊T_ph/2⌋ + 1, the f_HN and X_HN bounds, and T_ph ≤ T*: 0 violations.
  So the two reports complement each other there.
- CASE-B-LEN thin spot (REFEREE: 4 checks, all on nebc_cex_n14). My climbs add 1,291,962 checks, with both W-SIDE cases (§9).
### C.4 The lane's fixes file (P-N5-OUT-fixes-box37.md), checked item by item
- §1 (OUT-R1 = N-OUT-2): the repair is to read "against Step (K)" in §5 BASE (ii) and §6 as FBL-N (i) (R21 (c)) + F1 (R17 (a)), using
  only τ_{a+1} = τ_a. That is exactly my N-OUT-2, and it is Step (K)'s own proof (P-N5-Z §1). Correct.
  - Its forward pointer (P-N5-NEB §3-§4 cite Step (K) the same way) is noted for my NEB review.
- §2 (OUT-N1 = N-OUT-3): the SHAs I can check are mine, and they are right (R2-N5-SCOPE 6d6e4bcf, §C fb6fa696). REFEREE's (fb6089bf,
  257c3d81) are as its own report states. Correct.
- Map row N-OUT-1: recorded with no change of text, which is what I asked for. Correct.
- §3 (N-OUT-4). I checked:
  - the sha1s of nebc_cex_n14, tauw_A_cex_n24 and tauw_B_cex_n24;
  - its "c_w ≠ o" qualification, with my own code on all three traces: every θ-constant entry after an HN eviction on tauw_A has
    τ(o) = 9, c_w = 7 ≠ o, case A; on tauw_B, τ(o) = 2, c_w = 7 ≠ o, case B;
  - nebc_cex_n14's break: case B with c_w = o, both under SPEC (τ(o) = o) and under my own N5 (τ(o) = 3).
  So "NO-ENTRY for τ(o) ≠ o is FALSE when c_w ≠ o, in both cases" and "NO-ENTRY-B is FALSE" match my data.
  - Its "what survives" lines cite P-N5-NEB, which is not reviewed yet (next in my queue). I neither sign nor reject them here.
- The fixes file changes no statement or verdict, and none of my verdicts changes.
### C.5 Joint state
All §1-§6 signable statements of P-N5-OUT are PROVED (L-NEW succ. 16/17) and signed by both referees (Opus 5.5, D15), with no (P) and no
open gap. The citation and status repairs are in the fixes file. §7's two conjectures are FALSE (record), and the RESULTS entry should
say so.
