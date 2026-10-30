# R2-N5-WCH: independent second-referee report on P-N5-WCH (REFEREE-2 successor 22, Opus 5.5, D15)
Object: docs/new/P-N5-WCH-box79.md @ l-new 2ad78f51 (sha1 31caa72e5265b7373218ce64e38d253112189506, 550 lines); line
docs/new/P-N5-WCH-box79-line.txt (sha1 9ac6fdba5ca5910a4585babff5938a0d8d107a78). Both re-hashed here in a detached worktree at 2ad78f51:
match. Independence: written before opening any docs/referee/ file for this packet; the names-only count of «wch» in docs/referee/ was 0 at
the start (10:0xZ). Landed sources re-read:
- RESULTS R90's entry and its object P-N5-CUT-box43.md §1-§4: OPT-OFF, W-MON′, W-SUCC, W-RETURN-G, CUT-CHARGE classes;
- RESULTS R91's entry: (a) XW, (b) W-MON in the S4a-step form, (c) FB-W, (h) GAP-MON, (i) SW-IN, (k) REOPEN-W, (m) GAP-RED;
- RESULTS R15 (a), (d), R56, R57, R88 / R89 definitions;
- SPEC docs/new/N5-ssi-global.md l. 24-57.
Owner rulings applied: D1 «Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.»; D18 «Clearly
distinguish proven results from conjectures and open problems.»
Scope: a REDUCTION. [P-WCHτ], TIE*, NZ, ZFS, FBOS, NC, NT, ρ_P and B_R are not bounded. G-N5-TIME stays OPEN. Not M3, not a step-4 pass,
not a TARGET.md claim. N5 (§2-§6) and the VARIANT N5-LZC (§7) are separate objects; I checked them separately.

## 1. Verdict table
| § | item | verdict (Opus 5.5, D15) | gaps / notes |
| --- | --- | --- | --- |
| 2.1 | Fact REW (R1, R2), Fact LEX, COMMON PREFIX | SIGNED | none |
| 3 | Lemma TIE (a), (b) | SIGNED | none; N-1: the case split (a2) / (a3) must be read as «v reached after / before c* on π» (wording) |
| 4.1 | Lemma NEW-BOUND | SIGNED | none |
| 4.2 | Theorem RET-WCH (Step 1 tie-leave, Step 2 (i)-(iii), distinctness) | SIGNED | none; N-1 again for Step 2 (ii) / (iii) |
| 4.3 | Corollary RUN-WCH, Corollary REP-WCH | SIGNED | none; REP-WCH uses only R90 (g)'s definitions and RET-WCH, not FW-R*′ (N-3) |
| 5.1 | Lemma SIL-Z (a)-(c), Corollary SC-GXC | SIGNED | none; every premise is landed (R90 (a) (ii), (b)-(e), R91 (a), R15, SPEC S2, S4a, [V1], [V2]) |
| 5.2 | Lemma GXC-CLOSE, Theorem GXC-SPLIT | SIGNED | none |
| 5.3 | Lemma LEVEL-MON, Corollary DROP-PAID | SIGNED | none |
| 5.4 | Corollaries FBO-R56, FBO-SPLIT, ZF-SPLIT | SIGNED | none |
| 6 | Theorem WCH-RED (W), (G), (X), (S); Corollary WCH-ONE | SIGNED (composition and arithmetic checked) | none |
| 7.1-7.4 | N5-LZC: definition, LZ-OPT, W-MON_LZ, LZ-STRICT, RUN-WCH_LZ / REP-WCH_LZ | SIGNED (VARIANT; nothing transfers to N5) | none |
| 7.5 | Corollary LZ-NOSIL under ASSUMPTION OPT-ONLY | SIGNED as the implication; OPT-ONLY CHECKED: it holds (§2.7 below) | N-4 |
| 8 | trimmed items, DATA, READING, lane symbol table | not signed | DATA reproduced (§4) |
| line | 9ac6fdba | MATCHES §2-§7 | no REQUIRED fix; precision L-1 to L-4 (§3) |
| quotes | 35 «» quotes | all verbatim | N-2: four SPEC line tags (S1-rank, S1-val, S1-ord, S1-Xi) are one line low |

No gap. Nothing FALSE. No REQUIRED fix.

## 2. The items, as I checked them
### 2.1 Facts
- R1: rew(u) = p′(u) > p′(x) ≥ rew(x). R2: rew(x) = −p′(x) < −p′(u) ≤ rew(u). LEX: for one cycle node, the signed weight is Σ_r s_r 2^r with
  s_r ∈ {0, ±1} of the fixed parity of rank r, so |s_r − s′_r| ≤ 1 and the top differing rank decides (Σ_{r<R} 2^r = 2^R − 1). The order is
  lexicographic in CS, so COMMON PREFIX holds. Checked mechanically: CS order = SPEC key order on 0 of the sampled pairs failing (§4).
### 2.2 Lemma TIE
- (a) The proof is correct with one reading point (N-1). π is d's σ⁺-play.
  - (a1) π never visits v.
  - (a2) As written, «v lies on π's cycle». Its argument uses «π's path to c* avoids v», which holds only when π reaches c* before v.
  - (a3) As written, «v lies on π's path part», that is, before c*: the [S1-val] «path» is the segment before reaching c.
  - So the true partition is: (a1) π never visits v; (a2) π reaches c* before v (v on the cycle after c*); (a3) π reaches v before c*,
    whether v is on the tail or on the cycle before c*.
  - (a3)'s argument never uses that v is off the cycle: c* ∉ X, the ρ-cycle X, its top u, and the two sub-cases. So it covers v on the
    cycle before c* too.
  - With that reading, every step checks: [V1], [V2] hypotheses (paths avoid v), [F1] in H, R1 / R2. Both sub-cases of (a3) are
    contradictions. In (a3) the top u may be v itself (v ∈ X); the argument «u ∉ P(W(d))» covers that, since d's σ_t-path avoids v.
- (b) Correct: π not visiting v forces a different cycle node and W′(d) ◁ W(d) against [F1]; otherwise λ(W′(d)) = v and a non-empty P(W′(d))
  would have an even top above v, giving val_ρ(v) ▷ W′(v).
### 2.3 NEW-BOUND, RET-WCH, RUN-WCH, REP-WCH (the Lead's «tie-leave cases»)
- NEW-BOUND: every transition of F switches some Even vertex (Fact B; no fallback, τ constant). Per Even edge at most one NEW switch, none to
  σ_a(v). Correct.
- RET-WCH. If v is its own W-cycle node on F (λ_W constant), W(v) never changes, so every leave is TT. Otherwise c := λ_W(v) is fixed.
  - Step 1 (tie-leave): v ⊕ W_{k+1}(e) = W_{k+1}(v) together with W_k(v) = v ⊕ W_k(e) ([V1], σ_k(v) = e) forces W_{k+1}(e) ≠ W_k(e) when
    W_{k+1}(v) ≠ W_k(v). So W(e) changes at s = k.
  - Step 2: assume W(e) is constant on [k + 1, u + 1].
    - (i) π misses v: [F1] gives v ⊕ W_{k+1}(e) ◁ W_{k+1}(v).
    - (ii) v on the cycle after c (N-1 reading): with P(W_{k+1}(e)) = ∅ the ρ-cycle tops at c, and [F1] gives ◁; otherwise the top u′ is odd,
      by R1, and ◁ follows.
    - (iii) v before c on π: «v more relevant than c» is impossible, since e's σ_{u+1}-play would contain v on its cycle above c. The two
      sub-cases on u* are contradictions, by W-MON (R91 (b)) over the S4a steps [k + 1, u] and by [F1] / R2.
    - Closing chain: W_{u+1}(v) = v ⊕ W_{u+1}(e) = v ⊕ W_{k+1}(e) ◁ W_{k+1}(v) ⊴ W_{u+1}(v), a contradiction.
  - The cases are exhaustive: the leave k exists inside F, and «W_{k+1}(v) ≠ W_k(v)» splits into Step 1 or Step 2. The rest are TT.
  - Distinctness: k₂ ≥ u₁ + 1, so the intervals [k, u] are disjoint.
  - Correct. The Lead's «tie-leave cases»: Step 1 and the TT residual together cover every return; no case is missing.
- RUN-WCH: Σ_e TT_F(v, e) ≤ TIE_F(v) (one leave per switch; a TT leave is a TIE event at an S4a step of F). REP-WCH: a REPEAT of R90 (g) is a
  return (σ_{u₁+1}(y) = z, u₁ + 1 ≤ u₂, σ_{u₂}(y) ≠ z). Neither uses FW-R*′ or any unlanded item (N-3). Correct.
### 2.4 SIL-Z and SC-GXC («from landed R90 only»)
- The packet's class S matches R90 (e) / CUT-CHARGE (P-N5-CUT §4) exactly: not F, an anchor exists (not FR), smallest anchor q, v off-cycle
  for τ* on [q, j] (not C), W*(c) constant on [q, j] (not P).
- (a) The chain is a cycle of landed links whose ends coincide, so every link is an equality:
  - R90 (a) (ii) at q − 1 → q;
  - (c) W-SUCC on [q, j − 1], with off-cycle on [q + 1, j − 1] ⊆ [q, j];
  - (b) W-MON′ at j − 1 → j;
  - (d) W-RETURN-G, its hypotheses being exactly class S;
  - constancy of W*(c).
  - Then [V1] at j − 1 and j gives W*_j(v) = W*_{j−1}(v).
- (b) [S2], R91 (a) XW, [V1], strict [V2]. (c) R15, [S2], [V1], [V2]. All landed. Correct.
- SC-GXC: a class-S re-entry outside NC and NT is GXC verbatim (τ kept, so W* = W). A GXC event lies in one phase. R's phases are cut only by
  τ-changes, which are boundaries, so there are ≤ B_R + 1 of them. Correct.
### 2.5 GXC-CLOSE, GXC-SPLIT, LEVEL-MON, DROP-PAID, FBO-R56, FBO-SPLIT, ZF-SPLIT
- GXC-CLOSE: exits ≤ [x ∈ Z_a] + entries; there are no entries at in-phase fallbacks (R91 (h)), and an entry at an S4a step is a W-rise
  (R91 (k)). GXC-SPLIT: at an S4a step W-MON makes the GXC event a TIE event; otherwise it is CL or FBO. Correct.
- LEVEL-MON: Ξ_t ⊴ Ξ_{t′} (R15) ⊴ W_{t′} (XW) ⊴ W_t (no S4a W(v)-change between; FB-W at fallbacks; R91 §1's in-phase dichotomy), then
  COMMON PREFIX twice. DROP-PAID: at most 1 + WCH^S4a_P(v) segments, LEV non-decreasing within each, values in {1, …, n + 2}. Correct.
- FBO-R56: ≤ n_E switched vertices per in-phase fallback, then R56. FBO-SPLIT, ZF-SPLIT: SW-IN (R91 (i)) puts v ∈ Z_k, Z-flatness puts it
  in Z_{k+1}, and LEVEL-MON with t′ = t + 1 gives the DROP. Injective. Correct.
### 2.6 WCH-RED and WCH-ONE
- (W), (G), (X), (S) are the stated items composed. WCH-ONE: a W-run's transitions and a phase's in-phase S4a transitions are S4a steps
  inside one τ-stretch, so WCH_F(e), WCH^S4a_P(v) ≤ WCH_S(e). The arithmetic follows: Σ_e d_E(e)·w = m_E·w; |Z_a| ≤ n; Σ_v over n vertices.
  Correct.
### 2.7 N5-LZC (VARIANT) and OPT-ONLY
- LZ-OPT: every step of σ′ and τ_t is W*-consistent:
  - kept steps by the rule;
  - σ* and τ_t steps by [V1] for (σ*, τ_t), or by the top-of-cycle argument at ℓ = 0.
  - A consistent step lowers ℓ by 1 at a fixed cycle node, so x reaches c without repeats. From c, the consistent cycle has empty path sets,
    so all its vertices lie below c. So val(σ′, τ_t) = W*. Correct.
- W-MON_LZ ([F1]) and LZ-STRICT: Lemma TIE applies verbatim to σ⁺ := σ′, since its proof uses only [F1] for σ⁺, σ_t ∈ H, ρ ∈ H, [V1], [V2]
  and R1 / R2. Its two conclusions are exactly the keep rule's two clauses, so a switched v cannot tie. Correct.
- RUN-WCH_LZ / REP-WCH_LZ: §4's proofs, re-read with every premise re-proved for N5-LZC. Correct.
- OPT-ONLY (the referees were asked to check it): I read the landed proofs in R90's object, P-N5-CUT §2-§4.
  - OPT-OFF (ii) (Cases 1-3), W-MON′, W-SUCC and W-RETURN-G use (i) (pointwise optimality of σ_{t+1} in H_t against τ_t), each other,
    [V1]-type play facts and [S1-ord]. Nowhere do they use the S1 procedure or its tie-break; only (i)'s own proof does.
  - LZ-OPT supplies (i) for σ′.
  - Fact B uses [S4a]-[S4c] and R15 (d). σ′ differs from σ_t only at vertices where it takes σ*(v) ∈ A(v) ∖ {σ_t(v)}, that is, along
    improving edges. S4c fires exactly when σ′ = σ_t and τ_new = τ_t.
  - So OPT-ONLY holds for N5-LZC, and LZ-NOSIL holds without the assumption.
  - I recommend the line keep the label as is: the assumption is discharged by this report, not by a landed proof.
- No OPT-ONLY use in the N5 part: «OPT-ONLY» occurs only in §0 l. 27, §7.4's title («no OPT-ONLY»), §7.5 and §8.1. §2-§6 never use it.

## 3. My strict symbol test of the line file (by hand, every symbol and index; before reading the lane's §8.5)
| symbol | binder | verdict |
| --- | --- | --- |
| N5, SPEC S1-S5, 1E-N3, R57 | named, landed | bound |
| H_t, σ_t, τ_t, Iσ_t, run, transition, «switched» | in the line | bound |
| ⊴ ◁ ⊵ ▷, «more relevant», rank, reward | SPEC S1 | bound |
| n, n_E, m_E, d_E(e) | in the line | bound |
| Ξ_t, λ_Ξ, W_t, W(v), λ_W, «own Ω-cycle node» | in the line | bound |
| Z_t, τ-stretch, W-run, F, \|F\| | in the line; R89 | bound |
| phase, in-phase, f_P, ZF_P, WCH^S4a_P(v) | R38 (a), R91 | bound |
| λ-run, S4a steps, boundaries, B_R, class-S, SIL_R | R86, R90 (e) | bound |
| late adoption, REPEAT, REP_F, REP* | R88 (f), R90 (g); «REP* := max_F REP_F» | bound |
| ρ_P | «RESULTS R56's ρ of the phase P» | bound |
| σ⁺, W′, d, v, ⊕, (c, Q, ℓ) | Lemma TIE's clause | bound |
| e, returns, WCH_F(e), TT_F(v, e), k, u | RET-WCH's clause | bound |
| TIE_F, TIE_P, TIE* | in the line | bound |
| GXC event, GXC_X, X, NC_R, NT_R, R, P (phases inside R) | SC-GXC's clause | bound |
| a (first state of P), \|Z_a\|, FBO_P | GXC-SPLIT's clause | bound |
| LEV_t(v), coordinate sequence, t < t′, DROP_P(v), FBOS_P, ZFS_P | in the line | bound |
| k in NZ_P's «at k or k + 1» | not bound in that clause; the only binder is ZF_P's gloss «those k → k + 1 with Z_{k+1} = Z_k», another clause | L-1 (precision) |
| w, w(n) | «at most w(n) … (premise [P-WCHτ](w))»; w is never declared a function ℕ → ℕ | L-2 (precision) |
| S (τ-stretch), e | «every τ-stretch S … for every vertex e» | bound |
| σ*, σ′, W*, N5-LZC | the VARIANT clause, by reference to Lemma TIE's two forms | bound; L-3 (precision) |
| OPT-ONLY | «under ASSUMPTION OPT-ONLY that RESULTS R90 Fact B and (a) (ii), (b), (c), (d) hold verbatim for N5-LZC runs» | bound |
| distinct triples distinct (equality from ⊴ both ways) | RESULTS R84 (a) Fact DELTA, used by the packet (§1 l. 41), not in the line's premise list | L-4 (precision) |
- The line MATCHES §2-§7:
  - Lemma TIE is stated without the «path avoids v» half, a weakening that is allowed.
  - RET-WCH, NEW-BOUND / RUN-WCH / REP-WCH, SIL-Z / SC-GXC, GXC-CLOSE / GXC-SPLIT, LEVEL-MON and its corollaries, WCH-RED / WCH-ONE and the
    N5-LZC items each equal their packet statements.
  - The scope tail matches §6's last paragraph.
- L-1 to L-4 are precisions. None is required: k's clause-local meaning is unambiguous, w is fixed by «[P-WCHτ](w)», σ′ is pinned by «in the
  sense of Lemma TIE's two forms», and Fact DELTA is landed.

## 4. Pins re-run, and my own engine as a control
- Pin: experiments/new/check.sh «box 79» (my extraction of the w30 block, set -euo pipefail, detached worktree at 2ad78f51): PASS, exit 0
  (wchpk.py on tog6b_n32 for N5 and N5-LZC, and symtest.py «SYMTEST PASS»).
- Quotes (my own script, normalised whitespace, «…» split):
  - 35 «» quotes in §0-§7; every one is verbatim in SPEC, RESULTS.md, or the cited objects (P-N5-GAP-box69.md, P-N5-GP-box31.md,
    N5-phase-bound-box10.md). The exception is the Lead's brief quote at l. 2-3, a message.
  - SPEC tags: S2 (l. 47), S4a (51-53) and S4c (56-57) are exact.
  - S1-rank «SPEC:26», S1-val «27-28», S1-ord «29-30» and S1-Xi «31» are each one line low. The text sits at l. 27, 28-29, 30-31, 32, as
    R90's object cites it at 7039eb524 (N-2).
- Own engine: docs/referee-2/R2-N5-WCH/wch_check.py.
  - N5 loop: my lane's R2-N5-DUAL/dual_check.Runner on si.py.
  - N5-LZC loop: my own subclass, the keep rule coded from §7.1.
  - The lane's box79 / box78 scripts are NOT imported. The R90 (e) classes (anchors, smallest anchor, τ*-pieces, C / P / S) are computed
    from P-N5-CUT §3-§4's text.
  - Its checks, each 0: LEX; TIE (a), (b); NB; RW and RW1; RUN; REP; SZa-SZc; SCG; SC; GC; GS; LM, on ALL pairs t < t′ of a phase, not only
    consecutive ones; DP; F56; FS; ZS; GR. For N5-LZC: LZO, LZS, LZT, LZN.
- Pinned reproduction, tog6b_n32 from S3:
  - N5: returns 4, paid by a W(e)-change 3, TT 1, TIE 2 (= the pin).
  - N5-LZC: returns 3, paid 3, TIE 0 (= the pin).
- Corpus = the lane's: box59/sbcg.lst (719, S3) + si/root/logs/alt_all.lst (413: 93 valid start files; 319 lines without a start file run
  from S3 (files mode with runs = 0 skips them, so they were run separately); 1 invalid start file skipped (comp54_n80, non-edge 11 → 51)):
  1,131 runs per engine. Detached worktree at 2ad78f51. 0 violations on every check, both engines.

| engine | runs | transitions | W-runs | returns | paid by W(e) in [k, u] | TT | TIE (W-runs) | max returns per (F, edge) | class S | S not GXC | NC / NT | GXC | CL / FBO / FBOS | DROP | ZF / NZ / ZFS | REP* max | max WCH_S(e) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N5 | 1,131 | 21,790 | 8,941 | 6,246 | 6,158 | 88 | 397 | 17 | 84 | 0 | 0 / 0 | 3,602 | 2,985 / 232 / 196 | 4,690 | 112 / 59 / 44 | 6 | 48 |
| N5-LZC | 1,131 | 21,487 | 8,892 | 6,081 | 6,081 | 0 | 0 | 17 | 0 | — | 0 / 0 | — | — | — | — | 6 | 48 |
- Against the lane's §8.4 (1,132 runs):
  - N5: returns 6,265, paid 6,177, TT 88, TIE 397, max 17;
  - N5-LZC: returns 6,100, all paid, TIE 0.
  - TT, TIE and the maximum equal mine exactly. Returns and paid differ by exactly 19 on both engines: that is the one game I skip (invalid
    start file). The lane's start_pair accepts it, and its run starts from a state with a non-edge.
  - The lane's «W-runs 1692 / 1658» is a different unit (W-runs of length ≥ 1 that hold a return, by its sumpk.py), not a disagreement.
- Lemma TIE's hypothesis W′(v) = W(v) met at 541 switched vertices, all (a) / (b).
  - Control: dropping the hypothesis, (a)'s conclusion fails at 56,743 of 57,628 switched vertices (X_TIE_noeq).
- LEVEL-MON: 6,431,809 pairs checked. Control: read across an S4a W(v)-change, LEV decreases 26,107 times (X_LM_s4a), so the hypothesis bites.
- LZ-OPT: val(σ′, τ_t) = W* at all 20,845 N5-LZC S4a steps.
- LZ-NOSIL's conclusion: 0 class-S re-entries in N5-LZC (84 in N5).
- [P-WCHτ]'s w in the data: max WCH_S(e) = 48 on both engines (DATA only).

## 5. Notes (N-items; none is a gap)
- N-1 (§3 (a2) / (a3); §4.2 Step 2 (ii) / (iii)). Read «v lies on π's cycle» as «π reaches c* (c) before v», and «v lies on π's path part»
  as «π reaches v before c* (c)», the [S1-val] meaning of «path». With the literal tail / cycle reading, (a2) and (ii) would claim «π's path
  to c* avoids v» for a v on the cycle before c*, which is false. (a3) and (iii) cover that case unchanged. One clause each in a fixes file.
- N-2. Four SPEC line tags are one line low; the quotes are verbatim.
- N-3 (the Lead's watch item). REP-WCH needs only R90 (g)'s FIRST / REPEAT and R88's late adoption. FW-R*′ (R92) is neither used nor needed.
- N-4 (§7.5). OPT-ONLY holds (§2.7). The packet may keep the label; this report discharges it for the implication, and the CHECKER may
  record it.
- N-5 (§8.5, the lane's symbol test). symtest.py checks that each token has some binding phrase somewhere in the line. It cannot see a
  clause-scope slip like L-1, so it is not a substitute for the by-hand test.

## DONE / FINDINGS / NEEDS
- DONE: this report; docs/referee-2/R2-N5-WCH/wch_check.py; pin «box 79» PASS (exit 0); quote check.
- FINDINGS:
  1. Every item of §2-§7 SIGNED (Opus 5.5, D15); no gap, nothing false, no REQUIRED fix.
  2. OPT-ONLY checked and true: LZ-NOSIL holds; the N5 part never uses OPT-ONLY.
  3. N-1: the case split in Lemma TIE (a2)/(a3) and RET-WCH (ii)/(iii) must be read «before / after the cycle node» (wording).
  4. Line MATCHES; precisions L-1 (k in NZ_P), L-2 (w undeclared), L-3, L-4.
  5. N-2: four SPEC line tags off by one.
- NEEDS: Lead: route N-1, N-2, L-1..L-4 to L-NEW (fixes file); the §C word after REFEREE 19's report.
