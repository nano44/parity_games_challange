# N5 box 11, part 3 (L-SI successor 6): why NL= is delicate: a candidate leave shape at r = L (READING, for L-RED)
L-SI successor 6 (Opus 5.5; D14, D15, D18, L37, L40). Written 2026-10-25 ~13:20Z (date -u). Lane write-up, unrefereed; adds to
docs/si/N5-STR-box11.md (sha1 c7b9c671, frozen), which states CONJECTURE NL= and the reduction NJB ⇐ (P) ∧ NL=.
- Labels: PROVED (L-SI succ. 6); READING (argument sketch, not checked line by line); CONJECTURE; DATA.

## 1. Why r > L excludes it and r = L does not (PROVED, L-SI succ. 6)
- Setting: an in-phase S4a step s → s+1 of a scope run S after a fallback k0 of S with L := M_{k0} ≥ 0, with (h) at s and (A_s).
- Let p ∈ R_s be Even with σ_s(p)'s route π := π^s_{σ_s p} low (π ∩ H = ∅), and suppose o ∉ H.
- Let z ∈ F_s be a successor of p with COARSE_L(o ⊕ Ξ_s z) = COARSE_L(w) and β_L(Ξ_s z) = β_L(w), i.e. z agrees with w down to and
  including the rank-L bit. The prime case is z = e* (then o ⊕ Ξ_s(z) = w exactly, by H2 and Lemma G).
- Then (p, z) is a gate at s, of level r_s if r_s > L and of level exactly L if r_s = L:
  - Ξ_s(z) against b_s(p) = π ⊕ θ_s.
  - π and o are low. So their COARSE_L classes are (c, P(Ξ_s z) ∩ H) and (c, P(θ_s) ∩ H), which coincide iff COARSE_L(θ_s) = COARSE_L(w),
    i.e. iff r_s ≤ L.
  - If r_s > L and z = e*: the top difference is at rank r_s > L and favours z ((C7) through o: o ⊕ Ξ(e*) = w ▷ θ at level r_s). (For
    a general z of §1's kind this case is a READING: only COARSE_L and the rank-L bit of z are fixed.) So (p, z) is a gate
    into F_s of level r_s > L, which (A_s) forbids. Hence no such p lies in R_s at any state with r_s > L (and none enters, by NL (iii)).
  - If r_s = L: the classes agree and the rank-L bit favours z, so (p, z) is a gate into F_s of level exactly L. (A_s) allows it.
- So once r has dropped to L (the straddle's [t1, k], N5-STR-box11 §1), a low-route vertex p of R with an edge to e* (or to a free vertex
  agreeing with w to rank L) carries an admissible level-L gate out of R.

## 2. Candidate leave at r = L (READING; a target for L-RED, not a counterexample)
- S4a switches p → z if the arena optimum prefers it.
- In W-terms the comparison is p ⊕ W(z) against π_p ⊕ w = p ⊕ π ⊕ o ⊕ W(e*). For z = e*, it is decided by the top of ({o} ∪ π) ∩ V_{>c},
  or by the length if that set is empty.
- With rank o < L, o odd, rank o > rank c and π below c, the bypass is W-better (it drops an odd vertex). Then p leaves R at an S4a step
  with r = L. That violates NL= (ii).
- What a construction must also arrange:
  - p is in R at some state of the r = L stretch. By §1 it cannot be in R before t1 (the state where r reaches L), so it must ENTER R
    during the stretch, or at t1 − 1 → t1.
  - Entering means the arena optimum preferred the route through o at that step, while the bypass gate (p, e*) was already there (§1)
    and W-better. So entry and later exit need W to change in between: the route's value π ⊕ w can change only through π (w is constant
    on S), or the entry happens through a different predecessor chain.
- This tension (enter by the route, then leave by a bypass that was already W-better) is a plausible reason for the 0 leaves at r = L in
  743 steps (N5-STR-box11 §4). It is not a proof.
- CONJECTURE NL= stays as stated. If L-RED finds a leave at r = L, NJB's straddle stays OPEN, while D_M ≤ 1 (P-N5-ENT, CONDITIONAL on (P))
  is unaffected.
