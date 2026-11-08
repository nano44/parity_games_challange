# R224: adversary on L-LOWER 10's CONJECTURE STRETCH-AND-STACK (L-RED successor 58, Opus 5.5, D1 / D18 / D14; 2026-11-08, date -u)
Target: claude/l-lower 1802a93f235576d6d69b600527ee37131c915f5e, docs/lower/L10-design.md §1. It contains:
- Lemma STRETCH (PROVED, lane);
- Lemma ROOM-TIGHT on HIT7 (DATA: T′ = 510, one idle step in 219 of 289 gaps), with the target out/target_HIT7_H8.txt (sha1
  e031533adca196a246625ecc54b98a8f438380f2);
- the retrigger bill (261 events);
- CONJECTURE STRETCH-AND-STACK, rules R1-R5, with R3 as the attack point.
Lead (07:09Z): (a) check STRETCH and the T′ = 510 DATA with my own tools; (b) find a retrigger event class with no admissible selector
route, or a counting / parity obstruction. Model and notation: P-TOWER-FUEL §1-§2 (o_l, c_l = o_(l−1), j-windows, PULSE, GAP, Lemmas
0-3). Labels: SURVIVES / BROKEN; PROVED (lane) / DATA / CONJECTURE.

## 0. Verdict
| item | verdict |
| --- | --- |
| Lemma STRETCH | SURVIVES. The proof is right via R113 ALIGN; DATA 0 of 42,000 (§1) |
| T′ = 510 (minimal stretch of HIT7 at h = 8) and the retrigger bill (219 idle steps, 261 events, per-mover counts, free-and-holding counts) | SURVIVE: re-derived with my own constraint code (§2) |
| the frozen target out/target_HIT7_H8.txt (e031533a) and its description in §1a / R2 | BROKEN, fixable. Its first 7-window has ONE step, which no doubling level 7 can fill (P-TOWER-FUEL Lemma 1 (E1), (E4)). The §1a sentence «7-windows have lengths 2 (254) and 3 (1)» is false: they are 1 (1), 2 (253), 3 (1). Corrected target frozen (§2) |
| CONJECTURE STRETCH-AND-STACK (R3) | NOT refuted. New PROVED (lane) constraint PARITY-8 (§3): R3's suppliers are only the 2 movers of pair 8, and they must make ≥ 217 «shadow» moves at window-first steps, ≥ 147 of them right before an idle step. Each shadow move must be masked for every free-and-holding mover whose chain contains it |

## 1. Lemma STRETCH: proof and DATA
- Proof check. R113 ALIGN (landed) gives the key order of pair l as a function of s(2l), s(2l + 1), c_l(s) = o_(l−1)(s) and the
  constant γ_l. By induction from o_0 (pair 0 only), o_l is a function of the states of pairs 0..l. F(l) counts the changes of o_l
  along the run, and repeated states add no change. So F(0..h − 1) depends only on the sequence of distinct states of pairs
  0..h − 1. Correct.
- Scope remark: the lemma is about counting only. It does not claim that the stretched sequence is a run. That is the conjecture's
  job (R1-R3), as the note says.
- DATA (experiments/red/r224/okeys224.py, with L-LOWER's own okeys from sim6; unit: random redraw of every mover of pairs > l; set: the
  300 states of HIT7's stored run × 28 levels × 5 draws = 42,000; counter: o_l changed): 0.
- F(0..6) along the corrected target (§2), with pairs ≥ 7 held at the start: 2 6 14 30 62 126 254, equal to §1a.

## 2. T′ = 510 and the target, recomputed (experiments/red/r224/stack224.py)
- Input: HIT7 (l9/rec/LCOMP_L6_HIT7_F254_d28.txt, sha1 6a3b274d3af4d0d8f057f82c8f2919c84b7dd446, verified). Its run comes from
  L-LOWER's sim6 (T 299, 289 core steps).
- Everything else is my code, from P-TOWER-FUEL §1-§2:
  - j-windows cut at the changes of o_(j−1);
  - PULSE ≥ 8 − j and GAP ≥ 8 − j for j = 1..6 (Lemmas 2, 3);
  - every 7-window (cut at the changes of o_6) has ≥ 2 steps, because a doubling level 7 moves both members of pair 7 at distinct
    steps in EVERY 7-window, the first and the last included (Lemma 1 (E1) Φ(0) = 2, (E3), (E4));
  - minimal τ by longest path.
- Check E3 on the run: o_j changes exactly at pair-j moves for j = 1..6, 0 mismatches.
- Two constraint sets (out/stack224.txt):
  | variant | first o_6 change | T′ | 7-window lengths | windows < 2 | idle steps | gaps with an idle step | retrigger events |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | L-LOWER's (stretch.py: `need[(0, ch[0])] ≥ 2`) | 2 | 509 + their tail step = 510 | 1 (1), 2 (254), plus their tail | 1 | 220 + 1 | 219 | 261 |
  | corrected (first window ≥ 2: first change ≥ 3; last window ≥ 2) | 3 | 510 | 2 (255) | 0 | 221 | 219 | 261 |
- My «lower» variant equals L-LOWER's target line by line on lines 0-509. Their file adds a tail line 510, which makes the last window
  [508, 510], of length 3. In their file the first 7-window is [1, 1]: step 1 is idle and pair 6 first moves at step 2. Measured
  directly on e031533a: window lengths 1 (1), 2 (253), 3 (1).
- The corrected target = L-LOWER's states with one idle step PREPENDED, and without their trailing idle step. All 255 7-windows have
  length 2. Frozen: experiments/red/r224/out/target_fix.txt, sha1 12642daab5c24ce5f40b1d55cf1727d5c8d56a24.
- T′ = 510 = 2·255 is still the Lemma-3 bound, met exactly. The bill is unchanged:
  - 219 gaps; |M| 1 at 177 of them, 2 at 42;
  - per mover 12: 127, 10: 63, 11: 24, 9: 23, 4: 7, 6: 7, 8: 4, 3: 3, 5: 2, 13: 1 (261 in all);
  - free-and-holding 3: 155, 6: 118, 4: 117, 9: 101, 10: 89, 2: 97, 5: 44, 7: 37, 8: 27, 11: 2, 12: 1.
  All equal L-LOWER's need_HIT7_H8.out.
- Consequences for the note:
  - fix stretch.py (first change ≥ 3), re-freeze the target, and correct §1a's window sentence;
  - R2's «q_h moves exactly at the idle steps» needs an exception: in the corrected target the first window [1, 2] is all idle, so
    f_7 moves at idle step 1.

## 3. (b) Lemma PARITY-8 (PROVED, lane): what R3 forces on its suppliers
Premises: P-TOWER-FUEL Lemma 0 (MOVE: a mover moves only to c_l(s_t)) and Lemma 1 (E3) for a doubling level 7; R110's 𝓛^R_d (the key of
a level-l mover is c_l = o_(l−1), so only pair 8 is keyed through o_7). Setting: a run of G_8 whose pairs 0-6 follow the corrected
target and whose level 7 is doubling, as R1-R2 intend.
- (i) Every 7-window has exactly 2 steps and pair 7 moves twice in each (E4), so pair 7 moves at EVERY step 1..510, and by (E3) o_7 flips
  at every step. So c_8(s_t) = a* for every even t and ā* for every odd t.
- (ii) By Lemma 0, a level-8 mover y moves at an even step only to a*, and at an odd step only to ā*. After an even-step move, y is on
  c_8 at every later even step, so it is not free there. Its next move is therefore at an odd step, and vice versa: y's moves alternate
  in parity.
- (iii) Measured on the corrected target (out/parity224.txt):
  - the idle steps are step 1 and 220 even steps;
  - the 219 idle steps that carry the bill are even;
  - the o_6 changes, i.e. the window starts and core steps, are all odd;
  - 35 windows have a core second step.
  - R3 supplies every retrigger event at idle step i by a mover «keyed through o(h)» that moves AT i. By (i) and R110 those are the 2
    movers of pair 8: R3's «level h + 1 or above, keyed through o(h)» can only mean level h + 1, since a level ≥ h + 2 mover is keyed
    through o(h + 1) or higher.
  - So pair 8 makes ≥ 219 even-step moves, and by (ii) ≥ 219 − 2 = 217 odd-step moves.
- (iv) An odd-step move of y at t changes every chain through y at t. That is seen at step t + 1 by every core mover free there. The
  two movers of pair 8 can sit on at most 2·35 = 70 odd steps followed by a core step. So ≥ 217 − 70 = 147 of these SHADOW moves are
  followed by an idle step. There, every free core mover must HOLD, against a chain change it did not ask for.
- Reading for L-LOWER's item 2:
  - R3's selector budget must route 261 wanted events AND mask ≥ 147 shadow events. Both are carried by the same two pair-8 movers.
  - Their shadow moves fall on the window-first steps, which are exactly the steps where the free-and-holding counts (3: 155, 6: 118,
    …) apply.
  - This is not a contradiction: selectors can mask, as in HIT7's own τ / σ / ρ. But it fixes what to search for: a ranksolve with
    pair 8's alternation built in.
  - It also gives the refutation target the note names: an event or shadow class with no admissible selector route under PARITY-8.
  - Not done here: the ranksolve search itself (it needs L-LOWER's level-8 build, item 2).
- A route around PARITY-8: R3 could take its suppliers from pair 7 itself, since q_7 moves at every even idle step, or from levels ≥ 9,
  which are not keyed through o_7 and so do not alternate. That would change R3 as worded. I record it as a design option, not a gap.

## 4. Tools, instances, sources
- experiments/red/r224/stack224.py (minimal stretch, both variants, the target and the bill), okeys224.py (STRETCH premise + F-profile),
  out/stack224.txt, out/okeys224.txt, out/parity224.txt, out/target_fix.txt (frozen corrected target), out/target_lower.txt (my
  reproduction of L-LOWER's constraint set).
- Env LOW = worktree of claude/l-lower 1802a93f (git worktree add --detach). Only sim6.run / sim6.okeys are used from it.
- Sources opened: claude/l-lower 1802a93f docs/lower/L10-design.md (whole), P-TOWER-FUEL.md §1-§2, L6-supplier.md §0, L7 / L8 / L9-design
  §0, experiments/lower/l10/stretch.py, need.py, out/target_HIT7_H8.txt, out/need_HIT7_H8.out, l9/slack.py (windows).
Not a TARGET.md claim; not M3 or M4.
