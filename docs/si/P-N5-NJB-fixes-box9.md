# Fixes to packet P-N5-NJB (box 9 part 2), for the referees
L-SI successor 5 (Opus 5.5, D15/D18, L37/L40). Written 2026-10-25 09:35Z (date -u).
- Object: docs/si/P-N5-NJB-box9.md, sha1 f43a8823b3b50399dacb387697bdb433373ea671, pinned at trunk a7d85b3. The packet is FROZEN and
  is not edited. Each line below replaces packet text; where a line and the packet differ, the line governs.
- Sources: REFEREE successor 7, docs/referee/R-N5-NJB.md (referee 524d93f): gaps NJB-1, NJB-2. One lane item (NJB-L1, data only).
  REFEREE-2's R2-N5-NJB was not on trunk or origin/claude/referee-2 when this file was written; its items go to a fixes2 file.
- Labels: PROVED (L-SI succ. 4, repaired here by L-SI succ. 5), CONJECTURE, OPEN, DATA.

## NJB-1 (§2 Lemma MINSET, wording; REFEREE: SIGNED WITH GAP, closed by this line)
- The packet's §0 keeps R30's ABSORPTION: σ̄(o) changes from x0 with x0 ∈ F_k ∩ R_{k+1}. Only x0 = σ̄_t(o) is ever absorbed.
- New term. A member x of Mn_t ENTERS R at t when x ∈ F_t ∩ R_{t+1}. Several members may enter R at one step, and a member other than
  σ̄_t(o) may enter.
- Replacement text, word for word:
  - (b): "Inside the interval, Mn loses members only by entry into R, and its members keep their COARSE_M value."
  - (c): "COARSE_M(θ) changes at t → t+1 exactly when Mn_{t+1} = ∅. Then every member of Mn_t has entered R at t."
  - Proof of (b): "a member drops out only by entering R."
  - Consequence: "on the r > M part of a block, NJB (§5) is equivalent to 'Mn is never emptied by entries into R strictly inside the
    block'."
- The proofs use only entry into R, so no proof step changes.
- In §5 and §6 too, "absorption of a member of Mn" and "members absorbed" mean entry into R. The script minset.py counts entries
  (x ∈ Mn_t, x ∈ R_{t+1}).
- MINSET form of NJB, restated: inside a block (r > M part), Mn is never emptied by entries into R. Since σ̄_t(o) ∈ Mn_t (MINSET (a)),
  an emptying step t has every member of Mn_t entering R at t, σ̄_t(o) among them. So an emptying step is an R30 absorption: x0 = σ̄_t(o)
  is absorbed at t while every other member of Mn_t also enters R.

## NJB-2 (§4 Lemma ENT-SHAPE (5); REFEREE: NOT SIGNED as stated; (5′) SIGNED)
- Replace (5) by, word for word (the referee's line):
  "(5′) z's honest value rises at level exactly L at some transition s ∈ [k0, k). Either s = k0 and z ∈ R_{k0} ∩ F_{k0+1} (z leaves R
  at the fallback), or s is an S4a step in (k0, k) with z ∈ F_s ∩ F_{s+1}. In the second case U-loc and (A_s) leave only Even switches
  of level ≤ L on z's F-play, so the rise needs a switch of level exactly L on that play."
- Why s = k0 needs z ∈ R_{k0}: if z ∈ F_{k0}, Ξ(z) is unchanged at the fallback (FBL: z's F-play meets only flat cycle-node switches), so
  s ≠ k0. The packet's "z ∈ F_s (no leave)" holds only for s ≥ k0 + 1.
- Referee's instance of the local configuration (no violation): experiments/si/orlens/instances/cycelim_cex_n32.pg, fallback 15 of
  level 31: z = 7 ∈ R_15 ∖ R̄_16, Ξ(7) rises at level 31, and (15, 7) is a level-31 gate into F at 16 but not at 15. The full ENT setting
  never occurs in the data (R-N5-NJB §4.2).
- §5 obstruction, item (iii), replaced by:
  "(iii) an F-vertex z whose rank-L bit goes bad → good while its COARSE_L(Ξ z) stays fixed, either
     (iii-a) at an S4a step in (k0, k) through an F → F level-L switch on z's F-play, or
     (iii-b) at the fallback k0 itself, with z ∈ R_{k0} evicted from R at k0 (z ∈ R_{k0} ∩ F_{k0+1})."
- §5 text after the list, added: "So a violation's z may come from a fallback eviction at k0, not only from an F → F level-L switch
  inside the interval. The 569 / 1,159 local (iii-b) configurations of R-N5-NJB §5 show that branch is common on its own."

## NJB-L1 (§6 data, lane item: the two MINSET climb bests were summed under one name)
- Packet §6 says cl9_mn_a has "56 Mn-member absorptions inside block intervals and 33 intervals with |Mn| = 1". That sums the two climbs
  (logs/box9/minset_climb.txt is one TOTAL line over both files).
- Re-run 2026-10-25 by L-SI succ. 5, `python3 minset.py instances/box9/cl9_mn_a.pg`, then the same for cl9_mn_b (experiments/si/coarse/):
  - cl9_mn_a: intervals 13, Σ|Mn| at interval starts 185, intervals with min |Mn| ≤ 1: 0, member entries 56.
  - cl9_mn_b: intervals 33, Σ|Mn| 33, intervals with min |Mn| ≤ 1: 33 (|Mn| = 1 from every interval start), member entries 0.
  - Both: Mn emptied 0, MINSET (c) mismatches 0.
- So the corrected line is: "cl9_mn_a: 56 member entries into R inside 13 block intervals, |Mn| never 1. cl9_mn_b: |Mn| = 1 in all 33
  intervals of its one 34-fallback block, and no member ever enters R. Mn is never emptied in either."
- This matches L-RED 15's corrected relay (via the Lead, 2026-10-25 09:33Z): cl9_mn_b reaches |Mn| = 1 in 33 of 33 intervals and
  cl9_mn_a does not. The totals (46 intervals, 218, 33, 56) are unchanged. The handover line "|Mn| reaches 1 … cl9_mn_a has 56
  absorptions … none of the last member" mixes the two files in the same way.
- No statement depends on §6.
