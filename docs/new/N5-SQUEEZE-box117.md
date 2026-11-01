# N5-SQUEEZE (box 117): N5's two valuations squeeze every vertex monotonically — PROVED (lane), FAILS for TBR and ARSB on switchbestexp; blind on L-RED's builds, where ARSB is fast and N5 is slow
L-NEW successor 43, 2026-10-31 (date -u: after 21:00Z). Lead brief (start of successor 43), BOX 117: find ONE statement that FAILS for
ARSB or TBR on switchbestexp_N but plausibly holds for N5, using S4b's arena-restricted Odd step (or S4a against the current τ), not just
S4a; test it on the corpus, on L-RED's builds and on switchbestexp; prove it (lane) if possible; label PROVED / CONJECTURE / DATA.
ERRATUM (successor 43, box 118 start, reported to the Lead 22:2xZ): Lemma SQUEEZE below is NOT new. It is landed RESULTS R18 (d):
Lemma R (box 21 §2.1, G^d's order is the exact reverse of G's = Fact DUAL-ORDER) and Lemma S (b) (box 21 §2.2: L_σk ⊴ V_σk,τk ⊴ U_τk,
L non-decreasing, U non-increasing), SIGNED WITH GAPS (S1, S2, G-1OA-6) by both referees. Read «PROVED (lane)» on SQUEEZE as «= landed
R18 (d) Lemma S (b), re-derived». New in this box: its role as the N5 / TBR / ARSB separator (DATA), SETTLE-MON, BRACKET-MON and
SETTLE-RED / BRACKET-RED (lane), and all the DATA.
Labels: PROVED (lane), DATA, READING, OPEN. No count is bounded here. G-N5-TIME stays OPEN. This is not M3 and not a TARGET.md claim.

## 0. Answer
- The statement (PROVED (lane), §1): Lemma SQUEEZE. For every N5 run, every k and every vertex v,
  LO_k(v) ⊴ LO_(k+1)(v) ⊴ W_(k+1)(v) ⊴ HI_(k+1)(v) ⊴ HI_k(v), where
  - LO_k(v) := Ξ_(σ_k)(v), the valuation of v under σ_k and Odd's optimal counterstrategy σ̄_k (SPEC S1);
  - HI_k(v) := Ξ^d_(τ_k)(v), the valuation of v under τ_k and Even's optimal counterstrategy τ̄_k (SPEC S1 on G^d), read as the same
    (c, P, ℓ) triple in G's order;
  - W_k(v) := the valuation of the (σ_k, τ_k)-play from v.
  - So every vertex carries an interval [LO_k(v), HI_k(v)] that contains the current play's value and SHRINKS (nested) at every transition.
- Where S4b enters: HI is non-increasing only because τ moves along Odd's own improving edges (S4b's arena {τ(o)} ∪ Iτ(o); S4c's Odd
  branch picks from Iτ). The Even half (LO non-decreasing) holds for ARSB and TBR as well.
- Corollaries (PROVED (lane), §2):
  - SETTLE-MON: the settled set SET_k := {v : LO_k(v) = HI_k(v)} never shrinks, and a settled vertex keeps LO = W = HI for the rest of
    the run.
  - BRACKET-MON: lcp(LO_k(v), HI_k(v)) (common prefix of the digit vectors of box 107) never decreases. So B_k := Σ_v lcp is
    non-decreasing, with values in [0, n(n + 2)], and rises at ≤ n(n + 2) transitions.
  - REDUCTIONS (EQUIVALENCES): iterations ≤ (n + 1)·SG and iterations ≤ (n(n + 2) + 1)·BG, where SG / BG := the longest window of
    transitions without a growth of SET / a rise of B. Both are ≤ iterations, so G-N5-TIME ⟺ SG polynomial ⟺ BG polynomial.
- It FAILS for TBR and ARSB (DATA, faithful variants of box 115, §3): on switchbestexp_N, N = 2..6, HI rises at 2 / 5 / 11 / 18 / 18
  transitions under TBR and 2 / 6 / 13 / 22 / 25 under ARSB; settled vertices UNSETTLE 3 / 9 / 18 / 9 / 9 (TBR) and 3 / 9 / 18 / 30 / 45
  (ARSB) times; N5: 0 everywhere.
  - Quantitatively: N5's settle gap SG is 16 / 19 / 19 / 21 / 22, TBR's 30 / 63 / 107 / 132 / 132, ARSB's 29 / 67 / 144 / 221 / 221.
- It is BLIND where N5 is slow (DATA, §4): on L-RED's builds SET and B are flat for the whole run except the last step (SG = BG = iterations:
  fbg_K12_m6_m24 404, s3quad_K8_m30 264, fb3_K4_m6_m12_m12 135 of 159). On the same builds ARSB stops in 2 to 23 iterations.
  - READING: the separation is two-sided. τ moving only by Odd's own improvements protects N5 on switchbestexp (Odd never re-arms Even's
    carry). The same staleness is what L-RED's builds exploit: N5's Even plays for a long time against a τ that Odd's best reply would
    already have abandoned.
- So SQUEEZE is the N5-specific lemma the Lead asked for, but it does not bound anything inside a τ-stretch. The open core (XI-CH, the
  W-run / STAIR reductions) is untouched.

## 1. Lemma SQUEEZE — PROVED (lane)
- Premises:
  - [1E-N3-S1] (the standing SPEC premise of RESULTS R57): S1's procedure realises the pointwise optimum. On G, σ̄ minimises the
    valuation of every vertex at once against σ; on G^d, τ̄ does the same in G^d's order against τ.
  - RESULTS R15 (a) Lemma A, valid in any game, so on G and on G^d: switching a non-empty set of improving edges of a strategy gives a
    pointwise ⊵ valuation (⊵^d on G^d).
  - SPEC S4 with FIX 3: σ_(k+1)(y) ∈ {σ_k(y)} ∪ Iσ_k(y) for every Even y (S4a's arena; S4c's Even branch picks from Iσ_k); and
    τ_(k+1)(o) ∈ {τ_k(o)} ∪ Iτ_k(o) for every Odd o (S4b's arena; S4c's Odd branch picks from Iτ_k, and only when Iσ_k = ∅).
  - [LEX] (RESULTS R93): the order is linear.
- Fact DUAL-ORDER. For every play, its triple (c, P, ℓ) computed in G^d equals the one computed in G, and G^d's order on triples is the
  reverse of G's.
  - Proof. Ranks of G and G^d coincide (SPEC A3: Ω + 1 keeps the order and the index ties). p′^d(u) = 2·rank(u) + 1 − (Ω(u) mod 2), so
    for u ≠ c, p′^d(u) > p′^d(c) ⟺ rank(u) > rank(c) ⟺ p′(u) > p′(c). Hence c (the maximum of the cycle) and P agree, and ℓ is a step
    count.
  - Order: with p′(c) = 2r + b, reward(c) = 2r if b = 0 and −(2r + 1) if b = 1, while reward^d(c) = −(2r + 1) if b = 0 and 2r if b = 1. So
    reward^d = −reward − 1, which reverses the cycle-node comparison. The weight of every u ∈ P changes sign (Ω(u) changes parity), which
    reverses the P comparison. The length rule («c odd: longer is better for that game's Even») is applied with c's parity flipped and
    the players exchanged, so it orders lengths the same way for Even of G, i.e. reversed for Even of G^d. □
- Definitions: LO_k(v) := Ξ_(σ_k)(v); HI_k(v) := Ξ^d_(τ_k)(v) as a triple in G's order (DUAL-ORDER); W_k(v) := the valuation of the
  (σ_k, τ_k)-play from v.
- Statement. For every N5 run on every game, every vertex v, every state k ((a)) and every transition k → k + 1, fallback or not ((b), (c)):
  (a) LO_k(v) ⊴ W_k(v) ⊴ HI_k(v); (b) LO_k(v) ⊴ LO_(k+1)(v); (c) HI_(k+1)(v) ⊴ HI_k(v).
- Proof.
  - (a) LO_k(v) is the minimum over Odd's strategies of the (σ_k, ·)-play valuation [1E-N3-S1 on G], and τ_k is one of them. HI_k(v) is
    the G^d-minimum over dual-Odd strategies, i.e. by DUAL-ORDER the G-maximum over Even's strategies, of the (·, τ_k)-play valuation
    [1E-N3-S1 on G^d], and σ_k is one of them.
  - (b) If σ_(k+1) = σ_k there is nothing to show. Otherwise σ_(k+1) differs from σ_k exactly on a non-empty set of edges of Iσ_k (S4
    premise), so R15 (a) on G gives LO_(k+1) ⊵ LO_k pointwise.
  - (c) The same on G^d: τ_(k+1) differs from τ_k only on edges of Iτ_k, so R15 (a) on G^d gives Ξ^d_(τ_(k+1)) ⊵^d Ξ^d_(τ_k), which is
    HI_(k+1) ⊴ HI_k by DUAL-ORDER. □
- Where the proof uses N5's Odd step: only in (c), through «τ_(k+1)(o) ∈ {τ_k(o)} ∪ Iτ_k(o)», i.e. S4b's arena restriction. (a) and (b)
  hold verbatim for ARSB and TBR (with O_k := σ̄_k for ARSB, τ_k for TBR in place of τ_k).

## 2. Corollaries — PROVED (lane)
- SETTLE-MON. Let SET_k := {v : LO_k(v) = HI_k(v)}. Then SET_k ⊆ SET_(k+1), and for v ∈ SET_k and every j ≥ k:
  LO_j(v) = W_j(v) = HI_j(v) = LO_k(v).
  - Proof. For v ∈ SET_k with a := LO_k(v) = HI_k(v): a ⊴ LO_j(v) ⊴ W_j(v) ⊴ HI_j(v) ⊴ a by SQUEEZE (b), (a), (c) and induction on j;
    [LEX] gives equality. □
- BRACKET-MON. Let cs(·) be box 107's digit vector (reward of the cycle node; the signed bits of P by rank, top first; the signed length;
  n + 2 coordinates, lexicographic order = Even's order), and lcp the length of the common prefix. Then lcp(cs LO_k(v), cs HI_k(v)) is
  non-decreasing in k.
  - Proof. Box 107 Lemma SANDWICH: x ⊴ y ⊴ z ⇒ lcp(x, z) = min(lcp(x, y), lcp(y, z)). With a := LO_k(v) ⊴ a′ := LO_(k+1)(v) ⊴
    b′ := HI_(k+1)(v) ⊴ b := HI_k(v) (SQUEEZE): lcp(a, b) ≤ lcp(a′, b) and lcp(a′, b) ≤ lcp(a′, b′). □
  - So B_k := Σ_v lcp(cs LO_k(v), cs HI_k(v)) is non-decreasing with values in [0, n(n + 2)], and rises at ≤ n(n + 2) transitions.
- SETTLE-RED and BRACKET-RED (EQUIVALENCES). Let SG (BG) be the most consecutive transitions with no growth of SET (no rise of B). Then
  iterations ≤ (n + 1)·SG and iterations ≤ (n(n + 2) + 1)·BG, and SG, BG ≤ iterations. So G-N5-TIME ⟺ SG is polynomial ⟺ BG is
  polynomial.
  - Proof. SET grows at ≤ n transitions (it never shrinks), so the run splits into ≤ n + 1 windows without growth; likewise ≤ n(n + 2) + 1
    windows for B. □
- None of this bounds SG or BG. The reductions are stated to show what SQUEEZE alone can and cannot carry (§4).

## 3. It FAILS for TBR and ARSB on switchbestexp_N (DATA; box117/squeeze.py, box117/sep.py; instances and starts of box 115)
- Variants exactly as box115/abl.py (same VJ engine): TBR = S4a against τ_k, τ_(k+1) := σ̄_k; ARSB = S4a with σ̄_k for τ_k. O_k is the
  Odd strategy Even's step is taken against (τ_k for N5 / TBR, σ̄_k for ARSB); HI_k := Ξ^d_(O_k). SANDV (LO ⊴ HI violated) and LODROP are 0
  in every row (the Even half holds for all three, as §1 says).

| N | n | iters N5 / TBR / ARSB | HI rises (transitions) N5 / TBR / ARSB | UNSET N5 / TBR / ARSB | settle gap SG N5 / TBR / ARSB |
| --- | --- | --- | --- | --- | --- |
| 2 | 60 | 32 / 53 / 58 | 0 / 2 / 2 | 0 / 3 / 3 | 16 / 30 / 29 |
| 3 | 85 | 41 / 97 / 135 | 0 / 5 / 6 | 0 / 9 / 9 | 19 / 63 / 67 |
| 4 | 110 | 47 / 155 / 258 | 0 / 11 / 13 | 0 / 18 / 18 | 19 / 107 / 144 |
| 5 | 135 | 55 / 209 / 364 | 0 / 18 / 22 | 0 / 9 / 30 | 21 / 132 / 221 |
| 6 | 160 | 62 / 217 / 412 | 0 / 18 / 25 | 0 / 9 / 45 | 22 / 132 / 221 |

- The same runs, Odd side (sep.py; O-moves, those NOT in Iτ(O_k), O-returns, returns with no strict dual rise of the target):
  - N5: 2 / 3 / 4 / 5 / 6 moves, 0 outside Iτ, 0 returns.
  - TBR: 4 / 11 / 24 / 41 / 46 moves, 2 / 5 / 13 / 20 / 23 outside Iτ, 2 / 8 / 20 / 36 / 40 returns, 1 / 4 / 12 / 26 / 27 with no dual rise
    (ODD-RETURN of box 116 fails).
  - ARSB: 4 / 11 / 26 / 51 / 64 moves, 2 / 6 / 13 / 24 / 33 outside Iτ, 2 / 8 / 22 / 46 / 58 returns, 1 / 5 / 15 / 35 / 41 with no dual rise.
- The trace (squeeze.py with its 5th argument: per-state |SET|): N5's settled set on switchbestexp_2 grows 4 → 60 from state 16 on and
  never shrinks. ARSB's stays at 4 for 29 states, grows to 12, falls to 11 (an Odd re-optimisation) and stays there 9 states while the
  carry is replayed, then grows to 60. At N = 3 it happens twice: 12 → 11 for 28 states, then 21 → 18 for 11 states.
- READING: every unsettling is an Odd move that is not an Odd improvement (it is an Odd best reply to the CURRENT σ). It re-opens
  intervals that Even had already closed, and Even's carry is re-run inside the re-opened intervals. SQUEEZE forbids exactly that.

## 4. Where it is blind: L-RED's builds (DATA; box117/runred.sh, valid / repaired starts of box 116b)
| build | n | N5 iters | N5 SET growths / SG | N5 B rises / BG | ARSB iters |
| --- | --- | --- | --- | --- | --- |
| cp_K4 | 192 | 44 | 1 / 44 | 1 / 44 | 2 |
| suf_K4 / suf_K8 | 103 / 199 | 44 / 152 | 1 / 44, 1 / 152 | 1 / 44, 1 / 152 | 2 / 2 |
| fbA_K4_m8_m8 / fbA_K8_m8_m8 | 136 / 192 | 44 / 88 | 1 / 44, 1 / 88 | 1 / 44, 1 / 88 | 2 / 2 |
| fbg_K4_m6_m24 / K4_m6_m48 | 178 / 250 | 140 / 236 | 9 / 132, 9 / 228 | 9 / 132, 9 / 228 | 8 / 8 |
| fbg_K8_m6_m24 / K12_m6_m24 | 234 / 290 | 272 / 404 | 9 / 264, 9 / 396 | 9 / 264, 9 / 396 | 8 / 8 |
| s3quad_K8_m30 | 479 | 264 | 1 / 264 | 1 / 264 | 2 |
| fb3_K4_m6_m12_m12 (R165) | 215 | 159 | 25 / 135 | 25 / 135 | 23 |
| topfix_n10 | 210 | 64 | 62 / 3 | 62 / 3 | 73 |

- N5 never violates SQUEEZE on them (HI rises 0, UNSET 0). ARSB's HI rises once on fb3 and on topfix, with no unsettling.
- On every build designed against N5, SET and B are flat for (almost) the whole run: SG = BG ≈ iterations. N5 is slow while its τ
  stays put; ARSB, which re-optimises Odd every step, finishes in 2 to 23 iterations.
- READING: the builds keep τ frozen and drive Even's long climb inside one τ-stretch, below a constant HI. In that regime LO climbs to a
  point that is still lexicographically far from HI (no digit of LO agrees with HI until the end), so SQUEEZE sees no progress.
  - The finer bracket C_k := Σ_v lcp(W_k(v), HI_k(v)) (W against the CURRENT τ) does rise inside these stretches: its longest gap is
    10 / 18 / 32 / 32 / 56 on cp_K4 / suf_K8 / fbg_K12 / s3quad / fbg_K4_m48. But C is box 107's FROZEN potential with HI in place of the
    W-run end W_q (HI ⊵ W_q). It is monotone only where W is (W-MON: τ-constant, fallback-free), it drops at τ-changes and fallbacks
    (long121_n40: 8 drops), and box 107 already showed that a W-anchored bracket alone is DEAD (x31_rx48). Not pursued as a new statement.

## 5. Corpus (DATA; box117/runsqz.sh: L-SI box 53's 1,132 runs, box 113's repaired starts; outputs q_sbcg.txt, q_alt.txt)
- 0 violations of SQUEEZE (SANDV, LODROP, HIRISE all 0), of LO ⊴ W ⊴ HI (SANDW 0), of SETTLE-MON (UNSET 0) and of BRACKET-MON (B drops 0).
  These are proved statements; the zeros check the implementation (and cs's order agrees with the engine's in every comparison, CSV 0).
- At every stop SET = V (1,132 / 1,132). (Not used anywhere; it reflects that the final σ and τ are both optimal.)
- Gaps: SG ≤ 3.41n and BG ≤ 2.91n on the whole corpus (both on n5-epoch/instances/lend107_n32: n 32, 112 iterations, SG 109, BG 93);
  largest absolute s3quad_K8_m30 (SG = BG = 264 = iterations).
  - Summed over the corpus: iterations 21,845, SG 15,611, BG 12,256, CG 9,000. So on most runs the bracket moves only near the end.
- C (§4) drops at 674 τ-constant transitions over the corpus (at fallbacks and λ_W changes), as expected from W-MON's premises.
- READING: SG ≤ 4n and BG ≤ 3n hold on the corpus and on every L-RED build tested (the builds reach SG / n = 1.37 on fbg_K12_m6_m24).
  These are NOT stated as conjectures. A bound on BG is G-N5-TIME (BRACKET-RED), and on the long runs BG ≈ iterations: the data
  give no sign that B carries information the iteration count does not.

## 6. What this means (READING)
- SQUEEZE separates N5 from ARSB / TBR. (Box 116's ODD-RETURN rests on the same Odd-side monotonicity, HI's half, and fails with
  it (§3); box 116 did not test it on the variants.) SQUEEZE is PROVED for N5 from SPEC, the S1 premise of R57 and R15 (a), and it
  FAILS for both variants on switchbestexp_N for every N tested. By §1 (c), HI can rise only at a transition where some Odd move leaves
  Iτ; on switchbestexp these moves do raise HI (TBR at N = 4: 13 Odd moves outside Iτ, HI rises at 11
  transitions).
- It explains switchbestexp: Friedmann's switch-best mechanism needs Odd to re-open closed intervals (unsettle) so that Even's carry can be
  replayed; N5's τ never re-opens one.
- It does not explain N5's speed in general, and it cannot: the attack builds live inside one τ-stretch, where HI is constant and SQUEEZE
  degenerates to «LO is non-decreasing and bounded by a constant», true of every SI run. There, ARSB is the faster rule.
- So a proof of G-N5-TIME needs SQUEEZE (or something that implies it) for the τ-side, PLUS a bound on Even's climb inside a τ-stretch
  below a fixed HI. The second half is the existing open core (W-runs: STAIR / ROOT reductions; XI-CH). Nothing here closes it.
- Possible next target (untested; not stated as a conjecture): inside a τ-stretch HI is fixed, and HI(v) is Even's OPTIMAL value against
  τ. Does Even's S4a climb inside a τ-stretch reach HI in polynomially many steps relative to the one-player game G_τ (Odd fixed to τ)?
  That is a ONE-PLAYER question for Even (S4a restricted to Iσ, which is computed against σ̄, not against τ). On L-RED's builds ARSB, which
  uses the same Iσ but plays against σ̄, stops in 2 to 23 iterations, so the slowness comes from optimising against the stale τ inside
  that arena (READING, not tested further).

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box117/ (squeeze.py, sep.py, runsqz.sh, runred.sh, pincheck.sh; outputs q_sbcg.txt, q_alt.txt,
  q_red.txt (squeeze.py with the C columns), sbx_456.txt, pincheck.txt; inst/fb3_K4_m6_m12_m12 copied unchanged from l-red b31f9477); check.sh pin «box 117 SQUEEZE».
  - Faithfulness: N5 runs are n5x.step (SPEC). fb3_K4_m6_m12_m12, the one instance new to L-NEW: n5b = n5x «identical state sequences:
    True» (159 iterations), Oink 8fbf0a7 --zlk and --tl verified, equal regions, N5's regions agree. switchbestexp_2..6 as in box 115.
- FINDINGS:
  - PROVED (lane) SQUEEZE: LO ⊴ W ⊴ HI with LO non-decreasing and HI non-increasing (HI's half uses S4b's arena restriction);
    SETTLE-MON, BRACKET-MON; REDUCTIONS SETTLE-RED / BRACKET-RED (G-N5-TIME ⟺ SG poly ⟺ BG poly).
  - DATA: SQUEEZE FAILS for TBR and ARSB on switchbestexp_2..6 (HI rises 2-25 transitions, 3-45 unsettlings; SG 30-221 vs N5's 16-22).
  - DATA: on L-RED's builds SQUEEZE is blind (SG = BG ≈ iterations up to 404) and ARSB solves them in 2-23 iterations.
- NEEDS: Lead: route the τ-stretch one-player question (§6, last item) or another box.
