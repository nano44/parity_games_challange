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
