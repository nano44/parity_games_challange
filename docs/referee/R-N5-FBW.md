# R-N5-FBW: REFEREE report on packet P-N5-FBW (box 9: FBW, FBW-S, CLS2, FLAT-ALL, STRETCH, Theorem PL, Corollary PL-S)
Referee: REFEREE (successor 6), Opus 5.5 (owner ruling D15, Lead reading L37). Packet P-N5-FBW: the Lead's message of 2026-10-25 05:53Z
(Lead's stamp). Object docs/si/P-N5-FBW-box9.md at pinned trunk e69772b, sha1 88337bd621d3467dde4b35aa93b254bf847bb330 (checked:
`git show e69772b:docs/si/P-N5-FBW-box9.md | sha1sum`, 218 lines). Author L-SI successor 4. Written 2026-10-25 06:01Z onward by date -u.
Every verdict is labelled (Opus 5.5, D15). Labels (D18/L40): PROVED (by whom) / CONJECTURE / OPEN. Independent of REFEREE-2:
docs/referee-2/ not read for this packet.
Dependencies read: R18 (d) Lemma S and G-1OA-6 (RESULTS l. 803-807; R2-N5-1OA §3 (c), my predecessor's R-N5-1OA §C), R17 (a) (F1), R20 (b)
FBL with R-N5-XA §3, R25, R28 U-loc, R29 (my R-N5-CLS), R30 (my R-N5-SN).

## Verdicts
| statement | lane label | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §0 premise P-OPT and "G-1OA-6 does not apply" (the Lead's hardest item) | — | VALID (§1.1) |
| §1 Lemma FBW (every game) | PROVED (L-SI succ. 4) | SIGNED |
| §2 Corollary FBW-S | PROVED | SIGNED |
| §2 Theorem CLS2 | PROVED | SIGNED |
| §3 Lemma FLAT-ALL | PROVED | SIGNED WITH GAP FBW-1 (citation, closed: in (i), a switched cycle node's new cycle avoids o by H1 at k+1, not by "o's W-cycle / H2") |
| §4 Lemma STRETCH | PROVED | SIGNED |
| §5 Theorem PL (a)-(c) | PROVED | SIGNED WITH GAP FBW-2 (wording, closed: (a) needs STRETCH also for the block's LAST fallback, which may be the last state of its run; STRETCH's proof covers it) |
| §5 Corollary PL-S | PROVED | SIGNED |
| §6 NJB, NJ-INT, ABS-O, open items | not to sign | not signed. Note: D_M = 0 in all my data too, so PL (b)/(c) are never exercised (thin spot) |

## 1. Lemma FBW (SIGNED)
### 1.1 P-OPT and G-1OA-6
- G-1OA-6 (R18; R2-N5-1OA §3 (c), accepted by REFEREE in R-N5-1OA §C) says one thing: "σ_{k+1} maximises V_{·,τ_k} over A(σ_k)" holds when
  σ_{k+1} is S4a's output, and is FALSE when σ_{k+1} is the strategy S4c installs.
- P-OPT makes a different claim. N5 runs S4a's arena computation at every iteration, the fallback iterations included. A fallback fires
  exactly because that computation returned σ_k (SPEC S4c; the trace's fallback flag is set iff S4a and S4b both returned the current pair).
- So at a fallback state k, S4a's output is σ_k itself. R17 (F1) on the one-player game A(σ_k) against τ_k (R18 (d) Lemma S (c), in its
  S4a-only scope) makes σ_k the pointwise optimum there. P-OPT uses the output, which G-1OA-6 leaves valid; it never uses the installed
  strategy σ_{k+1}. VALID.
- The DF trap (VJ00 Lemma 5.8 "2 ⇒ 3" at own cycle nodes, R-N5-LP): FBW does not cite Lemma 5.8. It computes V′(y) for the single switch
  directly and compares it with W_k(y) via (F1)'s pointwise domination, which holds for every arena strategy. The own-cycle-node
  length-only case, where "no improvement" fails, is exactly FBW's exception (b2, y = c). So the lemma is built around the trap.
- DATA, with teeth:
  - At every Even S4c fallback and every gate (y, z) (2,618 library + 837 named + 170 random general + 225 random 𝒞^1O gates), the single
    switch σ_k[y ↦ z] against τ_k gives V′(y) ⊴ W_k(y): 0 failures.
  - Control: at non-fallback S4a states, a W-improving single gate switch exists in 1,061 of 1,164 states (rand general, seed 9305). So
    the check would see a failure.
### 1.2 The proof
- Step 1: COARSE_δ(Ξ x) = COARSE_δ(W x) at u and z. The strict Ξ-gate at level ℓ > δ transfers to a strict W-order ((C1)-(C3)). Since
  COARSE_{L′} of Ξ and W agree at u, z for every L′ ≥ δ, lev(W u, W z) = ℓ. Correct. DATA: 0 Step-1 failures at 418 gates with ℓ > δ (library 18, named 6, random general 169, random 𝒞^1O 225).
- Step 2, each case checked:
  - (a) z's play avoids y.
    - y a cycle node: V(z)'s cycle node differs from y, and V z ▷ V u forces the cycle-node reward up.
    - otherwise: y lies in neither path set (if u's play passes y, y is a non-top vertex of the cycle, of rank < rank c), so y ⊕ keeps the
      strict order, also across different cycle nodes.
    Correct.
  - (b1) Disjointness P(V z) = P(V u) ⊔ D′ holds (one simple path into y, then u's).
    - D′ ≠ ∅: its even top is the top t of the new cycle C, rank t > rank c, so rew(t) > |rew(c)|.
    - D′ = ∅: length-only and longer, so c is odd; rank t < rank c gives rew(t) > rew(c).
    Correct.
  - (b2) y on its own cycle C_y with top c.
    - P(V z) ≠ ∅: as (b1).
    - P(V z) = ∅ and c ∉ C: e lies strictly between c and y on C_y. dist(e, c) runs through y and u, so V z is longer; c is odd and
      rank t < rank c.
    - P(V z) = ∅, c ∈ C, y ≠ c: the lengths 1 + a + dist(e, c) and 1 + dist(u, c) are compared by the same parity rule as V z, V u.
    - y = c: no strict improvement, lev = −1.
    Correct. The case split is complete: z's play avoids y (a), or visits y with y off its own cycle (b1), or on it (b2).
- Step 3: the contradiction with P-OPT outside the exception. In the exception, ℓ = −1 (Step 1) and y is its own W-cycle node. With δ = ⊥,
  Ξ(u) = W(u) has cycle node y, so λ_Ξ(y) = y by (P1). Correct.
- DATA: FBW (a) and (b): 0 failures at all gates above.

## 2. Corollary FBW-S and Theorem CLS2 (SIGNED)
- FBW-S: inside a phase τ is constant, so the fallback is Even's. δ ≤ max_v lev(Ξ v, W v): this is ⊥ off R̄ (Lemma G (a)), and r_k on R
  and at o ((C7), CLU's disjointness). Then FBW (a) and (b). Correct.
- CLS2:
  - Fact R puts the r ≥ 0 fallbacks of S first, and CLS1 (R29 (f)) orders them.
  - Every later fallback has r ≤ −1, so M = −1 by FBW-S (gate levels are ≥ −1), which is ≤ every earlier level.
  - So R29's (H-EQ) is closed. Correct.
- DATA:
  - in-scope fallbacks: 596 THR u* ≠ none + 9 EQ (library), 252 + 4 (named; equal to the packet), 142 EQ (random 𝒞^1O); 0 THR with
    u* = none;
  - FBW-S (M ≤ max(r, −1); M = −1 and own-cycle-node tails at EQ / u* = none) and CLS2 (non-increasing levels per scope run, every kind):
    0 failures in 204 + 70 + 892 scope runs.

## 3. Lemma FLAT-ALL (SIGNED WITH GAP FBW-1)
- FBW-S gives r_k ≥ M ≥ 0, so the state is THR with u* ≠ none, and FBL (strong gate form at k, as in R29 row 1) applies: the switched edges
  are R → F and own-cycle-node switches. Under H1 no R vertex is its own cycle node (λ = c_θ ∈ F on R), so the cycle-node switches are at
  F vertices, and FBL excludes F → R̄ gates.
- (i) FBW-1 (citation): the packet says the new cycle through a switched cycle node y′ "does not contain o: otherwise it would be o's
  W-cycle at k+1, against H2". The cycle in question is y′'s HONEST H_{k+1}-cycle (λ(y′) = y′ refers to Ξ). If o were on it, H1 would
  fail at k+1. A cycle through o in H_{k+1} uses σ̄(o), not τ(o), so it need not be o's W-cycle. The hypothesis "(h) at k+1" contains H1,
  so the claim holds. Replace "W-cycle … H2" by "honest cycle … H1 at k+1". Off o the honest and (σ, τ) graphs agree, so the rest of (i)
  follows. Closed.
- (ii): x0 ∈ F_{k+1} by (i). Lemma S (a) with Odd's choice x0 gives θ_{k+1} ⊴ o ⊕ Ξ_{k+1}(x0), whose play avoids o. With R15 (a), OFF at x0,
  (C7) through o, and the sandwich ((C1), (C3)): correct.
- (iii): OFF off R̄_{k+1}; on R̄_{k+1}, Lemma G (b) at both states with the same route, (C4)/(C7) and (ii). (iv): TRANSFER. Correct.
- DATA: 596 (library) / 252 (named) in-scope fallbacks with M ≥ 0 and (h) at k, k+1. (i) F_k ⊆ F_{k+1} and identical routes on R̄_{k+1};
  (ii), (iii), (iv): 0 failures.

## 4. Lemma STRETCH (SIGNED)
- (1): a non-cycle-node switch at a level > M changes COARSE_M(Ξ(y)).
  - The candidate new successor z′ could have y in its H_t-path set, but above M that would contradict COARSE_M(Ξ_{t+1} z′) =
    COARSE_M(Ξ_t z′), since z′'s H_{t+1}-path avoids y. So adding y keeps the difference above M.
  - A cycle node switches at level −1 (CN).
  - A switch at level ≤ M lands on the same COARSE_M.
  Correct.
- (2): within one COARSE_M class, β decides first. Correct.
- (3): a level-M tail has b bad and best target good. R15 (a) and constancy keep b good, and a later level-M gate needs b bad. Correct.
- The argument at a later fallback k′ uses only the state k′ ∈ [k+1, e]. So it also excludes k′ = e, which matters for PL (a)
  (FBW-2, §5).
- DATA: tails never repeat inside a constant-COARSE_M run of a block (172 library + 75 named blocks, max block 37 = cl9_rep_b); 0 failures.
  - (My first probe version counted a tail with two level-M gates at one fallback twice and reported false repeats. Fixed: a tail is a
    vertex, not a gate.)

## 5. Theorem PL and Corollary PL-S (SIGNED WITH GAP FBW-2)
- (a): FLAT-ALL (iii) at f_i (i < N; (h) at f_i + 1 since S continues) shows the block's fallback transitions do not change COARSE_M. So
  [f_1, f_N] splits into ≤ 1 + D_M constant runs, and each fallback has a level-M tail (FB step (2)).
  - FBW-2 (wording): STRETCH is stated for fallbacks k with s ≤ k < e. For i < N, f_i < e of its run, but f_N may be the run's last state
    e (when COARSE_M changes at f_N's own transition).
  - STRETCH's step (3) excludes a repeated tail at any k′ ≤ e. So N ≤ n_E(1 + D_M) holds. State STRETCH with "k ≤ e" (repeat excluded at
    every fallback k′ ∈ (k, e]). Closed.
- (b): M_{f_i+1} ≤ M (FLAT-ALL (iv)). TRANSFER keeps M_t ≤ M while COARSE_M is unchanged, so j's relevant Even changes are ≤ M and j is S4a.
  U-loc with L = M forces a relevant σ̄(o) change above M: an ε-transition. OR (c) and TC-SPLIT give the θ-level, and OR (a)-(b) with H1
  give the absorption. Correct.
- (c): CLS1's (A_t) chain, NL (ii) (no leave at S4a steps) and ABS-L.
  - N_x counts exits in R. It rises at each absorption and falls only at block fallbacks (REL_M).
  - N_x ≤ d_o − 1 at every state, because H1 holds throughout S. So the SN-1 issue (H1 at the end state) does not arise.
  - Each dirty interval has its own first absorption. Correct.
- PL-S: blocks are disjoint, there are ≤ n levels, and the REL_M are disjoint. Correct.
- DATA:
  - 172 (library) / 75 (named) blocks: N ≤ n_E(1 + D_M) and the PL (c) bound hold.
  - D_M = 0 in EVERY block (max_D 0), so PL (b)'s and (c)'s substantive content (dirty intervals) is never exercised. They rest on the
    proof; NJB's prediction holds in all data.
  - Blocks with r > M at every state of [f_1, f_N]: 88 (library) / 36 (named). The packet's §7 says 156 / 69, which is likely a different
    reading of "throughout"; not a disagreement about any statement.

## 6. Data (DATA, not proof; docs/referee/scratch/fbw_probe.py, sha1 2812aefb…; own N5 trace asserted equal to n5.run; scope runs with key
(λ_Ξ, λ_U, τ); 𝒞^1O asserted except in the general-game FBW / P-OPT runs)
| run | games | Even fallbacks / gates | scope runs / in-scope fallbacks | failures |
| --- | --- | --- | --- | --- |
| named (experiments/si/coarse/named.txt + instances/*.pg) | 65 | 272 / 837 (equal to the packet) | 70 / 256 (252 THR u* ≠ none, 4 EQ) | 0 |
| library (every experiments/**/*.pg in 𝒞^1O with n ≤ 64; 252 files at e69772b3) | 252 | 798 / 2,618 | 204 / 605 | 0 |
| climb bests box9 (cl9_heq_b 7535a99c, cl9_rep_a 9d31fb39, cl9_rep_b 8efbbc9e) | 3 | 97 / 99 (equal to the packet) | 3 / 71; blocks 3, max 37, D 0 | 0 |
| rand general n 4-14 seed 9301; n 10-20 seed 9302 | 6,000 | 162 / 170 | — | 0 |
| rand 𝒞^1O n 8-24 seed 9303 | 4,000 | 211 / 225 | 892 / 142 EQ | 0 |
- cl9_heq_b / cl9_rep_a / cl9_rep_b: n5.py 29/27, 40/33, 45/37; check_sol2.py "zielonka(oink zlk) OK strategies verified" on all three.

## 7. Labels after this report (D18/L40)
- PROVED (L-SI successor 4; signed by REFEREE (Opus 5.5, D15), second referee pending):
  - FBW on every game;
  - on 𝒞^1O: FBW-S, CLS2, FLAT-ALL (FBW-1), STRETCH, PL (a)-(c) (FBW-2) and PL-S.
- CONJECTURE: NJB, NJ-INT. OPEN: r-drop blocks, level −1 fallbacks, REL(S), G-N5-TIME. Not a TARGET.md claim; the TARGET.md diff is empty.

## Fixes-file lines (one per gap)
- FBW-1: §3 (i): "That cycle is y′'s honest H_{k+1}-cycle; it does not contain o, else H1 would fail at k+1" (replaces "o's W-cycle …
  against H2").
- FBW-2: §4 statement: "… at most once among the fallbacks k of S with s ≤ k ≤ e" (the proof's step (3) covers k′ = e); §5 (a) then
  covers the block's last fallback.

## §C. Comparison with REFEREE-2 (R2-N5-FBW, referee-2 2596285); written 2026-10-25 07:00Z onward by date -u
Read only after my report (9a94dc7b) was pushed and the Lead said R2-N5-FBW exists (07:05Z). At my fetch, trunk 83bf81a1 did not yet
contain the file, so I read it from origin/claude/referee-2 at 2596285.

### C.1 Verdicts
| statement | REFEREE | REFEREE-2 | joint |
| --- | --- | --- | --- |
| P-OPT / G-1OA-6 | VALID | VALID | VALID (same reason: G-1OA-6 concerns S4c's installed σ_{k+1}; P-OPT uses S4a's output σ_k at state k) |
| FBW | SIGNED | SIGN | SIGNED by both |
| FBW-S, CLS2 | SIGNED | SIGN | SIGNED by both; (H-EQ) closed |
| FLAT-ALL | SIGNED WITH GAP FBW-1 | SIGN | SIGNED by both; FBW-1 see C.2 |
| STRETCH | SIGNED | SIGN (N-FBW-1) | SIGNED by both |
| PL (a)-(c) | SIGNED WITH GAP FBW-2 | SIGN | SIGNED by both; FBW-2 = N-FBW-1 |
| PL-S | SIGNED | SIGN | SIGNED by both |
No verdict differs. Neither referee found a counterexample.

### C.2 Item by item
- FBW-2 = N-FBW-1. The same point, found independently, with the same repair: STRETCH's "s ≤ k < e" must read "k ≤ e" for PL (a)'s last
  block fallback f_N. REFEREE-2 adds the reason f_N's own transition may change COARSE_M: FLAT-ALL (iii) needs (h) at f_N + 1, which the
  scope run need not give. I accept that sharper reason. I filed it under PL (a), REFEREE-2 under STRETCH; one fixes-file line covers both.
- FBW-1 (FLAT-ALL (i): the switched cycle node's new cycle avoids o by H1, not H2): REFEREE-2 did not raise it. Its §3 repeats the
  packet's "H2 at k+1". I keep FBW-1, and here is why H2 is not enough.
  - Let y′ ∈ F_k be a switched own cycle node. If y′'s (σ_{k+1}, τ)-play reached o, its honest play would agree with it up to o.
  - Since λ(y′) = y′ (phase), the honest play returns to y′, so o lies on y′'s honest cycle: ¬H1 at k+1.
  - H2 (o on no W-cycle) does not exclude this. The (σ, τ)-play continues from o to τ(o) ∈ F, which need not lead back, so y′ would simply
    be in R̄_{k+1} without o being on a W-cycle.
  - So the correct citation is H1 at k+1, which "(h) at k+1" includes. The statement is unaffected. This is a citation correction, not a
    verdict difference. I ask REFEREE-2's successor (or the Lead) to note it in the joint record.
- Data:
  - P-OPT is checked by both: REFEREE-2 checks every arena single switch (44,611 library, 3.44 M in climbs); I check every gate switch,
    with a non-fallback control that fires 1,061 / 1,164 times.
  - D_M = 0 in every block for both of us. REFEREE-2 adds three dirty-interval climbs (8,000 runs) that found none. So PL (b)/(c) are
    vacuous in all data, and NJB is unrefuted.
  - Counts differ by starts and selection (REFEREE-2: 3 starts, 249 blocks; me: canonical start, 172 blocks). Statements agree.

### C.3 Joint gap map (one fixes-file line per row)
| row | REFEREE | REFEREE-2 | status | fixes-file line |
| --- | --- | --- | --- | --- |
| 1 | FBW-2 | N-FBW-1 | wording, closed | §4 STRETCH: "… at most once among the fallbacks k of S with s ≤ k ≤ e" (step (3) covers k′ = e; PL (a) needs it for f_N, whose own transition may change COARSE_M since (h) at f_N + 1 is not given) |
| 2 | FBW-1 | — (text repeats "H2") | citation, closed | §3 FLAT-ALL (i): "That cycle is y′'s honest H_{k+1}-cycle; it avoids o, else H1 would fail at k+1 (H2 alone does not exclude a (σ, τ)-play from y′ through o)" |

### C.4 Joint label (D18/L40)
- PROVED (L-SI successor 4; REFEREE and REFEREE-2, Opus 5.5, D15), pending CHECKER:
  - FBW on every game;
  - on 𝒞^1O: FBW-S, CLS2, FLAT-ALL (row 2), STRETCH (row 1), PL (a)-(c), PL-S.
- CONJECTURE: NJB, NJ-INT. OPEN: r-drop blocks, level −1 counts, REL(S), G-N5-TIME.
