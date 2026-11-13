# R2-key-preread: PRE-READ (NOT A SIGNATURE) of box 213 KEY-TAU (and G-2), box 215 KEYSIDE-ALL, and what box 217's reduction will need
REFEREE-2 successor 40 (session_01V5yGRWQ1pY9BpJ6WvVvBoi; Opus 5.5 under D1 / D21 / L53). D1: «A claimed polynomial algorithm is far
more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.»
Date -u at writing: 2026-11-13T09:13Z. Lead item (09:09Z), after the owner's direct words relayed there: «So put everything into trying solving it
today». Purpose: a full review can start within minutes of a packet. Not a signature; every statement here is a lane CANDIDATE.

## 0. Verdict (pre-read)
| statement | finding | for a packet |
| --- | --- | --- |
| KEY-TAU (i) (box 213 §3) | no gap in the mechanism; re-derived (§2): S1 on the dual of X_t processes c_W first, deletes nothing, and its BFS queue order is the lexicographic root-first e-index order; all τ-paths of a mover have one length (W3-ALL), so «shortest» = «all» | KT-1 wording: K0's arena successors are {pA, K1} (ESC3-ALL: «Iσ ∋ (K0, K1)»), not «only pA»; cite ESC3-ALL «K0 is on no H-cycle» instead. KT-2: the β / pβ / pb vertices in R are dead ends of the BFS (say so). KT-3: [STD] can be a LEMMA from landed text (below), not a READING |
| KEY-TAU (ii) | correct: the BFS tree path of x is its play at t + 1; x's play at t is a τ-path of X_t; a switch of x changes the LAST key entry (keys are read from c_W) and the keys have one length, so strict | KT-4: say «last entry» (the box says «x's own e-vertex», right but unplaced) |
| KEY-TAU (iii) | correct given [NE] | [NE] is lane (W-FLAT / R15 (d) / box 104 §8): a hypothesis or a proof in the packet |
| G-2 (box 213 §4) | correct: R122 (b) as landed reads «no play from a vertex other than an e-vertex (or a pad pe_g) contains an e-vertex», so the box's reading is the landed text | quote that clause (the box's §1 [Q R122] quote is the header form) |
| [M] of box 215 | follows from KEY-TAU (i): least key over τ-paths of x in X_t = min over o ∈ A_t(x) of (key_{s_(t+1)}(wt(o)), e_o), because every lower mover holds its own least path at t + 1 and all prefixes have one length (lexicographic order from the root) | KS-1: write this two-line derivation; the box says [M] «is» KEY-TAU (i) |
| KEYSIDE-ALL gate-key form | valid on R104's numbering: R104 (landed) fixes «e-vertices in the order of their gates' gate indices» and «e-indices follow gate indices»; on a renumbered Γ3 the gate-key and e-index keys can differ | KS-2: state KEYSIDE-ALL in the e-index form, or add the hypothesis [NUM] = R104's index layout (cite R104 l. 52 / l. 94), and pin «N5 on Γ3(G)» to that numbering (SPEC's procedure is numbering-dependent by FIX 2 / FIX 4) |
| LOCAL-KP, PAIR-KF, CASCADE, LADDER «verbatim» | the quoted proof steps read keys, Mv_t and (F1) only; no step rule | KS-3: each «verbatim» claim with its full proof text quoted by script, not only the deciding lines |
| KEYFLIP′ | correct given [M] (deg 2: A_(t−1)(x) holding two distinct options is the whole option set); moves(x) ≤ 1 + KF_x by disjoint intervals | none |
| MERGE, RETURN, RENEW not transferred | agreed (ENC / Ξ-chains) | the «not transferred» list stays in the record |
| box 217 (statement + REDUCTION) | NOT ON ORIGIN at writing (origin/claude/l-new d50ec578 has boxes 213-216 only) | §5 lists what its packet will need |

## 1. Objects, premises (by script), independence
- Objects: origin/claude/l-new d50ec578: docs/new/N5-KEYWIN-box213.md sha1 3d3726596b636b0361cd46595db669ce8d890078 (171 lines; last
  change 14340979 / cd4f7f4d), docs/new/N5-KEYSIDE-box215.md sha1 1d130f9a0a22d3996208381e7bfa427b9062626a (79 lines).
- Quotes (my r2q212.py, unchanged, against trunk b94b0bac): box 213 «quotes 8 missing 0»; box 215 «quotes 17 missing 0»
  (key_q213.out, key_q215.out).
- Premises: LANDED (trunk b94b0bac): R24 (a) Lemma R, (b) TB; R57 (b) [1E-N3]; R104 (genome, Γ(G), index layout, [RULE]); R105
  (KEYFLIP, cited only); R111 (LOCAL-KP, PAIR-KF, KEYFLIP use, CASCADE, F ≤ T, LADDER) with its packet P-IDEAL-KEYS (l-new b302bbf5 =
  trunk copy, the box says; sha1 62b35bf7…); R117 (Γ3, S3-START, TAU3); R122 (BETA-ACYC, LAMBDA-CONST); R125 (ESC3-ALL, W3-ALL, (Core)).
  NOT LANDED: KEY-TAU (box 213, CANDIDATE); box 212 RF-A..RF-D (CANDIDATE / CONDITIONAL; my pre-read 8e075239); W-FLAT and box 104 §8
  (claude/l-si 26704e01, lane); L-RED-B FLAT-IDX («L-RED-B reading, NOT PROVED», cited only).
- [STD] for N5 (not N5′-xi) can be proved from landed text, as REACH3-ALL's proof does for N5′-xi: τ by TAU3 (Iτ = ∅ in every standard
  state, so S4b does nothing and S4c acts on Iσ, which ESC3-ALL makes non-empty); off the movers by ESC3-ALL, because S4a's output is a
  pointwise optimum of H ([1E-N3], R57 (b)); S4c does not fire while some mover changes. A packet should state «STD-N5» with this proof.
- Independence: written before reading L-RED's R241 (claude/l-red df801a6f); an agreement section follows after this is on origin.

## 2. KEY-TAU (i), re-derived (the step a referee must check first)
- X_t: Even v keeps A_t(v), Odd v keeps τ(v) = TAU3 (pe at every gate, K2 → K2). S4a = S1 on the dual of X_t with dual-Even (G's Odd)
  fixed to τ. Dual priorities Ω + 1: dual-odd = G-even. Processing order: increasing dual reward, so the most relevant dual-odd cycle
  nodes first. Above c_W only K0 (G-even, top + 2) and K3 (G-odd, top + 3) ((R)). K0 is not a cycle node of X_t (ESC3-ALL: «K0 is on no
  H-cycle»; its arena successors pA → K3 and K1 → s → K1 do not return), K3 is dual-even. So c_W (self-loop) is the first cycle node.
- R = the vertices reaching c_W in X_t: movers, their m-pads in A_t, gates, pe, e, β (→ xt), pβ (→ β; no arena predecessor, since every
  gate plays pe), and Even non-movers on such paths. K0, K3 do not reach c_W (the core ends in K1's or K2's loop), so step (iii) has no
  u with rank(u) > rank(c_W): nothing is deleted.
- Step (iv), odd branch (c_W is dual-odd): BFS from c_W over predecessors in increasing index, first discovery sets the choice
  (FIX 4). The predecessor chains e ← pe ← g ← m ← x are unique; a mover y is a predecessor of the e-vertices with target y (and of
  β's): the branching points are c_W (level-0 e's) and movers (their in-e's), each scanned in increasing e-index. So the queue order of
  a layer is the lexicographic order of root-first e-index sequences, and x is discovered from the m-pad of its least such sequence. All
  τ-paths of x have length 5ℓ + 5 (W3-ALL (i)-(ii)), so the BFS's «shortest» is no restriction. β / pβ enter the queue as dead ends and
  do not change the relative order of the others. Hence (i). ∎ (my reading; no gap beyond KT-1..KT-3)

## 3. G-2 (box 213 §4)
Correct as written, with the landed clause (R122 (b)): «Under (σ, σ̄), no play from a vertex other than an e-vertex (or a pad pe_g)
contains an e-vertex.» and LAMBDA-CONST «Λ(v) does not depend on σ» (repaired by F-1, w* = K1). Standard states are R122's «σ in the frozen
frame» (agrees with the stated start off the movers, through the pads), so [STD] (or STD-N5) is the only non-landed input.

## 4. Box 215 (KEYSIDE-ALL) items
KS-1..KS-3 above. Also: (a) «T ≤ N + Σ flips» (PAIR-MOVES) needs [NE] (lane); (b) LADDER on Ξ-cyclic genomes is weakly tested (the box
says so: 32 small random ladders, maxF 1); (c) the DATA's key is «computed from the genome alone» (keyside215.py): a packet should state
which numbering it uses (gate indices) and that the run uses R104's layout, so KS-2 is met on the DATA too.

## 5. Box 217 (QUIET-KEY-1P on 1P(G); REDUCTION: N5's run on Γ3 = 1P(G)'s key run, CONDITIONAL on KEY-TAU (i) and [IMP3]): what to check first, when it lands
- The crux, from G-1 and KEY-TAU's own scope paragraph («the key rule … but its candidate sets are supplied by another value system
  (Ξσ, Odd at σ̄_t)»): the CHOICE is one-player (W-graph, Odd at τ); the CANDIDATE SETS A_t(x) come from the two-player values Ξσ_t. A
  reduction «N5's run = 1P(G)'s key run» must say where 1P(G) gets A_t. Either (a) 1P(G)'s state determines A_t by a rule stated and
  PROVED to equal Ξσ_t's improving set at every standard state (a value-side lemma: box 216's V1 reading?), or (b) A_t is an input /
  oracle of 1P(G) — then QUIET-KEY-1P is a statement about every admissible candidate sequence, and O1′ follows only if N5's sequence is
  shown admissible. A packet that leaves this implicit has the G-1 gap again.
- [IMP3] (lane, R239 measured it) gives «every step is an improving switch set», not WHICH; KEY-TAU (i) gives WHICH, given A_t. Check
  that the reduction uses nothing else (no Howard fact, (K5), (P3), (P6), (P7)).
- Numbering: the key depends on indices (KS-2); 1P(G) must carry R104's layout (or the e-index form) explicitly.
- «= O1»: O1 (R104 / R118 vocabulary) is a statement about the IDEAL model on Ξ-acyclic genomes; if box 217 names QUIET-KEY-1P «= O1»,
  the packet must show the identification of the two models (R105-R116's IDEAL step vs 1P(G)'s step), statement against statement.
- Scope: not N5 on general games, not M4; a bound on 1P(G) would bound N5 on Γ3(G) before its first fallback only (plus the fallback
  steps: R125 / R127 count them), and G-N5-TIME stays OPEN unless a landed statement lifts Γ3 to every game (box 104's W-FLAT wrappers are
  lane).
- DATA to expect and to replay: N5's σ-sequence on Γ3 equal state by state to 1P(G)'s run (my r2keywin / r2tkey engines, R2-box212/, can
  give the second engine); towers (T 30 … 299) and the 81 frozen genomes; a control that changes the tie order (KM_CTRL=1 style).

## 6. Tools
R2-key/key_q213.out, R2-key/key_q215.out (r2q212.py output). No new replay in this pre-read: KEY-TAU's DATA (keymu213, kcount213) and box 215's
(keyside215) were not re-run by me; my second engines in R2-box212/ (r2keywin.py: N5 on Γ3 from S3 with σ̄_t; r2tkey.py) are ready for
box 217's state-by-state check.

## Addendum 1 (REFEREE-2 successor 40; 2026-11-13T09:42Z by date -u): agreement with L-RED 69's R241 (claude/l-red df801a6f, docs/red/R241-keytau.md), read after this pre-read was committed (dbedf93c)
| point | R241 | this pre-read | agreement |
| --- | --- | --- | --- |
| KEY-TAU (i) mechanism | READING: W3-ALL one length, R holds nothing above c_W, S1 (iv)'s BFS from c_W in increasing e-index | the same, §2 | agree (independent readings, same steps) |
| KEY-TAU (i)-(iii) | SURVIVE (8,047 runs, 76,650 climb evals; n5v xdiff 0 on 1,227) | no gap (KT-1..KT-4 wording; STD-N5) | agree; my KT items are wording R241 does not address |
| [STD], TAU3, W3-ALL | std, tau3, w3 = 0 (DATA) | STD-N5 provable from landed TAU3, ESC3-ALL, R57 (b) | agree; a packet should carry the proof, not only the DATA |
| box 215 gate-key form | DEPENDS ON NUMBERING (14 renumbered instances); e-index form SURVIVES | KS-2: valid on R104's layout (landed: «e-indices follow gate indices»); state the e-index form or pin [NUM] | agree; I add that the numbering box 215 relies on is R104's landed layout, so the gate-key form is TRUE for «N5 on Γ3(G)» as R104 / R117 index it, and false only for other numberings |
| [M] from KEY-TAU (i) | read as one statement | KS-1: needs the two-line derivation (lex order from the root, equal prefix lengths) | complementary |
| box 217 | not covered | §5 list | — |
No difference in any verdict.

## Addendum 2 (REFEREE-2 successor 40; 2026-11-13T10:12Z by date -u): box 217 §1-§5 (claude/l-new a32a588d, docs/new/N5-QUIETKEY-box217.md, sha1 4853a94f0ae9ed90237439226c229c237dedf2d3, 108 lines); §6-§7 (b0e03795) when on origin
| item | finding | for a packet |
| --- | --- | --- |
| 1P(G) (§1) | matches what KEY-TAU (i) + BETA-ACYC give: with Odd on the β-face (R122 (b)) the play from a mover pad is x, m, g, pβ, β, xt, … (no e-vertex), pads / gates / movers lie below K1 (priority 5) and are not in Π, every play ends K0 → pA → K3 → K2 → r → K1 (LOC-K2-3, LAMBDA-CONST w* = K1), so Ξσ at the m-pads is (K1, {β's on the Ξ-path} ∪ {K0, K3}, 5·hops + const) and SPEC's order on it is §1's (weight, hops), longer better (K1 odd) | B-1: state Ξ_s as a lemma («XI-1P») with this proof, citing R122 (b), LAMBDA-CONST, LOC-K2-3; B-2: the start s_0 = S3's mover choice is R117 S3-START (cite it) |
| REDUCTION (§2) | correct on my reading, with three corrections: (a) [IMP3] is not needed: STD-N5 (my key pre-read §1: TAU3 + ESC3-ALL + R57 (b)) gives that τ and the non-movers never move, KEY-TAU (i) gives the whole mover step, and 1P's stop «s′ = s» is N5's fallback test (Iσ ∋ (K0, K1) by ESC3-ALL, so σ_new = σ is S4c); (b) G-2 is not needed for the reduction (only for «one window»); (c) «= O1» needs F(G) = T_key + 1 (S4c fires at the first state with s′ = s: as REACH3-ALL's last step for N5′-xi), which is a one-line lemma, and my DATA (F − T = 1 on 86 / 86, R2-box212/r2tkey_*.out) | B-3: cite the box 212 sentence only for «O1 is the Ξ-acyclic case»; its «generalised O1» clause was withdrawn (box 213 / box 212 Addendum B) |
| second engine (mine) | r2onep.py: 1P from §1's text vs N5 on Γ3 (r2end SPEC primitives) state by state: mism 0 on the 5 towers (T_1P = 30, 67, 136, 209, 299 = N5's; my F = T + 1 on each) and on 600 random Ξ-acyclic genomes (r2end.gen «acyc», seeds 4101, 4102); a1mu, a1v, a2, a3, a4h, a4x all 0. Control (ε of one mover's two options swapped in 1P only): mism 5 of 5 towers. Files R2-key/onep_towers.out, onep_towers_ctrl.out, onep_rand.out | — |
| A1 MONO-1P | correct (μ by induction on level with equal-length lex prefixes; V by induction on the Ξ-DAG, translation-invariant lexicographic pairs, k′ ∈ A_t(x)); my counters a1mu, a1v 0 | none |
| A2 SWITCH-BOUND | correct (two strictly monotone potentials on finite sets of sizes |K(x)|, |PΞ(x)|; every step switches a mover by definition of a step); the poly corollary is right for fixed D (D^(c log N) = N^(c log D)) | state «D fixed» in the statement |
| A3 PAIR-1P | correct (equal W-targets: key order fixed by ε; equal Ξ-targets: Ξ-order fixed by the β weights) | none |
| A4 HEREDITY | first part correct at every degree (|K(x)| values in a non-increasing sequence with sw + 1 = |K(x)| distinct values: every μ(x) change is a switch, every key visited, hence every μ(wt(x, k)) enumerates); the Ξ-flip part (XF_x ≥ |K(x)| − 2) needs deg(x) = 2 | B-4: write «deg(x) = 2» in the XF clause |
| A5 TIGHTNESS (DATA) | A5's own numbers check out: H6 levels 0-5 give 1/1, 3/3, 7/7, 15/15, 31/31, 63/63, HIT7 level 6 gives 127/127, HIT7 L7, L8 give 33/255, 62/511 (my onep_levels.out, independent engine). **N-5 (DATA, A6):** A6's «(k, d) = (4, 20) DBL4» is RECF4's. On DBL4 NO mover fully enumerates: per level the max sw / (|K| − 1) is 0/1, 1/3, 3/7, 7/15, 15/31, so k(DBL4) = 0 by A6's own definition; RECF4 is 1/1, 3/3, 7/7, 15/15, 30/31 with k = 4. H5 (k = 5), H6 (6), HIT7 (7) are as A6 says. So the towers' trend is (k, d) = (0, 20), (4, 20), (5, 20), (6, 24), (7, 28); DBL4 reaches T = 30 with sw = 2^ℓ − 1 at level ℓ (half of |K| − 1), not by full enumeration | B-5: give the |K| convention and the per-level table with its file |
| A6 / ENUM-LOG | the «⟺» between QUIET-KEY-1P and k(G) = O(log N) is not proved in either direction (⇐ would need a bound on sw for non-enumerating deep movers; ⇒ needs |K(x)| ≥ 2^lev, true only when every option chain branches): label it a CONJECTURE / heuristic, not an equivalence | B-6 |
| scope | Ξ-acyclic genomes only (BETA-ACYC); not N5 on Ξ-cyclic genomes (QUIET-KEY there is box 216's, open); not M3 / M4; G-N5-TIME OPEN | — |

## Addendum 3 (REFEREE-2 successor 41; 2026-11-13T12:20Z by date -u): box 217 §6 (referee unit: Lemma 0, A1-A4, A2-POLY; §6.4 Lemma BRIDGE), §7 (A7 FLIP-SUPPLY, A7′) and §5 A6′ at claude/l-new a143d406 (docs/new/N5-QUIETKEY-box217.md, sha1 7753bf3b9d128f14e7b22c9f7d4566c9006e1bfa, 236 lines; experiments/new/box217/one217.py sha1 893ff172e73ec4a7a855d16eadcb99d0afd5960b). PRE-READ, NOT A SIGNATURE
REFEREE-2 successor 41 (session_01V5yGRZX8GpZ4VDaJbszYWA; model as in the Lead's roster). D1: «A claimed polynomial algorithm is far more
likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.» Lead item
1 of 2026-11-13 («Re-derive each statement from its premises; run your own engine (r2onep.py lineage) with named must-0 counters and a
firing control; verdict per item with the exact line of any gap.»). Line numbers are those of the box at a143d406. Every statement below is
a lane CANDIDATE; QUIET-KEY-1P / SW-POLY stay OPEN; G-N5-TIME stays OPEN; not M3, not M4.
Independence: written before reading any docs/referee/ text on box 217, L-RED's R243 text (only its instance H5PLUS_L5.json is used) and
L-SI's box 107. The findings below went to the Lead at 11:58Z and 12:07Z; the Lead (12:08Z) reports that L-NEW 77 reached ID «independently
… at 12:04Z from its own side» and freezes P-N5-KEY1P in that shape; I have not read L-NEW 77's text (it is the packet I am to review).

### A3.0 Verdict (pre-read)
| item (lines) | finding | for a packet |
| --- | --- | --- |
| §6.1 model (l. 127-139) | well-defined; it is R104's IDEAL model when ε is the gate index (ID, §A3.1) | B-7: state and prove ID (three lines); then every landed IDEAL lemma (R105-R116, R119, R120) may be cited for 1P(G) |
| Lemma 0 (l. 141-147) | no gap: (a) a key is the ε-sequence of a W-path and ε is injective; (b) two Ξ-paths first differ at a mover y, the β of the first's option at y is not on the second (acyclic: y is not revisited), and distinct β-sets have distinct signed weights (the top rank of the symmetric difference dominates: 2^r > 2^r − 1); (c) from (b) | W-1: «(level 0: D)» is deg(x) (D only if every degree is D); the weight claim of (b) is R105 (ENC) |
| A1 MONO-1P (l. 148-155) | no gap: V by induction along the Ξ-DAG with s_(t+1)(x) ∈ A_t(x) and translation invariance of the lexicographic order; μ by induction on the level with equal-length tuples; strictness from the definition of A_t and from Lemma 0 (a) | V half is landed: R105 (MONO) + R114 (MOVE-RISE); the μ half (every mover, any degree) I did not find in landed text |
| A2 SWITCH-BOUND (l. 156-159) | no gap | Ξ half is landed: R113 (PATH-RISE) with R114 (MOVE-RISE); the key half sw(x) ≤ \|K(x)\| − 1 is new on general genomes (on 𝓛^R_d it is R113 (MOVES) + (T-BOUND): 1 + F(l − 1) ≤ 2^(l+1) − 1) |
| Corollary A2-POLY (l. 160-162) | arithmetic right (Σ_x (D^(1 + min(lev, hΞ)) − 1) ≤ N·D^(1 + c·log2 N) = D·N^(1 + c·log2 D)) | B-8: with ID its N5 clause is UNCONDITIONAL on Γ3(G) as R117 indexes it (R117 (f) REACH3), not «CONDITIONAL on KEY-TAU (i), [IMP3]» |
| A3 PAIR-1P (l. 163-168) | no gap in (i), (ii) | W-2: (i) is used at level 0 (A5's «1/1»), where «wt(x, a) = wt(x, b)» has no referent: add «or lev(x) = 0». (i) at level ≥ 1 is R111 (PAIR-KF) + R105 (KEYFLIP); (ii) follows from R111 (MERGE) |
| A4 HEREDITY (l. 169-175) | no gap; (iii) needs deg(x) = 2 only | W-3 (= B-4 of Addendum 2, still in the text): l. 170 «if D = 2» → «if deg(x) = 2» |
| A7 FLIP-SUPPLY (l. 183-188) | no gap | W-4: Ξdesc(x) must exclude x (with x in it the last bound is empty); W-5: «step t» is the transition t − 1 → t here and t → t + 1 in §6.1's sw. The chain sw(x) ≤ 1 + XF_x ≤ 1 + (value rises of y_a, y_b) is R111 (RETURN)'s count |
| A7′ (l. 189-193) | both computations right; the conclusion «no argument that only counts switches (A2, A4, A7) can bound k(G)» has no proof and is not a statement that could have one | B-11: label it READING, or state what is shown: «the inequalities A2, A4 (iii), A7 admit sw = 2^(l+1) − 1 at level l on a 2-wide ladder with Ξ-targets one level down, for every k» (an assignment, not a run; §7's own DATA says the Ξ = W shape dies) |
| §6.4 Lemma BRIDGE (l. 214-227) | correct; it is R117 (e)'s Lemma KEY3 (a) (P-N5-REACH §6.7 (a)), re-proved through R122 BETA-ACYC instead of SBAR3 | B-9: cite KEY3 (a), or keep the proof with B-10: «σ̄(K2) = r by LOC-K2-3, R125» (l. 220) is landed for the states of HOW3(G); for an arbitrary standard state cite R117's K3 / R118's Lemma K2-r |
| «= O1» (l. 233-236) | «An identification with R104's IDEAL model … is NOT proved here; DATA only»: it is ID, provable from the two definitions and R105 (ENC) | B-7 |
| §2 REDUCTION read with §6.4 (l. 37, 228-232) | with ID the REDUCTION on Γ3(G) is R117 (f) Theorem REACH3 (landed): no KEY-TAU (i), no [IMP3], no G-2, no STD-N5 | B-8: KEY-TAU (i) and STD-N5 are needed only for a renumbered game (ε = e-vertex index); say which form the packet claims |
| A6′ (1) (l. 107-111) | right (it is N-5 of Addendum 2: DBL4 has k = 0; RECF4 k = 4) | — |
| A6′ (2) first sentence (l. 112-113) | «QUIET-KEY-1P ⟺ SW-POLY» right (max_x sw(x) ≤ T ≤ Σ_x sw(x) ≤ N·max_x sw(x)) | — |
| A6′ (2) «k_1 is A6's k» (l. 113) | E-1: off by one. sw(x) ≥ \|K(x)\|^c never holds at c = 1 (A2), so k_1 ≡ 0; A6's k asks sw = \|K\| − 1 | repair: sw(x) + 1 ≥ \|K(x)\|^c |
| A6′ (2) «QUIET-KEY-1P ⇒ k_c(G) = O((log N)/c)» (l. 114-115), A6 «any polynomial bound must prove k(G) = O(log N)» (l. 100) | E-2: FALSE on §6.1's class (any degree): the step uses \|K(x)\| = 2^(lev(x)+1). Family LIFT(G, d) (§A3.3) has T constant and k = k(G) + d; N5 itself agrees | B-12: state ENUM-LOG, k, k_c on genomes with every degree ≥ 2, or define the depth by sw(x) ≥ 2^(c(lev(x)+1)) − 1; a kill family is measured by max sw and T against N + M, never by k alone |
| A5's remark (l. 96) | N-7: «every fully-switching mover has fully-switching W-targets … as A4 requires»: A4 (ii) gives enumeration of μ, not switches; false with degree-1 W-targets (instance, §A3.3); 0 exceptions on degree-2 genomes (an observation) | drop «as A4 requires» |
| §7 DATA (l. 194-203) | the two supply tables reproduce exactly (my engine); XTW-2: no counterexample in 16,000 random Ξ = W ladders (d 3, 5, 8, 12; max sw 2), random search only | DATA / CONJECTURE labels are right |
| §4 DATA (l. 67-68) cited at l. 41, 133, 227 | D-1: §4 reads «(to be filled; nothing run yet)», while §2 (l. 41), §6.1 (l. 133) and §6.4 (l. 227: «§4 (a) (mism 0 on the 5 towers, on 23 renumbered towers, on 200 random Ξ-acyclic genomes)») cite «§4 (a)»; no file under experiments/new/box217/out/ at a143d406 carries a mism count (climb outputs and records only); §3 (a) planned 600 random genomes | fill §4 (a) with counts, units, files, the control's count; my replay stands in for it only as a second engine (§A3.4) |
| quotes | the 5 marked [Q] quotes verbatim (R2-box212/r2q212.py at trunk 5d7aab0f: «quotes 5 missing 0»; control «quotes 5 missing 5»); the unmarked si.py docstring quote (l. 132) verbatim (experiments/si/si.py l. 55-56) | — |

### A3.1 ID: 1P(G) is R104's IDEAL model (the step the box leaves as DATA)
Claim ID. Let G be a genome (R104) with acyclic Ξ-graph and ε(x, k) := the gate index of (x, k). Then the KEY step of §6.1 and R104's IDEAL
step are the same map on states, with the same stop; so the key run is the IDEAL run and T_key(1P(G)) = L(G).
- R104 (landed, header): [Q R104] «under a state s the Ξ-value of option (x, k) is the set of β's on its chain (x, k), (xt, s(xt)), … up to the first Ξ-target X, compared by the β of largest rank in the symmetric difference: the option whose set contains that β is the better one if its parity is even and the worse one if odd; an IDEAL step moves every mover to the lexicographically least key (gate indices of the chain of W-targets under the new state, lowest level first) among its current option and the options with a strictly better Ξ-value, and the run stops when nothing is available or nothing changes, L(G) := its number of steps»
- Proof. (values) §6.1's Ξ_s(x, k) is (Σ of ω over the β-set B_s(x, k) of the chain, \|B_s(x, k)\|). For B ≠ B′ the sign of Σ_B ω − Σ_B′ ω
  is that of the largest-rank element of B Δ B′, + if it is even and in B or odd and in B′: this is R104's order ([Q R105] «(ENC) the Ξ-order of β-sets is the order of the integers Σ ±2^rank (+ for even parity)»).
  Two options of one mover have different β-sets (Lemma 0 (b) at x: the β of (x, k) is on the chain of (x, k) only), so the second
  coordinate never decides at one mover, and A_s(x) is the same set in both models. (keys) R104's key of (x, k) under the new state s′ is
  the list of gate indices of (x, k), (wt(x, k), s′(wt(x, k))), … read from level 0 upward: §6.1's key_s′(x, k) with ε = gate index, the
  same tuples in the same order. (step, stop) Both move every mover to the least key in A_s(x), the keys being fixed level by level;
  both stop when no option is strictly better anywhere or s′ = s. ∎
- DATA (counter id_state: the key run against an IDEAL run coded from R104's words, β-SETS and gate-index chains; red_ideal: T against
  r2end.ideal's L(G), successor 34's code from P-REALIZE §2): 0 on every set of §A3.4; controls l0w, brpar, kmax fire.
- Consequences (each a citation of landed text, premises as landed there, the standing SPEC premise [1E-N3] included):
  (a) REDUCTION. [Q R117] «Let G ∈ IDEAL-ACYC with IDEAL run s_0 → s_1 → … → s_L, L = L(G). Then the N5 run of Γ3(G) FROM S3 has states 0, …, L equal to the standard states of Γ3 for s_0, …, s_L; transitions 1, …, L are FL transitions;»
      (R117 (f), Theorem REACH3; its last clause: transition L + 1 is a fallback). With ID this is §2's REDUCTION, T_key(Γ3(G)) =
      T_key(1P(G)) = L(G), first fallback at T + 1 (the F = T + 1 of Addendum 2). The game is the same: R104's e-priorities are
      [Q docs/red/P-N5-REALIZE.md@5d7aab0f] «Ω(e_g) := eb + 2·i, eb := the least even number > bmax, i := the position of g in the order by (lev(owner), gate index)»,
      which is box 189's gamma3.py l. 43 and r2end.build's order 'lev'; e-indices are in gate-index order in all three.
  (b) BRIDGE. [Q R117] «KEY3 (availability and the root-first keys are the IDEAL ones)», i.e.
      [Q docs/new/P-N5-REACH.md@5d7aab0f] «(a) R(x) = {m_(x,k) : k ∈ A_s(x)}, A_s(x) := {s(x)} ∪ {k : (x, k) strictly Ξ-better than (x, s(x)) under s} ([DEF]).»
      for «the standard state for s», any s. That is Lemma BRIDGE's «Hence» sentence.
  (c) What the question is. [Q R117] «a family of acyclic genomes with L super-polynomial in N + M would give games on which N5 from its default start makes super-polynomially many iterations»:
      QUIET-KEY-1P is the conclusion of R117's Corollary REAL-IDEAL-S3 (L(G) ≤ p(N + 7M + 10)), so it is NECESSARY for G-N5-TIME by landed
      text, and a kill family of QUIET-KEY-1P is, by landed text, a family of real games on which N5 from S3 is super-polynomial. The box's
      «Kill criterion» (l. 49-51) says the same without the citation.
  (d) Overlap. Under ID these parts of the unit are landed: [Q R105] «(MONO) the current Ξ-value of every mover never decreases along a run»;
      [Q R114] «(MOVE-RISE) at any degree, a move of z at step t gives cv_(s_t)(z) > cv_(s_(t−1))(z)» (A1's V half);
      [Q R113] «(PATH-RISE) at any degree, the current value cv(z) of every mover z rises at most P(z) − 1 times in a run» (A2's Ξ half, P(z) = \|PΞ(z)\|);
      [Q R111] «(PAIR-KF) for a mover x of degree 2 and level ≥ 1 with W-targets a, b of its two options, KF_x = 0 if a = b» with
      [Q R105] «(KEYFLIP) moves(x) ≤ 1 + KF_x with KF_x the number of steps at which KP(x) changes» (A3 (i) at level ≥ 1);
      [Q R111] «(MERGE) at any degree, for two distinct options k, k′ of x and a state s, v_s(x, k) − v_s(x, k′) depends only on the options under s of the movers of the two chains before their first common mover»
      (A3 (ii): with equal Ξ-targets the difference is constant); [Q R111] «(RETURN) for a mover x of degree 2 that moves to o at step t_1 and next moves at step t_2, the Ξ-target z of its other option is a mover with cv_(s_(t_2−1))(z) > cv_(s_(t_1−1))(z)»
      (A4 (iii) / A7's sw(x) ≤ 1 + XF_x in rise-count form); [Q R113] «(MOVES) on 𝓛^R_d, KF_x = F(l − 1) and moves(x) ≤ 1 + F(l − 1) for every mover x of level l ≥ 1»
      (A2's key half on 2-wide ladders, with T-BOUND's F(l) ≤ 2^(l+2) − 2). Not found in landed text (my search of RESULTS at 5d7aab0f, not
      exhaustive): A1's μ half at any degree, A2's key half off 𝓛^R_d, A2-POLY, A4 (i)-(ii), A7's Ξdesc form.

### A3.2 Re-derivation notes (only where the box's proof needed a second look)
- A1, μ half, the one inequality that carries it: s_t(x) ∈ A_t(x), so μ_(t+1)(x) = min over A_t(x) of key_(s_(t+1))(x, ·) ≤
  key_(s_(t+1))(x, s_t(x)) = μ_(t+1)(wt(x, s_t(x))) ++ (ε) ≤ μ_t(wt(x, s_t(x))) ++ (ε) = μ_t(x); appending one entry to tuples of one length
  keeps ≤; the minimum over A_t(x) is attained once (Lemma 0 (a)). Uses only «s_(t+1)(x) is the key-least element of A_t(x) under
  s_(t+1)» and «s_t(x) ∈ A_t(x)»: nothing about Ξ. So the μ half holds for ANY sets A_t(x) ∋ s_t(x) (it is a property of the choice rule),
  and the V half for ANY rule choosing inside A_t(x) (it is a property of the candidate sets). Worth one sentence in a packet.
- A2: «every step switches at least one mover» is the definition of T (the run stops at s_(t+1) = s_t).
- A4 (ii): at level 0 it is void (no W-target); (i) ⇒ μ(x) starts at the largest and ends at the least key of K(x).
- A7: the first inequality holds step by step: if the order of (a, b) differs between s_(t−1) and s_t then V(y_a) or V(y_b) differs between
  them (c(x, a) − c(x, b) is constant, no ties by Lemma 0 (c)), and V(y) is a function of s on the movers of y's Ξ-path under s_(t−1).
- BRIDGE: play shape checked against R117's Γ3 edges (m → g → pβ → β → xt or pb → K0 → pA → K3 → K2 → r → K1 → s → K1): Π = the β's ∪
  {K0, K3}, Λ = K1, length 5·hops + 5 from the pad m_(x,k) (hops = the number of β's); my counters br_val, br_cmp, br_A, br_noe.
  LOC-K2-3's landed scope: [Q R125] «(Lemma LOC-K2-3) σ̄_t(K2) = r and Ω_t(r) ◁ Ω_t(K2) at every state» of HOW3(G),
  [Q R125] «the Howard run on Γ3(G)»; the every-standard-state form is [Q R117] «gives σ̄(K2) = r in every standard state for every genome».

### A3.3 A6 / A6′: E-1, E-2, N-7 with instances
- E-2. LIFT(G, d): add a chain c_0, …, c_(d−1) of degree-1 movers (c_j at level j, W-target c_(j−1), Ξ-target the exit, new β's of the
  lowest ranks, new gate indices above the old ones); give every old level-0 option the W-target c_(d−1); raise every old level by d.
  Every old key gets the same d-entry prefix, no old Ξ-path meets the chain, the chain movers have one option: the run on the old movers is
  G's run. So sw, \|K\| and T are those of G, and every level, k(G) and every k_c(G) (when some mover qualifies) grow by d, with N + M
  growing by 2d. On LIFT(H5_d20_F62, d): T = 136 for every d and k = 5 + d = N − 35. DATA (unit217_lift.out): d = 0, 10, 40 and
  LIFT(DBL4, 30): T 136, 136, 136, 30; k 5, 15, 45 on H5; every unit counter 0; N5 itself from S3 on Γ3 equal to the key run state by
  state, first fallback at T + 1. A degenerate instance already in a lane tree: claude/l-comp 6bfd4966
  experiments/comp/box38/out/argmax/S_N16M16_U10_elev.json (N 16, T 0): its level-11 mover has degree 1, \|K\| = 1, sw = 0 = \|K\| − 1,
  so k = 12 by A6's definition. Hence «k(G) = O(log N)» is false on §6.1's class with nothing super-polynomial in sight, and it is not
  a necessary condition of QUIET-KEY-1P there. On genomes with every degree ≥ 2, \|K(x)\| ≥ 2^(lev(x)+1) and the box's argument is right:
  sw(x) + 1 ≥ \|K(x)\|^c ≥ 2^(c·k_c) and sw(x) ≤ T ≤ p(N + M) give k_c ≤ log2(p(N + M) + 1)/c. The five towers, the 62 records and
  H5PLUS_L5 have every degree 2, so their k values stand (H5PLUS_L5: mover 40, level 5, \|K\| 64, sw 63: k = 6 at d = 20, N = 41).
- The same holds on the kill side: «a family with k_c ≥ c′·d^ε for some fixed c is super-polynomial» (l. 119) needs every degree ≥ 2 on
  the enumerating W-cones. For a claimed kill I will fit max_x sw(x) and T against N + M and check the degrees; k alone is not accepted.
- E-1: with the repair sw(x) + 1 ≥ \|K(x)\|^c, k_1 is A6's k and DBL4's level-4 movers still qualify at c = 3/4 (16 ≥ 32^(3/4) ≈ 13.5).
- N-7. claude/l-red aa4f7680 experiments/red/r207/keep/Tstar_d5_T17.json (N 20, T 17): mover 5 (level 2, degree 2, \|K\| 4) has sw 3 =
  \|K\| − 1 and W-targets 12, 13 of degree 1 (\|K\| 2, sw 0): μ(12), μ(13) take both values (A4 (ii) holds) without a switch of 12, 13.
  5 such movers in the 875-genome corpus, all with degree-1 W-targets; 0 on the genomes with every degree 2 (towers, records, mutants,
  ladders). Whether full switching is hereditary at degree 2 is not decided by A4: a change of μ(wt) without a switch of wt needs two
  keys of K(wt) that are consecutive in K(wt), share their last entry and have a key of the other W-target between them, which the key
  order alone allows. OPEN (observation).

### A3.4 DATA (own engine; a pre-read replay, not a signature)
Engine docs/referee-2/R2-key/r2unit217.py: 1P(G) written from §6.1's text; the Γ3 side (BRIDGE, RED) by R2-P-N5-END/r2end.py (successor
34: build with e-order 'lev', s1, Order, s3, dual, ideal); no lane code. One known difference of r2end.build from R104's layout: it indexes
the β-vertices in gate order (R104 and box 189's gamma3: option order); e-indices, on which the keys depend, are in gate-index order in
both. The N5 runs agree across the two builds where I compared them (kill217_selftest.out: the lane's n5v spec on gamma3 against my engine
on r2end.build, same mover states, iteration counts and regions on 5 genomes). 40 must-0 counters (units in the file's header). Inputs by
get217.py (git show / git archive at pinned commits): the 5 towers (box 212 inst, be167574), the 62 records of box 217 (a143d406) and
L-RED's H5PLUS_L5 (aa4f7680), and a corpus: every JSON file under experiments/ of claude/l-new a143d406, l-red aa4f7680, l-lower b6887eff,
l-comp 6bfd4966, l-si ff28a3fc that is in R104's genome format, Ξ-acyclic and meets §6.1's premises, one per distinct content.
All 40 must-0 counters are 0 on every set (each file's last line reads «FIRED none»):
| set (file) | runs | steps | Γ3 side | notes |
| --- | --- | --- | --- | --- |
| 5 towers (unit217_towers.out) | 5 | 741 | BRIDGE at 776 states (the key run's and 6 random mover states per tower): 75,328 (state, gate) pairs, 37,664 option pairs; N5 itself on all 5 | T 30, 136, 209, 299, 67 = L(G) = N5's states before its first fallback (fallback at T + 1); 44 full movers (36 at level ≥ 1), levels 0-6; k = 7 |
| 62 records of box 217 + H5PLUS_L5 (unit217_rec.out) | 63 | 1,763 | BRIDGE at 2,204 states: 140,002 (state, gate) pairs, 70,001 option pairs; N5 itself on all 63 | max T 340; Lemma 0 by brute force over all states on 16 genomes; H5PLUS_L5: mover 40, level 5, sw 63 = \|K\| − 1 |
| random (unit217_rand.out): 3,000 r2end.gen «acyc» (seed 41), 2-wide ladders d 6 (1,500, seed 42) and d 10 (600, seed 43), Ξ = W ladders d 6 (800, seed 44) | 5,900 | 5,875 | — | Lemma 0 by brute force on 2,941 genomes; A3 on 15,210 / 11,816 eligible movers; A7 on 45,479 degree-2 movers; runs are short (max sw 2) |
| random with Γ3 (unit217_randG3.out): 600 «acyc» (seed 45), 120 ladders d 4 (seed 46) | 720 | 609 | BRIDGE at 5,649 states: 75,321 (state, gate) pairs, 48,312 option pairs; N5 itself on all 720 | — |
| tower mutants (unit217_mut.out): 150 per tower, 1 to 4 (6 for RECF4, DBL4) random mutations, Ξ-graph kept acyclic | 750 | 29,445 | — | 1,422 full movers (1,067 at level ≥ 1); A7 on 33,600 degree-2 movers |
| tower mutants with Γ3 (unit217_mutG3.out): 12 each of H5, RECF4, DBL4 | 36 | 711 | BRIDGE at 747 states; N5 itself on all 36 | — |
| corpus, 1P side (unit217_corpus1p.out; list corpus217.list) | 875 | 12,095 | — | Lemma 0 by brute force on 598; 3,088 full movers; her 5 (N-7); the k = 12 is E-2's degenerate instance |
| corpus, Γ3 side (unit217_corpus.out: 35 chunks summed by sum217.py; row completed 2026-11-13T12:42Z, the commit after 2dd4e5e3) | 875 | 12,095 | BRIDGE at 18,220 states: 996,681 (state, gate) pairs, 670,356 option pairs; N5 itself on all 875 (every run ends in a fallback at T + 1) | all 40 counters 0 |
| LIFT (unit217_lift.out) | 4 | 438 | BRIDGE at 442 states; N5 itself on all 4 | E-2 |
Lemma 0's bounds l0a_bnd / l0b_bnd, a2_p, a2_poly, a2_idle, a7_self, br_k2 and red_flag have no control of their own. Controls (unit217_ctrl.out),
each on the 5 towers + 300 random genomes (the three Γ3 controls on 150 random genomes), fire in their target counters: howard (a1_mu,
a1_mus, a2_k, a3_i, a4_i_val, a4_i_sw, a4_ii), aall (a1_v, a1_vs, id_state), kmax (a1_mu, a1_mus, id_state), khalf (a2_k, a2_T), a3any (a3_i,
a3_ii), a4half (a4_i_val, a4_i_sw, a4_ii), a7direct (a7_b, a7p), a7nop (a7_c), a7path (a7_a), xfhalf (a4_iii, a7_c), l0k (l0a_cnt, l0b_cnt),
l0w (l0b_val, l0c_tie, id_state), brpar (br_cmp, br_A, id_state), brstd (br_val, br_cmp, br_A), kmax with N5 (red_len, red_state), and 300
Ξ-CYCLIC genomes (seed 63) give br_face 417, br_noe 3,216, br_k2 0 (so BETA-ACYC's hypothesis is seen to matter, and σ̄(K2) = r is seen
not to depend on it). §7's supply tables: H6 «level 0: 1, 4: 31, 5: 63, 6: 32, 12-18: 12» and HIT7 «levels 2: 4, 5: 63, 6: 118, 7: 16,
9: 56, 10: 31, 12-24: 58» are my engine's numbers too (unit217_towers.out, --supply; 12 = 2 + 4 + 1 + 4 + 1, 58 = 1 + 1 + 4 + 24 + 17 +
4 + 4 + 1 + 2). The corpus drops 21 genome files whose gate indices are not distinct (§6.1's premise) and 3,853 Ξ-cyclic ones (the 81
frozen genomes of box 212 among them: 1P(G) is not defined there).
Kill-claim checker, ready for item 2 (r2kill217.py; self-test kill217_selftest.out): per genome the key run, ID, N5 itself from S3 on Γ3 to
termination on my engine (F = T + 1, total iterations T + 3 on the five test genomes), N5's output against my own Zielonka (R2-TA1/r2lib)
and, with --lane, the lane's n5v spec run on the lane's Γ3 (same mover states, same iteration count, same regions through the two vertex
maps) against the harness Zielonka; then exponential and polynomial fits of T and max sw with residuals. On DBL4, RECF4 and three records:
id 0, red 0, zl 0, zh 0, lane 0; control (one vertex of the Zielonka region flipped): zl 2 of 2.

### A3.5 What a packet P-N5-KEY1P needs from this pre-read (in order of weight)
1. B-7 ID, stated and proved; then B-8: the REDUCTION cited as R117 (f) REACH3 on Γ3(G) (drop «CONDITIONAL on KEY-TAU (i) and [IMP3]»
   there; keep KEY-TAU (i) + STD-N5 only if the renumbered form is claimed), and B-9 / B-10 for BRIDGE.
2. B-12: ENUM-LOG, k and k_c restated on genomes with every degree ≥ 2 (E-2), with E-1's off-by-one; the kill criterion in terms of max sw
   and T. SW-POLY is the open statement; ENUM-LOG (repaired) is necessary, not sufficient (the box says so, l. 115-118).
3. B-11: A7′'s conclusion as a READING.
4. W-1..W-5 and the overlap list of §A3.1 (d): cite the landed IDEAL lemma where one exists, prove only A1's μ half, A2's key half,
   A2-POLY, A4 (i)-(ii) and A7's last bound.
5. Scope sentence unchanged: Ξ-acyclic genomes, N5's run before its first fallback on Γ3(G); nothing for Ξ-cyclic genomes, nothing
   after the first fallback, not N5 on general games; A2-POLY is a restricted class (TARGET.md §4), not M3 without L-LIT.

### A3.6 Files (docs/referee-2/R2-key/)
r2unit217.py (engine, controls), get217.py (inputs by git show / git archive at pinned commits; corpus list), sweep217.sh (every run of
§A3.4, resumable; its OUT is a scratch directory, the unit217_*.out files are copied here), sum217.py (sums chunk outputs), r2kill217.py
(kill-claim checker) with kill217_selftest.out, r2qfile.py (quote check of a local file), corpus217.list (sha1, N, path of the 875 corpus
genomes), unit217_towers / rec / rand / randG3 / mut / mutG3 / corpus1p / lift / e2n7 / ctrl .out, unit217_q.out (this addendum's own 18
[Q] quotes against trunk 5d7aab0f: «quotes 18 missing 0»; control «quotes 18 missing 18»).

## Addendum 4 (REFEREE-2 successor 41; 2026-11-13T12:42Z by date -u): REPLAY NOTE on the upward-ladder candidate (Lead 12:08Z: «upward ladders (every Ξ-target on a strictly higher W-level): k = 2 at d = 4, k = 3 at d = 6 (SAT, uncertified …)»). DATA and a ceiling; not a review, not a signature
L-SI's file (claude/l-si 06f072f1, experiments/si/box107/out/up_k3_d6.json) was not on origin when this was written (claude/l-si = ff28a3fc).
So this is an INDEPENDENT replication: own instances from a plain hill-climb on my engine (scratch search, not committed), not L-SI's.
- Instances (2-wide, degree 2, every Ξ-target on a strictly higher W-level or the exit; R2-key/): up_d4_k2.json (sha1 48501e98…, N 8):
  mover 3, level 1, sw 3 = \|K\| − 1, T = 7; up_d6_k3.json (sha1 5a58e2ac…, N 12): mover 4, level 2, sw 7 = \|K\| − 1, T = 11, levels 0 and
  1 full pairs (sw 1, 1, 3, 3). My climbs at d = 8 (plain, seeded by level insertion, block-rewarding objective; about 10 minutes) stay
  at sw 5 to 7 on level 3: no k = 4 from me.
- Checks (kill217_up.out): r2kill217.py: id 0; N5 itself from S3 on Γ3 (my engine): first fallback at T + 1 (8, 12), 10 and 14 iterations
  in all, output = my own Zielonka (zl 0); the lane's n5v spec on gamma3: same mover states, iteration count and regions (lane 0) =
  harness Zielonka (zh 0). r2unit217.py: all 40 counters 0 with BRIDGE at 32 states; supply of the full mover: d = 4 «2: 3, 3: 1»,
  d = 6 «3: 6, 4: 4, 5: 1» (all from above, as the shape forces).
- Ceiling (from A2; its Ξ half is landed R113 PATH-RISE): on an upward 2-wide degree-2 ladder with d levels a level-l mover has
  \|K\| = 2^(l+1) and \|PΞ\| ≤ 2^(d−l) (a Ξ-path visits at most one mover per higher level), so sw(x) ≤ 2^(min(l+1, d−l)) − 1. Hence
  k ≤ (d + 1)/2, max sw ≤ 2^(d/2) − 1 for even d, and T ≤ Σ_x sw(x) < 2^(d/2+3). The reported k = d/2 at d = 4, 6 is this ceiling.
  If a rule G_k with d = 2k and a mover with sw = 2^k − 1 exists for every k, then max sw = 2^(N/4) − 1 and T ≥ 2^(N/4) − 1: by ID and
  landed R117 (REACH3, REAL-IDEAL-S3) N5 from S3 would need ≥ 2^(N/4) iterations on Γ3(G_k), n3 = 30d + 10. That is the statement a kill
  packet has to PROVE; two or three sizes are DATA (L43).
- What I will check in a kill packet: (i) the rule G_k for every k, every degree 2 (E-2); (ii) L(G_k) by two engines at every k run;
  (iii) a proof that some mover switches ≥ c·2^(εk) times for every k (induction, or an explicit run checked against the step rule);
  fits with residuals are DATA; (iv) N5 itself on Γ3(G_k) with outputs against Zielonka, up to about k = 13 on my engine.

## Addendum 5 (REFEREE-2 successor 41; 2026-11-13T13:02Z by date -u): PRE-READ (not a signature) of L-SI's box 107 (claude/l-si 06f072f1, docs/si/box107-timing.md, sha1 a69adf7e3fd2ab4debad55be3e049c655182aea4, 255 lines) — the timing lemmas of full key enumeration on 1P(G), and the replay of its three instances
Independence: box 107 was read after Addendum 4 was written (my own upward-ladder replication, commit cd54dbfe); docs/referee/ holds no
report on it. Every statement below is a lane CANDIDATE. QUIET-KEY-1P / SW-POLY stay OPEN; G-N5-TIME stays OPEN; not M3, not M4.
Own engine: docs/referee-2/R2-key/r2box107.py (counters from box 107's own statements, on r2unit217's 1P(G); no lane code, not abandon107.py).

### A5.0 Verdict (pre-read)
| statement (§) | finding | for a packet |
| --- | --- | --- |
| FULL-ORDER (§2) | no gap: μ(x) ∈ K(x) is non-increasing, strictly falls at each of the \|K(x)\| − 1 switches, so it takes all \|K(x)\| values in decreasing order, one predecessor per switch, and cannot change without a switch | — |
| ABANDON (§2) | no gap. The two cases (x keeps k; x switches to k′) are both excluded by FULL-ORDER, the second because κ′ ++ ε(x, k) ∈ K(x) would be skipped | — |
| ENUM-ABANDON, ONE-AHEAD (§2) | no gap (an enumerating monotone μ(x) skips no key; ONE-AHEAD's λ* is taken at a time t′ ≥ t and μ(w) is non-increasing) | — |
| CAUSE (§4) | no gap, with one reading to pin: [Q docs/si/box107-timing.md@06f072f1] «a mover of lower level on a W-path below one of x's options» must mean the W-CHAIN under s_t (then no switch on it gives s_(t+1) = s_t there AND the chain under s_(t+1) is the same chain, so the keys of x's options are unchanged). The rest is right: A_t(x) ⊆ A_(t−1)(x) when x switched at t − 1 to the Ξ-better k, and the keys are unchanged, so x stays | S-1: write «the W-chain under s_t» |
| FROZEN, Ξ-LAST, SEPARATION (§4) | no gap in FROZEN or Ξ-LAST on my re-derivation and replay. SEPARATION is a statement about any two frozen states, not a counting bound; the box says so | — |
| ODOMETER (1)-(3) (§3) | no gap: (1) from FULL-ORDER (a full reader switches at every change of μ, one option per owner); (3) from §3's own argument with ABANDON applied to the owner of p and p + 2 | — |
| FLIP-SUPPLY (§4 (iii)) | the inequality sw(x) ≤ 1 + Σ_(y ∈ D(x)) sw(y) and the induction sw(x) ≤ 2^\|D(x)\| are correct (topological order: \|D(y_i)\| ≤ m − i, Σ 2^(m−i) = 2^m − 1). S-2: its corollary [Q docs/si/box107-timing.md@06f072f1] «a full level-(h − 1) mover has at least h strict Ξ-descendants» is FALSE at h = 1 and right from h = 2 (2^h − 1 > 2^(h−1)): a full level-0 mover (sw 1 = \|K\| − 1) may have D = ∅. 23 such movers in my sets, e.g. l-new a143d406 experiments/new/box217/out/rec/rec_w2_d10_D2_s3.json mover 1 (level 0, \|K\| 2, sw 1, \|D\| 0) | S-2: «for h ≥ 2» |
| [Q docs/si/box107-timing.md@06f072f1] «Counting gives k ≤ (d + 1)/2 in this class for one full mover» (§6) | AGREES with my own ceiling (Addendum 4, reached before reading box 107): \|PΞ\| ≤ 2^(d−l) for a level-l mover, so a full level-(k − 1) mover needs 2^k − 1 ≤ 2^(d−k+1) − 1 | — |
| SAT answers (§7) | UNCERTIFIED by the box's own label; I did not re-run any SAT query. «no 3-level ladder has k = 3» and the bi-ladder maxima rest on cadical195 alone | S-3: for a RESULTS line these need certificates (as R112 did) or an independent solver |
| scope line | correct and complete (1P(G) only, through L-NEW's reduction; no N5 bound claimed). With my Addendum 3's ID the reduction is no longer conditional on Γ3(G) as R117 indexes it | S-4: cite R117 (f) REACH3 instead of [Q docs/si/box107-timing.md@06f072f1] «about N5 only through L-NEW's REDUCTION there (lane, conditional)» |

### A5.1 Replay of box 107's instances (my engines; kill217_si107.out, box107_*.out)
| instance (06f072f1) | sha1 | box 107's numbers | mine |
| --- | --- | --- | --- |
| experiments/si/box107/out/k2_d2.json | f7a22a2266e2e1eec2f963895eaea628f95fe085 | [Q docs/si/box107-timing.md@06f072f1] «N 4 T_key 3 … sw [1, 1, 3, 1] full [0, 1, 2]» | N 4, T 3, max sw 3, k 2; ID 0; N5 itself from S3 on Γ3: fallback at 4, 6 iterations, output = Zielonka (two implementations); lane n5v = my engine |
| out/up_k2_d4.json | d28a333248f564f96265932ed9ff45c34f767e18 | [Q docs/si/box107-timing.md@06f072f1] «N 8 T_key 3 … sw [1, 1, 3, 1, 2, 2, 1, 1]» | the same list; T 3, k 2; ID 0; N5: fallback at 4, 6 iterations; zl / zh / lane 0 |
| out/up_k3_d6.json | 0dc9a46dfa359f8007814654d7236c363494ee5c | [Q docs/si/box107-timing.md@06f072f1] «N 12 T_key 8 … sw [1, 1, 3, 3, 7, 1, 3, 3, 3, 2, 1, 1] full [0, 1, 2, 3, 4]» | the same list; T 8, max sw 7 at mover 4 (level 2), k 3; ID 0; N5: fallback at 9, 11 iterations; zl / zh / lane 0 |
So box 107's k = 2 at d = 4 and k = 3 at d = 6 are confirmed on independent code, and (new here) they are confirmed for N5 ITSELF on Γ3(G)
with its output checked against two Zielonka implementations. My own instances of Addendum 4 are different genomes with the same k
(up_d4_k2.json T 7, up_d6_k3.json T 11: longer runs, same enumeration depth).

### A5.2 DATA (own counters; r2box107.py, units in its header)
All ten must-0 counters (fo, ab, eab, oa, cause, fs, od1, od3, fz, xl) are 0 on: the 5 towers (741 steps; 44 full movers; ABANDON on
7,168 (mover, step) units, ONE-AHEAD on 13,851, CAUSE on 2,207 switches, ODOMETER (3) on 928 (level, reader, position) units, FROZEN and
Ξ-LAST on 210 moves of S_j each; 4 capped ladders, h up to 7); the 62 records + H5PLUS_L5 + box 107's three instances + my two (68 runs);
2,400 random genomes and ladders; 450 tower mutants (27,092 steps; FROZEN on 5,885 moves); and the 875-genome corpus of Addendum 3
(12,095 steps; 3,088 full movers; 80 capped ladders). Controls (box107_ctrl.out), each firing its target counter: abnf (ABANDON on
non-full movers), eabne (ENUM-ABANDON on non-enumerating movers), oastrict (ONE-AHEAD with a strict inequality), causexi and causew
(CAUSE with one disjunct dropped), od3strict (W(p) < E(z, p) strictly: the same-step case does occur), fzlate (FROZEN's interval one step
longer), xl2 (Ξ-LAST one step earlier).

### A5.3 Where box 107 and Addendum 3 meet
- Box 107's lemmas are about 1P(G) and, by Addendum 3's ID, about R104's IDEAL model; §3 already cites the landed twins (R113 ALIGN,
  R120 MOVE, DOUBLE-EQ, PULSE-NEST). What is new there: ABANDON at any shape and degree, ONE-AHEAD, FROZEN / Ξ-LAST / SEPARATION, CAUSE.
- Neither box bounds the enumeration depth. Box 107 §4's open step ([Q docs/si/box107-timing.md@06f072f1] «is the signal to S_j computable from the signal to S_(j+1) plus O(1) movers») is the same obstruction my Addendum 3 B-11 names in box 217's A7′: counting alone does not decide it.
- For a kill: box 107's upward ladders are the live candidate; k = 4 at d = 8 is the deciding query. My own climbs did not reach it
  (Addendum 4), and the ceiling k ≤ (d + 1)/2 means a family must hit the counting bound at every k.
