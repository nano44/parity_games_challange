# Fixes to packet P-N5-NJB, part 2: REFEREE-2's items and a concordance of both reports
L-SI successor 5 (Opus 5.5, D15/D18, L37/L40). Written 2026-10-25 11:02Z (date -u).
- Object: docs/si/P-N5-NJB-box9.md, sha1 f43a8823b3b50399dacb387697bdb433373ea671, pinned at trunk a7d85b3. FROZEN, not edited.
- Part 1: docs/si/P-N5-NJB-fixes-box9.md (l-si 32c2393, sha1 6a337748). It has NJB-1, NJB-2 and NJB-L1 (REFEREE succ. 7's R-N5-NJB).
  Part 1 is not edited either. Where a line here and a line in part 1 differ, the line here governs.
- Source: REFEREE-2 successor 7, docs/referee-2/R2-N5-NJB.md on origin/claude/referee-2 (head 8681e3f2 when read), with its §C and
  §C.3a. The joint gap map is its §C.3. Per §C.3a, REFEREE's §C (referee 5e85c70 / 0363a7b) accepted G-NJB-1.

## G-NJB-1 (MINSET (c), statement; REFEREE-2: SIGN WITH GAPS; joint row 1). Supersedes part 1's replacement texts for (b) and (c)
- The gap. Mn_{t+1} is defined against θ_{t+1}. By (a) at t+1, σ̄_{t+1}(o) ∈ Mn_{t+1}, so Mn_{t+1} ≠ ∅ at every interval state. Read
  literally, "(c) COARSE_M(θ) changes at t → t+1 exactly when Mn_{t+1} = ∅" therefore says COARSE_M(θ) never changes inside the interval.
  That is NJB, the CONJECTURE of §5.
- The proof proves the SURVIVOR form. Part 1's NJB-1 kept "Mn_{t+1} = ∅" in (c), so part 1's (c) text has the same gap. It is replaced
  here.
- Replacement text (the joint line of R2-N5-NJB §C.3 row 1, word for word):
  - (b): "a member of Mn_t that stays in F stays in Mn_{t+1} with the same COARSE_M value; members leave Mn only by entering R".
  - (c): "COARSE_M(θ) changes at t → t+1 exactly when no member of Mn_t lies in F_{t+1}; then every member of Mn_t entered R at t".
  - Consequence: "absorbed" → "entering R".
- The proof of (c) is the packet's, read with the survivor set Mn_t ∩ F_{t+1}. It is spelled out in R2-N5-NJB §2:
  - if some x ∈ Mn_t ∩ F_{t+1}, its frozen value equals COARSE_M(θ_t), and the sandwich gives COARSE_M(θ_{t+1}) = COARSE_M(θ_t);
  - if Mn_t ∩ F_{t+1} = ∅, every free exit at t+1 is free at t with an unchanged value strictly above the minimum, so the minimum
    rises.
- Status: literal (c) is NOT signed by either referee; survivor (c) is signed by both (R2-N5-NJB §C.3a).
- Part 1's "MINSET form of NJB, restated" was already in the survivor reading (an emptying step = every member of Mn_t enters R at t),
  so it stands. Its wording "Mn is never emptied by entries into R" means "Mn_t ∩ F_{t+1} ≠ ∅ at every interval step".
- Effect on the lane's own text: docs/si/N5-RL-box10.md does not use MINSET (c), and nothing there changes.

## N-NJB-1 (ENT-SHAPE (5); withdrawn by REFEREE-2 in §C.2)
- REFEREE-2 first signed (5) with the note N-NJB-1. That note assumed z ∈ F_{k0} and is withdrawn.
- Joint verdict: (5) as stated is NOT signed by either referee, and (5′) is signed by both. So part 1's NJB-2 line stands unchanged:
  (5′) verbatim, plus §5 item (iii) split into (iii-a) and (iii-b).
- REFEREE-2's independent data for (iii-b) (entp_probe.py, own N5): 278 local configurations in LIB ∪ NAMED, e.g. b6_xl2_n32, run 0,
  fallback 18 of level 31, y = 3, z = 23. The full ENT setting never occurs. It is a proof gap, not a counterexample.

## Concordance of the two reports (one row per gap)

| row | REFEREE (R-N5-NJB) | REFEREE-2 (R2-N5-NJB) | joint status | governing fixes line |
| --- | --- | --- | --- | --- |
| 1 | NJB-1 (wording: "absorbed" = entered R) | G-NJB-1 (statement: survivor form) | wording + statement; closed by the joint line | this file, G-NJB-1 (supersedes part 1's (b), (c) texts; part 1's NJB-1 term "enters R" kept) |
| 2 | NJB-2 ((5) not signed; (5′) signed) | N-NJB-1 withdrawn; NJB-2 accepted | (5) NOT SIGNED; (5′) signed by both | part 1, NJB-2 (unchanged) |
| — | — | — | data item | part 1, NJB-L1 (cl9_mn_a / cl9_mn_b split; no statement depends on it) |

- Signed by both, pending CHECKER (R2-N5-NJB §C.4): RDROP, PL (c′), PL-S′, MINSET (a), (b), (d) and survivor (c), NO-RF-OLD and its
  Corollary, ENT-SHAPE (1)-(4) and (5′).
- CONJECTURE: NJB, ENT. Further reductions: docs/si/N5-RL-box10.md (Propositions EV, EV+, TEV-RED, CONDITIONAL on (P); CONJECTURE TEV).
- OPEN: level −1 fallbacks per scope run, REL(S), G-N5-TIME.
