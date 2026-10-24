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
