# R221 LADDER, re-climbing and ρ at SET gates vs CANDIDATE N5′-xi (L-RED successor 56; Lead GO 23:02Z 2026-11-07)
Box (Lead): (1) adversary vs L-NEW 62's [LOC]-at-gates lemma (WAITING for its SHA); (2) LADDER: Ξ-cyclic genomes whose hub plays climb
k upward Ξ-edges, k growing; (3) ρ at SET gates. Labels: PROVED (lane, unrefereed) / PROVED-CONDITIONAL (named premise) / CONJECTURE /
DATA (unit, set, scope, counter) / DEAD (instance) / READING. Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN; N5′-xi stays a
CANDIDATE (D1). Tools: experiments/red/r221/ (own.py = R220's copy of R217's independent IDEAL-CYC run; lad221.py, ladclimb.py,
wit221.py, rho221.py; xcheck.py = R218's four-route check). No L-NEW code is used except inside xcheck.py's second routes.

## 0. Answers (milestone 1, 23:2xZ; milestone 2, 23:3xZ: RHO-E PROVED)
- (2) No family with R superlinear in N. The ladder question splits in two, and only one half is a resource:
  - Ascents alone are FREE and HARMLESS. SL(k) (§2, a static SET-ladder, N 2k) has plays with k − 1 ascents = U(G), and T ≤ 2,
    R ≤ 1 for k ≤ 32. Four routes agree (k 4 / 8 / 16: own = idealcyc, Γ3 regions = Oink, n5v xi = n5bxi = 5 iterations).
  - What a counter needs is RE-CLIMBS: the first e of a vertex's play drops back to a less relevant e inside one Λ-interval (a
    re-entry), many times. Lemma NO-REFLECT (§5, PROVED from E-MON) says the hub's e-sets must then run in binary-counter (carry)
    order, never in Gray-code / Towers-of-Hanoi order. Corollary ASC-LOG (§5) says a hub with 2^k e-sets needs only about
    log₂ k ascents, not k. Lemma RUNG-ALT (§6, from SWITCH-IN-DV) says a rung that re-climbs r times needs an alternative gate with
    at least r − 1 distinct values. That alternative must also read the climb above the rung: the R218 §4 hub pair again.
  - DATA: climbs targeted at ascents (K up to 6, N up to 24) reach 3-5 ascents with R ≤ 21 (R63K5: N 18, R 21, T 27). That is in
    line with earlier R-bests (rd3_d4: N 8, R 10). Re-entries per (vertex, Λ-interval) are ≤ 3 in every climb. LEAP_k reaches k
    re-entries with 2 ascents, which is linear.
  - Mechanism (DATA, §4): on climbing plays, Odd keeps an e almost always because of RET, i.e. the β-face loops back through the
    gate. Shares: 238 / 251 (L6K4), 460 / 535 (R53K5), 852 / 872 (LEAP_k8). LAM, a different cycle node, occurs 0 times.
    So climbs ride RET stretches, and item (2) feeds item (3).
- (3) Lemma RHO-SET (§7, PROVED-CONDITIONAL on F1, lane): at a SET-type gate g (Ξ-target = its own mover x), every RET stretch
  after the first starts with an adoption of g's option at x. Between consecutive starts Ω(e_g) rises strictly. So ρ_g ≤ D(y),
  where y is g's W-target, one level lower (sharper than SWITCH-IN-DV's D(g)). Lemma RHO-E (PROVED-CONDITIONAL on F1, lane;
  milestone 2): between consecutive starts, (Λ(y), E(y)) changes, unless y's cycle node lies above e_g ([BELOW] fails; A_g).
  - Corollary RHO-COUNT: ρ_g ≤ (2M + 3)·F′_B(M) + A_g, with B the number of ascents of y's plays and B ≤ U(G) (UP-B). So Σρ_g over
    SET gates is polynomial when U(G) = O(1) and ΣA_g is polynomial (needs [E-LEV] for UP-B; A_g = 0 in all data).
  - DATA: RHO-SET and RHO-E 0 violations on 76 gaps (73 runs: frozen L-RED instances + climbs), A_g = 0; adversarial climb §8.
- (1) Not started: L-NEW 62's lemma is not frozen yet (Lead 23:02Z).

## 1. Setting
As in R219 §1. IDEAL-CYC(G) of a genome G (RESULTS R104 shape; e above every β; [E-LEV] e-order by (level, gate)), Howard at the movers
with ties kept, Odd's optimal response by one-player SI (own.py). seq_t(v) = the e-vertices of Π_t(v) in play order. An ascent = a
consecutive pair of seq_t(v) whose second element is more relevant. U(G) = #options whose Ξ-target is a mover of higher level.
E_t(v) = set of seq_t(v). A re-entry at v = a step t − 1 → t with Λ(v) fixed, both seqs nonempty, and first(seq_t(v)) less relevant than
first(seq_(t−1)(v)). R counts σ̄-change steps (own.py labels C / R / p). F1 = values non-decreasing (box 192).

## 2. Hand ladders (lad221.py; DATA)
- LAD(k) (zig-zag a_l (level 1) e→ b_(l−1), b_j (level 0) Ξ→ a_(j+2)): inert, T 0, 0 ascents (k 2-8). Reason (FLIP-E): the e-face
  set {e(a_l)} ∪ E(b_(l−1)) contains the β-face set E(b_l), so it is lex larger, and Odd hides every e. A climbing gate needs a β
  alternative that lex-dominates the rest of the climb, or a RET loop (§4).
- SL(k) (lad221.sl): x_j (level 1) has SET (W→ y_j, Ξ→ x_j, even β) and an X-option; y_j (level 0) has Ξ→ x_(j+1) (up) and an
  X-option; gates of x_j rise with j. Start s0 = all SET, s1 = all X.
  Unit: one run per (k, start). Set: k 2, 4, 8, 16, 32. Scope: own.py. Counter: lad221.meas.

  | k | N | U(G) | max ascents | max D_E | max re-entries | T (s0 / s1) | R (s0 / s1) |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | 2 | 4 | 1 | 1 | 2 / 3 | 0 | 1 / 2 | 0 / 1 |
  | 4 | 8 | 3 | 3 | 2 / 3 | 0 | 1 / 2 | 0 / 1 |
  | 8 | 16 | 7 | 7 | 2 / 3 | 0 | 1 / 2 | 0 / 1 |
  | 16 | 32 | 15 | 15 | 2 / 3 | 0 | 1 / 2 | 0 / 1 |
  | 32 | 64 | 31 | 31 | 2 / 3 | 0 | 1 / 2 | 0 / 1 |

  UP-B is tight on SL(k). Four routes (xcheck.py, scratch copies; k 4 / 8 / 16, s1): own = idealcyc trajectory; subrun191 C 0, R 1,
  p 1; Γ3 (n 130 / 250 / 490) regions = Oink 8fbf0a7 --zlk; n5v xi 5 = spec 5 = n5bxi 5 (fallback 1); verify 0 / 0.
  Frozen: experiments/red/r221/inst/SL_k{2,4,8,16,32}_s{0,1}.json (inst/SHA1SUMS).

## 3. Climbs toward ladders (ladclimb.py; DATA)
Score (lexicographic) = (min(max ascents, K), R, T). Mutations retarget Ξ (upward allowed) and W, swap β ranks, flip β parities, swap
gates, change starts. Seeds: LAD(k) or random genomes (d levels × w movers, 2 options). Unit: best genome of one climb (3000-6000
iterations). Set: the 14 runs below. Scope: own.py (cap 3000 steps). Counter: lad221.meas on the best genome.

| run | seed / K | N | U | ascents | max D_E | T | C | R | max flips / gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L4K3 | LAD 4 / 3 | 8 | 4 | 3 | 3 | 12 | 5 | 6 | 6 |
| L6K4 | LAD 6 / 4 | 12 | 7 | 4 | 9 | 11 | 0 | 10 | 5 |
| L8K5 | LAD 8 / 5 | 16 | 9 | 4 | 5 | 12 | 3 | 8 | 4 |
| L10K5 | LAD 10 / 5 | 20 | 17 | 5 | 6 | 20 | 5 | 13 | 8 |
| L12K6 | LAD 12 / 6 | 24 | 13 | 5 | 5 | 23 | 6 | 13 | 8 |
| R33K3 | 3×3 / 3 | 9 | 5 | 3 | 5 | 11 | 3 | 7 | 5 |
| R43K4 | 4×3 / 4 | 12 | 9 | 3 | 4 | 13 | 5 | 7 | 4 |
| R53K5 | 5×3 / 5 | 15 | 14 | 4 | 10 | 15 | 1 | 11 | 8 |
| R63K5 | 6×3 / 5 | 18 | 14 | 4 | 13 | 28 | 4 | 21 | 7 |
| R83K6 | 8×3 / 6 | 24 | 17 | 4 | 3 | 25 | 11 | 8 | 9 |
| R44K4 | 4×4 / 4 | 16 | 13 | 4 | 4 | 14 | 4 | 6 | 4 |
| R62K5 | 6×2 / 5 | 12 | 12 | 3 | 7 | 16 | 5 | 10 | 6 |
| R102K6 | 10×2 / 6 | 20 | 19 | 4 | 8 | 26 | 7 | 13 | 14 |
| R53K3b | 5×3 / 3 | 15 | 11 | 3 | 7 | 16 | 3 | 12 | 9 |

(Final values, batches 1-2 complete; set = these 14 runs.) Batch 3 (SCORE=reent: score = max re-entries at one (v, Λ-interval);
8 runs, N 8-18, 4000 iterations): max re-entries 1 / 5 / 3 / 1 / 1 / 2 / 4 / 3 (E22 / E24 / E28 / E32 / E33 / E34 / E43 / EL6);
best E24: N 12, 5 re-entries, 3 ascents, R 8. Baseline from the Lead (23:06Z, L-SI 43 @ claude/l-si e3ac4b06, not opened by me): L-SI's
R-climbs with Ξ-cycles reach R 2 / 5 / 6 at d 2 / 3 / 4; my climbs are not R-climbs on L^R_d and use other scores. For comparison: rd3_d4 N 8 R 10, rd2_d7 N 14 R 13, LEAP_k64 N 261 R 128 (all with 2 ascents). More ascents
do not buy more R per vertex in this data.

## 4. Why Odd keeps a climbing e (wit221.py; DATA)
For every (t, v) and every e_g of seq_t(v) that is followed by a more relevant e (a climbing e, with g on the play), classify:
LAM (Λ(β_g) ≠ Λ(e_g)), RET (β-play of g passes g), EST (equal Λ, not RET: then E(β_g) >lex E(e_g) by FLIP-E; EST_ABOVE = the top of
the symmetric difference is above every later e of the climb). Unit: (t, v, e) triples. Scope: own.py. Counter: wit221.py.

| instance | LAM | RET | EST | EST_ABOVE | FLIP-E failures |
| --- | --- | --- | --- | --- | --- |
| L6K4 | 0 | 238 | 13 | 13 | 0 |
| R53K5 | 0 | 460 | 75 | 32 | 0 |
| L4K3 | 0 | 73 | 2 | 0 | 0 |
| rd3_d4 | 0 | 32 | 2 | 0 | 0 |
| LEAP_k2 / k4 / k8 / k16 | 0 | 90 / 264 / 852 / 2988 | 8 / 12 / 20 / 36 | 4 / 4 / 4 / 4 | 0 |

Re-entries (same script; unit: (v, Λ-interval)): max 3 (L6K4, R53K5), 1 (rd3_d4), 0 (L4K3); LEAP_k2 / 4 / 8 / 16: 2 / 4 / 8 / 16.
Lex decreases of E(v) inside a Λ-interval: 0 everywhere (E-MON).
READING: a climbing e is held either by a Ξ-loop back into its own gate (RET; with SET options that is case (ii) of GATE-REARM) or by a β
alternative that lex-dominates the rest of the climb (EST, Odd-reading). LAM never occurs. So ω(1) climbs are made of RET stretches, and
their count is ρ (§7).

## 5. Lemma NO-REFLECT and Corollary ASC-LOG: which recursion a re-climbing hub needs (D18 angle)
**Lemma NO-REFLECT (PROVED, lane; from E-MON of P-N5-ASC §3 @ l-new 95dc76d7, which survived R220).** Fix v and a maximal interval I
with Λ(v) fixed. Write E_t(v) as a 0/1 word indexed by the e-vertices in relevance order (most relevant = most significant). Then the
words E_t(v), t ∈ I, form a non-decreasing sequence of binary numbers. So a step that clears the most significant changed bit is
impossible inside I.
- Proof: lex order on e-sets compared by their most relevant differing element is exactly numeric order of these words. E-MON says
  E_t(v) is lex non-decreasing on I. ∎
- Corollary (Gray / Hanoi DEAD as hub dynamics). Suppose E(v) runs through the binary-reflected Gray code on k e-vertices, or any
  sequence with one bit flipped per change. Of its 2^k − 1 steps, 2^(k−1) − 1 clear a bit. Each such step is a numeric decrease, so
  it needs a change of Λ(v). Λ(v) takes at most 2M + 3 values (DESC-ALL count, box 192 X-GATE). So 2^(k−1) ≤ 2M + 3, i.e.
  k ≤ log₂(2M + 3) + 1. The Towers-of-Hanoi recursion T(k) = 2T(k−1) + 1 with a reflected second half is the same sequence. So it
  survives only for O(log M) bits.
- What survives is the binary carry recursion T(k) = 2T(k−1) + 1 in which the carry into bit i clears bits < i in the SAME change as
  it sets bit i (+1 at the low end). In the hub's play this is a re-entry: the hub stops entering bit 0 and enters bit i directly.
  Later it re-enters lower bits as they set again. A re-climbing counter therefore needs about 2^(k−1) re-entries at its hub inside
  one Λ-interval (READING). Data so far: ≤ 5 in re-entry-targeted climbs (E24, N 12), k at LEAP_k (N 4k + 5) (§3, §4).
**Corollary ASC-LOG (PROVED, lane; from HUB-ASC-G and UP-B @ l-new 95dc76d7).** If some vertex has D_E ≥ 2^k inside one Λ-interval,
the plays of that vertex need B ascents with F′_B(M) ≥ 2^k. Since F′_B(M) ≤ (2M)^(5·2^B − 3) for M ≥ 4 (induction: F_0 ≤ M², F_(B+1) ≤ 4M³F_B²), that means
B ≥ log₂ k − log₂ log₂ M − O(1), and also U(G) ≥ B.
- Computed: log₂ F′_B(M) for B = 0..4 is M 16: 7.1 / 26.4 / 65.2 / 142.6 / 297.4; M 64: 11.0 / 40.1 / 98.3 / 214.6 / 447.4;
  M 128: 13.0 / 47.1 / 115.1 / 251.3 / 523.7. At M = 64, B = 2 already allows 2^64 e-sets.
- READING (D18): the F′ recursion F_B ≈ M·F_(B−1)² squares at each ascent. The play splits at an ascent into a low segment and a high
  segment, and lex order on (high, low) is a two-digit counter in base F_(B−1). This is a van Emde Boas / repeated-squaring recursion
  (k bits → two halves, depth log k), not a Hanoi recursion (depth k). A k-rung ladder (one ascent per bit) is therefore NOT what an
  exponential counter must look like. The cheapest one would be a nested two-segment hub of depth about log k. Neither form is built.
  The game-side obstruction to either is the RE-ADOPTION count of §6, not the number of ascents.

## 6. Lemma RUNG-ALT: re-climbing is re-adoption (PROVED-CONDITIONAL on F1, lane; corollary of SWITCH-IN-DV, R218 §1)
Let x be a mover on a hub's climb (a rung) that adopts its climbing option o r times. Then D(g_o) ≥ r. Between two adoptions x sits on
some other option, so some option o′ ≠ o is adopted at least r − 1 times, and D(g_(o′)) ≥ r − 1.
- Proof: SWITCH-IN-DV for o and for the options adopted in between. Adoptions of o and of other options alternate, so other options
  are adopted at least r − 1 times. These spread over at most deg(x) − 1 options, so one of them is adopted at least
  (r − 1)/(deg(x) − 1) times; at degree 2 that is r − 1. ∎
- Reading: in the binary carry order, rung j re-adopts about 2^(k−j) times. So its alternative gate takes about 2^(k−j) distinct
  values, which needs the alternative's play to read the varying part of the climb above j. Its X-option (to K0) has D = 1 and allows
  ≤ 1 re-adoption. That is exactly why SL(k) is static. A re-climbing ladder is therefore a pair of hubs (climb, alternative) per rung
  that overtake each other at every carry. This is the R218 §4 hub-pair crux, now with a rung-wise lower bound on its values. OPEN.

## 7. ρ at SET gates (item 3)
Setting: g = gate of option k of x with Ξ-target x (SET type), lev(x) ≥ 1, W-target y, β-vertex b. RET_t ⇔ σ_t(x) = k and τ_t(g) = e.
While σ(x) = k, g's β-face is the cycle g b x g with Λ = b and Π = ∅. Call its value L: fixed, and below every value whose Π holds an e.
**Lemma RHO-SET (PROVED-CONDITIONAL on F1 and on Odd playing an optimal response; lane).**
(a) If σ_(t−1)(x) = σ_t(x) = k and τ_(t−1)(g) = β, then τ_t(g) = β. So every maximal RET stretch that starts at s ≥ 1 starts with an
adoption of k at x.
(b) If s < s′ are consecutive stretch starts, then Ω(e_g) rises strictly at some step inside (s, s′).
(c) ρ_g ≤ 1 + #strict rises of Ω(e_g) ≤ D(e_g) ≤ D(y).
Proof.
- (a) τ_(t−1)(g) = β with σ_(t−1)(x) = k means L ◁ Ω_(t−1)(e_g). The values differ: Λ = b with Π = ∅ on one side, and on the other
  side Λ = b only if e_g ∈ Π. F1 gives Ω_t(e_g) ⊵ Ω_(t−1)(e_g) ▷ L, and the β-face is again L, so Odd's optimal response keeps β.
- (b) Let t1 := the last t < s′ with σ_t(x) = k (t1 ≥ s) and g′ := σ_(t1+1)(x). Howard moved off k: Ω_(t1)(g′) ▷ Ω_(t1)(g).
  max_o Ω_t(g_o) is non-decreasing (F1 per gate). At s′ Howard adopts k: Ω_(s′−1)(g) ⊵ Ω_(s′−1)(g′) ⊵ Ω_(t1)(g′) ▷ Ω_(t1)(g).
  Since g is Odd's, Ω_(s′−1)(g) ⊴ Ω_(s′−1)(e_g).
  - If τ_(t1)(g) = e: Ω_(t1)(g) = Ω_(t1)(e_g), so Ω_(s′−1)(e_g) ▷ Ω_(t1)(e_g), a strict rise inside (t1, s′ − 1] ⊆ (s, s′).
  - If τ_(t1)(g) = β: L ◁ Ω_(t1)(e_g) ⊴ Ω_(s′)(e_g) (F1). But at s′, σ = k and τ = e, so Ω_(s′)(e_g) ◁ L. Contradiction.
- (c) The intervals (s, s′) of different consecutive pairs are disjoint. Ω(e_g) is a function of Ω(y) (single edge e_g → y). ∎
**Lemma RHO-E (PROVED-CONDITIONAL on F1 and Odd's optimal response, lane; replaces the CONJECTURE and the sub-lemma GAP-RETURN of
milestone 1).** Let s < s′ be consecutive RET starts at a SET gate g, and t1 := the last t < s′ with σ_t(x) = k. Assume [BELOW]:
Λ_(t1)(y) is less relevant than e_g. Then (Λ(y), E(y)) at s′ − 1 differs from (Λ(y), E(y)) at t1.
Proof. Suppose not: Λ(y) = w and E(y) = E_y at both t1 and t := s′ − 1. Put E := {e_g} ∪ E_y.
- y's play never passes x: otherwise it passes g and e_g (σ(x) = k at t1), and the cycle contains e_g, so w ⊵ e_g, against [BELOW].
  Hence at both times Λ(e_g) = w and E(e_g) = E (e_g ∈ Π because w is less relevant than e_g).
- At t1, τ(g) = e (RHO-SET (b)), so x's play is x g e_g y …: Λ_(t1)(x) = w and E_(t1)(x) = E. Movers and gates are less relevant than
  any cycle node, so they are never in Π.
- At t, σ_t(x) =: u ≠ k. Howard adopts k at s′, so Ω_t(g) ▷ Ω_t(u). As g is Odd's, Ω_t(e_g) ⊵ Ω_t(g). x's value has the same Λ and Π
  as u's. F1 at x gives Ω_t(x) ⊵ Ω_(t1)(x). So Λ_t(x) has reward between reward(w) and reward(w), i.e. Λ_t(x) = w.
- Suppose E_t(x) ≠ E. Let ε be the most relevant e in E Δ E_t(x). With equal Λ, two values are compared by the top of the symmetric
  difference of their Π's. When the e-parts differ, that top is ε: every non-e more relevant than an e is c_W, K0 or K3, which lie on
  both plays or on neither (E-DOM-ALL-d). The e-parts of Π_t(x) Δ Π_(t1)(x) and of Π_t(u) Δ Π_t(e_g) are both E Δ E_t(x).
  - If ε ∈ E_t(x), then Ω_t(u) ▷ Ω_t(e_g). Contradiction.
  - If ε ∈ E, then Ω_(t1)(x) ▷ Ω_t(x). Contradiction with F1.
- So E_t(x) = E ∋ e_g, i.e. x's play at t passes e_g, hence g. But g's only in-edge is from x, and x's play follows σ_t(x) = u ≠ k
  each time it is at x. Contradiction. ∎
**Corollary RHO-COUNT (PROVED-CONDITIONAL on F1, lane).** For a SET gate g: ρ_g ≤ 1 + #changes of (Λ(y), E(y)) over the run + A_g,
where A_g is the number of gaps violating [BELOW]. #changes ≤ (2M + 2) + Σ_I (D_E,I(y) − 1), and E is lex-monotone on each Λ-interval
I (E-MON). With HUB-ASC-G: ρ_g ≤ (2M + 3)·F′_B(M) + A_g, with B the max ascents of y's plays, and B ≤ U(G) under [E-LEV] (UP-B).
So Σρ_g over SET gates is polynomial when U(G) = O(1) and ΣA_g is polynomial. A_g counts gaps whose y-cycle node lies above e_g: the
analogue of R219's H_g (DATA 0 in every run, below).
DATA (rho221.py; unit: gates of level ≥ 1, and gaps between consecutive RET starts at SET gates; set: all frozen L-RED instances
r217-r221 inst/ plus the §3 climbs, 73 runs, file out/rho221_all.txt; scope: own.py): RHO-SET violations 0; RHO-E gaps 76: violations
0 (whole-gap form and endpoint form), gaps outside [BELOW] 0 (A_g = 0);
max ρ_g at one gate 5 (SW_k8s16, CYC type), at a SET gate 3 (L10K5); max over gates of ρ_g / (D_E(y)·L(y)) = 1.00; Σρ_g ≤ 1.5·N
everywhere (max R62K5; LEAP_k: Σρ = 2k + 1).

## 8. Adversarial climbs against RHO-SET / RHO-E (batch 4; RUNNING at milestone 2)
ladclimb.py with SCORE=rho: score = (RHO-SET + RHO-E violations, max ρ at a SET gate, R, T); Ξ-retargets favour SET options. Results
in out/H*.log when done. At milestone 2 (partial, 7 of 8 runs started): violations 0; max ρ at a SET gate 6 (H34, N 12), 5 (H25,
H43), 4 (H23, N 6).

## 9. Next
1. Item (1): L-NEW 62's [LOC]-at-gates lemma, when frozen (own.py on LEAP_k64, rd3_d4, R217-R219 runs first).
2. CYC-type RET gates (Ξ-loops longer than a self-loop): does RHO-SET / RHO-E extend? Then bound A_g (gaps with y's cycle node above e_g).
3. A two-hub rung (§6) in the carry order of §5, smallest k = 2 with two re-entries at one Λ-interval beyond LEAP's mechanism.
