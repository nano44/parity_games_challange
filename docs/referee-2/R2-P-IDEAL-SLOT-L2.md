# R2-P-IDEAL-SLOT-L2: line L-2 of P-IDEAL-SLOT against my REQUIRED SL-L1, SL-L2; P-IDEAL-SEG fixes entry 1
REFEREE-2 successor 27 (Opus 5.5, D12/D19). Written 2026-11-04 14:37Z (date -u). Object: claude/l-new 6eb389a6.

## Hashes (git show 6eb389a6:FILE | sha1sum)
- docs/new/P-IDEAL-SLOT-line-L2.txt 55e74726f0c7e6c6e27f780b779788014cc97e29, 1 line, 0 «|»; docs/new/P-IDEAL-SLOT-fixes.md 44bf76e7…,
  36 lines; packet 62901b5f and L-1 17236fb1 unchanged. docs/new/P-IDEAL-SEG-fixes.md 2e3dd532…, 20 lines.

## L-1 → L-2 token diff (my own git diff --word-diff run) = fixes entry 1's list (SEG s_(a−1); SHIFT construction; LIFT construction;
provenance). Nothing else changed.

## SL-L1 (LIFT construction): MET
- L-2: «(LIFT) at any degree, raising every level of a genome by one and adding two level-0 movers A, B with two options each (Ξ-target X
  and no W-target, four new ranks above all others, all of even parity, with the larger of each mover on its option 0, four new gates
  above all others, start option 0), every option of a mover of old level 0 getting W-target A, gives a genome in which A and B never move
  and whose run on the old movers is the old run, state for state».
- Every element of packet §5's construction is stated, including the single W-target A that my control lift_split_ctrl.json needs.
  Same content as my proposed text. ✓
- SHIFT (my P-2 = REFEREE SLOT-L1): «lowering every level ≥ 1 by one, the level-0 movers staying at level 0 (every option of a mover of
  old level 1 loses its W-target and gets the gate g(w, k_w) · Γ + g(x, k), with w its old W-target, k_w the only option of w and Γ
  larger than every gate; every other field and the start unchanged)» = packet §3. ✓
- SEG (my P-1 = SLOT-L3): «at the state before the interval's first step (s_(a−1))» = §1. ✓

## SL-L2 (scope of the SANDWICH remark in the DEAD clause): NOT MET
- L-2 keeps «and by SANDWICH any bound on that number in terms of d is a bound on T*(d − 1)» unchanged from L-1. «That number» is still
  bound only to SEG1-2D's class (2-wide degree-2 ladders, no degree-1 movers). SANDWICH gives the implication only for bounds over 𝓛_d
  (packet §6: «any bound seg1 ≤ f(d) on 𝓛_d implies T*(d − 1) ≤ f(d)»). A bound over degree-1-free ladders would bound only their own
  (d − 1)-supremum, which is not known to equal T*(d − 1). The DEAD clause does not bind «over 𝓛_d».
- Required word change for L-3 (one insertion):
  «and by SANDWICH any bound on that number in terms of d is a bound on T*(d − 1)» →
  «and by SANDWICH any bound on that number over 𝓛_d in terms of d is a bound on T*(d − 1)».
- Everything else in L-2 MATCHES (definitions 𝓛_d, T*(d), T; SEG-CAP; SANDWICH; DEAD data; scope tail; DATA; provenance).

Verdict on L-2: NOT YET. One word change (SL-L2) gives L-3; with it, MATCHES.

## P-IDEAL-SEG fixes entry 1 (my F-1, F-2): CORRECT
- F-1: new text «reached only by genomes with at most one degree-2 mover, e.g. r150_049.json with none: T 0, product 1». Checked:
  r150_049 has N 1, one option (T 0, product 1). My max ratio by number of degree-2 movers on box150/out/rand: {0: 1.0, 1: 1.0, 2: 0.6667, …},
  so «at most one» is exact on that set. ✓
- F-2: new quote «after a level-0 reset, the next segment is a sub-run of a segment already seen» = docs/new/N5-SEG-box157.md l. 24
  verbatim (8291ecf7); «no new states above» is now labelled as the lane's paraphrase. The killed statement is unchanged. ✓

## Addendum 1: line L-3 (claude/l-new b261c3f9), 2026-11-04 15:56Z (date -u)
- Hashes: docs/new/P-IDEAL-SLOT-line-L3.txt 0c51ce6da0a655c31112515c78cb0b5d22690168, 1 line, 0 «|»; P-IDEAL-SLOT-fixes.md cae85ce1…,
  43 lines (entry 2 appended); L-2 55e74726 and packet 62901b5f unchanged.
- Byte test: L-2 with its single occurrence of «any bound on that number in terms of d» replaced by «any bound on that number over 𝓛_d
  in terms of d» equals L-3 exactly (True). Token diff: one insertion «over 𝓛_d». SL-L2 MET.
- Optional only: the provenance tail still names «fixes entry 1»; entry 2 holds this change.
- Verdict: L-3 MATCHES. All my items on P-IDEAL-SLOT are closed.
