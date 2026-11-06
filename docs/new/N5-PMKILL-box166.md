# Box 166 N5-PMKILL: the proof attempt of PM breaks exactly at the key-rule step, and the failing configuration is realizable — CONJECTURE PM is DEAD (instance: one degree-2 IDEAL-ACYC genome, N 15, T 14, a mover with 4 Ξ-descendants moves 6 times > 5)
L-NEW successor 54, 2026-11-05 (date -u: see the commit). Lead brief BOX 166 (19:36Z): a lane proof attempt of PM («moves(x) ≤
(deg(x) − 1)(1 + desc(x))», box 165) at desc 4 by induction on desc, naming every step that uses the key rule, and handing over the
failing configuration as a query if the proof fails. Labels: PROVED (lane, unrefereed) / DATA / DEAD (instance) / READING. Model:
RESULTS R104 (P-IDEAL-FLIP §0); R105 as landed. Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Answer
- DEAD CONJECTURE PM (box 165), and with it the route «T ≤ Σ_x (1 + desc(x))».
  - Instance: experiments/new/box166/out/KILL_PM_compose_dd_d5_F14.json (sha1 c025a4b6). IDEAL-ACYC, every mover of degree 2, N = 15,
    levels 0-4, not ISO, not an 𝓛^R ladder. Real run from its start: T = 14.
  - Mover 12 (level 4) has Ξ-descendants {10, 11, 13, 14} (desc 4) and moves 6 times (steps 1, 2, 5, 8, 9, 10). PM's bound is 5.
  - Checks: box166/verify_kill.py (well-formed: W-targets exactly one level down, distinct gates and ranks, acyclic Ξ-graph).
    box150/check.py on the file: XSIM 0 (two independent simulators agree state for state); every R105 check (MONO, XI-NEW, RISE,
    CHAIN, KEYFLIP, DECR, TOP-MONO, RANK-BOUND, RESTR, ICHARGE, REC) reports 0 violations, so the run is a legal R104 run.
- Where the induction breaks (§1-§2): the only step that uses the key rule is «a mover with a strictly better option and the key
  preference on its current option is HELD». With KP_t free (Lemma FREE-KP) the dynamics is the key-free one, where PM fails at desc 4
  (box 165 §4). Moreover TWO independent key bits already suffice (§2, exact): 64 assignments of a 5-mover key-free violator to two free
  bits give 6 moves at desc 4; one bit gives at most 4.
- The kill (§3): a real clock genome (L-RED's dd_d5_F14, claude/l-red 002f7cd1 experiments/red/r197/lag) supplies the two bits as key
  orders of two pairs of its movers. The violator sits on top: its movers W-point to those pairs, and its Ξ-graph is disjoint from the
  clock's, so no descendant is added. The clock's run is not affected by the violator.
- READING (what survives): the kill does not lengthen runs. The violator's extra moves are paid for by the clock's key flips (KF of
  mover 12 = 14 = T). So it refutes the per-mover Ξ-bound, not polynomiality: T is still the clock's 14. A per-mover bound must
  count the key flips that reach a mover, i.e. W-side information. That is R105 KEYFLIP's quantity, which box 165 found not governed
  by the Ξ-position. Both pure forms are now out: Ξ-only (PM, DEAD) and KF-by-Ξ-position (unsupported).
- Still open and routed (Lead 19:36Z): PM on 𝓛^R_d (2-wide R197 ladders) and on R109's 𝓛_d. The composition does not stay in these
  classes: it adds movers to existing levels, while 𝓛^R has exactly 2 movers per level. On 𝓛^R every level is one pair, so a mover
  reads exactly one bit (its level − 1 pair order). The one-bit model gives ≤ 4 at desc 4 (§2), but different levels give different
  bits, so 𝓛^R is not covered by the one-bit bound either.

## 1. The induction and the step that uses keys (PROVED (lane) parts)
- Setting: degree 2, x with options a, b, move times t_1 < … < t_M. Moves alternate between a and b.
- RETURN (PROVED (lane), no keys). For i ≥ 2, if x moves to o at t_(i−1) and away from o at t_i, then Ξ(x, ¬o) rose strictly between
  the states s_(t_(i−1)−1) and s_(t_i−1). So V(z) rose strictly in that window, z := xt(x, ¬o), a Ξ-descendant (z ≠ X).
  Proof: o was strictly better at s_(t_(i−1)−1) and ¬o strictly better at s_(t_i−1). Ξ(x, o) is non-decreasing (CHAIN-UP, box 164 §1),
  so Ξ(x, ¬o) must have risen; Ξ(x, ¬o) = ε(x, ¬o) + V(z) by R105 ENC. ∎
  So moves(x) ≤ 1 + R_a + R_b, R_k := #steps at which V(xt(x, k)) rises (with the windows disjoint and alternating). MERGE (box 165)
  removes the rises common to both chains.
- Induction hypothesis candidates on the descendants:
  - (H-moves) PM for every descendant. It does not bound R_k: V(z) also rises when z's own descendants rise.
  - (H-values) PMV «VR(z) ≤ 1 + desc(z)», VR := #value rises. DEAD (experiments/new/box166/vr.py): dd_d5_F14 mover 6 (desc 7) has
    VR 10 > 8; 16 violating movers on 256 files (nd2_d5_F12 mover 5: desc 6, VR 9; big_d3_k3_W3 mover 8: degree 3, desc 1, VR 5 > 4).
  - So no Ξ-only induction hypothesis closes the step, even at desc 4.
- The key step. x moves at t iff (A) its other option is strictly better under s_(t−1), and (K) KP_(s_t)(x) is that option. (A) is
  Ξ-side (RETURN, MERGE, IM). (K) is the only use of the key rule. A proof of PM would need (K) to block the returns that (A) allows
  beyond 1 + desc.
- Lemma FREE-KP (PROVED (lane)). If KP_t(x) ∈ {a, b} is replaced by an arbitrary value for every mover and step, the runs are exactly
  the key-free paths in which, at each step, any subset of the unhappy movers switches (at least one if the run continues).
  Proof: under (A), a held mover is one with KP = its current option and a switching mover one with KP = the other option; every
  subset is realized by a choice of KP, and a happy mover never switches whatever KP is. ∎
  So any proof of PM must use correlations of KP across movers and time, and box 165 §4 shows that without them PM fails at desc 4.

## 2. How many independent key bits the failure needs (exact; box166/bbit.py, patterns.py, onebit.py)
- Violator V: box166/out/keyless_pmviol_N5_d4_m7.json (sha1 8b0619cc; = box165/out, key-free max 7 at desc 4). Its key-free schedule
  (freekp.py, 15 single switches, mover 2 moving 7 times) needs 5 movers held for up to 9 steps while unhappy.
- B-bit model: KP_t(x) = b_t[i(x)] XOR sign(x), or a constant; b_t ∈ {0, 1}^B free at every step. Max moves of mover 2 (desc 4,
  bound 5): B = 1: 4 (one bit, unlimited flips; with ≤ k flips, k = 0..4: 1, 2, 3, 4, 4); B = 2: 6 (64 winning assignments,
  out/patterns2.json sha1 aed2f8c0); B = 3: 7 (= key-free).
- A 2-wide ladder level gives one bit (the order of its pair). The kill needs two independently flipping key orders feeding the
  violator.

## 3. The composition that realizes it (exact search; box166/compose2.py)
- Clock C: any corpus genome and start. A bit = the order of two movers p, q of one clock level under the new clock state. A violator
  mover reading bit i with sign sg sits one level above, with option 0 W-pointing to p and option 1 to q (reversed if sg = 1); a
  constant reader W-points both options to one mover and its own gates decide. The violator's Ξ-targets stay inside V and its ranks
  sit above all clock ranks, so the clock's run is unchanged and desc(x) is unchanged for every violator mover.
- Search: every winning 2-bit pattern × ordered pairs of distinct clock bit-sequences × 32 violator starts, re-simulated. The first
  hit on dd_d5_F14 (4 random clock starts tried) was rebuilt as one genome and re-run by the plain simulator: 6 moves, desc 4.
- Run of the kill (state = movers 0..14; mover 12 is the violator's mover 2):
  0 110111111000000, 1 111111101110101, 2 111111000110001, 3 111110010110011, 4 111110110110011, 5 111100100110111,
  6 010000000111110, 7 010001011111110, 8 010001111011000, 9 000011101011101, 10 001011000011001, 11 001010010011001,
  12 001010110011001, 13 001000100011001, 14 001000000011001.
  moves per mover [1, 1, 3, 1, 3, 3, 7, 7, 3, 2, 1, 1, 6, 2, 3]; KF per mover [0, 0, 2, 2, 3, 3, 6, 6, 14, 14, 0, 2, 14, 14, 2].
- Box 165's searches missed it: they were local climbs and never put two clock key orders under one Ξ-shallow block.

## 4. Next (Lead decides)
- Tell L-RED (R206) and L-SI (box 71 item (0)): PM is dead in general. Their 𝓛^R / IM-frame queries remain meaningful only as «PM
  restricted to the class».
- What the kill teaches: per-mover bounds must charge to KEY flips that reach the mover (W-side) and to Ξ-returns jointly. A candidate
  that survives this instance (unchecked; it is the next screen if routed): moves(x) ≤ 1 + min(KF_x, R_x), with R_x := the number of
  Ξ-return opportunities (RETURN). That gives nothing polynomial by itself, since KF_x ≤ N·T (R105).
