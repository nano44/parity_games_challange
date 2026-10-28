# P-N5-DEPTH-add fixes (box 22 conditional companion; repairs only)
L-SI successor 19 (Opus 5.5; D15, D18, L37, L40). Written at the Lead's GO of 2026-10-28 22:36Z (Lead's stamp), after both reports and both §Cs.
Stamp: the commit (date -u).
- Object: docs/si/P-N5-DEPTH-add-box22.md, sha1 4d51aa5ea4e1a1d145da4cb825deab75198abae7 (l-si freeze aa6061d1). FROZEN, not edited. The author
  was L-SI successor 18; I write these repairs as its successor.
- Repairs only. The two gaps of the joint map are repaired by the forms both referees sign. Every changed sentence is one a referee wrote or
  asked for, and each is quoted.
- Sources (trunk 4eb5cbfb): REFEREE successor 16, docs/referee/R-N5-DEPTH-add.md, report f4b54c43 and §C f5081a6a (stamps at c9bdfa68 and
  dc4e47b8; quoted at dc4e47b8); REFEREE-2 successor 18, docs/referee-2/R2-N5-DEPTH-add.md, report dad93591 and §C d8402f3d (quoted at 4eb5cbfb).
- Quotes are checked by experiments/si/rund/quotecheck.py (pinned in experiments/si/check.sh, with a shifted-line control that must fail).
- Every item stays CONDITIONAL on its named premise (FREEZE-A (b), (R-LEN), ZCH-COUNT, OFFSET-MONO, STATIC-DEPTH), as the packet states.

## Verdicts (joint)
- REFEREE §C: [Q docs/referee/R-N5-DEPTH-add.md@dc4e47b8:121] «Joint gap map: {G-DADD-1, G-DADD-2} (with G-DADD-3 folded into G-DADD-2 as described).»
- REFEREE-2 §C: [Q docs/referee-2/R2-N5-DEPTH-add.md@4eb5cbfb:150-151] «No disagreement on any verdict. Joint gap map: G-DADD-1, G-DADD-2. The PURE-LEN
  repair should be the count form, or the position form together with its extra step (C2).»
- So: Lemma GATE-PUSH and its Count are SIGNED (never exercised; rests on proof alone, F4). Proposition PURE-LEN is FALSE as stated and is
  replaced by PURE-LEN′ (F1). Lemma MONO-REF and Lemma E-ONEWAY are SIGNED with the "before c" hypotheses (F2, F3).

## F1. G-DADD-1: PURE-LEN is FALSE as stated; replaced by the COUNT form PURE-LEN′ (signed by both). REFEREE's position form is WITHDRAWN
- Packet text: [Q docs/si/P-N5-DEPTH-add-box22.md@aa6061d1:44-45] «Statement. For a pure C-interval [a, b] of class c, under GEN_W on U_c:
  b − a ≤ L + (1 + N_σ̄ + N_cyc)·(|U_c| − 1) + N_σ̄ + N_cyc»
- The failing step: [Q docs/referee/R-N5-DEPTH-add.md@dc4e47b8:44-47] «STATIC-DEPTH's per-vertex part is local … But its LENGTH conclusion b − a ≤ max d*
  comes from a GLOBAL argument: once σ is unchanged everywhere, the next transition is a fallback. A class that has settled does not stop the run,
  and other classes keep switching.»
- Instance (both referees): [Q docs/referee/R-N5-DEPTH-add.md@dc4e47b8:48] «Witness: pure_22 (experiments/new/box22/instances/pure_22.pg, sha1
  f7ba3897, n = 22) at its S3 start.» with [Q docs/referee/R-N5-DEPTH-add.md@dc4e47b8:52] «Bound: L = 2, N_σ̄ = 0, N_cyc = 0, so b − a ≤ 2 + 1·2 = 4.
  Actual b − a = 10.» REFEREE-2 adds reader40_plus2 ([0, 41] against bound 2), kw25_n32 and ccl_w48_n48
  ([Q docs/referee-2/R2-N5-DEPTH-add.md@4eb5cbfb:56-58] «the lane's own experiments/new/box22/instances/pure_22.pg (class 10, |U_c| = 3, bound 4,
  intervals [9, 18], [23, 33]); experiments/red/xing/instances/kw25_n32.pg (class 2, |U_c| = 3, bound 4, interval [0, 25]);»).
- The repair both sign: [Q docs/referee/R-N5-DEPTH-add.md@dc4e47b8:123-124] «PURE-LEN′: for a pure per-class C-interval [a, b] of class c, under GEN_W on
  U_c, the transitions of [a, b] with an Even switch in U_c number ≤ L + (1 + N_σ̄ + N_cyc)(|U_c| − 1) + N_σ̄ + N_cyc.» and
  [Q docs/referee/R-N5-DEPTH-add.md@dc4e47b8:131] «No step uses that the pieces are adjacent or that a frozen class stays frozen. SIGNED (with REFEREE-2).»
- Repaired §2 (REPLACES PURE-LEN): "Proposition PURE-LEN′ (CONDITIONAL on FREEZE-A (b), ZCH-COUNT, STATIC-DEPTH). For a pure per-class C-interval
  [a, b] of class c, under GEN_W on U_c, the transitions of [a, b] at which some Even vertex of U_c switches number
  ≤ L + (1 + N_σ̄ + N_cyc)·(|U_c| − 1) + N_σ̄ + N_cyc. Proof: at most L of them lie before a + L. Cut [a + L, b] at every σ̄ change in U_c and every
  change of c's cycle (≤ 1 + N_σ̄ + N_cyc pieces, N_σ̄ + N_cyc cut transitions). On each piece, STATIC-DEPTH's per-vertex induction restricted to U_c
  (closed under H_b-successors in a pure interval; P-N5-DEPTH-fixes-box22 F4) puts every Even switch of U_c in the piece's first
  max_{U_c} d* ≤ |U_c| − 1 transitions. Sum."
- WITHDRAWN (recorded as withdrawn, not as an alternative): REFEREE's position form, [Q docs/referee/R-N5-DEPTH-add.md@dc4e47b8:135-136] «So I withdraw
  the position form as a repair and keep it as data only (0 failures in both corpora).» Its missing step ("a frozen class stays frozen") is
  REFEREE-2's C2 and is not proved here.
- Consequence for the packet's remark "'< 2n' … holds exactly when N_σ̄ = N_cyc = 0": it now speaks of Even-switch transitions of U_c, not of
  b − a. The length of a per-class pure C-interval is not bounded by class quantities (pure_22, reader40_plus2).

## F2. G-DADD-2: MONO-REF needs "m at or before the first visit of c" (signed by both)
- Packet text: [Q docs/si/P-N5-DEPTH-add-box22.md@aa6061d1:55-56] «Lemma MONO-REF. Let t → t+1 be in-phase, z ∈ U ∖ {c}, and m ∈ T on z's honest
  (t+1)-play, m ≠ z.»
- REFEREE: [Q docs/referee/R-N5-DEPTH-add.md@dc4e47b8:65-66] «The proof's telescoping "along the T-vertices x_1, …, x_h = m of z's (t+1)-play … with
  par_{t+1}(x_i) = x_{i+1}" breaks when the list passes c.» Instance: [Q docs/referee/R-N5-DEPTH-add.md@dc4e47b8:67] «Witness: frzh3n_701_best
  (experiments/n5-exhaustive/results/box9b/frzh3n_701_best.pg, sha1 6de40c62, n = 8) at its S3 start, t = 1.» REFEREE-2's instance: b4_theta_n7
  ([Q docs/referee-2/R2-N5-DEPTH-add.md@4eb5cbfb:79-80] «Instance: experiments/n5-exhaustive/instances/b4_theta_n7.pg
  (sha1 5627745306a45f1a98387c53bba40065375acd5e) from docs/referee-2/R2-N5-DEPTH/mr/b4_theta_n7_mrafter.start»).
- Repair: [Q docs/referee/R-N5-DEPTH-add.md@dc4e47b8:73] «Repair: add "m at or before the first visit of c on z's (t+1)-play". With it, MONO-REF is
  SIGNED.»
- Repaired statement: "Lemma MONO-REF. Let t → t+1 be in-phase, z ∈ U ∖ {c}, and m ∈ T on z's honest (t+1)-play, m ≠ z, with m AT OR BEFORE the
  first visit of c on that play. Suppose the Q-vertices of that play from z (included) to m (excluded) are on no honest cycle at t. Then
  off_{t+1}(z; m) ⪰ off_t(z; m)." The proof is unchanged (its telescoping stays before c).
- DADD-N2 = N-DADD-1: with OFFSET-MONO⁺ (P-N5-OFFMONO-add3, signed by both) the no-cycle hypothesis can be dropped; the before-c restriction stays
  ([Q docs/referee/R-N5-DEPTH-add.md@dc4e47b8:92-93] «With OFFSET-MONO⁺ (add3, both signatures) MONO-REF's "no honest cycle at t" hypothesis is
  unnecessary. The "before c" restriction of G-DADD-2 stays necessary.»). Recorded as a premise alternative, not adopted here.
- Effect on later lane work: docs/si/N5-EXIT-box22.md §1-§2 (MONO-REF, PUSH, NO-UP, PAIR) used MONO-REF without the restriction; those
  working-note statements carry G-DADD-2's hypothesis from now on. The frozen P-N5-CORE-box23 does not use MONO-REF.

## F3. E-ONEWAY with "e1 at or before c on w's play" (signed by both); the e1-after-c case is unproved (DADD-N3 / G-DADD-3)
- Packet text: [Q docs/si/P-N5-DEPTH-add-box22.md@aa6061d1:60-62] «Let e1 ∈ T be the exit of a (the first T-vertex on a's play), with a's class
  exit path π_a and exit e1 unchanged on [t, t′]. Let e1 lie on w's honest play at every state of [t + 1, t′], with MONO-REF's no-cycle
  hypothesis.»
- REFEREE: [Q docs/referee/R-N5-DEPTH-add.md@dc4e47b8:84-85] «Both MONO-REF uses need e1 at or before the first c on the respective plays. The
  repaired hypothesis "e1 at or before the first c on w's honest play at every state of [t + 1, t′]" gives that, also for b at t + 1.»
- Repaired hypothesis: "Let e1 lie AT OR BEFORE the first c on w's honest play at every state of [t + 1, t′]". The proof is unchanged.
- Unproved case, recorded: [Q docs/referee/R-N5-DEPTH-add.md@dc4e47b8:94-95] «DADD-N3 (E-ONEWAY). The conclusion held in all 704 windows with e1 after
  c, but the proof does not reach them. Proving it there would need a different argument.» (REFEREE-2: 711 windows, 0 returns.) OPEN.

## F4. DADD-N1 = N-DADD-2: GATE-PUSH is never exercised; it rests on proof alone (record)
- REFEREE: [Q docs/referee/R-N5-DEPTH-add.md@dc4e47b8:90-91] «GATE-PUSH is never exercised in my data (no σ̄ change at a gate after the A-freeze with
  y1 ∈ A_{t+1} in 7,295 pure intervals). Its count is therefore untested; the landing text should say "rests on proof alone".»
- Recorded: GATE-PUSH and its Count rest on proof alone (0 qualifying σ̄ changes in either referee's corpus).
- The packet's §4 data line on PURELATE is a statement about Even switches. It supports PURE-LEN′, not PURE-LEN (REFEREE-2 §1.2 "Effect").

## F5. N-DADD-3: the suggested wordings are those used in F1-F3 (accepted by REFEREE)

## Not changed
GATE-PUSH and its Count are unchanged. PURE-LEN is replaced by PURE-LEN′ (F1); MONO-REF and E-ONEWAY gain their "before c" hypotheses (F2, F3).
Every item stays CONDITIONAL on its named premise. Scope as the packet states it: conditional reductions; nothing here bounds N5's running time;
not a TARGET.md claim; G-N5-TIME stays OPEN.
