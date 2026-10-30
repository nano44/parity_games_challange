# R-N5-SETTLE-C: REFEREE §C on P-N5-SETTLE: cross-map against REFEREE-2 (R2-N5-SETTLE, claude/referee-2 301042bb), joint gap map, block-length reconciliation
Referee: REFEREE (successor 20), Opus 5.5 (D15).
- The Lead gave the §C word at 19:07Z (read 19:16Z by date -u). I opened docs/referee-2/R2-N5-SETTLE.md @ 301042bb (125 lines) only after
  that word, and after my report R-N5-SETTLE.md (1df722e9) was pushed.

## 1. Cross-map
| item | REFEREE (R-N5-SETTLE) | REFEREE-2 (R2-N5-SETTLE) | joint reading |
| --- | --- | --- | --- |
| Claim RG′ | SIGNED | SIGNED (against si.py l. 112-149) | agree. Both note that a good-u edge u → y with y ∈ M is never length-tight |
| T54 IDX-MONO / LEX-BFS as used in Case 2a | SIGNED (from SPEC S1 (iv)) | SIGNED (from si.py's recursion and BFS) | agree. Two sources, the same derivation |
| PLAY-CAUSE, W-MON, PATH | SIGNED | SIGNED | agree. Both: Ξ(x) is a function of (y_0 … y_i, Ξ(y_(i+1))) even if the play re-enters the prefix |
| RUN-SETTLE (Cases 1, 2a, 2b, 2c), RUN-COUNT | SIGNED | SIGNED | agree |
| HEAD-RED, T-XCH | SIGNED | SIGNED | agree |
| §1 «y ⊕ · preserves and reflects ⊴ and ◁» on one cycle node | not raised (I raised the same point for WRUN Fact EXT, not here) | N-1, with an instance where even non-strict monotonicity flips | I agree; I missed it here. Every use (Cases 2, 2b, 2c) has y in neither path set. Packet erratum |
| ARENA-MAX quote | verbatim modulo the bullet layout; SHA missing (N2) | N-2: one list marker dropped | same observation |
| RG′ word-diff note incomplete ((B)'s heading) | N1 | not raised | mine; wording |
| line: F unquantified | L1 REQUIRED | L-1 REQUIRED | same |
| line: T undefined (T-XCH) | L2 REQUIRED | L-3 REQUIRED | same |
| line: Iσ_k unbound | L4 (precision) | L-2 REQUIRED | I agree it is REQUIRED: it is used in H_k's definition and in nothing else in the line. I upgrade it |
| line: k free in Claim RG′ (and in H_k / tightness) | L3 REQUIRED | not raised | I keep it REQUIRED. «at every S4a step of a W-run … W_(k+1)» has no binder for k |
| line: «has ℓ_(k+1) ≥ …» without its argument | not raised | L-4 (precision) | agree |
| line: unlanded ARENA-MAX / LEX-BFS / IDX-MONO in the proof note | L4 note | L-5 (precision) | agree |
| line: tail lacks «not M3, not a step-4 pass, not a TARGET.md claim» | MISSED | L-6 (precision) | agree; every landed N5 line carries it |
| DATA: longest event-free block | N3: «44» is a mislabel; mine 63 (runfam_K40) on n ≤ 100 | N-3: 67 (gate_K64_n581), not reconciled | reconciled in §2 |

## 2. Longest event-free block: reconciled across three engines
- My engine (settle_probe.py) on the named instances:
  - gate_K64_n581 (n 581): 67 from the best-reward start; 3 from its .start.
  - runfam_K40 (n 79): 63 (best-reward start and .start alike).
  - x32_rand64 (n 64): 55. x32_rand48: 44.
- The lane's rwin output (experiments/si/heads52/rwin_*.txt @ 6a70a520) gives exactly these:
  - gate_K64_n581 has two runs, «LMAX 68 E 1 WMAX 67» and «LMAX 71 E 64 WMAX 3»;
  - runfam_K40 «WMAX 63»; x32_rand64 «WMAX 55»; x32_rand48 «WMAX 44».
- REFEREE-2's log (R2-N5-SETTLE/logs, 301042bb) says «max max_block: (67, 'red/usplit/instances/gate_K64_n581.pg#0')» (#0 = the default
  start) and «max max_E_F: (64, '…gate_K64_n581.pg#start')». So its report's «67 (gate_K64_n581 + start, …)» puts the start label on the
  wrong figure. The log agrees with my engine and the lane's.
- My earlier «63» was the maximum over n ≤ 100 only (MAXN 100 skipped gate).
- Joint reading: the longest event-free block in the corpus is 67 at n 581 (best-reward start), far below n − 1. The packet's §9 «the longest
  event-free block is 44 at n 48» is a mislabel. 44 / 48 = 0.92 is the largest ratio WMAX / n, where x32_rand48 leads. Fix §9 to «the
  largest ratio of an event-free block to n is 44 / 48 (x32_rand48); the longest block is 67 (gate_K64_n581, best-reward start)».
  DATA only.

## 3. Joint gap map
- Packet items to sign: EMPTY on both sides. Nothing FALSE.
- Packet errata:
  - ⊕ monotonicity needs y ∉ P of both arguments (R2 N-1);
  - ARENA-MAX quote marker and SHA (R2 N-2 / my N2);
  - RG′ word-diff note (my N1);
  - §9 longest block (my N3 / R2 N-3, reconciled).
- Line, REQUIRED (union):
  - F quantified (L1 = R2 L-1);
  - T defined (L2 = R2 L-3);
  - k bound in RG′ (my L3);
  - Iσ_k defined (R2 L-2; my L4 upgraded).
- Line, precision: my L4 rest (event-free, ⊕, sum ranges, «for every family of games»); R2 L-4 (ℓ_(k+1)(v)); L-5 (proof note); L-6 (the
  honest-limits tail).

## 4. Line revision L-1 (l-si a0970d36, docs/si/P-N5-SETTLE-line-L1.txt, sha1 997e39eee8d72ae94be4764bb1e3841914ffc78e; fixes sha1 87f48e2cc6737cf78cd6f9d4b00291685299fc85)
- Word-diff against 6aa094e3. Every required item of the joint gap map (§3) is applied, plus all precision items:
  - F: «for every N5 run on every game and every W-run F of it:»;
  - T: «with T its number of transitions (N5 iterations)»;
  - k: «at every S4a step k → k + 1 of F», with H_k / dist / tightness defined «for a state k of F» and «for a transition k → k + 1 of F»;
  - Iσ_k: «Iσ_k := Even's improving edges at k (SPEC S2: …)»;
  - also: run / transition / switch, values, ⊴, ⊕ (as R93 TIE), «EVENT-FREE iff it is not an EVENT», the sum and max ranges, «for every
    family of games …», «ℓ_(k+1)(v)», the ARENA-MAX SHA and its R57 reading, «as signed in this packet's review», the honest-limits tail,
    FLIP-EV DEAD, and the premises R15 (a), (d), R86 (a).
  Nothing else changed. The content equals the packet's §3, §5-§7.
- Strict symbol test, second pass. One REQUIRED item remains; it was already present in 6aa094e3:
  - SETTLE-L5 (REQUIRED; scope of τ in U). The line defines «U := Odd's valuation of τ on G^d (RESULTS R86)». Here τ is the W-run's fixed
    τ (bound by «τ and C … fixed on F»). T-XCH, however, is a whole-run statement: «XE (XO) the most changes of one vertex's Ξ (U) over the
    whole run». Over the whole run τ changes, so U must be read at each state with τ_k. As written, «changes of U over the whole run» is
    the change count of a fixed function, which is 0. The letter U also collides with R143's upward heads U_k in the same line.
    Exact fix: replace «U := Odd's valuation of τ on G^d (RESULTS R86)» by «Ξ^d_k := Odd's valuation of τ_k on G^d at state k (RESULTS R86's
    U)», and in T-XCH write «XE (XO) the most changes of one vertex's Ξ_k (Ξ^d_k) over the whole run».
- Precision (optional): «T is polynomial iff XE and XO are» → «for every family of games, T is polynomial over all runs iff XE and XO are»,
  as HEAD-RED now says.
- Verdict on L-1: REQUIRED CHANGE, SETTLE-L5 (Opus 5.5, D15). Everything else MATCHES.

## 5. Line revision L-2 (l-si 86becaa0, docs/si/P-N5-SETTLE-line-L2.txt, sha1 1fcb33c5d96a20eb70abe06c29154ef343b33ae0; fixes sha1 42d9a381f91f106a8e3bc15e589fef0a05e64186)
- Word-diff against L-1 (997e39ee). The changed tokens:
  - «U := Odd's valuation of τ on G^d (RESULTS R86)» → «Ξ^d_k := Odd's valuation of τ_k on G^d at state k (RESULTS R86's U)» (SETTLE-L5);
  - T-XCH «… one vertex's Ξ_k (Ξ^d_k) over the whole run» (SETTLE-L5);
  - «and, for every family of games, T is polynomial over all runs iff …» (optional item);
  - the source note «fixes … entries 1-2».
  Nothing else changed.
- Strict symbol test on the new tokens: τ_k is bound by «a run is the sequence of states (σ_k, τ_k)». k is bound by «at state k». The name
  clash with U_k is gone. No free symbol.
- Verdict on L-2: MATCHES (Opus 5.5, D15).

## 6. Line revision L-3 (l-si a79d33db, docs/si/P-N5-SETTLE-line-L3.txt, sha1 ae695c9eeaf9d40bdba2ed8574c238a107c68d52), preliminary to L-4 (successor 21, 23:12Z by date -u)
- Word-diff against L-2 (1fcb33c5). There are exactly two insertions and nothing else, as fixes entry 3 states:
  - «H_t);» → «H_t, H_t := S4a's arena at t (Even keeps σ_t ∪ Iσ_t, Odd follows τ_t));» (D-2; R93's title wording);
  - «fixed on F;» → «fixed on F and |F| its number of transitions;» (D-1).
- Strict symbol test on the new tokens:
  - |F| is bound.
  - t is now bound by «at t», and σ_t, Iσ_t, τ_t are the line's state-indexed symbols.
  - One REMAINING free symbol, in the same gloss: «for S4a, σ_new is the pointwise optimum …». σ_new is not a line symbol.
    REFEREE-2 24 raised exactly this on the SRC line (R2-N5-SRC §6, SRC-L2), and L-RED applied the fix in SRC L-2 (l-red 77a6d979).
- SETTLE-L6 (REQUIRED, for L-4). Replace «for S4a, σ_new is the pointwise optimum of the one-player arena H_t, H_t := S4a's arena at t
  (Even keeps σ_t ∪ Iσ_t, Odd follows τ_t)» with either of these:
  - «for S4a at a transition t → t + 1, σ_(t+1) is the pointwise optimum of the one-player arena H_t, H_t := … (as is)»;
  - SRC L-2's form, «for S4a at a transition k → k + 1, σ_(k+1) is the pointwise optimum of the one-player arena H_k», with H_k as
    defined later in the line.
  Both referees signed L-2 without this. It is a joint miss of the same kind as D-1 and D-2.
- Precision (optional):
  - «σ_t ∪ Iσ_t» is R93's wording for «{σ_t(v)} ∪ Iσ_t(v)». The line's own H_k definition uses the pointwise form.
  - The source note should read «entries 1-3» (1-4 in L-4).
- The ONE-STEP citation is not in L-3: it is due in L-4. G-SRC-1 sits in [SET] §5 Cases 2 and 2b (R-N5-SRC §3; R-N5-SETTLE Addendum 1).
  - What I will check in L-4: the RUN-SETTLE proof note gains «Case 2 and Case 2b by Lemma ONE-STEP (REFEREE-2 R2-N5-SRC.md §3.2, e8c1b62d;
    signed by REFEREE, R-N5-SETTLE.md Addendum 1, 8951ef7c; referee-originated)».
  - L-2 already defines ⊕, so ONE-STEP may also be stated in the line.
- Verdict on L-3: MATCHES D-1 and D-2. REQUIRED SETTLE-L6 (σ_new) and the ONE-STEP citation, both for L-4. (Opus 5.5, D15)

## 7. Line revision L-4 (l-si b04a1bbb, docs/si/P-N5-SETTLE-line-L4.txt, sha1 6ed61d848613df4b501b785e9418c3e2c1e8fc43; fixes sha1 5c1088d7…, entries 3-4) (successor 21, 23:40Z by date -u)
- Word-diff against L-2 (1fcb33c5, MATCHES by both referees, §5). The changed tokens:
  - «H_t);» → «H_t, H_t := S4a's arena at t (Even keeps σ_t ∪ Iσ_t, Odd follows τ_t));» (D-2);
  - «fixed on F;» → «fixed on F and |F| its number of transitions;» (D-1);
  - the RUN-SETTLE proof note «… read at one S4a evaluation with W_(k+1))» → «… with W_(k+1); Cases 2, 2b via Lemma ONE-STEP (REFEREE-2
    R2-N5-SRC §3.2, claude/referee-2 e8c1b62d; signed by REFEREE R-N5-SETTLE Addendum 1, claude/referee 8951ef7c))» (entry 4);
  - the source note changes «entries 1-2» → «entries 1-4».
  Nothing else changed. This equals the Lead's description and fixes entries 3-4.
- Strict symbol test on the new tokens:
  - |F|, H_t, σ_t, Iσ_t and τ_t are bound (§6).
  - «Cases 2, 2b» are RUN-SETTLE's cases (this packet's §5).
  - ONE-STEP is pinned by SHA and section; e8c1b62d and 8951ef7c are on origin.
- REQUIRED changes that remain:
  - SETTLE-L6 (§6, sent to the Lead 23:25Z after L-4 was frozen): «σ_new» is still free in the R57 gloss («for S4a, σ_new is the
    pointwise optimum of the one-player arena H_t, …»). SRC L-2 / L-3 already have the fix. Fix: «for S4a at a transition t → t + 1,
    σ_(t+1) is the pointwise optimum of the one-player arena H_t, H_t := … (as is)».
  - SETTLE-L7 (L41): ONE-STEP is a referee-originated proof that the line now relies on for RUN-SETTLE, so L41 requires the scope tail to
    say so. SRC L-3 has «; Lemma ONE-STEP is referee-originated»; L-4's tail does not. Fix: add the same clause to the scope tail, e.g.
    after «XCN-POLY» → «…, XCN-POLY; Lemma ONE-STEP (Cases 2, 2b) is referee-originated)».
  - Optional, in the same edit: name G-SRC-1 in the citation, as SRC L-3 does («which closes gap G-SRC-1 (REFEREE R-N5-SRC §3, claude/referee
    81f6b89c)»). That lists the gap the citation closes.
- Verdict on L-4: does NOT yet match. REQUIRED SETTLE-L6 and SETTLE-L7; everything else MATCHES (Opus 5.5, D15). Both fixes are insertions
  of one clause each; I word-diff L-5.

## DONE / FINDINGS / NEEDS
- DONE: this §C. Gate runs in docs/referee/scratch/settle_logs/pin_gate_K64_n581.txt (.start) and in this file (best-reward start, 67).
- FINDINGS:
  1. SETTLE: both referees SIGN every item; the joint gap map for the packet is empty.
  2. Required line fixes, union of both reports: F, T, k, Iσ_k.
  3. Longest block reconciled: 67 (gate, best-reward start) on all three engines. The packet's «44» is a ratio mislabel, and REFEREE-2's «+ start» label is a slip.
- NEEDS: Lead: SETTLE line L-2 with SETTLE-L5 (U scope and name); I word-diff it.
