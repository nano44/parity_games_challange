# R-N5-SN: REFEREE report on packet P-N5-SN (box 33: OR, TC-SPLIT, R-STICK, SN-PREFIX, H3H2, LEAVE, ABS-COUNT, WK, ABS-L)
Referee: REFEREE (successor 6), Opus 5.5 (owner ruling D15, Lead reading L37). Packet P-N5-SN: the Lead's message of 2026-10-25 03:42Z
(Lead's stamp). Object docs/new/P-N5-SN-box33.md at pinned trunk 2c70ef6, sha1 340d4f298d8ee137b53ff76d7dd81de49f8fa542 (checked:
`git show 2c70ef6:docs/new/P-N5-SN-box33.md | sha1sum`, 139 lines). Author L-NEW successor 13. Written 2026-10-25 03:55Z onward by date -u.
Every verdict is labelled (Opus 5.5, D15). Labels (D18/L40): PROVED (by whom) / CONJECTURE / OPEN. Independent of REFEREE-2:
docs/referee-2/ not read for this packet.
Dependencies read at trunk d1091416 (merged into claude/referee):
- R28 (my R-N5-OE: U-loc, OE and its step 2);
- R25 CAP-1 (R-N5-FB §4.2, which I re-derived in R-N5-OE §2.2);
- R23 (g) WM, with its proof in docs/si/N5-X-box4.md §8 l. 278-284;
- R24 (a)/(b) Lemma R and TB;
- R19 (a), R21 (a);
- P-N5-LP §3 (WAKE) and its fixes;
- P-N5-CLS §5-§6 (NL, CLS1; my R-N5-CLS with §C).

## Verdicts
| statement | lane label | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §0 phase-key transfer of WM (Lead's ask 1) | — | VALID: WM's proof uses only τ_{k+1} = τ_k at a non-fallback step and S4a's arena optimum (§0 below) |
| §1 Lemma OR | PROVED (L-NEW succ. 13) | SIGNED |
| §2 Lemma TC-SPLIT | PROVED | SIGNED |
| §3 Lemma R-STICK | PROVED | SIGNED |
| §3 Corollary SN-PREFIX | PROVED | SIGNED |
| §4 Lemma H3H2 | PROVED | SIGNED |
| §5 Lemma LEAVE | PROVED | SIGNED WITH GAP SN-3 (wording: the r_s = ⊥ case is not "empty"; the existence half still holds, by a one-line argument, §5) |
| §6 Corollary ABS-COUNT | PROVED | SIGNED WITH GAPS SN-1, SN-2. SN-1: the proof's "ends ≤ d_o − 1" needs H1 at the run's last state, which is not given. What is proved is #H1-ε ≤ d_o + REL_run, one more. The packet's (d_o − 1) form is OPEN; 0 counterexamples, and it is tight in data. SN-2: the per-phase sum omits ε-transitions at fallback transitions; add + f. |
| §7 Lemma WK | PROVED | SIGNED (data vacuous: the hypothesis "W unchanged at a and z" held at none of 49 wakes) |
| §8 Lemma ABS-L | CONDITIONAL on NL / CLS1 | SIGNED; its premise (P-N5-CLS NL, CLS1) is signed by both referees (R-N5-CLS + §C 8af63475; R2-N5-CLS ffe10e1) and is landing as R29. Data vacuous: no θ-change above L in any window |
| §9 EXIT-R / ORX FALSE, H-RE FALSE, K-chain | not to sign | EXIT-R instance checked against LEAVE (consistent); K-chain wakes reproduced (3 + 9 + 31, all even mode); not signed |

R-STICK and SN-PREFIX (the Lead's ask 2): 0 failures.
- Coverage: the 243-file library (21,276 R-STICK vertex checks incl. K-chain), 11,000 random games, and 5 adversarial climbs (~7,500
  mutations, seeded from jcl_zcl_cu_n48 and exitr_cex_n48).
- The proof is three lines and sound (§3).
- The data is thin after the prefix: 89 crossings after a prefix in the library, ~1 in random games. Most crossings (2,555) lie inside
  prefixes.

## 0. Phase key and WM (the Lead's ask 1)
- The packet's PHASE is (λ_Ξ, τ) constant (R27 / R28). R19-R25 are signed under (λ_Ξ, λ_U, τ).
- WM (R23 (g)): the proof (N5-X-box4 §8 l. 278-284; R-N5-Z §4) has three steps.
  - σ_{k+1} is S4a's optimum of the one-player arena (Even restricted to {σ_k(v)} ∪ Iσ_k(v), Odd fixed to τ_k).
  - An optimum dominates every arena strategy pointwise (R17 (F1)), and σ_k is one.
  - W_{k+1} is computed against τ_{k+1} = τ_k.
  So WM needs only τ_{k+1} = τ_k at a non-fallback transition, which the coarse key gives. VALID.
- Inside either key a non-fallback transition has Iσ_k ≠ ∅, otherwise τ would change (R-N5-Z §4).
- The other citations are statewise (R19 (a), R21 (a) XW, CAP-1) or already transferred in R28 (U-loc, OE step 2).

## 1. Lemma OR (SIGNED)
- (a) is R28's OE step 3 argument without H1.
  - If x0's H_{k+1}-path to c avoided o, its only relevant changes would be Even (𝒞^1O), of level ≤ E_k. U-loc would then freeze
    COARSE_{E_k} for x0, and OE step 2 freezes it for x1.
  - CAP-1 at k (λ(o) ≠ o, valid with o on a cycle too; R-N5-OE §2.2) orders them strictly at level ℓ > E_k. (C1)-(C3) carry the strict
    order to k+1, against CAP-1 at k+1.
  - So the path visits o, and the (σ_{k+1}, τ)-play agrees with it up to o. Correct.
- (b) is OE step 3 (H1 ⇒ x0 ∈ F_k). Correct.
- (c): lev(Ξ_k x1, Ξ_{k+1} x1) ≤ E_k < ℓ, so the ultrametric gives lev(Ξ_k x0, Ξ_{k+1} x1) = ℓ exactly, with the direction of the
  COARSE_{E_k} comparison.
  - o lies on neither path. x0's H_k-path to c can never visit o: H_k is functional and σ̄_k(o) = x0, so a visit would loop without
    reaching c. This holds without H1.
  - Since c ≠ o, (C7) with π = o applies. Correct.
- DATA: 327 ε-transitions (library), all with H1; (a), (b), (c) 0 failures.

## 2. Lemma TC-SPLIT (SIGNED)
- λ(o) = o ⇒ θ = (o, ∅, 0) constant. So λ(o) ≠ o, and (C7) with π = o equates lev(θ_k, θ_{k+1}) with lev(Ξ_k x0, Ξ_{k+1} x1). Both paths
  avoid o, as in §1 (c).
- U-loc on x1 gives ≤ E_k. (C6) gives ≤ max(O_k, E_k). The case O_k > E_k gives = O_k by OR (c).
- With x0 = x1, O_k = ⊥ and the bound is E_k. Correct.
- DATA: 1,664 θ-changes (library) + 815 (random), 0 failures.

## 3. Lemma R-STICK and Corollary SN-PREFIX (SIGNED)
- Preamble: v ∈ R_s has λ(v) = c_θ and W-cycle node c_w(s) (both plays follow v's route to o, then o's play). Correct. R-STICK's
  hypothesis is therefore exactly c_w(s) ≠ c_θ, for every v ∈ R_s.
- R-STICK: suppose v ∈ R_s leaves R at an S4a step.
  - G (a) at s+1 gives W_{s+1}(v) = Ξ_{s+1}(v), with cycle node c_θ (phase). WM gives W_{s+1}(v) ⊵ W_s(v), whose cycle node is c_w.
    The nodes differ, so rew(c_θ) > rew(c_w); rewards are injective, si.py l. 42-44.
  - XW at s gives rew(c_θ) < rew(c_w).
  - Contradiction. Correct.
- SN-PREFIX:
  - WM at o makes w non-decreasing along a fallback-free run, so rew(c_w) is non-decreasing.
  - XW at o gives rew(c_w) ≥ rew(c_θ), with equality ⟺ c_w = c_θ. So the equality states form a prefix.
  - After the prefix every step is S4a with c_w ≠ c_θ, and R-STICK makes R non-decreasing. Each crossing then adds a vertex, so there
    are ≤ n − 1 of them.
  - The per-phase count, f fallbacks splitting ≤ f + 1 runs, with crossings at fallbacks ≤ f, is correct. Correct.
- DATA (0 failures each):
  - R-STICK: 8,138 (library) + 13,138 (K-chain) + 75 (random) vertex checks.
  - Prefix property and no R-loss after the prefix: 638 library runs + 3,938 random runs.
  - Crossings after the prefix ≤ n − 1: max 89 in total over the library, all within the bound.
  - Per-phase crossing bound: 0 failures.

## 4. Lemma H3H2 (SIGNED)
- Under H1, the honest cycle of c_θ avoids o, and its vertices' (σ, τ)-plays equal their honest plays, so c_θ ∈ F.
- H3 puts c_θ on o's W-cycle. In the functional W-graph that cycle is c_θ's own (σ, τ)-cycle, the honest cycle, which avoids o. So H2.
  Correct.
- DATA: 5,140 (library) + 18,040 (random) states with H1 ∧ H3; H2 at all.

## 5. Lemma LEAVE (SIGNED WITH GAP SN-3)
- (h) follows from R-STICK (contrapositive) and H3H2. Correct.
- The level bound:
  - Lemma G (b) and (C7) give lev(Ξ_s q, W_s q) = r_s; the disjointness is as in CLU (R-N5-CLS §1).
  - XW, then G (a) and WM at s+1, give Ξ_s(q) ◁ W_s(q) ⊴ Ξ_{s+1}(q). (C5) gives lev(Ξ_s q, Ξ_{s+1} q) ≥ r_s.
  - U-loc with L = r_s − 1 then forces a relevant change of level ≥ r_s on q's H_{s+1}-path before λ(q). Correct.
- SN-3 (wording): "if r_s = ⊥ the claim is empty" is not quite right. The claim also asserts that a relevant change exists, and that
  half holds with a different argument:
  - q's (σ, τ)-play changes before o. Odd vertices other than o are forced, so some Even p on q's old route switches.
  - The common prefix of q's old and new routes lies in R_s, and c_θ ∈ F_s (H1). So p comes before λ(q) on q's H_{s+1}-path.
  - λ(p) = c_θ ≠ p, so the change is relevant.
  Replace "empty" by this line.
- DATA: 637 (library) + 1,441 (random) H1 leaves, plus exitr_cex_n48's leave. (h) at every one; a relevant change of level ≥ r_s on
  q's path at every one; 0 failures.

## 6. Corollary ABS-COUNT (SIGNED WITH GAPS SN-1, SN-2)
- The counting argument tracks N_t = #exits of o in R_t:
  - each H1 ε-transition moves x0 from F to R (OR (a), (b));
  - N decreases only by exit leaves (REL);
  - under H1, σ̄(o) ∈ F, so N_t ≤ d_o − 1 at H1 states.
- SN-1 (proof gap): the proof ends with "it ends ≤ d_o − 1". That holds only if H1 holds at the run's LAST state. H1 is constant only on
  crossing-free intervals (TC (i)), and an ε-transition is a crossing (R28 OE).
  - If the last H1 ε-transition t_m lands at a ¬H1 state, x1 = σ̄_{t_m+1}(o) lies in R as well, and N can reach d_o.
  - What the argument proves: N_{t_m} ≤ d_o − 1 (H1 at t_m) and N_{t_m} ≥ (m − 1) − REL, so m ≤ d_o + REL_run.
  - Nothing in the packet excludes an H1 ε-transition into a ¬H1 state.
  - DATA: no such transition anywhere (0 in 243 library files, 11,000 random games; 0 after 5 climbs that score exactly this event,
    ~7,500 mutations); the packet's (d_o − 1) form holds with equality in several runs (max excess 0).
  - Repair: state (d_o − 1) + REL_run with the extra hypothesis "H1 at the run's last state", and d_o + REL_run in general. Or prove that
    an H1 ε-transition keeps H1. That would close it; I did not find a proof.
- SN-2 (statement gap): the per-phase form "ε_{H1} ≤ (d_o − 1)(f + 1) + REL" sums the run bounds over the ≤ f + 1 fallback-free runs.
  ε-transitions AT fallback transitions belong to no run. Each fallback is at most one transition, so add + f. With SN-1 the proved
  per-phase form is d_o(f + 1) + REL + f. DATA: 0 ε-transitions at fallbacks (library and random), so the term is untested.
- The second sentence ("every such leave happens in the c_w = c_θ prefix; under H1 at an (h) state via a relevant change of level ≥ r")
  is R-STICK + LEAVE. Correct.

## 7. Lemma WK (SIGNED; data vacuous)
- I checked the proof against R24 (a)/(b) (the odd-mode choice: minimum index among fully optimal arena successors).
- Case "z not fully optimal at k′":
  - Bellman at the arena optimum k′ (R24 G-TB-1 closure) gives W_{k′}(y) ▷ y ⊕ W_{k′}(z).
  - At k′ + 1, with W unchanged at a and z, the choice z would give W_{k′+1}(y) = y ⊕ W(z) ◁ y ⊕ W(a) ⊴ W_{k′+1}(y), by Bellman with a
    in the arena H_{k′}.
  - Contradiction, in either mode.
- Case "z fully optimal and a < z":
  - At k′ + 1, a is fully optimal too: y ⊕ W(a) = W_{k′}(y) = y ⊕ W(z) = W_{k′+1}(y).
  - The odd-mode rule then picks a, not z. The mode is fixed by the cycle node of W(y), which is equal at k′ and k′ + 1 here.
- So z can win only in the even (BFS) mode. Correct. The packet's last sentence is loose ("the cycle node of W(a) = W(z), or of the
  strictly better a"): only the second case needs the mode, and there W(a) and W(z) have the same cycle node. Wording, not counted.
- DATA:
  - 49 wakes: 6 library, 43 K-chain (kchain4 / 10 / 32: 3 / 9 / 31, reproduced), all in even mode.
  - WK's hypothesis (W unchanged at a and z) held at NONE of them. In K-chain W changes at z, as the packet says.
  - So the lemma is untested by data; it rests on the proof.

## 8. Lemma ABS-L (SIGNED; premise signed by both referees, landing as R29)
- (A_j) on [k0+1, k] is CLS1's chain (OFFGATE base, NL (iii)), with (h) and r_j > L on the window.
- σ̄(o) unchanged ⇒ NL (i) freezes Ξ(x0) above L (x0 ∈ F_{j+1}, H1). Then (C7) with π = o gives a θ-level ≤ L.
- σ̄(o) changes with x0 ∉ R_{j+1} ⇒ both exits are frozen above L. CAP-1 at j and j+1 then forces lev(Ξ_j x0, Ξ_j x1) ≤ L, so
  lev(θ_j, θ_{j+1}) ≤ L by (C6).
- So x0 ∈ R_{j+1} ∖ R_j, at level O_j, and NL (ii) keeps x0 in R̄ on [j+1, k].
- The count ≤ d_o − 1 holds: at state k, H1 holds (k ∈ S), so σ̄_k(o) ∈ F_k, and the absorbed exits are distinct and all in R_k.
  (SN-1 does not arise here: H1 at the end is given.) Correct.
- DATA: 377 windows (k0, k) in the library, 153 θ-changes inside them, ALL at level ≤ L. The absorption branch never occurred, so the
  conclusion is untested by data and rests on the proof.

## 9. Not to sign
- exitr_cex_n48 (sha1 7a663df2…): my probe sees its H1 leave at an (h) state with a relevant change of level ≥ r on the leaver's path
  (LEAVE holds). Its ABS-COUNT runs are within (d_o − 1) + REL (excess 0). I did not re-derive EXIT-R / ORX themselves.
- K-chain (kchain4 2be32f30…, kchain10 4af3726f…, kchain32 63c5b0dd…): n5.py 6/1, 12/1, 34/1; check_sol2.py "zielonka(oink zlk) OK
  strategies verified" for all three; wakes 3 / 9 / 31 per my own wake definition (P-N5-LP §3).

## 10. Data (DATA, not proof; docs/referee/scratch/sn_probe.py sha1 dfdf786d…, absc_climb.py sha1 4f183c6f…; own N5 trace asserted
equal to n5.run; every game asserted in 𝒞^1O; phase key (λ_Ξ, τ), scope runs (λ_Ξ, λ_U, τ))
| run | games | phase transitions | key counts | failures |
| --- | --- | --- | --- | --- |
| library (every experiments/**/*.pg in 𝒞^1O, n ≤ 64; 243 files at d1091416) | 243 | 5,774 | ε 327 (all H1); θ-changes 1,664; R-STICK 8,138; runs 638 (crossings 2,555 in prefixes / 89 after); H1 leaves 637; ABS-L windows 377 | 0 |
| K-chain (kchain4/10/32, n 58/124/366) | 3 | 49 | wakes 43 (even mode); R-STICK 13,138 | 0 |
| rand 4000 n 8-24 seed 9101; rand 1500 n 20-40 seed 9102 | 5,500 | 2,839 | θ-changes 454; leaves 722; ε 2 | 0 |
| randb (extra edges into o and from o) 4000 n 8-24 seed 9103; 1500 n 20-40 seed 9104 | 5,500 | 2,563 | θ-changes 361; leaves 719 | 0 |
| climbs absc_climb.py (score: ABSC excess, H1-ε into ¬H1, ε count), 1,500 steps each, 3 from jcl_zcl_cu_n48, 2 from exitr_cex_n48 | 5 | — | best ε 16-18 per game; H1-ε into ¬H1 0; ABSC excess max 0 | 0 |
- The thin spots are named in each section above: WK (hypothesis never met), ABS-L (absorption branch never met), ABS-COUNT's fallback
  term (no ε at fallbacks), the ¬H1 branch of OR (no ¬H1 ε-transition), and crossings after a prefix (89).

## 11. Labels after this report (D18/L40)
- PROVED (L-NEW successor 13; signed by REFEREE (Opus 5.5, D15), second referee pending), on 𝒞^1O inside a phase: OR, TC-SPLIT, R-STICK,
  SN-PREFIX, H3H2, LEAVE (SN-3 wording), WK.
- ABS-COUNT is PROVED in the form "#H1-ε per fallback-free run ≤ d_o + REL_run; per phase ≤ d_o(f + 1) + REL + f". The (d_o − 1) form is
  proved when H1 holds at the run's last state; in general it is OPEN (CONJECTURE, 0 counterexamples).
- ABS-L is PROVED given R29 (NL, CLS1), whose premises are signed by both referees.
- OPEN: REL per phase, X_SN, K per phase, G-N5-TIME. Not a TARGET.md claim, not a step-4 pass. The TARGET.md diff is empty.

## Fixes-file lines (one per gap)
- SN-1: §6: "#H1-ε ≤ d_o + REL_run (proved); ≤ (d_o − 1) + REL_run if H1 holds at the run's last state; the unconditional (d_o − 1)
  form is OPEN (an H1 ε-transition into a ¬H1 state is not excluded)".
- SN-2: §6 per phase: "+ f for ε-transitions at fallback transitions" (with SN-1: d_o(f + 1) + REL + f).
- SN-3: §5: replace "if r_s = ⊥ the claim is empty" with "if r_s = ⊥, a relevant change still exists: some Even p on q's old route
  before o switches; it precedes λ(q) = c_θ ∈ F_s on q's H_{s+1}-path, and λ(p) ≠ p".

## Addendum (written 2026-10-25 04:02Z by date -u): L-RED probes relayed by the Lead (03:52Z message, read 04:01Z after my report)
- epsseg_cex_n48.pg (experiments/red/so/instances, sha1 b4c7dcb0…; n5.py 26 / 1; check_sol2.py "zielonka(oink zlk) OK strategies verified";
  one Odd choice vertex asserted): 17 ε-transitions, all H1. ABS-COUNT holds with the REL term: max excess 0, i.e. #H1-ε ≤ (d_o − 1) + REL_run
  in each run, with REL ≥ 1 where the count exceeds d_o − 1 (exit 33 released at an S4a step and re-absorbed, as L-RED says). OR, TC-SPLIT,
  R-STICK, SN-PREFIX, LEAVE (1 leave), H3H2: 0 failures.
- exitr_cex_n16.pg (sha1 6971211e…; n5.py 10 / 0; Oink OK, strategies verified): 5 ε (H1), 2 leaves; 0 failures, excess 0.
- Neither instance has an H1 ε-transition into a ¬H1 state, so SN-1 is unchanged: proved bound d_o + REL_run, the (d_o − 1) form OPEN. Verdicts
  unchanged.

## §C. Comparison with REFEREE-2 (R2-N5-SN, referee-2 ddbecaf + §A 91d95e8, on trunk de655692); written 2026-10-25 04:11Z onward by date -u
Read only after my report (59a886d1) and addendum (58dd6e86) were pushed, and after the Lead said R2-N5-SN exists (04:08Z).

### C.1 Verdicts
| statement | REFEREE | REFEREE-2 | joint |
| --- | --- | --- | --- |
| WM transfer to (λ_Ξ, τ) | VALID | VALID | VALID (same reason: only τ_{k+1} = τ_k and S4a's arena optimum) |
| OR, TC-SPLIT, R-STICK, SN-PREFIX, H3H2 | SIGNED | SIGN | SIGNED by both |
| LEAVE | SIGNED WITH GAP SN-3 (wording) | SIGN ("r_s = ⊥ vacuous") | SIGNED by both; see C.2 |
| ABS-COUNT | SIGNED WITH GAPS SN-1, SN-2 | SIGN WITH GAPS G-SN-1 (a), (b) | SIGNED by both in the repaired form; packet's d_o − 1 form CONJECTURE / OPEN |
| WK | SIGNED | SIGN (N-SN-1) | SIGNED by both |
| ABS-L | SIGNED (premise signed by both) | SIGN as CONDITIONAL, condition met on R29 | SIGNED by both; R29 has now LANDED (cf6801e), so the condition is met |
No verdict differs. Neither referee found a counterexample.

### C.2 Item by item
- SN-1 = G-SN-1 (a), and SN-2 = G-SN-1 (b). We found the same gap independently, with the same mechanism and the same repaired statement:
  - per fallback-free run, ε_{H1} ≤ d_o + REL_run, and ≤ (d_o − 1) + REL_run when the run's last state has H1;
  - per phase, ε_{H1} ≤ d_o(f + 1) + f + REL.
  The packet's form is a CONJECTURE with 0 counterexamples in both batches. REFEREE-2 ran 30,400 targeted climb runs; I ran 5 climbs
  aimed at the H1-ε → ¬H1 event.
- REFEREE-2's §A on epsseg_cex_n48 sharpens this. The packet's form holds there with EQUALITY (16 + 1 = 17). The mechanism G-SN-1 (a) fears
  (σ̄(o) entering R so that N reaches d_o) does occur, at 25 → 26, but that step leaves the phase. So it is a real mechanism, not yet seen
  inside a phase. I accept this. My addendum saw excess 0 on the same file without locating the phase-exit step. The repair direction is
  REFEREE-2's: show that inside a phase the state after an H1 ε-transition again has an exit in F.
- SN-3 (LEAVE, r_s = ⊥): REFEREE-2 reads the case as vacuous, as the packet does. The statement also asserts that a relevant change EXISTS
  on q's path, and for r_s = ⊥ that half needs its own one-line argument (my §5). With it the statement is true in both readings, so this
  is wording only. I keep it as an optional fixes-file line.
- N-SN-1 (WK: y ⊕ strictly monotone between W(z) and W(a)): I did not raise it. My §7 route compares the ⊕-values directly:
  - at k′, y ⊕ W(a) = W_{k′}(y) ▷ y ⊕ W(z) (Bellman, and z is not fully optimal);
  - at k′ + 1 both ⊕-values are unchanged, because W is unchanged at a and z.
  So it needs only the Bellman form W(y) ⊵ y ⊕ W(x) at an arena optimum (R24 G-TB-1 closure), not monotonicity of y ⊕.
  REFEREE-2's argument that y lies on neither W-path is also correct, and it justifies the packet's own wording. Accepted as a wording line.
  Either route closes it.
- Data agree where they overlap:
  - every ε-transition is H1 (REFEREE-2 725 over 3 starts; me 327 at the canonical start), with 0 at fallbacks;
  - ABS-L is vacuous (583 intervals vs my 377 windows; 0 θ-changes above L);
  - WK is vacuous (52 vs 49 wakes; the hypothesis is never met);
  - there is no ¬H1 ε-transition anywhere, so OR (c)'s ¬H1 branch rests on the proof.
  REFEREE-2's climbs give much more R-STICK coverage after a prefix (39,461 crossings vs my 89 in the library). That closes the thin spot
  I named.

### C.3 Joint gap map (one fixes-file line per row)
| row | REFEREE | REFEREE-2 | status | fixes-file line |
| --- | --- | --- | --- | --- |
| 1 | SN-1 | G-SN-1 (a) | proof gap; repaired form proved | §6: "per fallback-free run ε_{H1} ≤ d_o + REL_run, and ≤ (d_o − 1) + REL_run if the run's last state has H1 (proved); the unconditional (d_o − 1) form is a CONJECTURE (0 counterexamples; tight on epsseg_cex_n48, where N reaches d_o only at the phase exit 25 → 26)" |
| 2 | SN-2 | G-SN-1 (b) | statement gap; repaired | §6 per phase: "ε_{H1} ≤ d_o(f + 1) + f + REL (the + f covers ε-transitions at fallback transitions; 0 seen)" |
| 3 | — | N-SN-1 | wording | §7: "y lies on neither W-path of a, z (y ∈ R reaches o; z's play cannot pass y before o; after o only on o's W-cycle, below c_w), so y ⊕ is strictly monotone there; alternatively compare the ⊕-values directly via Bellman (R24 G-TB-1)" |
| 4 | SN-3 | (reads as vacuous) | wording, optional | §5: "if r_s = ⊥, a relevant change on q's path still exists: an Even p on q's old route before o switches; it precedes λ(q) = c_θ ∈ F_s, and λ(p) ≠ p" |
| 5 | (§8) | (§8) | condition met | §8: "ABS-L's premise NL / CLS1 is RESULTS R29 (landed cf6801e)": drop CONDITIONAL |

### C.4 Joint label (D18/L40)
- PROVED (L-NEW successor 13; REFEREE and REFEREE-2, Opus 5.5, D15), pending CHECKER, on 𝒞^1O inside a (λ_Ξ, τ) phase: OR, TC-SPLIT, R-STICK,
  SN-PREFIX, H3H2, LEAVE, WK, ABS-COUNT in the repaired form (row 1-2), ABS-L (on R29).
- CONJECTURE: ABS-COUNT's (d_o − 1) form. OPEN: REL per phase, X_SN, K per phase, G-N5-TIME.
