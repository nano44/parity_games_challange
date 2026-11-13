# Consequence map of the kill candidate EXP-IDEAL (packet P-N5-EXP, L-RED-B 5, claude/l-red-b 350d84eb; UNREFEREED): what it settles, what stays true with its purpose ended, and the contradiction check (a READING for the Lead's landing; not a result; nothing here is in force before P-N5-EXP is signed and landed)
L-NEW successor 77 (session_01V5yGRaRvmT6aAyZLgMCHoW), D1 / D18 / D25. Lead 12:42Z and 13:49Z: «The CONSEQUENCE MAP … with line numbers: (a)
every OPEN statement, conjecture or route the kill settles …, each «FALSE by EXP-IDEAL», «moot» or «unaffected» with a one-line reason;
(b) landed results whose statement stays true but whose stated purpose ends; (c) anything landed that G_k would CONTRADICT»; Lead
14:00Z: «mark separately the statements that are settled only CONDITIONALLY on R117's standing premises ([1E-N3], [RULE], [VJ-LOC])
from those settled on the model alone».
How it was made: sections A-D are the reports of four reader sub-agents of this session (one each for RESULTS R17-R75, RESULTS
R76-R130, GAPS + NOW, the lane boxes 209-218), reproduced as returned; §0-§2 are my synthesis and my own checks. Line numbers:
docs/RESULTS.md and docs/GAPS.md at trunk 5d7aab0f (both byte-identical at 6eaf4604), docs/NOW.md at 6eaf4604, lane documents at
l-new aa29064d. Every verdict assumes EXP-IDEAL survives its referees. Verdict words: FALSE by EXP-IDEAL / moot (not decided; its
only purpose was a polynomial bound for N5) / unaffected. Reader inferences marked «(inference)» or «Note» were not checked by me.

## 0. Synthesis
**EXP-IDEAL** (statement about R104's IDEAL model, no premise): G_k, k ≥ 3, Ξ-acyclic, degree 2, N = 9k − 16, L(G_k) = 2^k − 2.
My replay (experiments/new/box217/out/key1p_gk.out, gk_total.out): T_key = 2^k − 2 for k = 3..14, ideq 0 against R104's reference
simulator, largest sw 2^(k−2), enumeration depth k(G_k) = 1 (the family index k is NOT the enumeration depth of P-N5-KEY1P), all
packet counters 0; N5 itself on Γ3(G_k), k = 3..9: exactly T_key + 3 = 2^k + 1 iterations, one fallback at transition 2^k − 1.
**(a1) Settled ON THE MODEL ALONE (FALSE by EXP-IDEAL, no premise):** IDEAL-ACYC-POLY (R117 §8) = O1 = QUIET-KEY-1P and SW-POLY
(P-N5-KEY1P §3, §9, through its Lemma IDEAL-1P, or read directly as IDEAL statements); «U polynomial» and «KF polynomial» (R105 U-EQ,
KEYFLIP; RESULTS l. 10155; GAPS l. 11 UPDATE 2026-11-04 02:59Z); «M₂ polynomial», XF (UPDATE 11-04 13:41Z); «max R(x, k) polynomial»
(RISE-EQUIV, UPDATE 11-06 21:57Z); JOINT-POLY at degree ≤ 2 on Ξ-acyclic genomes (box 216 l. 162-165, as an IDEAL statement);
box 217's A6 «⇐» and «a super-polynomial family = k(G) ≥ c·d^ε» (l. 99-105; the converse of ENUM-NEC at c = 1: k(G_k) = 1); the
question «whether long IDEAL-ACYC runs exist» (GAPS UPDATE 11-07 10:30Z): they do. CONJECTURE LIN-2 (T ≤ 2N; UPDATE 11-04 13:41Z)
if its scope is degree-≤-2 IDEAL-ACYC (scope not restated in the row).
**(a2) Settled ONLY UNDER R117's STANDING PREMISES** ([1E-N3] = R57 (b), [RULE] = R24 (a), (b) with R103's bridge B, [VJ-LOC] = R36 (c),
R15 (d); R124 adds none): G-N5-TIME (GAPS l. 11) for N5 as specified: FALSE, with the exact landed count R124 EXACT-L (RESULTS
l. 15371): N5 from S3 makes exactly L(G_k) + 3 = 2^k + 1 iterations on n = 135k − 230 vertices; O1′ / KEY-CYC (box 212 l. 35, 193);
QUIET-RF and QUIET-KEY (box 216 l. 112-116); FL-S3-POLY and «every FL run … at most p(n)» (R117, R104 REAL-IDEAL; UPDATEs 11-02
11:22Z, 11-07 10:30Z); FL-POLY and GCH (R103; UPDATE 11-02 00:24Z); WRUN-POLY with every member of WRUN-EQ, TIE-POLY, [P-INT]
(R95; UPDATE 10-30 22:14Z), max HXS_F (R97), TIE* (R93), N_F, T1_F, TS_F (R98-R100), SG, BG, INC (R101), FLATTR_P (R94), P* / NM*
(R86-R89), FL_S (R89); the conjunction «B*, REP*, SC*, O* all polynomial» of R90 CUT-RED (B* ≤ 1 and O* = 0 on Γ3(G_k), so REP* or
SC* is super-polynomial; which one: not determined); R27's «rises and ε polynomial per phase», R64's EP-k premise, R67's N_split
(readers' derivations from «the run is one phase, one epoch, one W-run»: to be checked by a referee); NOW l. 2: RUN-LIN′, SW-RUN,
«OPEN: general games»; NOW l. 11: gauntlet step 4 for N5.
**(a3) Moot, not refuted:** every fallback-count route (FB-LIN, N_ep, N_K, [P-WCHτ], R91 GAP-RED, R56 FB-RED; the run has one
fallback and W constant); CONJECTURE ρ-POLY (R56; a reader's sketch says FALSE, unrefereed: listed as «to referee», not as settled);
every 2-wide-ladder statement (FLIP-ADD, SLOT-TRADE, PAIR-LIN, DBL-O(1), RISE-2D, the tower questions, μ(d), T^R(d), L-SI's ODOMETER
programme, my box 218, CONJECTURE XTW-2, k ≤ d/2 on upward ladders): G_k is not in 𝓛^R_d; ENUM-LOG and the enumeration-depth
searches (NOW l. 23-27: «k 6 at N 41», «no k = 8», depth-8 search: these k are enumeration depths, and G_k has depth 1); RF-C, RF-D,
LOUD-RF, BOUND-TRANSFER as routes.
**(a4) Unaffected:** every Howard / IDEAL-CYC / N5′-xi statement (R118, R121-R123, R125-R130: Howard takes about 4 steps on G_k and
N5′-xi at most N + 1 to its first fallback); the subclass theorems R17-R53, R57, R58, R61 (𝒞^1O, 𝒞^1E, 𝒞^kO, one-player: Γ3(G_k) is
in none); A_DTL's gaps (GAPS l. 6-9); G-N1-LB; termination R15.
**(b) True, purpose ended:** RESULTS R17-R130 as «partial step-4 lemmas for N5» (NOW l. 11). Kept as tools of the kill itself:
R24 (a), (b), R36 (c), R57 (b) (premises of R104 / R117), R104 (model), R105 ENC, R117 REACH3, R124 EXACT-L; of P-N5-KEY1P: IDEAL-1P,
RED-1P, KILL-TRANSFER, Lemma 0, A1-A4, A2-POLY (the positive subclass), SW-POLY ⟺ QUIET-KEY-1P (both sides now false), ENUM-NEC.
**(c) Contradictions: NONE FOUND.** Three unconditional polynomial counts were examined and are consistent: R47 (joint λ-runs per
run: the family's run is inside one), R70 (W-honest and D = ∅ states: D ≠ ∅ at every state of the run), R75 (sub-events at
path-free vertices); and R130's bound for N5 on W-flat wrappers W(H, s0) (F ≤ m_E − n_E + 1) is on another family of games (one
W-level; Γ3(G_k) has k + 1). Ladder-only results do not apply (G_k has up to 9 movers on a level; my count at k = 8, 12). The any-degree
lemmas hold on G_k with counters 0 (§1).

## 1. My own checks (DATA; experiments/new/box217)
- Membership and replay: inst_gk/ (byte copies of G_3 … G_14, SOURCE.txt, SHA1SUMS); key1p.py: ideq, l0, a1mu, a1v, a2, a3, a4h, a4x
  all 0 for k = 3..14; mism, nofb 0 for k = 3..9; gk_total.py: exl, fbn, fbat 0 for k = 3..9 (out/SHA1SUMS_gk; check.sh block).
- Not a ladder: levels at k = 5 hold 2, 2, 4, 7, 8, 6 movers; widest level 9 at k = 8 and 12 (scratch count). So R110, R112, R113's
  ladder clauses, R119's (WINDOW-ONCE, DBL-EQ, PASS-FREEZE, FUEL-EXACT, TOWER-NEED) and R120 have no instance in G_k.
- A2-POLY is not contradicted: the largest min(lev, hΞ) over the movers of G_k is k at k = 5, 8, 12 (scratch count).
- R124 EXACT-L is the exact landed transfer: «N5 … from S3 on Γ3(G) makes exactly L(G) + 3 iterations» and «N5's iteration count is
  polynomial in n iff L(G) is polynomial in N + M» (RESULTS l. 15371; quoted from the title, checked by the Lead on 6eaf4604).

## 2. Corrections to my own records that the readers found
- Box 218 §0 item 2 (l. 22-23), «Upward ladders are exponential in d only if the ceiling is reached up to an additive constant»:
  NOT proved. UP-CEIL proves T_key < 2^(⌈d/2⌉ + 3) and k ≤ (d + 1)/2 only; a half-rate mover near the middle level is not excluded,
  and G_k shows that half-rate families exist (off the ladder). The sentence is withdrawn here; the box is a DROPPED record.
- Box 217 l. 105 («A super-polynomial family = an infinite family with k(G) ≥ c·d^ε») was never withdrawn in place: it is false by
  G_k as an equality (P-N5-KEY1P §9 has the correct sufficient form by SW-POLY). Box 213 l. 24-25 pairs the largest switch counts
  with the largest |K(x)| of other movers (two separate maxima): a wording slip, noted here.
- NOW l. 22-27 name «k» for enumeration depth; EXP-IDEAL's index k is a different parameter (reader table C flags this as «if»).

## A. RESULTS R17-R75 against EXP-IDEAL (reader sub-agent report, reproduced as returned; its «DONE / FINDINGS / NEEDS» lines are the reader's, not mine)
### R17-R75 against EXP-IDEAL (RESULTS.md copy of trunk 5d7aab0f; read-only)

All 59 titles read in full. Bodies opened only to fix scope (R25, R27, R38, R47, R56, R60, R64, R67, R69, R70, R75) and R104 (c)-(j), lines 9930-9961.
Outcome: no contradiction found. 3 CHECK entries (all resolved as consistent), 3 reductions now decided, 1 conjecture refuted (by an unrefereed sketch), everything else TRUE-KEPT.

Fact used throughout (R104 (c) K, (d) PLAY, (e) SBAR, (f) TAU, (h) W; R117 transports it to Γ3): on states 0..L(G) the cycle nodes of Ξ and τ are constant, σ̄ = β-face and τ = e-face at every gate, σ̄(K2) = K1 ≠ τ(K2), Iτ = ∅, W is the same at every state, no fallback. So EXP-IDEAL's run is ONE phase, ONE joint λ-run, ONE epoch with D ⊇ all gates, f = 0. This is my reading of R104, not a signed sentence.

| R-id | line | class / scope | verdict | reason |
|---|---|---|---|---|
| R17 | 730 | N5 on one-player games: iteration bound | TRUE-KEPT | Γ3(G_k) is two-player; purpose «a bound on the candidate N5 itself on a subclass» was support for G-N5-TIME, purpose ends; R17 (a)-(c) stay cited lemmas |
| R18 | 778 | N5 on o-acyclic one-Odd-choice games, conditional on (P) | TRUE-KEPT | 𝒞^1O excludes Γ3(G_k); (P) proved in R36; step toward G-N5-TIME, purpose ends |
| R19-R23 | 836, 884, 924, 975, 1021 | N5 on one-Odd-choice games, per-phase lemmas | TRUE-KEPT | 𝒞^1O only; «partial step-4 lemmas for N5 on a subclass» = step toward G-N5-TIME, purpose ends |
| R24 | 1064 | one-Odd-choice games: Lemma R, TB, CASC, Theorem U1 | TRUE-KEPT | 𝒞^1O only; step toward G-N5-TIME, purpose ends; BUT R24 (a) Lemma R and (b) choice rule are named premises of R104/R117, so the kill rests on them |
| R25 | 1113 | any game per phase: fallbacks vs non-tame transitions; rest 𝒞^1O | TRUE-KEPT | Theorem FB is conditional on J and counts fallbacks only (the FL run has none); purpose ends |
| R26 | 1163 | one-Odd-choice games: W-flat runs short | TRUE-KEPT | 𝒞^1O only; note: EXP-IDEAL's run keeps W constant for 2^k − 2 steps, so this (and R24 CASC) does not extend beyond 𝒞^1O; purpose ends |
| R27 | 1218 | any game per phase: Theorem LP; corollaries on 𝒞^1O | REDUCTION-NOW-DECIDED | LP (any game): T ≤ (m−n+1)(T_rel+1), T_rel ≤ (n+1)(ρ+1)·n(n−1)+ε, ρ := #rises of the used level (not R56's ρ); X = «rises and ε polynomial per phase» ⇒ polynomial phases; one-phase run ⇒ X FALSE on Γ3(G_k); the inequality stays true |
| R28-R34 | 1293, 1338, 1389, 1450, 1502, 1560, 1614 | N5 on one-Odd-choice games (R31 FBW: every game, structural) | TRUE-KEPT | counts are 𝒞^1O; step toward G-N5-TIME, purpose ends |
| R35 | 1660 | one-Odd-choice games: per-level fallback count | TRUE-KEPT + CONJECTURE-OPEN | 𝒞^1O only; «the per-level conjecture» (NJB / ENT in the body) is a 𝒞^1O statement, not decided; purpose ends |
| R36 | 1717 | one-player games: no improving edge ⇒ optimal (Lemma P1) | TRUE-KEPT | unconditional fact; purpose does not end: R36 (c) is a named premise of R104/R117 |
| R37 | 1752 | one-Odd-choice games: blocked edges, per-level violation | TRUE-KEPT + CONJECTURE-OPEN | as R35 («the per-level conjecture») |
| R38 | 1816 | KEY, CN-LAST every game (structural); counts on 𝒞^1O | TRUE-KEPT | WCH, SCOPE-COUNT, FB-INT, NH1-FB are 𝒞^1O per the body; no every-game count; purpose ends |
| R39-R46 | 1862, 1928, 1987, 2041, 2108, 2159, 2222, 2270 | N5 on one-Odd-choice games (R43 STALE-GATE: every game, structural) | TRUE-KEPT | counts are 𝒞^1O; step toward G-N5-TIME, purpose ends |
| R47 | 2324 | every game: joint λ-runs per run; 𝒞^1O phases | CHECK | unconditional polynomial on every game, but it counts λ-runs, not their length; EXP-IDEAL's run sits inside one joint λ-run; no contradiction |
| R48 | 2362 | one-Odd-choice games: in-phase fallbacks polynomial | TRUE-KEPT | 𝒞^1O only; purpose ends |
| R49 | 2432 | one-Odd-choice games; ANTI on one-player games | TRUE-KEPT + CONJECTURE-OPEN | «CONJECTURE INTO» (𝒞^1O) not decided; «CONJECTURE "in scope, THR ⇒ M ≥ 0"» is already FALSE in the title, independent of EXP-IDEAL |
| R50 | 2494 | one-Odd-choice games: transitions per phase | TRUE-KEPT | 𝒞^1O only; purpose ends |
| R51 | 2567 | N5 polynomial on one-Odd-choice games (Theorem 1O-POLY) | TRUE-KEPT | SUBCLASS result stands (Γ3(G_k) ∉ 𝒞^1O); as support for G-N5-TIME, purpose ends |
| R52-R53 | 2626, 2658 | one-Odd-choice games, per phase | TRUE-KEPT | 𝒞^1O only (R53's «REDUCTION» is inside 𝒞^1O); purpose ends |
| R54 | 2720 | every game: DUAL, Φ-kO, ENDGAME; 𝒞^1E MIRROR | TRUE-KEPT | Φ-kO's n(n−1)+∏deg(o_i) is exponential on Γ3(G_k), no conflict; «(H-OF)» is about 𝒞^1O, not decided; purpose ends |
| R55 | 2778 | every game: structural disagreement-set lemmas | TRUE-KEPT | title: «nothing here bounds N5's running time on any class»; purpose ends |
| R56 | 2832 | every game per phase: f ≤ 1 + (n − 1)(2 + ρ) | TRUE-KEPT + CONJECTURE-FALSE | FB-RED counts fallbacks only, stays true; «CONJECTURE ρ-POLY»: ρ is exponential on Γ3(G_k) by the sketch in Note 3 (unrefereed; exact text of ρ-POLY is not in RESULTS) |
| R57 | 2893 | every game: OUT-G, BIT-G; 𝒞^1E polynomial | TRUE-KEPT | no iteration bound on general games; Γ3(G_k) ∉ 𝒞^1E (N Even movers of degree 2); premise «1E-N3» is also a premise of R104/R117 |
| R58 | 2959 | ≤ 2 Odd choice vertices per honest class | TRUE-KEPT | fallback count, conditional on R56; Γ3(G_k) has all gates in one honest class (cycle node K1): excluded; purpose ends |
| R59 | 3018 | every game: fallback ≥ one value-iteration round | TRUE-KEPT | lower bound on progress, no count; purpose ends |
| R60 | 3058 | every game per phase: f ≤ 1 + N_K, f ≤ 1 + n·N_ep | TRUE-KEPT | title: «N_K can be exponential»; ACCEL (b) bounds in-phase Even switches by N_K, so N_K ≥ 2^k − 2 on Γ3(G_k): consistent; purpose ends |
| R61 | 3103 | 𝒞^kO, k fixed; boundedly many Odd choices per class | TRUE-KEPT | fallback count on an excluded class; ROUTE-k, SAT-k, ALT structural; purpose ends |
| R63 | 3156 | every game per phase: crossings vs epochs | TRUE-KEPT | conditional on N_ep and the OPEN residual X_SN^pre; crossings only; purpose ends |
| R64 | 3206 | every game: phase = sum of epochs on G′_E | REDUCTION-NOW-DECIDED | EP-k: X = «N_ep polynomial and every N5^τ phase on G′_E ∈ 𝒞^{|D_E|}O polynomial» ⇒ polynomial phases; the run is one epoch with G′_E = Γ3(G_k) ⇒ X FALSE (second conjunct); EP-0 and EP-1 (|D_E| ≤ 1) untouched |
| R62 | 3267 | every game: structural (file order: after R64) | TRUE-KEPT | title: «no count»; the coarse freeze under (h3_D) bounds no transitions; purpose ends |
| R65 | 3324 | N5 vs N5^τ transfer; EP-1 for one disagreement vertex | TRUE-KEPT + CONJECTURE-OPEN | «(Στ)» concerns N5^τ on 𝒞^1O (audited, not signed): not decided; EP-1 needs |D_E| = 1; purpose ends |
| R66 | 3396 | every game per phase: D = ∅ epochs vs f | TRUE-KEPT | conditional on f; superseded by R70 (see R70); purpose ends |
| R67 | 3444 | every game: one fallback-free run of a phase | REDUCTION-NOW-DECIDED | SPLIT-RED: |S| ≤ N_split + (N_split + 1)(n + m − 1); X = «N_split(S) polynomial» ⇒ polynomial FL runs; EXP-IDEAL ⇒ X FALSE (N_split ≥ (2^k − 2)/(n + m) − 1 by PIECE_D (b), λ_W constant); OFFSET's 2^{B+1} and CHARGE-U stay true |
| R68 | 3516 | every game per phase: W-honest states vs f | TRUE-KEPT | conditional on f, X_dir, X_big and (Στ); superseded by R70; purpose ends |
| R69 | 3583 | every game per phase: structure of ρ events | TRUE-KEPT | title: «no count»; purpose ends |
| R70 | 3646 | every game per phase: W-honest and D = ∅ states | CHECK | unconditional 4n² − 3n per phase; no contradiction: every state of EXP-IDEAL's run has D ≠ ∅ and Ξ ≠ W (σ̄ = β-face, τ = e-face) |
| R71 | 3695 | every game per phase: f vs configurations | TRUE-KEPT | fallbacks only; min(N_ep, Π_q deg(q)) is exponential in general; the Δ^k and |D| ≤ 1 corollaries exclude Γ3(G_k); purpose ends |
| R72 | 3757 | every game per phase: RELAY chains of ρ events | TRUE-KEPT | title: «no count»; with Note 3, ROUTE_c + CYC_c + TOG_c is exponential on Γ3(G_k); purpose ends |
| R73 | 3813 | every game per phase: N_ep and f reductions | TRUE-KEPT | reduces N_ep and f (not transitions) to X_dir, X_big, NCONF_{≥2}, R⁰_{≥2}; the run has N_ep = 1, f = 0, so none is decided; purpose ends |
| R74 | 3877 | every game per phase: Bellman-Ford freezes | TRUE-KEPT | reductions in G_c, f, G-intervals (title: «not bounded here»); no iteration bound; purpose ends |
| R75 | 3971 | every game per phase: κ-offsets, FT-COUNT, TIE-CHARGE | CHECK | two unconditional polynomial per-phase counts, but of sub-events at path-free vertices (P(Ξ) = ∅); movers and gates of Γ3(G_k) have non-empty P-sets; no contradiction seen (not checked line by line) |

#### (1) Named conjectures and hypotheses in these titles
- «(P)» (R18): premise for one-player games; proved in R36; unaffected.
- «the per-level conjecture» (R35, R37): 𝒞^1O; not decided by EXP-IDEAL.
- «CONJECTURE INTO» (R49): 𝒞^1O; not decided.
- «CONJECTURE "in scope, THR ⇒ M ≥ 0"» (R49): already FALSE in the title.
- «(H-OF)» (R54): first-phase bound for N5^OF on 𝒞^1O; used by R57; not decided.
- «CONJECTURE ρ-POLY» (R56): ρ := Ξ-changes at Odd choice vertices per phase; FALSE under EXP-IDEAL by Note 3 (unrefereed).
- «1E-N3» (R57, standing SPEC premise): not decided; EXP-IDEAL itself uses it through R104/R117.
- «(Στ)» (R64, R65, R68, R70, R73): R48 (i) and R50 (h) for N5^τ on 𝒞^1O; not decided.
- State hypotheses, not conjectures: «(h_D)», «(h3_D)» (R55, R62, R67), «(NC)» (R62), «hypothesis (H)» (R72), «hypothesis (i)», «(ii)» (R67).
- Open quantities named in titles: N_K, N_ep (R60); X_SN^pre (R63); B, N_split, U(S) (R67); f_in, X_dir, X_big (R68, R70); ROUTE_c, CYC_c, TOG_c (R72); NCONF_{≥2}, R⁰_{≥2} (R73); G_c (R74); EXIT_x, D, ODDC_c (R75). Now exponential on Γ3(G_k): N_K, N_split, R27's rises + ε; by Note 3 also ρ and ROUTE_c + CYC_c + TOG_c.

#### (2) CHECK entries, quoted clauses
- R47: «every run has at most 2n(n − 1) + 1 joint λ-runs (Lemma Φ, every game)». Hypotheses: none. Consistent because the exponential run lies in one joint λ-run.
- R70: «in every phase the W-honest states number at most 4n² − 3n (Theorem HON-FF), with no fallback term, and so do the D = ∅ states, the D = ∅ epochs and the in-phase transitions whose source lies in a D = ∅ epoch (HON-0-FF)». Hypotheses: every game, premise 1E-N3. Consistent because D ≠ ∅ at every state of the run.
- R75: «the transitions with an F-touching κ-change number at most 2(n − 1)(|U_c| − 1) per phase (Lemma FT-COUNT)» and «STRICT_c + TIE_c ≤ 2(n − 1)(|U_c| − 1) (Corollary TIE-CHARGE)». Hypotheses: every game, per phase and class. Sub-event counts only.
- Looked at and not marked: R54 Φ-kO (bound exponential), R27 Lemma NU (per NU-run), R64 EP-0 / R65 EP-1 (per epoch with |D_E| ≤ 1), R71 (d) (|D| ≤ 1 throughout), R58 / R61 (bounded Odd choices per class).

#### Notes (unrefereed, for the Lead to route)
1. The «one phase, one epoch, D ⊇ all gates, f = 0, W constant» reading above carries R27, R47, R64, R67, R70; it should be checked against R104/R117 by a referee.
2. N5^τ (R64, R65) makes the same run: Iτ = ∅ at every state (R104 (f)), so S4b^τ = S4b there. Keep-τ-on-ties is not a rescue.
3. ρ-POLY sketch: while no gate changes Ξ, every option's Ξ-value is fixed, and an IDEAL step moves a mover only to a strictly better Ξ-value, so such a stretch has at most M − N steps; hence at least L(G_k)/(M − N + 1) − 1 transitions carry a ρ event.

DONE: classification of R17-R75 (59 entries, 41 rows); nothing edited in the repository, nothing committed.
FINDINGS: no contradiction with EXP-IDEAL in R17-R75. R27, R64, R67 reductions are decided (their X is FALSE on Γ3(G_k)). «CONJECTURE ρ-POLY» is FALSE by an unrefereed sketch. R24 (a)/(b), R36 (c), R57's 1E-N3 are premises of the kill itself.
NEEDS: Lead: have a referee check Notes 1-3, and read ρ-POLY's exact wording in the packet (it is only named in RESULTS, line 2871).

## B. RESULTS R76-R130 against EXP-IDEAL (reader sub-agent report, reproduced as returned; its «DONE / FINDINGS / NEEDS» lines are the reader's, not mine)
### R76–R130 against EXP-IDEAL (titles of docs/RESULTS.md at trunk 5d7aab0f)

Source: `‹session scratchpad›/trunk/RESULTS.md`, titles only. A body line was opened only to read the statement of a name the title leaves undefined (marked «body Lnnnn»). Nothing in the repository was edited. «…» marks a verbatim quote from the file, except the statements X in REDUCTION-NOW-DECIDED rows of the form «… polynomial» or «… ≤ p(n)», which are my wording of X.

Facts used in the reasons, all from the titles. On Γ(G_k) from R104's start and on Γ3(G_k) from S3, the states 0 … L, with L = 2^k − 2, form one FL run (R104 REALIZE, R117 REACH3). On it there is no fallback, τ is fixed (R124 E0), σ̄ sits on the β-face at every gate and all cycle nodes are fixed (R122 BETA-ACYC, LAMBDA-CONST), and W is fixed at every vertex. So this run is at once one phase, one τ-stretch, one W-run, one piece and one W-constant interval. "The run" below means this run. n = 63k − 106 on Γ(G_k) and 135k − 230 on Γ3(G_k).

| R-id | line | model / class | verdict | reason |
|---|---|---|---|---|
| R76 | 4101 | N5, every game, in-phase S4a runs; abstract model ABS | TRUE-KEPT | MIG-SPLIT and UL-RED (conditional, K(S) unbounded) bound no run; ABS-HEIGHT / ABS-TIE live in ABS, «the model's link to N5 is a READING»; purpose ends; «UL_G» not decided. |
| R77, R78 | 4178, 4247 | N5, every game; σ̄-constant intervals under GEN_W | TRUE-KEPT | STATIC-DEPTH, GCI-LEN-ρF, PURE-LEN′ need GEN_W, which fails on Γ(G), Γ3(G): a mover's options are W-tied (that is what an FL move is); purpose ends. |
| R79 | 4322 | N5, every game; phase restricted to used Odd edges | TRUE-KEPT | RESTRICT_H, REPRO_H: «they bound nothing»; neutral tool, holds on the run. |
| R80 | 4405 | N5, every game, one phase | TRUE-KEPT | PHASE-SW, FRESH-RED (\|I\| ≤ m_E + NOFRESH(I)) hold; on the run NOFRESH ≥ L − m_E; purpose ends. |
| R81 | 4520 | N5, every game; in-phase fallbacks per K-configuration | TRUE-KEPT | bounds fallbacks only; Γ3(G) has exactly one (R124); «FB-LIN» not decided; purpose ends. |
| R82 | 4653 | N5, every game; pieces (one phase, σ̄ constant) | CONJECTURE-FALSE | «CONJECTURE PIECE, every piece ≤ n − 1 transitions»: the run lies in one piece and L > n − 1 for k ≥ 9 on Γ(G_k), k ≥ 11 on Γ3(G_k). The proved part (STATIC-DEPTH′, EPOCH) stays true because GEN_W fails. «STATIC-DEPTH′-TIE»: list 1. |
| R83 | 4774 | N5, every game; REL-admissible segments of a run | TRUE-KEPT | GATE-RISE's count and REL-SPLIT (needs GEN_W, (H4′_rel)) stay true; purpose ends; «SEG-RUN» not refuted (the run is one segment, SEG = 1). |
| R84 | 4941 | N5, every game; top rank of a path set | TRUE-KEPT | bounds top changes only (≤ n − 1 per vertex and phase); with R86 the P-changes under a fixed top are super-polynomial on Γ3(G_k); purpose ends. |
| R85, R86 | 5064, 5269 | N5, every game; T against P*, P*^U and carries NM* | REDUCTION-NOW-DECIDED | bound ⇐ X (COMPOSE-RUN, COMPOSE-NM). X = «P*, P*^U polynomial», resp. «NM* polynomial»: FALSE on Γ3(G_k). τ fixed gives P*^U = 0, so Even's P* and NM* are super-polynomial. GATE-SHUT, SW-RETURN kept. |
| R87 | 5456 | VARIANT N5-SF (S4a against Odd's best reply) | CONJECTURE-OPEN | «CONJECTURE SF-POLY (SBC polynomial)»: about N5-SF, «it says nothing about N5 itself»; EXP-IDEAL runs N5's own S4a. |
| R88 | 5630 | N5, any game; frozen W-phases | TRUE-KEPT | counts W-changing transitions; the run has none; «FW-BF» not decided; purpose ends. |
| R89 | 5854 | N5, every game; τ-stretch length | REDUCTION-NOW-DECIDED | bound ⇐ X (STRETCH-RED). X = «NM^U, R*_S, FL_S, ρ_S polynomial»: FALSE on Γ3(G_k), since FL_S ≥ L by definition. |
| R90 | 6116 | N5, every game; T against B*, REP*, SC*, O* | REDUCTION-NOW-DECIDED | ⇔ (CUT-POLY and converse). X = «B*, REP*, SC*, O* polynomial»: FALSE on Γ3(G_k). There O* = 0 and B* ≤ 1 (R124), so REP* or SC* is super-polynomial (SC*, the W-silent re-entries, if W-tied options are never «blocked»: my reading). |
| R91, R92 | 6384, 6656 | N5, every game; fallbacks per phase; W-changes of a W-run | TRUE-KEPT | GAP-RED counts fallbacks; FW-R*′ … TXC-RED count W-changing transitions and late adoptions; the run has neither; «FB-LIN» not decided; purpose ends. |
| R93 | 6972 | N5, every game; W-runs and tie switches; VARIANT N5-LZC | TRUE-KEPT | NEW-BOUND gives TIE_F ≥ L − m_E on the run (WCH_F = 0); premise [P-WCHτ] not decided (W never changes). N5-LZC has TIE_F = 0 (LZ-STRICT), so it has no such FL run, but «nothing transfers to N5». |
| R94 | 7272 | N5, every game; phase length against flat transitions | REDUCTION-NOW-DECIDED | bound ⇐ X (PHASE-RED′). X = «FLATTR_P, Σ FLATSW_P polynomial»: FALSE on Γ3(G_k) (the run is one phase). |
| R95 | 7476 | N5, every game, every start; W-runs | REDUCTION-NOW-DECIDED | ⇔ chain WRUN-EQ. WRUN-POLY and each equivalent (XI-CH-POLY, P*-POLY, DEEP_k-POLY, the five conjunctions) FALSE on Γ(G_k), Γ3(G_k). Singly FALSE: FL-POLY, TIE-POLY, [P-INT]. Singly undecided: R*-, R3-, SB-, R°-, ALT-, FREE-POLY. NO-DEV is not hit: Ξ ≠ W at the gates. |
| R96, R97 | 7748, 8032 | N5, every game; W-run events and sources; T against XE, XO | REDUCTION-NOW-DECIDED | ⇔ (T-XCH, HEAD-RED, SRC-COUNT), all on Γ3(G_k). «XE, XO polynomial» FALSE (XO = 0, so XE is super-polynomial). «max SB_F, CN_F, HXU_F polynomial» FALSE; SB = CN = 0 on the run, so max HXU_F is super-polynomial («HX-POLY» false). «max HXS_F polynomial» FALSE. |
| R98 | 8296 | N5, every game; Odd relay, fuel re-routes | TRUE-KEPT | «a RELOCATION (no count is bounded here …)»; purpose ends. |
| R99, R100 | 8596, 8918 | N5, every game; W-runs: resets, descents, root changes | TRUE-KEPT | the equivalences are about W-changing transitions WCT_F; on the run WCT_F = 0 and \|F\| = T1_F = L (BW-ACC: N_F ≥ L); purpose ends. |
| R101 | 9251 | N5, every game; whole run: settle gap, bracket gap, INC | REDUCTION-NOW-DECIDED | ⇔ (SETTLE-RED, BRACKET-RED, CONSISTENT-RED). «SG polynomial», «BG polynomial», «INC polynomial»: all FALSE on Γ3(G_k). |
| R102 | 9478 | N5, every game; S4b output optimal | UNRELATED | premise lemma on S4b; on Γ3(G) Iτ = ∅ at every state (R124 E0). |
| R103 | 9641 | N5, every game; FL runs against gating changes GCH | REDUCTION-NOW-DECIDED | ⇔ (FL-GCH). «GCH polynomially bounded» FALSE on Γ(G_k), Γ3(G_k): GCH ≥ L/CAP − 1, CAP ≤ n + m. FL-ANCHOR (epoch ≤ CAP) must hold on the run. |
| R104 | 9864 | N5 from a given start on Γ(G), G Ξ-acyclic; defines IDEAL | REDUCTION-NOW-DECIDED | REAL-IDEAL: bound ⇐ X with X = «every FL run from every start pair ≤ p(n)» (FL-POLY, body L9967): FALSE, an FL run of exactly L on Γ(G_k). REALIZE is a tool of the kill packet. |
| R105 | 10155 | IDEAL, Ξ-acyclic, any width; degree ≤ 2 for KEYFLIP | REDUCTION-NOW-DECIDED | ⇔ (U-EQ, KEYFLIP). «U polynomial» and «KF polynomial» FALSE on G_k: U ≥ L/N − 1, KF ≥ L − N. The exponential bounds (EXACT-ENERGY, RANK-BOUND, RECURSION) stay. |
| R106 | 10401 | IDEAL, Ξ-acyclic, degree ≤ 2; improvement cube (USO) | TRUE-KEPT | T ≤ LP with LP exponential: no contradiction; the READING «a polynomial bound on T must use the W-key rule» is moot; tool: the G_k run is a directed path of o_G. |
| R107 | 10593 | IDEAL, Ξ-acyclic, any width | REDUCTION-NOW-DECIDED | ⇔ (M2-EQ). «M₂ polynomial» FALSE on G_k (M₂ ≥ L/N − 1). Also CONJECTURE-FALSE: «CONJECTURE LIN-2 (T ≤ 2N)», L > 18k − 32 for k ≥ 7. |
| R108 | 10812 | IDEAL, Ξ-acyclic, degree ≤ 2, any width | TRUE-KEPT | exponential bound T + 1 ≤ Π_l (n_l + 1) (3^d − 1 on ladders): not a contradiction; tool, must hold on G_k. |
| R109, R110 | 11030, 11323 | IDEAL on 𝓛_d, 𝓦_d, 𝓛^R_d | TRUE-KEPT | ladder recursion T*(d) ≤ 3T*(d − 1) + 2 and the flip model; G_k (up to 8 two-option movers per level, wires) is outside 𝓛_d and 𝓛^R_d; SHIFT, LIFT (any degree) are tools; «SLOT-TRADE», «FLIP-ADD» not decided. |
| R111 | 11598 | IDEAL, Ξ-acyclic, any width; LADDER on 𝓛^R_d | REDUCTION-NOW-DECIDED | PAIR-MOVES with CASCADE: T ≤ N + Σ flips and flips ≤ T. «pair flip counts polynomial» FALSE on G_k. LADDER's 3^(l+1) − 1 is exponential and ladder-only. Names: list 1. |
| R112 | 11909 | IDEAL on 𝓛^R_3 (machine) | TRUE-KEPT | T^R(3) = 8, an exact value on a restricted class; untouched. |
| R113 | 12152 | IDEAL on 𝓛^R_d; KP-MOVE, PATH-RISE at any degree | TRUE-KEPT | T ≤ 2^(d+2) − 2d − 4 is exponential and only on 𝓛^R_d: not a contradiction; its ladder purpose is unaffected; PATH-RISE, KP-MOVE are tools. |
| R114 | 12394 | IDEAL on 𝓛^R_d; RISE-EQUIV, MOVE-RISE at any degree | REDUCTION-NOW-DECIDED | ⇔ (RISE-EQUIV). «max R(x, k) polynomial» FALSE on G_k (≥ (L − 1)/M). PHIK-DESCENT, OPT-K and the certificates are exponential and ladder-only; kept. |
| R115 | 12697 | IDEAL, ISO genomes of 𝓛^R; IM for any acyclic degree-2 | TRUE-KEPT | T_∞(m) ≤ 2^(2m) − 1 is exponential and ladder-only; IM is a tool. |
| R116 | 13072 | IDEAL on 𝓛^R_d; REDUCE-XI, AND-GATE at any width | TRUE-KEPT | MOVES-EQUIV (μ ⇔ T^R) is ladder-only, neither side decided by EXP-IDEAL; REDUCE-XI gives a Ξ-target of G_k with ≥ (L − 1)/N moves. |
| R117 | 13362 | N5 from S3 on Γ3(G), G Ξ-acyclic | REDUCTION-NOW-DECIDED | REAL-IDEAL-S3: bound ⇐ X with X = «every FL run of N5 from S3 ≤ p(n)» (FL-S3-POLY, body L13453) and X = «N5 from S3 makes ≤ p(n) iterations»: both FALSE on Γ3(G_k). REACH3 is the kill packet's transfer tool. |
| R118 | 13607 | Howard on IDEAL-CYC(G); N5′-xi (RED-XI, REACH3-CYC) | TRUE-KEPT | the polynomial statements (ONEP-POLY, T-CYC) are for Howard's rule and N5′-xi: not a contradiction; unaffected. |
| R119, R120 | 13879, 14114 | IDEAL on 𝓛^R_d, doubling levels; HIT, ALT-MIN at any degree | TRUE-KEPT | structure of the ladder tower route, no bound on T; an off-ladder family now overtakes that route, its ladder questions stay open; HIT, ALT-MIN are tools. |
| R121 | 14320 | Howard, IDEAL-CYC; e-set height D_E | TRUE-KEPT | «bounds the e-set height … only, NOT R and NOT any running time», in the Howard model: not a contradiction. |
| R122 | 14744 | Ξ-acyclic genomes: Howard on IDEAL-CYC, N5′-xi on Γ3 | TRUE-KEPT | T_CYC ≤ N and first fallback ≤ N + 1 are Howard / N5′-xi bounds on the very games Γ3(G_k): not a contradiction («N5 with SPEC's S4a tie rule realises L(G) there»). BETA-ACYC, LAMBDA-CONST are rule-free tools for the kill packet. |
| R123 | 15076 | Howard on IDEAL-CYC, every genome | TRUE-KEPT | QUIET, UP-T bound T_CYC (Howard) only: not a contradiction. |
| R124 | 15371 | N5 and N5′-xi from S3 on Γ3(G) | REDUCTION-NOW-DECIDED | ⇔ (EXACT-L): «N5's iteration count is polynomial in n iff L(G) is polynomial in N + M». N5 makes exactly L + 3 = 2^k + 1 iterations on Γ3(G_k), with its one fallback at iteration 2^k − 1. This is the exact transfer of the kill. The identity uses SPEC's FIX 1-4 tie-breaks ([RULE]). |
| R125–R129 | 15595, 15726, 15903, 16127, 16368 | Howard on IDEAL-CYC / HOW3; N5′-xi mover phase on Γ3 | TRUE-KEPT | every bound (CHAIN3, QUIET-N, GATE-FLIP, ALL-TCYC, FVS-TCYC) and every equivalence (RE-, ALT-, C-, A*-EQUIV) is for Howard's rule or N5′-xi; «nothing is claimed for N5» (R127): not contradictions; unaffected. |
| R130 | 16525 | N5′-xi and N5 from S3 on W-flat wrappers W(H, s0) | CHECK | the one polynomial bound on N5's own iterations on a gadget family: list 2. Expected clear (wrappers have one W-level, G_k has k + 1). XI-EXP (N5′-xi exponential, CONDITIONAL) is untouched. |

Tally: TRUE-KEPT 34, REDUCTION-NOW-DECIDED 17, CONJECTURE-FALSE 1, CONJECTURE-OPEN 1, UNRELATED 1, CHECK 1 (55 entries).

#### 1. Named conjectures, hypotheses and DEAD statements

**Refuted by EXP-IDEAL**
- «CONJECTURE PIECE, every piece ≤ n − 1 transitions» (R82): FALSE, from k = 9 on Γ(G_k).
- WRUN-POLY, XI-CH-POLY, P*-POLY, DEEP_k-POLY, FL-POLY, TIE-POLY, [P-INT] (R95): FALSE, a W-run of L transitions.
- INT-LIN (R95; «\|I\| ≤ n − 1 for every W-constant interval I», body L7626): FALSE, same thresholds as PIECE.
- BIP-POLY (R95; «every BIP(ρ, τ) run … has at most p(n) steps», body L7625): FALSE if BIP's step is N5's step on a frozen stretch, as body L7555 reads; to confirm.
- HX-POLY (R96; «max HXU_F polynomial», body L7897): FALSE on Γ3(G_k).
- «CONJECTURE LIN-2 (T ≤ 2N)» (R107): FALSE for k ≥ 7. It seems already contradicted by R120's instance G7_best_d28 (N 56, F(6) = 222, and flips ≤ T by R111 CASCADE).
- IDEAL-ACYC-POLY, FL-POLY (every-start form) and FL-S3-POLY appear in no title of R76–R130; they are stated in the bodies of R104 (L9967) and R117 (L13453–13459). All FALSE. G-N5-TIME («stays OPEN» in every title) is FALSE for N5 as specified.
- R106's READING «a polynomial bound on T must use the W-key rule» and R111's TOWER READING «the doubling tower is not a shortcut around G-N5-TIME» are overtaken. L = 2^k − 2 equals TOWER's count 2^(l+1) − 2 at l = k − 1 (an observation only).

**Not decided by EXP-IDEAL**
- «UL_G» (R76): about unforbid-switches in global C-intervals; not readable from the data given.
- «STATIC-DEPTH′-TIE» (R82): (H1′), (H2), (H3′) hold on the run, so it is FALSE exactly if (H4′) holds at the last state. In genome terms (my translation): the W-target edges and Ξ-target edges of the movers' final options have no cycle together. A finite check on G_k.
- «SEG-RUN, SEG = O(n)» (R83): the run has SEG = 1.
- «FB-LIN» (R81, R91): fallbacks per phase; Γ3(G) has one. «FW-BF» (R88) and [P-WCHτ] (R93): W-changing transitions only.
- «SF-POLY» (R87): variant N5-SF.
- CN-POLY, XCN-POLY (R96): the run has no switch at C and no σ̄-change.
- «SLOT-TRADE» (R109, R110), «FLIP-ADD» (R110, R115; T_2(m) ≤ T^R(m) + O(m), body L11485), SUM_1 (R115), DBL-O(1) (R113), «RISE-2D» (R114): statements on 𝓛_d / 𝓛^R_d only. RISE-2D looks already false at d = 6 by DE37's instance with R114 MOVE-RISE (R(4, 1) ≥ moves(8) = 13 > 12); to confirm.
- MOVES-2D (R114, R116): ladder-only; already DEAD by DE37 (L17335), not by EXP-IDEAL.
- PAIR-LIN (R111, R113, R115), PM′_S, RENEW-COUNT (R111): their statements are not in RESULTS (packet P-IDEAL-KEYS l. 112, 164, 274). If stated on 𝓛^R_d only, not decided. If stated for all degree-≤-2 Ξ-acyclic genomes, any form that makes flips or moves polynomial is FALSE on G_k: the mover with 2^(k−2) moves has flips(a, b) ≥ 2^(k−2) − 1 and fewer than N Ξ-descendants.
- «IN-BOUND», OVT-DV (R121, R123) and HYPOTHESIS [E-LEV] (R121, R123, R125–R128): Howard / IDEAL-CYC side.
- XI-EXP, Claim NT (R130): N5′-xi; «N5 (SPEC) is not affected».

**Already DEAD before EXP-IDEAL, unchanged**: LOC as stated (R76), ABS-DEPTH-TIE (R77), PURE-LEN (R78), SW-LIN, XR-LIN (R80), the Δ form of TOP-MONO (R84), REP-LIN (R90), BIP-REL-1 (R95), FLIP-EV (R96), «every R-descent is a fuel re-route» (R100), «every λ_W-phase of a τ-stretch has at most n − 1 W-changing transitions» (R101), «Ξ at ODIFF vertices is constant inside an FL run» (R103), «T ≤ ⌊3N/2⌋ on degree-≤-2 IDEAL-ACYC» (R107), REPLAY (R108), SEG1-2D (R109), SC-ISO (R110, conditional), PM, PMV (R111), «D ≤ 2·LM + c» and «every mover of level l moves at most 2(l + 1) times» (R116), SUBDIV (R117), SEG-2P, ODD-FIXED (R118), the four DEAD statements of R119, RUN-TRANSFER (R125), D1, D3 (R126), D1–D7 with RW-WT, RW-WT*, RW-B0, RW-B0* (R127), R128's DEAD list. Proved, no longer a conjecture: RESTRICT_{u\|J} (R79).

**Do not occur** in the titles R76–R130: XTW, O1, O1′ (XTW and O1′ are nowhere in the file; «O0/O1» only at L16899, in an A_DTL dead end).

#### 2. CHECK

- **R130 (L16525), the only one.** Quote: «for EVERY parity game H and every positional Even strategy s0 of H, the W-flat wrapper W(H, s0) (…: every edge of H stretched to a 6-edge path through an Odd gate with a pad to an even self-loop c_W above H, …) … makes N5 stop after exactly F + 2 iterations with one fallback (F ≤ m_E − \|V_E\| + 1 under [RULE])». For a contradiction Γ3(G_k) would have to be such a wrapper: every gate's W-face leads to c_W, i.e. every mover is on W-level 0. G_k has k + 1 W-levels, and Γ3 has N + 7M + 10 vertices against the wrapper's n + 7·m_E + 6·m_O + n_O + 9, so none is expected. The bound agrees with R108 SEG-ONCE (level-0 movers move at most once). The kill packet should say this in one line.

Conditional polynomial bounds whose hypothesis must FAIL on the run (cleared, not CHECK):
- R77 STATIC-DEPTH, R78 PURE-LEN′, R82 STATIC-DEPTH′ / EPOCH, R83 STATIC-DEPTH-REL / REL-SPLIT: GEN_W fails (W-tied options).
- R95 NO-DEV: needs Ξ_t = W_t on the whole W-run; fails at every gate (σ̄ on β, τ on e).
- R101 CONSISTENT-RED: needs Iσ_k = IW_k at every transition.
- R96 RUN-SETTLE (event-free ≤ n − 1), R97 SRC-SETTLE (source-free ≤ n − 1 + m_C), R103 FL-ANCHOR (epoch ≤ CAP), R107 SINGLE-SHORT (single-mover steps give T ≤ N): they force super-polynomially many events, epochs and multi-mover steps.
- R76 ABS-HEIGHT / ABS-TIE, R77 ABS-DEPTH: abstract model, its link to N5 unsigned.

Polynomial bounds for Howard or N5′-xi (not contradictions): R118 ONEP-POLY, T-CYC; R122 ACYC-LIN, ACYC-XI; R123 UP-T; R125 CHAIN3; R126 QUIET-N; R129 K1-TCYC, FVS-TCYC, ALL-TCYC. Exponential or ladder-only bounds: R105, R108, R109, R111 LADDER, R113, R114, R115.

#### 3. Facts without a ladder hypothesis that must hold on G_k

IDEAL model on Ξ-acyclic genomes († = degree ≤ 2, which G_k has):
- R105: ENC, LOCAL, MONO, XI-NEW, RISE, CHAIN-BACK, DECREMENT, EXACT-ENERGY; † KEYFLIP, TOP-MONO, RANK-BOUND, INTERVAL-RESTRICT, INTERVAL-CHARGE.
- R106 †: DECOMP, MULTI→SINGLE.
- R107: MULTI-CHARGE, SINGLE-SHORT; † TRIGGER, XIFLIP, MIN-FLIP.
- R108: SEG; † SEG-ONCE, LEVEL-PRODUCT.
- R109: SHIFT, LIFT.
- R111: LOCAL-KP, CASCADE, RENEW, MERGE; † PAIR-KF, PAIR-MOVES, RETURN.
- R113: KP-MOVE, PATH-RISE. R114: KEY (degree-2 clause), RISE-EQUIV, MOVE-RISE. R115: IM. R116: REDUCE-XI, AND-GATE. R119: HIT, ALT-MIN.

Games Γ(G_k), Γ3(G_k):
- R104 REALIZE; R117 NO-REACH, REACH3 (S3-START, PAD); R122 BETA-ACYC, LAMBDA-CONST, ACYC-LIN, ACYC-XI; R124 E0–E4, ENDGAME-3-N5, EXACT-L; R125 ESC3-ALL, W3-ALL, REACH3-ALL; R118 LEVEL0, BR-SEG; R129 ALL-TCYC.
- N5 on every game, read on Γ3(G_k): R80 EVERY-SWITCH; R86 COMPOSE-RUN; R94 PHASE-RED, FLAT-SW; R96 RUN-SETTLE, T-XCH; R97 SRC-SETTLE; R99 BW-ACC; R101 SETTLE-MON, BRACKET-MON; R103 FL-TIGHT, PREFIX, FL-ANCHOR.

Sharpest tests for the family:
1. R108 SEG-ONCE: every level-0 mover moves at most once.
2. R111 PAIR-KF, PAIR-MOVES: every wire (two options, one W-target) has KF = 0 and moves at most once; the mover with 2^(k−2) switches has W-targets a ≠ b with flips(a, b) ≥ 2^(k−2) − 1.
3. R113 PATH-RISE with R114 MOVE-RISE: that mover has at least 2^(k−2) + 1 maximal Ξ-paths. R119 ALT-MIN: both its Ξ-targets are movers with at least 2^(k−3) − 1 rises.
4. R107 MULTI-CHARGE: at least L/N − 1 steps move two or more movers. R108 LEVEL-PRODUCT: C_(l+1) + 1 ≤ (C_l + 1)(n_(l+1) + 1) level by level.
5. R124 EXACT-L: N5 from S3 on Γ3(G_k) makes exactly 2^k + 1 iterations, one fallback at iteration 2^k − 1. R122: σ̄ on the β-face at every state, and Howard needs at most N steps.

#### DONE / FINDINGS / NEEDS

DONE: all 55 titles R76–R130 read in full and classified; line numbers from `grep -n '^### R'` on the trunk copy (5d7aab0f). No repository edit, no commit, no push; one scratch file written (this one).

FINDINGS:
- No landed entry in R76–R130 contradicts EXP-IDEAL. One CHECK (R130's N5 bound on W-flat wrappers), expected clear because G_k has k + 1 W-levels.
- 17 entries are reductions that EXP-IDEAL now decides; R104, R117 and R124 are the transfer chain, and R124 gives the exact count 2^k + 1.
- Newly false: PIECE (R82), WRUN-POLY and its equivalents with FL-POLY, TIE-POLY, [P-INT], INT-LIN (R95), HX-POLY (R96), LIN-2 (R107); BIP-POLY probably.
- STATIC-DEPTH′-TIE (R82) is decided by one finite check of (H4′) on G_k's final state.
- Every polynomial bound on these genomes in R118–R129 is for Howard's rule or N5′-xi, so the kill is of N5's key rule only; R124 records that EXACT-L depends on [RULE].
- Strongest consistency tests on G_k: wires and level-0 movers move at most once (R111, R108).

NEEDS:
- Lead: the statements of PAIR-LIN, PM′_S, RENEW-COUNT (docs/new/P-IDEAL-KEYS.md l. 112, 164, 274) to fix their status; they are not in RESULTS.
- Lead: confirm three readings of mine: BIP-POLY's step (body L7555), the (H4′) translation for STATIC-DEPTH′-TIE, and that RISE-2D and LIN-2 were already contradicted by landed instances.
- Skipped: entry bodies were not read except the lines cited; entries before R76 were not examined.

## C. docs/GAPS.md (every row; line 11 item by item) and docs/NOW.md (reader sub-agent report, reproduced as returned; its «DONE / FINDINGS / NEEDS» lines are the reader's, not mine)
### Consequence map of EXP-IDEAL for docs/GAPS.md and docs/NOW.md (read-only; nothing edited, committed or pushed)

Line numbers: GAPS.md = trunk 5d7aab0f; NOW = trunk 6eaf4604 (copy NOW-6eaf4604.md; lines 22-25, 31, 32 differ from 5d7aab0f).
Every verdict assumes EXP-IDEAL is correct (it is unrefereed) and uses refereed-only R104 / R117 / R122 / R124 under the standing premise 1E-N3.
Facts read off GAPS l.11 and used below: (i) R104 REALIZE / R117 REACH3: the L(G)-step run is ONE FL run (no fallback, τ fixed, W fixed at every vertex, σ fixed off the movers, σ̄ on the β-face at every gate); (ii) R122 LAMBDA-CONST: λ_Ξ fixed on Ξ-acyclic genomes, so that run lies in one phase, one W-run, one τ-stretch, one piece; (iii) R124: τ never changes, exactly one fallback, N5 from S3 makes exactly L(G) + 3 iterations on Γ3(G) (so 2^k + 1 on Γ3(G_k)).
Dates in [brackets] are inferred (the UPDATE gives a time only). Names of the brief that do NOT occur in GAPS.md: O1, O1′, KEY-CYC, QUIET-KEY-1P, IDEAL-ACYC-POLY, HXS-POLY, SW-RUN, RUN-LIN′, TF-PH (Lemma TF is proved), ENUM-LOG, box 217; «NEST» occurs only as the A_DTL row G-NEST and as proved lemmas PULSE-NEST / GAP-NEST (R120); «K1-» only as the proved Theorem K1-TCYC (R129).

#### (A1) GAPS.md, every row

| l. | id | owner | status | verdict | reason |
| --- | --- | --- | --- | --- | --- |
| 6 | GAP-A | L-ALG (L-RED attacks) | open | `unaffected` | A_DTL search count; no N5 statement used |
| 7 | GAP-C | L-ALG (L-RED attacks) | open | `unaffected` | A_DTL completeness |
| 8 | G-S5-6 | L-ALG | open | `unaffected` | (ACYC) here is A_DTL's tangle-graph hypothesis of R4, not Ξ-acyclicity |
| 9 | G-NEST | L-RED; L-ALG successor if any | open | `unaffected` | (NEST*-BOUNDED) for A_DTL on 𝒞^1P |
| 10 | G-N1-LB | L-NEW (optional; not routed) | open | `unaffected` | lower bound for IncreasingDiscountPI (N1), another algorithm |
| 11 | G-N5-TIME | L-NEW (L-LIT T22; referees later) | open | `FALSE by EXP-IDEAL` | N5 from S3 makes ≥ 2^k − 1 (by R124 exactly 2^k + 1) iterations on Γ3(G_k), n = 135k − 230 |
| 16 | G-N5-TERM | L-NEW (L-COMP checks runs) | closed | `unaffected` | termination (R15) stands; EXP-IDEAL shows the running time itself, not only R15's bound, can be exponential |
| 17 | G1 | L-STRUCT | closed | `unaffected` | separator lower bound L4 |
| 19 | G-FDL | L-ALG | closed | `unaffected` | A_DTL |
| 20 | G-Bthr | L-ALG | closed | `unaffected` | A_DTL |
| 21 | G-K5 | L-ALG | closed | `unaffected` | A_DTL |
| 22 | G-STR | L-ALG (L-RED attacks) | closed | `unaffected` | A_DTL |
| 23 | G-DOM | L-ALG (L-RED attacks) | closed | `unaffected` | A_DTL |

No row is `moot` as a whole: every route to G-N5-TIME is recorded inside line 11.

#### (A2) GAPS.md line 11 (G-N5-TIME): named open items

| UPDATE | name | gloss | verdict: reason |
| --- | --- | --- | --- |
| base | K9 reading; PREMISE VJ00 Prop. 7.4 | iterations ≤ C·n³·(2 + σ̄-changes + τ̄-changes) | `moot`: route already CLOSED 2026-10-19; σ̄ and τ are constant on the FL part of the G_k run, so no N5-specific repair of this form exists |
| base (box 21) | (FO*), (FO_1O) | open core of Theorem B (frozen-τ run); its one-Odd-choice case | (FO*) `unclear`: not stated in the row (the G_k run has τ frozen); (FO_1O) `unaffected`: 𝒞^1O, closed by R51 |
| base (box 11); 2026-10-24 04:39Z; 2026-10-26 00:38Z-[10-26] 19:14Z | «OPEN for two-player games», «≥ 2 Odd choice vertices, the general case», «Beyond 𝒞^1O: OPEN (frontier 𝒞^(≥2E,≥2O))», «general games OPEN» | the iteration bound outside 𝒞^1O / 𝒞^1E | `FALSE by EXP-IDEAL`: Γ3(G_k) has many Even movers and many Odd gates |
| 2026-10-24 04:39Z to 2026-10-26 02:18Z (R18-R51) | (TRUST), (X) ≡ (Z), (NH'), ROI / W-CYC, (C), (J-poly) / J = O(n), (CL-S), (E), (K_W), S_o, K, X_SN, REL(S), (L1) = NJB / ENT / RISE-LAST / PF-THETA, OUT-POLY, θ_ph / ρ, N_HN, level −1 | per-phase counts on 𝒞^1O | `unaffected`: restricted class 𝒞^1O; all closed by R47 / R48 / R50 / R51 |
| [10-25] 17:35Z, 22:36Z; 2026-10-26 00:38Z | CONJECTURES FB-CAP (L-RED), INTO (L-SI) | DATA conjectures of the 𝒞^1O chain; FB-CAP «stays OPEN» | `unclear`: not stated in the row (𝒞^1O context suggests unaffected) |
| [10-26] 03:19Z | (H-OF), (H-N5) | hypotheses of MIRROR for 𝒞^1E | `unaffected`: 𝒞^1E bound proved in R57 |
| [10-26] 03:45Z, 07:47Z | Δ1, Δ-RT, ¬(h3_D) | frontier of the D-set factorisation (≥ 2 disagreement vertices) | `unclear`: structural, no statement in the row |
| [10-26] 04:15Z-07:25Z | ρ-POLY (CONJECTURE), N_late, N_ep, N_K | fallbacks per phase f ≤ 1 + (n−1)(2+ρ), f ≤ 1 + n·N_ep | `moot`: fallback counts; the G_k run has one fallback, so not decided |
| [10-26] 06:23Z | crossings and T per phase on 𝒞^2O | two Odd choice vertices | `moot`: restricted class, not decided |
| [10-26] 07:36Z-18:58Z (R64-R73) | (Στ); \|D_E\| ≥ 2 epochs (len(E)); X_SN^pre; f, f_in, X_dir, X_big; band, N_split, U(S); \|𝒞_f(P)\|; ROUTE_c, CYC_c, TOG_c; NCONF_{≥2}, R⁰_{≥2} | epoch and fallback-source counts per phase | (Στ) `unaffected` (audit strength, R65); «N_ep and len(E) both polynomial» `FALSE by EXP-IDEAL` (Σ_E len(E) ≥ 2^k − 2 in one phase, D ⊇ all gates); each single count `moot` / which factor fails `unclear` |
| 2026-10-28 22:22Z-23:48Z; 2026-10-29 00:08Z | G_c, G-intervals; EXIT_x, D; CONJECTURE UL_G; ABS-DEPTH-TIE_keep; E-ONEWAY after c | reductions inside one phase; abstract keep-rule model | `unclear`: statements not in the row; none gives a run bound alone (`moot` if only that use) |
| 2026-10-29 01:25Z | SW-LIN, RUN-LIN | linear switch / run-length conjectures | `unaffected`: already DEAD (lane DATA; RUN-LIN kill reproduced by REFEREE) |
| 2026-10-29 02:19Z; 2026-10-30 05:59Z | CONJECTURE FB-LIN; \|𝒞^K_f(P)\|; Σ_v WCH^S4a_P(v), ZF_P; READER-INV (one referee) | in-phase fallbacks per phase linear (GAP-RED reduction) | `moot`: bounds fallbacks only; G_k run has 1 fallback and W constant; its only use was the bound |
| 2026-10-29 05:46Z | CONJECTURE PIECE (unconditional) | unconditional form of \|piece\| ≤ (CF + 1)n − 1 | `unclear`: FALSE if it bounds every piece polynomially (the 2^k − 2 run is one piece); CF not defined in the row |
| 2026-10-29 06:35Z | CONJECTURE SEG-RUN (SEG = O(n)) | segment count of a run is linear | `unclear`: gives \|S\| ≤ SEG·n − 1 only under (H4′_rel), GEN_W |
| 2026-10-29 06:46Z-15:26Z | P-changes under a fixed top (P*, P*^U); carries NM, NM*, NM*^U | path-set changes / carries of one vertex per λ-run | `FALSE by EXP-IDEAL`: COMPOSE-RUN / COMPOSE-NM make T polynomial in them |
| 2026-10-29 19:07Z, 23:27Z | R*_T, FW-BF; R*_S, FL_S, ρ_S, NM^U on unprotected targets | late adoptions; σ-changing W-constant transitions per τ-stretch | FL_S polynomial `FALSE by EXP-IDEAL` (whole run is σ-changing, W-constant); R*_T, R*_S, ρ_S `moot`; FW-BF `unclear` (undefined) |
| 2026-10-30 05:17Z | B*, REP*, SC*, O* | CUT-POLY: T polynomial iff all four are | conjunction `FALSE by EXP-IDEAL`; B* ≤ 1 and O* = 0 on Γ3(G_k) (R124), so B*, O* `moot`; REP* or SC* is super-polynomial, which one `unclear` |
| 2026-10-30 09:03Z | GATE_F, CNW_F, GXC_F, WZ_F(z), REP′_F | reduction of the W-changing transitions of a W-run | `moot`: W never changes on the G_k run; not decided |
| 2026-10-30 11:51Z | [P-WCHτ](w) | ≤ w(n) S4a steps per τ-stretch change W(e) | `moot`: holds trivially on the G_k run (0 W-changes); gives no bound without TIE* |
| 2026-10-30 11:51Z | TIE* | tie switches (W unchanged) per W-run | `FALSE by EXP-IDEAL`: RUN-WCH forces TIE_F ≥ L(G_k) − m_E |
| 2026-10-30 11:51Z | NZ_P, ZFS_P, FBOS_P, NC_R, NT_R, ρ_P, B_R; VARIANT N5-LZC | residual fallback / re-entry counts; N5 with ties kept | counts `moot`; N5-LZC `unclear` (variant, «nothing transfers to N5») |
| 2026-10-30 18:40Z | FLATTR_P, FLATSW_P | phase length ≤ poly·(FLATTR_P + …) | polynomial `FALSE by EXP-IDEAL`: the run lies in one phase (facts i, ii) |
| 2026-10-30 22:14Z | WRUN-POLY, XI-CH-POLY, P*-POLY, DEEP_k-POLY | every W-run polynomial (equivalent forms, WRUN-EQ) | `FALSE by EXP-IDEAL`: the FL run is one W-run of length L(G_k) |
| 2026-10-30 22:14Z | FL-POLY, TIE-POLY, [P-INT]; INT-LIN | W-constant transitions / tie switches / W-constant intervals polynomial | first three `FALSE by EXP-IDEAL` (whole run W-constant); INT-LIN `unclear` (undefined; FALSE if it is linear [P-INT]) |
| 2026-10-30 22:14Z | R*-POLY, R3-POLY, SB-POLY, R°-POLY, ALT-POLY, FREE-POLY; BIP-POLY | conjuncts of WRUN-EQ | `moot`: necessary only (their WRUN-EQ conjunctions are FALSE); BIP-POLY `unclear` (undefined) |
| 2026-10-31 02:23Z | max SB_F, max CN_F, max HXU_F (HEAD-RED); XE, XO (T-XCH); CONJECTURES HX-POLY, CN-POLY, XCN-POLY | W-run / run polynomial iff these counts are | «all polynomial» `FALSE by EXP-IDEAL`; XE and max HXU_F are the failing ones (τ, σ̄ fixed; movers are not cycle nodes); the three conjecture names `unclear` (not defined in the row) |
| 2026-10-31 07:02Z | max_v HXS_F(v) polynomial (SRC-COUNT; «HXS-POLY» in NOW l.2) | Ξ-changes at sources per W-run | `FALSE by EXP-IDEAL`: equivalent to WRUN-POLY |
| 2026-10-31 23:12Z (R98, R99); 2026-11-01 02:21Z | prefix events, HC / HC_F; N_F, T1_F, TD_F, DESC_F; R_F, S_F, TS_F, R^old_F | relocations / equivalences for W-run length | N_F, T1_F, TS_F polynomial `FALSE by EXP-IDEAL` (≥ L W-constant transitions); TD_F, DESC_F, R_F, S_F, HC `moot` (W-change counts) |
| 2026-11-01 05:28Z | SG, BG; INC | run length ⇔ settle / bracket gap; τ-stretch ⇔ inconsistent transitions | each polynomial `FALSE by EXP-IDEAL` (stated equivalences) |
| [10-26] 05:50Z; 2026-11-01 10:09Z | standing premise 1E-N3; G-N5T-1 (code conformance DATA) | S1's procedure realises the optimum | `unaffected`; the N5 kill inherits this premise through R104 / R117 |
| 2026-11-02 00:24Z | FL / GCH (Corollary FL-GCH) | FL runs polynomial iff gating changes are | both `FALSE by EXP-IDEAL` |
| 2026-11-02 11:22Z | «every FL run … length at most p(n)» ⇒ L(G) ≤ p(3(N + M) + 6) (REAL-IDEAL); Ξ-cyclic genomes «not covered» | necessity statement; IDEAL-ACYC-POLY = O1 in NOW / the brief | both sides `FALSE by EXP-IDEAL` (already from R104's start pair on Γ(G_k)); Ξ-cyclic part `moot` for N5 |
| 2026-11-04 02:59Z | U (U-EQ), KF (KEYFLIP) | T polynomial iff unchained steps / key flips are | `FALSE by EXP-IDEAL` (G_k is Ξ-acyclic of degree 2) |
| 2026-11-04 07:54Z | READING «a polynomial bound on T must use the W-key rule» | T ≤ LP, LP exponential | `moot`: no polynomial bound on T exists |
| 2026-11-04 13:41Z | M₂ (M2-EQ), XF; CONJECTURE LIN-2 (T ≤ 2N) | multi-mover steps; linear bound | M₂ polynomial `FALSE by EXP-IDEAL`; LIN-2 `FALSE by EXP-IDEAL` if its scope is degree-≤-2 IDEAL-ACYC (2^k − 2 > 2(9k − 16) for k ≥ 7), scope not restated, else `unclear` |
| 2026-11-04 23:38Z; 2026-11-05 20:08Z | CONJECTURES SLOT-TRADE, FLIP-ADD; T*(d), T_k(m) | trade-off / external-flip model on 2-wide ladders 𝓛_d, ISO 𝓛^R_d | `moot`: 2-wide ladders only (G_k has up to 8 movers per level); not decided |
| 2026-11-06 07:16Z | PAIR-LIN, PM′_S, RENEW-COUNT | key-side lane conjectures «not claimed» | `unclear`: scope not in the row (PAIR-LIN is FALSE via PAIR-MOVES if it covers all degree-2 IDEAL-ACYC, `moot` if 𝓛^R_d only) |
| 2026-11-06 07:16Z; 2026-11-07 16:38Z, 21:05Z | TOWER (READING); FUEL-NEED, FUEL (i); «F(6) = 222 is a cap» / seventh capped level | doubling tower on 2-wide ladders 𝓛^R_d | `moot`: ladder tower not decided; its purpose (super-polynomial L on Ξ-acyclic genomes) is met by G_k |
| 2026-11-06 17:00Z; 2026-11-07 05:07Z | PAIR-LIN, DBL-O(1), «F(l) ≤ F(l − 1) + 1 for γ_l(0) ≠ γ_l(1)»; FLIP-ADD, SUM_1, T_k(3) (k ≥ 2) | flip counts on 𝓛^R_d / IM frame | `moot`: 2-wide (ISO) ladders only |
| 2026-11-06 21:57Z | max R(x, k) (RISE-EQUIV) | T polynomial iff option rises are | `FALSE by EXP-IDEAL` on IDEAL-ACYC |
| 2026-11-06 21:57Z; 2026-11-07 07:42Z | RISE-2D, MOVES-2D; μ(d), T^R(d) | ≤ 2d rises / moves on 𝓛^R_d | `moot`: 2-wide only; MOVES-2D is already DEAD (DE37, NOW l.2) |
| 2026-11-07 10:30Z | «whether long IDEAL-ACYC runs exist» (not claimed); «every FL run of N5 from S3 … at most p(n)» (REAL-IDEAL-S3) | necessity for N5 from its default start | answered by EXP-IDEAL: they exist, so the S3 hypothesis is `FALSE by EXP-IDEAL` |
| 2026-11-07 14:48Z; 2026-11-08 14:06Z | R («no bound on R is claimed (OPEN)»), R_σ, Q_τ; OVT-DV ([LOC]), CONJECTURE IN-BOUND, HYPOTHESIS [E-LEV] | Howard on IDEAL-CYC; N5′-xi | `unaffected`: Howard / N5′-xi (R bounded later by R129 ALL-TCYC) |
| 2026-11-08 20:27Z | «iterations after the first fallback», Ξ-cyclic R | N5′-xi beyond its mover phase | `unaffected`; ACYC-XI gives N5′-xi ≤ N + 1 to its first fallback on Γ3(G_k) |
| 2026-11-09 00:52Z; 2026-11-11 23:47Z; 2026-11-12 06:44Z | Σ_v D^tot_E(v) with U(G) unbounded (OPEN); Γ3 transfer of QUIET; max_g min(D^tot(e_g), D^tot(β_g)) at k = 1 (OPEN) | class counts for IDEAL-CYC / N5′-xi's T3 | `unaffected`: Howard / N5′-xi |
| 2026-11-09 09:04Z | F, T3, L(G) («it bounds none of F, T3, L(G) (OPEN)»); EXACT-L | N5 from S3 on Γ3(G): exactly L(G) + 3 iterations (acyclic G) | L(G) polynomial (O1) `FALSE by EXP-IDEAL`; F polynomial on every genome (O1′ / KEY-CYC of the brief) `FALSE by EXP-IDEAL` (F = L(G) + 1 on acyclic G); T3 `unaffected` |
| 2026-11-12 13:58Z; 2026-11-13 04:22Z | max Dhi_y(b, J) («the open core»), Rtop, A, C, A*_all, A*_route | T3 polynomial iff … on HOW3 | `unaffected`: N5′-xi mover phase |
| 2026-11-13 06:56Z | ALL-TCYC scope («nothing is proved on Γ3, for N5′-xi, for N5»); LAM-GAP / SHARP (lane) | Howard on IDEAL-CYC polynomial | `unaffected` |
| 2026-11-13 10:06Z | Statement XI-EXP (CONDITIONAL on WRAP, Claim NT); «N5 (SPEC) is not affected» | N5′-xi needs 2^Ω(√n) iterations | `unaffected`; the last sentence holds for WRAP only: N5 now has its own kill candidate |

#### (B) NOW.md at trunk 6eaf4604: lines EXP-IDEAL changes

ENUM-LOG, QUIET-KEY, O1, O1′, KEY-CYC do not occur in the 6eaf4604 copy (5d7aab0f l.25 had «box 217 QUIET-KEY-1P (… ENUM-LOG OPEN)»; now «SW-POLY exact target»). SW-POLY and 1P(G) are not defined in NOW; rows below say «if».

| l. | quote / gloss | what changes |
| --- | --- | --- |
| 2 | «FRONTIER: … RUN-LIN′ (O(n) per run) and FB-LIN (f ≤ n per phase …) OPEN» | RUN-LIN′ FALSE (fallback-free run of 2^k − 2 at n = 135k − 230); FB-LIN moot (one fallback on Γ3(G_k)) |
| 2 | «CONJECTURE SW-RUN (per fallback-free run) open (DATA ≤ 0.67n)» | FALSE |
| 2 | «R90 CUT (… G-N5-TIME ⇔ B*, REP*, SC*, O* polynomial; a REDUCTION …)» | both sides FALSE; REP* or SC* super-polynomial on Γ3(G_k) |
| 2 | «R91 GAP (… FB-LIN ⇐ per-vertex S4a W-changes ∧ Z-flat fallbacks …)»; «R93 WCH (… one premise [P-WCHτ](w) …)» | routes moot (they bound fallbacks / W-changes, not the W-constant run) |
| 2 | «WRUN-EQ (WRUN-POLY ⇔ XI-CH-POLY ⇔ …)»; «SRC-COUNT WRUN-POLY ⟺ HXS-POLY» | every member FALSE |
| 2 | «FL-GCH (FL-POLY ⟺ GCH-POLY)»; «REAL-IDEAL, FL-POLY ⇒ IDEAL-ACYC-POLY» | IDEAL-ACYC-POLY FALSE, hence FL-POLY and GCH-POLY FALSE |
| 2 | «D18 (owner 2026-10-24 13:04Z): "Focus on N5 and work toward proving it ..."; Lead reading L40: all lanes on N5 (G-N5-TIME, open)» | the statement to prove is false for N5 as specified; lane basis needs a new owner ruling |
| 2 | «Frontier OPEN (Lead reading): … the intrinsic target is transitions per phase = fallback-free run lengths (CONJECTURE SW-RUN) × fallbacks per phase … records ≈ 3n» | target FALSE: one phase holds a fallback-free run of 2^k − 2; «records ≈ 3n» superseded |
| 2 | «OPEN: general games; NO polynomial bound for N5 on general games is proved.» | becomes: none exists for N5 as specified (once EXP-IDEAL is signed); R51 / R57 subclass bounds stand |
| 11 | «M4 Target \| IN PROGRESS (N5 focus, D18/L40): candidate N5 SSI-GLOBAL; gauntlet step 4 (running time, G-N5-TIME) OPEN» | step 4 FAILS for N5 as specified, so N5 becomes a dead end under the gauntlet rule once refereed; M4 loses its focus candidate |
| 11 | «RESULTS R17-R130 … are partial step-4 lemmas for N5» | no longer a route to M4; they stay as structure / subclass results |
| 11 | «Two routes, complementary …: the tower route (R104/R117/R120; SEVEN capped levels: HIT7 F(6) = 254 at d 28 …) targets N5» | its goal (super-polynomial L on Ξ-acyclic genomes) is reached by G_k, not a 2-wide ladder; the ladder tower (HIT7, S(5,6,7)) is moot |
| 11 | «On every Ξ-acyclic genome, towers included, N5′-xi has R = 0 (… ACYC-LIN …)» | unchanged; it is now the separating fact (N5′-xi linear on G_k, N5 exponential) |
| 11 | «The N5′-xi upper-bound route (R118): P-N5-ASC … QUIET / UP-T … Its transfer to Γ3 … is NOT proved» | not changed by EXP-IDEAL (stale against GAPS l.11: R121-R129 landed, R130 XI-EXP is a conditional dead end for N5′-xi) |
| 11 | «Corollary EXACT-L (lane): N5 from S3 on acyclic Γ3 = L(G) + 3 exactly» | with EXP-IDEAL: exactly 2^k + 1 iterations on Γ3(G_k) (landed as R124) |
| 11 | «OPEN: unbounded U(G) (ω(1) upward climbs; L-SI LADDER-R build)» | N5′-xi-side item, not decided by EXP-IDEAL (U(G_k) not given) |
| 11 | «A_DTL route (older): step 4 open, lanes parked» | unaffected; then the only candidate without a kill claim (N5: EXP-IDEAL; N5′-xi: R130, conditional) |
| 22 | L-SI 55: «box 107 timing structure of full enumeration on 1P(G) (… ODOMETER, one bit per level …); proof side of SW-POLY» | if SW-POLY is box 217's polynomial target (O1), no proof side remains; reassign |
| 23 | L-RED 70: «R243 H5PLUS_L5 k 6 at N 41, single-mover additions saturate): R243 §2 pair-on-top construction» | construction superseded if k is the same parameter (G_k: every k at N = 9k − 16, k = 6 at N 38); role becomes attacking EXP-IDEAL |
| 24 | L-RED-B 5: «B6 attempt 2, first-principles family on 1P(G) or the failing step as a lemma» | a family now exists; role becomes an independent replay / attack of EXP-IDEAL |
| 25 | L-NEW 77: «box 217 at a143d406, SW-POLY exact target, T 340 at N 64, no k = 8): freeze packet P-N5-KEY1P (… REDUCTION …)» | «no k = 8» overtaken if k is the same parameter (G_8: N 56, L 254; G_9: N 65, L 510); packet target false, repurpose as the kill packet |
| 26 | L-COMP 22: «BOX 47 C port of one217.py PASS …; K-lane search for enumeration depth 8» | search superseded; the C port can replay G_k and Γ3(G_k) (N5 count against Oink) |
| 27 | L-LOWER 16: «L18b largest P = 15 …; then L19 SAT (exact T(N), min d per enumeration depth k)» | exact small-N maxima no longer bear on O1; moot unless kept as data |
| 28 | L-FORMAL 5: «Fuel statements proved …; NoFault Statement accepted (proof deferred); KeyRuleS4aStatement next» | Lean target should move to EXP-IDEAL (L(G_k) = 2^k − 2); fuel statements serve the moot ladder tower |
| 30 | REFEREE 34: «PARKED 03:31Z …; succ. 35 when needed» | needed now: EXP-IDEAL is unrefereed |
| 31 | REFEREE-2 41: «Addendum 3 (box 217 §6 + BRIDGE, §7), then any kill / proof claim, then the packet review» | EXP-IDEAL is the kill claim, first in its queue |
| 32 | CHECKER 25: «C146 Add. 2 on the landed R130 …, C147 = Fuel rows #75-#78» | add the landing gate for EXP-IDEAL (dead-end entry, GAPS l.11 status, statement diff) |
| 57-58 | «Dead approaches (with obstruction) … DE1 … DE2 …» | N5 SSI-GLOBAL joins once signed (obstruction and instance G_k) |
| 64 | «Algorithmic: no polynomial algorithm (M4) yet. Best results are R2 (T-A1) and R3 …» | unchanged in substance; EXP-IDEAL would be a new lower-bound result (classification: Lead / owner) |
| 68 | «No blocking owner questions open.» | EXP-IDEAL opens one: what replaces D18's N5 focus |

DONE: read-only consequence map of GAPS.md (5d7aab0f, all 13 rows; the whole 239,722-character line 11 read) and NOW.md (6eaf4604); no repository file touched; this text saved at ‹session scratchpad›/cmap_GAPS_NOW.md.
FINDINGS: (1) only GAPS row G-N5-TIME changes; the A_DTL rows and all closed rows are unaffected. (2) By the row's own equivalences EXP-IDEAL also falsifies WRUN-POLY and its WRUN-EQ forms, FL-POLY / GCH, TIE*, T1_F, SG / BG / INC, FLATTR_P, max HXS_F, XE, NM* / P*, and «B*, REP*, SC*, O* all polynomial» (B*, O* stay small, so REP* or SC* blows up). (3) Fallback-count routes (FB-LIN, ρ-POLY, N_ep), [P-WCHτ] and every 2-wide-ladder / tower conjecture are moot, not refuted. (4) Howard / IDEAL-CYC / N5′-xi items (R118, R121-R130) are unaffected. (5) Not decidable from the two files: (FO*), PIECE, SEG-RUN, UL_G, FB-CAP, INTO, FW-BF, BIP-POLY, INT-LIN, HX-POLY / CN-POLY / XCN-POLY, PAIR-LIN, PM′_S, RENEW-COUNT, N5-LZC, and the meaning of SW-POLY / 1P(G) / «k» in the NOW roster.
NEEDS: Lead: confirm that SW-POLY (NOW l.22, l.25) is O1 and that the roster's enumeration depth k is EXP-IDEAL's k before rows 22-27 are rewritten. Owner: a ruling on D18's N5 focus once EXP-IDEAL has two referee signatures.

## D. Named statements of the lane boxes 209-218 and of P-N5-KEY1P (reader sub-agent report, reproduced as returned; its «DONE / FINDINGS / NEEDS» lines are the reader's, not mine)
### Named statements in boxes 209-218 and P-N5-KEY1P against EXP-IDEAL

Read-only pass over the ten lane documents in docs/new/ (branch claude/l-new, working tree at 2026-11-13 13:52Z). Nothing in the repository was edited.

**Conventions**
- File tags: 209 = N5-LEVEL3-box209.md, 210 = N5-GENLEVEL-box210.md, 212 = N5-RFLEVEL-box212.md, 213 = N5-KEYWIN-box213.md, 214 = N5-LIFT-box214.md, 215 = N5-KEYSIDE-box215.md, 216 = N5-VALUESIDE-box216.md, 217 = N5-QUIETKEY-box217.md, P = P-N5-KEY1P.md, 218 = N5-BITLADDER-box218.md.
- Line numbers are from `grep -n` / `cat -n` on the working tree.
- Box 218 changed while I was reading (mtime 13:49Z, untracked, now 112 lines). It no longer has FILL_ placeholders: the DATA is filled in and a header says the box is DROPPED because of G_k. Its line numbers below are for that version.
- Every verdict assumes EXP-IDEAL survives refereeing.
- Verdict rule used: «PROVED (lane)», landed quotes and dead-end records that stay valid are `unaffected-true`; CANDIDATE / CONDITIONAL / READING / CONJECTURE statements the family does not decide are `unaffected-open`.
- «(inference)» marks a consequence I derived from the stated EXP-IDEAL facts plus a lemma of these documents; it is not in the documents and was not run.
- In table cells `\|K(x)\|` is the document's |K(x)|.

#### Table

| box / file | line number | name | label in the document | what it says in ≤ 18 words | verdict | reason in one line |
| --- | --- | --- | --- | --- | --- | --- |
| all ten | 209: 5, 344, 360, 381; 210: 8; 212: 10, 268, 336; 213: 8, 171; 214: 1; 215: 79; 216: 8; 217: 1; P: 12, 321; 218: 12, 112 | G-N5-TIME | «stays OPEN» | N5 makes polynomially many iterations on every parity game. | FALSE by EXP-IDEAL | KILL-TRANSFER (P l.132): N5 from S3 on Γ3(G_k) makes at least 2^k − 1 (measured 2^k + 1) iterations on 135k − 230 vertices. |
| 209 | 95-124 | (K0′) CORE, (K2′) COARSE, (K1′) MONOTONE, (K3′) ALONG THE PLAY, (K4′) GATES, (K5′) DOM AT CLASS LEVEL | CANDIDATE (l.6: «every statement of this box is a CANDIDATE») | Five class facts for classes (Λ, e-set) on HOW3(G); classes never fall. | unaffected-open | Only HOW3 / N5′-xi; (K0′)-(K4′) are static and are what RF-D's [L3] borrows for N5. |
| 209 | 19, 128-139 | Lemma LEVEL3 (L1′)-(L5′) | CANDIDATE | Φ_t (lowest lagging class, −front size) never falls on HOW3(G); at most P3 values. | unaffected-open | Only Howard / N5′-xi. |
| 209 | 22, 177-180 | Lemma PLATEAU3 (i), (ii) | CANDIDATE | A plateau of constant Φ, and the tail, has at most n_E3 = N+6M+9 steps. | unaffected-open | Howard only (uses DOM and BR-SEG-G). |
| 209 | 24, 231 | Theorem T3-ALL | CANDIDATE | T3 ≤ P3·(n_E3 + 1) + n_E3 for every genome; degree 3 in N + M. | unaffected-open | A «T ≤ poly» for Howard's run only; no conflict with G_k (Howard takes about 4 steps there). |
| 209 | 25, 236, 365 | Corollary N5XI-G3 | CANDIDATE | N5′-xi from S3 on Γ3(G) makes exactly T3 + 3 ≤ poly iterations. | unaffected-open | About N5′-xi only (scope line l.4-5: «Not N5»). |
| 209 | 28, 240 | Corollary FLIPS3 | CANDIDATE | On HOW3(G) σ̄-changes, class changes and D^tot_E(v) − 1 are at most T3. | unaffected-open | Howard only. |
| 209 | 26-27, 30, 244, 329-334 | HYPOTHESIS [E-LEV]; CONJECTURES DEEP3, DEEP3-G, DEEP3-all, MOVER-DEEP3; U-FREE; SCC-LIN (L-SI's, cited) | HYPOTHESIS / CONJECTURE | L-SI's conjectured routes to polynomial T3 (U-FREE: T3 ≤ N + M + 4). | unaffected-open | All about T3 (Howard / N5′-xi). |
| 209 | 322-323 | R118 (l) Corollary T3 (quoted) | landed, quoted | N5′-xi's FL run on Γ3(G) is polynomial iff R is polynomial along Howard runs. | unaffected-true | Landed «polynomial iff», about N5′-xi only. |
| 209 | 335-337 | sentence «No landed statement gives a lower bound on T3 above linear … no super-polynomial family. None found.» | contradiction check | No lower bound on T3 above linear is known. | unaffected-true | Speaks of T3 (Howard) only; still accurate after G_k. |
| 210 | 22, 27, 31, 74-138 | Lemma G-CLASS (G-K1)-(G-K5); Lemma GEN-LEVEL (GL1), (GL3)-(GL5); Lemma GEN-PLATEAU (GP1)-(GP4) | CANDIDATE | Class facts and level potential hold on every Howard run of split-form games; at most 2·\|P\|·n non-stall steps. | unaffected-open | Howard on split-form games only; scope l.6-8 excludes N5 and N5′-xi. |
| 210 | 34, 139-142 | Hypothesis (OF); Theorem OF | CANDIDATE, CONDITIONAL on (OF) | If Odd's reply is constant on plateaus and the tail, T ≤ 2·\|P\|·n·(n_E + 1) + n_E. | unaffected-open | Conditional «T ≤ poly» for Howard only; (OF) fails on the known exponential Howard families (l.40). |
| 210 | 311-315, 334-337 | §8 «N5 itself» | READING + DATA (relabelled, Addendum A1 (3)) | (G-K1)-(G-K4), (GL1), (GL3) hold along N5's σ-sequence on split-form games; (G-K5), (GL4) do not. | unaffected-open | Structure without a bound; Γ3(G_k) is not in split form (209 l.375-377). |
| 212 | 13-16, 70-113 | (a) the per-lemma reading | READING | R123 / R125 static lemmas hold at every (standard) state, not only on Howard's run. | unaffected-open | Reading of landed proofs; no bound. |
| 212 | 17-21, 115-125, 308-313 | RF-A (i)-(iv), K5-NEW | CANDIDATE («Lean-checked (lane)») | Any improving run of IDEAL-CYC(G): class facts hold; at most P = 2M(N + 2M) non-stall steps. | unaffected-open | Bounds non-stall steps, not T; on G_k nothing lags (G-2), so it counts nothing. Its N5 use (RF-D) is moot. |
| 212 | 22-25, 149-157 | RF-B (P1), (P2), (P4), (P5′) | CANDIDATE | A plateau's set Y is closed and class-frozen; steps are identity or improving steps of H_Y. | unaffected-open | Structure only; on G_k the only window is the tail with Y = V. |
| 212 | 26-29, 168-172, 274-277 | RF-C | CANDIDATE | T ≤ P + (P + 1)·W; approved form T ≤ (P + 1)(λ* + 1) + tail. | moot | Decomposition whose N5 purpose was O1′ through RF-D; on G_k W = T_key. |
| 212 | 30-35, 180-197, 320-326, 336 | RF-D | CONDITIONAL on [IMP3] and [L3]; window clause WITHDRAWN (l.320) | T_key(G) ≤ P3 + (P3 + 1)·W_key(G); O1′ holds iff W_key(G) ≤ poly(N + M). | moot | Route to O1′ (KEY-CYC), now false; the «iff» stays true with both sides false (W_key(G_k) = T_key by G-2). |
| 212 | 62-66, 181-188 | [IMP3], [L3]; W-FLAT (box 104, L-SI) | hypotheses of RF-D; W-FLAT «lane, PROVED there, not refereed» | N5's pre-fallback steps on Γ3 are improving steps at movers through standard states. | unaffected-open | Not decided by G_k; on Ξ-acyclic genomes landed R117 REACH3 already gives the run. |
| 212 (also 215, 216, 217) | 212: 1, 34, 65-66, 193, 323-325; 215: 52; 216: 5, 103, 115, 164, 171; 217: 52 | O1′ (KEY-CYC) | OPEN (212 l.35: «an OPEN question») | F(G) ≤ poly(N + M) for every R104 genome, F N5's first fallback on Γ3(G). | FALSE by EXP-IDEAL | Contains the Ξ-acyclic case: F(G_k) = 2^k − 1 with N + M = 27k − 48. |
| 212, 213, 215, 216, 217 | 212: 38, 195-196, 334; 213: 26, 129; 215: 53; 216: 118; 217: 45-48, 52, 233 | O1 | OPEN (213 l.26: «O1 is OPEN») | The Ξ-acyclic case: N5's key run before its first fallback is polynomial. | FALSE by EXP-IDEAL | T_key(G_k) = L(G_k) = 2^k − 2. |
| 212 Add. B; 213 | 212: 320-329; 213: 12-17, 55-81 | G-1; (P2^τ); repair (a) | WITHDRAWN (212); false where tested, DATA (213) | Windows are not SPEC key-rule runs on a closed one-player sub-game; «τ(g) ∈ Y» fails. | unaffected-true | Dead end stays; vacuous on G_k (Y = V). |
| 212 | 202-203 | sentence «the difficulty of O1′ sits where RF-D puts it» | DATA remark | Long key-rule runs live inside one class-frozen window. | unaffected-true | Borne out: G_k's whole exponential run is one window. |
| 213 | 18-26, 83-90, 163-164 | KEY-TAU (i), (ii) | CANDIDATE (consolidation of landed lemmas) | N5 moves each mover to the least root-first-key option of A_t(x); own key μ_t(x) never rises. | unaffected-open | New only for Ξ-cyclic genomes and other numberings; on Ξ-acyclic G_k it is landed (P l.305-307). Not needed by the kill. |
| 213 | 90-91, 107-110 | KEY-TAU (iii) | CANDIDATE («not a polynomial bound», l.109) | Each mover switches at most \|K(x)\| − 1 times; T_key ≤ Σ_x (\|K(x)\| − 1). | unaffected-open | Exponential ceiling only; G_k stays below it. |
| 213 (also 212) | 213: 27-29, 118-128; 212: 333-335 | G-2 | PROVED-lane | Ξ-acyclic G: every class is constant on N5's pre-fallback run; one window, Y = V. | unaffected-true | The kill packet can USE it: G_k's run is one class-frozen, all-quiet window, so RF-C, RF-D and LOUD-RF give nothing. |
| 213 | 169 | sentence «T_key may be exponential (towers)» | not-claimed line | Leaves open that T_key is exponential. | unaffected-true | Borne out by G_k. |
| 214 | 7-9 | «The decisive question» | restated Lead question | A family where one mover switches 2^k − 1 times before the first fallback makes N5 exponential. | unaffected-true | Sufficient form only; G_k reaches the conclusion with 2^(k−2) switches. R124 EXACT-L's L + 3 = 2^k + 1 matches the measured count. |
| 214 | 11-23, 25-38 | prior tower-lift record; «block lifting» route | READING + DATA, negative result | H5, H6, HIT7 share no repeating block; no lift kept F(l) doubling beyond k = 7. | unaffected-true | Dead end on 2-wide ladder towers; G_k is rule-built off the ladder, so l.23 is outdated as a status line only. |
| 214 | 15-16 | L-LOWER uniform level templates | CANDIDATE-DEAD (cited) | Uniform level templates (d 6-12): «never two consecutive doubling levels». | unaffected-true | Ladder dead end; whether its reading «a working rule must be non-uniform in the level» fits G_k cannot be told from these texts. |
| 214 | 16 | CONJECTURE L5-TYPE | CONJECTURE (L-LOWER's; «open, no construction») | Only «O(h) added movers» is given here. | unclear | The statement is not spelled out in these documents. |
| 215 | 14-17 | [M] | CONDITIONAL (= KEY-TAU (i)) | s_(t+1)(x) is the least-key option of A_t(x) under the new state. | unaffected-open | As KEY-TAU (i). |
| 215 | 1, 22-32, 41-46, 90-96 | KEYSIDE-ALL: LOCAL-KP (a), (b); PAIR-KF (a), (b); PAIR-MOVES; CASCADE (a), (b); F ≤ T | CONDITIONAL on KEY-TAU (i); gate-key form «depends on numbering (R241)», e-index form restated l.90 | R111's key-side lemmas hold for N5 on Γ3(G) of every genome, Ξ-cycles included. | unaffected-open | New only for Ξ-cyclic genomes; claims no bound (l.53, 78). Its use as a route to O1′ is moot. |
| 215 | 36-40, 91 | KEYFLIP′ | CONDITIONAL on [M] | A degree-2 mover that moves takes its key-least option; moves(x) ≤ 1 + KF_x. | unaffected-open | Same; on G_k (landed form) it forces KF_x ≥ 2^(k−2) − 1 for the busiest mover (inference; a check, not a conflict). |
| 215 | 47-50 | LADDER | CONDITIONAL | On 𝓛^R_d with any Ξ-targets, F(l) ≤ 2 + 3F(l − 1) ≤ 3^(l+1) − 1. | unaffected-open | Only 2-wide ladders, and an exponential ceiling; G_k is not a ladder. |
| 215 | 55-60 | MERGE, RETURN (RETURN-COUNT), RENEW | «Not transferred» (record) | These value-side lemmas need ENC or acyclic chains and are not carried to Ξ-cyclic genomes. | unaffected-true | Record stays. |
| 215 | 51-53 | sentence «So O1′'s difficulty is on the value side …, as for O1.» | remark | Locates the open difficulty of O1′ and O1 on the value side. | moot | O1 and O1′ are false; no bound is left to locate. |
| 216 | 21-81 | V1 table (RF / HOW verdicts); (V1-a), (V1-b); «STRICT is RF» | READING; CONDITIONAL on [IMP3]; STRICT re-proof PROVED lane | RF-marked landed lemmas hold along N5's key run on Γ3; Howard-only items are listed. | unaffected-open | Reading and conditional structure, no bound; G_k decides none of it. |
| 216 | 82-85 | (V1-c) SAME-SUFFIX-IMP | PROVED lane | On a SAME-SUFFIX window an Even mover changes at most deg(o) − 1 times. | unaffected-true | Local structure. |
| 216 | 86, 98-104 | (V1-d) LOUD-RF (a), (b) | PROVED lane given the V1 table; CONDITIONAL on [IMP3] and [E-LEV] | Q ≤ n3·((2M + 3)·F′_(U(G))(M) − 1) and T_key ≤ Q + (Q + 1)·Wq. | moot | Route to O1′ for U(G) ≤ B through a bound on Wq; on G_k Q = 0 and Wq = T_key (by G-2). |
| 216 | 112-115 | QUIET-RF | OPEN | A polynomial bounds every improving run on a quiet sub-window with G_C, faces and boundary constant. | FALSE by EXP-IDEAL | N5's key run on Γ3(G_k) is one such window of 2^k − 2 steps (G-2, BETA-ACYC); the document draws this implication at l.118-120. To confirm on G_k: Q = 0, no gate flip. |
| 216 | 116 | QUIET-KEY | OPEN | The same bound for N5's key run only. | FALSE by EXP-IDEAL | Same window; its Ξ-acyclic one-player form is QUIET-KEY-1P (217 l.44-47). |
| 216 | 122-136 | V2 XFLIP | PROVED (lane) | N5 on every game: moves(x) ≤ 1 + XF_x at degree 2, (d−1)(1+OC_x) generally. | unaffected-true | The kill packet can USE it as a check: G_k's busiest mover has XF_x ≥ 2^(k−2) − 1. |
| 216 | 157-161 | JOINT | PROVED lane, CONDITIONAL on KEY-TAU (i) | moves(x) ≤ 1 + JF_x and JF_x ≤ min(KF_x, XF_x). | unaffected-true | Structural; on Ξ-acyclic genomes its condition is the landed IDEAL step. |
| 216 | 153, 162-165, 171 | V3 JOINT-POLY | OPEN (REFORMULATION, «not progress») | Σ_x JF_x ≤ poly(N + M) on N5's key run for every genome of degree ≤ 2. | FALSE by EXP-IDEAL | G_k has degree 2 and T_key ≤ 2N + Σ_x JF_x (l.163), so Σ JF ≥ 2^k − 2 − 2N; kill criterion V3 (l.171). |
| 216 | 103, 115, 164 | sentences «O1′ … holds IF Wq is polynomial»; «QUIET-RF gives … O1′»; «JOINT-POLY ⟺ O1′ at degree ≤ 2» | conditional / «⟺» | Each ties O1′ to a polynomial bound on Wq, sub-windows or Σ JF. | moot | The implications stand; every polynomial side falls with O1′. |
| 216 | 118-120 | sentence «an exponential tower family … would refute QUIET-KEY and QUIET-RF at once, and with them this route» | READING | An exponential Ξ-acyclic family kills QUIET-KEY, QUIET-RF and the route. | unaffected-true | Borne out by G_k (Ξ-acyclic, though not a ladder tower). |
| 216 | 208-210, 226-227 | sentences «QUIET3's bound L3 is not violated by N5 on these 88»; towers: Howard ≤ 12 steps, N5 up to 299 | DATA | N5's quiet windows stay below Howard's bound L3 on 88 frozen genomes. | unaffected-true | DATA on fixed instances; G_k repeats the contrast (Howard about 4, N5 2^k − 2). 2^k − 2 passes L3 only near k = 27 (inference, my arithmetic). |
| 217 | 37-42 | REDUCTION | PROVED lane, CONDITIONAL on KEY-TAU (i) and [IMP3] | For Ξ-acyclic G, N5's pre-fallback run on Γ3(G) is 1P(G)'s key run. | unaffected-true | Superseded by the unconditional RED-1P; the kill packet should cite RED-1P. |
| 217; P; 218 | 217: 43-47; P: 26, 66, 138-139, 227; 218: 1 | QUIET-KEY-1P (= R117's IDEAL-ACYC-POLY = «O1») | OPEN (P: «OPEN; not claimed») | T_key(G) ≤ p(N + M) for every Ξ-acyclic genome G. | FALSE by EXP-IDEAL | Direct: T_key(G_k) = 2^k − 2 with N + M = 27k − 48. |
| 217 | 50-52 | Kill criterion | criterion | A Ξ-acyclic family with super-polynomial T_key(1P) kills QUIET-KEY-1P, hence O1 and O1′. | unaffected-true | This is EXP-IDEAL's logic; «(the towers become a family)» did not happen (G_k is no tower). |
| 217; P | 217: 75-81, 148-155; P: 163-165 | A1 MONO-1P | PROVED lane / PROVED | Own key never rises, own Ξ-value never falls; both strict at a switch. | unaffected-true | Holds on G_k. |
| 217; P | 217: 82-85, 156-159; P: 176-180 | A2 SWITCH-BOUND | PROVED lane / PROVED | sw(x) ≤ min(\|K(x)\|, \|PΞ(x)\|) − 1; max sw ≤ T_key ≤ Σ_x sw(x). | unaffected-true | USE as a check: G_k's busiest mover x* needs lev(x*) ≥ k − 2 and hΞ(x*) ≥ k − 2 (inference). |
| 217; P | 217: 83-84, 160-162; P: 181-184 | Corollary A2-POLY | PROVED (N5 form via BOUND-TRANSFER) | T_key ≤ D·N^(1 + c·log2 D) if every mover has min(lev, hΞ) ≤ c·log2 N. | unaffected-true | A «T ≤ poly» on a class G_k lies outside (previous row); «needs movers … deep in BOTH graphs» stays true. |
| 217; P | 217: 86-88, 163-168; P: 187-194 | A3 PAIR-1P (i), (ii) | PROVED lane / PROVED | A degree-2 mover whose options share a W-target or a Ξ-target switches at most once. | unaffected-true | USE: G_k's «wires» switch at most once, so its busy movers have two W-targets and two Ξ-targets. |
| 217; P | 217: 89-92, 169-175; P: 197-208 | A4 HEREDITY (i)-(iii) | PROVED lane / PROVED | If sw(x) = \|K(x)\| − 1, x's W-targets enumerate too and XF_x ≥ \|K(x)\| − 2. | unaffected-true | Its hypothesis never holds above level 0 on G_k (k = 1); only «sw(x) ≤ 1 + XF_x» applies. |
| 217 | 93-98 | A5 TIGHTNESS | DATA, not a proof | On the towers the bottom 6-7 levels enumerate fully, fuelled by about 3k upper levels. | unaffected-true | DATA on five towers; not the mechanism of G_k. |
| 217 | 99-105 | A6 WHERE A POLYNOMIAL ARGUMENT FAILS | lane text; CORRECTED l.103-104; two sentences WITHDRAWN (P l.229-231) | Polynomial iff k(G) = O(log N); a super-polynomial family «=» one with k(G) ≥ c·d^ε. | FALSE by EXP-IDEAL | The ⇐ direction and the «=»: k(G_k) = 1 with T_key = 2^k − 2. The ⇒ direction survives as ENUM-NEC. |
| 217 | 106-118 | A6′ CORRECTION | correction (content PROVED in P §9) | QUIET-KEY-1P ⟺ SW-POLY; ENUM-LOG is necessary only; k_c defined; DBL4 is a HALF enumeration. | unaffected-true | Stays; G_k turns «converse not proved» into «converse false» at c = 1. |
| 217; P | 217: 116, 121, 181, 192, 207; P: 1, 218 | ENUM-LOG | necessary condition (217: k = k_1; P: k_c for every c) | Enumeration depth is O(log): k(G), or k_c(G) = O((1/c)·log(N + M)). | unaffected-open | Only necessary; at c = 1 G_k decides nothing (k = 1). For fixed c < 1 see note N2 (inference: k_c(G_k) ≥ k − 1). |
| 217 | 183-188 | A7 FLIP-SUPPLY | PROVED lane | XF_x ≤ Σ_(z ∈ Ξdesc(x)) sw(z), so sw(x) ≤ 1 + Σ_(z ∈ Ξdesc(x)) sw(z). | unaffected-true | USE as a check on G_k's busiest mover. |
| 217 | 119-122, 189-193, 204-207 | A7′ «COUNTING CANNOT PROVE ENUM-LOG»; the «timing form» | PROVED lane (A7′); «Not yet stated as a lemma» | Counting switches cannot bound k(G); an ENUM-LOG proof needs timing and order of flips. | moot | A route to ENUM-LOG, which was a step toward QUIET-KEY-1P and is only necessary. |
| 217 | 200-203 | «The naive self-fuelling shape DIES» | DATA (dead end) | Ξ = W ladders: T = d, k = 1, no mover switches more than twice. | unaffected-true | Ladder dead end. |
| 217 | 202 | CONJECTURE XTW-2 | CONJECTURE (untested beyond this) | On Ξ = W ladders every mover switches at most twice. | unaffected-open | Only about 2-wide ladders with Ξ-target = W-target. |
| 217 | 214-226 | Lemma BRIDGE | PROVED lane | At standard states of Γ3(G), G Ξ-acyclic, the Ξσ-order of a mover's pads is 1P's order. | unaffected-true | Redundant for the kill: the packet cites landed KEY3 (a) of R117 instead (P l.281-284). |
| 217 | 233-236 | «= O1», corrected | correction | Equality of 1P with R104's IDEAL model was not proved in box 217. | unaffected-true | Closed by Lemma IDEAL-1P (P §2). |
| 217 | 102 | sentence «The towers say the opposite trend so far … about three or four fuel levels per enumerated level.» | A6 text | Towers suggest full enumeration is cheap, so a kill rather than a bound. | unaffected-true | Right about the direction, wrong about the mechanism: G_k is exponential with k = 1, not by deeper full enumeration. |
| P | 18, 99-103 | Lemma IDEAL-1P | PROVED (L-NEW, unrefereed) | 1P(G) is R104's IDEAL model on Ξ-acyclic G; T_key(G) = L(G). | unaffected-true | The kill packet can USE it: L(G_k) = T_key(G_k). |
| P | 19, 120-131, 308-310 | Theorem RED-1P (a)-(c) | COROLLARY of landed R117 REACH3 | N5 from S3 on Γ3(G) follows 1P's key run; first fallback is transition T_key + 1. | unaffected-true | USE: the reduction that carries G_k to N5 (first fallback 2^k − 1, as measured). It needs R117's vertex indices. |
| P | 19, 132-134 | Corollary KILL-TRANSFER | COROLLARY (= R117 REAL-IDEAL-S3 (b)) | Super-polynomial T_key on Ξ-acyclic genomes gives at least T_key + 1 N5 iterations on Γ3. | unaffected-true | USE: the transfer step; n = N + 7M + 10 = 135k − 230 for G_k. |
| P | 19, 135-137 | Corollary BOUND-TRANSFER | COROLLARY | T_key(G) ≤ p(N + M) puts N5's first fallback by transition p(N + M) + 1. | moot | It existed to carry a polynomial bound on 1P(G) to N5; there is none. |
| P (also 217) | P: 20, 141-147; 217: 141-147 | Lemma 0 (a)-(c) | PROVED | Options have distinct keys and values; \|K(x)\| ≤ D^(lev(x)+1), \|PΞ(x)\| ≤ D^(hΞ(x)+1). | unaffected-true | USE: \|K(x)\| = 2^(lev(x)+1) on G_k (all degrees 2). |
| P; 217 | P: 25, 211-213, 227; 217: 112, 117 | SW-POLY | OPEN (P l.227); «QUIET-KEY-1P ⟺ SW-POLY» PROVED | sw(x) ≤ q(N + M) for every mover of every Ξ-acyclic genome. | FALSE by EXP-IDEAL | One mover of G_k switches 2^(k−2) times; the equivalence itself stands. |
| P | 25, 217-220 | ENUM-NEC | PROVED (every mover of degree ≥ 2) | T_key ≤ P implies k_c(G) ≤ (1/c)·log2(P + 1) for every 0 < c ≤ 1. | unaffected-true | An implication; its kill form T_key ≥ 2^(c·k_c) − 1 agrees with G_k. |
| P | 26, 227-229 | the converse of ENUM-NEC | OPEN (not claimed) | k_c(G) = O(log(N + M)) for every c would give QUIET-KEY-1P. | moot | A sufficient condition for a statement now false; read at c = 1 alone it is refuted (k(G_k) = 1). |
| P | 223-226 | Kill form (by SW-POLY, not by k) | part of §9 (PROVED) | A Ξ-acyclic family with super-polynomial max sw refutes QUIET-KEY-1P; KILL-TRANSFER applies. | unaffected-true | USE: G_k meets it; «k and k_c are diagnostics …, not its definition» fits the half-rate fact. |
| P | 229-231, 280 | withdrawals of box 217's two sentences | WITHDRAWN | The equivalence with k(G) = O(log N) and «must prove k(G) = O(log N)» are withdrawn. | unaffected-true | The withdrawal stands; see the half-rate list. |
| P | 221-222, 298-304 | LIFT(G, D) | REMARK / DATA (REFEREE-2 41's family) | A degree-1 chain under G raises k by D at constant T_key. | unaffected-true | Why k and k_c need all degrees ≥ 2; G_k has M = 2N. |
| P | 6, 275-284 | KEY3 (a), KEY3 (b) | landed (R117's packet, signed), cited | S4a's arena options at a mover are 1P's A_s(x); e-indices follow gate indices. | unaffected-true | USE: the value bridge inside RED-1P. No KEY2, KEY4 or KEY5 occurs in these ten documents. |
| P | 4, 12, 317 | sentences «on the critical path of BOTH outcomes»; «asserts nothing about whether long key runs exist»; «no super-polynomial family» | header / not-claimed lines | The packet serves a kill or a bound and claims neither. | unaffected-true | The kill branch is the one taken; the last two are status lines now outdated. |
| 218 | 6-9 | DROPPED | DROPPED on the Lead's word (13:49Z) | Box and the k ≤ d/2 question dropped: G_k kills QUIET-KEY-1P without ladders. | unaffected-true | The document already cites EXP-IDEAL (P-N5-EXP) as its reason. |
| 218 | 17-19, 38-60 | «No landed lemma forbids k = d/2 on upward ladders» | READING | Landed ladder results give only k ≤ (d + 1)/2 and T_key < 2^(⌈d/2⌉ + 3). | unaffected-true | Only upward 2-wide ladders. |
| 218 | 20-23, 63-66 | UP-CEIL | PROVED lane | Upward genome: sw(x) ≤ D^(min(lev(x)+1, d−lev(x))) − 1; upward ladder: k ≤ (d+1)/2. | unaffected-true | Only upward genomes. Check (inference): for k ≥ 5 G_k cannot be upward, or UP-CEIL fails. |
| 218 | 24-27, 67-74 | CEIL-SHAPE (i)-(iv) | PROVED lane, counting only | A full mover on an upward ladder forces its Ξ-targets' levels and a complete upper block. | unaffected-true | Needs a FULL mover on a 2-wide upward ladder; says nothing about G_k. |
| 218 | 32-34 | «parity obstruction» | WITHDRAWN | Obstruction to two consecutive fully enumerating levels on nearest-level upward ladders; argument withdrawn. | moot | Withdrawn in the text; it aimed at bounding full enumeration on ladders, which no longer bears on G-N5-TIME (l.6-9). |
| 218 | 34-35 | BI-LADDER | DEAD (L-SI's exact SAT; own climbs) | Both Ξ-targets on the pair one level up: longest runs 2, 3, 6, 8, 11 (d = 2..6). | unaffected-true | Ladder-class dead end at the sizes measured. |
| 218 | 1, 28-29, 94-95, 104-106 | templates «two options on the two movers of ONE pair» | DEAD (DATA, climbs; «search, not exact») | PURE, mirror, mirror1, mid, up2, down: k = 1 in all 28 runs (d = 4, 6). | unaffected-true | Ladder templates, dead «only as far as these climbs … go» (l.109). |
| 218 | 78-79 | CONJECTURE k ≤ d/2 on every upward ladder | CONJECTURE (untested beyond d ≤ 6) | Full-enumeration depth k ≤ d/2 on every upward ladder. | unaffected-open | Only upward ladders and full enumeration (k_1); G_k is neither; dropped as a route. |
| 218 | 22-23 | sentence «Upward ladders are exponential in d only if the ceiling is reached up to an additive constant» | under item 2 (PROVED lane) | Exponential runs on upward ladders need the full-enumeration ceiling. | unclear | UP-CEIL's proof (l.63-66) does not show this if «ceiling» means k; see half-rate item H9. |

Not found in these ten documents: a sentence of the form «a family … is the more likely outcome» (the only «more likely» is the owner's D1 quote, 209 l.8 and 210 l.10), and any name KEY2, KEY4 or KEY5.

#### Half-rate list

Sentences that assert or suggest that a super-polynomial run needs full enumeration (large k(G)), or equate a polynomial bound with ENUM-LOG.

| # | file, line | sentence | already withdrawn in the documents? |
| --- | --- | --- | --- |
| H1 | 217 l.99-101 | «A2 is tight at k …, so any polynomial bound must prove k(G) = O(log N), i.e. that full enumeration over k levels costs 2^Ω(k) fuel levels (or movers).» | Yes: P l.229-231 withdraws it, but for another reason (degree-1 movers, LIFT). As a bare necessity it is ENUM-NEC and true at degree ≥ 2; what G_k shows is that it is not the crux. |
| H2 | 217 l.103-104 | earlier text «claimed «QUIET-KEY-1P ⟺ k(G) = O(log N)» (wrong direction: only ⇒ is proved)» | Yes: 217 l.103-104 and l.115-117 (A6′), P l.229-230 and l.280. G_k upgrades «⇐ not proved» to «⇐ false»: k(G_k) = 1, T_key = 2^k − 2. |
| H3 | 217 l.105 | «A super-polynomial family = an infinite family with k(G) ≥ c·d^ε; L-LOWER L18's level-8 attempt is k = 8.» | Not in place. The bracket before it does not name it. It is superseded only implicitly by 217 l.118 (sufficient direction, with k_c) and P l.223-226. As an «=» it is false by G_k. |
| H4 | 217 l.119-122 | «Next for track A: (a) an exact characterisation of what a level-k full enumeration demands of the Ξ side … the candidate route to ENUM-LOG» | No. Written after A6′, it still makes ENUM-LOG the target although A6′ had just called it necessary only. |
| H5 | 217 l.181, 189-193, 204-207 | «toward ENUM-LOG»; «an ENUM-LOG proof must use the TIMING and ORDER of the flips»; «ENUM-LOG would follow if f grows exponentially, and fails if a construction keeps f constant» | Not individually (written 09:19Z, before the 10:03Z correction). P l.314 keeps A7, A7′ and «every statement about how large k(G) can be» out of the packet. |
| H6 | 217 l.97-98 | «So the towers are: k = 6, 7 bottom levels of FULL key enumeration (T ≥ 2^(k+1)), fuelled by d − k ≈ 3k upper levels.» | No (DATA). The counter-instance is already on record: DBL4 is a HALF enumeration with k = 0 (217 l.107-109, P l.262-263). |
| H7 | 217 l.201; 218 l.83, l.29 | climbs with objective «(k(G), T)» and «(k, the largest sw at level k, the sum of all sw)» | No. These searches rank full-enumeration depth first, so a half-rate family scores k ≤ 1 under them. 218 l.99 has one run under «the other objective». |
| H8 | 217 l.50-52; 214 l.7-9 | «(the towers become a family)»; «one mover switches 2^k − 1 times» | No. Both are sufficient forms and claim no necessity; they only assume the kill would be a full-rate tower family. |
| H9 | 218 l.22-23 | «Upward ladders are exponential in d only if the ceiling is reached up to an additive constant, and then by a factor 2^(d/2), never 2^d.» | No. UP-CEIL proves the «never 2^d» half only; a mover at half rate near mid level is not excluded. The box as a whole is DROPPED (l.6-9). |
| H10 | 218 l.76-77, l.4-5, l.110-111 | «Whether the two odometers can be made to drive each other for every k is the open question»; «which landed lemma, if any, forbids k = d/2 for all d?»; the d = 8 search with «the full mover of level 3» | No, but dropped with the box: l.8-9 says full enumeration on upward ladders «no longer bears on G-N5-TIME». |

Statements that already have it right: P l.1 («ENUM-LOG is necessary only»), P l.217-218 (ENUM-NEC), P l.223-226 (kill form by SW-POLY, «k and k_c are diagnostics»), P l.227-231, 217 l.112-118 (A6′). The true necessities are depth, not enumeration: 217 l.85 and P l.184 («needs movers that are deep in BOTH graphs»).

One wording slip that bears on «switches against |K(x)|»: 213 l.24-25 says the mover with 15, 31, 63, 127 switches «has |K(x)| = 2^20, 2^20, 2^24, 2^28 possible keys», but l.150-151 and P l.258-264 show these are two separate maxima (HIT7's 127-switch mover is at level 6 with |K| = 128). Not withdrawn in box 213.

#### Notes (inferences, not in the documents)

- **N1. How far below |K(x)| the busiest mover of G_k can be.** If every mover has degree 2 (M = 2N) and the W-levels are 0..k, Lemma 0 (a) gives |K(x)| = 2^(lev(x)+1) ≤ 2^(k+1), and A2 gives lev(x*) ≥ k − 2 for the mover with 2^(k−2) switches. So |K(x*)| is 2^(k−1), 2^k or 2^(k+1): two to eight times its switch count. If the brief's «|K(x)| much larger» means more than that, one of the stated facts needs a second look.
- **N2. ENUM-LOG for c < 1.** From N1, sw(x*) + 1 ≥ |K(x*)|^c whenever c·(lev(x*) + 1) ≤ k − 2. That holds for every k ≥ (2 + c)/(1 − c): from k = 5 at c = 1/2, and from k = 5 to 11 at c = 3/4 depending on x*'s level. Then k_c(G_k) ≥ k − 1, about N/9. So G_k leaves ENUM-LOG untouched only at c = 1; the packet's k_c form (P l.218) fails on it for each fixed c < 1. Nothing PROVED breaks, because the packet states that form only as a consequence of QUIET-KEY-1P.
- **N3. UP-CEIL.** With d = k + 1 levels and D = 2 it caps sw at 2^⌈(k+1)/2⌉ − 1, which is below 2^(k−2) for k ≥ 5. So G_k must have a Ξ-target on the same or a lower W-level than its mover, or UP-CEIL is wrong.
- **Not read (outside the brief):** the untracked docs/new/P-N5-KEY1P-after-EXP-draft.md and experiments/new/box217/out/key1p_gk.out, which could confirm N1-N3 directly.

## E. Not claimed; TARGET.md diff
This file decides nothing. EXP-IDEAL is a kill CANDIDATE until two referees sign P-N5-EXP and CHECKER passes it (D1); every «FALSE»
above is conditional on that. If it lands, candidate N5 (SPEC S1-S5 from its default start S3) fails gauntlet step 4 (TARGET.md §5)
and becomes a dead end with the instance family Γ3(G_k); TARGET.md's statement (§2) is untouched: it is neither proved nor refuted
by the failure of one candidate. Not M3, not M4.
