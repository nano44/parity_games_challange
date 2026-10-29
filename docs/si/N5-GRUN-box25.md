# N5-GRUN (box 25): G is not intrinsic (readers lift it to 1.23n with the run unchanged); Lemma GATE-RISE; Theorem STATIC-DEPTH-REL and the reader-proof cut count SEG
L-SI successor 21 (Opus 5.5; D18, Lead reading L40). Lead's brief 2026-10-29 03:02Z, STEP 2: «CONJECTURE G-RUN, the number of σ̄ changes per
fallback-free run (DATA ≤ 1.07n) ... SPLIT gives |S| ≤ G + (G + 1)(n − 1), so G = O(n) yields O(n²) per run». Working note, unrefereed, not
frozen. Not a TARGET.md claim. Nothing here bounds N5's running time; G-N5-TIME stays OPEN. Labels (D18 / L40): PROVED (lane) / CONJECTURE /
OPEN / DATA / READING / DEAD. Counts are TRANSITIONS. Tools: experiments/si/grun/ (gstat.py, gaterise.py, readerg.py, anchor.py,
relseg.py, gclimb.py); outputs grun/*.txt, grun/out/.

## Summary
| § | item | label |
| --- | --- | --- |
| §1 | G per run in the library: max 48 (1.06n); the champions are one-gate games with G ≈ run; one gate can change 62 times (gate_K64_n581) and return to an earlier option 61 times | DATA |
| §1 | the data bound "G ≤ 1.07n" is beaten without readers: G 35 at n 29 (1.21n; gclimb from pftheta34) | DATA |
| §2 | Lemma GATE-RISE: a clean σ̄ change at u strictly raises Ξ(u) itself; so G ≤ Σ_gates XR_S(u) + ties + cycle / pass-through cases | PROVED (lane); a REDUCTION |
| §3 | G is NOT intrinsic: Odd readers (no predecessors) raise G on runfam_K10 from 9 to 91 at n 74 (1.23n) with the run unchanged (99); Even anchors put the readers into R81's K, so G^K (σ̄ compared on K) is not intrinsic either (91 at n 99). Since G ≤ \|S\|, G-RUN is no easier than RUN-LIN′ in general | DATA (instances pinned); READING |
| §4 | Theorem STATIC-DEPTH-REL: STATIC-DEPTH′ with σ̄ and the cycles required constant only on the end state's plays from Even choice vertices; Corollary REL-SPLIT: \|S\| ≤ SEG·n − 1, SEG = number of maximal REL-admissible segments; SEG is unchanged by readers and anchors (9 on runfam_K10 with or without 25 readers / anchors) | PROVED (lane); REDUCTION; DATA |
| §5 | CONJECTURE SEG-RUN (SEG = O(n); DATA ≤ 0.79n in the library, ≤ 1.00n after climbs): with REL-SPLIT it gives O(n²) per run | CONJECTURE, DATA |

## 0. Setting
As N5-PIECE-box25 §0. A run S: a maximal fallback-free stretch of one phase. G(S): the transitions t → t + 1 of S with σ̄_t ≠ σ̄_{t+1}.
XR_S(v): the transitions of S at which Ξ(v) changes. Landed premises used: SPEC S1, S4a, S4c; RESULTS R15 (a) Lemma A with (d) («Ωσ ⊴
Ω_{Switch_I(σ)}» for every non-empty set I of improvements; N5's S4a applies Switch_I with ∅ ≠ I ⊆ Iσ), so Ξ_{t+1} ⊵ Ξ_t pointwise at every
in-phase S4a transition; RESULTS R57 (a) premise (VJ) («for every positional σ and every positional Odd strategy τ′, Ξσ(v) ⊴ V_{σ,τ′}(v) at
every v»); R77 (c)'s proof steps and R80 (a) EVERY-SWITCH as in N5-PIECE-box25 §0; R81's K (Fact K1: every Even vertex outside K has
out-degree 1).

## 1. DATA (grun/gstat.py; logs grun/gstat_alt.txt (default starts), grun/gstat_alt_start.txt (pinned starts))
| corpus | runs | max G | max G/n | max changes of one gate in a run | max returns of one gate | max CH(u)/deg(u) |
| --- | --- | --- | --- | --- | --- | --- |
| alt_all, default starts | 745 | 48 | 1.06 (pftheta34_n32: 34) | 35 | 18 | 1.94 |
| alt_all, pinned starts | 921 | 64 (gate_K64_n581) | 1.06 | 62 | 61 | 31 (a 2-option gate) |
- The top runs by G/n are all one-gate games (so_th, pftheta, pft35, so_sor5, x31_*), with G ≈ |S|: in pftheta34_n32 the gate (19 options)
  changes at every one of the 34 transitions, visiting options in the order 2, 18, 21, 26, 21, 7, 20, 19, 29, 6, 5, 21, 26, 21, 7, 20, 7,
  21, 26, 21, 7, 20, 19, 29, 6, 5, 9, 25, 30, 2, 18, 12, 23, 16, 17 (τ = 17): option 21 is taken 7 times.
- Climbs (grun/gclimb.py, score G − CN·n): from pftheta34_n32 (CN 0.5, n ≤ 48 / 64; logs grun/out/pg_n*.log): G 35 at n 30 and n 29
  (1.17n, 1.21n; grun/out/pg_n64_1), G 36 at n 31; they shrink n rather than grow G. From random one-gate seeds at fixed n ≤ 12, 16, 24, 32
  (CN 0, grun/out/fx_*.log): G/n ≤ 0.75. No growth beyond linear seen.

## 2. Lemma GATE-RISE (PROVED, lane, elementary)
Statement. Let t → t + 1 be an in-phase S4a transition, u an Odd vertex with σ̄_t(u) = y1 ≠ y2 = σ̄_{t+1}(u), u on no honest cycle at t and
at t + 1, y2's honest t-play not through u, and Ξ_t(y1) ≠ Ξ_t(y2). Then Ξ_{t+1}(u) ▷ Ξ_t(u).
Proof. u off the honest cycle: Ξ_t(u) = u ⊕ Ξ_t(y1) and Ξ_{t+1}(u) = u ⊕ Ξ_{t+1}(y2). Let τ′ := σ̄_t with u's choice set to y2. y2's
(σ_t, σ̄_t)-play avoids u, so it is also its (σ_t, τ′)-play, and u's (σ_t, τ′)-play is u followed by it: V_{σ_t,τ′}(u) = u ⊕ Ξ_t(y2). By (VJ),
u ⊕ Ξ_t(y1) = Ξ_t(u) ⊴ u ⊕ Ξ_t(y2). The map x ↦ u ⊕ x is strictly monotone on valuations (S1: for equal cycle nodes it adds u to both path
sets or to neither and 1 to both lengths, so the comparison is unchanged; for different cycle nodes the cycle nodes decide), so Ξ_t(y1) ⊴
Ξ_t(y2), strictly since they differ. R15 (a) gives Ξ_{t+1}(y2) ⊵ Ξ_t(y2). So Ξ_{t+1}(u) = u ⊕ Ξ_{t+1}(y2) ⊵ u ⊕ Ξ_t(y2) ▷ u ⊕ Ξ_t(y1) = Ξ_t(u). □
Count. CH_S(u) ≤ XR_S(u) + TIE_S(u) + CYC_S(u) + THRU_S(u) (the three excluded cases), hence G ≤ Σ_{gates u} (XR_S(u) + TIE_S(u) + CYC_S(u)
+ THRU_S(u)). This differs from R80's RISE-GATE-CLEAN (a κ-rise of the ABANDONED option y1): here the gate itself rises.
DATA (grun/gaterise.py; MUT=1 demands a strict rise of Ξ(y2) instead and must bite):
| corpus | σ̄ changes | clean | tie | on cycle | y2 through u | failures | Ξ monotone failures | count failures | MUT=1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| alt_all (gaterise_alt.txt) | 2,270 | 2,114 | 75 | 8 | 73 | 0 | 0 | 0 | 1,892 failures |
| alt_all, pinned starts (gaterise_alt_start.txt) | 4,020 | 3,752 | 82 | 10 | 176 | 0 | 0 | 0 | |
| lib41 (gaterise_lib41.txt) | 2,031 | 1,889 | 76 | 10 | 56 | 0 | 0 | 0 | |
- The largest XR_S of a gate in a run is 35 (1.06n) on alt_all and 63 (gate_K64_n581) with pinned starts. GATE-RISE moves the question from
  G to XR of the gates; XR per vertex is not bounded (XR-LIN DEAD per phase, N5-ALT-box23 §8), so this is a reduction, not a bound.

## 3. G is not intrinsic (DATA; instances pinned in §6)
- grun/readerg.py: add Odd READER vertices to runfam_K10 (n 49, run [1, 100] of 99 transitions, G 9): priority 0, no predecessors, edges to
  2-6 vertices of one honest class; keep a reader if σ, σ̄, τ and the fallback flags on the old vertices are unchanged at every state, τ (readers
  included) and the readers' cycle nodes are constant on [1, 100] (so [1, 100] is still one fallback-free run), and G grows. 25 readers
  (grun/out/rdr_K10.log): G 9 → 22, 28, 35, ..., 91 at n = 74, run 99 throughout: G = 1.23n, above the 1.07n data bound, with the run fixed.
- grun/anchor.py: for each reader o add an Even ANCHOR e (edges {e, o}, self-loop of a fresh top even priority, σ0(e) = e): e never leaves
  its loop, the readers enter R81's K, and SAME holds (old vertices unchanged at every state; 0 fallbacks on [1, 100]): G^K = G = 91 at n = 99.
- Since every σ̄-changing transition is a transition, G ≤ |S| always. So G = O(n) follows from RUN-LIN′ (|S| = O(n)), and the reader
  padding shows that G can be pushed to ≈ |S| without changing S (here 91 of 99). READING: G-RUN is therefore not a weaker target than
  RUN-LIN′, and SPLIT's product G·(n − 1) mostly counts σ̄ changes nobody reads. A useful cut count must ignore σ̄ changes outside the plays
  that matter: §4.

## 4. Theorem STATIC-DEPTH-REL (PROVED, lane) and Corollary REL-SPLIT (a REDUCTION)
Definitions at a state b of a run. Q := the Even vertices of out-degree ≥ 2. X_b := the least set containing Q and every Even vertex on the
W-play or honest play at b of a member. RO_b := the Odd vertices on the honest b-play of a member of X_b. CW_b / CH_b := the W- / honest
cycles reached by the W- / honest b-plays of the members of X_b; T_W, T_H their vertices. [a, b] is REL-ADMISSIBLE if it lies in one run,
σ̄_t = σ̄_b on RO_b and every cycle of CW_b (CH_b) is a W-cycle (honest cycle) at every t ∈ [a, b]. Depths dW, dH, d as in STATIC-DEPTH′
(N5-PIECE-box25 §2) on the vertices of the W- and honest b-plays of X_b; (H4′_rel): that recursion is well founded.
Theorem STATIC-DEPTH-REL. If [a, b] is REL-admissible, (H4′_rel) and GEN_W hold, then every v ∈ X_b settles (W-play from a + dW(v), honest
play from a + dH(v)) and b − a ≤ max_{v ∈ Q} d(v) ≤ n − 1.
Proof. The proof of STATIC-DEPTH′ verbatim, restricted to the vertices of the W- and honest b-plays of X_b: the recursion from an Even
v ∈ X_b visits only vertices of v's b-plays (y = σ_b(v) and its b-plays are suffixes of v's), every Odd vertex it treats in the honest frame
lies on the honest b-play of a member of X_b, so in RO_b where σ̄ is constant, Odd vertices treated in the W-frame use τ, and every Even
vertex it treats is in X_b; the terminals are the cycles of CW_b, CH_b, which persist. For an Even v of out-degree 1, (A) and (B) are
trivial (σ_t(v) = y always). Length: at t ≥ a + max_Q d, σ_t = σ_b on Q, and every Even vertex outside Q has out-degree 1, so σ_t = σ_b;
a further transition would contradict R80 (a) EVERY-SWITCH. □
- It contains STATIC-DEPTH′ ((H2), (H3′) on all vertices imply the restricted forms).
Corollary REL-SPLIT. Cut a run S from its end into maximal REL-admissible segments [a_1, b_1], ..., [a_SEG, b_SEG] (b_SEG = end of S; a_i least
with [a_i, b_i] admissible; b_{i−1} := a_i − 1). If (H4′_rel) and GEN_W hold at every b_i, |S| ≤ Σ_i (b_i − a_i) + SEG − 1 ≤ SEG·n − 1. Each
cut a_i − 1 → a_i (i ≥ 2) is a transition at which σ̄ changes on RO_{b_i} or a cycle of CW_{b_i} ∪ CH_{b_i} appears; so SEG − 1 ≤ G + CF.
(Proof: Theorem on each segment; minimality of a_i.) □
- Reader-proof (READING, checked in data): a reader (no predecessors) lies on no play of another vertex, and an anchor's plays are its own
  loop, so neither enters RO_b, CW_b, CH_b, and SEG is unchanged: SEG = 9 on runfam_K10, on rdr_K10 (25 readers) and on anc_K10 (25 anchors).
DATA (grun/relseg.py; every segment with (H4′_rel) checked per vertex and for length; MUT=1 uses d − 1):
| corpus | runs | segments | max SEG | max SEG/n | max segment | (H4′_rel) failures | violations | MUT=1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| alt_all (relseg_alt.txt) | 745 | 1,908 | 26 | 0.79 (pftheta34: 24 at n 32; so_sor5: 19 at n 24) | 67 | 45 | 0 | SET_V 994 |
| alt_all, pinned starts (relseg_alt_start.txt) | 921 | 2,890 | 62 (gate_K64_n581) | 0.79 | 55 | 49 | 0 | |
- G − (SEG − 1) reaches 46 (pp_K48_n449): many σ̄ changes there are not cuts. On runfam_K10 SEG = 9 against G = 9 (10 pieces, one σ̄ change
  is off RO).
- Honest limits: (H4′_rel) fails at 45 of 1,908 segment ends (alt_all); those segments are not bounded by the theorem (all are within n − 1
  in data). GEN_W is a hypothesis (as in R77). SEG is not bounded here.

## 5. CONJECTURE SEG-RUN and climbs
- CONJECTURE SEG-RUN: SEG = O(n) for every run. With REL-SPLIT (where (H4′_rel), GEN_W hold) it gives |S| = O(n²) per run, polynomial.
  DATA: max SEG/n = 0.79 in the library, 1.00 after climbs. A super-linear SEG needs many cuts that each change σ̄ on the end state's relevant plays.
- Climbs (grun/gclimb.py OBJ=SEG, CN 0.5; logs grun/out/sg_*.log; the log lines say "G" for the objective): from so_sor5_n24 SEG 23 at
  n 23 (1.00n, grun/out/sg_4); from pftheta34_n32 SEG 26 at n 29 (0.90n) and 24 at n 30 (still running at this write); from runfam_K10
  12 at n 18. pg_n64_1 (the G climb's 35 at n 29) has SEG 25 (0.86n). So the data bound is SEG ≤ 1.00n; nothing super-linear. In these
  one-gate instances the segments have length ≈ 1: the run is a sequence of relevant σ̄ changes, and SEG ≈ |S|.

## 6. Pins (grun/out/; sha1sum)
- rdr_K10: runfam_K10 + 25 Odd readers, n 74, run [1, 100] (99), G 91, SEG 9. .pg a7ac4830ddfd9c49a3c0ad1379cae26299a35bee, .start
  f95c5587016a4b572f7e15539342d8c2f8e97aae.
- anc_K10: rdr_K10 + 25 Even anchors, n 99, the same run, G = G^K = 91, SEG 9. .pg 13833299ac0734e6b605a8f4a23b9e1857e51c9c, .start
  941f1e4ce6639380a30e7e5964c5ac801610a41d (reproduced by grun/anchor.py in check.sh).
- pg_n64_1: G 35 at n 29 (1.21n), SEG 25, no readers, default start. .pg 1b9f5e810267c55873db1bbdd2fbaef6de65ff1c.
- One engine (n5x via root/common.rows) throughout; check.sh "box 25" (grun) re-runs the reader / anchor counts.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/si/grun/ tools, logs, pins; check.sh block "box 25" (grun).
- FINDINGS: (1) G-RUN's data bound 1.07n is beaten (1.21n without readers; 1.23n with readers, run unchanged), and G is not intrinsic:
  readers and anchors raise G (and G^K) to ≈ |S| without changing the run, so G-RUN is no weaker than RUN-LIN′ and SPLIT's G is the wrong
  cut count. (2) PROVED (lane) Lemma GATE-RISE (a clean σ̄ change raises Ξ at the gate): G ≤ Σ_gates XR + ties + cycle cases (reduction).
  (3) PROVED (lane) Theorem STATIC-DEPTH-REL and Corollary REL-SPLIT: |S| ≤ SEG·n − 1 with SEG the reader-proof count of maximal
  REL-admissible segments (where (H4′_rel), GEN_W hold at the segment ends); CONJECTURE SEG-RUN (SEG = O(n), DATA ≤ 1.00n) would give
  O(n²) per run. OPEN: any bound on SEG, XR of gates, or G.
- NEEDS: none from the owner.
