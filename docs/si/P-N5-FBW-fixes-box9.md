# P-N5-FBW fixes (box 9): the referees' items, written out
L-SI successor 4 (Opus 5.5, D18/L40). Lead relay 07:05Z. Written 2026-10-25 07:08Z (date -u).
- Object: the packet docs/si/P-N5-FBW-box9.md, pinned at trunk e69772b, sha1 88337bd621d3467dde4b35aa93b254bf847bb330. It was re-checked
  at this commit and is unchanged. The packet is NOT edited; this file is its correction layer. The file contains repairs only: no
  strengthening of the reviewed text (Lead 06:56Z).
- Sources:
  - REFEREE: docs/referee/R-N5-FBW.md (referee 9a94dc7b), table and "Fixes-file lines".
  - REFEREE-2: docs/referee-2/R2-N5-FBW.md (referee-2 25962855), §4.
- Verdicts: every statement is SIGNED by both referees. Neither report has a NOT SIGN, and neither has a counterexample.

| item | referee | statement | kind | status |
| --- | --- | --- | --- | --- |
| FBW-1 | REFEREE | §3 Lemma FLAT-ALL (i) | citation | closed by the repair below |
| FBW-2 | REFEREE | §4 STRETCH statement / §5 PL (a) | wording | closed by the repair below |
| N-FBW-1 | REFEREE-2 | §4 STRETCH statement | wording (same point as FBW-2) | closed by the same repair |

## FBW-1 (§3 FLAT-ALL (i))
- Replace "That cycle does not contain o: otherwise it would be o's W-cycle at k+1, against H2." by:
  - "That cycle is y′'s honest H_{k+1}-cycle (λ(y′) = y′ refers to Ξ). It does not contain o, else H1 would fail at k+1. The
    hypothesis '(h) at k+1' contains H1. Off o the honest graph and the (σ, τ)-graph agree, so the rest of (i) follows."
- (REFEREE: a cycle through o in H_{k+1} uses σ̄(o), not τ(o), so it need not be o's W-cycle.)

## FBW-2 = N-FBW-1 (§4 STRETCH statement, used in §5 PL (a))
- In §4, replace "among the fallbacks k of S with s ≤ k < e" by "among the fallbacks k of S with s ≤ k ≤ e".
- The proof is unchanged. Step (3) shows that b stays good on [k+1, e], so y is not a level-M tail at any later fallback
  k′ ∈ (k, e], k′ = e included.
- §5 (a) then also covers the block's last fallback f_N. That fallback may be the last state of its constant-COARSE_M run, when
  COARSE_M changes at f_N's own transition (REFEREE FBW-2; REFEREE-2 N-FBW-1).

## Labels after both reports (D18/L40)
PROVED (L-SI successor 4; REFEREE and REFEREE-2, Opus 5.5, D15), pending CHECKER: Lemma FBW, Corollary FBW-S, Theorem CLS2, Lemma
FLAT-ALL (with FBW-1), Lemma STRETCH (with FBW-2 = N-FBW-1), Theorem PL (a)-(c), Corollary PL-S. NOT TO SIGN as before (§6). G-N5-TIME
stays OPEN.
