# Referee report R-P8: PREFIX-MONO-X* and relevant steals (GAP-A-M §22s), with the §22u chain

Referee: REFEREE (successor), running on Opus 5.5 under owner ruling D12 (Lead reading L33). Packet 8: the Lead's message
of 15:43Z. Pin: trunk a907c46, docs/alg/GAP-A-M.md §22s (line 2529 ff.) and §22u. Code: dtl.cpp @ 8fbf0a7 ("N" = that
line). Written to 15:43Z (date -u). Uses my R-P7 (EXACT, PREFIX-MONO-X) and R2-P7's G-P7-c2. docs/referee-2/R2-P8.md was not read.

## Verdict
| item | verdict (Opus 5.5, D12) | lines checked |
|---|---|---|
| EXACT*: P(τ) = Cl_{pr τ}(P(τ⁺) ∪ {τ}; F_τ) | SIGN (a corollary of EXACT; the non-fired tangles are redundant BECAUSE of EXACT, nothing new is needed) | 110-185 (return true only when a vertex is added, 146, 163-182), 690-705 |
| PREFIX-MONO-X* under (NS*) | SIGN | as R-P7 (a)/(b) |
| Corollary: a non-rise of Π_R needs a relevant new steal | SIGN WITH GAPS: G8-1 (the count over consecutive visit pairs needs the factor 3 of G-P7-c2; closed) | 713-776 |
| §22u chain, as a conditional: F_R ≤ (n+1)·n·#fired(R) given (STEAL-ONCE), hence (FALL) ⇐ (STEAL-ONCE) ∧ (FIRED-R) | VALID as a conditional, with G8-1's factor 3: F_R ≤ 3·(|R|+1)·|R|·#fired(R). (STEAL-ONCE) and (FIRED-R) are DATA, not signed | n/a |

## EXACT* (the Lead's question)
F_τ := the tangles for which attractTangle returned true during the region step of τ (round r understood). attractTangle
returns true only after adding at least one vertex (146 can_attract_new, 163-182), so "fired" = "added vertices".
- P(τ) ⊆ Cl(P(τ⁺) ∪ {τ}; F_τ). The code's run of the region step is a derivation: every vertex attraction (74-90) and
  every tangle firing is an instance of a Cl rule with premises in the current set (R-P7 (a) ⊆: trigger escape popped,
  escapes in CurZ, P(τ⁺) or outside R, new vertices of priority ≤ pr τ, vertices outside P(τ⁺) by 138-139). The tangles
  used are exactly F_τ. So the whole region is derivable from the base with the rules of F_τ, i.e. lies in that lfp.
- Cl(P(τ⁺) ∪ {τ}; F_τ) ⊆ P(τ). F_τ ⊆ T \ E_τ (a fired tangle misses P(τ⁺), 138-139). Cl is monotone in its tangle set
  (R-P7 (b)), so Cl(·; F_τ) ⊆ Cl(·; T \ E_τ) = P(τ) by EXACT.
- Is a closure over F_τ alone really equal to the one over T \ E_τ? Yes, and the redundancy of the non-fired tangles of
  T \ E_τ is not an extra assumption: it is the content of EXACT's ⊇ half (the closure over all of T \ E_τ is no larger
  than the code's region), which R-P7 and R2-P7 both signed. A tangle of T \ E_τ that did not fire either was tried and
  failed (some premise false in the final set, by the last-pop argument) or its new vertices were already added by other
  rules; in both cases it contributes nothing to the lfp. EXACT* is EXACT plus monotonicity, nothing more.
- Note: F_τ depends on the pop order (a tangle can be pre-empted by vertex rules), so F_τ is a property of the run, not of
  (V, T) alone. That is harmless: it is the earlier run's F_τ that the lemma uses, and that run is fixed.
DATA (p8probe.py): EXACT* holds at every region step (0 failures in 235,470 stable / 246,213 Oink steps; table below).

## PREFIX-MONO-X*
(NS*): F_τ ∩ E′_τ = ∅ for every τ processed in the earlier run. Since F_τ ⊆ T \ E_τ, (NS*) is implied by (NS) of §22r
and is weaker.
- τ not processed in run 1: as before.
- τ processed in both: F_τ ⊆ T ⊆ T′ and F_τ ∩ E′_τ = ∅, so F_τ ⊆ T′ \ E′_τ. EXACT* for run 1, EXACT for run 2,
  monotonicity: P(τ) = Cl(P(τ⁺) ∪ {τ}; F_τ) ⊆ Cl(P′(τ⁺) ∪ {τ}; T′ \ E′_τ) = P′(τ).
- Absorbed (τ ∈ P′(τ⁺)): P′(τ⁺) is closed under the threshold-pr τ rules of T′ \ E′_τ (EXACT's closedness, valid at an
  unprocessed index) ⊇ F_τ, and contains P(τ⁺) ∪ {τ}; so it contains Cl(·; F_τ) = P(τ).
SIGN.
Corollary (round induction, C1-C4, and G7-c1's strict rise at e*): unchanged from R-P7 with (NS*) in place of (NS),
since the induction uses (NS) only through the per-step inclusion. §22s's gloss "t is split" is right: t ∈ F_τ misses
P(τ⁺) (it fired there), and t ∈ E′_τ means the later prefix, the union of the regions of higher-index tops, meets t
without containing it.
G8-1 (closed). The corollary says Π_R fails to rise between two visits only at a relevant new steal. Turned into a count
over CONSECUTIVE visit pairs, it needs G-P7-c2's interval argument (prefix inclusions compose over a stretch with no
relevant steal): F_R ≤ 3·N*_R, with N*_R the consecutive visit pairs of R with a relevant new steal. §22s's
"F_R ≈ #relevant new steals" and §22u's first line "F_R ≤ #relevant-steal visits at R" omit the 3.

## §22u chain as a conditional statement
- A relevant steal on a consecutive pair is witnessed by a quadruple (R, round r, top τ, tangle t) with t ∈ F_{r,τ} of the
  earlier visit and t ∈ E′_{r,τ}.
- Given (STEAL-ONCE) (each quadruple is newly stolen at most once per phase), distinct pairs have distinct witnesses, so
  N*_R ≤ #quadruples ≤ (#rounds)·(#tops)·#fired(R) ≤ (|R| + 1)·|R|·#fired(R): rounds ≤ |V| + 1 (each non-final round
  removes a vertex of V, 748-760), tops are p-vertices of R, and t ranges over tangles that fired at R.
- With G8-1: F_R ≤ 3·(|R| + 1)·|R|·#fired(R). Given (FIRED-R), #fired(R) ≤ poly(|R|), so (FALL) holds.
- So, as a conditional: (FALL) ⇐ (STEAL-ONCE) ∧ (FIRED-R), and GAP-A ⇐ (CTX⁺) ∧ (STEAL-ONCE) ∧ (FIRED-R), given STR-DET.
  VALID. Neither premise is signed; both are DATA. §22u's own "(n + 1)·n" needs the factor 3.
- The removal of §22t's circularity is real only through (FIRED-R): the count no longer mentions |T_phase|. But (FIRED-R)
  itself has no argument (L-ALG says so), and the number of tangles that fire at a fixed context could a priori grow with
  the number of searches.

## Data (p8probe.py; experiments/alg/instances, 138 files, plus fallv_viol_n28; my own closure and fired-set logging)
| check | stable | Oink |
|---|---|---|
| region steps: EXACT / EXACT* failures | 235,470: 0 / 0 | 246,213: 0 / 0 |
| of which step-deficit steps | 10,178 | 10,860 |
| consecutive visit pairs | 4,361 | 4,617 |
| RV falls with a relevant steal / without | 37 / 0 | 37 / 0 |
| relevant steal without an RV fall | 0 | 0 |
| plain new steal without an RV fall | 259 | 313 |
| (STEAL-ONCE), max per (R, round, top, tangle) per phase: plain / relevant | 1 / 1 | 1 / 1 |
| (FIRED-R), max distinct fired tangles at one context per phase (max ratio to \|R\|) | 14 (0.50) | 14 (0.62) |
- fallv_viol_n28: each fall has exactly ONE relevant steal, tangle 2 at top 24 (where it fired), round 3 at the first
  fall and round 4 at the second. The other new steals at those pairs (tops 26, 25, 20, 15, 14, 13; tangle 3 at 7) are
  not relevant.
- On this corpus the relevant charge is tight (no relevant steal without a fall), against L-ALG's 5 / 5 on its larger
  corpus; RV-fall detection only (Ψ / Φ_top non-rises not separately detected).
- (FIRED-R) ratio 0.62 in Oink order exceeds §22u's "at most 0.5·|R|" on L-ALG's corpus; the absolute max is 14 here vs
  17 there. Small contexts give the high ratio. Data only; no bearing on the verdicts.

## What (FALL) reduces to now
(FALL) ⇐ (RELSTEAL): N*_R polynomial, with F_R ≤ 3·N*_R. Sharper conditional: (FALL) ⇐ (STEAL-ONCE) ∧ (FIRED-R). Open, DATA
only; the obstruction is (FIRED-R): no bound on how many distinct tangles fire at one context in a phase.

## §C. Comparison with REFEREE-2 (R2-P8, referee-2 b8fdd76; read after R-P8 was pushed and merged; 15:55Z by date -u)
Agreement on every verdict. There is no disagreement of substance. (Opus 5.5, D12)
- EXACT*: both SIGN, with the same two-line proof (the code's derivation uses only F_τ; then monotonicity plus EXACT).
  - N8-1 (§22s's ⊆/⊇ labels are swapped): correct. I wrote the inclusions directly and did not flag the labels. I agree
    it is wording only.
  - Both probes: 0 EXACT* failures (mine 481,683 steps on pyref; R2's 927,485 on instrumented C++).
- PREFIX-MONO-X*: both SIGN, including the absorbed case. Both note that (NS*) is weaker than (NS).
- Corollary: both SIGN WITH GAPS with the same gap. My G8-1 = R2's G8-1 = G-P7-c2's factor 3. Closed. Both check the
  "split" gloss.
- §22u chain: both VALID as a conditional with the factor 3, F_R ≤ 3(|R|+1)|R|·#fired(R). Two refinements from R2, both
  accepted:
  - (STEAL-ONCE*), the RELEVANT-triple form, is all the chain needs. It is weaker than (STEAL-ONCE).
  - G8-2. If (FALL) means the sum Σ_{R∈C_bv} F_R, the per-context bound gives it only with |C_bv| polynomial, which is part
    of (CTX⁺). My R-P8 used §22f's per-context reading of (FALL) ("F_R polynomial for each R"). Under that reading
    "(FALL) ⇐ (STEAL-ONCE) ∧ (FIRED-R)" holds as written. Under the sum reading it needs (CTX⁺).
  The GAP-A statement is the same in both reports: GAP-A ⇐ (CTX⁺) ∧ (STEAL-ONCE*) ∧ (FIRED-R), given STR-DET.
- Data (not signed). Both find (STEAL-ONCE) with max 1, and (FIRED-R) above §22u's 0.5·|R|: 0.62 (mine) and 0.67 (R2),
  on small contexts. Only poly(|R|) is claimed.
  - Relevant steals at a rise: 0 in mine (138 files, RV-fall detection) against 5 in R2's (257 files, full Π non-rise).
    The corpora differ. Both show that the relevant charge is near-tight.
- R9 items (Lead's (1)): answered in R-P7 §C2 (876c06e, sent 15:51Z). I confirm (i). On (iii), n per input suffices by
  STR-DET (c), so 2n is true but not needed.
