# N5-FSEG (box 55): RET is impossible (Lemma NO-RET), so ODD-STEP is unconditional and SRC-ROOT is a clean relocation. First-segment selectors: on the depth-3 instance the three gates are released by peeling ONE deviator's first segment front to back; no depth cap follows
L-SI successor 36 (Opus 5.5; D18). Lead 2026-10-31 09:46Z: «BOX 55, in this order: (1) Settle RET first … either prove it impossible
(handling the case of an even-priority o above the cycle), or give the instance … (2) Then bound S4a switches at first-segment Even
selectors, using OVERTAKE-W / NEW-EDGE / CARRIER / GATE (L-NEW box 108 …) [and] ONE-SOURCE / k-SOURCE (R155 / R156). The question:
does the first-segment structure … force the gates of a nested selector to be released in an order that caps the nesting depth? …
hit_b6a_1 … has h^W = 3 … Test any cap against it.» Written 2026-10-31 from 09:5xZ (date -u; see commit).
- Labels: PROVED (lane) / CONJECTURE / DEAD / DATA / READING. Not a TARGET.md claim. G-N5-TIME stays OPEN.
- Setting, notation and premises: box 54 (docs/si/N5-SRC-box54.md §1): [R15a], [R57], [PLAY] with its function Φ; R97's W-run
  notation. Path sets: P(ξ) := the vertices of the play before the first visit of the cycle node that are more relevant than it; the
  start vertex counts (SPEC S1). Order on path sets: SPEC Q1 (top of the symmetric difference decides). Order on values: reward of the
  cycle node first (SPEC S1).
- Sources opened: box 54 note; claude/l-new 2d791480 docs/new/N5-HDEPTH-box108.md §2-§4 (NEW-EDGE, OVERTAKE-W, CARRIER, GATE, depth-3
  shape); claude/l-new 046960222 experiments/new/box109/out/hit_b6a_1 (.pg, .start) and box108/carrier.py (run unchanged except its
  import path, output below); docs/new/N5-ssi-global.md S1 and Q1.

## 1. Lemma NO-RET (PROVED, lane)
- Statement. Let k → k + 1 be an N5 transition with σ_(k+1) = Switch_I(σ_k) for some I ⊆ Iσ_k (every N5 transition, R15 (d)). Let o be
  Odd and x := σ̄_k(o). If Ξ_(k+1)(x) = Ξ_k(x), then Ξ_(k+1)(o) = Ξ_k(o).
- So ODD-STEP (box 54 §2) holds without its hypothesis «o is not on x's new play», RET never occurs, ODD-RELAY holds without (ii),
  and Corollary SRC-ROOT ends only in (a) a prefix event or (c) a Ξ-change at an Even C-node.
- Proof. Suppose Ξ_(k+1)(x) = Ξ_k(x) =: v_x and Ξ_(k+1)(o) ≠ Ξ_k(o); by [R15a], ξ := Ξ_(k+1)(o) ▷ Ξ_k(o). If o is not on x's
  (σ_(k+1), σ̄_(k+1))-play, box 54's ODD-STEP already gives a contradiction. So let o be on it, and let γ = z_0 z_1 … z_(j−1) (z_0 = x)
  be that play up to (excluding) its first visit of o. Write ξ = (w, P, ℓ).
  - (E1) Ξ_k(o) = Φ(o; v_x): o's old play is o followed by x's old play, as σ̄_k(o) = x.
  - (E2) v_x = Ξ_(k+1)(x) = Φ(γ; ξ): x's new play is γ followed by o's new play.
  - (E3) Let ρ := σ̄_(k+1) except ρ(o) := x. ρ agrees with σ̄_(k+1) on γ, so o's (σ_(k+1), ρ)-play is the pure cycle Z := o z_0 … z_(j−1)
    o … . Let m be the most relevant vertex of Z. By [R57], ξ ⊴ val(σ_(k+1), ρ)(o), a value with cycle node m.
  - (E4) Φ composes: Φ(a; Φ(b; v)) = Φ(ab; v) for sequences a, b (case split on whether the cycle node of v occurs in a, in b, or in
    neither). So Ξ_k(o) = Φ(oγ; ξ) by (E1), (E2).
  - Case w = o. Then Φ(oγ; ξ) = (o, ∅, 0) = ξ, against ξ ≠ Ξ_k(o).
  - Case w ≠ o, w ∉ γ.
    - o's new path to w avoids γ: if it met z_t ∈ γ, the play would continue along γ back to o and close a cycle without w.
    - Sub-case A: o is more relevant than w. Then o ∈ P (o starts its own path), so o ∈ P(v_x) by (E2). By (E1)-(E2) v_x is also x's OLD
      value, so x's old play visits o before its first visit of w. But σ̄_k(o) = x, so after o that play returns to x and repeats a
      cycle through x and o that the first visit of w must lie on, before o: contradiction.
    - Sub-case B: o is less relevant than w. Put R := the vertices of γ more relevant than w (disjoint from P by the first bullet). By
      (E4), Ξ_k(o) = (w, P ⊔ R, ℓ + j + 1).
      - R ≠ ∅, top t. Ξ_k(o) ◁ ξ with symmetric difference R forces Ω(t) odd (Q1). Every vertex of Z other than those in R is less
        relevant than w, so m = t: an odd cycle node more relevant than w. Its reward −p′(t) is below w's reward (w even: positive;
        w odd: −p′(w) > −p′(t)). So val(σ_(k+1), ρ)(o) ◁ ξ, against (E3).
      - R = ∅. Then Ξ_k(o) and ξ differ only in length, ℓ + j + 1 > ℓ, and Ξ_k(o) ◁ ξ means shorter is better for Even, i.e. Ω(w) even.
        Every vertex of Z is less relevant than w, so m's reward is below p′(w) = w's reward, and again val(σ_(k+1), ρ)(o) ◁ ξ.
  - Case w ≠ o, w ∈ γ, say w = z_i.
    - x's new play visits w, later o, and o's play returns to w: o and the part of γ after w lie on that play's cycle Cy, whose most
      relevant vertex is w. In particular o is less relevant than w, and o's new path to w runs along Cy, so P = ∅: ξ = (w, ∅, ℓ).
    - Put R := the vertices of z_0 … z_(i−1) more relevant than w. By (E2), v_x = (w, R, i); by (E1), Ξ_k(o) = (w, R, i + 1).
    - R = ∅. Z's vertices are z_0 … z_(i−1), w and the part of Cy from w to o, all at most as relevant as w, so m = w and the path
      from o to w along Z is o z_0 … z_(i−1) w. So val(σ_(k+1), ρ)(o) = (w, ∅, i + 1) = Ξ_k(o) ◁ ξ, against (E3).
    - R ≠ ∅, top t. If Ω(t) is even, R ▷ ∅, so Ξ_k(o) ▷ ξ, against ξ ▷ Ξ_k(o). If Ω(t) is odd, m = t is an odd cycle node more relevant
      than w, and val(σ_(k+1), ρ)(o) ◁ ξ, against (E3). □
- The subcase the Lead named (o of even priority above the cycle) is Sub-case A: it dies not by the closed cycle but by the OLD play
  (o would sit in x's path set, yet σ̄_k(o) = x makes x's old play loop back before reaching w).
- DATA (si/fseg55/retsearch.py; 0 expected, the MUT control must bite):
  - corpus (box 54 oddadd.py): VSTEPB 0 on 1,132 games;
  - random and targeted search, every N5 transition: see §3 (ret_out.txt).

## 2. First-segment selectors and the depth-3 instance (DATA / READING)
- Definitions (box 54 §3). FS_k(o): o's first segment at k. An Even y is an FS-SELECTOR at k if y ∈ FS_k(o) for some o ∈ D_k ∪ D_(k+1).
- By SRC-ROOT with NO-RET, every source event at an Odd source carries a prefix event, i.e. an FS-selector switch or a D-entry on a first
  segment, or a Ξ-change at an Even C-node. DATA (corpus, fseg.py): 4,570 W-run source events; 4,544 carry an FS-selector switch; the
  other 26 all carry a switch at an Even C-node (cw11_n24: 11, all at C-node 7; nep22f_n64: 2 per list at C-node 48); 0 unexplained.
  33,794 W-run switches, 6,303 of them at FS-selectors; max switches of one FS-selector in one W-run 31.
- hit_b6a_1 (L-NEW box 109; n 32, 43 iterations; W-run 20..43 has h^W = 3; si/fseg55/fseg.py -t):
  - L-NEW's carrier.py: one level-2 stretch B2 = 20..40, 23 carriers, top pending digit u18, lower digits u29 / u8, all fixed at
    k = 40 by gate 6 through the NEW edge (6, 0), at a source event.
  - Every one of the 11 source events of the game carries an FS-selector switch (SRCFS 11, SRCNOFS 0).
  - The releases at the end of the run are ONE deviator, Odd 0 (τ(0) = 11, priority 17), being peeled:
    - k 20-33: FS(0) = [1, 5, 21, 18, 23] (18 has odd priority 29, the top of Ξ(0)'s path set).
    - k 34: Even 1 switches (FS of 0 and 4); σ̄(0) jumps from 1 to 5. Source event.
    - k 35: Even 9 switches (FS of 4); k 36: Even 5 switches; σ̄(0) jumps to 21. Source events.
    - k 39: Even 21 switches (21 → 30), FS(0) becomes a 24-vertex play through 6; k 40: Even 6 switches 22 → 0 by the new edge (6, 0)
      (the top gate), a source event; at 41 Odd 0 leaves D (σ̄(0) = τ(0) = 11).
    - Between them only source-free settling (k 37, 38), as R97 SRC-SETTLE predicts.
  - So the three nested gates are released bottom-up by consecutive switches on ONE first segment, front to back. The first-segment
    structure does order the releases (along the segment), but that order is what produces the depth, not what caps it.
- READING (answer to the Lead's question; not a theorem).
  - No constant cap follows from the first-segment structure. hit_b6a_1 realises depth 3 with every gate an FS-selector of one
    deviator, released in segment order at source events.
  - What the structure suggests instead is a PEEL count: Odd 0's choice moves along its own first segment (1 → 5 → 21), each move
    triggered by an Even switch at the current head of the segment. If a deviator's first segment only shrinks between such peels,
    a deviator is peeled at most |FS| ≤ n times before it re-grows or leaves D. Then depth would be paid by «segment re-growths», and
    the open question would be how often a first segment can re-grow inside a W-run. At k 39 the segment of 0 re-grows from 4 to 24
    vertices once.
  - Measured (peel.py) and DEAD as a reduction: on the quadratic pins first segments RE-GROW at almost every source event and are
    never peeled: obs_K12_m24 GROW 529 / PEEL 0 (max per deviator 23, HXS 24); sbq2_K8_m16 GROW 353 / PEEL 0 (max 72, HXS 128);
    latew_K16_m32 GROW 961 / PEEL 0 (max 31, HXS 32); hit_b6a_1 GROW 8 / PEEL 2. So «HXS ≤ n·(1 + GROW)» is true but GROW is not
    smaller than HXS.

## 3. Tools, data, pins
- experiments/si/fseg55/: fseg.py (FS-selectors, per-transition timeline with -t, corpus summary), retsearch.py (NO-RET search, MUT
  control), runfseg.sh, runret.sh, inst/hit_b6a_1 (byte-identical to claude/l-new box109/out; sha1 in inst/pins.sha1).
- Outputs: fseg_sbcg.txt, fseg_alt.txt (corpus), ret_out.txt (NO-RET search), engines_hit.txt.
- hit_b6a_1: xeng state sequences identical; n5 43 iterations (2 fallbacks); Oink zlk OK, strategies verified.
- NO-RET search: see ret_out.txt; 9 runs × 100,000 games (n 8 / 12 / 16, out-degree ≤ 3; bias 0 none, 1 vertex 0 Odd at the top
  EVEN priority, 2 vertex 0 Odd at the top odd priority); RETX 0 in every run; ONPLAY (o on its old choice's new play, the case NO-RET
  had to handle) occurs tens of thousands of times. MUT control bites.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/si/fseg55/ (fseg.py, peel.py, retsearch.py, run scripts, outputs, inst/hit_b6a_1); check.sh «box 55»;
  DEAD.md «box 55». SHAs: see the commit and the message to the Lead.
- FINDINGS:
  1. PROVED (lane): Lemma NO-RET. ODD-STEP is unconditional, RET never occurs, and SRC-ROOT ends only at a first-segment prefix event or
     a Ξ-change at an Even C-node. The even-priority subcase dies by the OLD play, not by the closed cycle.
  2. DATA: corpus source events 4,544 FS-switch + 26 C-node switch + 0 other; NO-RET search 900,000 games, 0.
  3. DEAD: a constant depth cap from first-segment order (hit_b6a_1: the three gates are consecutive switches on ONE deviator's segment,
     front to back, at source events); and the PEEL reduction (segments re-grow at almost every source event; GROW ≈ HXS).
  4. READING: the first segment orders releases along itself, which is what MAKES depth; a bound must count segment re-growths, which in
     data are as many as the source events. Item (2) of the brief (bound S4a switches at FS-selectors) is NOT achieved.
- NEEDS: none from the owner.
