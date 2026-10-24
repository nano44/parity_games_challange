# N5 box 2: θ-changes inside a (w, u*)-run (CYC-u*)
L-SI successor 1 (Opus 5.5, D15), box 2. Lead GO 2026-10-24 15:23Z, box to ~18:00Z. Started 15:22Z; first version 15:35Z (date -u).
Status: proof attempt on L-NEW's open item (CYC-u*) (docs/new/N5-xing-box27.md §8b). Labels: PROVED (by whom), CONJECTURE (with
data), OPEN, DATA, READING. Unrefereed. No polynomial bound is claimed. G-N5-TIME stays OPEN.
Object: N5 = docs/new/N5-ssi-global.md SPEC S1-S5. My runs use experiments/si/orlens/ortrace.py (same loop as experiments/new/n5.py;
gaps.py asserts equal counts). Notation: docs/si/N5-OR-lens.md §1-§2 (lev, ⊕, Lemma U), box 21 §3.5 (Lemma G), box 27 §1 and
§8b (u*, Lemma UD).

## 0. Result in one paragraph
- **Setting.** A (w, u*)-run is a maximal sequence of consecutive states inside one joint λ-phase, on 𝒞^1O, with:
  - τ, w = W(o) and u* fixed;
  - θ = Ξ(o) ◁ w;
  - (h) at every state.
  θ changes inside a run only strictly below u* (Lemma UD, L-NEW).
- **Classification of θ-changes (DATA, thclass.py).** Every θ-change on the instances is one of three kinds:
  - INR: the argmin exit e = σ̄(o) enters R, i.e. e "eliminates itself";
  - SELF: e stays the argmin and its value rises;
  - OVER: e's value rises above another exit's.
  Inside runs the third kind ("other") never occurs.
- **PROVED (L-SI), Lemma VIS.** If the argmin exit e enters R and its new loop ρ ∪ {o} contains a vertex above u* that is not in
  P(Ξ(e)), then e is never again σ̄(o) in the same run.
  - Corollary: at most d such "visible" self-eliminations per run, where d = o's out-degree.
  - In particular, if o itself is more relevant than u*, every INR event is visible.
- **FALSE**, both with Oink-verified instances:
  - "each exit self-eliminates at most once per run": inr2_n32, n 32, exits 29 and 17 each self-eliminate twice in one run, all invisible;
  - "each exit's value rises at most twice per run while it is the argmin": rise3_n32, n 32, three rises of exit 7.
- **The Lead's question, "is θ's sequence a monotone path of polynomial length in a finite structure?"**
  - The visible part of θ's motion, i.e. INR events whose loop shows above u*, is bounded by d per run (Lemma VIS).
  - The invisible part is a recursion one level below u*, with no fixed reference value (w is irrelevant there).
  - Neither the parametric family LP(t) = G^t nor a USO face walk turns θ-changes into breakpoints of a fixed structure: θ is Odd's
    value against N5's CURRENT σ, not against Even's G^t-optimum (§3).
  - (CYC-u*) stays OPEN.
- **DATA:** θ-changes per run, max 17 at n 32 with d = 11 (inr2_n32); climbs in §4.

## 1. Setting and facts used
ASSUMPTIONS (each one line):
- A1: 𝒞^1O — o is the only Odd vertex with out-degree > 1.
- A2: (h) at every state considered (box 21 §3.5).
- A3: all states considered lie in one joint λ-phase with τ fixed.
- A4: w = W(o) is fixed and θ ◁ w (throttled) on the run.
Definitions.
- u*: the most relevant vertex of P(θ) Δ P(w), where w beats θ. It is "none" if P(θ) = P(w); then "above u*" means "above the
  cycle node c".
- R_k: the vertices whose σ_k-path reaches o. On 𝒞^1O the honest play and the τ-play coincide before o.
- Exits: o's successors. Under (h), σ̄_k(o) ∉ R_k: otherwise the honest play from o would return to o.
Facts:
- (F-bell) θ_k = o ⊕ Ξ_k(σ̄_k(o)) (S1; o is not a cycle node by (h)).
- (F-mono) Ξ_k ⊴ Ξ_{k+1} (R15 (a)).
- (F-route) If e ∈ R_k with σ_k-path ρ to o (o excluded), then Ξ_k(e) = ρ ⊕ θ_k.
  - The honest play from e follows ρ to o and then o's honest play.
  - By (h), o's play does not return to o.
  - So it meets no vertex of ρ: from such a vertex it would follow ρ back to o.
  - Hence P(Ξ_k(e)) = (ρ ∪ {o})↑c ∪ P(θ_k), where ↑c means "more relevant than the cycle node c".
- (UD) L-NEW, box 27 §8b, PROVED by the lane: within a run, all θ_k have the same path set at and above u*.
  - If consecutive θ's differed at or above u*, Lemma UD would move u* (or give θ = w).
- (U) docs/si/N5-OR-lens.md Lemma U (ii): a ⊴ b ⊴ c implies lev(a, b) ≤ lev(a, c).

## 2. Lemma VIS (PROVED, L-SI successor 1, 15:35Z)
**Statement.** Let k, k+1 be states of one (w, u*)-run (A1-A4) with:
- e := σ̄_k(o), e ∉ R_k, and e ∈ R_{k+1};
- ρ := e's σ_{k+1}-path to o (o excluded), and L := ρ ∪ {o};
- D := {x ∈ L : x more relevant than u* (than c if u* = none)} \ P(Ξ_k(e)).
If D ≠ ∅, then σ̄_j(o) ≠ e for every later state j of the same run.

**Proof.** Suppose σ̄_j(o) = e for a state j > k of the run. Then j ≥ k+2, since e ∈ R_{k+1}.
1. By (F-bell), θ_k = o ⊕ Ξ_k(e) and θ_j = o ⊕ Ξ_j(e).
   - Neither Ξ_k(e) nor Ξ_j(e) contains o: e ∉ R_k by hypothesis, and e ∉ R_j by (h).
   - So P(Ξ_k(e)) = P(θ_k) \ {o} and P(Ξ_j(e)) = P(θ_j) \ {o}.
2. By (UD), P(θ_k) and P(θ_j) agree at and above u*. Hence P(Ξ_k(e)) and P(Ξ_j(e)) agree at and above u*, and
   lev(Ξ_k(e), Ξ_j(e)) ≤ 1 + rank(u*). If u* = none, the path sets are equal and the level is ≤ 0.
3. By (F-route) at k+1, P(Ξ_{k+1}(e)) ⊇ L↑c ⊇ D.
   - Every x ∈ D is more relevant than u* and lies outside P(Ξ_k(e)).
   - So top(P(Ξ_k(e)) Δ P(Ξ_{k+1}(e))) is at least as relevant as the top of D, which is above u*.
   - All three values have the phase's cycle node.
   - So lev(Ξ_k(e), Ξ_{k+1}(e)) > 1 + rank(u*) (> 0 if u* = none).
4. (F-mono) gives Ξ_k(e) ⊴ Ξ_{k+1}(e) ⊴ Ξ_j(e).
   (U) gives lev(Ξ_k(e), Ξ_{k+1}(e)) ≤ lev(Ξ_k(e), Ξ_j(e)), which contradicts 2 and 3. □

**Corollary VIS.**
- (a) In one run, at most d INR events are visible (D ≠ ∅): each retires its exit from σ̄(o) for the rest of the run.
- (b) If o is more relevant than u* (and than c), every INR event is visible, since o ∈ D always. In such a run there are ≤ d INR
  events.
- (c) The same argument gives a general fact. If e = σ̄(o) at two states k < j of a run, then e's honest value changes only below
  u* between them: every Ξ_t(e), k ≤ t ≤ j, agrees with Ξ_k(e) at and above u*. The proof is steps 1, 2 and 4 with any t in
  place of k+1.

**Lemma VIS′ (PROVED, L-SI, 15:40Z; the general form, without u*).** Same setting.
- Let e = σ̄_k(o) enter R at k → k+1 with loop L = ρ ∪ {o}.
- Let t := the most relevant vertex of (L↑c) \ P(Ξ_k(e)). If L↑c ⊆ P(Ξ_k(e)), then t := none.
- If σ̄_j(o) = e at a later state j of the same joint λ-phase, with τ fixed and (h) at k, k+1 and j, then
  v := top(P(θ_k) Δ P(θ_j)) exists and is at least as relevant as t.
- In words: before e can be Odd's best reply again, θ itself must have changed at the level of the loop's new top vertex, or
  higher.
Proof.
- As in VIS, steps 1 and 4: lev(Ξ_k(e), Ξ_j(e)) = lev(θ_k, θ_j) on path sets (o is in both θ's or in neither, and in neither Ξ).
  So it is 1 + rank(v), or ≤ 0 if P(θ_k) = P(θ_j).
- lev(Ξ_k(e), Ξ_{k+1}(e)) ≥ 1 + rank(t) when t ≠ none.
- U (ii) gives 1 + rank(t) ≤ lev(Ξ_k(e), Ξ_j(e)). □
- VIS is the special case: inside a (w, u*)-run, v is less relevant than u* (Lemma UD).
- VIS′ needs neither w fixed nor a throttled state.
Use: every repeated self-elimination of an exit is charged to a θ-change at level ≥ t. This does not count θ-changes by itself:
a monotone lexicographic sequence can change at a fixed level many times. OPEN whether the charges can be made injective.

DATA check (oneinr.py; 0 violations of the conclusion, as the proof requires):

| instance | INR events in runs | visible | violations |
| --- | --- | --- | --- |
| sc32 (new/box25) | 17 | 9 | 0 |
| s_tp32_final | 15 | 6 | 0 |
| cycelim_cex_n32 | 10 | 5 | 0 |
| theta_tp32 | 3 | 3 | 0 |
| fts_best16 | 2 | 2 | 0 |
| thclimb_n16_s12 | 6 | 6 | 0 |
| inr2_n32 | 9 | 0 | 0 |

Re-run at 15:40Z on the corrected run definition, which tests (h) at every state (thclass.hstate, added 15:31Z): the same
numbers. rise3_n32: 12 INR events, 5 visible, 0 violations.

## 3. What fails, and the reading on the Lead's two structures
**FALSE: "each exit self-eliminates (INR) at most once per (w, u*)-run".**
- Instance: experiments/si/orlens/instances/inr2_n32.pg (n 32, sha1 9689990d…, canonical start; one Odd choice vertex o = 0,
  d = 11).
- n5.py: 32 iterations, 1 fallback. Oink zlk OK, strategies verified.
- In the run of states 5-23 (u* = rank 31) σ̄(o) walks the exits 5 → 28 → 25 → 2 → 27 → 2 → 28 → 5 by OVER events (states 5-11).
- Then 8 INR events follow (states 12-19), each exit entering R one per iteration: 5, 28, 25, 2, 27, 17, 26, 29.
- Exit 29 is σ̄(o) again at state 22 and enters R a second time. Exit 17 does the same at state 23.
- All INR events of the run are invisible (D = ∅), consistent with Lemma VIS.
- Found by climb.py --run, seeded from s_tp32_final.

**FALSE: "each exit's value rises at most twice per run while it is the argmin".**
- Instance: instances/rise3_n32.pg (n 32, sha1 4f45bbec…, canonical start, d = 14).
- n5.py: 30 iterations, 1 fallback. Oink zlk OK, strategies verified.
- Exit 7 rises 3 times in the run of states 5-18.

**Reading on "a monotone path in a finite structure".**
- LP(t) = G^t (o a terminal of value t), Post-Ye's parametrised family (N5-OR-lens §3.3b).
  - As t rises, each vertex's G^t-optimal choice flips from o-free to through-o at most once (box 25 §5 (6)), so G^t has ≤ n
    breakpoints.
  - θ would walk those breakpoints if Even played the G^θ-optimum at every state, i.e. the honest optimum.
  - N5 plays the G^w-optimum over the gate, so Even's σ is not G^θ-optimal (trust mode), and θ = o ⊕ min over exits of the CURRENT
    σ-paths. θ-changes are not breakpoints of G^t.
  - Lemma VIS is exactly the visible part, where the loop's top vertex lies above u* and the order alone forbids a return.
- USO face walk. The coarse value below u* is a function of σ|below u*, but N5's steps are not the USO's out-edges of a fixed face:
  the gate is honest and the selection is G^w. I have no face structure in which θ moves monotonically along a path of polynomial
  length. READING.
- Recursion. Below u* there is no fixed reference: w is decided at u*. So the "next u*" of box 27 §8c must be defined between
  consecutive θ's themselves.
  - Lemma VIS (c) shows that between two argmin times of the same exit, the exit's value moves only below u*.
  - Iterating gives one level per "u*-like" vertex, n levels, and an n^depth bound, the same obstacle box 27 §8c names.

## 4. Climbs (DATA; climb.py --run, canonical start unless seeded; one Odd choice vertex)
Fitness = θ-changes inside one (w, u*)-run under (h), then max INR per exit per run, then max rise per exit per run, then d.
Running 15:27Z-16:12Z; results below when they end.

## 5. Files (experiments/si/orlens/)
- thclass.py: θ-change classes; hstate(), the (h) test; ustar().
- urun.py: per-run counts.
- oneinr.py: Lemma VIS check.
- perexit.py: per-exit INR / rise counts per run.
- climb.py --run [--runmax]: climbs.
- instances/inr2_n32.pg, instances/rise3_n32.pg.
