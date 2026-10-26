# R2-N5-ROOT: REFEREE-2 report on P-N5-ROOT-box20 (BF-F_D, FREEZE-A, R-LEN, ROOT-PIECE, DL-SPLIT) and its addendum P-N5-ROOT-add-box20 (GATE-SHIFT, FREEZE-G, RELAY-PIECE)
Referee: REFEREE-2 successor 17 (session_01P2K6kCftytexWsuJfNFtV4), Opus 5.5 (D15, L37). Written 2026-10-26 18:25Z (date -u).
Objects (both frozen, on trunk; author L-SI successor 16):
- docs/si/P-N5-ROOT-box20.md, sha1 d3788bc0ce0e3da2d54298c58e227e437242419a (`git show <trunk>:… | sha1sum`; l-si freeze ced5cf27), 164 lines.
- docs/si/P-N5-ROOT-add-box20.md, sha1 af1c7ad4581cce4a9830b4ed01e2370d26ef850b (l-si freeze 829003b2), 156 lines.
Independence: written before opening any REFEREE file on ROOT. `git ls-tree --name-only -r origin/claude/referee docs/referee/ | grep -ic root`
gave 2 at 17:07Z and 16 at 18:45:30Z, the push turn (file NAMES only, nothing opened; this report was final before that read). Lane tools
(experiments/si/root/*.py, experiments/si/rund/quotecheck.py) NOT run or imported.
Checker: docs/referee-2/R2-N5-ROOT/root_check.py (own; SPEC loop through my lane's R2-N5-RUND; Ξ and W are my own play values with the ENGXI
cross-check; D, F_D, A, R_u, DD, Δ, M, MW, MoptA, MoptG′ all computed by me, the optima by simple-path enumeration with a budget). It checks every
item at every state / transition / piece / interval, and FREEZE-A, FREEZE-G and RELAY-PIECE from EVERY start state s of each maximal run.
Quote check: my R2-N5-CHOSEN/qtags.py: 9/9 (packet) and 11/11 (addendum) tagged quotes verbatim at the tagged commits and lines.
Scope (D1): ROOT-PIECE is a REDUCTION (it bounds path-weight changes of an Odd vertex by (f + G_c + 1)·poly(n); G_c is not bounded); DL-SPLIT is a
decomposition, not a bound; RELAY-PIECE bounds re-routings per G-interval, the number of G-intervals is not bounded. Nothing here bounds N5's
running time, ρ, N_ep or f. Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Verdicts
| item | verdict | premises (checked) |
| --- | --- | --- |
| §2 Lemma BF-F_D | SIGN | (F1) on S4a's arena (P2), XW, G_D (a), (V1), (Aκ), (M1κ), (M2κ), injective rewards |
| §3 Theorem FREEZE-A (a), (b) | SIGN | BF-F_D; (Aκ), (A0κ), (M2κ); the lasso remark |
| §3 FREEZE-A (c) | SIGN (wording note N-ROOT-1: the q = c case is outside (Aκ)'s domain; the conclusion holds) | (b); κ-Y-FORM_D (P1) |
| §3 (R-LEN) | SIGN (wording note N-ROOT-2: its text speaks of Ξ on A_t, but q ∈ D_t is not in A_t; the count holds directly) | (b), (INJ), Ξ monotone |
| §4 Corollary ROOT-PIECE | SIGN (as a reduction in G_c) | FREEZE-A, R-LEN |
| §5 Lemma DL-SPLIT | SIGN; its condition is MET (RELAY-CHAIN landed as RESULTS R72) | R63 (a) R-STICK_D; κ-Y-FORM_D (P1); additivity; RELAY-CHAIN (R72) for (i) |
| add §2 Lemma GATE-SHIFT (a), (b) | SIGN | G_D (a), κ-Y-FORM_D, (Aκ); (b): XW, WM-G (R62 (d)), (F1) (P2), (V1), (M1κ) |
| add §3 Theorem FREEZE-G (a)-(c) | SIGN | GATE-SHIFT, BF-F_D / FREEZE-A (a)'s step, WM-G, (F1), (M2κ) |
| add §4 Corollary RELAY-PIECE (i), (ii) | SIGN | FREEZE-A (b), FREEZE-G (c), (M2κ) |
| the Lead's question (addendum §5: FREEZE-G (b), (c), RELAY-PIECE vacuous in the lane's data) | made to bite, partly: §2 | — |
No gap. Notes N-ROOT-1..7 (§3). Not reviewed (as both packets ask): ROOT §6, addendum §5-§6 (READING, DATA, OPEN).

## 1. Proof check (every step re-derived; the points worth recording)
### P-N5-ROOT
- BF-F_D. Case 1 is (Aκ) + (M2κ). Case 2: M_t(x) > M_t(σ_t v) with both values of cycle node c gives (v, x) ∈ Iσ_t, so σ″ := σ_t[v ↦ x] is a
  strategy of S4a's arena H_t, and σ_{t+1} (the arena optimum, premise P2 of 1E-N3) dominates it pointwise ((F1)); W_{t+1}(v) = Ξ_{t+1}(v) has
  cycle node c by G_D (a) (v ∈ F_D(t+1)). (i) x's play avoids v: (V1) gives W_{σ″}(v) = v ⊕ W_t(x); XW and the reward comparison force W_t(x)'s
  cycle node to be c (any other cycle node would have larger reward and propagate through W_{σ″}(v) ⊴ W_{t+1}(v)); then (M1κ). (ii) x's play
  passes v: with v ∈ F_D(t), MW_t(x) = wt(q) + M_t(v); XW at x and Case 2 give wt(q ∪ {v}) > 0, so the σ″-cycle Z = v → x → q → v has an even top
  of rank > rank(c) (the top dominates the signed sum), whose reward exceeds c's, and (F1) then contradicts W_{t+1}(v)'s cycle node c. CORRECT.
- FREEZE-A (a): induction on t − s. G[A_{t+1}] ⊆ G[A_t] (A non-increasing; Odd vertices keep the τ-edge; τ constant). Even z: BF-F_D (z ∈
  F_D(t) ∩ F_D(t+1) because A_{t+1} ⊆ A_t). Odd z: z ∉ D_{t+1}, so next_{t+1}(z) = τ(z) = x, then (Aκ), (M2κ). CORRECT.
- FREEZE-A (b): z ∈ A_t has its W-play = honest play (no D-vertex on it), staying in A_t, simple up to c, using G[A_t]'s edges; so M_t(z) is
  that path's weight ≤ MoptA_t(z). Paths of G[A_t] have ≤ |A_t| − 1 ≤ L edges, so (a) gives equality for t ≥ s + L, and the sandwich
  MoptA_{t′} ≤ MoptA_t (fewer paths) with (M2κ) gives constancy. CORRECT.
- FREEZE-A (c): q ∉ D_t ⇒ q ∈ A_t and M_t(q) = M_{s+L}(q) = wt(q) + M_{s+L}(τ q) ∈ V_q; q ∈ D_t ⇒ q on no honest cycle, q ≠ c, and (Aκ) gives
  M_t(q) = wt(q) + M_t(y*) with y* ∈ A_t, frozen by (b). (κ-Y-FORM_D is invoked but only (Aκ) is needed for membership in V_q.) Monotone M(q)
  in ≤ deg(q) values ⇒ ≤ deg(q) − 1 changes at the counted transitions. CORRECT; N-ROOT-1 for q = c (then q ∉ D_t, M(c) = 0, and τ(c) is c's
  successor on c's cycle, of M-value 0, so 0 ∈ V_q; the cited (Aκ) is stated for z ≠ c only).
- (R-LEN): over the counted states M(q) takes ≤ deg(q) values and, for each, the length is monotone in [1, |U| − 1], so κ(q) takes
  ≤ deg(q)(|U| − 1) values: ≤ deg(q)(|U| − 1) − 1 changes. CORRECT; N-ROOT-2.
- ROOT-PIECE: cut at the ≤ f + G_c fallbacks and A-gains; each of the ≤ f + G_c + 1 pieces satisfies FREEZE-A's hypothesis; per piece ≤ L ≤
  |U| − 1 transitions before s + L and ≤ deg(q) − 1 counted after. Arithmetic re-done for both bounds. CORRECT.
- DL-SPLIT. Split part: an entering z ∈ A_{t+1} ∖ A_t lies in R_D(t); if its first D_t-vertex u stays in D_{t+1}, R63 (a) R-STICK_D excludes
  z split, and z's old route up to u (Odd vertices on τ, unchanged) can avoid D_{t+1} at t + 1 only through an Even switch on it: (B).
  (A) with a clean change: if none of (i), (ii), TOG, then y1 = σ̄_t(u) ∈ Y^u_{t+1} with κ_{t+1}(y1) = κ_t(y1) (additivity, unchanged
  path, exit and exit value), κ-Y-FORM_D at t + 1 (minimum at y2), (SG), κ-Y-FORM_D at t (y2 ∈ Y^u_t by cleanness, minimum at y1): κ_t(y2) =
  κ_t(y1), a TIE. CORRECT. (i)'s consequence is RELAY-CHAIN (a), now landed as RESULTS R72 (I re-read it at trunk), so the condition is met.
  Wording: N-ROOT-3 ("ROUTE event" in (ii) and in the consequence line), N-ROOT-4 (the quantifier of (B)).
### P-N5-ROOT-add
- GATE-SHIFT (a): z's honest play and W-play agree up to u (Odd vertices before u are outside D_t), then continue with σ̄_t(u)'s and τ(u)'s
  plays, both inside A_t, both avoiding π and u, both ending on c's cycle; so M_t(z) and MW_t(z) differ exactly by Δ_t(u); Δ_t(u) ≥ 0 by
  κ-Y-FORM_D (τ(u) ∈ Y^u_t; minimum at σ̄_t(u); κ compares M first). CORRECT (u ≠ c because c lies on σ̄_t(u)'s play, which avoids D_t).
- GATE-SHIFT (b): Case 1 via XW, WM-G and the reward argument; Case 2 via (F1) on σ″ = σ_t[z ↦ x] and (V1) (x's play avoids z). CORRECT.
  Note that (b) needs no F_D hypothesis on z: the W-frame step is exact and the honest frame lags by the gate's offset.
- FREEZE-G (a): induction with G′[E_{t+1}] ⊆ G′[E_t] (a vertex keeps its role: A_t ∩ R_u(t) = ∅ and both sets are non-increasing). The four
  vertex kinds: A (FREEZE-A's step), u (its τ-edge into A), Odd R_u (τ-edge, N non-decreasing on R_u by WM-G), Even R_u (Case 1 through
  N = M + off with off(σ_t z) = Δ ≥ off(x); Case 2 avoiding: GATE-SHIFT (b)'s argument; Case 2 passing: a positive-weight cycle would give
  W_{t+1}(z) a cycle node other than c, so wt(z) + wt(q) ≤ 0). CORRECT.
- FREEZE-G (b), (c): the W-play of z ∈ E_t is a simple G′[E_t]-path to c, so N ≤ MoptG′; paths have ≤ L edges; sandwich; M = N − off with off
  constant per vertex on the interval. (c) as FREEZE-A (c), with q's honest play not returning to q because y's play, inside A_t or through
  π_y, u and A_t, avoids D_t ∋ q and q ≠ u. CORRECT.
- RELAY-PIECE (i): after FREEZE-A's freeze, M(τ u) is frozen and M(σ̄ u) takes values among the frozen M(y), y ∈ succ(u) ∩ A; M(u) =
  wt(u) + M(σ̄ u) is non-decreasing, so Δ is non-increasing and constant on blocks: ≤ deg(u) G-intervals. (ii) sums FREEZE-G (c) per block.
  CORRECT.

## 2. The Lead's question: can FREEZE-G (b), (c) and RELAY-PIECE be made to bite?
- In natural games (my library runs, as in the lane's): NO G-interval runs past its freeze index s + |E_s| − 1 (0 of 9,902 G-intervals on lib41
  × 3 starts, 0 of 9,048 on my 𝒞^1O files, 0 in lib2o, the named instances and the random sets). The addendum's §5 vacuity claim for FREEZE-G
  (b), (c) is CONFIRMED on natural data. RELAY-PIECE does run past FREEZE-A's freeze index s + |A_s| − 1 there (45 runs on lib41, 138 on the
  𝒞^1O files, 3 on lib2o; 0 failures), but its gap Δ NEVER changes after that index, so only its one-value / one-interval case is exercised.
- Constructed games: disjoint unions. A G-interval needs a long fallback-free S4a run inside one phase while a small class keeps its gate. A
  phase of a disjoint union is a phase of every component at once, so I take a DRIVER with a long S4a run (x32_rand64: a 55-step run at S3,
  x32_rand48: 44, xsnf52_n64: 52; found by my s4a_runs.py over lib41) and add one small random component with Odd choices and a random start;
  only the small component's classes are checked (COMP_MIN). 12,000 unions (4 searches × 3,000; logs union_*.txt, union2_*.txt):
  - 25,497 G-intervals run past their freeze index; FREEZE-G (b)'s constancy holds in all of them (77,887,938 constancy checks), FREEZE-G (c)
    in 2,431,531 checks, RELAY-PIECE (i), (ii) past FREEZE-A's index in 26,616 runs; 0 violations.
  - BUT these are mostly STATIC: the small class has already converged when the interval starts. Only 24 of the 25,497 intervals contain an
    Even switch inside the class, and only 5 contain a change of N (the W-frame path weight) inside the interval before the freeze — the
    substantive case "the class moves, then freezes by s + L and stays frozen". All 5 pass. Instances saved: docs/referee-2/R2-N5-ROOT/union/
    (21 games; u7101_1900, u7201_1948 and u7202_374 hold the 5 intervals with N changing; .pg + .start, reproduce with `COMP_MIN=64 python3 root_check.py start union/u7101_1900.pg
    union/u7101_1900.start`).
  - The control that TIGHTENS (b)'s freeze index ("constancy from s + L − 1", early) does not bite on any of the 21 saved union instances, which hold every
    interval with an in-class switch and all 5 with N moving (logs/mut_early_unions.txt), nor on lib41 (0 failures): the class always converges well before the |E_s| − 1 bound. (FREEZE-G (a)'s edge budget IS tight: "one more edge", fg1, fails 20
    times on lib41 and 8 times on 1,500 unions — that is (a), which is well exercised, not (b).) And Δ never changes after FREEZE-A's
    index in any union either, so RELAY-PIECE (i)'s multi-value case and (ii)'s multi-interval sum are never exercised.
- Answer: FREEZE-G (b), (c) are made to bite only weakly (5 substantive intervals, in constructed union games); their L-bound is never tight;
  RELAY-PIECE's multi-interval content is never exercised. These rest on PROOF ALONE, which I have checked line by line (§1). FREEZE-G (a)
  and GATE-SHIFT (a), (b) are well exercised in natural data (§4), and their controls bite.

## 3. Notes (no gap)
- N-ROOT-1 (FREEZE-A (c), q = c). The statement allows q = c (Odd cycle node); the proof's first branch uses (Aκ), stated for z ∈ U_c ∖ {c}.
  For q = c: σ̄_t(c) ∈ A_t forces c ∉ D_t (c's honest play would return to c ∈ D_t), M(c) = 0, and τ(c) is c's successor on its cycle with
  M = 0 (every other vertex of the cycle has rank < rank(c)), so 0 ∈ V_q. One sentence, or exclude q = c (as FREEZE-G (c) does).
- N-ROOT-2 (R-LEN wording). "On [s + L, e], Ξ on A_t changes only in its length" does not cover q ∈ D_t (not in A_t), but the count
  deg(q)(|U| − 1) − 1 follows directly: M(q) ∈ V_q (≤ deg(q) values), and for each value the length is monotone in [1, |U| − 1].
- N-ROOT-3 (DL-SPLIT (ii) and its consequence). "(ii) u has a ROUTE event" is defined by its parenthetical as a change of some class exit path or
  exit of u's options; P-N5-FLIP §3's ROUTE is a kind of ρ EVENT, and u need not have a ρ event at t → t+1 (a tie). So (ii) is a "route change at
  u", and the consequence line's "transitions carrying a ROUTE / CYC / TOG event" should read "… or a route change at a D-leaving vertex".
- N-ROOT-4 (DL-SPLIT's quantifier). "(A) some entering vertex z … or (B) z is unsplit" — (B) has no binder; the proof shows the stronger
  "every entering z has (A) or (B)", which is what the data check (DLS_A + DLS_B = DLS_entering in every set).
- N-ROOT-5 (premise forms). BF-F_D, GATE-SHIFT (b), FREEZE-A / FREEZE-G use (F1) on S4a's arena, i.e. the standing premise 1E-N3 in form P2
  (S1 returns the arena optimum), and WM-G (R62 (d)) which rests on the same; FREEZE-A (c), GATE-SHIFT (a) and DL-SPLIT use κ-Y-FORM_D (P1).
  The packets say "1E-N3" globally; naming P1 / P2 per item (as P-N5-FLIP does) would help the landing.
- N-ROOT-6 (DATA, DL-SPLIT's case (iii)). (iii) (TOG or TIE) holds at 579 clean D-leaves in my data, but never alone: always together with (i) or
  (ii) (DLS_case_iii_only = 0). This agrees with the packet's "case (iii) never occurred" read as "never the only case".
- N-ROOT-7 (DATA, vacuity). FREEZE-G (b), (c) and RELAY-PIECE's multi-interval content are untested on natural games and only weakly tested on
  constructed unions (§2). The landing text should carry "rests on proof alone" for them.

## 4. Data (DATA, not proof; logs in docs/referee-2/R2-N5-ROOT/logs/, reproduce with run_all.sh, run_union.sh, run_union2.sh)
| set | runs | states | BF-F_D | GATE-SHIFT (a) / (b) | FREEZE-A pieces (beyond s + L; UNK) | FREEZE-A (a) checks | A-gains (entering: A / B; clean A: i / ii / iii) | G-intervals (beyond; UNK) | FREEZE-G (a) checks | RELAY-PIECE beyond FREEZE-A's index |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nep90_n40, nep76_n40, frz40 (lane starts), long121_n40 (its start) | 4 | 398 | 27,821 | 2,419 / 4,054 | 452 (23; 223) | 10,564 | 47 (169 / 21; 40 / 125 / 3) | 544 (0; 382) | 9,847 | 0 |
| lib2o minus referee games × 5 starts | 205 | 1,395 | 35,193 | 4,776 / 5,598 | 1,759 (31; 193) | 59,731 | 35 (319 / 7; 6 / 317 / 2) | 871 (0; 104) | 46,390 | 3 |
| lib41 minus referee games × 3 starts | 1,230 | 19,460 | 922,585 | 89,736 / 169,309 | 25,737 (869; 7,350) | 631,681 | 530 (6,295 / 224; 556 / 5,552 / 423) | 9,902 (0; 5,024) | 280,283 | 45 |
| my 503 𝒞^1O files × 2 starts | 1,006 | 17,807 | 869,853 | 107,009 / 201,611 | 22,399 (1,320; 6,954) | 555,846 | 529 (5,696 / 265; 0 / 5,228 / 97) | 9,048 (0; 5,255) | 156,188 | 138 |
| random 2 / 4 / all-Odd-choice games (3,000 + 2,000 + 1,500 games × 3 starts) | 19,500 | 50,101 | 16,988 | 11,300 / 154 | 76,887 (164; 0) | 360,020 | 152 (448 / 35; 22 / 177 / 39) | 7,142 (0; 0) | 62,492 | 0 |
| unions: driver x32_rand64 / x32_rand48 / xsnf52_n64 + one small random component (small classes only; 4 × 3,000) | 12,000 | 645,611 | 3,672,278 | 68,302 / 20,445 | 1,062,454 (883,585; 0) | 167,376,065 | 73 (208 / 27; 3 / 102 / 15) | 38,527 (25,497; 0) | 8,052,999 | 26,616 |
0 violations of every check in every set. Reproductions of the lane's figures (packet §6, addendum §5) at the same starts: BF-F_D 7,827 on nep90
and 8,701 on nep76; GATE-SHIFT (a) 684 / 404 and (b) 943 / 661 on nep90 / nep76 — all equal to the lane's counts; nep90's phase@4 has 15 A-gains,
all D-leaves (the lane's 15). Every entering vertex of every A-gain is (A) or (B) (DLS_A + DLS_B = DLS_entering), and every clean (A) has (i), (ii)
or (iii).
Controls (lib41, 1 start, unless stated): gs0 (GATE-SHIFT (b) with Δ := 0) 9,469 failures (and 204 on nep90; the lane's 188); fa1 (FREEZE-A (a)
with one more edge) 81 failures; fg1 (FREEZE-G (a) with one more edge) 20 failures on the library and 8 on 1,500 unions (x32_rand48 + k 4);
early (FREEZE-G (b)'s constancy from s + L − 1) 0 failures on the library and 0 on the 21 saved union instances (N-ROOT-7).
UNK: FREEZE-A pieces and G-intervals whose path enumeration went over budget (2·10⁵ paths; 10⁵ in the unions) are skipped and counted above;
they are the large classes of the n = 40-64 library games.

## 5. Signatures
P-N5-ROOT: Lemma BF-F_D, Theorem FREEZE-A (a)-(c), (R-LEN), Corollary ROOT-PIECE (a reduction in G_c), Lemma DL-SPLIT (its RELAY-CHAIN
condition met by RESULTS R72): SIGN. P-N5-ROOT-add: Lemma GATE-SHIFT (a), (b), Theorem FREEZE-G (a)-(c), Corollary RELAY-PIECE (i), (ii): SIGN.
All on every game, inside one phase, under the standing SPEC premise 1E-N3 (P1 and P2, N-ROOT-5). No gap; notes N-ROOT-1..7. FREEZE-G (b), (c)
and RELAY-PIECE's multi-interval content rest on proof alone: vacuous on natural data, only weakly exercised on constructed unions (§2).
REFEREE-2 successor 17 (Opus 5.5, D15).
