# Box 128 N5-PCOUNT: PORTAL-COUNT (proof side of TWO-FIX-NL), from L-RED 41's Lemma PORTAL
L-NEW successor 45, 2026-11-01 07:48-08:0xZ (date -u). Lead GO 07:48Z. Input: docs/red/R173-portal.md at claude/l-red 02119133 (read-only).
Code: experiments/new/box128/ (pcount.py, witness.py, runcorp.sh, pincheck.sh, c_corpus.txt, pincheck.txt). check.sh block «box 128».
Labels: PROVED (lane) = proved here, not refereed; DATA; READING; DEAD (with instance).

## 0. Answer
- The proposed count «W-strict Even moves ≤ (#branching X) × (#ZC stretches at X)», read per pivot h, is DEAD. Instance:
  topfix_n10 (n = 210, ODIFF 0 window), h = 192, stretch [6, 64]: 36 W-strict moves against a bound of 20, and no class's Ξ-cycle
  node changes at all. h alternates between a hub class 193 and 19 fresh Even-gate classes 64, 67, …, 112, one per level, and
  re-enters the hub 18 times. Every hub re-entry is a DIFF move (different classes), which PORTAL does not cover.
- What does hold, and is proved below: Lemma STATIC-TIE. It needs no classes, no TWO-FIX and no ZC: a W-strict repeat move of h is
  paid by a change of Ξ or W at one of h's two options. With PORTAL this gives an exact charging (Corollary STRICT-PAY). That
  charging is a relocation onto XI-CH / WCH at h's successors, not a polynomial count.
- The kill sits in a regime that is already polynomial: ODIFF 0 makes Ξ = W, the window is switch-best SI on G_τ, and RESULTS R101
  CONSISTENT-RED applies. So it refutes the COUNT, not TWO-FIX-NL. Any polynomial count has to recurse through the Even gates
  (classes that are themselves Even pivots), which a flat (#X) × (#ZC) product cannot do.

## 1. Review of Lemma PORTAL's proof (I am not its author)
The case analysis (P5, cases θ_1 odd / even) checks out line by line. One simplification: A_c = (prefix_1 Δ prefix_2) ∩ {rank > rank c},
so whenever A_c ≠ ∅ its maximum is the same vertex M := max(prefix_1 Δ prefix_2). That makes the «max stays the max» steps immediate.
Weak points:
- W1 (statement vs corollary). The conclusion is W_{j2}(i_1) = W_{j2}(i_2): the MOVE is a tie. It does not say «W does not rise at h».
  W_{j2}(h) can exceed W_{j2−1}(h) through a rise of W(X) at j_2. Corollary PORTAL-1's phrase «W(h) rises strictly through class-X
  options at most once» should read «at most once per ENTRY into class X». Re-entry X → Y → X is a fresh entry; that is the killing
  pattern in §0. With «W-strict move» := W_j(new) ▷ W_j(old) (as in pcount.py) the lemma itself is fine.
- W2 (P2 needs h ∉ the W-plays). The optimality step «σ_j(h) maximises W_j over the arena» fails when an option's W_j-play runs
  through h: the VJ comparison corner. DATA: WORSE (W_j(new) ◁ W_j(old)) occurs 13 times in the corpus, always at the corner
  (WORSE_NOCORNER 0). Smallest case: n4all_maxph_0 (n = 4), h = 2 switches 1 → 2 (a self-loop); the old option's play runs 1 → 2 and is
  longer to the odd cycle node 2. So the {h} part of NR is NEEDED, but only for the W-plays at t = j_1 and t = j_2. (An earlier remark
  of mine that it was superfluous is withdrawn; not in any pushed file.)
- W3 (NR, ZC only at the end points). The proof uses the Ξ-plays only at t = j_1 − 1 and j_2 − 1 (P3, P4) and the W-plays only at j_1
  and j_2 (P2, P5's θ's). ZC at the two end points already gives ZC throughout, by Ξ-monotonicity. NR can be weakened to the four end
  times.
- W4 (prefix part of NR = a self-cycle). Lemma NR-CYC (PROVED, lane): if a vertex u of prefix(h, i) lies on X's play in either world at
  some time, then X lies on the cycle of that play, and the cycle contains u. Proof: prefix vertices have out-degree 1 in G_F, the
  same edge in both worlds (Even vertices of out-degree 1 in G; Odd vertices off D, where τ = σ̄). So from u the play is the prefix
  walk to X: it returns to X. ∎ This is L-RED's escape (C). It is not chargeable to PLAY-CONTAIN or SBC-XI from what I have:
  PLAY-CONTAIN places Ξ-changes on plays, and NR failure is a static cycle property. DATA: no same-class pair in the corpus at all
  (SAME 0), so neither ZC nor NR failures arise there.
- W5 (fallbacks). Only transitions j_1 and j_2 need to be fallback-free (S4a optimality); the in-between condition can be dropped.

## 2. PROVED (lane)
- Lemma STATIC-TIE. Setting: any N5 run (SPEC S1-S5), under the standing premise of RESULTS R57 (S4a's σ_{k+1} is a pointwise optimum
  of the one-player arena H_k: Even v keeps {σ_k(v)} ∪ Iσ_k(v), Odd follows τ_k).
  - Let an Even h move i_0 → i_1 at transition j_1 and next i_1 → i_2 at j_2, with neither transition an S4c fallback. Let τ be
    constant on the states j_1 − 1, …, j_2. W_j := val(σ_j, τ).
  - Suppose (S-Ξ) Ξ_{j1−1}(x) = Ξ_{j2−1}(x) for x ∈ {i_1, i_2}; (S-W) W_{j1}(x) = W_{j2}(x) for x ∈ {i_1, i_2}; (H) the W_{j1}- and
    W_{j2}-plays from i_1 and i_2 avoid h.
  - Then W_{j2}(i_2) = W_{j2}(i_1): the second move is not W-strict.
  - Proof.
    - (1) σ_{j2−1}(h) = i_1 (no move in between), so i_2 ∈ Iσ_{j2−1}(h): Ξ_{j2−1}(i_2) ▷ Ξ_{j2−1}(i_1).
    - (2) By (S-Ξ), Ξ_{j1−1}(i_2) ▷ Ξ_{j1−1}(i_1) ▷ Ξ_{j1−1}(i_0); the second relation holds because i_1 ∈ Iσ_{j1−1}(h). So i_2 ≠ i_0
      and i_2 ∈ Iσ_{j1−1}(h).
    - (3) σ′ := σ_{j1} with h ↦ i_2 is a strategy of H_{j1−1}. By (H), the plays from i_1 and i_2 do not pass h. So
      val_{σ′}(h) = h · W_{j1}(i_2) and W_{j1}(h) = h · W_{j1}(i_1), where h · v prepends h. Prepending h preserves the order: with
      different cycle nodes the order is decided by the cycle-node reward; with the same one, h joins both P or neither and both ℓ grow
      by 1. Pointwise optimality of σ_{j1} gives W_{j1}(i_1) ⊵ W_{j1}(i_2).
    - (4) In the same way at j_2 (i_1 = σ_{j2−1}(h) is in H_{j2−1}): W_{j2}(i_2) ⊵ W_{j2}(i_1).
    - (5) By (S-W): W_{j2}(i_1) = W_{j1}(i_1) ⊵ W_{j1}(i_2) = W_{j2}(i_2) ⊵ W_{j2}(i_1). So the two are equivalent, and equal as
      values, since the key (reward, signed weight, ±ℓ) determines (c, P, ℓ). ∎
- Corollary STRICT-PAY. Inside a fallback-free stretch with τ constant, Ξ and W are pointwise monotone (SPEC termination; R17 (a) F1).
  So (S-Ξ), (S-W) are equivalent to constancy on the intervals. The Ξ-intervals [j_r − 1, j_{r+1} − 1] and the W-intervals
  [j_r, j_{r+1}] of consecutive moves of h overlap only at end points, so each change event (x, transition) is charged at most
  once per h. Hence, for every h and stretch:
  - STRICT_h ≤ 1 + CORNER_h + Σ_{x ∈ succ(h)} (ΞCH(x) + WCH(x)), where CORNER_h counts moves failing (H).
  - Summing over h: Σ_h STRICT_h ≤ #movers + #corners + Σ_x d_E(x)·(ΞCH(x) + WCH(x)).
  - PORTAL refines this for same-class pairs under NR: only Ξ-cycle-node changes at X pay there.
  - This is a RELOCATION onto XI-CH / WCH at successors, nothing more.
- Fact ZC-COUNT (definition chase). The ZC stretches at X inside a window number 1 + (the number of changes of λ_Ξ(X) in the window).
  Inside a frozen W-phase (RESULTS R88: λ_Ξ constant by definition) ZC holds at every X.

## 3. DEAD: the proposed count (instance topfix_n10)
- Game experiments/new/box52/out/topfix_n10.pg (sha1 4b65d3dc2735…, n = 210), default best-reward start written out by start_pair
  (box128/topfix_n10_default.start, sha1 f704f8444a06…). Window [6, 64], ODIFF 0, no fallback.
- h = 192 (priority 67, 20 successors). Classes: hub 193 (Even, out-degree 18) and gates 64, 67, …, 112 (Even, out-degree 3; one per
  successor 6, 9, …, 54). No class has a Ξ-cycle-node change in the stretch (LC_h = 20). Moves @7, 9, 10, 12, …, 58, 60: 54 → 2 → 193 →
  6 → 193 → 9 → … → 54 → 193; all 36 are W-strict. The hub is re-entered 18 times; each re-entry is paid (STRICT-PAY) by a Ξ-change
  of a non-cycle-node coordinate at an option (PAID_XI 544 / 544 on this game).
- Pin (pincheck.txt): Oink 8fbf0a7 --zlk and --tl verified, N5 regions agree (pinwin AGREE True), n5b identical state by state
  (64 iterations, 0 fallbacks).

## 4. Corpus DATA (813 distinct (game, start) pairs of si/anc58/corpus_fixed.lst, Erratum E-1; c_corpus.txt; 0 errors)
| quantity | value |
| --- | --- |
| windows / fallback-free stretches | 1,293 / 1,581 |
| Even moves in stretches / W-strict / flat / WORSE (all at the corner) | 18,836 / 18,576 / 247 / 13 |
| first moves of h in the stretch | 14,876 |
| SAME-class repeat moves (PORTAL pairs) | 0 |
| DIFF repeat moves / of which W-strict | 3,960 / 3,860 |
| class re-entries (RET) / W-strict | 2,009 / 1,964 |
| STATIC-TIE violations (STATVIOL) | 0 |
| non-first strict paid by an option's Ξ-change / by W only | 3,758 / 102 |
| (stretch, h) breaking the per-h (#X)(#ZC) count | 15 pairs; max excess 16 (topfix_n10) |
| (stretch, h) with STRICT_h > 2 deg(h) − 1 | 9 pairs; max STRICT_h / deg(h) 7.5 (dlc_d4) |
| (stretch, h) with ≥ 2 re-entered classes | 12 pairs; max 3 classes (u1t_own6_n32) |
| max W-strict moves of one h in one stretch | 48 (ladderd0_k48_n156) |

## 5. The Lead's sub-questions
- NR removable or chargeable (PLAY-CONTAIN, SBC-XI)? The {h} part: no; it is the VJ comparison corner (W2), and 429 corpus moves sit
  there. The prefix part = self-cycle (Lemma NR-CYC, route (C)); I found no charge. Inside TWO-FIX, σ̄ is constant, so SBC-XI has
  nothing to say.
- ZC stretches counted by λ_Ξ changes? Yes, by definition (Fact ZC-COUNT). Inside a frozen W-phase ZC holds everywhere. The count
  still fails, because the payer of a class re-entry is not a cycle-node change.
- W-flat moves already paid? READING: no. FB-D / DROP-D concern fallbacks. R101's SETTLE-MON / BRACKET-MON count states (settled set,
  bracket prefix), not moves. W-flat transitions are the open F term of TF-RED (box 122). Corpus: 247 flat moves.
- Exact obstruction to the count: hub re-entry. A pivot can return to the same class once per level while new gate classes supply
  the alternation. The re-entry is paid by P / ℓ changes of the hub's Ξ, i.e. XI-CH at a branching vertex. Recursing through the gates
  (each gate is an Even pivot) is the natural next form. On ODIFF 0 windows that recursion is switch-best SI, already polynomial
  (R101 CONSISTENT-RED); with ODIFF > 0 it is open.

## 6. Optional item (availability toggles) not attempted.

## DONE / FINDINGS / NEEDS: in the Lead message and notes/L-NEW.md.
