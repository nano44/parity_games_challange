# Referee report R-P4: packet 4 (GAP-A-M §22: S0, PREFIX-MONO, POS-FALL, ROOT-BOUND, the §22e reduction, bit cost)

Referee: REFEREE, running on Opus 5.5 under owner ruling D12 (Lead reading L33). Packet: the Lead's message of 12:01Z.
Pin: trunk 44d1428, docs/alg/GAP-A-M.md §22 (lines 1853-2000). Code: tools/oink/src/src/solvers/dtl.cpp @ 8fbf0a7
("N" = that line). Written 12:02Z-12:05Z (date -u). docs/referee-2/R2-P4.md was not read. The code facts C1-C6 of
docs/referee/R-STEP5.md §0 are used, and so are the FDL (R-PROVED2 (h), reduced log) and 1.2b (attractors monotone in T
at a fixed input).

## Verdict
| item | verdict (Opus 5.5, D12) | lines checked |
|---|---|---|
| (a) (S0) | SIGN (reading R-a1) | 65-101, 110-185, 198-202, 690-706 |
| (b) PREFIX-MONO, its use of O1, corollaries C1-C4, RMONO, NO-LATER | SIGN WITH GAPS: R-b1 (closed: which closure Cl is meant) | 690-706, 712-760, 722-731 |
| (c) (POS-FALL) on clean transitions | SIGN | 690-706, 722-731 |
| (d) Theorem ROOT-BOUND and the per-phase bound | SIGN WITH GAPS: G-d1 (closed: Ψ's components when no threshold loop runs) | 712-716, 765-771 |
| (e) §22e reduction GAP-A ⇐ (CTX) ∧ (DIRTY) | SIGN WITH GAPS: G-e1 OPEN (e* in Dom), G-e2 (off by one, closed) | 643-776, 852-991 |
| (f) bit cost (TARGET.md §3) | SIGN, conditional, as in R-PROVED2 (k) | - |

No REJECT. There is one OPEN gap, G-e1: the case split "e* lies in a best_vertices call or in a −1 attractor" is DATA for
Dom pieces. Provably, e* ∉ sptl, and e* lies in Dom only through an X-straddling acceptance.

## (a) (S0) — SIGN (Opus 5.5, D12)
Every addition to region(τ) is one of the following, with q = pr τ (C2: CurR is consumed across tops and CurZ is the
current region):
- A p-vertex u with pr(u) ≤ q and an edge to a popped v ∈ region(τ) (74, 88). This is a threshold-q vertex rule.
- An opponent vertex u with pr(u) ≤ q and no successor in CurR \ CurZ (76-86). So all its R-successors lie in
  P(τ⁺) ∪ region(τ) (consumed or current), and it has the edge to v.
- A tangle accepted at an escape pop (200-201), whose new vertices are in CurR with priority ≤ q (138-141) and whose
  escapes are in CurZ, consumed (P(τ⁺) or popped) or outside R (155-156). This is a threshold-q tangle-rule instance with
  base P(τ⁺) ∪ {τ}.
So P(τ) ⊆ Cl_q(P(τ⁺) ∪ {τ}).
R-a1 (reading). Cl_q is dtl_ideal.lfp:
- only the NEW vertices of a tangle need priority ≤ q;
- a tangle needs ≥ 1 escape in the set;
- an opponent vertex needs ≥ 1 successor in the set.
The prose in §22c says "every vertex of priority ≤ q" and omits the trigger. (S0) holds under either reading.

## (b) PREFIX-MONO — SIGN WITH GAPS (Opus 5.5, D12)
- "Processed" matches the code: 692 skips a top already in the union of earlier regions.
- O1 is used correctly. Tops are taken in decreasing index (691), and indices are sorted by priority (oink.cpp:35,
  ensure_sorted), so the last processed top τ′ > τ has q′ = pr τ′ ≥ q.
- Induction: all three cases are correct.
  - The non-processed case is immediate.
  - In the processed/processed case, (S0) for run 1, step-ideal for run 2, and (S1) monotonicity in B and T (lfp: every
    rule is monotone in Z and T only adds rules) give the claim.
  - In the processed/absorbed case, P′(τ⁺) is threshold-q′ closed, hence threshold-q closed: every q-rule instance, with
    new vertices ≤ q ≤ q′, is a q′-rule instance. It contains P(τ⁺) ∪ {τ}, so it contains Cl′_q(P(τ⁺) ∪ {τ}) ⊇ P(τ).
- R-b1 (closed). For C2 the closure must have the trigger (R-a1). The threshold loop pushes ALL of Z at every level (724),
  so its pop loop computes exactly the triggered closure: W_t = Cl_t(W_{t−1}) = Cl_t(U). A trigger-free closure would
  overstate the code's W_t, because a tangle with no escape in the set is never tried (200-201).
- C1: U = P(lowest index). C2 holds by (S1). C3: candidates (714) and rescue (737-738) are monotone in U and W_t, and
  V ⊆ V′, so V_next ⊆ V′_next. C4 is immediate.
- Over all rounds: a returned stable V is a fixpoint of the round (716, 765-767), so the induction V_i ⊆ V′_i continues
  past either run's return. On a −1 return, RV records every drop round (770). RMONO follows for clean transitions:
  same V_1 (G′ fixed) and T_s ⊆ T_{s+1}.

## (c) POS-FALL — SIGN (Opus 5.5, D12)
- e* is not a threshold-level tattr: its output is the component W_{r,t} of Ψ, which would then differ.
- So e* is the region tattr of some τ_j in round r. Its input ({τ_j}, CurR = R \ P(τ_j⁺), pr τ_j) is equal in both
  searches, by FDL (earlier entries identical), and its output is strictly larger.
- Take v ∈ region′(τ_j) \ region(τ_j). v is unconsumed at τ_j in both runs, and v ∈ U_r(s) = U_r(s+1), so in s its region
  top has a lower index.
- RV equal gives V_r equal, so C4 applies to every vertex in every round (s+1 step-ideal). Every term n − index weakly
  falls, and v's falls strictly. So Φ_top falls. Correct.

## (d) ROOT-BOUND — SIGN WITH GAPS (Opus 5.5, D12)
- The case split is correct:
  - RV changes ⇒ it rises (RMONO);
  - RV equal and Ψ ≠ ⇒ Ψ rises componentwise (C1, C2);
  - RV and Ψ equal ⇒ POS-FALL.
- A transition with e* after the root call has an identical root call, so Π is equal.
- Chain heights:
  - RV: ≤ n coordinates, values 1..n+1 or INF, so ≤ n(n+1) rises.
  - Ψ: ≤ (n+1)(d+2) components, each ⊆ G′, so ≤ (n+1)(d+2)n rises.
  - Φ_top: 0 ≤ Φ_top ≤ (n+1)n², so at most that many falls.
- A strictly increasing chain in the lexicographic product has length ≤ ∏(h_i + 1) − 1 < H. Dirty transitions can lower Π
  arbitrarily, so per phase #(root-e* transitions) ≤ (#DIRTY + 1)·H + #DIRTY, with the stated H. Correct.
- G-d1 (closed; convention). When a round returns at 716 (no candidates), it runs no threshold loop, so Ψ's W_{r,t} are
  not computed. With RV equal, one search can have candidates in round r and the other none (U_r may differ). Fix: define
  W_{r,t} := Cl_t(U_r) for every round and level, whether the loop ran or not. Then the components align, and C2 keeps
  them monotone. The data tool should use the same convention.

## (e) §22e reduction — SIGN WITH GAPS (Opus 5.5, D12)
- best_vertices is a function of (R, p, T), with G fixed in a phase. Checked at 643-776:
  - It reads R, V (reset at 852) and the tangle store.
  - It reads this->G only for the deletion test at 132. A zombie tangle answers false either way, and the deletion flags
    change no answer.
  - It reads str only at 73, for members of the current set, which were written when they joined (694, 89, 171).
  - Candidates are written before they are read. W and X are not read. Q is empty at entry.
  - It writes str, but nothing downstream reads str before writing it (R-PROVED2 (h)(i)).
  Correct.
- The −1 attractor is a function of (R, X) and T. Its input comes from the threshold scan (898-912): seeds and t are a
  function of (R, X), via attracts(p, v, X, R). The search_rec-local Z is empty there (reset at 875 and 955, initially
  empty).
  - The attractor (918-923) consumes R, but popped vertices are always in Z. So "to ∈ R_cur ∧ to ∉ Z" ⟺ "to ∈ R0 ∧
    to ∉ Z", and "v ∉ Z ∧ v ∉ R_cur" ⟺ "v ∉ R0". It equals the non-consuming triggered closure of the seeds in R0 at
    threshold t, with every seed pushed and popped.
  - That closure is monotone in T (1.2b). Its output ⊆ R grows strictly at each change, so there are ≤ n changes per
    (R, X) along a phase. Correct.
- §22c does not use R = G′. PREFIX-MONO, its corollaries, POS-FALL and the chain heights are per round at a fixed context
  R, with V_1 = the p-priority vertices of R and n bounding |R|. Correct.
- The per-context count is correct. Π_R(T_s) is defined at every s (as a hypothetical call), and Π_R(T_s) ≠ Π_R(T_{s+1})
  at every transition whose e* is in a call at R. By PREFIX-MONO it rises unless the call under T_{s+1} has a step
  deficit (D_R).
- G-e1 (OPEN). The reduction assumes that e* lies in a best_vertices call or in a −1 attractor; the text says "DATA: never
  in sptl or Dom". Here is what follows from the code:
  - e* ∉ sptl. sptl's first pass recomputes the final round's regions of the identical preceding best_vertices call (same
    R, V*, T, and code path 481-500 vs 690-706). In s+1 it extracts only duplicates (nothing is learned before e*), so a
    reduced log has no further pass (FDL alignment).
  - e* in a Dom tattr, at an S piece (878-890) or a P piece (962-991), is NOT excluded. By the (YZ) reading (R-STEP5
    claim 4), Dom equals the final round's region loop step for step until Dom accepts an X-straddling tangle, i.e. one
    with a vertex in old X or in an earlier part. The final rounds are identical in s and s+1. So e* can be in Dom only
    through such an acceptance in s or s+1 at that piece. That happens on data (strfam_S5_n46, stable order).
  - Dom's output as a function of (V, R, X, T) is not shown to be monotone in T: it consumes top-down, which is the same
    obstruction as MONO. So these transitions have no budget yet.
  - Needed: either a proof that an X-straddling Dom acceptance cannot be the first difference, or a third term in the
    bound (and a third named statement).
- G-e2 (closed). A transition with no differing tattr is possible once per phase: s+1 repeats s, re-finds only duplicates
  and returns false (1068), so it is the last search. The bound should read S − 1 ≤ … + 1.
With G-e1, the reduction is correct as: GAP-A ⇐ (CTX) ∧ (DIRTY) ∧ (DOM-e*), where (DOM-e*) is "the number of transitions
whose first difference lies in a Dom tattr is polynomial per phase".

## (f) Bit cost — SIGN, conditional (Opus 5.5, D12)
- §22 bounds a count (searches per phase). H = O(n^8), and the sums over C_bv and C_T are combinatorial bounds; the
  algorithm never computes or stores them.
- The conversion to time is DTL-proof.md §3(e) / GAP-A-M §21c, signed in R-PROVED2 (k):
  - tangles ≤ n·searches (Lemma W with SCC1);
  - O((|T| + n)² n⁴ (m + n²)) word operations;
  - every stored number is an index, a priority ≤ n (after step-0 compression), a tangle index ≤ |T| or a bit.
- With (CTX), (DIRTY) and G-e1's (DOM-e*) polynomial, the number of searches is polynomial, so |T| is polynomial and
  every word has O(log n) bits. Unit cost = bit cost under TARGET.md §3. No number in the argument is used at unit cost
  beyond a word.

## Open points after this report
1. G-e1: e* in Dom through an X-straddling acceptance (no budget). It is an open term of the reduction, or must be
   excluded.
2. (CTX) and (DIRTY), DATA only, as the text says.
3. PI-RISE on dirty transitions (§22d), DATA only.

## Findings for the author (L-ALG), one line each
- R-a1/R-b1: define Cl_q as dtl_ideal.lfp (new vertices ≤ q, ≥ 1 escape in the set); C2 needs the trigger.
- G-d1: define W_{r,t} := Cl_t(U_r) also for rounds that return at 716.
- G-e1 (OPEN): "e* never in sptl or Dom" is DATA. e* ∉ sptl is provable; e* ∈ Dom needs an X-straddling Dom acceptance
  and has no budget. Add (DOM-e*) or exclude it.
- G-e2: one transition per phase may have no differing tattr (s+1 learns nothing); add +1.
