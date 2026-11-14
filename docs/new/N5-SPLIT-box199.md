# Box 199 (D18): a game lemma at the split mover; the downward charge (L-NEW successor 66, Opus; 2026-11-08, written 18:09Z by date -u)
Lead brief (successor 66 start, «go» 17:51Z): find the mover u on v's play where a z-route and a y-route split; use Howard at the movers
(F1, DOM, STRICT; the Ξσ tie only among exact ties) to prove a DOWNWARD charge «each re-win of y at u is paid by a class change of a
vertex on the y-route below y»; combine it with PAIR-HIGH's UPWARD charge into a bound on P(y) or C; say what it gives and on which premises.
Labels: PROVED (lane, unrefereed) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD. Nothing here is a TARGET.md claim. G-N5-TIME stays
OPEN; N5′-xi stays a CANDIDATE (D1). Setting and notation: box 197 §1 and box 198 (docs/new/N5-PAIR-box198.md): a vertex v of Γ3(G), a
Λ-interval I of v in HOW3(G) (Λ_t(v) = w on I), E_t(v), tops, c_y, Dhi_y, U_y := the e-vertices more relevant than y, wt(y) := the single
successor of the e-vertex y (its W-target mover).
Premises: P-N5-CHAIN (frozen l-new 93531b03; line L-4 a69c8aa9; both referees MATCH, landing as R125 pending) §2 [OPT], (R), (Core), (E-DOM);
§4 F1, F3, F4′, F5, F6, STRICT; §5 CN2-3, LOC-GATE3, LOC-K2-3, NO-TIE3; §7 E-MON3. Nothing here uses [E-LEV] except where said.
Tools: experiments/new/box199/split199.py; record split199.out (11 frozen instances); check199.sh -> check199.out, re-run by check.sh
block «BOX 199 SPLIT».

## 0. Answer
- PROVED (lane): Lemma SPLIT. Every change of v's e-set happens at a split vertex u. u is a mover that switched to a strictly better
  successor, or a gate whose face order flipped. The change at v IS a change at u, with the same Λ = w and the same symmetric difference.
- PROVED (lane): Lemma REWIN / REWIN-HI. Take a re-win: two consecutive y-tops of (v, I) through the same split u and the same new successor b.
  Between them b's value rises strictly, and the rise is ABOVE y: E_t2(b) ∩ U_y >lex E_t1(b) ∩ U_y. This holds for mover splits (Howard:
  F1, STRICT, F5) and gate splits (LOC-GATE3, NO-TIE3).
- DEAD: the downward charge as briefed («paid by a class change below y»). On every one of the 11 instances there are re-wins where NO
  vertex of the y-route changes Λ or any letter less relevant than y. The smallest is CX4_n21 (192 of its 219 re-wins). REWIN-HI says what
  pays instead: a change above y, at b.
- CONJECTURE RW-WT (DATA, 0 failures in 4,460 re-wins): at a re-win the change above y sits in E(wt(y)), the fixed W-target of y. Every such
  letter is an ASCENT after y. DEAD for re-entries that are not re-wins: GROW7_n34 (18 re-entries; y re-enters under a new PREFIX letter
  before y, with E(wt(y)) constant). Also DEAD as a bound c_y(v) ≤ #values of E(wt(y)) ∩ U_y: HOLD2K_n84 (18).
- What the combination gives: NOTHING polynomial. PAIR-HIGH + REWIN-HI give a localized recursion of RA-PATHS' shape, now over
  (vertex, letter) pairs (§3). It is no smaller than PAIR-HIGH's in the abstract. A polynomial bound would still need a bound on the
  non-re-win re-entries W and on the recursion's paths; neither is proved. The D18 idea tried (§4, a product-order chain bound) is DEAD on data.

## 1. Lemma SPLIT (PROVED, lane; premises [OPT], F1, F5, F6, LOC-GATE3, LOC-K2-3, NO-TIE3)
Let t − 1, t ∈ I with E_(t−1)(v) ≠ E_t(v), and let P_s(v) be the play from v under (σ_s, σ̄_s), s ∈ {t − 1, t}. P_s(v) is a simple path
followed by one cycle, and Ω_s(v) is read off it ([OPT], F3). The two plays differ, so let u be the first vertex of P_t(v) at which they
leave by different edges: old := its successor at t − 1, new := at t. Then:
(i) u is a mover with σ_(t−1)(u) ≠ σ_t(u), or a gate with σ̄_(t−1)(u) ≠ σ̄_t(u). Non-mover Even vertices and pads have one successor in
    HOW3 (F6, [G3]). The only Odd vertices are the gates and K2, and σ̄(K2) = r at every state (LOC-K2-3).
(ii) Mover: Ω_(t−1)(new) ▷ Ω_(t−1)(old) (F5).
(iii) Gate: Ω_(t−1)(old) ◁ Ω_(t−1)(new) and Ω_t(new) ◁ Ω_t(old) (LOC-GATE3: Odd's face is the ◁-smaller; NO-TIE3: never equal). With F1
    this gives Ω_t(old) ▷ Ω_t(new) ⊵ Ω_(t−1)(new) ▷ Ω_(t−1)(old): the abandoned face rose strictly.
(iv) TRANSFER: Λ_(t−1)(u) = Λ_t(u) = w, and E_(t−1)(v) Δ E_t(v) = E_(t−1)(u) Δ E_t(u). So the change at v is a change of u's e-set inside
    a Λ-interval of u, with the same top.
Proof of (iv). u lies on the part common to both plays. The play from u at s is the suffix of P_s(v) from u, closed by the same cycle
(positional strategies). So Λ_s(u) = Λ_s(v) = w. Let A be the e-letters above w strictly before u on P_t(v). These are not on the cycle,
since cycle vertices other than w are less relevant than w. A is common to s = t − 1 and s = t, and E_s(v) = A ⊔ E_s(u). ∎
DATA (split199.py; unit: one change at one (v, I); set: the 11 instances of §5; scope: N5′-xi from S3 on Γ3, up to the first fallback):
playfail, kindfail, hwfail, gtfail, trfail all 0 on 34,518 changes. Splits: movers or gates only (no K2). Kinds of y-tops: at y's own mover,
at y's gate, upstream.

## 2. Lemma REWIN and Lemma REWIN-HI (PROVED, lane; premises as §1 plus F3, F4′, STRICT, CN2-3, (E-DOM), (Core))
Let t1 < t2 be consecutive y-tops of (v, I) (y enters E(v) at both). Let both have the same split u (§1) and the same new successor b,
and let a be u's successor at t2 − 1 (a ≠ b). Then
(a) Ω_(t2−1)(a) ▷ Ω_t1(b);
(b) REWIN: Ω_(t2−1)(b) ▷ Ω_(t2−1)(a) ▷ Ω_t1(b), so b's value rose strictly on [t1, t2 − 1];
(c) REWIN-HI: E_t2(b) ∩ U_y >lex E_t1(b) ∩ U_y.
Proof.
- (a), u a mover: σ_t1(u) = b ≠ σ_(t2−1)(u), so there is a first s ∈ (t1, t2 − 1] with σ_s(u) ≠ σ_(s−1)(u) = b. By F3 and F6,
  Ω_r(u) = ext(u, Ω_r(σ_r(u))). By F1, STRICT and F1 + F4′ (u is in no Π: CN2-3):
  Ω_(t2−1)(u) ⊵ Ω_s(u) ▷ Ω_(s−1)(u) = ext(u, Ω_(s−1)(b)) ⊵ ext(u, Ω_t1(b)).
  So ext(u, Ω_(t2−1)(a)) ▷ ext(u, Ω_t1(b)). The order is total, and F4′ (X ⊴ Y ⇒ ext X ⊴ ext Y) gives Ω_(t2−1)(a) ▷ Ω_t1(b).
- (a), u a gate: its successors are its two faces, so a is the face other than b at all times. At t1 Odd plays b: Ω_t1(b) ◁ Ω_t1(a)
  (LOC-GATE3, NO-TIE3). By F1, Ω_(t2−1)(a) ⊵ Ω_t1(a).
- (b): at t2 u moves from a to b. For a mover this gives Ω_(t2−1)(b) ▷ Ω_(t2−1)(a) (F5). For a gate, Odd played a at t2 − 1, so
  Ω_(t2−1)(a) ◁ Ω_(t2−1)(b) (LOC-GATE3, NO-TIE3). Then use (a).
- (c):
  - Λ_t1(b) = Λ_(t2−1)(a) = w, since both vertices are on v's play after u at those times (§1 (iv)). So [VJ] compares Π_(t2−1)(a) and
    Π_t1(b) by z, the most relevant vertex of their symmetric difference: z is in the larger one if even, in the smaller one if odd.
  - Vertices more relevant than an e-vertex are e-vertices, c_W, K0 and K3 (E-DOM). c_W is in no Π, and K0, K3 lie on both plays or on
    neither (equal Λ, (Core)).
  - y ∈ E_t1(b): y entered E(v) at t1, and the part before u is common to the plays at t1 − 1 and t1 (§1 (iv)). Also y ∉ E_(t2−1)(a),
    because y ∉ E_(t2−1)(v) = A′ ⊔ E_(t2−1)(a).
  - If no e-letter above y were in the difference, then z = y, which is even (e-priorities are even), and y ∈ Π_t1(b). That would give
    Ω_t1(b) ▷ Ω_(t2−1)(a), against (a).
  - So z is an e-letter above y, and z ∈ E_(t2−1)(a): hence E_(t2−1)(a) ∩ U_y >lex E_t1(b) ∩ U_y.
  - At t2 the top of v's change is y, so E_(t2−1)(v) ∩ U_y = E_t2(v) ∩ U_y. Both split as A₂ ⊔ (the successor's part), with the same A₂
    (§1 (iv); u is not an e-vertex). So E_(t2−1)(a) ∩ U_y = E_t2(b) ∩ U_y. ∎
- Corollary REWIN-COUNT. Fix (v, I, y) and a pair (u, b), and let R_ub be the number of re-wins through (u, b). Λ(b) = w at every y-top
  through (u, b), so Λ(b) = w on their whole span (F1, F2). On that span E(b) ∩ U_y is lex-nondecreasing (E-MON3), and by (c) it rises
  strictly across each re-win. Hence R_ub ≤ Dhi_y(b, J_b) − 1, J_b being b's Λ-interval containing the span, and
      c_y(v, I) ≤ 1 + W_y(v, I) + Σ_(u, b) (Dhi_y(b, J_b) − 1),
  where W_y(v, I) := the re-entries whose two y-tops have different (u, b).
- DATA (unit: one re-win; same set and scope): dnfail 0 and rhfail 0 on 4,460 re-wins (3,629 mover / 831 gate splits).
- Controls (CX4_n21): ctrl3 (strict rise on [t1, t1]) dnfail 219; ctrl4 (U_y := ∅) rhfail 219; ctrl1 (Howard direction reversed)
  hwfail 444; ctrl5 (gate test negated) gtfail 284.

## 3. The downward charge, and what the combination gives
- DEAD (the brief's form): «each re-win of y at u is paid by a class change of a vertex on the y-route below y». Reading: some vertex q of
  b's play at t2 has Λ_t1(q) ≠ Λ_(t2−1)(q), or a change of its e-letters less relevant than y, on [t1, t2 − 1].
  - Counter dn_nobelow_all (unit: re-win; must be 0 for the claim) is > 0 on all 11 instances.
  - Smallest instance: CX4_n21 (r225/inst, sha1 ef29debb, N 21, M 35) has 192 of 219 re-wins with no such change. First one: v = x0,
    y = e(10,0), t1 = 4, t2 = 6, u = x0, b = m_(0,0).
  - REWIN-HI is what replaces it: the forced change is ABOVE y (dnlo = 0, dnhi = rewin on every instance).
- CONJECTURE RW-WT: at every re-win, E(wt(y)) ∩ U_y takes ≥ 2 values on [t1, t2]. So the change above y is at y's fixed W-target, i.e. an
  ascent letter after y.
  - DATA: rwfail 0 on 4,460 re-wins. In the other direction, zbefore = 0: no re-win's top lies between b and y.
  - Not proved. (c) only places the change somewhere on b's play above y. The step missing to get from (c) to RW-WT: «the route letters
    between b and y are the same at t1 and t2».
  - DEAD for all re-entries (counter wcfail; unit: re-entry): GROW7_n34 (r226/inst, sha1 42bbd562), 18 re-entries.
    - First one: v = x10, y = e(15,1), wt(y) = x0, t 4 → 6. E(v) goes {e(14,0), e(15,1)} → {e(14,0), e(10,0)} → {e(14,0), e(10,0),
      e(15,1)}. E(x0) = {e(14,0)} at t 4, 5, 6.
    - y was expelled by e(10,0), a PREFIX letter (x10's own e-face, before y on the play), and re-entered under it by a different route
      (the split moved).
    - The same 18 appear in HOLD2K_n84 and HOLD3K_n125 (both contain GROW7). On HOLD2K_n84 (sha1 423a4a88) they also break the bound
      c_y(v) ≤ #values of E(wt(y)) ∩ U_y on the y-tops' span (wbfail 18).
- What PAIR-HIGH (upward) + REWIN-HI (at b) give:
  - Exactly REWIN-COUNT: c_y(v) ≤ 1 + W_y(v) + Σ_(u,b) Σ_(z ≻ y) c_z(b, J_b).
  - It has the shape of RA-PATHS (c_y ≤ 1 + Σ c_z), moved from v to the successors b on the y-route, and the sum over (u, b) can multiply.
    In the abstract it is no smaller than PAIR-HIGH: BIN realizes the latter with equality, and nothing here excludes the same at b.
  - With RW-WT it would localize further: every b becomes the one vertex wt(y), and only ascent letters count. Without [E-LEV] that is still
    the recursion C(y) ≤ 1 + W + k·Σ C(z) over an «ascent DAG». Under [E-LEV] each edge of that DAG needs an upward Ξ-edge on a play after y
    (UP-JUMP3), and different edges may reuse the same Ξ-edge, so the depth is ≤ M only.
  - Verdict: polynomial, quasi-polynomial: NOT obtained. The combination gives NOTHING beyond PAIR-HIGH as a bound.
  - It needs in addition (all OPEN):
    - (S4) W_y(v) polynomial: non-re-win re-entries, where the split pair (u, b) changes;
    - (S5) the number of distinct split pairs per (v, y) bounded (DATA ≤ 3);
    - a path bound in the localized DAG.
  - Premises: SPLIT and REWIN(-HI) use only P-N5-CHAIN's facts (R125, pending landing: both referees MATCH L-4). PAIR-HIGH is a lane lemma
    (box 198, survives L-RED 61). RW-WT is a CONJECTURE. No hypothesis beyond these; [E-LEV] only in the RW-WT reading.

## 4. D18: one idea from outside the toolkit (order theory: chains in a product of two chains) — DEAD here
- Idea. At y-tops, E(v) ∩ U_y = Pre ⊔ Suf, with Suf := E(wt(y)) ∩ U_y. Suf is lex-nondecreasing (E-MON3 at wt(y); Λ(wt(y)) = w on the
  span, counter wlamfail 0).
  - If Pre (the letters of U_y before y on v's play) were lex-nondecreasing too, the y-tops would form a chain in the componentwise
    product of two chains.
  - Then every step would raise at least one coordinate, and c_y ≤ #Pre + #Suf − 1 would be ADDITIVE (the Dilworth / Greene–Kleitman
    picture of chains in a grid).
- DATA: Pre is NOT monotone (counter premono_no; unit: (v, I, y)): GROW7_n34 18, GROW8_n53 14 (r226/inst, sha1 57758f40), HOLD3K_n125 18
  (r227/inst, sha1 2c3e610b), DU21_h4 165 (claude/l-si box89/inst, sha1 48da0ccb). DEAD.
- And even where it holds it is no gain (READING): every change of Pre or of Suf is a change of v's high part, so #Pre + #Suf − 1 ≤ Dhi_y(v),
  PAIR-HIGH's bound. The exponential in BIN comes from the recursion over letters, not from the product.

## 5. DATA table (split199.py; scope N5′-xi from S3 on Γ3, up to the first fallback; maxima over (v, I, y) of the genome)
| instance | N | M | T3 | changes | re-entries | re-wins (mover/gate) | max c_y | max W | max (u,b) | wcfail | wbfail | dn_nobelow_all | premono_no |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C2CX4_n23 | 23 | 38 | 11 | 951 | 389 | 336 (232/104) | 4 | 3 | 2 | 0 | 0 | 255 | 0 |
| CX4_n21 | 21 | 35 | 10 | 728 | 286 | 219 (136/83) | 5 | 2 | 2 | 0 | 0 | 192 | 0 |
| DSALT6_n108 | 108 | 206 | 21 | 333 | 81 | 79 (69/10) | 4 | 1 | 2 | 0 | 0 | 56 | 0 |
| DSALT7_n108 | 108 | 206 | 11 | 249 | 31 | 26 (18/8) | 4 | 1 | 2 | 0 | 0 | 24 | 0 |
| DSALT9_n416 | 416 | 801 | 30 | 9424 | 3315 | 2241 (2175/66) | 5 | 2 | 3 | 0 | 0 | 1234 | 0 |
| GROW7_n34 | 34 | 86 | 13 | 1552 | 289 | 192 (93/99) | 4 | 2 | 2 | 18 | 0 | 60 | 18 |
| GROW8_n53 | 53 | 147 | 18 | 3123 | 920 | 598 (448/150) | 5 | 3 | 3 | 0 | 0 | 366 | 14 |
| HOLD2K_n84 | 84 | 175 | 13 | 1793 | 286 | 185 (66/119) | 4 | 1 | 2 | 18 | 18 | 77 | 0 |
| HOLD3K_n125 | 125 | 252 | 17 | 2290 | 377 | 242 (111/131) | 4 | 2 | 2 | 18 | 0 | 82 | 18 |
| DU21_h4 | 220 | 419 | 24 | 13848 | 603 | 313 (260/53) | 3 | 1 | 2 | 0 | 0 | 97 | 165 |
| NK6_cl21 | 108 | 206 | 11 | 227 | 31 | 29 (21/8) | 4 | 1 | 2 | 0 | 0 | 16 | 0 |
- Counters that must be 0 and are 0 on every row: playfail, kindfail, hwfail, gtfail, trfail (SPLIT); dnfail (REWIN); rhfail (REWIN-HI);
  rwfail (RW-WT, data only); wlamfail. Units: §1-§3. ctrl2 (W-target bound with one value) wbfail 200 on CX4_n21.
- Instances (frozen copies, experiments/new/box199/inst/SHA1SUMS):
  - CX4_n21 ef29debb (claude/l-red experiments/red/r225/inst);
  - GROW7_n34 42bbd562 and GROW8_n53 57758f40 (r226/inst);
  - DSALT6/7/9 4136b27d / 16d48b3c / da3308b5 (r226/inst, = box198/inst);
  - C2CX4_n23 57b895ff, HOLD2K_n84 423a4a88, HOLD3K_n125 2c3e610b (r227/inst);
  - NK6_cl21 408b9988 (claude/l-si box88/inst, = box198/inst).
  - DU21_h4 48da0ccb (claude/l-si experiments/si/box89/inst; = L-SI pins.sha1, reproduced by L-RED 61 R227-si89 at l-red 04506b2e).
- Reading: max c_y ≤ 5 everywhere; re-wins are 52-98 % of the re-entries; W ≤ 3, split pairs ≤ 3. Nothing grows. These are short runs
  (T3 ≤ 30), not a bound. DU21_h4 (switch-depth 8, D_U 21) has max c_y 3: the additive regime, as L-RED 61 found.

## 6. Next (for the Lead)
- Prove or kill RW-WT: the step «route letters between b and y equal at t1, t2». A kill would be a re-win whose high change sits between b
  and y. The data have none (zbefore 0).
- (S4): the non-re-win re-entries are where y re-enters under a new prefix (GROW7 pattern). A lemma there would have to use the prefix
  letter's own Λ-interval. That is the next game restriction to try.
- L-RED / L-SI: a family with growing W_y or growing numbers of split pairs per (v, y) would be the first real pressure on REWIN-COUNT.

## Addendum 1 (L-NEW successor 66, 19:05Z by date -u; Lead 18:50Z: «RW-WT FIRST … then write exactly what RW-WT + REWIN-COUNT + R121 give … then (S4)»; Lead 19:00Z relays L-RED 61 R227-box199 (claude/l-red 1ea37d91): box 199 SURVIVES, RW-WT not broken on its own engine, rw 0 on 2,994 re-wins / 19 genomes)
Verdict on RW-WT: NOT proved in general, NOT killed. PROVED for every re-win whose t2-step is single-split (Corollary RW-1, 2,000 of the
4,498 re-wins on the frozen set). In general it is reduced to one CONJECTURE, RW-B0, with three-source DATA. A stronger form, ROUTE-LOW (all
y-tops), is DEAD.

### A1.1 ROUTE-LOW (DEAD)
- Statement tried: at every y-top of (v, I) with split u, no letter of U_y lies on v's new play between u and y. If true it would give RW-WT
  at once (§2 (c): E(b) ∩ U_y would be E(wt(y)) ∩ U_y).
- DEAD. Counter ytopB_ne (unit: y-top; must be 0): 65 on experiments/new/box199/inst/ROUTELOW_n21.json (sha1 80f9b977; N 21, M 38;
  CX4_n21 plus 3 random options, srch199.py seed 7 sample 429). Also 8 on DSALT9_n416, a natural climb.
  - First case: v = x0, t = 2, y = e(11,0), split u = gate (10,0).
    - The play at t − 1 is x0 x10 x18 x13 e(13,0) x2 …; at t it is x0 x10 e(10,0) x17 x13 e(13,0) x2 x11 e(11,0) x20.
    - The high letter e(13,0) lies on the new route.
  - Mechanism: TWO splits in one Howard step (movers 2, 5, 7, 8, 18 switch at t).
    - The gate flip at (10,0) re-routes the play, which re-merges at x13 before e(13,0).
    - The switch at x2, after e(13,0), is what brings y.
  - In all 21 + 5 search hits, the failures are at y-tops that are NOT re-wins (Bne below is 0).

### A1.2 Lemma RW-SHAPE (PROVED, lane; premises as §2)
Take a re-win (t1 < t2 through (u, b), a := u's successor at t2 − 1, m := wt(y)). Write E_s(b) ∩ U_y = B_s ⊔ S_s, with B_s the U_y-letters
of b's play at s before y and S_s := E_s(m) ∩ U_y. If S_t1 = S_t2 (RW-WT fails at this re-win), then:
(i) B_t2 ≠ ∅;
(ii) for every f ∈ B_t2, some vertex of b's play at t2 strictly between f and y has a different successor at t2 − 1 (a SECOND split, after f).
Proof.
- (i): S is constant on [t1, t2]: Λ(m) = w there, and E-MON3 holds at m. By §2 (c), B_t2 ⊔ S >lex B_t1 ⊔ S, so the top of the difference
  is in B_t2.
- (ii), the sandwich:
  - Ω_(t2−1)(a) ◁ Ω_(t2−1)(b) (§2 (b)) and Ω_(t2−1)(b) ⊴ Ω_t2(b) (F1). All three have Λ = w.
  - So, as in §2 (c), the three e-sets compare lexicographically on U_y.
  - E_(t2−1)(a) ∩ U_y = E_t2(b) ∩ U_y, since the top at v at t2 is y (§2 (c), last step).
  - A lex-sandwiched set agrees with the two equal ends on U_y. [If it differed from the lower end, its most relevant difference d in U_y
    would be in it; the upper end agrees with the lower end on U_y, so it would differ from the upper end first at d, with d in the middle
    set: middle > upper, a contradiction.]
  - So f ∈ E_(t2−1)(a) ∩ E_(t2−1)(b). The plays from a and from b at t2 − 1 both pass f, and from f on they are the same path (positional
    strategies, same state).
- (ii), the second split:
  - That common path does not contain y, because y ∉ E_(t2−1)(a).
  - At t2, y lies after f on b's play. So the play from f at t2 − 1 and the play from f at t2 differ.
  - Their first split is a vertex strictly after f and before y with a changed successor (Lemma SPLIT (i)). ∎
- Corollary RW-1 (PROVED). RW-WT holds at every re-win at which the only vertex of v's play before y whose successor changes at t2 is u
  ("single-split"). Such a vertex would have to lie on b's play after f, which is part of v's play. Counter rw_single (unit: re-win):
  these re-wins are proved, not sampled.
- Corollary RW-2 (PROVED). RW-B0 ⇒ RW-WT. RW-B0: at every re-win, B_t1 = B_t2 = ∅, i.e. b's route to y carries no U_y-letter.
  (B_t2 = ∅ already contradicts (i).)

### A1.3 CONJECTURE RW-B0 (DATA, three sources)
- Frozen set (box199/inst, 12 genomes incl. ROUTELOW_n21; split199.out):
  - Counters Bne_t1 and Bne_t2 (unit: re-win; must be 0) are 0 / 0 on 4,498 re-wins, of which 2,000 single-split (RW-1, proved) and 2,498
    multi-split. rwfail 0.
  - Control ctrl6 (Bne counted always) fires: 219 / 219 on CX4_n21.
- Random search, experiments/new/box199/srch199.py (unit: re-win; set: 4,000 genomes; scope: Γ3 engine up to the first fallback, cap
  3000 steps):
  - Sampling: 60 % are a base with 1-3 random options (bases CX4_n21, C2CX4_n23, GROW7_n34); 40 % are fresh random genomes (levels ≤ 3,
    4-12 movers, 1-3 options each).
  - Seed 8 (log srch199_s8.log, FINAL line): 315,065 re-wins, Bne_t1 0, Bne_t2 0, rwfail 0, rhfail 0, every SPLIT counter 0; ytopB_ne in
    21 genomes.
  - The committed srch199.py (importing split199) reproduces the scratch run's line «200 {…}» byte for byte. A seed-7 run (about 430
    genomes, stopped to add the Bne counters) also has rwfail 0.
- L-RED 61, independent engine (own.py, Γ without pads), relayed by the Lead 19:00Z: rw 0 on 2,994 re-wins / 19 genomes, plus a
  falsification climb (rw 0 at iteration 178). I have not opened 1ea37d91 yet.
- Sweep of all 286 distinct lane genomes (claude/l-red and claude/l-si inst dirs, box196/197 copies): running (tracked). 24 done at
  19:00Z, all must-be-0 counters 0. A later addendum completes it.
- Weight: strong DATA, no proof. The missing step is exactly RW-SHAPE's double split at a re-win: u returns to b at the same step at
  which a vertex after a high route letter f brings y.

### A1.4 What RW-WT + REWIN-COUNT + R121 give (the Lead's question)
- Corollary REWIN-ASC (PROVED CONDITIONAL on RW-WT; under HYPOTHESIS [E-LEV]; N5′-xi from S3 on Γ3(G) up to the first fallback;
  premises P-N5-CHAIN, R125 pending landing, incl. HUB-ASC-G3 and UP-B3, its Γ3 form of R121's HUB-ASC-G and UP-B; R121 itself is on
  IDEAL-CYC).
  - For every (v, I, y): R_y(v, I) ≤ SPL_y(v, I) · (F′_(U(G))(M) − 1) ≤ 3M · (F′_(U(G))(M) − 1). Here R_y := the re-wins of y,
    SPL_y := the distinct split pairs (u, b), and F′_B(M) := (M² + 3M + 1)(1 + M·F′_(B−1)(M)²), F′_0(M) := 1 + M(M + 1)/2 (P-N5-ASC §4).
  - Hence c_y(v, I) ≤ 1 + W_y(v, I) + 3M · (F′_(U(G))(M) − 1).
  - Proof.
    - Fix (u, b). Under RW-WT each of its re-wins changes E(m) ∩ U_y, m = wt(y), at a time where Λ(m) = w. So R_ub ≤ D_E,J(m) − 1,
      J := m's Λ-interval containing the span.
    - By UP-B3, seq_t(m) has ≤ U(G) ascents at every t. By HUB-ASC-G3, D_E,J(m) ≤ F′_(U(G))(M_w) ≤ F′_(U(G))(M).
    - A split pair is an edge leaving a mover (to its pad, M of them) or a gate (to a face, 2M), so SPL_y ≤ 3M. Sum over (u, b);
      REWIN-COUNT. ∎
- So (S5) is TRIVIAL: SPL ≤ 3M, polynomial. Box 199 §3 listed it as open; that was wrong, and is corrected here.
- What the bound buys:
  - For U(G) ≤ B fixed the re-win term is polynomial. But T3 is already polynomial in that class by Theorem CHAIN3 (box 196; under [E-LEV],
    CONDITIONAL on P-N5-END and P-N5-ASC §4), so REWIN-ASC adds NO new class.
  - For U(G) unbounded, F′_U is doubly exponential in U: no bound.
  - The open terms after RW-WT:
    - W_y, the non-re-win re-entries (S4), in every class;
    - the re-win term itself, when U is unbounded, i.e. the high-part values of the one vertex wt(y).
  - A per-letter gain over HUB-ASC-G3 would need D_E restricted to U_y at wt(y) to be polynomial: that is the hub problem again, at a
    lower vertex. READING: RW-WT localizes the re-win charge to a fixed vertex, which is the form a landed result can bite on, but the
    landed bound bites only for bounded U.

### A1.5 Next: (S4)
- Test case: L-RED 61's C-climb genome with wc (= W summed) 86 at N + M 307, to be frozen at its next commit. Its re-entries with a
  changed split pair are the GROW7 prefix pattern (§3): y is expelled by a letter before it, and re-enters under it by another route.
- Plan: per such re-entry, measure whether the new prefix letter's own Λ-interval or e-set changed (a charge to the PREFIX letter z, z ≻ y,
  before y).
- Tools: experiments/new/box199/split199.py (new counters Bne_t1, Bne_t2, rw_single, rw_multi, ytopB_ne; control 6) and srch199.py; record
  split199.out, check199.out, srch199_s8.log.

## Addendum 2 (L-NEW successor 66, 19:48Z by date -u; the (S4) step; L-RED 61 test cases claude/l-red ba6ac84c; Lead 19:34Z: «wc» is a total, per-letter W ≤ 3)
Answer: (S4) is UNNECESSARY.
- REWIN-HI and RW-SHAPE never use that the two y-tops are consecutive. Restated for any two y-tops through the same split pair, they bound
  c_y with NO W term (Lemma PAIR-SPLIT, Corollary SPLIT-COUNT, both PROVED).
- With the all-pairs form of RW-WT (CONJECTURE RW-WT*), every y-top of every (v, I) charges to the one vertex wt(y).
- What remains open is a recursion over an «ascent DAG». On data that DAG is much larger than the real counts.

### A2.1 Lemma PAIR-SPLIT (PROVED, lane; premises as §2)
Let t < t′ be ANY two y-tops of (v, I) whose splits (§1) are the same pair (u, b), and let a := u's successor at t′ − 1 (a ≠ b, since u
moves to b at t′). Then:
- (a′) Ω_(t′−1)(a) ▷ Ω_t(b);
- (b′) Ω_(t′−1)(b) ▷ Ω_t(b);
- (c′) E_t′(b) ∩ U_y >lex E_t(b) ∩ U_y.
Proof: §2's proof with (t1, t2) := (t, t′). Every step uses only what follows, and none uses that no y-top lies in between:
- σ_t(u) = b ≠ σ_(t′−1)(u), which gives a first departure s ∈ (t, t′ − 1]; for a gate, its two faces and Odd's choice at t;
- y ∈ E_t(b), y ∉ E_(t′−1)(a), and the top y at t′. ∎
- Corollary SPLIT-COUNT (PROVED). For each pair (u, b), the values E(b) ∩ U_y at the y-tops through it are pairwise distinct (c′). They
  lie in one Λ-interval J_b of b, since Λ(b) = w at each of them (F1, F2). Hence
      c_y(v, I) ≤ Σ_((u,b) ∈ SPL_y(v,I)) Dhi_y(b, J_b) ≤ 3M · max_b Dhi_y(b, J_b),
  with no W term: (S4) is not needed. The price is the factor SPL ≤ 3M and the move from v to the b's. In the abstract model this is no
  better than PAIR-HIGH.
- Corollary RW-SHAPE* (PROVED, same proof as A1.2 with any same-pair t < t′). If E(wt(y)) ∩ U_y is equal at t and t′, then b's play at t′
  has a U_y-letter f before y, and a second split after f at t′.
  - So RW-B0* (no U_y-letter on b's route at same-pair y-tops) ⇒ RW-WT*.
  - And RW-WT* holds at every same-pair couple whose t′-step is single-split.

### A2.2 CONJECTURE RW-WT* and what it gives
- RW-WT*: for any two y-tops of (v, I) through the same split pair, E(wt(y)) ∩ U_y differs.
- Corollary C-WT (PROVED CONDITIONAL on RW-WT*):
      c_y(v, I) ≤ Σ_(u,b) #values of E(wt(y)) ∩ U_y on the span of its y-tops ≤ 3M · Dhi_y(wt(y), J),
  J the Λ-interval of wt(y) (Λ(wt(y)) = w at every y-top, counter wlamfail 0). Hence C(y) := max_(v,I) c_y ≤ 3M · max_J Dhi_y(wt(y), J).
- Unrolled with PAIR-HIGH at wt(y): C(y) ≤ 3M · (1 + Σ_(z ∈ Z(y)) C(z)). Here Z(y) := the letters z ≻ y that lie in E_t(wt(y)) at some
  state (the «ascent DAG»; under [E-LEV] each edge needs an upward Ξ-edge on a play after y, by UP-JUMP3).
- With HUB-ASC-G3 / UP-B3 (R125 pending; the Γ3 form of R121), under [E-LEV]: C ≤ 3M · F′_(U(G))(M), and T3 via C-EQUIV.
  - That is polynomial for U(G) bounded, which CHAIN3 already covers: still no new class.
  - It replaces REWIN-ASC (A1.4) by a bound on all of c_y, with no W term.
- DATA (split199.py; unit: same-pair couple / (v, I, y); set: 15 instances = box199/inst incl. the L-RED W-cases; scope as §5):
  - rh2fail (PAIR-SPLIT) 0, rw2fail (RW-WT*) 0 on 6,771 same-pair couples; spfail (SPLIT-COUNT) 0, spwfail (C-WT's first inequality) 0.
  - Control ctrl4 (U_y := ∅): rh2fail 313, rw2fail 313, spfail 161, spwfail 161 on CX4_n21.
- DATA (zdag199.py; unit: genome; static Z over the whole run, all Λ): the ascent DAG is much larger than the real counts. Real
  max c_y is 2-5 everywhere.
| instance | letters | Z depth | Z fan-out | max paths P_Z |
| --- | --- | --- | --- | --- |
| CX4_n21 | 35 | 4 | 4 | 12 |
| GROW7_n34 | 86 | 6 | 6 | 32 |
| GROW8_n53 | 147 | 7 | 9 | 112 |
| HOLD3K_n125 | 252 | 6 | 8 | 47 |
| DSALT9_n416 | 801 | 6 | 9 | 90 |
| DU21_h4 | 419 | 5 | 19 | 366 |
| W68_n66 | 184 | 7 | 8 | 62 |
| W86_n77 | 230 | 6 | 10 | 102 |
  (all 15 rows in experiments/new/box199/zdag199.out.) So the static recursion, like RA-PATHS, is loose by one to two orders on these
  short runs. A useful bound must use the Λ-intervals and the time order, not the static DAG.

### A2.3 The W-cases on the padded engine (Lead's request, «report both counts»)
| instance (sha1) | N | M | T3 | re-entries | re-wins | non-re-win (Σ W) | max W_y | max c_y | max (u,b) | wcfail | lemma counters |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W86_n77 (d99b0b7e) | 77 | 230 | 19 | 913 | 478 | 435 | 2 | 5 | 2 | 159 | all 0 |
| W14_n75 (f22ae7d7) | 75 | 225 | 13 | 538 | 258 | 280 | 3 | 4 | 3 | 26 | all 0 |
| W68_n66 (6a8463f8) | 66 | 184 | 8 | 169 | 20 | 149 | 1 | 2 | 2 | 127 | all 0 |
- L-RED's own.py (Γ without pads) counts, relayed: W86 re-entries 493, re-wins 257, wc 86; W68 re-entries 91, re-wins 11, wc 68 (wc is L-RED's own total, relayed as such; I have not reconciled it with re-entries − re-wins). The padded Γ3 has
  more vertices v, hence more (v, I, y) triples. Per letter the two engines agree in shape: max W_y ≤ 3, max c_y ≤ 5.
- Copies: box199/inst/W86_n77.json, W14_n75.json, W68_n66.json (from claude/l-red ba6ac84c experiments/red/r227/inst; sha1 = its SHA1SUMS).
- Sweep record (Addendum 1 §A1.3, completed). All 286 distinct lane genomes; 281 finished in 600 s, every must-be-0 counter 0, Bne 0,
  rwfail 0 on 23,350 re-wins. The 5 timed out: H7C, H8A, H8C, HP7b_mup, HP8b_mup.

### A2.4 Status after box 199 (labels)
- PROVED (lane, P-N5-CHAIN facts only): SPLIT, TRANSFER, REWIN, REWIN-HI, PAIR-SPLIT, SPLIT-COUNT, RW-SHAPE(*), RW-1, RW-2.
- CONJECTURE: RW-B0 / RW-B0* (⇒ RW-WT / RW-WT*). DATA: about 346,700 re-wins over four sources (5,254 frozen + 315,065 search + 23,350 sweep + 2,994 L-RED), 0 fails.
- DEAD: downward charge below y (CX4_n21); W-target charge for all re-entries (GROW7_n34); W-target bound (HOLD2K_n84); ROUTE-LOW
  (ROUTELOW_n21); the product-chain idea (§4).
- OPEN core, in its sharpest form here: max_J Dhi_y(wt(y), J), the number of distinct high parts above y of ONE vertex wt(y).
  - Polynomial in N + M would give C polynomial (C-WT), hence T3 polynomial (C-EQUIV), on RW-WT*.
  - It is again a hub problem, at the lower vertex wt(y), for the letters above y.

## Addendum 3 (L-NEW successor 66, 20:23Z by date -u; Lead 19:58Z relays L-SI 47 BOX 90, claude/l-si 4ded1e8d: FW staircase family, RA-LOG and (S2) DEAD, «test Addendum 2's bound on FW4_2 / FW6_4 / FW8_4»)
- FW does not threaten Addendum 2's C bounds. Its large P comes entirely from distinct split pairs, of which there are at most 3M. The
  RW-WT* charge is trivial there.
- DATA (split199.py and zdag199.py; unit: (v, I, y) for the maxima, same-pair couple for rh2fail / rw2fail; set: the 7 FW instances of
  claude/l-si experiments/si/box90/inst, sha1 = its SHA1SUMS, copies in box199/inst; scope: N5′-xi from S3 on Γ3, up to the first
  fallback).
  - Every lemma counter is 0: playfail, kindfail, hwfail, gtfail, trfail, dnfail, rhfail, rwfail, Bne, rh2fail, rw2fail, spfail, spwfail.
  - T3 = 3d + 5 is reproduced.
| instance (sha1) | d, k | T3 | re-entries | re-wins | max c_y | max W_y | max (u,b) per (v, I, y) | Z depth / max P_Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FW4_2 (e583d437) | 4, 2 | 17 | 5 | 0 | 3 | 2 | 3 | 1 / 1 |
| FW6_3 (5c9090c1) | 6, 3 | 30 | 12 | 0 | 4 | 3 | 4 | 1 / 1 |
| FW6_4 (cc7e713c) | 6, 4 | 37 | 14 | 0 | 5 | 4 | 5 | 1 / 1 |
| FW8_2 (108a63cf) | 8, 2 | 29 | 13 | 0 | 3 | 2 | 3 | 1 / 1 |
| FW8_4 (3b81a63c) | 8, 4 | 47 | 22 | 0 | 5 | 4 | 5 | 1 / 1 |
| FW12_2 (f8801013) | 12, 2 | 41 | 21 | 0 | 3 | 2 | 3 | 1 / 1 |
| FW16_2 (94df42b7) | 16, 2 | 53 | 29 | 0 | 3 | 2 | 3 | 1 / 1 |
- READING:
  - On FW every y-top of a letter comes through a NEW split pair: no re-wins, and c_y = #split pairs = k + 1.
  - No letter above y ever lies on wt(y)'s plays (Z depth 1), so Dhi_y(wt(y), J) = 1.
  - Hence C-WT (A2.2) reads C ≤ SPL · 1 ≤ 3M, and is TIGHT here: max c_y = max SPL. SPLIT-COUNT likewise: each pair contributes 1.
  - The Fibonacci growth of P (RA paths) is invisible to these bounds. RA counts paths over the letters; SPLIT-COUNT counts split pairs
    (edges) times high-part values at the b's. That is the step from box 198's P (exponential on FW, so (S3) is false) to a C bound.
  - FW(d, k) gives C = k + 1 ≤ M: linear, not polynomial-breaking. The C-WT bound 3M · Dhi_y(wt(y)) has room for it.
- Consistent with L-SI's per-pair multiplicity m(y, z) ≤ 2 (relayed; CONJECTURE RA-MULT(K)): in SPLIT-COUNT's terms, a large c_y needs
  many split pairs or many high-part values at wt(y), not a deep RA.
- What a counter-family to C-WT must do (READING): make Dhi_y(wt(y), J), the number of distinct high parts above y of the one vertex wt(y),
  grow super-polynomially. That needs ascents after y (Z depth ≥ 2), which FW does not have.
- Records regenerated: split199.out, zdag199.out (22 instances); check199.out unchanged.

## Addendum 4 (L-NEW successor 66, 21:14Z by date -u; Lead 21:14Z: «PROVE RW-B0* … if RW-B0* resists, write exactly the missing step and stop»)
Verdict: RW-B0* is NOT proved. Below is what is proved toward it, and the one missing step.
- RW-B0* is not a property of a single y-top. ROUTE-LOW, the single-y-top form, is DEAD (A1.1). A proof must use both y-tops of the couple.
- PROVED (A1.2 / A2.1 with any same-pair t < t′). If RW-WT* fails at a couple (S_t = S_t′, S := E(wt(y)) ∩ U_y), then all of the
  following hold at once:
  - (F1′) some f ∈ U_y lies on b's play at t′ before y;
  - (F2′) at t′ − 1 the plays from a := u's successor and from b both pass f and coincide from f on, and that common suffix avoids y;
  - (F3′) E_(t′−1)(a) ∩ U_y = E_(t′−1)(b) ∩ U_y (the sandwich), so Ω_(t′−1)(b) ▷ Ω_(t′−1)(a) is decided strictly BELOW y, by the parts of
    the two plays before f: «u's return to b at t′ is LOW-REASONED»;
  - (F4′) at t′ a second vertex u′, strictly between f and y on b's play, changes its successor, and it is u′, not u, that brings y.
- THE MISSING STEP (to be proved, or killed by an instance): a same-pair return of u to b cannot be low-reasoned (F3′) while a vertex
  after a high letter f brings y at the same step (F4′).
  - Proving it gives RW-B0* (indeed RW-WT* directly). Then C-WT is unconditional on P-N5-CHAIN's premises:
        C(y) ≤ 3M · max_J Dhi_y(wt(y), J).
  - The ROUTELOW_n21 mechanism (A1.1) realizes (F2′) and (F4′) at an ISOLATED y-top. A kill must make the same happen at a second y-top
    through the SAME pair, with (F3′).
- Where a proof could start (READING, not done):
  - At t (the earlier y-top) u also moved to b. If f was already on b's route at t, then (F3′) at t′ compares the same two pre-f segments
    that u compared at t. But u left b in between because a′ became strictly better (STRICT), and the post-f parts have since changed
    in the same way for both.
  - A potential argument on the pre-f segments (their low parts are lex-monotone where Λ is fixed, E-MON3 at the segment's vertices) is
    the natural tool. I did not complete it.
- DATA unchanged: Bne_t1 = Bne_t2 = 0 and rw2fail = 0 on every instance and sample (A1.3, A2.2, Add. 3).

## Addendum 5 (L-NEW successor 66, 21:50Z by date -u; Lead 21:27Z relays L-SI 47 BOX 90 milestone 2 (MW family, claude/l-si 2d0344d3); Lead 21:37Z relays L-RED 62's kill of RW-WT / RW-WT* / RW-B0 / RW-B0* (claude/l-red 68639e7a, docs/red/R228-box199.md Addendum A))
### A5.1 DEAD: RW-WT, RW-WT*, RW-B0, RW-B0* (and C-WT's premise)
- Instance experiments/new/box199/inst/RWX_n95.json (sha1 da8b3a30; N 95, M 233; T3 12). Copy of claude/l-red
  experiments/red/r228/inst/RWX_n95.json. L-RED 62 checked its premises: R104 form, [E-LEV], S3 standard, all states standard.
- Re-run on my split199.py (this commit; the counters are unchanged from 42e9c728):
  - rwfail 31, Bne_t2 31, rw2fail 31, spwfail 31 (unit: re-win / same-pair couple / (v, I, y)). All 31 failures are at multi-split
    re-wins (rw_multi 31, rw_single 0).
  - Every PROVED-lemma counter is 0: playfail, kindfail, hwfail, gtfail, trfail, dnfail, rhfail, rh2fail, spfail, wlamfail, and the new
    rw1fail (RW-1: a failure at a single-split re-win).
- Witness (L-RED's ids): v = u = mover 17, b = 240, y = 764, wt(y) = mover 20, same-pair y-tops t 3 / t′ 6.
  - E(wt(y)) ∩ U_y = ∅ at both times, while E(b) ∩ U_y goes ∅ → {647}, and 647 lies on b's route BEFORE y.
  - So the forced rise of REWIN-HI is on the route, as RW-SHAPE allows: (F1′)-(F4′) of Addendum 4 all occur. The missing step of
    Addendum 4 is FALSE.
- Consequences:
  - Corollary C-WT and the A1.4 consequence REWIN-ASC lose their premise. They stand only as implications from a false conjecture.
  - RW-1 (single-split re-wins) and RW-SHAPE(*) SURVIVE; RWX_n95 is consistent with them.
  - C = 2 on RWX_n95: a reduction died, not polynomiality.
- C6G8_n54 (claude/l-red r228/inst, sha1 52067442, N + M 204): C = 6 (max c_y 6, max split pairs 2). All proved counters 0; RW counters 0
  there.

### A5.2 MW family (L-SI BOX 90 milestone 2; copies in box199/inst, sha1 = claude/l-si SHA1SUMS)
| instance (sha1) | T3 | re-entries = re-wins | max c_y (= 2n + 1) | at the argmax: split pairs | y-tops per pair | values of E(wt(y)) ∩ U_y | Z depth / fan / P_Z |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MW4_2 (7fc9f49f) | 31 | 152 | 9 | 1 | 9 | 9 | 3 / 5 / 10 |
| MW8_2 (66b84dcb) | 55 | 304 | 17 | 1 | 17 | 17 | 3 / 9 / 18 |
| MW16_2 (2fce5fd9) | 103 | 608 | 33 | 1 | 33 | 33 | 3 / 17 / 34 |
| MW32_2 (445031d1) | 199 | 1,216 | 65 | 1 | 65 | 65 | 3 / 33 / 66 |
- Every lemma counter is 0. Here the RW counters are 0 too (rw2fail 0 on 30,304 same-pair couples at MW32_2), and W = 0: every
  re-entry is a re-win through ONE split pair.
- So on MW, SPLIT-COUNT is TIGHT through the high parts of b (Dhi_y(b) = c_y with one pair), and the high parts of wt(y) also grow, 2n + 1.
  FW grows the split pairs; MW grows the high parts at one pair. Both are linear in n with T3 linear: the bounds hold, nothing breaks.
- Argmax tool: a scratch variant of split199.py recording (c_y, SPL, per-pair maximum, values of E(wt(y)) ∩ U_y) at the max (v, I, y).
  It is not committed; its numbers are in the table above.

### A5.3 What survives, and the open core now
- PROVED (lane, P-N5-CHAIN facts, R125 pending), all SURVIVE L-RED 61 / 62: SPLIT, TRANSFER, REWIN, REWIN-HI, PAIR-SPLIT, SPLIT-COUNT,
  RW-SHAPE(*), RW-1.
  - L-RED checked line by line that consecutiveness is unused.
  - SPL ≤ 3M = M mover edges + 2M gate faces holds because β_g, K0, K1, K3 are frozen in HOW3 (F6, (Core)).
- The surviving C bound is SPLIT-COUNT:
      c_y(v, I) ≤ Σ_((u,b) ∈ SPL_y(v,I)) Dhi_y(b, J_b) ≤ 3M · max_b Dhi_y(b, J_b),
  b ranging over the successors at split vertices, i.e. the first vertices of y-routes.
- OPEN CORE, sharpest form: the number of distinct high parts (e-letters above y) of the ROUTE vertices b, on one Λ-interval.
  - These are vertices on v's play just after a split. Their high parts can change on the route before y (RWX_n95) or at wt(y) (MW).
  - A polynomial bound on max over y, b, J of Dhi_y(b, J) gives C polynomial, hence T3 polynomial (C-EQUIV).
  - It is not a reduction to one fixed vertex per letter: that form (C-WT) is DEAD.
