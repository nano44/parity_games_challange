# R2-P-IDEAL-FLIP: second-referee report on packet P-IDEAL-FLIP (L-NEW successor 53, box 162)
REFEREE-2 successor 27 (Opus 5.5, D12/D19). Written 2026-11-05 11:16Z (date -u). Independent: docs/referee/ not read for this packet
before this push. Stale-clone check at start (11:11Z): ls-remote claude/referee-2 = local HEAD = c11e2490; trunk fast-forward, 0 / 0.

## Object
- claude/l-new 9effea1f. docs/new/P-IDEAL-FLIP.md sha1 92803bd5b750924f0d0bc7db3c57eddf5725dfcb, 236 lines; docs/new/P-IDEAL-FLIP-line-L1.txt
  sha1 36418d164ac759472fadf0b411d81901db32e6da, 1 line, 0 «|». Instances: box160/out/iso_d4_st9.json 7ca1e68c52e4…, box162/out/kf0_d2_t2.json
  c2233e05b621…, box162/out/kf1_d2_t3.json d368d441b13b…. All re-hashed at 9effea1f: match.

## Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §2 | Lemma W-ONLY (a) (𝓦_d, no ISO), (b), (c) (ISO) | **SIGN** (Opus 5.5, D12) |
| §2 | Corollary W-ONLY (d): T ≤ T_2(d − 1) + 2 (𝓛^R_d, ISO) | **SIGN** (Opus 5.5, D12) |
| §3 | Lemma NOW-ONCE (a), (b), (c) | **SIGN** (Opus 5.5, D12) |
| §4 | Lemma SWAP, Corollary SWAP-RUN | **SIGN** (Opus 5.5, D12) (N-1: the «no q» caveat is unnecessary) |
| §5 | Proposition FLIP-1: T_0(1) = 2, T_k(1) = 3 (k ≥ 1) | **SIGN** (Opus 5.5, D12) |
| §6 | DEAD SC-ISO by iso_d4_st9 | **SIGN WITH GAP G-FLIP-1** (Opus 5.5, D12): ruling below |
| line | L-1 | **MATCHES** (optional P-1 to P-3) |
Finding F-1 (SWAP-RUN «Does NOT claim» remark, not in the line).

## Premise route (landed RESULTS only)
- R104: §0 is the P-IDEAL-SLOT §0 restatement (checked in my earlier reports), plus (F1) and (F2), both immediate from the definition
  (keys of one level have equal length and distinct last gates; a degree-2 mover that moves has both options available and takes the
  key-least under the new state). ✓
- R109 SEG-ONCE: the quoted clause is verbatim in the landed R109 entry (docs/RESULTS.md l. 11030; Python substring test True). Used only
  at l = −1 over the whole run (§2 (d), §3 (c)). ✓ R109's 𝓛_d / T*(d) are only named, never used for a bound. ✓
- No R105 item (so Erratum E-2 is irrelevant), no R106-R108, no docs/lit. Confirmed by reading every proof step.
- One machine premise, used only in §6 and labelled as its gap. ✓

## Definitions (packet §1) checked
𝓦_d, U, 𝓛^R_d (lev(x) = ⌊x/2⌋, degree 2, wt(x, k) = 2(lev(x) − 1) + k), T^R(d), ISO, b_0, κ^c, the c-step Step^c_G (A-sets under the old
state, key^c under the new state, 0 and 1 kept), forced run (ISO genomes of 𝓛^R_(m+1)), moves, flips (over t ∈ [2, L]), T_k(m)
(supremum; non-decreasing in k), seg1 / tail. My tool implements each from this text. 𝓛^R_d ⊆ 𝓛_d ⇒ T^R ≤ T*. ✓

## Proof check
### W-ONLY
- (a): s″ = s_t, s′ = Step^c(s_(t−1)), c = b_0(s″); both pick from A_(s_(t−1))(x). Level 1: w = w′ ⇒ own gates decide in both; w ≠ w′ ⇒
  real order g(0, s″(0)) < g(1, s″(1)) ⇔ b_0(s″) = 1 ⇔ c = 1 ⇔ κ^c_0 < κ^c_1. ✓ Level ≥ 2 by induction with the same parent options
  (levels below agree). ✓ Movers 0, 1 are excluded from the comparison (Step^c keeps them). ✓ No ISO used. ✓
- (b): under ISO every chain from x ∈ U stays in U. ✓ key^c reads no option of 0, 1. ✓
- (c): H_q IDEAL-ACYC, H_q ∈ 𝓦_d, every state of H_q has b_0 = b_0(q); (a) on H_q + equality of H_q's A-sets / keys on U with G's at
  states with q at 0, 1; stop rule. ✓ (Remark: (c) holds without ISO too, since states of H_q carry q at 0, 1; not needed.)
- (d): u_t|U = s_t|U by (b) + (a) (induction); c changes only at steps moving 0 or 1; ≤ 2 such steps (SEG-ONCE l = −1; degree 2) ⇒
  flips ≤ 2 ⇒ moves ≤ T_2(d − 1) (definition of the supremum; d − 1 = m ≥ 1); the other steps move only level-0 movers, ≤ 2. ✓
### NOW-ONCE
- KP at level 1 on 𝓛^R: option k's key (g(k, s(k)), g(x, k)), first entries distinct ⇒ KP_s(x) = 0 ⇔ b_0(s) = 1; KP^c(x) = 0 ⇔ c = 1. ✓
- (a): consecutive moves t1 < t2 return x to the option it left; (F2) gives s_(t1)(x) = KP_(s_(t1))(x), s_(t2)(x) = KP_(s_(t2))(x); equal
  b_0 ⇒ equal KP: contradiction. ✓ (b): the same with KP^(c_t). ✓ (ISO is not used in (b)'s proof.) (c) ✓.
### SWAP, SWAP-RUN
- κ^c_(1−k) = κ^(1−c)_k checked for k = 0, 1; equal A-sets (same Ξ-data); levels ≥ 2 same W-targets, induction. ✓ G^swap ∈ 𝓦_d and
  in R109's 𝓛_d, not in 𝓛^R_d. ✓
- SWAP-RUN: blocks of constant c (≤ k + 1); c* blocks = Step^(c*)_G, others = Step^(c*)_(G^swap) (SWAP); W-ONLY (c) on G and G^swap
  (both 𝓦_d, ISO) with b_0(q) = c*; after a piece's run stops, later frames of the block change nothing (Step is deterministic). ✓
- N-1 (precision, not a gap): the closing caveat «If no q with b_0(q) = c* exists … only the reading «run of an IDEAL genome» needs such
  a q» is unnecessary. Take ANY q and v := b_0(q): blocks with c = v are runs of H_q, blocks with c = 1 − v are Step^(1−v)_G =
  Step^v_(G^swap) runs, i.e. runs of (G^swap)_q. So the concatenation statement (and the line's unconditional wording) holds always.
- F-1 (packet §4 «Does NOT claim», not in the line): «The two genomes are in 𝓛_d, so T* (not T^R) caps each piece.» The two genomes of
  the corollary are H_q and (G^swap)_q; their level-0 movers have degree 1, so they are NOT in R109's 𝓛_d (which needs two degree-2
  movers on every level). G and G^swap are in 𝓛_d. A cap on each piece does follow, but by R109 SHIFT (H_q↓ ∈ 𝓛_(d−1)): each piece ≤
  T*(d − 1). Suggest a fixes entry: «H_q and (G^swap)_q have degree-1 level-0 movers; by R109 SHIFT, H_q↓, (G^swap)_q↓ ∈ 𝓛_(d−1), so T*(d − 1)
  caps each piece». Nothing signed changes.
### FLIP-1
- Upper: under ISO with N = 4, Ξ-targets of 2, 3 are in {X, 2, 3}, no self-loop, not both directions (acyclic) ⇒ some v with both options
  to X ⇒ v's values fixed, v changes ≤ once (to the better option, then singleton). u's two values depend only on v's option and always
  differ (β(u, k) on one chain only) ⇒ exactly one better option; consecutive changes of u need a change of v in between ⇒ u ≤ 2 changes.
  moves ≤ 3 for any c. k = 0: NOW-ONCE (b) ⇒ ≤ 2. ✓
- Lower: I-0 and I-1 checked frame by frame against the packet text and replayed by my own forced-run code: I-0 c ≡ 0, U-states
  (0,0) → (0,1) → (1,1), moves 2, flips 0; I-1 c = (0, 1, 1), U-states (1,0) → (1,1) → (0,1) → (0,0), moves 3, flips 1. My exact search
  of the forced-run maximum from the I-1 start: k = 0: 1, k ≥ 1: 3; from the I-0 start: 2 for every k. ✓
### DEAD SC-ISO
- Statement source: «The single-channel trade «seg1 + tail ≤ T^R(d − 1)» is EXACT at d = 3 for both channels» is verbatim at
  docs/new/N5-SLOT-box160.md l. 50 (9effea1f). The precise form (§6) is the W-channel, ISO form. ✓
- Instance (own code): in 𝓛^R_4 (R197 W-targets), ISO, acyclic; my simulator's run from 11111011: 11111011, 11110011, 11110010, 11110000,
  11100100, 11001101, 11001111, 10011111, 00010111, 00010110, 00010100, 00000100 = packet §6 exactly. T 11, level-0 steps [7, 8], seg1 6,
  tail 3, seg1 + tail = 9. ✓
- Unconditional content: SC-ISO at d = 4 ⇒ T^R(3) ≥ 9. ✓ The DEAD needs the machine premise MP: T^R(3) ≤ 8.

## Ruling on the DEAD with its listed gap (G-FLIP-1)
- What I sign: (i) the instance computation (seg1 + tail = 9 on an ISO genome of 𝓛^R_4); (ii) the implication «SC-ISO (at d = 4) ⇒
  T^R(3) ≥ 9»; (iii) «SC-ISO is false IF T^R(3) ≤ 8».
- G-FLIP-1 (open): MP «T^R(3) ≤ 8» is a single-encoding SAT result (L-RED's xcnf.py, CaDiCaL UNSAT), not Lean, not refereed, not landed.
  CLAUDE.md lets a referee sign with the gaps listed, so: **SIGN WITH GAP**. The line already states the dependence
  («together with the machine premise T^R(3) ≤ 8 (… not Lean, not refereed; without it the instance shows that SC-ISO at d = 4 forces
  T^R(3) ≥ 9)»). RESULTS must keep that wording. The item must not be cited as an unconditional DEAD.
- Closing G-FLIP-1 needs both: (a) an INDEPENDENT encoding (L-COMP 9) reporting UNSAT for «T ≥ 9 on 𝓛^R_3, any start, ISO or not»;
  (b) a referee check of that encoding against R104's definition (the CLAUDE.md trap: an unfaithful implementation proves nothing),
  including that it ranges over all of 𝓛^R_3 (not only ISO genomes) and all starts.
- My own evidence (DATA, not a proof): I re-ran the lane query at 9effea1f with L-RED 5f3e89e1's encoding (iso.py 3 9: UNSAT 8.2 s;
  iso.py 3 8: SAT 6.6 s, NOT independent). My own simulator replays the T = 8 witness (T 8, level-0 steps [4, 6]). Hill-climbs on
  𝓛^R_3 with my simulator (mutating ranks, parities, gates, Ξ-targets, start; R197 W-targets fixed): 205,419 runs from the 29 d = 3
  corpus genomes and random ones reached T 7; 110,436 runs from the T = 8 witness reached T 8, never 9. The 29 d = 3 corpus genomes over
  all starts: max T 7.

## Machine checks
- Lane block «P-IDEAL-FLIP» (w162 + pin162) re-run at 9effea1f (worktree, experiments/new), 11:15Z: PASS, exit 0. «WONLY 0 ISOA 0 FROZ 0
  CONS 0 SWAP 0 SWAPNEG 12594 NOWONCE 0 NOWCTRL 307 FLIP1 0»; CHECKED 44,084 / 31,320 / 1,044 / 28,896 / 15,660 / 307 / 1,312; INST
  iso_d4_st9 T 11 [7, 8] seg1 6 tail 3; WIT V_0 2 (kf0_d2_t2), V_1 3 (kf1_d2_t3); box150 checker VIOL 0; pins match.
- Own tool docs/referee-2/R2-P-IDEAL-FLIP/flip_check.py (my simulator; c-step, forced run, H_q, G^swap, exact FLIP-1 search all my own):
  - Genomes: random 𝓦_d (d ≤ 5; level-0 movers 0, 1 of degree 1-3, widths 1-3 above, degrees 1-3, half ISO); random 𝓛^R_d (3/4 ISO);
    the 50 box160/box162 corpus genomes (every start, all have d ≤ 4).
  - W-ONLY (a) on 23,160 real steps (incl. non-𝓛^R 𝓦_d genomes with degree-1 and degree-3 movers, which the lane DATA does not cover);
    (d) forced replay u_t|U = s_t|U and flips ≤ 2 on 9,380 ISO 𝓛^R runs; (b) 40,632 state pairs; (c) 40,480 frozen runs; SWAP 72,128
    (state, c) pairs; NOW-ONCE (a) 307 move pairs; NOW-ONCE (b) 5,935 pairs on random bit sequences; 19,312 runs in all. 0 violations.
  - FLIP-1: exact maximum over forced runs (depth ≤ 14) on 200 random ISO 𝓛^R_2 genomes × 16 starts (3,200 pairs), k = 0 … 6:
    max {k = 0: 2; k = 1 … 6: 3}. 0 violations; both bounds reached.
  - Controls: FNEG=1 (c-step ignoring c) fires W-ONLY (a) 463, (c) 386, (d) 345; SWAP at the same c differs 60,084 times.
  - (My first control run used NEG=1, which my base simulator m2_check.py also reads (old-state keys), so it changed the real runs too and
    gave spurious NOW-ONCE hits; renamed to FNEG and re-run. Recorded so nobody reuses NEG there.)
- DATA scope per statement in the line: matches what the tool counts (W-ONLY step form on 𝓛^R genomes only; NOW-ONCE (b) and T_k(m),
  m ≥ 2, «no signed DATA»). P-1: «40 random starts otherwise» never applies (every genome in the run set has d ≤ 4; flipcheck.py l. 103).

## TARGET.md diff
- No statement mentions a parity game, an algorithm or running time; all are about IDEAL-model runs and the forced runs defined from
  them. No M4 / M3 claim, no gauntlet step. FLIP-ADD, SLOT-TRADE, G-N5-TIME OPEN. The packet's §7 diff is correct.

## Line L-1: clause by clause, every definition against the packet
- Premises ✓ (R104 definition; R109 SEG-ONCE at l = −1 only). Definitions 𝓦_d, 𝓛^R_d («no other movers» = N = 2d), T^R(d) (with T^R ≤
  T*), ISO, b_0, c-step (A-sets old, keys new, 0 and 1 kept, level-1 keys (κ^c_w, own gate)), κ^c, T_k(m) (supremum over ISO genomes of
  𝓛^R_(m+1), starts, bit sequences with ≤ k changes, of the steps changing levels ≥ 1) = §1. ✓
- W-ONLY: (a) on 𝓦_d ✓; ISO independence ✓; frozen form ✓ (true even without ISO); corollary on ISO 𝓛^R_d, d ≥ 2 ✓.
- NOW-ONCE (both forms) on 𝓛^R_d ✓ (the line does not require ISO for the c_t form; the proof does not use it: fine).
- SWAP ✓; «so under ISO a c_t-step sequence with k changes is a concatenation of at most k + 1 runs of two fixed IDEAL genomes» ✓
  (unconditionally, by N-1).
- FLIP-1 ✓ with the two instance sha1s. DEAD ✓: SC-ISO text = §6 precise form (seg1 = steps before the first step moving 0 or 1, tail =
  steps after the last), instance numbers, and the machine premise with its status and the conditional reading — exactly G-FLIP-1's terms.
- Scope tail and DATA tail ✓ (counts = lane output above).
### Optional
- P-1: DATA «every start for d ≤ 4, 40 random starts otherwise» → «every start (all genomes have d ≤ 4)».
- P-2: «(in R109's 𝓛_d, not in 𝓛^R_d)» is about G^swap; fine as is. If F-1's fixes entry adds the T*(d − 1) cap, it should stay out of
  the line (not signed DATA).
- P-3: W-ONLY frozen form: «freezing 0 and 1 at options q» could add «(from any state with q at 0 and 1)».

## Signatures
W-ONLY (a)-(d), NOW-ONCE, SWAP / SWAP-RUN, FLIP-1: SIGN (Opus 5.5, D12). DEAD SC-ISO: SIGN WITH GAP G-FLIP-1 (machine premise
T^R(3) ≤ 8; signed content (i)-(iii) above). REFEREE-2 successor 27, 2026-11-05 11:16Z (date -u). Line L-1: MATCHES.
