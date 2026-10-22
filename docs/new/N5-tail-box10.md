# Box 10 (i): can N5's frozen-σ Odd tail follow a CDAG-type chain gen(m)? NO for this family; obstruction named (L-NEW successor 4, Fable 5.1; written 2026-10-21 22:23Z by date -u)
Target: G-N5-TIME, Lead box-10 brief 22:03Z, route (i) of N5-SB-box9.md §5: make the Odd-only tail of N5 (σ frozen at Even's final strategy,
every iteration = Odd's restricted optimum in G_σ over the arena {τ(o)} ∪ Iτ(o), Iτ = Odd's improvements against Even's fresh best reply τ̄)
follow the chain gen(m) of CDAG_n (N5-K9-Pstrict-counter.md), with τ̄'s exploits as the gate masks. Status: NOT BUILT; the gadgeted
Odd-CDAG family gives tails of at most 3 iterations (exhaustive at n = 3, random at n = 4..6); the exact reason is §3. N5 is not killed.
Tools: experiments/new/tail/ (tailsim.py, variants.py, exsearch.py, exsearch2.py, genrule.py, abstractgate.py, masklift.py, lifttrace.py; outputs in tail/logs/).

## 1. Setting (what the tail is)
- Once σ is Even-optimal (Iσ = ∅; Iσ depends on σ only), Even never moves again, and each iteration is Odd's step S4b: τ' = Odd's optimum in
  G_σ (Even fixed to σ) over the arena {τ(o)} ∪ {w : (o, w) ∈ Iτ}. Iτ is the honest VJ00 improvement set of τ in G (Even best-replying with τ̄).
- The GATE of an edge (y, w) with current t = τ(y) is open iff Ξτ(w) ≻_Odd Ξτ(t), i.e. iff Even's best-reply value at w is worse for Even than at t.
  A MASK is an Even exploit (a τ̄-deviation from σ downstream of w) that makes w look at least as good for Even as t.
- Both tail simulations here call n5_lock.step (= n5.py's loop) unmodified: tailsim.tail asserts Even never moves when σ is optimal.

## 2. The family (tailsim.build) and what it does
- Odd vertices 1..n form the dual CDAG: x → u for every u < x, sink 0 (Odd, priority 1, self-loop); priority of v = 2(n+1−v)+1 (v = 1 most
  relevant). Every edge x → u passes an Even gadget e[x,u] (priority 0, never in a path set) with σ(e[x,u]) = u and optional EXPLOIT edges to
  Odd vertices (upward ones allowed) or other gadgets. In G_σ the Odd game is exactly CDAG_n, so an ungated tail is switch-best (1 step).
- Checks in genrule.py: along gen(n) (n = 3..7) the executed step is always among the "rule R" predictions: for y < n, (y, w) fires iff
  τ(y+1) = w; the top fires (n, z−1) with z the largest z ≤ n−1 having τ(z) ≠ z−1 (a binary counter). The rule predicts up to 3 edges at a
  state; gen serialises them; firing them together would only shorten the chain by a constant factor. So a gate realising rule R suffices,
  and rule R reads UPSTREAM state (τ(y+1)) for every y < n.
- Masking load along gen(n) (improving edges not executed): mean 0.75 / 1.82 / 3.12 / 4.56 / 6.09, max 2 / 5 / 9 / 14 / 20 at n = 3..7
  (K10 §2 again, for the Odd side).
- Results (tail from τ0 = all → sink, σ = gadgets direct, σ optimal required):
  | search | configs | best tail with σ optimal |
  | --- | --- | --- |
  | n = 3, exhaustive, ≤ 1 exploit target per gadget (Odd targets 0..3) | 15,625 | 1 |
  | n = 4, random, 0-2 targets per gadget (Odd vertices + gadgets) | 20,000 | 1 |
  | n = 5, random, same | 6,000 | 1 |
  | n = 4 / 5 / 6, random exploits AND random start τ0 (exsearch2.py) | 8,000 each | 3 / 2 / (σ never optimal) |
  Non-optimal σ (Even still moving) gives ordinary N5 runs of 8 / 9 / 10 iterations at n = 4 / 5 / 6: linear-looking, as in every earlier climb.
- Abstract gate rules on the pure CDAG (abstractgate.py; the step is the arena optimum over the open edges, bottom-up with new values):
  "up1" = mask (y, w) iff τ(y+1)'s path set is strictly worse for Odd than τ(y)'s (this is exactly what the exploit e[y,w] → y+1 realises, since
  the current gadget e[y,τ(y)] carries the same exploit and ties are not improvements), and "upall" (any higher vertex). Over ALL n! starts,
  n = 4..7: max steps 3 / 4 / 5 / 6 for none, up1 and upall alike. Up-reading gates do not lengthen the CDAG chain at all.

## 3. The obstruction (L-NEW reading; exact, elementary)
Fact B (favourite target). If t = τ(y) satisfies Ξτ(t) ⪰_Even Ξτ(w) for every successor w of y (t is Even's favourite successor of y under τ̄),
then every edge (y, w) with Ξτ(w) ≠ Ξτ(t) is in Iτ: no mask exists for y. Proof: the gate compares Ξτ(w) with Ξτ(t). □
Consequence for gen(m) in any family where the sink edge is Even's favourite from every CDAG vertex (true here: the sink gives Even the
value (0, ∅, ·), and any path meeting a relevant Odd vertex is worse): in gen(n) the bottom vertex 2 keeps τ(2) = 0 and its improving edge (2, 1)
must stay masked until (2, 1) fires, which is step 7 of 11 at n = 4 and about the middle of gen(n) in general. By Fact B it fires at the first
step instead. Inductively every vertex whose current target is the sink fires to its current best at once, so from τ0 = all → sink the tail
is one step (the table above). From other starts the bottom-adjacent vertices are resolved first and nothing makes them wait again.
Lemma G (K10 §1, dual) covers the other escape: ∅-valued gift paths (gadget chains to the sink, longer paths to an odd sink) mask
state-independently, so they freeze a vertex for the rest of the tail instead of gating it.
What gen(m) needs and this family cannot give: a vertex waiting at Even's favourite target while an improving edge of it is masked. More
generally the mask of (y, w) is an exploit downstream of w (§4), and the condition it must encode for gen (τ(y+1) = w) lives upstream.

## 4. How real tails lift masks (DATA, box-9 instances; masklift.py, lifttrace.py; tail/logs/masklift_n5b9.txt)
Along N5's own runs (best-reward start) on instances/n5b9/* and n5adv/best_n24_seed24:
- Gates of G_σ-improving Odd edges are mostly CLOSED (e.g. tc2: 1,100 of 1,299 edge-iterations; fc1: 985 of 1,182).
- LIFTS (closed → open while τ(y) is unchanged) are common: 16-70 per run, nearly all inside the tail, and most fire at the next iteration
  (tc2: 54 lifts, 42 fire; fc1: 70 / 49; sg3: 48 / 37).
- CLOSURES (open → closed while τ(y) is unchanged) are almost absent: 3 in sg5, 0 in the other ten runs.
- Cause of a lift (lifttrace.py on tc2): the previous iteration's Odd move lies ON Even's exploiting play from w and removes the exploit
  ("exploit on w-play before [9], after []"). So the tail is a cascade of downstream repairs that open upstream gates, one hop per iteration,
  exactly Lemma T's propagation with the gate as the brake. It reads downstream, never upstream.
Candidate (GATE-MONO, DATA, unproved): in a frozen-σ tail an open gate stays open while τ(y) is unchanged (3 exceptions in sg5 to check).
If true it says a waiting vertex's open set only grows, which is the opposite of what a counter needs (gen closes (3,2) after it fired).

## 5. Verdict for route (i)
- The CDAG-type chain gen(m) cannot be the tail's Odd chain in the gadgeted Odd-CDAG family (Fact B + the searches). The same Fact B applies
  to any family in which the chain's bottom vertex waits at Even's favourite target, which every gen-type chain on a DAG with a sink does.
- A tail killer would need masks that read upstream state. The only upstream-reading exploits are paths that climb to a higher vertex and come
  back down; these compare that vertex's current path set with τ(y)'s ("up1"/"upall"), and on the pure CDAG they give at most n − 1 steps.
- Not excluded by this box: a non-DAG G_σ (Odd's one-player game with cycles) in which waiting vertices never sit at Even's favourite target.
  Box 9's climbs over general games (tail ≈ 1.4n, per-vertex flips ≈ n/3) are the evidence against it so far.
