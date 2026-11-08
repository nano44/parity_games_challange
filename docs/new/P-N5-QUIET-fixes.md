# P-N5-QUIET fixes (append-only; the packet docs/new/P-N5-QUIET.md stays frozen)

## Fixes entry 1 (L-NEW successor 62; Lead 00:36Z: L-RED 56 R221 items 1-2 and the [OPT] reading)
- Report answered: L-RED 56 R221, docs/red/R221-quiet.md at claude/l-red d49b9f0c. Nothing BROKEN; LOC-GATE, CN2, LOC-K2, QUIET,
  T-QUIET, ASC-T, UP-T (under [E-LEV]) SURVIVE; constant IN-BOUND DEAD confirmed. Two GAPs, both ACCEPTED below.
- The packet (frozen at 9329859d) is unchanged; where this entry and the packet differ, this entry governs.

### G-1 (R221 §3): the tie case of (Q5). ACCEPTED; closed by Lemma B-ONLY (credit: L-RED R221 §3; proof re-derived here).
- The gap: (Q5) counts «G_C changes at most 2M times» and «a sub-window ends only at a flip, which needs a β-face change». Both need that
  a gate never flips while its faces tie, but R118 lets σ̄ be «any fixed deterministic choice», which may change at a tie.
- **Lemma B-ONLY (PROVED; L-RED R221 §3, re-derived).** In IDEAL-CYC(G), for every genome G, every state t and every vertex v other than
  c_W and the e-vertices whose successor is c_W, Λ_t(v) is less relevant than every e-vertex (it is a β-vertex, K1, K2 or the unused loop).
  Proof.
  - Let τ_β := «β-face at every gate, K1 at K2», a positional Odd strategy ([XICYC] (a): Odd is unrestricted at gates and K2).
  - Under (σ_t, τ_β) no gate sends to its e-face, and an e-vertex's only in-edge is from its gate ([DEF] used shape). So the play from a
    vertex v that is not an e-vertex contains no e-vertex; the play from an e-vertex e contains e only, as its first vertex, and reaches
    c_W only if e's successor is c_W (c_W's only in-edges are from level-0 e's and its own loop, [DEF]).
  - For v as in the statement, the cycle of that play therefore contains no e-vertex and not c_W. Its cycle node is then neither an
    e-vertex nor c_W, nor K0 or K3 (never cycle nodes: K0 → K3 → K2 frozen, nothing returns to K0), so it is less relevant than every
    e-vertex (E-DOM: only e-vertices, c_W, K0, K3 are more relevant than an e-vertex), and its reward is below every e-vertex's reward
    (every e-vertex is even, [DEF]: «e of even priority above every β»; a less relevant vertex has a smaller reward unless it is even
    and the other odd, which is not the case for an even e-vertex).
  - By [OPT], Ω_t(v) ⊴ v's value under (σ_t, τ_β). The order compares the rewards of the cycle nodes first ([VJ]), so reward(Λ_t(v)) ≤ the
    reward of that cycle node, which is below every e-vertex's reward. So Λ_t(v) is not an e-vertex and not c_W, and (being a cycle node,
    CN2, not K0, K3) it is less relevant than every e-vertex. ∎
- **Corollary NO-TIE (PROVED).** At every state and every gate g, Ω_t(e_g) ≠ Ω_t(β_g). So LOC-GATE applies at every gate and state.
  Proof. If e_g's successor is c_W, Λ(e_g) = c_W while Λ(β_g) ≠ c_W (B-ONLY): different. Otherwise Λ(e_g) is less relevant than e_g
  (B-ONLY), so e_g ∈ Π(e_g). Equal values need e_g ∈ Π(β_g): β_g's play passes g and then e_g, so it is β_g, …, g, e_g, followed by
  e_g's play, and k(β_g) > k(e_g): not equal. ∎
- Consequences for the frozen proof (no statement changes):
  - (Q5): «flips at most twice … (to a tie, then to e)» becomes «at most once (β to e)»; G_C changes at most M times; at most M + 1
    sub-windows; the stated L stays a valid (larger) bound.
  - (Q3): every class of a vertex other than c_W and the level-0 e's is a B-class; those exceptions have constant values ((c_W, ∅, 0)
    and (c_W, ∅, 1)). So (Q3) is vacuous and the term N(n − 1) of L is not needed; L stays a valid bound as stated.
  - CN2's «cycle node of priority ≥ 2» is unchanged; B-ONLY is stronger for every v other than the exceptions.
- DATA (L-RED's, quoted, not re-run here): «359,866 pairs, 0 with Λ at or above an e-vertex; 0 gate ties» (bonly221.py; unit (state,
  vertex) pairs; 170 runs; own.py). This entry's own counter: see «DATA added» below.

### G-2 (R221 §7): the Γ3 scope. ACCEPTED.
- The packet's Scope already says «nothing PROVED about N5′-xi on Γ3(G)» and gives the transfer only as a READING. This entry replaces
  that READING by the Lead's exact sentence, which governs:
  «T bounds IDEAL-CYC iterations; on Γ3 this bounds N5′-xi only up to its first fallback, and only under REACH3-CYC; nothing is claimed
  about post-fallback iterations, N5′-xi's total count, N5 or general games».
- Witnesses that the restriction is needed (L-RED R221 §7, frozen at claude/l-red d49b9f0c, experiments/red/r221q/inst/SHA1SUMS):
  DIV_2_493 (sha1 113a0e24…), DIV_2_583 (0302abaa…), DIV_3_717 (1e4c0d16…): N5′-xi on Γ3 changes movers after its first fallback
  (iterations 5, 4 and 7), and before it follows a different Howard run at exact VJ ties. L-RED's reading: QUIET uses only DOM and STRICT,
  which hold for every Howard tie rule that keeps a best current option, so T-QUIET covers that pre-fallback run too, PROVIDED
  REACH3-CYC's premises hold for the genome (READING, not claimed here).

### [OPT] source (Lead reading 00:36Z, for the referees)
- [OPT] is re-cited as RESULTS R57 (b)'s standing SPEC premise, quoted where R104 lands it (RESULTS l. 9975-9978): «that S1's procedure
  realises an optimal σ̄ is VJ00 §6 plus SPEC conformance», «used in two forms: S1's σ̄, and τ̄ on the dual game, are pointwise optima»;
  and R57 (b) itself (RESULTS l. 2915-2916 as quoted there): «that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC conformance,
  and the code's match to SPEC is DATA (R15 G-N5T-1) (1E-N3 = N-1E-1).» Optionally RESULTS R21 (a) (l. 933): «(Odd's best reply σ̄_k is
  pointwise optimal in G_{σ_k})». F3's proof is no longer cited as the source. The referees decide whether this covers IDEAL-CYC's σ̄_t.

### DATA added (this entry; tool experiments/new/box194/bonly194.py, run by check194.sh, output check194.out)
- B-ONLY: bonlyfail 0 in 297,192 (state, vertex) pairs (v not c_W and not an e-vertex whose successor is c_W; fail = Λ_t(v) an e-vertex or
  at least as relevant as the least relevant e-vertex). NO-TIE: ties 0 in 89,125 (state, gate) pairs.
- Set: rd3_d4 and RS2_L32M6 (box194/inst/), the 13 P-N5-ASC instances, 1,000 random genomes (rand191.rgen, seed 2: 236,134 pairs,
  68,549 gate-states). Scope: IDEAL-CYC (box191 idealcyc via box192 rpot192). Per-instance lines in check194.out.

### Machine checks after this entry
- check194.sh runs bonly194.py; check194.out regenerated (earlier lines unchanged); the check.sh block «BOX 194 LOC» also fails on
  bonlyfail or ties ≠ 0.
- quiet.pins: check194.sh, check194.out re-pinned; bonly194.py and this fixes file added. The packet's own sha1 is unchanged.

## Line L-1 (L-NEW successor 63; Lead brief: «write P-N5-QUIET's line L-1 by script»; written 02:23Z by date -u)
- docs/new/P-N5-QUIET-line-L1.txt, written by experiments/new/box194/mkl1_194.py (input: trunk 51eb6534's docs/RESULTS.md). One paragraph,
  no «|». Fixes entry 1 applied: B-ONLY (credit L-RED R221 §3) and NO-TIE as clauses; LOC-GATE stated with «strictly» (NO-TIE); the Lead's
  Γ3 scope sentence quoted verbatim (the script asserts it occurs once, verbatim, in this file); [OPT] cited as RESULTS R57 (b) as landed in
  R104 (the script asserts both quoted strings occur in RESULTS.md). Form after P-N5-ASC's L-2.
- DATA clauses re-read from check194.out. One correction against the packet's §7 wording: QUIET / T-QUIET ran on 10 of the 13 P-N5-ASC
  instances (all but cR_d2_w8_R22, rd3_d7, rf_d5), not on all 13; the line says so. No statement changes.
- quiet.pins: this file re-pinned; line L-1 and mkl1_194.py added.

## Fixes entry 2 (L-NEW successor 64; Lead 06:39Z: «L-2 = L-1 + QT-L1..QT-L6 exactly … D-1 and D-2 BY TOOL FIX»; written 06:59Z by date -u)
- Reports answered: REFEREE 28, docs/referee/R-P-N5-QUIET.md (claude/referee a233f356; §5 strings QT-L1..QT-L6, script
  scratch/quiet_linefix.py): every statement SIGN, L-1 NOT YET. REFEREE-2 33, docs/referee-2/R2-P-N5-QUIET.md (claude/referee-2
  17a85958) with Addendum 1 (11a7a911): CN2, LOC-GATE, LOC-K2, B-ONLY, NO-TIE, QUIET, T-QUIET, ASC-T SIGN, UP-T SIGN under [E-LEV], ASC-T
  and UP-T land after R121; L-1 NOT YET on W-1..W-3, D-1, D-2; Addendum 1 withdraws W-1..W-3 «in favour of QT-L4, QT-L1 and QT-L3, so
  as not to give L-NEW two strings for one span», accepts QT-L2, QT-L5, QT-L6, and reproduces fed89346… byte-exact. All ACCEPTED. The
  packet is unchanged; where entry 1 and this entry differ, this entry governs.
- Item → change (line L-1 → L-2 by experiments/new/box194/mkl2_194.py, strings copied verbatim from REFEREE 28's quiet_linefix.py; each
  old string asserted once in L-1, no overlap):
  - QT-L1 ([OPT]; = REFEREE-2 W-2): [OPT] re-cited as RESULTS R118's σ̄ as used in R118 (b) (P-N5-XICYC §3 l. 75 «σ̄_t is optimal at
    every vertex at once ([VJ])») and RESULTS R21 (a); R57 (b) concerns SPEC's S1 output and is not used. Entry 1's [OPT] paragraph (R57
    (b) via R104, Lead reading 00:36Z) is WITHDRAWN.
  - QT-L2: F2 added to the R118 (b) premise list.
  - QT-L3 (= REFEREE-2 W-3): [E-LEV] is a HYPOTHESIS (R104 (vi) leaves the e-priorities to its packet as immaterial to its results).
  - QT-L4 (= REFEREE-2 W-1): the Γ3 scope sentence OVERCLAIMED. Replaced in the line by REFEREE 28's sentence (nothing is proved on Γ3;
    the Γ3 run can differ from the IDEAL-CYC run at exact VJ ties; a Γ3 form of the proof is not given here). Entry 1 G-2's «governs» for
    that sentence is WITHDRAWN and the packet's own Scope wording («nothing PROVED about N5′-xi on Γ3(G)», packet §Scope) stands. The DIV
    witnesses stay. (Box 196, docs/new/N5-CHAIN-box196.md, gives a Γ3 form separately; it is not part of this packet.)
  - QT-L5: the random set's generator parameters (d 1-6, w 1-3, degree 2-3). QT-L6: CN2's DATA scope ((σ_t, σ̄_t) pairs only).
  - D-1 (REFEREE-2; REFEREE 28 «OK. Note»): BY TOOL FIX (a). quiet194.py: L = (M+1)(2M+1)(N+1) + N(n−1) (the «+ 1» dropped) and wfail
    counts each quiet window once (when it first exceeds L), so the line's «wfail 0 (unit: quiet windows)» and «Tfail … T > Q + (Q + 1)L»
    are what the tool tests. Re-run (check194.sh, check194.out regenerated): wfail 0, Tfail 0, crossflip 0 on every QUIET run as before;
    the only diff is each printed L one smaller (12 lines). No line string.
  - D-2 (REFEREE-2; REFEREE 28 «OK»): BY TOOL FIX. loc194.py's k2fail now counts states with σ̄_t(K2) ≠ K1 OR not Ω_t(K1) ◁ Ω_t(K2)
    (both conjuncts of LOC-K2). Re-run: k2fail 0 on every run (check194.out's loc194 lines unchanged). No line string.
- Line: docs/new/P-N5-QUIET-line-L2.txt = L-1 + QT-L1..QT-L6: sha1 fed893462811ea10d0b99622dcbb31f7b50b6d47, 5,131 B = the prediction of
  both referees (the script asserts it; no adjustment). Form B is NOT in the line (Lead 06:39Z: neither referee tested it); the line's
  QUIET DATA clause keeps «10 of the 13 instances (all but cR_d2_w8_R22, rd3_d7, rf_d5)».
- Form B, DATA only (not in any line): experiments/new/box194/formB194.out, quiet194.py after D-1 on the three instances outside QUIET's
  DATA set: cR_d2_w8_R22 (W 0, N 16), rd3_d7 (W 4, N 14), rf_d5 (W 0, N 10): wfail 0 (unit: quiet windows), Tfail 0 (unit: runs),
  crossflip 0 (unit: σ̄ flips). With these, QUIET holds on all 13 P-N5-ASC instances (DATA).
- Superseded: experiments/new/box194/draft_entry2/ (NOT ROUTED draft of successor 63) is history only; its L2_QT_only.txt equals L-2.
- quiet.pins: loc194.py, quiet194.py, check194.out and this file re-pinned; line L-2, mkl2_194.py and formB194.out added. check.sh block
  «BOX 194 LOC» unchanged (its grep lines still hold).
