# N5 on o-cyclic 𝒞^1O, box 27: crossings in throttled stretches (XING), via a coarse valuation
L-NEW successor 9 (Opus 5.5, D15). Lead GO 2026-10-24 14:22Z (date -u), box to ~17:20Z, stop rule ~16:45Z.
Labels (L40): PROVED (by whom), READING (proof sketch), CONJECTURE (with data), OPEN. ASSUMPTION used throughout: (h) at the states
involved. Nothing here covers states where (h) fails. No running-time claim for N5. G-N5-TIME stays OPEN.
The packet P-N5-RE (docs/new/P-N5-RE-box26.md, pinned at trunk 52c7261) is NOT edited. §0 corrects box 26's notes and adds the
example the Lead asked for.
Notation: box 26 (docs/new/N5-reentry-box26.md) and the packet, §0-§1:
- R, F, routes ρ, o-free values h, Lemma G (a)-(c), Lemma W (box 21 §2.5), R15 (a) (Ξ non-decreasing);
- a (θ, w)-STRETCH is a run inside one joint λ-phase with τ, θ, w constant and (h) at every state;
- THROTTLED means θ ◁ w.
Code: experiments/new/box25/ (coarsecheck.py, fbedges.py, crossings.py, xingclimb.py, xtrace.py).

## 0. Corrections and additions to box 26 (dated 2026-10-24 14:45Z)
- CORRECTION to box 26 §7.3 data and to the 14:12Z (XING) conjecture. The crossing climbs xc16, xc24, xcf20 and tr20_s4 have θ = w at
  every state of their long stretches, so they are UNTHROTTLED. There the band is empty, and the stretch is already bounded:
  - Lemma G with θ = w gives Ξ = W, and the gate is exactly G_τ's improving set;
  - fallbacks are W-flat (box 25 §3, PROVED);
  - box 21 Lemma PT with R17 Theorem PH then gives ≤ n − 1 value-changing transitions per stretch (PROVED by combining those
    results).
  - So those numbers say nothing about (XING). Re-measured on throttled stretches only (crossings.py, now the default):

    | instance | n | crossing transitions per throttled stretch | max crossings of one vertex |
    | --- | --- | --- | --- |
    | theta_tp32 | 32 | 10 | 1 |
    | returns_rt48 | 48 | 9 | 2 |
    | returns_ph64 | 64 | 9 | 2 |
    | fts_best16 | 16 | 3 | 2 |
    | thetare_n | 11 | 1 | 1 |
    | xc16 / xc24 / xcf20 / tr20_s4 | | 0 | 0 |

  - The conjecture of box 26 §7.3 is restated: crossing transitions per THROTTLED (θ, w)-stretch are poly(n). §2-§3 below reduce it
    further.
- EXAMPLE for the packet's Corollary RE: L-COMP's thetaA_canon_n8 (experiments/n5-exhaustive/instances/thetaA_canon_n8.pg, sha1
  10c55131…; Lead re-run Oink OK, strategies verified). It is the smallest canonical-start instance of a non-ROUTE re-entry:
  - class WRISE after an arena leave, with θ = w rising via an Even move at τ(o) = 7;
  - consistent with Lemma RE: the re-entry's interval contains a θ-change.
- L-COMP's thetaA_n6 (n 6, random start) is the same kind (WRISE, θ = w from state 1, unthrottled).
- On T29 Lemma B (Johnson reweighting). A reweighting preserves every comparison N5 makes, so it preserves the band. The band
  comes from the gate and the selection valuing o at different terminals (θ against w), not from a lack of increasingness. What
  removes it is a COARSENING (§1), not a reweighting.

## 1. The coarse valuation: one algebra on the band
Fix a throttled (θ, w)-stretch.
- By (h), θ and w have the same cycle node c.
- Let u* := the most relevant vertex of P(θ) Δ P(w), where w beats θ, if P(θ) ≠ P(w). Otherwise u* := none, and θ, w differ only
  in length.
- For a value v = (c', P, ℓ), put COARSE(v) := (c', P ∩ {vertices more relevant than u*}). It ignores the length, and keeps all of
  P when u* = none. Order: cycle node first, then path set, as in VJ00.
Lemma C (PROVED, L-NEW). At every state of the stretch, COARSE(Ξ(v)) = COARSE(W(v)) for every v, and COARSE(Ξ(v)) is non-decreasing
along the stretch, fallbacks included. So COARSE(W) is non-decreasing too, even where W drops (box 25 §3).
Proof.
- If v ∈ F, then Ξ(v) = W(v) (Lemma G (a)).
- If v ∈ R, then Ξ(v) = π_v ⊕ θ and W(v) = π_v ⊕ w (Lemma G (b)). π_v is disjoint from both continuations, and
  P(θ), P(w) agree above u*. So the coarse parts agree.
- Monotonicity is R15 (a), since COARSE is order-preserving (⊵ implies coarse ⊵). □
Lemma FBL (PROVED, L-NEW). Let a fallback happen at a throttled (h)-state. Then every edge it switches is either a LEAVE (x ∈ R,
z ∈ F, type d2) or a flat switch at a cycle node of F. In particular, F's plays are unchanged except for flat switches, and every
non-flat fallback contains a leave.
Proof.
- The fallback fires only when the S4a arena optimum is σ itself. By (F1) σ is then pointwise optimal in the arena, so no gate edge is
  strictly W-improving. Flat switches at a vertex's own cycle node are the only W-ties allowed by R15 (b) / the P-N5-1OA flat case.
- By Lemma G (d), a gate edge that is not W-improving is of type (d2), x ∈ R and z ∉ R.
  - Gate edges R → R and F → F are honest-improving iff W-improving (Lemma G (c), (a)).
  - Gate edges F → R are honest-improving, hence W-improving, since w ⊵ θ.
- S4c switches every vertex that has a gate edge. □
DATA (fbedges.py): every switched edge at the 36 throttled (h)-fallbacks of fts_best16, theta_tp32, returns_rt48, returns_ph64,
i1h_fts_best16, fbh_drop9 and fbh_thr is a leave (D2 77, other 0). No such fallback in 15,000 random runs.
Lemma CR (coarse R17; READING, L-NEW). It transcribes R17 Lemma P / Theorem PH into the coarse order. The fallback-step part of
Case B is new and is proved below; the transcription of R17's Case B sub-cases (B1/B2, cycle creation) into the coarse order is
argued, not written out. In a throttled (θ, w)-stretch (fallbacks allowed), coarse values change only at the first n − 1 transitions of the
stretch.
Proof.
- Work in the one-player game G_τ with the coarse order. By Lemma C, COARSE(Ξ) = COARSE(W) =: Ω^c.
- R17 Lemma P (docs/new/N5-phase-bound-box10.md §2) uses four things: (V1), (V2), (F1) for the step taken, and (F2) monotonicity.
  - (V1) and (V2) hold for the coarse order: the prefix x ⊕ adds x to the coarse set iff x is more relevant than u* (and than the
    cycle node), on both sides at once.
  - (F2): Lemma C.
- Case B. The edge (x, z) is coarse-improving. Then it is fine Ξ-improving, so it is in the gate.
  - At an ARENA step, (F1) for the arena (fine W) gives W_{k+1}(x) ⊵ val_{σ̂}(x). Hence Ω^c_{k+1}(x) ⪰ coarse(val_{σ̂}(x)).
  - At a FALLBACK step (throttled, (h)), by Lemma FBL x is in R, z ∈ F, and x switches to its honest-best gate edge z* ∈ F. The F side
    is unchanged, so z*'s path avoids x, and
        Ξ_{k+1}(x) = x ⊕ Ξ_k(z*) ⊵ x ⊕ Ξ_k(z)    ((V1), honest-best, (V2)).
    Take coarse.
- Case A is R17's case A with coarse values. Case A2 (x its own cycle node) is unchanged.
- Hence after j transitions, Ω^c_j(x) ⪰ coarse(value(r)) for every simple path r of ≤ j edges from x to a cycle node of the phase
  (paths through o continue along τ(o) in G_τ).
- After n − 1 transitions every Ω^c(x) is maximal among such coarse path values. Later values are values of actual plays, i.e. of
  such paths, so they cannot increase, and by monotonicity they cannot decrease. □
DATA (coarsecheck.py): C1 (coarse Ξ = coarse W) and C2 ("last coarse change ≤ n − 1") hold with 0 failures, fallbacks included:
- on fts_best16, theta_tp32, returns_rt48, returns_ph64, theta_thf16, thetare_n, i1h_fts_best16;
- on 8,000 random runs.
- Max index of the last coarse change: 10 (theta_tp32, n 32). On returns_rt48 / ph64, throttled stretches of 40 / 56 transitions have
  no coarse change at all.

## 2. Re-entries after arena leaves are paid by coarse progress
Theorem XA (L-NEW). The strict coarse increase per re-entry is PROVED (Lemma W, R15 (a), Lemma C). The count ≤ n(n − 1) is READING,
because it uses Lemma CR.
- Setting: a throttled (θ, w)-stretch with u* ≠ none. Let x leave R at L by an arena step, its own or downstream of one, i.e. no
  fallback at L. Let x next re-enter at E inside the stretch.
- Claim: COARSE(Ξ_{E+1}(x)) ▷ COARSE(Ξ_L(x)).
- So inside one stretch, such re-entries number at most Σ_x #(coarse increases of x) ≤ n(n − 1), and all of them lie in the first
  n − 1 transitions.
Proof.
- At an arena step, Lemma W gives W_{L+1}(x) ⊵ W_L(x) = π^L ⊕ w. Since x ∈ F_{L+1}, W_{L+1}(x) = Ξ_{L+1}(x).
- By R15 (a), Ξ_{E+1}(x) ⊵ Ξ_{L+1}(x). By Lemma G (b), Ξ_{E+1}(x) = π^{E+1} ⊕ θ. So π^{E+1} ⊕ θ ⊵ π^L ⊕ w.
- Suppose the coarse parts were equal, i.e. the route vertices above u* coincide. The two sides then first differ at u*, which lies on
  a continuation and not on either route. There w is better, so π^{E+1} ⊕ θ ◁ π^L ⊕ w, a contradiction.
- Hence the coarse parts differ, and the fine order forces the coarse one strictly up. Count: Lemma CR. Each of at most n − 1
  transitions raises at most n vertices. □
When u* = none (P(θ) = P(w), only lengths differ): the same argument gives, at equal coarse value, a strictly shorter or strictly
longer route (by the parity of c). That allows at most n re-entries per coarse value, so ≤ n²(n − 1) per stretch. (READING: the same
proof with the length added.)

## 3. The per-stretch reduction
Corollary (READING, since it uses Lemma CR; L-NEW). In a throttled (θ, w)-stretch S with u* ≠ none:
- entries(x) ≤ 1 + re-entries(x), and leaves(x) ≤ 1 + entries(x);
- the non-flat fallbacks of S are at most the leaves at fallbacks (Lemma FBL). Flat fallbacks change no value, and R15 (d) bounds them
  by 4n(n − 1) between value changes;
- re-entries = (after arena leaves: ≤ n(n − 1), Theorem XA) + (after fallback leaves: (FB-RE)).
- Hence:
      crossing transitions(S) + non-flat fallbacks(S) ≤ 4n + 4n(n − 1) + 4·FB-RE(S),
  and by PIECE (packet §5):
      value-changing transitions(S) ≤ (n − 1)·(5n + 4n(n − 1) + 4·FB-RE(S) + 1).
- So inside a throttled (θ, w)-stretch everything is polynomial except (FB-RE).
OPEN (FB-RE): re-entries, inside one throttled (θ, w)-stretch, of vertices whose last leave was forced by a fallback.
- By Lemma RE each such re-entry strictly improves x's route (θ constant). It may do so below u*, with no coarse gain.
- DATA (coarsecheck.py, reentry.py): 0 inside a stretch on every pinned instance.
  - returns_rt48: one throttled stretch of 40 transitions with 42 fallback leaves, 0 re-entries inside it.
  - All THETA re-entries of box 26 come after fallback leaves, but in a LATER (θ, w)-stretch (θ changed), so they are not FB-RE.

## 4. Where this leaves N5 on o-cyclic 𝒞^1O (READING; assumes (h))
N5 on o-cyclic 𝒞^1O is polynomial if the following are poly(n) per joint λ-phase:
- (a) (θ, w)-stretches, i.e. θ-changes plus w-changes. (CYC) and Lemma Wo: w is monotone, but its changes are not otherwise
  bounded.
- (b') (FB-RE) per throttled stretch.
- (d) Transitions at states where (h) fails.
Unthrottled stretches are bounded by Lemma PT + R17 (§0). Throttled stretches are bounded by §3 given (b').
Fallbacks are no longer a separate item inside throttled (h)-stretches: §3 bounds the non-flat ones and R15 (d) the flat ones.
