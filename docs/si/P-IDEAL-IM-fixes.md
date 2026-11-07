# P-IDEAL-IM fixes
Fixes to the frozen packet docs/si/P-IDEAL-IM.md (claude/l-si cb2b0c60, sha1 7bef9419…). The packet file is not edited. Each entry
lists the referee item, the change, and where it lands. L-SI successor 40, 2026-11-06 (date -u: see the commit). Lead fix round 1
(21:47Z).

## Entry 1 (both referees: REFEREE 24, claude/referee 0e24d8ca, docs/referee/R-P-IDEAL-IM.md; REFEREE-2 28, claude/referee-2,
docs/referee-2/R2-P-IDEAL-IM.md, draft 7856e7a9)
| item | referee | change | lands in |
| --- | --- | --- | --- |
| IM-G1 (required) | REFEREE | the sentence F-1 below, added to the proof of Corollary COMPOSE-LB (§4) | this entry |
| IM-L2 (optional, taken) | REFEREE | the DATA clause separates the counts made once per state (IM, LOCAL, independence of s(z)) from those made per state and both c | line L-2 |
| W-1 | REFEREE-2 | the BIT-CHAIN count covers part (i) only; the line now says «BIT-CHAIN (i)» | line L-2 |
| W-2 | REFEREE-2 | the COMPOSE figures are re-measured with a named seed and command (F-2); the old figures 6,786 / 16,853 are withdrawn | line L-2, check75.sh |
| IM-L1 (optional, not taken) | REFEREE | the re-check addendum has not landed; nothing to cite yet | — |

### F-1 (IM-G1): the bit of H's frozen level 0 equals the given c
Inserted in §4, proof of Corollary COMPOSE-LB, after «Give H's level-0 movers both options with Ξ-target X, and choose the start so
that each takes its better option»:
- «Choose also the β ranks and gate indices of the four level-0 options as follows.
  - Their ranks are the four smallest, below every rank of K's and G's upper options, so the rank order of every upper option is
    unchanged.
  - Their gates are the four smallest, below every other gate, so the gate order of every upper option is unchanged.
  - Order them so that, for the start options q(0), q(1) of movers 0 and 1, g(0, q(0)) < g(1, q(1)) holds iff c = 1, i.e.
    b_0(q) = c (R110's definition of b_0).
  - By ISO the level-0 options lie on no Ξ-chain of an upper option, so the A-sets of the upper movers are unchanged.
  - Their gates enter the run of H on the levels ≥ 1 only through b_0 (R110 W-ONLY). R110's c-step does not read them at all (its
    level-1 keys are (κ^c_w, gate)), so K's c-step sequence is unchanged.
  - The movers 0 and 1 then never move (each is happy forever, both options' values being their own constant ε), so b_0 of every
    state of the run is b_0(q) = c, and R110 W-ONLY makes every step of H's IDEAL run the c-step with this c.»
- The rest of the proof is unchanged.
- REFEREE noted the achievability («level-0 gates and ranks are free, no W-role, ISO»); this sentence states it.

### F-2 (W-2): COMPOSE DATA, re-measured
- Command (from experiments/si/box68): `python3 compose.py 200 68` → «COMPOSE random pairs 200 KPART 0 GPART 0».
- Negative control: `NEG=1 python3 compose.py 200 68` → «COMPOSE random pairs 200 KPART 21234 GPART 54433».
- Both lines are now asserted verbatim by experiments/si/box75/check75.sh, so verify re-measures them.
- Other seeds (DATA, this entry): seed 1 gives 21,731 / 54,286 and seed 7 gives 22,088 / 55,603, inside the REFEREE-2 range of about
  18-24k / 46-60k. The packet's figures 6,786 / 16,853 (box 68 note) came from an unrecorded seed and smaller run, and are withdrawn.

### F-3 (W-1, IM-L2): the DATA clause checked against imcheck.py's counters
Line numbers are those of experiments/si/box75/imcheck.py.
- Per state and both c (lines 69-81): XSTEP (own c-step = box 64 simulator), MONO (VALUE-MONO), BITCHAIN (BIT-CHAIN (i):
  b_l = [key(A_l) < key(B_l)]; part (ii) is not counted separately; it enters KEY-DIR's prediction), KEYDIR.
- Once per state (line 83: `if c == 1: continue`):
  - FRAME_OWN (independence of s(z));
  - FRAME_LOCAL (IM (a));
  - IM (y unhappy and on a chain: (b) and (c)); its negative control counts (c) only, with the direction reversed.
  - FRAME_STEP compares the frame step with the c-step for both c2 ∈ {0, 1} (lines 97-108), once per state each.
- Line L-2 states exactly these scopes.

## Line
- docs/si/P-IDEAL-IM-line-L2.txt = line L-1 with exactly three replacements, made by script:
  - the DATA scope (F-3);
  - the COMPOSE figures (F-2);
  - the source note, which now names this fixes file.
