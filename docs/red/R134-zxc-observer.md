# R134: one gap vertex climbs Ξ at almost every transition of a Θ(n²) W-run. R120's wave observer on the one-world mkr has ZXC_F(obs) = Km + K + 1 (589 = 1.6n of |F| = 612 at n 368). But ZXC ≤ |F| by definition, so per-vertex ZXC cannot exceed the W-run, and the climbs feed no LATE′ adoption unless the W/Ξ divergence lies in a PRIVATE prefix (Lemma GAP-IN-PREFIX, lane proof). The circle amplifies only through |F| itself, which is R124's third-factor wall. DATA + READING
L-RED successor 32 (Opus 5.5; D1/D18). Lead 2026-10-30 07:34Z: "R134 ... Make ONE gap vertex z climb Ξ many times inside one W-run, aiming at
≥ n² and ideally exponential, while z stays in the gap ... Start from cr_n80 (l-new box74/inst) ... plus your wdepth / latew devices. If it
stalls, give the exact obstruction in terms of TWO-SOURCE / PREFIX." Written 2026-10-30 from 08:15Z (date -u). Labels: PROVED (lane) /
DATA / READING. Not a TARGET.md claim; G-N5-TIME OPEN.

## 1. Definitions (L-SI box 51 §3, l-si 7dd85b02; read only)
- Z_s: the gap vertices at state s, those with Ξ_s(z) ≠ W_s(z), so Ξ_s(z) ◁ W_s(z) by XW.
- ZXC_F(z): the transitions s → s + 1 of a W-run F with z ∈ Z_s and Ξ_(s+1)(z) ▷ Ξ_s(z).
- GAP-CLIMB: LATE′ adoptions ≤ Σ_z d_E(z)·ZXC_F(z).
- Counter: zxc/zxc.py (new, on L-NEW's n5x; --lzc for N5-LZC). It prints per game the top vertices by ZXC_F(z) in their W-run, and TXC
  (the climbs with W(z) fixed).

## 2. DATA: ZXC of one vertex at the trivial ceiling |F|
- Family: span/mkrw.py K m (the one-world mkr of R127, no late devices) plus R120's Even wave observer (mix/obs2.py OWNER=0 ABOVE=a):
  obs → {y_j → r_j}, with markers q_j just above the reactor a-markers. obs follows the reactor wave and switches at almost every
  transition. Its Ξ and its W both rise at each switch, and the gap (pivot level: Ξ through the η-ladder, W through the W-ladder) never
  closes before the end.
  | K | m | n | iterations = |F| (one W-run) | ZXC_F(obs) | Km + K + 1 | TXC_F(obs) | next vertex (ZXC) |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | 4 | 16 | 128 | 76 | 69 | 69 | 0 | Tp_i: 8 |
  | 8 | 32 | 248 | 280 | 265 | 265 | 0 | Tp_i: 16 |
  | 12 | 48 | 368 | 612 | 589 | 589 | 0 | Tp_i: 24 |
- So ZXC_F(z) = Θ(n²) for a single z: 589 = 1.6n. All of it is WZ (W rises too): the observer's own switch lies on the shared prefix of
  its two plays (R131's mechanism).
- Checks on K 4: N5-LZC gives the same 76 / 69 (zxc.py --lzc); n5b = n5.py state by state (xeng.py); Oink zlk OK on n5b's solution.
  check.sh gate: K 4, m 16 → obs 69 / 76.
- cr_n80 (l-new box74/inst) is BREADTH (ρ ≈ |Q|·|F| with |F| = 15). It cannot give a large ZXC for one vertex, because ZXC_F(z) ≤ |F|.
  I did not climb it further.

## 3. Lemma GAP-IN-PREFIX (PROVED, lane), and why the observer's climbs buy no adoptions
- Statement. Let y be Even, a = σ_t(y), and z another successor. Suppose the W_t-plays and the Ξ_t-plays (Odd's best reply) from z and
  from a have the same private prefixes, i.e. both pairs first meet at the same vertex x along the same vertices. Then
  W_t(z) ▷ W_t(a) ⟺ Ξ_t(z) ▷ Ξ_t(a). So (y, z) is not BLOCKED at t.
- Proof. This is §2's Lemma PREFIX of R132, applied once to the W-plays and once to the Ξ-plays. In both, the comparison is decided by the
  same prefix symmetric difference (and the same prefix lengths), whatever the two (possibly different) tails from x are. □
- Corollary. A BLOCKED edge, hence every late or LATE′ adoption, needs a W/Ξ divergence (an Odd q with BR_t(q) ≠ τ(q)) on the private
  prefix of z or of a. In R127's devices that divergence is c_J itself (honest r_J against τ yh_J). In R131's family it is c_(J+1),
  below z_J.
- DATA: readers R → {obs, obsB}, with obsB a second observer on the same reactors (markers reversed, shifted, random or on a subset;
  random priorities and owners). zxc/obsread.py, 3 seeds × 10 min, 1517 draws, every one a single W-run: REP(R) = 0 and no late
  adoption at R in every draw. The two observers' plays share the reactor chains down to the pivot, where the divergence sits.

## 4. READING: the exact obstruction (TWO-SOURCE / PREFIX / GAP-IN-PREFIX)
- ZXC_F(z) ≤ |F| for every z, by definition (one climb per transition). The observer reaches it. So a large ZXC for one vertex is not the
  bottleneck. The bottleneck is |F|.
- To turn climbs into LATE′ adoptions of (y, z), the climbs must be released through a divergence on z's private prefix
  (GAP-IN-PREFIX). Between two adoptions, y must leave z, which needs a rise of the alternative a's W on a's private prefix
  (TWO-SOURCE / PREFIX).
- So LATE′(y, z) ≤ min(ZXC_F(z), WCH on a's private prefix) + 1 ≤ |F| + 1. The data's best is R127's K per edge.
- Summing over edges gives LATE′ ≤ m_E·(|F| + 1). With FW-R*′ (|F| ≤ (n − 1)(R*′ + 1)) that is box 74's circle, gain (n − 1)·m_E.
- The circle can only amplify if |F| itself grows. A W-run longer than about n² is R124's third factor, blocked by R108 §4's reused
  waiting gate. The observer shows the other side: inside a Θ(n²) W-run one vertex can carry Θ(|F|) climbs and switches at no extra
  cost. Amplification needs a sub-run (a nested clock) that a single gate reopens Θ(n) times. That is the same wall, met from the ZXC side.
- "ZXC ≥ n²" for one vertex is therefore EQUIVALENT to a W-run of length ≥ n². Nothing known exceeds n²/77, and the observer family
  stays below n²/200.

## DONE / FINDINGS / NEEDS
- DONE: zxc/zxc.py (ZXC / TXC per W-run, N5 and N5-LZC), zxc/obsread.py (two-observer reader search), observer data (K 4, 8, 12),
  check.sh gate, this note.
- FINDINGS:
  1. DATA: one gap vertex climbs Ξ at all but 2K − 1 transitions of a single Θ(n²) W-run: ZXC(obs) = Km + K + 1, 589 = 1.6n at n 368.
     Two engines agree, Oink OK, and N5-LZC is the same.
  2. PROVED (lane): GAP-IN-PREFIX. A block needs a W/Ξ divergence on a private prefix. 1517 two-observer readers: 0 REPEATs.
  3. READING: ZXC_F(z) ≤ |F|, so a super-quadratic ZXC is the same as a super-quadratic W-run. The circle's gain is realised only
     through |F|, so the wall is R124 / R108 §4 again.
- NEEDS: none from the owner.
