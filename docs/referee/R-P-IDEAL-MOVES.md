# R-P-IDEAL-MOVES: REFEREE report on P-IDEAL-MOVES (L-NEW successor 57, box 187)
REFEREE successor 24 (Opus 5.5, D15), 2026-11-06 (date -u in the commit). Independent: docs/referee-2/ was not opened on this packet.
- Object: claude/l-new d86adc86 (an ancestor of origin), detached worktree. Re-measured:
  - packet 5ce2947d…, 202 lines; L-1 819c5815…, 4,313 bytes;
  - movescheck.py 8153717b…; movescheck.out 48740209…;
  - instances pass_d3_D3 8bca9764…, pass_d4_D4 3bf6a4a4…, pass_d5_D5 16be2e59…, m4_z4_r7 7c158e2f….
- Premises checked on trunk b876c884.

## 0. Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §1 | REDUCE-XI; Corollary MOVES-EQUIV | SIGN |
| §2 | AND-GATE (a), (b), (c) | SIGN |
| §3 | WINDOW-DOUBLE (a), (b) (incl. BURST-2) | SIGN |
| §4 | SEG-WINDOW (a)-(e) | SIGN |
| §5 | DEAD-SEG (c ≤ 4); DEAD-LEV | SIGN (instances recomputed with my own simulator) |
| §6 | DATA / exclusions / TARGET diff | not to sign; check.sh block PASS; DATA rule applied (§3) |
| line | L-1 | MATCHES; optional MV-L1 |

## 1. Premises and proofs
- Premise quotes are FOUND verbatim on b876c884:
  - R105 ENC, LOCAL, MONO, XI-NEW, RISE («at any degree»);
  - R110's 𝓛^R_d;
  - R113 ALIGN, F0 and the notation quotes (KP_s, c_l, γ_l, F(l)).
  E-2 does not bear.
- REDUCE-XI: SIGN.
  - XI-NEW / RISE give, for the least-level mover h of step t ≥ 2, a strict Ξ-descendant y moving at t − 1. The last edge of a path to
    y makes y a Ξ-target, so y ∈ Z.
  - t ↦ t − 1 is injective.
- MOVES-EQUIV: SIGN. Each level-0 mover moves at most once (F0), and Z ∩ level ≥ 1 has ≤ 2d − 2 movers. This gives
  3 + (2d − 2)μ(d), and with μ ≤ 2d it gives 4d² − 4d + 3.
- AND-GATE: SIGN.
  - (a): the degree-2 A-set is {s} or both options, and the step takes the key-least option under s_t.
  - (b): s_t(x) = π_(s_(t−1))(x) = KP_(s_t)(x) at both consecutive moves; the windows are disjoint.
  - (c): v(x, a) is non-decreasing (ENC + MONO), so the strict chain holds.
- WINDOW-DOUBLE: SIGN.
  - (a): ALIGN's order formula, and c_j changes only at flips of the pair below.
  - (b): the PAIR-DOUBLE potential argument on a window, with Φ(a) ≤ 2. BURST-2 is the F_W(j − 1) = 0 case.
- SEG-WINDOW: SIGN.
  - (a): consecutive moves at t − 1 and t give a KP change at t (AND-GATE (b)), and by ALIGN that is a flip of (u, w).
  - (b): the pass-through descent ends at a moving pair, at level 0 at the latest, since level-0 keys are their own gates.
  - (c): (a) + WINDOW-DOUBLE (b), and F0 at l = 1.
  - (d): (a) + BURST-2.
  - (e): AND-GATE (a)-(c) with LOCAL. The chain's movers after x are not x (acyclic).

## 2. Independent checks (my simulator t3r_sim.py; no lane code)
- DEAD-SEG:
  - pass_d3_D3, start 110100: in 𝓛^R_3, T 4, mover 5 (level 2, ∈ Z) moves at 1, 2, 3; segment D 3, LM 0.
  - pass_d4_D4, start 01010111: T 4, mover 7 (level 3, ∈ Z) moves at 1-4; D 4, LM 0.
  - pass_d5_D5, start 0101010110: T 5, mover 9 (level 4, ∈ Z) moves at 1-5; D 5, LM 0.
  - So «D ≤ 2·LM + c» fails for c ≤ 4. All EQUAL to §5 and movescheck.out.
- DEAD-LEV: m4_z4_r7, stored start 10111010: in 𝓛^R_4, T 8, mover 4 (level 2, ∈ Z) moves at 1, 2, 3, 5, 6, 7, 8. That is 7 > 6.
  EQUAL.
- check.sh block «P-IDEAL-MOVES» at d86adc86: PASS (pins; movescheck.out regenerated identically).

## 3. DATA rule (every signed clause of L-1 has a counter or a no-DATA entry; counters read in movescheck.py)
| clause of L-1 | counter / entry | verdict |
| --- | --- | --- |
| REDUCE-XI: step t − 1 moves a member of Z; T ≤ 1 + Σ moves(z) | RX (l. 40: both) | MATCH |
| MOVES-EQUIV | «no separate DATA» | MATCH |
| AND-GATE: moves iff s ≠ π = KP | AGA (l. 51) | MATCH |
| AND-GATE: moves(x) ≤ 1 + min(KF_x, PF_x) | not counted; follows by arithmetic from AGB on every consecutive pair (disjoint windows, each with a π and a KP change) | MATCH by arithmetic (optional MV-L1) |
| AND-GATE: v(x, b) rises when π changes to b | AGC (l. 54) | MATCH |
| WINDOW-DOUBLE: pass-through clause | «no separate DATA» | MATCH |
| WINDOW-DOUBLE: F_W(j) ≤ 2 + 2F_W(j − 1) | WPD (l. 86), 1,288,162 pairs | MATCH |
| WINDOW-DOUBLE: BURST-2 | SWD (l. 80) | MATCH |
| SEG-WINDOW: flips at every step (a) | SWA | MATCH |
| SEG-WINDOW: a mover of level < l at every step (b) | SWB (also D ≤ 1 + LS + PT) | MATCH |
| SEG-WINDOW: D bound (c) | SWC | MATCH |
| SEG-WINDOW: 3-step clause (d) | «no separate DATA» | MATCH |
| SEG-WINDOW: a chain mover other than x moves (e) | SWE (l. 70-72; g.play lists the movers AFTER x, so the check is not vacuous) | MATCH |
| DEAD items | «DEAD-SEG …», «DEAD-LEV …» lines | MATCH |
- Optional MV-L1: the line's «AND-GATE 0 on … every pair of consecutive moves» covers moves ≤ 1 + min(KF, PF) only by arithmetic.
  Either say «(the min bound by arithmetic)», or leave it (C125 G-9 (iii) precedent: a bound that follows by arithmetic from counted
  checks is a note).

## 4. TARGET diff, line L-1
- TARGET: every statement is inside R104's IDEAL model; MOVES-EQUIV is an equivalence, not a bound. Not M3, not M4, not a gauntlet step.
  G-N5-TIME OPEN. Agreed.
- L-1:
  - Shape: one line, 68 «(» / 68 «)», depth never negative, 0 «|», one « — », «2026» once.
  - Definitions diffed against §0: T, Mv_t, moves (E2c), Z, KP_s, KF_x, π_s, PF_x, v_s, F_W(j), T^R(d), μ(d), metronome segment, LM
    all MATCH. The pair l − 2 is (2l − 4, 2l − 3); correct.
  - Claims MATCH their signed forms.
  - The source note names the packet; all proofs are in it.
- Verdict: L-1 MATCHES.

## DONE / FINDINGS / NEEDS
- DONE: premise byte tests; every proof re-derived; DEAD instances recomputed; check.sh block; DATA rule clause by clause; L-1.
- FINDINGS: every item SIGNED; L-1 MATCHES; optional MV-L1.
- NEEDS: none.

## §C. Fixes entry 1 and line L-2 (REFEREE successor 25, 2026-11-07T00:0xZ by date -u; Opus 5.5, D15)
- Objects (claude/l-new 9995f5a2, fetched; sha1 of the bytes in that commit):
  - docs/new/P-IDEAL-MOVES-fixes.md (entry 1): e933f4d3b42ec0405fefd5654d7b7afe5eea35be, 4,635 B. EQUAL to the Lead's relay.
  - docs/new/P-IDEAL-MOVES-line-L2.txt: f3692aaa033540ff0494b0aac6b2d524757d5c00, 4,495 B. EQUAL.
  - Unchanged: packet 5ce2947d1ee4dab3… (= the signed pin), L-1 819c58159100d77e…, movescheck.py 8153717b….
  - REFEREE-2's report read for the required texts: claude/referee-2 38a2adb6, docs/referee-2/R2-P-IDEAL-MOVES.md l. 104-115.
- Byte test (own script; the five «old» → «new» items parsed from the fixes file, wrapped lines joined by one space):
  - each old string occurs exactly once in L-1; L-1 with R1..R5 applied in order is byte-equal to L-2 (4,495 = 4,495 B).
  - So L-2 = L-1 + exactly R1..R5, nothing else.
  - Shape: one line, 71 «(» / 71 «)», depth never negative, 0 «|». The word diff in the entry agrees with these five items.
- Meaning, item by item (against the packet text):
  | item | new text | packet | verdict |
  | --- | --- | --- | --- |
  | R1 (W-1) | «… μ(d) is shown equal to T^R(d) up to a factor 2d − 2 and an additive 3, so MOVES-2D is sufficient, not necessary, for a polynomial bound on T^R» | §1 MOVES-EQUIV l. 88-93: μ(d) ≤ T^R(d) ≤ 3 + (2d − 2)·μ(d); MOVES-2D ⇒ T^R(d) ≤ 4d² − 4d + 3; μ polynomial iff T^R polynomial | first half MATCHES; «not necessary» NOT PROVED (MV-C1) |
  | R2 (W-2) | «flips while 2j and 2j + 1 are on different options before the step» | §3 (a) l. 115-116: p := 2j, q := 2j + 1, s_(t−1)(p) ≠ s_(t−1)(q) | MATCH |
  | R3 (W-3) | «some mover other than x on the chain under s_(t−1) of the option x takes at t + 1 moves at t» | §4 (e) l. 142-143: «some mover of the chain of (x, s_(t+1)(x)) under s_(t−1), other than x, moves at t» | MATCH; this is the reading REFEREE-2 asked for («… moves at t») |
  | R4 (MV-L1) | «every pair of consecutive moves (the min bound by arithmetic)» | AND-GATE (b); my §3 row | MATCH (the form I suggested) |
  | R5 | source note names fixes entry 1 and its file | — | MATCH |
- MV-C1 (required). The packet proves that MOVES-2D is sufficient. It does not prove that MOVES-2D is not necessary: no statement
  says that a polynomial T^R is compatible with μ(d) > 2d. MOVES-2D is open; the DEAD m4_z4_r7 gives 7 ≤ 2d = 8, and l. 177 says
  «Does NOT claim: anything about MOVES-2D». If MOVES-2D is true, it is trivially necessary. «Not necessary» is therefore an
  unproved claim inside the not-claimed clause. (REFEREE-2's W-1 intent was right: the equivalence claim is gone. Only its last two
  words overreach.)
  - Exact fix, one replacement on L-2 (old occurs exactly once):
    «so MOVES-2D is sufficient, not necessary, for a polynomial bound on T^R)» → «so MOVES-2D is sufficient for a polynomial bound on
    T^R, and its necessity is not shown: a polynomial bound on T^R gives only μ polynomial)»
  - Result, tested by my script: one line, 4,563 B, 71 «(» / 71 «)», sha1 747dfa48c3a6a1d75f4d92aea5aa086128b87588 (with a source
    note unchanged; if L-NEW also updates R5's note to name entry 2, the sha1 changes).
- DATA rule, clause by clause:
  - No count changes: the word diff touches no number, and the DATA parenthesis differs from L-1 only by R4.
  - R2's clause is WINDOW-DOUBLE's pass-through clause. It keeps «no separate DATA».
  - R3 narrows the SEG-WINDOW (e) clause to «moves at t». The counter SWE (movescheck.py l. 15, 70-72) checks exactly that set and
    time: for t ∈ [a, b − 1], some y ∈ g.play(S[t − 1], x, S[t + 1][x]) with y ∈ Mv[t]. Unit (per segment step), set (every metronome
    segment) and scope all match «0 on all 225,917 metronome segments … and its last one».
  - R4: AGB (l. 9, 56) counts every consecutive pair; the min bound follows by arithmetic and is now labelled so.
  - R1: MOVES-EQUIV keeps «no separate DATA».
- §6 l. 202 «an equivalence of two open bounds»: the fixes entry's wording note («μ polynomial», «T^R polynomial») is right. No
  packet edit needed; the packet does not contain W-1's overclaim (l. 90-91 says «iff» between the polynomial bounds only).
- Verdict:
  - Fixes entry 1 is CORRECT for W-1 (equivalence overclaim removed), W-2, W-3, MV-L1 and the D-1..D-3 notes.
  - L-2 MATCHES the byte test.
  - L-2 does NOT YET MATCH in meaning: one required replacement, MV-C1 above. With it, the line MATCHES.
  - All packet items stay SIGNED.
- I did not read docs/referee-2/ beyond the W-1..W-3 texts named above. This section is not a comparison with REFEREE-2's §C.

## §C add. 1. Fixes entry 2 and line L-3 (REFEREE successor 25, 2026-11-07T00:4xZ by date -u; Opus 5.5, D15)
- Objects at claude/l-new d7b96be8 (fetched):
  - fixes file (entries 1-2): sha1 8d6223a2fe19e9de37aa86f7bb5b7c2e8dff341c, 7,238 B. Its first 4,635 B are byte-equal to entry 1's
    file (e933f4d3), so it is append-only.
  - L-3: sha1 d3983c68cdda03e81fdaedec770af587f758d84e, 4,567 B.
  - Unchanged: packet 5ce2947d, L-1 819c5815, L-2 f3692aaa, movescheck.py 8153717b.
- Byte test (own script):
  - R6's and R7's old strings each occur exactly once in L-2.
  - L-2 + R6 = 4,563 B, sha1 747dfa48…, which is my §C prediction.
  - Then + R7 = 4,567 B, sha1 d3983c68…, byte-equal to L-3. The replacement texts in entry 2 equal the applied ones.
  - Shape: one line, 71 «(» / 71 «)», depth never negative, 0 «|».
- Meaning:
  - R6 is exactly MV-C1's text. It states sufficiency (§1 MOVES-EQUIV) and «a polynomial bound on T^R gives only μ polynomial»
    (§1: μ(d) ≤ T^R(d)). MATCH.
  - R7: the source note names entries 1-2. MATCH.
  - Note (no fix): entry 2 labels R6 «the Lead's text verbatim». The text is REFEREE 25's MV-C1, relayed by the Lead. Entry 2's
    MV-C1 bullet attributes it correctly.
- DATA: no count or DATA clause changes. The DATA parenthesis is byte-equal to L-2's.
- Verdict: fixes entry 2 is CORRECT. L-3 MATCHES the byte test and in meaning. All packet items stay SIGNED.
- The Lead's question: does any signed statement depend on MOVES-2D being open? This concerns L-LOWER 3's CANDIDATE kill, which I
  have not replayed; I did not open its files. Answer: NO. I checked every occurrence in the packet (5ce2947d):
  - As an antecedent only:
    - MOVES-EQUIV l. 90-91, «In particular MOVES-2D implies T^R(d) ≤ 4d² − 4d + 3».
    - Its proof l. 93, «Under MOVES-2D, μ(d) ≤ 2d».
    - A false MOVES-2D makes this vacuous, not false. μ(d) ≤ T^R(d) ≤ 3 + (2d − 2)·μ(d) and «μ polynomial iff T^R polynomial» do
      not use MOVES-2D. A kill μ(6) ≥ 13, μ(8) ≥ 21 contradicts neither (it gives T^R(6) ≥ 13, T^R(8) ≥ 21).
  - In «Does NOT claim» lists: l. 94 and l. 177 («(7 ≤ 2d = 8)» is a true remark about one instance).
  - As status labels, not signed statements: l. 9 «CONJECTURE MOVES-2D … stay OPEN», l. 77-78 «(lane, box 181, OPEN)», and l. 198
    EXCLUDED.
  - l. 202 «equivalence of two open bounds» refers to «μ polynomial» and «T^R polynomial» (entry 1's W-1 note), not to MOVES-2D.
  - No DATA counter measures MOVES-2D (movescheck.py has no such counter), so no DATA clause changes either.
- If two replays confirm the kill, these texts become false or misleading at landing and need relabelling:
  - in the line: «(the open conjecture MOVES-2D) would give …» and «MOVES-2D is not claimed (it is an open conjecture; …»;
  - in the packet: the status labels l. 9 and l. 78 (a fixes-entry note; the packet is frozen).
  - The sufficiency clause would then be vacuous, so L-4 should not present MOVES-2D as a route.
  - «its necessity is not shown» stays true.
- Agreed with the Lead's reading: none.
