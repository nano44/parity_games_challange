# R-restrictC-preread: PRE-PACKET READ (NOT A SIGNATURE) of L-SI 51's Lemma RESTRICT-C (box 101 Addendum D.2), with Addendum C's quotes
REFEREE successor 32 (D1 «Treat every such claim … as wrong until it passes the gauntlet below.»). Date -u at writing: 2026-11-12T13:03Z. Lead 12:47Z item B1.
This is a read to find errors early. It is not a referee signature: no packet is frozen, and a packet review, if one comes, is separate.
Not read before this verdict: docs/referee-2/, L-RED 65-66's records (R232, R234), L-LIT T65. Read: box 99, box 100, box 101 (all at
claude/l-si d8945c4a), the landed entries R104, R117, R118, R125 in trunk docs/RESULTS.md (471aba45), the landed packets P-N5-XICYC
(sha1 149e2414…, fixes 90d0f09d…) and P-N5-CHAIN (6e613ba7…), and claude/l-formal 9dde1527's two Lean files.

## 0. Verdict
| item | verdict |
| --- | --- |
| Caveat «the proof of BR-SEG (DOM, STRICT, PATH) does not use a tie rule» | **CONFIRMED on the landed text** (§2): no step uses which ⊴-best successor is taken, and the packets' own signed definitions leave ties free. |
| Lean `BrSegStatement` (l-formal 9dde1527) against R118 (d) | **hypotheses MATCH** (§3): every Lean hypothesis holds in R118 (d)'s setting, with two bridges (injective priorities = SPEC's p′; F1 = landed R15 (a)). The PROOF commit 4b376da4 was not on origin at 13:02Z (date -u): not seen, not built by me. |
| RESTRICT-C (i), (ii), (iii) | **no gap found** (§4), with wording item W-2 (G′ as a genome). |
| RESTRICT-C (iv) | **GAP (exact, wording): W-1.** The sentence «every two-player window of C (σ̄ and Λ constant on V_R) has at most N′ … steps» is FALSE as written (instance C6G8_n54, §4.4); it is TRUE in BR-SEG's own form, which is all the route uses. Exact string in §4.4. |
| Citation form of (iv) | **C-1** (§2.3): no landed STATEMENT says BR-SEG for every HOW3 run of Γ3; the packet must carry it as a lemma (six lines from R125 (d)) or cite the Lean theorem once CHECKER has it. |
No FALSE mathematics found. Own replay (§5): every must-be-0 counter 0 on 26 pinned instances and 1,200 random genomes, controls fire.
G-N5-TIME stays OPEN; nothing here is a TARGET.md claim (§7).

## 1. Objects and premises (measured with git, not copied)
- claude/l-si d8945c4a (ancestor of origin/claude/l-si, checked): docs/si/box101-lamgap.md sha1 3295dcc1cf8bffc52b5b5ca13e4652cbae2ca648,
  31,057 B, 327 lines. Its first 258 lines equal the file at 2d2f9a0e (sha1 76eeeb5c…, 25,219 B): Addendum D is append-only.
- Quotes by script (scratch/restrictc_quotes.py, every outermost «…» of a section located in the named RESULTS entries at trunk 471aba45):
  - Addendum C.1: **10 quotes, 0 missing**, all in R118's entry (restrictc_logs/quotes_C1.out).
  - Addendum D.2: **4 quotes, 0 missing**: R125 (e) CN2-3, R125 (c) REACH3-ALL, R118 (d) BR-SEG; «§4 applies on Γ3» is the R118 entry's own
    description of (l), not a packet quote (restrictc_logs/quotes_D2.out).
- In context:
  - R118 (a): a Howard step is a RELATION («every mover x goes to a successor of ⊴-largest Ω_t value, and keeps σ_t(x) if σ_t(x) is such
    a successor»). R118 (d) is stated for IDEAL-CYC on Γ(G) [every genome]. R118 (l) is stated for the N5′-xi run on Γ3(G) from S3.
  - R125's title defines HOW3(G) by «every mover moving to a ⊴-best successor and keeping a best current one»; (d) gives F1, F3, F4′, F5,
    F6, DOM, STRICT on HOW3(G) for every genome; (e) CN2-3 is for every positional pair; (i) NO-TIE3 and (g) LOC-K2-3 are per state.
  - Add. C.1's last bullet (R counts only steps with a gate flip) follows from R125 (g) / R118's K2-r: correct.

## 2. The caveat: does BR-SEG's proof use a tie rule? No.
### 2.1 The proof, step by step (P-N5-XICYC §3-§4, l. 68-111, with fixes entry 2's F4′)
- F1 (l. 69-70): R15 (a), for any non-empty unambiguous improvement set. A Howard step switches a mover only to a strictly better
  successor, whichever best one it takes. No tie rule.
- F5 (l. 80): «σ_(t+1)(x) is ⊴-best among x's successors under Ω_t. If σ_(t+1)(x) ≠ σ_t(x), then Ω_t(σ_(t+1)(x)) ▷ Ω_t(σ_t(x)).» This is the
  only property of the step that DOM and STRICT use, and every ⊴-best choice has it.
- DOM (l. 86-88): F3, F6 at t + 1; F1; F4′; F5. STRICT (l. 89-91): DOM, F5, F4′, F3, F6. No tie rule.
- PATH (l. 92-101): induction on the path; a mover step uses DOM, a non-mover step uses F3 with the frozen edge or σ̄_t = σ̄_a. No tie rule.
- BR-SEG (l. 102-111): the switching mover x, STRICT, the play π of x under (σ_(a+j+1), σ̄_a), μ(π) ≤ N, PATH at t = a + j. No tie rule,
  and no property of the start state: only «non-mover Even vertices have one (frozen) successor» and F6.
- σ̄: «chosen by a fixed deterministic rule (any rule …)» (l. 57). The proof uses σ̄ only through its constancy on the window (hypothesis) and
  F1 / F3. On Γ3 it is unique anyway at every state (R125 (i), (f), (g)).
### 2.2 The signed definitions already say so
- P-N5-XICYC §2 l. 58-60 (in its «To sign» table, row «§2 definitions: IDEAL-CYC(G); Howard step; step labels»): «Ties among best
  successors may be broken by any rule.» So R118 (d) is a theorem about every run of that relation.
- P-N5-CHAIN §2 l. 88-89 (HOW3's definition, R125): «a HOWARD step: every mover x goes to a successor of ⊴-largest Ω_t value and keeps
  σ_t(x) if it is such a successor (ties among best successors by any rule)».
- So L-SI's sentence is a correct reading, and more than a reading: it is in the frozen text both referees signed.
### 2.3 C-1 (citation, REQUIRED in a packet)
- RESTRICT-C (iv) applies BR-SEG to a HOW3 run of G′ on Γ3(G′) whose tie resolution is inherited from G's run. That run need not be
  N5′-xi's own run on Γ3(G′) (N5′-xi resolves exact ties by SPEC's arena choice and indices, which the restriction may change).
- Landed statements: R118 (d) is IDEAL-CYC on Γ; R118 (l) bounds T3 of the N5′-xi run. Neither STATES «in every HOW3 run of Γ3(G), any tie
  resolution, a run of p-steps has at most N steps». Its proof exists in landed pieces: R125 (d)'s F1, F3, F4′, F5, F6, DOM, STRICT on
  HOW3 plus P-N5-XICYC's PATH and BR-SEG arguments, which use nothing else (§2.1; F4′'s side condition at a non-mover z_0: z_0 is in
  neither Π because Λ(z_0) = w ≠ z_0 and π is simple, as fixes l. 56 says; at a mover: movers are in no Π, R125 (e)).
- Required: the packet states that lemma («BR-SEG3») with this six-line proof and cites R118 (l)'s «§4 applies on Γ3» as its precedent,
  or cites the Lean theorem (§3) once CHECKER has passed it. «(R118 (d) / (l) on G′)» alone is not an exact citation.

## 3. Lean `BrSegStatement` against R118 (d)
Object: claude/l-formal 9dde1527 (= origin/claude/l-formal at 13:02Z), lean/lemmas/PGLemmas/Defs.lean (sha1 b41c937c…, 8,919 B) and
Statements.lean (sha1 aaa3c0c2…, 7,691 B). At 9dde1527 these hold definitions and statements only («no proofs yet»); the Lead's 4b376da4
(Corollaries.lean, `brseg`) is not on origin. I compared the STATEMENT; I ran no Lean build (no toolchain in this container).
| R118 (d), in P-N5-XICYC's setting | `BrSegStatement` (Statements.lean l. 60-78) | match |
| --- | --- | --- |
| Γ(G), IDEAL-CYC | any finite V, any `E`, `V0`, `Mov ⊆ V0` | Lean is more general |
| [VJ] «priorities made injective by rank» | `Function.Injective pr`; `rew`, `setLt`, `Val.lt` as Friedmann §3 | bridge B-1: take pr := SPEC's p′ (P-N5-REALIZE l. 17 «p'(v) := 2·rank(v) + (Ω(v) mod 2), rank by (Ω(v), v)»): injective, same parity, same order |
| non-mover Even vertices frozen | `σ t v = σ a v` for v ∈ V0 ∖ Mov on the window | yes |
| Howard step, R118 (a) | `HowardAt` at every mover, t ∈ [a, a+j] (Defs.lean l. 127: ⊴-best successor; keep the current one if it is best) | yes; ties free («any choice is a Howard step») |
| Ω_t = value against Odd's optimal σ̄_t | value of the pair (σ_t, τ_t) for ANY τ; F1 is a hypothesis | Lean assumes less of τ; bridge B-2: F1 is landed R15 (a) (refereed-only, not Lean) |
| Λ and σ̄ constant on a, …, a+j+1 | `lam` constant at every v; `τ t v = τ a v` off V0 | yes |
| «the step a+j → a+j+1 changes σ» | `∃ x ∈ V0, σ (a+j+1) x ≠ σ (a+j) x` | yes |
| F6 (no mover is its own cycle node) | not assumed | Lean is more general |
| j ≤ N − 1 | `j + 1 ≤ Mov.card` | yes |
- Verdict: the hypotheses MATCH. A Lean proof of exactly this type gives R118 (d) for every tie resolution, and it gives BR-SEG on Γ3
  directly: take V := Γ3(G′) (or V_R inside Γ3(G), a successor-closed set), V0 := its Even vertices, Mov := its movers, τ := σ̄. That would
  settle the caveat AND C-1 by Lean, given B-1 and B-2.
- What I did NOT check, and CHECKER must: that the theorem in Corollaries.lean at 4b376da4 has type `BrSegStatement V` unchanged (the
  Lead's «conditional on F1» = the F1 hypothesis above, or an extra one?), no sorry, axioms propext / Classical.choice / Quot.sound only,
  and the build. The Lean `val` is the play value of a positional pair (Defs.lean l. 75-118: `OnCycle`, `lam`, `plen`, `pset`, `val`), which is the
  fleet's Ω_t when τ_t = σ̄_t (P-N5-XICYC F3's first sentence).
- Remark (not needed for B′): with Mov := C's movers and the movers of Reach(C) ∖ C counted as frozen after t0(C), the same Lean statement
  would give N_C in place of N′. My replay saw no window above |C| (§5, gtNC 0).

## 4. RESTRICT-C re-derived
Notation: S := Reach(C) (movers), V_R := the vertices of Γ3(G) reachable from S's movers, N′ := |S|. φ: Γ3(G′) → Γ3(G) maps a vertex to
the vertex of the same name (mover, m-pad, gate, pe, pβ, e, β, pb of the same option; c_X, c_W, K0-K3, pA, s, q, r to themselves).
### 4.1 (i): no gap found, with W-2
- S is closed under D(G)'s edges (W- and Ξ-targets), so V_R is successor-closed: a mover's edges go to its m-pads, then its gates, the two
  face pads, e (then the W-target or c_W) and β (then the Ξ-target, or pb, then K0); the core and its pads are closed. Every mover has an
  option and every option a β with an edge towards u, and W-targets lead down to level 0, so V_R contains the core and c_W.
- φ is a bijection onto V_R ∪ {c_X} that preserves owners and successor lists (the builder is local per option plus the fixed core).
- Priorities: β keeps 6 + 2br + bp; e-vertices keep their (lev, gate) order and stay even and above every β; c_W, K0, K3 stay on top in
  that order with their parities; movers 0, gates 1, c_X 2, K2 3, K1 5 and the pads other than m-pads are constants. Indices: every block
  keeps its internal order under an increasing renumbering. So φ preserves the relevance order (priority, then index) on all vertices
  but the m-pads, and the parity on all vertices (an m-pad has priority 2 or 0). As stated. CORRECT.
- **W-2 (wording, REQUIRED, small).** «G′ is the genome … with the same (lev, gate, br, bp) entries»: by R104's line a genome has «a
  distinct β-rank with a parity, a distinct gate index», and G′ is one. But R104's packet, where the landed proofs live, defines br and
  gate as bijections ONTO 0..M − 1 (P-N5-REALIZE l. 56-57), and G′'s entries have gaps. The lemmas RESTRICT-C applies to G′ «for every
  genome» (R125 (d), (e), (i); R118) use the rank order only, so nothing fails; say one of: (a) «G′ with br and gate compressed
  order-preservingly onto 0..M′ − 1 (this changes β-priorities but not the relevance order or any parity)», or (b) «genome in the sense
  of R104's line (distinct ranks and gate indices)». My replay ran both forms (§5): 0 failures.
### 4.2 (ii): no gap found
- A play from V_R stays in V_R. By R125 (e), read in Γ3(G) and in Γ3(G′) (both have the same cycles; every cycle but c_X's loop has a
  vertex of priority ≥ 3, and m-pads have priority ≤ 2 in both), the cycle node is a vertex of priority ≥ 3 and Π holds only such
  vertices. φ preserves their order and parity, so Λ, Π and the length correspond, and so does ⊴ on values. Odd's pointwise optima are
  determined by the closed subgame and ⊴, so they correspond too (and are unique at the states of the run: R125 (f), (g), (i)). CORRECT.
### 4.3 (iii): no gap found; it holds for EVERY state a ≥ 0 (t0 is not used)
- At a state t ≥ a the transported state is a standard state of G′ (non-movers frozen at the same choices; at t = a it is G′'s start).
  A mover x ∈ S has its successors (its m-pads) in V_R, and Ω_t on V_R is Ω′_t by (ii). So G's step at x (to a ⊴-best successor iff the
  current one is not ⊴-best) is a legal step of G′ at x, whatever tie resolution G's run used. CORRECT.
- A point the text passes over, needed in (iv): if a step t → t + 1 switches no mover of S, then every mover of S is at a ⊴-best successor,
  so G′'s run has ENDED at t − a; the transported state then never changes again (values on V_R depend on σ|V_R only). So the transported
  sequence is a HOW3 run of G′ up to its own end T′, followed by repetitions of its last state when T′ < T3 − a.
- The argument uses closure only. In particular a = 0 works: G′_0 := G restricted to S with G's own start gives Γ3(G′_0) ≅ Γ3(G)|V_R with
  NO m-pad exception, and the whole run restricted to V_R is a run of G′_0 plus repetitions. OPTIONAL simplification: state RESTRICT-C
  for a = 0 and drop «up to m-pad priorities»; a window at any time ≥ t0 is then a window of that one run.
### 4.4 (iv): GAP W-1 (exact, wording)
- As written: «Hence every two-player window of C (σ̄ and Λ constant on V_R) has at most N′ ≤ |Reach(C)| ≤ N steps». With box 100 §4's
  definition («A window is a maximal run of states a..b ≥ t0 …»), this is FALSE: after G′'s run has ended, the window runs on to T3.
  - Instance (one command, restrictc_logs/literal_iv_C6G8.out): C6G8_n54 (sha1 52067442…, box 91), C = {mover 20} (level 0, one option
    [−1, −1]: a sink SCC), S = C, N′ = 1, t0 = 0, T3 = 17: σ, σ̄ and Λ are constant on V_R (17 vertices) over states 0, …, 17, a window
    of 17 steps > 1. The replay counts such windows as «lit»: 59 of 403 (C, a) pairs on the pinned instances.
- What the proof gives, and what box 100's WINDOW count needs: BR-SEG's form. Exact replacement for (iv):
  «(iv) Hence, if σ̄ and Λ are constant on V_R over the states b, b + 1, …, b + j + 1 (b ≥ a) and the step b + j → b + j + 1 switches a
  mover of Reach(C), then j ≤ N′ − 1, with N′ = |Reach(C)| ≤ N: at most N′ consecutive steps that switch a mover of Reach(C) keep σ̄ and
  Λ constant on V_R. (A step that switches no mover of Reach(C) ends G′'s run; nothing on V_R changes after it.)»
- Proof of that form: by 4.3 the states b − a, …, b − a + j + 1 are states of ONE HOW3 run of G′ before its end; Λ′ and σ̄′ are constant on
  them at every vertex of Γ3(G′) (V_R by hypothesis; c_X trivially); the last step changes σ′. BR-SEG on HOW3(G′) (C-1) gives j ≤ N′ − 1.
- Why the WINDOW count survives: in every window but the last, every inside step switches a mover of S (else nothing changes later and
  the window is the last); in the last window the switching steps are an initial segment. So the steps after t0 at which a mover of C
  switches number at most (#windows)·(N′ + 1). The parenthesis «(the core's Λ and σ̄ are constant: R118's K2-r)» is true and not needed
  (the core is in V_R).
### 4.5 Smaller points
- (iii)'s sentence «After t0(C) the movers of Reach(C) ∖ C do not switch …» is true and not needed for (i)-(iv); it is what turns
  «switches a mover of Reach(C)» into «switches a mover of C» in the route.
- «from its start S3(G′)»: the run is a HOW3 run from G′'s standard state. SPEC's S3 is not used (S3-START would need R117 on G′; avoid).
- The bound is N′ = |Reach(C)|, not N_C; D.3's row B′ says «Gap(C) ≤ N», which agrees.

## 5. Replay with my own code (scratch/restrictc_replay.py; no lane code; logs scratch/restrictc_logs/)
- Engine: my lane's xicyc_replay (own Γ3 builder from R104 / R117's text, own VJ valuation and best reply, Howard at the movers; tie rule:
  keep if best, else the larger index); own SCC / Reach / restriction code; generator end_replay.gen (successor 29).
- For each genome: SCCs of D(G); up to 4 largest and 4 random SCCs C; a ∈ {0, t0(C), two random states}; G′ built from (Reach(C), σ_a);
  Γ3(G′) built by the same builder on its own; φ by names. t0 in the safe reading (first state from which no mover of C′ switches again).
- Must-be-0 counters (units in the script header): (i) i_img, i_own, i_edge (successor LISTS), i_start, i_rel (relevance order on the
  non-m-pad vertices), i_par; (ii) ii_val (values of the transported pair, every state t ≥ a, every vertex), ii_br and ii_sbar (G′'s own
  best reply, from a cold start and from σ̄'s image), ii_rand (3 random positional pairs of the FULL edge relation per (C, a)), cn_pad
  (CN2-3 in both games); (iii) iii_step (each transported step legal for G′ on G′'s own values, per mover), iii_stut (a step changing
  nothing on S: G′ terminal there, and no later change); (iv) iv_brseg (BR-SEG form with bound N′).
- Results:
  | set | (C, a) pairs | must-be-0 | controls: c_mpad / pairs with a changed m-pad; c_open / open pairs; c_iv | lit | max window |
  | --- | --- | --- | --- | --- | --- |
  | 26 pinned (box 91: 11, box 93: 8, box 98: 7; SHA1SUMS all OK at d8945c4a) | 403 | all 0 | 208 / 208; 277 / 277; 10 | 59 | 7 |
  | rand × 200, seed 3202 | 617 | all 0 | 252 / 252; 216 / 243; 36 | 12 | 2 |
  | deep × 200 | 732 | all 0 | 355 / 355; 284 / 309; 9 | 24 | 3 |
  | wide × 200 | 801 | all 0 | 326 / 326; 338 / 400; 29 | 26 | 2 |
  | acyc × 200 | 1,393 | all 0 | 530 / 530; 789 / 1,012; 378 | 44 | 3 |
  | selfl × 200 | 658 | all 0 | 253 / 253; 241 / 300; 15 | 25 | 3 |
  | COMPRESS=1 (W-2 form (a)): 26 pinned | 403 | all 0 | 208 / 208; 277 / 277; 10 | 59 | 7 |
  | COMPRESS=1: rand × 200, seed 3203 | 671 | all 0 | 266 / 266; 259 / 308; 41 | 18 | 3 |
- Controls: c_mpad (the relevance order INCLUDING m-pads) breaks on every pair whose m-pad priorities changed, so «up to m-pad
  priorities» is needed for a > 0 and the test is not vacuous. c_open (C alone, outside targets cut, where C is not closed) changes a
  mover's value on every such pair of the pinned set. c_iv (bound N′ // 4) fires.
- Records: tdiff 0 (G′'s own run under my tie rule equals the transported run on every pair); gtNC 0 (no BR-SEG-form window above |C|
  for a ≥ t0).
- Limits, stated plainly: windows are short (max 7 against N′ up to 153), so the data test that nothing breaks, not tightness. Exact
  Howard ties occur on 2 of the 26 instances (DWT20_2803 1, C98_5_5_3 2), so «any tie resolution» is carried by the proof (§2), not by
  data. Large zero counts are DATA, not evidence of the lemma.

## 6. Addendum C's route (read for consistency; not re-derived as a verdict)
- Theorem R-SPLIT's arithmetic follows from its three inputs (R ≤ Σ flips by K2-r; TWO-CROSS's injective charge per face; DEPTH-COUNT3
  with D1's fix). I did not referee DEPTH-COUNT3.
- **N-1 (for the Lead).** TWO-CROSS (box 100 §2) is P-N5-GATE §3.1 Lemma GATE-RACE (a), (b) (packet sha1 f3a584e6…: «(a) If o flips at t
  from face p to face q, then Ω_t(p) ≠ Ω_(t−1)(p). (b) #flips(o) ≤ min(ch_p + ch_q, 2·min(ch_p, ch_q) + 1).», same proof), signed by
  both referees on both runs (R-P-N5-GATE §0 row 3.1) and due to land as R128. The route can cite it by R-id then, not as a lane lemma.
- N-2. DEPTH-COUNT3's Λ part (≤ n3 − 1 changes per vertex) is weaker than landed R118 (e) / (l) (≤ 2M + 2 per vertex, C ≤ n3·(2M + 2)).

## 7. TARGET.md diff and scope
- RESTRICT-C bounds a window length on Γ3(G), a restricted class; no algorithm claim, no bound on T3 (DEEP3 is a CONJECTURE). Not M3, not
  M4 (TARGET.md §2, §4), not a step-4 pass. G-N5-TIME stays OPEN; N5′-xi stays a CANDIDATE (D1).

## 8. Tools and outputs (docs/referee/scratch/)
restrictc_quotes.py, restrictc_replay.py; restrictc_logs/: quotes_C1.out, quotes_D2.out, replay_inst.out, replay_{rand,deep,wide,acyc,
selfl}.out, replay_inst_compress.out, replay_rand_compress.out, literal_iv_C6G8.out. Instances: `git archive d8945c4a` of
experiments/si/box91/inst, box93/inst, box98/inst into the scratchpad, `sha1sum -c SHA1SUMS` 11 / 8 / 7 OK.

## Addendum 1 (REFEREE successor 32; date -u at writing 2026-11-12T14:03Z): the Lean proof commit, seen and built
- claude/l-formal 4b376da4 (ancestor of origin/claude/l-formal, checked) reached origin after §3 was written. Defs.lean (sha1 b41c937c…)
  and Statements.lean (aaa3c0c2…) are byte-identical to 9dde1527, so §3's comparison is of the statement that is now proved:
  Corollaries.lean (sha1 c8f5b435…) l. 52 `theorem brseg : BrSegStatement V`, by `lam_gap_sharp` on the window a, …, a + j + 1.
- Own build (a referee's build, not CHECKER's exact-commit run): `git archive 4b376da4 lean/lemmas` into the scratchpad; Lean v4.35.0 by
  elan, Mathlib cache at the pinned commit 56a00585…; `lake build`: «Build completed successfully (3149 jobs).»; `grep -rnw
  --include=*.lean -e sorry -e admit -e axiom . --exclude-dir=.lake`: no output; `lake env lean Axioms.lean`: «'PG.brseg' depends on
  axioms: [propext, Classical.choice, Quot.sound]», the same for lam_gap_sharp, brsegG, brsegG_noH0 (scratch/box208_logs/lean_*.out).
- So §0's second row now reads: hypotheses MATCH, and the theorem of that exact type is proved in Lean at 4b376da4 (my build). The
  tie-rule caveat is settled twice, on the landed text (§2) and by Lean, given the bridges B-1 (injective priorities = SPEC's p′) and
  B-2 (F1 = landed R15 (a), a Lean hypothesis). C-1 can be met by citing `PG.brseg` by name and commit once CHECKER has run it.
- Nothing else in this report changes. W-1, W-2 and C-1 stand.
