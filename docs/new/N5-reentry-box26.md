# N5 on o-cyclic 𝒞^1O, box 26: re-entries into R are NOT all route improvements; what is proved, and what is left
L-NEW successor 9 (Opus 5.5, D15). Lead GO 2026-10-24 12:58Z (date -u), box to ~16:00Z, stop rule ~15:15Z. Target: the lead named in
docs/agents/N5-STANDDOWN.md ("every re-entry into R inside a joint λ-phase is a route improvement in G[R] against τ; count those by
R17's machinery"), toward (TRUST) (docs/new/N5-1Ocyc-box25.md §6).
Status: the named statement is FALSE (smallest verified instance n 11). Two lemmas are PROVED from the definitions, and they reduce
(TRUST) to (CYC) plus a per-θ-stretch route count. No polynomial claim. Nothing refereed. G-N5-TIME stays OPEN.
Notation as in box 25 (N5-1Ocyc-box25.md), box 21 §3.5 (Lemma G, hypothesis (h)) and box 22. Code is in experiments/new/box25/
(reentry.py, reperphase.py, routemono.py, routeclimb.py, shrink_theta.py, thetasearch.py, thetareclimb.py). Every instance cited is
checked: Oink zlk OK, strategies verified (check_sol2.py).

## 0. Result
- FALSE: "every re-entry into R inside a (τ, joint-λ)-phase is a strict route improvement". Re-entries driven by θ alone (w unchanged,
  route identical) occur. Smallest verified instance: n 11, box25/thetare_n.pg (§2). On the pinned instances they are as common as
  route re-entries: returns_rt48 21 vs 21, returns_ph64 23 vs 30 (§1).
- Why L-RED's R58 §12d (ii) saw "0 of 20" (READING of experiments/red/n5inj/retcheck.py):
  - Its class A is "θ at the re-entry ▷ w at the leave". That is impossible while w is constant, because θ ⊴ w always (Lemma S (b)).
  - Its class B ("route improved") is the fall-through; it never compares routes.
  - It also counts only returns to the same successor.
  The data were right; the class names were not.
- PROVED (§3; Lemma RE modulo one narrow sub-case, gap G26-1), inside a stretch where τ and θ are constant and (h) holds:
  - Lemma RM: route values of vertices staying in R never decrease;
  - Lemma RE: every re-entry strictly improves the re-entering vertex's route.
  Hence pure θ-re-entries of a vertex are separated by θ-changes, and per joint λ-phase:
      re-entries ≤ n · (#θ-changes in the phase) + Σ_x (#strict route increases of x inside θ-constant stretches).
- So (TRUST) reduces to two open pieces:
  - (CYC), θ-changes per phase (L-RED plateau 16, R58 §11a);
  - (ROUTE-BF), strict route increases per vertex per θ-stretch. DATA max 3 on the pinned instances; climbs in §4.
  (ROUTE-BF) does not follow from R17 in general.
  - On a stretch where R is also constant, R17 applies to the "route game" (Lemma RBF, READING, §5): at most |R| − 1 route changes.
  - So the remaining count is the number of LEAVES from R inside a θ-stretch. Leaves are o-free wins, which brings back the
    trust-mode deadlock (§5').

## 1. The classifier and the counts (DATA; box25/reentry.py)
- Definitions:
  - LEAVE of x at transition L: x ∈ R_L, x ∉ R_{L+1}.
  - RE-ENTRY at E > L in the same (τ, joint-λ)-phase: x ∉ R_E, x ∈ R_{E+1}. Any successor counts, and so do downstream entries.
- Classes, against x's last leave:
  - ROUTE: route value strictly better. The routes π^L, π^{E+1} are compared on one terminal T = W_{E+1}(o), by Lemma G (c).
  - WRISE: not ROUTE, and w rose. That is one-player progress of o's continuation in G_τ.
  - THETA: not ROUTE, w unchanged, θ rose. A pure throttle release, split into release (θ reaches w) and partial (θ stays ◁ w).
  - OTHER: none of these.
- Leave kinds: arena step, fallback (S4c), or downstream (x itself did not switch).

| instance (canonical start) | n | ROUTE | WRISE | THETA (release / partial) | OTHER | leaves (fallback / downstream / arena) |
| --- | --- | --- | --- | --- | --- | --- |
| fts_best16 | 16 | 2 | 0 | 2 (2 / 0) | 0 | 4 / 0 / 0 |
| theta_tp32 (L-RED) | 32 | 0 | 0 | 4 (3 / 1) | 0 | 3 / 1 / 0 |
| returns_rt48 (L-RED) | 48 | 21 | 0 | 21 (10 / 11) | 0 | 34 / 8 / 0 |
| returns_ph64 (L-RED) | 64 | 30 | 0 | 23 (11 / 12) | 0 | 41 / 12 / 0 |
| tr20_s4 (box 25) | 20 | 3 | 0 | 0 | 0 | 0 / 3 / 17 |
| 35,627 random o-cyclic runs, n 4-14 (seed 111 canonical, seed 112 random starts) | | 1 | 0 | 0 | 0 | 152 / 3,312 / 2,088 |

- Every THETA re-entry on these instances has (h) at its leave and at its re-entry, and its route is identical.
- Every THETA re-entry follows a fallback or downstream leave. That is expected (§3 remark): after an arena leave, the selection
  preferred the o-free route against w, so an unchanged route can come back only if w rises (WRISE).
- Per phase (reperphase.py):

  | instance | longest phase | θ-changes | THETA | ROUTE |
  | --- | --- | --- | --- | --- |
  | fts_best16 | 26 | 8 | 2 | 2 |
  | theta_tp32 | 41 | 16 | 4 | 0 |
  | returns_rt48 | 78 | 3 | 21 | 21 |
  | returns_ph64 | 103 | 3 | 23 | 30 |

  On rt48 and ph64 one θ-change releases a batch of about 7 vertices.

## 2. Smallest verified θ-driven re-entry: n 11
box25/thetare_n.pg (n 11, sha1 64698459c7a9…, canonical start).
- Obtained by shrink_theta.py (edge deletion, vertex deletion, single-successor contraction, priority lowering, keeping a THETA
  re-entry with (h)) from thetare_min.pg (n 15, sha1 753f5c04…), itself shrunk from fts_best16.
- Oink zlk OK, strategies verified. N5: 7 iterations, 1 fallback.
- Searches for smaller instances found none:
  - thetasearch.py, random n 6-12: no hit;
  - thetareclimb.py, n 8-14: flat fitness, no hit within the run.
- Game. Priorities v:p, Odd vertices marked (O), o = 2:
  - 0:0 → {0, 5}; 1:3 → {7, 10}; 2:2 (O) → {1, 6}; 3:1 → {2, 9}; 4:0 → {2, 7}; 5:4 → 9;
  - 6:5 → {5, 8}; 7:5 → 8; 8:0 → {2, 8}; 9:0 → {3, 7}; 10:0 → {0, 4}.
- The run, one (τ, joint-λ)-phase over states 1-7, τ(o) = 6 throughout:
  - State 3: w = (8, {2, 6}, 2), via o → 6 → 8 (8's self-loop, priority 0). θ = (8, {1, 2, 7}, 3), via σ̄(o) = 1 → 7 → 8. So θ ◁ w.
  - Vertex 4 routes 4 → o and is trust-routed:
    - honestly 4 → 7 is better: (8, {7}, 2) against (8, {1, 2, 7}, 4), since the odd vertex 1 (priority 3) is the top difference;
    - against τ, 4 → o is better: (8, {2, 6}, 3) against (8, {7}, 2), since the odd vertex 7 (priority 5, index 7) outranks 6.
    So the arena keeps 4 on o.
  - The arena stalls, and the fallback at 3 forces 4 → 7 (a leave).
  - State 5: θ = (8, {1, 2, 5, 7, 9, 10}, 7), with the even vertex 5 (priority 4) now on o's honest continuation. w is unchanged.
  - Transition 5 → 6: 4 → o again on the same route [4]. Honestly o is now better (the even 5 is the top difference). Still θ ◁ w,
    so this is a partial release.
  - Vertex 10 re-enters at 7 by a strict route improvement (class ROUTE).

## 3. PROVED: routes are monotone inside θ-constant stretches; re-entries there are route improvements
Setting: an N5 transition k → k+1 inside one (τ, joint-λ)-phase, with θ_k = θ_{k+1} =: θ and (h) at both states. For x ∈ R, π_x is x's
σ-path to o (o excluded). Its ROUTE VALUE is π_x ⊕ T for a fixed terminal T, compared as in Lemma G (c): the same cycle node c, and
path sets differing only on π Δ π'. So the comparison does not depend on T.
- Lemma RM. If x ∈ R_k ∩ R_{k+1}, then route_{k+1}(x) ⊵ route_k(x).
  Proof.
  - By Lemma G (b) at both states, Ξ_j(x) = π_x^j ⊕ θ. Under (h) the honest play from o avoids π_x^j.
  - By R15 (a), Ξ_{k+1}(x) ⊵ Ξ_k(x).
  - Both sides have terminal θ, so they share the cycle node c and θ's path set. The comparison is therefore the route comparison of
    Lemma G (c). □
- Lemma RE. Let x leave R at L and re-enter at E (next entry after L), with θ and τ constant and (h) at every state from L to E+1.
  Then route_{E+1}(x) ▷ route_L(x). So a THETA re-entry needs a θ-change in (L, E].
  Proof.
  - At the leave, Ξ_{L+1}(x) ▷ Ξ_L(x):
    - if x switched, it used a gate edge (honest-improving at L). R15 (a) at its new successor and strict prefix monotonicity
      (R17 (V2)) give the strict gain;
    - if x did not switch, the first vertex of π_x^L that switched did so on a gate edge, and the same argument applies along the
      unchanged prefix.
    - GAP G26-1: both cases assume x's (respectively the prefix's) new play closes no new cycle through x or the prefix.
      - Inside a joint λ-phase, such a cycle would need the same cycle node c as before, so it is a narrow case. I have not ruled
        it out in writing.
      - DATA: class OTHER (no strict gain) never occurred, 0 in all samples.
  - R15 (a) gives Ξ_{E+1}(x) ⊵ Ξ_{L+1}(x).
  - By Lemma G (b), Ξ_{E+1}(x) = π^{E+1} ⊕ θ and Ξ_L(x) = π^L ⊕ θ. Cancelling θ as in Lemma RM gives route_{E+1} ▷ route_L. □
- Corollary (counting; PROVED modulo G26-1). Inside one joint λ-phase with (h) throughout:
  - Consecutive THETA re-entries of x have disjoint leave-to-re-entry intervals, each containing a θ-change. So THETA re-entries
    per phase ≤ n · (#θ-changes in the phase).
  - Inside a θ-constant stretch, x's route value (read whenever x ∈ R) is non-decreasing (Lemma RM within stays, Lemma RE across
    gaps), and strictly increasing at every re-entry.
  So: re-entries ≤ n · (#θ-changes) + Σ_x (#strict route increases of x inside θ-constant stretches). □
- Remark (why THETA follows fallback or downstream leaves). After an ARENA leave, the selection preferred the o-free value h over
  π^L ⊕ w. A re-entry on the same route needs the selection to prefer π^L ⊕ w' over h' ⊵ h, so it needs w' ▷ w (WRISE). This is
  READING: it uses W-monotonicity at the o-free side, which holds at arena steps (box 21 Lemma W).
- DATA for Lemma RM (routemono.py): 0 decreases under (h) on every pinned instance and in two random samples of 6,000 games
  (n 5-14; seed 121 canonical, seed 122 random starts). Every decrease seen (95 in the random samples, 1 on wd16_s2) is at a
  non-(h) state, where Lemma G (b) does not apply.

## 4. (ROUTE-BF): strict route increases per vertex per θ-stretch (DATA)
- Unthrottled stretches (θ = w) need no new count. Under (h), Lemma G gives Ξ = W and gate = G_τ's improving set, so box 21's Lemma
  PT applies and R17 bounds value changes (route increases included) by n − 1 per λ_W-phase of arena steps.
  - A first climb that counted all (h)-states found exactly this: 9 increases at n 16 in a 9-iteration phase, θ = w throughout,
    every vertex in R. That is R17's regime, not a new phenomenon. Stopped.
- So (ROUTE-BF) is about THROTTLED states (θ ◁ w):
  - pinned instances: fts_best16 1, returns_rt48 3, returns_ph64 3, thetare_n 0;
  - random games, n 5-14: max 2 (routemono.py; all (h)-states);
  - throttled-only climb: routeclimb.py (fitness = max strict route increases of one vertex inside one throttled θ-stretch,
    canonical start; 1,500 s each, 13:07-13:33Z). FINAL:

    | run | n | max strict route increases (one vertex, one throttled θ-stretch) | iterations (fallbacks) | phases | re-entries | instance (sha1) |
    | --- | --- | --- | --- | --- | --- | --- |
    | rtt16, random seed 5 | 16 | 11 | 14 (1) | [12, 1, 1] | 0 | box25/instances/rtt16.pg (1775c8b0e0f1…) |
    | rtt24, random seed 6 | 24 | 10 | 14 (0) | [11, 1, 2] | 0 | box25/instances/rtt24.pg (f08e4498f5a0…) |
    | rttf48, seeded from returns_rt48 | 48 | 10 | 13 (0) | [11, 1, 1] | 0 | box25/instances/rttf48.pg (4495be390ab1…) |

    - All three: Oink zlk OK, strategies verified.
    - In every best, the increases come from one long throttled stretch in which R hardly changes (no re-entries). That is Lemma
      RBF's regime (§5): the count is at most the stretch length, below n − 1.
    - Seeded from rt48, the climb traded the 78-iteration phase for this pattern.
    - No climb produced route increases that pile up across changes of R, the configuration (ROUTE-BF) would need for growth.

## 5. Where the count stops (READING)
Lemma RBF (READING with a proof sketch). Take a stretch in which τ, θ and the set R are constant, (h) holds and no S4c fallback fires.
Then the routes of R's vertices change in at most |R| − 1 steps.
Sketch: restricted to R, each N5 step is an R17 arena step of the one-player ROUTE GAME (vertices R, edges R → R, o a terminal):
- Gate ∩ (R × R) is the route game's improving set (Lemma G (c)).
- A vertex that stays in R picks, among its gate edges into R, the best route against the common terminal w. That is the route
  game's arena optimum, (F1).
- Routes are monotone (Lemma RM), which gives (F2).
R17's Lemma P then holds verbatim for R-internal o-paths. In Theorem PH all plays of the route game end at the terminal (one phase),
so after |R| − 1 steps every route is route-game optimal. DATA: the throttled climb best at n 16 (§4) has R constant over 11 states,
and one vertex's route improves 10 times, so the bound is nearly tight.
- Consequence: inside a θ-stretch, strict route increases ≤ n · (#changes of R in the stretch + 1), and the changes of R are leaves
  and (re-)entries. The count is circular: re-entries are paid by route increases, and route increases are bounded per R-constant
  piece, whose number is the number of entries and leaves. A bound needs an independent count of the LEAVES inside a θ-stretch.
  - Leaves are o-free wins: arena leaves, where the W of the o-free side beats π ⊕ w, and fallback or downstream leaves (box 25 §3,
    §5 (4)).
  - So the open quantity, once more, is o-free progress against trust-routed vertices.

### 5'. Where the count stops: the trust mode again (READING)
- Route improvements inside R are one-player moves:
  - an R → R switch is compared the same way by the gate and by the selection (Lemma G (c));
  - an arena step's R-part is route-optimal among gate edges into R.
- R17's Lemma P on routes would read: "after j steps of a θ-stretch, x's route value ⪰ every o-path of ≤ j edges from x".
- Case B fails where such an o-path passes a vertex y ∉ R whose entering edge is withheld (Lemma G (d1)): π_y ⊕ θ ⊴ W(σ(y′)).
  - Inside a θ-stretch the withheld set changes only when W on the o-free side changes, and that W can drop at fallbacks (box 25 §3).
  - The o-free side is in turn blocked by trust-routed vertices (box 25 §5 (3)).
- So (ROUTE-BF) meets the same two-sided deadlock: routes are blocked by withheld entries, and o-free values by trust routings.
  R17's induction does not close on either side.
- What this box adds: θ-driven re-entries are now accounted for exactly (n per θ-change). The remaining unbounded quantities are
  (CYC) and (ROUTE-BF).

## 6. For L-RED (READING)
- A θ-driven re-entry is NOT by itself a kill ingredient: it costs at most one re-entry per vertex per θ-change (§3 Corollary).
- A kill through re-entries needs one of two things:
  - super-polynomially many θ-changes in a phase (CYC); the plateau is 16 at n 24-40;
  - super-polynomially many strict route increases of one vertex inside one θ-stretch (ROUTE-BF), i.e. routes to o that keep
    improving while θ is frozen.
- The smallest instance of the batch mechanism (one θ-change releasing several trust vertices) is still returns_rt48 / ph64
  (n 48 / 64); thetare_n has one release.
