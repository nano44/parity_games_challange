# P-N5-OUT fixes (box 37 packet): REFEREE OUT-R1, OUT-N1; REFEREE-2 N-OUT-1..4; §7 status (NO-ENTRY-B and NO-ENTRY with c_w ≠ o FALSE)
L-NEW successor 17 (Opus 5.5, D15/D18), session_01ESR6bpU1r4ZjFsMExZtFpq. Written 2026-10-25 14:0xZ by date -u (clock 14:06:58Z), at the
Lead's request (14:03Z, Lead's stamp). Repairs only. Frozen at its commit; items from the §Cs go to a fixes2 file.
- Object: docs/new/P-N5-OUT-box37.md, sha1 9f032e616b515d703da4939cc1b0de89eb658aba, pinned trunk 719ce66. Unchanged.
- Reports:
  - REFEREE (succ. 8), docs/referee/R-N5-OUT.md at fa08687: all statements SIGNED; notes OUT-R1, OUT-N1; no gap.
  - REFEREE-2 (succ. 9), docs/referee-2/R2-N5-OUT.md final at referee-2 dfcaae67 (merged trunk 9f83566): all SIGN; notes N-OUT-1..4;
    no gap.
- No verdict or statement changes. No proof step changes, except the citation in §2 below.

## Map
| item | packet place | repair | kind |
| --- | --- | --- | --- |
| OUT-R1 = N-OUT-2 | §5 BASE (ii) of NO-ENTRY-A; §6 CASE-B-LEN | cite FBL-N (i) (R21 (c)) + F1 (R17 (a)) for "no arena edge raises W at v at a", instead of Step (K) (R23 (a), "inside a phase") | citation; covers b = a with a phase-exiting fallback |
| OUT-N1 = N-OUT-3 | §0 dependency table, KEY and FB-INT rows | status "IN REVIEW" → "signed by both referees (P-N5-SCOPE; landing)" | status wording |
| N-OUT-1 | §1 SPLIT (b) and §3 F-FLAT Step 1, the "(filled in)" target-o step | none: landed FBL-N (iii) uses the convention o ∈ R (P-N5-X §0), so R21 (c) (iii) already covers the target o; the filled-in step is correct and redundant | record |
| N-OUT-4 | §7 (not to sign) | CONJECTURE NO-ENTRY-B → FALSE; CONJECTURE NO-ENTRY for τ(o) ≠ o → FALSE when c_w ≠ o (both cases); see §3 | status (post-pin lane finding) |

## 1. OUT-R1 / N-OUT-2: the Step (K) citation at the base
- REFEREE (OUT-R1, remark, no gap): "(K) is used at the state a only, so b = a with a phase-exiting fallback is covered."
- REFEREE-2 (N-OUT-2, citation): Step (K) (R23 (a)) is stated "for a fallback inside a phase". NO-ENTRY-A lets a+1 leave S, and then
  possibly the phase (b = a). Cite FBL-N (i) + F1, or require a+1 ∈ S. NE-COUNT always has a+1 ∈ S.
- Repair. In §5 BASE (ii) and in §6 (CASE-B-LEN), read "against Step (K) (R23 (a))" as follows.
  - At the Even fallback a → a+1 with τ unchanged, σ_a is a pointwise arena optimum in G_τ (FBL-N (i), RESULTS R21 (c)).
  - The one-player optimum dominates every arena strategy pointwise (F1, RESULTS R17 (a)).
  - So no arena edge (v, z) raises W at v.
  - This uses only τ_{a+1} = τ_a, which holds at every Even fallback (S4c, FIX 3). It is Step (K)'s own proof.
- The same applies to P-N5-NEB §3 and §4 (pinned trunk 314d220, sha1 ba15e51f), which cite Step (K) the same way. That goes into a NEB
  fixes file, not here.

## 2. OUT-N1 / N-OUT-3: stale status of KEY and FB-INT
- Both are P-N5-SCOPE items, signed by both referees: REFEREE R-N5-SCOPE fb6089bf + §C 257c3d81; REFEREE-2 R2-N5-SCOPE 6d6e4bcf + §C
  fb6fa696. SCOPE fixes: docs/new/P-N5-SCOPE-fixes-box36.md (l-new eb5477a2, sha1 e2550755…). Landing is pending.
- Repair: the KEY and FB-INT rows read "signed by both referees; landing (P-N5-SCOPE)".

## 3. N-OUT-4: §7 status after the pin (lane box 38; DATA, verified by the Lead and reproduced by REFEREE-2 on its own traces)
- CONJECTURE NO-ENTRY-B (τ(o) = o, case B) is FALSE, from the canonical start.
  - Instance: experiments/new/box38/instances/nebc_cex_n14.pg, sha1 399119afb8741f3689081389e70729891937df7b. n 14, o = 7, rank(o) 6 <
    rank(c_θ = 12) 8.
  - n5 9 iterations / 5 fallbacks; Oink zlk OK, strategies verified (Lead re-run 12:54Z).
  - The run: the HN fallback at 1 → 2 switches 3 from 7 to 6, a length-only R → R̄ switch with Ξ(3) (12, ∅, 3) → (12, ∅, 4). At 2 a
    gate 4 → 3 goes from F into R̄. S4a 2 → 3 enters 4, with θ = (12, ∅, 2) constant.
  - Also from a start pair: experiments/new/box38/instances/neb_cex_n11.pg (sha1 232b8951…) + .state (7b79ecd5…).
- CONJECTURE NO-ENTRY for τ(o) ≠ o is FALSE when o does not top its W-cycle (c_w ≠ o), in both cases, from the canonical start.
  - experiments/new/box38/instances/tauw_A_cex_n24.pg (case A), sha1 e29908d546d62e64903b41aa987351c3b3c68a62; n5 16 / 3; Oink OK.
  - experiments/new/box38/instances/tauw_B_cex_n24.pg (case B), sha1 c0ad4f0ca6ce9a35d3c89b377e686eef58dc3845; n5 10 / 4; Oink OK.
  - Lead re-runs 13:36Z.
- What survives (lane PROVED, packet P-N5-NEB, pinned, in the referee queue):
  - NO-ENTRY holds exactly in case A with c_w = o at the fallback, any τ(o) (NEB §3).
  - Elsewhere every break is paid by a θ-change or an R̄-rise (NEB §1, §6).
  - For τ(o) = o, the §7 "given NO-ENTRY" reduction is replaced by NEB Corollary OUT-1. It holds in both cases without NO-ENTRY-B.
- §7's "Reduction (READING) given NO-ENTRY" is therefore valid only in case A with c_w = o (for τ(o) = o: case A).
- DEAD END ROUTE-FROZEN (rfroz_cex_n16, sha1 a9b40395…): unchanged; REFEREE-2 reproduces it.
- The RESULTS entry should carry these FALSE statuses (REFEREE-2 N-OUT-4).
