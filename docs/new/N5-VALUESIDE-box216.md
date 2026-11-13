# Box 216 (D18): VALUE SIDE — which landed value-side lemmas hold for ANY improving run of standard states (hence for N5's key run on Γ3(G) under [IMP3]); XFLIP (moves ≤ 1 + XF for degree-2 movers, PROVED lane for N5 on every game); JOINT-POLY (a reformulation of O1′ at degree ≤ 2, not progress). Not a bound; G-N5-TIME stays OPEN; not M3, not M4
L-NEW successor 76 (session_01V5yGRXFkFRGsbtdAPyKqXN), D1 / D14 / D18 / D21. STATEMENT written 2026-11-13 from 06:45Z (date -u), before
any run. Approved by the Lead 04:58Z as successor 75 proposed it (its 04:57Z message, relayed verbatim by the Lead 06:44Z): «V1 first (the
per-lemma rule-free reading, with deciding lines), then V2 XFLIP (proof plus counter), with V3 JOINT-POLY labelled honestly as a
reformulation equivalent to O1′ at degree ≤ 2 up to a factor N». Lead «go» 06:44Z: «Quote every deciding line by script, as briefed.»;
«State the definition exactly as you will count it, including how ties (equal values) are treated, in the statement before you run anything.»
Labels: READING (V1: what the landed proofs prove, line by line), PROVED (lane; unrefereed) for V2 and for the two re-proofs in V1,
CONDITIONAL where named, REFORMULATION (V3), DATA (§5, not to sign). Nothing here is a RESULTS entry. **G-N5-TIME stays OPEN.**

## 0. Setting and the one hypothesis
- Γ3(G), standard states, Ω_t (the [VJ] value against Odd's pointwise-optimal reply σ̄_t), HOW3(G), T3: as in RESULTS R125 (P-N5-CHAIN §2).
- An IMPROVING RUN OF STANDARD STATES: states 0, …, T, each a standard state of Γ3(G) (non-mover Even vertices at the standard choice,
  P-N5-CHAIN [G3]), each step t → t + 1 changing σ exactly at a non-empty set of movers, each to a successor y with Ω_t(y) ▷ Ω_t(σ_t(x)).
  No rule says WHICH movers move or WHICH strictly better successor they take. Howard's run HOW3(G) is one such run.
- [IMP3] (box 212 §6, CONDITIONAL there; source W-FLAT, box 104, lane): N5's run from S3 on Γ3(G) up to its first fallback is such a run
  (with the READING «Ξσ's order on Γ3 is Ω_t's», box 212 §6). Everything V1 marks RF therefore holds for N5's key run under [IMP3].
- A lemma is **RF** (rule-free) if its proof uses, of the run, only: F1 (values never fall), the strict half of F5 («strictly better than
  the current option when they differ»), facts proved from these (STRICT, CYC), and per-state (static) lemmas. It is **HOW** if a deciding
  line uses F5's «⊴-best» half, DOM (which uses it), the tie rule [HOW] / [N5XI], or QUIET3 / T-QUIET3 (which use DOM).

## 1. V1 READING (dated 2026-11-13 ~06:20-06:50Z; proofs read in the landed packets at trunk 65e02855; every «…» after a [Q] tag is
## checked by experiments/new/box212/quotes212.py with DOC = this file, output experiments/new/box216/quotes216.out)
### 1.1 Why F1 and STRICT are RF
- F1's source is R15 (a), stated for ANY improving set: [Q R15] «Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00
  §4.4), Ωσ ⊴ Ω_{Switch_I(σ)}.» P-N5-CHAIN's F1 uses only that a step is such a set: [Q docs/new/P-N5-CHAIN.md@65e02855] «A Howard step
  switches exactly the movers whose new successor is strictly better, one switch per vertex: a non-empty unambiguous set of improvements
  (VJ00 §4.4)». An improving run's step is such a set by definition (§0). **RF.**
- F5 has two halves: [Q docs/new/P-N5-CHAIN.md@65e02855] «F5. σ_(t+1)(x) is ⊴-best among x's successors under Ω_t, and Ω_t(σ_(t+1)(x)) ▷
  Ω_t(σ_t(x)) when they differ (definition of HOW3).» The first half is **HOW**; the second is §0's definition (**RF**).
- DOM is **HOW**: its last inequality is F5's first half: [Q docs/new/P-N5-CHAIN.md@65e02855] «which by F5 and F4′ is ⊵ ext(x, Ω_t(y)).»
- STRICT uses DOM only at y = σ_(t+1)(x): [Q docs/new/P-N5-CHAIN.md@65e02855] «Proof: DOM gives ⊵ ext(x, Ω_t(σ_(t+1)(x))); F5 and F4′
  (strict) give ▷ ext(x, Ω_t(σ_t(x))) = Ω_t(x) by F3 and F6.» and that part of DOM's proof is F1 + F4′ + F3 + F6 only:
  [Q docs/new/P-N5-CHAIN.md@65e02855] «F3, F6 at t + 1 give Ω_(t+1)(x) = ext(x, Ω_(t+1)(σ_(t+1)(x))); by F1 and F4′ (x ∉ any Π, CN2-3) this is
  ⊵ ext(x, Ω_t(σ_(t+1)(x)))». The strict step is F5's second half. So **STRICT is RF** (re-proof: these two lines, nothing else; PROVED
  lane).
- CYC is F1 + F2 + static facts: [Q docs/new/P-N5-CHAIN.md@65e02855] «and by F1 and F2 it changes only to a vertex of strictly larger
  reward.» **RF.** F2, F3, F4′, F6 are [VJ] facts or properties of standard states: **RF** (no run property).

### 1.2 The table (verdict, then the deciding line; «static» = proved for every standard state / every positional pair, no run property)
- R121 (IDEAL-CYC; the Γ3 forms below are the ones N5 needs). **E-MON: RF** — [Q docs/new/P-N5-ASC.md@65e02855] «F1: Ω_t(v) ⊴ Ω_(t+1)(v).
  With equal cycle node w, [VJ] decides by z» (F1 on IDEAL-CYC for any improving run: box 212 RF-A). **CHAIN-DECOMP: RF** (static; its
  proof cites only [DEF], F3 and the play). **SKELETON, HUB-ASC(B): RF** (abstract chain systems). **HUB-ASC-G: RF** (E-MON, CHAIN-DECOMP,
  F1, F2). **UP-JUMP, UP-B, NOUP: RF** (static, under [E-LEV]).
- R125 (Γ3). **REACH3-ALL**: a statement about N5′-xi's run only; not transferable (N5's analogue is [IMP3], box 212 §6). **ESC3-ALL,
  W3-ALL, CN2-3, LOC-GATE3, LOC-K2-3, B-ONLY3, NO-TIE3: RF** (static; box 212 §2 read their proofs: no run property). **F1, F2, F3, F4′,
  F6, STRICT, CYC: RF** (§1.1). **F5 (first half), DOM: HOW** (§1.1). **QUIET3, T-QUIET3: HOW** — (Q2): [Q docs/new/P-N5-CHAIN.md@65e02855]
  «(by DOM x's value at t + 1 would lie in that class)»; (Q5): [Q docs/new/P-N5-CHAIN.md@65e02855] «by induction on h with DOM at x».
  **(F-cls3) and «Q ≤ Σ_v (D^tot_E(v) − 1)»: RF** — [Q docs/new/P-N5-CHAIN.md@65e02855] «So each class is a convex set of values, each
  vertex is in each class during one interval of states (F1), distinct classes compare the same way at all times, and Q ≤ Σ_v
  (D^tot_E(v) − 1).» (non-core vertices, W-1 repair, P-N5-CHAIN fixes entry 3). **E-MON3: RF** — [Q docs/new/P-N5-CHAIN.md@65e02855]
  «Proof. F1: Ω_t(v) ⊴ Ω_(t+1)(v).» **CHAIN-DECOMP3: RF** (static). **HUB-ASC-G3: RF** — its proof uses
  [Q docs/new/P-N5-CHAIN.md@65e02855] «E-MON3, CHAIN-DECOMP3, F1, F2, CYC on Γ3» (its intervals of states of HOW3(G) read as intervals of the
  run). **UP-JUMP3, UP-B3: RF** (static: [Q docs/new/P-N5-CHAIN.md@65e02855] «UP-JUMP3 is a statement about plays»). **CHAIN3: HOW**
  (its proof applies T-QUIET3 and REACH3-ALL).
- R127 (HOW3). **SPLIT (i): RF** (static: [Q docs/new/P-N5-SPLIT.md@65e02855] «Non-mover Even vertices and pads have one successor in
  HOW3 (F6, [G3]).» — in an improving run of standard states too). **SPLIT (ii): RF** — its line [Q docs/new/P-N5-SPLIT.md@65e02855] «F5:
  σ_t(u) is ⊴-best under Ω_(t−1) and strictly better than σ_(t−1)(u) when they differ.» cites F5, but the claim (ii) «Ω_(t−1)(new) ▷
  Ω_(t−1)(old)» is its second half alone. **SPLIT (iii), (iv) TRANSFER: RF** (LOC-GATE3, NO-TIE3, F1, (PL)). **REWIN (a): RF** — mover
  case: [Q docs/new/P-N5-SPLIT.md@65e02855] «Then Ω_(t2−1)(u) ⊵ Ω_s(u) (F1) ▷ Ω_(s−1)(u) (STRICT) = ext(u, Ω_(s−1)(b)) ⊵ ext(u, Ω_t1(b))»
  (F1, STRICT, F4′: RF). **REWIN (b): RF** — [Q docs/new/P-N5-SPLIT.md@65e02855] «At t2, u moves from a to b. Mover: Ω_(t2−1)(b) ▷
  Ω_(t2−1)(a) (F5).» (second half only). **REWIN-HI (c), REWIN-COUNT, PAIR-SPLIT, SPLIT-COUNT: RF** (PAIR-SPLIT:
  [Q docs/new/P-N5-SPLIT.md@65e02855] «Proof: §3's proof with (t1, t2) := (t, t′).»; SPLIT-COUNT adds E-MON3, F1, F2 and the edge count).
  **RW-SHAPE(*), RW-1: RF** (§3 (b), F1, F2, E-MON3). **PAIR-HIGH, RA-PATHS, PAIR-COUNT, RE-COUNT: RF** (abstract / E-MON3). **ASC-WIT,
  ASC-ROOT: RF** (static: [Q docs/new/P-N5-SPLIT.md@65e02855] «Static (any σ against an optimal σ̄); not a bound.»). **RE-EQUIV, ALT-EQUIV,
  C-EQUIV: HOW in their upper-bound halves (T3 bounded by the count)** — [Q docs/new/P-N5-SPLIT.md@65e02855] «Sum D^tot_E(v) − 1 over the n3 vertices and apply
  T-QUIET3.»; their «≤ T3» halves (Rtop ≤ n3·T3, A ≤ max(1, T3), C ≤ max(1, T3)) are RF.
- R128 (HOW3 and IDEAL-CYC). **GATE-RACE (a), (b), TRIGGER: RF** — [Q docs/si/P-N5-GATE.md@65e02855] «LOC-GATE3 and NO-TIE3 at t − 1
  (Odd on p) and at t (Odd on q), with F1 for q» **GATE-LOW-NULL (a), (b), (b′): RF** (static + E-MON3: [Q docs/si/P-N5-GATE.md@65e02855]
  «Both faces are in one Λ-interval over {t − 1, t} (hypothesis), so E(p_b) is lex-nondecreasing (E-MON3)»). **NP-SHAPE: RF** (static).
  **E-FACE-PAYS (a)-(d), WAIT-QUIET: RF** — [Q docs/si/P-N5-GATE.md@65e02855] «GATE-RACE (a) uses F1 and Odd's ◁-choice only.»
  **SAME-SUFFIX: Odd half RF, Even half HOW** — [Q docs/si/P-N5-GATE-fixes.md@65e02855] «an Even mover is at t on a ▷-best option for the
  values at t − 1 ([HOW]).» **STEP-BOUND: RF** ([Q docs/si/P-N5-GATE.md@65e02855] «A value is a function of the play; a play changes only if
  a successor on it changes.»). **PARALLEL: RF** ([OPT], E-MON3, positional plays). **PAIR-EXPEL, EXPEL-COUNT: RF** — Step 1 is REWIN (a)'s
  argument: [Q docs/si/P-N5-GATE-fixes.md@65e02855] «(the argument of P-N5-SPLIT §3 (a), Lemma REWIN (a), with F1, STRICT, F3, F4′, CN2-3;
  nothing of P-N5-SPLIT is a premise)». **A*-EQUIV (i), (ii): RF; (iii) HOW** (through C-EQUIV's T-QUIET3 half). **PROVISO on Γ3: RF**
  (B-ONLY3 at the mover D, static).

### 1.3 What V1 gives (CONDITIONAL on [IMP3]; PROVED lane given the table, which is a READING to be refereed)
- (V1-a) Every RF item above holds along N5's key run on Γ3(G) of every genome, up to its first fallback.
- (V1-b) The Howard-only items are exactly: F5's «⊴-best» half, DOM, QUIET3 / T-QUIET3, CHAIN3, REACH3-ALL, the «T3 ≤ …» halves of
  RE-EQUIV / ALT-EQUIV / C-EQUIV / A*-EQUIV (iii), and SAME-SUFFIX's Even half.
- (V1-c) SAME-SUFFIX-IMP (PROVED lane; the RF replacement of SAME-SUFFIX's Even half). On a window W as in SAME-SUFFIX, in any improving run
  an Even mover o changes σ(o) at most deg(o) − 1 times on W. Proof: SAME-SUFFIX's proof makes the ⊴-preorder of o's successors constant on W;
  each change goes to a strictly ▷-larger successor (§0), so the ⊴-class of σ(o) strictly rises at each change; there are at most deg(o)
  classes. ∎
- (V1-d) LOUD-RF: stated in §1.4 as a CONDITIONAL reduction (Lead 06:49Z point (1)).

### 1.4 LOUD-RF (CONDITIONAL reduction, not a bound) and the missing QUIET piece
Definitions, with sources (all landed):
- [Q docs/new/P-N5-CHAIN.md@65e02855] «U(G) := the number of options (x, k) whose Ξ-target is a mover of level > lev(x).»
- [Q docs/new/P-N5-ASC.md@65e02855] «Here F′_0(M) := 1 + M(M + 1)/2 and» with [Q docs/new/P-N5-ASC.md@65e02855] «F′_B(M) := (M² + 3M + 1)(1 + M·F′_(B−1)(M)²).»
  (R121's line: [Q R121] «F′_0 = F_0 (DESC-POLY on the whole interval), F′_B(M) = (M² + 3M + 1)(1 + M·F′_(B−1)(M)²)»). For fixed B, F′_B
  is a polynomial in M.
- [Q docs/new/P-N5-ASC.md@65e02855] «HYPOTHESIS [E-LEV] (only for §6 UP-JUMP and UP-B): the e-priorities increase with the level of their
  gate's mover. Formally: lev(x) < lev(x′) implies pr(e_(x,k)) < pr(e_(x′,k′)).» It is a property of the builder, not of a landed R-id.
- class_t(v) := (Λ_t(v), E_t(v)); a step is LOUD if some vertex changes class, else QUIET; Q := #loud steps; a quiet window is a maximal
  interval of states whose steps are all quiet (P-N5-CHAIN §6's definitions, verbatim in meaning); Wq := the longest quiet window (steps).
**LOUD-RF (PROVED lane given the V1 table; CONDITIONAL on [IMP3] and [E-LEV]).** On N5's key run on Γ3(G) up to its first fallback:
  (a) Q ≤ Σ_v (D^tot_E(v) − 1) ≤ n3·((2M + 3)·F′_(U(G))(M) − 1), n3 = N + 7M + 10;
  (b) T_key ≤ Q + (Q + 1)·Wq.
Proof. (a): (F-cls3) is RF (§1.2); D^tot_E(v) ≤ (2M + 3)·F′_(U(G))(M) is HUB-ASC-G3 with UP-B3, both RF, the second under [E-LEV]. (b): the
steps are loud or quiet, and the quiet ones form at most Q + 1 windows. ∎
So, under [IMP3] and [E-LEV], on every genome class with U(G) ≤ B (B fixed), O1′ (T_key polynomial) holds IF Wq is polynomial. Not
claimed: any bound on Wq.
**The missing piece, named.** QUIET3 bounds Wq ≤ L3 for Howard; its only HOW lines are (Q2)'s «by DOM» and (Q5)'s Bellman-Ford induction
«with DOM at x» (§1.2). Everything else in its proof ((Q1), (Q3), (Q4), (F-cls3), the gate-flip count in (Q5)) is F1 + LOC-GATE3 / NO-TIE3
+ static. Inside a quiet window, (Q4)-(Q5) reduce the run to sub-windows on which, for each B-class C, the graph G_C (C's movers with the
options whose gate's chosen face is in C), its chosen faces and C's boundary values are constant; there the run is an improving run of
a FIXED one-player game: each C-mover picks a G_C-option, plays are simple G_C-paths (internal edges: β-faces to Ξ-targets) ending at a
boundary point (an e-face into the class (w, S ∖ {e}), the core exit, or w), compared by [VJ]. The smallest statement that would replace
the DOM step:
- **QUIET-RF (OPEN).** There is a polynomial p such that every improving run of standard states, on a sub-window of a quiet window in
  which G_C, its chosen faces and C's boundary values are constant, has at most p(N, M) steps. With (Q5)'s count of sub-windows (at most
  2M + 1 per class level, M + 1 levels) and (Q3) (E-class movers: at most N(n3 − 1) changes, RF: F1 only), QUIET-RF gives
  Wq ≤ (M + 1)(2M + 1)(p(N, M) + 1) + N(n3 − 1) for EVERY improving rule, and then LOUD-RF gives O1′ under [IMP3], [E-LEV], U(G) ≤ B.
- **QUIET-KEY (OPEN; weaker, enough for N5).** The same with «improving run» replaced by «N5's key run» (KEY-TAU's rule).
- READING (not a claim): a sub-window is a one-player lexicographic path game on the Ξ-graph of one class, i.e. box 212 RF-D's «generalised
  O1»; QUIET-RF asks it for every improving rule, QUIET-KEY for the key rule only. DATA (§5 (vi)): on the tower DBL4_d20_F30, N5's whole
  key run is one quiet window with no gate flip (Q = 0, Wq = Tk = 30), so the towers are QUIET-KEY instances: an exponential tower family
  (L-LOWER L18's attempt) would refute QUIET-KEY and QUIET-RF at once, and with them this route.

## 2. V2 XFLIP (PROVED, lane; holds for N5's WHOLE run on EVERY game, fallbacks included)
**Definitions (exactly as counted).** Run N5 (SPEC S1-S5) on a game; states σ_0, σ_1, …, σ_T (σ at the start of each iteration and at the
end). For an Even vertex x with exactly two successors y_0, y_1 and a state t, let Ξ_t := Ξ_(σ_t) (SPEC S1's valuation of σ_t, against
σ̄_t) and d_t(x) := 0 if Ξ_t(y_0) is strictly better than Ξ_t(y_1), 1 if Ξ_t(y_1) is strictly better, and «=» if they are equal (TIE).
Delete the TIE states; XF_x := the number of states t of the remaining sequence whose d_t(x) differs from that of the previous remaining
state (alternations of the strict order, ties skipped). moves(x) := #{t ≥ 1 : σ_t(x) ≠ σ_(t−1)(x)}.
**Statement.** moves(x) ≤ 1 + XF_x. More generally, for x with d ≥ 2 successors, moves(x) ≤ (d − 1)·(1 + OC_x), OC_x := the number of
t ≥ 1 at which the weak order of x's successors under Ξ_t differs from that under Ξ_(t−1).
**Proof.** Every change of σ(x) is to a strictly Ξ_(t−1)-better successor: in S4a σ_new is a strategy of the arena H, whose Even edges go
to A(v): [Q docs/new/N5-ssi-global.md@65e02855] «A(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ} for Even v.» with [Q docs/new/N5-ssi-global.md@65e02855]
«Iσ = {(v, w) : owner(v) = Even, w ≠ σ(v), Ξσ(w) strictly better than Ξσ(σ(v))}»; in S4c the fallback takes an edge of Iσ: [Q docs/new/N5-ssi-global.md@65e02855] «for every Even v with an improving edge set σ_new(v) = the w with (v, w) ∈ Iσ»;
S4b does not change σ: [Q docs/new/N5-ssi-global.md@65e02855] «Even v only the edge to σ(v).» and «τ_new = Odd's optimal counterstrategy (S1 procedure on H', not dual) to σ.» Degree 2: let t_1 < t_2 < … be the move steps; x alternates y_a → y_b → y_a …, so d_(t_i − 1)(x) is the new successor, a strict
value, and these alternate; between two consecutive moves the remaining sequence alternates at least once at a state in
(t_i − 1, t_(i+1) − 1], and these intervals are disjoint. So moves(x) − 1 ≤ XF_x. Degree d: between two consecutive order changes the weak
order is constant and each move strictly raises σ(x)'s class, at most d − 1 times. ∎
- On successor 75's «(F2)»: the step used is SPEC S2's strictness (with S4a's A(v)), not P-N5-CHAIN's F2 (cycle rewards). READING: «F2»
  there named S2.
- With box 215 (CONDITIONAL on KEY-TAU (i)): moves(x) ≤ 1 + min(KF_x, XF_x); sharper, §3's JF_x.

- NULL switches (Lead 07:13Z, from L-RED-B 4's B5, lane DATA): N5 can switch x to a successor that is strictly Ξσ-better ONLY by the
  length component, with x the cycle node of both plays, so that no valuation changes (S4a keeps σ in the arena tie and S4c's fallback
  takes the switch, or S4a's arena takes it). XFLIP covers it: d_t(x) compares the WHOLE si.Engine key (cycle reward, path weight, signed
  length), so the new successor is strictly better at t − 1 and the move is counted in moves(x); its proof uses only «strictly better
  before the move». A null switch leaves d unchanged, so moving back needs a later strict reversal, i.e. an alternation. Own instance
  inst/NULLSW_n4.pg (4 Even vertices: v = 0 of priority 8 with edges to a (length 2 back to v) and b (length 1)): N5 switches v from a
  to b with every valuation unchanged (vals (0, 0, 0), (0, 0, 2), (0, 0, 1), (0, 0, 1) before and after); xflip216: xmove 0, xflip 0.
- Where it matters for V1: STRICT (σ changes, so Ω(x) strictly rises) is FALSE at a null switch. V1's list is for Γ3's MOVERS, where F6
  [Q docs/new/P-N5-CHAIN.md@65e02855] «No mover is the cycle node of its own play» excludes it, so STRICT and everything citing it ((Q6), REWIN (a), PAIR-EXPEL Step 1)
  stand on Γ3; gate216's counter strict is 0 on the frozen set. LOUD-RF counts steps (loud or quiet), not value changes, and does not
  assume that a move changes a value; QUIET-RF's count of E-class moves ((Q3), (Q6)) uses STRICT, hence F6, hence Γ3.

## 3. V3 JOINT-POLY (REFORMULATION; honest label)
**Definition (as counted; degree-2 movers on Γ3, N5's key run before its first fallback).** KP_t(x) as in box 215 (the key-least option
under s_t, KEY-TAU's keys). J_t(x) := k if option k is strictly Ξ_(t−1)-better than the other option AND KP_t(x) = k; else «none».
JF_x := the number of steps t whose J_t(x) ≠ none differs from the previous non-none J value.
**JOINT (PROVED lane, CONDITIONAL on KEY-TAU (i) through box 215's reading of N5's choice «the option in A_(s_(t−1))(x) with the least
key_(s_t)(x, ·)»).** moves(x) ≤ 1 + JF_x and JF_x ≤ min(KF_x, XF_x). Proof: a move to option b at t has b ∈ A_(t−1)(x) (strictly
Ξ_(t−1)-better, §2) and b key-least in {current, b} = all options (degree 2), so J_t(x) = b; moves alternate, so JF_x ≥ moves(x) − 1. Two
consecutive J-alternations t < t′ (values a then b) have a KP change in (t, t′] and an XF alternation state in (t − 1, t′ − 1]; for
consecutive alternations these intervals are disjoint. ∎
**JOINT-POLY (OPEN; a reformulation, not progress).** Σ_x JF_x ≤ poly(N + M) on N5's key run before its first fallback, for every genome
with every mover of degree ≤ 2. Then T_key ≤ N + Σ_x moves(x) ≤ 2N + Σ_x JF_x (each step moves a mover, [IMP3]). HONEST LABEL: since
JF_x ≤ T_key, Σ_x JF_x ≤ N·T_key, so JOINT-POLY ⟺ O1′ at degree ≤ 2, up to a factor N. It names the coupling (a move needs the key order
and the Ξ-order to agree); it does not bound it.

## 4. Kill criteria
- V1: a lemma marked RF whose counter fires on N5's key run (a must-0 below > 0) kills that RF verdict (and with it V1-a for that lemma);
  a lemma marked HOW whose counter fires there is confirmed NOT rule-free (expected for F5-best, DOM; recorded either way).
- V2: xmove > 0 or xflip > 0 or xflipd > 0 on any run kills XFLIP (and would contradict SPEC S2 / S4a as implemented).
- V3: jmove > 0 or jfmin > 0 kills JOINT; a genome family with Σ JF super-polynomial in N + M kills JOINT-POLY (and then O1′ at degree ≤ 2).

## 5. DATA plan (tools in experiments/new/box216/; nothing run before this statement)
- V1 (N5 = SPEC mode, before the first fallback; Howard xi mode as reference): (i) box 196's qt3_196.py with Q196_MODE=spec (unchanged
  tool): must-0 cnlow, locfail, ties, bonly, k2fail, upfail, emon; HOW items wfail (QUIET3), Tfail (T-QUIET3) recorded, not must-0;
  nohoward is the firing control (fires in spec mode). (ii) box 199's split199.py under SPEC mode through an import wrapper split216.py
  (no file of box 199 edited): must-0 playfail, kindfail, hwfail, gtfail, trfail, dnfail, rhfail, rh2fail, spfail, rw1fail, wlamfail.
  (iii) gate216.py (new, Γ3, SPEC and xi modes): must-0 f1 (F1), strict (STRICT), grfail (GATE-RACE (a)), gr2fail (GATE-RACE (b)),
  efp (E-FACE-PAYS (a)), npshape (NP-SHAPE (a)), stepb (STEP-BOUND), par (PARALLEL (i)-(iii)), pexp (PAIR-EXPEL), ssimp (V1-c: moves on a
  maximal interval of constant weak order > deg − 1), loud (V1-d: Q > Σ_v (D^tot_E(v) − 1)); HOW descriptive: f5best ((state, mover):
  the new successor not ⊴-best), dom (DOM violated); Wq (longest quiet window). Firing controls: G216_CTRL=1 (F1 tested with the order
  reversed: f1 fires), G216_CTRL=2 (Odd's face read as the ▷-LARGER face: grfail fires), and xi mode, where f5best and dom must be 0.
- V2 xflip216.py (any game; N5's whole run, SPEC mode; Ξ from the n5v Engine's key): must-0 xmove ((step, Even vertex): σ changes to a
  successor not strictly Ξ_(t−1)-better), xflip (degree-2 Even vertices: moves > 1 + XF), xflipd (degree ≥ 3: moves > (d − 1)(1 + OC)).
  Controls: X216_CTRL=1 swaps the two successors' Ξ values («swap the gates' Ξ values», the Lead's control): xmove must fire at every move;
  X216_CTRL=2 sets XF := 0 and OC := 0: xflip / xflipd must fire wherever a vertex moves twice (shows the counter is not vacuous).
  Sets: Γ3 of box 212's frozen genomes + the 5 towers + box 213 inst + 600 random Ξ-cyclic genomes; and, since V2 is about every game,
  Oink's generated families at small size (tc, tc+ via tools/oink/build, if they run under n5v in time; else NOT RUN, named).
- V3 (degree-2 genomes only, N5 key run on Γ3): per mover KF, XF, JF, moves; must-0 jmove (moves > 1 + JF), jfmin (JF > min(KF, XF));
  descriptive: Σ JF, max JF, T_key, and Σ JF / (N·T_key). Towers and the ladder genomes L^R_d of box 215 for growth (numbers on named
  instances only, L43).
- (vi) QUIET under other improving rules (Lead 06:49Z point (1)): gate216.py with G216_MODE = idx and seq (box 190's n5v modes: S4a's
  TIE by largest index; SPEC's σ_new at ONE vertex), with xi (Howard) and spec (N5): Q, Wq and Tk per genome, plus every must-0 counter
  (each mode is an improving run of standard states, so the RF counters must be 0 in every mode). Descriptive; QUIET-RF and QUIET-KEY
  are not tested by finitely many instances.
- Runners resumable (600 s per genome), at most 2 CPU jobs, outputs pinned (SHA1SUMS), summ216.py, check216.sh + a check.sh block.

## 6. Not claimed
No bound on T_key, T3 or any quiet window of N5; nothing after the first fallback except V2 (which is about every iteration); nothing about
Ξ-order = Ω_t-order beyond box 212's READING; V1 is a reading of proofs, not a re-proof (except STRICT, SAME-SUFFIX-IMP, LOUD-RF, XFLIP,
JOINT, written out above). TARGET.md §2 (M4) asks for a deterministic algorithm polynomial on every parity game; nothing here is that.

## 7. DATA (not to sign; run 2026-11-13 06:53Z-07:35Z by date -u, two workers, one container restart at ~07:07Z resumed from the
## outputs; every number below is from summ216.py's output out/summ216.txt; outputs pinned in out/SHA1SUMS)
Sets: FROZEN = box 212's 81 frozen genomes (run212.sh's ALL list) + the 5 towers of box212/inst (DBL4_d20_F30, H5_d20_F62, H6_d24_F126,
HIT7_d28_F254, RECF4_d20_F60; copied from claude/l-comp 2fa72fb5, L-COMP box 29, box212/inst/SOURCE.txt) + box213/inst (TAUESC_rand2150, TAUESC_dense2151): 88 genomes, 0 timeouts in every row.
RAND = eg195.gen family «rand», Ξ-cyclic only, 200 genomes per seed (seeds 2161-2163; qt3: 2161, 2162).
- (i) qt3_196.py, Q196_MODE=spec, FROZEN: cnlow, locfail, ties, bonly, k2fail, upfail, emon, nonstd 0 (must0_sum 0); HOW items: nohoward
  14,440 (fires: N5 is not Howard), wfail 0 and Tfail 0 (QUIET3's bound L3 is not violated by N5 on these 88, though it is not proved
  for N5); RAND 2161, 2162: must0_sum 0.
- (ii) split216.py (split199.py unchanged, spec), FROZEN: playfail, kindfail, hwfail, gtfail, trfail, dnfail, rhfail, rh2fail, spfail,
  rw1fail, wlamfail 0 (must0_sum 0).
- (iii) gate216.py, FROZEN, spec: f1, strict, imp, grfail, gr2fail, efp, npshape, stepb, par, pexp, ssimp, loud 0 (must0_sum 0); HOW
  items fire: f5best 14,440, dom 37,209. xi (Howard): must0_sum 0 and f5best 0, dom 0. RAND 2161-2163, spec: must0_sum 0. So no RF
  verdict of §1.2 is killed, and the two HOW items checked by counter (F5's first half, DOM) are confirmed NOT rule-free on N5's run
  (kill criterion V1, as stated).
- (iv) xflip216.py, FROZEN (whole run, spec): xmove, xflip, xflipd 0; RAND 2161-2163: 0; own null-switch instance inst/NULLSW_n4.pg: 0.
- (v) V3, FROZEN: jmove 0, jfmin 0 (degree-2 movers); RAND: 0. Σ JF > 0 on 6 of 88 genomes only: the five towers and W14_n75 (Σ JF 1). Towers
  (Tk; Σ moves of degree-2 movers before the fallback; Σ KF; Σ XFm; Σ JF; max JF): DBL4_d20_F30 30; 100; 272; 124; 73; 14 —
  RECF4_d20_F60 67; 203; 512; 248; 171; 29 — H5_d20_F62 136; 351; 748; 482; 327; 31 — H6_d24_F126 209; 491; 998; 614; 456; 62 —
  HIT7_d28_F254 299; 1103; 2304; 1277; 1066; 126. On the MW / MWR / CW families KF = JF = 0 and every degree-2 mover moves once
  (e.g. MW32_2: Tk 196, 260 movers, 260 moves).
- QUIET (the §1.4 target), FROZEN, gate216 Q / Wq: on the five towers N5's key run has Q = 0, no gate flip and Σ_v (D^tot_E(v) − 1) = 0:
  the whole run is ONE quiet sub-window with G_C, its faces and the boundary constant, of Wq = Tk = 30, 67, 136, 209, 299 steps; Howard
  (xi) on the same genomes is also all quiet, with Wq = Tk = 9, 9, 9, 12, 8. On the MW families both runs are all loud (Wq = 0;
  N5 Tk 196 vs Howard 199 on MW32_2). Largest Wq over FROZEN: N5 299 (HIT7), Howard 12 (H6). So the towers are exactly QUIET-KEY's
  instances: a fixed one-player game on which Howard's Bellman-Ford step converges in ≤ 12 steps and N5's key rule takes up to 299.
- (vi) other improving rules (idx, seq): in progress at this commit (runC216.sh); reported in the next push.
