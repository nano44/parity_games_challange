# R199 Nested doubling (delay-δ stacks): k = 2 nested levels EXIST (exact, pinned nd2_d5_F12_n96, d 5); k = 3 (delays 4, 2, 1) is UNSAT at d ≤ 5 and UNDECIDED at d 6-7; tools: C-ELEMENT form of the IDEAL step, exact boolean synthesis in the R104 set semantics (L-RED successor 48)
Started 2026-11-03 07:20Z (Lead brief STEP 1, date -u). Brief: «Build a delay-δ line for δ = 3, and stack delays 3, 2, 1 over three levels so
that three consecutive levels double, at d = 6-7 … Success means the trend toward ~2^(d/2) carries … Failure means the exact obstruction to
a delay ≥ 3, stated as a lemma.» Labels: PROVED (lane), EXACT (z3, machine-checked, not Lean), DATA, OPEN. Model: IDEAL-ACYC (RESULTS R104),
degree 2, width-2 W-ladder (R197 notation) plus optional W-leaf helpers. Premises: RESULTS R104 (REALIZE) for pins; R189 Corollary LAG /
RE-REVERSAL and R198 Lemmas K0-K3 (lane, quoted from their files) for redundant solver clauses. Not a TARGET.md claim. G-N5-TIME OPEN.
No family.

## 0. Answer
- Target family (r199/genk.py): k NESTED doubling levels over a base level 0 with F_0 = 2: period P = 2^k, L = 3P; level j moves at
  every carry of level j − 1 (prompt mover) and P / 2^j steps later (late mover). On the W side this gives F = [2, 6, 12, …, 3·2^k]:
  levels 1..k double (level 1 at 2F_0 + 2, the others at 2F_(l−1)). The W side (gates, starts) is satisfiable for every k tried (build.py).
  The question is the Ξ side.
- k = 2 (delays 2, 1; L 12): EXACT. d 4 (one level above): UNSAT (4.9 s; agrees with the exact d 4 bound F_2 ≤ 10 of R197 §2b, an
  independent encoding). d 5 (two levels above): SAT (4194 s) → nd2_d5_F12: L 12, F = [2, 6, 12, 8, 4], exactly the prescribed pattern.
  Mechanism (r197/trace.py): v1 (late, level 1) is woken by v2 (late, level 2), v2 by its prompt partner u2; base u0 / v0 woken by u4 / v4
  (level 4): the delay-2 line of level 1 runs THROUGH the late mover of the doubled level above (a C-element divider: v1's key flips
  once per base interval, its Ξ-comparison follows v2). Pinned nd2_d5_F12_n96 (n 96; sha1 .pg c232f62b…, .start 4260debb…): PIN OK
  (startck, Oink 8fbf0a7 --zlk + verify, --tl + verify, xeng); lemck L 12, 0 violations. Genome checks against R104's hypotheses: Ξ
  acyclic, W-targets one level down, gates and ranks distinct; N 10, M 20, R104 n = N + 3M + 6 = 76 (the pin, stab pad 1, has 96).
- k = 3 (delays 4, 2, 1; L 24; F [2, 6, 12, 24]): EXACT UNSAT on the bare d 4 ladder (2.6 s) and at d 5 (one level above, 246 s).
  The two-base-interval variant (L 16, F [1, 4, 8, 16], same delays) is UNSAT at d 5 (69 s). d 6 (two levels above): UNDECIDED (unhinted
  timeouts 7000 s and 14000 s; delay-chain hint 9000 s). Hints from nd2: its full Ξ map with a level inserted UNSAT (4.2 s); its top-level
  + aux wiring (levels ≥ 3) UNSAT (56 s); its aux wiring alone UNSAT (124 s): the k = 2 mechanism does not extend by inserting a level.
  d 7: UNKNOWN (14000 s); d 6 L 16: UNKNOWN (10000 s; portfolio §3a).
- So: delay-2 nesting (two doubling levels) needs 2 levels above the stack (k = 2: d = k + 1 + 2); delay-4 nesting (three levels) is
  impossible with ≤ 1 level above and open with 2-3. No d(k) trend can be stated from k = 2 alone. NOT a family.

## 1. C-ELEMENT form of the IDEAL step (PROVED, lane; r199/req.py)
- Lemma C-ELEMENT. Degree 2. Let KP_t(x) be the key-preferred option of x under the keys of s_t and C_s(x) the strictly Ξ-better option
  of x at s (two option chains of x differ in x's own faces, distinct β's never tie under the R104 comparison). Then
  s_t(x) = KP_t(x) if KP_t(x) = C_(t−1)(x), and s_t(x) = s_(t−1)(x) otherwise.
  Proof. A_(t−1)(x) is {s_(t−1)(x)} if C_(t−1)(x) = s_(t−1)(x), and both options otherwise; x takes the key-least element of A_(t−1)(x)
  under the keys of s_t (R104 IDEAL step). If KP_t(x) = C_(t−1)(x): either both equal s_(t−1)(x) (x stays = KP), or both differ from it
  (both options available, x goes to KP). If they differ, one of them is s_(t−1)(x): if C_(t−1)(x) = s_(t−1)(x), only the current option
  is available; if KP_t(x) = s_(t−1)(x), x stays on its key-least option. ∎
- Corollary (prescribed runs). A state sequence s_0..s_L is the IDEAL run of a genome iff (i) every move goes to KP_t (W side: gates,
  and on a width-2 ladder only 2 gate bits per level matter, R198 K3), (ii) C_(t−1)(x) = s_t(x) at every move, (iii) C_(t−1)(x) =
  s_(t−1)(x) at every non-move with KP_t(x) ≠ s_(t−1)(x) (Ξ side). Requirements (ii)-(iii) are what r199/req.py lists.
- Lemma GREEDY (PROVED, lane; r199/xisearch.py docstring): with Ξ-targets fixed, the Ξ requirements are pairs of β-sets with a required
  winner; ranks and parities exist iff repeatedly choosing a face whose parity demands over the undecided requirements agree, giving it
  the highest free rank, empties the list (exchange argument). DATA: dd_d5_F14's own Ξ-targets pass (check.sh).

## 2. Why the bare ladder cannot nest three levels (PROVED, lane, for the period-8 target; z3 agrees)
- In the k = 3 target the even steps contain exactly one mover, the late mover x_3 of the top doubled level (delay 1). Every LAG move
  at an odd step (v2 at t ≡ 3 mod 4, v1, u0, v0) is woken by a Ξ-descendant that moved at t − 1 (R189 Corollary LAG / R178 XI-NEW), so
  each of them Ξ-reaches x_3. x_3 itself is LAG (its key order is unchanged at even steps), woken at t − 1 ≡ 3 mod 4, where the only
  movers are u3 (the prompt partner) and v2; v2 is excluded (v2 reaches x_3, acyclicity), so x_3 reaches u3. u3 moves at t and t + 2
  (t ≡ 3 mod 4); RE-REVERSAL needs a descendant of u3 moving at t or t + 1: only v2 (at t) or x_3 (at t + 1, an ancestor) qualify, so u3
  reaches v2: cycle u3 → v2 → x_3 → u3. ∎ Extra levels above the stack remove the argument: their movers have keys that flip at every
  step (R_3 flips at every step), so they can move at even steps PROMPTLY (no wake needed). The exact runs say one extra level is not
  enough (d 5 UNSAT), and two are enough for k = 2 but undecided for k = 3.

## 3. Runs (EXACT where stated; r199/xbmc.py: main levels fixed to the target, extra levels free; LEM clauses on)
| target | levels above | d | result |
| --- | --- | --- | --- |
| k 2, L 12 | 1 | 4 | UNSAT 4.9 s |
| k 2, L 12 | 2 | 5 | SAT 4194 s, nd2_d5_F12 (pinned) |
| k 3, L 24 | 0 | 4 | UNSAT 2.6 s (xisat) |
| k 3, L 24 | 1 | 5 | UNSAT 246 s |
| k 3, L 24 | 1 + 2 W-leaf helpers at level 4 | 5 | UNKNOWN 10000 s |
| k 3, L 24 | 2 | 6 | UNKNOWN 7000 s, 14000 s; chain hint UNKNOWN 9000 s |
| k 3, L 24 | 2, nd2 map (level inserted) / levels ≥ 3 / aux only | 6 | UNSAT 4.2 / 56 / 124 s |
| k 3, L 16 (two base intervals) | 1 | 5 | UNSAT 69 s |
| k 3, L 24 | 3 | 7 | UNKNOWN 14000 s |
| k 3, L 16 | 2 | 6 | UNKNOWN 10000 s; seeds 1-3 portfolio to 21:00Z (§3a) |
| k 3, L 16 | 1 + 2 helpers | 5 | UNKNOWN 6000 s |
- Sanity: dd_d5_F14 levels 0-3 fixed, level 4 free: SAT 68 s, replay matches.
- §3a Where the d 5 refutation lives (EXACT, xbmc CORE): with the main Ξ-requirements switched off (CORE=1) both k = 3 targets stay UNSAT
  at d 5 (57.7 s / 96.9 s): main TIMING (RE-REVERSAL / LAG over Ξ-reach) + the level-4 movers' exact IDEAL semantics suffice. With the main
  requirements on and the level-4 IDEAL rule kept only at a set of steps (CORE=2, deletion-minimised, 600 s per check, UNKNOWN keeps a step):
  L 16 target UNSAT with the rule at steps {4, 5, 6, 9, 10, 15} only. In the L 16 target the level-1 late moves are at t 5, 13 and the base
  move at t 9; steps 4-6 and 9-10 bracket the first two of these (step 15 is not explained). READING: the late wakes that §2 shows must come
  from even-step movers above the stack. The pure wake-order relaxation (xwake.py: K, RE-REVERSAL, LAG, Ξ out-degree ≤ 2, comparison bits that change only on
  descendant moves) is SAT for every target, so the priority-value semantics of the level-4 movers is essential: no purely combinatorial
  (wake-graph) obstruction exists at this granularity. Lemma candidate (OPEN): one level above a 3-level nested stack cannot supply the
  even-step wakes at the delay-4 and base steps; not proved by hand.
- cegar.py (xwake proposes level-4 schedules, xisat refutes each with all states fixed) refuted 98 schedules of the d 5 L 16 case in 2 h
  without converging (stopped): schedule enumeration is not a route to d 6.
- Arithmetic note (PROVED, lane): a literal delay stack 3, 2, 1 cannot fully nest: a level-1 interval split at offset 3 leaves a
  level-2 interval of length 1 (3 = 2 + 1), in which level 3 cannot place a late move strictly inside; full nesting with delay 1 at the top
  over k levels needs base intervals ≥ 2^k, i.e. delays 2^(k−1), …, 2, 1 (the genk targets).
- Lost d 5 rows of successor 47 (rerun from 07:21Z): killed at the Lead's 10:20Z timebox, UNKNOWN (REL never returned; ~95 CPU-min each):
  XI=free KF=1 LAG=1 FMIN=2:13 liftloop.py 5 14 and FMIN=3:15 liftloop.py 5 18 (r197). Mine, same timebox: FMIN=1:1,2:3,3:7,4:15 at d 5 L 16.

## 4. Trend table (score: longest run of consecutive levels with F_l ≥ 2F_(l−1), F_(l−1) ≥ 2)
| pin | d | n (pin) | L | F | run | label |
| --- | --- | --- | --- | --- | --- | --- |
| dbl_d3_F6_n60 | 3 | 60 | 8 | [2, 6, 7] | 1 | exact (R197) |
| c4x_d5_F12_n96 | 5 | 96 | 12 | [2, 6, 12, 9, 2] | 2 | exact (R198) |
| dd_d5_F14_n96 | 5 | 96 | 14 | [2, 3, 6, 14, 7] | 2 | exact (R198) |
| nd2_d5_F12_n96 | 5 | 96 | 12 | [2, 6, 12, 8, 4] | 2 (nested, prescribed) | exact (R199) |
| tri_d5_L12_n96 | 5 | 96 | 12 | [2, 1, 3, 5, 8] | weak (ratios from F_1 = 1, over steps 2..L) | successor 47 (R198 §0b) |
- No run of 3 with F_(l−1) ≥ 2 is known. Growth claim: none.

## 5. OPEN / next
- k = 3 at d 6-7 (runs above). If SAT: realise, pin, then k = 4 to read d(k). If UNSAT at d 7: an obstruction lemma generalising §2
  (wakes of the lower late movers must pass through prompt movers of levels above; count how many such levels a delay 2^(k−1) needs).
- Faster exact engine for d ≥ 6: partial hints from §2's forced edges (x_3 → u3, v_low → x_3) are sound to add only when proved; §2 is
  proved for the bare ladder only.

## 5b. CORRECTION (2026-11-03 20:39Z, date -u; after L-NEW successor 50, box 151, relayed by the Lead 20:37Z)
- §3a said «the pure wake-order relaxation (xwake.py …) is SAT for every target, so the priority-value semantics … is essential: no purely
  combinatorial (wake-graph) obstruction exists at this granularity». That was an ARTEFACT: xwake.py's «reaches» relation was not acyclic
  (transitivity was asserted only for three distinct movers, and the degree-2 closure equation never forced reach(x, x), so 2-cycles
  x → y → x passed). Fixed in r199/xwake.py (antisymmetry + transitivity). Reproduced with the fix (all W-feasible gate choices of each
  target, r199/allgates.py; per choice < 3 s):
  | target | levels above (d) | fixed relaxation |
  | --- | --- | --- |
  | k 2, L 12 | 1 (d 4) / 2 (d 5) / 3 / 4 | UNSAT / SAT / SAT / SAT |
  | k 3, L 24 | 0 (d 4) / 1 (d 5) / 2 (d 6) / 3 (d 7) / 4 (d 8) | UNSAT / UNSAT / SAT / SAT / SAT |
  | k 3, L 16 | 1 (d 5) / 2 (d 6) / 3 / 4 | UNSAT (2 choices) / SAT / SAT / SAT |
- So the d ≤ 5 refutations ARE combinatorial: they follow from the wake-order clauses alone (K: moves go to KP; RE-REVERSAL; LAG; Ξ-reach a
  strict partial order of an out-degree-≤ 2 graph; comparison bits obeying the C-element rule and changing only when a reached mover moves),
  all of which hold on every IDEAL-ACYC run at degree 2. The relaxation exactly reproduces the exact frontier for k 2 (d 4 UNSAT, d 5 SAT)
  and k 3 (d ≤ 5 UNSAT). It is SAT at d 6-8 for k 3: no refutation there; its SAT schedules are the candidates for the exact check (CEGAR).
- The empty main core (CORE=1) and the step core {4, 5, 6, 9, 10, 15} (CORE=2) are EXACT statements about xbmc and stand; the READING drawn
  from the old xwake runs is withdrawn. Scope note (applies to all R199 refutations): a target's gates are those build.py picks; the
  corrected relaxation is now checked over ALL W-feasible gate choices (1, 1 and 2 choices with the full F for the three targets).

## 6. Files
experiments/red/r199/: xwake.py (wake-order relaxation; FIXED 20:39Z, §5b), allgates.py, cegar.py, cubes.py, slack.py, offs.py, masks.py, req.py, xisearch.py, xisat.py, xbmc.py, xbmc2.py (all-free exact BMC; slow at d 3, not used for results), build.py,
genk.py, gen3.py, match.py, schedof.py, synth.py (first LIA attempt, superseded); lag/nd2_d5_F12.json; instances/ (pin + pins.sha1);
out/ gitignored (logs). check.sh block «R199».
