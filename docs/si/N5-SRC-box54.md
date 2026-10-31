# N5-SRC (box 54): Odd sources are additive relays. Every Ξ-change at an Odd source is relayed from the next source on its old Ξ-play or starts at an Even switch on that play's first segment. The brief's candidate potentials are DEAD on sbq2_K8_m16
L-SI successor 36 (Opus 5.5; D18). Lead 2026-10-31 (after 08:13Z): «FIRST BOX (proof side of HXS-POLY …): bound the source events
directly … Find a monotone quantity on D-vertices … It must bound E^S_F polynomially, or bound it by a named smaller quantity. If it
fails, give the instance where Ξ at a single Odd source changes super-linearly in one W-run, or the closest you find, and its mechanism.»
Written 2026-10-31 from 08:1xZ (date -u; see commit).
- Labels: PROVED (lane) / CONJECTURE / DEAD / DATA / READING. Not a TARGET.md claim. G-N5-TIME stays OPEN. No count is bounded here.
- Object: N5 (SPEC S1-S5, docs/new/N5-ssi-global.md). Setting and notation as RESULTS R97 (l. 8032): W-run F, τ and C fixed on F,
  Ξ_k, σ̄_k, W_k, D_k, S_k = D_k ∪ D_(k+1) ∪ C, source event, E^S_F, HXS_F(v).
- Sources opened: RESULTS R97 (l. 8032) and R15 (a), (d) (l. 624-645); docs/red/P-N5-SRC.md §2 (PLAY-CAUSE^S: the play decomposition
  below is quoted from its proof), l-red; docs/red/R155-recursion.md §2 (ONE-SOURCE), docs/red/R156-twosource.md §1 (k-SOURCE), l-red;
  docs/red/R145-flipev.md §3 (sbq2 family), l-red; docs/new/N5-ssi-global.md S1, S2, S4.

## 0. Summary
| § | item | label |
| --- | --- | --- |
| 2 | Lemma OLD-PLAY: a Ξ-change at x needs an Even switch on x's OLD Ξ-play | PROVED (lane) |
| 2 | Lemma ODD-STEP: an Odd vertex's Ξ changes only if its old choice's Ξ changes (or it lies on that choice's new play) | PROVED (lane) |
| 2 | Lemma ODD-RELAY and Corollary ODD-ADD: an Odd vertex whose option rides a fixed prefix into u changes Ξ only when u does; on an interval, Ξ-changes at o ≤ #transitions at which some source of its options changes (no degree factor) | PROVED (lane) |
| 3 | Corollary SRC-ROOT: a source event at an Odd source is a relay chain along its old Ξ-play ending at a PREFIX EVENT (an Even switch or a D-entry on a first segment), a C-vertex change, or a RET exception | PROVED (lane); a relocation, not a smaller count |
| 4 | The brief's candidates: rank of σ̄(o) in the W-order of succ(o); ASC-W; TURN-W | DEAD (sbq2_K8_m16, src2_K3) |
| 5 | Mechanism of the quadratic single Odd source (sbq2_K8_m16, 128 Ξ-changes at Odd 260 in one W-run of 152) | DATA / READING |
| 6 | Pins and corpus | DATA |

## 1. Premises (all signed or landed)
- [R15a] RESULTS R15 (a), (d): N5's S4a step applies Switch_I with I ⊆ Iσ_k, so Ξ_(k+1) ⊵ Ξ_k pointwise (VJ00 Lemma 5.7).
- [R57] RESULTS R57's standing SPEC premise (as quoted in R97): S1's procedure realises the pointwise optimum, i.e. for every positional
  Odd strategy ρ and every vertex x, Ξ_k(x) ⊴ val(σ_k, ρ)(x).
- [PLAY] (P-N5-SRC §2, proof of PLAY-CAUSE^S, quoted): «Every value on a play is (cycle node w of its eventual cycle, the vertices of the
  path to the first occurrence of w that are more relevant than w, the length of that path). … So Ξ_(k+1)(x) is determined by the
  sequence y_0 … y_(i−1) and the value Ξ_(k+1)(y_i), by a function that does not depend on k.» We write val(y_0) = Φ(y_0 … y_(i−1); val(y_i))
  for any play y_0 y_1 … of one strategy pair and any i ≥ 1. Φ does not depend on the state or the strategies.
- Transitions: everything in §2 holds for every N5 transition k → k + 1 at which σ_(k+1) arises from σ_k by S4a (so for every transition
  of a W-run). τ plays no role in §2; it enters only through D_k and C in §3.

## 2. Odd vertices relay (PROVED, lane)
- Lemma OLD-PLAY. If Ξ_(k+1)(x) ≠ Ξ_k(x), then some Even vertex of x's (σ_k, σ̄_k)-play switches at k.
  - Proof. If none switches, x's (σ_(k+1), σ̄_k)-play is its (σ_k, σ̄_k)-play, so val(σ_(k+1), σ̄_k)(x) = Ξ_k(x). By [R57] at k + 1,
    Ξ_(k+1)(x) ⊴ Ξ_k(x); by [R15a], Ξ_(k+1)(x) ⊵ Ξ_k(x). So they are equal. □
- Lemma ODD-STEP. Let o be Odd and x := σ̄_k(o). If Ξ_(k+1)(x) = Ξ_k(x) and o is not on x's (σ_(k+1), σ̄_(k+1))-play, then
  Ξ_(k+1)(o) = Ξ_k(o).
  - Proof. Let ρ := σ̄_(k+1) except ρ(o) := x. x's (σ_(k+1), σ̄_(k+1))-play avoids o, so ρ agrees with σ̄_(k+1) on it, and o's
    (σ_(k+1), ρ)-play is o followed by that play. By [PLAY] with i = 1, val(σ_(k+1), ρ)(o) = Φ(o; Ξ_(k+1)(x)). At k, o's
    (σ_k, σ̄_k)-play is o followed by x's (σ_k, σ̄_k)-play, so Ξ_k(o) = Φ(o; Ξ_k(x)). As Ξ_(k+1)(x) = Ξ_k(x), val(σ_(k+1), ρ)(o) = Ξ_k(o).
    [R57] at k + 1 gives Ξ_(k+1)(o) ⊴ Ξ_k(o), and [R15a] gives ⊵. □
  - The excluded case (o on x's new play while Ξ(o) changes and Ξ(x) does not) is called RET below. DATA: 0 in the corpus (§6).
  - RET, partial (READING, not signed). With γ := x's new play up to o, Ξ_k(o) = Φ(oγ; Ξ_(k+1)(o)) (compose [PLAY] twice), and the
    Odd strategy σ̄_(k+1)[o ↦ x] closes the cycle {o} ∪ γ. This kills RET when o is its own new cycle node, and when the cycle node w
    of Ξ_(k+1)(o) is not on γ and the most relevant vertex of {o} ∪ γ is not o itself with even priority above w. It does NOT kill
    that last subcase (the closed cycle is then bad for Odd, and no contradiction follows), and the case w on γ is not analysed.
    Open (queue).
- Lemma ODD-RELAY. Let o be Odd, x := σ̄_k(o), u a vertex of x's (σ_k, σ̄_k)-play, and π the part of that play from x up to (excluding)
  the first visit of u. Suppose
  - (i) no Even vertex of π switches at k, and σ̄_(k+1)(z) = σ̄_k(z) for every Odd z ∈ π;
  - (ii) o is not on x's (σ_(k+1), σ̄_(k+1))-play.
  If Ξ_(k+1)(o) ≠ Ξ_k(o), then Ξ_(k+1)(u) ≠ Ξ_k(u).
  - Proof. By (i), x's (σ_(k+1), σ̄_(k+1))-play also runs along π and reaches u: every vertex of π moves as at k. By [PLAY] at both
    states, Ξ_j(x) = Φ(π; Ξ_j(u)) for j = k, k + 1. If Ξ(u) did not change, Ξ(x) would not change, and ODD-STEP with (ii) would give
    Ξ_(k+1)(o) = Ξ_k(o). □
- Corollary ODD-ADD (interval form). Let I be a set of transitions of the kind above, o an Odd vertex and U a set of vertices. Suppose
  at every k ∈ I at which Ξ(o) changes, (i) and (ii) hold for some u_k ∈ U on σ̄_k(o)'s old play. Then
  |{k ∈ I : Ξ_(k+1)(o) ≠ Ξ_k(o)}| ≤ |{k ∈ I : Ξ_(k+1)(u) ≠ Ξ_k(u) for some u ∈ U}| ≤ Σ_(u ∈ U) XCH_I(u),
  where XCH_I(u) is the number of k ∈ I at which Ξ(u) changes.
  - Proof. ODD-RELAY maps each change of Ξ(o) at k to a change of Ξ(u_k) at the same k. □
  - Contrast (READING). For an Even selector h, L-RED's k-SOURCE (R156 §1) gives ≤ K_0 + Σ_b K_b (1 + WCH(u_b)) switches, and the class
    sizes K_b are realised (R157, rcl_K24): h re-climbs a class after each landing outside it. An Odd vertex cannot re-climb. Ξ(o) is
    the minimum of its options' values, and it moves only when its current option's value moves (ODD-STEP). So the degree of an Odd
    vertex never multiplies. Inside a W-run, any multiplication of source events must happen at EVEN vertices, i.e. at S4a's W-choices.

## 2b. With L-NEW's O-ARENA (Lead 08:36Z; L-NEW 41 box 107, claude/l-new f63719c5, lane-PROVED there, NOT signed): the same relay holds for W (READING)
- O-ARENA (as relayed by the Lead): on a W-run, W_k is the Odd best-response value to σ_k in the arena G_O where Odd vertex z keeps only
  {τ(z)} ∪ I_τ(z). So Ξ_k and W_k are Odd-optimal values of the SAME σ_k in nested games G_O ⊆ G.
- The W-side analogue of §2 is immediate and needs no O-ARENA: Odd vertices follow τ in W-plays, so W(o) = Φ(o; W(τ(o))) and an Odd
  vertex's W changes exactly when W(τ(o)) does. O-ARENA adds that this fixed choice is also Odd-OPTIMAL in G_O, so the two values of an
  Odd vertex are the two optima of one σ in nested games, and in both games Odd vertices relay additively (§2).
- What it suggests (READING, not proved, not developed in this box): an Odd source o ∈ D is where the two optima differ. Every change of
  Ξ(o) is rooted at an Even switch on o's old Ξ-play (OLD-PLAY), so a bound on source events is a bound on the Even switches on
  deviators' old Ξ-plays whose effect the G_O-optimum does not absorb.

## 3. Where a source event starts (PROVED, lane; a relocation, not a smaller count)
- Definitions, for a transition k → k + 1 of a W-run F and an Odd vertex o with x := σ̄_k(o):
  - the FIRST SEGMENT of o at k is the part of x's (σ_k, σ̄_k)-play from x up to (excluding) its first vertex u in D_k ∪ C (u := none if
    the play closes first);
  - a PREFIX EVENT at (o, k): an Even vertex of the first segment switches at k, or an Odd vertex z of it has σ̄_(k+1)(z) ≠ σ̄_k(z),
    or u is none;
  - a RET event at (o, k): Ξ(o) changes at k and o is on x's (σ_(k+1), σ̄_(k+1))-play.
  - Remark: u always exists. If x's old play met no vertex of D_k, it would be its (σ_k, τ)-play, whose cycle's most relevant vertex c has
    λ_W(c) = c, i.e. c ∈ C (λ_W is fixed on F). So «u none» never occurs (DATA: PFXNOU 0).
- Corollary SRC-ROOT. Let k → k + 1 be a transition of F and o_0 an Odd vertex in S_k whose Ξ changes at k. Define o_(j+1) := the
  vertex u of o_j's first segment, as long as o_j is Odd, (o_j, k) is neither a prefix event nor a RET event. Then every o_j that is
  defined has Ξ_(k+1)(o_j) ≠ Ξ_k(o_j), each o_(j+1) lies in D_k ∪ C on o_0's (σ_k, σ̄_k)-play, and the sequence stops at an o_t such
  that one of the following holds:
  - (a) (o_t, k) is a prefix event (an Even switch or a D-entry on o_t's first segment);
  - (b) (o_t, k) is a RET event;
  - (c) o_t ∈ C is Even (a Ξ-change at an Even W-cycle node).
  - Proof. ODD-RELAY with u = o_(j+1) and U = D_k ∪ C, applied step by step. Each o_(j+1) lies on o_j's old play, which is a suffix of
    o_0's old play, so all o_j lie on o_0's old play. Odd vertices of D_k ∪ C are relayed further. The sequence cannot run forever: o_0's
    old play is a lasso with finitely many vertices, and if the o_j repeat, all first segments around the lasso carry no Even switch,
    so no Even vertex of o_0's old play switches, against OLD-PLAY. □
- So at a source event, the root of the change at an Odd source is either an Even switch on a first segment of a source (a), a
  D-entry there (a), a C-change (c), or the exception (b). Per vertex: HXS_F(o) ≤ PFX_F(o) + RELAY_F(o) + RET_F(o), where RELAY_F(o)
  counts the transitions at which the next source u of o changes and o's first segment is fixed.
- What this does and does not give (READING).
  - It does not bound E^S_F: the transitions carrying a prefix event are a subset of the source events, so «PFX-POLY» is not smaller
    than HXS-POLY. It is a relocation from the Odd side (σ̄, S1's best response) to the Even side (S4a's switches on first segments).
  - On a first segment the Odd vertices follow τ (they are outside D_k). So an Even vertex y of o's first segment has its Ξ-play equal
    to its W-play up to u: Ξ_k(y) = Φ(seg; Ξ_k(u)) and W_k(y) = Φ(seg; W_k(u)). y is a W-selector of the kind ONE-SOURCE / k-SOURCE
    count. The open core HXS-POLY therefore reads: how often can S4a switch an Even vertex that lies on the first segment of an Odd
    deviator (or of the Odd vertex about to deviate)?
- DATA (§6). Corpus (1,132 games, 1,692 W-runs): 8,990 Ξ-changes at Odd sources; 2,187 relays, 6,803 prefix events (6,745 Even switches,
  58 D-entries, 0 «u none»), RET 0. On obs_K12_m24, src2_K3, rcl_K24 and latew_K16_m32 EVERY Odd-source change is a prefix event; on
  sbq2_K8_m16, 649 of 769 (120 relays).

## 4. The brief's candidate potentials (DEAD)
- (a) The rank of σ̄_k(o) among o's successors in the W_k-order: DEAD on experiments/si/src54/inst/sbq2_K8_m16 (= L-RED pin
  flipev/instances/sbq2_K8_m16, byte-identical). At Odd o = 260 (successors 242 = τ(260) and 259): W_k(242) = W_k(259) at ALL 153
  states of the run (one W-run), while σ̄(260) changes 128 times (si/src54/wtie.py: «Wtie 153 sbflips 128»). Any potential built from the
  W-order of succ(o) and σ̄(o) is constant here. The same holds for any potential built from (D_k, Ξ_k on D_k) through o's successor
  W-values only.
- (b) CONJECTURE ASC-W («two consecutive Ξ(v)-changes whose top-differing rank does not rise have a W(v)-change between them»; true at
  sbq2's vertex 260, where the inner climb ascends and every descent coincides with a W(260)-change): DEAD. src2_K3 (L-RED pin
  wlev/instances/src2_K3): Odd source 62, Ξ(62) changes at k = 24 → 25 (top rank 235) and k = 26 → 27 (top rank 233; the odd vertex of
  rank 235 is replaced by rank 233, then 231): a descending staircase with W(62) constant. Pins: 1,012 such pairs on src2_K3, 540 on
  sbq2_K8_m16 (si/src54/ascw.py «BAD»).
- (c) TURN-W («a reversal of direction in the top-rank sequence of Ξ(v) needs a W(v)-change nearby»): DEAD, 67 reversals without a
  W(v)-change on src2_K3 (23 at sources), 58 on sbq2_K8_m16 (30 at sources).

## 5. The quadratic single Odd source, and its mechanism (DATA / READING)
- Instance: sbq2_K8_m16 (n 261, one W-run of 152 transitions; L-RED R145: the family has |F| = K(m + 3), Ξ-changes K·m at the root, n
  = 16K + 5 at m = 2K, so ≈ n²/512; 512 at n 517). Here: Odd 260 (priority 0, successors 242, 259) changes Ξ 128 = K·m times, all
  σ̄-flips (ARG 128, of which 64 return to a successor used before). E^S_F = 144, HXS max 128 (si/src54/srcev.py).
- Mechanism, read off si/src54 traces (states 0-58 printed):
  - Outer level (K = 8 rounds): W(260) changes in a single top rank per round, 245, 246, 247, … (ascending, one rank per round).
  - Inner level (m = 16 per round): the two options' Ξ gain the path-set ranks 136, 137, …, 150 alternately (138, 140, … on 242's side;
    137, 139, … on 259's side). Each gain is a prefix event: an Even switch on that option's first segment (§3). σ̄(260) flips at each
    gain, because the other option is then lower for Odd.
  - At the end of a round Ξ(260) changes at a high rank (227, then 225 with the new W round; 223 / 221; …) and the inner ranks
    136-150 are reset. The root's top-differing rank sequence is ascending inside a round and descends only when W(260) changes.
  - So the quadratic count is the product (W-rounds) × (prefix events per round): depth 2. The Odd root multiplies nothing (ODD-ADD); the
    product sits in the Even switches on the two first segments, re-armed once per W-round.
- What a third level needs (READING). By ODD-ADD the Odd vertices only relay. A cubic count at one Odd source would need the prefix
  events of its first segments to be themselves a product, i.e. an Even selector on a first segment whose re-climbs (k-SOURCE's K_b
  factor) are re-armed by a W-leapfrog of two lower sources, each re-armed in turn. This is L-RED 37's FEEDBACK question, seen from
  the proof side: the factor is per Even level, and no lemma here bounds the number of Even levels.

## 6. Tools, data, pins
- experiments/si/src54/: srcev.py (source events per W-run, by kind D / C, coordinate, ARG / KEEP (σ̄ changed or not), returns);
  oddadd.py (checks OLD-PLAY, ODD-STEP, RET, ODD-RELAY; PROP / PFX split; MUT=1 control: VOLD must bite); ascw.py (ASC-W, TURN-W);
  wtie.py (the W-tie at 260); runodd.sh (corpus); inst/ (the five pins, byte-identical copies, sha1 in inst/pins.sha1).
- Pins (si/src54/pins_out.txt):

| pin | n | |F| | E^S | HXS max | Odd-source changes | relays | prefix events | VOLD / VSTEP / RET / relay failures |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sbq2_K8_m16 | 261 | 152 | 144 | 128 (Odd 260) | 769 | 120 | 649 | 0 / 0 / 0 / 0 |
| obs_K12_m24 | 272 | 324 | 24 | 24 | 577 | 0 | 577 | 0 / 0 / 0 / 0 |
| src2_K3 | 285 | 324 | 24 | 24 | 577 | 0 | 577 | 0 / 0 / 0 / 0 |
| rcl_K24 | 321 | 324 | 24 | 24 | 577 | 0 | 577 | 0 / 0 / 0 / 0 |
| latew_K16_m32 | 482 | 560 | 528 | 32 | 2,017 | 0 | 2,017 | 0 / 0 / 0 / 0 |

- Corpus (si/src54/odd_sbcg.txt, odd_alt.txt; box 50b's lists: 719 + 413 = 1,132 games): 21,845 iterations, 1,692 W-runs, 104,383
  Ξ-changes; VOLD 0, VSTEP 0, RET 0, relay failures 0; 8,990 Odd-source changes = 2,187 relays + 6,803 prefix events (6,745 switches,
  58 D-entries); max HXS at an Odd source 61.
- Engines: xeng.py (n5 on si.py vs L-COMP's n5b) state sequences identical on all five pins (si/src54/xeng_pins.txt). Oink 8fbf0a7:
  si/src54/oink_pins.txt.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/si/src54/ (tools, pins, outputs); docs/si/DEAD.md «box 54»; experiments/si/check.sh «box 54». SHAs: see
  the commit and the message to the Lead.
- FINDINGS:
  1. PROVED (lane): OLD-PLAY, ODD-STEP, ODD-RELAY, Corollary ODD-ADD (Odd relays are additive, no degree factor; contrast k-SOURCE).
  2. PROVED (lane): Corollary SRC-ROOT: an Odd-source event is a relay chain ending at a prefix event, a C-change or RET. A relocation
     of HXS-POLY to S4a's switches on deviators' first segments, not a smaller count.
  3. DEAD: W-rank potential (sbq2: W(242) = W(259) at all 153 states, 128 flips), ASC-W, TURN-W (src2_K3, sbq2_K8_m16).
  4. DATA: corpus 0 violations of every lemma check; 76% of Odd-source changes are prefix events, 24% relays, RET 0.
  4b. READING (§2b): with L-NEW's O-ARENA, Ξ and W are two Odd optima of one σ in nested games; the W-side relay is immediate (τ fixed).
  5. READING: sbq2's quadratic is (W-rounds) × (prefix events per round); a third level needs a nested Even selector on a first
     segment (k-SOURCE's per-level factor), which is where a proof must bound the depth or L-RED 37 must build it.
- NEEDS: none from the owner.

## ERRATUM (L-SI successor 37, 2026-10-31; P-N5-ODD fixes entry 4)
- sbq2_K8_m16.start sets τ(242) := 243, a non-edge (REFEREE 21 D-ODD-1, REFEREE-2 24 F-1). The W-rank DEAD of §4 is WITHDRAWN (W(242) =
  W(259) at 0 states on the repaired start sbq2_K8_m16_fix.start). The sbq2 rows of this note change to: oddadd ODDCH 2206, OSRC 762,
  PFX 642, MAXHXS 136 (VOLD 0, VADD 0); MUT VOLD 2849; ASC-W BAD 525, TURNBAD 58; σ̄(260) flips 128. Details in docs/si/P-N5-ODD-fixes.md.
