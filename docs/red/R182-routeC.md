# R182 Route (C) (the pivot h on X's own play): Lemma C-STATIC (PROVED, lane): inside one λ_W-phase at h, W-strict same-portal moves of h climb a STATIC order of the private prefixes, so there are at most deg(h) − 1 of them, whether or not h is on X's play; the escape (C) therefore does not give a W-strict same-portal climb in one λ_W-phase; the only uncovered case is a prefix vertex on X's W-play with θ on that prefix (NR-CYC); DATA: no route-(C) climb longer than 1 move (L-RED successor 42)
Started 2026-11-01 16:36Z (Lead GO, last box before park, date -u). Brief: «Build the escape that PORTAL and PHASE-PORTAL leave open, where
the pivot h moves while h is on X's own play (NR fails at h) … Target: a W-strict same-portal climb inside ONE λ_W-phase at bounded
ODIFF, with PHNF super-linear per λ_W-phase. Otherwise give the exact obstruction and the smallest instance. Note NR-CYC (L-NEW box 128,
lane) …». Labels: PROVED (lane), DATA, READING. Not a TARGET.md claim. G-N5-TIME stays OPEN. No kill.

## 0. Answer
- Not buildable in the form asked. Route (C) adds nothing inside one λ_W-phase.
- Lemma C-STATIC (PROVED, lane; §1): inside one λ_W-phase at h, h's W-strict same-portal moves strictly increase in a fixed order of
  its class-X options. That order depends only on θ (h's W-cycle node) and the options' private prefixes. So there are at most
  #(class-X options) − 1 ≤ deg(h) − 1 such moves.
  - It needs neither NR at h nor ZC.
  - It needs NOPRE: no prefix vertex of the two options involved lies on X's W-play at the move. With NR-CYC, NOPRE is exactly «X is
    not on a W-cycle through a prefix vertex».
- So a W-strict same-portal climb of super-constant length inside one λ_W-phase needs:
  - (i) a high-degree pivot (the climb is then still ≤ deg(h) − 1, linear), or
  - (ii) the NR-CYC case with θ on the private prefix of an option that sits on X's cycle: §2, the only open escape.
- DATA:
  - The route-(C) climb (cscore / climb182; after the fix, 4 climbs from random games, n 16-32, 30k
    mutations each; before it, 4 more whose «2 moves» was the bug below) never produced two consecutive W-strict
    same-portal moves with ZC and h on X's play.
    - An apparent 2-move instance (c2) had an S4c fallback at its second move: that was a scorer bug (fallback flag read off by
      one), fixed before any reporting.
  - C-STATIC checker (cstatic.py): 0 violations on 34 climb outputs from R173 / R174 / R182 and the R173 pins, and on 4 climbs
    that maximise the run length (best: 2 moves, pin cstat_n24).

## 1. Lemma C-STATIC (PROVED, lane)
Setting:
- A TWO-FIX window (τ, σ̄ constant).
- An Even h, and its options of class X = cls(h, i) (R173 §1: the first branching vertex of G_F after the choice-free prefix(h, i)).
- Transitions j_1 < … < j_k, each a move of h with no S4c fallback at j_r: o_r = σ_(j_r − 1)(h) → i_r = σ_(j_r)(h), both of class X.
  Consecutive, as in R174's ZRUNs.
- Each move W-strict: key W_(j_r)(i_r) > key W_(j_r)(o_r).
- Same W-cycle node θ of h at every j_r (one λ_W-phase at h).
- NOPRE: no vertex of prefix(o_r) ∪ prefix(i_r) lies on X's W-play at j_r.

Statement. i_1, …, i_k are strictly increasing in ≺_θ, the order on class-X options given by comparing prefix(i) ⊕ V for any value
V with cycle node θ. So the i_r are distinct and k ≤ #(class-X options) − 1.

Proof.
1. Fix r and j = j_r. Let V_j be X's W-value at state j (σ_j, τ).
   - For an option i of class X, the W-play from i is prefix(i) followed by X's W-play.
   - prefix(i) is a fixed walk (out-degree 1 in G_F, the same edge in both worlds).
   - By NOPRE no prefix vertex of o_r, i_r recurs on X's play, so the play from i is prefix(i) then exactly X's play.
   - This holds when X's play passes h (route C): the play from o_r then runs prefix(o_r) → X → … → h → prefix(i_r) → X …, and that is
     still X's play at state j.
   - So W_j(i) = prefix(i) ⊕ V_j for i ∈ {o_r, i_r}.
2. V_j's cycle node is θ.
   - h's W-play is prefix(i_r) ⊕ X's play, so h's W-cycle node is V_j's cycle node, unless the cycle runs through prefix(i_r).
   - In that case θ ∈ prefix(i_r) lies on X's play, which NOPRE excludes.
3. With a common V_j of cycle node θ, key(prefix(i) ⊕ V_j) − key(prefix(i′) ⊕ V_j) is decided by:
   - the prefix vertices above θ (path-set weight, with V_j's part common);
   - then the prefix lengths, with the parity of θ.
   That is ≺_θ, independent of j. So the W-strict move at j_r gives o_r ≺_θ i_r.
4. o_(r+1) = i_r (consecutive moves of h). Hence i_1 ≺_θ i_2 ≺_θ … ≺_θ i_k. □
- Remarks.
  - No ZC and no NR at h are used. PORTAL's tie conclusion is stronger, but it needs NR. C-STATIC trades it for the weaker «static
    order» and covers route (C).
  - Across λ_W-phases ≺_θ changes with θ. Hence PHNF per λ_W-phase is bounded per portal by deg − 1, and the per-level fresh-portal
    picture of R173 §2 stands.

## 2. What remains open (exact obstruction)
- NOPRE fails, i.e. by NR-CYC (L-NEW box 128) X is on a W-cycle through a prefix vertex u of some option i.
- If θ (h's W-cycle node) is on X's part of the cycle, step 1 still holds: the play from i reaches u and then follows the cycle,
  which is prefix(i) ⊕ (X → θ). The order is static again.
- Uncovered sub-case: θ ∈ prefix(i)'s tail (between u and X).
  - Then W(i) is static (its path to θ is inside prefix(i)).
  - The other options' values prefix(i′) ⊕ V_j run through X → … → u → … → θ, and these move with X's path to u.
  - So the order between i and i′ can flip once per change of X's W-path to u. A long climb needs those changes inside one λ_W-phase
    with θ fixed: W-path changes on X's cycle that keep θ. I did not build this; it is the exact remaining escape.
- Smallest instance: none produced. The longest C-STATIC run found is 2 moves (cstat_n24, n 24, ODIFF 0, sha1 340aea17c564…;
  startck OK, Oink --zlk + verify «OINK OK», --tl + verify exit 0, xeng identical). It is not a route-(C) climb (ZC or h-on-play fails at
  one of its two moves).

## 3. Files (experiments/red/r182/)
- cscore.py (route-(C) runs: ZC + h on X's play), climb182.py, cstatic.py (Lemma C-STATIC checker), climbcs.py, climbs_cstatic.txt,
  out/, instances/ (cstat_n24 + start, pins.sha1). check.sh block «R182».
