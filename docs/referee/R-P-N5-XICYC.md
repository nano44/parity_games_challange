# R-P-N5-XICYC: REFEREE report on P-N5-XICYC (L-NEW successor 59, box 191)
REFEREE successor 26 (Opus 5.5, D15). Written from 2026-11-07T07:44Z (date -u); the header time of record is the commit time.
Packet frozen at claude/l-new fd1266a5; fixes entry 1 and line L-2 at 86afce49. I did NOT read docs/referee-2/ for this report.
Owner D1: «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's
own, as wrong until it passes the gauntlet below.» This packet claims no polynomial algorithm; it bounds Howard runs in terms of R.

## 0. Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §3 | Fact F4 (as stated) | FALSE as stated (XC-1, instance §2.1); TRUE in the restricted form F4′. Every §4 use is inside F4′ |
| §4 | Theorem BR-SEG | SIGN WITH GAP XC-1 (proof cites F4; all its uses satisfy F4′; statement unchanged) |
| §4 | Lemma CYC-COUNT | SIGN |
| §4 | Theorem T-CYC | SIGN WITH GAP XC-1 (inherited from BR-SEG) |
| §4 | Corollary ONEP-POLY | SIGN WITH GAP XC-1 (inherited); optional O-1 (K2's optimum is unique) |
| §4 | Lemma LEVEL0 | SIGN |
| §5 | Theorem BR-SEG-G (a)-(c) | SIGN WITH GAPS XC-1, XC-2 (DOM is FALSE for Even vertices of a general game, instance §2.1; repaired proofs of STRICT and PATH in §2.2; statement unchanged) |
| §6 | Lemma DECOMP-G | SIGN |
| §6 | Theorem RED-XI | SIGN WITH GAP XC-2 (inherited from BR-SEG-G) |
| §7 | Theorem REACH3-CYC | SIGN as PROVED-CONDITIONAL on [REACH-L], WITH GAPS XC-3 (hidden SBAR3 use through K3 (b)/(d); every-genome proof supplied in §3.2) and XC-4 (premise [1E-N3] not named) |
| §7 | Corollary T3 | SIGN as an EQUIVALENCE only, same condition and gaps as REACH3-CYC |
| §8 | DEAD SEG-2P | SIGN; rule-free (Howard ties 0 on all three runs; Λ is part of the unique value) |
| §8 | DEAD ODD-FIXED | SIGN; rule-free (every R-step of the three runs is forced: no Odd strategy is optimal in both states) |
| L-2 | the line | byte test MATCHES fixes entry 1; verdict NOT YET: XC-L1, XC-L2, XC-L3 (DATA rule), XC-L4 (premises), exact texts in §5 |

## 1. Objects (sha1 of the bytes, re-hashed; all EQUAL to the Lead's relay)
- claude/l-new fd1266a5 is an ancestor of 86afce49; 86afce49 changes no packet byte (git diff --stat: fixes, L-2, level0_191.py, pins,
  check.sh, box doc, notebook).
- docs/new/P-N5-XICYC.md 149e2414… (same at fd1266a5 and 86afce49); line L-1 d6f77b12…; fixes b4ad5bca…; line L-2 857d21c8…;
  experiments/new/box191/xicyc.pins 521ce400… (at fd1266a5 the pins file was c65b9655…, the pre-fixes version).
- Every sha1 listed in xicyc.pins is equal to the bytes at 86afce49 (sha1sum -c on the worktree).
- Byte test L-1 → L-2: R-1's old string occurs once in L-1, the new string once in L-2, and L-2 = L-1 with that one replacement,
  byte-equal (2,663 → 4,502 bytes, both with a final newline).
- check.sh blocks «BOX 191 XI-CYCLIC» and «P-N5-XICYC» (experiments/new/check.sh lines 965-978 at 86afce49, run as extracted from
  experiments/new in a worktree at 86afce49): both print PASS, exit 0.
- I also re-ran every counter named in L-2 at 86afce49 (§4; output docs/referee/scratch/xicyc_logs/lane_counters_rerun.out, commands
  in lane_counters_rerun.sh). Every printed line equals L-2's numbers.

## 2. §3-§6: the proofs
### 2.1 F4 as stated is false; DOM is false on general games (XC-1, XC-2)
- F4 says ext(v, ·) is ⊴-monotone and strictly monotone, «v is added to both Π or to neither, so the symmetric difference is
  unchanged». This fails when v already lies in one of the two Π-sets.
  - Instance (own engine, docs/referee/scratch/xicyc_dom.py, output xicyc_logs/dom_f4_cex.out): w (priority 2), y (4), v (9).
  - A = (w, ∅, 3) ▷ B = (w, {v, y}, 3), since the top of the difference is v, odd, and lies in B.
  - ext(v, A) = (w, {v}, 4) ◁ ext(v, B) = (w, {v, y}, 4), since the difference is now {y}, even, and lies in B.
- F4′ (restricted; TRUE, by the packet's own proof): if v ∉ Π(A) ∪ Π(B), then A ⊴ B ⇒ ext(v, A) ⊴ ext(v, B) and A ◁ B ⇒
  ext(v, A) ◁ ext(v, B). It also holds whenever v ranks below Λ(A) and Λ(B): then ext only adds 1 to k on both sides.
- §4 uses only F4′:
  - DOM, STRICT and PATH's mover case apply ext at movers: priority 0, below every possible cycle node of Γ(G) (F6).
  - PATH's non-mover case applies F4 to Ω_t(z_1) and val(tail). Ω_t(z_1) is z_0's own play after its first step, and z_0 is not
    its cycle node, so z_0 ∉ Π(Ω_t(z_1)). val(tail) comes from the simple path π minus z_0.
  - So BR-SEG, T-CYC and ONEP-POLY stand. XC-1 asks L-NEW to restate F4 as F4′ in a fixes entry, with this list of uses.
- §5 reads §4's proofs «with "mover" read as "Even vertex"». DOM is then FALSE.
  - Instance: Even vertices w (priority 2, loop), x (9, → w, y), y (4, → x, w); σ_0: x → w, y → x. The Howard step 0 → 1 switches
    y only, to w (H0 holds at y: Λ = w before and after).
  - Ω_1(x) = (w, {x}, 1) ◁ ext(x, Ω_0(y)) = (w, {x, y}, 3). DOM claims ⊵.
  - Cause: Ω_0(y)'s play passes x, so x ∈ Π(Ω_0(y)) and F4 is used outside F4′. STRICT's proof has the same defect: Ω_t(σ_(t+1)(x))
    may contain x.
  - In random games DOM fails in 150 steps (xicyc_logs/brsegg_own.out: 9 at n 7, 141 at n 10).

### 2.2 Repaired proofs for §5 (statement of BR-SEG-G unchanged; these replace DOM)
- STRICT-G. Let x switch at step t → t+1 with Λ_t(x) ≠ x ≠ Λ_(t+1)(x) (H0), and put y′ := σ_(t+1)(x).
  - Ω_(t+1)(y′) ⊵ Ω_t(y′) by F1, and Ω_t(y′) ▷ Ω_t(σ_t(x)) by F5; transitivity gives Ω_(t+1)(y′) ▷ Ω_t(σ_t(x)).
  - Neither set contains x: each is x's own play after its first step (at t + 1 and at t), and x is not its cycle node.
  - F4′ (strict) and F3 at t and t + 1: Ω_(t+1)(x) = ext(x, Ω_(t+1)(y′)) ▷ ext(x, Ω_t(σ_t(x))) = Ω_t(x).
- PATH-G, the case of an Even z_0 (t − 1 ∈ [a, b], (t − 1) − a ≥ μ − 1). Put y := σ_t(z_0).
  - Ω_t(y) ⊵ Ω_(t−1)(y) by F1.
  - Ω_(t−1)(y) ⊵ Ω_(t−1)(z_1), because the Howard step t − 1 → t gives z_0 a ⊴-best successor under Ω_(t−1).
  - Ω_(t−1)(z_1) ⊵ val(tail) by induction.
  - Ω_t(y) excludes z_0 (Λ_t(z_0) = w ≠ z_0), and val(tail) excludes z_0 (π is simple). F4′ and F3 give
    Ω_t(z_0) = ext(z_0, Ω_t(y)) ⊵ ext(z_0, val(tail)) = val(π).
  - The Odd and frozen cases are as in the packet (F4′ applies there, §2.1).
- With these, BR-SEG's argument gives (a) under H0 verbatim. (b): each vertex's Λ takes strictly increasing rewards among at most n
  vertices (F1, F2). (c) is the arithmetic of T-CYC.
- DATA, own engine (docs/referee/scratch/xicyc_brsegg.py; Odd's reply by local improvement, checked against brute force over all Odd
  strategies on 300 games, 0 differences):
  - 3,300 random games (n 7 and 10, priorities 0..2n−1);
  - 0 stretches of H0-steps with constant (Λ, σ̄) longer than n_E;
  - the ratio reaches 1.0, so the bound is tight on these data.
- Switch-all family (own engine and own S3 best-reward start from SPEC S3 / FIX 1 text, xicyc_sae.py):
  - N 2-7 reproduce L-2's T, C, R and longest p-run exactly (sae_own_N2-3.out, sae_own_N4-7.out);
  - H0 holds at every step (0 H0-failing steps).

### 2.3 The other §4/§6 statements (checked line by line)
- BR-SEG: π is simple and lies in E_a; μ(π) ≤ N; F3 along π gives Ω_(a+j+1)(x) = val(π); PATH at t = a + j needs j ≥ μ(π); STRICT
  contradicts. Every step changes σ (the run stops at the first state with no strict improvement), so a p-run of r steps has
  r − 1 ≤ N − 1.
- CYC-COUNT:
  - Under the frozen start the possible cycle nodes are the β's, the e's, c_W, K1, K2 and c_X.
  - K0 → K3 → K2 and K1 → K1, so K0 and K3 lie on no cycle. c_X has no other in-edge.
  - So each vertex ≠ c_X has at most 2M + 3 possible cycle nodes, hence at most 2M + 2 changes (F1, F2).
- T-CYC: there are at most C + R + 1 maximal p-runs, each of at most N steps.
- ONEP-POLY:
  - Gates have one successor, and K2's values come from the closed core.
  - K2 → K1 (cycle node K1, priority 5) is strictly better for Odd than its loop (node K2, priority 3), so K2's optimal choice is
    UNIQUE and every rule picks it (O-1: say this rather than «the deterministic rule picks the same»). R = 0.
- LEVEL0:
  - c_W's in-edges are its loop and the level-0 e-faces, and each e-face's only in-edge is its gate.
  - top is the largest even priority on any cycle: K0 (top + 2) lies on no cycle.
  - Switching every level-0 gate to its β-face removes c_W from every play from g. That play's node then has a strictly smaller
    reward, so the optimality of σ̄_t is contradicted.
  - One level: every gate and K2 are forced, so R = 0.
- DECOMP-G: σ changes only at S-iterations, by Switch_I with I ⊆ Iσ of the σ in force, and Ωσ depends on σ alone ([R15d]).
- RED-XI:
  - |S| ≤ C + R + (C + R + 1)·n_E ≤ (n_E + 1)(n(n − 1) + R_σ + 1), using R ≤ R_σ: R_σ counts every S-step with a σ̄ change, C-steps
    included.
  - A prefix of a Howard run obeys the same bound. R_σ is relative to the fixed σ̄ rule.

## 3. §7: REACH3-CYC and Corollary T3
### 3.1 Hidden uses, ESC3 and W3 re-read
- ESC3 (β_g part): every H-play from xt(g) is mover → pad → gate → pe → e → … → c_W, and every H-play from pb_g enters the core. Neither
  takes a β-face, and β_g lies on no cycle of H. No Ξ-use.
- W3 (i)-(iii): the (σ, τ)-plays and the H-plays follow τ = pe at every gate, and W(β_g) takes one β step. No Ξ-use, no corner.
- HIDDEN USE (XC-3): ESC3's core part is «Core: K3 (d)», K3 (d) rests on K3 (b), and K3 (b) ends «These values hold once SBAR3 gives
  σ̄(K2) = r». SBAR3 is labelled IDEAL-ACYC.
  - So §7's «Not used: … SBAR3» is false as written, and §7's «Iσ ∋ (K0, K1) in every standard state (K3, every genome)» rests on an
    acyclic-only lemma.
  - The fact itself holds for every genome (§3.2). This is a labelling defect of P-N5-REACH's K3 («every genome»), harmless there
    because REACH3 is IDEAL-ACYC.
- TAU3 uses K3 (c) (no SBAR3); S3-START and PAD use no acyclicity.

### 3.2 σ̄(K2) = r for every genome (closes XC-3; to be put in a fixes entry by L-NEW)
- In every standard state σ(K1) = s and s → K1, so K1's play is K1 → s → K1 (cycle node K1, Ω 5) whatever Odd does. The core is
  closed: its only in-edges come from the pads pb_g.
- K2's two options:
  - r leads to node K1, with reward −p′(K1);
  - its loop has node K2, with reward −p′(K2).
- K1 outranks K2 (Ω 5 > 3) and both are odd, so −p′(K1) < −p′(K2): r is strictly better for Odd.
- S1's σ̄ is a pointwise optimum ([1E-N3] P1), so σ̄(K2) = r.
- K3 (a)-(d) then hold verbatim for every genome, and so do ESC3 and the TIE sets {xt(g)} at β_g and {pA} at K0.

### 3.3 The rest of the proof, checked
- τ: TAU3 holds for every genome.
- Movers: W3 (iii) gives TIE(x) = R(x) = {σ(x)} ∪ Iσ(x), and x is not its own H-cycle node. The Ξσ-best element of R(x) is a ⊴-best
  successor overall, because every successor outside R(x) is ⊴ σ(x). If σ(x) is best, Iσ(x) = ∅ and σ(x) is kept.
- No Even vertex with |A(v)| ≥ 2 is its own H-cycle node: movers have node c_W, β_g has node c_W, and K0 lies on no cycle of H.
- Step T3: R(x) = {σ(x)} everywhere and Iσ ∋ (K0, K1), so S4c fires.
- Corollary T3:
  - movers have Ω 0, below every cycle node (PAD (b): Ω ≥ 3), so §4's F4 uses stay in F4′;
  - the possible cycle nodes in Γ3 are again the β's, e's, c_W, K1, K2 (+ c_X), so C ≤ n3(2M + 2);
  - LEVEL0's argument holds on Γ3 (c_W's in-edges are unchanged; K0 → pA → K3 lies on no cycle);
  - FL run = [0, T3], since W is constant (W3 (i)). ⇒ holds because R ≤ T3; ⇐ by the bound. This holds for each fixed σ̄ rule.
- XC-4: §7 identifies N5′-xi's Ξσ (S1's procedure) with §4's Ω_t (VJ value against an optimal σ̄), and its W* with H's optimum. That
  is [1E-N3] P1/P2 (RESULTS R57 (b) as landed in R104), which neither §1 nor [REACH-L] names. It is landed, so this is a citation
  gap. The line must name it (XC-L4).

### 3.4 Replay (own Γ3 builder from P-N5-REACH §3 text + own engine; L-NEW's box190 n5v.py «xi» as the object under test)
- Script: docs/referee/scratch/xicyc_reach3.py. For each genome:
  - my Γ3 equals gamma3.build(G, PADS) (priorities, owners, successor sets, start);
  - N5′-xi from S3 visits only standard states up to T3;
  - under MY values every N5′-xi mover step is a Howard step (current kept when best);
  - the stop is the first state with no strictly better mover successor;
  - the fallback FLAG is set exactly at transition T3 + 1;
  - the longest p-run is ≤ N.
- 22 of 22 pinned genomes OK (8 inst/cyc*.json, 14 box189 corpus; xicyc_logs/reach3_files.out).
- 300 of 300 random genomes OK (rand191.rgen as the generator only, seed 77, 681 mover-phase transitions;
  reach3_rand300_seed77.out). In 11 of them my tie rule («keep, then larger index») picks a different best successor from N5′-xi's
  rule at an exact VJ tie; both are Howard steps.
- BR-SEG / CYC-COUNT / LEVEL0 on IDEAL-CYC(Γ), own engine, 500 random genomes (brseg_gamma_own.out):
  - 0 p-runs > N; 0 runs with C > n(2M + 2);
  - σ̄ on the e-face in 0 of 8,196 (state, level-0 gate) pairs.

## 4. §8: DEAD, and the lane counters
- Own replay of the three pinned genomes (sha1 c8be0e60…, ff56b858…, 9af1c2a6…; xicyc_logs/dead_own.out). Γ(G) is built with
  R104's vertex order (movers, gates by gate index, β's by option order, e's by gate index, c_X, c_W, K0-K3); my Odd reply is local
  improvement from the previous reply.
  - Labels identical to L-2: ppppppppRC; CCCCpRRRRppRRRpRppp; pppRppRppRppRRRpppppp.
  - Longest Λ-keeping run 9 > 8, 15 > 14, 21 > 18. Howard ties 0 in all three runs, so the σ-sequence does not depend on the index
    order of the tie rule.
  - Λ is a component of the unique value Ω_t, so these lengths do not depend on any σ̄ rule.
- DEAD ODD-FIXED, rule-free (xicyc_oddfixed.py, oddfixed_own.out):
  - Candidate sets: C_t(v) := {u : ext(v, Ω_t(u)) = Ω_t(v)} if Λ_t(v) ≠ v, else {u : Λ_t(u) = v}. These are necessary for optimal
    choices (F3).
  - At every one of the 1 + 8 + 6 R-steps, C_t(v) ∩ C_(t+1)(v) = ∅ at 1 to 7 Odd vertices v. So NO Odd strategy is optimal in both
    states, and σ̄ changes under EVERY deterministic rule.
  - All 15 R-steps lie inside the Λ-keeping runs above.
- Lane counters re-run at 86afce49 (lane_counters_rerun.out) reproduce exactly:
  - level0 3,422 / 17,013 / 0;
  - subrun 1000 21: 0;
  - seg1p 300 11: 0 / 0 in both models;
  - brseg_gen191 random 2000 3 12: 0;
  - howard3 1,061 + 1,106 = 2,167 transitions, all zeros;
  - eq 297/300 (ties 3) and 974/1,000 (ties 26).
- Two L-2 counts have no committed output:
  - «555»: brseg_gen191.py's random mode computes h0 per game but prints only «of which with an H0 event». I added one counter by
    exact string replacement (xicyc_logs/brseg_instr.py). It prints 555, and its original output line is byte-equal to the lane's
    (brseg_gen191_instrumented_2000_3_12.out). h0 counts steps in which some switching Even vertex is its own cycle node at the
    START of the step.
  - switchallexp N 6, 7: only N 2-5 are pinned (inst/sae_2..5.pg; my regenerated files have equal sha1) and printed (check191.out).
    I regenerated N 6, 7 with pgsolver_port.py (sha1 5dc850b1…, ff46e32f…) and ran the lane's brseg_gen191.py (sae_lane_N6-7.out)
    and my own engine (sae_own_N4-7.out). Both give T 630 / 1243, R 116 / 241, longest p-run 17 / 19, C 0, n_E 59 / 68, as in L-2.
- level0_191.py imports from the absolute path /home/user/parity_games_challange/experiments/new/box191, so it reads whatever checkout
  sits there. Here that was trunk 6f9cc0b0, whose idealcyc.py and rand191.py are byte-equal to 86afce49's (diff -rq). Optional O-2:
  use the script's own directory, as the other tools do.
- Optional O-3: ONEP-POLY's DATA counts Λ-keeping runs and C, not R = 0 itself. The line says so correctly.

## 5. Line L-2: DATA rule, clause by clause, and required fixes
Clauses with matching counters (unit, set, scope checked against the code):
- BR-SEG (subrun191: genomes with a p-run > N; rgen d 1-6);
- CYC-COUNT (seg1p191: genomes with C > N·M, both models; N·M < n(2M + 2), so the count is stronger than the clause);
- ONEP-POLY (seg1p191 ONE-player);
- LEVEL0 (level0_191: (state, level-0 gate) pairs of IDEAL-CYC runs; e-face = the successor of larger priority);
- BR-SEG-G random games (brseg_gen191: games with a p-run > n_E, a superset of the H0 runs);
- the DEAD items (labels read off subrun191);
- the context clause (rand191 eq; «exact VJ tie» = equal keys of the two next choices at every mover).
- T-CYC and RED-XI carry «no separate DATA» correctly.

Required (each is an «old» → «new» replacement in L-2, to be recorded in a fixes entry; nothing else changes):
- XC-L1 (DATA rule: the named command does not print the count).
  - Old: «H0 itself is not checked by the tool, which counts 555 steps in these runs where some switching Even vertex is its own
    cycle node»
  - New: «H0 itself is not checked; 555 steps of these runs switch some Even vertex that is its own cycle node at the start of the
    step (brseg_gen191.py does not print this count; reproduced by REFEREE R-P-N5-XICYC with one added counter,
    docs/referee/scratch/xicyc_logs/brseg_gen191_instrumented_2000_3_12.out)»
  - Equivalent: L-NEW commits its own printing counter and names it instead.
- XC-L2 (no committed output or pin for N 6, 7).
  - Old: «against n_E = 23, 32, 41, 50, 59, 68;»
  - New: «against n_E = 23, 32, 41, 50, 59, 68 (N 2-5: inst/sae_2..5.pg and check191.out; N 6, 7: pgsolver_port.py switchallexp 6
    and 7, sha1 5dc850b1… and ff46e32f…, brseg_gen191.py output docs/referee/scratch/xicyc_logs/sae_lane_N6-7.out);»
  - Equivalent: pin sae_6/7 and commit the lane's own output.
- XC-L3 (scope: «bad stops» is undefined in the line, and the tool does not read the fallback flag that the REACH3-CYC clause
  asserts).
  - Old: «0 non-standard states, 0 non-Howard mover steps and 0 bad stops in 2,167 mover-phase transitions of 1,000 genomes»
  - New: «0 genomes with a non-standard state among states 0, …, T3, 0 non-Howard mover steps, and 0 genomes whose first state
    with no strictly better mover successor is followed by a transition that changes a mover, in 2,167 mover-phase transitions of
    1,000 genomes (the tool does not read the fallback flag; the fallback at transition T3 + 1 is checked by REFEREE R-P-N5-XICYC on
    22 of 22 pinned and 300 of 300 random genomes, docs/referee/scratch/xicyc_logs/reach3_*.out)»
- XC-L4 (premises of REACH3-CYC; XC-3, XC-4).
  - Old: «(Theorem REACH3-CYC, CONDITIONAL on P-N5-REACH's S3-START, PAD, K3, TAU3, ESC3, W3, not landed)»
  - New: «(Theorem REACH3-CYC, CONDITIONAL on P-N5-REACH's S3-START, PAD, K3, TAU3, ESC3, W3, not landed, with σ̄(K2) = r proved
    for every genome in P-N5-XICYC's fixes (K3 (b) otherwise cites SBAR3, which is IDEAL-ACYC), and on the landed premise [1E-N3]
    (RESULTS R57 (b), as landed in R104: S1's σ̄ and S4a's arena optimum are pointwise optima))»

Packet fixes asked (a fixes entry; the packet stays frozen):
- XC-1: restate F4 as F4′ and list its §4 uses (§2.1).
- XC-2: replace DOM in §5 by STRICT-G and PATH-G (§2.2).
- XC-3: the σ̄(K2) = r argument (§3.2); correct §7's «Not used: … SBAR3».
- XC-4: add [1E-N3] to §1 for §7.
Optional: O-1 (ONEP-POLY's uniqueness at K2), O-2 (level0_191.py's absolute path), O-3.

TARGET.md diff: none of these statements is a TARGET.md theorem. Nothing here bounds R, so G-N5-TIME stays OPEN, and N5′-xi stays a
CANDIDATE (no gauntlet step 4 pass).

## 6. Tools and outputs (committed)
docs/referee/scratch/:
- xicyc_vj.py (own VJ values, comparison, ext, Odd local improvement, brute force);
- xicyc_replay.py (own Γ / Γ3 builder from R104 / P-N5-REACH §3 text, IDEAL-CYC Howard, labels);
- xicyc_reach3.py, xicyc_oddfixed.py, xicyc_dom.py, xicyc_brsegg.py, xicyc_brseg_rand.py, xicyc_sae.py;
- outputs in xicyc_logs/ (input sha1s in inputs.sha1).

## §C. Fixes entry 2 and line L-3 (REFEREE successor 26; date -u at writing 2026-11-07T09:01Z)
- Objects at claude/l-new 50c80a92 (worktree; sha1 of the bytes):
  - fixes a83e54d2… (entries 1 and 2);
  - line L-3 1690b6ad…, 5,543 bytes;
  - packet 149e2414… unchanged; L-2 857d21c8… unchanged;
  - xicyc.pins c77781e0…: `sha1sum -c` OK, all 40 entries.
- check.sh blocks «BOX 191 XI-CYCLIC» and «P-N5-XICYC» at 50c80a92 (extracted from experiments/new/check.sh): both PASS, exit 0.
- After my report was pushed (695b610c), I read docs/referee-2/R2-P-N5-XICYC.md only as fixes entry 2 quotes it.
- Byte test (own script):
  - R1-R6 are parsed from fixes entry 2. Each old string occurs once in L-2 and each new string once in L-3.
  - L-2 with R1-R6 applied is byte-equal to L-3 (sha1 1690b6ad…, 5,543 bytes).
  - R5's and R6's old and new strings are my XC-L3 and XC-L4 texts verbatim (wrapped lines joined).
  - R3 and R4 replace my XC-L1 / XC-L2 old strings with other texts (judged below).
- XC-L2 (R4, «Equivalent» form): MET.
  - inst/sae_6.pg and inst/sae_7.pg have sha1 5dc850b1… / ff46e32f… (equal to my regenerated files) and are pinned in xicyc.pins.
  - data/sae_6_7.out equals my run of the lane counter on my regenerated files (xicyc_logs/sae_lane_N6-7.out), apart from the path
    prefix.
- XC-L3 (R5) and XC-L4 (R6): MET (verbatim).
- XC-L1, resolved by REFEREE-2's W-4 (R3) under the Lead's ruling: «H0 is not checked by the tool, and these runs include steps at which
  H0 fails». XC-L1's intent is MET. My intent was:
  - (i) the line must not state a count that the named command does not print. W-4 states no count.
  - (ii) the caveat must say what the data does not cover. W-4 says it more directly than my text did: my «555» counted steps with
    some self-cycle-node switcher, which is not an H0 failure.
  - W-4's existential claim is true on exactly that set: one counter added by exact string replacement to the lane's brseg_gen191.py
    (H0 fails at a step iff no switching Even vertex has Λ ≠ itself both before and after) gives «INSTR H0-failing steps 388 of 2072».
    The original output line is byte-equal (xicyc_logs/brseg_gen191_H0fail_2000_3_12.out, tool brseg_h0_instr.py). This agrees
    with fixes entry 2's figure from REFEREE-2 (388 of 2,072).
  - Optional (no fix required): the line could cite that counter.
- Packet repairs:
  - XC-1: CLOSED. F4 is replaced by F4′ with its proof and the full list of §4 uses, including §7's Corollary T3 on Γ3 (movers Ω 0
    < 3).
  - XC-2: CLOSED. STRICT-G and PATH-G are stated in full (my §2.2 text); BR-SEG-G (a) follows; RED-XI inherits (c); «No DOM is used in
    §5 or §6». REFEREE-2's Z × Z route is recorded as a second route and is not needed.
  - XC-3: CLOSED.
    - §7's «Not used» is corrected.
    - Lemma K2-r is my §3.2 argument. Its premise [1E-N3] P1 is the XC-4 premise.
    - Its IDEAL-CYC variant (K1 frozen to its loop: node K1 beats node K2) is also correct.
    - REFEREE-2's N-1 (LEVEL0's «R-flips only at gates of level ≥ 1» also needs σ̄(K2) constant) is correctly answered by the same
      uniqueness.
  - XC-4: CLOSED. [1E-N3] is added to §1 for §7, quoted from R104 l. 9864.
  - O-1: DONE.
  - O-2: DONE. level0_191.py imports from its own directory; data/level0_1000_41.out = «states 3422, … pairs 17013, … e-face 0»,
    unchanged.
  - O-3: handled by R2.
- Verdicts:
  - fixes entry 2 CORRECT; L-3 MATCHES, by the byte test and in meaning;
  - XC-1 to XC-4 and XC-L1 to XC-L4 all closed;
  - every statement of §0 is now SIGN: BR-SEG, T-CYC, ONEP-POLY and BR-SEG-G with their repaired proofs, RED-XI, REACH3-CYC and
    Corollary T3 still PROVED-CONDITIONAL on [REACH-L] (R117, not landed), and the DEAD items as before.

## §C add. 1. Line L-4 (CHECKER C132 R1-R7; R118) (REFEREE successor 26; date -u at writing 2026-11-07T12:39Z)
- Objects at claude/l-new e36fdfcd (worktree; sha1 of the bytes):
  - L-4 85fe809c…, 6,342 bytes, 73 «(» = 73 «)», 0 «|»;
  - L-3 1690b6ad… unchanged;
  - fixes 90d0f09d… (entry 3 appended; every C132 new string occurs in it);
  - xicyc.pins df6f4799…
  - C132 read at claude/checker d6b877f7; RESULTS R117 read at trunk ac1bc37c (l. 13362 ff.).
- Byte test (own script): R1-R7 are parsed from C132 §5 (wrapped lines joined by one space). Each old string occurs once in L-3 and
  each new string once in L-4. L-3 with R1-R7 applied is byte-equal to L-4 (sha1 85fe809c…, 6,342 bytes).
- R1 in meaning, against R117's landed entry and this report: CORRECT.
  - R117's entry signs S3-START [every genome] and PAD [every genome] in (c) and (d). Its transfer lemmas carry
    [IDEAL-ACYC; K3 and TAU3 every genome], so ESC3 and W3 are signed for acyclic Ξ-graphs only.
  - R117's line states S3-START and PAD inside REACH3, «for every G with an ACYCLIC Ξ-graph».
  - The every-genome forms of ESC3 and W3 are P-N5-XICYC §7's re-reading, which this report signed (§3.1, with XC-3 closed by
    Lemma K2-r). So «CONDITIONAL on … ESC3, W3 for every genome» states the remaining condition exactly: the every-genome forms of
    ESC3 and W3 are not a landed result.
  - Dropping «not landed» is right, since R117 has landed.
  - The rest of the clause (σ̄(K2) = r in the fixes; the [1E-N3] premise) is unchanged from L-3.
- R6: CORRECT. docs/referee/scratch/xicyc_logs/brseg_gen191_H0fail_2000_3_12.out exists at 42648076 and prints «INSTR H0-failing steps
  388 of 2072». «with one counter added to brseg_gen191.py» is how it was made (§C).
- R7: CORRECT.
  - STRICT-G and PATH-G are this report's §2.2; Lemma K2-r is §3.2.
  - Both are restated in fixes entry 2.
  - «signed by both referees»: this report's §C closes XC-2 and XC-3. REFEREE-2's Addendum 1 (claude/referee-2,
    docs/referee-2/R2-P-N5-XICYC.md l. 189-197) signs BR-SEG-G and RED-XI with STRICT-G / PATH-G and accepts K2-r. Read after my
    reports were pushed.
- R2-R5: CORRECT.
  - R2: the fixes file is named with its entries.
  - R3, R4: the proof lemmas and the T3 / C bounds carry no counter.
  - R5 is a wording fix.
- Verdict: L-4 MATCHES, by the byte test and in meaning. All statements stay as signed in §C.
