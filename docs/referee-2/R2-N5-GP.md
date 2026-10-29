# R2-N5-GP: REFEREE-2 report on packet P-N5-GP (L-SI box 31): W-MON, XW, Lemma GP*, Corollaries GP, GP+, FW-R*
Referee: REFEREE-2 successor 20, Opus 5.5 (D15, L37), independent second referee. Written 2026-10-29 from 16:41Z (date -u).

**Object.**
- docs/si/P-N5-GP-box31.md, sha1 cd4866df18b55f44b3ef3d52de65943eeffe9140, 177 lines, at l-si freeze d072bb28. Measured with
  `git show d072bb28:<path> | sha1sum`; equal to the Lead's figure.
- Pinned files, measured at d072bb28:
  - experiments/si/core/gp.py 270f247c;
  - rund/quotecheck.py 29bb4a97;
  - instances ccl_w48_n48.pg a7056dea, rlin_cex_n40.pg 670ba1ff, rlin_cex_n40.start e488c00f (all = the packet's sha1s).

**Independence.**
- Name count `git ls-tree --name-only -r origin/claude/referee docs/referee/ | grep -ic gp` = 0 at 16:41:06Z; 14 at 17:08:13Z (push turn, after a fresh fetch).
  Names only. No docs/referee/ file opened.
- The lane's gp.py and quotecheck.py were READ, then RUN as check.sh l. 699-710 (blocks "box 31 §6" and "box 31 packet"), with `python3 -I`
  in a detached worktree at d072bb28. Output: logs/pinned_check.txt. They were never imported.
- My control is my own code: R2-N5-GP/gp_check.py.
  - State loop: my lane's R2-N5-DUAL/dual_check.Runner, on si.py (SPEC S1's own implementation, read-only).
  - W is my own play value of the (σ, τ)-plays.
  - Phases, frozen W-phases, blocked edges, unblocked paths, U_t, S_{d,t}, same-pair gates, tail-disjointness and late adoptions are all
    written from the packet's definitions.

**Scope (D1).** A REDUCTION per frozen W-phase only, not a bound on the run. R*_T is not bounded, and FW-BF and G-N5-TIME stay OPEN. Not a
TARGET.md claim, no running time.

## 0. Verdicts (all "(Opus 5.5, D15)")
| § | item | verdict |
| --- | --- | --- |
| §1 | setting, [FRZ] frozen W-phase, [H] arena, premises | SIGNED (well formed; 13/14 quotes strictly verbatim, the 14th a faithful elision: N-GP-1) |
| §2 | Lemma W-MON | SIGNED (with the standing premise that S4a's σ_new is the one-player optimum: N-GP-2) |
| §2 | Lemma XW | SIGNED (the first part is SPEC S1-Xi's "minimising at every vertex at once", i.e. R57 (a)'s (VJ) premise: N-GP-2) |
| §3 | Lemma GP* | SIGNED. Every R17 (b) sub-case is redone without the Ξ-improvement in Case B (the key point, §2.3) |
| §3a | Corollary GP | SIGNED |
| §3a | Corollary GP+ | SIGNED |
| §4 | Corollary FW-R*: WCH ≤ (n − 1)(R*_T + 1) per frozen W-phase | SIGNED |
| — | approved RESULTS line | NOT CHECKED: its text was not in any file I could read. Requested from the Lead at 16:5xZ (§2.6) |
| §5, §6 | READING, DATA | not signed. Pinned checks reproduced EXACTLY (§3.1) |

No gap. No item FALSE. Notes N-GP-1..N-GP-6 (§4).

## 1. Premises
- 14 quotes. The lane's quotecheck: quotes=14 bad=0, QUOTES PASS; --mut: QUOTES FAIL.
- My strict qcheck: 13/14 OK, SHIFT=1 control 0/14.
- The one MISS is [CASE-A] (box10 l. 32-37). Its "…" elides A1's closing parenthetical ("(If the cycle node c of Ω_k(ρ_k(x)) differs from
  u, then … the prefixed values are ordered the same way.)"). Faithful; N-GP-1.
- Read in context at 2a435f8f4:
  - SPEC S1-S5;
  - RESULTS R15 (d) and R17 (a)-(f);
  - R17's object docs/new/N5-phase-bound-box10.md §1-§3 (l. 10-80), i.e. [F1], [PRE], [V1], [V2], [VAL], Lemma P with Cases A and B in full,
    Theorem PH;
  - N5-FRZ-box29 §0 is restated in [FRZ].

## 2. Proof check
**2.1 W-MON.**
- Inside a phase τ is constant. A non-fallback transition changes σ ([STEP]) through S4a with Iσ_t ≠ ∅, so σ_{t+1} = S4a's σ_new.
- That is S1 run on dual(H_t) against τ: Odd's optimum on the dual, i.e. Even's pointwise optimum on H_t in G's order. G^d's order is the
  exact reverse of G's: my N-GS-2, R2-N5-MPGS-s20.
- (σ, τ)-plays in G and H_t coincide for strategies inside H_t, and ρ_t ∈ H_t. So [F1] gives W_{t+1} ⊵ W_t. ✓
- Data (WMON): W_{t+1} ⊵ W_t and ⊵ 3 random H_t-strategies at every in-phase non-fallback transition. 0 violations.

**2.2 XW.**
- First part: Ξ is the pointwise minimum over Odd's replies (SPEC S1-Xi; the signed form is R57 (a) (VJ)), and τ is one reply. ✓
- Second part: a W-play avoiding D is step by step the (σ, σ̄)-play. ✓
- Data (XW): 0 violations, both parts, every vertex of every state.

**2.3 GP*: the key point (Case B without the improvement).** I re-derived every case against R17's Lemma P (box10 l. 29-55).
- Induction bookkeeping. r′ = r minus its first edge: simple, avoids x, ≤ k − a edges, and its i-th Even edge is r's (i + 1)-th, checked at
  state (k + 1) − 1 − (i + 1) = k − 1 − i. So r′ is unblocked at state k. ✓ The first edge is checked at state k. ✓ L = 0 at any k: λ_W
  constant on F gives W_k(u) = (u, ∅, 0). ✓
- Case A. Its trigger is "not blocked and ∉ Iσ_k" ⇒ W_k(z) ⊴ W_k(ρ_k x), since the order is total; or x Odd, or z = ρ_k(x). In each the
  hypothesis R17's Case A uses holds. A1 uses [V1] and [V2]: r′ avoids x, and ρ_k(x)'s path avoids x. A2 is the reward comparison. Then
  W-MON. ✓
- Case B, (x, z) ∈ Iσ_k:
  - ρ̂ ∈ H_k, and [F1] gives W_{k+1}(x) ⊵ val_ρ̂(x). This uses only W-MON's first part.
  - R17's Case B used the improvement Ω_k(z) ≻ Ω_k(ρ_k(x)) in exactly two places: B1's on-cycle sub-case and B2. There it narrowed the
    possibilities to "top even" or "∅ with c odd and longer".
  - GP* splits these places completely, without the improvement:
    - B1 (x ∉ π, off c's cycle): no improvement used in R17 either. val_ρ̂(x) = x ⊕ W_k(z) ⊵ x ⊕ value(r′) by [V2]. ✓
    - B1′ (x ∉ π, on c's cycle, x ≠ c). Z = x, π, arc(c → x) is simple: the arc from c to x and π's cycle segment meet only at c, because x
      ∉ π. The vertices of Z above c are exactly P(π).
      - (i) P(π) = ∅: (c, ∅, |π| + 1) = x ⊕ W_k(z) ⊵ value(r) for either parity of c. R17 had only "c odd, longer"; the even case is the
        same computation. ✓
      - (ii) top of P(π) even: top(Z) has a better reward than c, so λ_W(x) changes at k + 1, which is impossible in F. ✓
      - (iii) top odd [NEW]: W_k(z) is below every (c, ∅, ·) by DELTA. value(r′) ⊴ W_k(z) puts value(r′)'s P-set below ∅ (same c; equal
        weights force equal sets) or its cycle node u below c. x is less relevant than c, so value(r) ◁ (c, ∅, ℓ_x) = W_k(x). ✓
    - B2 (x ∈ π, so λ_W(x) = c):
      - B2a, x = c: u ≠ x, and value(r′) ⊴ W_k(z) (cycle node x) forces reward(u) < reward(x), so value(r) ◁ (x, ∅, 0). This is R17's own
        argument. ✓
      - B2b, x ≠ c. W_k(z) = π[z..x) ⊕ W_k(x) and W_k(x) = x ⊕ W_k(ρ_k x). The P-sets differ exactly by D′, and c ∉ Z.
        - (i) top of D′ even: λ_W changes, impossible. ✓
        - (ii) top odd [NEW]: W_k(z) ◁ W_k(ρ_k x). ✓
        - (iii) D′ = ∅: c odd ⇒ top(Z) (less relevant than c) has a better reward ⇒ λ_W changes, impossible; c even [NEW] ⇒ same P-set,
          longer path ⇒ W_k(z) ◁ W_k(ρ_k x). ✓
        - In (ii) and (iii)-even, Case A's A1 applies (x is not its own cycle node). ✓
  - The partition is complete: x ∈ π, or x ∉ π and on or off c's cycle; and x = c is possible only if x ∈ π.
- No step uses Ω_k(z) ≻ Ω_k(ρ_k(x)), nor any W-improvement of (x, z): the packet's claim holds.
- Data:
  - GPS: GP* on all enumerated unblocked paths, 0 violations.
  - F1H: W_{k+1}(x) ⊵ val_ρ̂(x) at every Case B edge, 0 violations.
  - IMP: the three "impossible in F" configurations (B1′(ii), B2b(i), B2b(iii) with c odd) never occurred.
  - The NEW sub-cases do occur (alt_all: B1′(iii) 4, B2b(ii) 41, B2b(iii)-even 66; lib41: §3.2), so the data exercise them.

**2.4 GP, GP+ (§3a).** Both reduce to "no edge to ALLOWED⁺(x, t) is blocked at t", then GP*. The four cases:
- ρ_t(x): blocked needs W_t(z) ▷ W_t(ρ_t x), which fails for z = ρ_t(x).
- Iσ_t: not blocked by definition.
- U_t: W_t(z) = Ξ_t(z) by XW (second part); then ⊴ Ξ_t(ρ_t x) by [S2], not improving; then ⊴ W_t(ρ_t x) by XW (first part).
- Same basin S_{d,t} of a same-pair, tail-disjoint gate:
  - ρ_t(x) ∈ S_{d,t}, because x is Even and d Odd.
  - p(y) avoids D, so it is also the σ̄-prefix.
  - Tail-disjointness gives W_t(y) = p(y) ⊕ W_t(d) and Ξ_t(y) = p(y) ⊕ Ξ_t(d), with the same cycle node c (same pair).
  - The comparison p ⊕ A vs q ⊕ A depends only on the high parts of p Δ q (A's P-set is disjoint from both, by tail-disjointness), then on
    |p| vs |q| with c's parity. So it is independent of A, and the Ξ-comparison transfers to W.
  - ✓ (equality transfers too).
- Each corollary is signed on its own. Should GP* need repair, the four cases still give "not blocked", but GP* is needed to conclude.
  The table's "each also follows from §3's Case A / Case B directly" is true in that sense: the induction of §3 run with ALLOWED⁺ in place
  of "unblocked".
- Data (NOTBL): 0 blocked edges inside ALLOWED⁺ (U and same-basin cases included) at every state of every frozen W-phase.

**2.5 FW-R*.**
- The first n − 1 transitions are free.
- For a W-change at k ≥ a + n − 1: π = the ρ_{k+1}-play from x to u = λ_W(x), with u a cycle node of state a. π is simple, L ≤ n − 1 ≤ k − a,
  and value(π) = W_{k+1}(x).
- If π were unblocked at k, GP* and W-MON would give W_k(x) = W_{k+1}(x), using that distinct values are distinct in the order. So some
  Even edge (y_i, y_{i+1}) is blocked at t = k − 1 − i ∈ [a, k − 1].
- A blocked edge is neither ρ_t(y_i) nor in Iσ_t, so ρ_{t+1}(y_i) ≠ y_{i+1} (S4a, non-fallback). Since ρ_{k+1}(y_i) = y_{i+1}, y_i adopts
  it at some τ′ ∈ [t + 1, k]: a late adoption, since the edge was blocked at t < τ′. Also k − τ′ ≤ i ≤ n − 2.
- Each τ′ is charged by at most n − 1 values of k. ✓
- Data (FWR): WCH ≤ (n − 1)(R*_T + 1) in every frozen W-phase checked.
  - Max R*_T 40 and max WCH 49 (alt_all). This is the lane's grow_K40_n373 case: R*_T 40, WCH 45 in the lane's count over its own frozen
    phase. My figures are maxima over all phases.

**2.6 The approved RESULTS line.**
- Not checked: "L-SI's 16:26Z wording" is not in any file on trunk or l-si that I can read. LEAD-STATE (16:23Z) records only the required
  tail "; per frozen W-phase only, not a bound on the run" and speaks of "FW-R′ WCH ≤ (n−1)(R_T+1)".
- Two requirements for the line:
  - It must state FW-R*'s R*_T (transitions adopting a previously BLOCKED edge), or note R*_T ≤ R_T if it keeps R_T.
  - It must claim nothing beyond W-MON, XW, GP*, GP, GP+ and FW-R* per frozen W-phase.
- Requested from the Lead; I append the check when it arrives.

## 3. Re-runs and own control
**3.1 Pinned (logs/pinned_check.txt).** check.sh l. 700-710, run as one block with `set -e`: exit 0. Both echo lines print PASS.
- rlin_cex_n40: `'D1': (0, 10, 10, 40, 1, …, 1, 11)`, GP PASS, RED PASS, RLIN PASS.
- ccl_w48_n48: `'D1:R_T/(n-1)': (0.0212…, 1, 3, 48, 1, …, 15, 18)`, GP PASS.
- MUT=all on ccl_w48_n48: GP FAIL (the control bites).
- quotecheck: quotes=14 bad=0, QUOTES PASS; --mut: QUOTES FAIL.

**3.2 Own control (gp_check.py; every log RESULT PASS, 0 violations of WMON, XW, GPS, F1H, IMP, NOTBL, FWR).** PCAP 300 paths per (k, x).
| corpus | runs | frozen W-phases | GP* paths checked | Case B edges (F1H) | NOTBL checks | max R*_T / WCH | X_GPall (plain Lemma P fails) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| random 3000 games n 4-14, S3 + 3 random | 12,000 | 29,440 | 63,315 | 1,679 | 14,167 | 0 / 3 | 0 |
| random 400 games n 15-30, S3 + 2 random | 1,200 | 4,326 | 11,430 | 225 | 3,815 | 0 / 2 | 0 |
| alt_all, pinned starts (93 valid, 1 invalid skipped) | 93 | 1,970 | 887,036 | 9,299 | 159,321 | 40 / 49 | 125,338 |
| lib41_noref, S3 + 1 random | pending (run in 8 chunks, in progress at push 1) | | | | | | |
| ccl_w48_n48 (S3) | 1 | 39 | 89 | 46 | 876 | 1 / 3 | 2 |
| rlin_cex_n40 (pinned start) | 1 | 4 | 58,296 | 199 | 569 | 0 / 10 | 0 |
| runfam_K100 (pinned start + S3) | pending (in progress at push 1) | | | | | | |

- Agreement with the lane's pins:
  - ccl_w48_n48: frozen phase of 3 transitions, R*_T = 1, WCH 3, plain Lemma P fails (the lane: [15, 18], R_T 1, WCH 3, MUT=all FAIL).
  - rlin_cex_n40: one 10-transition frozen W-phase, R*_T 0, WCH 10 ≤ 39 (the lane: R = 0, WCH 10, L 10).
- Sub-case census (alt_all): B1 9,087; B1′(i) 18; B1′(iii) 4; B2a 83; B2b(ii) 41; B2b(iii) c even 66; the impossible ones 0.
- In random games frozen W-phases are short (≤ 3 transitions) and nothing is blocked, so the library and lane pins carry the information.

## 4. Notes (not gaps)
- N-GP-1 (quote form). [CASE-A] elides A1's closing parenthetical with "…". The elided sentence is the cycle-node-differs remark of A1, which
  GP*'s Case A also needs, via [V2]'s "(or whose cycle nodes differ)". Faithful; quote it whole or cite [V2]'s clause.
- N-GP-2 (standing premises, one line each).
  - W-MON reads S4a's σ_new (S1 on the dual of H_t) as Even's pointwise optimum of H_t. That needs the order reversal between G^d and G
    (exact, N-GS-2) and the SPEC-conformance premise (R57 (b)).
  - XW's first part is R57 (a) (VJ).
  - Name both.
- N-GP-3 (Case B: the parity of c in B1′(i)). R17 restricted P(π) = ∅ to "c odd, longer" (by improvement). GP*'s B1′(i) covers both parities
  with one formula, which is correct because [V2] needs no parity. Worth one clause, since it is where GP* is strictly more general than R17.
- N-GP-4 (B1′'s cycle shape). "Z = x, π, then the arc of c's old cycle from c back to x" is simple because x ∉ π. Then π's part on c's cycle
  (from its entry point to c) and the arc c → x meet only at c. One clause; the packet asserts it.
- N-GP-5 (§3a's table wording). "each also follows from §3's Case A / Case B directly" means the §3 induction run with ALLOWED(⁺) for
  "unblocked". The four non-blocked cases alone do not conclude without that induction. Wording only.
- N-GP-6 (FW-R*'s R*_T vs the 16:23Z "R_T"). R*_T counts adoptions of previously BLOCKED edges. An R_T over a larger edge class (not in
  ALLOWED⁺) is ≥ R*_T, so a line stated with R_T is implied, but weaker. The RESULTS line should use R*_T (§2.6).

## 5. DONE / FINDINGS / NEEDS
- DONE: this report; docs/referee-2/R2-N5-GP/{gp_check.py, named.lst, run_all.sh, logs/ (pinned_check.txt included)}.
- FINDINGS:
  - W-MON, XW, GP*, GP, GP+ and FW-R* all SIGNED, with no gap.
  - The key point holds: every R17 (b) sub-case is redone without Case B's improvement. Three sub-cases are new (B1′(iii), B2b(ii),
    B2b(iii) with c even), each closed through Case A's A1 or a direct order comparison, and all three occur in data.
  - The pins are reproduced exactly.
  - The RESULTS line is not yet checked (text not received).
- NEEDS: Lead: the verbatim RESULTS line; route N-GP-1..6 to L-SI. I write §C after REFEREE's GP report.
