# R2-N5-DEPTH: REFEREE-2 report on packet P-N5-DEPTH (N-MONO, ABS-DEPTH in the model; STATIC-DEPTH, PURE-END, GCI-LEN-ρF in N5)
Referee: REFEREE-2 successor 18 (session_01WT4cukhJyjxHKaBJWikCkK), Opus 5.5 (D15, L37). Written 2026-10-28 from 21:40Z (date -u).
Object: docs/si/P-N5-DEPTH-box22.md, sha1 549c7fb72d767293b6bf2ae5bbbb8809084df707 (on trunk = the pin), 152 lines, frozen. Author L-SI
successor 18. Quotes pinned at 982f5c629, 58061d91, 02240121, 54de3f2f.
Independence: written before opening any REFEREE file on DEPTH. In the push turn, after `git fetch origin claude/referee`, `git ls-tree
--name-only -r origin/claude/referee docs/referee/ | grep -ic depth` gave 16 at 2026-10-28 22:00:42Z (2026-10-26 19:04:54Z: 0). Names only; none opened.
Lane tools (experiments/si/root/absdepth.py, abscyc.py, staticdepth.py) NOT run or imported.
Checkers (own; docs/referee-2/R2-N5-DEPTH/):
- absdepth_check.py: the model, on my R2-N5-GCX/abs_check.py simulator, with GEN checked exactly over all simple paths.
- depth_check.py: N5. SPEC loop on si.py; my own Ξ / W play values. (H2)-(H4), d*, H_b, GEN_W (in its used form), PURE-END,
  GCI-LEN-ρF; also the DEPTH-add checks, reported in R2-N5-DEPTH-add.md.
- Quotes: my R2-N5-CHOSEN/qtags.py.
Scope (D1): ABS-DEPTH is about an abstract model. STATIC-DEPTH and GCI-LEN-ρF bound intervals under the strong hypotheses (H2)
(σ̄ constant), (H3) (common constant cycles), (H4) and GEN_W, which cover only part of the global C-intervals (§6 (G1)-(G4) of the packet).
Nothing here bounds N5's running time. Not a TARGET.md claim. G-N5-TIME stays OPEN. The packet depends on no unlanded packet: checked; its
premises are SPEC, R18 (d) / R57 (a), R69's P2, R72's (SW), R56's (M2κ), and the frozen GCX model definition.

## 0. Verdicts (all "(Opus 5.5, D15)")
| § | item | verdict |
| --- | --- | --- |
| §1 | Fact N-MONO (model) | SIGN, with "pointwise N-maximal" read as pointwise GREATEST, the reading the model's existence assumption makes (N-DEPTH-1) |
| §1 | (MONO), (MONO-SUCC), (TERM) (cited from GCX §4, proofs given) | CORRECT |
| §1 | Theorem ABS-DEPTH (under GEN) | SIGN |
| §2 | Facts (W-MONO), (Ξ-SUCC), (CV) | CORRECT |
| §2 | Theorem STATIC-DEPTH (under (H1)-(H4), GEN_W) | SIGN |
| §2 | Corollary PURE-END | SIGN |
| §3 | Corollary GCI-LEN-ρF | SIGN |
| §4 | the GEN instance | DATA, reproduced exactly with my simulator (§2) |
| §0 | quotes | 12/12 VERBATIM in their line ranges |
No gap. Notes N-DEPTH-1..5 (§3).

## 1. Proof check
### 1.1 §1 N-MONO and ABS-DEPTH (model)
- (TERM). A switched u has M_{t+1}(u) = w(u) + M_{t+1}(s_{t+1} u) ⪰ w(u) + M_t(s_{t+1} u) ≻ w(u) + M_t(s_t u) = M_t(u), by (MONO) at the
  successor and the arena's strictness. So Σ M rises strictly while s changes. CORRECT.
- N-MONO. s_t is a valid strategy on arena edges, so it is a candidate, and N_{t+1} ⪰ N_t needs s_{t+1}'s N to DOMINATE every candidate. That
  is "pointwise maximal" in the sense of greatest (N-DEPTH-1). CORRECT under that reading.
- ABS-DEPTH. Induction on d = d*(v) over the final forest. y* = s*(v), and play*(v) = v·play*(y*) is simple.
  - (A) If y* ∉ Al_{s_t}(v) at some t ≥ d − 1, v must later take y*, which needs M_{t′}(y*) > M_{t′}(s_{t′} v). But M_{t′}(y*) = M*(y*) =
    M_t(y*) ≤ M_t(s_t v) ≤ M_{t′}(s_{t′} v) (MONO-SUCC). CORRECT.
  - (B) s′ := s_{t+1}[v ↦ y*] is valid: y*'s play under s_{t+1} is play*(y*) and avoids v, and plays through v follow it. It uses
    Al_{s_t}-edges, by (A). So N_{t+1}(v) ⪰ w(v) + N*(y*) = N*(v), and with N-MONO, N_t(v) = N*(v) for t ≥ d. GEN gives play_t(v) = play*(v).
  - s_t is determined by the plays, so the run is fixed by max d* ≤ n. CORRECT.
  - The remark "the induction runs on the final forest; it never inspects non-chosen successors" is right.

### 1.2 §2 STATIC-DEPTH
- Facts.
  - (W-MONO): σ_t is an arena strategy and σ_{t+1} is Even's pointwise optimum in the arena game H_t (R18 (d) (a) on H_t = P2). W is the
    (σ, τ)-play value in G = the valuation in H_t.
  - (Ξ-SUCC): (M2κ) with λ constant, and (SW) for a switch.
  - (CV): (H3) fixes next on cycle vertices, so their plays are constant.
  All CORRECT.
- d*: H_b's maximal paths end at cycle vertices (sinks), since every non-sink has an out-edge and H_b is acyclic off them. So d*(v) ≤ (the
  number of non-cycle Even vertices) ≤ n − 1. CORRECT.
- Induction.
  - Odd v ∉ D: σ̄ = τ at v by (H2) and D constant. u ∈ D: both successors fixed.
  - Even v, (A): suppose y* ∉ {σ_t v} ∪ Iσ_t(v). Then Ξ_t(y*) ⊴ Ξ_t(σ_t v) (⊴ is total). The later switch to y* needs Ξ_{t′}(y*) ▷
    Ξ_{t′}(σ_{t′} v) by (SW). But Ξ_{t′}(σ_{t′} v) ⊵ Ξ_t(σ_t v) by Ξ-SUCC, and Ξ_t(σ_t v) ⊵ Ξ_t(y*) = Ξ_{t′}(y*), because y* is settled and a
    valuation is a function of the play. Contradiction. CORRECT.
  - Even v, (B): s′ = σ_{t+1}[v ↦ y*] uses state-t arena edges (by (A)). y*'s W-play under σ_{t+1} is its play at b, which avoids v: v is not a
    cycle vertex, and its W-play at b is a lasso starting at v off the cycle. So W_{s′}(v) = v ⊕ W_b(y*) = W_b(v). P2 gives
    W_{t+1}(v) ⊵ W_b(v), and W-MONO up to b gives ⊴. GEN_W gives the same W-play, hence σ_{t+1}(v) = y*, and the honest play is
    v·(y*'s honest play) = the one at b. CORRECT.
- End. From a + max d*, σ_t = σ_b; Even cycle vertices are covered by (H3). A transition with σ and τ unchanged is a SPEC S4c fallback,
  excluded by (H1). So b ≤ a + max d*. CORRECT. This is the one global step of the proof (it needs ALL Even vertices settled); see
  R2-N5-DEPTH-add §PURE-LEN for why that matters.

### 1.3 PURE-END, GCI-LEN-ρF
- PURE-END. Every D-vertex is D-direct at b.
  - For z ∈ A_b: the W-play has no gate, so it is the honest play, and z's only H_b-path is it (H_b branches only at D).
  - For v ∉ A_b: an H_b-path is the simple W-prefix up to the first gate u, then τ(u) or σ̄(u) ∈ A_b, then the unique path inside A_b. The
    parts are disjoint (prefix vertices are not in A_b). So H_b has no cycle off the cycle vertices.
  - No gate lies on a W-cycle (all are reached inside A_b), and inside A_b the two frames agree. So every cycle is common. CORRECT.
  - "(H3), constancy on [a, b], remains a hypothesis" is right.
- GCI-LEN-ρF. A global C-interval of a λ_W-constant fallback-free in-phase run gives (H1); σ̄ constant gives (H2); STATIC-DEPTH gives
  b − a ≤ max d* ≤ n − 1. CORRECT.
- The Scope remark against R91 §3 (neither contains the other) is a reading; I accept it.

## 2. DATA (own checkers; every violation count 0; counts from docs/referee-2/R2-N5-DEPTH/logs/)
Model (absdepth_check.py):
- 20,000 cyclic models × 3 rules (absdepth_cyc.txt: 36,711 runs; 150,963 vertex checks).
- The same with values in {−2..2}, so ties are frequent (absdepth_cyc_vals.txt: 37,449 runs).
- 20,000 acyclic models × 3 rules (absdepth_acyc.txt: 60,000 runs; 269,658 vertex checks).
- N-MONO, and ABS-DEPTH per vertex and in length WHERE GEN HOLDS: 0 violations. Sharp (fix time = max d*): 4,051 / 3,361 / 7,954 runs.
- Without GEN (counted apart):
  - per-vertex failures: 30 / 87 / 26;
  - runs longer than max d*: 9 / 18 / 7. These occur ONLY under non-keep tie rules (flip 10, random table 8 in the vals log); under the basic
    rule 0. See N-DEPTH-3.
- §4 instance (logs/absdepth_instance.txt): under the basic rule my run is (t3, t5, 0) → (1, t5, 0) → (1, 2, t4), exactly the packet's.
  At state 1, vertex 2's play is 2 → 0 → 1 → t5 with N = 2 = N*(2), while its final play is 2 → t4. GEN fails at 2: three paths have N = 2.
N5 (depth_check.py; logs/total.txt sums named.txt (L-RED ul family, the union instances of R2-N5-DEPTH-add, the rund instances, nep90,
nep76, long121, ...), lib41 × 3, lib2o × 5 and random k = 2, 4, 5, kO; 46 RESULT lines, all OK; 21,775 runs, 79,060 states, ENGXI 0):
| check | checks | violations | detail |
| --- | --- | --- | --- |
| STATIC-DEPTH (every [a, b] inside a σ̄-constant sub-run with (H3) on [a, b] and (H4) at b; per-vertex settling and length) | 53,113 intervals | 0 | 17,348 with gates; sharp (b − a = max d* > 0) 651; GEN_W (used form) failed in 13, conclusion intact there; longest 55 on x32_rand64 (n 64, max d* 56); longest with gates 26 on x32_waves48 (max d* 37, one gate), as the packet reports |
| PURE-END (every state at which all D-vertices are D-direct) | 18,339 | 0 | — |
| GCI-LEN-ρF (global C-intervals with σ̄ constant and (H3)) | 3,499 | 0 | of 4,747 global C-intervals: 479 with a σ̄ change ((G1)), 766 without (H3); 1,022 with gates; longest 55 (x32_rand64, n 64) |

## 3. Notes
- N-DEPTH-1 (N-MONO). "pointwise N-maximal" must mean pointwise GREATEST (dominating every candidate). Otherwise N_{t+1} ⪰ N_t does not
  follow. The model's "assumed to exist" makes sense only for that reading. The same point as REFEREE's GCX-N4 on P-N5-GCX.
- N-DEPTH-2 (STATIC-DEPTH's last step is global). The bound b − a ≤ max d* uses "σ unchanged ⇒ fallback". So it needs every Even vertex of
  the game settled, not only those of one class. The class-restricted settling (each v settled from a + d*(v)) holds by the same induction
  for any set closed under H_b-successors. The interval-length conclusion does not restrict. This is what breaks P-N5-DEPTH-add's PURE-LEN
  (see R2-N5-DEPTH-add.md, G-DADD-1).
- N-DEPTH-3 (CONJECTURE ABS-DEPTH-TIE, not signed). For a general deterministic tie rule it is FALSE in the model. Example (absdepth_cyc_vals,
  rule flip):
  - Non-terminals 0, 1; terminals T2 (h 0, T 2) and T3 (h 2, T 2); succ(0) = {T2}, succ(1) = {0, T2, T3}; w = (−2, −1); start s(1) = 0.
  - Run: s(1) = 0 → T2 → T3, fixed after 2 steps, against max d* = 1.
  - Under the basic (keep) rule, 0 runs exceed max d* in all my data.
  - State the conjecture for keep rules. This is the same mechanism as G-GCX-1 on P-N5-GCX.
- N-DEPTH-4 (GEN_W). My check uses GEN_W's USED form (distinct W-plays of a vertex at states of the interval have distinct W-valuations).
  It failed in 13 intervals, all with the conclusion intact. The packet's GEN_W quantifies over all W-plays, a stronger hypothesis.
- N-DEPTH-5 (thin). (H3) plus (H4) excludes 766 of 4,747 global C-intervals, and σ̄ changes exclude 479 more: GCI-LEN-ρF covers 3,499.

## §C. Comparison with REFEREE (R-N5-DEPTH, claude/referee 1d74c963, file sha1 cdd642a6; successor 16), written 2026-10-28 22:05Z (date -u), after my report was pushed (dad93591)
- Verdicts identical: N-MONO (with the "greatest" reading), ABS-DEPTH, STATIC-DEPTH, PURE-END and GCI-LEN-ρF SIGN, no gap. JOINT GAP MAP:
  EMPTY.
- Notes:
  - DEPTH-N1 = N-DEPTH-1 ("pointwise maximal" = greatest).
  - DEPTH-N2 = N-DEPTH-3 (ABS-DEPTH-TIE false for general deterministic rules). Found by both on the same one-vertex tie mechanism; both
    propose restating it for keep rules.
  - DEPTH-N3 (GCI-LEN-ρF does not use the global C-interval structure; it is STATIC-DEPTH on any such interval): CORRECT, I accept it
    (missed by me).
  - DEPTH-N4 (sharpness common): agrees with my 651 sharp intervals.
  - Mine without counterpart:
    - N-DEPTH-2: STATIC-DEPTH's length step is global. REFEREE states the same fact in R-N5-DEPTH-add §2, where it breaks PURE-LEN.
    - N-DEPTH-4: GEN_W checked in its used form; REFEREE saw no GEN_W failure, I saw 13 with the conclusion intact.
    - N-DEPTH-5: thin coverage.
- Data agree: the §4 instance's run; b6_xs and x32_waves48 lengths; 0 failures everywhere; non-GEN overruns only under non-keep rules.
- Result: no disagreement. Joint map empty. REFEREE-2 successor 18 (Opus 5.5, D15).
