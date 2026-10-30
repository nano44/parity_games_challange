# R148: the HXS-side attack. HXS at ONE source is quadratic, K(m + 1) at an Odd observer (n 259: 136), so HXS-POLY's per-vertex count is not O(n), but no super-quadratic W-run follows. In SRC-SETTLE's terms the wall is a DICHOTOMY: every family seen is event-rich with source blocks of length about 1 (mkrw, observers, gate) or event-poor with blocks of length about n (runfam, switchbestexp). No corpus game has both 15 source events and a 15-long block. A cubic needs a SHARED ladder that gates every engine step. The design, its exact layer conditions and the two-signal reset it needs are given in §3; NOT built
L-RED successor 35 (Opus 5.5; D1/D18). Lead 2026-10-30 21:38Z, box R148: «the HXS-side attack you propose: a deviator g whose min over
succ(g) rises once per settling wave. Push it super-linearly, ideally super-quadratically, in one W-run.» Written 21:4xZ (date -u).
- Labels: DATA / READING / design (NOT built). Nothing in this box is PROVED except what P-N5-SRC already states.
- Not a TARGET.md claim. G-N5-TIME stays OPEN.
- Sources: docs/red/P-N5-SRC.md (frozen, this lane); docs/red/R143-settle.md §2 (upward feedback); span/mkrw.py and mix/obs2.py docstrings
  (R127, R120).
- Tool: experiments/red/xcn/hxs.py, which prints, per W-run, max_v HXS_F(v), its vertex, owner, out-degree and role (C / D).

## 1. DATA: HXS at one source
| game (n5b SPEC) | n | \|F\| | E^S_F | max_v HXS_F(v) | top vertex |
| --- | --- | --- | --- | --- | --- |
| mkrw LATE=1 K4 m8 | 122 | 44 | 36 | 8 = 2K | reactor deviators (Odd, deg 2), m of them |
| mkrw LATE=1 K4 m16 | 186 | 76 | 68 | 8 | same |
| mkrw LATE=1 K8 m8 | 178 | 88 | 72 | 16 | same |
| mkrw LATE=1 K8 m16 | 242 | 152 | 136 | 16 | same |
| + obs2 observer (OWNER=1) K4 m8 | 131 | 44 | 40 | 36 = K(m + 1) | observer o (Odd, deg m, no in-edges), in D |
| + obs2 K8 m8 | 187 | 88 | 80 | 72 | observer |
| + obs2 K8 m16 | 259 | 152 | 144 | 136 | observer |
| runfam_K40 (L-SI) | 79 | 171 | 8 | 8 | Odd 5, deg 6 |
- Reading:
  - On mkrw, E^S_F ≈ 0.9|F|: almost every transition is a source event. The events are spread over the m reactor deviators, 2K each.
  - An Odd observer whose minimum over the reactors rises at every reactor flip collects them all at ONE source: HXS = K(m + 1),
    quadratic. This is R139's XICH(obs) for the Odd observer, which deviates (σ̄(o) ≠ τ(o)), so it is in D.
  - So «a deviator g whose min over succ(g) rises once per wave step» exists, at quadratic count. The observer has no in-edges, so it
    changes no other Ξ and adds nothing to |F|.
- Corpus (src_corpus.txt, max over the W-runs of a game): the largest (max E^S) × (max source block) is 441, on runfam_K40 (7 × 63).
  No game has max E^S ≥ 15 AND max source block ≥ 15. Families split:
  - EVENT-RICH: mkrw / observers / gate_K64 (E^S up to 63, blocks ≤ 5);
  - BLOCK-RICH: runfam_K40 (block 63, E^S 7), switchbestexp_8 (44, 6), fc_8 (46, 5).

## 2. What SRC-SETTLE says a super-quadratic W-run needs (READING from P-N5-SRC §2-§5)
- |F| ≤ E^S_F + (E^S_F + 1)(n − 1 + m_C), and a source block's normal part has every switch at block time j at W-layer ≥ j + 1.
- So |F| = ω(n²) needs E^S_F = ω(n) source events with blocks of average length ω(n²)/E^S_F. For a cubic family that is E^S ~ n² and
  blocks ~ n: an event-rich engine whose every event is followed by a long block. §1 shows no family does this.
- Layer conditions on a long block of length L that ENDS in a source event at g:
  - (L1) by PLAY-CAUSE^S, Ξ(g) can change at block time j only if ℓ(g) ≥ j + 1. So the engine's sources sit at W-layer ≥ L.
  - (L2) for the next block to be long again, low layers must switch again. So g's change must reach a LOW vertex, through a deviator h
    at low W-layer whose Ξ-play runs up to g (R143's upward head). h ∈ D changes in the same event.
  - (L3) a vertex whose (σ, σ̄)-play already passes h changes its Ξ instantly, with no switch. So the ladder re-waves only if its vertices
    point AWAY from h when the event comes.
- (L3) is the obstacle every one-W-run family hit. A ladder x_1 … x_L with x_i → {x_(i−1), z_(i−1)} waves once when h rises (x_i
  switches to x_(i−1) at time i). After that every x_i points down the ladder, and the next rise of h is instantaneous.
  - A re-wave needs a RESET: the z-rail must rise above the ladder between two h-rises, which takes one transition, since every x_i sees
    its z_(i−1) at once.
  - So each wave costs two alternating source events (h, then z): the Lead's (a) three-signal pattern, inside the HXS frame.

## 3. Design: a gated shared ladder (NOT built)
- Parts:
  - an engine with Θ(n²) steps (mkrw: K pivot climbs × m reactor steps);
  - ONE ladder of length L (§2) with base deviator h and reset rail z;
  - two Odd observers: o_h (base) and o_z (rail), each a min over reactor groups;
  - a gate: each reactor step r_j → r_(j+1) must ALSO read the ladder top T, through an Odd q_(j+1) → {T, r_j} whose minimum caps the
    improvement of r_(j+1) until T has risen.
- Cycle per engine step: reactor flip → o_h rises (source event) → wave up the ladder, L transitions, no source event → T rises → the
  gate q lifts → next reactor flip → o_z rises → reset (1 transition) → … So |F| ≈ (number of engine steps) × L ≈ K·m·L ~ n³/27 if every
  step waits.
- Exact conditions that are not yet shown realisable in N5:
  - (G1) W-ties. Every ladder edge must be W-tight on both rails at every state (P-N5-SETTLE Claim RG′: S4a picks only W-tight arena
    edges), so W(x_(i−1)) = W(z_(i−1)) for all i, in one W-run (λ_W fixed). With the top priority at a W-cycle node c this is
    length-only: two rails of equal W-length.
  - (G2) the gate must bind for exactly the NEXT reactor. T is shared, so its value after step j must cap q_(j+1) and no other. The
    caps then need a strictly increasing ladder of Ξ-values at T, one per engine step. The observer supplies them: Ξ(o_h) after step j is
    the next unflipped reactor's value. But the cap passes through the ladder's path, and its path sets must preserve the order (E1.12's
    proviso).
  - (G3) ARENA-MAX look-ahead (R140, R143 §5 (b)): S4a's W-optimum may let r_(j+1) shortcut the gate if a W-better route exists in the
    arena. rel2's delay chains met this ("rises ≥ 2 apart"). The gate must not be a W-shortcut.
  - (G4) Lemma ADD (R144): costs add for releases of one closure. Whether ADD forbids the multiplication here, with one ladder reused
    by every step, is exactly the open question. ADD bounds Σ R°_Φ ≤ |F| − SB, which is not a bound on |F|, so it does not forbid it as
    stated.
- If (G1)-(G3) are realisable, the result is a cubic W-run: still polynomial, so not a kill of N5, but it breaks the quadratic wall and
  shows that HXS-POLY needs more than per-vertex counting. Nested ladders (a ladder gating a ladder) would then be the route to higher
  degree.

## 4. Status
- Box R148 is partial: data (§1), a reduction-side reading (§2) and a design (§3), with nothing built and no kill.
- HXS-POLY is unrefuted. HXS at one vertex is Θ(n²) on the observer family. Every family has |F| = O(n²).
