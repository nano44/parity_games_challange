# R-N5-ODD: REFEREE report on packet P-N5-ODD (L-SI box 57): OLD-PLAY, NO-RET / ODD-STEP, ODD-RELAY / ODD-ADD, SRC-ROOT, FUEL-LEX / FUEL-COUNT
Referee: REFEREE (successor 21), Opus 5.5 (D15). Lead brief 2026-10-31 12:40Z (read 12:38Z by date -u). REFEREE-2 reviews independently.
- Object and pin: docs/si/P-N5-ODD-box57.md at claude/l-si 0afc0d70a. `git show 0afc0d70a:<path> | sha1sum` =
  03eec41d3bfc63a6945d0f30d831a46f14e46b84 (146 lines). The line docs/si/P-N5-ODD-line.txt has sha1
  cd121dffd06dbc794f3154e34aa238d8df81f837. Both equal the Lead's figures.
- Independence: I opened no docs/referee-2/ file for this packet.
- Scope (D1): a RELOCATION. No count is bounded. G-N5-TIME stays OPEN. Not a TARGET.md claim.
- Every verdict below is labelled (Opus 5.5, D15).

## Verdicts
| § | item | verdict |
| --- | --- | --- |
| 1 | premises; Φ and (Φ-comp) | CHECKED (§1). [PLAY] is verbatim from P-N5-SRC §2, the signed proof of R97 (N-ODD-1) |
| 2 | Lemma OLD-PLAY | SIGNED |
| 3 | Lemma ODD-STEP, Case I and Case II = Lemma NO-RET (all sub-cases) | SIGNED |
| 4 | Lemma ODD-RELAY; Corollary ODD-ADD | SIGNED |
| 5 | Corollary SRC-ROOT | SIGNED |
| 6 | Lemma FUEL-LEX | SIGNED, with proof-text gap G-ODD-1 closed here (§6). The statement is unaffected |
| 6 | Corollary FUEL-COUNT | SIGNED (precision N-ODD-2: REP must be read as «not EQHI») |
| 7 | DATA, pins, DEADs | not to sign. Data defect D-ODD-1: the pinned start of sbq2_K8_m16 contains a non-edge, and the box-54 W-rank DEAD rests on it (§7) |
| — | RESULTS line (cd121dff) | REQUIRED CHANGES ODD-L1 to ODD-L4 (§8) |

## 1. Premises
- [R15a]. RESULTS l. 624 R15 (a) is Lemma A (Ωσ ⊴ Ω_{Switch_I(σ)} for non-empty I), and R15 (d) says every N5 iteration applies such a
  switch to σ and/or τ. Ξ_k depends on σ_k only, so Ξ_(k+1) ⊵ Ξ_k at every transition (I = ∅ when only τ moves) ✓.
- [R57]. RESULTS R57 l. 2915-2916, standing premise «S1's procedure realises an optimal σ̄» (1E-N3). Read as the pointwise optimum, as
  in every landed N5 line since R96: Ξ_k(x) ⊴ val(σ_k, ρ)(x) for every positional Odd ρ and every x ✓.
- [PLAY]. The four quoted fragments are verbatim in docs/red/P-N5-SRC.md §2 at l-red 0521fb82, the signed proof of R97's PLAY-CAUSE^S.
  They are not in RESULTS R97's landed text (checked by script).
  - N-ODD-1: the line should cite «P-N5-SRC §2 (proof of RESULTS R97 PLAY-CAUSE^S)», as the packet's own §1 does.
- Φ, written out (the packet leaves it implicit). For v = (w, P, ℓ) and a finite sequence a = a_0 … a_(i−1):
  - if w = a_j, with j its first occurrence in a: Φ(a; v) := (w, rel_w(a_0 … a_(j−1)), j);
  - otherwise: Φ(a; v) := (w, rel_w(a) ∪ P, i + ℓ);
  - rel_w(·) is the set of listed vertices more relevant than w.
  - On a play, this is [PLAY]'s function: the eventual cycle, and so w, is shared by y_0 and y_i.
- (Φ-comp) ✓, as a FORMAL identity in all three cases (w first in a; w first in b only; w in neither). The formal reading is needed:
  in ODD-STEP (E2), the sequence oγ followed by ξ is not a play of one strategy pair.
- W-run notation is R89 / R97 ✓.

## 2. OLD-PLAY
- If no Even vertex of x's (σ_k, σ̄_k)-play switches, then x's (σ_(k+1), σ̄_k)-play is that same play.
- [R57] at k + 1 with ρ := σ̄_k gives Ξ_(k+1)(x) ⊴ Ξ_k(x), and [R15a] gives ⊵. ✓ SIGNED.

## 3. ODD-STEP and NO-RET (every sub-case re-derived)
- (E1) ✓. If o lies on x's old play, Φ(o; ·) is still the right function, because the identity is only used with i = 1.
  - Degenerate x = o (a self-loop): then the hypothesis is the conclusion.
- Case I ✓. ρ(o) := x is a legal Odd move. ρ = σ̄_(k+1) on x's new play, because o is not on it. So val(σ_(k+1), ρ)(o) = Φ(o; v_x) =
  Ξ_k(o) ◁ ξ, against [R57] at k + 1.
- Case II.
  - (E2) and (E3) ✓. The (σ_(k+1), ρ)-play from o is the pure cycle Z = o z_0 … z_(j−1), because σ̄_(k+1)-next of z_(j−1) on x's new
    play is o.
  - w = o ✓. Φ(oγ; ξ) = (o, ∅, 0) = ξ.
  - w ∉ γ ∪ {o}: «o's new path TO w avoids γ» ✓. A first hit of some z_t before w would continue along γ to o and close a cycle without
    w. (If w came before z_t, the path to w has already ended.)
    - A ✓. o ∈ P ⊆ P(v_x), and v_x is x's OLD value, so x's old play visits o before w. Then it returns through σ̄_k(o) = x, so the play is
      periodic through x … o, and w would have to come before o.
    - B ✓. R and P are disjoint because the path avoids γ, and Ξ_k(o) = (w, P ⊔ R, ℓ + j + 1).
      - R ≠ ∅: Q1 forces Ω(t) odd. Then m = t, and reward(t) = −p′(t) < reward(w) for either parity of w. So val ◁ ξ, against (E3).
      - R = ∅: equal path sets and a longer length is worse for Even, so Ω(w) is even. Then m is below w, reward(m) < p′(w), and val ◁ ξ.
  - w = z_i ∈ γ ✓.
    - The repeated vertex of x's new play may be some z_t with t < i, if o's path re-enters γ before w. The cycle still contains
      z_i, …, z_(j−1) and o, with top w. So ξ = (w, ∅, ℓ), v_x = (w, R, i) and Ξ_k(o) = (w, R, i + 1).
    - R = ∅ gives m = w and val = (w, ∅, i + 1) = Ξ_k(o) ◁ ξ.
    - R ≠ ∅: if the top t is even, then Ξ_k(o) ▷ ξ; if t is odd, then m = t and val ◁ ξ. Contradiction in each case.
- The case split w = o / w ∈ γ / w ∉ γ ∪ {o} is exhaustive, and A / B is exhaustive (o ≠ w). SIGNED.

## 4. ODD-RELAY, ODD-ADD
- π is a play prefix before the first visit of u, so it is a simple path, and every vertex on it moves the same at k + 1.
- So Ξ_j(x) = Φ(π; Ξ_j(u)) for j = k, k + 1. The case u = x (π empty) is trivial.
- The contrapositive with ODD-STEP is ✓. ODD-ADD matches each change of Ξ(o) at k with a change of Ξ(u_k) at the same k ✓. SIGNED.

## 5. SRC-ROOT
- u_k(o) exists ✓. If the old play from x meets no vertex of D_k, it is the (σ_k, τ)-play, whose cycle top c has W-cycle node c, so
  c ∈ C (λ_W is fixed on F).
- Each step is ODD-RELAY with π = FS_k(o_j) and u = o_(j+1). «Not a prefix event» is exactly its hypothesis.
- A non-Odd o_t lies in D_k ∪ C, and D_k is Odd, so o_t ∈ C is Even ✓.
- Termination ✓. If some o_j repeats, the walk o_0 FS(o_0) o_1 FS(o_1) … covers all of o_0's old play. The o_j are Odd, and no Even
  vertex of any FS switches. That contradicts OLD-PLAY at o_0.
- SIGNED. The «Reading» (a relocation, not a smaller count) is right and is not signed.

## 6. FUEL-LEX, FUEL-COUNT
- G-ODD-1 (a proof-text gap in FUEL-LEX, CLOSED here; the statement is unaffected).
  - For b = a = (1, r), the proof «suppose every change of Ξ(z) strictly between t and t′ has key < (1, r)». That is not the negation
    of EQHI: the negation is «key ≤ (1, r)», which leaves intermediate changes of key exactly (1, r) uncovered.
  - Closing argument. Changes of key < (1, r) leave the cycle node and every rank ≥ r unchanged. Changes of key (1, r) flip rank r with
    all higher ranks fixed. After the rise at t, bit r is the Even-better bit β. Consider the FIRST change of key (1, r) after t, at
    some u ∈ (t, t′) or at t′ itself. It moves rank r away from β with all higher ranks equal, so it is a fall, against [R15a].
  - So no change of key (1, r) occurs in (t, t′), and the written argument then applies at t′.
- FUEL-LEX: SIGNED with this sub-case.
- FUEL-COUNT ✓.
  - Charges: ASC goes to the change at t′, EQHI to a change u ∈ (t, t′). For each, «the last re-route at a transition ≤ u» is k, with
    key a. The windows (t, t′] are disjoint. So #ASC + #EQHI ≤ HC.
  - REP(2, 0) ≤ n − 1: the cycle-node reward of Ξ(z) rises strictly.
  - A block of consecutive REP(0, 0) boundaries chains re-routes of key (0, 0): a strictly descending run cannot leave (0, 0). There is
    no higher-key change on the contiguous union of their windows, so only the length moves, strictly one way, among ≤ n + 1 values.
  - Blocks ≤ 1 + A, runs ≤ n(1 + A), N ≤ (n + 2)·n(HC + n).
  - N-ODD-2 (precision): a boundary that is both EQHI and REP must be counted as EQHI. The block argument uses «no change of key > (0, 0)
    in the window», which is «not EQHI».
- SIGNED.

## 7. Controls (own engine; docs/referee/scratch/odd_probe.py, `python3 -I`, rl_engine; no lane code)
- Checks:
  - OLD: OLD-PLAY at every Ξ-change.
  - STEP: ODD-STEP at every Odd o and transition; caseII counts Case II.
  - ROOT: SRC-ROOT's chain from every changing Odd o_0 in every W-run. Every o_j must change, lie on o_0's old play and never repeat;
    the chain ends at (a) or (b).
  - LEX / CNT: FUEL-LEX on consecutive re-routes of each pair (the packet's definition, every Even y), and FUEL-COUNT's bound.
- Corpus: box 59 sbcg.lst ∪ alt_all.lst = 719 distinct games, MAXN 100 (656 analysed, 63 skipped), start file when present. Results:
  - 950 W-runs, 7,401 transitions;
  - OLD 107,213 checks, STEP 115,522 (Case II 14,299), ROOT 11,513 chains (end (a) 11,496, of which 79 by an Odd choice change only;
    end (b) 17; longest 8);
  - FR 11,884 fuel re-routes (ASC 217, EQHI 106, REP 0), CNT 11,213 pairs;
  - VIOLATIONS 0. Logs: odd_logs/runs/, odd_logs/sum.txt.
- Random: 2 × 2,000 games, n 6-14, seeds 1 and 2: VIOLATIONS 0 on both. Seed 1 had STEP 11,352 (Case II 3,900), OLD 9,193 and ROOT 103
  (odd_logs/rand_s1.txt, rand_s2.txt).
- MUT controls, on the pins sbq2, obs, src2, rcl, hit_b6a_1, nep56 and so_th (MAXN 400, so latew_K16_m32 at n 482 is run separately;
  odd_logs/pins_mut*.txt):
  - MUT 1 (OLD reads only the play prefix before its cycle): bites, OLD_V 342.
  - MUT 2 (no EQHI clause): bites, LEX_V 10, all on so_th_n32.
  - MUT 3 (SRC-ROOT without the Odd-choice prefix event): never bites, on the pins or on the 5 corpus games with Odd-only endings. So in
    data a later Even switch or C-node always catches the chain. The proof still needs the clause, because ODD-RELAY needs π free of
    Odd choice changes.
- latew_K16_m32 (n 482, start, MAXN 600; odd_logs/pin_latew.txt): 1 W-run of 560 transitions, OLD 9,297, STEP 214,480, ROOT 6,733,
  FR 2,017 (max 16 per pair, = the packet's «latew 16»); VIOLATIONS 0.
- Lane reconciliation (FSONLY=1 restricts y to box 56's first-segment selectors, as srcfuel.py does):
  - so_th_n32: FUELEV 21, EQHI 6 = lane;
  - nep56_n32: ASC 2 = lane; re-routes 57 against the lane's FUELEV 56. One re-route is unreconciled. It does not affect LEXV 0 on
    either side.
- Pins.
  - L-SI's own check.sh blocks «box 54» to «box 57» and the P-N5-ODD pin block (lines 994-1051 of experiments/si/check.sh at 0afc0d70a),
    run alone in a detached worktree: all PASS, EXIT 0.
  - Oink (built at 8fbf0a7 by scripts/setup_oink.sh): `oink --zlk --verify` solves and verifies sbq2_K8_m16, obs_K12_m24, src2_K3,
    rcl_K24, latew_K16_m32, hit_b6a_1 and nep56_n32.
- D-ODD-1 (DATA defect, not a signed item). sbq2_K8_m16.start (sha1 98b0927a…) sets τ(242) := 243.
  - Odd 242's successors are 244, 246, …, 258, so 243 is not one of them.
  - The same file (same sha1) is at l-red flipev/instances (R145's source) and at L-NEW box97/inst and box110.
  - The lane engines (n5x.start_pair) accept it unchecked. My parser rejects it (core_probe.parse_start: «invalid … given start skipped»).
  - Consequence: the box-54 DEAD of the W-rank potential (packet §7; docs/si/DEAD.md «box 54» l. 674: «W(242) = W(259) at all 153
    states») rests on the non-edge. 259's only successor is 243, so with τ(242) = 243 both vertices lead to 243.
  - docs/referee/scratch/sbq2_start_check.py repairs τ(242) to each of its 8 real successors. In every case the run still has 153 states
    and σ̄(260) still flips 128 times, but W(242) = W(259) holds at 0 states, not 153.
  - So the W-rank DEAD's witness is an artifact of an unfaithful start. The DEAD needs a new instance or must be withdrawn.
  - The quadratic σ̄-flip count itself is robust: it is the same for all 8 repairs.

## 8. RESULTS line (cd121dff): strict symbol test, clause by clause
- REQUIRED changes:
  - ODD-L1. ODD-ADD reads «the Ξ-changes of o on a set of transitions are at most the transitions at which one of the relayed vertices
    changes». «The relayed vertices» is undefined, and the hypothesis is lost. Fix: «for a set I of transitions and a set U of vertices
    such that at every k ∈ I at which Ξ(o) changes, ODD-RELAY's hypothesis holds for some u_k ∈ U: |{k ∈ I : Ξ(o) changes at k}| ≤
    |{k ∈ I : Ξ(u) changes at k for some u ∈ U}|».
  - ODD-L2. «rise transitions» (FUEL-LEX) is used but never defined. Fix, in the fuel definition: «its rise transition := k − 1 → k».
  - ODD-L3. F is bound only inside SRC-ROOT's clause («in every W-run F»). FUEL-LEX and FUEL-COUNT use F («k − 1 ∈ F», «in F»,
    «transitions u of F») with no binder in their clauses. This is the recurring miss (cf. SETTLE-L1). Fix: «for every N5 run on every
    game and every W-run F of it» in the quantifier.
  - ODD-L4. In the R57 gloss «Ξ_k(x) ⊴ val(σ_k, ρ)(x) for every positional Odd strategy ρ», x is free. Fix: «… ρ and every vertex x».
- Precision:
  - N-ODD-1 ([PLAY] source).
  - Φ is defined but used by no claim of the line; keep it (it is harmless) or drop it.
  - SRC-ROOT: add «every o_j's Ξ changes at k», and that o_t may be o_0.
  - «HXS-POLY of RESULTS R97» is a name from R97's freeze message, not its landed line. Say «the polynomiality of max HXS_F in R97's
    SRC-COUNT».
  - «rank» (in the key) is SPEC Q1's.
- Token pass otherwise clean:
  - run, transition, switches, Ξ_k, σ̄_k, values, the order, W-run, τ, C, D_k, S_k, H_k, FS_k, u_k, prefix event, fuel re-route, key,
    n, N, HC are bound;
  - o, x and u are bound in their clauses.
- TARGET.md diff: a RELOCATION. «no count is bounded; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim» ✓. No
  algorithm or complexity claim.
- DATA in the tail («corpus 0 violations …, 900,000 random games 0 for NO-RET») is consistent with §7 of the packet and with my runs.
- Verdict: MATCHES the signed items once ODD-L1 to ODD-L4 are applied.

## DONE / FINDINGS / NEEDS
- DONE: this report; odd_probe.py, sbq2_start_check.py, odd_logs/.
- FINDINGS:
  1. Every item to sign is SIGNED. G-ODD-1 (FUEL-LEX proof text, an intermediate change of equal key) is closed here. Nothing is FALSE.
  2. Line: REQUIRED ODD-L1 (ODD-ADD), ODD-L2 (rise transition), ODD-L3 (F unbound), ODD-L4 (x free).
  3. D-ODD-1: sbq2_K8_m16.start has the non-edge 242 → 243. The box-54 W-rank DEAD's witness is an artifact of it. The file is shared
     by L-RED (flipev, R145) and L-NEW (box 97, box 110). The quadratic σ̄-flip count survives every repair.
- NEEDS: Lead: route ODD-L1..L4, G-ODD-1 and N-ODD-2 to an L-SI successor (docs/si/P-N5-ODD-fixes.md). Route D-ODD-1 to L-SI (the W-rank
  DEAD), L-RED (flipev start, R145) and L-NEW (box 97 / 110 copies); every lane engine should reject a non-edge start.

## §C. Line revision L-1 and the fixes file (successor 21, 14:22Z 2026-10-31 by date -u)
- Objects (re-hashed):
  - docs/si/P-N5-ODD-line-L1.txt at claude/l-si ab0baf919, sha1 3e25138b9e7ef228ddba306d35ae3897cb797ea2 (one line, no heading marker);
  - docs/si/P-N5-ODD-fixes.md, sha1 67fbe3a4ce37aa31bd819ce2b22a30c185443a85 (F0 + entries 1-4).
  - I opened no docs/referee-2/ file. REFEREE-2's items are known to me only as the fixes file quotes them.
- Word-diff against cd121dff (`git diff --no-index --word-diff=porcelain`): every changed token maps to a fixes item, and nothing else
  changed.
  - E3.4 «ρ and every vertex x» = my ODD-L4 ✓.
  - E3.9 «; «rank» is SPEC Q1's» ✓.
  - E3.6 «(P-N5-SRC §2, the signed proof of RESULTS R97 PLAY-CAUSE^S)» = my N-ODD-1 ✓.
  - E3.3 «W-run F of a run», «for a W-run F, …» (twice), «and for every W-run F of the run,» = my ODD-L3 ✓.
  - E3.2 «its rise transition := k − 1 → k» = my ODD-L2 ✓.
  - E3.5 the k / x / u / o quantifiers in OLD-PLAY, ODD-STEP, ODD-RELAY and SRC-ROOT ✓.
  - E3.1 ODD-ADD with I, U and ODD-RELAY's hypothesis = my ODD-L1 ✓.
  - E3.8 «every o_j's Ξ changing at k», «(possibly o_0)» ✓.
  - E3.7 «the polynomiality of max HXS_F in RESULTS R97's SRC-COUNT» ✓.
  - E3.11 the referee-originated repairs in the scope tail ✓.
  - E3.10 the DATA wording ✓.
  - The source tag names the fixes file and successors 36, 37 ✓.
- My REQUIRED ODD-L1, L2, L3 and L4 are all met.
- The scope tail names the referee-originated repairs: «the proofs of FUEL-LEX and FUEL-COUNT carry referee-originated repairs (G-ODD-1,
  written independently by REFEREE and REFEREE-2; G-ODD-2 = N-ODD-2; docs/si/P-N5-ODD-fixes.md entries 1-2)» ✓ (L41). The scope words
  RELOCATION / G-N5-TIME OPEN / not M3 / not a TARGET.md claim are unchanged ✓.
- Strict symbol test on L-1, every clause:
  - k, x, o and u are now bound in their clauses. F is bound by «for every W-run F of the run». I, U and u_k are bound in ODD-ADD; o_0,
    o_j and o_t in SRC-ROOT; (y, z), a and b in FUEL-LEX.
  - ONE remaining free pair: ODD-L5 (REQUIRED). «(Corollary FUEL-COUNT) the number N of fuel re-routes of (y, z) in F …». (y, z) is
    bound only in FUEL-LEX's own clause («for every pair (y, z) and consecutive fuel re-routes …»), and the clauses are separated by «;».
    So in FUEL-COUNT the pair is bound in another clause. Fix: «(Corollary FUEL-COUNT) for every pair (y, z), the number N …».
  - This pair was already free in cd121dff, and my first report missed it (§8 «Token pass otherwise clean»). It is my miss, not a change
    made by L-1.
- Fixes file:
  - Entry 1 (G-ODD-1): both referees are quoted verbatim, and the adopted replacement proof is correct. If EQHI fails, the first change
    in (t, t′] with key ≥ (1, r) has key exactly (1, r), every earlier change in (t, u) has key < (1, r), and u moves rank r off β, a fall.
    This is my closing argument in a «first such u» form ✓.
  - Entry 2 (G-ODD-2 = my N-ODD-2): ACCEPTED. REFEREE-2's repair, «classify a boundary as ASC, else EQHI, else REP» with only pure REP
    (0, 0) boundaries chained, is exactly my N-ODD-2. I sign it (Opus 5.5, D15). Under L41 this is my independent signature of the
    repair.
  - Entry 3: the mapping is as checked above.
  - Entry 4 (D-ODD-1): the W-rank DEAD is WITHDRAWN and the W-rank potential is OPEN. That is the right consequence. The repaired
    figures agree with mine: 153 states, Wtie 0, 128 flips. I have not re-run the lane's other re-counts (oddadd, ascw, srcfuel, anc).
    The new start validation (startcheck.py) is the remedy I asked for.
- Verdict on L-1: does NOT yet match, only because of ODD-L5 ((y, z) in FUEL-COUNT), a one-phrase insertion. Everything else MATCHES
  (Opus 5.5, D15).
