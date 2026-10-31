# R2-N5-ROOT114: REFEREE-2 report on P-N5-ROOT (box 114): DESC-ROOT, ROOT-STAIR, ORIGIN-NEW, RELAY, NEW-FUEL, ROOT-SPLIT, FUEL-ROOT-STAIR
Referee: REFEREE-2 successor 25 (session_01V5yGRaPp26T6iMUpCRmXsW), Opus 5.5 (D15).
Written 2026-10-31 18:4xZ (date -u). Name: R2-N5-ROOT.md already exists (successor 17, the older L-SI packet P-N5-ROOT-box20).
Independence: written without opening docs/referee/ (REFEREE's d8a2f428) or docs/new/P-N5-ROOT-fixes-box114.md (c4279144).
I read both only after this report is pushed.

## 0. Object
- docs/new/P-N5-ROOT-box114.md at l-new ed2fdaf2: sha1 f06f493ebd31e886517959abb13f7724f2e2f819, 158 lines. Re-hashed: match, and the
  file is the same at l-new head a82e7c55.
- Line draft docs/new/P-N5-ROOT-line.txt at ed2fdaf2: sha1 954af7be0e7771edade79a5f5e936e4ab46bcbda. Re-hashed: match.
- Premises opened, at the commits named:
  - P-N5-STAIR (l-new 9a58765f, docs/new/P-N5-STAIR-box112.md) §1 and §6: COPY with the fixed map π_v; C constant.
  - P-N5-ODD (l-si 0afc0d70a, docs/si/P-N5-ODD-box57.md) §6: the fuel re-route definition, FUEL-LEX and FUEL-COUNT N ≤ n(n + 2)(HC + n).
  - RESULTS R15 (a), (b), (d) (docs/RESULTS.md l. 624): Lemma A is for any non-empty unambiguous set of improvements. Lemma B's equality
    case forces Λσ(v) = v. Under (d), every N5 iteration switches Even only along edges of Iσ.
  - RESULTS R89 (W-run), R91 (W-MON, and OPT-OFF), R93 (LEX).

## 1. Claims table
| § | claim | verdict | note |
| --- | --- | --- | --- |
| §2 | Lemma DESC-ROOT (walk, x_j ∉ C, descent at k with previous change k′, type R/T/S, j = 0 if not COPIED; DESC_F ≤ n(R + T + S), T ≤ TS) | **SIGNED** | §3.1 |
| §3 | Theorem ROOT-STAIR (|F| ≤ T1 + n(3n + 1) + (3n + 1)n(R + S + TS); R + S ≤ n·WCT; TS ≤ n|F|; the equivalence) | **SIGNED** | §3.2 |
| §4 | Lemma ORIGIN-NEW (origin root change, k − 1 ∈ F ⇒ (y, z) ∉ H_(k−1), so (y, z) ∈ Iσ_k \ Iσ_(k−1)) | **SIGNED**, for k → k + 1 a transition of F (the packet's §1 setting) | §3.3. As the LINE words it (k unbound), it is FALSE: ROOT114-L1 |
| §4 | Corollary RELAY | **SIGNED** (same reading) | contrapositive of ORIGIN-NEW |
| §5 | Lemma NEW-FUEL | **SIGNED** | §3.4. It even holds with k unbound (P-1) |
| §5 | Corollary ROOT-SPLIT | **SIGNED**, for k a transition of F | as worded in the line, it is FALSE at k = q (ROOT114-L1) |
| §6 | Corollary FUEL-ROOT-STAIR | **SIGNED** | §3.5. Conditional on [FUEL-COUNT] and on [COPY] / [STAIR], which both referees signed and which have not landed yet |

No claim is FALSE as the packet states it. There is no gap in the packet.

## 2. Gap map
| id | where | kind | status |
| --- | --- | --- | --- |
| ROOT114-L1 | line: ORIGIN-NEW, ROOT-SPLIT (and the root-change definition) | **REQUIRED**: k is not bound to a transition of F; the statements are false at k = q | open (line) |
| ROOT114-L2 | line: premise «P-N5-STAIR … as in its line L-1, docs/new/P-N5-STAIR-line-L1.txt» and «β … descents and DESC_F as in P-N5-STAIR's line L-1» | **REQUIRED**: L-1 is superseded. Both referees required STAIR-L1-1 there (v, b unbound in COPY …); cite line L-2 (l-new 6903f1b3, sha1 44f56e96), or R-number once landed | open (line) |
| P-1 | §5 proof, «S4a picks σ_(k+1)(y) in H_k(y)» | precision | optional |
| P-2 | §4 proof, step 1 | precision: it is RESULTS R91 Lemma OPT-OFF, already landed | optional |
| P-3 | line: HC_F | precision: «the last fuel re-route of (y, z) at a transition ≤ u» (FUEL-COUNT's words) is shortened to «the last fuel re-route» | optional |
| P-4 | packet §1 / line: [FUEL-COUNT] | cite P-N5-ODD by its landed R-number (R98 draft at C108) or its current line, once landed | optional; Lead decides |

### ROOT114-L1 (REQUIRED): bind k
- Line text: «a ROOT CHANGE is a pair (y, k) with y switching at k and W(y) changing at k …; (Lemma ORIGIN-NEW) if (y, k) is an origin root change
  and k − 1 ∈ F, then (y, σ_(k+1)(y)) ∉ H_(k−1); … (Corollary ROOT-SPLIT) every root change (y, k) with k − 1 ∈ F is a fuel re-route or a
  relay entering by an edge of H_(k−1)».
- Here F = [p, q] is a set of states. With k = q, the state k − 1 = q − 1 lies in F, but the transition q → q + 1 is not a transition of F.
  It is the cut: an S4c fallback, a λ_W change, or a τ change.
- The proof needs k → k + 1 in F three times: W-MON (W_(k+1) ⊵ W_k), C fixed at k + 1, and λ_W(y) fixed at k + 1.
- Counterexample: experiments/new/box113/inst/w_re3_1.pg (sha1 c59735b4…) with its start w_re3_1.start (3614ad94…), at l-new ed2fdaf2.
  - The W-run is F = [2, 6]. Transition 6 → 7 is an S4c fallback (τ unchanged, λ_W unchanged).
  - k = 6, y = 12, z = 29: σ_5(12) = σ_6(12) = 22 and σ_7(12) = 29.
  - W(12): (11, 201465856, 4) → (11, 218234880, 4), a change. W(29) = (11, 218103808, 3) at states 5, 6 and 7, so the root change is an origin.
  - k − 1 = 5 ∈ F, and (12, 29) ∈ H_5.
  - So ORIGIN-NEW as worded fails. ROOT-SPLIT as worded fails too: the change is not a fuel re-route (the edge is old) and not a relay.
  - Evidence: docs/referee-2/R2-N5-ROOT114/bnd.py, logs/bnd_w_re3_1.txt, and pins.txt (lines «EX BND_ONEW_FAILS_fb … w_re3_1 …@6»).
- Size of the problem: there are 2,977 such boundary origins with an old edge on the corpus (logs/corpus_totals.txt: BND_ONEW_FAILS_fb
  2,394, BND_ONEW_FAILS_lamW 583) and 42 on the pins.
- Fix (wording only; the packet's proofs are unchanged): define a root change as a pair (y, k) with k → k + 1 a transition of F, y switching at k
  and W(y) changing at k. Equivalently, write «if k → k + 1 is a transition of F, k − 1 ∈ F and (y, k) is an origin root change» in
  ORIGIN-NEW, and «every root change (y, k) at a transition k → k + 1 of F with k − 1 ∈ F» in ROOT-SPLIT.
- The packet itself should say the same in §4. Its §1 («every transition is an S4a step») is the reading under which I sign.

### P-1 (optional): NEW-FUEL holds with k unbound
- The proof's first step uses S4a's arena at k. RESULTS R15 (d) gives the same thing at every N5 iteration: Even switches only along Iσ_k.
- The Claim needs Ξ_k ⊵ Ξ_(k−1) and, if y switched at k − 1, (y, z0) ∈ Iσ_(k−1). Both come from R15 (a), (d) at any iteration: at a pure-τ
  step σ is unchanged, so Ξ_σ is too.
- So NEW-FUEL is true as the line words it, even at k = q. This is consistent with the data: 833 new-edge switches at the transition leaving
  a W-run (BND_newedge_*), and 0 NEW-FUEL failures among them.
- No change is needed. If ROOT114-L1 binds k for the whole line, NEW-FUEL is covered either way.

## 3. Review notes per claim

### 3.1 DESC-ROOT
- For i < j, x_i ∉ C and x_i switched at no transition of [k′, k]. So s_t(x_i) = x_(i+1) for every state t ∈ [k′, k + 1]: Odd vertices
  follow the fixed τ, and Even vertices are unswitched.
- So COPY applies to every pair (x_i, x_(i+1)) at every transition of [k′, k]. COPY's π_v is fixed by v's own rank bit and the parity of
  λ_W(v), which is constant on F (STAIR §6: «the same direction for all j»).
- So the composite π is the same at k′ and at k. That is the point the strict inequality q_k(x_j) > q_(k′)(x_j) needs, and it holds.
- The walk reaches λ_W(v) ∈ C. Vertices before it on the (σ_(k+1), τ)-play are not cycle nodes: their cycle node is λ_W(v), and λ_W is fixed
  on F. So j exists, and x_j ∉ C because C-values are constant.
- The counting is right:
  - For fixed (x, k) the descents mapped to it have distinct v, so there are at most n.
  - A T-descent's tie switch lies in the open window (k′, k), and the windows of one vertex are disjoint, so the map is injective.
  - My tool builds that injection explicitly (check DCNT).
- The type classification R / T / S / COPIED is exhaustive and exclusive.

### 3.2 ROOT-STAIR
- The forward bound: [STAIR] gives |F| ≤ T1 + n(3n + 1) + (3n + 1)·DESC. Then DESC ≤ n(R + T + S) ≤ n(R + S + TS).
- The converse: R + S ≤ DESC ≤ n·WCT ≤ n|F|, TS ≤ n|F|, and T1 ≤ |F|.
- Both directions are polynomial, so the equivalence holds.

### 3.3 ORIGIN-NEW (checked with special care, as the Lead asked)
- Let k → k + 1 be a transition of F with k − 1 ≥ p. Then transition k − 1 → k is an S4a step of F, with τ_(k−1) = τ.
- G′ := H_(k−1) with Odd fixed to τ. σ_k is an Even strategy of G′, since σ_k(y) ∈ H_(k−1)(y). Its valuation in G′ is W_k, and by
  [1E-N3] it is pointwise optimal in G′.
- **The cycle-node exception.** The known failure («a maximum has no improvement» is false at own cycle nodes) is exactly R15 (b)'s equality
  case, Λσ(v) = v.
  - Here Λ_(σ_k)(y) in G′ is the cycle node of W_k(y), which is λ_W(y). λ_W is fixed on F.
  - y ∉ C, because W(y) changes at k and C-values are constant (COPY's last clause). So y is not its own cycle node.
  - So an improvement (y, z) of σ_k in G′ would give Ω′ ⊵ W_k by R15 (a) and Ω′ ≠ W_k by R15 (b), against optimality.
  - This is RESULTS R91 Lemma OPT-OFF verbatim («a pointwise-optimal Even strategy ρ has Ω_ρ(c) ⊴ Ω_ρ(ρ(v)) for every edge (v, c) at every
    Even v that is not its own Ω_ρ-cycle node»), applied to G′ (P-2).
  - The argument also uses that (y, z) is an edge of G′, which is the hypothesis being refuted. Switch_{(y,z)}(σ_k) stays in G′.
- **Is a root change ever at C?** No. C is the set of own W-cycle nodes on F, and they never change value on F. The packet uses this
  correctly: the root vertex y has a W-change, so y ∉ C.
  - The packet does not need «z ∉ C». z may be in C; then W(z) is constant and the change is an origin, which is fine.
- **The Φ step.** s_k(y) = z0 and s_(k+1)(y) = z, and y is not the cycle node, so y is in neither path set: W_k(z0) and W_(k+1)(z).
  - Reason: the play from the successor reaches λ_W(y) before it could return to y. This holds even when y lies on the cycle.
  - Both values have cycle node λ_W(y), so Φ(y; ·) is order-preserving on them (the ⊕-reflection caveat «y in exactly one path set» from my
    WRUN / SETTLE notes does not arise).
  - Using W_(k+1)(z) = W_k(z) (origin) and the [LEX] linearity step, W_(k+1)(y) ⊴ W_k(y). Then W-MON gives equality, which is a
    contradiction.
- (y, z) ∈ Iσ_k: z ∈ H_k(y) and z ≠ σ_k(y). (y, z) ∉ Iσ_(k−1): it is not in H_(k−1).
- Data: OPTOFF (the optimality consequence, on every Even y not in C and every edge of H_(k−1)): 695,167 checks, 0 violations. ONEW: 0
  violations on 25,679 origin root changes with k − 1 ∈ F.

### 3.4 NEW-FUEL
- Each step is right:
  - (y, z) ∈ Iσ_k, because S4a picks in H_k(y) (or by R15 (d) in general, P-1).
  - Ξ_(k−1)(z) ⊴ Ξ_(k−1)(z1): z ≠ z1 and (y, z) ∉ Iσ_(k−1), with [LEX] linearity.
  - The Claim Ξ_k(z0) ⊵ Ξ_(k−1)(z1) holds in both cases.
  - Then Ξ_k(z) = Ξ_(k−1)(z) would give Ξ_k(z) ⊴ Ξ_k(z0), against ▷.
- The conclusion together with the hypotheses is P-N5-ODD §6's fuel re-route definition, word for word.

### 3.5 ROOT-SPLIT and FUEL-ROOT-STAIR
- An R-descent (x, k) has k′ ≥ p and k′ < k, so k − 1 ∈ F. It is a root change. So it is either new-edge (a fuel re-route, by NEW-FUEL)
  or old-edge (a relay, by RELAY). R = R^fuel + R^old.
- (y, k) ↦ a fuel re-route of (y, σ_(k+1)(y)) at k is injective, so R^fuel ≤ Σ N_F.
- [FUEL-COUNT] as signed: N ≤ n(n + 2)(HC + n), with HC FUEL-COUNT's HC, which the packet copies exactly. Substituting into §3 is
  arithmetic.
- Restricting the sum to pairs with N ≥ 1 is harmless: only those terms are needed for the first inequality.

## 4. Pins and DATA, re-run with my own code
- Tool: docs/referee-2/R2-N5-ROOT114/root_check.py.
  - It runs on my R2-N5-LATEP N5 loop and R89 W-runs, with my R2-N5-WRUN start reader (validated starts). β is from STAIR §5.
  - The lane's box113/*.py is not imported.
  - Checks: DROOT, DCNT, RSTAIR, RCC, ONEW, OPTOFF, NFUEL, RSPLIT, FRS. Boundary probes BND_* cover the transition leaving each W-run.
- Corpus: L-SI box 53's 1,132 games = sbcg.lst (runs=1) + alt_all split into with-start (94, runs=0) and start-less (319, runs=1).
  - Logs: logs/sbcg.txt, alst.txt, alns.txt; totals in logs/corpus_totals.txt. RESULT PASS, 0 violations, in all three.

| quantity | packet §7 | mine |
| --- | --- | --- |
| W-run transitions | 14,028 | 14,028 |
| DESC / R / S / T / COPIED | 14,755 / 7,606 / 932 / 1 / 6,216 | 14,755 / 7,606 / 932 / 1 / 6,216 |
| TS | 397 | 397 |
| DESC-ROOT misses | 0 | 0 (14,755 walks; 6,216 with j > 0) |
| origin root changes (k − 1 ∈ F), ORIGIN-NEW violations | 25,679, 0 | 25,679 (30,488 − 4,809 at k = p), 0 |
| new-edge switches (k − 1 ∈ F), NEW-FUEL violations | 27,539, 0 | 27,539, 0 |
| R^old | 47 | 47 (R^fuel 7,559) |

- Pins (logs/pins.txt, pins_each.txt, run on the l-new ed2fdaf2 files):

| pin | lane check.sh «box 113» | mine |
| --- | --- | --- |
| frz32 | NFSW 44, ORIGCH 44, RD_K1 21, RD_OLDEDGE 3, RD_NEW 18 | NEWEDGE 44, origins after p 62 − 18 = 44, R 21, R^old 3, R^fuel 18 |
| lcount2_n23 | NFSW 5, ORIGCH 4, RD_K1 1, DR 1 DT 1 DS 1 | 5, 8 − 4 = 4, R 1, T 1, S 1 (TS 1) |
| cp_K4 | NFSW 3177, ORIGCH 3177, RD_K1 388, DESC 388 | 3177, 3275 − 98 = 3177, R 388, DESC 388 |
| w_re3_1 | DR 11 DT 0 DS 2 | R 11, T 0, S 2 (R^old 2: the packet's «w_re3_1 has 2») |
| hit_b6a_1 | DR 17 DT 0 DS 1 | R 17, T 0, S 1 |
| fbg_K4_m6_m48 (fixed start) | DESC 640 = 430 copies + 210 R, all fuel | DESC 640, COPIED 430, R 210 = R^fuel 210, R^old 0 |

- frz32's 3 old-edge relay R-descents (§7 DEAD (a)) are reproduced. lcount2_n23's T-descent (§7 DEAD (b)) is reproduced.
- I did not re-run cp_K4 as DEAD (c) (the witness-set U); it is outside what is to be signed.
- Oink: scripts/setup_oink.sh (8fbf0a7) built here, exit 0. The tool is docs/referee-2/R2-N5-ROOT114/oink_pins.py, log
  logs/oink_pins.txt.
  - It runs `oink --zlk -v` on each pin, and Oink reports «verified» on every one.
  - Its regions equal N5's final regions (from my loop) on every pin: w_re3_1, hit_b6a_1, frz32, lcount2_n23, cp_K4, and fbg on both start
    files. On fbg the two start files give identical counts.
- The tool bites: the BND probes find the 2,977 corpus and 42 pin boundary failures of ORIGIN-NEW-as-worded (ROOT114-L1). So ONEW is not
  vacuous.

## 5. Line diff against TARGET.md scope words
- Subject: «N5 on EVERY game» uses TARGET §1's games and n := |V|. No polynomial bound, no algorithm claim, no unit-cost arithmetic.
- The tail says «REDUCTIONS and EQUIVALENCES (no count is bounded here; …; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md
  claim)».
- This is consistent with TARGET §2 (M4 untouched) and §4 (nothing is presented as M3/M4). The DEAD clauses name their instances.
- There is no asymptotic word («O(1)», «linear», «unbounded») backed only by fixed pins. That was the lesson of SRC-L5, and I checked for it.
- There is no referee-originated proof (L41), so no «referee-originated» tag is needed. If ROOT114-L1 is fixed by wording only, that stays true.
- Binder pass, clause by clause:
  - F, p, q, k, k′, v, x_j, y, z: all bound except k in the root-change clauses (ROOT114-L1).
  - (y, z) in NEW-FUEL, N_F, HC_F: bound.
  - The sums: bound («over Even edges (y, z) with N_F(y, z) ≥ 1»).
- The premise list matches the packet's §1, except the STAIR line version (ROOT114-L2).
- Verdict on the line: **REQUIRED** (ROOT114-L1, ROOT114-L2). Then a word-diff of the revision.

## DONE / FINDINGS / NEEDS
- DONE: this report; the tool docs/referee-2/R2-N5-ROOT114/{root_check.py, oink_pins.py, bnd.py}; logs/; the corpus and pins re-run; Oink
  zlk verified on 6 pin games.
- FINDINGS:
  - DESC-ROOT, ROOT-STAIR, ORIGIN-NEW, RELAY, NEW-FUEL, ROOT-SPLIT and FUEL-ROOT-STAIR are all SIGNED (Opus 5.5, D15). There is no gap in
    the packet.
  - ORIGIN-NEW's use of R15 A / B is sound: y ∉ C, because W(y) changes and C-values are constant, so y is never an own cycle node. It
    equals R91 OPT-OFF.
  - Line ROOT114-L1 is REQUIRED: k is unbound. ORIGIN-NEW and ROOT-SPLIT as worded are false at the transition leaving F (w_re3_1, k = 6,
    y = 12, z = 29, S4c fallback).
  - Line ROOT114-L2 is REQUIRED: cite STAIR line L-2, not the superseded L-1.
  - NEW-FUEL holds even with k unbound, via R15 (d) (P-1).
  - The packet's DATA and pins are reproduced exactly.
- NEEDS: Lead: route ROOT114-L1 and L2 to L-NEW for line L-1. Send me the word-diff when it exists.
