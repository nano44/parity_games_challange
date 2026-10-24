# o-cyclic one-Odd-choice games: what survives of the box-24 argument, and the exact obstruction (box 24, second half)
L-NEW successor 8 (Opus 5.5, D15). Lead routing 03:15Z (date -u): continue on the o-cyclic case, stop rule ~05:00Z.
Status: one partial lemma (PROVED under a stated hypothesis; DATA without it), the obstruction with instances, and no surviving
induction. Not refereed.
Companion: docs/new/N5-1Oacyc-box24.md (packet P-N5-1OA, the o-acyclic theorem). Its Steps 1-2 (Prop X, Lemma 1) hold for every
𝒞^1O game. Steps 3-5 are where the o-acyclic hypothesis is used.

## 1. What replaces "o's exits lie in X"? The partial lemma
Notation as in P-N5-1OA §1, with U_τ(v) := Odd's honest valuation at v read in G's order. By Lemma S (a) this is the pointwise
maximum over Even strategies of V_{·,τ}(v). An exit e of o is COMPLETE at state k if Ξ_k(e) = U_{τ_k}(e), and INCOMPLETE otherwise
(then Ξ_k(e) ◁ U(e)).

Lemma 2' (PROVED given Prop X and (P), under hypothesis (H): the (σ_k, τ_k)-play from o does not return to o).
Statement: in any 𝒞^1O game, at a pure transition from state k with θ_k ◁ w_k, the punishing exit a := σ̄(o) is incomplete.
Hence a ∈ Y, since every exit in X is complete by Lemma 1 and Lemma S (a).
Proof.
- Suppose a is complete: Ξ(a) = U(a). Let b := τ(o).
- a's honest play does not return to o; otherwise σ̄(o) would close a cycle through o, and then the remark below applies. So
  θ = o ⊕ Ξ(a).
- By (H), w = o ⊕ W(b), and W(b) = V_{σ,τ}(b) ⊴ U(b).
- If U(b) ⊴ U(a), then w ⊴ o ⊕ U(a) = o ⊕ Ξ(a) = θ, which contradicts θ ◁ w. So U(a) ◁ U(b). That says a is strictly better
  for Odd than b in Odd's honest order (Lemma R), so (o, a) ∈ Iτ.
- Then S4b moves τ (P-N5-1OA Step 3), and the transition is not pure. □
- Remark: if σ̄(o) = a closes a cycle through o, then a ∈ Y trivially, since a reaches o.

DATA (experiments/new/box22/incomplete.py, without assuming (H)):
- 4,000 random 𝒞^1O games (n 4..14): 172 pure states with θ ◁ w.
- fts_best16: 24 such states.
- In every one, a ∈ Y and a is incomplete (0 exceptions).

What the lemma says.
- In the o-acyclic proof the throttle θ ◁ w dies at the first pure step, because exits are frozen and complete.
- In o-cyclic games the throttle can survive pure steps, but only through an incomplete exit in Y.
- So the natural replacement potential is "the number of incomplete exits". Ξ only rises and U_τ is fixed while τ is, so each
  exit becomes complete at most once per τ-block.

## 2. Why that potential does not give a bound: the self-throttling exit (the obstruction)
- On fts_best16 (box 21 §3.4; n 16, canonical, τ never moves) the exits {2, 4, 5, 14, 15} are ALL incomplete at states 2-25 and
  ALL become complete together at state 26 (incomplete.py, per-state output). So completion events give nothing until the end.
- Mechanism (DATA, 24 of 24 throttled pure states of fts_best16):
  - the punishing exit a's best route against τ (Even's best reply τ̄ to τ) passes THROUGH o;
  - but a itself currently avoids o's reach set R.
  - So a's honest value through that route is capped at π ⊕ θ, with θ = o ⊕ (minimum exit value). And a's entering edge is
    withheld (Lemma G (d1)).
  - The exits throttle themselves: θ is low because the exits are low, and the exits are low because their good routes go
    through o, which is valued at θ.
  - θ can rise only through o-FREE improvements inside the exit regions. Each rise moves σ̄(o) to the next lowest exit, which
    gives the laps 14 → 15 → 4 → 2 → 14 → … of box 21 §3.4.
- Random games show a second, smaller mechanism: 39 of 172 throttled pure states have a ∈ R. There σ̄(o) closes an Odd-good cycle
  through o, the honest cycle node at o changes, and this is bounded by Lemma Φ (box 21 §2.3). 43 of 172 have a's best route
  through o (the self-throttling case).
- So in o-cyclic games the open quantity is exactly (CH-1O) restricted to self-throttled stretches: how many o-free value
  increases can the exit regions make while every exit's good route runs through o? Nothing proved here bounds it, and the per-path
  inductions of box 22 fail on the same configuration.

## 3. Smallest instances
- Lemma 2's conclusion (θ = w at pure steps) fails already at n = 4: experiments/new/box22/instances/cyc4.pg (sha1 bff7a8c2…).
  - Vertices (priority): 0 (4) self-loop; 1 (1) → {0, 2}; o = 2 (4, Odd) → {1, 2, 3}; 3 (6) → {0, 1}.
  - Canonical run: 1 iteration; Oink zlk OK, strategies verified.
  - At state 0: τ(o) = 1 and σ̄(o) = 3, with θ = (0, ·) ◁ w = (2, ∅, 0).
  - Exit 3 is incomplete: its current route 3 → 0 is bad. Even's best reply would route it 3 → 1 → o, which is the
    self-throttling shape. So Odd's honest gate sees no improvement, and Odd stays at τ(o) = 1.
  - Even repairs 3 → 1 in one pure step, and θ = w. The throttle survives exactly one pure transition here.
  - Found by cycsearch.py: the first hit among o-cyclic games at n = 4.
- A pure block longer than R17's one-player per-phase bound: fts_best16 (n 16). X = ∅ and τ is constant, so all 27 transitions
  of its long λ-phase are pure (27 > 15).
  - cycclimb.py (fitness = longest pure run in one joint λ-phase − (n − 1); 1,500 s at n 8 / 10 / 12 / 14) found none with
    positive fitness. Final numbers are in the box-end message.
  - So the smallest such instance has 15 ≤ n ≤ 16, unless a longer search finds a smaller one.

## 4. Stop rule
No induction for the o-cyclic case survived. Every candidate needs to bound the o-free progress of self-throttled exit regions,
which is the same counting problem as (CH-1O), with nothing frozen. Per the Lead's rule I stop here.
Open statement for a successor or for L-RED's θ-change families:
- (CYC) In o-cyclic 𝒞^1O, the number of θ-changes inside stretches where τ is fixed and some exit is incomplete is poly(n).
- (CYC) is not enough on its own. In o-cyclic games, the analogue of P-N5-1OA's Lemma 3 (θ = w ⇒ Ξ = W everywhere) also needs a
  proof, because o's continuation may re-enter Y. With both, Prop X and R17 would give the 𝒞^1O bound by the same block count
  (READING).

## 5. Box-24 end data (2026-10-24 04:22Z by date -u). New section; the frozen packet N5-1Oacyc-box24.md is not touched.
- Referee aid for P-N5-1OA (Lead 03:21Z suggestion). climbPure.py maximises pure transitions on o-acyclic 𝒞^1O and checks
  L1 / L2 / L3 at every improvement; 45 min each.

  | n | pure transitions (one block) | instance | sha1 | improvements with L1/L2/L3 failures |
  | --- | --- | --- | --- | --- |
  | 14 | 18 | box22/instances/pure_14.pg | 41d22650… | 0 |
  | 22 | 33 | box22/instances/pure_22.pg | f7ba3897… | 0 |

  Both instances are Oink zlk OK with strategies verified.
- o-cyclic cycclimb.py (longest pure run inside one joint λ-phase − (n − 1)), final, 1,500 s each:
  - n 8: −1; n 10: 0; n 12: −2; n 14: −5.
  - So no o-cyclic instance with n ≤ 14 beats R17's per-phase bound. fts_best16 (n 16) remains the smallest known.
- L-RED R58 §10 (via the Lead 03:38Z): the ring reading of fts_best16.
  - o's exits lie on one σ-path back to o, and σ̄(o) walks along it.
  - θ-change climbs stay below n (13 at n 16, 16 at n 24).
  - A super-linear θ-count would need nested rings; none is built.
- REFEREE-2 (via the Lead 03:51Z): Lemma 1 holds on all of 𝒞^1O, and the o-cyclic break is exactly Lemma 2. This agrees with §1-§2.
