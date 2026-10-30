# R136: the pattern clock. Fresh route patterns cost switches on the route: PAT(X, g) ≤ 1 + Σ switches of the route's Even vertices in the W-run, so a cheap pattern clock IS a long W-run. Fleet families give PAT = SERVED = K (the pivot). A shared clock (both gates of X enter T's play) dies by Lemma ALT-ESCAPE. No kill
L-RED successor 33 (Opus 5.5; D1/D18). Lead 2026-10-30 12:02Z: "R136 ... the adversary side of the same count. Try to make the FRESH route
patterns cheap: an Even 'pattern clock' that supplies a new (X, g, route-pattern) triple per upward wait, using fewer than exponential
resources ... how many distinct route patterns per signal route N5 can cycle through inside one W-run while Ξ stays monotone ... polynomial-
versus-exponential data on growing families, and the obstruction if it stays polynomial." Written 2026-10-30 from 12:05Z (date -u).
Labels: PROVED (lane) / DATA / READING. Not a TARGET.md claim. G-N5-TIME OPEN. Definitions: R135 §4 (self-routed block, route π, pattern).

## 1. Counter (experiments/red/pclock/patcount.py, n5b SPEC)
Definitions, per W-run F (τ constant) and per pair (X, g):
- PAT_F(X, g): the number of distinct Even patterns on π over the self-routed blocks of (X, g).
- SERVED_F(X, g): the number of switches X → g made after a self-routed block of (X, g) in F, counting one per block episode. Each one is
  an upward wait that was served.
The counter also prints the busiest route vertex at the max-PAT pair. It checks online that PAT ≤ 1 + (switches in F so far of the Even
vertices seen on the routes), and prints "PAT-BOUND VIOLATION" if that fails. No violation occurred on any run below.

## 2. Lemma PAT-SW (PROVED, lane; elementary)
- Statement. PAT_F(X, g) ≤ 1 + Σ_{v ∈ U} SW_F(v).
  - U is the set of Even vertices on the routes of (X, g) in F.
  - SW_F(v) is the number of switches of v in F.
  - Hence SERVED_F(X, g) ≤ PAT_F(X, g), by R135 Lemma WAIT-CYCLE (no served wait reuses a pattern), and SERVED_F(X, g) ≤ 1 + |U| · max_v
    SW_F(v).
- Proof.
  - A pattern is the tuple (v, σ(v)) over the Even vertices v on the play π from g to X.
  - Two blocks with different patterns differ in σ(v) for some v ∈ U, so some vertex of U switched between them.
  - Order the distinct patterns by first appearance. Each new pattern needs at least one switch of a vertex of U since the previous new
    pattern. □
- Consequence (READING). A pattern clock with super-polynomially many fresh patterns is a vertex set U ≤ n whose members switch
  super-polynomially often inside one W-run. By pigeonhole that is the same as a super-polynomial W-run. The triple count therefore gives
  the adversary no cheaper resource than the original target.
  - For the proof side it is a recursion: SW(X) ≤ (lateral / unblocked part) + Σ_g SERVED(X, g) ≤ (lateral) + deg(X)·(1 + Σ_{v ∈ U(X, ·)}
    SW(v)).
  - It closes to a polynomial only if the route-dependency X → U(X, ·) is shallow, or the multiplicities are bounded.
  - In a dependency chain of depth d with factor ≥ 2 per level it allows 2^d. The ladder is the shape of that recursion.

## 3. DATA: growing families (mkrb = R124's bidirectional chain, the fleet's longest quadratic W-runs)

| family | n | iterations | self-routed blocks | served waits | max PAT | max SERVED | clock vertex (its switches) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mkrb K 2 m 16 | 78 | 68 | 1027 | 61 | 2 | 2 | hp |
| mkrb K 4 m 8 | 78 | 72 | 519 | 57 | 4 | 4 | hp (3) |
| mkrb K 4 m 16 | 102 | 136 | 2055 | 121 | 4 | 4 | hp |
| mkrb K 8 m 8 | 126 | 144 | 1039 | 113 | 8 | 8 | hp (7) |
| mkrb K 8 m 16 | 150 | 272 | 4111 | 241 | 8 | 8 | hp (7) |
| bidir_K8_m32 (pin) | 198 | 528 | 16399 | 497 | 8 | 8 | hp (7) |
| mkrb K 12 m 16 | 198 | 408 | 6167 | 361 | 12 | 12 | hp |
| mkrb K 16 m 16 | 246 | 544 | 8223 | 481 | 16 | 16 | hp |
| latew_K8_m32 (pin) | 370 | 280 | 279 | 1 | 8 | 1 | – |
| tiedrb_K8_m16 (pin) | 270 | 153 | 151 | 1 | 8 | 1 | – |

- max PAT = max SERVED = K. It is independent of m, and the pattern clock is the pivot h′ with K − 1 switches: PAT-SW is tight there.
- Served waits in total grow as about K·m (the reactor waves), each pair served at most K times. Everything is polynomial: linear per
  pair, quadratic in total.

## 4. A cheap clock: let T's own play be the pattern (pclock/mkte.py), and why it dies
- Design. Every leader A_j (2 ≤ j ≤ k − 1) of dg_k reads level j − 1 through Odd gates h(A_j, c) → {q → u(j − 1, c) (τ), e(j, c)}. The
  escape e(j, c) is an Odd vertex with an odd priority between the level-j and level-(j+1) markers and the single successor T.
  - While T's play passes A_j, the route e → T → … → A_j is T's play.
  - Its pattern is the upper ladder's choices along that play, a counter whose patterns need not recur. WAIT-CYCLE does not forbid this.
- DATA (dgstat + patcount on n5b; te_8: xeng identical, Oink zlk OK with strategies verified):

  | k | iterations | served waits | Ξ cycle nodes |
  | --- | --- | --- | --- |
  | 3 | 4 | 1 | e2_0 |
  | 4 | 5 | 0 | e2_0, e3_1 |
  | 6 | 7 | 0 | e2_0, e3_1, e4_1, e5_1 |
  | 8 (pin) | 9 | 0 | e2_0, e3_1, …, e7_1 |

  Odd closes the cycle through A_j's CURRENT gate's escape (h → e → T → … → A_j → h). τ changes once.
- Lemma ALT-ESCAPE (PROVED, lane).
  - Setting. X has gates g_0, g_1 with escapes e_0, e_1 (fixed vertices). There are two events, in the spirit of R135 §4 (a):
    - a self-routed block of g_0 while X is on g_1, and later a self-routed block of g_1 while X is on g_0;
    - at each event BOTH escapes' plays reach X along the same continuation π_t (a shared entry, as in mkte: e_0, e_1 → T).
  - Claim: the two events are incompatible.
  - Proof.
    - Write A_t for the most relevant vertex of π_t ∪ {X} above the cycle node c* of Ξ_t(X), and M(·) for the most relevant vertex above c*.
    - At an event for gate c, the block (R135 §4) needs M(e_c, A_t) to be odd or absent.
    - Odd must not close the cycle through the current gate's escape (g_(1−c) → e_(1−c) → π_t → X → g_(1−c)). If it did, Ξ_t(X) would not
      be c*-valued, against (a). So M(e_(1−c), A_t) must be even, which makes the cycle not better for Odd.
    - The two maxima differ, so an escape attains one of them. Case analysis (irrelevant escapes count as lowest):
      - (i) e_c is odd, and e_c ≻ A_t ≻ e_(1−c) with A_t even;
      - (ii) e_(1−c) is even and e_(1−c) ≻ A_t, and either e_c is odd with e_c ≻ A_t, or e_c ≺ A_t with A_t odd or absent.
    - Apply this to c = 0 and to c = 1:
      - both escapes odd: (i) twice gives e_0 ≻ e_1 ≻ e_0;
      - both even: (ii) twice gives e_0 ≺ A ≺ e_1 and e_1 ≺ A′ ≺ e_0;
      - one even and one odd, or an irrelevant one: one of the two events has neither (i) nor (ii) available.
    - Every case is a contradiction. □
- So a shared pattern clock cannot serve both gates of one vertex. Each gate of X needs a signal route with its own entry, and each such
  route needs its own fresh patterns, which by PAT-SW means its own switching vertices.

## 5. The obstruction, stated (READING)
- Per upward wait the adversary pays one switch on that gate's private route (PAT-SW + WAIT-CYCLE). Routes of X's two gates cannot share
  their entry (ALT-ESCAPE).
- If the routes of different vertices could share switching vertices freely, the recursion of §2 would allow 2^depth. The open question is
  exactly whether one switching vertex can feed fresh patterns to the routes of many waiting gates at once, each gate with a different
  entry point.
- Tried once (Addendum 1, dead): escapes entering one shared chain at DIFFERENT depths (π_0 a proper suffix of π_1). ALT-ESCAPE assumes the same continuation;
  with nested entries the maxima A_t^(0) ⪰ A_t^(1) can differ.

## Addendum 1 (2026-10-30 12:25Z, date -u): nested entries tried once
- pclock/mkte.py NEST=1: the copy-1 escape enters T's chain one level lower (→ A_k), so the routes are nested, not shared.
- k = 4, 6, 8: 4, 6, 8 iterations, 0 served waits. Ξ cycle nodes are the escapes again (e2_0, e3_1, …, e7_1). τ changes once.
- It dies before ALT-ESCAPE is even needed. While X's current gate's own escape route reaches X with an odd-dominant maximum, Odd closes
  that low cycle (R135 §4, the t2 < t1 branch: one wait at most).
- So §5's "not tried" item is now tried in this one form. Nested entries with the current gate's route avoiding X remain open.

- DONE:
  - experiments/red/pclock/patcount.py (PAT / SERVED / clock vertex, with an online PAT-SW check).
  - pclock/mkte.py (shared T clock), pin pclock/instances/te_8 (xeng identical, Oink OK).
  - check.sh "R136" section.
- FINDINGS:
  1. PROVED (lane) Lemma PAT-SW: fresh patterns ≤ 1 + switches of the route's Even vertices in the W-run. A cheap pattern clock is a long
     W-run, so there is no new resource.
  2. DATA: on the fleet's longest W-runs (mkrb), max PAT = max SERVED = K, linear. The clock is the pivot h′, independent of m. Served waits
     in total ≈ K·m.
  3. PROVED (lane) Lemma ALT-ESCAPE: the two gates of one vertex cannot share a pattern clock with the same continuation. The shared T clock
     te_k dies: 0-1 served waits, k + 1 iterations.
  4. READING: the remaining kill route is a switching vertex that feeds DIFFERENT-entry routes of many gates; nested-depth entries are
     untried. No kill of G-N5-TIME or N5.
- NEEDS: none from the owner. Lead: PAT-SW and ALT-ESCAPE to L-NEW 38 with WAIT-CYCLE if useful.
