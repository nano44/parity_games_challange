# R234: adversary on L-SI 51 box 101 Lemma LAM-GAP and box 100 (WINDOW, TWO-CROSS, DEPTH-COUNT3) (L-RED successor 66)
Written 2026-11-12 (date -u in the commit). Lead 10:00Z: «NEW ITEM 0 … box 101 … claims Lemma LAM-GAP PROVED (lane) … Attack it first:
(a) The proof case by case … (b) The match between WINDOW's window … and LAM-GAP's hypothesis … (c) Kill side … Verdict on LAM-GAP to me
first: SURVIVES / GAP (exact wording) / DEAD (frozen instance).» Targets: claude/l-si 23d39400 docs/si/box101-lamgap.md (sha1 7e7692bb),
docs/si/box100-scclin.md (3b6ae726). Labels: SURVIVES / GAP / PROVED (lane) / DATA (unit, set, scope, counter) / READING. Not a TARGET.md
claim; G-N5-TIME stays OPEN; N5′-xi stays a CANDIDATE (D1).
Tools (experiments/red/r234): lg234.py (INDEPENDENT one-player VJ engine + Howard over ALL tie resolutions; no code from own.py, si.py or
lamgap101.py), xlg234.py (replays box 101's own random games through lg234), w234.py (WINDOW / LAM-GAP on Γ3 HOW3 runs), d234.py
(DEPTH-COUNT3 and TWO-CROSS counters on Γ3), run234.sh. Γ3 runs use this lane's engine r232/how3_232 (graph from L-NEW fcba92fc, env LNEW).

## 0. Verdicts
- Lemma LAM-GAP (box 101 §2): SURVIVES every step. It is even true one step sharper (Lemma SHARP, §3, PROVED (lane)): b − a ≤ |Ch|, and
  that bound is attained (DATA §6). Box 101's |Ch| + 1 is correct, only not tight.
- GAP W1 (wording, harmless; box 100 §4 and box 101 §3): «G_C[φ]» fixes EVERY mover outside C at its final strategy, upstream movers
  included. In the two-player run at t ≥ t0 the upstream movers (SCCs that reach C) may still switch, so Ω_t is NOT the value of σ_t in
  G_C[φ] at upstream vertices, and «Λ constant for every vertex» in the two-player run does not give «Λ constant for every vertex of
  G_C[φ]». Fix: take G_C[φ] on Reach(C) (the vertices reachable from C's movers; closed under successors, so a one-player game in its own
  right). Then Ω_t = one-player value on Reach(C), and box 101 §3 goes through verbatim (window over Reach(C) ⊇ window over all of Γ3).
  w234 checks exactly this replay: 0 mismatches on 26 instances (§6).
- Lemma TWO-CROSS (box 100 §2): SURVIVES (premises (d), (f), (i) quoted below; my counter twocross_unm 0, control fires).
- Lemma DEPTH-COUNT3 (box 100 §3): GAP D1 (the proof omits a case; the conclusion stays polynomial after a fix):
  - The definition gives a length-only change (Π_t = Π_(t+1)) depth |Π_t|. So a length-only change with |Π_t| ≤ c is a «change of depth in
    [0, c]» and is counted by the statement.
  - The proof treats «d > c (including length-only changes)» together: «the c + 1 most relevant elements of both sets are common, so
    P_a = P_b». For a length-only change P does not rise, so the P-count S_c(n3) − 1 does not cover it, whatever d is.
  - The case is not vacuous on Γ3: d234 counts 2,590 length-only changes with |Π| ≤ 3 on 100 random genomes (804 at gate faces) (§6).
  - Fix (PROVED, lane, §4): on a Λ-interval Π never falls, so each Π value is one contiguous plateau, and on a plateau len moves strictly
    monotonically in [0, n3 − 1]. The length-only changes with |Π| ≤ c are therefore at most n3·(n3 − 1)·S′_c(n3) per vertex, where
    S′_c(n) := Σ_(j=0..c) C(n, j). Corrected statement: Ω(v) makes at most n3·(S_c(n3) − 1) + n3·(n3 − 1)·S′_c(n3) changes of depth in
    [0, c]. WINDOW's first factor gains the same term per face (2·I_C·n3(n3 − 1)S′_c(n3)); every conclusion of box 100 / 101 stays
    polynomial and unchanged in form.
- Theorem WINDOW (box 100 §4): SURVIVES with W1 and D1 applied. The step «window = Howard run of one fixed one-player game» is replayed
  state by state on the 26 frozen instances: replayfail 0; control (one face of φ flipped) mismatches every window (§6).
- Kill side (c): no one-player VJ game has a constant-Λ window > |Ch| (so none > |Ch| + 1) in any of these searches:
  - exhaustive n ≤ 4 (every graph, parity vector, start and tie resolution; 18.9 million runs at n = 4);
  - box 101's 3,000 seed-1 games, replayed with ALL tie resolutions;
  - climbs at n = 5, 7, 9 maximising window − |Ch|.
  Windows of exactly |Ch| are common, so SHARP is tight.

## 1. Premises (grep of trunk docs/RESULTS.md at 071392490)
- l. 15648: «(d) Facts F1, F3, F4′, F5, F6, DOM, STRICT on HOW3(G) (§4 l. 149-) [every genome]: F1 by R15 (a), not R118 (b)»
- l. 15651: «(f) Lemma LOC-GATE3 (§5 l. 175): «Let t be a state, g a gate, a := σ̄_t(g) ∈ {pe_g, pβ_g}, b the other face, Ω := Ω_t. If
  Ω(a) ≠ Ω(b), then Ω(a) ◁ Ω(b).». Both SIGN»
- l. 15654: «(i) Corollary NO-TIE3 (§5 l. 209): «At every state and gate g, Ω_t(pe_g) ≠ Ω_t(pβ_g).». Both SIGN»
- l. 637: «(a) Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴ Ω_{Switch_I(σ)}. This is VJ00 Lemma 5.7
  as stated (VJ00's Improve already allows any non-empty I)»
- One-player reading of R15 (a) (box 101's (M)): a one-player game is a parity game whose Odd vertices (and frozen Even vertices) have
  out-degree 1, so Odd's optimal reply is the only one and Ωσ is the one-player value. A Howard step switches each v ∈ Ch at most once,
  to a successor with a strictly larger value: a non-empty unambiguous set of improvements, or the empty set at the end. Lemma A applies
  as stated. SURVIVES. (R15's side finding, «Improve(σ) ≠ σ ⇒ σ not maximum» failing at cycle nodes, concerns strictness only; (M) uses ⊴.)

## 2. LAM-GAP, case by case (box 101 §2)
- P1-P3 against VJ (own.py VJ.val / VJ.cmp, the R118 [VJ] order: Λ by reward, then the most relevant element of Π_a Δ Π_b, then len,
  shorter better iff Λ even). P1: if v ≠ Λ(v), σ(v)'s path to Λ is the suffix of v's (also when v is on the cycle: v comes after Λ). P2:
  for equal Λ, v enters both Π or neither, Δ is unchanged, len + 1 on both; for different Λ only the rewards decide. Note: P2 needs v ∉ Π
  on both sides, which «paths avoid v» gives. P3: trivial. All SURVIVE.
- (U): SURVIVES (a play's prefix to Λ is a simple path in the game graph).
- (L), base k = 0: a path with c(P) = 0 has no Ch vertex before ℓ, so for v ∈ Ch the claim is vacuous; for deterministic v it is the
  inner induction along P. SURVIVES.
- (L), deterministic v, Λ(v) = v: «u's play returns to v, so Λ(u) = v; val(u) ⊵ value(P′) forces rew(v) > rew(ℓ)». Right: different Λ
  compare by reward, and v ≠ ℓ. SURVIVES.
- (L), v ∈ Ch: the successor w = σ_(a+k)(v) is ⊴-best at a + k − 1 (moved to a best one, or kept a best current one). Any tie rule.
  Then (M) at w, then P1-P2 at time a + k, where w's path avoids v because v ≠ Λ(v). The case Λ(v) = v uses w (not u): w's play returns
  to v, so Λ(w) = v, and the reward argument repeats. Box 101 writes «as in the deterministic case»; that is correct with w in place of u.
  SURVIVES.
- (O): (L) at k = |Ch| covers every simple path to Λ_a(v); with (U), val = opt. SURVIVES.
- (E), the exit step, all three cases:
  - Λ(w) ≠ ℓ: at t* + 1, v → w; whether v is on w's new cycle or not, Λ(v) = Λ(w) = Λ_(t*)(w) ≠ ℓ (Λ(w) constant by the window).
    SURVIVES. This answers the Lead's question: a non-top switch to a successor with another top always changes Λ(v). A switch that
    «closes a cycle avoiding ℓ» is the sub-case v on w's new cycle: that cycle's top is Λ(w) ≠ ℓ.
  - Λ(w) = ℓ, w's path Q avoids v: v·Q is a simple path to ℓ, so ext(v, value(Q)) ⊴ opt(v) = ext(v, opt(σ v)); P2 reflects. SURVIVES.
  - Q passes v: at t* + 1, w's path is the suffix of v's (avoids v), val_(t*+1)(w) = opt(w) by (M) and (U), and P2 reflects again.
    SURVIVES.
  - «At t* + 1 all values are unchanged … every non-top improving switch at t* + 1 ends the window»: SURVIVES (if t* + 2 ≤ b, nobody
    switches at t* + 1, so the run stops there).
- The «all simple paths» quantifier in (L): SURVIVES. It is what makes the proof work without suffix-optimality: (L) never applies ext to
  a value whose path may pass v.

## 3. Lemma SHARP (PROVED, lane; sharpens LAM-GAP by one)
Statement. In LAM-GAP's setting, b − a ≤ |Ch|.
Proof. If |Ch| = 0 nothing switches and b = a. Let |Ch| ≥ 1, t* := a + |Ch|, and suppose b ≥ t* + 1. By box 101 (E), only top vertices
ℓ ∈ Ch (Λ(ℓ) = ℓ) switch at t*. Let ℓ switch at t* to w.
- If Λ_(t*)(w) ≠ ℓ: as in (E)'s first case, Λ_(t*+1)(ℓ) = Λ(w) ≠ ℓ. Contradiction.
- If Λ_(t*)(w) = ℓ: every simple path from w to ℓ has at most |Ch| − 1 choice vertices before ℓ (ℓ ∈ Ch is its end). By (L) at
  k = |Ch| − 1 and (U), val_(t*−1)(w) = opt(w) = val_(t*)(w) ((M) and (U) again). The same holds for u := σ_(t*)(ℓ), which lies on ℓ's
  cycle, so Λ(u) = ℓ. Howard at t* − 1 ≥ a made u ⊴-best for ℓ by the values at t* − 1. So val_(t*)(w) = val_(t*−1)(w) ⊴ val_(t*−1)(u) =
  val_(t*)(u): the switch is not improving. Contradiction.
So nobody switches at t*, the run stops at t*, and b ≤ t*. ∎
- Consequence: Gap(C) ≤ N_C, and box 101's factor (N_C + 2) becomes (N_C + 1). Cosmetic.
- Tightness (DATA §6): windows with b − a = |Ch| exist at every size tried (exhaustive n = 3: 382; n = 4: 35,680; box 101's seed-1 games:
  118; climbs reach b − a = |Ch| at |Ch| = 4 and 5).

## 4. DEPTH-COUNT3, GAP D1 and its fix (PROVED, lane)
- Gap: §0. The rest of box 100 §3's proof is right: Λ changes ≤ n3 − 1 per vertex (F1; a Λ change raises its reward strictly); for a
  Π change of depth d ≤ c, z is in P_s and is the most relevant element of P_a Δ P_b, on the same side as in Π, so P rises; for a Π
  change of depth d > c the top c + 1 elements agree. d234's shallow_noP_PI (a Π change of depth ≤ c without a P rise) is 0 everywhere.
- Fix: on one Λ-interval Π is ⊴-non-decreasing (F1 at fixed Λ), so each Π value occupies one contiguous plateau. On a plateau (Λ, Π fixed)
  len moves strictly in one direction inside [0, n3 − 1]: at most n3 − 1 changes. Plateaus with |Π| ≤ c: at most S′_c(n3) per
  Λ-interval, at most n3 Λ-intervals. ∎
- Downstream: Deep_c(C) (flips charged to depth > c) is unchanged. A flip charged to a length-only change with |Π| ≤ c is now counted by
  the fixed DEPTH-COUNT3. d234's charged_lenshallow is 0 on all data so far, so no such flip has been seen.

## 5. TWO-CROSS (box 100 §2)
- (i): Ω_t(a) ◁ Ω_t(b) (LOC-GATE3 + NO-TIE3 at t), Ω_t(b) ⊴ Ω_(t+1)(b) (F1), Ω_(t+1)(b) ◁ Ω_(t+1)(a) (at t + 1). SURVIVES.
- (ii): injective charging (one step, one face) and alternation (flips alternate «away from pe» / «away from pβ»), so ≤ 2m + 1. SURVIVES.

## 6. DATA
- Engine agreement (xlg234 1 3000 9; unit vertex value; set: box 101's seed-1 games and both of its runs per game): valdiff 0 of 85,567
  values between lg234 and own.VJ (relabelled by relevance rank).
- Reproduction in the target's convention: lamgap101.py 1 3000 9 7 (env RED = l-red 59daaef2) prints box 101's line byte for byte
  (max_window 4 at_Ch 6, optchecked 238); l1probe100.py 100 3 2 MWR4_2 prints «maxLamGap 26», as box 100 §5.1.
- LAM-GAP / SHARP, independent engine (lg234; unit: Howard run over one tie resolution; window = b − a over all-vertex Λ):
  - exhaustive n = 3 (out/lg_exh3.out; 2,744 games: every out-degree-≥1 graph × parity vector, every start, every tie resolution; 14,356 runs):
    gapfail 0, sharpfail 0, eqCh 382 (windows with b − a = |Ch| ≥ 1); max b − a per |Ch| 0/1/2/2 at |Ch| 0/1/2/3. Control CTRL=1 (bound
    |Ch| − 1): gapfail 598 (fires).
  - box 101's 3,000 seed-1 games with ALL tie resolutions from both of its starts (6,438 runs): gapfail 0, sharpfail 0, eqCh 118, max b − a
    4 at |Ch| 6 (box 101: 4 at 6).
  - climbs (lg234 climb SEED N ITERS; score b − a − |Ch| − 1 over 6 starts, all tie resolutions; out/lg_climb_*): best excess −1
    (b − a = |Ch|) at n = 5 (|Ch| 4), n = 7 (|Ch| 5), n = 9 seed 12 (|Ch| 5); n = 9 seed 11 best −2 (b − a 7, |Ch| 8); never 0.
  - exhaustive n = 4 (810,000 games, 18,882,016 runs; out/lg_exh4.out): gapfail 0, sharpfail 0, eqCh 35,680; max b − a per |Ch|
    0/1/2/3/3 at |Ch| 0/1/2/3/4; capped 0.
- WINDOW on Γ3 (w234 via run234.sh; unit: two-player window after t0 of the largest SCC C; set: 26 frozen instances of box 99; window
  length = b′ − a with b′ the first window state at which no mover of C switches):
  - replayfail 0 (every window's C-states and every Reach(C) value equal the one-player Howard run of G_C[σ̄_a] on Reach(C));
  - lamgapfail 0, sharpfail 0; max length 7 (MWR4/8/16_2, N_C 44/80/152), ≤ 6 elsewhere;
  - control CTRL=1 (one face of φ flipped): mismatches 14 of 14 windows on MWR4_2 and on C98_4_5_3 (fires).
- DEPTH-COUNT3 / TWO-CROSS on Γ3 (d234, c = 3; unit: vertex change / gate flip):
  - 100 random genomes (seed 2341, r231 dep231.rgen): lenshallow 2,590 (gate faces 804), shallow_noP_PI 0, charged_lenshallow 0,
    twocross_unm 0 of 984 flips; control ctrl_to_unm 250 (fires).
  - 26 frozen instances (out/d234_inst.out): lenshallow 284 (faces 89), shallow_noP_PI 0, charged_lenshallow 0, twocross_unm 0 of
    1,116 flips; control ctrl_to_unm 679 (fires).
