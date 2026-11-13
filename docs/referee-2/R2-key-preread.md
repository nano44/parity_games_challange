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
