# R-P-ACYC: REFEREE report on P-ACYC (L-SI successor 43, box 81)
REFEREE successor 28 (Opus 5.5, D15). Written from 2026-11-08T00:47Z (date -u). The header time of record is the commit time.
The packet is frozen at claude/l-si e3ac4b06. I did NOT read docs/referee-2/ for this report.

## 0. Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §0 | premises: R104 (definitions), R117 (Γ3 definition), R118 [VJ], (a), (d), (j), (k), (l), scope; R15's object; SPEC S4 / S4c | all LANDED on trunk 37a4855e; every quote verbatim and in the entry it names (script) |
| §1 | facts [RANK], [CORE], [cX]; FROZEN FRAME | CORRECT (re-derived from R104's and R117's quoted text) |
| §1 | FIRST FALLBACK (definition) | CORRECT against SPEC S4 / S4c (optional AC-5) |
| §2 | Lemma BETA-ACYC on Γ(G) and on Γ3(G) | SIGN |
| §2 | Lemma LAMBDA-CONST | SIGN WITH GAP LC-1 (the proof never fixes w* = K1; with w* = K2 the statement would be false at K1; repair below) |
| §3 | Theorem ACYC-LIN (C = R = 0, T_CYC ≤ N) | SIGN WITH GAP LC-1 (R = 0 at K2 rests on «a fixed deterministic rule», which needs a unique optimum; repair below). Required data wording AC-2 |
| §4 | Corollary ACYC-XI | SIGN as PROVED-CONDITIONAL on R118 (k) and (l), WITH GAP LC-1 (inherited; on Γ3 it can also be closed by (k)'s own Lemma K2-r) |
| §5 | READING | header Scope sentence and §5's last bullet OVERREACH (AC-3, required text); AC-4 (required, minor) |
| §6 | DATA | every replayed count EQUAL (own engine); check81.sh re-run PASS |
| L-1 | line | NOT YET: AC-L1 to AC-L5 required (premises; DATA scope, units and sets) |
| §7 | TARGET.md diff | CLEAN |

LC-1 is a proof gap with a one-line repair. No conclusion changes. With the repair in a fixes entry, LAMBDA-CONST, ACYC-LIN and
ACYC-XI become SIGN; ACYC-XI stays PROVED-CONDITIONAL.

## 1. Objects
- Frozen commit claude/l-si e3ac4b06f13cd0c7c7ac4589b0c5824bf41ca5a7. `git merge-base --is-ancestor e3ac4b06 origin/claude/l-si`: true.
  Checked out as a worktree.
  - docs/si/P-ACYC.md: sha1 0e9edcfda3e3a68dee63ff01427d526b14c67bc4, 16,852 B (`git show | sha1sum`, `wc -c`). This EQUALS the
    brief.
  - docs/si/P-ACYC-line-L1.txt: sha1 bb12deec6fb0129b4ea9f5af7dd96d6302c5ca50, 2,085 B. This EQUALS the brief. Parentheses
    balance 27 / 27.
  - experiments/si/box81/pacyc.sha1 pins both files. I re-ran box81/check81.sh at the frozen commit: exit 0, «box 81 checks: PASS»
    (scratch/acyc_logs/check81_rerun_e3ac4b06.out).
- Trunk: docs/RESULTS.md on my branch is byte-equal to trunk 37a4855e (cmp).
- My tools (docs/referee/scratch/; logs in acyc_logs/):
  - acyc_replay.py: Howard on IDEAL-CYC(Γ) and IDEAL-CYC(Γ3) with every counter of §6, plus three counters the lane does not have
    (lamfail, eplay, brute force).
    - It runs on successor 26's own VJ engine xicyc_vj.py and Γ / Γ3 builder xicyc_replay.build, written from R104's and R117's text.
    - No lane code is used in any counter. Set A is reproduced by importing lemma81.agen, which is the set's definition.
  - acyc_xi.py: Corollary ACYC-XI along N5′-xi on Γ3.
    - N5′-xi itself is L-NEW's box190 n5v.py (byte copy in box81/ref/, pinned). I have no second N5′-xi.
    - Everything else is mine: builder equality, S3-START, standard states, the first-fallback index, and equality with my own Howard
      run.
  - acyc_quotes.py: every «…» of the packet, searched in trunk RESULTS (joined lines, per entry) and in trunk SPEC.
  - acyc_tn.py, acyc_depth.py: T / N and T against the level count d.
  - acyc_linefix.py: applies AC-L1 to AC-L5 to L-1.

## 2. Premises (§0, task 3)
- acyc_quotes.py (acyc_logs/quotes.out) finds 29 «…» in the packet.
  - 27 are found verbatim, each in the entry the packet names:
    - R104: genome, Ξ-graph, game, start (4);
    - R117: Γ3(G) (1), and §5's REALIZE quote (1);
    - R118: [VJ] order, σ̄, (a) game / Howard step / T_CYC / C / R, (d), (j), (k) form / T3 / fallback / premises, (l) applies /
      bound / fallback, scope (17), and §1's «non-mover Even vertices frozen in standard states» (1);
    - R15: the SPEC object (1);
    - SPEC docs/new/N5-ssi-global.md: S4 and S4c (2).
  - The other two are not premises:
    - «Freeze a short packet P-ACYC» is the Lead's brief.
    - «Polynomial only on a restricted class … » is TARGET.md §4 l. 31 (verbatim, checked by grep).
  - The lane's count «28 of 28» covers the same 28 non-brief quotes.
- Every premise is LANDED:
  - R104, R117 and R118 are [refereed-only] entries on trunk at l. 9864, 13362 and 13607.
  - SPEC is R15's object («N5 "SSI-GLOBAL" as specified in docs/new/N5-ssi-global.md»), at SPEC l. 50 and l. 56-57.
- What each premise is used for:
  - R118 (g) ONEP-POLY and Lemma K2-r are not used. LC-1's repair below needs one fact that both of them state («K2's optimal choice
    is unique: node K1 beats node K2 for Odd by reward»; σ̄(K2) = r on Γ3). The repair re-proves that fact in one line, so no new
    premise is needed.
  - [1E-N3] enters only through (k), as the packet's §4 says.

## 3. Definitions and facts (§1, task 2)
- [RANK]: CORRECT. Priorities from R104's text:
  - movers 0, gates 1, unused loop 2, K2 3, K1 5;
  - β = 6 + 2·rank + parity ≥ 6;
  - every e is even and above every β;
  - c_W = top, the least even number ≥ 2 above every other priority;
  - K0 = top + 2 (even), K3 = top + 3 (odd).
  - R117's pads have priority ≤ 2.
  - VJ relevance is by (priority, index), so ties play no role.
- [CORE]: CORRECT. K0 → {K1, K3}, K1 → {K0, K1}, K2 → {K1, K2}, K3 → {K1, K2}: no edge leaves the core.
  - With the frozen frame (K0 → K3, K1 → K1, K3 → K2; on Γ3 K0 → pA → K3, K1 → s → K1, and q, r are pads of core edges), the only
    edge into the core from outside is β → u, or β → pb_g → u on Γ3.
- [cX]: CORRECT (no in-edge in R104's edge list).
- FROZEN FRAME on Γ3:
  - Agrees with R117's transport (pA, s on the frozen edges; pb_g only on β_g → u; K3 → K2 unpadded).
  - My builder's transported start equals N5′-xi's S3 state 0 off the movers on all 309 genomes (s3startdiff 0; R117 S3-START).
- FIRST FALLBACK against SPEC:
  - S4 l. 50: «one iteration = one pass with Iσ ∪ Iτ ≠ ∅».
  - S4c l. 56: «c. FALLBACK, if σ_new = σ and τ_new = τ».
  - The packet's «Iteration k … is the k-th pass of SPEC S4 … a FALLBACK iff S4c applies in it: σ_new = σ and τ_new = τ after S4a and
    S4b» is the same notion. A pass with Iσ = Iτ = ∅ is S5's stop, not a pass that S4 makes, so «k-th pass» = «k-th iteration».
  - Consistent with R118 (k) «transition T3 + 1 is an S4c fallback» and (l) «comes at iteration T3 + 1».
  - AC-5 (optional): write «the k-th iteration of SPEC S4 (one pass with Iσ ∪ Iτ ≠ ∅)».

## 4. Proofs (task 1; each step re-derived)
### 4.1 Lemma BETA-ACYC: SIGN (on Γ and on Γ3)
- (1) The τ′-play from a gate:
  - every β → mover step is a Ξ-edge xt(x, σ(x)), so the movers met form a Ξ-path;
  - acyclicity makes the path finite, so it ends at a β whose target is X, then u;
  - by [CORE] it runs K0 → K3 → K2 → σ̄(K2) into the K1 loop or the K2 loop;
  - its prefix holds K0 and K3, no e, and not c_W (c_W has only its loop).
  - Correct.
- (3) A cycle with no e and no K vertex alternates mover → (m) → gate → (pβ) → β → mover. That is a Ξ-cycle: impossible.
  Correct.
- (4) A cycle that meets an e has its most relevant vertex among the e's: K's are unreachable from it (closed core), and c_W is only a
  self-loop. That vertex is even, so its reward beats any odd cycle node, and Ω_σ̄(g) ▷ Ω_τ′(g). Correct.
- (5) Both plays end in w* = Λ under σ̄(K2) (τ′ keeps σ̄(K2)).
  - Both Π-sets contain K0 and K3. Neither contains c_W. Pads, gates and movers (≤ 2 < 3) are in neither.
  - β's (≥ 6 > 5) can be in both, but every e is above every β.
  - π contains e_g and the τ′-play contains no e, so the top of the symmetric difference is an e of π, which is even. Hence
    Ω_σ̄(g) ▷ Ω_τ′(g), against pointwise optimality. Correct.
  - The packet does not name the β's in the Π-sets. That changes nothing, because e > β.
- The second clause (no e on a play from a non-e vertex) follows from (1) and the β-faces. Correct.
- Consequence used later: every optimal counterstrategy takes the β-face, so σ̄ is unique at the gates whatever the rule.
- Own DATA:
  - eplay 0: (state, vertex) pairs whose (σ, σ̄)-play from a non-e, non-pe vertex meets an e. 0 on 768 states of set A and 44 of B,
    on Γ and on Γ3; 861 / 1,534 on CONTROL.
  - nonstrict 0 (the β-face strictly better for Odd).
  - Brute force over all Odd strategies: 0 value differences on 305 states with M ≤ 12.

### 4.2 Lemma LAMBDA-CONST: SIGN WITH GAP LC-1
- The vertex list is right in substance: c_W for c_W, for the level-0 e's and for their pe pads; the unused loop for itself; for every
  other vertex, the cycle node of the core.
- LC-1 (gap, required repair).
  - BETA-ACYC (1) (l. 96) leaves w* := «K1 if σ̄(K2) leads to K1, else K2».
  - LAMBDA-CONST then says «w* for every other vertex» (l. 117), which includes K1.
    - In the K2 branch Λ(K1) = K1 ≠ K2 = w*, because K1 is frozen on its loop.
    - So the statement holds only if that branch never happens, and the proof never shows this.
  - The proof's reason for constancy (l. 123-124) is «Odd's optimal choice at K2 does not depend on σ. Under a fixed deterministic
    rule it is the same in every state».
    - That needs a unique optimum. A rule that reads σ could pick differently between two tied optima in different states.
  - Repair (one line, from §0 only):
    - From K2, Odd's two choices give the cycle nodes K1 (priority 5, odd) and K2 (3, odd). For Even an odd cycle node of higher
      priority has lower reward, so K1 is strictly better for Odd.
    - Hence σ̄(K2) is unique: K1 on Γ, r on Γ3 (the cycle K1 → s → K1 has node K1).
    - So w* = K1 in every state, and the K2 branch is void.
    - This is R118 (g)'s O-1 sentence and Lemma K2-r. The repair re-proves it, so no new premise is needed.
- With the repair: SIGN.
- Own DATA lamfail 0: states where some vertex's cycle node differs from the repaired prediction (c_W / cX / K1). 0 on all 768 + 44
  states on Γ and on Γ3, and 0 on 3,842 states from random starts.

### 4.3 Theorem ACYC-LIN: SIGN WITH GAP LC-1
- C = 0 follows from LAMBDA-CONST.
- R = 0 needs σ̄ constant at every Odd vertex:
  - the gates by BETA-ACYC (unique);
  - K2 by LC-1's repair (unique). The packet's «at K2 the same choice (LAMBDA-CONST's proof)» inherits LC-1.
- With every step a p-step, R118 (d) gives T_CYC ≤ N.
- «Every start mover state» is in R118 (d)'s scope:
  - (a) and (d) fix no start (P-N5-XICYC §2: «A state σ_t is the start off the movers plus a choice at every mover»).
  - Equivalently, the run from σ_0 is the run of IDEAL-CYC(G′), where G′ is G with its start replaced by σ_0. Γ(G′) = Γ(G), since the
    start enters no priority of Γ, and G′ is Ξ-acyclic.
  - AC-6 (optional): say so in the proof.
- AC-2 (required, packet text l. 133). «The bound is attained: T_CYC = N on some genomes of §6's set A (max T/N = 1.0)» is true only
  at N = 1.
  - Set A has 16 genomes with N = 1, and T = N on 10 of them. Over N ≥ 2 the maximum is 0.8 (N 5, T 4) (acyc_tn.py,
    acyc_logs/agen_TN.out).
  - Replace it with: «T_CYC = N occurs in set A only at N = 1 (10 runs); over N ≥ 2 the largest T_CYC / N is 0.8 (N 5, T 4).»
- Own DATA:
  - T_gt_N 0 and R 0 on sets A and B (both models).
  - From 5 random mover starts per set-A genome (1,500 runs, 3,842 states): T_gt_N 0, C 0, R 0, notbeta 0.
  - T_CYC ≤ d + 1 (d = number of levels) on all 1,500 runs, with T > d on 16 (acyc_depth.py). This is DATA only, no claim. It
    suggests T_CYC is governed by depth, not N.

### 4.4 Corollary ACYC-XI: SIGN as PROVED-CONDITIONAL on R118 (k) and (l), WITH GAP LC-1 (inherited)
- By (k), states 0 … T3 are standard, and their mover parts form a Howard run on Γ3. Standard states are R117's transported start off
  the movers, which is the frozen frame on Γ3.
- BETA-ACYC and LAMBDA-CONST on Γ3 give C = R = 0 for (l)'s counts. (l) then gives T3 ≤ N and the first fallback at T3 + 1. Correct.
- On Γ3 LC-1 can also be closed by (k)'s own premise Lemma K2-r (σ̄(K2) = r in every standard state).
- The condition is stated correctly in §4: [REACH-L] is signed in R117's entry (S3-START, PAD, K3, TAU3 for every genome; ESC3, W3 for
  acyclic), plus Lemma K2-r and [1E-N3] as in (k). L-1's premise wording is incomplete here (AC-L2).
- Own DATA (acyc_xi.py, N5′-xi = L-NEW n5v, A ∪ B = 304 genomes):
  - builder differences 0, S3-START differences 0, no fallback 0, non-standard states 0;
  - k1 ≠ own-Howard T + 1, or mover sequence ≠ own Howard, 0;
  - k1 − 1 > N 0; max (k1 − 1)/N 1.0 on A, 0.25 on B.
  - B: k1 = 10, 13, 11, 10 (EQUAL to §6).

## 5. L-1 (task 5: the DATA rule clause by clause; premises)
| clause of L-1 | counter in L-1 (unit, set, scope) | finding |
| --- | --- | --- |
| BETA-ACYC, β-face | σ̄ off the β-face, (state, gate) pairs, A ∪ B, IDEAL-CYC and Γ3 | OK; scope (stored start / S3) not stated → AC-L3 |
| BETA-ACYC, no e on non-e plays | none | missing → AC-L3 (no-DATA entry, or my eplay counter, Form B) |
| LAMBDA-CONST | C 0 (steps with a Λ change) | OK |
| ACYC-LIN | C 0, R 0, runs with T_CYC > N 0, IDEAL-CYC | the start is unstated and the theorem covers every start → AC-L3 |
| ACYC-XI | non-standard states 0, genomes with first fallback after N + 1 0 | «no fallback» excluded silently (pacyc81.py skips it); «= T3 + 1» and the R117 comparison have no entry → AC-L4 |
| control | 121, C 15, R 25 | set unnamed; model, states and unit missing → AC-L5 |
| premises | SPEC S4c used, not listed; (k)'s premises cited as R117's only | AC-L1, AC-L2 |

Required changes. Each old string occurs exactly once in L-1, and no two overlap (acyc_linefix.py, acyc_logs/linefix.out):
- AC-L1
  - old «the order ⊴ and σ̄ of R118 [VJ]):»
  - new «the order ⊴ and σ̄ of R118 [VJ]; for the corollary's iterations and fallback, SPEC S4 and S4c, RESULTS R15's object):»
- AC-L2
  - old «PROVED-CONDITIONAL on R118's REACH3-CYC, whose premises RESULTS R117's entry signs for acyclic Ξ-graphs)»
  - new «PROVED-CONDITIONAL on R118's REACH3-CYC, whose [REACH-L] premises RESULTS R117's entry signs for acyclic Ξ-graphs, with Lemma
    K2-r and [1E-N3] as listed in R118 (k))»
- AC-L3
  - old «L6Z_KILL238_d28 (44 states), σ̄ off the β-face in 0 (state, gate) pairs, C 0, R 0, runs with T_CYC > N 0 (lemma81.py,
    IDEAL-CYC)»
  - new «L6Z_KILL238_d28 (44 states), each run from the genome's stored start (IDEAL-CYC) or from S3 (Γ3), σ̄ off the β-face in 0
    (state, gate) pairs (BETA-ACYC's no-e-vertex clause: no separate DATA), C 0, R 0, runs with T_CYC > N 0 (lemma81.py, IDEAL-CYC;
    ACYC-LIN from other mover states: no separate DATA)»
- AC-L4
  - old «genomes with first fallback after iteration N + 1 0;»
  - new «genomes with no fallback 0, genomes with first fallback after iteration N + 1 0 (k = T3 + 1 is R118 (k)'s own clause, and N5's
    L(G) is R117's: no separate DATA);»
- AC-L5
  - old «control, five Ξ-cyclic genomes: σ̄ off the β-face 121, C 15, R 25»
  - new «control, five Ξ-cyclic genomes rd2_d3, rd2_d4, rd3_d3, rf_d4, RS2 (59 states; the same counts on IDEAL-CYC and along N5′-xi on
    Γ3): σ̄ off the β-face in 121 (state, gate) pairs, C 15, R 25»
- (The «new» strings above are wrapped for reading. The exact strings, one line each, are in acyc_linefix.py.)
- L-1 with AC-L1 to AC-L5 applied: sha1 c8ed32a8424ac126f0280c897962cca139ce6d79, 2,638 B, parentheses 36 / 36
  (acyc_logs/L1_with_AC.txt).
- DATA rule on my own new texts:
  - «no fallback 0»: pacyc81 «nofallback 0» on A and B; mine «nofb 0».
  - «59 states», «121», «C 15», «R 25»: pacyc81_cyclic_control.out and lemma81_cyclic_control.out; mine control.out (G and G3), and
    acyc_xi notequal 0, so the N5′-xi states are the Howard states.
  - The control names come from check81.sh's lemma81 / pacyc81 command lines.
  - The rest of the new text is no-DATA entries.
- Form B (optional, either form accepted). Instead of AC-L3's two no-DATA entries, cite my counters:
  - «(BETA-ACYC's no-e-vertex clause: 0 (state, vertex) pairs, REFEREE R-P-ACYC, docs/referee/scratch/acyc_logs/agen_300_7.out and
    towers.out)»;
  - «(ACYC-LIN from other mover states: runs with T_CYC > N 0, C 0, R 0 in 1,500 runs, five random starts per set-A genome, REFEREE
    R-P-ACYC, docs/referee/scratch/acyc_logs/starts_300_7_5.out)».

## 6. §5 READING (task 4)
- The reading «tower families bear on N5 (S4a root-first key) only; N5′-xi's mover phase is ≤ N on Ξ-acyclic genomes» is CORRECT in
  that form:
  - R117 realises L(G) as N5's FL run from S3 on acyclic genomes, which is the tower route's whole domain (R104 is «on acyclic Ξ-graphs»).
  - §4 caps N5′-xi's mover phase at N there.
- AC-3 (required, packet text l. 10-11 and l. 154-156). Two sentences say more than is proved:
  - Scope: «Hence a super-polynomial tower family would bear on N5 only, and N5′-xi lower bounds need Ξ-cyclic genomes.»
  - §5: «For N5′-xi to be slow, R must grow (R118 (l)'s equivalence), and R = 0 on every Ξ-acyclic genome. So a candidate counter for
    N5′-xi must have a Ξ-cycle.»
  - R118 (l)'s equivalence concerns «N5′-xi's FL run on Γ3(G)», the mover phase, only. The packet itself leaves the iterations after
    the first fallback unbounded (§4 «Not claimed»), and games that are not of the form Γ3(G) are not covered at all.
  - Replace the Scope sentence with: «Hence a super-polynomial tower family would bear on N5's FL run, not on N5′-xi's mover phase; a
    genome family on which N5′-xi's mover phase on Γ3(G) from S3 is super-polynomial must have Ξ-cycles.»
  - Replace §5's last two sentences with: «For N5′-xi's mover phase on Γ3(G) to be long, R must grow (R118 (l)'s equivalence), and R = 0
    on every Ξ-acyclic genome. So a genome family with a long N5′-xi mover phase must have Ξ-cycles; the iterations after the first
    fallback, and games not of the form Γ3(G), are not covered.»
  - L-1 is already correct here («N5′-xi's mover phase is linear in N»; «nothing is claimed about iterations after the first fallback,
    about Ξ-cyclic genomes»).
- AC-4 (required, minor, l. 149). «its FL run has length exactly L(G)» should be «… exactly L(G) if L(G) ≥ 1 (no FL run if L(G) = 0)»,
  as R117 says.
- «The two algorithms differ only in S4a's tie rule»: CORRECT (R118's premise text: N5′-xi is SPEC S1-S5 «with ONE change in S4a»).

## 7. DATA replay (task 5; own engine)
| packet §6 item | packet | mine (log) |
| --- | --- | --- |
| A, IDEAL-CYC: states / notbeta / nonstrict / C / R / T>N / max T/N | 768 / 0 / 0 / 0 / 0 / 0 / 1.0 | EQUAL (agen_300_7.out, G) |
| B, IDEAL-CYC | 44 / 0 / 0 / 0 / 0 / 0 / 0.25 | EQUAL (towers.out, G) |
| A, B on Γ3 along N5′-xi: notbeta / nonstd / no fallback / k1−1>N | 0 / 0 / 0 / 0 | EQUAL (agen_300_7.out G3, xi_agen_300_7.out, xi_towers.out) |
| B: k1 for N = 40, 48, 56, 56 | 10, 13, 11, 10 | EQUAL (xi_towers.out) |
| CONTROL: notbeta / C / R / runs T>N (59 states) | 121 / 15 / 25 / 4 | EQUAL on Γ and Γ3 (control.out, xi_control.out) |
| Γ3 mover phase = IDEAL-CYC Howard state for state | 12 of 12 (real81.py) | mine: Γ3 Howard = Γ Howard on 300 + 4 + 5 of 309; N5′-xi = own Howard on 309 of 309 |
| §0 quotes | 28 of 28 | 27 found by script plus TARGET l. 31 by grep (§2) |
| T_CYC = N attained | «some genomes of set A» | only at N = 1 (AC-2) |

All Ξ-acyclicity labels were checked with my own DFS: A 300 / 300 acyclic, B 4 / 4, CONTROL 0 / 5.

## 8. TARGET.md diff (§7): CLEAN
- No statement has the M4 form of TARGET.md §2 («for every parity game G, A on input G halts within p(n + m) steps and outputs the pair
  (W_E(G), W_O(G))»).
- Every statement is about Howard steps on IDEAL-CYC(G) or N5′-xi's mover phase on Γ3(G), for Ξ-acyclic genome games: a restricted
  class (TARGET.md §4 l. 31).
- No iteration total, no bit cost (§3) and no output correctness is claimed. Not M3, not a gauntlet step (§5). G-N5-TIME stays OPEN.
- §7's quotes and paraphrase of TARGET.md are accurate.

## 9. What I need
- L-SI: a fixes entry with:
  - LC-1's repair (§4.2);
  - AC-2, AC-3, AC-4 (packet text);
  - L-2 = L-1 with exactly AC-L1 to AC-L5 (or Form B for AC-L3's two no-DATA entries). Expected sha1 c8ed32a8… for the plain
    AC-L1 to AC-L5.
  - Optional: AC-5, AC-6.
- Me: a byte test of L-2 and a check of the fixes entry.

## §C. Fixes entry 1 and line L-2 (REFEREE successor 28; date -u at writing 2026-11-08T02:37Z)
After my verdict (d3d0a600) I read REFEREE-2's items only as they are quoted in the fixes entry and byte-copied in fix1/.
- Objects: claude/l-si 01a68edc (ancestor of origin/claude/l-si), read by `git show` / `git archive`:
  - packet docs/si/P-ACYC.md 0e9edcfd…, 16,852 B, and L-1 bb12deec…, both unchanged;
  - docs/si/P-ACYC-fixes.md dd3d4546…, 10,104 B (entry 1);
  - L-2 docs/si/P-ACYC-line-L2.txt 3a3096a45df6ca22e8099ca4e1a9ac1779c1321e, 2,741 B (EQUAL to the Lead's relay), parentheses 38 / 38.
  - fix1/ref_d3d0a600.md is byte-equal to my report at d3d0a600 (cmp).
- Byte test (scratch/acyc_l2.py, which reads my strings from acyc_linefix.py; acyc_logs/l2_bytetest.out):
  - L-1 + my AC-L1..AC-L5 = c8ed32a8…, 2,638 B, my prediction. This is EQUAL to the lane's statement.
  - I rebuilt L-2 from L-1 with five replacements, each old string once in L-1:
    - AC-L1, AC-L2, AC-L3 verbatim;
    - REFEREE-2's longer old string «σ̄ off the β-face 0, non-standard states 0, genomes with first fallback after iteration N + 1 0;»
      (which contains my AC-L4 old string) → «σ̄ off the β-face 0, states that are not standard (σ off the movers and τ) 0, » + my AC-L4
      new string;
    - my AC-L5 new string with REFEREE-2's D-3 insertion «; e-priorities ordered by (lev, gate index), as in ref gamma3.build» before
      its first «)».
  - The result is byte-equal to L-2 (sha1 3a3096a4…, 2,741 B).
  - My strings in L-2:
    - AC-L1, AC-L2, AC-L3 and AC-L4 new strings occur once each, whole (AC-L4 as the tail of the combined string).
    - AC-L5's new string occurs with the D-3 insertion only, as intended.
    - All five old strings occur 0 times.
- Packet-text items: every «Old» of entry 1 occurs once in the frozen packet (scratch/acyc_f1old.py, acyc_logs/f1_old.out: 11 of 11).
  - F-1 (LC-1): CORRECT.
    - The new proof step decides K2 by the cycle nodes K1 (5) and K2 (3), concludes that the optimum is unique toward K1 (r on Γ3) and
      that w* = K1, and says why «w* for every other vertex» needs it.
    - ACYC-LIN's R = 0 now cites «the unique optimal choice».
    - LC-1 is CLOSED for LAMBDA-CONST, ACYC-LIN and ACYC-XI.
  - F-2 (AC-2): my text, verbatim. tn81.out agrees with my agen_TN.out (10 at N = 1; 0.800 at N 5).
  - F-3 (AC-3, reconciled with REFEREE-2): CORRECT.
    - «C + R» is more exact than my «R». (l)'s bound is in C and R, and both are 0 on acyclic genomes by ACYC-LIN.
    - Every overreach I named is removed.
    - AC-7 (optional): (a)'s «N5′-xi's mover phase (its first N + 1 iterations)» counts the fallback iteration into the mover phase. By
      §4 the mover phase has at most N iterations, and the first fallback is iteration T3 + 1 ≤ N + 1. Better: «(at most N iterations;
      the first fallback comes at iteration ≤ N + 1)».
  - F-4 (AC-4): CORRECT.
  - F-5 (τ in the standard-state counter, «no fallback»): CORRECT.
    - My own counter (acyc_xi.py, extended): taubad = states 0..k1−1 whose τ differs from the standard τ (pe_g at every gate, K2 → K2).
    - Result: 0 on A (768 states), B (44) and the control (59); s3startdiff, nonstd and nofb are 0 on all 309 genomes
      (acyc_logs/xi_*_r1.out).
  - F-6 (AC-L5 + D-3): CORRECT. My builder orders the e's by (level, gate), and its control counts 121 / 15 / 25 on 59 states are
    EQUAL to the lane's.
  - F-7 (N-1, packet only): the quote «S1's σ̄, and τ̄ on the dual game, are pointwise optima» is verbatim in trunk RESULTS (l. 9864,
    R104; also l. 9977, 13742).
  - F-8 (D-4): CORRECT. My count of iterations after the first fallback to the S5 stop (N5′-xi = L-NEW n5v) is 2 on 300 / 300, 4 / 4
    and 5 / 5.
  - F-9 (AC-5, AC-6): my texts, verbatim.
- DATA rule on L-2, clause by clause:
  - the AC-L1..AC-L5 clauses as checked in §5;
  - the new «states that are not standard (σ off the movers and τ) 0», which matches pacyc81t's nonstd + taubad (unit states, sets A,
    B, scope states 0..k1−1) and my taubad;
  - the D-3 insertion is not a count.
  - MET.
- check81.sh at 01a68edc (git archive, includes fix1/check_fix1.sh): exit 0, «P-ACYC fix1 checks: PASS», «box 81 checks: PASS» (acyc_logs/check81_rerun_01a68edc.out).
- Verdict: fixes entry 1 CORRECT. L-2 MATCHES, by the byte test and in meaning.
  - Statements: BETA-ACYC SIGN; LAMBDA-CONST SIGN; ACYC-LIN SIGN; Corollary ACYC-XI SIGN as PROVED-CONDITIONAL on R118 (k) REACH3-CYC
    and (l) Corollary T3.
  - No gap remains open. AC-7 is optional (packet wording only; not in L-2).
