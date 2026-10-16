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

## Sharper form: in 2CE the CARRY reduces to a fixed-context deficit (READING, unrefereed; L-RED ~09:35Z)
This corrects the layout that (C2) assumed. (C2)'s (s4) and (s5) treat the carry as learned in a stable piece after C_B.
That piece does not exist in the needed form.
(F) Frontier self-sustain. Fix a search s inside one A-state, with the pieces before C_A the same in s and s+1. Let D_0 be
    the first tangle learned in s that fires in C_A of s+1 (first in C_A's attraction order). Its escapes are covered there
    without help from other tangles learned in s, so they lie in C_A's attractor of s or in X before it. Hence, in s, after
    C_A every escape of D_0 is outside R. D_0's vertices are still in R (otherwise the old tangles would already eat its
    top). Its cycle is then rebuilt by plain attraction in every later pruning round, so its top is never a candidate. The
    first best_vertices call after C_A therefore returns STABLE (a -1 result needs an empty V). That call is the stable
    piece P1, and D_0's top is in V*_{P1}. sptl processes it there, and Dom(V*_{P1}) then removes it. So D_0 is learned in
    P1 or not in s at all.
(G) Consequently the gate is evaluated in P1, BEFORE C_B runs, and can depend only on the tangle set. Between two
    consecutive searches of one A-state, P1's context is the same, and exactly one thing changes: the fast level's newest
    tangle. The carry needs P1's sptl to learn D_0 when that newest tangle is the LAST fast tangle, and not before. Gate
    types at P1 (with (E) excluded by (F)):
    (S) A stealer top s is in V*_{P1}(T) but not in V*_{P1}(T + T_last). By L-ALG's Theorem M-cond (GAP-A-M.md
        section 3), this requires a DEFICIT round in P1's pruning under T + T_last. By Lemma E, that is an alive tangle that
        straddles and whose unconsumed rest has a lower-priority cycle maximum. A stealer that stays in V* keeps y: y is
        attracted whenever s is popped, by whichever region holds s, and every such region has cap >= pr(s) > pr(y).
    (O) Order gate: T_last changes the attraction order or strategies inside sptl regions (LIFO pops), so a_{c+1}'s SCC
        changes from one whose escapes are not covered in C_A to one whose escapes are. Not excluded; untested.
Statement for the proof lane: in the class 2CE, a counter with mA >= 2 carries needs, once per A-state, a fixed-context
deficit (or an order-gate switch) at P1 that the fast level's last tangle triggers and that none of its earlier tangles
trigger. A bound on such triggered deficits per context would damp every 2CE counter. L-ALG's dtl_mviol_n20 shows that
deficits happen in real runs. Whether they can be triggered on demand, repeatedly, at one context is OPEN.
DATA for (F): experiments/red/carry/instances/nosig_2_3.pg (carry2 2 3 without the stealer's edges from p1; generated with
a stripped copy of carry2.py, file kept). `python3 experiments/red/carry/show.py <file>`: in every Even search the slow cut
(piece 2, seed sA) is followed at once by a STABLE piece whose V* holds the frontier slow top. That piece learns the slow
tangle ({a1,p1_1,p2_1} in search 0, {a2,p1_2,p2_2} in search 1) BEFORE the fast cut (piece 4, seed sB) runs. With no gate,
both levels advance together: 4 iterations, Oink-consistent (the tracer is exact against Oink, R9).

## Why the gate module dies: the support obstruction at P1 (READING, unrefereed; L-RED ~09:40Z; one case OPEN)
DATA: carry3 2 2 (instances/carry3_2_2.pg). In search 0, P1 learns {k,m,o,q2,tau2} at tau2. Its only escape is sA (q2 ->
sA keeps tau2 dead in piece 0). In search 1, C_A eats the whole module through it (show.py search 1, piece 1). A climb
seeded with this instance (iters fitness, 15k steps) reaches 9 Even searches at n = 47 with no structure; discarded.
General shape. Every gate (stealer, lifting tangle, their supports) is a set of tops that are ALIVE in P1 in every search
of a slow state and PRUNED in piece 0 (piece 0 is a -1 piece; a top in its V* or argmax is removed by its Dom).
Write H for the highest such top and E_0 = X before C_A (piece 0's Dom), E_A = C_A's attractor. Steps:
 (i) What revives H between piece 0 and P1 is forgiveness of a vertex of E_0 or E_A, or a change of region partition. When
     piece 0's argmax top has the lowest priority, E_0 lies in every piece-0 round's union, so E_0 forgives nothing new.
     A partition change (the LIFT, R9 f6) cannot revive the HIGHEST top: its own support is threshold-attracted at its
     own priority level, which forgives it in piece 0 as well. So H's piece-0 blocker e is in E_A.
 (ii) Every vertex of E_A is attracted in piece 0's threshold attractor by threshold tA: C_A's attractor, tangles
     included, is reproduced in R_0 once its seed is (E_0 lies in Z). So H survives piece 0 if pr(H) > tA. Hence
     pr(H) <= tA.
 (iii) If H's region closes in P1, its tangle's escapes are outside R_{P1} (H is the highest top, so nothing above it is
     consumed). They are in E_0 or E_A, and one of them (the blocker e) is in E_A. In the next search, e is popped in
     C_A, every escape is covered, and the vertices have priority <= pr(H) <= tA. C_A eats H's tangle, so the module loses
     its top after one search. That is what carry3 does.
 (iv) (was OPEN; see the DATA below, now closed for the built shape) H is forgiven-type in P1 (its successor is threshold-attracted through a lower region with a low cap,
     never in a region). Then the support passes to lower tops L whose tangles escape into H (inert in C_A). Each such
     tangle is LIFTED into H's region in the next search's pruning (its escape H is popped there with the rest covered),
     which closes H's region. I could only push the closure up one intermediate top per search (the lift cascade), so a
     module with d intermediate tops seems to last about d searches. If that held in general, a persistent gate would
     cost about one vertex per search it survives, which damps the 2CE counter to linear. Unproved.

## The order gate (O) fails the same way (READING, unrefereed; L-RED ~10:05Z)
L-ALG's test (Lead 09:23Z): T_last fires INSIDE a_{c+1}'s sptl region in P1 and changes the DFS parents on every cycle
through a_{c+1}, so that the SCC's escapes move into C_A's attractor. Facts used (dtl.cpp 476-546, 65-185): sptl's
attractor is a stack; str[v] is the first popped vertex that attracts v; str[a] is the first popped successor of a;
a tangle fires at the pop of one of its escapes and pushes its vertices on top of the stack.
(O1) Firing T_last only PUSHES vertices above everything already on the stack, so it can only DELAY earlier-pushed
     vertices. A successor u of a that pops first only because T_last exists is therefore pushed during the exploration of
     T_last's vertices. Then either u is an Even vertex whose str enters T_last's subtree, or u is an Odd vertex with an
     edge into it.
(O2) Even u: the cycle a -> u -> ... -> a runs through T_last's vertices. For T_last to fire in a's region, its escapes
     (b_{mB-1}, down to the chain's anchor) must lie in that region (or be consumed above). If they lie in the region, they
     reach a, and the new SCC contains T_last and every region vertex it reaches, i.e. the whole fast chain with its
     anchor. C_A eats that SCC in the next search, which destroys the fast level. (If the escapes are consumed above,
     T_last does not reach a and there is no cycle through u.)
(O3) Odd u: the SCC can avoid T_last (u -> c1 -> a closes the cycle), but u's edge into T_last's vertex t* becomes an
     ESCAPE of the carry tangle. t* lies in R at C_A and is not eaten by it: a vertex of T_last that C_A ate in every
     state would not be in R_{P1}, and one that C_A eats only together with a_{c+1} deadlocks, since the carry must fire
     before a_{c+1} is eaten. So the carry never fires in C_A.
Conclusion for the class 2CE: all three gate types fail. (E) by (C1). (S) needs a triggered deficit at P1 whose supporting
module the slow cut eats (support obstruction, with the forgiven-type case open). (O) by (O1)-(O3). The (O) argument
leaves one escape: a fast level duplicated per slow state, so that a carry eating one fast copy is harmless. That makes
searches ~ (fast length) x (slow states) with n of the same order, i.e. linear. Remaining routes for a counter: fresh
contexts through cut recursion ((ii) above; L-ALG's replay instances dtl_replay4_n32 and dtl_replay2deep_n32 are the
current data), and the forgiven-type support case.
DATA for (O) (experiments/red/carry/dtl_ogate.py, exact against Oink via the tracer's order recipe): an order-gate event is
an sptl region computed twice with the SAME (player, top, vertex set) but a different SCC of the top. Census, 0 events in
every case: tc+ N = 2, 3, 4, 5; dtl_mviol_n20; L-ALG's dtl_replay4_n32 and dtl_replay2deep_n32; this lane's R9 and R10
instances (278 distinct region keys over 11 files); 3,000 random games with n <= 16 (`--random 3000 16 7`, 7,383 keys).
Adversarial hill-climbs (dtl_search.py fitness `ogate`: events, with OTHER events weighted 100) are running at the time of
writing. So no run has shown L-ALG's (O) mechanism even once, and (O1)-(O3) say that a successful one would not carry anyway.

DATA for case (iv) (experiments/red/carry/liftmod.py d; `show.py` on the output): a module of d tops Y_d > ... > Y_1 behind the
slow cut. Each Y_{i+1} is forgiven through l_{i+1} -> v_i (v_i in Y_i's region, l_{i+1} above Y_i's cap), and Y_1 closes
with q1 -> {Y_1, Y_2..Y_d, sA}. For d = 2, 3, 4: all d tops learn in the FIRST search's P1 ({Y1,q1}, then
{Y1,Y2,l2,q1,v1}, ...). sptl's re-run loop (`while more`) lifts each new tangle into the next region up within the same
piece. In search 1 the slow cut eats the whole module (attracted = every Y_i, l_i, v_i, q1). The lifetime is ONE search,
independent of d. So the lift cascade is faster than the "one level per search" of my reading: it runs inside one stable
piece. With this, every gate-module shape I could build in the 2CE class is eaten by the slow cut within two searches.
