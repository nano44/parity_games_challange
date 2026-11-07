# R2-P-IDEAL-MOVES: second-referee report on packet P-IDEAL-MOVES (L-NEW successor 57, box 187)
REFEREE-2 successor 29 (Opus 5.5, D1/D18/D20). Written 2026-11-06 23:1xZ to 23:3xZ (date -u). Independent: docs/referee/ not read
for this packet before this push. Stale-clone check at start (23:04Z): ls-remote claude/referee-2 = 280d2313 = local after ff-only
(the clone was detached, 113 behind); not shallow after fetch --unshallow; 2 ahead / 178 behind trunk 09476aba, merged (no rebase).

## Object
- claude/l-new d86adc86 (ls-remote at 23:04Z and 23:10Z: unchanged). Re-hashed at d86adc86, all match the brief:
  docs/new/P-IDEAL-MOVES.md sha1 5ce2947d1ee4dab317e5c06446b38f050146cafb, 202 lines; docs/new/P-IDEAL-MOVES-line-L1.txt
  819c58159100d77ec509348345cfd1a641a6f9e7, 1 line; experiments/new/box187/movescheck.py 8153717b8596…, movescheck.out 4874020973e0…;
  box186/out/pass_d3_D3.json 8bca9764…, pass_d4_D4.json 3bf6a4a4…, pass_d5_D5.json 16be2e59…, box187/inst/m4_z4_r7.json 7c158e2f…
  (= l-red 4b61200d:experiments/red/r213/out/m4_z4_r7.json, sha1 re-measured; 4b61200d is an ancestor of claude/l-red).

## Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §1 | Lemma REDUCE-XI | **SIGN** (Opus 5.5, D1) |
| §1 | Corollary MOVES-EQUIV (incl. MOVES-2D ⇒ T^R(d) ≤ 4d² − 4d + 3) | **SIGN** (Opus 5.5, D1) |
| §2 | Lemma AND-GATE (a), (b), (c) | **SIGN** (Opus 5.5, D1) |
| §3 | Lemma WINDOW-DOUBLE (a), (b) (incl. BURST-2) | **SIGN** (Opus 5.5, D1) |
| §4 | Lemma SEG-WINDOW (a), (b), (c), (d), (e) | **SIGN** (Opus 5.5, D1) |
| §5 | DEAD-SEG (c ≤ 4; pass_d3/d4/d5) | **SIGN** (Opus 5.5, D1) (recomputed by my own simulator) |
| §5 | DEAD-LEV (m4_z4_r7) | **SIGN** (Opus 5.5, D1) (recomputed by my own simulator) |
| line | L-1 | **MATCHES after W-1, W-2** (W-1 required: scope of «equivalent»; W-2 required: an ambiguous antecedent) |
No statement is REFUSED. No gap is listed: every proof is complete from the landed premises and R104's definition.
§6 (DATA / READING) is not signed; its DATA attribution notes D-1..D-3 below are wording only.

## Premise route (landed RESULTS only; docs/lit and lane files not used)
- Every «…» quote of the packet's premise list (16 quotes: R105 ENC, LOCAL, MONO, XI-NEW, RISE and «at any degree»; R110's 𝓛^R_d;
  R113 ALIGN, F0 and its four notations) and the two quotes inside §1 and §4 were matched by script against docs/RESULTS.md at trunk
  b876c884, whitespace-unwrapped: 18/18 verbatim. Each sits in the named entry: R105 l. 10155 (XI-NEW, RISE, ENC, LOCAL, MONO all
  before «and at degree ≤ 2 only», so at any degree and «any number of movers per level»); R110 l. 11323; R113 l. 12152.
- RESULTS Erratum E-2 corrects R105's CHAINED binder, TOP-MONO's RANK_t and KEYFLIP's moves(x) (RESULTS l. 10916 wording); the packet
  uses none of those. moves(x) is defined in §0 directly as #{t : x ∈ Mv_t}. ✓
- R104: §0's step rule matches R104 l. 9864 «an IDEAL step moves every mover to the lexicographically least key (gate indices of the
  chain of W-targets under the new state, lowest level first) among its current option and the options with a strictly better Ξ-value,
  and the run stops when nothing is available or nothing changes». ✓ No R104 theorem used. ✓
- T^R(d) is R110's «the largest number of steps over 𝓛^R_d and all starts» (R110 is stated on acyclic Ξ-graphs). Lead reading L49
  (T^R_ISO vs T^R) does not bear: MOVES-EQUIV is about T^R over all of 𝓛^R_d and uses no FLIP-ADD or W-ONLY. ✓
- Dependency order: §1 ← R105 XI-NEW/RISE, R113 F0; §2 ← R104 def, R105 ENC/MONO; §3 ← R113 ALIGN, F0; §4 ← §2, §3, R105 LOCAL,
  ALIGN, F0. No cycle, no unlanded premise (R114 / P-IDEAL-RISE not used; R111 CASCADE not used). ✓

## Proof checks (own re-derivation, line by line)
- **REDUCE-XI.** For 2 ≤ t ≤ T a least-level mover h of step t exists (Mv_t ≠ ∅); RISE gives a strict Ξ-descendant y on h's chain
  moving at t − 1; y is the Ξ-target of the last edge of the path, so y ∈ Z. Injectivity of t ↦ t − 1 gives T − 1 ≤ #{t ≤ T − 1 :
  Mv_t ∩ Z ≠ ∅} ≤ Σ_z moves(z). T ≤ 1 trivial. ✓ (RISE is used only for its existence clause; XI-NEW is only its antecedent.)
- **MOVES-EQUIV.** Lower: moves(z) ≤ T. Upper: REDUCE-XI with Z split by level; level-0 movers of Z contribute ≤ 2 (F0), the ≤ 2d − 2
  movers of level ≥ 1 contribute ≤ μ(d) each. 3 + (2d − 2)·2d = 4d² − 4d + 3. ✓ «μ polynomial iff T^R polynomial»: from the two
  inequalities. ✓ (μ(1) := 0 is consistent: at d = 1, T ≤ 1 + 2 = 3.)
- **AND-GATE.** (a) π well defined (β(x, k) is on the chain of (x, k) and, by acyclicity, not on the other chain), so at degree 2 A =
  {s(x)} or both options, the latter iff s(x) ≠ π; then x takes the key-least option under s_t, which is KP_(s_t)(x) (option keys are
  distinct: their last entries are distinct gates). ✓ (b) both endpoints of the windows are correctly placed; disjointness of [t_i,
  t_(i+1) − 1] and of [t_i + 1, t_(i+1)] gives PF_x, KF_x ≥ M − 1. ✓ (c) v(x, a) = ε(x, a) + current value of xt(x, a) is
  non-decreasing by ENC + MONO (MONO at any degree, so xt(x, a) may have any degree); strict at both ends. ✓
- **WINDOW-DOUBLE.** (a) If neither of p, q moves and both sit on one option, ALIGN's order is γ_j(i) before and after; so they are on
  different options, Φ = 1, and the order [s(p) = c_j(s)] can change only if c_j changes, i.e. only if the pair j − 1 flips (c_j(s) is
  read off the order of the current keys of 2j − 2, 2j − 1, which is exactly what R113's flip tracks). ✓ (b) Φ′ bookkeeping, ALIGN's
  «moves to option c_l(s_t)», the telescoping sum and h(0) = 2, h(1) = 1, h(2) = −2 all re-derived; the j-b-steps in W are F_W(j − 1)
  many by definition. ✓ (BURST-2 is the case F_W(j − 1) = 0.)
- **SEG-WINDOW.** (a) AND-GATE (b) on the consecutive moves t − 1, t puts a KP change at t; ALIGN KP = c_l; c_l changes iff (u, w)
  flips. ✓ (b) the descent uses §3 (a) at levels l − 1, …, 1 (each ≤ d − 2, so §3's j ≤ d − 1 holds) and the gate-key argument at level
  0. ✓ (c) §3 (b) with j = l − 1 and the same W = [a + 1, b] (needs a < b; D = 1 is trivial). l = 1 by F0. ✓ (d) any W ⊆ [a + 1, b] of
  consecutive steps is a §3 window; (a) makes every step of W a flip of pair l − 1; BURST-2 gives |W| ≤ 2. ✓ (e) AND-GATE (b) on
  moves t, t + 1 puts the π change at t; AND-GATE (a) at t + 1 gives b = π_(s_t)(x) = s_(t+1)(x); AND-GATE (c) the strict rise; if no
  y_i (i ≥ 1) moved at t the chain of (x, b) and its β-set are the same under s_t (this is the definition; LOCAL is the same fact);
  y_i ≠ x by acyclicity. ✓
- **DEAD-SEG / DEAD-LEV.** Arithmetic: 3 > 0 + 2, 4 > 0 + 3, 5 > 0 + 4; 7 > 6 = 2(2 + 1), and 7 ≤ 1 + F(1) ≤ 1 + 2F(0) + 2 ≤ 7
  (R113 MOVES / PAIR-DOUBLE / F0: consistent, and tight; F-4). The killed conjecture is stated only for c ≤ 4 (not «O(1)»), as the
  packet says. ✓

## Machine checks (own code; outputs in docs/referee-2/R2-P-IDEAL-MOVES/)
- **Own simulator** r2moves.py (sha1 9e45a9f4…, written from R104's text: β-SETS compared by the top β of the symmetric difference,
  integers only for v; no lane code imported). On the frozen corpus of l-new d86adc86 (same selection rule as movescheck: L^R_d genome
  files under box150-box187, every start for N ≤ 10, stored start otherwise): **208 files, 63,223 runs, 140,395 steps, 225,917
  segments, 1,288,162 windows, max D 9** — every count equal to movescheck.out. cmpgen.py: my run = the lane's box150 Gen run on all
  63,223 runs (0 mismatches), run-hash 9dae285766bf.
- **Counters (0 = no violation), corpus and 300 random acyclic L^R_d genomes (d 2-6, seed 29, 85,440 runs):** RX1 (per-step form) 0,
  RX2 (T ≤ 1 + #{t ≤ T − 1 : Mv_t ∩ Z ≠ ∅}) 0, RX3 (T ≤ 1 + Σ moves) 0, MEQ (per run, T ≤ 3 + (2d − 2)·max_(z ∈ Z, lev ≥ 1) moves(z))
  0, F0 0, AGA (both sentences of (a)) 0, AGB 0, AGBm (moves ≤ 1 + min(KF, PF)) 0, AGC 0, WDA (§3 (a), on 31,212 flips with no move of
  the pair) 0, WDB 0, WB2 0, SWA 0, SWB1 0, SWB2 0, SWC 0, SWD (§4 (d) on every sub-window) 0, SWE1 (π change at t to s_(t+1)(x)) 0,
  SWE2 (strict rise) 0, SWE3 (chain mover ≠ x) 0. (Random genomes are shallow: max D 2 there; the corpus carries the depth.)
- **Negative control** (--neg, keys under the OLD state): RX1 9,670, RX3 1,325, AGA 135,567, AGB 15,285, SWA 8,933, SWB1 8,371, SWB2
  6,763, SWC 4, SWD 4: the key-side counters are live. (Value-side counters AGC, SWE* stay 0, as they should: they do not use keys.)
- **DEAD instances recomputed by my simulator** (all R110-wired, distinct gates/ranks, Ξ-acyclic, mover in Z):
  pass_d3_D3 start 110100: mover 5 (level 2) moves at [1, 2, 3], T 4, LM 0; pass_d4_D4 start 01010111: mover 7 (level 3) at [1..4],
  T 4, LM 0; pass_d5_D5 start 0101010110: mover 9 (level 4) at [1..5], T 5, LM 0; m4_z4_r7 stored start 10111010: mover 4 (level 2)
  moves 7 times (steps 1, 2, 3, 5, 6, 7, 8), T 8. All equal to movescheck.out. Under --neg the instances do not reproduce (the
  instances depend on the new-state key rule, as they must).
- **check.sh block «P-IDEAL-MOVES»** run in an archive of d86adc86: «… instances 8bca9764 3bf6a4a4 16be2e59 7c158e2f: PASS», exit 0
  (blk187.out).

## DATA rule (every signed clause: a counter or a no-DATA entry) — movescheck.py counter code read
- RX: per-step form and the Σ-inequality; the middle inequality is implied by the per-step form, not counted separately (D-1).
- AGA: (a)'s iff; (a)'s second sentence implied at degree 2. AGB: (b)'s first sentence; «Hence moves(x) ≤ 1 + min(KF_x, PF_x)» has
  neither counter nor no-DATA entry (D-2). AGC: (c). ✓
- WPD = WINDOW-DOUBLE (b); SWD = BURST-2 on maximal flip-free windows of pair j − 1 (sufficient: sub-windows inherit). The tool's
  docstring labels SWD «SEG-WINDOW (d) BURST-2», the packet §6 assigns it to WINDOW-DOUBLE: label mismatch, harmless (D-3). (a): no-DATA
  entry ✓.
- SWA/SWB/SWC/SWE = SEG-WINDOW (a)/(b)/(c)/(e), on every segment; SWE checks only (e)'s chain-mover clause; (e)'s «π(x) changes at t
  and the value rises strictly» is covered only through AGB + AGC (D-2). (d): no-DATA entry ✓. MOVES-EQUIV: no-DATA entry ✓.
- D-1..D-3 are attribution notes on §6 (not signed); my counters RX2, AGBm, SWE1, SWE2, WDA, SWD, MEQ fill each of them: 0 violations.
  No fix is required for signing.

## L-1 (diffed clause by clause against the packet)
- Premise list, notation, REDUCE-XI, AND-GATE, SEG-WINDOW (a)-(e) as listed, both DEAD items and the DATA parenthetical (counts equal to
  movescheck.out; «first three clauses and its last one» = SWA, SWB, SWC, SWE in L-1's clause order) match the packet. ✓
- **W-1 (required).** L-1: «MOVES-2D is not claimed (it is an open conjecture, here shown equivalent up to a factor 2d − 2 to a
  polynomial bound on T^R)». The packet shows μ(d) ≤ T^R(d) ≤ 3 + (2d − 2)μ(d) and MOVES-2D ⇒ T^R(d) ≤ 4d² − 4d + 3; MOVES-2D (μ ≤ 2d)
  is not equivalent to a polynomial bound on T^R (a polynomial T^R gives only μ polynomial). Replace by: «MOVES-2D is not claimed (it is
  an open conjecture; here μ(d) is shown equal to T^R(d) up to a factor 2d − 2 and an additive 3, so MOVES-2D is sufficient, not
  necessary, for a polynomial bound on T^R)».
- **W-2 (required).** L-1 WINDOW-DOUBLE: «… is a step at which the pair (2j − 2, 2j − 1) flips while the two movers are on different
  options» — «the two movers» reads as 2j − 2, 2j − 1. Replace by «… flips while 2j and 2j + 1 are on different options before the
  step».
- W-3 (optional). SEG-WINDOW last clause: «… some mover other than x on the chain under s_(t−1) of the option x takes at t + 1 moves»
  → «… moves at t».

## Findings
- F-1: all statements SIGN; no gap.
- F-2: L-1 MATCHES after W-1, W-2.
- F-3: §6 DATA attribution notes D-1..D-3 (not signed; filled by my counters, all 0).
- F-4: DEAD-LEV is tight for R113 MOVES + PAIR-DOUBLE + F0: a level-2 mover moves ≤ 1 + F(1) ≤ 1 + 2F(0) + 2 ≤ 7 on every 𝓛^R_d
  genome, and m4_z4_r7 attains it (my simulator: F(0..3) = 2, 6, 5, 4).

## Addendum 1: fix round 1 (claude/l-new 9995f5a2; REFEREE-2 successor 29, 2026-11-06 23:5xZ by date -u)
- Object: docs/new/P-IDEAL-MOVES-fixes.md entry 1 sha1 e933f4d3b42e…, 4,635 B; docs/new/P-IDEAL-MOVES-line-L2.txt sha1 f3692aaa0335…,
  4,495 B, 1 line, 71 «(» = 71 «)», depth never negative, 0 «|»; packet 5ce2947d and L-1 819c5815 unchanged. git diff d86adc86..9995f5a2
  touches only those two files and experiments/new/check.sh (pins).
- Byte test (own script): each of the five old strings R1-R5 occurs exactly once in L-1; L-1 with R1-R5 applied == L-2 byte for byte. ✓
- R1 = my W-1 text verbatim ✓. R2 = W-2 ✓ («before the step» = s_(t−1), as packet §3 (a)). R3 («moves at t;») is what W-3 meant ✓.
  R4 «(the min bound by arithmetic)»: true, moves(x) ≤ 1 + min(KF_x, PF_x) follows from the AGB pairs as in AND-GATE (b)'s last
  sentence (my AGBm counter: 0) ✓. R5 source note ✓.
- Entry 1's W-1 note is right: the packet itself (§1 l. 90-91, «μ is bounded by a polynomial in d iff T^R is») does not overclaim; only
  L-1 did. The §6 l. 202 wording note («two open bounds» = «μ polynomial» and «T^R polynomial») is correct. D-1..D-3 unchanged, as I
  said none was required. DATA unchanged (tool, output, instances unchanged).
- check.sh block «P-IDEAL-MOVES» at 9995f5a2 (archive): «… fixes e933f4d3, line L-2 f3692aaa: PASS», exit 0 (blk187_fr1.out).
- Verdict: fixes **CORRECT**; **L-2 MATCHES** the packet with fixes entry 1 (Opus 5.5, D1). Statement verdicts unchanged (all SIGN).

## Addendum 2: fix round 2 (claude/l-new d7b96be8; REFEREE-2 successor 29, 2026-11-07 00:4xZ by date -u)
- Object: docs/new/P-IDEAL-MOVES-fixes.md sha1 8d6223a2fe19…, 7,238 B; its first 4,635 B are byte-identical to entry 1 (e933f4d3), so
  the file is append-only ✓. docs/new/P-IDEAL-MOVES-line-L3.txt sha1 d3983c68cdda…, 4,567 B, 1 line, 71 «(» = 71 «)», depth never
  negative, 0 «|». git diff 9995f5a2..d7b96be8 touches only these two files and the check.sh pins.
- Byte test (own script): R6 and R7 each occur exactly once in L-2; L-2 with R6, R7 applied == L-3 byte for byte ✓.
- **MV-C1: I agree; it corrects my miss.** My W-1 text «sufficient, not necessary» claimed non-necessity, which the packet does not
  prove (MOVES-2D is open; were it true, it would be necessary for anything trivially). R6 says only what §1 proves: MOVES-2D ⇒ T^R(d)
  ≤ 4d² − 4d + 3, and a polynomial T^R gives only μ polynomial (μ(d) ≤ T^R(d)) ✓. R7 source note ✓.
- check.sh block «P-IDEAL-MOVES» at d7b96be8 (archive): «… fixes 8d6223a2, line L-2 f3692aaa, line L-3 d3983c68: PASS», exit 0
  (blk187_fr2.out).
- Verdict: entry 2 **CORRECT**; **L-3 MATCHES** the packet with fixes entries 1-2 (Opus 5.5, D1). Statement verdicts unchanged.
- On the L-LOWER 3 CANDIDATE kill of MOVES-2D (not replayed by me; noted only): **no signed statement depends on MOVES-2D being open**.
  MOVES-EQUIV's «MOVES-2D implies T^R(d) ≤ 4d² − 4d + 3» is an implication, true whether MOVES-2D is true or false (vacuous if false);
  μ(d) ≤ T^R(d) ≤ 3 + (2d − 2)μ(d) and «μ polynomial iff T^R polynomial» do not mention MOVES-2D. DEAD-LEV's «Does NOT claim: anything
  about MOVES-2D» stays true. Only status remarks would change: packet header/§0 «CONJECTURE MOVES-2D … OPEN» and L-3's «(it is an open
  conjecture; …)». The candidate numbers are consistent with the packet: μ(6) = 13 and μ(8) = 21 are far below the R113 bound, and the
  packet's DATA (d 5: 9 ≤ 10) is not contradicted.

## Addendum 3: fix round 3 (claude/l-new fd5c163f; REFEREE-2 successor 29, 2026-11-07 01:5xZ by date -u)
- Object: docs/new/P-IDEAL-MOVES-fixes.md sha1 510152dab351…, 9,674 B; its first 7,238 B are byte-identical to entries 1-2 (8d6223a2):
  append-only ✓. docs/new/P-IDEAL-MOVES-line-L4.txt sha1 73c16d1e2b00…, 4,598 B, 1 line, 71 «(» = 71 «)», depth never negative, 0 «|».
  git diff d7b96be8..fd5c163f: the two files above, check.sh pins, notes/L-NEW.md and box 188 (N5-KILLREPLAY, replay.py, logs; no
  genome JSON, and box188 is outside movescheck's 150-187 corpus anyway). Packet, L-1..L-3, tool, output, instances unchanged.
- Byte test (own script): R8, R9, R10 each occur exactly once in L-3; L-3 with R8-R10 applied == L-4 byte for byte ✓.
- Meaning: L-4 contains no «open» and no status claim on MOVES-2D; «(the lane conjecture MOVES-2D, not claimed here)» and «(its status
  is not part of this result; …)» are true under either outcome of the L-LOWER candidate; the implication «would give T^R(d) ≤ 4d² −
  4d + 3» stays true (vacuous if MOVES-2D is false) ✓. Entry 3's wording note (packet l. 9, l. 77-78 «OPEN» labels superseded) is
  consistent with my Addendum 2 (only status remarks depended on it) ✓.
- Note: the brief cites Lead ruling L50 at trunk 6ca995ed. At 01:5xZ that object is on no ref of origin (all heads fetched); trunk is
  fc665614 and has no «L50» in docs/DECISIONS.md or DECISIONS-INDEX.md. Entry 3 itself cites a «Lead reading, 01:16Z». I did not open
  L50; the verdict does not depend on it (L-4 is correct with or without it).
- check.sh block «P-IDEAL-MOVES» at fd5c163f (archive): «… fixes 510152da, line L-2 f3692aaa, line L-3 d3983c68, line L-4 73c16d1e:
  PASS», exit 0 (blk187_fr3.out).
- Verdict: entry 3 **CORRECT**; **L-4 MATCHES** the packet with fixes entries 1-3 (Opus 5.5, D1). Statement verdicts unchanged (all SIGN).
- Post-note (02:1xZ): L50 is now on origin at trunk 6ca995ed (docs/DECISIONS.md l. 440, index row l. 45), opened. Its (2) «P-IDEAL-MOVES
  lands with a line that makes no status claim about MOVES-2D (fix round 3, L-4). Its signed items do not depend on MOVES-2D (both
  referees, 2026-11-07).» agrees with L-4 and with my Addendum 2. Addendum 3's verdict stands.

## Addendum 4: fix round 4 / L-5 for CHECKER C129 (claude/l-new 571c75c5; REFEREE-2 successor 30, 2026-11-07 03:5xZ by date -u)
- Object (sha1 of the bytes at 571c75c5, equal to the Lead's relay 04:00Z): docs/new/P-IDEAL-MOVES-line-L5.txt a42257cb159b…, 4,750 B;
  P-IDEAL-MOVES-fixes.md fba3443ac0d7…, 12,899 B (entry 4); L-4 73c16d1e… unchanged. Source of R1-R3: docs/checker/C129.md at claude/checker
  a1963575 §5.
- Byte test (own script R2-P-IDEAL-MOVES/bt_l5.py, output bt_l5.out): each of R1, R2, R3's old strings occurs exactly once in L-4 and each
  new string once in L-5; L-4 with R1-R3 applied == L-5 byte for byte, sha1 a42257cb159b2e51128c2334062d44edb97661f6, 4,750 B (= C129 §5's
  computed sha1); 1 line, 74 «(» = 74 «)», depth never negative, 0 «|» ✓.
- Meaning, measured with my own simulator (R2-P-IDEAL-MOVES/r2l5.py on r2moves.py class G; output r2l5.out; no lane code):
  - R1 (E-1): on the 63,223 corpus runs, T = 1 + #{t ≤ T − 1 : Mv_t ∩ Z ≠ ∅} holds on 59,502 and T = 1 + Σ_(z ∈ Z) moves(z) on 8,399 ✓
    (both C129 numbers). The first form is the one REDUCE-XI's statement in L-5 states («for 2 ≤ t ≤ T step t − 1 moves a member of Z»),
    so «equality … on 59,502» is now named by its own equation ✓.
  - R2 (E-2): pass_d3_D3.json (8bca9764) from 110100 and pass_d4_D4.json (3bf6a4a4) from 01010111 give T 4 (D 3, 4, LM 0 as in my
    r2moves.out DEAD lines); from their stored starts 000000 / 00000000 both give T 2. So the instance is reproducible only with the start
    named, as R2 does ✓.
  - R3 (N-1): m4_z4_r7.json is run from its stored start 10111010 (my r2moves.out DEAD line «start 10111010 … T 8 moves 7 … LM 6») ✓.
    The cited path experiments/red/r213/out/m4_z4_r7.json is on claude/l-red (sha1 7c158e2f…, byte-equal to experiments/new/box187/inst/
    m4_z4_r7.json), not on trunk 3c428cde; the path is unchanged since L-4 (not new in this round).
- Entry 4 quotes C129 E-1, E-2, N-1 correctly and changes no statement, proof, tool, output or instance ✓.
- Verdict: entry 4 **CORRECT**; **L-5 MATCHES** the packet with fixes entries 1-4, in bytes and in meaning (Opus 5.5, D1). Statement
  verdicts unchanged (all SIGN).
