# R-N5-DUAL: REFEREE report on packet P-N5-DUAL (L-NEW box 43: Lemma DUAL, Theorem MIRROR, Corollary Φ-kO, Lemma ENDGAME)
Referee: REFEREE (successor 11, session_01VH2ckvgGP9CGkb8Suno5f1), Opus 5.5 (owner ruling D15, Lead reading L37).
- Routing: the Lead's message of 23:02Z (Lead's stamp), "review it AFTER P-N5-KW" (my R-N5-KW was pushed at 56ac6538 before I started).
- Object: docs/new/P-N5-DUAL-box43.md at trunk df073cb5, sha1 a51f7c30c267a4c02088cf2c849388e28c4121fa (checked with
  `git show df073cb5:docs/new/P-N5-DUAL-box43.md | sha1sum`; identical on my tree), 150 lines. Author: L-NEW successor 22.
- Written 2026-10-25T23:05Z-23:30Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/R2-N5-DUAL* file read. No lane code run or imported (mirror.py, dblfb.py, dualsym.py,
  n5x.py not run). D1: each statement treated as wrong until its proof was checked.
- Premises re-read: SPEC docs/new/N5-ssi-global.md S1-S5 (text, l. 25-60) and FIX 1-4; RESULTS R15 (a)-(d), R38 (a) KEY, R47 (a) Lemma Φ.
- Tools: own engine scratch/rl_engine.py; new probe scratch/dual_probe.py (run5 = rl_engine.run with the S4c side rule as a parameter:
  N5 or N5^OF) and climb scratch/dual_climb.py. Logs scratch/dual_logs/.

## Verdicts
| § | statement | label | verdict (Opus 5.5, D15) |
| --- | --- | --- | --- |
| §1 | Lemma DUAL, first sentence (N5 on G = mirror of N5^OF on G^d, every game, every start pair) | PROVED | SIGNED |
| §1 | Lemma DUAL, second sentence (plain N5 on G^d agrees with the mirror until the first two-sided fallback) | PROVED | SIGNED WITH GAP DUAL-1 (wording: the sentence states two different agreement points; the right one is "first possible difference at state j + 1") |
| §1 | Theorem MIRROR (a) (𝒞^1E: σ changes ≤ d_e − 1, dual phases ≤ n(n − 1) + d_e) | PROVED | SIGNED |
| §1 | Theorem MIRROR (b), as an IMPLICATION from (H-OF) | PROVED (implication) | SIGNED as an implication; (H-OF) is NOT proved (as the packet says) |
| §1 | Theorem MIRROR (c) ((H-N5) ⇒ (H-OF)) | PROVED | SIGNED |
| §1 | Corollary Φ-kO (every game) | PROVED | SIGNED |
| §1 | Lemma ENDGAME (every game) | PROVED | SIGNED |
| §2 | start / N5^OF table | to check, not to sign | READING checked in its general argument; rows spot-checked (§6); NOT a proof-by-proof audit |
| §3 | N5-MULTI §2-§4, the cross-field reading | not to sign | not signed |

Summary: every statement to sign is SIGNED; one wording gap (DUAL-1). Nothing here bounds N5's running time on any class: MIRROR (b)
is an implication whose hypothesis (H-OF) is open, and with (c) it reduces to (H-N5), which is the open 𝒞^1O per-phase question
(G-N5-TIME). Φ-kO is unconditional and polynomial for fixed k (phases only, not iterations). Not a TARGET.md claim, not a step-4 pass.

## 1. Lemma DUAL: SIGNED (first sentence), SIGNED WITH GAP DUAL-1 (second sentence)
- (E) Ω + 2 invariance. I read SPEC S1 line by line (l. 26-46). Ω enters only through rank(v) = position by (Ω(v), v), Ω(v) mod 2 (in p′,
  in reward, in the signed path-set weight, in the length rule "c odd / c even", and in the VJ case split "Ω(u) even / odd",
  "Ω(v) even / odd"), plus owners, successor and predecessor lists (index order). Ω ↦ Ω + 2 changes none. S3 uses Ω's values
  (r(w) = ±Ω(w)), but DUAL is stated for a given start pair, and S3's order is preserved by + 2 anyway. Correct.
- (S2): SPEC S1's last bullet puts Odd's side on G^d (Ω + 1, owners swapped), and S2 defines Iτ there. So G^d's Even improving set for
  its strategy τ is N5's Iτ, and G^d's Odd improving set for σ is computed on (G^d)^d = G with Ω + 2, which is N5's Iσ by (E). Correct.
- (S4a on G^d) ↔ N5's S4b: the dual of G^d's S4a arena H″ is G (Ω + 2) with G-Odd restricted to {τ(v)} ∪ Iτ(v) and G-Even fixed to σ,
  i.e. N5's H′ with Ω + 2; SPEC S4a takes "Odd's optimal counterstrategy in the dual of H″ to the dual-Even strategy", SPEC S4b takes
  "Odd's optimal counterstrategy (S1 on H′, not dual) to σ": the same S1 computation on the same arena up to Ω + 2. Correct.
- (S4b on G^d) ↔ N5's S4a: H‴ (G^d with G^d-Odd = G-Even restricted to {σ(v)} ∪ Iσ(v), G^d-Even = G-Odd fixed to τ) is the dual of N5's S4a
  arena H, and both steps run S1's Odd counterstrategy on that arena against τ. Correct.
- (S4c): N5 on G falls back on Even's side iff Iσ ≠ ∅; N5^OF on G^d falls back on its Odd's side (= G's Even) iff its Odd improving set
  (= Iσ) is non-empty. Same side always. The target rule "(valuation, index)-maximal" uses Ξσ on G, resp. on G with Ω + 2 (= by (E)),
  and Ξτ on G^d in both. Correct. S4's simultaneity ("both steps computed from the SAME (σ, τ), applied together") and S5's stop rule
  are symmetric. Induction on k: correct.
- Second sentence. The proof (N5 and N5^OF on G^d differ only at a fallback with both improving sets non-empty, which on G^d are exactly
  G's two-sided fallbacks) is correct. DUAL-1 (wording): the sentence says the runs agree "up to and including the state right after
  the first two-sided fallback's source", and then "i.e. it can differ first at state j + 1". The state right after the source j is
  j + 1, so the two phrasings contradict each other. The proof gives the second one: agreement on states 0..j, first possible
  difference at state j + 1. Fixes line: "agree on states 0, …, j; the first possible difference is at state j + 1".
- DATA (§5): DUAL exact in every run of my engine; the plain mirror first differs exactly at j + 1 in every run with a two-sided
  fallback, and never without one. On the packet's example exitr_cex_n48.pg (sha1 7a663df2, checked): first two-sided fallback at
  2 → 3 ("E2"), plain mirror differs first at state 3, N5 on G 22 iterations, N5 on G^d 23 (it falls back for Odd at 3 → 4): the
  packet's numbers, reproduced on an independent engine.

## 2. Theorem MIRROR: SIGNED ((b) as an implication)
- (a) On 𝒞^1E every Even vertex but e has one successor, so σ is determined by σ(e). Every σ-change applies a non-empty improving switch
  set to σ (S4a moves only to gate targets, R15 (d); S4c switches improving edges), so σ strictly rises in R15 (c)'s ≺, which depends on
  σ alone; no σ repeats, ≤ d_e values, ≤ d_e − 1 changes. Dual phases (λ^U, σ constant) end at a λ^U-change (≤ n(n − 1), R47 (a) (b),
  (c)) or a σ-change. Correct.
- (b) G ∈ 𝒞^1E ⇒ G^d ∈ 𝒞^1O with Odd choice vertex e and the same n. DUAL makes N5's run on G the mirror of N5^OF's on G^d; dual phases
  of the former are exactly (λ, τ)-phases of the latter (G^d's Even valuation of its strategy τ^{G^d} = G's τ is U_τ, and τ^{G^d}'s
  partner is G's σ). Memorylessness: the next state is a function of the current one (SPEC S4), so each phase is the first phase of
  the run from its first state. (n(n − 1) + d_e) · L(n) + (n(n − 1) + d_e − 1) ≤ (n(n − 1) + d_e)(L(n) + 1). Correct, as an
  implication.
- (c) Until the first two-sided fallback the N5^OF and N5 runs from x coincide. At a two-sided fallback N5^OF's Odd switch-all changes τ
  (each target is strictly improving, so differs from τ(v)), ending the phase; so the first N5^OF phase is a prefix of (or equal to)
  the first N5 phase. Correct. My probe checks this prefix property directly (MOFC, §5).
- Scope READING (𝒞^1E has unboundedly many Odd choice vertices): correct as a reading.

## 3. Corollary Φ-kO: SIGNED
- τ is determined by its values at the Odd choice vertices; no τ repeats (R15 (c) on G^d, where τ is the Even strategy); so ≤ ∏ deg(o_i)
  distinct τ's and ≤ ∏ deg(o_i) − 1 τ-changes; phases ≤ 1 + n(n − 1) + ∏ deg(o_i) − 1. The mirror the same. On 𝒞^1O it is R47's Φ-1O.
  For fixed k, ≤ n(n − 1) + n^k. Correct. (A bound on phases, not on iterations.)
- The Remark (per-vertex "τ(o_i) changes ≤ deg(o_i) − 1" false with ≥ 2 choice vertices on both sides): DATA, not signed; not re-run.

## 4. Lemma ENDGAME: SIGNED
- Iσ depends on σ alone (Ξσ is σ's valuation against Odd's optimum). Iσ = ∅ ⇒ S4a leaves σ; S4c then falls back for Odd only; σ stays,
  Iσ stays ∅. Mirror: Iτ = ∅ ⇒ S4b leaves τ; S4c falls back for Even (if Iσ ≠ ∅) or the run stops. Correct.

## 5. Data (DATA, not proof; scratch/dual_probe.py on rl_engine; logs scratch/dual_logs/)
Every run checks: DUAL (N5 on G = mirror of N5^OF on G^d, statewise, same length); PLAIN (first difference of plain N5 on G^d from the
mirror, which must come after G's first two-sided fallback j → j + 1); OM2 (N5 on G = N5 on G with Ω + 2); ENDGAME (both halves);
PHIK (distinct τ's ≤ ∏ deg(o_i), phases ≤ n(n − 1) + ∏ deg(o_i), and the mirror with σ, Even choice vertices, dual phases); MIR_A on
𝒞^1E games; MOFC on 𝒞^1O games (first N5^OF phase from a sampled state is a prefix of the first N5 phase from it).
| corpus | runs | runs with a two-sided fallback (fallbacks) | failures |
| --- | --- | --- | --- |
| lib41 (412 files; 367 with n ≤ 64, 45 larger skipped), S3 start | 367 | 14 (51) | 0 |
| lib41, S3 + 2 random start pairs | 1,101 | 50 (128) | 0 |
| 3,000 random games, k = 0..4 Odd choice vertices (30 % dualised, giving 𝒞^1E), n 4-14 | 3,000 (378 𝒞^1E) | 0 | 0 |
| exitr_cex_n48.pg (the packet's example), S3 | 1 | 1 (1) | 0 |
| climbs dual_climb.py, 3 × 1,200 s (seeds 31, 32 from the 10 lib41 games with a two-sided fallback at S3; 33 random) | 390,158 runs (194,079 evals) | 135,671 (297,779) | 0 |
- PLAIN: in every run with a two-sided fallback the plain mirror differed, and its first difference was exactly at state j + 1 (the
  counter for "later than j + 1" never fired); in no run without one did it differ.
- MOFC: 24,056 sampled states (all corpora; lib41 and its random-start run overlap at S3), prefix property holds. MIR_A: 698 𝒞^1E runs. OM2 and ENDGAME: every run.
- Mine vs the packet: on the n ≤ 64 part of lib41 I see 14 runs with 51 two-sided fallbacks at the S3 start; the packet counts 15 runs
  and 54 over all 412 files (it includes the 45 games with n > 64 that my probe skips). Consistent.
- Thin: random games never produce a two-sided fallback (0 in 3,000; the packet's dualsym data agree); the climbs supply them.

## 6. The §2 table (not to sign)
- The general READING is right: an in-phase N5^OF transition is an N5 transition from the same state (an N5^OF-only transition is an
  Odd fallback, which changes τ and ends the phase), and a per-phase count transfers through MIRROR (c)'s prefix property, provided
  the N5 statement holds from every start pair.
- Spot check (statements only): `awk '/^### R17 /,/^### R49 /' docs/RESULTS.md | grep -i "S3|start pair|canonical start|..."`: no
  signed statement in R17-R48 restricts the start; R18 (a), (c) say "any start pair" / "ANY start pair"; every other hit is a DATA
  line. I did NOT audit each proof for an unstated use of the S3 start or of pre-phase history (column (i)); that audit is what
  (H-N5) from every start pair needs, and it is not signed by this report.
- R18 (c) row ("its count uses N5's fallback rule"): flagged by the packet itself; (c) is not needed for MIRROR.

## 7. Corner cases (Lead's list)
- Two-sided fallbacks: the only place N5 and its mirror can part (DUAL second sentence); exercised on 14 lib41 runs (51 fallbacks) and
  in climbs (§5), with the first difference exactly at j + 1.
- The tie rule: N5^OF differs from N5 exactly at two-sided fallbacks (by definition); DUAL's first sentence holds through them (§5).
- Ω + 2 invariance: proved from SPEC's text (§1); tested by running N5 on G and on G with Ω + 2 from the same start pair (OM2, §5).

## 8. Notes for the fixes file
- DUAL-1: second sentence of Lemma DUAL: "agree on states 0, …, j; the first possible difference is at state j + 1".
