# R11: the (r2) step of L-ALG's (alpha)-exclusion regress fails on a real A_DTL run (L-RED, 2026-10-16 ~09:55Z; produced on Opus 5.5)
Target (Lead 09:13Z): claude/l-alg docs/alg/DTL-proof.md section 2.3, "Route for excluding (alpha)": a straddle of t' in
search s3 needs a non-monotone pruning change since s2 (when t' was learned). That change needs a straddling tangle created
strictly EARLIER (step (r2)). "Iterating, the straddling tangle with the earliest creation order has no such cause, so it
cannot straddle." GAP-A-M.md section 7 proves (r1) per call with no dominion in between. The open step is (r2).
Status words: DATA / READING.

## DATA (reproducer experiments/red/carry/r2_check.py, in experiments/red/check.sh)
Instance: experiments/red/carry/instances/lalg_dtl_mviol_n20.pg, a byte copy of claude/l-alg
experiments/alg/instances/dtl_mviol_n20.pg (sha1 4cb3335f521fa70d74e4a10f02f03f1953658b42). Run: this lane's tracer
dtl_flipflop.py on L-COMP's dtl_py (exact against the pinned Oink: 1 dominion, 17 tangles, 6 iterations). Labels origK.
1. The first Odd tangle of the run in creation order is t4 = {orig11, orig18}. It is learned in the first Odd search, in
   the deep stable piece 7 (|R| = 13, after seven pieces). Its escapes orig2 and orig10 (the exits of the opponent vertex
   orig11) are outside that piece's R, so they are forgiven there. orig17 (priority 21) is in R but is pruned before the
   stable round, so the player vertex orig18 (priority 4) joins orig11's region.
2. In the next Odd search (same G', no dominion between), first best_vertices call (R = G'), round 0: orig17 is alive and
   its region takes orig18. orig11 (priority 9) is in its own region and has a self-loop. That is Lemma E's shape: (a) a
   tangle vertex is consumed by an earlier region; (b) the unconsumed rest {orig11} has a cycle whose maximum is a
   surviving lower top. L-ALG's dtl_ideal.Anatomy (run read-only with L-ALG's order recipe) reports round 1 of this call as
   a survival-changing deficit (the code prunes orig6, which the ideal union keeps). t4 is the only straddler listed for
   that round.
3. Claim-P drops follow one search later (Odd search 3 -> 4 in the tracer's 0-based count): orig1 and orig16 go from
   round 7 to 6 and orig19 from 8 to 7, as L-ALG read off Oink's trace (8 -> 7 and 9 -> 8, 1-based). Those straddlers
   (t9-t11) were learned after t4.

## READING
- (r2) fails as stated. The earliest-created Odd tangle straddles with the full Lemma-E shape, one search after its
  creation, and no earlier-created Odd tangle exists that could cause it. The regress has no base case.
- The cause is a case the route does not list. The route assumes that "in s3 the same edges exist" and that the forcing
  of s2 applies again at the last region. That holds when t' is learned and used in the same context. Here t' is learned
  in a deep piece, where its escapes were forgiven because they lay in X, and used in the first call, where they are in
  R. Neither listed exception (a top above a in s2 is no longer a top in s3; a sub-tangle straddles itself) is what
  happens: in s2's stable round no top lies above orig11, and orig17's region in s3 belongs to a top that was pruned in
  s2's context.
- So any well-founded regress must order straddles by something other than creation time. A candidate is the depth or
  size of the learning context. The proof lane decides.
- Not shown: that this straddle by itself produces (alpha) (the lowest top's successor inside the orphan). This instance
  breaks the regress step, not (alpha)'s exclusion.
