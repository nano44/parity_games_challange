# P-N5-ODD (packet, L-SI boxes 54, 55, 57): Odd vertices relay Ξ-changes; every source event at an Odd source starts at an Even switch (or an Odd choice change) on a first segment, or at an Even C-node; fuel re-routes of a pair are paid by more significant changes of the target. A RELOCATION, not a bound
L-SI successor 36 (Opus 5.5; D18). Lead 2026-10-31 11:48Z: «freeze a REFEREE PACKET P-N5-ODD from boxes 54-55 (and 57 if its claims are
clean): OLD-PLAY, ODD-STEP (unconditional via NO-RET), NO-RET, ODD-RELAY, ODD-ADD, SRC-ROOT. Use the usual packet shape: exact
statements, premises (R15, R57, R97's Φ), proofs, pins, DEADs, and a one-line RESULTS line draft with its scope tail (a REDUCTION /
relocation; G-N5-TIME stays OPEN).» FROZEN 2026-10-31 (this commit); its sha1 and the line file's sha1 go to the Lead. Repairs go to
docs/si/P-N5-ODD-fixes.md, never into this file.
- Sources (working notes; where they differ, THIS packet governs): docs/si/N5-SRC-box54.md (§2, §3), docs/si/N5-FSEG-box55.md (§1),
  docs/si/N5-FLEX-box57.md (§1, §2).
- Status: a RELOCATION. No count is bounded. G-N5-TIME stays OPEN. Not M3, not a step-4 pass, not a TARGET.md claim.
- Object: N5 only (SPEC S1-S5, docs/new/N5-ssi-global.md, with Q1-Q4 and FIX 1-4).

## 0. What to sign
| § | item | label |
| --- | --- | --- |
| 2 | Lemma OLD-PLAY | PROVED (to sign) |
| 3 | Lemma NO-RET, and Lemma ODD-STEP (unconditional) | PROVED (to sign) |
| 4 | Lemma ODD-RELAY; Corollary ODD-ADD | PROVED (to sign) |
| 5 | Corollary SRC-ROOT (inside a W-run) | PROVED (to sign); a relocation |
| 6 | Lemma FUEL-LEX; Corollary FUEL-COUNT | PROVED (to sign); FUEL-COUNT is a relocation |
| 7 | DATA, pins, DEADs | NOT to sign |

## 1. Setting, premises, notation
- A run of N5 is its sequence of states (σ_k, τ_k); a transition is k → k + 1. Ξ_k := Ξ_(σ_k) and σ̄_k := S1's Odd counterstrategy to σ_k
  (SPEC S1). Values (c, P, ℓ) (cycle node; the vertices of the play before the first visit of c that are more relevant than c, the start
  vertex included; the length to that visit) and the order ⊴ / ◁ / ⊵ / ▷ (better for Even) are SPEC S1; path sets compare by Q1 (the top
  rank of the symmetric difference decides). An Even vertex y SWITCHES at k if σ_(k+1)(y) ≠ σ_k(y).
- [R15a] RESULTS R15 (a), (d): at every N5 transition σ_(k+1) = Switch_I(σ_k) for some I ⊆ Iσ_k (possibly empty), and Ξ_(k+1) ⊵ Ξ_k
  pointwise (VJ00 Lemma 5.7).
- [R57] RESULTS R57's standing SPEC premise (S1's procedure realises the pointwise optimum): for every positional Odd strategy ρ and every
  vertex x, Ξ_k(x) ⊴ val(σ_k, ρ)(x).
- [PLAY] RESULTS R97, proof of PLAY-CAUSE^S (P-N5-SRC §2), quoted: «Every value on a play is (cycle node w of its eventual cycle, the
  vertices of the path to the first occurrence of w that are more relevant than w, the length of that path). … Ξ_(k+1)(x) is determined by
  the sequence y_0 … y_(i−1) and the value Ξ_(k+1)(y_i), by a function that does not depend on k.» Write Φ(y_0 … y_(i−1); v) for that
  function: for any play y_0 y_1 … of one positional strategy pair and any i ≥ 1, val(y_0) = Φ(y_0 … y_(i−1); val(y_i)).
  - (Φ-comp) Φ(a; Φ(b; v)) = Φ(ab; v) for finite sequences a, b. Proof: by the case split of [PLAY] on where the cycle node w of v first
    occurs (in a; in b but not in a; in neither): each case gives the same (w, relevant vertices before the first w, length). □
- W-run notation (RESULTS R89 / R97): in a W-run F, τ and C := {v : λ_W(v) = v} are fixed; D_k := {Odd o : σ̄_k(o) ≠ τ(o)};
  S_k := D_k ∪ D_(k+1) ∪ C; H_k := S4a's arena at k (Even v keeps {σ_k(v)} ∪ Iσ_k(v)).

## 2. Lemma OLD-PLAY (PROVED)
- Statement. At every N5 transition k → k + 1 and for every vertex x: if Ξ_(k+1)(x) ≠ Ξ_k(x), then some Even vertex of x's (σ_k, σ̄_k)-play
  switches at k.
- Proof. If none switches, x's (σ_(k+1), σ̄_k)-play equals its (σ_k, σ̄_k)-play, and a value depends only on the play, so
  val(σ_(k+1), σ̄_k)(x) = Ξ_k(x). [R57] at k + 1 gives Ξ_(k+1)(x) ⊴ Ξ_k(x), and [R15a] gives ⊵. □

## 3. Lemma NO-RET and Lemma ODD-STEP (PROVED)
- Lemma ODD-STEP. At every N5 transition k → k + 1: let o be Odd and x := σ̄_k(o). If Ξ_(k+1)(x) = Ξ_k(x), then Ξ_(k+1)(o) = Ξ_k(o).
- Proof. Put v_x := Ξ_k(x) = Ξ_(k+1)(x). Suppose Ξ_(k+1)(o) ≠ Ξ_k(o); by [R15a], ξ := Ξ_(k+1)(o) ▷ Ξ_k(o).
  - (E1) o's (σ_k, σ̄_k)-play is o followed by x's, as σ̄_k(o) = x. So Ξ_k(o) = Φ(o; v_x).
  - Case I: o is not on x's (σ_(k+1), σ̄_(k+1))-play. Let ρ := σ̄_(k+1) except ρ(o) := x. ρ agrees with σ̄_(k+1) on x's new play, so
    o's (σ_(k+1), ρ)-play is o followed by that play, and val(σ_(k+1), ρ)(o) = Φ(o; v_x) = Ξ_k(o) ◁ ξ, against [R57]. 
  - Case II (Lemma NO-RET): o is on x's (σ_(k+1), σ̄_(k+1))-play. Let γ = z_0 … z_(j−1) (z_0 = x) be that play before its first visit of o,
    and ξ = (w, P, ℓ).
    - (E2) x's new play is γ followed by o's new play, so v_x = Φ(γ; ξ); with (E1) and (Φ-comp), Ξ_k(o) = Φ(oγ; ξ).
    - (E3) Let ρ := σ̄_(k+1) except ρ(o) := x. It agrees with σ̄_(k+1) on γ, so o's (σ_(k+1), ρ)-play is the pure cycle Z := o z_0 … z_(j−1).
      Let m be its most relevant vertex. By [R57], ξ ⊴ val(σ_(k+1), ρ)(o), a value with cycle node m.
    - Case w = o: Φ(oγ; ξ) = (o, ∅, 0) = ξ, against ξ ≠ Ξ_k(o).
    - Case w ≠ o, w ∉ γ. First, o's new path to w avoids γ: meeting z_t ∈ γ would continue along γ back to o and close a cycle without w.
      - A: o is more relevant than w. Then o ∈ P, so o lies in the path set of v_x = Φ(γ; ξ). v_x is also x's OLD value, so x's
        (σ_k, σ̄_k)-play visits o before its first visit of w; after o it returns to σ̄_k(o) = x, so that play is periodic through x and o
        and the first visit of w must lie before o: contradiction.
      - B: o is less relevant than w. Let R := the vertices of γ more relevant than w (disjoint from P). Then Ξ_k(o) = (w, P ⊔ R, ℓ + j + 1).
        - R ≠ ∅ with top t: Ξ_k(o) ◁ ξ forces Ω(t) odd (Q1). All other vertices of Z are less relevant than w, so m = t, an odd cycle node
          more relevant than w; its reward −p′(t) is below w's reward. So val(σ_(k+1), ρ)(o) ◁ ξ, against (E3).
        - R = ∅: Ξ_k(o) and ξ differ only in length (ℓ + j + 1 > ℓ), so shorter is better for Even, i.e. Ω(w) is even. All of Z is less
          relevant than w, so m's reward is below p′(w), and again val(σ_(k+1), ρ)(o) ◁ ξ.
    - Case w ≠ o, w = z_i ∈ γ. x's new play visits w, then o, and o's play returns to w, so o and z_(i+1) … z_(j−1) lie on that play's cycle,
      whose most relevant vertex is w. Hence o is less relevant than w, o's new path to w runs on that cycle, and P = ∅: ξ = (w, ∅, ℓ).
      Let R := the vertices of z_0 … z_(i−1) more relevant than w. By (E2) v_x = (w, R, i); by (E1) Ξ_k(o) = (w, R, i + 1).
      - R = ∅: m = w and the path from o to w along Z is o z_0 … z_(i−1) w, so val(σ_(k+1), ρ)(o) = (w, ∅, i + 1) = Ξ_k(o) ◁ ξ, against (E3).
      - R ≠ ∅ with top t: if Ω(t) is even, R ▷ ∅, so Ξ_k(o) ▷ ξ, against ξ ▷ Ξ_k(o); if Ω(t) is odd, m = t is an odd cycle node more relevant
        than w and val(σ_(k+1), ρ)(o) ◁ ξ, against (E3). □
- Remark. Case II with o of even priority above w is Sub-case A: it dies by x's OLD play, not by the closed cycle Z.

## 4. Lemma ODD-RELAY and Corollary ODD-ADD (PROVED)
- Lemma ODD-RELAY. At an N5 transition k → k + 1, let o be Odd, x := σ̄_k(o), u a vertex of x's (σ_k, σ̄_k)-play, and π the part of that play
  from x up to (excluding) its first visit of u. If no Even vertex of π switches at k and σ̄_(k+1)(z) = σ̄_k(z) for every Odd z ∈ π, then
  Ξ_(k+1)(o) ≠ Ξ_k(o) implies Ξ_(k+1)(u) ≠ Ξ_k(u).
- Proof. Every vertex of π moves at k + 1 as at k, so x's (σ_(k+1), σ̄_(k+1))-play also runs along π into u, and by [PLAY]
  Ξ_j(x) = Φ(π; Ξ_j(u)) for j = k, k + 1. If Ξ(u) did not change, Ξ(x) would not change, and ODD-STEP would give Ξ_(k+1)(o) = Ξ_k(o). □
- Corollary ODD-ADD. Let I be a set of N5 transitions, o an Odd vertex and U a set of vertices such that at every k ∈ I at which Ξ(o) changes,
  the hypothesis of ODD-RELAY holds for some u_k ∈ U. Then |{k ∈ I : Ξ_(k+1)(o) ≠ Ξ_k(o)}| ≤ |{k ∈ I : Ξ(u) changes at k for some u ∈ U}|
  ≤ Σ_(u ∈ U) XCH_I(u), XCH_I(u) := the number of k ∈ I at which Ξ(u) changes. (Each change of Ξ(o) at k is matched with a change of Ξ(u_k)
  at the same k.) □

## 5. Corollary SRC-ROOT (PROVED; inside a W-run)
- Definitions, at a transition k → k + 1 of a W-run F, for an Odd o with x := σ̄_k(o): the FIRST SEGMENT FS_k(o) is the part of x's
  (σ_k, σ̄_k)-play from x up to (excluding) its first vertex u_k(o) in D_k ∪ C. u_k(o) exists: otherwise the play meets no vertex of D_k,
  so it is its (σ_k, τ)-play, whose cycle's most relevant vertex c has λ_W(c) = c, i.e. c ∈ C. A PREFIX EVENT at (o, k): some Even vertex
  of FS_k(o) switches at k, or some Odd z ∈ FS_k(o) has σ̄_(k+1)(z) ≠ σ̄_k(z).
- Statement. Let o_0 be Odd with Ξ_(k+1)(o_0) ≠ Ξ_k(o_0). Define o_(j+1) := u_k(o_j) as long as o_j is Odd and (o_j, k) is not a prefix event.
  Then every defined o_j lies on o_0's (σ_k, σ̄_k)-play and has Ξ_(k+1)(o_j) ≠ Ξ_k(o_j), and the sequence ends at an o_t such that
  (a) o_t is Odd and (o_t, k) is a prefix event, or (b) o_t ∈ C is Even.
- Proof. ODD-RELAY with u = o_(j+1) gives the changes; each o_(j+1) lies on o_j's old play, a suffix of o_0's. If the sequence did not end,
  some o_j would repeat; then the first segments of all o_j cover o_0's old play, none carries an Even switch, and the o_j are Odd, so no
  Even vertex of o_0's old play switches at k, against OLD-PLAY. □
- Reading: R97's E^S_F counts transitions with a Ξ-change at a vertex of S_k. By SRC-ROOT, at every such transition with an Odd changing
  source there is a prefix event at some source or a Ξ-change at an Even C-node on that source's old play. This relocates HXS-POLY (R97)
  to Even switches (and Odd choice changes) on first segments. It is not a smaller count: the transitions with a prefix event at a
  changing source are themselves source events.

## 6. Lemma FUEL-LEX and Corollary FUEL-COUNT (PROVED)
- Definitions, inside a W-run F. A FUEL RE-ROUTE of a pair (y, z) at k: an Even y switches to z := σ_(k+1)(y) at k, k − 1 ∈ F,
  (y, z) ∉ H_(k−1), and Ξ_(k−1)(z) ≠ Ξ_k(z). (Box 56 restricts y to first segments; nothing below uses that.) Its KEY is the key of the
  change Ξ_(k−1)(z) → Ξ_k(z): (2, 0) if the cycle node changes, else (1, r) with r the top rank of the path-set difference, else (0, 0);
  ordered (0, 0) < (1, r) < (1, r′) < (2, 0) for r < r′. Its RISE TRANSITION is k − 1.
- Remark (trivial bound). Distinct fuel re-routes of (y, z) have distinct rise transitions, so their number is ≤ XCH_F(z).
- Lemma FUEL-LEX. Let k < k′ be consecutive fuel re-routes of (y, z) with keys a, b and rise transitions t < t′. If b ≥ a, then (ASC) b > a,
  or (EQHI) b = a and Ξ(z) changes at some transition u, t < u < t′, with a key > a, or (REP) b = a ∈ {(2, 0), (0, 0)}.
- Proof. Let b = a = (1, r) and suppose every change of Ξ(z) strictly between t and t′ has key < (1, r). Then Ξ_(t+1)(z) and Ξ_(t′)(z) have the
  same cycle node and the same bits at every rank ≥ r; call the bit at r β. The change at t has key (1, r) and is a rise ([R15a]), so β is
  the better bit for Even (Q1). The change at t′ has key (1, r) too, so it moves rank r away from β with all higher ranks fixed, making
  Ξ_(t′+1)(z) ◁ Ξ_(t′)(z), against [R15a]. □
- Corollary FUEL-COUNT. Let N be the number of fuel re-routes of (y, z) in F, and HC the number of transitions u of F at which Ξ(z) changes at
  a key strictly greater than the key of the last fuel re-route of (y, z) at a transition ≤ u. Then N ≤ n(n + 2)(HC + n).
- Proof.
  - The keys take at most n + 2 values, so a maximal strictly descending run of consecutive keys has ≤ n + 2 members.
  - At each run boundary (consecutive k < k′ with b ≥ a), FUEL-LEX gives ASC, EQHI or REP. ASC is charged to the change at t′ (key b > a),
    EQHI to a change at some u ∈ (t, t′) (key > a); both are higher-digit changes counted by HC, and the windows (t, t′] of distinct
    boundaries are disjoint. So the number of ASC and EQHI boundaries is ≤ HC.
  - REP at (2, 0): each such boundary is a cycle-node change of Ξ(z), and the reward of that cycle node strictly rises (R15 a), so ≤ n − 1.
  - REP at (0, 0): along consecutive REP (0, 0) boundaries no change of key > (0, 0) happens, so Ξ(z)'s cycle node and path set are fixed and
    its length moves strictly in one direction among ≤ n values; so ≤ n − 1 consecutive ones. They are separated by the other boundaries.
  - With A := #ASC + #EQHI + #REP(2, 0) ≤ HC + n − 1: #runs ≤ 1 + A + (n − 1)(1 + A) = n(1 + A) ≤ n(HC + n), and N ≤ (n + 2) · #runs. □
- Reading. Pair width is a recursion on the target's higher digits. Nothing here bounds HC or the depth of that recursion, and nothing
  excludes a pair feeding its own target's higher digits (y on z's Ξ-play: 1,375 of 5,146 corpus fuel re-routes).

## 7. DATA, pins, DEADs (NOT to sign)
- Engines. Pins byte-identical to their sources (sha1 in experiments/si/src54/inst/pins.sha1, experiments/si/fseg55/inst/pins.sha1):
  sbq2_K8_m16, obs_K12_m24, src2_K3, rcl_K24, latew_K16_m32 (l-red / l-new), hit_b6a_1 (l-new box 109). xeng (n5 on si.py vs L-COMP's n5b):
  state sequences identical on all six; Oink zlk OK with strategies verified on all six; nep56_n32 xeng identical, Oink OK.
- OLD-PLAY / ODD-STEP / ODD-RELAY (experiments/si/src54/oddadd.py): corpus 1,132 games (box 50b lists), 1,692 W-runs, 104,383 Ξ-changes:
  VOLD 0, VSTEP 0, VSTEPB (Case II with Ξ(o) changing) 0, relay failures 0; MUT control bites (VOLD 2,881 on sbq2).
- NO-RET (experiments/si/fseg55/retsearch.py): 9 × 100,000 random games (n 8 / 12 / 16, out-degree ≤ 3; an Odd vertex at the top even or
  odd priority in 6 of them), every transition: RETX 0; Case II configurations 23,143-108,067 per run; MUT control bites.
- SRC-ROOT (experiments/si/fseg55/fseg.py, experiments/si/grow56/srcfuel.py): corpus 4,570 W-run source events: 4,544 carry a switch on a
  first segment, the other 26 a switch at an Even C-node; 0 unexplained. Odd-source changes 8,990 = 2,187 relays + 6,803 prefix events.
- FUEL-LEX (srcfuel.py): corpus 5,146 fuel re-routes, LEXV 0 (ASC 31, EQHI 82, REP 0); nep56_n32 ASC 2; so_th_n32 EQHI 6; quadratic pins one
  strictly descending run per pair (obs max 12, sbq2 8, latew 16).
- DEADs (docs/si/DEAD.md «box 54», «box 55», «box 56»): the W-rank potential (sbq2: W(242) = W(259) at all 153 states, σ̄(260) flips 128);
  ASC-W and TURN-W (src2_K3 Odd 62); a constant first-segment depth cap (hit_b6a_1); PEEL; FUEL-MONO (so_th_n32 pair (12, 6)); FUEL-DESC
  (nep56_n32 pair (28, 2)). FUEL-LEX is the corrected form of the last two.
- check.sh blocks «box 54», «box 55», «box 56», «box 57» pin all of the above.

## 8. Proposed RESULTS line
- docs/si/P-N5-ODD-line.txt (one line, no heading marker; sha1 reported with this file's).
