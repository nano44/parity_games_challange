# R2-N5-SF: REFEREE-2 report on packet P-N5-SF (L-NEW box 55): N5-SF, Lemmas SF-TERM, DECOUPLE, ONE-PLAYER, Theorem SF-RED
Referee: REFEREE-2 successor 20, Opus 5.5 (D15, L37), independent second referee. Written 2026-10-29 from 15:55Z (date -u).

**Object.**
- docs/new/P-N5-SF-box55.md, sha1 dbc2345f62454d442e951de025b1b2aef8a35317, 172 lines, at l-new freeze 95a7a581. Measured with
  `git show 95a7a581:<path> | sha1sum`; equal to the Lead's figure.
- Pinned files, measured at 95a7a581:
  - experiments/new/box55/pcheck.py f4d741c2;
  - box54/n5sf.py 1ea3bdc7;
  - box21/n5x.py bbc7d4c9;
  - box49/quotecheck3.py eaf18411;
  - instances switchbestexp_2.pg b3d5bc29 and n3cov_lean.pg bcf8dbf6 (both equal to check.sh's sha1s).
- Trunk note: the Lead's trunk merge 59d3f707 was not yet on origin at my first fetch (15:55Z). It was there at 16:03Z. I worked from the
  freeze commit 95a7a581 throughout.

**Independence.**
- Name count `git ls-tree --name-only -r origin/claude/referee docs/referee/ | grep -ic sf` = 0 at 15:55:17Z. 0 at 16:03:20Z (push turn,
  after a fresh fetch). Names only. No docs/referee/ file opened.
- The lane's pcheck.py, ntcheck.py and quotecheck3.py were READ, then RUN as check.sh's box-55 commands, from experiments/new in a detached
  worktree at 95a7a581 with `python3 -I`. Output: R2-N5-SF/logs/pinned_check.txt. They were never imported.
- My control is my own code: R2-N5-SF/sf_check.py.
  - N5-SF is written there from the packet's §0 definitions, on si.py (SPEC S1's own implementation, read-only).
  - N5 itself comes from my lane's R2-N5-DUAL/dual_check.Runner. It is used for ONE-PLAYER's "N5's iteration on G_σ̄" and for the WIN
    comparison.
  - No lane module is imported.
- Quotes: my ../R2-N5-CORE/qcheck.py.

**Scope (D1).**
- A REDUCTION for a VARIANT of N5. It bounds N5-SF's iteration count by a polynomial times SBC, and SBC by twice the count. It does not
  bound SBC (CONJECTURE SF-POLY OPEN).
- Not about N5 itself (G-N5-TIME untouched). Not a TARGET.md claim. Not a gauntlet pass.

## 0. Verdicts (all "(Opus 5.5, D15)")
| § | item | verdict |
| --- | --- | --- |
| §0 | definitions (σ̄(σ), Ξσ, Iσ, λ_Ξ, N5-SF = S4a′ / S4b′, A, F, F^d, run, distinct-σ sequence, G_σ̄, SBC, LAM, stretch) | SIGNED (well formed; F is a function of σ alone) |
| §2 | Lemma SF-TERM | SIGNED |
| §2 | Lemma DECOUPLE | SIGNED |
| §3 | Lemma ONE-PLAYER (a), (b) | SIGNED (the τ-side mirror needs one line: N-SF-2) |
| §3 | Theorem SF-RED (a) stretch bound b − a ≤ n + m, ≤ n − 1 Ξ-changes | SIGNED |
| §3 | Theorem SF-RED (b) #σ − 1 < (n+m+1)(1 + LAM_σ + SBC_σ), LAM_σ ≤ n(n−1), I < (n+m+1)(2(n²−n+1) + SBC) | SIGNED |
| §3 | Theorem SF-RED (c) SBC_σ ≤ #σ − 1, SBC ≤ 2I; polynomial iff SBC is | SIGNED |
| — | Proposed RESULTS line (15:27:39Z) | MATCHES the signed content (§2.6) |
| §3 Remarks, §4, §5 | READING / DATA / CONJECTURE / status | not signed. §4 pins reproduced EXACTLY (§3.1) |

No gap. No item FALSE. Notes N-SF-1..N-SF-6 (§4).

## 1. Premises
- 18 quotes.
  - The lane's quotecheck3 gives "quotes=18 bad=0, QUOTES PASS", and --mut gives QUOTES FAIL.
  - My strict qcheck: 18/18 OK. The SHIFT=1 control gives 0/18.
- Read in context at 305cc8be:
  - RESULTS R15 (a)-(d) and limits (l. 628-650). (c)'s "every non-empty switch of improvements goes strictly up in ≺" is for VJ00's
    unambiguous switches, which is what SF-TERM (i) supplies.
  - R17 setting and (a)-(f) (l. 730-750).
  - SPEC S1-S5, FIX 3.

## 2. Proof check
**2.1 SF-TERM.**
- (i) S4a′'s arena gives an Even v only σ(v) and its Iσ-targets, and S4c's Even branch picks one Iσ-target per vertex. So each σ-change is
  Switch_J(σ) with ∅ ≠ J ⊆ Iσ and one edge per vertex. With Iσ = ∅ nothing changes σ: S4a′ inherits "Else σ_new = σ", and S4c's Even branch
  needs Iσ ≠ ∅. The same holds for τ on G^d (S4b′, S4c's Odd branch).
- (ii) R15 (c), applied separately on G and on G^d, gives no recurrence of σ or of τ.
- (iii) S4c guarantees that every iteration changes σ or τ, so I ≤ (#σ − 1) + (#τ − 1).
- (iv) The only exit is S5.
- ✓ Data (TERM): 0 violations. Every iteration changes something, no σ or τ recurs, I ≤ (#σ − 1) + (#τ − 1), and the stop has
  Iσ = Iτ = ∅.

**2.2 DECOUPLE.**
- Iσ, Ξσ and σ̄(σ) are functions of σ: R15 (d), plus S1's determinism. So A(σ) and F(σ) are τ-free.
- At a σ-change from (σ, τ), Iσ ≠ ∅. Two cases:
  - A(σ) ≠ σ: then σ_new = A(σ) ≠ σ, S4c cannot fire (it needs σ_new = σ), so σ := F(σ).
  - A(σ) = σ: σ can change only through S4c's Even branch, which sets F(σ). FIX 3 keeps τ in that iteration.
- So σ^(j+1) = F(σ^(j)), and Iσ^(j) ≠ ∅ for j < p. At the stop Iσ^(p) = ∅.
- The mirror: τ changes only through S4b′ (A^d(τ)) or S4c's Odd branch (only when Iσ = ∅). Either way the new τ is F^d(τ). Iσ = ∅ affects
  when τ changes, not to what. ✓
- Data:
  - ORB: the run's distinct-σ (τ) sequence equals the τ-free (σ-free) orbit of F (F^d), at every run.
  - ORB2: a second run from (σ_0, random τ_0′) gives the same distinct-σ sequence, and (random σ_0′, τ_0) the same distinct-τ sequence,
    at every run.
  - 0 violations in both.

**2.3 ONE-PLAYER.**
- (a) In G_σ̄, Odd's only strategy is σ̄, so the optimal reply is σ̄. The plays under (σ, σ̄) are the same in G and G_σ̄ (Odd vertices follow
  σ̄ in both; Even edges are the same). So the valuation of σ in G_σ̄ is the play value of (σ, σ̄(σ)), which is Ξσ, and S2 gives the same Iσ.
  This rests on the SPEC-conformance premise that S1's procedure returns the optimal-reply play value (N-SF-1). ✓
- (b) N5's S4a on G_σ̄ with τ = σ̄ builds exactly S4a′'s arena H, the same graph with the same lists, and runs the same deterministic
  procedure, so it gives A(σ).
  - In G_σ̄ every Odd vertex has out-degree 1, so Iτ = ∅ and τ_new = τ.
  - N5's S4c fires iff A(σ) = σ, with the same argmax over (Ξσ(w), w).
  - ✓
- Data (OPa, OPb, every σ^(j), j < p, both sides): S1 on G_σ̄ reproduces Ξσ and Iσ, and F(σ^(j)) equals one dual_check.Runner iteration on
  G_σ̄. 28,052 Even and 17,111 Odd checks, 0 violations.
- The τ side is checked on G^d_τ̄ (N-SF-2).

**2.4 SF-RED (a).**
- On a stretch, σ̄(σ^(j)) = σ̄ and λ_Ξ are constant. By DECOUPLE and ONE-PLAYER (b), σ^(a..b) are consecutive states of N5's run on G_σ̄ from
  (σ^(a), σ̄), with valuations Ξσ^(j) (ONE-PLAYER (a)).
- No vertex changes its cycle node there, so the b − a transitions form a PREFIX of the first λ-phase of that run. This is enough: R17 (c)
  bounds a whole λ-phase (N-SF-3).
- R17 (e): every S4a step is switch-best. An S4c step is value-flat and leaves no improving edge in G_σ̄.
  - If it lies inside the stretch (j + 1 ≤ b), then σ̄(σ^(j+1)) = σ̄. So Iσ^(j+1) in G equals its set in G_σ̄, which is ∅ (ONE-PLAYER (a)).
  - Hence j + 1 = p = b: at most one S4c transition, and it is the last.
- R17 (c): fewer than n + m′ ≤ n + m switch-best steps in the phase, at most n − 1 of them value-changing. So b − a ≤ n + m, and Ξ-changes
  ≤ n − 1. ✓
- Data (SEG, FBLAST): 0 violations.
  - Max stretch: 69 (alt_all), 59 (fam), 56 (lib41), 52 (hard), always far below n + m.
  - Remark 1's sharper "< n + m" was never at the limit (SEGsharp = 0).

**2.5 SF-RED (b), (c).**
- (b) Stretches are maximal intervals with (σ̄, λ_Ξ) constant. A boundary j has σ̄ or λ_Ξ changing at j → j + 1, so there are ≤ LAM_σ + SBC_σ
  boundaries and S ≤ 1 + LAM_σ + SBC_σ stretches.
  - p = Σ(b − a) + (S − 1) ≤ S(n + m) + S − 1 < S(n + m + 1). ✓
  - LAM_σ: R15 (a) on each Switch_J gives pointwise ⊴. The reward of λ_Ξ(v) never falls and strictly rises at a change (injective rewards),
    so ≤ n − 1 changes per vertex and LAM_σ ≤ n(n − 1). ✓ The same on G^d, which has the same n and m.
  - I ≤ (#σ − 1) + (#τ − 1) < (n + m + 1)(2 + LAM_σ + LAM_τ + SBC) ≤ (n + m + 1)(2(n² − n + 1) + SBC). The inequality stays strict even
    when #σ = 1. ✓
- (c) SBC_σ counts some of the p transitions of the distinct-σ sequence, so SBC_σ ≤ p.
  - Each σ-change and each τ-change happens in its own iteration (≤ one change per side per iteration), so p, q ≤ I and SBC ≤ 2I.
  - The equivalence follows, read over all runs of the class. ✓
- Data (BND): 0 violations on 14,220 runs. Max SBC: 75 / 16 (E / O, hard), 49 (alt_all), 47 (fam), 41 (lib41). Max LAM: 28 (lib41).
  Max I: 489 (hard).

**2.6 The proposed RESULTS line.** Checked clause by clause against the signed items:
- "terminates (Lemma SF-TERM; R15 (c), (d))": SF-TERM uses R15 (c), and R15 (d) through "Iσ depends on σ alone" (DECOUPLE, and SF-TERM (i)'s
  improvement sets). OK.
- "sequence of distinct σ depends on σ_0 alone and that of τ on τ_0 alone (Lemma DECOUPLE)": OK.
- "SBC/2 ≤ I < (n + m + 1)(2(n² − n + 1) + SBC)": exactly SF-RED (b), (c). OK.
- "SBC = the σ-changes at which σ̄(σ) changes plus the mirror": matches §0's SBC_σ + SBC_τ. OK.
- "(Theorem SF-RED; R15 (a), (c), (d), R17 (c), (e))": OK.
- "a reduction, polynomial iff SBC is; CONJECTURE SF-POLY OPEN; output correctness as N5's (rests on G-N5T-3)": OK.
- The RESULTS line MATCHES the signed content and claims nothing beyond it.

## 3. Re-runs and own control
**3.1 Pinned (logs/pinned_check.txt).** The check.sh box-55 commands at 95a7a581:
- n3all_maxph_0: `ROW E_ n 3 m 6 values 3 orbit 3 SBC 1 LAM 1 SEG 2 SEGMAX 1`, CHECK PASS.
- switchbestexp_2: `ROW E_ n 60 m 130 values 59 orbit 59 SBC 4 LAM 0 SEG 5 SEGMAX 18`, CHECK PASS.
- n3cov_lean: `ROW E_ n 48 m 128 values 29 orbit 29 SBC 11 LAM 4 SEG 12 SEGMAX 6` and `ROW O_ … values 6 orbit 6 SBC 3 LAM 5 SEG 6
  SEGMAX 0`, CHECK PASS.
- MUT=1: `E_ORB_V`, CHECK FAIL (the control bites).
- ntcheck: NT PASS.
- quotecheck3: quotes=18 bad=0; --mut: QUOTES FAIL.
- All exactly as §4 and check.sh l. 190-207 print.

**3.2 My N5-SF against the lane's ROW figures (logs/pins.txt).** My independent implementation gives the same SBC, LAM, stretch count and
maximum stretch, both sides, on all three pins:
- n3all: E 1 / 1 / 2 / 1; O 0 / 0 / 1 / 1.
- switchbestexp_2: E 4 / 0 / 5 / 18; O 2 / 2 / 3 / 0.
- n3cov_lean: E 11 / 4 / 12 / 6; O 3 / 5 / 6 / 0.

This holds only after reading the partial start file n3cov_lean.start as the lane does (unlisted vertices take the S3 start). With
unlisted vertices on their first successor (trap 1 of my notebook), the Even side gives SBC 12 and 13 stretches (N-SF-4).

**3.3 Own control (sf_check.py; every log RESULT PASS, 0 violations of TERM, ORB, ORB2, OPa, OPb, SEG, FBLAST, BND, WIN).**
| corpus | runs | iterations | OP checks E / O | fallbacks E / O | X_ORBN5 (N5's σ-sequence ≠ N5-SF's) |
| --- | --- | --- | --- | --- | --- |
| random 3000 games n 4-14, S3 + 3 random starts | 12,000 | 17,092 | 12,276 / 12,321 | 495 / 559 | 1,559 |
| random 400 games n 15-30, S3 + 2 random | 1,200 | 2,889 | 2,227 / 2,297 | 46 / 62 | 590 |
| lib41_noref (410 files), S3 + 1 random | 820 | 8,902 | 8,420 / 2,001 | 59 / 19 | 510 |
| alt_all, pinned starts (93 valid; 1 invalid start skipped) | 93 | 1,505 | 1,497 / 146 | 10 / 2 | 72 |
| box 54 families (fam.lst = box54/fam.lst): given starts + S3 | 34 | 1,161 | 1,055 / 111 | 0 / 0 | 23 |
| hard families (hard.lst = box55/hard.lst @ 95a7a581; switchbestexp, switchallexp, Oink M1 generators), S3 | 73 | 2,613 | 2,577 / 235 | 0 / 0 | 33 |
| total | 14,220 | 34,162 | 28,052 / 17,111 | 610 / 642 | 2,787 |

- WIN (DATA): N5-SF's final λ-parity regions equal N5's from the same start on all 14,220 runs. As the packet says, this is data, not proof
  (G-N5T-3).
- X_ORBN5 (DATA): N5-SF is a different algorithm from N5. On 2,787 runs N5's distinct-σ sequence differs from N5-SF's.

## 4. Notes (not gaps)
- N-SF-1 (standing premise). ONE-PLAYER (a) identifies S1's output on G_σ̄ with the (σ, σ̄)-play value. This is the SPEC-conformance premise
  of R15 limit (ii) (G-N5T-1, DATA). OPa: 0 mismatches over 45,163 checks.
- N-SF-2 (the τ-side mirror of ONE-PLAYER (b), one line). F^d(τ) uses S4b′'s S1 run on the G-arena H′. N5's S4a on G^d_τ̄ runs S1 on the dual
  of a G^d-arena, which is G's arena with priorities Ω + 2. Ω + 2 keeps ranks, parities and lists, so the outputs are equal. Same as SPEC's A3
  row. My OPb on the Odd side runs exactly that (Runner on the cut G^d): 17,111 checks, 0 mismatches.
- N-SF-3 (SF-RED (a), one clause). The stretch is a PREFIX of the first λ-phase of N5's run on G_σ̄. That run may continue past b, while
  N5-SF moves to a new σ̄. R17 (c) bounds the whole phase, so it bounds the prefix. Say "a prefix of a λ-phase".
- N-SF-4 (§4 DATA convention). pcheck reads a partial start file with unlisted vertices taken from the S3 start (n5x.start_pair). §4 does not
  say so, and the ROW figures depend on it (n3cov_lean: E SBC 11 under S3 fill, 12 under first-successor fill). Data only; state the
  convention.
- N-SF-5 (Remark 1, not signed). The data never reach the signed n + m or the sharper n + m − 1. Max stretch 69 on games with n + m in the
  hundreds. The difference in Remark 1 is invisible in practice.
- N-SF-6 (SF-RED (c) reading). "Polynomially many iterations on a class iff SBC is polynomially bounded there" is read over all runs (all
  starts) on the class. With a fixed start rule (S3), the same equivalence holds per start rule, since (b) and (c) are per run. One clause.

## 5. DONE / FINDINGS / NEEDS
- DONE: this report; docs/referee-2/R2-N5-SF/{sf_check.py, pins.lst, fam.lst, hard.lst, run_all.sh, logs/ (pinned_check.txt included)}.
- FINDINGS:
  - SF-TERM, DECOUPLE, ONE-PLAYER and SF-RED (a), (b), (c) all SIGNED, with no gap.
  - The RESULTS line matches the signed content.
  - The pins are reproduced exactly, and my independent N5-SF reproduces the lane's ROW figures.
  - 14,220 runs, 0 violations.
  - Six notes, all one-clause: N-SF-2 (Ω + 2 for the mirror) and N-SF-3 (prefix of a λ-phase) are the textual ones.
- NEEDS: Lead: route N-SF-1..6 to L-NEW (P-N5-SF-fixes-box55.md). I write §C after REFEREE's SF report.
