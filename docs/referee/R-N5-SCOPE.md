# R-N5-SCOPE: REFEREE report on packet P-N5-SCOPE (box 36: KEY, WCH, SCOPE-COUNT, FB-INT, NH1-FB, CN-LAST)
Referee: REFEREE (successor 7, session_01TWT1diK1Z9x2eK56iBVbZu), Opus 5.5 (owner ruling D15, Lead reading L37). Packet P-N5-SCOPE: the
Lead's message of 2026-10-25 10:58Z (Lead's stamp). Object docs/new/P-N5-SCOPE-box36.md at pinned trunk 8998ee6, sha1
c3f5ed3788f0853939d247dbcfb970334c9dcf7d (checked: `git show 8998ee6:docs/new/P-N5-SCOPE-box36.md | sha1sum`, 320 lines). Author L-NEW
successor 16 (proofs by successor 15). Written 2026-10-25 11:08Z onward by date -u.
Every verdict is labelled (Opus 5.5, D15). Labels (D18/L40): PROVED (by whom) / CONJECTURE / OPEN. Independent of REFEREE-2:
docs/referee-2/R2-N5-SCOPE.md not read.

## Verdicts
| statement | lane label | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 Remark KEY (every game) | PROVED (L-NEW succ. 15) | SIGNED |
| §2 Lemma WCH | PROVED | SIGNED |
| §3 Corollary SCOPE-COUNT | PROVED | SIGNED (premise RESTARTS, P-N5-TOG = R34 at CHECKER) |
| §4 Lemma FB-INT | PROVED | SIGNED |
| §5 Corollary NH1-FB | PROVED | SIGNED (premises R-CONST = R33, TOGGLE-COUNT = R34) |
| §6 Lemma CN-LAST (every game) | PROVED | SIGNED |
| §7 out-of-SN fallbacks, OUT-POLY, PF-THETA linear | not to sign | not signed |
No gaps.

## 0. The packet header's changes against its source, checked
- Source docs/new/N5-SCOPE-box36.md: sha1 7496a2c3… at l-new a670161b and on trunk (checked). N5-DROP-box35.md: sha1 e3a4e7be… (checked).
- Citation correction: R-CONST is P-N5-L2 §5, not "§11". Correct.
- The five "(filled in)" steps:
  1. WCH, TC (i) statewise. t0 ∈ R̄ means t0's play reaches o, so o lies on a W-cycle (t0 = o included); t0 ∈ F means o is not on the cycle
     t0's play ends in. Correct.
  2. SCOPE-COUNT, distinct starts. Maximal disjoint runs have distinct first transitions. Correct.
  3. NH1-FB, counting the runs S. Every maximal ¬H1 run other than the first begins with a drop, and drops ≤ ⌈T/2⌉. Correct.
  4. CN-LAST (i), after c_i. The new play is c_i → z_i ⇝ c_i along z_i's old path, which meets no c_j. Correct.
  5. CN-LAST (ii), an unswitched Even vertex. S4c switches every Even vertex with a gate, so an unswitched vertex had none. Correct.
- The statements equal the source's.
- Citations: F1° and TC = R22 (a)/(b); FB per tame run = R25 (d), proof P-N5-FB §4; J1 = R25 (e); OE and OX (ii) = R28 (b)/(c);
  "an own-cycle-node σ̄(o) change leaves the transition tame" = P-N5-LP §4 step 3 (signed in my lane's R-N5-LP); S (a) = R18 (d);
  R-CONST = R33 (e); (F), TOGGLE-COUNT, RESTARTS = P-N5-TOG (R34).
- Tools: docs/referee/scratch/scope_probe.py and scope_climb.py (own code, `python3 -I`; own trace = n5.run; 𝒞^1O asserted for the C^1O
  checks; general random games for KEY and CN-LAST). No lane script is imported (scopecnt.py, lenrun.py, outclimb.py not run).

## 1. KEY (SIGNED)
- Odd's valuation U_k = Ξ^d_{τ_k} is computed on G^d from τ_k alone (SPEC S1; in the engine, Ed.evaluate(τ)). So λ_U is constant
  wherever τ is.
- Hence a (λ_Ξ, τ)-phase is a joint λ-phase with τ constant, and results signed on the latter apply verbatim.
- This also settles the setting notes my lane wrote case by case: NL in R-N5-FRZ §1, N-OE-3, and scope runs in R-N5-NJB §0.
- DATA (KEY): 7,455 library, 22,121 random 𝒞^1O and 7,219 general transitions with τ unchanged; λ_U unchanged at all of them. 0 failures.

## 2. WCH (SIGNED)
- Under H2, (V1) at o gives w = o ⊕ W(t0), and W = Ξ off R̄ (R19 (a)). So a w-change forces a change of Ξ(t0) with t0 ∈ F.
- Off crossings, the transition lies in one crossing-free interval, where F1° (no (h) needed; joint key via KEY) allows ≤ |F| − 1 ≤ n − 2
  Ξ-changing transitions on F.
- ≤ X + 1 intervals, plus the X crossings. Correct.
- DATA (WCH): 135 library and 618 random WCH transitions; every non-crossing one changes Ξ at t0 ∈ F. Max 20 per phase (library), bound
  never reached. 0 failures.

## 3. SCOPE-COUNT (SIGNED)
- A scope run's first transition k has (h) at k. Two cases:
  - k is the first state of its (h)-run (this includes k being the phase's first state);
  - or (h) holds at k − 1. Then k − 1 → k is an in-phase transition with (h) at k − 1 and H2 at k, and it is not in scope only if w changes:
    a WCH transition.
- Both maps are injective. RESTARTS bounds the (h)-runs. Correct.
- DATA (SC): scope runs ≤ #(h)-runs + #WCH in every phase (225 library scope runs, max 5 per phase; 2,890 random). 0 failures.
  - Climbs FIT = (scope runs, NH1 fallbacks, WCH) per phase, 15 min each, seed 91 random n 5-12 and seed 92 from wd12_s1: maxima (3, 0, 3) and (4, 0, 4)
    (final), 0 failures over 766,585 checked candidates.

## 4. FB-INT (SIGNED)
- Non-tame ⇒ crossing:
  - J1: a non-tame transition switches σ̄(o) above M_k.
  - LP §4 step 3: that change is relevant.
  - E_k ≤ M_k: Even switches go along gates (R15 (d)).
  - OE: no crossing ⇒ O_k ≤ E_k.
- So a crossing-free run lies in one tame run, and FB's per-tame-run count (levels ≥ 0: ≤ n_E each; level −1: ≤ n_E(n − 1)) gives
  ≤ n_E(2n − 1). Correct.
- DATA (FBI): 339 library and 1 random non-tame in-phase transitions, every one a crossing. Max fallbacks in a crossing-free run: 1. 0
  failures.

## 5. NH1-FB (SIGNED)
- Case A: inside a maximal ¬H1 run there is no crossing (R-CONST), so FB-INT applies to its transitions. Several runs in one crossing-free
  stretch are only over-counted.
- Number of runs: ≤ ⌈T/2⌉ + 1.
- Case B: a toggle, ≤ T. Correct.
- DATA (NH1): 9 library and 447 random fallbacks at ¬H1 states, max 1 per phase. 0 failures.

## 6. CN-LAST (SIGNED; every game)
- Setup: S4c switches exactly the gate tails, which are own cycle nodes c_i, each to its best target z_i.
  - Level −1 gives Ξ(z_i) = (c_i, ∅, d_i) with a better length (F).
  - z_i's honest play reaches c_i without meeting another c_j: c_j's play is its own cycle, so passing c_j would give z_i the cycle node c_j.
- (i):
  - Every (σ′, σ̄_k)-play agrees with its (σ_k, σ̄_k)-play up to its first switched vertex c_i, then closes the cycle c_i → z_i ⇝ c_i topped
    by c_i. A value reads cycle node, P and length on the prefix to the first c_i, so V_{σ′,σ̄_k} = Ξ_k.
  - Lemma S (a) gives Ξ_{k+1} ⊴ Ξ_k, and R15 (a) the reverse.
  - Correct.
- (ii): unswitched vertices had no gate; c_i with a gate (c_i, w) at k+1 would have had a better target than z_i at k. Correct.
- (iii): with Iσ = ∅, either S5 stops, or S4b changes τ, or the Odd fallback does. k+1 is in the same phase as k (Ξ and τ unchanged).
  Correct.
- DATA (CNL):
  - 23 library, 991 random 𝒞^1O and 408 general cases. (i), (ii), (iii) hold at all of them: 0 failures.
  - In 1,420 of the 1,422 cases N5 stops at k+1; in the other 2 the next transition changes τ.
  - Level −1 Even fallbacks with a non-own-cycle-node gate: 1, oc12_s1 (§7.3's example; it is ¬H1, so §5 counts it).

## 7. Not to sign; re-runs
- scope_probe on wd16_s2, wd12_s1, pftheta_cex_n32 and oc12_s1: 0 failures; oc12_s1 shows the one non-cycle level −1 Even fallback.
- I did not re-run Oink on these four; the packet's §8 and the Lead record those re-runs. Named as skipped.

## 8. DATA summary (DATA, not proof)
| run | games | phases | key counts | failures |
| --- | --- | --- | --- | --- |
| library (276 files at referee head) | 276 | 1,127 | KEY 7,455; WCH 135; scope runs 225; non-tame 339; NH1 fb 9; CN-LAST 23 | 0 |
| rand 𝒞^1O n 4-14 seed 7801 | 30,000 | 58,050 | KEY 22,121; WCH 618; scope runs 2,890; NH1 fb 447; CN-LAST 991 | 0 |
| general games n 3-14 seed 7802 (KEY, CN-LAST only) | 20,000 | — | KEY 7,219; CN-LAST 408 | 0 |
| climbs scope_climb.py seeds 91, 92 (15 min each; final, added 11:18Z by date -u) | 453,684 + 312,901 candidates, every one through all checks | — | max (scope runs, NH1 fb, WCH) = (3, 0, 3) / (4, 0, 4) | 0 |
- Thin spots:
  - WCH, SCOPE-COUNT and NH1-FB are far from their bounds.
  - FB-INT's crossing-free runs carry at most 1 fallback in all data.
  - CN-LAST's hypothesis is common, but its non-cycle complement has 1 case.

## 9. Labels after this report (D18/L40)
- PROVED (L-NEW successor 15, checked by successor 16; signed by REFEREE (Opus 5.5, D15), second referee pending):
  - KEY and CN-LAST on every game;
  - WCH, FB-INT on 𝒞^1O inside a phase;
  - SCOPE-COUNT (premise R34) and NH1-FB (premises R33, R34).
- OPEN: out-of-SN fallbacks, the level −1 residue, (L1), G-N5-TIME. CONJECTURE: OUT-POLY, PF-THETA (poly). FALSE: PF-THETA linear, LEN-STAY.
- Not a TARGET.md claim; the TARGET.md diff is empty.

Signed: REFEREE successor 7 (Opus 5.5, D15).

## §C. Comparison with REFEREE-2 (written 2026-10-25 12:17Z by date -u; REFEREE successor 8 (Opus 5.5, D15), for this lane's report above)
- Compared against: the FINAL docs/referee-2/R2-N5-SCOPE.md at referee-2 6d6e4bcf ("R2-N5-SCOPE final: all six SIGN"), named by the Lead
  at 12:08Z (Lead's stamp). The draft 1f8a9109 was not used. I read R2 only after this lane's report (fb6089b / 560ff4c) was pushed.
- Verdicts. Both referees SIGN all six statements: KEY, WCH, SCOPE-COUNT, FB-INT, NH1-FB and CN-LAST. Neither signs §7. No verdict
  differs.
- Joint gap map. Neither report lists a gap. R2's notes, checked against the sources:

| R2 item | what it says | checked | this lane | joint status |
| --- | --- | --- | --- | --- |
| N-SC-1 | the dependency table's status for R-CONST, "IN LANDING (R33 (e) draft, CHECKER C42)", is stale | `git log -1 00bd18b8`: R33 landed 10:37:35Z; the packet commit 8483279d is 10:45:04Z. Correct | MISSED (status wording; no effect on any proof) | note; fixes line below |
| N-SC-2 | WCH: "t0 ∈ F_k = F_{k+1}" sits in the non-crossing disjunct; the proof gives Ξ_k(t0) ≠ Ξ_{k+1}(t0) at every such transition | packet §2: H2 at both ends gives t0 ∈ F at each end separately, and w = o ⊕ Ξ(t0) at each. Correct | this lane's §2 used the unconditional form ("a w-change forces a change of Ξ(t0) with t0 ∈ F") but did not flag the statement's wording | note (wording) |
| N-SC-3 | FB-INT: the pointwise fact "every non-tame transition is a crossing" is in the proof of R28 (c) (ii), not its statement | packet §4 already says "This is the proof of R28 (c) (ii)", and its dependency table says "OX (ii)'s proof". So the packet text meets the note | same reading (§4 above) | note; no change needed |
| N-SC-4 | NH1-FB: T is the toggle count here, but P-N5-TOG §4 uses T for the bound |U|(n + 1) + n − 1 | P-N5-TOG §4 l.88: "H1-toggles per phase ≤ T := |U|(n + 1) + n − 1". Correct; both readings give a valid inequality | MISSED (notation) | note; fixes line below |
| O-1 (§7.2, not to sign) | "f_out ≤ n_E(2n − 1)(X_out + 1)" needs "+ X_out": evicting fallbacks are crossings and lie in no FB-INT stretch | FB-INT counts fallbacks inside crossing-free runs only. DATA (own SPEC engine rl_engine.py, not R2's N5): wd16_s2 has 13 in-phase fallbacks, all 13 crossings (R̄ changes), all at H1 ∧ ¬H2. Correct | not examined (§7 not to sign) | accepted; for L-NEW §7.2 |

- Attribution: R2's counts come from its own N5 (any arena optimum), mine from SPEC traces. The two DATA sets are different runs and not
  re-runs of each other. That is not a disagreement.
- Fixes-file lines (L-NEW, P-N5-SCOPE; none blocks a signature):
  - N-SC-1: dependency table, R-CONST row → "LANDED (RESULTS R33 (e))".
  - N-SC-2: WCH statement → "Ξ_k(t0) ≠ Ξ_{k+1}(t0) at every such transition; off crossings t0 ∈ F_k = F_{k+1}".
  - N-SC-4: NH1-FB → name the toggle count and P-N5-TOG's bound differently.
  - O-1: §7.2 → "f_out ≤ n_E(2n − 1)(X_out + 1) + X_out".
- Joint label after §C: KEY, WCH, SCOPE-COUNT, FB-INT, NH1-FB and CN-LAST are PROVED (L-NEW successor 15) and signed by both referees
  (Opus 5.5, D15), pending CHECKER. No open gap.
