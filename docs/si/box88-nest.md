# Box 88: do type-II leapfrogs NEST? (L-SI successor 46; Lead brief 2026-11-08, «go» 11:11Z)
Written 2026-11-08 (date -u in the commit). Labels: PROVED (lane) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD (instance) / READING.
Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1).
Tools: experiments/si/box88/ (leap88.py census; climb88.py generic climb; climbp88.py MIRROR lane climb; tie88.py, blind88.py CARRY
tests; check88.sh, wired). Inputs: the 26 frozen instances of boxes 84-86 (pinned there) and the instances frozen in box88/inst (pins.sha1).
Scope of every run: box81/ref idealcyc (IDEAL-CYC Howard, [E-LEV]), cap 3000.

## 0. Answer
- FAILURE as a counter: no family found in which k (type-II flips per unit, leap87's counter) grows super-linearly with h. What grows
  is a RELABELLING: on the MIRROR family the flips per unit stay ≤ 5 for every h (ev = 5 at h = 3, 4, 5 and the h = 6 builds), and k
  rises only because type-I flips become type-II flips. The 2k term of LEAPFROG-ASC is never used (L-RED R225-leap §2, confirmed here
  by an independent census: ev ≤ |E_U| − 1 on every unit).
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
- maxalt (L-NEW 65 box 197, asc197.py): NOT RUN. The commit 2f4167cd named by the Lead is not on origin/claude/l-new at my fetches
  (head 8b67d40e at 11:2xZ), so asc197.py is not available here.

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

## 5. Climbs
(pending)

## 6. CONJECTURE TWO-COPY-RED, SET branch (box 88 form)
(pending)
