# Referee report R-psolC: fidelity of L-ATTR's psolC to HKP DTR15-4 (claude/l-attr 02174e2)

Referee: REFEREE. Date: 2026-10-15 (routed by the Lead 08:45Z, 2 h box). Claim under check: docs/attr/A3-psolC-results.md,
"psolC is not complete", with instance experiments/attr/instances/psolc_min_n4_m6.pg and tc N = 2 (22 vertices).
Implementation: experiments/attr/psolc.py; line map docs/attr/psolC-impl.md (C1–C11, A1–A5).
Source opened by me: M. Huth, J. H.-P. Kuo, N. Piterman, "Static analysis of parity games: alternating reachability under
parity", Imperial College DTR 2015/4, downloaded from https://www.doc.ic.ac.uk/research/technicalreports/2015/DTR15-4.pdf into an
isolated directory; sha256 a7b61fe3a72926a94a3019e34620339f38aa653fe8aeed9ab4210187763e9cd6 (matches the Lead's and L-LIT's).
Read: §2 (min-parity, p.3), Def. 1 (p.4), Def. 2 and Thm 1 with proof (pp.5–6), Cor. 1, §4 Lemma 2 with proof, F^p_G (2),
Lemma 3 (p.7), the Fig. 4 remark on the first-visit variant, Fig. 5 (p.9, pseudocode), Thm 2 with proof (pp.8–9), Example 3
and Fig. 6 (pp.10–11; the figure read from the rendered page), Thm 4 with proof (p.12). Out of scope (Lead): Thm 4's
multi-round step; PA** ⊊ Solved(psolC).
Machine checks (mine): docs/referee/scratch/psolccheck.py — psolC written by me from Defs 1–2, Thm 1 and Fig. 5 on the FULL
product V × C(G)_⊥ (not the reachable part), both readings of A1; run on the instance, DTR Figs. 1, 4, 6, tc N = 2, and
exhaustively against the lane's psolc.py (see §4).

## Verdict: FAITHFUL. DE3 can be recorded with the instance.
| item | verdict |
| --- | --- |
| 1. psolc.py / line map vs Fig. 5, Defs 1–2, Thm 1 | FAITHFUL under the literal reading (Def. 1: the prefix minimum includes the start colour); C1–C11 all as mapped; A2–A5 correctly resolved |
| 1. ruling on A1 | the chapter's algorithm is the literal reading: Def. 1 ("0 ≤ i ≤ j"), Def. 2's first edge (min(c(v), c(v'))), Thm 1's proof (c(π·v) = min over 0..n) and Lemma 2's proof all include the start colour; Example 3 step (ii) is the only place that drops it and is an error in the worked example, not a definition. Both readings are sound (Lemma 2's segment argument works for either); the literal one decides at least as much on every game run (§4) |
| 2. hand run on psolc_min_n4_m6.pg, both readings | no vertex decided under either; Odd wins all four (§2) |
| 3. tc N = 2 | nothing decided under either reading (my code and the lane's); Oink: 11 vertices Even, 11 Odd |
| the instance kills every reading | yes: the two readings differ only in whether c(v_0) enters the minimum, and on this game that never changes a parity (§2) |

## 1. Implementation against the paper
Conventions. DTR is min-parity (p.3). The lane maps pr ↦ c = M − pr with M even ≥ max pr: order reversed, parity kept; psolC
reads colours only through min and %2, so this is exact. Player 0 = Even. OK.
Def. 1 (p.4): p wins π for reaching (X, p) under parity iff ∃ j > 0 with v_j ∈ X and min{c(v_i) : 0 ≤ i ≤ j} ≡ p; the
opponent wins iff every such visit has the minimum of parity 1 − p (in particular, if X is never visited after position 0).
Def. 2 (p.5): G^p_X on V × C(G)_⊥; owner of (v, l) = owner of v; E' = {((v, ⊥), (v', min(c(v), c(v'))))} ∪ {((v, c), (v',
min(c, c(v')))) : c ∈ C(G), v ∉ X or c%2 ≠ p}; nodes (v, c) with v ∈ X, c%2 = p have no edges (dead ends = targets). Thm 1
(p.6): Wr_p(G, X) = {v : (v, ⊥) ∈ Attr_p(G^p_X, Z)}, Z = X × {c : c%2 = p}. Fig. 5 (p.9): psolC tries player 0, then 1,
restarts on G \ W after a removal; tryPlayer: X = fixedpoint(G, V^p, p), returns Attr_p[G, X] if X ≠ ∅; fixedpoint: W = V;
repeat {X = X ∩ W; W = X ∩ Wr_p(G, X)} until X ⊆ W; return X.
psolc.py: `wr_in_X` builds the part of G^p_X reachable from X × {⊥}: from (v, ⊥) the record is min(c(v), c(w)) (literal) or
c(w) (`exclude_start`); from (v, l) it is min(l, c(w)); a node (v, l) with l ≠ ⊥, v ∈ X, l%2 = p gets no successors; the
attractor of Z is computed on the reachable part with the opponent's counters over the explored successors (all successors
of a reachable node are reachable, so counting is exact); result {x ∈ X : (x, ⊥) ∈ A}. This is Def. 2 + Thm 1 restricted
as the Fig. 5 caption prescribes ("only constructing nodes and edges ... reachable from X × {⊥}"); restriction is exact
because attractor membership of a node depends only on its forward cone. (v, ⊥) is never a target (⊥ has no parity), which
is Def. 1's j > 0. OK (C6–C9). `fixedpoint`: equivalent to Fig. 5's loop (the first X ∩ V is X; X = ∅ returns ∅, where Fig. 5
would evaluate Wr on the empty set, undefined by Def. 1 but harmless since ∅ ⊆ W: A2 OK). `try_player`, `run`: Fig. 5's
order (player 0 first, restart from player 0 after every removal; A3). `attr`: standard attractor inside the residual,
X included (C5). Residual = subgame on alive vertices, successors filtered by `alive` (C10, A5: the complement of a
p-attractor is a trap for p, so every remaining vertex keeps a successor). C11 (cost) not asserted by the code, fine.
`positional_strategies` (row S) is outside psolC (DTR Thm 3: psolC's strategies need memory); it solves the decided subgame
with Zielonka/Oink and asserts agreement — a verification aid, correctly labelled as the lane's own, not the paper's.
No unfaithful line found. Validation: my implementation (full product, no reachability restriction) gives on DTR Fig. 1 the
gfp {v0, v2} and solves all (Example 1 / Thm 3's Y); on Fig. 4 the gfp {v0, v1, v3, v5} and solves all (Example 2); on Fig. 6
nothing (Example 3), with the X-sequence V∖{v1} → {v2..v6} → {v2,v3,v4,v6} → {v2,v3,v6} → {v2,v6} → {v6} → ∅ under the
literal reading and DTR's printed sequence under the excluded-start reading — exactly the lane's A1 observation. The Fig. 6
transcription instances/dtr_fig6.pg (all squares; colours 2,1,2,0,0,2,2; v0→v1, v0↔v5, v1→v2, v2→v3, v2↔v6, v3→v4, v4→v0)
matches the rendered figure.
A1 in detail. DTR Example 3 (ii): "v4 and v5 are lost by player 0, as player 1 can move from them to node v0 ... and then play
as for the initial X to get minimal color 1". With c(v4) = 0 included (Def. 1), the play v4 v0 v1 v2 has minimum 0 and v4 is
won by player 0; only v5 (colour 2) is lost. So the example's step (ii) uses the minimum over positions > 0. Every formal
statement in the chapter includes position 0: Def. 1 ("0 ≤ i ≤ j"), Def. 2's first edge line, Thm 1's proof ("c(π) denote
min{c(v_i) | 0 ≤ i ≤ n}", δ(π·v) = δ'(v, c(π·v))), Lemma 2's proof ("min{c(v_j) | 0 ≤ j ≤ k}"). Ruling: the algorithm "from
the chapter text" is the literal reading; the example contains a slip. The lane implemented the literal reading and measured
the other: correct choice, correctly reported. Soundness of both: Lemma 2's composition covers every position ≥ 1 by exactly
one segment under either reading, and the min-Inf argument goes through (my re-derivation: if m = min Inf(π), the segments
containing m have minima ≤ m of parity p, some value m' ≤ m is a segment minimum infinitely often and hence in Inf(π), so
m = m' has parity p).

## 2. Hand run on psolc_min_n4_m6.pg, straight from the definitions
The file: v0: pr 1, Even, → v0, v1; v1: pr 2, Even, → v2; v2: pr 1, Even, → v2, v3; v3: pr 3, Even, → v0 (the results document
prints pr(v3) = 5; the file holds the TARGET-compressed 3; psolC depends on priorities only through order and parity, so the
two are the same instance). All vertices are Even's. Max-parity winner: every cycle (the loops at v0, v2 with top 1, the
4-cycle with top 3) has odd top priority, so Odd wins all four vertices (Zielonka agrees).
Colours (M = 4): c(v0) = 3, c(v1) = 2, c(v2) = 3, c(v3) = 1; Odd = player 1 wants min Inf odd.
Player 0: X = V^0 = {v1}. Wr_0(G, {v1}): every path from v1 back to v1 passes v3 (colour 1), so the prefix minimum of any
visit to X is 1, odd; v1 ∉ Wr_0. gfp = ∅ (both readings: the start colour 2 is not the minimum).
Player 1: X = V^1 = {v0, v2, v3}. Since all vertices are Even's, v ∈ Wr_1 iff EVERY play from v has some later visit to X with
odd prefix minimum. Round 1: v0 — Even plays v0 v1 v2 v2 v2 …: the visits to X are the v2's, each with prefix minimum
min(3, 2, 3) = 2 (literal) or min(2, 3) = 2 (excluded start): even, so Even detracts and v0 ∉ Wr_1. v2 — every first step
lands in X (v2 itself with minimum 3, or v3 with minimum min(3,1) = 1; excluded start: 3 or 1): odd, v2 ∈ Wr_1. v3 — the only
step goes to v0 ∈ X with minimum min(1, 3) = 1 (literal) or 3 (excluded start): odd, v3 ∈ Wr_1. X := {v2, v3}. Round 2: v2 —
first step to v2 or v3 ∈ X, odd minimum: in. v3 — Even plays v3 v0 v0 v0 …, never visiting X again: out. X := {v2}. Round 3:
v2 — Even plays v2 v3 v0 v0 …, never returning to X: out. X := ∅. gfp = ∅.
Neither player yields a fixpoint; psolC returns the game unchanged under BOTH readings. The readings differ only in whether
c(v_0) enters the minimum; at every decision above the parity is the same with or without it, so no reading of A1 rescues
the instance. My code and the lane's print identical traces (§4). The obstruction is the one DTR name on p.11 (weak-parity
acceptance): from v0 Even passes the colour-2 vertex v1 and then stays in the trap {v2} that Even loses in the parity game;
the prefix minimum 2 is never repaired.

## 3. tc N = 2
tools/oink/build/tc 2 (22 vertices, priorities 0..11). Oink (zlk, verified): 11 vertices won by Even, 11 by Odd. The lane's
psolc.py: UNDECIDED 22 of 22 under both readings. My implementation: the same, both readings (player 1's X-sequence
{10,14,19,21} → {10,19,21} → {10,19} → {19} → ∅, player 0's gfp empty). Confirmed.

## 4. Mine against the lane's on all small games
psolccheck.py --exhaustive: my psolC (full product) and the lane's psolc.py (reachable part), both readings, on every labelled
game with ≤ 3 vertices (4 + 324 + 175,616; all owners, priorities 0..n) and 3,000 random 4-vertex games (priorities 0..4):
decided sets and residuals identical on every game under both readings; no unsound decision against my Zielonka. Literal
psolC is complete on all 175,616 three-vertex games (the lane: all 41,440 canonical ones); the excluded-start reading is
complete on 175,484 (132 literal-only games, 0 the other way; the lane's 26 is the canonical count), and 9 literal-only among
the 3,000 random 4-vertex games, 0 the other way. So the lane's "literal is strictly stronger and never loses" holds on my
data too, and the two implementations are interchangeable on everything run.

## Findings
1. (N) A3-psolC-results.md prints the instance with pr(v3) = 5 while the committed file has pr(v3) = 3 (same game after TARGET
   compression). Print the file's priorities.
2. (N) psolC-impl.md A1 says "the switch implements the example's reading"; add that the example's reading is contradicted by
   Thm 1's and Lemma 2's proofs as well, so it is a slip in Example 3 and not an alternative definition (this report §1).
3. (N) The paper's Fig. 5 caption restricts G^p_X to the part reachable from X × {⊥}; my check used the full product and
   agrees, so the restriction (C9) is confirmed exact, not only argued.

## Gaps
- Thm 4's multi-round step and PA** ⊊ Solved(psolC): out of scope, not checked.
- The lane's exhaustive n = 4 and families data (A3 §3–4) are not re-run by me; the fidelity verdict rests on the line map,
  the hand runs and the exhaustive agreement of two independent implementations on n ≤ 3 plus random n = 4.
- Nothing Lean-checked (a dead-end record, not a result).
