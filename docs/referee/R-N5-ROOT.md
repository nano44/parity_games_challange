# R-N5-ROOT: REFEREE report on packet P-N5-ROOT-box20 (BF-F_D, FREEZE-A, ROOT-PIECE, DL-SPLIT) and its addendum P-N5-ROOT-add-box20 (GATE-SHIFT, FREEZE-G, RELAY-PIECE); every game, inside one phase
Referee: REFEREE (successor 15), Opus 5.5 (owner ruling D15). FIRST referee (Lead brief 16:41Z by date -u). REFEREE-2 reviews ROOT independently after EPC.
- Objects and pins:
  - docs/si/P-N5-ROOT-box20.md, sha1 d3788bc0ce0e3da2d54298c58e227e437242419a, 164 lines: on my tree, at the l-si freeze ced5cf27 and at
    trunk 539b4192 (an ancestor of HEAD): match.
  - docs/si/P-N5-ROOT-add-box20.md, sha1 af1c7ad4581cce4a9830b4ed01e2370d26ef850b, 156 lines: on my tree, at l-si 829003b2 and at the pin
    trunk 539b4192: match. Author of both: L-SI successor 16.
- Written 2026-10-26T16:42Z-17:10Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/ file on ROOT on my tree, on trunk or on origin/claude/referee-2 at any of my fetches (re-listed
  in the same turns; 0 / 0 / 0 ROOT files at 17:10Z, the FLIP log below excluded; the one name matching "root" there is docs/referee-2/R2-N5-FLIP/logs/mut_root_ppK12.txt, an old FLIP log, not
  opened). No lane code run (experiments/si/root/*.py, experiments/si/rund/quotecheck.py neither executed nor imported; start files read as
  data). D1.
- Premises read against their text: RESULTS R55 setting (D_k, u(v), R_D, F_D, π_v; l. 2786-2787), R55 (a) G_D (a), R54 / R55 game-general
  readings of R17 (a)-(c), R18, R21 (a) XW (l. 2792-2794), R17 (a) (F1)/(F2) and (V1), R21 (a) XW, R56 setting and (a) (Aκ), (A0κ), (M1κ), (M2κ),
  (INJ), R56 (d) κ-Y-FORM_D, R61 (e) ALT (CLEAN), R62 setting and (d) WM-G (premise: S1 returns the arena optimum), R63 setting (SPLIT /
  UNSPLIT) and (a) R-STICK_D, R38 (a); P-N5-FLIP §1 additivity (signed as a proof step); P-N5-CHOSEN RELAY-CHAIN (a) (signed by both referees,
  §Cs at d08011be and REFEREE-2's).
- Quotes: all [Q path@commit:lines] tags of both packets PASS my lane's own checker (scratch/flip_quotes.py): ROOT 9 of 9, addendum 11 of 11.
- Tool: scratch/root_probe.py (own engine rl_engine; W from the (σ, τ)-play; exact best path weights in G[A_t] and G′[E_t] by simple-path
  enumeration with a budget; checks in §5), scratch/frg_climb.py (hill climb for a G-interval past its freeze window). Logs scratch/root_logs/.

## Verdicts (sign-off line per item)
| packet § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| ROOT §2 | Lemma BF-F_D | SIGNED |
| ROOT §3 | Theorem FREEZE-A (a), (b), (c) | SIGNED (note ROOT-N1 on (c) at q = c) |
| ROOT §3 | (R-LEN) | SIGNED (note ROOT-N4: the count follows from the chain of distinct (M, length) pairs; the A_t sentence is not what q needs) |
| ROOT §4 | Corollary ROOT-PIECE | SIGNED, as a REDUCTION (G_c and f unbounded here, as the packet says) |
| ROOT §5 | Lemma DL-SPLIT: split (A) / (B) | SIGNED (note ROOT-N3, wording of (B)) |
| ROOT §5 | DL-SPLIT case (A), clean: (i) or (ii) or (iii) | SIGNED; (i)'s "carries a ROUTE, CYC or TOG event" rests on RELAY-CHAIN (a), now signed by both referees (P-N5-CHOSEN §Cs), not yet landed |
| ROOT §5 | the Consequence (G_c decomposition) | SIGNED as a decomposition (not a bound) |
| add §2 | Lemma GATE-SHIFT (a), (b) | SIGNED |
| add §3 | Theorem FREEZE-G (a) | SIGNED (exercised in data) |
| add §3 | Theorem FREEZE-G (b) | SIGNED; its first sentence (N_t ≤ MoptG′[E_t] at every t) exercised; its freeze sentence rests on PROOF ALONE (vacuous in all data and searches, §5) (note ADD-N1 on the base case) |
| add §3 | Theorem FREEZE-G (c) | SIGNED on PROOF ALONE (vacuous in all data and searches; its inner step checked at every state, §5) |
| add §4 | Corollary RELAY-PIECE (i), (ii) | SIGNED; exercised in 6 library runs only (§5) |
| §6 / §5-§6 | maps, READINGs, data | not signed (as briefed) |
No gap. Notes ROOT-N1..N5, ADD-N1..N2. Inside one phase; ROOT-PIECE and RELAY-PIECE are reductions (G_c, f and the number of G-intervals are
not bounded); nothing here bounds ρ, N_ep, f or N5's running time; not a TARGET.md claim; G-N5-TIME stays OPEN.

## 1. ROOT §2-§4, re-derived (parentheticals checked one by one)
- §1 setting ✓. Every in-phase transition is S4a or an Even S4c fallback ✓ (FIX 3). The (F1) step on S4a's arena H_t needs σ_{t+1} to be
  Even's arena optimum against τ: the standing premise 1E-N3 in its P2 form (R62's WM-G premise; P-N5-FLIP §1 names P1 / P2) — the packet says
  "with the standing premise 1E-N3" without naming P2 (ROOT-N2, citation).
- BF-F_D ✓. Case 1 (Aκ), (M2κ) ✓. Case 2: both values have cycle node c, M decides (M1κ), so (v, x) ∈ Iσ_t and σ″ ∈ H_t ✓; (F1) ✓; v ∈ F_D(t+1) ⇒
  W_{t+1}(v) = Ξ_{t+1}(v), cycle node c (G_D (a)) ✓.
  - (i) ✓: x's play avoids v, so it is x's σ″-play and W_{σ″}(v) = v ⊕ W_t(x) (V1) ✓; a cycle node u ≠ c for W_t(x) would have reward > reward(c)
    (W_t(x) ⊵ Ξ_t(x), XW) and pass to W_{σ″}(v) and W_{t+1}(v) ✓; "v ∉ P(W_t x) (that set lies on x's play)" ✓; (M1κ) ✓.
  - (ii) ✓: v ∈ F_D(t) makes v's (σ_t, τ)-play honest with W = Ξ ✓; a vertex of q on v's play repeats on x's play, hence lies on the cycle,
    where wt = 0 ✓; Case 2 gives wt(q ∪ {v}) > 0 ✓; Z = v → x → q → v under σ″ (only v's edge changes) ✓; the largest-rank vertex of Z above c
    dominates the signed sum, so it is even and the top of Z, with reward > reward(c) ✓ (for c odd, any even reward exceeds it); (F1)
    contradiction ✓. The remark "(i) does not use v ∈ F_D(t); (ii) does" ✓; F_D(t+1) is needed in both (my MUT=3 drops it: 48 failures).
- FREEZE-A ✓.
  - (a) induction ✓: G[A_{t+1}] ⊆ G[A_t] "(A_{t+1} ⊆ A_t; Even edges into A_{t+1} are edges into A_t; Odd vertices keep their τ-edge, τ constant
    on the phase)" ✓; Even z ∈ A_{t+1} ⊆ A_t is in F_D(t) ∩ F_D(t+1), BF-F_D ✓; Odd z ∈ F_D(t+1) is not in D_{t+1}, so σ̄_{t+1}(z) = τ(z) = x ✓.
  - (b) ✓: z's (σ_t, τ)-play avoids D_t, so it is its honest play; every vertex on it is in F_D(t) ∩ U = A_t ✓; its prefix to c is a simple
    G[A_t]-path ✓; ≤ |A_t| − 1 ≤ L edges ✓; the sandwich for t ≤ t′ ✓.
  - (c) ✓: q ∉ D_t ⇒ q ∈ A_t ⊆ A_{s+L}, M_t(q) = M_{s+L}(q), and τ(q) ∈ A_{s+L} gives M_{s+L}(q) = wt(q) + M_{s+L}(τ q) ✓ — by (Aκ) for q ≠ c; for
    q = c (an Odd cycle node) both sides are 0, τ(c) lying on c's cycle, so the conclusion holds but (Aκ) is not what gives it (ROOT-N1).
    q ∈ D_t ⇒ q on no honest cycle, q ≠ c "(c lies on y*'s play, so c ∉ D_t)" ✓; membership M_t(q) = wt(q) + M_t(y*) ∈ V_q ✓ (the minimum
    over Y^q_t is more than membership needs). Monotone ⇒ ≤ deg(q) − 1 changes ✓.
  - (R-LEN) ✓ in its count: at the counted states (M_t(q) ∈ V_q, lengths in [1, |U| − 1] for q ≠ c), Ξ_t(q) runs through a chain of distinct
    values ordered by (M, s_c·ℓ), so ≤ deg(q)(|U| − 1) values and ≤ deg(q)(|U| − 1) − 1 changes. Its first sentence speaks of A_t, which q
    (possibly in D_t) need not belong to (ROOT-N4, wording).
- ROOT-PIECE ✓. Cutting at fallbacks and A-gains leaves ≤ f + G_c + 1 pieces satisfying FREEZE-A's hypothesis; L ≤ |U| − 1; arithmetic ✓
  (the Ξ-bound is even a little loose: (f + G_c + 1)((|U| − 1)(deg q + 1) − 1) + f + G_c suffices).

## 2. DL-SPLIT, re-derived
- Split ✓. z ∈ A_{t+1} ∖ A_t lies in U ∖ A_t = R_D(t) ∩ U with first D_t-vertex u. u ∉ D_{t+1}: a D-leave, σ̄_{t+1}(u) = τ(u) ≠ σ̄_t(u) ✓. Else z ∉
  R_D(t+1); R-STICK_D (RESULTS R63 (a): a split v ∈ R_D(s) stays in R_D(s+1) at an in-phase S4a transition) makes z unsplit at t ✓ (SPLIT /
  UNSPLIT as R63's setting: λ_W vs λ); z's (σ_t, τ)-route up to u reaches u ∈ D_{t+1}, Odd vertices on it follow τ (constant), so if no Even
  vertex on it switched, z would still reach u at t + 1: some Even vertex of the route switched ✓. The packet's "since τ and σ̄(u) are unchanged"
  should read "since τ is unchanged" (σ̄(u) plays no part in a (σ, τ)-route; ROOT-N3).
- Case (A), clean ✓. With ¬(i), ¬(ii) and no TOG at e1: y1's class exit path and exit are the same at t + 1 (¬(ii)), the path avoids u (u on no
  honest cycle at t, y1 = σ̄_t(u)), e1's play at t + 1 avoids u (no TOG; for e1 = c, c's cycle, u on no honest cycle at t + 1), so y1 ∈ Y^u_{t+1}
  and κ_{t+1}(y1) = κ_t(y1) (additivity; κ(e1) unchanged by ¬(i); κ(c) constant) ✓. κ-Y-FORM_D at t + 1 with the minimum at y2 = σ̄_{t+1}(u) ✓;
  κ non-decreasing ✓; y2 ∈ Y^u_t (clean) and the minimum at t at y1 ✓: a TIE ✓. (i)'s "carries a ROUTE, CYC or TOG event" is RELAY-CHAIN (a)
  applied to e1's ρ event, word for word ✓ (P-N5-CHOSEN, signed by both referees; RESULTS entry pending).

## 3. Addendum: GATE-SHIFT, FREEZE-G, RELAY-PIECE, re-derived
- GATE-SHIFT (a) ✓. π's Odd vertices are outside D_t, so σ̄_t = τ there ✓; both continuations (σ̄_t(u)'s and τ(u)'s plays) lie in A_t (u ∈ DD_t)
  ✓, avoid D_t ∋ u ✓, and are disjoint from π (π ⊆ R_D(t), the continuations ⊆ F_D(t)) ✓; W = Ξ on τ(u)'s play (G_D (a)) ✓; path weights add over
  distinct vertices ✓; Δ_t(u) ≥ 0 by κ-Y-FORM_D at the D-vertex u (u ∈ Q ∩ U, u ≠ c, on no honest cycle; τ(u) ∈ Y^u_t; κ compares M first) ✓.
- GATE-SHIFT (b) ✓. Case 1: XW, then WM-G on the S4a transition (premise as R62) ✓; W_{t+1}(z) has cycle node c by (a) at t + 1 ✓, which pins
  W_t(z)'s cycle node ✓. Case 2 as BF-F_D (i) ✓ (the hypothesis that x's (σ_t, τ)-play avoids z replaces F_D(t)). The control with Δ := 0 in
  the M-form fails (181 times), so the offset term is needed.
- FREEZE-G ✓.
  - Facts ✓: on R_u(t), M = N − Δ (GATE-SHIFT (a)); on A_t, N = M (G_D (a)); N_t(z) = wt(z) + N_t(next) along the W-play, next ∈ R_u(t) or = u ✓;
    N non-decreasing on R_u (WM-G, cycle node c at both ends) and on A ((M2κ)) ✓.
  - (a) induction ✓ in all four cases. G′[E_{t+1}] ⊆ G′[E_t] "(A and R_u non-increasing; the edge rule depends only on membership)" ✓ (A_t ∩
    R_u(t) = ∅). Even z ∈ R_u(t+1): σ_t(z) ∈ R_u(t) (the next vertex of z's W-play, or u itself) ✓; Case 1 uses off_t(σ_t z) = Δ ≥ off_t(x) ✓;
    Case 2, x's play passing z: N_t(x) = wt(q) + N_t(z) (a vertex of q on z's W-play lies on its cycle, wt 0) ✓, and wt(Z) > 0 would give
    W_{σ″}(z) a cycle node above c, against W_{t+1}(z)'s cycle node c (GATE-SHIFT (a) at t + 1) ✓. The base N_t(c) = 0 needs c ∉ R_u(t): true,
    since σ̄_t(u)'s honest play lies in A_t and reaches c's cycle, so c ∈ F_D(t) (ADD-N1: one sentence).
  - (b) ✓: z's W-play to c is a simple G′[E_t]-path ✓; ≤ |E_t| − 1 ≤ L edges ✓; sandwich ✓; off constant on the interval ✓.
  - (c) ✓: q ∉ D_t ⇒ q ∈ A_t (y ∈ A_t) or q ∈ R_u(t) (y ∈ R_u(t)), so q ∈ E_t ⊆ E_{s+L}, and q ∉ D_{s+L} ✓; q ∈ D_t ⇒ y's honest play does not
    return to q (π_y has no D_t-vertex, σ̄_t(u)'s play avoids D_t) ✓, (Aκ) ✓.
- RELAY-PIECE ✓. (i): FREEZE-A (b) pins M(τ u) and the values M(σ̄_t u) after s + L_A (L_A = FREEZE-A's L, A_s ∋ τ(u) non-empty) ✓; M(u) =
  wt(u) + M(σ̄ u) non-decreasing (u ≠ c) ⇒ Δ non-increasing ✓; blocks of constant Δ are G-intervals ✓ (the other conditions hold on all of
  [s, e]). (ii): per G-interval ≤ (|U| − 1) + (deg(q) − 1), plus ≤ deg(u) − 1 boundaries; arithmetic ✓. The wording "(consecutive ones sharing a
  transition at which Δ changes)" means the Δ-changing transition lies between two blocks, in neither (ADD-N2).

## 4. Vacuity (the Lead's request)
FREEZE-G (b)'s freeze sentence and (c) apply only to a G-interval with e − s ≥ |E_s| − 1 + 1; RELAY-PIECE needs s + L_A < e. In data:
- No G-interval outlives its freeze window: max (e − s) − (|E_s| − 1) = −3 on the library (n ≤ 24, 1,899 G-intervals), −2 on 3,000 random games
  (392), −21 / −29 on nep90 / nep76 (107 / 94). My hill climb (scratch/frg_climb.py, fitness = that excess, every root_probe check run on every
  candidate) over n = 5-10, two seeds, 100,000 candidates each, reached −1 and never 0. So FREEZE-G (b)'s freeze and (c) are NOT exercised:
  they rest on PROOF ALONE. A disjoint union with a static gadget class would make them formally non-vacuous, but tests nothing (the class
  would not move), so I did not count that.
- What IS exercised, non-vacuously: FREEZE-G (a) (47,498 checks in the library batch) and (b)'s first sentence N_t ≤ MoptG′[E_t] at every
  state (47,498); FREEZE-G (c)'s inner step at every state of every G-interval (FRGC: 4,123); FREEZE-A's frozen regime (378 library pieces past
  s + L, 1,007 checks of FREEZE-A (c)); RELAY-PIECE (i) on the 6 library runs (of 1,706) where s + L_A < e, and (ii) on their 13 (run, q) pairs (max 5 changes).

## 5. Data (own engine; DATA, not proof; 0 failures of every signed check)
Checks as in scratch/root_probe.py's header: BFF, FRA (a), (b) at every state and after the freeze, (c), RPC, DLS (split and the clean case),
GSA, GSB, FRG (a), (b) at every state and after the freeze, FRGC (FREEZE-G (c)'s inner step at every state), FRG (c), RLP (i), (ii).
| sample | runs | phases | BF-F_D | FREEZE-A (a) / (b) (pieces; past s + L) / (c) | ROOT-PIECE (q, phase) | DL-SPLIT entering z: (A) / (B); clean (A): (i) / (ii) / tie / TOG | GATE-SHIFT (a) / (b) | FREEZE-G (a) = (b) checks (G-intervals) / FRGC; max excess | RELAY-PIECE runs (non-vacuous) | UNK (FRA / FRG) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| scratch/fbc_lib.txt, n ≤ 24 (592 files), S3 + 4 random | 2,960 | 12,115 | 316,395 | 142,861 (3,463; 378) / 1,007 | 7,937 | 2,708 / 156; 252 / 1,980 / 237 / 221 | 13,268 / 21,868 | 47,498 (1,899) / 4,123; −3 | 1,706 (6) | 165 / 111 |
| random 3,000 games (n 5-14, ≤ 6 Odd choice vertices, seed 451), S3 + 6 random | 21,000 | 56,704 | 45,208 | 73,487 (6,013; 164) / 407 | 12,945 | 311 / 44; 22 / 139 / 24 / 9 | 818 / 233 | 4,695 (392) / 1,464; −2 | 386 (0) | 0 / 0 |
| nep90_n40 at its start | 1 | 5 | 7,827 | 359 (23; 0) / 0 | 7 | 53 / 0; 5 / 49 / 0 / 0 | 684 / 943 | 997 (107) / 131; −21 | 61 (0) | 19 / 84 |
| nep76_n40 at its start, budget 3·10⁶ | 1 | 10 | 8,701 | 242 (16; 0) / 0 | 5 | 45 / 0; 6 / 39 / 0 / 0 | 404 / 661 | 383 (94) / 42; −29 | 57 (0) | 15 / 85 |
| FREEZE-G climbs (scratch/frg_climb.py, n 5-10, seeds 1 and 2, 100,000 candidates each, S3 + 6 random per candidate, every check) | — | — | — | — | — | — | — | best excess −1 | — | — |
- Lane figures reproduced exactly at the lane's start files: BF-F_D 7,827 / 8,701 checks on nep90 / nep76; GATE-SHIFT (a) 684 / 404 and (b) 943
  / 661 (packet ROOT §6 and addendum §5). (The lane's lib41 counts use other starts and are not comparable.)
- Mutations (each bites; n ≤ 20 library, S3 + 2 random, 1,413 runs): MUT=1 (one more edge in FREEZE-A (a) and FREEZE-G (a)): FRA (a) 136
  failures, FRG (a) 1; MUT=2 (GATE-SHIFT (b) in the M-form with Δ := 0): 181; MUT=3 (BF-F_D without v ∈ F_D(t + 1)): 48.
- DL-SPLIT's (iii) alternatives never stand alone: a 1,000-game random run (n 5-14, S3 + 6 random, 7,000 runs) counted 0 clean D-leaves
  with neither (i) nor (ii) (scratch/root_logs/rand_iii.txt).
## 6. Notes (none blocks a signature)
- ROOT-N1 (FREEZE-A (c), q = c). For an Odd cycle node q = c with σ̄_t(c) ∈ A_t, (Aκ) does not apply (it is stated for z ≠ c); the claim holds
  because τ(c) lies on c's cycle and both sides are 0. One sentence.
- ROOT-N2 (premise name). (F1) on S4a's arena (BF-F_D Case 2, GATE-SHIFT (b), FREEZE-G (a)) and WM-G use 1E-N3 in its P2 form (S1 returns the
  arena optimum); name P2 as P-N5-FLIP §1 does.
- ROOT-N3 (DL-SPLIT (B), wording). "since τ and σ̄(u) are unchanged" → "since τ is unchanged": the route is a (σ, τ)-play.
- ROOT-N4 ((R-LEN), wording). The count deg(q)(|U| − 1) − 1 follows from the chain of distinct (M, length) pairs of q at the counted states;
  the sentence about Ξ on A_t is true but is not the step q needs (q may lie in D_t).
- ROOT-N5 (data, DL-SPLIT). The (iii) alternatives occur (library n ≤ 24: 237 ties, 221 TOG steps at e1; non-exclusive counts), but never as
  the only case: in 7,000 random runs every clean D-leave also had (i) or (ii) (0 "(iii) only"). This agrees with the packet's "case (iii)
  never occurred" read as "never alone".
- ADD-N1 (FREEZE-G (a), base). N_t(c) = 0 needs c ∉ R_u(t); true (σ̄_t(u)'s play in A_t reaches c's cycle, so c ∈ F_D(t)); say so.
- ADD-N2 (RELAY-PIECE (i), wording). The G-intervals are disjoint blocks; the Δ-changing transition lies between two of them.

## §C. Comparison with REFEREE-2 (written 2026-10-26T18:58Z by date -u, after the Lead's word of 18:52Z; REFEREE-2's report
docs/referee-2/R2-N5-ROOT.md at origin/claude/referee-2 3febbfaf, read only after my predecessor's report 619fccf2 was pushed)
Written by REFEREE successor 16 as SUCCESSOR to the author of this report (successor 15): I re-read the report above, the two packets'
statements and REFEREE-2's report, and re-ran the checks named below with my own engine. Every verdict below is labelled (Opus 5.5, D15).
### Verdicts
| item | REFEREE (619fccf2) | REFEREE-2 (3febbfaf) | joint |
| --- | --- | --- | --- |
| ROOT §2 BF-F_D | SIGNED | SIGN | SIGNED |
| ROOT §3 FREEZE-A (a), (b), (c) | SIGNED (ROOT-N1, q = c) | SIGN (N-ROOT-1, q = c) | SIGNED |
| ROOT §3 (R-LEN) | SIGNED (ROOT-N4) | SIGN (N-ROOT-2) | SIGNED |
| ROOT §4 ROOT-PIECE | SIGNED as a REDUCTION | SIGN (a reduction in G_c) | SIGNED as a REDUCTION |
| ROOT §5 DL-SPLIT, split, clean case (A), Consequence | SIGNED; (i) rested on RELAY-CHAIN (a), "not yet landed" | SIGN; the condition is MET, RELAY-CHAIN landed as RESULTS R72 | SIGNED; condition MET (RESULTS R72 is on trunk, l. 3757, re-read) |
| add §2 GATE-SHIFT (a), (b) | SIGNED | SIGN | SIGNED |
| add §3 FREEZE-G (a), (b), (c) | SIGNED; (b)'s freeze and (c) on PROOF ALONE (vacuous in all data) | SIGN; vacuous on natural data, weakly exercised on constructed unions (5 intervals with N moving) | SIGNED; (b)'s freeze and (c) rest on PROOF ALONE on natural games; weakly exercised only on REFEREE-2's unions |
| add §4 RELAY-PIECE (i), (ii) | SIGNED; "exercised in 6 library runs" | SIGN; its multi-value / multi-interval content never exercised | SIGNED; only the one-value case is exercised (see Data) |
Verdicts identical. Joint gap map: EMPTY.
### Notes, matched
| REFEREE | REFEREE-2 | joint |
| --- | --- | --- |
| ROOT-N1 (FREEZE-A (c), q = c outside (Aκ)) | N-ROOT-1 (same) | same note |
| ROOT-N2 (name 1E-N3's P2 form for (F1) on S4a's arena and WM-G) | N-ROOT-5 (P2 there, and P1 for the κ-Y-FORM_D items: FREEZE-A (c), GATE-SHIFT (a), DL-SPLIT) | REFEREE-2's fuller form ACCEPTED |
| ROOT-N3 (DL-SPLIT (B): "since τ and σ̄(u) are unchanged" → "since τ is unchanged") | — | REFEREE's wording note |
| — | N-ROOT-3 ((ii) is a route change at u; FLIP's ROUTE is a ρ event; the Consequence says "ROUTE event") | ACCEPTED, as wording. I checked whether it hides a case: in clean case (A) with no TIE, u has a ρ event: κ_t(y1) < κ_t(y2) (minimum at y1, y2 ∈ Y^u_t, no tie) and κ_t(y2) ≤ κ_{t+1}(y2), so κ_{t+1}(u) > κ_t(u). With (ii) that IS a FLIP ROUTE event at u, so the Consequence's list holds in FLIP's sense too (with a tie, "a tie" covers it). Data agree: 1,663 "(ii) only" clean D-leaves, u's value changed at every one (scratch/rootc_probe.py, II_NORHO_U 0) |
| — | N-ROOT-4 ((B) has no binder; the proof gives "every entering z is (A) or (B)") | ACCEPTED (my predecessor's probe classifies every entering z, DLS_A + DLS_B = DLS_chk) |
| ROOT-N4 ((R-LEN) wording) | N-ROOT-2 | same note |
| ROOT-N5 ((iii) never alone in data) | N-ROOT-6 (same, 579 cases) | same finding |
| ADD-N1 (FREEZE-G (a) base: c ∉ R_u(t)) | — (its §1 notes u ≠ c for GATE-SHIFT (a), the same fact) | REFEREE's note |
| ADD-N2 (RELAY-PIECE (i): the G-intervals are disjoint blocks) | — | REFEREE's wording note |
| §4 vacuity: FREEZE-G (b) freeze, (c) on proof alone | N-ROOT-7 (same, plus the union games) | same; the landing text should carry "rests on proof alone" for FREEZE-G (b)'s freeze sentence, (c) and RELAY-PIECE's multi-value content |
### Data
- Both own engines, 0 failures; both reproduce the lane's BF-F_D 7,827 / 8,701 and GATE-SHIFT (a) 684 / 404, (b) 943 / 661 on nep90 / nep76.
- Correction to my predecessor's §4: RELAY-PIECE "exercised in 6 library runs" means only that s + L_A < e there. In those 6 runs Δ(u) never
  changes after s + L_A (my scratch/rootc_probe.py: RLP_nonvac 6, RLP_DCHG 0, on the same 2,960 runs). So (i)'s multi-value case and (ii)'s
  multi-interval sum are not exercised in my data either, as REFEREE-2 found.
- REFEREE-2's constructed unions, re-run with my predecessor's engine (scratch/root_probe.py, unchanged). Games u7101_1900, u7201_1948 and
  u7202_374 (copied from 3febbfaf into scratch/rootc_inputs/), each at its .start, BUDGET 10⁵. FREEZE-G: 6 intervals, 3 of them past their
  freeze window (max excess 45). FRG (c) 563 checks, FRGC 720, FREEZE-A pieces past s + L 3, RELAY-PIECE non-vacuous 3. 0 failures
  (scratch/rootc_logs/r2unions_root_probe.txt). So FREEZE-G (b)'s freeze sentence and (c) are formally exercised on those games under my
  engine too. I did not re-count REFEREE-2's "5 intervals with N moving".
No disagreement; nothing open between the referees on ROOT. The OFFMONO and OFFMONO-add §Cs follow on the Lead's word.
