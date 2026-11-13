# R240: adversary against FLAT-IDX (L-RED-B 3, B3 §3) — VERDICT: DEPENDS ON NUMBERING (true for wrap104's numbering; false for W(H, s0) as defined; the numbering-free form «least root-first key» SURVIVES)
L-RED successor 68 (Opus 5.5, D21 / L53). Lead brief 2026-11-13 02:19Z: «R240: attack FLAT-IDX … «Depends on numbering» is a third possible
verdict. State which.» Labels: DATA (unit, set, scope, counter) / READING.
D1 (owner, verbatim): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the
fleet's own, as wrong until it passes the gauntlet below.»
**Source caveat: the file named in the brief (claude/l-red-b 9bce72fa, docs/red-b/B3-guide.md) was NOT on origin when I worked
(`git ls-remote`: claude/l-red-b = 9aa0771fa, 2026-11-13T00:43Z; 9bce72fa is not in its history; no B3-guide.md in its tree). I attacked
the claim as the Lead's brief states it; I did not read L-RED-B's proof sketch. Scope: N5 on W(H, s0) before its first fallback only;
nothing here is about N5 on other games; G-N5-TIME stays OPEN.**

## 0. The claim (from the brief) and the verdict
«On W(H, s0) (wrap104), before N5's first fallback and while τ is standard at the gates, σ_(j+1)(v) is the least-position option of
{σ_j(v)} ∪ Iσ_j(v) for every Even vertex v of H. So positions never increase, and at most |E(H)| iterations move H.»
POSITION of a pad m_(v,w) := the index of w in H.succ[v] (wrap104 creates the valve, pβ, pe, gate and pad of v's edges in that order).
| part | verdict | evidence |
| --- | --- | --- |
| «least position» and «positions never increase», on wrap104's numbering | SURVIVES (DATA) | notmin 0, idxinc 0 on 2,211 games (8 families, PERM none) |
| the same, on W(H, s0) as defined (box 104 §3 fixes only «the new vertices are indexed after V») | FALSE: depends on numbering | renumbering the pe's alone: notmin 1,947, idxinc 1,072 (PERM pe); 42 frozen instances, each re-run on n5v (xdiff 0) |
| numbering-free form: σ_(j+1)(v) = the element of A_j(v) with the least ROOT-FIRST KEY (index of its pe, then gate, then pad) = WRAP Remark (3) / R104 [RULE] | SURVIVES (DATA) | keymin 0 under all six numberings (13,266 games) |
| «at most |E(H)| iterations move H» | SURVIVES (DATA) | hbound 0 everywhere (it follows from the key form: keys only decrease, WRAP Remark (3): F ≤ m_E − |V_E| + 1) |
| proviso «τ standard at the gates» | holds on every run | taunstd 0 everywhere (WRAP (ii)) |
- So FLAT-IDX is a statement about wrap104's NUMBERING, not about W. Its correct numbering-free content is the root-first key rule,
  which is already WRAP Remark (3); «position» equals «key» exactly when the pe's of v are indexed in H.succ[v] order.

## 1. Why (READING; the Lead's two named weak points)
- «Same arena value»: in S4a's arena every option m of v ∈ V_E has W*(m) = (c_W, ∅, 3) and W*(v) = (c_W, ∅, 4) (WRAP (W6)); DATA: w6tie 0
  in R237. So SPEC's choice at v is not decided by values but by SPEC S1's procedure on the dual at the cycle node c_W.
- «BFS discovers v through its least-index pe»: SPEC FIX 4 (BFS: FIFO layers, predecessor lists in increasing index, the choice is the
  vertex from which v is first discovered). From c_W the first layer is c_W's predecessors in index order (the pe's), then their
  gates, then the pads, then v from the pad whose pe came first. That is the root-first key (pe, g, m), lexicographic in vertex
  indices. Nothing in W's definition orders the pe's of v by H.succ[v]; wrap104 does.
- DATA confirming the mechanism: permuting the gates alone (PERM g) or the pads alone (PERM m) changes nothing (notmin 0): the pe's
  index decides first and the pe's are distinct, so the gate and pad indices never break a tie. Permuting the pe's (PERM pe), all new
  vertices (all) or reversing them (rev) makes notmin and idxinc fire, while keymin stays 0.

## 2. DATA (experiments/red/r240/flat240.py; out/flat240.out; instances out/inst_*.pg, sha1 in out/SHA1SUMS)
N5 = n5s237 mode spec (SPEC-exact, R237) from S3 on W(H, s0) = box 104's wrap104.wrap (objects only), then the new vertices renumbered
(PERM); second engine box 190 n5v spec (state by state up to the first fallback F) on every 10th game and on every saved instance.
Families (aim237 + new «par»): eqprio 400 (one or two priority values: index ties), loops 300 (self-loops everywhere), oneowner 300,
optstart 200 (T = 0), par 400 (groups of Even vertices sharing one successor set and one priority: parallel structure), plen 300, pset
300, perm fig4 (Friedmann's G_2 under 10 renumberings of H): 2,211 games per numbering, n ≤ 12.
| PERM | notmin | idxinc | keymin | hbound | taunstd | notA | n5v xdiff (sampled) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| none (wrap104) | 0 | 0 | 0 | 0 | 0 | 0 | 0 (222) |
| g (gates only) | 0 | 0 | 0 | 0 | 0 | 0 | 0 (222) |
| m (pads only) | 0 | 0 | 0 | 0 | 0 | 0 | 0 (222) |
| pe (pe's only) | 1,947 | 1,072 | 0 | 0 | 0 | 0 | 0 (222) |
| all (random) | 1,944 | 1,050 | 0 | 0 | 0 | 0 | 0 (222) |
| rev (reversed) | 2,876 | 2,081 | 0 | 0 | 0 | 0 | 0 (222) |
- Per family (out/flat240.out): optstart is 0 under every PERM (no H-move before the first fallback); every other family fires under
  pe / all / rev, the largest being par (notmin 893 / 926 / 1,199).
- Instances (two per (PERM, family) that fires; .pg with sha1 in out/SHA1SUMS), each re-run on n5v: xdiff 0 on all 42. Example:
  out/inst_all_eqprio_6.pg, sha1 4a48aff5fb7be00ae8e8124d0df7a228a673c4ea: notmin 1, idxinc 1, F 2; n5v takes the same states.
- Control (must fire): N5′-xi (CTRL=1, mode xi, which takes the Ξσ-best option = Howard): notmin 197 and 215, keymin 197 and 215 on
  eqprio 200 and perm fig4 (5 games, F up to 27). hbound and taunstd have no control.

## 3. What this does and does not touch
- Proposed wording for B3 (L-RED-B's to decide): «σ_(j+1)(v) is the element of {σ_j(v)} ∪ Iσ_j(v) with the least root-first key (pe, g,
  m); with wrap104's numbering this is the least position in H.succ[v]». That is WRAP Remark (3), so FLAT-IDX adds nothing beyond the
  numbering remark. Any use of «position» in a proof about W(H, s0) must name the numbering.
- The bound «at most |E(H)| iterations move H» stands in both readings.
