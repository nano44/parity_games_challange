# N5-RET (box 98): what pays for a RETURN of the head order / type inside a W-run? A fresh Even entry or an Even-edge RETURN, by box 92's TRIPLE-RED split. On gate_K and pp_K every order return is paid by fresh entries (no Even edge is re-entered, so |F| ≤ m_E − n_E). On the quadratic pins (sbq2, obs, latew) no head order ever returns: their length is Even-edge returns (RET ≈ 0.9|F|). So head-type returns are not the bottleneck; Even-edge returns are, and those are XI-CH-POLY again (RET-ΞRISE)
L-NEW successor 40 (Opus 5.5), D14 / D18, Lead reading L40. Lead 20:42Z: «BOX 98, your choice … My suggestion: the head-type RETURNS charge,
the one missing piece L-LIT T61 names («a bound needs a charge for RETURNS of the head type; no opened source supplies one»). On gate_K64,
34 types and 31 returns: what pays for a type return?» Written 2026-10-30 20:50Z-21:0xZ (date -u). Working note, unrefereed. Labels: PROVED
(lane) / DATA / READING. Not a TARGET.md claim. G-N5-TIME stays OPEN; no W-run count is bounded here.

## 0. Sources, setting
- L-LIT T61 (l-lit 1ad851ee, docs/lit/T61-order-charging.md; read from origin/claude/l-lit, not on trunk) §2.6 (S5a): «gate_K64_n581 has 5
  distinct head orders and 60 returns (34 types, 31 returns) in a 71-transition W-run with 64 σ̄-changing transitions»; finding 4: «NO-REPEAT
  must be replaced by a charge for type RETURNS».
- Box 97 (docs/new/N5-ORD-box97.md): A_F, the refined order on A_F, ORDER-DET-R, FLIP-ORD (SBT_F ≤ ORDCH_F + XCN_F).
- Box 92 packet P-N5-WRUN §4 (R95 draft, line L-5), as signed by both referees:
  - TRIPLE-RED «|F| ≤ m_E + Σ_{(X′, g′)} RET_F(X′, g′)»;
  - RET-ΞRISE «RET_F(X, g) ≤ ΞCH_F(g)»;
  - «a return of X to g is a transition of F at which X enters g having held g at an earlier state of F».
- Tool: experiments/new/box98/retpay.py (W-runs, U_k, A_F and the refined order as box97/orderdet.py). Driver: box98/runret.sh (box 50b's
  corpus + the three box-97 pins). Outputs: box98/ret_sbcg.txt, ret_alt.txt, ret_pins.txt (one line per W-run). Pin: new/check.sh «box 98 RET».
- An ORDER RETURN here is a transition k → k + 1 of F at which the refined order of A_F becomes an order seen at an earlier state of F
  (other than k). This is box 97's datum, not T61's ordered-ultrametric type on U_k, so the counts differ from T61's: gate_K64 has 59 order
  returns here and 31 type returns in T61. The charge in §1 does not depend on which datum is used.

## 1. Lemma PAY (PROVED, lane; elementary, the first inequality of TRIPLE-RED made per transition)
- Definitions, for a W-run F = [a, b]:
  - an ENTRY is an Even vertex y switching to z at a transition of F;
  - the entry is a RETURN if y held z at an earlier state of F, and FRESH otherwise;
  - RETT_F := the transitions of F with at least one return. Then RETT_F ≤ Σ_{(X, g)} RET_F(X, g).
- Statement:
  - every transition of F that is not in RETT_F has a fresh entry;
  - there are at most m_E − n_E transitions with a fresh entry;
  - so every count of transitions of F, in particular head-order returns, head-type returns (T61) and σ̄-changing transitions, is at
    most |F| ≤ (m_E − n_E) + RETT_F.
- Proof.
  - Every transition of a W-run switches some Even vertex (P-N5-SETTLE §1: τ fixed and no S4c fallback, so S4a changed σ). A transition
    not in RETT_F therefore has an entry, and that entry is fresh.
  - A fresh entry (y, z) has z ≠ σ_a(y). It is fresh only once in F, because afterwards y has held z.
  - Distinct transitions have distinct fresh edges. So the transitions with a fresh entry number at most the number of Even edges other
    than the n_E edges of σ_a, which is m_E − n_E. □
- With RET-ΞRISE: |F| ≤ (m_E − n_E) + Σ_{(X, g)} ΞCH_F(g). This is box 92's XI-RUN up to the constant, so PAY adds no new reduction. What it
  adds is the ANSWER to the brief: a head-type return is paid by a fresh Even entry (at most m_E per W-run) or by an Even-edge return.
  Nothing else is needed.

## 2. DATA: which payer is used
| instance | n | |F| | m_E | fresh-entry transitions | RETT_F (transitions with an Even return) | order returns (refined, A_F) | σ̄-changing transitions | |A_F| |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gate_K16_n197 | 197 | 23 | 351 | 23 | 0 | 11 | 16 | 11 |
| gate_K64_n581 | 581 | 71 | 1119 | 71 | 0 | 59 | 64 | 11 |
| pp_K12_n161 | 161 | 19 | 279 | 19 | 0 | 9 | 14 | 15 |
| pp_K48_n449 | 449 | 55 | 855 | 55 | 0 | 45 | 50 | 15 |
| sbq2_K8_m16 (R145) | 261 | 152 | 115 | 33 | 120 | 0 | 144 | 113 |
| obs_K12_m24 | 272 | 324 | 149 | 49 | 289 | 0 | 1 | 97 |
| latew_K16_m32 | 482 | 560 | 227 | 65 | 496 | 0 | 513 | 191 |
- gate_K and pp_K never re-enter an Even edge inside the W-run.
  - Every order return there, and every σ̄-change, is paid by a fresh entry. |F| ≤ m_E − n_E.
  - Their linear growth in K is edge CONSUMPTION: m_E grows with K. It is not recurrence.
  - So T61's 31 type returns on gate_K64 are paid by 71 distinct fresh Even edges.
- The quadratic pins have NO order return at all.
  - Their length is Even-edge returns: RETT_F / |F| = 0.79 (sbq2), 0.89 (obs), 0.89 (latew).
  - The remaining transitions (32-65) are fresh, as PAY says.
- Corpus (runret.sh, 1,695 W-runs, 0 timeouts; run 2026-10-30 20:5xZ):
  - 469 order returns in 141 W-runs.
  - 201 of them lie in 39 W-runs with no Even return at all (paid by fresh entries alone).
  - In 81 W-runs, every order return's interval (since the previous occurrence of that order) contains an Even return.
  - 17 order-return intervals contain no fresh entry; they are paid by Even returns only.
  - PAY's split holds on every W-run: |F| ≤ fresh-entry transitions + RETT_F (0 violations), and the fresh-entry transitions ≤ m_E (0
    violations).

## 3. Reading (what this says about the open core)
- PROVED (lane, §1): a charge for head-type returns exists, and it is TRIPLE-RED's: fresh Even entries (≤ m_E − n_E) plus Even-edge returns.
  Type returns cost nothing beyond what |F| already costs.
- DATA (§2): the two phenomena are disjoint on every extreme family seen.
  - Order / type returns occur where Even edges are only consumed: gate, pp, fcobs. fcobs mixes the two (e.g. fcobs_6: 36 order
    returns, RETT 26).
  - Long W-runs (sbq2, obs, latew) occur where Even edges RETURN and the head order never recurs.
  - So a bound on type returns would neither be necessary for WRUN-POLY (gate_K is linear anyway) nor sufficient (latew is quadratic
    with zero type returns).
- The missing charge is therefore NOT for type returns. It is for Even-edge returns: RET_F(X, g) ≤ ΞCH_F(g), i.e. XI-CH-POLY. Box 92 split
  that further into REG (self-routed block, ≤ the routes' WAIT-CYCLE′ count) and FREE returns.
- The quadratic pins put the open quantity in Even-edge returns at a few targets g, each re-entered once per Ξ-rise of g. That is L-RED
  R145's / R143's mechanism, not a head-order mechanism.
- READING (D18, no source opened): in matroid / greedy-exchange terms, gate_K is a «basis-exchange walk» that uses each element once, so it
  is linear in the ground set. The hard instances re-insert elements, and in the exchange literature only a potential (here Ξ, ordinal
  with 2^Θ(n) values) pays for a re-insertion. That is the same wall as XI-CH-POLY.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box98/ (retpay.py, runret.sh, ret_sbcg.txt, ret_alt.txt, ret_pins.txt); new/check.sh «box 98 RET».
  SHA: see the commit.
- FINDINGS:
  - Lemma PAY: PROVED (lane, elementary). Every transition of a W-run has a fresh Even entry or an Even-edge return, so head-type returns
    are ≤ |F| ≤ (m_E − n_E) + RETT_F.
  - DATA: on gate_K / pp_K every order return is paid by fresh entries (RET 0, |F| ≤ m_E − n_E). On sbq2 / obs / latew there are 0 order
    returns and RETT_F ≈ 0.8-0.9 |F|.
  - READING: the missing charge is for Even-edge returns (XI-CH-POLY via RET-ΞRISE), not for head-type returns. T61's gap is closed by
    TRIPLE-RED.
- NEEDS: none from the owner.
