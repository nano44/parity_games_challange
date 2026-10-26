# R-N5-ENT: REFEREE report on packet P-N5-ENT (box 11: FZ, BF, RB, WALK, CYC-EV, TEV-FB; ENT-X with NJB-A, D1, PL-S″)
Referee: REFEREE (successor 8, session_01YRPeH49wEXXq7vW5qK35Gz), Opus 5.5 (owner ruling D15, Lead reading L37).
- Routing: the Lead's queue of 12:55Z (Lead's stamp).
- Object: docs/si/P-N5-ENT-box11.md at pinned trunk 765e893, sha1 4fd22be79f7050a7f466288c76eea8bfe2f669d0, 198 lines. Checked with
  `git show 765e893:docs/si/P-N5-ENT-box11.md | sha1sum`. Author: L-SI successor 6.
- Written 2026-10-25T13:06Z onward by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independence: I did not read docs/referee-2/R2-N5-ENT.md.
  - Disclosure: I had already checked §1-§3's content as the RL fixes source (docs/si/N5-TEV-box11.md, sha1 58a0b3cf), in R-N5-RL
    Addendum A2 (d104aac2), after reading R2-N5-RL.
  - The packet's §1-§2 differ from that text only in rewording (diffed). TEV-FB, §4 and §5 are checked here for the first time.

## Verdicts
| § | statement | packet label | verdict (Opus 5.5, D15) |
| --- | --- | --- | --- |
| §1 | Lemma FZ, Lemma BF | PROVED (no (P)) | SIGNED |
| §2 | Lemma RB, Corollary WALK (a)-(c) | PROVED (no (P)) | SIGNED |
| §3 | Lemma CYC-EV | PROVED (no (P)) | SIGNED |
| §3 | Proposition TEV-FB | PROVED (no (P)) | SIGNED |
| §4 | Theorem ENT-X (the ENT setting is empty) | PROVED CONDITIONAL on (P), only via EV+ | SIGNED CONDITIONAL ON (P); label exact |
| §5 | Corollary NJB-A, Corollary D1 (D_M ≤ 1), Corollary PL-S″ (≤ 2·n·n_E fallbacks of level ≥ 0 per scope run) | PROVED CONDITIONAL on (P), via ENT-X | SIGNED CONDITIONAL ON (P); labels exact |
| §6 | NJB in full (straddling interval), TEV at S4a states, level −1 fallbacks | not to sign | not signed |

No gaps.
- Labels. (P) enters only through P-N5-RL's EV+: EV ⇐ FREE-FREEZE ⇐ BL (c) ⇐ (P).
  - EV+ was signed CONDITIONAL ON (P) by both referees (R-N5-RL; R2-N5-RL 30dc5f54).
  - TEV-RED is not used, so RL-1 and RL-3 do not arise.
  - (P) itself is P-N5-P1's Lemma P1, signed by both referees (R-N5-P1 58a5b734 + §C; R2 e036e4c5), pending CHECKER. With P1 landed,
    §4 and §5 become unconditional.
- Premises are landed: R15, R19, R29, R31, R35 (the NO-RF-OLD Corollary, ENT-SHAPE (4), RDROP).

## 1. §1-§3 (FZ, BF, RB, WALK, CYC-EV): checked; see R-N5-RL Addendum A2 for the line-by-line check
- The (Σ) facts are correct.
  - (Σ2): (h) at every state of [k0, k], because each is the source of a transition of S.
  - (Σ3): no leave, so F_k ⊆ F_{k0} ⊔ Ev, and Ev ∩ F_k = R_{k0} ∩ F_k.
  - (Σ4): M_k ≤ L (CLS2).
  - (Σ5): c ∈ F_{k0} ∩ F_k.
  - (Σ6): a rise gives B ≠ A, with cycle node c constant.
- RB is the step that needs k to be a fallback state, through (Σ4).

## 2. TEV-FB: checked
- By CYC-EV, an Ev vertex of x_k's play lies on its pre-c path. Take the last one, e = p_i, and f = p_{i+1}.
- Step 1: f ∈ F_k ∖ Ev ⊆ F_{k0}. An Odd e ≠ o would have its unique successor in R̄_{k0}. Correct.
- Step 2.
  - FZ at f, then BF at e (b_k(e) = Ξ_k(f)), then Lemma G at u_e ∈ R̄_{k0}, give COARSE_L(Ξ_k f) = (c, (π_{u_e} ∩ H) ⊔ A).
  - The path part lies in F_{k0}, so π_{u_e} ∩ H = ∅ and o ∉ A.
  - o is the first vertex of θ_{k0}'s play and not its cycle node (H1), so o ∈ P(θ_{k0}) iff rank o > rank c. Hence o ∉ H. Correct.
- Step 3: (P2) along o, p_0, …, p_i (none is c; their cycle node is c), then (C4), give B = ({p_0..p_i} ∩ H) ∪ A ⊋ A. Correct.
- Step 4: WALK (c) from e (π_e = {e} ⊔ π_{u_e}, the part after e low) gives B ⊆ A. Contradiction. Correct.
- It uses a rise and (Σ4) only. It does not use M_k = L or (P). It is TEV at the fallback state k. L-RED's tevlast_cex_n40, a failure at
  an S4a state, is consistent with this: the gate (15, 21) of level 33 > L at t = 7 is exactly what (Σ4) forbids at k.

## 3. ENT-X and §5: checked
- ENT-X. EV+'s hypotheses are the ENT setting, word for word (P-N5-RL §6: consecutive fallbacks k0 < k of S, M_{k0} = M_k = L ≥ 0,
  r > L on [k0+1, k], a rise).
  - EV+ says x_k's play meets Ev; TEV-FB says it avoids Ev. Contradiction, so the setting is empty.
  - There is no circularity: TEV-FB does not use EV+ or any (P) item.
- NJB-A.
  - The first change j of a dirty interval is an S4a step with lev(θ_j, θ_{j+1}) > M (R31 PL (b)): a rise.
  - Consecutive fallbacks of a block are consecutive fallbacks of S (CLS2, P-N5-NJB §0), so the interval is the ENT setting with
    L = M = M_{f_i} = M_{f_{i+1}}.
  - Correct.
- D1. r is non-increasing along S (Fact R). Intervals fall into three kinds:
  - r > M throughout: clean (NJB-A);
  - r ≤ M at f_i + 1: clean, since RDROP puts the first change at r_j > M and r stays ≤ M;
  - the straddling interval: at most one, since after r ≤ M it stays ≤ M.
  - Correct.
- PL-S″: R31 PL (a), N ≤ n_E(1 + D_M), per block, over ≤ n levels ≥ 0. So ≤ 2·n·n_E. Correct.
  - This removes REL(S) from R35 PL-S′ (conditional on (P)).
  - It is not a running-time bound: level −1 fallbacks and the out-of-scope parts remain (§6; G-N5-TIME open).

## 4. DATA (DATA, not proof; own code docs/referee/scratch/cyc_probe.py, rl_probe.py; logs rl_logs/cyc_*.txt)
- Own engine, no lane code; 𝒞^1O asserted.

| set | (Σ) pairs | FZ | BF | RB | WALK | failures (FZ, BF, RB, WALK, M_k ≤ L, Ev on C_k) | pairs with a rise |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NAMED (75) | 262 | 6,177 | 515 | 344 | 529 | 0 | 0 |
| LIB (234) | 377 | 10,525 | 1,080 | 578 | 1,121 | 0 | 0 |
| tev_cex_n40 (L-RED; input only) | 15 | 414 | 19 | 16 | 19 | 0 | 0 |

- The pair, RB and WALK counts equal the packet's §7 exactly (262 / 344 / 529; 377 / 578 / 1,121; 15 / 16 / 19). The packet's RB / BF
  column counts RB checks; my BF column also counts BF at Even v whose a stays in F.
- Thin spot: no (Σ) pair with a rise exists in any data, mine or the lane's. So CYC-EV, TEV-FB, ENT-X and §5 have vacuous hypotheses in
  data and rest on the proofs. ENT-X's conclusion is itself that the setting is empty, which fits.
- My earlier RL climbs (R-N5-RL §8.1) also never produced the ENT setting.

## TARGET.md diff
Not a claim of TARGET.md §2. These are lemmas about N5 on 𝒞^1O inside scope runs, and the packet says so: "not a running-time bound …
G-N5-TIME stays OPEN". PL-S″ bounds fallbacks of level ≥ 0 per scope run only.

Signed: REFEREE (successor 8) (Opus 5.5, D15).

## §C. Comparison with REFEREE-2 (written 2026-10-25 14:33Z by date -u; REFEREE successor 8 (Opus 5.5, D15))
- Compared against: the FINAL docs/referee-2/R2-N5-ENT.md at referee-2 b7df84b8 (trunk d39644c), named by the Lead at 14:33Z (Lead's
  stamp). I read it after this report (55a3f6fb) was pushed.
- Verdicts: identical.
  - Both referees sign FZ, BF, RB, WALK (a)-(c), CYC-EV and TEV-FB, without (P). R2 also signs the §0 facts (Σ1)-(Σ6); I checked them
    in my §1.
  - Both sign ENT-X, NJB-A, D1 and PL-S″ CONDITIONAL ON (P), with (P) entering only through EV+.
  - Neither signs §6.
- Joint gap map: empty. R2's notes:

| R2 note | what it says | checked | this lane | joint status |
| --- | --- | --- | --- | --- |
| N-ENT-1 | ENT's CYC-EV has the RL-fixes conclusion under a weaker hypothesis, (Σ) + rise without M_k = L; its proof uses only M_k ≤ L (CLS2), so ENT's form implies RL's | correct. My R-N5-RL A2 noted the same ("does not use M_k = L"), and so does the packet's §3 setting line | same reading | ACCEPTED (note) |
| N-ENT-2 | §7's "vacuous everywhere" is too strong: NJB-A's hypothesis (an interval with r > M throughout) occurs, 698 / 601 / 701 times, all clean | correct. A (Σ) pair is exactly NJB-A's hypothesis. My own data has 262 + 377 + 15 such pairs, all clean (0 rises). D1 and PL-S″ concern every block, so they are non-vacuous as statements too. Only CYC-EV, TEV-FB and ENT-X (which need a rise) are vacuous | MISSED: my §4 repeated the lane's "§3-§5 have vacuous hypotheses". Corrected here: vacuous only for CYC-EV, TEV-FB and ENT-X; NJB-A's conclusion is exercised (clean) at 654 pairs | ACCEPTED (wording, packet §7 and my §4) |
| N-ENT-3 | §0's status of the RL report is stale | packet §0: "REFEREE-2's report is pending". RL has since converged (R2 30dc5f54, §C 88571b0) and landed as R37 | not flagged | ACCEPTED (note) |

- Fixes-file lines (L-SI, P-N5-ENT; none blocks a signature):
  - N-ENT-1: §3, note that CYC-EV and TEV-FB need only M_k ≤ L, so they imply the RL-fixes form.
  - N-ENT-2: §7 thin spot: "vacuous" → "vacuous for CYC-EV, TEV-FB, ENT-X; NJB-A / D1 hypotheses occur (all clean)".
  - N-ENT-3: §0: P-N5-RL status → RESULTS R37.
- R36 lifts the (P) condition: yes.
  - ENT-X, NJB-A, D1 and PL-S″ use (P) only through EV+ (R37). EV+ uses it only through FREE-FREEZE ⇐ BL (c), i.e. (P) on the one-player
    game G_τ[F_k].
  - R36 (d) states P1 exactly for G[X], G_τ and G_τ[F_k].
  - So with R36 and R37 landed, all four are PROVED without condition, as R37 recorded for EV, EV+ and TEV-RED′.
  - This adds no running-time bound: G-N5-TIME stays open (level −1 fallbacks; the straddling interval of NJB).
- Joint state: P-N5-ENT §1-§5 is signed by both referees (Opus 5.5, D15), pending CHECKER. Its labels are PROVED (§1-§3), and PROVED
  after R36 (§4-§5).
