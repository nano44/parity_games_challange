# R2-N5-FBC: REFEREE-2 report on packet P-N5-FBC (FB-RISE_C, SAT_C, Theorem FB-C, Corollaries (a)-(d))
Referee: REFEREE-2 successor 17 (session_01P2K6kCftytexWsuJfNFtV4), Opus 5.5 (D15, L37). Written 2026-10-26 14:40Z (date -u).
Object: docs/new/P-N5-FBC-box47.md, sha1 32d3776cf4090fb15c1d0cb4c8b4f59276f64e21 (`git show de02d37e:… | sha1sum` and the same at l-new
1f8d6d7d), 138 lines, pinned at trunk de02d37e, frozen. Author L-NEW successor 26. Reviewed as a new object; my predecessor's R2-N5-HONFF
(same box, FB-RISE) is a reference, since FB-RISE_C's Even case is FB-RISE (a)'s items 2-3 verbatim.
Independence: written before opening any REFEREE file on FBC or CHOSEN. `git fetch origin claude/referee` + `git ls-tree --name-only -r
origin/claude/referee docs/referee/ | grep -ic -e fbc -e chosen` gave 0 at 13:34Z, 0 at 14:38Z, and 22 at 14:51Z, the push turn (REFEREE pushed its
own FBC and CHOSEN material between 14:38Z and 14:51Z; I saw file NAMES in that listing only, opened nothing, and this report's text,
verdicts and notes were final before 14:51Z). The count is read from that command's output, never from a template. The lane's tools (experiments/new/box47/*.py) were NOT run or imported.
Checker: docs/referee-2/R2-N5-FBC/fbc_check.py (own; on my lane's R2-N5-HONFF/honff_check.py path enumeration and R2-N5-HON/hon_check.py
state loop; Ξ, W are my own play values, cross-checked against the engine every state: ENGXI). LEV_C EXACT per (phase, configuration) by
enumeration of all simple H_C-paths to cycle nodes of λ, with a budget; over budget, an iterative-deepening mode (DEEP) computes min(LEV_C, D)
for the least D that still decides every fallback source of that configuration, so those sources are checked exactly too.
Quote check: own script docs/referee-2/R2-N5-FBC/quotes.py (independent of the lane's quotecheck.py).
Scope (D1): FB-C bounds f per phase by the DISTINCT CONFIGURATIONS at fallback sources; that number is itself unbounded on general games
(Π_q deg(q) in the worst case). Nothing here bounds N5's running time. Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Verdicts
| item | verdict | premises (checked) |
| --- | --- | --- |
| §1 Lemma FB-RISE_C | SIGN | SPEC S2, S4c, FIX 3; (MON) = R15 (a), (d) via (VJ) under P1; R17 (V1), (V2); Lemma P Case A with Ω := Ξ_t (P-N5-HONFF's Q-A, answered YES by both referees) |
| §1 Lemma SAT_C | SIGN | LEV_C's definition; honest play at a C-state is an H_C-play; (MON); R15 (d) |
| §1 Theorem FB-C (f ≤ \|𝒞_f(P)\|·(4n² − 3n)) | SIGN | FB-RISE_C, SAT_C, LEV_C monotone, LEV_C ≥ 0 |
| §2 Corollary (a) | SIGN | FB-C; one configuration per epoch; a configuration is a choice per q ∈ Q |
| §2 Corollary (b) (𝒞^kO, Δ^k·(4n² − 3n)) | SIGN | (a) with \|Q\| = k, Π_q deg(q) ≤ Δ^k |
| §2 Corollary (c) (\|D_k\| ≤ 1: 1 + Σ_q(deg q − 1) ≤ 1 + m; general \|D\| ≤ d form) | SIGN | (a); D's definition imported silently (N-FBC-3) |
| §2 Corollary (d) (with R61 (f)) | SIGN | (a); R61 (f) |
| header: "(a)'s N_ep form and (d) are WEAKER than landed R60 (c) EPOCH" | CONFIRMED for n ≥ 2; FALSE only at n = 1 (vacuous) | arithmetic below, §2 |
| §6 quotes (14) | all VERBATIM at l-new 80509398 and at trunk de02d37e (same line numbers) | own quotes.py |
No gap. Notes N-FBC-1..6 (§3). Not reviewed (as briefed and as the packet asks): §3 (τ-frame context / dead charge), §4 (DATA), §5 (OPEN),
the READINGs.

## 1. Proof check
- Setting. H_C := G with every Odd v cut to σ̄_C(v); C ranges over configurations σ̄|Q. LEV_C(k) is defined at EVERY state of P (it reads only
  Ξ_k and the paths of the FIXED graph H_C), and is non-decreasing on P by (MON) with λ fixed in the phase. CORRECT, and the independence of
  LEV_C from the state's own configuration is what the whole-phase count needs.
  - LEV_C(k) ≥ 0 at every state: the only 0-edge paths are x = u for a cycle node u of λ, and λ(x) = x gives Ξ_k(x) = (x, ∅, 0) = value(r)
    throughout the phase. So the unsaturated values lie in {0, …, n − 2}, as FB-C's count needs (the packet does not say this; N-FBC-1).
- FB-RISE_C (fallback t → t+1 in-phase, source t a C-state). In-phase ⇒ Even's fallback (FIX 3), λ_{t+1} = λ, S4c switches every Even x with
  Iσ_t(x) ≠ ∅ to the (Ξ_t(w), w)-maximum z*(x). For r = x → z → r′ a simple H_C-path with |r| ≤ j := min(LEV_C(t) + 1, n − 1): |r′| ≤
  LEV_C(t), so Ξ_t(z) ⪰ value(r′).
  - x ODD. In H_C the only edge at x is to σ̄_C(x), so z = σ̄_C(x) = σ̄_t(x) (t is a C-state; outside Q the successor is unique), hence x's
    honest play at t is x then z's. λ(x) ≠ x: (V1) gives Ξ_t(x) = x ⊕ Ξ_t(z) with z's honest path to λ(x) avoiding x; r′ avoids x (r simple);
    (V2) gives Ξ_t(x) ⪰ x ⊕ value(r′) = value(r); (MON) to t + 1. λ(x) = x: Ξ_t(x) = (x, ∅, 0), z's play returns to x so Ξ_t(z) has cycle
    node x, value(r′) has cycle node u ≠ x (r simple, \|r\| ≥ 1), and Ξ_t(z) ⪰ value(r′) with different cycle nodes forces rew(x) > rew(u),
    so (x, ∅, 0) ≻ value(r). CORRECT. The conclusion is reached AT t, i.e. the Odd half of LEV_C is automatically one level ahead at a
    C-state — the packet's READING, and the exact point where the honest frame beats the τ-frame (in G_τ an Odd vertex of D can undercut its
    τ-path; LEV_odd is then needed, P-N5-HONFF's FB-RISE (a)).
  - x EVEN. Items 2 and 3 of FB-RISE (a)'s proof, which I re-read line by line in the H_C frame: item 2 (z non-improving) is Lemma P's Case
    A with Ω := Ξ_t, ρ := σ_t, whose hypothesis is exactly Ξ_t(z) ⪯ Ξ_t(σ_t x), then (MON); item 3 (z improving, so x is switched) uses
    Ξ_t(z*) ⪰ Ξ_t(z) ⪰ value(r′), (MON), and at t + 1 (V1)/(V2) in 3a and the cycle-node comparison in 3b. Every ingredient reads only: the
    G-edge (x, z) (Even vertices keep all their edges in H_C, as in G_τ), the bound value(r′) ⪯ Ξ_t(z), S4c, Case A, (MON), (V1), (V2),
    λ_{t+1} = λ. None reads the frame of r′, so the import is sound. CORRECT.
  - The C-state hypothesis is used ONLY in the Odd case; the Even case holds at every state (N-FBC-2).
- SAT_C. At a C-state t the honest play from x follows σ_t at Even and σ̄_C at Odd vertices, i.e. it is an H_C-play, and its prefix to the
  first visit of λ(x) is a simple H_C-path r_x with Ξ_t(x) = value(r_x) ⪯ B_C(x). LEV_C(t) = n − 1 covers every simple path (≤ n − 1 edges),
  so Ξ_t ⪰ B_C, hence Ξ_t = B_C. For a later C-state t′: Ξ_{t′} ⪯ B_C = Ξ_t ⪯ Ξ_{t′} (MON), so Ξ is constant on t, …, t′ (Ξ non-decreasing),
  and with τ constant on P, R15 (d) gives t′ − t ≤ 4n(n − 1). CORRECT. (Ξ_{t′} ⪯ B_C uses only that t′ is a C-state.)
- Theorem FB-C. Per C ∈ 𝒞_f(P): consecutive unsaturated sources have LEV_C(t_{i+1}) ≥ LEV_C(t_i + 1) ≥ LEV_C(t_i) + 1 (FB-RISE_C, monotone,
  t_i + 1 ≤ t_{i+1}), and LEV_C ∈ {0, …, n − 2} there, so at most n − 1 of them; saturated sources are C-states after the first saturated
  C-state, so SAT_C puts them in 4n(n − 1) + 1 consecutive states. (n − 1) + 4n(n − 1) + 1 = 4n² − 3n. Each in-phase fallback source is a
  C-state for exactly one C, and that C is in 𝒞_f(P), so f ≤ \|𝒞_f(P)\|·(4n² − 3n). CORRECT.
- Corollaries. (a): distinct configurations ≤ N_ep (an epoch has one configuration) and ≤ Π_q deg(q); 𝒞_f(P) ⊆ the visited configurations.
  (b): \|Q\| = k on 𝒞^kO and Π_q deg(q) ≤ Δ^k. (c): with \|D_k\| ≤ 1 the visited configurations are τ|Q and its one-vertex deviations, at most
  1 + Σ_q(deg(q) − 1) ≤ 1 + m; the general \|D\| ≤ d count Σ_{j≤d} C(\|Q\|, j)(Δ − 1)^j is the choice of the deviating set and its targets.
  (d): (a) with R61 (f). All CORRECT.

## 2. The header's comparison with R60 (c) EPOCH (the Lead's question), checked
- EPOCH (c) (landed, RESULTS R60): f ≤ 1 + n·N_ep. (a)'s N_ep form: f ≤ (4n² − 3n)·N_ep. Difference: (4n² − 3n)N_ep − (1 + n·N_ep) =
  N_ep(4n² − 4n) − 1, which is > 0 for every n ≥ 2 (N_ep ≥ 1), so (a)'s N_ep form is WEAKER, as the header says. At n = 1 it is −1, i.e. the
  FB-C form is numerically smaller; that case is vacuous (one vertex, Q = ∅, N_ep = 1, f ≤ 1 either way). So: CONFIRMED for n ≥ 2, with the
  n = 1 exception (N-FBC-4). My checker asserts the n ≥ 2 form at every phase with a fallback (CMP_header_Nep_form_not_weaker, 0 failures).
- (d) against the landed EPOCH + R61 (f) (f ≤ 1 + n(1 + Σ_q(ρ_q + tie_q + nc_q + cyc_q))): same algebra with K := 1 + Σ ≥ 1, difference
  K(4n² − 4n) − 1 > 0 for n ≥ 2. So (d) is WEAKER too, as the header says. CONFIRMED (n ≥ 2).
- What FB-C adds over EPOCH, checked quantitatively. FB-C beats EPOCH exactly when \|𝒞_f(P)\|·(4n − 3) < N_ep. In every phase of my data the
  ratio N_ep/\|𝒞_f\| stayed far below 4n − 3: the maximum ratio is 45.0 at n = 32 (lev_l_sc.pg phase at state 8: N_ep 45, visited
  configurations 15, \|𝒞_f\| 1), against 4n − 3 = 125. So the counters CMP_fbc_below_epoch and CMP_fbc_below_r56 are 0 in all 50,000+ runs:
  the FB-C bound never beat EPOCH's or R56's number anywhere in my data (N-FBC-5). The structural claim ("a configuration that recurs is paid
  once", so (b) and (c) are not implied by EPOCH) is CORRECT as a statement about the FORM of the bound; the packet's own §2 bullet cites
  1,399 epochs against 257 configurations, which is a ratio of 5.4, well under 4n − 3. I also confirm the recurrence itself: configurations
  repeat inside a phase (visited 1,100 against 1,934 epochs in the library runs), so the per-configuration reading is not vacuous.
- R56 (f) (f ≤ 1 + (n − 1)(2 + ρ)) and FB-C are incomparable as FORMULAS (different quantities, neither factor dominates), which is what the
  header claims; in DATA, as above, FB-C's number was never the smaller one.

## 3. Notes (no gap)
- N-FBC-1 (completeness of FB-C's count). The unsaturated count "with values in {0, …, n − 2} there are at most n − 1 of them" needs LEV_C ≥ 0
  at every state of P. It holds (0-edge paths exist only at cycle nodes of λ, where Ξ = (x, ∅, 0) throughout the phase), but the packet does
  not say it. One sentence in §0 or in FB-C's proof would close it.
- N-FBC-2 (hypothesis strength). FB-RISE_C's Even case uses only LEV_C's definition at t, S4c, Case A, (MON), (V1), (V2): it holds at ANY
  source state, not only a C-state. The C-state hypothesis is needed exactly for the Odd case (z = σ̄_C(x)). Worth stating, since it says
  where the configuration frame is actually paid for.
- N-FBC-3 (imported definition). §2 (c) uses \|D_k\| ≤ 1, but §0 imports from P-N5-HONFF §0 only "state k, σ̄_k, Ξ_k, λ, phase P, in-phase,
  value(r)", and D is defined in P-N5-HON §0 (l. 44: D_k := {q ∈ Q : σ̄_k(q) ≠ τ(q)}), not in HONFF §0. Add D to the imported list. (I checked
  that this reading is the one that makes (c) true: with D_k as above, \|D_k\| ≤ 1 at every state gives exactly the configurations τ|Q and its
  one-vertex deviations. My checker asserts \|D_k\| = \|{q : σ̄_k(q) ≠ τ(q)}\| at every state, 0 failures.)
- N-FBC-4 (the header's "weaker"). True for n ≥ 2, false at n = 1 (vacuously). Either say "for n ≥ 2" or ignore; it changes nothing signed.
- N-FBC-5 (where the bound stands, DATA). The FB-C number never beat EPOCH's or R56's in any phase I ran (max N_ep/\|𝒞_f\| = 45 at n = 32,
  threshold 4n − 3 = 125). The gain is the form, not the number, on the data available.
- N-FBC-6 (thin spot, as the packet's §5 says). SAT_C's saturated branch is barely exercised: max 1 saturated source per (phase,
  configuration) in every set, and the longest window between a saturated C-state and a later one is 2 transitions, against the bound
  4n(n − 1). My control "at most 1 saturated source per C" (MUT=sat) therefore does NOT bite on the library: SAT_C's 4n(n − 1) + 1 term is
  untested, and FB-C's bound is in practice decided by the unsaturated term.

## 4. Data (DATA, not proof; logs in docs/referee-2/R2-N5-FBC/logs/, reproduce with run_all.sh; logs_v1/ = the first pass, before the DEEP mode)
| set | runs | states | phases | phases with a fallback | f | configs at sources (Σ\|𝒞_f\|) | visited configs / N_ep (those phases) | (phase, C) pairs with exact LEV_C (DEEP: deepened / still UNK) | fallbacks checked by FB-RISE_C (unsat / sat) | Q-A checks in H_C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| named instances (s4c8_n13, j5_n16, j10_n24, j7_n32, j8_n32, farrise25_n32, zcl_rx_n32, wd16_s2, lap_n6_s1_110421, lev_l_x, rise_thin51_n40, b5_o11, ffin12_n32, ffin5_n32, ffin4_n24 (+ .start), immp_cex_n11 (+ .start), fr39_q4_n48 (+ L-RED's start, budget 3·10⁷) | 17 | 583 | 64 | 18 | 140 | 33 | 104 / 218 | 18 exact (8 deepened, 7 UNK) | 117 (116 / 1) | 4,490,631 |
| lib41 minus referee games × 3 starts | 1,230 | 19,383 | 7,208 | 253 | 1,090 | 305 | 1,100 / 1,934 | 138 exact (89 deepened, 78 UNK) | 586 (545 / 41) | 11,018,221 |
| my 503 𝒞^1O files × 2 starts | 1,006 | 17,986 | 4,164 | 347 | 2,017 | 414 | 1,359 / 2,425 | 188 exact (138 deepened, 88 UNK) | 1,025 (975 / 50) | 16,916,468 |
| random 2 Odd choice vertices, n 5-12 (3,000 × 3) | 9,000 | 21,100 | 19,837 | 256 | 256 | 256 | 257 / 257 | 256 exact | 256 (0 / 256) | 2,467 |
| random 4 Odd choice vertices, n 6-14 (2,000 × 3) | 6,000 | 16,296 | 15,532 | 187 | 187 | 187 | 188 / 188 | 187 exact | 187 (1 / 186) | 2,165 |
| random, all Odd vertices with choices, n 6-16 (1,500 × 3) | 4,500 | 12,426 | 11,701 | 123 | 123 | 123 | 123 / 123 | 123 exact | 123 (0 / 123) | 1,890 |
0 violations in every set, of: FB-RISE_C (2,294 fallback sources checked exactly, 1,637 of them unsaturated so the rise is a real
constraint), the Odd case alone at every C-state (ODDC; 2,551 more checks in the deepened mode), LEV_C's monotonicity over whole phases,
Ξ_t = a simple H_C-path value and Ξ_t ⪯ B_C at every C-state (XIB, 5,067 states), SAT_C's Ξ = B_C and its window (2,336 checks), FB-C's
per-C counts and the f bound, Corollaries (a)-(d) including the general \|D\| ≤ d form (58,506 phases), the D-definition identity, and Lemma P's
Case A pointwise in H_C (32,431,842 checks). Maxima: f 37 in one phase (rise_fb38_n48, \|𝒞_f\| 1, N_ep 3); \|𝒞_f\| 4 (elimn_cex_n48,
zcl_rx_n32); unsaturated sources of one configuration 25 (farrise25_n32, n 32, bound n − 1 = 31); saturated per configuration 1 everywhere;
saturated window 2 transitions (tog6b_n32); deepening depth needed 14 (x31_rx32, rx32_best).
Controls (must fail): plus2 (FB-RISE_C with LEV_C(t) + 2) 298 failures on the library; tau (LEV read in G_τ instead of H_C, i.e. dropping the
configuration frame) 14,399 failures (554 of them FB-RISE_C itself, 2,659 the Odd case) — the honest frame is what makes the Odd case free;
sat ("at most 1 saturated source per C", the packet's §5 hope) 0 failures, i.e. it does NOT bite (N-FBC-6).
UNK: in the table's runs (budget 3·10⁶) 173 (phase, configuration) pairs stayed over budget even after deepening, covering 1,519 fallback
sources; they are skipped for the LEV_C checks and counted here. Re-running the six worst named instances at budget 3·10⁷ (run_big.sh, logs
big_*.txt) decides nearly all of them: j7_n32, j8_n32 and lev_l_x come out fully decided (0 UNK), and ffin12_n32, rise_thin51_n40 and
zcl_rx_n32 keep one undecided configuration each; 31 more fallback sources are checked exactly there, all passing.

## 5. Signatures
Lemma FB-RISE_C, Lemma SAT_C, Theorem FB-C, Corollaries (a), (b), (c), (d): SIGN, on every game, under the standing SPEC premise 1E-N3 (in
form P1, through (MON)) and P-N5-HONFF's question Q-A (answered YES by both referees; if Q-A were "no", FB-RISE_C falls with FB-RISE, as the
packet's header says). No gap. The header's claim that (a)'s N_ep form and (d) are weaker than the landed R60 (c) EPOCH: CONFIRMED for n ≥ 2
(n = 1 vacuous exception, N-FBC-4). Notes N-FBC-1..6. REFEREE-2 successor 17 (Opus 5.5, D15).
