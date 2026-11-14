# N5-CHAIN (box 125): how TWO-FIX windows chain inside a τ-stretch: every σ̄-change is a Ξ-change at an Odd vertex or a FLAT move (proved), so «windows per stretch» relocates onto XI-CH at Odd vertices
- L-NEW successor 44 (Opus 5.5), D14 / D18. Lead GO 2026-11-01 04:38Z: «BOX 125: the σ̄-change transitions of the fbg / fbA regime, which
  TWO-FIX does not cover. Measure how windows chain in a τ-stretch …; what moves σ̄ between them … Then ask whether «windows per τ-stretch»
  has a potential, or relocates to XO / XI-CH. … Say how ODIFF behaves across consecutive windows.»
- Read first: L-RED 40 R170 (claude/l-red 729fb521, docs/red/R170-twofix.md) §0-§1, Lemma FREEZE.
  - FREEZE: a TWO-FIX window is an initial segment of the N5 run on G_F, the game with every Odd vertex where σ̄ = τ frozen, under its (NT).
  - So ODIFF ≤ 1 windows are polynomial (RESULTS R17 / R51). It is L-RED's lemma, cited here as theirs (lane, not refereed).
- Definitions: τ-stretch as in P-N5-GATE. An SBC is a stretch transition k → k + 1 with σ̄_k ≠ σ̄_(k+1), where σ̄ := si.Engine's optimal
  Odd counterstrategy. Windows per stretch = SBC + 1.
  - For each Odd v whose σ̄(v) moves at an SBC, the move is classified two ways.
    - VAL if Ξ(v) changes there, FLAT if not (chain.py's field name is TIE).
    - TOW (new σ̄(v) = τ(v)), AWAY (old σ̄(v) = τ(v)) or SIDE (neither).
- Tool: experiments/new/box125/chain.py; runcorp.sh (→ c_sbcg.txt, c_alt.txt); red.txt (L-RED builds); pincheck.sh (→ pincheck.txt).

## 0. Answer
- PROVED (lane), §1: every σ̄-move at an Odd vertex v is a Ξ(v)-change (VAL) or leaves Ξ(v) unchanged (FLAT, which includes ties).
  Every VAL move has v's old play through an Even vertex switched at that transition (box 121 PLAY-CONTAIN).
  - So SBC ≤ #{transitions with a Ξ-change at some Odd vertex} + #{transitions with only FLAT moves}.
  - «Windows per τ-stretch» therefore relocates onto XI-CH restricted to Odd vertices, plus FLAT moves. This is the relocation the Lead
    anticipated, and it is not a new potential.
- DATA (§2):
  - L-RED builds: all σ̄-moves are VAL (0 FLAT), all are TOW or AWAY (0 SIDE), and there are 0 fallbacks at SBCs.
  - SBC = 6K on fbg (24 / 48 / 72 for K = 4 / 8 / 12, the same for m = 24 and 48) and 8K + 1 on fbA (33 / 65). One Odd vertex flips 2K
    times (MAXFLIP 8 / 16 / 24).
  - Corpus (813 distinct runs): VAL 8,105, FLAT 106 (29 runs), SIDE 2,851. The largest SBC / n is 2.3 (nep92_n40: 92 SBCs at n = 40); the
    largest single-vertex flip count is 67.
- ODIFF across consecutive windows (the Lead's question): it OSCILLATES in a narrow band and ends at 0 at the stretch's end.
  - fbA_K8: 32-34. fbg_K12: 48-51.
  - TOW − AWAY = the starting ODIFF when the run ends at ODIFF 0: bookkeeping, not a potential.
  - The windows are short (fbg: ≤ m; fbA: ≤ 2) with large ODIFF. So FREEZE + R51 (ODIFF ≤ 1) covers none of the builds' windows.
- Combination asked for («windows per stretch polynomial» + FREEZE / R51 per window): it does NOT combine on the builds. Their windows
  all have ODIFF ≥ 32. On the corpus, ODIFF ≤ 1 windows hold 5,167 of 6,775 window transitions (box 122, windows of length ≥ 4).
- nep92_n40 (n5-epoch/instances/nep92_n40.pg with nep92_n40.start) shows the other extreme:
  - One τ-stretch of 95 transitions has 92 SBCs, i.e. windows of length ~1, with ODIFF only 1-6.
  - The cost sits in ONE Odd vertex: v = 0, out-degree 16. σ̄(0) moves 69 times in the run (67 inside the stretch) and Ξ(0) changes 76
    times, at n = 40.
  - So the count here is XI-CH at a single high-degree Odd vertex. Windows are not the unit.

## 1. Lemma SBC-XI (PROVED, lane)
- Classification (definitional): a σ̄-move at Odd v at transition k → k + 1 is VAL if Ξ_(k+1)(v) ≠ Ξ_k(v), else FLAT. The data's «TIE»
  column counts FLAT moves.
  - FLAT covers two cases: a true tie (both choices optimal against σ_(k+1)), and the case where the old choice's value rose while another
    successor attains exactly the old value.
  - A first draft of this note called every FLAT move a tie. That was wrong; it is corrected here.
- Statement:
  - (a) SBC ≤ #{transitions with a Ξ-change at some Odd vertex} + #{transitions whose σ̄-moves are all FLAT}.
  - (b) For a VAL move, the (σ_k, σ̄_k)-play from v visits an Even vertex switched at k.
- Proof: (a) every SBC has at least one moving Odd vertex, and each move is VAL or FLAT. (b) is box 121 PLAY-CONTAIN with x = v. ∎
- So «windows per τ-stretch» relocates onto XI-CH at Odd vertices plus FLAT moves. FLAT moves are rare: 106 of 8,211 in the corpus, 0 on
  the builds.
- DATA: the one corpus move without a switched Even vertex on its old play (8,210 / 8,211) is a FLAT move, consistent with (b).

## 2. DATA tables
- L-RED builds (box125/red.txt; repaired starts as box 116b):

| build | n | K (iters) | stretch T | windows | SBC | VAL / FLAT | TOW / AWAY / SIDE | movers | max flips of one Odd vertex |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fbA_K4_m8_m8 | 136 | 44 | 44 | 34 | 33 | 72 / 0 | 44 / 28 / 0 | 23 | 8 |
| fbA_K8_m8_m8 | 192 | 88 | 88 | 66 | 65 | 144 / 0 | 88 / 56 / 0 | 39 | 16 |
| fbg_K4_m6_m24 | 178 | 140 | 139 | 25 | 24 | 56 / 0 | 36 / 20 / 0 | 21 | 8 |
| fbg_K4_m6_m48 | 250 | 236 | 235 | 25 | 24 | 56 / 0 | 36 / 20 / 0 | 21 | 8 |
| fbg_K8_m6_m24 | 234 | 272 | 271 | 49 | 48 | 112 / 0 | 72 / 40 / 0 | 37 | 16 |
| fbg_K12_m6_m24 | 290 | 404 | 403 | 73 | 72 | 168 / 0 | 108 / 60 / 0 | 53 | 24 |

  - On fbg, m multiplies the window length and not the number of windows. fbg_K4 with m = 24 or 48 has the same 24 SBCs and stretch
    lengths 139 / 235.
- Corpus (box125/c_*.txt, distinct (game, start)): 854 stretches, 12,282 stretch transitions, 4,102 SBCs (4,956 windows), 194 SBCs at
  fallbacks. Moves: 8,211, of which VAL 8,105 and FLAT 106; TOW 2,896, AWAY 2,464, SIDE 2,851. 20 runs have SBC > n.
- Pin (box125/pincheck.txt): nep92_n40 (ce224ec31e56…, start 10fdf3a3c76c…). Oink 8fbf0a7 --zlk and --tl «solution verified», regions
  AGREE, n5b identical (98 iterations, 8 fallbacks).

## 3. READING (not to sign)
- The chain of boxes 121-125 has reduced the τ-stretch to two counts, both Ξ-change counts.
  - Inside windows: fallbacks (box 123, CONJECTURE FB-XO, XO = Ξ-changes on O) and the climbs (TF-PH, conjecture).
  - Between windows: σ̄-moves = Ξ-changes at Odd vertices (SBC-XI).
- Every route so far ends at XI-CH, now with the extra information WHERE: at Odd vertices whose best response flips between τ(v) and
  another successor. nep92_n40's vertex 0 has 76 Ξ-changes against n = 40. Polynomially many Ξ-changes per Odd vertex is the open
  statement. Its natural measure is the out-degree (16 there).
- Candidate next box (untested): per-Odd-vertex Ξ-change count against out-degree and n. Is Ξ(v)'s change count at an Odd vertex
  ≤ deg(v)·(something polynomial)? Each Ξ(v)-change is the minimum over deg(v) successors moving. If each successor's Ξ rose monotonically
  with few changes the minimum would change few times. The successors' changes are the same problem one level down, which is XI-CH-POLY's
  recursion.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box125/{chain.py, runcorp.sh, c_sbcg.txt, c_alt.txt, red.txt, pincheck.sh, pincheck.txt}; check.sh
  block «box 125».
- FINDINGS:
  - SBC-XI PROVED (lane): σ̄-moves are Odd-vertex Ξ-changes or FLAT moves, so windows per stretch relocates onto XI-CH at Odd vertices.
  - ODIFF oscillates (32-34, 48-51) and is not a potential.
  - FREEZE + R51 does not combine on the builds: their windows have ODIFF ≥ 32.
  - nep92_n40 puts 76 Ξ-changes on one Odd vertex at n = 40.
- NEEDS: Lead: decide whether the lane continues on XI-CH at Odd vertices (per-vertex change count vs out-degree) or parks the τ-stretch
  line here. My context is about 375k (park at about 550k).
