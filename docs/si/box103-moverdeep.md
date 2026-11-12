# Box 103: MOVER-DEEP3 at k = 1: deep mover changes are pure gains there (DATA); GAIN-COUNT (PROVED) reduces MOVER-DEEP3 to CONJECTURE NOLOSS-k1
L-SI successor 51 (Opus 5.5), D18 / D14 / D1; Lead 12:08Z («NEXT: (a), the MOVER-DEEP3 proof attempt from E-MON3 + Howard greed at k = 1,
approved as box 103 … Until then [L-NEW 72's box 208], work your own route»). Labels: PROVED (L-SI lane, unrefereed) / CONJECTURE / DATA
(unit, set, scope, counter) / DEAD / READING. Not a TARGET.md claim; G-N5-TIME stays OPEN; N5′-xi stays a CANDIDATE (D1). Tools:
experiments/si/box103/ (mdeep103.py, wcdeep103.py, run103.sh, check103.sh); engine L-RED 65 how3_232 (claude/l-red 59daaef2, read-only).

## 0. Answer
- MOVER-DEEP3 is NOT proved, at k = 1 or otherwise. Measuring first gave a sharper target:
  - every mover change at fixed Λ whose e-depth exceeds 1 is, at k = 1, a PURE GAIN (the e-set grows by inclusion, nothing lost);
  - deep LOSSY changes (an e-vertex lost) and deep E-UNCHANGED changes occur only at k ≥ 2 (DATA §2).
- Lemma GAIN-COUNT (PROVED, lane; §1): per mover, between two consecutive changes that lose an e-vertex or change Λ, there are at most M
  pure gains. So pure gains are paid for by lossy or Λ changes.
- Corollary (PROVED, lane; §1). The deep mover changes are bounded by a polynomial plus (M + 1)·(the deep lossy and deep E-unchanged
  changes). Hence MOVER-DEEP3 (e-form, c = 1) ⇐ CONJECTURE NOLOSS (deep lossy and deep E-unchanged changes polynomially many), and DATA
  says that at k = 1 there are none (CONJECTURE NOLOSS-k1).
- DEAD (§3): «at k = 1 every mover change has e-depth ≤ 1». Killed by WC16_2 (sha1 995e7132): mover 67 at t = 3 gains e(33, 0) under 16
  common e-vertices (e-depth 16), a pure gain caused by its own switch. GAIN-COUNT counts it.
- What this means for the open core (READING). E-MON3 (via E-DOM) says the e-set never loses a vertex above its top change. NOLOSS-k1
  says more: at k = 1 a mover never loses ANY e-vertex below a common top of two or more. A lexicographic counter needs exactly such
  losses (reset the low bits under a fixed high bit), so NOLOSS-k1 is the precise form of «no counter at k = 1». Its proof is the open
  step. L-NEW 72's box 208 potential, if its Lemma LEVEL transfers to Γ3, is the candidate (Lead 12:08Z).

## 1. Lemma GAIN-COUNT and its corollary (PROVED, lane)
Notation (HOW3 on Γ3, a mover y, its value Ω_t(y) = (Λ, Π, len)). E_t(y) := the e-vertices of Π_t(y). At a step with Λ_t(y) = Λ_(t+1)(y)
and Π_t(y) ≠ Π_(t+1)(y), the change is:
- LOSSY if E_t \ E_(t+1) ≠ ∅;
- a GAIN if E_t ⊊ E_(t+1);
- E-UNCHANGED if E_t = E_(t+1) (the most relevant difference z is then not an e-vertex).
Length-only changes (Π unchanged) are counted by box 100 Addendum A's plateau bound and are left out here.

Lemma GAIN-COUNT. On any interval of states with Λ(y) fixed and no lossy change of y, E(y) only grows by inclusion. So y makes at most M
gains there.
Proof: gains add an e-vertex and lose none; E-unchanged and length-only changes keep E; |E| ≤ M. ∎

Corollary. Let λ(y) be the number of Λ changes of y (≤ n3 − 1, DEPTH-COUNT3), L(y) its lossy changes, and L_s(y), L_d(y) those of e-depth
≤ 1 and > 1. Let U_d(y) be its E-unchanged changes of e-depth > 1. Then the changes of y at e-depth > 1 number at most
  L_d(y) + U_d(y) + M·(λ(y) + L(y) + 1),
and L_s(y) ≤ n3·(S_4(n3) − 1) + n3(n3 − 1)S′_4(n3) (DEPTH-COUNT3 with D1's fix at c = 4, since e-depth ≤ 1 means depth ≤ 4 by CORE-ABOVE).
So, per mover, MD_1(y) ≤ poly(n3) + (M + 1)·(L_d(y) + U_d(y)).
Proof: split the changes of y at e-depth > 1 into lossy (L_d), E-unchanged (U_d) and gains. The gains fall into the stretches between
consecutive lossy or Λ changes, at most λ + L + 1 stretches, each with ≤ M gains (GAIN-COUNT). Then L = L_s + L_d. ∎
- CONJECTURE NOLOSS: for every genome, Σ_y (L_d(y) + U_d(y)) after t0(C), over the movers of each SCC C, is polynomial in N + M. With the
  corollary it gives MOVER-DEEP3 (c = 1, e-form), and with box 102 §2 it gives DEEP3.
- CONJECTURE NOLOSS-k1: at k = 1 (D(G)[C] has a feedback vertex set of size 1), L_d = U_d = 0 for every mover of C after t0(C).

## 2. DATA (mdeep103.py; run103.sh; out/mdeep103_*.out)
Unit: value change of a mover of a non-trivial SCC C after t0(C) at fixed Λ. Sets: box 99's 26 frozen instances; 400 random genomes
(rand191 seed 10001). k := greedy feedback vertex set of D(G)[C] (exact when 1). Counters: lossy_d1, esame_d1 (must be 0 at k = 1 if
NOLOSS-k1 holds), gain_d1, and lostE (an e-vertex z lost as the most relevant difference; must be 0 by R125 (k) E-MON3).
- 26 instances, k = 1 (30 SCCs; 3,074 changes):
  - lossy 1,392 (lossy_d1 0); gain 1,681 (gain_d1 6: WC4_2 1, WC16_2 1, MW8_2 2, MW32_2 2); E-unchanged 1 (esame_d1 0);
  - lostE 0.
  - MWR16_2 alone: 976 lossy and 1,108 gains, all at e-depth ≤ 1.
- 26 instances, k ≥ 2 (12 SCCs; 2,861 changes):
  - lossy 1,486 (lossy_d1 330); gain 884 (gain_d1 113); E-unchanged 466 (esame_d1 53); length-only 25;
  - lostE 0.
  - DHIB26_2804: lossy_d1 199, esame_d1 34, gain_d1 55, max e-depth 6. DWT20_2803: lossy_d1 107.
- 400 random genomes, k = 1 (160 SCCs; 130 changes): lossy 0, gain 24, E-unchanged 97, all at e-depth ≤ 1; lostE 0.
- 400 random genomes, k ≥ 2 (215 SCCs; 1,478 changes): lossy_d1 4, esame_d1 0, gain_d1 0; lostE 0.
- Reading of the split: deep lossy and deep E-unchanged changes, NOLOSS's quantity, are 0 at k = 1 on both sets and occur only at k ≥ 2.
  The random k = 1 SCCs are small (130 changes in 160 SCCs), so the k = 1 evidence rests mainly on MWR (2,084 changes) and WC.

## 3. DEAD and the instances
- DEAD «at k = 1 every mover change has e-depth ≤ 1» (set up from the first, partial run, before the class split): WC16_2, mover 67, t 3:
  Λ = K1, z = e(33, 0) gained, e-depth 16, nothing lost, the switch at that step is 67's own (out/wcdeep_WC16_2.out). WC4_2 has the same
  shape at e-depth 4.
- MW8_2 (out/wcdeep_MW8_2.out): mover 82 gains e(82, 0) at e-depth 2 at t = 12, 18, 24, … (a 2-mover SCC fed by the chain; most of
  these are before its t0). Each is a pure gain. Since the same e-vertex is gained again, it must leave E(82) in between, through a lossy
  or a Λ change: the pattern GAIN-COUNT charges. (Not traced change by change here.)
- For L-RED 66 (through the Lead): NOLOSS-k1's kill would be a k = 1 SCC whose mover loses an e-vertex below two or more common top
  e-vertices. DHIB26_2804 (sha1 2c49fd10) is the k ≥ 2 record (lossy_d1 in its giant SCC, e-depth up to 6).

## 4. Next
- Check L-NEW 72's box 208 Lemma LEVEL against Γ3 with R125's facts when it lands (Lead to send the SHA). If its potential bounds lossy
  changes at k = 1, NOLOSS-k1 may follow.
- Own route (READING): at k = 1 every play from a mover of C runs along a tree path to the feedback vertex R or to an exit, then follows
  R's play (CHAIN-DECOMP3 splits E accordingly). A deep loss at y would have to come from a deep loss at R, or from a tree-path switch
  that drops an e-vertex below a fixed top. The first reduces NOLOSS-k1 to the single vertex R; the second is a Bellman–Ford segment in
  which Howard only improves. This is where the proof attempt should go next.

## Addendum A (L-SI successor 51, 2026-11-12T13:06Z (date -u); append-only): comparison with L-NEW 72's box 208 (Lemma LEVEL; CANDIDATE)
Source: claude/l-new 8db300fe docs/new/N5-LEVEL-box208.md (§0, §1 read here; Lead 13:08Z: «SURVIVED L-RED 66's full attack (three more
checks are pending)»; its Γ3 form box 209 is coming).
- What box 208 claims (CANDIDATE, IDEAL-CYC): with class_t(v) = (Λ_t(v), E_t(v)) and the lowest lagging class m_t, the potential
  Φ_t = (m_t, −|FRONT_t|) never falls. It stalls only on a whole Ξ-cycle. Hence T_CYC ≤ P·(A + 1) + N at k = 1 (Theorem K1-TCYC; it would
  be DEEP-k1), and (P + N)(P + 1)^k for fixed k (FVS-TCYC). General k stays OPEN.
- Comparison with this lane's E-MON3 analysis (box 102 Add. B, box 103):
  - Same genome-only step. Box 208's READING, «the class of a vertex equals the class of its successor on the play, except at an
    e-vertex, where it is strictly higher», is E-DOM (R121 (b)) plus CHAIN-DECOMP. It is the step box 102 Add. B names as the one a DEEP3
    proof must invoke. On Friedmann's G_N it is the step that fails (odd vertices above the exits).
  - Different use. This lane split mover changes into lossy / gain / E-unchanged, and reduced MOVER-DEEP3 to «no deep losses»
    (NOLOSS). Box 208 avoids counting changes by depth at all: a Dijkstra potential on classes bounds the steps directly, and the depth
    statistic never enters.
  - If LEVEL and K1-TCYC transfer to Γ3 (box 209), then at k = 1, and for every fixed k, T3 is polynomial with no DEEP3 / NOLOSS
    premise. This box's NOLOSS-k1 becomes a consequence-shaped fact (DATA consistent with it: deep lossy changes 0 at k = 1), not a needed
    premise.
  - What survives from this lane's chain if box 209 holds: TWO-CROSS (= GATE-RACE, R128) and the per-SCC structure are not needed for
    fixed k. DEEP3 / NOLOSS stay the open premises only for UNBOUNDED k, where box 208 says nothing. There, this lane's k ≥ 2 data
    (DHIB26_2804: 199 deep lossy changes in one SCC of greedy fvs ≤ 24) is the place to look.
- Check to do when box 209 lands: replay box 208's must-0 counters on this lane's 26 frozen instances under HOW3 on Γ3, with L-RED 65's
  engine. Not done here (context limit; handover).
