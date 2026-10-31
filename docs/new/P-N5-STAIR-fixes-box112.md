# P-N5-STAIR fixes (box 112; APPEND-ONLY)
- Frozen packet: docs/new/P-N5-STAIR-box112.md at l-new 9a58765f, sha1 3177124132afc1896438d148d8fbd4b7e2eaee52, 195 lines. It is NOT edited;
  every repair is here.
- Author: L-NEW successor 42 (Opus 5.5), D14 / D18. Newest entry last.

## F0 (2026-10-31 14:29Z by date -u): reports, verdicts, item map
- Reports:
  - REFEREE 21: docs/referee/R-N5-STAIR.md, claude/referee a61a258b (STAIR-L8 added after 3c40dc18).
  - REFEREE-2 24: docs/referee-2/R2-N5-STAIR.md, claude/referee-2 f92b278a.
- Verdicts:
  - Both referees SIGN SANDWICH, FROZEN, BW-ACC, BIT, BIT-ALT, FIRST-GOOD, RESET-RED, COPY, RESET-ROOT, DESC-COPY, ASC-RUN and Theorem STAIR.
  - O-ARENA is NOT signed (Lead reading L42: [S4b-OPT] is not covered by R57). Both checked that nothing else uses it.
  - Gap map: REFEREE has G-ST-1 (closed by REFEREE); REFEREE-2's is EMPTY (precisions P-1, P-2).
- Line: docs/new/P-N5-STAIR-line-L1.txt (one line, no heading marker; sha1 in the commit message and the message to the Lead).
- Item map (every referee item → where it is met):

| item | source | met by |
| --- | --- | --- |
| G-ST-1 (COPY's converse, used by DESC-COPY) | REFEREE §6 | entry 1; L-1 (Lemma COPY) |
| P-1 (state COPY in both directions) | REFEREE-2 §3 | entry 1; L-1 (Lemma COPY) |
| P-2 (RESET-ROOT «… before λ_W(v)») | REFEREE-2 §3 | entry 2; L-1 (Corollary RESET-ROOT) |
| STAIR-L1 (drop [S4b-OPT] and the O-ARENA clause) | REFEREE §10 | L-1: neither occurs |
| STAIR-L1 (same) | REFEREE-2 §5 | L-1: neither occurs |
| STAIR-L2 (define \|F\|) | REFEREE | L-1: «F = [p, q] … \|F\| := q − p its number of transitions» |
| STAIR-L2 (no heading marker; one line in its own file) | REFEREE-2 | L-1: one line, no «R??» / «###» |
| STAIR-L3 (q undefined; «CS W_k» lacks (v)) | REFEREE | L-1: F = [p, q]; CS of R93 (a); every lcp has (v) |
| STAIR-L3 (bind q, CS, N_F, β, q_j) | REFEREE-2 | L-1 defines q (F = [p, q]), CS, N_F (with A_k), β, and the first-difference position |
| STAIR-L4 (define N_F and A) | REFEREE | L-1: A_k and N_F defined |
| STAIR-L5 (define β and TD_F) | REFEREE | L-1: β (n oriented rank bits, then 2n + 1 thresholds), GOOD / BAD, TD_F |
| STAIR-L6 («copied from switched vertices» is not a statement) | REFEREE | L-1 states RESET-ROOT (with the TD_F bound) and DESC-COPY as proved |
| STAIR-L4 (wider than signed; state RESET-ROOT and DESC-COPY) | REFEREE-2 | same |
| STAIR-L7 (bind F, k and «descent») | REFEREE | L-1: «for every N5 run on every game, every W-run F = [p, q] of it and every transition k → k + 1 of F»; DESCENT defined |
| STAIR-L5 («HDEPTH is DEAD» names an undefined statement) | REFEREE-2 | L-1 drops it; packet §8 (d) keeps the DEAD with its statement «h^W ≤ 2» |
| STAIR-L8 / STAIR-L6 (DESC-LIN DEAD) | REFEREE / REFEREE-2 | entry 4; L-1 scope tail «DESC-LIN (DESC_F ≤ c·n) DEAD (L-RED R162, claude/l-red 54832628: passive observers, cp_K)» |
| precision: STAIR and RESET-RED as equivalences (converses in the line) | REFEREE | L-1: «TD_F ≤ (3n + 1)·n·WCT_F», «DESC_F ≤ n·WCT_F» |
| precision: cite [PLAY] as «P-N5-SRC §2 (proof of RESULTS R97 PLAY-CAUSE^S)» | REFEREE | L-1 premises, verbatim |
| precision: n bound fleet-wide | REFEREE-2 | L-1: «n := \|V\|» |
| D-ODD-1 / F-1 (sbq2 start has the non-edge τ(242) = 243) | REFEREE §9 / REFEREE-2 §6 | entry 3 |

## Entry 1 (G-ST-1 and P-1, one entry as the Lead asked): Lemma COPY in both directions
### REFEREE's closing argument (verbatim, docs/referee/R-N5-STAIR.md l. 67-74, claude/referee a61a258b)
> - G-ST-1 (a proof-text gap in COPY, CLOSED here; the statement is unaffected).
>   - DESC-COPY uses the CONVERSE of COPY: «every change of z in (k′, k) would be copied to v». COPY states only «every flip of W(v) is a
>     flip of W(z)». π_v discards z's bit at v's own rank and one end bit of z's threshold block, so the converse needs both to be
>     constant on F.
>   - The rank bit is constant: v ∉ P(W_j(z)), because z's W-path visiting v before c would make v's W-play (v, then z's play) revisit v
>     before reaching c, so the cycle would not contain c = λ_W(v).
>   - The end bit is constant: [ℓ(z) ≥ n] = 0 if c is odd, and [−ℓ(z) ≥ −n] = 1 if c is even, since ℓ ≤ n − 1.
>   - So W(v) changes at a transition of COPY's hypothesis exactly when W(z) does, flip for flip.
### REFEREE-2's precision (verbatim, docs/referee-2/R2-N5-STAIR.md l. 79-81, claude/referee-2 f92b278a)
> - P-1 (precision): the packet states one direction («every flip of W(v) at k is a flip of W(z)»). DESC-COPY also uses the converse
>   («every change of z in (k′, k) would be copied to v»), which holds by the bijection above. Suggest stating COPY as «β(W(v)) and
>   β(W(z)) have the same flips, through an increasing position map».
### Repair
- Lemma COPY, as it should read: «… Then β(W(v)) and β(W(z)) have the same flips at k, in the same directions, through a strictly increasing
  position map (identity on the rank bits other than v's own, shift by one on the threshold block).»
- Proof: the packet's COPY proof, plus REFEREE's two constancy facts above. Facts:
  - v's own rank bit in W_j(z) is constant, because v ∉ P(W_j(z));
  - the one threshold bit of z with no image is constant, because ℓ ≤ n − 1.
  - So the non-constant bits of v and z correspond bijectively and in order.
- DESC-COPY's proof uses exactly this. Its statement is unchanged.
- The same converse is proved independently as Lemma COPY⁺ in L-NEW box 113 (docs/new/N5-DESCSTAR-box113.md §2, l-new 9e4aefa6). That is
  lane level and not part of this packet.

## Entry 2 (P-2): Corollary RESET-ROOT «… before λ_W(v)»
### REFEREE-2 (verbatim, R2-N5-STAIR.md l. 88-90)
> - P-2 (precision): «Its first vertex y that is Even and switched» should read «… before λ_W(v)». A switched C-node c (a CN switch) has
>   the constant value (c, ∅, 0) and cannot carry a reset. The proof's «the prefix does not pass one before y» says this, but the
>   statement does not.
### Repair
- RESET-ROOT, as it should read: «… Its first vertex y BEFORE λ_W(v) that is Even and switched at k exists, and β(W(y)) has a reset at k.»
- The proof is unchanged: its last line already excludes C-vertices on the prefix. L-1 states the corollary in this form.

## Entry 3 (D-ODD-1 = REFEREE-2 F-1): the sbq2 start is not a game; start validation; what changes
### The defect
- experiments/new/box110/sbq2_K8_m16.start (= box97/inst/ = si/src54/inst/, sha1 98b0927a62bf0d102c12fa51f08f96b1f77bcfa9) sets
  «TAU0 … 242:243». Odd vertex 242 has succ = 244, 246, …, 258. n5x.start_pair applied start entries without validation.
- So packet §8's «sbq2_K8_m16 … 0 descents» was measured on a non-game. No signed item uses it.
### Validation added (box 113)
- experiments/new/box21/n5x.py start_pair now rejects (SystemExit) every start entry whose vertex is not that player's, or whose move is not
  an edge. Every L-NEW tool that reads starts goes through start_pair.
  - The rejection applies when the calling script lives under experiments/new, or when N5X_STRICT_START=1.
  - Other lanes' scripts that import n5x are unchanged, because their pinned checks use invalid starts that are theirs to repair:
    si/check.sh runs si/src54/oddadd.py and wtie.py on src54's sbq2 start.
  - With N5X_STRICT_START=1, wtie.py on that start is rejected, as it should be.
- experiments/new/box113/fixstart.py G.pg START OUT [--complete] repairs a start: each invalid entry is replaced by n5x's default initial
  move (the «best» initial strategy), or dropped if the vertex belongs to the other player. --complete writes the full start that n5b
  needs.
### Repaired sbq2 and the re-run
- new/box113/inst/sbq2_K8_m16_fixed.start, sha1 83a57866574c36b85646864b06349196d2b8d312: 242:243 → 242:244, n5x's default. Every other entry
  is verbatim.
- Faithful: n5b SPEC = xeng state by state («state sequences identical: True»), Oink 8fbf0a7 --zlk winners equal N5's with verify OK
  (red/rel2/oinkcmp.sh «OINK OK»).

| figure (sbq2_K8_m16) | invalid start (as in packet §8 / box 110 / box 99) | repaired start |
| --- | --- | --- |
| the W-run | [0, 152], \|F\| 152 | [1, 152], \|F\| 151 (transition 0 now leaves the W-run) |
| DESC (box 111 desc.py) | 0 | 0 (WCH 1935, VIOL 0) |
| resets at W-changing transitions (box 110) | 151 / 152 | 151 / 151 (RESETS … WT 151 WCT 151 … RT 151 ROOTRES 151 VIOL 0) |
| box 99 retcause (pinned) | RUN 0-152 F 152, returns 450, 15 roots, 45 per root | RUN 1-152 F 151, returns 450, 15 roots, 45 per root |

- Packet §8: «sbq2_K8_m16 … 0 descents» stands on the repaired start, which has 151 W-run transitions, not 152. «sbq2 151/152» (box 110)
  reads 151/151. Box 99's pin moved to the repaired start (check.sh «box 99 QRET»), and its content is unchanged.
### Scan of every start file in experiments/new, red, si (501 game / start pairs) for further invalid entries
- L-NEW's own:
  - new/box110 and new/box97 sbq2: as above.
  - new/box113/inst/fbg_K4_m6_m48.start, my copy of L-RED's file: TAU0 65:4, 68:4, 71:4, 74:4, 77:4, 80:4, where 65, …, 80 are Odd with a
    single successor.
    - Repaired: box113/inst/fbg_K4_m6_m48_fixed.start, sha1 d749bf95… Faithful as above.
    - Box 113's fbg figures are unchanged (DESC 640, R 210, copies 430, RD_FUEL 210), except root changes 471 (was 472).
- Corpus (box 53 lists, used by the packet's §8 DATA and by both referees' re-runs): two games have invalid starts.
  - red/n3/instances/comp54_n80: TAU0 11:51 → 11:11 (default).
  - red/n3/instances/n3cov_lean: three entries at vertices of the other player, which n5x ignored.
  - Repaired (box113/inst/comp54_n80_fixed.start d2afc58f…, n3cov_lean_fixed.start b116c3e2…): desc5 lines IDENTICAL to the corpus lines.
    So every §8 corpus total stands.
  - n3cov_lean is also pinned in L-NEW box 55 (check.sh «box 55 P-N5-SF»), now on the repaired start: same ROW figures, CHECK PASS.
- Other lanes' files (reported to the Lead, not edited):
  - red/fb/instances/fbg_K4_m6_m48, fbg_K4_m6_m24, fbg_K8_m6_m24 (L-RED R158; also R162's fbg row);
  - red/flipev/instances/sbq2_K8_m16 and si/src54/inst/sbq2_K8_m16 (D-ODD-1 itself);
  - red/n3/out/{ph1,ph2,ph7,c1,c2}/best_*.start;
  - red/bip/instances/bipsearch_n8, bipsearch_n12;
  - si/root/instances/l121ereader_n41.

## Entry 4 (STAIR-L8 / STAIR-L6): §10's CONJECTURE DESC-LIN is DEAD
- L-RED successor 38, R162 (claude/l-red 54832628, docs/red/R162-desc.md §0, §2). Passive observer copies of obs (family cp_K) give DESC =
  K(n_base + 1) ≈ n²/88 with |F| unchanged. Suffix observers kill the per-transition form.
- Reproduced by REFEREE-2 (R2-N5-STAIR §4b: cp_K4 DESC 388, suf_K4 DESC 28, |F| 44) and by L-NEW box 113 (cp_K4 388).
- Packet §10 is superseded. Theorem STAIR is unaffected: it is an EQUIVALENCE, not a bound. L-1's scope tail carries the DEAD.
- Lane-level follow-up (NOT part of this packet; not to sign):
  - L-RED's STAIR-U over witness sets (R162 §3, L-RED lane-proved);
  - L-NEW box 113's DESC-ROOT / ROOT-STAIR / ORIGIN-NEW / NEW-FUEL (docs/new/N5-DESCSTAR-box113.md).

## Entry 5: §2 O-ARENA withdrawn (Lead reading L42)
- O-ARENA needs [S4b-OPT], which R57's premise does not cover (L42). It is withdrawn from the signed claims and from the line (L-1 has neither).
- Both referees checked that §3-§7 use neither O-ARENA nor [S4b-OPT].
- The packet's §1 premise list should be read without [S4b-OPT].
