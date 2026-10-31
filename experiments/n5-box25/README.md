# Box 25: INS, tight-arena insertions in W-constant intervals of N5 (L-COMP successor 8)
Lead 2026-10-31 02:50Z (D18), independent numeric side of L-SI box 53b / L-NEW box 106. Lane-PROVED, not refereed, in
docs/si/N5-SBF-box53.md §7 (l-si 481bc6c2): inside a W-constant interval I, KEYCH_I(x) ≤ 1 + INS_I(c). INS-POLY is open and equivalent
to the open core; L-RED 36 attacks it by construction (R153). Work 03:20Z-04:3xZ (date -u). Labels: DATA / CONJECTURE / READING. Not a
TARGET.md claim; G-N5-TIME open.

## Definitions (from the §7 text) and tool
- ins.py: my own implementation on n5b, written from the §7 text. L-SI's treestab.py was read for its scan ranges, not imported; it
  is run only by xins.py, in its own process.
- W-runs: as box 23 (rstar.wruns).
- W-constant interval I = [p, e] (e > p): a maximal stretch of a W-run with W_t = W_{t+1}, scanned left to right.
- c: an even W-cycle node. X_c := {x ≠ c : λ_W(x) = c}.
- Tight successors: T(y) := {z : λ_W(z) = c, y ⊕ W(z) = W(y)}, where y ⊕ (u, P, l) := (u, P ∪ {y} if y is more relevant than u, l + 1).
- Tight arena: A_t(y) := ({σ_t y} ∪ Iσ_t(y)) ∩ T(y).
- LexTree: layer by layer in W-length; Odd vertices follow τ; an Even vertex takes its arena element of least key.
- INS_I(c): transitions t → t+1, p ≤ t ≤ e − 1, at which some A_{t+1}(y) ⊄ A_t(y). This is treestab.py's range.
- INS2: the same with t ≤ e − 2 (the range in the §7 text). On every witness here INS2 ∈ {INS − 1, INS}.
- KEYCH_I(x): key changes of x over I.
- Checks (each 0 everywhere below):
  - LTX: LEX-TREE;
  - TSX: TREE-STABLE;
  - NOVT: OVERTAKE (each insertion is a strict Ξ-overtake);
  - KB: KEYCH ≤ 1 + INS.

## 1. Cross-check against treestab.py (L-SI, l-si 481bc6c2): 0 disagreements
- xins.py vs L-SI's committed experiments/si/sb53/tree_{alt,sbcg}.txt (fields intervals, LTX, TSX, NOVT, KB, MAXKEYCH, MAXINS):
  413 / 413 + 719 / 719 = 1,132 / 1,132 games agree (results/xins_alt.txt, xins_sbcg.txt).
  - tree_red.txt's two games (si/gate/inst/…) are not on trunk: 0 compared.
- u23sw64_n32: KEYCH 8 = 1 + INS 7, equal to treestab.py. Corpus max INS 7 / KEYCH 8, both there.
- tie_n32 (L-RED R152, l-red ac75403e, read with git show): reproduced.
  - n5b: 15 iterations, longest W-run 13 (R152: «iters 15 maxL 13»).
  - INS 5, KEYCH 6 on one interval, identical to treestab.py.
  - (R152's re-entry counts are o1.py's quantity, not re-measured.)
- Every climb pin below is also run through treestab.py: identical.

## 2. Climbs (climb25.py: fitness = (max INS_I(c), |I| of that (I, c), the run's longest W-run); start pair mutated)
| n | family | budget | steps | INS | |I| | W-run | INS / n | |I| / n | witness |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 16 | fresh | 900 s | 106k | 2 | 3 | 12 | 0.13 | 0.19 | |
| 24 | fresh | 900 s | 96k | 0 | 4 | 4 | 0 | 0.17 | |
| 32 | seeded u23sw64_n32 (INS 7) | 1,800 s | 57k | 7 | 8 | 11 | 0.22 | 0.25 | |
| 32 | seeded tie_n32 (INS 5) | 1,800 s | 54k | 8 | 9 | 15 | 0.25 | 0.28 | ins8_n32 |
| 48 | seeded u23sw64_n32, padded by 16 Even self-loops | 1,800 s | 33k | 9 | 10 | 11 | 0.19 | 0.21 | ins9_n48 |

- Pins (n5-box23/pin23.py ALL OK: n5 = n5b, Oink zlk, verify, xeng, rstar = xirise; treestab.py identical):
  - ins8_n32: sha1 b4f15f23e4a9…; it 20, 1 fallback (outside the interval); INS 8, INS2 7, KEYCH 3; interval [4, 13] of a W-run of 15.
  - ins9_n48: sha1 dc27b00c7fba…; it 17; INS 9, INS2 9, KEYCH 2; interval [3, 13] of a W-run of 11.

## 3. Findings
1. DATA: ins.py = treestab.py on 1,132 / 1,132 corpus games, on u23sw64_n32 (8 = 1 + 7) and on tie_n32 (6 = 1 + 5). LTX = TSX = NOVT = KB = 0
   everywhere measured, including every climb step: no climb stopped on a violation.
2. DATA: the max INS found is 9 (n 48), against corpus 7. INS / n ≤ 0.25; INS ≤ |I| always. On the maximal witnesses INS = |I| − 1:
   - ins8_n32, ins9_n48, u23sw64_n32 (7 of 8), and the fresh n 16 best (2 of 3), each with an insertion at almost every transition;
   - not on tie_n32 (5 of 7) or the fresh n 24 best (0 of 4).
   - So INS tracks the length of the W-constant interval, and the interval length is what the climbs fail to grow: |I| ≤ 10 at
     n ≤ 48.
   - Fresh climbs find INS ≤ 2. A W-constant interval with switches is rare in random games: L-SI counts 35 in the whole corpus (§7 DATA).
3. DATA: KEYCH can be far below 1 + INS: 3 vs 9 (ins8_n32), 2 vs 10 (ins9_n48). The bound is attained only on u23sw64_n32 / tie_n32.
4. CONJECTURE (data only, climbs n ≤ 48): INS_I(c) ≤ |I| − 1 with |I| = O(n) is all that local search reaches. No instance has INS > n / 4.
   This says nothing about constructions: L-RED R153 is the adversary.

## Files
ins.py, xins.py, climb25.py, climbs25.sh, check.sh (in verify), instances/ (pins), seeds/ (u23sw64_n32 copy; tie_n32 from l-red
ac75403e), climbs/ (each climb's best .pg/.start, climbs_end.txt), results/ (xins_*.txt).
