# Box 88: do type-II leapfrogs NEST? (L-SI successor 46; Lead brief 2026-11-08, «go» 11:11Z)
Written 2026-11-08 (date -u in the commit). Labels: PROVED (lane) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD (instance) / READING.
Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1).
Tools: experiments/si/box88/ (leap88.py census; climb88.py generic climb; climbp88.py MIRROR lane climb; tie88.py, blind88.py CARRY
tests; check88.sh, wired). Inputs: the 26 frozen instances of boxes 84-86 (pinned there) and the instances frozen in box88/inst (pins.sha1).
Scope of every run: box81/ref idealcyc (IDEAL-CYC Howard, [E-LEV]), cap 3000.

## 0. Answer
- FAILURE as a counter: no family found in which k (type-II flips per unit, leap87's counter) grows super-linearly with h. On the
  untuned MIRROR towers the flips per unit stay at 5 (h = 3-5 and HP6b-HP8b, h = 6-8), and k
  rises only because type-I flips become type-II flips. Lane climbs raise the per-bit flips (tuned maxev 3 / 7 / 9 / 9 at h = 2-5, §5),
  not super-linearly, and always within NEST-CHARGE. On the 26 frozen instances ev ≤ |E_U| − 1 on every unit (my census, = L-RED
  R225-leap §2). That is NOT a lemma: L-RED 60 killed «ev ≤ |E_U| − 1» in general (R226-race §3, witnesses SHARP_EU1 / SHARP_EU2) and
  proved Lemma SHARP (ev ≤ |E_U| − 1 + 2k + ε).
- Exact obstruction (PROVED, lane, §2): **Corollary NEST-CHARGE**: on a LEAPFROG-ASC unit, ev ≤ 1 + da + db, where da, db count the strict
  increases of a_t, b_t on I. So k ≤ ev ≤ 1 + (D_U,I(w) − 1) + Σ_(o ≠ S) (D_U,I(g_o) − 1), and the nesting depth (L-RED's counter, §1) ≤ k.
  This is box 85's FLIP-U read as a bound on NESTING, not a new lemma: nesting of type-II flips cannot exceed the U-projected e-set
  heights at the bit's own w and gates. A family with super-linear k is therefore a family with super-linear D_U at one w or gate,
  i.e. the core (Σ_v D^tot_E, L-RED R225 EQUIV), and SET-flip nesting is not an independent route. This agrees with L-RED's READING
  (R225-leap §3): TWO-COPY-RED's SET branch and ADD(c) are one statement.
- What the data adds to FLIP-U (§4): it is tight (ev = 1 + da + db) on some unit of 23 of the 26 instances (maxratio 1.0 in out/leap88.out), and very loose on the lowest MIRROR bit
  (da + db = 2, 7, 13, 20 at h = 2-5, ev = 3, 5, 5, 5): the compared plays rise in LOCKSTEP. The e-set heights at w grow linearly, and the
  flips do not follow them.
- CARRY (§3): Lemma CARRY-TIE (PROVED, lane): with constant cycle nodes, the projected dynamics at ranks ≥ r depends on data below r
  only through Π_r-tied choices at Howard switches. DATA: such tie decisions happen at EVERY step on HP3 / TC3m / CL2_21, and the
  low-blind run stops at once (T = 0). So CARRY-TIE is true but vacuous on these families: the absence of a carry is NOT explained by a
  lack of ties. Recorded so that nobody uses it as the obstruction.
- maxalt (L-NEW 65 box 197, asc197.py at claude/l-new 2f4167cd, run read-only from a scratch extract, --files; out/asc197_run.out):
  HP2-5_mup 2 / 4 / 4 / 5, HP6b 4, CL2_21 5, TC5m 5, ND4_hp3 3, and the climb best NK6_cl21 6, the first instance above 5. COUNTING (asc197.py
  l. 87-95): per (v, maximal Λ-interval I), the sequence of tops; for each ordered pair x ≠ y, the greedy length (number of TERMS) of
  the longest subsequence x, y, x, y, …; maxalt = the max. It is an alternation LENGTH, not the Davenport–Schinzel order s: order s forbids
  length s + 2, so maxalt 6 means s ≥ 5 on NK6_cl21 (L-NEW's «s = 4» = maxalt 5). DATA only; no DS source opened by me.

## 1. Counters (exact, so that L-RED 60's depth-2 race can be compared)
leap88.census, unit = (mover x, SET option S, maximal interval I with every cycle node constant and Λ(x) ∈ {K1, K2}); events = steps
t → t + 1 with t, t + 1 ∈ I where [σ(x) = S] changes (leap87's and FLIP's convention). At an event state t: a_t, b_t, z_t, type I / II as
box 87 §2; H_t := {v ∈ a_t ∩ b_t : v more relevant than z_t}.
- ev, k (#type-II events), EU = |E_U|, excess = ev − EU.
- depth := #distinct min(H_t) over the type-II events of the unit = L-RED's «maxdepth» (R225-leap §2, claude/l-red 029e5d8b), verbatim.
- da, db := #steps u → u + 1 inside I (u + 1 < t_end) with a_(u+1) ≠ a_u, resp. b_(u+1) ≠ b_u; monofail := #steps where a or b decreases
  (E-MON + PROJ-MON predict 0); chargefail := #units with ev > 1 + da + db (NEST-CHARGE predicts 0).
- Option sets: default = the real bits' SET options (names file, as leap87); ALL=1 = every option whose Ξ-target is its own mover (as
  L-RED's leap225, without its PRIV / NODE filter).
- Switch census (nest88.py, my own implementation of L-RED 60's N2 / depth, R226-race §4, claude/l-red d08e317a; nest226.py not used):
  a SWITCH compares the NEW option with the OLD one at every mover with ≥ 2 options; N2 = #type-II switches; depth = max over (x, maximal
  Λ(x)-interval) of #distinct heads. On HP2-5_mup it gives L-RED's row exactly (switches 34 / 77 / 177 / 246, type I 34 / 76 / 172 / 235,
  N2 0 / 1 / 5 / 11, max type II per (x, I) 0 / 1 / 2 / 4, depth 0 / 1 / 2 / 2). Comparison: leap88's k compares S with the BEST other
  option (b_t), N2 compares new with old; k (ALL, summed) 0 / 4 / 11 / 20 ≥ N2 on HP2-5.
- Cross-check: default mode gives leap87's units / type I / type II / maxk on all 26 instances (out/leap88.out vs box87/out/leap87.out);
  ALL mode gives L-RED's HP row exactly (units 3 / 5 / 7 / 9, type II 0 / 4 / 11 / 20, maxk 0 / 3 / 4 / 5, maxdepth 0 / 2 / 3 / 3) and 156
  units on the 26 (L-RED: 158 on 27 = these + CX4_n21's 2). Two implementations agree.

## 2. Corollary NEST-CHARGE (PROVED, lane)
Setting and hypotheses: those of LEAPFROG-ASC (box 87 §1: PRIV, NODE, constant cycle nodes on I).
**Claim.** ev ≤ 1 + da + db.
Proof. Let t < t′ be consecutive events. They have opposite directions (F3). If t is ON and t′ OFF, then a_t >lex b_t and b_t′ >lex a_t′
(F2). If a_t′ = a_t and b_t′ = b_t, these contradict each other; so a or b changes at some step in (t, t′]. Symmetric for OFF then ON.
The intervals (t, t′] of consecutive events are disjoint, so ev − 1 ≤ da + db. ∎
**Corollary.** k ≤ ev ≤ 1 + (D_U,I(w) − 1) + Σ_(o ≠ S, Λ(g_o) = λ) (D_U,I(g_o) − 1), and depth ≤ k.
Proof. a_t = π({e_S} ∪ E_t(w)) is lex-nondecreasing on I (F1), so each strict change is a new value of π(E_t(w)): da ≤ D_U,I(w) − 1.
b_t is the maximum of the chains π(E_t(g_o)); it changes only at a step where some π(E_t(g_o)) changes, and each of those chains is
nondecreasing: db ≤ Σ_o (D_U,I(g_o) − 1). depth counts distinct heads of type-II events, so depth ≤ k ≤ ev. ∎
- Relation to box 85: FLIP-U (box 85 §2 (6′)) is the same count with every gate's changes added; NEST-CHARGE only counts changes of the
  maximum b. The content of box 88 is the reading: nesting is charged to e-set heights at the bit's own w and gates.
- Consequence for TWO-COPY-RED's SET branch (box 87 §5): under (b) (Σ_v D^tot_E polynomial) the SET branch holds for free; without
  (b) T3 is super-polynomial by EQUIV anyway. So the SET branch adds nothing to the core. READING: a counter build should target D_U at a
  bit's w / gates (hub heights), which is L-RED 60's depth-2 race on the non-SET side, not a separate SET-flip design.

## 3. Lemma CARRY-TIE (PROVED, lane) and why it does not help
Notation: si.Engine values val = (cycle node c, path set P, length). For a rank r, Π_r(val) := (reward(c), weight(P ∩ ranks ≥ r)).
- (REFINE) Π_r is order-preserving: val ≤ val′ ⇒ Π_r(val) ≤ Π_r(val′). (Same cycle node: the max of the symmetric difference decides; if it
  has rank ≥ r it decides Π_r too, otherwise the Π_r-parts are equal. Different cycle nodes: decided by the first component, kept by Π_r.)
- (ODD) For a fixed Even strategy σ, Odd's optimal values project to the optimum of the projected order: Odd's optimal play from v is
  ≤ every play from v, so its Π_r is ≤ every play's Π_r (REFINE), and it is attained. So Π_r(val_σ(v)) is a function of σ alone,
  computed with priorities ≥ r and the cycle nodes only.
- (HOWARD) σ_(t+1)(y) is a Π_r-maximal successor of y (REFINE). If y has one Π_r-maximal successor, that choice is a function of the
  Π_r-values; otherwise data below r (lower ranks of the path, the length) or the keep-current rule decides.
**Lemma CARRY-TIE.** On steps with constant cycle nodes, Π_r(val_(t+1)) is determined by σ_t, the Π_r-values at t and the choices made at
Π_r-tied movers. Hence lower levels can steer the dynamics at ranks ≥ r (a «carry» into level r) only through tie decisions (tie88.py's
counter). ∎ (from ODD and HOWARD)
DATA (tie88.py, blind88.py; unit = Howard step; set HP3_mup, TC3m, CL2_21; counter: steps with ≥ 1 tie decision / tie decisions / tie
switches, per real bit's threshold r): HP3_mup B1 17 / 489 / 70 of T = 17; TC3m B1 17 / 810 / 111 of 17. The LOW-BLIND-r run (ties keep
the current successor, then the larger index) stops at T = 0 for every bit on all three: every early step is a tie decided below r (the
delay lanes). So the channel is wide open everywhere, and CARRY-TIE does not explain why no carry appears.

## 4. DATA
Unit / scope / counters as §1. «per-bit» = default mode (real bits).
| set | units | type I | type II | maxk | maxdepth | maxev | chargefail | monofail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 26 frozen, per-bit (out/leap88.out) | 72 | 123 | 61 | 5 | 3 | 7 | 0 | 0 |
| 26 frozen, ALL (out/leap88_all.out) | 156 | — | 98 | 5 | 3 | 7 | 0 | 0 |
LOCKSTEP (per-bit; lowest real bit B1 of HP_mup; counters ev, k, depth, da, db, EU):
| h | ev | k | depth | da | db | EU |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 3 | 0 | 0 | 1 | 1 | 19 |
| 3 | 5 | 3 | 2 | 4 | 3 | 41 |
| 4 | 5 | 4 | 2 | 7 | 6 | 99 |
| 5 | 5 | 5 | 1 | 11 | 9 | 159 |
CLIMBS: see §5 (filled at the end of the box).

## 5. Climbs (DATA; frozen bests in box88/inst, sha1 in pins.sha1)
Unit = genome; scope as §1; counters leap88 (per-bit or ALL as named), nest88 (N2, depth), asc197 (maxalt, alternation LENGTH, §0).
| climb | seed genome / cfg | iterations | best (frozen as) | T | maxk | maxev | maxdepth | N2 / switch-depth | maxalt |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| climb88 (ALL; climb225 mutations) seed 2881 | CL2_21 | 1500 | NK6_cl21 | 11 | 6 | 7 | 3 | — | 6 |
| climb88 (ALL) seed 2882 | HP3_mup | 3000 | ND4_hp3 | 11 | 4 | 5 | 4 | — | 3 |
| climbp88 (per-bit; MIRROR lanes) h = 3 seed 2883 | HP3_mup lanes | 300 | HP3t | 17 | 3 | 7 | 2 | 1 / 1 | 4 |
| climbp88 h = 4 seed 2884 | HP4_mup lanes | 300 | HP4t | 24 | 7 | 9 | 4 | 6 / 2 | 5 |
| climbp88 h = 5 seed 2885 | HP5_mup lanes | 150 | HP5t | 71 | 7 | 9 | 2 | 13 / 2 | 6 |
| climbp88 h = 5 resume, seed 2895 | HP5t cfg | stopped at 14:05Z after ~70 min, no gain (only improvements are logged, so the iteration count is not known) | — (= HP5t) | 71 | 7 | 9 | 2 | — | — |
| (h = 6 lane climb seed 2886 from extrapolated lanes) | doubled HP5 lanes | stopped at 12:19Z after ~45 min, no gain over its seed (iteration count not logged) | — | 56 | 3 | 3 | 1 | — | — |
- No climbed genome violates NEST-CHARGE, E-MON or Claim C (chargefail / monofail / ascfail 0 on every scored genome; climb88 records
  violations and found 0 in 4,500 mutants).
- Fit: tuned per-bit maxev(h) = 3 / 7 / 9 / 9 at h = 2 / 3 / 4 / 5 (h = 2: HP2_mup); maxk(h) = 0 / 3 / 7 / 7. Neither is super-linear;
  maxev is flat from h = 4 to 5. A binary counter needs bit 1 to flip ≥ 2^h − 1 times (31 at h = 5).

## 6. CONJECTURE TWO-COPY-RED, SET branch (box 88 form)
- PROVED residue (lane): by NEST-CHARGE, the SET flips of a bit on a LEAPFROG-ASC unit are at most 1 + the strict increases of a_t and
  b_t, i.e. charged to the U-projected e-set heights of its w and gates. So the SET branch follows from (b) «Σ_v D^tot_E polynomial»; it is
  not an independent obstruction or route.
- **CONJECTURE (READING, SET branch only, unchanged in content, now with the nesting counter named).** On IDEAL-CYC under [E-LEV], the type-II
  flips of one SET bit within one LEAPFROG-ASC unit (leap88's k) are polynomially many in N + M; equivalently by NEST-CHARGE it suffices
  that D_U,I at a bit's w and gates is. Strongest DATA: maxk ≤ 7 and maxev ≤ 9 on the 26 frozen instances, HP6b-HP8b and every climbed
  genome (§4-§5); tuned MIRROR maxev 3 / 7 / 9 / 9 at h = 2-5; nesting depth (L-RED's counter) ≤ 4 (ND4_hp3, HP4t).
- Not covered: non-SET switches (L-RED 60's NEST-POLY, of which this is the SET part), cycle-node changes, non-hub e-set changes.
- DEAD in this box: the hope that SET-flip nesting gives a counter independent of hub heights (NEST-CHARGE). Instance: HP5t (lowest bit 9
  flips, k 7, da 13, db 11).
