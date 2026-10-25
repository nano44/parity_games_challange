# R-N5-KW: REFEREE report on packet P-N5-KW (L-SI box 15: W-ONCE, Facts A0/A/B, FRZ-U, LEN, PAR, H-PATH, KIND-MONO, CASC-B, CW-INT, E-SEG, Theorem RUN, Corollary KW-S, Corollary PHASE)
Referee: REFEREE (successor 11, session_01VH2ckvgGP9CGkb8Suno5f1), Opus 5.5 (owner ruling D15, Lead reading L37).
- Routing: the Lead's message of 22:04Z (Lead's stamp), item (2). One review unit:
  - docs/si/P-N5-KW-box15.md, sha1 c0b0111fcc2259e4ed9d43647bc4fa08cec452a5, 406 lines;
  - docs/si/P-N5-KW-addendum-box15.md, sha1 8d6bfb3c32d80ed7040df4ae2dee56bb9bb9b5bd (units: transitions; switches ≤ n · transitions).
  Both checked with `git show d9291be0:<file> | sha1sum` at the pin d9291be0 and identical on my tree. Author: L-SI successor 10.
- Written 2026-10-25T22:20Z-22:44Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: I have not opened any docs/referee-2/R2-N5-KW* file. I read the lane's experiments/si/kw15/kwcheck.py only to
  learn what its "freeze delay" measures (§12); no lane code was run or imported. I did not read docs/new/N5-KW-box42.md's cross-read
  sections. D1: each statement treated as wrong until its proof was checked.
- Premises re-read in their landed text (docs/RESULTS.md): R15 (a), (d); R17 (F1); R19 (a), (d) (SG); R20 (d); R21 (a) XW; R22 (a) F1°,
  (b) TC; R23 (g) WM; R24 (a)-(c), (e); R26 (a)-(d), and the proof text of R26 (c) / (a) in docs/new/P-N5-U23-box31.md §1-§2 (sha1
  ee3e5d1e…, the object of R26); R27 (a), (d), (e), (g); R30 (c); R34 (e), (f); R38 (a). SPEC docs/new/N5-ssi-global.md S1-S4, FIX 2-4, Q1.
- Tools: own engine scratch/rl_engine.py with scratch/rl_probe.py; new probe scratch/kw_probe.py and climb scratch/kw_climb.py.
  Logs scratch/kw_logs/.

## Verdicts
| § | statement | label | verdict (Opus 5.5, D15) |
| --- | --- | --- | --- |
| §2 | Lemma W-ONCE (every game); Corollary W-ONCE′ | PROVED | SIGNED |
| §3 | Fact A0, Fact A, Fact B | PROVED | SIGNED |
| §3 | Lemma FRZ-U | PROVED | SIGNED |
| §4 | Corollary LEN | PROVED | SIGNED (note KW-N2, wording) |
| §5 | Lemma PAR | PROVED | SIGNED |
| §5 | Lemma H-PATH | PROVED | SIGNED |
| §5 | Lemma KIND-MONO | PROVED | SIGNED (vacuous after the freeze in all data, §12) |
| §5 | Lemma CASC-B | PROVED | SIGNED |
| §5 | Lemma CW-INT | PROVED | SIGNED |
| §5 | Proposition E-SEG | PROVED | SIGNED WITH GAP KW-1 ((i) / N_cut as written; one-line repair, no bound downstream changes) |
| §6 | Theorem RUN | PROVED | SIGNED (r ≥ 2; KW-N3) |
| §7 | Corollary KW-S | PROVED | SIGNED (note KW-N4: (E) made explicit) |
| §8 | Corollary PHASE (conditional on f only) | PROVED | SIGNED (note KW-N1, wording of the W_ch case split) |
| §8 | READINGs (FB-POLY plug-in; assembly) | READING | not signed; checked: correct as readings, conditional on P-N5-FBPOLY and P-N5-PHI landing |
| §9-§11 | weak points, data, lane notes | READING / DATA | not signed |

Summary.
- One gap, KW-1, a counting definition in E-SEG (i)-(ii); the repair is one line and changes no bound used by Theorem RUN.
- The two steps both lanes called weakest hold:
  - FRZ-U does not rest on a transfer of R20 CR. Its proof is self-contained (Claim P^c, cases A, B1, B2, B3, and the closing step),
    and I re-derived each case (§3).
  - CASC-B uses R26 (c)'s step 2 only through "kinds constant" and R26 (a)'s step-4 induction. The proof text of R26 (c) step 2 already
    lets A1 re-route (kind-A switches are not events in R26), and c_w's switches move only A2, which enters neither kind-B values nor
    kind-B keys (§6).
- Corner cases (Lead): self-loop at o, o = c_θ, |R| = 2, c_w = c_θ: each traced through the proofs (§11) and counted in data.
- No (P) beyond the landed premises listed above. Labels exact. Not a running-time bound for N5 on general games, not a TARGET.md
  claim, not a step-4 pass. G-N5-TIME stays OPEN until P-N5-FBPOLY, P-N5-PHI and this packet land.

## 1. Setting (§1): checked
- In a phase τ is constant, so a transition with σ unchanged by S4a is an Even S4c fallback (SPEC S4c, FIX 3): correct.
- κ-order = SPEC Q1's path-set order restricted to V_{>m*}: correct. Adding a common disjoint set C, or one element x ∉ A ∪ B, preserves
  ⪯: the top of the symmetric difference is unchanged. Correct.
- Kinds: c_w ∈ π_{c_w} (π_{c_w} starts at c_w), so c_w is kind A; A2's routes run along C_W to o without passing c_w: kind B. Correct.

## 2. W-ONCE (§2): SIGNED
- Step 2 (A_{k+1}(v) ⊆ A_k(v)): σ_{k+1}(v) ∈ A_k(v) since S4a chooses inside its arena. For z ∈ A_{k+1}(v) \ {σ_{k+1}(v)}:
  Ξ_k(z) = Ξ_{k+1}(z) ▷ Ξ_{k+1}(σ_{k+1}v) = Ξ_k(σ_{k+1}v) ⊵ Ξ_k(σ_k v), the middle equality by Ξ_{k+1} = Ξ_k. So z is a strict gate
  target at k (z ≠ σ_k(v) by strictness). Correct.
- Step 3: (F1) (R17) at k and k+1, with the same τ (phase). W_{k+1} = val(σ_{k+1}) is attained in H_k and σ_{k+1} is a strategy of H_{k+1},
  so W_{k+2} ⊵ W_{k+1}; H_{k+1} ⊆ H_k gives ⊴. Correct, on every game (no 𝒞^1O used).
- W-ONCE′ is the contrapositive inside one phase. Correct.

## 3. Facts A0, A, B and FRZ-U (§3): SIGNED
- A0. On 𝒞^1O both plays from v ∈ R \ {o} follow σ and forced edges along π_v.
  - H1: o's honest continuation never meets π_v (it would return to o), so Ξ(v) = π_v ⊕ θ.
  - ¬H1, c_θ ≠ o: if c_θ ∉ π_v and π_v met C_Θ at q ≠ o, π_v would follow C_Θ from q to o; q lies on the arc c_θ → o, which is
    disjoint from the arc o → c_θ. So the honest path is a prefix of π_v up to c_θ, or π_v followed by the arc o → c_θ. Both terminals
    (θ at o, (c_θ, ∅, 0) at c_θ) are stretch constants. Correct.
  - W frame the same (H2: o's W-continuation is in F; ¬H2: C_W = o → A1 → c_w → A2 → o). The W cycle node of every v ∈ R is c_w.
- A. Under H1 the path set is (π_v ∩ V_{>c_θ}) ⊔ P(θ) with P(θ) ⊆ F ∪ {o}, disjoint from π_v. Under ¬H1 the vertices after c_θ (on π_v,
  or on the arc) lie on C_Θ, below c_θ. Intersect with V_{>m*} ⊆ V_{>c_θ}. Correct, and C_Ξ, C_W are constant and disjoint from π_v.
- B. The cycle nodes agree within each frame, the constant parts cancel in the symmetric difference, and the top of
  (π_y Δ π_z) ∩ V_{>c} is the top t of the κ-difference, since t > m* ⪰ c and every other differing vertex is in the κ-difference or
  ranked ≤ m*. Both frames then decide by t (SPEC Q1). Correct.
- FRZ-U, re-derived case by case:
  - (MON): WM (R23 (g)) at a non-fallback in-phase step; both values have cycle node c_w (A0); (C1) and (A-W) at k and k+1; C_W cancels.
  - Base and x = o: ρ = (o) forces L = 0. Odd x ≠ o: a = z, so Case B is impossible.
  - Case A: (IH), Case A and adding x (x ∉ ρ′ by simplicity, x ∉ π_a since π_x = x·π_a is simple), then (MON). Correct.
  - Case B: Fact B gives Ξ_k(z) ▷ Ξ_k(a), so z ∈ A_k(x) and σ̂ ∈ H_k; (F1) at x.
    - B1: z's σ_k-play is π_z, then o, then o's W-continuation (in F under H2, on C_W under ¬H2). B1's hypotheses keep x off it, so
      the σ̂-play from z is the σ_k-play and (V1) gives val_σ̂(x) = x ⊕ W_k(z), with cycle node c_w. COARSE_{m*} of both sides via
      (A-W) at k (for z) and at k+1 (for x ∈ R_{k+1} = R). Correct.
    - B2: π_z = (z … x′)·x·π_a, so κ(π_z) = κ(Z) ⊔ κ(π_a), and κ_k(z) ≻ κ_k(a) makes the top t of κ(Z) even. top(Z) = t. Even t ranked
      above c_w has reward(t) > reward(c_w) (an even beats every odd; among evens rank decides). (F1) then gives W_{k+1}(x) a cycle node
      of reward > reward(c_w), against A0 at k+1. Correct.
    - B3: x ∈ C_W \ {o}: π_a ⊆ C_W lies below c_w ⪯ m*, so κ_k(a) = ∅ and κ(π_z) has an even top t > m*. π_z avoids the C_W-arc from o
      to x (else it would reach x). The σ̂-cycle through x and o is x · π_z · (arc o → x), simple, with top t. Same contradiction. Correct.
    - The three cases are exhaustive (x ∈ π_z; else x ∈ C_W under ¬H2; else B1).
  - Closing step: π_x^t is a simple G_τ-path in R to o with ≤ r − 1 edges, so Claim P^c at k0 + r − 1 and (MON) from k0 + r − 1 to t.
    Correct. It needs only k0 + r − 1 ≤ t ≤ kT.
- The proof does not cite R20 (d) CR; it is R17 P^c's structure transcribed, with Fact B in place of Lemma C and the two cycle cases
  argued from A0. I found nothing of R20's throttled setting ((h), u*) being used.

## 4. LEN (§4): SIGNED, note KW-N2
- LEN-Ξ: with m* = c_θ the whole path set of Ξ(v) lies above c_θ = m*, so it equals κ(π_v) ⊔ C_Ξ and is frozen after f0. With the cycle
  node fixed and Ξ non-decreasing (R15 (a)), the length is monotone. LEN-W the same with WM.
- Length ranges. KW-N2 (wording): "≤ r − 1 for v ∉ {o, c_θ}, plus the constant terminal length" is loose under ¬H1, where the terminal
  can switch between θ at o (length d_θ) and (c_θ, ∅, 0) at c_θ as c_θ enters or leaves π_v. The right statement is that the whole
  honest length from v to c_θ is the length of a simple path inside R ending at c_θ, so it lies in [1, r − 1]. Under ¬H2 the same for the W-length
  to c_w: for kind B, π_v, o and A1 are disjoint (an A1 vertex is kind A) and avoid c_w, so |π_v| + d ≤ r − 1. Under H1 / H2 the
  length is |π_v| + const with |π_v| ∈ [1, r − 1]. In every case ≤ r − 1 values, so ≤ r − 2 changes per vertex. The counts stand.
- Counts per run: (r − 1) transitions before f0 plus ≤ r − 1 changeable vertices × (r − 2). Correct.

## 5. PAR, H-PATH, KIND-MONO (§5): SIGNED
- PAR: XW (R21 (a)) θ ⊴ w; distinct cycle nodes compare by reward first, so reward(c_θ) < reward(c_w). c_w odd with c_w ≻ c_θ gives
  reward(c_w) < reward(c_θ) in both parities of c_θ. Correct, at every state of a phase.
- H-PATH: c_w ∉ C_Θ (c_θ tops it, c_w ≻ c_θ); under H1 c_θ ∈ F (TC (i)), the honest path is π_v then F; under c_θ = o it is π_v. After
  c_θ on π_v the path runs along C_Θ. So c_w is on the honest path iff c_w ∈ π_v, and then in P(Ξ(v)) (c_w ≻ c_θ, c_w ∉ P(θ)). Correct.
- KIND-MONO: after f0, P(Ξ(v)) ∩ V_{>c_w} is frozen (FRZ-U, m* = c_w), so at a kind change c_w is the top of the path-set difference
  (H-PATH); Ξ(v) increases (R15 (a)) with cycle node c_θ fixed, so the new set contains c_w iff Ω(c_w) even, which PAR forces. One-way,
  hence ≤ 1 change. Correct.

## 6. CASC-B (§5): SIGNED (the Lead's weak step 2)
- I compared the packet's written-out proof with R26's text (P-N5-U23-box31.md §2 step 1-2 and §1 step 4).
  - R26 (c) step 2 (kind B) uses: kinds constant (its step 1), A0 for kind-B values, the common key prefix, and §1 step 4's induction.
    It does not mention c_w. c_w enters only in step 3 (kind A: "Also c_w does not switch on the sub-run", for Ξ(c_w)).
  - In R26's own setting kind-A vertices may already switch inside an event-free sub-run (only kind-changing switches and c_w's switches
    are events). So A1 can already re-route there, and R26's step 2 is already written for a moving common prefix.
  - A c_w switch changes A2 = c_w's route only. Kind-B values: Ξ(z) depends on σ along π_z and the constants θ, c_θ (A0); W(z) =
    π_z ⊕ w. Kind-B keys: z's W-play is π_z, o, A1, c_w; the key (SPEC FIX 4: BFS first discovery from the cycle node, = root-first index
    sequence, R24 (b) TB-even) reads c_w ← A1 ← o ← π_z. Neither contains A2. So c_w's switches are invisible to step 2.
- Step 2's choice rule: the switch target is the key-minimum among TIED arena edges (Lemma R + TB). The minimum is not in F (crossing) and
  not kind A (kind change), so it is kind B; the step-5 induction shows z1 is minimal among the kind-B candidates. Correct.
- Step 4's lexicographic comparison with a common prefix reduces to the route parts, which have equal length (|π_z| = ℓ(v) − 1 for every
  tied kind-B candidate). Correct.
- Step 5's induction starts at any step 0 of Γ (S_1 = 0 holds at any start), so CASC-B applies to every kind-change-free part of a
  W-flat segment, not only to maximal ones. Correct.

## 7. CW-INT (§5): SIGNED
- Step 1: a kind-A successor of c_w would close a cycle through c_w avoiding o. Correct.
- Step 2: kind-B values are functions of kind-B σ's (A0), constant without kind-B switches and kind changes. Correct.
- Step 3: R15 (d): Ξ_t(σ_{t+1}c_w) ▷ Ξ_t(σ_t c_w); the new successor is kind B at t+1 (step 1) and so at t (no kind change at t).
  Correct. A switch of c_w never causes a kind change itself (c_w stays kind A; its new successor is kind B), consistent.
- Step 4: strictly increasing values of a fixed valuation on successors: ≤ deg(c_w) − 1 switches. Correct.

## 8. E-SEG (§5): SIGNED WITH GAP KW-1
- KW-1 (counting definition; one-line repair). (i) says N_B(Q) "counts the transitions of Q with a kind-B switch" and bounds it by
  (e(Q) + 1)(r − 2) via CASC-B on the kind-change-free parts. CASC-B says nothing about the e(Q) kind-change transitions themselves, and
  such a transition can contain a kind-B switch (e.g. a kind-B vertex switching to a kind-A successor is both a kind change and a
  kind-B switch). As written (i) is therefore unproved; the proof gives N_B(Q) ≤ e(Q) + (e(Q) + 1)(r − 2).
  - Repair (either): define N_B(Q) as the kind-B-switch transitions WITHOUT a kind change; or define N_cut(Q) := #transitions of Q with
    a kind change or a kind-B switch. Then N_cut(Q) ≤ e(Q) + (e(Q) + 1)(r − 2) ≤ (e(Q) + 1)(r − 1), which is (ii)'s stated bound, and
    (ii)-(iv) and Theorem RUN (c) go through unchanged (they use only N_cut). No instance: in all data post-freeze kind changes are 0
    (§12), so (i) as stated is not contradicted, and it is not needed in its stated form.
- (ii): CW-INT on each of the ≤ N_cut + 1 gaps between cuts, plus ≤ 1 c_w switch per cut transition: ≤ N_cut + (Δ − 1)(N_cut + 1) ≤
  Δ(N_cut + 1). Correct.
- (iii): an event is a kind-changing switch (⊆ the e(Q) kind-change transitions) or a c_w switch. e + Δ((e + 1)(r − 1) + 1) ≤
  (e + 1)(Δr + 1) − 1: checked. Correct.
- (iv): each event-free part of Q lies inside one event-free sub-run of R26 (c) (Q is a contiguous part of one R26 W-flat run; R26's
  setting U3 / U23 is exactly ¬H2, c_w ≠ o, split by the honest frame), whose switches fall at its steps < 2r − 4. Correct.
- (v): KIND-MONO for each vertex of R \ {o, c_w}; o and c_w never change kind. Correct.

## 9. Theorem RUN (§6): SIGNED, note KW-N3
- (S1) from A0: correct.
- (a) LEN-Ξ. (b) "a route-form stretch lies in one piece": TC (i) makes H1, H2 constant on the crossing-free interval, c_θ is constant
  in the phase and w on the stretch; so both route forms are constant; with θ, w constant the stretch is inside one R24 piece (or a U2
  stretch). CASC's induction, like CASC-B's, starts at any step of a W-flat run, so it bounds each post-f0 W-flat segment by r − 2
  switch transitions. Correct.
- (c) Σ_Q (e(Q) + 1) ≤ (r − 2) + (r − 1)(r − 2) + 1 = (r − 1)², and (Δr + 1)(2r − 3) ≤ 2Δr² (2r − 3 ≤ 3Δr). Checked. Total ≤ 3Δr⁴.
- KW-N3 (wording): for r = 1 (R = {o}) the case-(b) expression is negative (r − 2 = −1); the count is 0 there. Read the bounds for
  r ≥ 2, or with max(0, ·). (My probe tripped on this before I clamped it: §12.)

## 10. Corollary KW-S and Corollary PHASE (§7, §8): SIGNED, notes KW-N1, KW-N4
- KW-S (K_W): m* = c_w by LEN-W; m* = c_θ by W-ONCE′ inside a run (no fallback in a run, so a W-changing transition other than the
  first follows a Ξ-changing one of the same run), RUN (a) on R and F1° on F. 1 + (r − 1)² + (n − r − 1) ≤ n². Units: transitions
  (addendum §1), as R26 (b), (d). Correct.
- KW-N4: (E) is stated only as "polynomial". Explicitly, per run of a U3 / U23 stretch with c_w ≻ c_θ: ≤ (r − 1) + Σ_Q E(Q) ≤ (r − 1) +
  (Δr + 1)·(r − 1)², from E-SEG (iii), (v) and the pre-f0 count. Worth one line in the fixes file.
- K: a wake is a relevant Even switch (R27 (e)), so K_t ≤ T_rel; K_s ≤ n·K_t (addendum). Correct; the packet uses only K_t.
- PHASE, step by step:
  1. Theorem LP's first inequality (R27 (d)), any game. Correct.
  2. Relevant transitions: on 𝒞^1O the only relevant Odd change is σ̄(o)'s (S_o); a relevant Even switch has λ(y) ≠ y and (SG) (R19 (d),
     every N5 transition) makes it Ξ-changing. Correct.
  3. Every in-phase transition is a fallback, a stretch boundary, or a run transition; runs ≤ N_st + f. Correct.
  4. F1° per crossing-free interval (≤ n − 1, ≤ X + 1 intervals); RUN with r ≤ n. Correct.
  5. N_st − 1 ≤ X + Θ + W_ch. Correct.
  - Landed bounds, each matched to its RESULTS text: X (R30 (c) SN-PREFIX + R34 (e), (f) with T_H = n² + 2n − 1); Θ (R27 (g) TH; Θ = 0
    when c_θ = o since θ = (o, ∅, 0)); S_o (R27 (g) SO; S_o = 0 when c_θ = o, no relevant σ̄(o) change); W_ch (R24 (e) WC, R19 (a), F1°).
  - KW-N1 (wording): the W_ch split "by TC (i) one of three cases holds" is not a per-interval split: TC (i) fixes H2 on the interval,
    but c_w = o versus c_w ≠ o is a property of w and can change inside a ¬H2 interval. R24 (e) WC is stated for every crossing-free
    interval with ¬H2, so it covers both sub-cases at once; the bound W_ch ≤ (f + X + 1)n² stands.
  - O-forms: X = O(d_o n³(f + n²)), N_st = O(n²(f + X)), N_Ξ = O(Δn⁶(f + X)), T = O(mΔn⁶(f + X)) = O(mΔd_o n⁹(f + n²)). Checked.
- READINGs of §8: with f = O(n²) (FB-POLY) the exponents follow; the assembly needs P-N5-FBPOLY and P-N5-PHI to land. Correct as
  READINGs. Not signed.

## 11. Corner cases (Lead's list), traced through the proofs
- Self-loop at o (o ∈ succ(o)). If τ(o) = o: ¬H2 with c_w = o (W route form, C_W = {o}, B3 vacuous); if σ̄(o) = o: ¬H1 with c_θ = o.
  No proof counts deg(o) except S_o ≤ d_o(Θ + 1), where the self-loop is one of d_o choices. Nothing breaks (cf. FBP-1).
- o = c_θ. A0 terminal θ = (o, ∅, 0); LEN-Ξ length |π_v| ∈ [1, r − 1]; H-PATH's "honest path is π_v" branch; PHASE: Θ = S_o = 0.
- |R| = 2 (R = {o, v}). f0 = k0 + 1; LEN gives 0 changes after f0 (one length value); under ¬H2, C_W = {o, v} and c_w ∈ {o, v}; if c_w = v
  then σ(v) = o is its only route-respecting choice, so no switch on R after f0; E-SEG with r − 2 = 0 and 2r − 4 = 0 is consistent.
- c_w = c_θ. m* = c_θ (tie rule): case (a), LEN-Ξ; FRZ-U's B2 / B3 compare t > m* = c_w directly. PAR and the c_w ≻ c_θ lemmas are
  not entered.
- In data (§12), each corner occurs, including after the freeze.

## 12. Data (DATA, not proof; scratch/kw_probe.py on rl_engine; logs scratch/kw_logs/)
Corpora (𝒞^1O asserted per game; 0 failures of every check in every corpus):
| corpus | runs / evals | log |
| --- | --- | --- |
| (L) P-N5-RHO's 412-file list: 253 𝒞^1O games, SPEC S3 start | 424 runs, 990 phases | kw_logs/lib3.txt |
| (L) + 3 random start pairs per game | 965 runs, 4,194 phases | kw_logs/lib3_rs3.txt |
| 3,000 random 𝒞^1O games, n 6-30 (rl_probe.rand_c1o) | 543 runs (nearly vacuous) | kw_logs/rand3000.txt |
| prep climbs, 3 × 1,500 s (seeds 11, 12 from the 10 library games with U3 / U23 runs, kw_logs/u3_starts.txt; 13 random) | 1.6M evals | kw_logs/climb_u3_1{1,2}.txt, climb_rand_13.txt |
| targeted climbs FIT=thin, 3 × 1,500 s (W-ONCE pairs, post-freeze U3 / U23 length, post-freeze kind changes; seeds 21, 22 as above, 23 random) | 638,217 evals | kw_logs/climb_thin_*.txt |
Checks and counts (library + random starts / all climbs):
- Fact A (FA): 232,611 / millions of vertex-states; Fact B (FB): 1,553,254 pairs in the library run alone.
- MON and FRZ (freeze at k0 + r − 1): 45,120 MON checks; FRZ 1,052 library post-freeze states, ≈ 8.7M in climbs.
- LEN, Theorem RUN per run (case bound with E-SEG's own counts): 965 library runs, every climb run.
- PAR 2,324 / ≈ 5.1M states; H-PATH 10,590 / ≈ 21.9M vertex-states.
- CW-INT: 375,424 + 38,007 c_w switches inside windows (whole runs, the lemma has no freeze hypothesis); CASC-B: 687,103 kind-B switches.
- E-SEG (i) AS STATED (N_B over all kind-B-switch transitions): 293,621 post-freeze W-flat segments, 0 violations (vacuous for KW-1's
  case: no post-freeze kind change occurs).
- KW-S (K_W per stretch, runs per stretch ≤ f_st + 1): 14,466 / ≈ 3.1M stretches; max K_W 40 (library).
- Corollary PHASE, every inequality (LP, T_rel, N_Ξ, N_st, W_ch, X, Θ / Θ = 0, S_o): 4,194 / ≈ 2.77M phases. Library maxima: T 112,
  T_rel 112, N_Ξ 112, N_st 109, X 100, S_o 49, f 33.
- Corners: runs with a self-loop at o 223 (96 reach the freeze), o = c_θ 68 (32), |R| = 2 86 (49), c_w = c_θ 704 (228) in the library
  with random starts; all four occur in climbs too.
VACUOUS or THIN in my data (the statements rest on their proofs, checked above):
- KIND-MONO: 0 post-freeze kind changes, over 2,455,342 post-freeze transitions of U3 / U23 runs with c_w ≻ c_θ in the targeted climbs
  (as the packet's §10 says for its own data).
- W-ONCE: 2 checks (library); on my engine Ξ-flat S4a transitions are rare (7 of 5,336 in-phase S4a steps of the library) and the
  targeted climbs did not raise them. The lane's 0.85M checks come from REFEREE-2's tracer; I did not re-run them.
- Freeze delay (KW-N5): over runs that reach k0 + r − 1 the largest actual delay is 1 (FRZD_postrun_max), as the packet's §10 says.
  Over all runs it reaches the bound: κ changes at step 40 of a 40-transition run on experiments/red/xing/instances/kw_n48.pg (r = 48;
  also kw25_n32 25, block_bk32 21). Both are within FRZ-U; the packet's line is a statement about its measure (kwcheck.py l. 60-68).
- Probe artefact (no finding): with r = 1 my first RUN bound went negative (KW-N3); clamped, re-run.

## 13. Notes and gap for the fixes file (one line each)
- KW-1 (E-SEG (i)-(ii)): define N_cut(Q) := #transitions of Q with a kind change or a kind-B switch (or N_B without kind changes); then
  N_cut ≤ (e + 1)(r − 1) and (ii)-(iv), RUN (c) are unchanged.
- KW-N1 (PHASE, W_ch): cite R24 (e) WC for every ¬H2 interval; drop "by TC (i) one of three cases".
- KW-N2 (LEN): the length range is the whole honest (W) length to the cycle node, in [1, r − 1].
- KW-N3 (RUN): bounds for r ≥ 2 (count 0 for r = 1).
- KW-N4 (KW-S): (E) per run ≤ (r − 1) + (Δr + 1)(r − 1)².
- KW-N5 (DATA): the freeze-delay line of §10 is the max over runs that reach k0 + |R| − 1 (kwcheck.py l. 60-68); over all runs it is
  r − 1-tight (§12).
