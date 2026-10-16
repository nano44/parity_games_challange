# R10: the CARRY step for DTL, two-level reset+replay (L-RED, box 2026-10-16 08:12Z-16:10Z; produced on Opus 5.5)
Candidate: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7. Status words: DATA / READING / OPEN.

## Interim 1 (~09:30Z)
- DATA: the fast level works alone. experiments/red/carry/bsolo.py mB mA builds a chain b_1..b_mB that a cut (seed s,
  threshold above the chain) eats at a rate of one tangle per search. Each b_i's tangle carries private witnesses g_{i,j}
  (Even, pr 0, -> b_i). bsolo 4 2: 4 Even searches, one tangle each, plus the closing search
  (`python3 experiments/dtl/../red/dtl/dtl_flipflop.py` on the output; Oink MATCH: 2 dominions, 4 tangles, 7 iterations).
- READING (redundancy): in one best_vertices call, a stored tangle whose top is still in V adds nothing to the threshold
  attractor: plain attraction from the top rebuilds it once its escapes are covered. A tangle can change a pruning round
  only (i) after its top has been pruned, or (ii) by being lifted into a HIGHER top's region, where it covers vertices of
  priority between its top and that top (cap effect). This is why a deep-learned carry driver is hard to use in piece 0.
- First 2-level wiring (experiments/red/carry/carry2.py): the slow chain is eaten by an earlier cut (seed sA); eating a_j
  also eats the witnesses g_{.,j}, which kills every fast tangle of the old state (f1). The carry gate is an Even vertex
  p1_k that a high "stealer" top sigma takes while the fast level is unfinished, so the carry tangle has NO gate escape.
  First run (carry2 2 3): FAILS for a design reason. sigma's high cap pulls almost the whole game into its region at
  piece 0, so piece 0 is stable and nothing is counted. Next step: confine the stealer so its region holds only the
  p1's (lower its cap, or block the Even back-paths a_k -> p1_k).

## The CARRY obstruction for two cut-eating levels (READING, unrefereed; L-RED ~09:10Z)
Class 2CE. Within one search_rec call, the slow level A is a chain a_1..a_mA eaten one per A-step by a cut C_A (threshold
tA). The fast level B is a chain b_1..b_mB eaten one per search by a LATER cut C_B (threshold tB). The fast tangles carry
witnesses W_j, which C_A eats together with a_j, so every fast tangle of an older state dies (f1). The carry tangle at
a_{c+1} must be learned in the stable piece P after C_B only once B is exhausted (b_mB eaten), and must fire in C_A of the
next search. Its escapes must therefore be in C_A's attractor or outside R there.
(C1) Gate dichotomy. What unblocks a_{c+1}'s region in P when B is exhausted is one of:
  (E) an Odd vertex of the would-be tangle loses a successor from R_P. That successor is an escape of the tangle. It is
      eaten only by C_B or later (else it would be outside R_P in every state and gate nothing), so it lies in R and outside
      C_A's attractor in the next search. The carry cannot fire in C_A.
  (S) an Even vertex y on every cycle through a_{c+1} is no longer taken by a region that sptl computes earlier, i.e. a
      "stealer" top s in V*_P while B is unfinished leaves V*_P when B is done.
  Priorities are static and V*-membership of a_{c+1} reduces to (E)/(S) applied to its pruning. So the gate is (S).
(C2) What (S) forces:
  (s1) pr(s) > pr(a_{c+1}) (its region is computed first).
  (s2) a_{c+1} lies in s's region whenever y does. Every successor of a_{c+1} that sits in its region depends on y (a
       successor that does not would give a cycle avoiding y), so an Even a_{c+1} is attracted through it and an Odd
       a_{c+1} has all its edges there; caps allow it since pr(a) < pr(s). Hence every vertex that C_A eats with a_{c+1}
       through attraction of priority <= pr(s) lies in s's region in P (or in an earlier region). That includes the
       witnesses W_{c+1}, unless they are protected by caps.
  (s3) W_{c+1} must sit in the fast tops' regions in P. So either every b_i is processed before s (pr(b_i) > pr(s)), or
       the witnesses hang on a_{c+1} through a vertex of priority > pr(s). C_A can eat such a vertex only if tA > pr(s).
  (s4) s must leave V*_P when C_B eats b_mB, without being eaten itself (if C_B eats s, it eats y: pr(y) <= pr(a) <= tA
       < tB by (s5)). Removing vertices from R never uncovers an Odd link, and an Even link that loses its support is
       eaten if its priority is <= tB. So the support chain from s to the eaten part passes a vertex of priority > tB:
       pr(s) > tB (also when s is kept alive through a forgiving threshold).
  (s5) C_A precedes C_B. If C_B's seed reaches X only through C_A's attractor, C_A attracts the seed itself unless
       tB > tA. So tB > tA.
  Combining: if pr(b_i) > pr(s) for all i, then (s4) gives pr(s) > tB >= pr(b_mB) > pr(s). Otherwise (s3) gives
  tA > pr(s) > tB > tA. Both are contradictions. So no 2CE wiring has a carry. This is the failing step of R9 section 4b,
  stated for this class.
Routes the statement does NOT cover (open): (i) a non-cut piece between C_A and C_B that supplies C_B's seed target, so
(s5) need not hold. My first paper attempt fails because that piece's context contains the uneaten a's with the fast level
pruned, so the gate is open there and the carry is learned too early. (ii) The fast level inside the recursion of C_A's
remainder (fresh context). (iii) Levels living in pruning rounds instead of cuts, where L-ALG's straddle reset (Lemma E,
GAP-A-M.md) acts at a FIXED context. A straddle is a region phenomenon, so it cannot act inside a cut attractor.
