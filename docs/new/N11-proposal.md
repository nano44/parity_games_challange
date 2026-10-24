# N11 proposal: N5-HT, N5 with an honest override at trust conflicts (D14; PROPOSED, NOT RUN)
L-NEW successor 8 (Opus 5.5, D15), box 22, 2026-10-24 (date -u in the commit). Lead brief 01:47Z: "propose, but not run, your own
next (c) approach under D14, as a one-page note". Nothing below has been implemented or tested. No claim.

## Why (from boxes 21-22)
- N5's Even step is a gated best reply. The gate is honest (Iσ, computed against Odd's fresh best reply σ̄), and the selection
  trusts τ (Lemma S).
- Every inductive invariant tried for N5's stretch bound fails at one configuration, the trust-mode deadlock
  (N5-1O-box22.md §1.3-§1.4):
  - a vertex z keeps a route through o because τ makes it look good, although an honest-improving o-free edge is gated;
  - an upstream x is then withheld from z.
- Removing the trust altogether (selection against σ̄) gives Schewe's switch-best, which is exponential (BARRIERS B8). So trust
  is what N5 uses to escape B8, and it is also what creates the deadlock.
- N5-HT keeps the trust except where it conflicts with an available honest improvement.

## The rule (SPEC sketch; S1-S3, S4b, S4c and S5 as in N5-ssi-global.md)
S4a' (Even; Odd symmetric on G^d):
1. σ_W := the N5 step, i.e. the optimum over A(σ) against τ.
2. Conflict vertices C := Even vertices x where the honest value of σ_W's choice is below the honest value of the best gated
   option. Precisely: Ξσ(σ_W(x)) ◁ max_{(x, z) ∈ Iσ} Ξσ(z) (values read at the current σ, as in S2).
3. σ' := σ_W outside C. On C, σ'(x) := argmax_{(x, z) ∈ Iσ} (Ξσ(z), z), the S4c rule.
4. σ' changes σ only on edges of Iσ ∪ {(x, σ(x))}, so σ' is σ switched on a subset of Iσ.

Hence:
- Termination: RESULTS R15 (c) applies verbatim (any nonempty subset of Iσ goes strictly up in ≺).
- Correctness at the stop: unchanged (Iσ = Iτ = ∅, R15 / VJ00 as for N5).
- Cost per iteration: N5's plus one pass over Iσ.

## Barrier screen (docs/lit/BARRIERS.md)
- B8 (switch-all, switch-best): the override is switch-all-like on C. If C is large at every step, N5-HT behaves like
  switch-all, which is exponential (Friedmann). The first test is therefore switchallexp / switchbestexp.
- B9 (index-based rules): not index-based, since the override uses honest values.
- B11 (DLM, symmetric SI "independently of the rule"): Thm 1 is for SSI's arenas. N5 escapes DLM by jump-ahead switches
  (R57 §3), and N5-HT keeps them outside C. Must be tested.
- L1 (local potentials lapped by delay lanes): N5-HT has no new potential. R15's order is untouched.
- R58 Theorem W: still applies, so long runs must be wide.
- Evasion reading (READING, unproved): on 𝒞^1O, a conflict at z is exactly trust mode. With the override, z leaves R as soon as
  its o-free edge is gated, which removes the deadlock that breaks I3 / I4. I4 may then become provable there, and §2 of the
  box-22 file would give ≤ 2n − 2 steps per stretch.

## Cheapest falsification test (< 2 h; to be run only after a Lead GO)
1. Implement n5ht.py: n5x.step plus steps 2-3 above. Count conflicts per iteration.
2. Kill tests, in this order, each with verify:
   - switchallexp and switchbestexp N = 2..8 (B8);
   - DLM families 1-2 from DLM's start pairs (B11);
   - L-RED's HLg_k, G_ζ, sym_h* (R56, R57);
   - box 21's frozen-τ* climbs (fts_g43, fts_best39).
   Dead if any family grows faster than n^3 at the sizes that run.
3. Invariant test: I3 / I4 (box22/shrinkP.py predicates, HREQ = NOFB = 1) on random 𝒞^1O games and on i4_hand.
   - If I4 holds there, the next box is a proof attempt of N5-HT on 𝒞^1O.
4. Climb (box21/climb_fix.py modes, fitness = iterations) at n 16 / 24 / 32, as a quick screen.
- Cost: ~1 h to implement, ~1 h of runs. Oink is built (scripts/setup_oink.sh).

## Second option, noted, not ranked
"N5 from a relaxation-guided τ_0" (Theorem B (c): an optimal τ_0 turns N5 into the frozen run). It is cheap but heuristic: it
changes the start, not the worst case. It is not proposed as a (c) approach.

## FREEZE (box 23, Lead GO 02:16Z Oct 24; written 02:16Z by date -u, BEFORE any run)
The rule is frozen exactly as coded in experiments/new/n11/n5ht.py (sha1 598cc9000e293e2a6e59e0cc9b030dd0b4912604). Results cite the commit that adds this section.
- S1-S3, S5: as N5 (N5-ssi-global.md SPEC; the same si.py engine, dual game, best-reward start, output Engine.regions(σ)).
- S4a' (only if Iσ ≠ ∅):
  1. σ_W := N5's S4a step, computed by the same code as n5.py.
  2. For each Even x with at least one edge in Iσ, compute b(x) := max over (x, z) ∈ Iσ of (key(Ξσ(z)), z). Here key is si.py
     Engine.key, "larger = better for Even", and Ξσ is the valuation at the CURRENT σ, not at σ_W.
  3. x is a conflict iff key(Ξσ(σ_W(x))) < first component of b(x), a strict comparison of valuations.
  4. For every conflict x, σ'(x) := the second component of b(x). Ties in valuation go to the larger index, the S4c rule.
  5. Elsewhere σ'(x) := σ_W(x).
- S4b' (only if Iτ ≠ ∅): the same on G^d, with τ_W := N5's S4b step and Ξτ, Iτ, Ed.key ("larger = better for Odd").
- Both steps start from the same (σ, τ) and are applied together.
- S4c (unchanged): if σ' = σ and τ' = τ, one switch-all fallback. Even goes first, choosing by max (key(Ξσ(w)), w); Odd only if
  Iσ = ∅. The fallback is counted.
- An iteration is a pass with Iσ ∪ Iτ ≠ ∅. Conflicts are counted (cE + cO per iteration).
- Termination and correctness: σ' and τ' are σ and τ switched on subsets of Iσ and Iτ, so RESULTS R15 (c)-(d) apply.
Faithfulness check (condition 2): run(..., ht=False) is N5. On a sample, (a) the ht=False traces must equal n5.run, and (b) every
n5ht run with 0 conflicts in every iteration must give a trace equal to n5's. Both are asserted in n11/faith.py.
Verification (condition 3): every reported run goes through experiments/new/check_sol2.py (Oink zlk regions, both strategies
verified).
