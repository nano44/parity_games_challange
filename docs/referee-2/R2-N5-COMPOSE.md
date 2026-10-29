# R2-N5-COMPOSE: REFEREE-2 report on packet P-N5-COMPOSE (L-SI box 28): SW-RETURN, LEN-MONO, Theorem COMPOSE, Corollaries COMPOSE-RUN, COMPOSE-NM
Referee: REFEREE-2 successor 20, Opus 5.5 (D15, L37). Written 2026-10-29 from 11:54Z (date -u).

**Object.**
- docs/si/P-N5-COMPOSE-box28.md, sha1 e1b977aa9cf1583d5e0c442a8f87d024230b6524, 141 lines, at l-si freeze 3ca0932d. Measured with
  `git show 3ca0932d:<path> | sha1sum`; equal to the Lead's figure.
- Pinned files, measured at 3ca0932d:
  - experiments/si/rund/quotecheck.py 29bb4a97;
  - experiments/si/chg/compose.py 9fc3b081;
  - experiments/si/check.sh 7747e70c, box 28 block l. 595-610;
  - instances runquad_K8_m30_n192.pg ebaa6ac5 and dlsep_kill_n70.pg e500ea47 (both = the packet's sha1s).

**Independence.**
- Name count `git ls-tree --name-only -r origin/claude/referee docs/referee/ | grep -ic compose` = 0 at 11:54:22Z (after `git fetch origin
  claude/referee`); 0 at 11:59:23Z (push turn, after a fresh fetch). Names only. No docs/referee/ file has been opened.
- The lane's quotecheck.py and compose.py were READ, then RUN as the pinned re-runs, with `python3 -I` from experiments/si in a detached
  worktree at 3ca0932d. Output: logs/pinned_check.txt. They were never imported.
- My checks use my own code: R2-N5-COMPOSE/compose_check.py.
  - State loop: my lane's R2-N5-DUAL/dual_check.Runner, on si.py (SPEC S1's own implementation, read-only).
  - MATCHED test: my lane's R2-N5-MATCHPHI/mphi_check.matched.
  - Everything else is written from the packet's §1 definitions.
  - Quotes: ../R2-N5-CORE/qcheck.py.

**Scope (D1).** A REDUCTION of N5's iteration count to the path-set-change counts P*, P*^U, which are not bounded here (and via §6 to
carries, OPEN). Not a TARGET.md claim. No running-time bound. G-N5-TIME stays OPEN.

## 0. Verdicts (all "(Opus 5.5, D15)")
| § | item | verdict |
| --- | --- | --- |
| §1 | setting, symbols (λ-run, λ^U-run, phase, ENT, SW, RISE, PCH, P*, P*^U), facts (F-SW), (F-MON) | SIGNED (well formed; F-SW and F-MON proved correctly from [S4a-c], [STEP], [MON]) |
| §2 | Lemma SW-RETURN (any stretch, both players) | SIGNED |
| §3 | Lemma LEN-MONO (any λ-run, both players) | SIGNED (it holds on any stretch with λ constant: N-C2) |
| §4 | Theorem COMPOSE (λ-run chain; phase bound) | SIGNED |
| §5 | Corollary COMPOSE-RUN: T ≤ 2n(n−1) + (n(n−1)+1)·n·(m_E(P*+1) + m_O(P*^U+1)), every run, every game | SIGNED (Lead's points (1) and (2) checked: §2.4) |
| §6 | Corollary COMPOSE-NM (the implication, [MΦ] ASSUMED) | SIGNED as an implication. The "phase → λ-run" replacement is VALID (Lead's point (3), §2.5). Read NM^U with G^d's parities (N-C3) |
| §7 | data, pinned check | DATA, not signed. Reproduced EXACTLY (§3.1) |

No gap. No item FALSE. Notes N-C1..N-C5 (§4).

## 1. Premises
- 16 quotes. The lane's quotecheck gives "quotes=16 bad=0" and its --mut control gives "QUOTES FAIL".
- My strict qcheck: 15/16 OK. The SHIFT=1 control gives 0/16, so the checker bites.
- The one MISS is [MΦ] (MPGS l. 97-98). The packet joins two lines with "…" and drops the bold marks "**". The words are otherwise verbatim (N-C1).
- Opened at b025560c9 and read in context:
  - SPEC S1, S2, S4a-c.
  - RESULTS R15 (a) (Lemma A, l. 631) and (d) (l. 640-642).
  - RESULTS R47 (l. 2325-2345). (c) is item (a)(c) of "Lemma Φ (every game)", NOT of Corollary Φ-1O (𝒞^1O).
  - RESULTS R84 (a) Fact DELTA.
- [MΦ] is P-N5-MPGS (A), which I reviewed (R2-N5-MPGS-s20, supplementary; record R2-N5-MPGS.md by successor 19: SIGNED).

## 2. Proof check
**2.0 §1 facts.**
- (F-SW), Even side:
  - S4a's arena keeps only the edges to A(v) = {σ(v)} ∪ Iσ(v), so every changed σ(v) is an Iσ_t-target.
  - S4c moves v to an Iσ-target.
  - An Even fallback leaves τ unchanged (FIX 3).
- (F-SW), Odd side: the same with S4b, S4c, Iτ_t.
- (F-MON): σ_{t+1} = Switch_I(σ_t) with I = the changed edges ⊆ Iσ_t. I is unambiguous because σ_{t+1} is a strategy, so R15 (a) gives
  Ξ_{t+1} ⊵ Ξ_t. If σ is unchanged, Ξ is unchanged (Ξ depends on σ alone, R15 (d)).
- (F-MON) dual: R15 (a) holds on every game, hence on G^d, with I ⊆ Iτ_t.
- ✓ Data: FSW and FMON, 0 violations at every transition and every vertex (§3).

**2.1 Lemma SW-RETURN.**
- Ξ-SUCC (Ξ_t(σ_t v) non-decreasing).
  - If v does not switch: (F-MON).
  - If v switches to w: Ξ_{t+1}(w) ⊵ Ξ_t(w) ▷ Ξ_t(σ_t v), by (F-MON) and (F-SW) with [S2].
  - ✓
- The chain for consecutive entries e < e′ into c, with leaving step s ∈ [e+1, e′−1]:
  - Ξ_{e′}(c) ▷ Ξ_{e′}(σ_{e′}v): (v, c) ∈ Iσ_{e′}.
  - ⊵ Ξ_{s+1}(σ_{s+1}v): Ξ-SUCC, s + 1 ≤ e′.
  - ⊵ Ξ_s(σ_{s+1}v): (F-MON).
  - ▷ Ξ_s(c): (v, σ_{s+1}v) ∈ Iσ_s and σ_s(v) = c.
  - ⊵ Ξ_{e+1}(c): (F-MON), s ≥ e + 1.
  - Every link is correct, so Ξ(c) changes at a transition t ∈ [e+1, e′−1].
- Every such t has t, t + 1 ∈ R, because R is contiguous and contains e and e′ + 1.
- The windows of successive pairs are disjoint, so k entries give ≥ k − 1 changes of Ξ(c) in R. ✓
- No property of R beyond contiguity is used: "any stretch" is right.
- The Odd side is the same on G^d with U, τ, Iτ and ⊴_d. ✓

**2.2 Lemma LEN-MONO.**
- On a λ-run the cycle node c₀ of Ξ_t(c) is fixed. By [S1-ord] the key reduces to (weight(P), then ℓ in c₀'s direction).
- By (F-MON) Ξ_t(c) is non-decreasing. A P-change has distinct weights ([DELTA]), so the weight rises strictly at it and never falls.
  Hence no P-value recurs, and there are exactly PCH + 1 contiguous blocks.
- Inside a block every change is ℓ-only and strict in one direction. ℓ ∈ {0, …, n − 1}: the play is a lasso on ≤ n distinct vertices, and
  ℓ is the index of c₀ on it. So a block has ≤ n − 1 changes.
- RISE ≤ PCH + (PCH + 1)(n − 1) = n·PCH + n − 1. ✓
- The proof uses only "λ constant on R", not maximality (N-C2). Data: LEN, LENB (blocks contiguous) and LEND (ℓ-direction, cycle node fixed
  inside a block): 0 violations.

**2.3 Theorem COMPOSE.**
- SW_R(v) = Σ_{c ∈ succ v} ENT_R(v, c) ≤ Σ_c (1 + RISE_R(c)) (SW-RETURN).
- 1 + RISE_R(c) ≤ n·PCH_R(c) + n = n(PCH_R(c) + 1) (LEN-MONO).
- PCH_R(c) ≤ P*_R, and there are ≤ m_E Even edges. Only v with SW_R(v) > 0 contribute. ✓
- Phase. τ is constant inside a phase, so every transition of 𝒫 changes σ ([STEP]) and |𝒫| ≤ Σ_v SW_𝒫(v). λ is constant on 𝒫, so LEN-MONO
  applies to 𝒫 itself (N-C2). ✓

**2.4 Corollary COMPOSE-RUN, pressed on the Lead's points (1) and (2).**
- (1) The λ-run counts.
  - [Φ] (c) is part of R47's every-game Lemma Φ ("(a) Lemma Φ (every game): … (c) along a run at most n(n − 1) transitions change λ and at
    most n(n − 1) change λ^U"). R47's quoted line 2338 is exactly that item.
  - It is read separately for λ and λ^U. The λ-runs are the maximal runs between λ-changing transitions, so there are ≤ n(n − 1) + 1 of
    them, and likewise for λ^U-runs.
  - Neither R47's joint count 2n(n − 1) + 1, nor Φ-1O, nor R48, nor any phase count is used. ✓
  - Data: max 29 λ-runs and 32 λ^U-runs in one run (lib41), never above n(n − 1) + 1. #(i), #(iii) ≤ n(n − 1) at every run.
- (2) The classification.
  - Kinds are assigned by first match: (i) λ changes; (ii) σ changes; (iii) λ^U changes; (iv) otherwise.
  - In (iv), σ and λ^U are unchanged, so τ changes by [STEP].
  - (ii): t, t + 1 lie in one λ-run, and the transition has ≥ 1 Even switch counted in SW_R. Distinct transitions have distinct switches,
    so #(ii) ≤ Σ_R SW_R.
  - (iv): t, t + 1 lie in one λ^U-run, with ≥ 1 Odd switch, so #(iv) ≤ Σ_{R′} SW_{R′}.
  - Fallbacks:
    - An Even S4c fallback changes σ only (FIX 3), so it is kind (i) or (ii).
    - An Odd S4c fallback (only when Iσ = ∅) leaves σ, hence λ, unchanged, so it is kind (iii) or (iv).
    - S4a + S4b together is kind (i) or (ii).
  - No transition is unclassified ([STEP]: σ or τ changes).
  - T = #(i) + #(ii) + #(iii) + #(iv) ≤ 2n(n − 1) + Σ SW_E + Σ SW_O ≤ 2n(n − 1) + (n(n − 1) + 1)·n·(m_E(P* + 1) + m_O(P*^U + 1)). ✓
  - Data: 40,406 transitions classified (kinds (i)-(iv): 13,857 / 19,061 / 5,104 / 2,384 summed over corpora), 0 unclassified.
    #(ii) ≤ Σ SW_E and #(iv) ≤ Σ SW_O at every run. Both RUN inequalities hold at all 14,428 runs.
  - The control X_RUN0 (drop kinds (i), (iii)) bites at 8,597 runs: the 2n(n − 1) term is needed.

**2.5 Corollary COMPOSE-NM, pressed on the Lead's point (3).**
- MPGS (A)'s Corollary proof uses exactly the following:
  - ranks are distinct;
  - P_t ⊆ R_c with c fixed along the stretch;
  - Φ ∈ [−Σ odd pos, Σ even pos];
  - MATCHED ⇒ Φ rises by ≥ 1 (Lemma MATCH-Φ, a statement about two sets and a parity pattern);
  - counting.
- Nothing uses τ, or the phase's maximality. MATCHPHI's own Remark said so ("holds for any sequence of subsets of R_c"), and both
  REFEREE-2 MPGS reports confirm it.
- On a λ-run, λ(v) is constant, so c is fixed and P_t ⊆ R_c holds. So "phase → λ-run" is not merely a reading: it is the same proof
  verbatim. ✓
- The Odd side runs on G^d. Ranks are the same ([A3]), and parities flip. MATCHED, w and NM^U must be read with G^d's parities (Ω + 1).
  MATCH-Φ's proof holds for every parity pattern, so the bound holds (N-C3).
- K ≤ n − 1 ⇒ K(K + 1)/2 ≤ n²/2, and the bound is monotone in NM, so P*_R ≤ (n²/2)(NM*_R + 1) + NM*_R. ✓
- Data: the NM bound holds on 56,999 Even and 21,286 Odd (vertex, λ-run) pairs with a P-change. Max NM 62 / PCH 67 (alt_all) and 42 / 71 on
  l121reader_n41 (= the packet's §7 figure).

## 3. Re-runs and own control
**3.1 Pinned (logs/pinned_check.txt).**
- quotecheck: "quotes=16 bad=0"; --mut: "QUOTES FAIL".
- compose.py, the three commands of §7. Each TOP line matches the packet character for character:
  - runquad: `TOP (263, …, 0, 263, 481, 1016, 195072, 265890048, 8, 15, 15, 15, 192)`, I0 I1 LDIR LBLK I2 I3 PASS;
  - dlsep_kill_n70: `TOP (12, …, 0, 12, 39, 387, 26810, 14059640, 5, 6, 7, 4, 70)`, the same 6 PASS;
  - MODE=run seglast_kill_n110: `TOP (16, …, 0, 16, 27, 152, 16066, 0, 20, 1, 4, 2, 110)`, RUNI0 R47 EI1 OI1 ELDIR OLDIR ELBLK OLBLK PASS.

**3.2 Own control (compose_check.py; all RESULT PASS, 0 violations of FSW, FMON, SWR, LEN, LENB, LEND, CMP, RUN, NM).**
| corpus | runs | transitions | SWR checks (E / O) | LEN checks (E / O) | CMP (E / O) | phases |
| --- | --- | --- | --- | --- | --- | --- |
| random 3000 games n 4-14, S3 + 3 random starts | 12,000 | 19,091 | 174,178 / 174,155 | 212,395 / 197,988 | 22,588 / 21,054 | 1,597 |
| random 500 games n 15-30, S3 + 2 random | 1,500 | 4,048 | 69,201 / 66,558 | 89,262 / 81,498 | 3,941 / 3,584 | 308 |
| lib41_noref (410 files), S3 + 1 random | 820 | 13,433 | 222,336 / 74,742 | 224,771 / 148,346 | 4,127 / 2,056 | 791 |
| alt_all, pinned starts (93 valid, 1 invalid start skipped: start files are VALIDATED) | 93 | 3,323 | 51,412 / 2,663 | 19,407 / 9,082 | 403 / 181 | 128 |
| named lane pins: runquad_K8_m30_n192, dlsep_kill_n70, seglast_kill_n110, segcount_kill_n20, l121reader_n41 (start file + S3 + 1 random each) | 15 | 511 | 6,104 / 941 | 5,680 / 3,884 | 66 / 43 | 16 |
| total | 14,428 | 40,406 | 523,231 / 319,059 | 551,515 / 440,798 | 31,125 / 26,918 | 2,840 |

- SW-RETURN was checked on every λ-run / λ^U-run, every phase, the whole run and 20 random stretches per run.
- Controls (they bite, so the terms are needed):
  - X_SWR0, ENT ≤ RISE without the "+1": 233,008 (stretch, v, c) checks.
  - X_LEN0, RISE ≤ PCH: length-only rises exist (42,128 (λ-run, c) checks).
  - X_RUN0 (above).
- X_LENfull (LEN-MONO across λ-changes) never bit. The λ-run restriction is used by the proof, but my data do not show it is needed.
  Not a finding against the packet.
- Max S1/S2 (Σ SW over Σ (1 + RISE)) is 0.8. Consistent with the packet's slack reading.

## 4. Notes (not gaps)
- N-C1 (quote form). [MΦ]'s quote joins MPGS l. 97 and 98 with "…" and drops "**". The lane's checker accepts it; my strict one does not.
  The content is faithful. This is the recurring "… over a line break" theme; quote the two lines separately.
- N-C2 (LEN-MONO / COMPOSE scope). The proofs need only "λ constant on R", not maximality. Theorem COMPOSE's phase statement applies LEN-MONO
  to a phase, which is a sub-stretch of a λ-run. Say "any stretch with λ (λ^U) constant" in LEN-MONO and Theorem COMPOSE. One word.
- N-C3 (§6, Odd side). For λ^U-runs on G^d, MATCHED / CARRY / NM^U are read with G^d's parities (Ω + 1, same ranks). "NM* over both
  players" should say so. The bound holds because MATCH-Φ is parity-agnostic. My check reads them that way: NM_O, 0 violations.
- N-C4 (§6 status). [MΦ] is signed by REFEREE-2 (record: R2-N5-MPGS.md, successor 19). REFEREE's MPGS report is not yet out (name count 0
  at 11:54Z). So §6 stays an implication until [MΦ] lands, as the packet labels it.
- N-C5 (READING §7 "L/S1 ≤ 1, S1/S2 ≤ 0.75 per phase"). My max S1/S2 is 0.8 on lib41 λ^U-runs (Odd side on λ^U-runs, not phases). That
  is not the packet's quantity, so there is no conflict. Noted because the packet's 0.75 is a per-phase Even figure.

## 5. DONE / FINDINGS / NEEDS
- DONE: this report; docs/referee-2/R2-N5-COMPOSE/{compose_check.py, named.lst, run_all.sh, logs/ (pinned_check.txt included)}.
- FINDINGS:
  - SW-RETURN, LEN-MONO, Theorem COMPOSE and COMPOSE-RUN all SIGNED, with no gap. COMPOSE-NM is SIGNED as an implication.
  - The three pressure points hold: (1) only R47 Lemma Φ (c), every game, read per map; (2) every transition, fallbacks included, is in
    exactly one kind and charged; (3) MPGS (A)'s proof uses only "c fixed", so the λ-run replacement is the same proof.
  - Pinned quotecheck and compose.py are reproduced exactly.
  - My own checker shows 0 violations on 14,428 runs.
- NEEDS: Lead: route N-C1..N-C5 to L-SI. I write §C after REFEREE's COMPOSE report.
