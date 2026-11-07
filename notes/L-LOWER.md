# L-LOWER notebook

## Successor 7 HANDOVER (2026-11-07 ~20:1xZ, context ~350k; to PARK after this push unless the Lead asks for more)
### DONE (claude/l-lower)
- 9113b5cc handover check (score 5). 4f25ae6f C134 duty: fixes entry 2 + docs/lower/P-TOWER-FUEL-line-L3.txt (7328e673…, 4,908 B =
  C134 §5 target) by l5/mkL3_tf.py / mkfix2_tf.py; p_tower_check.py pins L-3 + SL41 119 j-windows. Referee byte tests: pending (Lead).
- 8cc6ebc6 BOX L7 round 1, e66baa63 round 2, this commit round 2b (docs/lower/L7-design.md; experiments/lower/l7/, l7check.py in check.sh):
  RC-PLATEAU survives (4 frozen RC-free genomes ≤ 190); PROVED (lane) WINDOW-CAP, PULSE-TRIGGER, DECOUPLED, GUARD, GREEDY-COMPLETE;
  ranksolve.py exact (SL41 6,023 conditions, 0.2 s); DATA COUPLING-UP, one-read XOR, SL41 not RC-free by q5 re-points; sequential
  schedule DEAD without helpers at h = 2 (exhaustive, 5,941 wirings); KILL_M2D_d6 breaks the cycle with a cascade-fired helper (§7).
- BOX L7 success NOT met (no 7-capped genome). CONJECTURE CONTEXT-COUPLING stated (L7 §8), not a packet.
### IN FLIGHT / NEEDS (successor 8)
- Item (a) of Lead 19:20Z: L6G_TEST1_d28.txt (sha1 86cf1903…) was NOT on origin/claude/l-comp at 19:33Z (head 07203ac2a; its
  D_l6g_best.txt = SL41 field for field, npaths 1). When it lands: freeze a copy in l7/rec/, run l6/struct48.py, l7/runstats.py, l6/win.py,
  tight.py, readpath.py, l7/fired.py; diff vs SL41; check whether its run equals SL41's (rcfree says SL41's trajectory is not RC-free by q5
  re-points, so it must differ elsewhere).
- Design next step: add helper pairs to sched.py (key-fired moves in parallel with the lower move, as KILL_M2D_d6 does), smallest
  case h = 2 at d = 3 or 4; decide wirings exactly with ranksolve (exh2.py style, or wsearch.py with the guard args).
- ONE-READ XOR proof attempt (L7 §8): for fixed i exactly one chain reaches b (else Δ is j-independent); the other chain can merge
  with it only after b; case split on the max element over Q_i, Z_i, (b, j), R_j not closed.
### Things only I know (successor 7)
- Push verify takes ~20 min; wait for `! pgrep -f "bash scripts/push.sh"` AND the «exit» line in the output before committing.
- Never start background python with `&` (I did once, killed it at once): use tracked run_in_background tasks.
- fev binary: gcc -O2 -o fev experiments/lower/l5/fev.c -lm (scratchpad, lost on restart). L-COMP files: git show <sha>:path.

## Successor 7 (Opus 5.5) — GO from Lead 18:45Z 2026-11-07
### Resume point
- Handover check 9113b5cc (score 5). DUTY C134 (Lead 18:28Z): fixes entry 2 + docs/lower/P-TOWER-FUEL-line-L3.txt (sha1 7328e673…,
  4,908 B, = C134 §5 target) by experiments/lower/l5/mkL3_tf.py / mkfix2_tf.py from a byte copy of docs/checker/C134.md (claude/checker
  23871f48: `git show origin/claude/checker:docs/checker/C134.md > C134.md`); p_tower_check.py pins L-3, asserts SL41 119 j-windows
  (3, 7, 15, 31, 63). Next: both referees byte-test L-3; then RC-PLATEAU read (L-COMP 11 lanes D_l6*) and BOX L7.
- 4f25ae6f pushed (C134 duty; reported 19:07Z). BOX L7 round 1 (docs/lower/L7-design.md, experiments/lower/l7/): RC-PLATEAU survives
  L-COMP af466f89 (4 frozen RC-free genomes, F(6) 117/160/134/190, sim6 + fev agree; copies l7/rec/LCOMP_*). PROVED (lane):
  WINDOW-CAP, PULSE-TRIGGER, DECOUPLED, GUARD, GREEDY-COMPLETE (ranks = decision-list consistency; ranksolve.py exact).
  DATA: SL41 trajectory not RC-free by re-pointing 10/55 (104 + 2,704 genomes, 0); COUPLING-UP (ideal pair 6 on SL41 wiring changes
  34 helper trajectories, every mover 0-13 infeasible alone); one-read XOR 0 of 84,000 wirings, with context 864 of 180,000.
- Next: sequential schedule for pairs 0-7 (pair 7 = o(6)-keyed helpers telling q5 «pair 6 done»), reading sets from L7 §5 tables,
  enumerate consistent wirings, decide each with ranksolve. Watch D_l6g on claude/l-comp.
- Round 2 (Lead 19:35Z GO for the sequential design): sched.py capped targets h = 2..7; exhaustive d = 2: 0 of 5,941 wirings realize
  h = 2 (α 1 and 0) -> DEAD without helpers (Ξ-cycle f1 -> pair 0 -> q1 -> f1); L7 §7-§8 (CONJECTURE CONTEXT-COUPLING, not a packet).
  Next: add helper pairs to the schedule (key-fired moves breaking each cycle), smallest case h = 2 with d = 3, exhaustive if possible.
  Item (a) L6G_TEST1 (86cf1903) still not on origin/claude/l-comp at 19:33Z.
### Things only I know (successor 7)
- ranksolve on SL41 runs in 0.2 s; rcfree (b) 2,704 solves ~170 s. clamp.ideal6 takes o(5) from the original run (pairs 0-5 unchanged).
- The design sketch (h, h2 = pair 7 reading f5, firing on o(6); q5 decision list) is now in L7 §6;
  the per-state tables behind it are hand-derived (not in a tool yet).

## Successor 6 HANDOVER (2026-11-07 ~17:3xZ, context ~500k; PARKED after this push)
### DONE (claude/l-lower; product docs/lower/L6-supplier.md; tools/data experiments/lower/l6/)
- BOX L6 (constructive test of CONJECTURE L5-TYPE on SL41): success NOT met (no 6-capped genome with F(6) > 222). Exact reason (L6 §7):
  MERGE at 22 under parent (9,1) (DATA); TOP-CLOCK (PROVED, lane: TOP-ADD needs ≥ 5 added levels to move 29 times); SAME-STEP (length-2
  windows); RETURN-CHAIN 10:0 → 55 → 12 feeds capped pair 5; single key-gated supplier RANK-LOCKED (PROVED with instance values).
  Also PROVED (lane): TAP, TRANSPARENT-LEVEL. Gadget plateau 95/127 good windows (rec/GAD95_P8_d29.txt, sha1 d0de3499…, xcheck'd vs L-NEW
  box150: 0/0). D18 analogy: synchronous circuits (register / combinational / setup time / carry-lookahead) — lookahead fails by TAP.
- §5b: top capped levels are fuelled by «q reads f»; §5c: READ-NEST DEAD on SL41 (readnest.py); §5d: the 48/127 plateau has the same
  16/16/16 profile in SL41, G7_best, L-SI snapshot and w1 (2 of 4 not crossed); all four have q₅ graph-upstream of pair 6.
- CONJECTURE RC-PLATEAU (role form, L6 §5d): levels 0-5 capped and a Ξ-path from q₅ (pair-5 member moving second) into pair 6 ⇒
  F(6) ≤ 222. General form (any j) DEAD (rcgen.py: capped levels j = 2..5 with such paths, e.g. snapshot j = 5). j = 6 form: DATA only.
- Guard for L-COMP 11 (routed 17:27Z, replaces its D_d28b lane): experiments/lower/l6/guard_l6.py (sha1 18e85589…, needs sim6.py):
  guard(D, mode) → (ok, info), modes 'noreturn' (role-based: q₅ from the run, npaths(D, q₅, {12, 13}) == 0 and levels 0-5 capped),
  'nomerge91', 'pulse3', 'either'; roles(D, S, O, j); npaths(D, src, T); score(D) = (min(caps, 6), −npaths(q₅, pair 6), F(6)).
  CLI: python3 experiments/lower/l6/guard_l6.py GENOME.txt noreturn. Seed SL41 (npaths 1; needs ≥ 2 edits). Read L-COMP's result:
  F(6) > 222 under 'noreturn' kills RC-PLATEAU.
- DUTY P-TOWER-FUEL fix round 1: fixes entry 1 + L-2 (d866ca50…, 4,586 B) at 740f6c79; BOTH referees MATCH L-2 (REFEREE §C d39fc93a,
  REFEREE-2 Add. 1 fa010874). Lead drafts R120 for CHECKER C134.
### IN FLIGHT / NEEDS (successor 7)
- DUTY: CHECKER C134's L-3 items for P-TOWER-FUEL (the Lead relays). Write fixes entry 2 + docs/lower/P-TOWER-FUEL-line-L3.txt by
  script in the style of experiments/lower/l5/mkL2_tf.py / mkfix_tf.py (copy every exact string from byte copies of the report; each
  old once in L-2, each new once in L-3), extend p_tower_check.py to pin L-3 and assert any new unit; never edit the packet, L-1, L-2.
- L-COMP 11's 'noreturn' climb result: dissect any F(6) > 222 genome with win.py / tight.py / readpath.py / struct48.py.
- Open ideas (none started): a lower tower where the (9,1) chain does not merge into 22, or PULSE_5 ≥ 3 under (9,1).
### Things only I know (successor 6)
- No detached runs left (gad/gad2 runs finished; binaries in the scratchpad are gone on restart: gcc -O2 -o gad2 experiments/lower/l6/gad2.c -lm).
- Push takes ~20 min of verify here; wait on `! pgrep -f "bash scripts/push.sh"` AND the «exit» line before any commit (did so every time).
- xcheck recipe: git archive origin/claude/l-new experiments/new/box150 experiments/new/box139 experiments/new/box187 | tar -x -C DIR
  (run from the repo ROOT, else the pathspec fails); l3/txt2json.py G.txt PREFIX; LNEW=DIR python3 -I l3/xcheck.py PREFIX_dNN.json.
- L-SI genomes used: claude/l-si 38f08152 experiments/si/box80/out/climb_s2_snapshot.txt (0d676179…), climb_w1_P0.json (622f68e5…).

## Successor 6 (Opus 5.5) — BOX L6: build the fuel supplier for SL41's level 6 (GO from Lead 14:08Z, 2026-11-07)
### Resume point
- Handover check 2ce74ff9 (score 5). Product: docs/lower/L6-supplier.md; tools/data experiments/lower/l6/ (sim6.py = Python big-int
  simulator agreeing with fev; win.py windows/deciders; ins.py level insertion; dropscan.py; gad.c / gad2.c gadget annealers).
- Result so far: success NOT met (F(6) never > 222 with 6 capped). Exact reason (L6 §7): MERGE at 22 (11:1 → 9:1 → 54:0 → 22 under
  parent (9,1)); TOP-CLOCK (PROVED: TOP-ADD on SL41 needs ≥ 5 added levels to move 29 times); SAME-STEP (length-2 windows); couplings:
  12 feeds capped pair 5 (10:0 → 55 → 12) and a single key-gated supplier is RANK-LOCKED (22-side needs a 2^87 drop at 240, none
  exists; 11-side needs an idle β of rank ≥ 88, freezing 63 of 79 good windows). Gadget plateau 95 good 6-windows (rec/GAD95_P8_d29.txt).
- D18 analogy: synchronous circuits (Ξ = register, key cascade = combinational ripple, length-2 window = setup-time; carry-lookahead
  via the Gray-code cycle of pair 4's b-step types) — lookahead fails because a path reads the whole downstream sum (TAP).
- DUTY P-TOWER-FUEL fix round 1 DONE 740f6c79 (fixes 0902efb9…, L-2 d866ca50… 4,586 B; mkL2_tf.py / mkfix_tf.py; check pins L-2).
  Waiting for both referees' byte tests; answer further items with fixes entry 2 + L-3 by script, never edit packet / L-1 / L-2.
- 16:44Z Lead ruling: guard 'noreturn' (role-based) shipped b8729f80 for L-COMP 11; no 6-capped seed meets it (SL41 npaths 1). The 48/127
  plateau: same 16/16/16 profile in SL41, G7_best, L-SI snapshot and w1 (2 not crossed). RC-PLATEAU general form DEAD (rcgen.py).
- 15:53Z Lead: (a) READ-NEST by hand -> DEAD on SL41 (readnest.py: 10's path needs 12; 12 reads 13 kills all caps at step 1);
  (b) predicate guard_l6.py + seed SL41 sent for L-COMP; GAD95 xcheck'd vs box150 (0/0).
- Milestone report sent to Lead 15:50Z (SHAs 2ce74ff9, fa9104fa, e362f15b, 3329b094, 740f6c79). Waiting for routing (READ-NEST
  test SL41′ or a non-merging tower).
- Next ideas (not started): a lower tower where the (9,1) chain does not merge into 22, or PULSE_5 ≥ 3 under (9,1) (gives the fuel a
  register); multi-mover gadgets outside gad2's space.
### Things only I know (box L6)
- gad/gad2 binaries and runs live in the scratchpad (lost on restart); rebuild: gcc -O2 -o gad2 experiments/lower/l6/gad2.c -lm.
  gad's «good» counter differs from win.py by one on SL41 (78 vs 79: first-window handling); on GAD95 both give 95.
- With insertion at P, old movers ≥ 2P shift by +2; at P = 6 pass J = 7 (old pair 6) and FT = 254 to gad2.

## Successor 5 HANDOVER (2026-11-07 ~12:4xZ, context ~420k; PARKED after this push)
### DONE (claude/l-lower; docs/lower/L5-rule.md is the box's product; tools/data experiments/lower/l5/)
- §1-§2: H5→H6 dissection (revert.py, greedyback.py: ~half drift, ~70 Ξ-targets forced at every level); fuel source = f(own b-step
  type) (fuelsrc.py; ruler/Hanoi DEAD). §4: uniform templates (utmpl.c) give ≤ 1 doubling level. §5: GAP-NEST (PROVED, lane).
- §6: seventh-level obstruction. G7_best: 30 level-5 PULSE/GAP violations (corrected from 31), all type (9,1) + first window. SL41_d28
  (rec/, sha1 c1b46c31…, xcheck'd vs L-NEW box150 Gen ae8e185d: SIM-MISMATCH 0, movescheck 0): all room conditions met, F(6) 222; fuel
  gap: crossed pair 6 decided by (87, 9, 1) in all 48 failing windows (domin.py). DOMINANCE-FREEZE, CROSS-ECONOMY (PROVED, lane).
  Local repair DEAD up to: 166 single dominator edits, 2,970 single closure re-targets, 20k random 2-edit, 144,011 two-edit (supplier 19).
- §7: CONJECTURE L5-TYPE (O(h) suppliers per extension); evidence fuelctx.out (capped-level fuel = own type only).
### PACKET P-TOWER-FUEL FROZEN at 7f7ff6f5 (Lead ruling 12:36Z (b)): docs/lower/P-TOWER-FUEL.md + line docs/lower/P-TOWER-FUEL-line-L1.txt
  (sha1 408470ad…) + check experiments/lower/l5/p_tower_check.py (in check.sh; pins G7_best b995fff2…, SL41 c1b46c31…, the line).
  Premises landed only (R104 def, R105 ENC, R110 def, R113 ALIGN); MOVE, DOUBLE-EQ, PULSE-NEST re-proved inside. Referee items go into
  a fixes file docs/lower/P-TOWER-FUEL-fixes.md + new line files L-2…; NEVER edit the frozen packet or line L-1.
### ROUTED (Lead): L-COMP 11 (session_01V5yGRYPZqSkyP1GtiC8bMh) lane D: from SL41, GUARD 0-5, F(6), 2-3 simultaneous edits outside
  pairs 0-5, one restart biased to a changing β > 87 on 22's / 11's chain. Read its result before redoing anything.
### NEXT (successor): (1) if L-COMP finds F(6) > 222 from SL41: dissect with domin.py / fuel6.py which supplier beat (87, 9, 1), and test
  the same move at H5 → H6 (Lead: the L5-TYPE test). (2) Packet draft: GAP-NEST + PULSE-NEST re-proved + DOMINANCE-FREEZE + CROSS-ECONOMY,
  premises landed only (R104, R105 ENC, R110, R113, R116; not R119). (3) Hand design: a supplier needs a β above rank 87 on 22's or 11's
  chain that changes once per pulse under parent (9,1); 19 (β 95, 23 moves while 9 parked) is the candidate; 2 edits are not enough.
### Things only I know: see «Things only I know (box L5)» below (fev batches, revert.py importable, SLACK score, xcheck recipe, push slip).

## Successor 5 (Opus 5.5) — BOX L5: the inductive rule G_h → G_(h+1), or its obstruction (GO from Lead 09:42Z, 2026-11-07)
### Resume point
- Handover check 9ef2e415 (score 4.5). Corrected: DUTY P-M2D-DEAD is CLOSED (both referees MATCHED L-3: REFEREE §C add. 1 70ec6882,
  REFEREE-2 Add. 2 59bfa452; CHECKER C131 PASSED 2c6a2c1b; DE37 MOVES-2D DEAD on 𝓛^R_d LANDED in trunk 172af6ad; Lead 09:42Z, relayed,
  not opened by me). No duty open.
- Box L5 write-up: docs/lower/L5-rule.md; code/data: experiments/lower/l5/. Brute climbing is L-COMP 10's (D_d32 from G7_best_d28 + 4
  TOP-ADD); ask the Lead to route any seed/constraint.
- Pre-go DATA (lpaudit, stored start): per-window fuel sources alternate by window parity (two feeders per level); exceptions H6 level 3
  (period 4) and H5 level 3 (two irregular windows). Not a ruler/Hanoi function (ruler test DEAD). Lead: look at the period-4 exception.
- 10:3xZ state (docs/lower/L5-rule.md §1-§7): fuel source = function of the b-step type (member × direction) on H6/DBL4/RECF4/G7;
  greedy walk back H6 → H5: ~half drift, ~70 Ξ-targets forced at every level; GAP-NEST (PROVED, lane); G7_best's only 7-level pulse/gap
  deficit = level 5, type (9, 1) (trigger 15 key-gated by the first move of pair 5); 94k random single splices: no gain; uniform
  templates (P ≤ 3): one doubling level only. CONJECTURE L5-TYPE (O(h) delay movers per extension). Template runs out/r_p* may still run.
- 11:1xZ state: SL41_d28 (targeted SLACK climb from G7_best; all 7-level PULSE/GAP conditions met, F(6) still 222). Obstruction = fuel:
  pair 6 is CROSS onto (22, 11) and decided by (87, 9, 1) in all 48 failing windows (domin.py); single edits (domfix) and 20k two-edit
  fuel splices (fuelsplice) fail. Lemmas (lane): GAP-NEST, DOMINANCE-FREEZE, CROSS-ECONOMY (docs/lower/L5-rule.md §5-§6).
  Capped-level fuel depends on own b-step type only (fuelctx.out). Next idea: a supplier for D = cv(22) − cv(11) of rank > 87 that
  changes once per pulse under parent (9, 1) — candidates from good-window deciders (19, 20 at ranks 91-95; 7 at 101).
### Things only I know (box L5)
- SLIP (12:0xZ): committed 5bc47311 while push.sh was verifying a92b5226 (my wait loop tested «output file non-empty», which the
  commit step had already written). push.sh pushed only the verified a92b5226; 5bc47311 went out in the next push. Check now: wait on
  `! pgrep -f "bash scripts/push.sh"` AND «exit» in the task output before any commit.
- Two-edit supplier search (retall2) at 144k genomes ran in ~10 min with fev batches of 400; the SL41 plateau is > 2 edits deep.
- xcheck against L-NEW: `git archive origin/claude/l-new experiments/new/box150 experiments/new/box139 experiments/new/box187 | tar -x
  -C $SP/lnew; LNEW=$SP/lnew python3 -I ../l3/xcheck.py f.json`.
- revert.py is importable (main guarded); greedyback/splice/domfix/fuelsplice import rd/wr/caps from it. fev = batch evaluator (one
  process, many genomes): use it for all batch searches; utmpl GENOME= mode is an independent exact-order simulator.
- mclimb.c SLACK=J:NEED score = 256·(good J-windows) + F(LV) under GUARD; validated on H6 / G7_best (L5 §6).
### Sources opened (this box)
- claude/l-si 9b51f2cb docs/si/N5-TOWER-box80.md §0-§6 (PULSE-NEST, CAP-PULSE, ZONE, INSERT-PASS, STRETCH-NEED, delay lines);
  docs/si/N5-TROPICAL-box76.md §2 (ALT-MIN, HIT), §8-§12 (TOWER-NEED, FUEL-NEED, PASS-FREEZE, RE-ENTRY); experiments/si/box80/delay80.out.
- Friedmann's binary-counter games: NOT opened; not used.
Successor 4 (Opus 5.5, D1/D14/D18/D20) started 2026-11-07 03:30Z (date -u); BOX L4 (12 h): the fifth doubling level, S(h), by an
explicit recursive design with proofs. Successor 3's sections below are kept unchanged as history.

## Successor 4 handover check (2026-11-07 03:4xZ, date -u)
1. Branch claude/l-lower, head 8938e403 (= local ref = origin = ls-remote; clone unshallowed: is-shallow false; local branch was
   behind and fast-forwarded with `merge --ff-only origin/claude/l-lower`). Versus trunk claude/vibrant-johnson-nxvvxo (ls-remote
   663c6447): 10 ahead, 106 behind (`rev-list --left-right --count`). No trunk merge (not needed for this box).
2. Open work: (a) DUTY P-M2D-DEAD L-2 (8938e403) waits for the referees' byte tests; no new item from REFEREE (head f66942c1) or
   REFEREE-2 (b0860fcd) yet. Next: answer any item with fixes entry 2 + L-3, by script; never edit the frozen packet. (b) BOX L4: an
   explicit recursive G_h whose new top level doubles (F(4) = 62 never reached; best 46), using WIRE / COPY / TOP-ADD, PASS-FREEZE and
   a re-entrant fuel path (L-SI 41 RE-ENTRY). Next: rebuild the tools in the scratchpad, dissect REC_d10_tower's fuel, design h = 5.
   Predecessor's in-flight climbs died with its container (not resumed; superseded by the explicit-design angle).
3. docs/GAPS.md rows owned by L-LOWER: none (`grep -c L-LOWER docs/GAPS.md` = 0). The box works against G-N5-TIME (L-NEW, open).
4. Rulings (verbatim, docs/DECISIONS.md; status docs/DECISIONS-INDEX.md): D18 «Focus on N5 and work toward proving it. Explore
   novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied
   together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly
   distinguish proven results from conjectures and open problems.» (active); D1 «A claimed polynomial algorithm is far more likely
   to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.»
   (active); D14 «D» / «You know it can also test prveiously not tested approaches, it can come up with it own as well» (active).
5. Trap: stale/shallow clone (the local branch ref lagged origin at start this time: `git status` said «use git pull»). Check:
   ls-remote vs `rev-parse HEAD` and `origin/claude/l-lower`, `is-shallow-repository` = false. Also: never edit a script a detached
   chain is executing (bash reads incrementally).

Successor 3 (Opus 5.5, D1/D14/D18/D20) started 2026-11-07 00:05Z (date -u); STEP 0 handover check below; BOX L3 (explicit families
for μ(d), IDEAL-ACYC model on 𝓛^R_d). The predecessor's T-L2 text (2026-10-15) is kept below unchanged as history.

## Successor 4 HANDOVER (2026-11-07 ~06:45Z, context ~420k)
### DONE (claude/l-lower; docs/lower/L4-tower.md is the box's product)
- Lane lemmas (unrefereed, premises landed only): DRV-RELAX §1, DUAL §2, DOUBLE-EQ′ §3, FROZEN-WINDOW §4 (+ NO-CROSS/NO-PARALLEL),
  LATE-PREF + FUEL-PER-WINDOW §4b. Checks: experiments/lower/l4/l4check.py (in experiments/lower/check.sh).
- CANDIDATE records (experiments/lower/l4/rec/; sim.py = box150 Gen, movescheck 0, memcheck (i)-(vi)):
  DBL4_d20_F30 (43704358…; F 0 2 6 14 30), H5_d20_F62 (2204079d…; F 2 6 14 30 62, T 136; REPRODUCED by L-SI 41),
  H6_d24_F126 (fb37fec9…; F 2 6 14 30 62 126, T 209), RECF4_d20_F60 (354b7d44…), F56, F53, F52.
- DUTY P-M2D-DEAD fix round 2: afc85c57 (entry 2, L-3 4c056511…, fixes f5b3f78a…); waiting for the referees' byte tests of L-3.
- SHAs: 5dcfa1e1 (check), 7777fc4f, 127a5f8c, 2f15c81a, afc85c57, 33eb8593, c45cf2f3, 10cac3d9, then push 9 (diffg + text genomes).
### Confirmations (Lead 07:14Z, relayed; not opened by me): H5_d20_F62 and H6_d24_F126 REPRODUCED by L-SI 41 and L-RED 53;
RECF4_d20_F60 and DBL4_d20_F30 REPRODUCED by L-RED; end to end on the real Γ3 games two N5 engines (n5v, n5b) agree: 33 / 70 / 139 /
212 iterations = L + 3, one FL run of length L(G), Oink-verified (Lead's summary; open the L-SI / L-RED / engine commits to cite).
### WARNING: rclimb.c's __int128 values overflow when ranks reach 127 (d ≥ 32; L-COMP 10). Use L-COMP's rclimb30.c (192-bit,
experiments/comp/box30/ on claude/l-comp) at d ≥ 32. No result of mine came from d ≥ 32 (the one d 32 climb, G7d32, was stopped at
07:15Z without a record). Seeds 300000-329999 are L-COMP's (box 30): keep outside.
### Seventh level status: guarded climb (`GUARD=5 LV=6 ANNEAL=0.02 $SP/rclimbG out/H6d28.txt 162 …`, rclimb.c GUARD) holds F 2 6 14
30 62 126 and reaches F(6) = 190 at d 28 (254 needed); L-COMP box 30 runs the same target (A).
  RELAUNCH (successor 5): `SP=<scratch>; gcc -O2 -o $SP/rclimbG experiments/lower/l4/rclimb.c -lm; cd experiments/lower/l4;
  python3 -I ../l3/lift.py rec/H6_d24_F126.txt 4 out/H6d28.txt; GUARD=5 LV=6 ANNEAL=0.02 OUT=out/G7_s162.txt setsid nohup
  $SP/rclimbG out/H6d28.txt 162 400000000 > out/G7_s162.log 2>&1 &` (d 28 only: ranks ≤ 111; for d ≥ 32 use L-COMP's rclimb30.c).
  Its best genome at PARK (09:0xZ) is committed as rec/G7_best_d28.txt: T 270, F 2 6 14 30 62 126 222 158 126 80 32 28 20 8 …
  (levels 1-5 exact; F(6) = 222 vs cap 254; plateau since iteration ~106M). Warm restart: use it in place of out/H6d28.txt, a new seed
  (< 300000), and re-arm a monitor on `grep "F 2 6 14 30 62 126 2[3-9][0-9]"` in the log. Tried: LV=6 alone (loses level 5), CHAIN=6
  (collapses the tower), GUARD=5 LV=6 (this run: 160 → 190 → 208 → 222), frozen levels 0-4 (FROZENBELOW=10: stalls at F(5) = 94).
  Next idea: lift to d 30 (ranks ≤ 119, still int128-safe) or move to L-COMP's rclimb30.c and lift to d 32+.

## Successor 4 PARKED (2026-11-07 09:0xZ, context ~520k): handover = the «Successor 4 HANDOVER» section above. All my background jobs stopped.
### IN FLIGHT (die with the container; logs in experiments/lower/l4/out/, gitignored)
- Seventh level: `LV=6 ANNEAL=0.02 OUT=out/L7_s131.txt $SP/rclimb128 out/H6d28.txt 131 400000000` (H6d28 = lift.py H6 + 4 levels;
  at handover F 2 6 14 30 62 94 128 …: level 5 lost). Frozen-core: `FROZENBELOW=10 LV=5 ANNEAL=0.02 $SP/rclimbF out/H5d24.txt 141 …`
  (F(5) stuck at 94).
### RECIPE (how H5 and H6 were found; restart in a fresh container)
1. `gcc -O2 -o $SP/rclimb128 experiments/lower/l4/rclimb.c -lm` (__int128 values: exact for d ≤ 32).
2. Seed: rec/H6_d24_F126.txt (or H5: `python3 -I experiments/lower/l4/j2t.py rec/H5_d20_F62.json > h5.txt`).
3. TOP-ADD 4 levels: `python3 -I experiments/lower/l3/lift.py seed.txt 4 out.txt`.
4. Climb the next level: `LV=<h> ANNEAL=0.02 OUT=o.txt $SP/rclimb128 out.txt SEED 400000000` (LV = the level whose F must double;
   H5 → H6 took ~34M proposals; CHAIN=<h> scores exact doubling of levels 1..h; ANNEAL ≥ 0.3 destroys the tower).
5. Verify: txt2json.py, l3/sim.py, `LNEW=<l-new tree> l3/xcheck.py`, fwcheck.py, lpaudit.py, l3/memcheck.py f.json 8; pin in l4check.py.
### NEXT (Lead 06:09Z / 06:14Z)
1. Third point: F(6) = 254 at d 28 (same recipe). 2. An explicit rule G_h → G_(h+1): H5→H6 raw diff is global (diffg.py); compare
   block structure (top pair reads pair below + partner; level below fed by an equal-rate block 2-3 levels up; L-SI 41 box79 wiring79).
3. Least d for five capped levels (truncated seeds d 16 / 12 got F(4) 41 / 30 so far).
### Things only I know
- rclimb ANNEAL is per score unit/256 (LV) or /200 (CHAIN, ANYRUN); ANYRUN score is degenerate (rewards trivial doublings): do not use.
- fwcheck.py random generators rarely hit FROZEN-WINDOW's hypothesis; dd_tg counts it.
- The Lead once routed «6c5a6ff» (my typo, corrected): the H5 commit is c45cf2f3.

## Successor 4 BOX L4 state (2026-11-07 ~04:3xZ)
### Resume point
- Write-up: docs/lower/L4-tower.md (§1 DRV-RELAX, §2 DUAL, §3 DOUBLE-EQ′, §4 FROZEN-WINDOW + NO-CROSS/NO-PARALLEL/four targets, §5 DATA,
  §6 obstruction reading). Code: experiments/lower/l4/ (drv.c, drvpy.py, drvpath.py, blk.py, tmpl.c, rclimb.c, j2t.py, fwcheck.py,
  l4check.py in experiments/lower/check.sh). Records: l4/rec/RECF4_d14_F52.json (1e0b0a58…), RECF4_d16_F53.json (9b08c289…).
- Binaries in the scratchpad: `gcc -O2 -o $SP/drv drv.c -lm`, `gcc -O2 -o $SP/rclimb rclimb.c -lm`, `gcc -O2 -o $SP/tmpl tmpl.c`.
- IN FLIGHT (detached, die with the container; logs in l4/out/, gitignored): F(4) climbs `LV=4 ANNEAL=0.15 OUT=out/C14b_s21.txt
  $SP/rclimb out/C14_F52.txt 21 300000000` (also s22), `… OUT=out/C16_s1.txt $SP/rclimb out/C16seed.txt 31 300000000` (C16seed =
  C14_F52 + 2 TOP-ADD levels, lift.py), C14_s1 from out/tow14.txt. rclimb uses long double: exact only for d ≤ 16 (ranks ≤ 63).
- DUTY P-M2D-DEAD: fixes entry 2 (PM-C1 + W-1′ merged) and line L-3 (docs/lower/P-M2D-DEAD-line-L3.txt, sha1 8d7dbfe5…, by
  l3/mkL3.py); pins in l3/p_m2d_check.py. Waiting for both referees' byte tests of L-3.
- Records: rec/RECF4_d20_F56.json (1167b8a6…; F 2 6 13 28 56, T 71). Climbs at d 20 use $SP/rclimb128 (__int128; CHAIN=4 / ANYRUN=1
  scores: exact-doubling rewards; ANNEAL ≤ 0.05 there, 0.3 destroyed the seed).
- Max consecutive doubling levels observed: 3 (never 4). LATE-PREF (§4b) + lpaudit.py show the window events come from above.
### Next
1. Design a tower pair with four distinct targets whose fourth target rises once per window (§6 OPEN); seed from RECF4_d16_F53.
2. FROZEN-WINDOW (b) to the referees if the Lead wants a packet (premises: landed only).
### Sources opened (this box)
- docs/RESULTS.md R105 (l. 10155: ENC, MONO), R113 (l. 12152, PAIR-DOUBLE proof l. 12220), R104 (l. 9864, definition); claude/l-si
  b97aee9a docs/si/N5-TROPICAL-box76.md §7 (DBL-EQ), §8-§11 (TOWER-NEED, ACYC-SPLIT, FUEL-NEED, PASS-FREEZE, FUEL (i)/(ii), RE-ENTRY);
  claude/l-new 73b3d1fd docs/new/P-N5-REACH.md header and §1 premises (REACH3 from S3; not used as a premise here); claude/referee
  f66942c1 / claude/referee-2 b0860fcd logs; later 008039cc §C (PM-C1) and 5c8aea53 Add. 1 (W-1′).
- claude/l-red 6e743ab1 experiments/red/r214/lower3/replay.out (7,591 B, sha1 4492ee28…): 9 distinct genomes «>2d», incl. d 6 mover 8
  moves 13 (2d 12) and d 8 mover 15 moves 21 (2d 16); box150 XSIM 0. Cited in L-3 (fixes entry 2).
### Dead ends (this box)
- Free-e relaxation as a search target: «F(4)» 63 at m 13 only via 57 e-changes (l4/out/rf4_s2.gen); F0 forbids; use EB=2.
- Recursion «add one crossed level on the targeted top pair»: killed by FROZEN-WINDOW (b) (theorem); instances REC_d10_tower (CROSS
  pair 3, F(4) 23), forced crossed pair 4 climbs (F(4) ≤ 34, out/X14_a2.txt), seedCR2 (CROSS pair 2: F(3) 20 < 22).
- One-active-mover-per-level (KM-type) fuel chain: LP ≈ 2m even with free keys (drv HALF).
### Things only I know
- drv.c hash keys are unsigned (s << 3): m ≤ 14 in OBJL mode. blk.py refuses genomes with a level-0 Ξ-target (DRV-RELAX hypothesis).
- In rclimb, ANNEAL is per score unit/256 for LV mode: 0.15 works, ≥ 1 is a random walk.

## Successor 3 handover check (2026-11-07 00:1xZ, date -u)
1. Branch claude/l-lower. At start: local ref = HEAD = origin = ls-remote = aa8995e8 (clone was shallow: `fetch --unshallow`, then
   `merge --ff-only origin/claude/l-lower`: already up to date). Merge of trunk claude/vibrant-johnson-nxvvxo (ls-remote 2ccd037b) was a
   fast-forward (the branch had no commits beyond the merge-base): HEAD = 2ccd037b, `rev-list --left-right --count HEAD...trunk` = 0 0.
   Before the merge: 0 ahead (aa8995e8 is an ancestor of trunk), 9,388 behind.
2. Open work: the predecessor's three k = 9 SAT runs (B_2(5) ≥ 10) died with its container (no processes here; their checkpoints were
   gitignored). Goal parked by the Lead (L25); not resumed. New work: BOX L3 (this brief): (a) explicit recursive family G_d with
   μ(G_d) ≥ 2d, (b) compositions beyond 2d, (c) the obstruction. Next step: own simulator (experiments/lower/l3/), cross-checked
   against L-NEW's movescheck.py on box186/187, then the d = 4/5 witnesses' structure.
3. docs/GAPS.md rows owned by L-LOWER: none (`grep -c L-LOWER docs/GAPS.md` = 0). BOX L3 works against G-N5-TIME (major, L-NEW, open).
4. Rulings (verbatim, docs/DECISIONS.md; status docs/DECISIONS-INDEX.md):
   D1 «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as
   wrong until it passes the gauntlet below.» (active); D18 «Focus on N5 and work toward proving it. Explore novel approaches,
   especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make
   reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven
   results from conjectures and open problems.» (active); D14 «D» / «You know it can also test prveiously not tested approaches, it can come up with it own as
   well» (verbatim, typos the owner's; active).
5. Trap: stale/shallow clone (the checkout looked current but was shallow; a merge on a shallow clone can misreport the base). Check:
   ls-remote vs `git rev-parse claude/l-lower` and HEAD, `rev-parse --is-shallow-repository` = false before merging. Older trap kept:
   `pkill -f PATTERN` kills one's own shell; use anchored pgrep and kill PIDs.
- Note on the brief's goal (a): «μ(G_d) ≥ 2d for every d» cannot hold at d = 3: the packet's lane DATA (L-RED R213, one solver)
   gives the Ξ-target maxima 1, 3, 4 by level at d = 3, so μ(3) = 4 < 6 (and T^R(3) = 8, R112). Reading: aim at μ(G_d) ≥ 2d for d ≥ 5
   (the first tight case) and at the growth rate.

## Successor 3 PARKED (2026-11-07 ~03:3xZ, after P-M2D-DEAD fix round 1: fixes entry 1 + line L-2; waiting for the referees' byte tests)

## Successor 3 HANDOVER (2026-11-07 ~02:2xZ, context ~450k; Lead asked to plan the handover near 550k)
### DONE (all pushed on claude/l-lower; see docs/lower/L3-families.md and docs/lower/P-M2D-DEAD.md)
- Simulator sim.py (+ inline second implementation in p_m2d_check.py), cross-checked vs box150 Gen / box139 XSIM / movescheck.
- Lane lemmas (unrefereed): TRI, TRI-MU (no upward option ⇒ level-l mover ≤ 2l moves), FEEDBACK (a)/(b), TOP-ADD, WIRE, COPY; family A
  (T = 2d, μ = 2⌊2(d−1)/3⌋+1, data to d 40, proof pending).
- MOVES-2D DEAD (CANDIDATE → reproduced by L-NEW box 188 and L-SI 41; L-RED pending): kill/KILL_M2D_d6_mu13, d8_mu21; packet
  P-M2D-DEAD FROZEN (87fcdf73) with check block p_m2d_check.py; μ records d 7-12 (kill/README.md).
- Tower: REC_d10_tower (F 2 6 14 30 = R113 caps); T records 59 (d 11), 66 / 99 (d 13), 107 (d 14), 114 (d 15); F(4) up to 46 (d 14).
### IN FLIGHT (die with this container; logs gitignored in experiments/lower/l3/out/)
- out/pNF_d15.log: annealed F(4) climb from the COPY nested-fuel seed: FINISHED at F(4) = 40, T 49 (below the 46 record).
- out/pMF_m6.log: climb from the inert MUTUAL-FEEDBACK seed (mutual.py; F(4) 9).
- Restart lines (cwd experiments/lower/l3, SP = scratchpad with binaries built by `gcc -O2 -o $SP/psearchA psearch.c -lm`):
  `LV=4 SCORE=1 ANNEAL=16 $SP/psearchA out/TOW10cp5.txt 131 80000000 14 10000000` (seed copies in experiments/lower/l3/seeds/:
  TOW10cp5.txt = REC_d10_tower + copy of levels 0-4 on top, ranks adjacent; mf_m6.txt = mutual.py seed; b_pT_d15.txt = the T 114 genome); `SCORE=2 $SP/psearchA
  <txt> seed iters LM 8000000` for T climbs (lift.py adds levels). psearch env: SCORE 0 μ / 1 max F (LV=l: F(l)) / 2 T; LMIN, ANNEAL.
### NEXT (Lead's top goal: S(h), the least d with h consecutive doubling levels)
1. Fuel the 5th tower level (F(4) = 62) from a block outside the tower's Ξ-down-closure (L-SI ACYC-SPLIT/FUEL-NEED). Start C ACTIVE.
2. If a height-5 tower appears, try to make the nesting recursive and prove T ≥ c·2^(αd) (lane), data to d ≈ 16.
3. Otherwise extract the obstruction (what blocks F(4) > 46) for L-SI.
4. Family A-RUN proof (low priority).
### NEEDS
- Lead: route P-M2D-DEAD to the referees (done per 01:43Z); L-RED's replay result.

### Resume point
- Code: experiments/lower/l3/ — sim.py (own simulator, from the R104 definition), trace.py, xcheck.py (vs L-NEW box150 Gen +
  movescheck counters; needs LNEW = an l-new tree: `git archive origin/claude/l-new experiments/new | tar x -C DIR`), tricheck.py
  (TRI / TRI-MU / FEEDBACK checks), genA.py (family A), l3check.py (fast regression in check.sh), tsearch.c (uniform templates),
  lsearch.c (template levels on a fixed base genome, BASE=txt), psearch.c (perturbation climb from a base txt; LM = mutable levels).
  Binaries are built into the scratchpad (gcc -O2 -o $SP/x x.c); rebuild after a container change.
- Status: §2 TRI, §3 TRI-MU, §4 FEEDBACK, §7 TOP-ADD written with proofs (lane); family A data to d = 40, A-RUN proof pending.
- MOVES-2D DEAD (§9): kill/KILL_M2D_d6_mu13.json (μ 13 at d 6), kill/KILL_M2D_d8_mu21.json (μ 21 at d 8); reported to the Lead 00:31Z.
- IN FLIGHT (detached; resumable: rerun the same line, finished levels are skipped): lift→climb chains
  `PFX=out/cA/c SP=$SP ./chain.sh kill/KILL_M2D_d8_mu21.txt 8 12 20000000 100` (cA), `PFX=out/cB/c … out/best_d7.txt 7 12 … 200`
  (cB), `PFX=out/cC/c … kill/KILL_M2D_d6_mu13.txt 6 11 … 300` (cC), cwd experiments/lower/l3. Records so far (verified by xcheck +
  box150 check.py): d 7: 17 (out/best7_d7.json), d 9: 29 (out/cA/j_d9.json, F = 2 3 8 9 12 13 28 27 7: a doubling level).
- Never edit chain.sh while a chain runs (bash reads scripts incrementally; I killed and restarted cA once for that).
### Sources opened (this box)
- claude/l-si 0803d551 docs/si/N5-TROPICAL-box76.md l. 167-170 (L-SI 41 replay of my nine genomes: «Every (d, T, mover, moves) of the
  README table is reproduced»); claude/l-red 55557951 experiments/red/r214/lower3/, memb.py, lowrep.py (L-RED 52 replay; verdict
  in the commit message «ideal.py / fa / lemck / box150 reproduce all 9»); claude/referee c011995c docs/referee/R-P-M2D-DEAD.md
  (PM-L1..L4); claude/referee-2 6eba8b93 docs/referee-2/R2-P-M2D-DEAD.md (W-1, N-1, N-2).
- docs/RESULTS.md R104 (l. 9864, IDEAL-model definition), R110 (l. 11323, 𝓛^R_d), R112 (l. 11909, T^R(3) = 8), R113 (l. 12152,
  ALIGN, F0, PAIR-DOUBLE, MOVES, T-BOUND, PATH-RISE), R114 (l. 12394); R111 (l. 11598, CASCADE/LADDER, read only).
- claude/l-new d86adc86-era docs/new/P-IDEAL-MOVES.md (§0-§6: REDUCE-XI, MOVES-EQUIV, AND-GATE, WINDOW-DOUBLE, SEG-WINDOW, DEAD-SEG,
  DEAD-LEV, lane DATA μ by level d 3: 1, 3, 4); experiments/new/box187/movescheck.py, box150/check.py (Gen), box186/out/*.json,
  box187/inst/m4_z4_r7.json.
- claude/l-red 242fbd1e notes/L-RED.md (successor 51 PARK, successor 52 handover; R213: MOVES-2D exact d 3, holds d 4; R214 DENSE
  runs), experiments/red/r214/keep/dense_d5_l3_H10.txt + out/dense_d5_l3_H10.json (36d340c7; μ 10 at d 5; copied byte-identical to
  experiments/lower/l3/inst/, sha1 a449d771…), out/c_m5_*ext_d6* (climb d 6: maxR 10).
### Things only I know
- The Lead's goal (a) «μ(G_d) ≥ 2d for every d» is false at d = 3 (μ(3) = 4, L-RED R213 data) and maybe at d = 6 (my lift search
  and L-RED's climb both stop at 10 < 12). TRI genomes cap at 2d − 2 (proved), so any 2d family needs upward options.
- tsearch mode 2 once preferred cyclic templates (sentinel bug, fixed: cyclic = −1e9).
- Family A d = 10 run (rows = steps, E/O = even/odd mover of each level moves):
  1 .O .. .. .O .. .. .O .. .. .O / 2 E. .. .O .O .. .O .O .. .O .O / 3 .. .O .O .. .O .O .. .O .O .. / 4 .. E. .. .O .O .. .O .O .. .O
  … / 20 .. .. .. .. .. .. .. .. .. E.  (regenerate: python3 -I experiments/lower/l3/trace.py with genA 10).

## Predecessor (T-L2, 2026-10-15) notebook, kept as history
# L-LOWER notebook (T-L2 theory box ended 2026-10-15 19:30Z; handover for the Lead / a successor)
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point
Branch claude/l-lower. Read docs/lower/L2-theory.md first (the box's product), then L1-statement.md (model), L1-report.md,
L2-data.md. Left RUNNING detached at 19:21Z in this container (they die with it; logs in experiments/lower/ are snapshots):
result_b2_n5_k9.log (general n = 5, k = 9; round 3), result_k5_deg2_k9.log (K_5, k = 9; round 7),
result_b2_n5_k9_p2sz1-2-3.log (|P_2| ∈ {1,2,3}, k = 9; round 2). To resume in a new container: the checkpoints
b2_n5_k9.subset.json, k5_deg2_k9.subset.json, b2_n5_k9_p2sz1-2-3.subset.json are gitignored (lost with the container);
restart from the committed k = 8 cores: `cp b2_n5_k8.subset.json b2_n5_k9.subset.json` is not possible either (ignored), so
seed from b2_n5_k8.json's "subset_games" (write it to b2_n5_k9.subset.json) and run `python3 -I cegar5two.py 9 2000000 200 1`;
likewise P2SIZES=1,2,3 from b2_n5_k8_p2sz1-2.json, and `python3 -I cegar_class5.py 9 200` for K_5 (seeds itself).
Each k = 9 SAT round with 600-1200 five-vertex games took 1-3 h on this machine; budget a day.

## DONE (this box; see docs/lower/L2-theory.md for everything, with SHAs and commands)
- MECHANISM (the box's main finding, data): the gate above 2n − 2 is the price of serving two COUNTS of priority-2 vertices
  with one vertex-anonymous program. n = 4: every single count costs 6, every pair of counts except {1, 2} costs 6, {1, 2}
  costs 7 (class table, L2-theory §3). n = 5: |P_2| = 1 costs exactly 8 (C3, full sweep of 4.58e9 games), |P_2| ∈ {1, 2}
  costs ≥ 9 (C2'), the general class ≥ 9 (C2, two solvers), the family K_5 ≥ 9.
- B_2(4) ≥ 7 certificate minimised: 68 whole games / 217 vertices (b2_n4_k6_core3.json), UNSAT by 4 solvers; localised
  to the class K (one Even vertex e of priority 1, Odd a (P_2), b (P_2 or P_1), c (P_1), all out-degrees 2): 28 games
  (core_exact_k6.json), 97 bisimulation classes (qcore_exact_k6.json), 53-pair kernel. Table of classes in L2-theory §3.
- B_2(5) ≥ 9: 414-game core b2_n5_k8.json, UNSAT by CaDiCaL (29 min) and Glucose (50 min).
- Lemmas 2.1 (one bit per gate), 2.2 (tower) in L2-theory §2.
- Goal (a) (human-readable proof): NOT achieved; obstruction measured (DRUP 63k lemmas; chain-only enumeration 8 561
  partitions at level 4; last gate has > 1000 admissible sets). Goal (b): family K_n defined; growth unproved; data gap ≥ 1
  at n = 4, 5.

## IN FLIGHT
- The three k = 9 runs above (undecided at the end of the box). UNSAT in any = B_2(5) ≥ 10 (gap grows).

## NEEDS
- Lead: decision on parking (L2-theory §5b: recommendation = park the theory goal; keep the two cheap n = 5 experiments).
- Owner/Lead: an independent DRAT/LRAT checker is not available in this container (the platform classifier refused
  `curl` + `gcc` of drat-trim); the standard applied is "UNSAT by ≥ 2 independent solvers" (4 at n = 4, 2 at n = 5).

## Things only I know
Tooling quirks (in addition to the previous session's list, kept below):
- `pkill -f PATTERN` kills your own shell when PATTERN occurs in the command line you typed (it did, twice). Use
  `pgrep -f "^python3 -I script.py"` (anchored) and kill the PIDs.
- `cmd | tail -N` shows nothing until cmd ends; for long runs write to a log file and `tail -n` it.
- coremin2/coremin3/qmin minimise with ONE solver instance and assumptions (seconds per call); coremin.py (plain) costs one
  full solve per call (20 s at n = 4, 30 min at n = 5). Minimal cores are not unique; several orders, keep the smallest.
- The depth-type machinery (levels.py on a core, tower.py on all 51.9M (game, vertex) pairs, 16 min, 6 GB) shows the core
  needs modal depth 4 only; the 90 mixed depth-5 types of the full class live in other games (tower.py's M_6 list).
- cegar_owner.py classes: owner mask + P_2 masks + `FILTER` (numpy expression over deg(v), loop(v)); runs take seconds to
  minutes; the class table in L2-theory §3 is exactly these runs (logs result_*.log).
- sat_shape.py 'chain+j' shapes are NOT restrictive as written (they let all gates read all earlier gates): ignore those
  results; 'full' and 'chain' are correct.
- cegar5two.py samples random 5-vertex games (no full sweep): an UNSAT core is a proof, a SAT candidate is not an upper bound.
- Memory: a k = 9 instance with ~7 000 nodes is ~11M clauses (~4 GB); keep ≤ 2 such solves at once (16 GB cgroup).
Previous session's list (still valid):
- All SAT searches encode "program with k Cpre gates" by truth tables: gate i reads (P_2, V_E, s_1..s_{i-1}); the output is
  a truth table too. UNSAT on any successor-closed subset of games is a valid lower bound (projection argument).
- One-player: satsearch.py (exact on Q_n), cegar5b.py (n=5; W per priority pattern cached in $W5_CACHE); OOM at ~20e6 clauses.
- Two-player: vec2.py, sat2.py (`exact n kmax`, `cegar4 k per_round`), depth2.py (minimal depth, ~15 min, ~6 GB).
- Running detached: `setsid nohup python3 -I x.py > log 2>&1 &` (inside parentheses).
- One-player n=4 structure (L1-report §3): the 6-gate chain uses distance and two-visit bits (pigeonhole witnesses).

## Queue (if the lane continues)
1. Read the three n = 5 results; if k = 9 UNSAT: B_2(5) ≥ 10, update L2-theory §4, §5, §6 and L2-data table.
2. If k = 9 SAT with a candidate passing 2·10^6 random games: full sweep by (owner, priority) pattern (1024 × 28.6M games,
   ~1 h) before claiming B_2(5) = 9.
3. K_6 (cegar_class5.py generalised to n = 6; 2 × 15^6 = 22.8M games, sweep feasible) at k = 10, 11: growth of the gap on
   the family.

## Sources opened
| source (arXiv id / DOI) | result used (theorem / section) | opened on | note |
| --- | --- | --- | --- |
| Chatterjee-Dvořák-Henzinger-Loitzenbauer, arXiv 1711.09148 v1 (SODA 2018) | §1 p.1-2 model and the "2n one-step operations" remark; §2 Preliminaries (Pre/Post, Set Disjointness, Thm 2.1); Reduction 3.1; Lemma 3.4 (O(1) bits per one-step op); Reduction 3.9 (p.7); Thm 3.10 (p.7) and its proof (p.13); Thm 3.11; §4 upper bounds (Büchi O(min(SCC+D, |T|·D))) | 2026-10-14 | pdftotext of arXiv v1 PDF; Reduction 3.9 graph has out-degree ≥ 1 everywhere |
| Arnold-Niwiński-Parys, LIPIcs.CSL.2021.9 (DOI 10.4230/LIPIcs.CSL.2021.9) | §2 fixed-point expressions, f_{A,B}, trees, Prop. 2.5 (S_{n,h} universal, width n^{lg(h/lg n)+O(1)}); §3.1 definition of ‖F‖_{U,V} (cases (1)-(3)), Lemma 3.1, Lemma 3.2 (|U|·|V| queries), Remark 3.3; §3.2 Algorithm 1, Lemma 3.4, 3.5, 3.6 (worklist, |V| to |V|(1+nd) queries), Cor. 3.7; Thm 5.1; Remark 5.5 | 2026-10-14 | DROPS PDF; intro p.9:2 states the symmetric bound n^{2·lg(d/lg n)+O(1)} explicitly |
| Bradfield-Walukiewicz, "The mu-calculus and model-checking", Handbook of Model Checking (author copy www.labri.fr/perso/igw/Papers/igw-mu.pdf) | formula (1), p.19 (after Theorem 7): μZ_{2d+1}.νZ_{2d}...νZ_0.γ with γ = ∧_i (p_i ⇒ (p_Eve ∧ ⟨b⟩Z_i) ∨ (p_Adam ∧ [b]Z_i)); Acc = limsup even (p.13) | 2026-10-15 | unnumbered display; typo γ(Z_0..Z_d); used for Transfer 2.4's vertex-priority form |
| Emerson-Jutla-Sistla, TCS 258 (2001) 491-522 (people.irisa.fr/Nicolas.Markey/PDF/Papers/tcs258(1-2)-EJS.pdf) | Theorem 3.2 (parity tree automaton emptiness as μ-calculus model checking), Lemma 3.5 | 2026-10-15 | numbered primary statement for the nested-fixpoint characterisation (automata form; index convention shifted) |
| Chatterjee-Dvořák-Henzinger-Svozil, arXiv 1909.04983 v1 | Algorithm 1 (black-box set-based progress measure), lines 3-16: worklist (popActiveSet) | 2026-10-14 | adaptive; used only for the CAUTION in Transfer 2.4 |
| REFEREE report R-L1 (claude/referee 9b01cbb, docs/referee/2026-10-14-L1-statement-check.md) and L-LIT T9 (trunk 735a4c7, docs/lit/T9-L1.md) | findings 1-9, gaps G1-G6; T9 (a), (b) | 2026-10-15 | fleet documents, not sources; drove v2 of the statement |

| Chatterjee-Dvořák-Henzinger-Loitzenbauer, arXiv 1706.04889 v1 (CSL 2017), "Improved Set-based Symbolic Algorithms for Parity Games" | §1 p.3 (classical set-based algorithm O(n^c) symbolic operations, O(c) sets); Theorem 20 (App. D.1: ClassicParity, O(n^c) symbolic one-step and set operations); Lemma 27 (App. D, "Simplified Analysis"): "O(n^2) symbolic one-step and set operations for c = 2", i.e. two-player Büchi; Theorems 8, 9 (c ≥ 3) | 2026-10-15 | adaptive model (attractors, repeat-until loops); no lower bound for games beyond the one-player Ω(n) of SODA'18; SODA'18 (1711.09148) itself contains no two-player statement (the word "game" occurs only in the grant line) |

## Dead ends
- T-L1 via depth/locality: capped at 2n-1 by Theorem B (docs/lower/L1-report.md §2); instance: the lasso pair of Lemma 2.1'.
- T-L1 via two-party communication (CDHL's method): capped at Θ(n) on Reduction 3.9 (two bits per Pre); no family found where a
  Pre costs O(1) bits and the problem costs ω(n) bits.
- Uniform O(n) construction for one-player Büchi from chains: window-1 chains need >= 12 gates at n=5 (UNSAT cores
  cegar5_k{8,9,10,11}_w1.json), window-2 >= 9 (cegar5_k8_w2_b.json); the n<=4 chains are pigeonhole witnesses specific to n.
- "e-profile" witness idea (colour vertices by exact min distance to P_2, follow e-decreasing paths; a losing graph then needs
  L+1 distinct vertices on a pattern path of length L): sound, but incomplete — the greedy path may run into a losing P_2 vertex
  (instance: v -> u_1 (P_2, u_1 -> z loop) and v -> long cycle with P_2); not pursued further.
- T-L1 itself: data against (B_1 = 2n-2 for n <= 5); parked by the Lead 07:50Z.
- T-L2 (a), human-readable proof of B_2(4) = 7 (2026-10-15): no short proof; instances b2_n4_k6_core3.json (68 games),
  core_exact_k6.json (28 games of class K), qcore_exact_k6.json (97 classes), qcore_exact_k6_pairs_k6.json (53 pairs);
  obstruction: DRUP 63 298 lemmas, chain-only case tree 8 561 live partitions at level 4 (docs/lower/L2-theory.md §3b).
