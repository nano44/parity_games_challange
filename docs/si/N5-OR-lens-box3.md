# N5 box 3: from VIS′ to a count of θ-changes — additive or multiplicative?
L-SI successor 1 (Opus 5.5, D15), box 3. Lead GO 2026-10-24 16:30Z, box to ~19:00Z. Started 16:32Z; first version 16:45Z (date -u).
Status: proof attempt on (CYC-u*) / (CYC') of docs/new/N5-xing-box27.md §8. Labels: PROVED (by whom), CONJECTURE (with data),
OPEN, DATA, READING. Unrefereed. No polynomial bound is claimed. G-N5-TIME stays OPEN.
Notation and lemmas: docs/si/N5-OR-lens.md (lev, ⊕, Lemma U), docs/si/N5-OR-lens-box2.md (VIS, VIS′, INR / SELF / OVER), box 21
§3.5 (Lemma G), box 27 §8b (u*, UD).

## 0. Answer in one paragraph
- **The charges are MULTIPLICATIVE as a proof scheme.** The Lead asked whether charging θ-changes level by level gives an additive
  bound. It does not, and the obstruction is exact:
  - every SELF/OVER θ-change at path-set level r is paid by a rise, at level ≥ r, of the argmin exit's o-free value (Lemma CH,
    PROVED);
  - those o-free values are one-player quantities in G[F] (Lemma G (a)), and R17's layering bounds them, but only inside a PIECE,
    i.e. while R is constant (PIECE, refereed in P-N5-RE);
  - every INR θ-change is itself a crossing (the exit and its upstream enter R), so it ends the piece and resets the one-player
    resource that would have paid for the next SELF/OVER;
  - so the payer is reset by the event being paid. With VIS′ (a repeated INR is charged to a higher θ-change, but up to d exits may
    charge the same one), this gives T(≥ r) ≤ poly · (1 + T(> r)), whose depth is the number of levels used.
- **Data say the factor per level is small.**
  - No path-set level carries more than 5 θ-changes on the pinned and climbed instances. The counter bound allows
    #(level r) ≤ 1 + #(levels > r).
  - Climbs against a constant per level: §4.
- **PROVED reductions (L-SI):**
  - Lemma LEN: between consecutive path-set changes of θ there are at most n length-only θ-changes. On sc32, 25 of 43 θ-changes are
    length-only.
  - Lemma CH: the SELF/OVER charge above.
  - Hence #θ-changes per phase ≤ (n + 1) · (1 + Σ_r m_r), where m_r = θ-changes at path-set level r.
  - So (CYC) holds if m_r ≤ poly(n) for every level r: CONJECTURE (LEVEL-poly).

## 1. Setting
ASSUMPTIONS (each one line):
- A1: 𝒞^1O (o is the only Odd vertex with out-degree > 1).
- A2: one joint λ-phase with τ fixed.
- A3: (h) at the states used (needed only in Lemma CH and in the classification of θ-changes).
Notation:
- θ_k = Ξ_k(o). Its cycle node c is fixed in the phase.
- The LEVEL of a θ-change k → k+1 is the top rank of P(θ_k) Δ P(θ_{k+1}), or "length" if the path sets agree.
- m_r := the number of θ-changes at level r in the phase.

## 2. PROVED statements (L-SI successor 1)
**Lemma LEN.** Between two consecutive θ-changes whose level is a path-set level, there are at most n − 1 θ-changes at level
"length".
Proof:
- In between, θ's cycle node and path set are fixed.
- θ is ⊴-monotone (R15 (a)), so its length moves strictly in one direction: up if c is odd, down if c is even.
- The length is the number of steps from o to c on a simple path, so it lies in [1, n − 1]. □
Corollary: #θ-changes ≤ n · (1 + Σ_r m_r).

**Counter bound (PROVED, elementary; holds for any ⊴-monotone sequence).** m_r ≤ 1 + Σ_{r' > r} m_{r'}.
Proof:
- A change at level r sets the membership of the rank-r vertex u_r to its good status (in P if u_r is even, out of P if it is odd),
  and agrees above r.
- A second change at level r needs u_r back in its bad status first.
- Only a change at a higher level can alter u_r while agreeing above r. □
This alone gives 2^(#levels): the binary counter.

**Lemma CH (charge for SELF/OVER).** Let e = σ̄_k(o) with e ∉ R_k and e ∉ R_{k+1} (a SELF or OVER event, (h) at k and k+1), and let
θ change at k → k+1. Then the level of the θ-change is at most lev(Ξ_k(e), Ξ_{k+1}(e)). So the argmin exit's own honest value rises
at a level ≥ the θ-change's level.
Proof:
- θ_k = o ⊕ Ξ_k(e) (F-bell).
- θ_{k+1} = Ξ_{k+1}(o) ⊴ o ⊕ Ξ_{k+1}(e): e ∉ R_{k+1} is one of Odd's options at o, and Odd's honest reply is pointwise optimal; the
  deviation's play is o, then e's play, which avoids o.
- θ_k ◁ θ_{k+1} (a θ-change, R15 (a)).
- So θ_k ◁ θ_{k+1} ⊴ o ⊕ Ξ_{k+1}(e), and U (ii) gives lev(θ_k, θ_{k+1}) ≤ lev(o ⊕ Ξ_k(e), o ⊕ Ξ_{k+1}(e)) = lev(Ξ_k(e), Ξ_{k+1}(e)).
  The last step is F-pre: o is added to both values or to neither. □
Since e ∉ R at both states, Ξ(e) = W(e) is e's o-free value (Lemma G (a)). So every SELF/OVER θ-change at level r is paid by a rise
of an o-free value at level ≥ r.

**VIS′ (box 2) for INR.** A repeated INR of the same exit is charged to a θ-change at a level ≥ the loop's top new vertex. Up to d
exits can be charged to the same θ-change.

DATA checks (chcheck.py): Lemma CH 150 checks on 11 instances, 0 violations. Longest run of consecutive length-only θ-changes: 7
(sc32), within Lemma LEN's n − 1.

## 3. Additive or multiplicative: the obstruction (READING, every step from §2 or a cited PROVED lemma)
For an additive bound, each level's payers would have to be "fresh": a resource spent at level r must not be restored by a
higher-level event. The candidate payers are:
1. **o-free progress of exits (for SELF/OVER, Lemma CH).**
   - Inside a piece (R constant, no fallback, τ, θ, w constant), the o-free game G[F] runs R17. So F-values change at most |F| − 1
     times per piece (PIECE, P-N5-RE §5, signed by both referees).
   - But a piece ENDS at every θ-change. In particular it ends at every INR, which is both a θ-change and a crossing (the exit and
     all vertices routing through it enter R).
   - The R17 layering, "after j steps every F-vertex dominates every o-free path of ≤ j edges", fails across crossings exactly at
     trust-routed vertices. A path through a vertex now in R is still a path of G, but the vertex's honest value is π ⊕ θ, below its
     o-free continuation (box 21 §3.6 (ii); box 22 I3 FALSE, i3hn).
   - So the payer for the next SELF/OVER is restored at each INR.
   - Recursion: SELF + OVER ≤ (n − 2) · (#pieces) ≤ (n − 2) · (1 + #θ-changes + #crossings + #fallbacks). θ-changes appear on
     both sides: MULTIPLICATIVE.
2. **The exits themselves (for INR, VIS′).**
   - A repeated INR of e needs a higher θ-change, but each higher θ-change can be charged by every exit once.
   - This gives m(INR at ≤ r) ≤ d · (1 + T(> r)): MULTIPLICATIVE with factor d per level.
3. **What would make it additive.** Either of:
   - (i) a monotone potential that both rises at every INR and is NOT restored by the o-free progress that pays SELF/OVER;
   - (ii) a proof that higher-level θ-changes restore only levels that were not yet paid, i.e. m_r ≤ c without the "+ higher"
     term.
   (ii) is the data's behaviour (§4) and the content of CONJECTURE (LEVEL-poly). I have no argument for either.

DATA, the shape of the multiplicative structure (levels.py; sequence of (level, class) for the longest phase):
- run_x_inr2 (n 32): the high-level SELF events 27S and 24S are each followed by a σ̄-lap that re-fixes the SAME block of lower
  levels {22, 12, 14, 10, 20, 16} one at a time. Level 12 is used 4 times.
  - This is a counter with two nested digits. Each "carry" re-fixes ~d lower levels, the laps of box 25 §4.
- sc32 (n 32): 43 θ-changes, of which 25 are length-only (Lemma LEN's regime): the INR chains move θ by length, since the chained
  exits share their path set and differ only in distance.

## 4. Data and climbs
Per-level counts on the instances (ldepth.py):

| instance | n | θ-changes | path-set changes | distinct levels | max m_r |
| --- | --- | --- | --- | --- | --- |
| run_x_inr2 | 32 | 43 | 30 | 14 | 4 |
| sc32 | 32 | 43 | 18 | 10 | 5 |
| s_tp32_final | 32 | 35 | 13 | 7 | 4 |
| run_m_inr2 | 32 | 29 | 14 | 9 | 3 |
| cycelim_cex_n32 | 32 | 24 | 11 | 8 | 2 |
| inr2_n32 | 32 | 19 | 7 | 6 | 2 |
| run_m_n24 | 24 | 19 | 5 | 4 | 2 |
| theta_tp32 | 32 | 16 | 14 | 8 | 4 |
| theta_thc24 | 24 | 16 | 6 | 5 | 2 |
| theta_thf16 | 16 | 13 | 13 | 7 | 4 |
| fts_best16 | 16 | 8 | 8 | 5 | 2 |

Climbs (climb.py --level: fitness = (max m_r, θ-changes); 3,000 s from 16:34Z): seeded from run_x_inr2 and sc32, and random n 20
and 28. Interim at 16:35Z: max m_r 7 (sc32 seed) and 6 (run_x_inr2 seed). Final numbers below when they end.

## 5. Files (experiments/si/orlens/)
- levels.py: (level, class) sequence and per-level counts.
- ldepth.py: per-level maxima and counter-nesting depth.
- climb.py --level.
- chcheck.py: Lemma CH and LEN check.
