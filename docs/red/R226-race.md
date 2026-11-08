# R226 item 2 (D18 own item): the DEPTH-2 RACE, and the «events ≤ |E_U| − 1» sharpening (L-RED successor 60, Opus 5.5, D1 / D18 / D14; 2026-11-08, date -u)
Box R226 (Lead «go» 11:14Z). Engine: R221 own.py (IDEAL-CYC Howard on Γ(G), [E-LEV], my own independent implementation), cap 3000.
Labels: PROVED (lane, unrefereed) / CONJECTURE / DATA / DEAD. Every DATA line names its counter, unit, set and scope.
Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN.
Tools in experiments/red/r226/:
- compose226.py: union, rewire, add_opt, check.
- sweep226.py, d2fam226.py, digit226.py: the three families.
- nest226.py: generalized type-II census.
- ex226.py, exshow226.py, sharp226.py: the sharpening tests.
- trace226.py, vals226.py: traces.
Frozen instances: experiments/red/r226/inst/ (sha1 in inst/SHA1SUMS).

## 0. Answers
| question | answer | label |
| --- | --- | --- |
| Does depth 2 multiply (factor 4 per level) or add? | ADDS in every family I built: T ≤ 15 against 10 + 10 for a sequential pair, and maxD ≤ 12 against CX4's 11. No doubling (§2). | DATA (weak: sampled families, one climb) |
| «events ≤ \|E_U\| − 1» in every LEAPFROG-ASC unit | FALSE. Frozen witnesses SHARP_EU1 (\|E_U\| = 1, one event) and SHARP_EU2 (3 movers, \|E_U\| = 2, two events) (§3) | DEAD |
| The correct sharpening | Lemma SHARP: #events ≤ \|E_U\| − 1 + 2k + ε, where ε = 1 iff the first event has M = e_S. Tight on SHARP_EU1 / EU2 (§3) | PROVED (lane), from box 87's (F2), Claim A, the counting step and PRIV |
| The unified conjecture | CONJECTURE NEST-POLY, stated in §4 (quantity, bound, scope) | CONJECTURE |
| maxalt (L-NEW BOX 197) next to X, D, T | NOT RUN: asc197.py is not on origin (claude/l-new head 8b67d40e6 at 11:2xZ; 2f4167cd not fetched) | — |
| Trap found in my predecessor's random row | leap225.py's `rand` aggregate starts max-keys at 0. So R225-leap §2's random «maxexcess 0» was an artifact. The true value is 0 too, but for a real reason (§3). | fix noted (no edit to R225 files) |

## 1. What CX4_n21's slow High is (READING from traces: vals226.py, trace226.py)
- e-relevance among level 1: e10 < e15 < e9 < e13 < e14 < e8 ([E-LEV]: level, then gate rank 6, 10, 13, 27, 32, 34).
- The High source x17 runs a 2-DIGIT COUNTER: {e13} < {e14} < {e9, e8} < {e13, e8} < {e14, e8}.
  - The low digit is e9 / e13 / e14, from x17's options to x9, x13, x14.
  - The carry is e8. It enters through x9 → x7 → x8. x2's switch (t 6) then carries it to the other low routes, since x13 and x14 have e → x2.
  - The low digit then RESETS: {e14} is followed by {e9, e8}, and e13 and e14 re-enter with e8 (top re-entries in L-NEW's sense).
- Each counter value is held exactly 2 steps (changes at t = 1, 3, 5, 7, 9). That is because the race x0 / x10 / x18 inserts the bonus e10 at every
  even step.
- So T = 10 = 2 × 5 = (race factor) × (counter length). The hub's D = 11 = T + 1.
- A MULTIPLYING depth would need one of two things. Either a race whose output is the slow High of another race (hold 4: T = 4 × 5), or a third
  counter digit above e8 (10 values, each held 2 steps: T = 20). Both were built as families (§2).

## 2. Depth-2 builds (DATA). Counter: T (own.py steps), maxD (max #distinct e-sets at one vertex on a Λ-interval), X (comp225 additive
excess at the max-(X, D) hub), Hn17 (max #distinct values of x17 on a Λ-interval). Scope: own.py IDEAL-CYC, [E-LEV], cap 3000.
| family (unit: one genome) | built how | size | count | max T | max maxD | max Hn17 | T histogram (main) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CX4_n21 (reference) | R225 X-climb | N 21 | 1 | 10 | 11 | 6 | — |
| SEQ: union(CX4, CX4) + one Ξ-rewire (sweep226.py) | all 3 gate placements (above / below / interleaved) × every option of one copy × every mover of the other copy, both directions | N 42 | 4,413 | 15 | 11 | — | 10: 4,323; 11-15: 90 |
| D2R: CX4 + router r (2 options into the High chain) + bonus mover f (W r) + FEEDBACK option at x17 → f or r (d2fam226.py, seed 2611) | the Lead's shape; targets in H = {x9, x10, x13, x14, x15, x17, x18, x19}; ranks sampled | N 23 | 3,000 | 12 | 12 | — | 6: 1,077; 10: 1,643; 11: 211; 12: 6 |
| DG3: CX4 + digit mover h (gate rank top w.p. 1/2) + router p + one new option at c ∈ {x2, x7, x9, x17, x18} → h or p (digit226.py, seed 2621) | third-digit attempt; all targets sampled | N 23 | 3,000 | 12 | 12 | 8 | (Hn17, T) = (6, 10): 1,622 |
| T-climb from DG3's best (climb225.py, seed 2631, 2,500 iterations) | R225 mutations | N 23 | 1 | 15 | 16 | — | — |
- Best genomes frozen: inst/CC2_n42.json (SEQ best: copy-A x7 option 1 Ξ → copy-B x2, gates «above»; T 15), inst/D2R_n23.json (T 12, maxD 12,
  X 4), inst/DG3_n23.json (T 11, maxD 12, Hn17 8).
- Reading of the table:
  - SEQ composes sequentially: T ≤ 10 + 5. One copy's counter restarts the other's tail, and maxD never exceeds a single copy's 11.
  - D2R and DG3 add at most 2 to T and 2 to Hn17. A multiply would show T ≈ 20 or Hn17 ≈ 12 at N 23. The T-climb, whose mutations are the
    broadest I have, also stays far below 20 (§5).
- VERDICT (DATA, weak): depth 2 ADDS. This counts as evidence for the unified conjecture (§4), not as a proof.
- Why weak:
  - The families are samples of one gadget shape each.
  - A designed third digit with a correct carry and reset of e8 (e8 must LEAVE every low route when e_h arrives) was not hand-wired. Only its
    sampled family was run.
- What would kill the verdict: a genome of size ≤ 30 with Hn17 ≥ 10 at hold 2, or T ≥ 20.

## 3. The sharpening «#events ≤ |E_U| − 1» (L-SI box 87 units; R225-leap §2)
### 3.1 DEAD as stated
- ex226.py repeats R225-leap's random census (latch225.rgen seed 2271, 3,000 genomes) with a correct max. In 28 genomes some PRIV + NODE unit has
  #events = |E_U|.
- All 28 have one shape: |E_U| = 1 (e_S is the most relevant e of the game), with one event, an ON at which a_t = {e_S} and b_t = ∅.
- Frozen: inst/SHARP_EU1.json (from rgen 2271 #1818).
- Restricting to |E_U| ≥ 2 does not save it. My climb (exclimb226.py seed 2601) found inst/SHARP_EU2.json:
  - N 3; unit B = x2, S = option 0, I = steps 0-2, |E_U| = 2.
  - Events: ON at t 0 (a = {e2.0}, b = ∅), then OFF at t 1 (a = {e2.0}, b = {e2.1}).
  - #events 2 = |E_U|.
- R225-leap's «maxexcess 0» on the random row came from leap225.py's `rand` aggregate, which starts every max-key at 0. On the 27 frozen
  genomes the sharpening does hold (max excess −1).
### 3.2 Lemma SHARP (PROVED, lane; unrefereed)
Setting: a LEAPFROG-ASC unit (B, S, I) with PRIV and NODE (L-SI box 87; R225-leap §2 definitions: a_t = π({e_S} ∪ E_t(w)), b_t = max_lex
π(E_t(g_o)) over o with node λ, M = max(a ∪ b), z = max(a Δ b); k = #type-II events).
Statement: #events ≤ |E_U| − 1 + 2k + ε, where ε := 1 if the FIRST event of the unit has M = e_S, and ε := 0 otherwise.
Moreover (P1) an event with M = e_S is a type-I ON with a_t = {e_S}, b_t = ∅, and (P2) at most one event has M = e_S, and it is the first.
Proof.
- (P1) Every element of E_U is at least as relevant as e_S, and e_S ∈ a_t ⊆ E_U.
  - So M = e_S forces a_t = {e_S} and b_t ⊆ {e_S}.
  - PRIV gives e_S ∉ π(E(g_o)) (the step R225-leap §1 uses for strictness in (F2)), so b_t = ∅.
  - An OFF needs b_t >lex a_t by (F2), which is impossible with b_t = ∅ ≠ a_t. So the event is an ON.
  - a_t ∩ b_t = ∅, so no shared head exists: the event is type I.
- (P2) Events are the flips of the boolean [σ(B) = S], so ON and OFF alternate.
  - Suppose events j < j′ both have M = e_S. Both are ON by (P1), so some OFF j″ lies strictly between them.
  - M never falls (Claim A) and M ≥ e_S always. So M_(j″) = e_S, which contradicts (P1).
  - Hence at most one event has M = e_S. By Claim A every event before it also has M = e_S, so it is the first event.
- Count:
  - Delete the first event if ε = 1.
  - Every remaining event has M ∈ E_U \ {e_S}, by (P2) and because type-II events have M ≥ head > z ≥ e_S.
  - LEAPFROG-ASC's counting (R225-leap §1: inside a run of type-I events M rises strictly, by Claim B; between runs it never falls, by
    Claim A; runs ≤ k + 1) applied to the value set E_U \ {e_S} gives ≤ (|E_U| − 1) + k + k.
  - Add ε. ∎
- What it rests on: box 87's (F2), Claim A, Claim B, the run counting, and PRIV's consequence e_S ∉ b_t. All SURVIVED in R225-leap §1. The lemma is
  only as strong as those.
- Corollaries:
  - With k = 0: #events ≤ |E_U| − 1 + ε.
  - If σ(B) = S at the start of I, the first event is an OFF, so ε = 0 and #events ≤ |E_U| − 1 + 2k.
- Tightness: SHARP_EU1 (|E_U| 1, events 1, ε 1) and SHARP_EU2 (|E_U| 2, events 2, ε 1) meet the bound with equality.
### 3.3 DATA (sharp226.py checks the bound with ε′ := [first event is an ON with b_t = ∅] ≥ ε, which is weaker, plus P1 and P2 directly)
| set (unit: PRIV + NODE unit) | units | P1 fail | P2 fail | units with ε′ = 1 | max (#events − bound) | max #events |
| --- | --- | --- | --- | --- | --- | --- |
| 28 frozen genomes (inst84 HP2-5, r223/inst_si85 ×11, inst86 ×11, CX4_n21, OFFUP_n4) | 160 (= R225-leap's 158 + OFFUP's 2) | 0 | 0 | 141 | −1 | 7 |
| random, latch225.rgen seed 2272, 3,000 genomes | 5,370 | 0 | 0 | 160 | 0 | 3 |
| adversarial climb (sharp226.py climb seed 2602; 200 restarts × ≤ 300 mutations; score = (excess, #events)) | 609 | 0 | 0 | 182 | 0 | 4 |
- No unit exceeds the bound. The bound is met with equality on random and climbed units.

## 4. The unified CONJECTURE (the READING of R225-leap §3, made exact)
Quantity (nest226.py):
- A SWITCH is a step t → t+1 at a mover x with ≥ 2 options and σ_(t+1)(x) = g_new ≠ g_old = σ_t(x).
- It is a «reward» switch when Λ_t(g_new) ≠ Λ_t(g_old).
- Otherwise let E_new, E_old be the e-vertices in Π_t(g_new), Π_t(g_old), and z = max(E_new Δ E_old).
  - The switch is TYPE II iff some e ∈ E_new ∩ E_old is more relevant than z, i.e. it is decided below a shared head. Its head is the least
    relevant such e.
- N2(G) := total number of type-II switches in the run.
- depth(G) := max over (x, maximal Λ(x)-interval) of the number of distinct heads.
**CONJECTURE NEST-POLY.** For N5′-xi on Γ3(G) (IDEAL-CYC Howard, [E-LEV]) there is a polynomial q with N2(G) ≤ q(n) for every parity game G.
NEST-POLY alone does NOT give T3 polynomial. That also needs a bound on the type-I switches between consecutive type-II switches at one mover (Status below).
- Scope: Γ3(G) and IDEAL-CYC Howard only. It is not claimed for any other improvement rule.
- It unifies two earlier conjectures:
  - TWO-COPY-RED's SET branch: SET flips are switches at B.
  - ADD(c): CX4's race x0 is a type-II switch under the shared High.
- Status: CONJECTURE. Its unproved core is how many type-I switches occur between two type-II switches at one mover. That is what LEAPFROG-ASC
  bounds at SET bits only (Lemma SHARP), and it is not proved at non-SET movers. A proof of NEST-POLY would close G-N5-TIME on Γ3.
- A strictly weaker, testable form: depth(G) ≤ c for an absolute c. This is FALSE for the SET-only depth on L-SI's HP family (R225-leap §2: 0, 2, 3, 3).
  In this switch census the depth stays ≤ 3 everywhere (table below), so a constant bound on THIS depth is not refuted.
DATA (nest226.py; unit = genome; scope own.py, cap 3000; out/nest_frozen.txt):
| set | T | switches | type I | type II (N2) | max type II per (x, I) | depth |
| --- | --- | --- | --- | --- | --- | --- |
| HP2 / HP3 / HP4 / HP5_mup | 11 / 17 / 37 / 43 | 34 / 77 / 177 / 246 | 34 / 76 / 172 / 235 | 0 / 1 / 5 / 11 | 0 / 1 / 2 / 4 | 0 / 1 / 2 / 2 |
| box 85 TC2 … TC5m, CL2_21 … CL3_32 (11) | 10-43 | 55-381 | — | 0-11 (TC5m 11, TC4m 5, CL2_21 4) | ≤ 4 | ≤ 2 |
| box 86 (11) | 8-17 | 25-89 | all | 0 | 0 | 0 |
| T-climb bests c12 / c15 / c18 (R225 §4) | 18 / 19 / 20 | 18 / 20 / 21 | all | 0 | 0 | 0 |
| X-climb best cx_leap8_2264 | 17 | 34 | 20 | 14 | 7 | 1 |
| CX4_n21 / CC2_n42 / D2R_n23 / DG3_n23 | 10 / 15 / 12 / 11 | 26 / 50 / 34 / 39 | 20 / 38 / 24 / 29 | 6 / 12 / 10 / 10 | 4 / 4 / 5 / 4 | 3 / 3 / 3 / 3 |
- N2 grows with h on L-SI's mirror family (0, 1, 5, 11 at h 2-5, while T grows 11 → 43). This growth is what
  must be polynomial. The four HP points cannot tell a polynomial from an exponential. The next measurement is HP6 / HP7, which L-SI can build.
- The depth-2 builds add type-II switches (6 → 10-12) without raising the depth (3).

## 5. T-climb from DG3 (climb225.py seed 2631, score (T, Σ(D−1)), 2,500 iterations; out/climbT_2631.*)
- FINAL: T 15, Σ(D−1) 996, maxD 16 (best genome out/climbT_2631.json). From DG3's T 11 the climb adds 4.
- That is BELOW the R225 §4 climbs from random seeds (N 12 / 15 / 18 → T 18 / 19 / 20). Seeding from the race gadget does not help T.
- No multiply: a doubled depth-2 race would sit near T 20 at this size.

## 6. Next
- A DESIGNED third digit on x17's counter. The carry must drop e8 from every low route when e_h enters, so x2 needs a second switch. This is the
  one build that could still show MULTIPLY.
- HP6 / HP7 (L-SI) through nest226.py: does N2 grow polynomially in h?
- maxalt (asc197.py) on CX4_n21, CC2_n42, D2R_n23, DG3_n23 once L-NEW's 2f4167cd is on origin.
