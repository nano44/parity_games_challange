# R-N5-NJB: REFEREE report on packet P-N5-NJB (box 9 part 2: RDROP, PL (c′), PL-S′, MINSET, NO-RF-OLD, ENT-SHAPE)
Referee: REFEREE (successor 7, session_01TWT1diK1Z9x2eK56iBVbZu), Opus 5.5 (owner ruling D15, Lead reading L37). Packet P-N5-NJB: task 3
of the Lead's brief of 2026-10-25 08:07Z (Lead's stamp). Object docs/si/P-N5-NJB-box9.md at pinned trunk a7d85b3, sha1
f43a8823b3b50399dacb387697bdb433373ea671 (checked: `git show a7d85b3:docs/si/P-N5-NJB-box9.md | sha1sum`, 160 lines; the same on trunk
87265268). Author L-SI successor 4. Written 2026-10-25 08:56Z onward by date -u.
Every verdict is labelled (Opus 5.5, D15). Labels (D18/L40): PROVED (by whom) / CONJECTURE / OPEN. Independent of REFEREE-2:
docs/referee-2/ not read for this packet.
Background read: P-N5-FBW (sha1 88337bd6…) with its fixes (91ff4216…) and my lane's R-N5-FBW (9a94dc7b + §C a04615b5); RESULTS R25
(OFF, FB step (2), CAP-1), R28 U-loc, R29 (Fact R, TRANSFER, OFFGATE, NL, CLS1 and its (A)-chain), R30 (OR, TC-SPLIT, ABS-L), R19 (a),
R20 (b) FBL, R21 (a) XW.

## Verdicts
| statement | lane label | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 Lemma RDROP | PROVED (L-SI succ. 4) | SIGNED (DATA vacuous: no dirty interval anywhere) |
| §1 Theorem PL (c′) | PROVED | SIGNED |
| §1 Corollary PL-S′ | PROVED | SIGNED |
| §2 Lemma MINSET (a)-(d) + Consequence | PROVED | [§C: (c) as written is NOT signed (G-NJB-1, missed here, accepted); survivor form signed] SIGNED WITH GAP NJB-1 (wording: in (b), (c) and the Consequence, "absorption" / "absorbed" must mean "enters R". R30's absorption, defined in the packet's §0, is the entry of x0 = σ̄(o) only. Several members can enter R at one step, and a member other than σ̄(o) can enter, so the R30 reading makes (c)'s "every member … has been absorbed" false. DATA: 4 named-set steps of each kind). Closed |
| §3 Lemma NO-RF-OLD | PROVED | SIGNED |
| §3 Corollary | PROVED | SIGNED (DATA vacuous) |
| §4 Lemma ENT-SHAPE (1)-(4) | PROVED | SIGNED |
| §4 Lemma ENT-SHAPE (5) | PROVED | NOT SIGNED as stated (gap NJB-2). The proof does not exclude that z's level-L rise happens at the fallback transition k0 → k0+1 itself, with z ∈ R_{k0} leaving R there. Then no S4a step in (k0, k) carries it. The local configuration occurs in the data (§4.2). The repaired form (5′) is SIGNED |
| §5 NJB, ENT, obstruction | not to sign | not signed |

Fixes-file lines (one per gap):
- NJB-1 (§2 MINSET, wording): in (b), (c) and the Consequence, replace "absorption into R" / "absorbed" by "entry into R" / "entered R" (several members may enter at one step; only one of them can be σ̄(o)).
- NJB-2 (§4 ENT-SHAPE (5)): replace (5) by "(5′) z's honest value rises at level exactly L at some transition s ∈ [k0, k). Either s = k0 and z ∈ R_{k0} ∩ F_{k0+1} (z leaves R at the fallback), or s is an S4a step in (k0, k) with z ∈ F_s ∩ F_{s+1}. In the second case U-loc and (A_s) leave only Even switches of level ≤ L on z's F-play, so the rise needs a switch of level exactly L on that play." Item (iii) of §5's obstruction list must then also allow the fallback case.

## 0. Setting and citations
- Setting: P-N5-FBW §0. R̄ contains o; scope runs as in R29 §0.
- Scope runs are read in R29's setting: a joint λ-phase (λ_Ξ, λ_U) with τ constant. This is the key my probe uses (as in fbw_probe.py).
  - P-N5-FBW §0 writes "PHASE: λ_Ξ and τ constant" and then defines scope runs by R29 §0.
  - All the R29 lemmas used (Fact R, OFFGATE, NL, CLS1) are signed for scope runs in R29's setting, and NL also transfers to (λ_Ξ, τ)
    (R-N5-FRZ §1). So no citation is used outside its signed setting.
- The other citations are signed: PL (a)/(b), FLAT-ALL (FBW-1), STRETCH (FBW-2) and FBW-S from P-N5-FBW (both referees, pending CHECKER);
  R25 CAP-1 (λ(o) ≠ o), OFF and FB step (2); R28 U-loc; R30 OR and TC-SPLIT; R19 (a); R20 (b) FBL in its u* ≠ none strong gate form
  (as in R29 row 1); R21 XW; R15 (a).
- Tools: docs/referee/scratch/njb_probe.py (own code, `python3 -I`; own trace = n5.run; 𝒞^1O asserted on every game; every check named
  below) and l2_oink.py (Oink `--zlk -v` at 8fbf0a7). No lane script is imported; lane instances are inputs only.
- Data sets:
  - NAMED = experiments/si/coarse/named.txt + instances/*.pg + instances/box9/*.pg: 72 files, the packet's 53 + 12 + 7.
  - LIB = every experiments/**/*.pg in 𝒞^1O with n ≤ 64 at referee head: 261 files.
  - RANDOM = 6,000 𝒞^1O games, n 6-20.

## 1. RDROP, PL (c′), PL-S′ (SIGNED)
- RDROP:
  - PL (b) makes j an S4a step with lev(θ_j, θ_{j+1}) = O_j > M ≥ 0.
  - The transition j lies inside S (between two block fallbacks), so w_{j+1} = w_j.
  - θ_j ◁ θ_{j+1}: R15 (a), and the level is > ⊥. Also θ_{j+1} ⊴ w_{j+1} = w_j (XW). (C5) gives O_j ≤ r_j.
  - Correct.
- PL (c′):
  - P is an initial segment of [f_1, f_N], because r is non-increasing along S (Fact R). Every dirty interval's first change j has
    r_j > M (RDROP), so j ∈ P.
  - Distinct dirty intervals have distinct first changes, and each is an absorption (PL (b)).
  - On the part of an interval inside P, the (A)-chain runs: OFFGATE gives (A_{f_i+1}) for L = M_{f_i} = M, and NL (iii) propagates it
    at S4a steps with r > M. f_i ∈ P whenever any state of the interval is, since P is initial. NL (ii) then forbids leaves at every
    S4a step starting in P.
  - N_x: every state of [f_1, f_N] has (h), since each is the start of a transition of S, f_N included. So σ̄(o) ∈ F and
    0 ≤ N_x ≤ d_o − 1 at every state, including the end state of the last transition counted.
    - An absorption raises N_x by at least 1, since no exit leaves at that step.
    - Decreases happen only at block fallbacks f_i (i < N), whose releases are counted by REL_M. No other fallback of S lies in
      [f_1, f_N] (CLS2).
    - So #absorptions in P ≤ (d_o − 1) + REL_M.
  - Distinctness of the absorbed exits (ABS-L, used by the old PL (c)) is not needed. Correct.
- PL-S′: the blocks of S are disjoint, there are ≤ n levels ≥ 0, and the REL_M are disjoint parts of REL(S). Correct.
- DATA (njb_probe RDROP, PLC): §5.

## 2. MINSET (SIGNED WITH GAP NJB-1)
- (a):
  - Under H1 (scope), λ(o) ≠ o, so the packet's λ(o) = o branch is vacuous: o would lie on its own honest cycle.
  - σ̄_t(o) ∈ F_t is a full Ξ-minimiser over succ(o) (CAP-1), and θ_t = o ⊕ Ξ_t(σ̄_t o) (P2).
  - For a free exit x, o lies on no play from x, so o ⊕ preserves ⊴ ((C7)). Hence θ_t is the minimum over free exits, and (C1) passes
    it to COARSE_M.
  - Correct.
- (b):
  - NL (ii) gives F_{t+1} ⊆ F_t, and NL (i) freezes COARSE_M on F_{t+1}.
  - A member x that stays free keeps its value. Then COARSE_M(θ_{t+1}) ⊴ that value (a, at t+1) = COARSE_M(θ_t) ⊴ COARSE_M(θ_{t+1})
    (R15 (a), (C1)). So x ∈ Mn_{t+1}.
  - Hence members leave only by entering R. Correct.
- (c) and (d): correct as written (for (d): FLAT-ALL (i)-(iii) at f_i, with (h) at f_i + 1 for i < N).
- NJB-1 (wording):
  - The packet's §0 defines ABSORPTION as R30's: "σ̄(o) changes from x0 with x0 ∈ F_k ∩ R_{k+1}". (b), (c) and the Consequence use
    "absorption into R" / "absorbed" for ANY member entering R.
  - In (c), "every member of Mn_t has been absorbed at t" is true only in the entry sense. If |Mn_t| ≥ 2 and all members enter R at
    t, only x0 = σ̄_t(o) is absorbed in R30's sense.
  - DATA (named set): 4 steps where two or more members enter R at once, and 4 where a member other than σ̄_t(o) enters.
  - The proof uses only entry into R, so this is wording. Closed by the fixes-file line.
- DATA (MS): §5.

## 3. NO-RF-OLD and Corollary (SIGNED)
- (A_s) on [k0 + 1, t*]: OFFGATE at k0 + 1, then NL (iii) at the S4a steps, all with r > L.
- z ∈ F_t and no leave give z ∈ F_s for every s ∈ [k0 + 1, t] (F_{s+1} ⊆ F_s), with COARSE_L(Ξ_s z) = ζ (NL (i)).
- COARSE_L(b_j y) = ζ:
  - ◁ ζ would make (y, z) a gate into F_j of level > L, against (A_j).
  - b_j ⊴ b_t gives ⊴ ζ.
- Route decomposition at s ∈ {j, t}:
  - b_s(y) = Ξ_s(σ_s y) = ρ_s ⊕ θ_s with ρ_s the route of σ_s(y) (R19 (a) under (h); y ∈ R_s).
  - P(Ξ_s z) ⊆ F_s, and ρ_s ⊆ R_s is disjoint from it.
  - So ρ_s has no vertex above max(L, rank c), and P(θ_s) ∩ V_{>L} = P(Ξ_s z) ∩ V_{>L}, the same set at j and at t.
  - So COARSE_L(θ_j) = COARSE_L(θ_t), and the sandwich θ_j ⊴ θ_{j+1} ⊴ θ_t contradicts the choice of j.
- Edge cases:
  - L = −1: COARSE_{−1} = (c, P), and the formula holds.
  - L = ⊥: (A_t) at ⊥ forbids every gate into F, so the lemma is immediate.
  - Correct.
- Corollary:
  - M_k ≥ 0 makes k THR with u* ≠ none (FBW-S).
  - FBL's strong form: every non-flat switched edge is R → F.
  - NO-RF-OLD at t = t* = k puts its tail outside R_j.
  - A level-L tail (FB step (2)) switches along a non-flat edge (level L ≥ 0), so it is an entrant.
  - Correct.
- DATA (NORF): §5. The Corollary's hypothesis (a COARSE_L θ-change followed by a fallback of level ≥ 0 with r > L throughout) never
  occurs: vacuous, as the packet's §6 says.

## 4. ENT-SHAPE ((1)-(4) SIGNED; (5) NOT SIGNED as stated, gap NJB-2)
### 4.1 Items (1)-(4)
- (1):
  - y ∈ R_k ∖ R_j: NO-RF-OLD applies to every gate, not only switched ones.
  - On [k0 + 1, k]: the (A_s) argument of §3.
  - At k0, two cases:
    - y unswitched: FLAT-ALL (iii) at k0.
    - y switched: its max gate level is < L, because y is not a level-L tail at k0 by (3). (3)'s proof uses (2) only at k0 + 1, and
      (2) there uses (1) only on [k0 + 1, k], so there is no circularity. By FB step (2) y switches to a target of that level, and
      that target's COARSE_L is unchanged (FLAT-ALL (iii)).
  - Correct.
- (2): a level-L gate at k makes b_k(y) bad (rank L > rank c, since the difference sits at v_L ∈ P Δ P′ ⊆ V_{>c}). b is non-decreasing
  with constant COARSE_L, so it was bad throughout. Correct.
- (3): STRETCH step (3) would make b_{k0+1}(y) good, against (2). Correct.
- (4): COARSE_L(Ξ z) is constant (OFF at k0, which needs only z ∉ R̄_{k0+1}; NL (i) after). If z were good at k0, (y, z) would be a level-L
  gate at k0, so y would be a level-L tail there, against (3). Correct.
### 4.2 Item (5): gap NJB-2
- (5) says the bad → good change of z's rank-L bit happens "at some S4a step in (k0, k) while z stays in F". Between k0 and k it must
  happen at SOME transition s ∈ [k0, k), but s = k0 (the fallback transition) is not excluded.
  - If z ∈ F_{k0}: Ξ(z) is unchanged at the fallback. By FBL, z's F-play meets only flat cycle-node switches, which change no value. So
    s ≠ k0.
  - The proof never shows z ∈ F_{k0}. "z ∈ F_s (no leave)" is established only for s ≥ k0 + 1.
  - If z ∈ R_{k0}, z leaves R at the fallback: a tail on its route switches R → F at a level ≤ L. z's value can then rise at level
    exactly L at k0 → k0+1 while its COARSE_L stays fixed (OFF). (4) still holds (z is bad at k0), and (y, z) becomes a level-L gate
    into F at k0 + 1, which (A_{k0+1}) allows.
- DATA (njb_probe ENTP_strict): the local configuration is common.
  - Pattern: an in-scope fallback k0 of level L ≥ 0 with (h) at k0 + 1, and an Even edge (y, z) with
    - z ∈ R_{k0} ∖ R̄_{k0+1};
    - lev(Ξ_{k0} z, Ξ_{k0+1} z) = L, a rise;
    - y unswitched with COARSE_L(b y) unchanged;
    - (y, z) a level-L gate at k0 + 1 but not at k0.
  - Count: 569 such edges in the named set and 1,159 in the library (§5). Checked by hand: cycelim_cex_n32.pg (experiments/si/orlens/
    instances), fallback 15 of level 31, (h) at 15 and 16.
    - z = 7 ∈ R_15 ∖ R̄_16, and Ξ(7) goes from (17, P, 4) to (17, P′, 3) with lev 31, a rise: the rank-31 vertex leaves P.
    - y = 15 keeps σ(15) = 3, and COARSE_31(b y) stays (17).
    - (15, 7) has level 29 and is not a gate at 15; it is a level-31 gate into F at 16.
  - The full ENT setting (a COARSE_L θ-change after k0, with r > L up to a level-L fallback k) never occurs. So this is a proof gap, not a
    counterexample.
- With (5′) (fixes line NJB-2), the lemma is correct: the S4a branch is the packet's argument; the fallback branch is the omitted case.
  This matters for §5's obstruction: a violation of NJB may also get its z from a fallback eviction at k0, not only from an F → F
  level-L switch.

## 5. DATA (DATA, not proof)
- njb_probe.py, 0 failures in every check on every set:

| set | scope runs | blocks (M ≥ 0) / with an r-drop | max block | max D_M | MINSET intervals / states / Σ\|Mn\| / \|Mn\| = 1 | member entries (multi / not σ̄) | Mn emptied | MSd checks | NORF j / gate checks | ENTP_strict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NAMED (72) | 77 | 83 / 41 | 37 | 0 | 243 / 405 / 1,464 / 208 | 40 (4 / 4) | 0 | 290 | 6 / 130 | 569 |
| LIB (261) | 211 | 177 / 85 | 37 | 0 | 409 / 855 / 2,507 / 441 | 40 (4 / 4) | 0 | 470 | 9 / 168 | 1,159 |
| RANDOM (6,000, n 6-20) | 966 | 0 | — | — | — | — | — | — | — | — |

- Blocks with an r-drop (r ≤ M somewhere in [f_1, f_N]): 41 named, 85 library. These are where PL (c′) goes beyond PL (c), and the
  bound holds there with D_M = 0.
- Random 𝒞^1O games produce no level ≥ 0 block, so the evidence is the named set and the library.
- Packet instances re-run (l2_oink.py; N5 = own trace = n5.run; Oink zlk verified, regions agree):
  - cl9_mn_a (sha1 f60b411a…, 39 iterations / 15 fallbacks);
  - cl9_mn_b (dcec4e14…, 41 / 35);
  - cl9_norf_a (33580f22…, 35 / 2);
  - cl9_norf_b (a90ad304…, 32 / 2).
  - Iteration and fallback counts equal the packet's.
- Thin spots (named):
  - D_M = 0 in every block of every set, so RDROP and PL (c′)'s dirty-interval content is vacuous.
  - The NO-RF-OLD Corollary and ENT-SHAPE's full setting never occur.
  - MINSET (c)'s "emptied" branch never fires (Mn is never emptied inside an interval). The lemmas rest on the proofs.

## §C. Comparison with REFEREE-2 (docs/referee-2/R2-N5-NJB.md, referee-2 45eae593, read from origin/claude/referee-2). REFEREE successor 7, written 2026-10-25 09:46Z by date -u (stamp corrected from an estimated 09:49Z)
Signature (Opus 5.5, D15). I opened R2-N5-NJB only after my report (524d93f5) was pushed. Also read: L-SI's fixes file
docs/si/P-N5-NJB-fixes-box9.md (l-si 32c2393), sha1 6a3377482739a9dd5fdfcddc82314c9304ff94ec (checked). It carries my NJB-1 and NJB-2
lines verbatim, and lane item NJB-L1 (data only).

### C.1 Verdicts
| statement | REFEREE | REFEREE-2 | joint |
| --- | --- | --- | --- |
| RDROP, PL (c′), PL-S′, NO-RF-OLD + Corollary | SIGNED | SIGN | signed by both |
| MINSET (a), (b), (d) | SIGNED (with NJB-1, wording) | SIGN ((b) in the survivor reading) | signed by both; rows 1-2 |
| MINSET (c) | SIGNED (with NJB-1). I wrote "(c) correct as written": WRONG, see C.2 | SIGN WITH GAPS G-NJB-1 (statement) | CHANGED HERE: I adopt G-NJB-1. Literal (c) is NOT signed (it is equivalent to NJB on the interval); the survivor form is signed by both. Joint label SIGNED WITH GAPS NJB-1, G-NJB-1 |
| ENT-SHAPE (1)-(4) | SIGNED | SIGN | signed by both |
| ENT-SHAPE (5) as stated | NOT SIGNED (NJB-2) | SIGN (N-NJB-1 closes the fallback case) | VERDICT DIFFERS (C.3). I keep NOT SIGNED for the literal (5). (5′) (fixes 6a337748 NJB-2) is signed by me; REFEREE-2 to rule on (5′) |
| §5 | not signed | not signed | — |

### C.2 G-NJB-1: missed by me, accepted
- Mn_{t+1} is defined against θ_{t+1}. By (a) at t+1 (t+1 in the interval, r > M), σ̄_{t+1}(o) ∈ Mn_{t+1}, so Mn_{t+1} ≠ ∅ always.
- Literal (c), "COARSE_M(θ) changes at t → t+1 exactly when Mn_{t+1} = ∅", therefore says COARSE_M(θ) never changes inside the interval.
  On the r > M part that is NJB itself (PL (b)), the open CONJECTURE of §5. The proof does not prove it.
- What the proof proves is REFEREE-2's survivor form: COARSE_M(θ) changes iff Mn_t ∩ F_{t+1} = ∅.
  - My §2 (b) argument is exactly this survivor argument ("a member that stays free keeps its value … so x ∈ Mn_{t+1}").
  - I then wrongly called (c) "correct as written".
- My probe's MSc check tested the LITERAL form and could not fail while NJB holds in the data: Mn_{t+1} was never empty and COARSE_M(θ)
  never changed (MS_emptied 0).
- Lesson: a statement whose defining set is nonempty by a sibling clause must be read against that clause before signing; a data check
  of an "iff" that is vacuous on one side tests nothing.
- L-SI's fixes file still has the literal (c), with my NJB-1 wording ("entered R"). So the fixes2 file must carry G-NJB-1's line (row 2).

### C.3 ENT-SHAPE (5): NJB-2 against N-NJB-1, reconciled
- N-NJB-1 (REFEREE-2 §4) argues that the fallback k0 → k0+1 does not move Ξ(z): "z ∈ F_{k0} ∩ F_{k0+1}, so z's honest play stays in F and
  meets no R tail".
  - That argument is correct for z ∈ F_{k0}. My §4.2 gives the same one for that case.
- But nothing in the packet, in R2-N5-NJB or in my reading gives z ∈ F_{k0}.
  - The facts available are z ∈ F_s for s ∈ [k0 + 1, k] (NL (ii), no leave at the S4a steps) and COARSE_L(Ξ z) constant on [k0, k]
    (OFF at k0 needs only z ∉ R̄_{k0+1}).
  - At k0 itself z may lie in R_{k0} and be evicted by the fallback (an R → F switch on z's route).
- In that case the level-L rise can sit at k0 → k0+1:
  - the hand-checked instance cycelim_cex_n32.pg fallback 15 (§4.2);
  - 569 named / 1,159 library local configurations (§5).
  - (4) still holds, and (A_{k0+1}) admits the resulting level-L gate into F.
- So N-NJB-1 closes the branch z ∈ F_{k0} and leaves the branch z ∈ R_{k0} open. The packet's (5) asserts the rise is at an S4a step in
  (k0, k) in both branches, and no proof covers the second.
- Decision (REFEREE, Opus 5.5, D15):
  - ENT-SHAPE (5) AS STATED stays NOT SIGNED.
  - (5′) (both branches) is SIGNED, as is (5) under the added hypothesis z ∈ F_{k0} (that is N-NJB-1).
  - I ask REFEREE-2 (via the Lead) to rule on whether N-NJB-1 assumed z ∈ F_{k0}. If it did, both referees would sign (5′) and neither
    the literal (5).
- Impact: none on any count. ENT-SHAPE is descriptive (the shape of a potential NJB violation), and its full setting is vacuous in all
  data of both referees. The (iii-b) branch is now in the obstruction list (fixes 6a337748, NJB-2).

### C.4 Items found by one referee only, and data
- NJB-1 (REFEREE only; "absorbed" vs "entered R"). REFEREE-2 did not raise it. Its survivor repair of (b) says "members of Mn_t leave F
  only by absorption", which repeats the loose usage. The lane's fixes file adopted "entry into R", and row 1 keeps it.
- NJB-L1 (lane): the packet's §6 summed two climb files under one name. Data only; no statement depends on it.
- Data agree. In all sets of both referees: D_M = 0, Mn never emptied, no fallback after a COARSE_L θ-rise, and the full ENT setting
  never occurs. REFEREE-2's counts come from its N5 with arbitrary S4a optima; mine from the SPEC trace.

### C.5 Joint gap map (one fixes-file line per row)
| row | REFEREE | REFEREE-2 | kind / status | fixes-file line |
| --- | --- | --- | --- | --- |
| 1 | NJB-1 | — | wording, closed | §2 (b), (c), Consequence: "entry into R" / "entered R" for "absorption" / "absorbed" (fixes 6a337748 NJB-1) |
| 2 | missed, accepted | G-NJB-1 | statement, closed by repair | §2 (c): "COARSE_M(θ) changes at t → t+1 exactly when Mn_t ∩ F_{t+1} = ∅; then every member of Mn_t has entered R at t"; §2 (b): "Mn_t ∩ F_{t+1} ⊆ Mn_{t+1}, with the same COARSE_M values" (REFEREE-2's line, with row 1's wording; for the fixes2 file) |
| 3 | NJB-2 | N-NJB-1 (branch z ∈ F_{k0} only) | statement; literal (5) NOT SIGNED by REFEREE; (5′) signed by REFEREE | §4 (5′) as in fixes 6a337748 NJB-2. N-NJB-1's sentence is the proof of its branch s ≠ k0 when z ∈ F_{k0} |

### C.6 Joint label (D18/L40)
- PROVED (L-SI successor 4, repaired by successor 5; REFEREE and REFEREE-2, Opus 5.5, D15), pending CHECKER:
  - RDROP, PL (c′), PL-S′;
  - MINSET (a), (b), (d) and survivor-(c) (rows 1-2);
  - NO-RF-OLD + Corollary, ENT-SHAPE (1)-(4).
- ENT-SHAPE (5′): signed by REFEREE. REFEREE-2 to confirm (C.3). The literal (5) is not signed by REFEREE.
- CONJECTURE: NJB, ENT. OPEN: level −1 fallbacks per scope run, REL(S), G-N5-TIME.
- Thin: D_M = 0 everywhere. RDROP, PL (c′)'s dirty content, the NO-RF-OLD Corollary and ENT-SHAPE's full setting are never exercised.
- Not a TARGET.md claim; the TARGET.md diff is empty.

Signed: REFEREE successor 7 (Opus 5.5, D15).

### C.7 Converged state (written 2026-10-25 10:33Z by date -u, after REFEREE-2 §C.2 / §C.3a, referee-2 21429c9 + 16d27d1)
- REFEREE-2 withdraws N-NJB-1 as a proof of (5): it assumed z ∈ F_{k0}.
- Both referees: ENT-SHAPE (5) as stated NOT SIGNED, (5′) SIGNED; literal MINSET (c) NOT SIGNED, survivor-(c) SIGNED.
- No verdict differs on P-N5-NJB. Joint label as in C.6, with (5′) now signed by both.
