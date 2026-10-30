# R148: CONJECTURE CASCADE-LIN (L-NEW 40, box 99) is DEAD as stated, and so is every «CASC = O(n)» form. One FRESH entry roots 121 > n/2 (cascl_K4_m8_N100, n 222), 321 > n (cascl66_K4_m8_N150, n 272), and 3,620 = 8.6n (casctf_n10_N210, n 420). The instances are passive clones of an Even vertex that returns 1, 2 or 2N − 3 times per root (topfix_N, L-NEW box 52), so CASC can be Θ(n²) while |F| is linear. CASCADE-EQ stays a valid reduction, but its target must charge transitions, not return entries. Shape (ii) (growing root depth) is not attempted
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

## 3. Beyond n/2: CASC is not O(n) for any constant (DATA, DEAD forms)
- «CASC ≤ n» is DEAD as well. casc/instances/cascl66_K4_m8_N150 (n 272) is mkrw K4 m8 plus 150 clones of Even 66, which returns TWICE per
  root. One FRESH tick (('FRESH', 4, 38, 9)) roots 321 > n returns. xeng identical, Oink OK.
- Per-(X, root) counts on the corpus (casc/retcause_xr.py = L-NEW's retcause.py plus one XROOT output line; casc/runxr.sh →
  casc/xr_corpus.txt; 599 W-runs with returns, 0 errors):
  - max returns of one Even X per root: 1 in 530 W-runs, 2 in 52, 3 in 12, and 5, 9, 13, 17 on topfix_n4, n6, n8, n10 (L-NEW box 52);
  - topfix_N: 2N − 3 at n ≈ 21N (n10: 17 at n 210; n12, run separately: 21 at n 252, Even 235, root ('FRESH', 236, 237, 9), depth 0).
- So the repair «each Even X returns O(1) times per root» is DEAD too: the count grows linearly along topfix_N.
- With clones, CASC grows quadratically. casc/instances/casctf_n10_N210 (n 420) is topfix_n10 plus 210 clones of Even 193, default start
  written out by casc/defstart.py.
  - One FRESH root (('FRESH', 194, 195, 9)) has 3,620 = 50 + 210·17 returns, 8.6n. Chain depth 0. xeng identical, Oink OK.
  - Along topfix_N with M = n_0 clones: CASC ≈ n_0·(2N − 3) ≈ n²/42. Not built beyond n10. The two factors, clones and topfix's per-X
    count, are each pinned.
- Reading:
  - |F| is untouched in every case: clones are passive, and topfix's W-run is 58 transitions at n 210.
  - So CASCADE-EQ, |F| ≤ (m_E − n_E)(1 + max CASC), remains a valid REDUCTION, but max CASC can be Θ(n²) while |F| is linear.
  - CASC-POLY as a TARGET is therefore not sharper than the trivial CASC ≤ n_E·|F|. The cascade count conflates «many returns» with «many
    transitions».
  - A useful version must charge transitions, not return entries. For example: the number of TRANSITIONS containing a return rooted at e
    (RETT per root, box 98's unit). In casctf it is ≤ |F| = 58, whatever the clones do.
- Shape (ii) (root chains of growing depth) is not attempted. Corpus depth ≤ 1 on every instance here. As the Lead notes, ARENA-MAX and
  SETTLE stopped every counter so far.

## 4. Pins (experiments/red/check.sh «R148»)
- casc/instances/cascl_K4_m8_N100, cascl66_K4_m8_N150, casctf_n10_N210: regenerated (mkrw or L-NEW's topfix_n10, then clone.py and
  defstart.py) and compared (cmp); casc/retx.py return counts; xeng; Oink.
- L-NEW's retcause output is kept as data (casc/retcause_out.txt). retcause.py is not on claude/l-red (not yet merged to the trunk), so
  check.sh does not run it.
