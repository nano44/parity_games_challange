# Handover check: L-STRUCT (successor, Opus 5.5 per D15; written 2026-10-22 07:09Z by date -u)
Every answer is measured from the repository at the time of writing (commands named), not recalled. Predecessor:
L-STRUCT session_01VH4fd2Fq8XeXtyUfkwLJV1 (Fable 5.1), parked 2026-10-14 ~22:00Z, handover notebook at 729c965.

## 2026-10-22 07:09Z

### 1. Branch, head, distance to trunk
- Branch `claude/l-struct`. After `git fetch origin`: local HEAD = origin/claude/l-struct = 729c965 (not stale).
  Trunk origin/claude/vibrant-johnson-nxvvxo = 0f33c779; merge-base 42e7e84a;
  `git rev-list --left-right --count HEAD...trunk` -> 37 ahead, 2758 behind.
- Step 0: `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` -> 99020dbb. Two add/add conflicts, both lane files:
  docs/struct/L4-proof.md and docs/struct/S3-statement.md. Trunk's copies are byte-identical to l-struct 50dc28b
  (`git diff 50dc28b2:<f> trunk:<f>` empty; trunk commit 0f54b151 "S2/S3 definitions copied from l-struct 50dc28b"),
  and the lane's versions are strictly newer, so both were resolved to the lane's version (`git checkout --ours`).
  S1-statement.md and S2-lower-bound-statement.md on trunk equal the lane's (no diff). Now 38 ahead, 0 behind;
  39 ahead after this file's commit.

### 2. Open work and the next step of each
Nothing is in flight: the lane was parked with all work pushed; no detached runs belong to it.
- T3 (docs/struct/S3-statement.md; w^V(n,d) = s^V(n,d) for d <= n+1): PARKED data conjecture. Data: equality on every
  computed cell with d <= n+1, last (4,5) V = 10 = 10. Proof routes "rewire to strong" (D-C1, D-C2) and "hidden universal
  tree" (D-HB2) are dead (notebook Dead ends). Next step: the n = 5 computation in the plan below; an untried proof idea
  (notebook queue 2: compare minimal weak and minimal strong separators of one cell state by state) waits behind it.
- n = 5 diagonal cells (5,5) V, (5,6) V: lower bounds only, all from L-COMP (experiments/sat-hard/results.md lines 47-57,
  LRAT-verified): w^V(5,5) >= 10, s^V(5,5) >= 10 (>= 11 by CEGAR, proof pending, CNF lost), s^V(5,6) >= 10. No upper
  bound at n = 5 exists. Next step: the plan below.
- Stale record found in my own files (fix in the first commit after "go"): results/automata/weak_V_n4_d6_k9.json is a
  committed run with k_start 9 and value 10 (3107 s), i.e. k = 9 refuted and a 10-state weak (4,6) V-separator found;
  its automaton re-verified now against the maximal families (464 even, 708 odd graphs: 0 violations, 10 s). So
  w^V(4,6) = 10 = s^V(4,6), but results/table.md ("- / 10"), README.md ("a 9-state search is open") and
  S2-lower-bound-statement.md line 62 ("open from k = 10") still say open. make_table.py misses it because of the
  `_k9` file name. The k = 9 UNSAT rests on that run (not re-run today).
- Notebook queue item 3 ("second referee for L4") is stale: GAPS G1 is closed with two signatures (9bf5301, d76c9e1),
  RESULTS R1. Fix in the notebook after "go".

### 3. docs/GAPS.md rows I own
- G1 (major, L-STRUCT, **closed** 2026-10-15): L4, s^V(n,n) >= n^Omega(lg n); two referee signatures 9bf5301, d76c9e1;
  remaining gap G-L4-1 (CDFJLP Thm 5.1 used as a black box) recorded in RESULTS R1. (`grep -n "L-STRUCT" docs/GAPS.md`.)
- No open row. T3 is a conjecture in S3, not a GAPS row.

### 4. The three owner rulings that most constrain me (verbatim), with their DECISIONS-INDEX status
1. D15 (docs/DECISIONS.md#d15; index row D15 **active**):
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
   Lead reading L37 (active): main effort (c); I decide the next computation myself and report it as information.
2. D14 (docs/DECISIONS.md#d14; index row D14 **active**):
   > D
   > You know it can also test prveiously not tested approaches, it can come up with it own as well
   Lead reading L35 (2) (index row L35 active): "Option B (weak separators) is queued for after the Fable reset." This
   is why the lane is woken.
3. D1 (docs/decisions/D001-launch-brief.md; index row D1 **active**):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   A small weak separator is an algorithm (CDFJLP Prop. 3.2); a gap at n = 5 is DATA about a model, never an
   algorithm claim. Lead reading L7 (under D1's M3 list) sets what counts: T3 proved and double-refereed, with L4.

### 5. One trap that bit this lane before, and the check that prevents it
- Trap: `pkill -f` / `pgrep -f` with a pattern that also occurs in my own command line killed my shell and two
  running SAT jobs (notebook "Things only I know"). Check: every long run is started detached with its PID written to
  a file in out/ (`echo $! > out/<cell>.pid`) and stopped only by `kill $(cat out/<cell>.pid)`; no -f patterns.
- Second trap, relevant to the plan: the BFS symmetry breaking forces all k states reachable, so "UNSAT at k" alone
  says nothing about smaller k. Check: every lower bound is a full ladder from a proved lower bound (monotonicity in
  n and d), never one query at k = s - 1.

## Box plan: Option B, the most informative next computation (for the Lead to confirm at "go")
Question: can deterministic weak separators beat L4 (s^V(n,n) >= n^Omega(lg n))? T3 (w = s for d <= n+1) would say no.

**Decision: hunt for a gap at n = 5, (5,6) V first, then (5,5) V, upper side (SAT) first.** Not the growth of w along
the diagonal.

Reason.
1. No finite table answers the asymptotic question. w^V(n,n) for n <= 4 is 1, 2, 5, 7 (equal to s); one more point
   (n = 5) cannot separate n^Omega(lg n) from a polynomial, so "growth of w" is uninformative for the question as posed.
2. What a finite computation CAN do is refute T3: one cell with d <= n+1 and w < s kills the only proposed route to
   "no" (T3 + L4) and hands the lane a witness to generalise into a family (the T3-pos route, the only route to "yes").
   Equality at n = 5 only adds weak evidence. So the value is concentrated on the gap outcome.
3. n = 5 is the first place a gap can appear: every cell with n <= 4 and d <= n+1 is equal. Gaps so far appear in
   pairs (d = 2h-1, 2h) and only with d large relative to n: (2,5), (2,6), (3,5), (3,6); none at (4,5) or (4,6)
   (w^V(4,6) = 10 = s^V(4,6), item 2). (5,6) has the largest d inside the T3 range (d = n+1), so it is the likeliest
   gap cell; (5,5) is cheaper and is run alongside.
4. Cost is asymmetric. A gap needs a weak separator with k states (a SAT answer, usually fast) plus "strong UNSAT at k"
   (the strong encoding is ~2x cheaper than weak: (4,5) V 1496 s vs 3319 s). Equality needs "weak UNSAT at s-1", the
   most expensive query (~20x per state; L-COMP: 1-2 h per k per core already at k = 9-10 for n = 5). So run the
   cheap side first and decide the expensive side only on the numbers.

Steps (time box ~12 h wall, 4 cores; kill criteria in brackets).
- P0 calibration (<= 1 h): n = 5 V maximal families for d = 5, 6 (sizes, generation time); reproduce L-COMP's LRAT-backed
  lower bounds w^V(5,5) >= 10 and s^V(5,6) >= 10 with my encoder (independent pipelines must agree; disagreement stops
  the box and goes to the Lead); time k = 10 weak and strong to extrapolate. [If one k = 10 query exceeds 4 h, the
  equality side is declared out of reach and only P1-P2 run.]
- P1 upper side: smallest weak and smallest strong separators found by SAT for (5,6) V and (5,5) V, searching k downward
  from a constructed upper bound (lifting the n = 4 witnesses; s^E via CFGO trees bounds s^V from above), every SAT
  answer re-verified by wsep/automata.py on the full families. Output U_w, U_s per cell.
- P2 gap certificate: if U_w < U_s at a cell, prove strong UNSAT at k = U_w (full ladder from 10). Success = a gap at
  d <= n+1, T3 REFUTED: reported to the Lead at once with the automaton, LRAT proof and both pipelines' agreement;
  then lasso_analysis on the witness (T3-pos).
- P3 equality side only if P0's extrapolation fits the box: weak ladder to U_s - 1. Otherwise the cell is recorded as
  "w, s in [10, U]" with the cost obstruction, and the lane turns to the proof idea in item 2 using the n <= 4 data.
- Every number from committed scripts (a run_n5v.sh driver; logs and automata under results/), make_table.py fixed to
  read k-suffixed files; table, README, S2 and S3 updated in the same commit as each new value.
