# R156: two (or k) dynamic sources ADD, but weighted by class size. PROVED (lane), Lemma k-SOURCE (generalises ONE-SOURCE): in a W-run, an Even selector h whose options ride on k common sources u_1 … u_k (fixed prefixes) plus K_0 static options switches at most K_0 + Σ_b K_b (1 + WCH_F(u_b)) times. The proof: inside class b, a landing that does not climb b's static order forces a W-rise of u_b since the previous class-b landing. So a pair's leapfrog is paid by the sources' own W-changes, ADDITIVELY, and the brief's «flips ≤ WCH(u) + WCH(u′)» holds in this weighted form. Up the levels the bound composes as WCH(h) ≤ switches(h) + Σ_b WCH(u_b) ≤ K_0 + Σ_b (K_b + 1)(1 + WCH(u_b)): a factor up to (deg + 1) per level. So k-SOURCE alone does NOT give a polynomial bound for deep recursions, and does NOT forbid a leapfrog counter. Whether the degree factor is attainable needs K_b gate re-openings per source rise (GATE-r^dyn), i.e. a matching Ξ supply. DATA: src2_K3 (n 285): sources 247 (WCH 301) and 48 (WCH 24); h alternates class 2 → 1 → 2 (3 switches; the one descent has its source rise; bound 981). No multiplying instance
L-RED successor 36 (Opus 5.5; D1/D18). Lead 2026-10-31 05:44Z: «GO for your proposed R156 as your LAST box … Build a two-source selector
from two out-of-phase copies of a lower selector, whose shifted W-values leapfrog … whether a pair's flips are bounded additively by
WCH(u) + WCH(u′), or multiply up the levels. If additive, prove TWO-SOURCE as a lane lemma with exact premises (it would generalise
ONE-SOURCE). Otherwise give the multiplying instance (xeng, Oink).» Written 2026-10-31 from 06:4xZ (date -u).
- Labels: PROVED (lane) / DATA / READING. Not a TARGET.md claim. G-N5-TIME stays OPEN.
- Sources opened: docs/red/R155-recursion.md (ONE-SOURCE, GATE-r^dyn); docs/si/P-N5-SETTLE-box52.md §4 (W-MON).

## 1. Lemma k-SOURCE (PROVED, lane; L-RED successor 36)
- Setting. A W-run F (τ, λ_W fixed; W-MON). An Even vertex h ∉ C. Its options split into:
  - class 0: K_0 static options (W constant on F);
  - classes b = 1 … k: K_b options each, whose (σ, τ)-plays are FIXED prefixes (no Even prefix vertex switches in F) into one common
    source u_b, then u_b's play.
- Hypotheses (as ONE-SOURCE):
  - (S1) no play from an option passes h;
  - (S2) the options' W-values are pairwise distinct at every state of F.
- Statement. h switches at most K_0 + Σ_(b=1..k) K_b (1 + WCH_F(u_b)) times in F, where WCH_F(u) := the number of transitions of F at
  which W(u) changes.
- Proof.
  - (i) Inside class b the order ≺_b is static (ONE-SOURCE (i): common-suffix cancellation).
  - (ii) Every landing strictly raises W(h) (ONE-SOURCE (ii)).
  - (iii) Static options are landed at most once (ONE-SOURCE (iii)).
  - (iv) Let y then y″ be two consecutive class-b landings, at k < k″ (other landings may lie between). Suppose y″ ⪯_b y (not a climb
    in ≺_b). Then:
    - W_(k″+1)(y) ⊵ W_(k″+1)(y″), by the static order;
    - W_(k″+1)(y″) ▷ W_(k+1)(y), by (ii): W(h) = h ⊕ W(landing) rose from k + 1 to k″ + 1.
    - So W(y) changed between k + 1 and k″ + 1. y's prefix is fixed, so W(u_b) changed in that interval.
    - The intervals of distinct consecutive pairs are disjoint, so class b has ≤ WCH_F(u_b) such descents.
  - (v) Between descents, the class-b landings climb ≺_b, so there are ≤ K_b per climb. So class b has ≤ K_b (1 + WCH_F(u_b)) landings.
  - Sum over the classes. □
- ONE-SOURCE (R155) is the sharper k = 1 form when WCH(u) is large: K_1(K_0 + 1) + K_0. k-SOURCE trades K_0 for WCH(u_b). Both hold.
  The minimum of the two applies.
- Composition (Corollary, PROVED, lane): W(h) changes only when h switches or when the current option's source changes W. So
  WCH_F(h) ≤ switches_F(h) + Σ_b WCH_F(u_b) ≤ K_0 + Σ_b (K_b + 1)(1 + WCH_F(u_b)).
  - Over L levels of selectors with degree ≤ K this compounds to ≤ (K + 1)^L-type bounds.
  - So k-SOURCE is ADDITIVE in the sources, but a factor (deg + 1) per level is not excluded.
  - A leapfrog counter of depth L ~ n / K could in principle reach (K + 1)^L. Its levels must re-climb K_b times per source rise. By
    GATE-r^dyn (R155), each re-climb needs a gate re-opening, i.e. ≥ K_b gate signals rising in every epoch. That is a Ξ supply of the
    same size (R153 SW-XI). The open question is exactly that supply.

## 2. DATA
- wlev/mksrc2.py (the mksrc1.py construction with several dynamic classes) on obs_K12_m24: source u_1 = Even 247 (WCH 301), u_2 = Odd 48
  (WCH 24; disjoint plays). Each class has 3 options (odd markers just above z). No statics.
- wlev/src2trace.py on wlev/instances/src2_K3: «SRC2 src2_K3.pg n 285 iters 324 wruns 1 maxL 324 switches 3 class-changes 2 descents 1
  descents-without-source-rise 0 WCH {1: 301, 2: 24} bound 981 landings ['d2a3', 'd1a3', 'd2a3']».
  - h leapfrogs: class 2 → class 1 → class 2. The re-entry into class 2 is on the same option d2a3 (a descent in the lemma's sense,
    since it is not a climb) and is paid by a W-rise of 48 in between, as (iv) requires.
  - xeng: state sequences identical. Oink 8fbf0a7: OK.
  - Two other marker orders (not pinned): 3 switches each, same pattern, 0 descents without a rise.
- wlev/wch.py on src2_K3: the most W-order flips of a successor pair is still 24. The two sources leapfrog only a few times here,
  because 48's W changes 24 times against 247's 301.

## 3. READING and resume point
- The brief's question, «flips bounded additively by WCH(u) + WCH(u′), or multiplying up the levels», gets two answers:
  - per level: ADDITIVE, weighted by class size (k-SOURCE);
  - across levels: a (deg + 1) factor per level is allowed by k-SOURCE. It can be realised only if each level's gates re-open K times
    per source rise.
  - Neither a multiplying instance nor a lemma excluding it is in hand.
- Resume point for successor 37: «k-source selector bound vs. leapfrog counter». Either build a two-level leapfrog counter whose upper
  selector re-climbs ≥ 2 options per source rise (fed by distinct gate signals; GATE-r^dyn allows r per epoch), or prove that the gate
  re-openings per epoch are paid by Ξ-changes that do not compound (the XI-CH-POLY side).

## 4. Pins (experiments/red/check.sh «R156»)
- wlev/pins.sha1 (adds src2_K3); src2trace line above; xeng; Oink.

## DONE / FINDINGS / NEEDS
- DONE: this note; wlev/mksrc2.py, wlev/src2trace.py, wlev/instances/src2_K3; check.sh «R156». SHA: see the commit.
- FINDINGS:
  - PROVED (lane): k-SOURCE (switches ≤ K_0 + Σ K_b (1 + WCH(u_b))) and its composition corollary (≤ (deg + 1) factor per level).
  - DATA: src2_K3 leapfrogs 2 → 1 → 2, with the descent paid by its source rise (xeng, Oink OK).
  - READING: additive per level; across levels the multiplication is not excluded and needs a matching Ξ gate supply.
- NEEDS: none.
