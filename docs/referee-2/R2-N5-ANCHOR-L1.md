# R2-N5-ANCHOR-L1: word-diff of P-N5-ANCHOR line L-1 (REFEREE-2 successor 25, Opus 5.5, D15; written 2026-11-01 18:36Z by date -u)
- Object: claude/l-new 6bcf5529, docs/new/P-N5-ANCHOR-line-L1.txt, sha1 baad574de36cd167a60bbad7831d491e2958cf87 (re-hashed: match).
  - Base: the frozen line 7f140d0c, unchanged at 6bcf5529. 543 → 601 words.
  - The frozen packet ad97ad88 is unchanged. Fixes file sha1 4cff05c1 (re-hashed).
- My report docs/referee-2/R2-N5-ANCHOR.md (b431ec81) was pushed before this. I have now also read REFEREE's R-N5-ANCHOR.md, to check the
  «(both referees)» attribution only.

## Token diff: every change, nothing else
1. Premise: «RESULTS R57 [-/ R102-]». R57 alone (optional item). 1E-N3 here is S4a's optimality, which R57 covers; R102 (S4B-OPT) is not
   used. ✓
2. «not its own [-W-cycle node-]{+W′-cycle node,+}». My P-ANC-3. ✓
3. «[-(item (R1), referees to rule))-]» → «((R1) holds as a consequence of R24 (a) and (b)'s choice rule (both referees)); a tie-break
   chooses the κ-least FULLY W′-optimal option, W′ := the arena optimum, where an option is a corner when x occurs on its play before its
   cycle node (vacuous for fully W′-optimal options))».
   - The (R1) ruling is stated. **ANCHOR-L1 met.**
   - «(both referees)» is accurate: REFEREE R-N5-ANCHOR.md l. 10 «(R1): [RULE] at non-movers | RULED: covered. No separate premise», and
     mine §2.
   - Ties are FULLY W′-optimal under W′ := the arena optimum. The corner is defined in the before-cycle-node form and noted vacuous. This
     is my G-ANC-1, and REFEREE's ANC-1 is the same reading. **ANCHOR-L2 met, except κ (below).**
4. «ℓ* := the largest level of an Even vertex not in CN{+ (1 if none)+};». My P-ANC-2. ✓
5. «[-afterwards-]{+at transitions j ≥ s0 + ℓ*+} each Even c ∈ CN moves at most #T_c − 1 [-times,-]{+times in the epoch,+}».
   - This is REFEREE's ANC-L2 and correct. A move after state s0 + ℓ* − 1 is a transition j ≥ s0 + ℓ*, and packet §4 (ii) counts them
     inside the epoch. ✓
6. «docs/new/P-N5-ANCHOR-box134.md{+ with its fixes entry 1, docs/new/P-N5-ANCHOR-fixes-box134.md+};». ✓
- Nothing else changed. The DEAD clause, CIRC, FL-GCH and the scope tail are token-identical.

## One item left
- **ANCHOR-L1-1 (REQUIRED, one phrase): κ is undefined in the line.** «the κ-least FULLY W′-optimal option» is the line's only use of κ.
  - Neither the frozen line nor L-1 defines it.
  - R24 (b)'s signed text has «indices» and «pk(v)», not κ.
  - My ANCHOR-L2 asked for «κ as in packet §1». A free symbol in a landing line is CHECKER's recurring E-item.
  - Fix: after «κ-least», add «(κ := the vertex index if x's W′-cycle node c is odd, and the root-first key — the indices of the play path
    from c to the option, c excluded, compared lexicographically — if c is even)», or the equivalent wording of packet §1 [RULE].
- Not required: the optional CIRC j-range and N-ANC-2 items are in the fixes file, not in the line, so the line needs nothing for them.

## Verdict
**Does not yet MATCH**: ANCHOR-L1-1, defining κ, is REQUIRED. Every other item of mine is met, and nothing beyond the listed items changed.
I will word-diff L-2.

## DONE / FINDINGS / NEEDS
- DONE: this file; the token diff; the sha1s; REFEREE's (R1) ruling checked for the «both referees» attribution.
- FINDINGS:
  - ANCHOR-L1 and ANCHOR-L2 are met, and P-ANC-2/3 are taken.
  - REFEREE's ANC-L2 anchor is correct.
  - One new REQUIRED item: κ is a free symbol (ANCHOR-L1-1).
- NEEDS: Lead: ANCHOR-L1-1 to L-NEW for line L-2.
