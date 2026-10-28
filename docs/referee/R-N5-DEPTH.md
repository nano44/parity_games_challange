# R-N5-DEPTH: REFEREE report on packet P-N5-DEPTH (L-SI box 22: Fact N-MONO, Theorem ABS-DEPTH, Theorem STATIC-DEPTH, Corollary PURE-END, Corollary GCI-LEN-ρF)
Referee: REFEREE (successor 16), Opus 5.5 (owner ruling D15). FIRST referee (Lead queue of 18:43Z / 19:18Z by date -u).
- Object and pin: docs/si/P-N5-DEPTH-box22.md, sha1 549c7fb72d767293b6bf2ae5bbbb8809084df707, 152 lines, author L-SI successor 18: the same
  sha1 on my tree and at the l-si freeze 2201aa2d (an ancestor of HEAD).
- Written 2026-10-26T19:26Z-19:31Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/ file on DEPTH on my tree, on trunk or on origin/claude/referee-2 (re-listed in the same turn; 0 / 0 / 0 at 19:30Z).
  No lane code run (experiments/si/root/absdepth.py, abscyc.py, staticdepth.py, experiments/si/rund/quotecheck.py neither executed nor
  imported). D1.
- Premises read against their text: SPEC S1 (l. 28-29), S4a (l. 51, 53), S4c (l. 56); RESULTS R18 (d) Lemma S (a) (l. 803-804) with R57 (a)
  and 1E-N3 P2 (R69, l. 3596); (SW) (l. 3768-3769); (M2κ) (P-N5-FBPOLY-box41 l. 97) with (M1κ); R69 (d) Lemma STATIC (l. 3612-3613);
  P-N5-GCX-box21 §4's model (l. 63-64) and §1's global C-interval (l. 32-33); L-RED R91 §5's GCI-LEN (l. 101).
- Quotes: all 12 "[Q path@commit:lines] «…»" quotes verbatim at their tagged commits and lines (scratch/flip_quotes.py: QUOTES 12 FAILED 0).
- Tools (own, docs/referee/scratch/): abs_depth.py (ABS-DEPTH and N-MONO on my model simulator abs_model.py, which I wrote for R-N5-GCX from
  the GCX §4 text), depth_s4.py (the packet's §4 instance and my LOC game under every rule), depth_probe.py (STATIC-DEPTH, its steps,
  PURE-END, GCI-LEN-ρF in N5 on my engine rl_engine). Logs depth_logs/.

## Verdicts (sign-off line per item)
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 | (MONO), (MONO-SUCC), (TERM) (quoted remarks with proofs) | CHECKED (true in the model) |
| §1 | Fact N-MONO | SIGNED, with "pointwise maximal" read as pointwise GREATEST (DEPTH-N1; the same reading as GCX-N4) |
| §1 | Theorem ABS-DEPTH (cyclic model, under GEN, any deterministic rule) | SIGNED |
| §2 | Theorem STATIC-DEPTH (N5, every game, under (H1)-(H4) and GEN_W) | SIGNED |
| §2 | Corollary PURE-END | SIGNED |
| §3 | Corollary GCI-LEN-ρF | SIGNED (immediate from STATIC-DEPTH; scope remark consistent) |
| §4 | the instance (GEN needed for the per-vertex form) | CONFIRMED on my simulator (not a to-sign item) |
| §6 | CONJECTURE ABS-DEPTH-TIE | not a to-sign item, but FALSE as stated for general deterministic rules (DEPTH-N2, one-vertex counterexample); open for rules that keep a maximal current choice |
| §5, §6 | data, (G1)-(G4), CONJECTURE STATIC-DEPTH-TIE, READING | not signed |
No gap in the signed items. Notes DEPTH-N1..N4. Nothing here bounds N5's running time; GCI-LEN is proved only for the intervals covered
(σ̄ constant, (H3), (H4), GEN_W); not a TARGET.md claim; G-N5-TIME stays OPEN.

## 1. The model: N-MONO and ABS-DEPTH, re-derived (parentheticals checked one by one)
- (MONO) ✓: M_t(u) ≤ w(u) + M_t(s_{t+1} u), with equality if u keeps its choice and strict inequality if u switches (arena); summing along
  the finite s_{t+1}-play gives M_{t+1} ⪰ M_t. (MONO-SUCC) ✓: M_{t+1}(s_{t+1} v) ⪰ M_t(s_{t+1} v) ⪰ M_t(s_t v). (TERM) ✓: a switching vertex
  strictly raises its M, so Σ_v M strictly rises while s changes, and there are finitely many strategies. (All under the model's assumption
  that a pointwise maximal arena strategy exists at each step.)
- N-MONO ✓ under one reading (DEPTH-N1). s_t is valid and uses arena edges, so it is a candidate. "s_{t+1}'s N is pointwise maximal among
  the candidates" gives N_{t+1} ⪰ N_t only if "pointwise maximal" means pointwise GREATEST (dominating every candidate). A merely undominated
  maximal element would not give it. The model's "ASSUMES one exists" fits the greatest reading, and that is how I sign it. In the acyclic
  model the two readings agree.
- ABS-DEPTH ✓. Induction on d = d*(v) along the final forest ✓.
  - y* := s*(v) is terminal (d = 1), or d*(y*) = d − 1 ✓ ("(play*(v) = v · play*(y*) is simple)" ✓).
  - (A) ✓: if y* ∉ Al_{s_t}(v), then v must take y* at a later t′, which needs M_{t′}(y*) > M_{t′}(s_{t′} v). But M_{t′}(y*) = M_t(y*) ≤
    M_t(s_t v) ≤ M_{t′}(s_{t′} v) by (MONO-SUCC).
  - (B) ✓: s′ = s_{t+1}[v ↦ y*] is valid, because y*'s s_{t+1}-play is play*(y*) and avoids v. It uses arena edges ✓. N_{s′}(y*) = N_{t+1}(y*)
    = N*(y*), since only v changed and y*'s play avoids v. So N_{t+1}(v) ⪰ N*(v). (B) holds under either reading of "maximal": an s′ beating
    s_{t+1} at v would dominate it.
  - With N-MONO, N_t(v) = N*(v) for t ≥ d ✓. GEN turns equal N into equal plays ✓. Run fixed after max d* ≤ n ✓. The theorem holds for any
    deterministic rule: neither (A) nor (B) looks at the rule.

## 2. STATIC-DEPTH, PURE-END, GCI-LEN-ρF, re-derived
- Setting ✓. d*(v) is well defined by (H4). d*(v) ≤ n − 1 "(the number of non-cycle Even vertices on a longest H_b-path)" ✓: every maximal
  H_b-path ends at a cycle vertex (a sink), so it holds ≤ n − 1 non-cycle vertices.
- (H2)'s parenthetical "(A ρ-free interval in R69 (d)'s sense satisfies this.)" ✓: R69 (d)'s ρ-free interval has σ̄|Q constant, and Lemma
  STATIC gives σ̄_k = σ̄_I on all Odd vertices.
- Facts ✓. (W-MONO): σ_t is in S4a's arena, and P2 with R18 (d) (a) on the arena game gives the pointwise maximum. (Ξ-SUCC): (M2κ) with
  (M1κ) (λ constant) if kept; (SW) then (M2κ) if switched. (CV): (H1), (H3).
- Theorem ✓.
  - Odd v ∉ D and u ∈ D ✓: both plays are v (resp. u) followed by the successors' plays, which are fixed by (H2).
  - Even v, (A) ✓: v takes y* at some t′ ∈ [t, b − 1], and Ξ_{t′}(y*) ▷ Ξ_{t′}(σ_{t′} v) ⊵ Ξ_t(σ_t v) ⊵ Ξ_t(y*) = Ξ_{t′}(y*). "(y* settled, and a
    valuation is a function of the play)" ✓.
  - Even v, (B) ✓: s′ is an arena strategy of state t (by (A)). y*'s W-play under σ_{t+1} is its W-play at b, and it avoids v ("v is not a
    cycle vertex, and its W-play at b is v·(y*'s), simple up to a cycle not through v") ✓. So W_{s′}(v) = W_b(v). Pointwise optimality and
    W-MONO give W_{t+1}(v) = W_b(v) ✓. GEN_W ("paths to the same cycle": the W-cycles are constant by (H3), λ_W by (H1)) gives the same W-play,
    so σ_{t+1}(v) = y* and the honest play is v·(y*'s) ✓.
  - The ending ✓: σ_t = σ_b from a + max d* (non-cycle Even v by the first step of its W-play; cycle Even v by (H3)). An unchanged σ with τ
    constant is SPEC's FALLBACK (S4c, quoted), excluded by (H1). So b ≤ a + max d* ✓.
- PURE-END ✓. For z ∈ A_b the W-play meets no gate, σ̄ = τ off D, so the honest play equals the W-play and is z's only H_b-path ✓. For v ∉ A_b,
  every H_b-path is v's W-play up to its first gate u, then τ(u) or σ̄(u) ∈ A_b (D-direct), then that vertex's play in A_b ✓. The two parts are
  disjoint and simple ✓. No gate lies on its own W-cycle, since τ(u)'s W-play avoids D ∋ u. Every honest play agrees with the W-play up to
  the first gate and then enters A_b. So every cycle of either frame lies in A_b, where the frames coincide ✓. "((H3), constancy on [a, b],
  remains a hypothesis.)" ✓.
- GCI-LEN-ρF ✓: a fallback-free λ_W-constant run inside one phase gives (H1), σ̄ constant gives (H2); STATIC-DEPTH. The global C-interval
  structure is not used, so the corollary holds for any interval with these hypotheses, global C-interval or not.

## 3. The §4 instance and CONJECTURE ABS-DEPTH-TIE
- §4 instance CONFIRMED (scratch/depth_s4.py). On my simulator the run is (t3, t5, 0) → (1, t5, 0) → (1, 2, t4), fixed after 2 ≤ max d* = 3,
  under rules basic, basicM, lowest index, hash and sizedep (anti takes (1, t5, t4) in between and also fixes after 2). The game is non-GEN.
- CONJECTURE ABS-DEPTH-TIE ("in the model, the run is fixed within max d* steps without GEN") is FALSE as stated for general deterministic
  rules (DEPTH-N2). My one-vertex LOC game from R-N5-GCX (scratch/loc_cex.py) is non-GEN with max d* = 1. Under the rules "anti" and
  "sizedep" its run b → c is fixed only after 2 steps. Random cyclic models (abs_depth.py, logs absdepth_3000_s21_w3, _s22_w1): 18
  non-GEN runs end later than max d*, all under those two rules or a hash-based rule. No such run occurs under basic, basicM or lowest index
  (a rule that keeps a maximal current choice, or an order-consistent one), and no GEN run ever does. The conjecture is open only for such
  rules. N5's tie rule (SPEC S1 on the arena) is a different question; CONJECTURE STATIC-DEPTH-TIE is not touched.

## 4. Data (own engines; DATA, not proof; 0 failures of every signed check)
Model (abs_depth.py, cyclic random digraphs n 3-7, 6 rules per game; runs stop where no greatest strategy exists):
| log | fixed runs (GEN / non-GEN) | ABS-DEPTH per-vertex checks, GEN runs (failures) | non-GEN per-vertex failures (expected; §4) | runs fixed later than max d* (GEN / non-GEN) | sharp (fix = max d*), GEN |
| --- | --- | --- | --- | --- | --- |
| absdepth_3000_s21_w3 (weights −3..3) | 3,246 / 12,930 | 12,798 (0) | 72 | 0 / 8 | 294 |
| absdepth_3000_s22_w1 (weights −1..1, ties frequent) | 1,794 / 14,996 | 6,876 (0) | 66 | 0 / 10 | 144 |
N-MONO: 0 failures in both logs (N non-decreasing at every step). Control MUT=1 (per vertex from d* − 1): 612 failures in GEN runs.
N5 (depth_probe.py; for each end state b the least a with (H2), (H3), so every later start is implied):
| set (log in depth_logs/) | N5 runs | (H1) runs | STATIC-DEPTH intervals (with gates; sharp) | per-vertex checks | step (B) value checks | PURE-END states (with gates) | GCI-LEN-ρF intervals (with gates) | max length − (n − 1) | failures |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lib 1,140 files, n ≤ 40 (4 parts), S3 + given + 2 random | 2,739 | 2,741 | 8,918 (4,263; 375) | 512,278 | 453,098 | 19,361 (9,796) | 2,046 (1,080) | 0 | 0 |
| lib41 (experiments/new/box41), n ≤ 64, S3 + 2 random | 1,130 | 1,494 | 6,667 (3,477; 432) | 842,104 | 760,784 | 13,427 (8,014) | 1,313 (792) | −1 | 0 |
| random 𝒞^kO, n 4-16, k ≤ 6, seed 222 | 9,000 | 1,387 | 1,059 (37; 113) | 6,353 | 3,155 | 16,583 (2,816) | 960 (33) | −2 | 0 |
| nep90 / nep76 / long121, L-RED ul instances, cxmig_k (given starts) | 18 | 42 | 184 (178; 0) | 71,541 | 65,134 | 213 (189) | 35 (29) | −33 | 0 |
- The lane's figures reproduce. At S3, b6_xs_n24 / n32 / n40 have an interval of length max d* = 21 / 29 / 36. The longest interval with gates
  is 26 (x32_waves48, n = 48; the lane's 26).
- No local GEN_W failure occurred: every per-vertex check passed outright. Control MUT=1 (per vertex from a + d*(v) − 1): 3,010 failures on
  the n ≤ 24 library. (H4) failed at 33 end states and the cycle sets differed at 4,293 (those are outside the theorem; counted).

## 5. Notes (none blocks a signature)
- DEPTH-N1 (model reading). N-MONO, and with it ABS-DEPTH's last step and (TERM)'s fixed point N*, need "pointwise maximal" read as pointwise
  greatest; say so (the same point as GCX-N4).
- DEPTH-N2 (CONJECTURE ABS-DEPTH-TIE). False as stated for general deterministic rules (the one-vertex game, rules anti / sizedep; §3).
  Restate it for rules that keep a maximal current choice (or order-consistent rules), where my data show no counterexample.
- DEPTH-N3 (GCI-LEN-ρF, scope). The proof does not use that [a, b] is a global C-interval. The corollary is STATIC-DEPTH read on any
  interval of a λ_W-constant fallback-free in-phase run with σ̄ constant, (H3), (H4) and GEN_W.
- DEPTH-N4 (data). Sharpness (length = max d*) is common in natural data (920 intervals over the four sets). The theorem's bound is
  attained, not slack.

DONE: this report. FINDINGS: all SIGNED, no gap; ABS-DEPTH-TIE false as stated (DEPTH-N2); DEPTH-N1, N3, N4. NEEDS: Lead: route the notes to
L-SI's fixes file (docs/si/P-N5-DEPTH-fixes-box22.md); §C against REFEREE-2 on your word.

## §C. Comparison with REFEREE-2 (written 2026-10-28T22:20Z by date -u, after the Lead's word of 22:16Z; REFEREE-2's report
docs/referee-2/R2-N5-DEPTH.md at origin/claude/referee-2 dad93591 and its §C d8402f3d, read only after this report was pushed at 1d74c963)
Written by REFEREE successor 16, the author. Every verdict is labelled (Opus 5.5, D15).
- Verdicts identical: N-MONO (greatest reading), ABS-DEPTH, STATIC-DEPTH, PURE-END, GCI-LEN-ρF SIGNED; §4 instance confirmed by both. Joint
  gap map: EMPTY.
- Notes matched:
  - DEPTH-N1 = N-DEPTH-1 ("pointwise maximal" read as greatest).
  - DEPTH-N2 = N-DEPTH-3 (ABS-DEPTH-TIE false for general rules; the same one-vertex mechanism; restate it for keep rules).
  - DEPTH-N3: accepted by REFEREE-2.
  - DEPTH-N4 is compatible with its 651 sharp intervals.
  - N-DEPTH-2 (STATIC-DEPTH's length step is global): ACCEPTED. It is the same fact that breaks PURE-LEN (R-N5-DEPTH-add §2).
  - N-DEPTH-4 (13 local GEN_W failures with the conclusion intact, in its corpus; 0 in mine): a data difference between corpora, no conflict.
  - N-DEPTH-5 (thin coverage): ACCEPTED.
- Data agree (the §4 run; b6_xs 21 / 29 / 36; x32_waves48 26; non-GEN overruns only under non-keep rules). Nothing open on DEPTH.
