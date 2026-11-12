# R-P-N5-QN: first referee report on packet P-N5-QN (box 203)
REFEREE successor 30 (Opus 5.5, D15; D1 «Treat every such claim … as wrong until it passes the gauntlet»). Date -u at writing: 2026-11-09T07:38Z.
Object: claude/l-new e252182d (ancestor of origin/claude/l-new, checked), docs/new/P-N5-QN.md sha1 97254bd2a97f28bb0c14ab5f4d236ee723821dd9,
20,725 B (git show | sha1sum, wc -c; = the Lead's 07:34Z brief). No fixes file exists yet at e252182d. docs/referee-2/ and L-RED 63's
R229-box203 were NOT read before this verdict.

## 0. Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §2 | Theorem GATE-CLASS (IDEAL-CYC, every genome) | **SIGN** (PROVED). Every step re-derived (§3 below). |
| §3 | Corollary GATE-FLIP (a) | **SIGN** (PROVED). |
| §3 | Corollary GATE-FLIP (b) | **SIGN** (PROVED under its ascent hypothesis; the U(G) form under HYPOTHESIS [E-LEV], labelled so). |
| §4 | Corollary QUIET-N | **SIGN** (PROVED). The «Against R123» bullet's «R123's ASC-T and UP-T hold with L + 1 replaced by N + 1» is not in «To sign» and I did not check it: READING only (LN-4). |
| §5 | Lemma (k+1)-Λ | **SIGN** (PROVED) with wording note QN-1 (the list of values names «the most relevant vertex of each cycle of Ξ_σ»; it is that of the Γ(G)-cycle through it). The count k + 1 is right. |
| §6 | DEAD D1, D2, D3 | **CONFIRMED** on my own engine (§4), except D3's k = 2 WC family (not re-run; cited). |
No GAP. No statement is refused. TARGET.md diff CLEAN (§6).

## 1. Premises (§1), by my own script
- scratch/qn_quotes.py on trunk b8408b39 (an ancestor of origin trunk, checked) docs/RESULTS.md and P-N5-XICYC.md (sha1 149e2414):
  **24 quotes, 0 missing** (qn_logs/quotes.out): R104 6, P-N5-XICYC 1, R118 6, R121 3, R123 8. Each hit lies in the entry the packet names.
- In context (read in RESULTS at b8408b39):
  - R118 (d) BR-SEG «in IDEAL-CYC(G) := Γ(G) of ANY genome G (Ξ-cycles allowed) … every maximal run of p-steps has at most N steps»;
    every genome, IDEAL-CYC: the packet's scope.
  - R118 (e): «each vertex's Λ moves only to a vertex of strictly larger reward …» is the stated reason of the signed Lemma CYC-COUNT.
    (C1) uses it; it also follows from F1 (Ω_t ⊴ Ω_(t+1)) and distinct rewards. Fine.
  - R121 HUB-ASC-G: the hypothesis is per vertex («if seq_t(v) has at most B ascents for every t ∈ I»), so GATE-FLIP (b)'s hypothesis on
    e_g and β_g is the right one; the whole-run bound (2M + 3)·F′_B(M) is R121's.
  - R123: CN2, B-ONLY, NO-TIE, LOC-GATE, LOC-K2, class / loud / quiet, QUIET, T-QUIET: all IDEAL-CYC, every genome.
- Readings (D1)-(D5) of [DEF]: each checked against the quoted R104 text. (D1) e_g's only in-edge is from g: the e-vertex is per option
  with the gate's W-face edge only. (D2) E-DOM: priorities e > every β ≥ 6 > K1 = 5 > K2 = 3; above e only c_W (top), K0 (top + 2), K3
  (top + 3). (D3) core in-edges: K0 ← K1, β's; K1 ← K0, K1, K2, K3; K2 ← K3, K2; K3 ← K0: from outside only β → u = K0. (D4) c_X: only its
  loop. (D5) as defined. CORRECT.

## 2. Model
- IDEAL-CYC(G) = R118 (a): non-mover Even vertices frozen at R104's start (K0 → K3, K1 → K1, K3 → K2, β → Ξ-target or u); Odd = gates and
  K2 (R118 (a) «Odd is unrestricted (gates and K2)»); Howard steps at the movers. Odd vertices with a choice: the gates and K2 only.

## 3. Proofs, each step re-derived
- GATE-CLASS. Assume class(e_g), class(β_g) unchanged at t; s ∈ {t − 1, t}.
  - Case 1 (w_a ≠ w_b): rewards distinct ([VJ], injective priorities), so the faces' order is by Λ, the same at both s; LOC-GATE picks the
    strictly smaller face: same face. Correct.
  - Case 2 (w_a = w_b = w): a = e_g → c_W gives Λ(a) = c_W ≠ Λ(b) (b = β is no B-ONLY exception): Case 1. Else B-ONLY: w less relevant than
    every e-vertex; a ≠ w and a starts its play, so a lies on the path to w and is more relevant than w: e_g ∈ E_s(a). Correct.
  - 2a (e_g ∉ Π_s(b)): e_g ∈ Π_s(a) Δ Π_s(b), so its most relevant z ⪰ e_g; by (D2) z ∈ {e-vertices, c_W, K0, K3}. c_W is in no Π here
    (a play reaching c_W has node c_W, excluded for a and b). K0 / K3: a and b are non-core; by (D3) a play from a non-core vertex enters
    the core only at K0, then K0 → K3 → K2 frozen, σ̄_s(K2) = K1 (LOC-K2), K1 → K1 frozen; so K0 ∈ play ⟺ K3 ∈ play ⟺ node K1, and both
    plays have node w: K0, K3 in both Π or in neither. (This is the case split W-1 needed on Γ3 for P-N5-CHAIN; here it is made, since the
    argument is applied only to the two non-core faces.) So z is an e-vertex ⪰ e_g, hence the top of π(E_s(a)) Δ π(E_s(b)); z even, so
    [VJ] puts the value containing z above; LOC-GATE: σ̄_s(g) is the face with lexicographically smaller π(E_s). A function of the π-pair.
    Correct.
  - 2b (e_g ∈ Π_s(b)): b's play passes e_g, whose only in-edge is from g (D1), so the play has g → e_g: σ̄_s(g) = e_g. Correct.
  - Mixed: e_g ∈ Π_s(b) for exactly one s means E_s(b) changes (E = the e-vertices of Π): excluded. Both PRIV: equal π-pairs. Both non-PRIV:
    both e_g. ∎ Correct.
- (C1). Classes (Λ, E) of one vertex: Λ moves only to strictly larger reward (R118 (e)); at fixed Λ, E only rises (R121 E-MON) and a class
  change at fixed Λ is a change of E, so strict. The order (reward(Λ), E lex) is total, so the classes appear in strictly increasing order
  and never repeat: exactly D^tot(v) − 1 class-change steps. Correct.
- GATE-FLIP (a): each flip step is a class-change step of e_g or β_g (GATE-CLASS), each counted at most D^tot − 1 times (C1). (b): (a) with
  R121's whole-run D_E(v) ≤ (2M + 3)·F′_B(M) for v = e_g, β_g; UP-B for B = U(G) under [E-LEV]. Correct.
- QUIET-N: a quiet step changes no class, so no Λ: not C. σ̄ unique at every state (gates: NO-TIE + LOC-GATE; K2: LOC-K2's strict ◁), so
  R118's «any fixed deterministic choice» is σ̄; at gates σ̄ is unchanged (GATE-CLASS, contrapositive), at K2 constant: not R. So p. A maximal
  quiet window lies in a maximal p-run: ≤ N steps (BR-SEG). T_CYC = Q + (quiet steps) ≤ Q + (Q + 1)·N; Q ≤ Σ_v (D^tot(v) − 1) since each
  loud step is a class-change step of some vertex (C1). Correct. (QUIET-N is strictly stronger than R123 QUIET / T-QUIET: N ≤ L.)
- (k+1)-Λ: Z the cycle of v's play, w its top. B-ONLY: no e-vertex on Z (it would be above w), Z ≠ c_W's loop. If Z meets the core, the
  core part of every play is K0 → K3 → K2 → K1 → K1 (frozen, LOC-K2), so Z = K1's loop, w = K1. Z ≠ c_X's loop (D4, v ≠ c_X). Else Z has
  movers, gates and β's only (no pads in Γ(G)); a gate on Z goes to its β-face (no e on Z), a β to its frozen Ξ-target (a target X would
  enter the core). So Z's movers form a cycle of Ξ_σ, and w is the top of the Γ(G)-cycle Z, which that Ξ_σ-cycle determines. Ξ_σ has
  out-degree ≤ 1, so its cycles are disjoint; each is a Ξ-graph cycle (self-loops count), so each contains a vertex of a minimum feedback
  set of size k, distinct for disjoint cycles: ≤ k cycles. ∎ Correct.
  - QN-1 (wording, REQUIRED in the line, optional in a fixes entry): the statement's «the most relevant vertex of each cycle of the
    functional graph Ξ_σ on the movers» names a mover; the value is the most relevant vertex (a β) of the Γ(G)-cycle through that Ξ_σ-cycle.
    The proof says so («Z with w is determined by that cycle»). The bound k + 1 is unaffected.

## 4. Replays with my own code (scratch/qn_replay.py, qn_dead.py; logs scratch/qn_logs/)
- Engine: successor 26's xicyc_replay.howard (own Γ(G) builder from R104's text, own VJ valuation, Howard switch-best at movers, IDEAL-CYC
  freezing); own generator end_replay.gen; own minimum feedback set by exhaustion. No lane code imported.
- Counters (all must be 0): lfail (GATE-CLASS), gfail (GATE-FLIP (a)), qflip, qnotp (quiet step not labelled p), qfail (quiet window > N),
  Tfail, Qfail (Q > Σ(D − 1)), c1fail (a class repeated after leaving it: (C1)), lamfail ((k+1)-Λ), gtie (NO-TIE). Controls: ctrlE (flips
  with the e-face's class unchanged), ctrlK (states with more than k Λ-values).
- Families rand, deep, wide, acyc, selfl, 300 each, seed 2032 (1,500 runs; k up to 7), and 8 pinned files (MWR4/8/16_2, K1F21_n48,
  K1C16_n400, k1fail_202, ST4_k1, ST8_k1; from git archive e252182d): **every counter 0**; ctrlE fires (103 / 249 / 110 / 0 / 131 on the
  families, 9 / 17 / 33 / 22 / 70 / 2 on the files), ctrlK fires (202 / 76 / 202 / 607 / 142). (qn_logs/sweep.out)
- Records equal to the packet's §9: max flips of one gate MWR4/8/16_2 9 / 17 / 33, K1F21_n48 21, K1C16_n400 31. acyc: 0 flips (R122 BETA-ACYC).
- DEAD witnesses (qn_dead.py, qn_logs/dead.out; sha1 prefixes of the files re-measured and equal to §6): k1fail_202 gate (4, 0) 2 flips,
  C = 0 (so lamch 0 and 2 > 2·0 + 1): D1 CONFIRMED. MWR4/8/16_2 gate flips 2n + 1 = 9 / 17 / 33 with C = 0: D2 CONFIRMED. ST4_k1 3 and ST8_k1 7
  ascents at k = 1, K1C16_n400 and K1F21_n48 3 each: D3 CONFIRMED at k = 1 (the k = 2 WC family is cited, not re-run).
- The lane's own checks from `git archive e252182d`: qn.pins 56 rows, `sha1sum -c` all OK; box203/check203.sh re-run: rc 0, output
  byte-identical to check203.out.

## 5. DATA rule on §9 (counter predicates read in the code, gfc203.py / lam203.py at e252182d)
- gfc203.py l. 117-127: lfail counts flip steps with neither face's class (Λ, E) changing (GFC_CTRL=3: e-face only) = §9's «a flip with
  neither face changing class»; gfail per gate, flips > D(e) + D(β) − 2 = GATE-FLIP (a); l. 133-142: loud = some vertex changes class;
  qflip per quiet step with σ̄ changing at an Odd vertex; qfail per run with max quiet window > N; Tfail per run, T > Q + (Q + 1)N. Units as
  §9 states. OK.
- lam203.py l. 4-5 and l. 20: genomes with k > 12 are SKIPPED for lfail (k not an int). §9 does not say so, and the outputs do not report
  how many were skipped. LN-5 below. (My replay has no skip: lamfail 0 on 1,500 runs with k ≤ 7.)
- Γ3 counts: «DATA only, nothing claimed». OK.

## 6. TARGET.md diff: CLEAN
- No algorithm claim; one model (IDEAL-CYC of R104 / R118 genomes); QUIET-N sharpens a landed bound and makes no new class polynomial
  (§4's last bullet; §10). Not M3, not M4 (TARGET.md §2, §4), not M4-R (§4b: no algorithm), not a step-4 pass; G-N5-TIME stays OPEN.

## 7. Line requirements (no line exists yet; what I will test L-1 against)
- LN-1. Statements and labels as §0: GATE-CLASS, GATE-FLIP (a), (b), QUIET-N, (k+1)-Λ PROVED, IDEAL-CYC, every genome; GATE-FLIP (b)'s U(G)
  form under HYPOTHESIS [E-LEV]; DEAD D1-D3 with instances.
- LN-2. (k+1)-Λ's values in QN-1's corrected form.
- LN-3. Premises by R-id exactly as §1 lists them (R104 [DEF] definitions only, R118 (a), (d), (e), R121 E-MON / HUB-ASC-G / UP-B, R123 CN2,
  B-ONLY, NO-TIE, LOC-GATE, LOC-K2, QUIET, T-QUIET); no lane packet as premise.
- LN-4. «R123's ASC-T and UP-T hold with L + 1 replaced by N + 1»: omit, or label READING (not signed by me).
- LN-5. DATA clauses with units as in §5; the lam203 clause says genomes with k > 12 are skipped and how many (or that none were).
- LN-6. Scope: IDEAL-CYC only; nothing on Γ3, N5′-xi or N5; Γ3 counts as DATA only.
- LN-7. TARGET tail in the landed form (R123 / R124): «… is not M4, so this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not
  a TARGET.md claim».
- LN-8. Source note: packet sha1 97254bd2 frozen at l-new e252182d with its fixes entries, L-NEW successor 68; L-RED 63's attack and L-SI
  49 / L-RED 63 related statements cited as related, not premises.

## 8. Tools and outputs (committed, docs/referee/scratch/)
qn_replay.py, qn_dead.py, qn_quotes.py; qn_logs/: sweep.out, dead.out, quotes.out.

## §C. Fixes entry 1 and line L-1 (REFEREE successor 30, Opus 5.5, D15; date -u at writing 2026-11-09T10:42Z)
- Objects (Lead 10:41Z): claude/l-new 02a928a3 (ancestor of origin/claude/l-new, checked). docs/new/P-N5-QN-line-L1.txt sha1
  28bf566bdf95d0708b3b80303bfa7311c8d5d8b1, 7,357 B, one line, 140 «(» = 140 «)», 0 «|». Packet sha1 97254bd2 unchanged (frozen).
- Reproduction: from `git archive 02a928a3`, box203/mkl1_qn.py on RESULTS at trunk 8ba1b23b (R124 landed) asserts its inputs and
  rewrites L-1 byte-identically (cmp: SAME; sha1 28bf566b). qn.pins 61 rows, `sha1sum -c` all OK.
- Against my line requirements (§7), on the bytes:
  - LN-1: GATE-CLASS, GATE-FLIP (a), (b), QUIET-N, (k+1)-Λ as in the packet; GATE-FLIP (b)'s U(G) form «under HYPOTHESIS [E-LEV]», with
    [E-LEV]'s definition as R121 lands it («lev(x) < lev(x′) implies pr(e_(x,k)) < pr(e_(x′,k′))», checked in trunk RESULTS); DEAD D1-D3
    with instances and sha1s equal to those I re-measured (§4). D1 now defines lamch(g) (Λ changes at e_g or β_g), consistent with my C = 0
    check. PASS.
  - LN-2 / QN-1: «the most relevant vertex of the Γ-cycle through its movers, their chosen gates and β-faces» (one value per Ξ_σ-cycle,
    plus K1): exactly my QN-1 correction. PASS.
  - LN-3: premises by R-id only (R104 definitions; R118 (a), (d) BR-SEG, (e) with its stated reason, the order ⊴ and labels C / R / p; R121
    E-MON, and HUB-ASC-G whole-run form / UP-B for (b) only; R123 CN2, B-ONLY, NO-TIE, LOC-GATE, LOC-K2); «not used: any lane packet, …,
    any P-N5-CHAIN fact». PASS.
  - LN-4: «R123's ASC-T and UP-T hold with L + 1 replaced by N + 1» is absent from L-1 (grep: «ASC-T» 0 times); fixes entry 1 l. 38-39 keeps
    it as a READING. PASS.
  - LN-5: units as the code computes them (§5); lam203's skip is stated with its count: «lam203.py skips genomes with k > 12, and none of
    these 4,000 was skipped (unit: genomes; skip203.py, out2/skip203.out: k ≤ 5 on every genome)»; out2/skip203.out at 02a928a3 reads
    skipped_k_gt_12 0 on all three sets, max k 5 (rand), 1, 2. PASS.
  - LN-6: IDEAL-CYC only; Γ3 counts «DATA only, nothing claimed»; the Γ3 sentence is a correct reading of R118 (k), (l) «under
    REACH3-CYC's premises» and names the exact-VJ-tie divergence. PASS.
  - LN-7: TARGET tail «… is not M4, so this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim» = R123 /
    R124 landed form (mkl1_qn.py asserts it against RESULTS). PASS.
  - LN-8: source note names the frozen packet (l-new e252182d, sha1 97254bd2) with fixes entry 1, L-NEW 68-69, and the related lane
    statements as «not premises». PASS.
  - The citation of my replay («REFEREE 30 R-P-N5-QN §4 (claude/referee 452800c5; 1,500 runs and 8 pinned files)») is accurate.
- Fixes entry 1: QN-1 taken in one governing sentence; LN-4 as a READING; DSALT6's window 10 (lane engine) vs 11 (REFEREE-2's engine), both
  ≤ N and explained by R118 (a)'s free tie rule: CORRECT (QUIET-N's bound is tie-rule independent).
- Verdict: fixes entry 1 CORRECT. **Line L-1 MATCHES** the packet read with fixes entry 1 and meets LN-1..LN-8. Statements as §0 (all
  SIGN). docs/referee-2/ read only for the strings fixes entry 1 cites.

## §D. Fixes entry 2 and line L-2 (REFEREE successor 31, Opus 5.5, D15; date -u at writing 2026-11-12T02:58Z; Lead 02:58Z byte test)
- Objects: claude/l-new 70501a99 (ancestor of origin/claude/l-new, checked). docs/new/P-N5-QN-line-L2.txt sha1
  166e4695b07843ae73e2d23ac92802c256f31113, 7,187 B; L-1 at 70501a99 sha1 28bf566b… (unchanged, the line my predecessor's §C matched).
  Fixes entry 2: line-only (CHECKER C140 E-1 = flag G-L43; Lead ruling R-D2a 02:30Z).
- Byte test: scratch/qn_l2.py applies R-D2 then R-S to L-1, both strings typed from CHECKER C140 §4 (claude/checker 445372f9), not from the
  lane's generator. Each old string occurs once in L-1. After R-D2: sha1 2e85dfe5…, 7,060 B (= C140's intermediate); after R-S: sha1
  166e4695…, 7,187 B. `cmp` with the lane's L-2: **EQUAL** (qn_logs/l2test.out). Nothing else changed. One line, 0 «|», 137 «(» = 137 «)»,
  «D2» 0, «406ef2fd» once, «pending» / «landed» 0. The join reads «… (4, 0): 2 flips, lamch 0); D3 «every e-sequence has at most k + 1
  ascents» …»: D3 keeps its name.
- Meaning. R-D2: D2 «at k = 1 every gate flips at most c·(lamch(g) + 1) times», «every constant c», rested on three instances; at lamch 0
  the bound is c, and 9 / 17 / 33 flips refute it only for c ≤ 32. «Every constant c» needs the MWR(n) count for every n, which no signed
  text proves (my predecessor's §4 confirmed the numbers, not the family). Under L43 the item is DATA, not DEAD: dropping it is right.
  R-S: the instances stay in the C = 0 DATA clause with their source (L-RED 63, claude/l-red 406ef2fd) and sha1s 856d369b, 918f1414,
  2ccda9a9, which match box93/inst/SHA1SUMS at claude/l-si 9c0349b1 (same files; R-P-N5-GATE §1.1). The numbers 9 / 17 / 33 at lamch 0 are
  reproduced independently by my own engine (R-P-N5-GATE §3.2, both runs: max flips 9 / 17 / 33 with lamch 0 at the max-flip gate).
- Re-signature (as REFEREE, for the DEAD list): D1 and D3 as my predecessor's §0 / §4 signed them (CONFIRMED; D3's k = 2 WC family cited,
  not re-run); D2 removed from DEAD (now DATA). Every statement and label of P-N5-QN unchanged.
- Verdict: fixes entry 2 CORRECT. **Line L-2 MATCHES** (= L-1 + R-D2 + R-S exactly; = CHECKER C140 §4's L-2).
