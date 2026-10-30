# N5-BIP (box 89): BIP-POLY. Anatomy of Even-side releases under a frozen σ̄ (lifters sit below the first Odd deviation, are plain switches, dependency depth ≤ 2). CONJECTURE BIP-REL-1 (each Even edge is released at most once per frozen stretch): 0 violations on 1132 corpus runs and the quadratic pins; the non-strict form is DEAD (ueonce_n27). Theorem BIP-RED (lane, under premise [SUB]): |F| ≤ SB_F + (SB_F + 1)(n − 1)(R°+1) + FL_F, with R° the most strict releases in one frozen stretch; with BIP-REL-1, R° ≤ m_E. So W-runs are polynomial if BIP-REL-1, SB-POLY (σ̄ changes per W-run) and FL-POLY hold
L-NEW successor 38 (Opus 5.5), D14 / D18, Lead reading L40. Lead 2026-10-30 14:34Z: «BOX 89 = BIP-POLY. Bound the Even-side releases
under a frozen σ̄, starting from ARENA-MAX (R140, l-red 47000632), BIP-MON and NO-DEV … find exactly what releases each EVEN release, and
whether a potential in G_ρ … strictly drops per release, bounded by a poly-size label set. If arbitrary-order label-correcting is
exponential …, state which property of the τ-optimiser order (ii) excludes the bad orders. Otherwise give the instance.» Written
2026-10-30 14:35Z-15:20Z (date -u). Working note, unrefereed. Labels: PROVED (lane) / CONJECTURE / DEAD / DATA / READING. Not a TARGET.md
claim. G-N5-TIME OPEN.

## 0. Sources and setting
- docs/new/N5-ONEP-box88.md (BIP(ρ, τ), BIP-MON, NO-DEV, the two mechanisms O / B); RESULTS R88 (BLOCKED, R*_T, GP*, FW-R*), R89
  (GP*-RUN); L-RED R140 (l-red 47000632, Lemma ARENA-MAX: «W_{t+1}(v) ≥ val(ρ, τ_t)(v) for every Even strategy ρ of the arena H_t»,
  relayed by the Lead; I did not re-derive it).
- Opened (D18, shortest paths): [Ral] T. Ralphs, IE411 "Graphs and Network Flows", Lecture 11 (Lehigh), slide 3: «Generic – O(n²C)
  iterations (recall d(j) bounded by nC and −nC) – No specified method for selecting an arc violating optimality conditions»;
  «Modified – By repeatedly scanning arcs in a fixed order, we can get a strongly polynomial time algorithm.» (PDF text read.) NOT
  opened: Johnson 1973, Kershenbaum, Shier-Witzgall (exponential examples for specific orders, per a search-result snippet of a
  Bertsekas paper; not cited as a source).
- FROZEN STRETCH Φ := a maximal interval of states of a W-run F on which σ̄_t is constant (= ρ). On Φ, N5 is BIP(ρ, τ) (box 88).
  A STRICT release in Φ is a late adoption of (y, z) whose blocking state also lies in Φ. R°_Φ counts the transitions of Φ carrying one.
  SB_F := the transitions of F at which σ̄ changes, so F has SB_F + 1 frozen stretches and SB_F transitions between them.

## 1. Anatomy of Even-side releases (DATA, box89/bipprobe.py)
- For every EVEN release (y, z) in a frozen stretch, with last block q: the LIFTERS are the Even vertices x on z's (σ_q, ρ)-play whose choice
  differs at the release.

  | instance | releases | lifters after / before the first deviation o (ρ(o) ≠ τ(o)) | lifters that were releases | Ξ(z) values in [q, t] | dependency depth |
  | --- | --- | --- | --- | --- | --- |
  | obs_K12_m24 | 23 | 276 / 0 | 0 | 2 | 1 |
  | fx K = 4, m = 16 | 7 | 52 / 0 | 0 | 2 | 1 |
  | corpus (1132 runs, bip_*.txt) | 531 | 386 / 199 | 9 (of 585) | ≤ 2 | ≤ 2 |

- So on the quadratic frozen families a release is lifted by a one-player climb INSIDE the subtree of ρ(o) below the first deviation. The
  climb uses plain switches (never releases), and it raises Ξ(z) exactly once. In the corpus, W(ρ(o)) changes between block and release in
  336 of 531 cases.
- Answer to "what releases an EVEN release": a plain Even climb below the poison. The poison itself stays (box 88: poison kept 25/25 on obs).

## 2. CONJECTURE BIP-REL-1, and the label-correcting reading
- CONJECTURE BIP-REL-1: in every frozen stretch Φ of every W-run of N5, each Even edge (y, z) has at most one strict release. Hence
  R°_Φ ≤ m_E.
- DATA (box89/relpe.py, STRICT=1; relpes_*.txt): corpus 1132 runs, max strict releases of one edge per frozen stretch = 1 (0 violations).
  Max R°_Φ 40 (grow_K40_n373). Pins: obs_K12_m24 1, latew_K16_m32 1 (its 16 releases of one edge fall in 16 different frozen stretches),
  gate_K64_n581 1.
- DEAD: the non-strict form (blocks counted anywhere in F, releases inside one frozen stretch).
  - si/root/instances/ueonce_n27.pg (sha1 c90d5ab8…, its S3 start): edge (10, 23) released twice in one frozen stretch; with STRICT=1 it
    has 0 strict releases.
  - new/box48/instances/long121_n40.pg (S3 start): 2 non-strict, 0 strict.
  - In both, the blocks came from an earlier stretch with a different σ̄. That is mechanism O feeding mechanism B.
- READING ([Ral], D18). In label-correcting terms, ρ fixes the arc costs. BIP-REL-1 says each arc is "re-opened" (blocked → offered →
  taken) at most once per stretch. Generic label correction is only pseudo-polynomial (O(n²C)), and the VJ path-set weights make C
  exponential. Polynomiality comes from scanning in rounds. Inside a stretch, GP* plus ARENA-MAX is the round structure: S4a takes the
  arena's one-player optimum, a whole Bellman-Ford pass over the offered arcs (R140). A release starts a new pass. So the property of the
  τ-optimiser order that excludes bad orders is ARENA-MAX: no "locally best but globally delayed" relaxation is ever postponed (R140
  NO-LOCAL-DELAY). What can still be postponed is an arc whose ρ-value is poisoned, and BIP-REL-1 says each such arc is postponed at most
  once per stretch. Not proved.
- Proof attempt (not closed). Suppose (y, z) is released at t1, left at s > t1 for h, re-blocked at q2 > s and released again at t2. Then
  Ξ_s(h) ▷ Ξ_s(z), ARENA-MAX gives W_(s+1)(h) ⊵ W_(s+1)(z) (when z's τ-play avoids y), and at q2 W(z) ▷ W(σ y) with Ξ(σ y) ⊵ Ξ_s(h). So W(z)
  must overtake W(σ y) after s, while Ξ(z) stays below. That needs a fresh W-gap at z created after s with ρ fixed. I found no
  contradiction, nor an instance.

## 3. Theorem BIP-RED (PROVED, lane, under premise [SUB])
- Premise [SUB]: R88's Corollary FW-R* (on W-runs by R89 GP*-RUN) holds verbatim on every sub-interval of a W-run, with R* counted
  inside the sub-interval. Its hypotheses (τ constant, λ_W constant, no S4c) are inherited by sub-intervals. I did not re-check R88's
  proof for any use of the run's maximality, so this is labelled a premise.
- Statement. Under [SUB], every W-run F has |F| ≤ SB_F + (SB_F + 1)·(n − 1)·(R° + 1) + FL_F, where R° := max over frozen stretches Φ of F
  of R°_Φ. With CONJECTURE BIP-REL-1, R° ≤ m_E.
- Proof. The transitions of F are the SB_F σ̄-changing ones plus those inside the SB_F + 1 frozen stretches. In a stretch Φ, [SUB] gives at
  most (n − 1)(R°_Φ + 1) W-changing transitions, and the rest are counted in FL_F. □
- Consequence (READING). Polynomial W-runs ⇐ BIP-REL-1 ∧ SB-POLY (σ̄ changes per W-run ≤ p(n)) ∧ FL-POLY ∧ [SUB]. This splits the
  W-run problem cleanly:
  - BIP-REL-1: a static two-fixed-strategy statement (ρ, τ fixed);
  - SB-POLY: Odd's optimal reply moving while τ is fixed, i.e. mechanism O (latew: SB_F 513 at n 482, quadratic);
  - FL-POLY: flats, L-SI's FL-GAP / ZFL (l-si 19ecc5e1).

## DONE / FINDINGS / NEEDS
- DONE: experiments/new/box89/bipprobe.py, relpe.py (STRICT env), run.sh / run2.sh / run3.sh, bip_*.txt, relpe_*.txt, relpes_*.txt;
  check.sh "box 89"; this note.
- FINDINGS:
  1. DATA: under a frozen σ̄, Even-side releases are lifted by plain one-player climbs below the first Odd deviation. Dependency depth ≤ 2
     (corpus), = 1 on obs / fx. Ξ(z) rises exactly once between block and release.
  2. CONJECTURE BIP-REL-1 (each edge strictly released ≤ 1 time per frozen stretch): 0 violations, 1132 runs plus latew / obs / gate pins.
     Non-strict form DEAD on si/root/instances/ueonce_n27 (and long121_n40), where blocks are inherited from an earlier σ̄.
  3. PROVED (lane, under [SUB]) Theorem BIP-RED: |F| ≤ SB_F + (SB_F + 1)(n − 1)(R° + 1) + FL_F. With BIP-REL-1, polynomial W-runs ⇐ SB-POLY
     ∧ FL-POLY.
  4. READING ([Ral] opened): generic label correction is O(n²C) with C exponential here. ARENA-MAX supplies the "round" structure that
     makes Bellman-Ford polynomial. What it does not cover is the re-opening of poisoned arcs (BIP-REL-1).
- NEEDS: none from the owner. Lead: (a) a referee could check [SUB] against R88's proof (sub-interval FW-R*); (b) L-RED's BIP adversary
  should aim at two strict releases of one edge in one frozen stretch; (c) mechanism O (SB_F) is the other residual. P-N5-FIXD still
  queued. My context is about 60% used; I can take one or two more boxes before parking.
