# R2-N5-FRAME: REFEREE-2 report on packet P-N5-FRAME (L-NEW box 65): Odd-side freeze and fixed-τ stretch reductions for N5
Referee: REFEREE-2 successor 21, Opus 5.5 (D15, L37; D1 "Never downgrade the referee to save money"), independent second referee.
Written 2026-10-29 from 20:58Z (date -u).

**Object.**
- docs/new/P-N5-FRAME-box65.md at l-new 938d87967ce501058bc6d015e506403c73858034: sha1 ce8c4803ee18dc90ee761863d006d0aca0476542, 194 lines
  (`git show 938d8796:<path> | sha1sum`, `| wc -l`); equal to the Lead's figures. 938d8796 is an ancestor of origin/claude/l-new.
- Approved RESULTS line docs/new/P-N5-FRAME-box65-line.txt at origin/claude/l-new: sha1 acf3234f84cb682d71444501e89cfd61247dcd6 (= the Lead's).
- Premises read in context: SPEC S1-S5 (docs/new/N5-ssi-global.md @ 9905dac3, l. 20-60); RESULTS R15 (a), (c), (d); R17 (a); R47 (a);
  R56 (headline and setting); R85 (c); R86 (headline and body (e), l. 5345-5357); R88 and its object docs/si/P-N5-GP-box31.md @ d072bb28
  (sha1 cd4866df…, §1-§4 in full, line by line for §3.3).

**Independence.** `git ls-tree --name-only -r origin/claude/referee docs/referee/ | grep -ic frame`: 0 at 20:58Z (handover), 16 at 21:21Z and 21:36Z
(after a fresh fetch; names only, no file opened, no `git log` on origin/claude/referee). REFEREE 18 reviews in parallel; I have not seen
its report. The lane's box59 / box62-box65 scripts were RUN only as the pinned check (experiments/new/check.sh in a detached worktree at
938d8796, logs/pinned_check.txt) and never imported. My control is my own code: R2-N5-FRAME/frame_check.py on my lane's
R2-N5-DUAL/dual_check.Runner (SPEC N5 on si.py, read-only) and R2-N5-MATCHPHI's matcher.

**Scope (D1, D18).** A REDUCTION for plain N5 on every game. Nothing here bounds N5's iteration count: NM^U on unprotected targets, R*_S,
FL_S and ρ_S are unbounded. G-N5-TIME stays OPEN. Not a TARGET.md claim, not M3, not a gauntlet pass.

## 0. Verdicts (all "(Opus 5.5, D15)")
| § | item | verdict |
| --- | --- | --- |
| 1 | setting, premises, new definitions | well formed; 9/9 quotes verbatim (own fquote.py; SHIFT=1 control 0/9); every cited RESULTS item says what the packet uses (§1) |
| 2.1 | Lemma FRAME-τ (i)-(iv) | SIGNED |
| 2.2 | Lemma DUAL-ORDER | SIGNED |
| 2.3 | Lemma ODD-FREEZE (H1′, H2, H3) | SIGNED (every inequality direction checked, §2.3; the optimality step is R57 (a) (VJ) on G^d: N-FR-2) |
| 2.4 | Lemma ENT-FREEZE | SIGNED |
| 2.5 | Corollary COMPOSE-FREEZE (a)-(e) | SIGNED. (e)'s premise [R86e] ACCEPTED as a premise: it IS displayed in RESULTS (R86 headline and body (e)); no re-proof needed (§2.5, N-FR-1) |
| 3.1 | Lemma SUCC-MON | SIGNED |
| 3.2 | Lemma LATE-RISE | SIGNED |
| 3.3 | Lemma GP*-RUN | SIGNED. R88's proofs (W-MON, GP* all cases, FW-R*) checked line by line: no step uses σ̄, D or λ_Ξ constant (§3.3) |
| 3.4 | Corollary R*-RISE | SIGNED |
| 3.5 | Theorem STRETCH-RED, with its "Consequence (to sign as stated)" | SIGNED (fallback count correct when τ is constant: §3.5, N-FR-5); Consequence SIGNED |
| 4 | READING, DATA | not signed. Pinned checks reproduced: all PASS at 938d8796; dw_3 figures reproduced by my own code (§4.1) |
| — | approved RESULTS line (acf3234f) | MATCHES §2-§3 in content and claims nothing beyond them, but two symbols are undefined in it: **Q** (required fix: read with Q unspecified, "Q ≤ …" can be taken as Q = 0, and that reading is FALSE on data, §5) and NM^U_R(e) (precision fix). N-FR-7 |

No gap. No item FALSE. Notes N-FR-1..N-FR-10 (§6).

## 1. Premises
- Quotes. The packet's nine «» quotes ([Q SPEC:28-29], 30-31, 32, 45-46, 47, 51-53, 54-55, 56-57 at 9905dac3; [R85c] RESULTS
  l. 5108-5109 at c9045f86) are verbatim (whitespace-normalised substring of the cited lines): logs/quotes.txt 9/9; SHIFT=1 0/9.
  The unmarked «» citations are also verbatim at c9045f86: R17 (a) F1 (l. 738-739, across a line break), R15 (d) «Iσ depends on σ alone»,
  R56's headline, and R86's two referee cells «MΦ's proof reads verbatim with c fixed» and «MATCH-Φ's proof holds for every parity
  pattern».
- R47 (a) (c): «at most n(n − 1) transitions change λ and at most n(n − 1) change λ^U» (every game). ✓ as [R47a] uses it.
- R56: phases as R38 (a) KEY (maximal (λ_Ξ, τ)-constant runs); its fallbacks are the in-phase Even S4c fallbacks; ρ := the pairs
  (transition of the phase, Odd q of out-degree ≥ 2) with Ξ(q) changing. ✓ as [R56] uses it.
- R86: ENT_R, RISE_R, PCH_R per stretch R; SW-RETURN on every stretch; LEN-MONO on every λ-run, dually on λ^U-runs. ✓

## 2. The Odd side
**2.1 FRAME-τ.**
- (i) is S4a's arena verbatim.
- (ii) S4b: τ_new is chosen in H′, where Odd o keeps only {τ(o)} ∪ Iτ(o). Otherwise τ_new = τ. S4c's Odd branch picks from Iτ; its Even
  branch leaves τ. ✓
- (iii) Each τ-change is Switch_I(τ) with I = the changed vertices' new edges, ∅ ≠ I ⊆ Iτ, unambiguous (R15 (d)). R15 (c) on G^d: no
  strategy recurs in any such sequence. The τ-changing transitions form one. ✓
- (iv) Iτ is read from Ξτ on G^d, which depends on τ alone. ✓
- Data: FT2 (every Odd o, every transition), FT3 (no τ recurs), FT4 (equal τ ⇒ equal Iτ): 0 violations (§4).

**2.2 DUAL-ORDER.**
- rank is the position in the (Ω, v) order. Ω + 1 preserves that order, so ranks, relevance (max p′ ⇔ max rank) and the triples agree in
  G and G^d.
- Each of the three components reverses:
  - reward: same parity in G ⇒ the opposite preferences on relevance in G^d; mixed parity ⇒ each side prefers its own;
  - signed weight: every term flips sign;
  - length: its rule depends on c's parity, which flips.
- The order is lexicographic and each component reverses, so the whole order reverses. Distinct triples are distinct (R84 (a) DELTA), so
  strict and non-strict forms both reverse. ✓
- Data (DORD): on every pair of distinct values met at a state (Ξ, U and W values), G's key order is the exact reverse of G^d's; 0
  violations. Engine ranks equal in G and G^d. (Pairs are sampled above 5,000 per state; counted.)

**2.3 ODD-FREEZE: the directions (Lead's point (2)).** Write ⊴ for G's order and ⊴^d for G^d's.
1. The (τ, σ_e)-play from e is P_e followed by the (τ, σ_e)-play from τ(o) (o is Odd and follows τ). The (τ, τ̄)-play from τ(o) avoids
   P_e (H2), and σ_e = τ̄ off P_e. By induction along it, the (τ, σ_e)-play from τ(o) is π_o = the (τ, τ̄)-play from τ(o): value U(τ(o)),
   cycle node w ∉ P_e. ✓
2. The full play from e: its cycle node is w, its path set P_o ∪ {y ∈ P_e : y more relevant than w} (a disjoint union), its length |P_e| + ℓ_o.
   The two path sets differ exactly in {y ∈ P_e : y ≻ w}. Its top is x, of even Ω (H3), so the signed weight rises by +2^rank(x) − (lower
   terms) > 0. **val_{σ_e}(e) ▷ U(τ(o))** in G's order. ✓
3. τ̄ minimises G^d's order at every vertex over Even's (G^d-Odd's) replies to τ: SPEC S1-dual with S1-Xi, i.e. R57 (a) (VJ) on G^d, as
   R85 Fact B2 cites it (N-FR-2). So U(e) ⊴^d val_{σ_e}(e) (σ_e is one positional reply, and the triples are the same in G and G^d), and
   by DUAL-ORDER **U(e) ⊵ val_{σ_e}(e)** in G's order. ✓
4. Chain: U(e) ⊵ val_{σ_e}(e) ▷ U(τ(o)), so U(e) ▷ U(τ(o)) in G, i.e. U(e) ◁^d U(τ(o)) (DUAL-ORDER): WORSE for τ's owner on G^d.
5. S2 on G^d puts (o, e) in Iτ only if U(e) ▷^d U(τ(o)) (strictly better for the G^d-Even player, who owns τ). That fails. **(o, e) ∉ Iτ.** ✓
- Every inequality points the right way. The only premise beyond SPEC's text is (VJ) (step 3).
- Edge cases checked:
  - e = o (a self-loop): P_e = (o), and the proof is unchanged.
  - (H2) includes τ(o) itself, because P_e contains o.
  - (H1′) is equivalent to the existence of a simple path from e to o in G_τ (Odd vertices other than o follow τ, Even vertices free). σ_e
    can be taken as that path on P_e and τ̄ elsewhere, and the play up to o never meets a vertex off P_e (N-FR-3).
- Data:
  - OF: no protected edge is in Iτ, at every state of every run and on EVERY τ of 1,650 small random games (alltau mode, 27,435 τ).
  - OF_mid and OF_opt, the two inequalities of steps 2 and 3, hold on the witness at every hit.
  - OFBF: my path search and a literal brute force over ALL positional σ_e (the definition of (H1′)) agree on every Odd edge for n ≤ 7-8.
  - Controls: dropping (H3)'s "even" or (H3)'s "more relevant than w" bites thousands of times. Dropping (H2) NEVER bites (N-FR-4).

**2.4 ENT-FREEZE.** ODD-FREEZE at t gives (o, e) ∉ Iτ_t. FRAME-τ (ii) gives τ_{t+1}(o) ∈ {τ_t(o)} ∪ Iτ_t(o). e is neither, because
τ_t(o) ≠ e. ✓ Data EF: 0.

**2.5 COMPOSE-FREEZE.**
- (a) An entry at t → t + 1 inside R needs τ_t(o) ≠ e = τ_{t+1}(o). If (o, e) ∉ UNP_R, it is protected at t, and ENT-FREEZE excludes the
  entry. ENT_R counts transitions with both ends in R, as R86's "transitions of R" (|𝒫| is defined that way there), which matches UNP's
  "t + 1 ∈ R". ✓
- (b) SW-RETURN (dual, every stretch): ENT_R(o, e) ≤ 1 + RISE^U_R(e). LEN-MONO (dual, λ^U-run): RISE^U ≤ PCH^U + (PCH^U + 1)(n − 1). Then
  1 + PCH + (PCH + 1)(n − 1) = n(PCH + 1), an equality. ✓
- (c) Each Odd switch enters exactly one e: Σ_o SW = Σ_{(o,e)} ENT. Then (a) and (b). ✓
- (d) At most n(n − 1) transitions change λ^U ([R47a]). Every other τ-changing transition has both ends in one λ^U-run (≤ n(n − 1) + 1
  of them) and contains ≥ 1 Odd switch. ✓
- (e) **The Lead's point (1).**
  - [R86e] is accepted as a premise, and it does not need re-proving here, because it IS displayed in RESULTS:
    - R86's headline (docs/RESULTS.md l. 5269) says COMPOSE-NM's premise «both referees sign as holding, with RESULTS R85's MATCH-Φ …
      because MATCH-Φ's proof reads verbatim on every λ-run (λ^U-run on G^d), where c = λ(v) is fixed»;
    - its body (e) (l. 5345-5357, unchanged on trunk) quotes both referees' §6 cells and F3 (NM^U read with G^d's parities).
  - The per-vertex form the packet uses is the premise itself: [MΦ] is R85 (c)'s per-vertex Corollary, and R86 (e) signs it «with
    "phase" replaced by "λ-run" (resp. "λ^U-run" on G^d)».
  - For the record, the three-line reason, which I re-derived:
    - on a λ^U-run, c = λ^U(e) is fixed;
    - P(U_t(e)) ⊆ the K ranks above rank(c) by [S1-val];
    - MATCH-Φ and its counting use nothing else (they are statements about a sequence of subsets and a parity pattern, here G^d's).
  - K ≤ n − 1 gives K(K + 1)/2 ≤ n²/2, and the bound is monotone in PCH, so (b)-(d) hold with it substituted. ✓
- Data (per λ^U-run; UNP computed from my protection search, a truncated search counted as UNPROTECTED, which keeps (a) sound and makes
  (b)-(d) only stricter): CFa, CFb, CFc, CFd, CFe all 0. CFe checks both forms, K(K+1)/2 and n²/2, with carries from my own matcher.

## 3. The Even side inside a τ-stretch
**3.1 SUCC-MON.** σ_{t+1}(y) ∈ {σ_t(y)} ∪ Iσ_t(y) (S4a's arena; S4c's Even branch picks from Iσ; otherwise unchanged). Ξ_{t+1} ⊵ Ξ_t
pointwise (R15 (a) with I = the changed edges ⊆ Iσ_t, R15 (d); Ξ depends on σ alone). Both cases are then as written. ✓ The proof gives
more: a STRICT rise whenever σ(y) changes (N-FR-8). Data SM: 0. Control X_SM_W: W_t(σ_t y) is NOT monotone along runs (it drops at
τ-changes), so the lemma is about Ξ, not W.

**3.2 LATE-RISE.** Ξ_u(z) ▷ Ξ_u(σ_u y) (S2 at u) ⊵ Ξ_t(σ_t y) (SUCC-MON) ⊵ Ξ_t(z): trivially if z = σ_t(y); otherwise (y, z) ∉ Iσ_t and the
order is total. ✓ Data LR: 0 (every Even edge, every pair t < u, via the running maximum over the non-improving states).

**3.3 GP*-RUN (a widening of landed R88).** I re-read R88's object (P-N5-GP-box31.md @ d072bb28, sha1 cd4866df) §2-§4 line by line:
- W-MON (§2): uses «τ_{t+1} = τ_t» (true on a τ-stretch), [STEP] (so σ changes), «not a fallback» (so σ_{t+1} = S4a's σ_new with
  Iσ_t ≠ ∅), S4a's one-player optimum of H_t, and [F1] on H_t. "Inside a phase" appears only in the statement; λ_Ξ is never used. ✓
- GP* (§3):
  - BLOCKED at t uses Iσ_t of THAT state; "unblocked at state k" uses L ≤ k − a, so every referenced state lies in F.
  - The base case and the L = 0 case use λ_W(u) = u on F.
  - Case A uses [CASE-A] with W_{k+1} ⊵ W_k (W-MON).
  - Case B uses ρ̂ ∈ H_k (Iσ_k at state k) and [F1].
  - The sub-cases use λ_W(x) = c from W_k's structure: B1′(ii), B2b(i) and B2b(iii) with c odd are excluded by «λ_W constant on F».
  - σ̄, D and λ_Ξ occur nowhere in §3. ✓
- FW-R* (§4): uses GP*, W-MON, «u = λ_W(x) constant on F, so u is a cycle node of state a», and S4a's form of non-fallback transitions. ✓
- σ̄, D, U_t, S_{d,t} and λ_Ξ occur only in §3a (GP, GP+) and §1's [FRZ] definition, which GP*-RUN does not restate. **The packet's claim
  holds: a W-run has every property R88's proofs use.** ✓
- Data, on W-runs (σ̄ and λ_Ξ allowed to move):
  - GPS (GP* path enumeration, PCAP 200, on W-runs of ≤ GPMAX states): 0.
  - FWR on every W-run: 0.
  - GPS_paths_notfrozen counts the paths checked inside W-runs that are NOT frozen W-phases, so the widening is exercised.
  - The control X_GPall (blocked restriction dropped) bites.

**3.4 R*-RISE.**
- t_1: a state of F before u_1 at which (y, z) was blocked (blocked ⇒ ∉ Iσ). t_i := u_{i−1} + 1: σ_{t_i}(y) = z, so (y, z) ∉ Iσ_{t_i}
  (S2 needs w ≠ σ(v)). σ_{u_i}(y) ≠ z, so t_i < u_i, and t_i ≤ u_i ≤ b − 1 keeps t_i in F.
- Each adoption is from Iσ_{u_i} (no fallback in F; even a fallback picks from Iσ).
- LATE-RISE ⇒ Ξ(z) changes at some transition in [t_i, u_i). The intervals are disjoint (t_{i+1} = u_i + 1).
- So the late adoptions of (y, z) are ≤ RISE_F(z), and R*_T ≤ #late adoptions ≤ Σ_z d_E(z)·RISE_F(z). ✓
- Data RR, RRsum: 0.

**3.5 STRETCH-RED (the Lead's point (3)).**
- |S| = transitions with both ends in S. Each changes σ (τ is constant; R15 (d)). ✓
- Q := the fallback or λ_W-changing transitions of S. Cutting them leaves ≤ Q + 1 W-runs. ✓
- λ_W count:
  - in a fallback-free piece, W-MON gives W_{t+1} ⊵ W_t; it needs only τ constant and a non-fallback transition, not a phase;
  - the cycle node is the first key and rewards are injective, so a cycle-node change is a strict reward rise;
  - so each vertex's W cycle node changes ≤ n − 1 times per piece, the λ_W-changing transitions per piece are ≤ n(n − 1), and there are
    fb_S + 1 pieces. Q ≤ fb_S + n(n − 1)(fb_S + 1). ✓
- Per W-run: (n − 1)(R*_T + 1) W-changing transitions (GP*-RUN) plus its W-flat σ-changes. Summed:
  |S| ≤ Q + (Q + 1)(n − 1)(R*_S + 1) + FL_S ≤ the stated bound, which multiplies FL_S by Q + 1 needlessly (N-FR-6). ✓
- **fb_S, counted when τ is constant.**
  - A phase (R38 (a)) needs τ constant and S is a MAXIMAL τ-constant run, so every phase meeting S lies inside S.
  - The phases meeting S partition S's states and are separated by λ_Ξ-changing transitions: there are ≤ (λ_Ξ-changes in S) + 1 ≤
    n(n − 1) + 1 of them.
  - A fallback inside S is an Even S4c fallback: an Odd S4c fallback changes τ, so it cannot lie inside S. It either changes λ_Ξ (≤ n(n − 1)
    such transitions in the whole run) or has both ends in one phase, where R56 counts it (≤ 1 + (n − 1)(2 + ρ) ≤ 1 + (n − 1)(2 + ρ_S)).
  - The count is correct, and also under the wider reading of R56's "in-phase" (source state in the phase), which only over-counts. ✓
- Data SR0 (σ changes at every transition inside S), SR1, SR2, SR3, SRpc (per piece), FB56 (R56 as used, per phase), WM (W-MON on every
  fallback-free piece of every τ-stretch): 0.
- **Consequence (to sign as stated).** Split F's transitions into the λ-changing ones (≤ n(n − 1), [R47a]) and those inside one λ-run R.
  Then RISE_{F∩R}(z) ≤ RISE_R(z) ≤ n(PCH_R(z) + 1) (LEN-MONO on R), and F meets ≤ n(n − 1) + 1 λ-runs. So RISE_F(z) ≤ n(n − 1) +
  (n(n − 1) + 1)·n·(PCH* + 1). With R*-RISE: R*_S ≤ m_E·(n(n − 1) + (n(n − 1) + 1)·n·(PCH* + 1)), PCH* the largest PCH_R(z) over λ-runs R
  meeting S (each measured on all of R). A polynomial in n, m_E and PCH*. ✓ Data CONS (both the per-z inequality and the sum): 0.

## 4. Re-runs and own control
**4.1 Pinned (logs/pinned_check.txt).**
- experiments/new/check.sh, run whole in a detached worktree at 938d8796: exit 0. Every block prints PASS, including the four the packet
  pins: «box 63 ODD-FREEZE: dw_3 81 hypothesis hits, 0 improving», «box 64 STRETCH», «box 64 FRAME-STRETCH DEAD family: mk_4_16», «box 64
  GP*-RUN: dw_3 one W-run of 26 W-changing transitions, 4 late adoptions, FW-R* holds».
- Reproduced by my own code (logs/dw3_dump.txt, DUMP=1):
  - dw_3's W-run [15, 41]: 26 transitions, WCH 26, R*_T 4, 11 late adoptions of edges, 3 σ̄/λ_Ξ cuts inside (= the lane's "4 frozen phases
    (3 sbar cuts)").
  - ODD-FREEZE hits on states 0-40: 81, the lane's figure exactly, with the search uncapped (OFNODE 2·10⁶; at the default cap 2 searches
    truncate and count as unprotected).

**4.2 Own control (frame_check.py).** Every log ends RESULT PASS, 0 violations of FT2, FT3, FT4, DORD, UPLAY, OF, OF_play, OF_mid, OF_opt,
OFBF, EF, CFa-CFe, SM, LR, WM, GPS, FWR, RR, RRsum, SR0-SR3, SRpc, FB56, CONS.
| corpus | runs (states → transitions) | ODD-FREEZE edges / protected hits / ENT checks | λ^U-runs: CFa edges | SUCC-MON / LATE-RISE checks | W-runs (not frozen W-phases) | GP* paths (in non-frozen W-runs) | late adoptions / max R*_T | controls that bite |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| random 1500, n 3-8, S3 + 3 random, BF = 8 (OFBF 37,216 = every edge, 0 mismatches) | 6,000 / 6,712 | 37,216 / 3,423 / 1,472 | 47,005 | 19,919 / 717 | 12,219 (61) | 2,525 (290) | 0 / 0 | noH3e 955, noH3r 732, SM_W 2,615 |
| random 2300, n 6-14, S3 + 2-3 random | 8,900 / 15,260 | 129,422 / 9,894 / 5,434 | 147,659 | 79,915 / 3,725 | 23,112 (138) | 6,338 (776) | 2 / 1 | noH3e 2,653, noH3r 2,038, GPall 2 |
| random 300, n 15-30, S3 + 2 random | 900 / 2,501 | 37,630 / 3,065 / 2,101 | 40,736 | 29,211 / 1,682 | 3,223 (22) | 1,438 (212) | 2 / 1 | noH3e 512, noH3r 576 |
| alltau: EVERY τ of 1,650 random games n 3-11 (BF on n ≤ 7: 69,062 edges, 0 mismatches) | 27,435 τ | 238,570 / 5,782 / — | — | — | — | — | — | noH3e 17,949, noH3r 3,683 |
| box59/sbcg.lst, all 719 games, S3 (576 with counters; 143 in stopped chunks, see below) | 576 / 9,897 | 260,674 / 30,033 / 27,439 | 112,648 | 536,341 / 49,047 | 4,166 (274) | 10,185,914 (7,612,664) | 991 / 17 | noH3e 3,871, noH3r 2,167, GPall 790,359, FW0 5, SR_Q0 11 |
| box64/mkr (4 games: start file + S3 + random; mk_16_100 start only) | 11 / 2,191 | 120,608 / 2,201 / 2,190 | 4,408 | 248,596 / 4,374 | 2,202 | (GPMAX) | 0 / 0 | SR_Q0 3 (mk_6_24, mk_8_32, mk_16_100) |
| box64 dual family (8 games, start files where present + S3 + random) | 21 / 881 | 184,063 / 940 / 899 | 6,959 | 76,820 / 43 | 852 (27) | 2,750 (2,750) | 0 / 0 | noH3e 1,146; max NM^U 163 (COMPOSE-FREEZE (e) exercised) |

- In every log X_OF_noH2 = 0 (N-FR-4), SR1_sharp_fails = 0 (N-FR-6).
- Max over sbcg: PCH^U 13 and NM^U 10 on unprotected targets; stretch 264. Over mkr: one τ-stretch of 1,648 σ-changes (mk_16_100, Q = |S|).
- Caps, all counted:
  - ODD-FREEZE's path search stops at OFNODE nodes (20,000; 3,000 on n > 100; 2,000 on mk_16_100). An unfinished search counts as
    UNPROTECTED, which is conservative for COMPOSE-FREEZE: OF_truncated_unknown 48,110 on sbcg and 51,243 on mkr. ODD-FREEZE and
    ENT-FREEZE are checked on every hit found.
  - GP*'s enumeration: PCAP 200 paths and NODECAP 20,000 nodes per (k, x), only on W-runs of ≤ GPMAX states (60; 20 on n > 100;
    GPS_dfs_truncated 31,989 on sbcg). FW-R*, R*-RISE, CONS and STRETCH-RED are exhaustive.
  - DORD samples 5,000 pairs per state above that (2,000 / 1,000 on big games).
- sbcg ran in 8 chunks. Chunks 0, 1, 3, 4 and 5 stalled on games with n > 200. I stopped them (pgrep / kill) after 5, 22, 39, 8 and 69 files
  (143 files, 0 VIOLATION lines, counters lost with the stop: logs/sbcg_part{0,1,3,4,5}_killed.txt). Their remaining 289 files were re-run:
  247 with n ≤ 100 at the default caps (logs/sbcg_rest_small{0,1}.txt) and 42 with n > 100 at the light caps (logs/sbcg_rest_big.txt).
  So every one of the 719 games was run.
- mkr's first run (logs/mkr_killed_oldcode.txt, an earlier code version) was stopped on mk_16_100 and re-run as logs/mkr_small.txt and
  logs/mkr_big.txt. Chunks 2, 6 and 7, dual.txt and the random logs started before the counters X_SR_Q0 and DUMP were added, so they do not
  report X_SR_Q0; their checks are the same.

## 5. The approved RESULTS line (acf3234f), clause by clause (the Lead's point (4))
- Setting: "SPEC S1-S5; W_t …; a τ-stretch …; a W-run … none of whose transitions is an S4c fallback or changes λ_W; U, τ̄(τ), λ^U-runs,
  ENT, RISE, PCH as in RESULTS R86, blocked edges and late adoptions as in RESULTS R88". Matches §1. τ̄(τ) is SPEC S1's (Odd's side), not
  R86's; harmless, since SPEC S1-S5 is cited first.
- FRAME-τ (i)-(iv): matches §2.1.
- ODD-FREEZE / "protected": every hypothesis of §2.3 is there:
  - (H1′): positional σ_e = τ̄ off P_e, reaching o before repeating;
  - P_e: up to and including the first visit of o;
  - (H2);
  - (H3): even and more relevant than the cycle node of the (τ, τ̄)-play from τ(o);
  - e ∈ succ(o), e ≠ τ(o).
  - ENT-FREEZE: matches.
- COMPOSE-FREEZE: (a), (b) (final form), (d) and (e) match §2.5. (c) and the RISE intermediate are omitted, which is fine. [R86e] is
  cited as «the premise RESULTS R86 (e) signs as holding», which is correct (§2.5).
  - **NM^U_R(e) is not defined in the line.** Precision fix: add "NM^U_R(e) the carries of U(e)'s path sets in R, read with G^d's
    parities (RESULTS R86 (e), F3)".
- SUCC-MON, LATE-RISE, GP*-RUN, R*-RISE (per edge; the sum form omitted): match §3.1-§3.4. GP*-RUN inherits R88's line, which carries
  "at most k − a edges" and "W-cycle node of F's first state", the N-GP-7 fix.
- STRETCH-RED: fb_S, R*_S, FL_S and ρ_S are all defined. **Q is not.**
  - The packet defines Q := the transitions of S that are an S4c fallback or change λ_W.
  - The line's "|S| ≤ Q + (Q + 1)(…), Q ≤ fb_S + n(n − 1)(fb_S + 1)", with Q free, reads as a claim for any Q under the bound. Q = 0 then
    claims |S| ≤ (n − 1)(R*_S + 1) + FL_S, which is FALSE (control X_SR_Q0, §4.2). Instances are the lane's own FRAME-STRETCH family,
    with its start files (logs/mkr_small.txt):
    - mk_6_24 (n 149): one τ-stretch [0, 162] with |S| 162, Q 162 (every transition changes λ_W), R*_S 0, FL_S 0, fb_S 0, and 162 > 148;
    - mk_8_32 (n 197): |S| 280 > 196, also with Q = |S|;
    - mk_16_100 (n 498): |S| 1648 > 497, Q = |S| (logs/mkr_big.txt).
    The true Q satisfies the packet's bound: 162 ≤ 0 + n(n − 1)·1.
  - **Required fix: add "Q := the transitions of S that are an S4c fallback or change λ_W".**
- Tail: "a REDUCTION (NM^U on unprotected targets, R*_S (hence Even's PCH), FL_S and ρ_S are not bounded here; G-N5-TIME stays open; not
  M3, not a step-4 pass, not a TARGET.md claim)". Matches. "(hence Even's PCH)" points at the Consequence, which the line does not state;
  harmless.
- The line claims nothing beyond §2-§3.
- **Verdict on the line:** MATCHES in content once Q is defined (required) and NM^U_R(e) is defined (precision).

## 6. Notes (not gaps)
- N-FR-1 (Lead's point (1)). [R86e] stands as a premise. RESULTS displays it in R86's headline («whose premise both referees sign as
  holding … because MATCH-Φ's proof reads verbatim on every λ-run (λ^U-run on G^d)») and in body (e) l. 5345-5357, both cells quoted. The
  brief's "not displayed in RESULTS" is not accurate. The per-vertex λ^U-run form IS the premise ([MΦ] is per vertex).
- N-FR-2 (citation). ODD-FREEZE's step "τ̄ maximises G's order for Even among plays (τ, α) from e" is SPEC S1-Xi's «minimising … at every
  vertex at once» on G^d, i.e. RESULTS R57 (a) (VJ) on G^d, which R85's Fact B2 cites for the same step. Name it.
- N-FR-3 (simplification). (H1′) is equivalent to: there is a simple path from e to o in G_τ (Odd vertices other than o follow τ; Even
  vertices free). σ_e can always be chosen equal to τ̄ off the path, and the play up to o never leaves it. Brute force over all positional
  σ_e agrees with the path test on every Odd edge (OFBF, n ≤ 7-8).
- N-FR-4 ((H2) never needed). Dropping (H2) (keeping (H1′), (H3)) never produced an edge of Iτ: X_OF_noH2 = 0 on every run state and on
  every τ of 1,650 small games (27,435 τ). The same pattern as GATE-SHUT's (H2) (R85, N-MPGS-1 / N-GS-3). A sketch for the cases I tried by hand: if
  P_e meets the (τ, τ̄)-play from τ(o), Even either shortcuts at the first meeting vertex or closes a cycle through x. (H2)'s necessity is
  not exhibited. A possible strengthening, OPEN, not needed for any signature.
- N-FR-5 (Lead's point (3)). STRETCH-RED's fallback count is correct: the phases meeting S lie inside S (maximality), and an in-S fallback
  is Even and either λ_Ξ-changing or in-phase (§3.5).
- N-FR-6 (looseness). STRETCH-RED holds with FL_S added once: |S| ≤ Q + (Q + 1)(n − 1)(R*_S + 1) + FL_S. Data: the sharper form never
  fails (SR1_sharp_fails 0).
- N-FR-7 (RESULTS line, REQUIRED). Define Q in the line (§5). Define NM^U_R(e) (precision).
- N-FR-8 (SUCC-MON, stronger). Ξ_t(σ_t(y)) rises STRICTLY at every transition where σ(y) changes (the proof's last chain is strict).
- N-FR-9 (COMPOSE-FREEZE (b)). The second inequality is an identity: 1 + PCH + (PCH + 1)(n − 1) = n(PCH + 1).
- N-FR-10 (DATA, not signed). [CORRECTED in R2-N5-FRAME-C.md §C.7: freeze2.py counts box 63 (H1) over all 42 states = 81; (H1′) gives 84 (81 on states 0-40, a coincidence).] Original: the lane's 81 ODD-FREEZE hits on dw_3 are states 0-40; there are 84 over all 42 states.

## 7. DONE / FINDINGS / NEEDS
- DONE: this report; docs/referee-2/R2-N5-FRAME/{frame_check.py, fquote.py, mkr.lst, dual.lst, run_all.sh, logs/ (pinned_check.txt
  included)}.
- FINDINGS:
  - All ten items SIGNED, with no gap. ODD-FREEZE's directions are correct.
  - [R86e] is accepted as a premise and is displayed in RESULTS.
  - GP*-RUN: R88's proofs never use σ̄, D or λ_Ξ.
  - STRETCH-RED's fallback count is correct for constant τ.
  - The RESULTS line matches but must define Q (required): with Q free, "Q = 0" is a false reading.
  - (H2) of ODD-FREEZE was never needed in data (open strengthening).
- NEEDS: Lead: add Q's definition, and NM^U_R(e)'s, to the RESULTS line (N-FR-7); route N-FR-1..10 to L-NEW. I write §C after REFEREE's
  FRAME report, on your word.
