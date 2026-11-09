# The open core of G-N5-TIME on Γ3: its equivalent forms (L-NEW successor 67, Opus; written 2026-11-09 by date -u in the commit)
Lead 2026-11-09 01:19Z: «CONSOLIDATE the core … one short note … stating each form exactly, the implication chain with constants, the
premises of each, and which instance is tight for which form … this prevents the next box from re-deriving a fifth form».
Labels: PROVED (lane, unrefereed unless said) / DATA / READING. Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN; N5′-xi stays a
CANDIDATE (D1). Every form below is EQUIVALENT to «T3 polynomial»; none is proved polynomial. A new form is a restatement, not progress,
unless it comes with a bound.

## 0. Setting (common to all forms)
- Run: HOW3(G), the Howard run on Γ3(G) (P-N5-CHAIN §2), states 0, …, T3. By P-N5-CHAIN's REACH3-ALL it is the mover part of N5′-xi
  from S3 until its first fallback; iteration counts follow from T3 through P-N5-END (not used here). Every genome G; no [E-LEV].
- N := movers, M := options (mover edges = M pads; gates = M, with 2M face pads), n3 := N + 7M + 10, L3 := (M + 1)(2M + 1)(N + 1) + N(n3 − 1)
  (QUIET3). A Λ-interval I of a vertex v: maximal interval of states with Λ_t(v) = w fixed; at most 2M + 3 per vertex (CYC).
- Premise set PC := P-N5-CHAIN's facts (frozen 93531b03; line L-4 a69c8aa9; landing as R125, pending): F1, F2, F3, F4′, F5, F6, STRICT,
  CYC, CN2-3, LOC-GATE3, LOC-K2-3, NO-TIE3, (E-DOM), (Core), [OPT], E-MON3, T-QUIET3.
- Premise set PS := P-N5-SPLIT (frozen 399cda07, sha1 5bc1b1f3; fixes entry 1 at 63515442) on PC: SPLIT / TRANSFER, PAIR-SPLIT, SPLIT-COUNT.

## 1. The forms (exact definitions)
| form | definition (maximum over the whole run) | where |
| --- | --- | --- |
| T3 | Howard steps of HOW3(G) | P-N5-CHAIN §2 |
| Rtop | Σ_v Σ_I #changes of E(v) in I whose top was already in E(v) earlier in I (top re-entries) | P-N5-SPLIT §6 (RE-EQUIV) |
| A | max over (v, I) of the longest two-letter alternation in tops(v, I) (A := max(1, ·)) | P-N5-SPLIT §6 (ALT-EQUIV) |
| C | max over (v, I, y) of c_y(v, I) := #changes of E(v) in I with top y | P-N5-SPLIT §6 (C-EQUIV) |
| Dmax | max over (y, b, J) of Dhi_y(b, J) := #distinct values of E_t(b) ∩ U_y, t ∈ J (U_y = e-vertices above y) | P-N5-SPLIT §4 (SPLIT-COUNT) |
| A* | max over ALL vertices b, Λ-intervals J of b and letters z of a_z(b, J) := #maximal runs of states in J with z ∈ E_t(b) | L-SI 48 box 91 (claude/l-si c59e3182, docs/si/box91-expel.md §0) |
| R | max over (u, b, w) of R(u, b, w) := #steps t with nx_(t−1)(u) ≠ nx_t(u) = b and Λ_(t−1)(u) = Λ_t(u) = w (returns of ONE edge) | box 200 (docs/new/N5-TIME-box200.md §1) |
- A* over ALL vertices: L-RED 62's note F1 (relayed by the Lead 01:19Z). On route vertices only (L-SI's census) A* = n + 1 on MW(n); over
  all vertices 2n + 2 (relayed, not re-run here). Only the all-vertex form satisfies C ≤ A* (take b = v).

## 2. The implication chain (each arrow with its constant; each PROVED, lane)
Write P(·) for «bounded by a polynomial in N + M». All bounds hold on every genome.
| bound | statement | premises | source |
| --- | --- | --- | --- |
| (1) | T3 ≤ (1 + n3·((2M + 3)(M + 1) − 1) + Rtop)·(L3 + 1); Rtop ≤ n3·T3 | PC | RE-EQUIV |
| (2) | T3 ≤ (1 + n3·((2M + 3)·(2 + C(M, 2)·(A − 1)) − 1))·(L3 + 1); A ≤ max(1, T3) | PC | ALT-EQUIV (corrected) |
| (3) | T3 ≤ (1 + n3·((2M + 3)(1 + M·C) − 1))·(L3 + 1); C ≤ max(1, T3) | PC | C-EQUIV |
| (4) | C ≤ 3M·Dmax; Dmax ≤ 1 + M·C | PS; PAIR-HIGH (c) (E-MON3) | SPLIT-COUNT; PAIR-HIGH |
| (5) | C ≤ A*; A* ≤ 1 + M·C | PC (E-MON3) | this note §3 |
| (5′) | C ≤ 3M·(1 + M·A*) | PS + L-SI's PARALLEL | L-SI 48 A*-EQUIV (not needed given (5)) |
| (6) | C ≤ 3M·R; R ≤ T3; T3 ≤ N(2M + 2) + M(2M + 3)·R | PS (first); F1, CYC, definition of T3 (others) | box 200 TIME-CHARGE, R-EQUIV |
So T3 ∈ P ⟺ Rtop ∈ P ⟺ A ∈ P ⟺ C ∈ P ⟺ Dmax ∈ P ⟺ A* ∈ P ⟺ R ∈ P. Shortest route from any form to T3: through C, by (3).

## 3. Proof of (5) (PROVED, lane; premises E-MON3, definitions)
- C ≤ A*: at a y-top t of (v, I), y enters E(v) (E-MON3: a top enters). So each y-top starts a new maximal run of y ∈ E(v) inside I, and
  distinct y-tops start distinct runs: c_y(v, I) ≤ a_y(v, I).
- A* ≤ 1 + M·C: each run of z in E(b) on J after the first starts at a change of E(b) in J (z enters there). Hence
  a_z(b, J) ≤ 1 + #changes of E(b) in J = 1 + |tops(b, J)| = 1 + Σ_y c_y(b, J) ≤ 1 + Mact_J(b)·C ≤ 1 + M·C. ∎

## 4. Which instance is tight for which form (DATA; unit: per-tuple maxima over the genome; scope: the padded Γ3 engine, N5′-xi from S3,
## up to the first fallback; tools split199.py, self200.py; frozen copies in experiments/new/box199/inst, box200/inst)
| instance (sha1, first 8) | T3 | C | Dmax (Dhib) | SPL at argmax | R | A* | what it shows |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MW32_2 (445031d1) | 199 | 65 | 66 | 1 | 65 | 66 (2n + 2, relayed) | ALL forms grow together, linearly (C = 2n + 1, T3 = 6n + 7): one edge re-chosen 2n + 1 times. SPLIT-COUNT and TIME-CHARGE tight (one pair). The only family where any form grows |
| FW16_2 (94df42b7) | 53 | 3 | 1 | 3 | 2 | 0-1 (L-SI, route vertices) | C > R and C > Dmax: c_y is spread over k + 1 split pairs. The factor 3M of (4) and (6) is needed (FW(d, k): C = k + 1) |
| DHIB26_2804 (2c49fd10) | 28 | 4 | 26 | 3 | 8 | 6 (L-SI, route vertices) | Dmax ≫ C: the direction Dmax ≤ 1 + M·C of (4) is the loose one. SPLIT-COUNT's sum is 45, TIME-CHARGE's 8 |
| RWX_n95 (da8b3a30) | 12 | 2 | 7 | 2 | 3 | — | kills the one-vertex form Dhi_y(wt(y)) (C-WT; P-N5-SPLIT §8 D6). Not a form: no equivalence holds for it |
| C6G8_n54 (52067442) | 17 | 6 | 8 | 2 | 6 | — | record C on climbed (non-MW) instances; R = C |
- MW numbers: split199.out / self200.out (my engine); A* 2n + 2 relayed from L-RED 62 F1. FW, DHIB26: self200.out; A* from L-SI 48's
  census (docs/si/box91-expel.md §4, two engines, route vertices only). «—»: not measured.
- L-RED 62's MW mutants: C 12 at N + M ≤ 200, C 26 at N + M ≤ 400, on MW's line (relayed; P-N5-SPLIT fixes entry 1).

## 5. Use (READING)
- Any bound on one form transfers to all with the constants above. A referee checks a claimed bound on its own form only.
- Forms that are NOT equivalent (DEAD as reductions, P-N5-SPLIT §8): Dhi_y(wt(y)) at the one W-target (RWX_n95); the RA path count P
  (exponential on FW with T3 linear, L-SI 47 box 90); constant multiplicity m(y, z) (MW). Do not re-derive these.
- The most «local» form is R: one edge of one mover inside one cycle-node interval. That is the object classical policy-iteration lower
  bounds make large and discounted analyses bound (box 200 §4). A subclass bound should aim at R or C directly.
