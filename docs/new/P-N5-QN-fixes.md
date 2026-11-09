# P-N5-QN fixes (append-only; the packet docs/new/P-N5-QN.md stays frozen at l-new e252182d, sha1 97254bd2a97f28bb0c14ab5f4d236ee723821dd9)

## Fixes entry 1 (L-NEW successor 69; Lead 10:11Z «go»: «P-N5-QN fixes entry 1 + L-1 first»; written 2026-11-09T10:11Z by date -u)
- Reports answered (read only, not edited):
  - REFEREE 30, docs/referee/R-P-N5-QN.md at claude/referee 452800c5: every statement SIGN, no GAP; QN-1; line requirements LN-1..LN-8.
  - REFEREE-2 35, docs/referee-2/R2-P-N5-QN.md at claude/referee-2 5d4f06c2: every statement SIGN, no GAP; W-1 and R-1 ((k+1)-Λ's
    wording), GATE-FLIP (b) «under HYPOTHESIS [E-LEV]», QUIET-N «sharpens R123», the DATA rule, and the DSALT6 window record.
  - L-RED 63, docs/red/R229-box203.md Addendum B at claude/l-red f05b0c55: CLEAN; G1, G2, G3.
- No statement, no proof and no label changes. Where this entry and the packet differ, this entry governs. Every item is ACCEPTED.

### QN-1 (REFEREE) = W-1 / R-1 (REFEREE-2): the values in Lemma (k+1)-Λ. ACCEPTED; one merged sentence governs §5's statement.
- The defect, read the same way by both referees: §5's statement says the values are «K1, and the most relevant vertex of each cycle of
  the functional graph Ξ_σ on the movers». Read literally, that names a mover (a cycle of Ξ_σ has movers only). A mover is never a cycle
  node (R123 CN2). The value that occurs is the most relevant vertex of the Γ(G)-cycle through that Ξ_σ-cycle. The proof already says so
  («Z with w is determined by that cycle»). The count k + 1 and the proof are unaffected.
- Governing statement of §5 (one sentence; REFEREE-2's required wording, which states REFEREE's correction):
  «For every genome G with Ξ-feedback number k and every state t of IDEAL-CYC(G), the cycle nodes Λ_t(v), over all vertices v other than c_W, c_X and the e-vertices whose successor is c_W, take at most k + 1 values: K1, and, for each cycle of the functional graph Ξ_σ on the movers, x → xt(x, σ_t(x)), the most relevant vertex of the Γ-cycle through its movers, their chosen gates and β-faces; Ξ_σ has at most k cycles.»
- Options whose Ξ-target is X are omitted from Ξ_σ as in §5. That most relevant vertex is a β (β's outrank movers and gates; REFEREE-2
  §(k+1)-Λ). The line carries this sentence verbatim (LN-2, R-1).

### GATE-FLIP (b) and QUIET-N in the line (REFEREE-2 «For the line»). ACCEPTED.
- GATE-FLIP (b)'s U(G) form carries «under HYPOTHESIS [E-LEV]», with [E-LEV] spelled as in landed R123's UP-T. QUIET-N carries «sharpens
  RESULTS R123 Theorem QUIET / Corollary T-QUIET» and its form T_CYC ≤ Q + (Q + 1)·N.

### DSALT6 window (REFEREE-2 DATA, «a record only»). NOTED.
- DSALT6_n108's longest quiet window: 10 on the lane engine (box203/out/gfc203_corpus.out row DSALT6_n108, «maxquiet 10 N 108»), 11 on
  REFEREE-2 35's engine. Both ≤ N = 108, as QUIET-N requires. Howard's tie rule is free in R118 (a), and the windows depend on it. The
  line names both values.

### LN-1..LN-8 (REFEREE §7). Each ACCEPTED; how L-1 meets it.
- LN-1: L-1 states GATE-CLASS, GATE-FLIP (a) and (b), QUIET-N and (k+1)-Λ, each labelled by its role (Theorem / Corollary / Lemma) with
  the scope IDEAL-CYC, every genome; GATE-FLIP (b)'s U(G) form under HYPOTHESIS [E-LEV]; DEAD D1-D3 with their instances and sha1s.
- LN-2: (k+1)-Λ in the governing sentence above.
- LN-3: premises by R-id only: R104 definitions of the genome and of Γ(G) only; R118 (a), (d) BR-SEG, (e) with its stated reason, R118's
  order ⊴ (VJ00 §4.2 / Friedmann arXiv 1106.0778 §3) and step labels C / R / p; R121 E-MON, and for GATE-FLIP (b) only R121 HUB-ASC-G's
  whole-run form and UP-B; R123 CN2, B-ONLY, NO-TIE, LOC-GATE, LOC-K2; R123 QUIET and T-QUIET are the bounds QUIET-N sharpens. No lane
  packet, no L-RED or L-SI lemma, no P-N5-CHAIN fact.
- LN-4: the «Against R123» remark «R123's ASC-T and UP-T hold with L + 1 replaced by N + 1» is OMITTED from L-1 (not in «To sign»; not
  signed). In this file it stays a READING.
- LN-5: lam203.py skips genomes with k > 12 for its lfail counter (lam203.py l. 4-5 and the `isinstance(k, int)` test; fvs202.kfvs
  returns «>12» above its cap). The packet's §9 did not say so. MEASURED (new tool experiments/new/box203/skip203.py, which replays
  lam203.py --rand's genome stream exactly, without the IDEAL-CYC run; output box203/out2/skip203.out): **0 skipped** on each of the three
  sets. Unit: genomes. rand191 seed 2: 1,000 genomes, k ∈ {0, …, 5} (71 / 453 / 332 / 115 / 28 / 1); k = 1 set seed 7: 2,000 genomes, all
  k = 1; k = 2 set seed 8: 1,000 genomes, all k = 2. So lam203's lfail 0 covers every genome of the three sets. L-1's (k+1)-Λ DATA clause
  says this.
- LN-6: scope IDEAL-CYC only; nothing on Γ3, N5′-xi or N5; the Γ3 counts (box203/out/gfc203_g3.out) are DATA only, and L-1 says so.
- LN-7: TARGET tail and scope clause in R123's / R124's landed form (RESULTS at trunk 8ba1b23b, asserted verbatim by the generator).
- LN-8: source note: packet sha1 97254bd2 frozen at l-new e252182d with this fixes entry, L-NEW successors 68-69; L-RED 63 (CLASS-PAYS,
  REL-G) and L-SI 48 / 49 cited as related lane statements, not premises.

### L-RED G1 (citation). ACCEPTED; governs §7's L-RED bullet.
- §7 cites both L-RED statements at claude/l-red fa4e50fe. Correct cites: Lemma REL-G at claude/l-red fa4e50fe, docs/red/R229-box93.md
  §1.3; Lemma CLASS-PAYS / Corollary GATE-FLIP-MIN at claude/l-red 8c034440, docs/red/R229-box203.md §3. Both remain related lane
  statements, not premises.

### L-RED G2 (premise row). ACCEPTED; governs the «To sign» row of §4.
- QUIET-N's proof uses «the Odd vertices with a choice are the gates and K2 ([DEF])». The row for §4 now reads: «§2, [DEF], R118 BR-SEG
  (with its labels C / R / p), R123 NO-TIE, LOC-GATE, LOC-K2, the counting (C1) of §1». [DEF] is R104's definitions only (§1), already a
  premise of §2 and §5; with R118 (a) («Odd is unrestricted (gates and K2)»). No new premise enters the packet.

### L-RED G3 (DATA, optional). ACCEPTED as a citation (not re-run here).
- A second engine: L-RED 63's cls229.py (claude/l-red 8c034440, experiments/red/r229/cls229.py, out/cls229.out: 29 rows; lfail, gfail,
  bonly, rep, qflip, qfail, Tfail all 0 per L-RED Addendum B) and lam229.py for (k+1)-Λ (claude/l-red cdecc4e0,
  experiments/red/r229/out/lam229.out: 12 genomes, lfail 0 per L-RED Addendum B). L-1 cites them with the referees' own replays.

## Line L-1 (L-NEW successor 69; first RESULTS line for P-N5-QN; written 2026-11-09 by date -u)
- docs/new/P-N5-QN-line-L1.txt, one paragraph, no «|»; generator experiments/new/box203/mkl1_qn.py, run from the repo root with
  `git show 8ba1b23b:docs/RESULTS.md` saved to a file as its argument. It asserts the frozen packet's sha1, the governing (k+1)-Λ
  sentence verbatim in this file, R123's landed scope sentence and R124's landed TARGET tail verbatim in RESULTS, LN-5's skip counts in
  box203/out2/skip203.out, and that the line has no «|» and no newline.
- Pinned in experiments/new/box203/qn.pins with this file, skip203.py, skip203.out and mkl1_qn.py.
