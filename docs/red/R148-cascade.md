# R148: CONJECTURE CASCADE-LIN (L-NEW 40, box 99) is DEAD as stated. On cascl_K4_m8_N100 (n 222) one FRESH entry (a tick of the clock vertex 4) roots 121 > n/2 = 111 returns, 0.545n. The instance is mkrw LATE=1 K4 m8 plus 100 passive clones of one returning Even vertex. Each clone adds exactly one return to every root, so the ratio tends to 1. CASCADE-EQ's use is untouched: |F| is unchanged (44) and CASC ≤ n here. Shape (ii) (growing root depth) is not attempted
L-RED successor 35 (Opus 5.5; D1/D18). Lead 2026-10-30 21:49Z: «Make it R148, ahead of your HXS idea. Two kill shapes: (i) one fresh entry
rooting > n/2 returns; (ii) root chains of growing depth … Use L-NEW's box99/retcause.py root map (read only), and say whether your
construction's roots are FRESH.» Written 2026-10-30 from 21:50Z (date -u).
- Labels: DEAD (with instance) / DATA / READING. Not a TARGET.md claim. G-N5-TIME stays OPEN.
- Sources opened: l-new b376575c docs/new/N5-QRET-box99.md (all: §0-§3, the conjecture §2.4 «in every W-run, every fresh entry roots at
  most n/2 returns»); experiments/new/box99/retcause.py (docstring and output format). retcause.py is run UNCHANGED from a git archive
  of l-new b376575c (/tmp/claude-0/lnew99).
- The earlier R148 note on the HXS side (docs/red/R148-hxs.md, the Lead's first R148 target) is superseded as the box target. Its §1 data
  stands.

## 1. The kill (shape (i))
- Instance experiments/red/casc/instances/cascl_K4_m8_N100.pg + .start (n 222):
  - base: LATE=1 span/mkrw.py 4 8 (L-RED R127/R138; n 122);
  - plus casc/clone.py with X = 63, N = 100: 100 new Even vertices 122 … 221, each with X's priority (ties by index, SPEC A1), X's
    successors {64, 65}, no in-edges, and start σ0 = σ0(63).
- n5b SPEC: one W-run of 44 transitions, the same as the base. The clones have no in-edges, so no other vertex's play changes.
- L-NEW's retcause.py, unchanged (casc/retcause_out.txt):
  - «RUN 0-44 F 44 returns 798 … ROOT kinds {'FRESH': 798} distinct roots 7 max returns per root 121 chain depth {0: 780, 1: 18}»;
  - top root «('FRESH', 4, 38, 9), 121»: the fresh entry 4 → 38 at q = 9, a tick of the clock vertex 4.
  - 121 > n/2 = 111, so CASCADE-LIN fails.
  - Every root is FRESH (as the Lead asked). Chain depth ≤ 1.
- Checks: xeng state sequences identical (L-NEW n5.py on L-SI si.py vs n5b); Oink 8fbf0a7 --zlk winners equal to N5's and verify passes
  (rel2/oinkcmp.sh: OINK OK); casc/retx.py (L-RED, n5b) counts the same 798 returns.

## 2. Mechanism and scaling (DATA)
| instance | n | \|F\| | returns | max returns per root (retcause) | ratio |
| --- | --- | --- | --- | --- | --- |
| mkrw K4 m8 | 122 | 44 | 98 | 21 | 0.17 |
| + 60 clones of 63 | 182 | 44 | 518 | 81 = 21 + 60 | 0.45 |
| + 100 clones of 63 (pin) | 222 | 44 | 798 | 121 = 21 + 100 | 0.545 |
| sbq2_K8_m16 | 261 | 152 | 450 | 45 | 0.17 |
| + 100 clones of 119 | 361 | 152 | 1,950 | 145 = 45 + 100 | 0.40 |
- Vertex 63 alternates between 64 and 65. Its 7 returns are rooted at the 7 distinct roots, one each: 4 ticks of vertex 4 and 3 fresh
  entries of vertex 3.
- A clone does the same, so each root gains exactly one return per clone: CASC(e) = CASC_0(e) + N, while n = n_0 + N.
- So CASC / n → 1 as N grows. CASC > n/2 iff CASC_0 + N > (n_0 + N)/2, i.e. N > n_0 − 2·CASC_0 (here 122 − 42 = 80).
- Reading:
  - The clones are passive. They add returns and Even edges (m_E − n_E grows by N), but not transitions.
  - CASCADE-EQ, |F| ≤ (m_E − n_E)(1 + max CASC), stays true. The kill does not threaten WRUN-POLY. It only shows that «n/2» is not the
    constant.

## 3. What survives, and the repaired target (CONJECTURE / READING)
- CONJECTURE CASCADE-LIN′ (L-RED, data only): in every W-run, every Even vertex X returns at most once per root, so CASC_F(e) ≤ n_E.
  - On the five instances of §2 every clone and every original returner has exactly one return per root.
  - Not measured on the corpus: retcause.py does not print per-(X, root) counts, and I did not modify it.
- A kill of CASCADE-LIN′ in shape (i) needs one Even X with ≥ 2 returns rooted at the same fresh entry: an oscillation p → q → p of X
  inside one root's cascade (depth ≥ 1, a second return driven by another return of the same root). Clones of such an X would then give
  CASC / n → 2. Not built.
- Shape (ii) (root chains of growing depth, the counter shape) is not attempted. As the Lead notes, ARENA-MAX and SETTLE stopped every
  counter so far. In P-N5-SRC's terms each depth step is a source event whose block must re-wave the lower bits, which is R148-hxs §2's
  reset obstacle (L3).

## 4. Pins (experiments/red/check.sh «R148»)
- casc/instances/cascl_K4_m8_N100: regenerated from mkrw + clone.py and compared (cmp); casc/retx.py output; xeng; Oink.
- L-NEW's retcause output is kept as data (casc/retcause_out.txt). retcause.py is not on claude/l-red (not yet merged to the trunk), so
  check.sh does not run it.
