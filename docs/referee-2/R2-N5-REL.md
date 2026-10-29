# R2-N5-REL: REFEREE-2 report on packet P-N5-REL (box 25): Lemma GATE-RISE and its Count, Theorem STATIC-DEPTH-REL, Corollary REL-SPLIT
Referee: REFEREE-2 successor 19 (session_01V5yGRZzoAVpZvqB1LedCVF), Opus 5.5 (D15, L37). Written 2026-10-29 from 04:47Z (date -u).
Object: docs/si/P-N5-REL-box25.md, sha1 f79300a2d01cfb0aa27ad7214bcefbd84eafd7bb (measured with `git show <ref>:<path> | sha1sum` at l-si 07f19760 and
origin/claude/l-si: both equal the pin), 128 lines, frozen. Author L-SI successor 21. Quote base b28123a58.
INDEPENDENCE:
- I have not opened any REL file under docs/referee/ and have not run `git log` on origin/claude/referee.
- Name count `git ls-tree --name-only -r origin/claude/referee docs/referee/ | grep -c 'N5-REL'`: 0 at 2026-10-29 04:40:50Z, taken before I opened
  REFEREE's SDPRIME report on the Lead's word; 0 at 2026-10-29 04:54:13Z (push turn, after `git fetch origin claude/referee`). Names only.
- REFEREE's SDPRIME report, read for my SDPRIME §C, overlaps this packet in one premise point (W-MONO / Ξ-SUCC at λ_W changes, its SDP-N2). I
  had found that point myself before (R2-N5-SDPRIME §1). N-REL-6 below is mine, and says so.
Lane tools (experiments/si/grun/*.py, experiments/si/rund/quotecheck.py) NOT run or imported. Lane INSTANCE files from
experiments/si/grun/out/*.pg, *.start (origin/claude/l-si) are copied as inputs into docs/referee-2/R2-N5-REL/inst/ (data, no code).
Checker: docs/referee-2/R2-N5-REL/rel_check.py (own; reuses my R2-N5-SDPRIME/sdprime_check.py for cycles, (H3′) and STATIC-DEPTH′'s
recursion), seg_case.py; quotes with ../R2-N5-CORE/qcheck.py; run_all.sh; logs/.
Scope (D1): GATE-RISE bounds σ̄-changes by Ξ-changes plus three exception counts. STATIC-DEPTH-REL and REL-SPLIT reduce a run's length to SEG,
which is not bounded (CONJECTURE SEG-RUN OPEN). Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Verdicts (all "(Opus 5.5, D15)")
| § | item | verdict |
| --- | --- | --- |
| §1 | Lemma GATE-RISE | SIGN (step 3's injectivity is used on u-free values only, N-REL-2) |
| §1 | its Count (CH_S(u) ≤ XR + TIE + CYC + THRU; G(S) ≤ Σ_u) | SIGN |
| §2 | Theorem STATIC-DEPTH-REL (REL-admissible [a, b], (H4′_rel), GEN_W) | SIGN |
| §3 | Corollary REL-SPLIT (\|S\| ≤ SEG·n − 1; SEG − 1 ≤ G(S) + CF(S)) | SIGN (a REDUCTION) |
| §2 | Remark (contains STATIC-DEPTH′ and R77 (c)); not in the to-sign table | correct for the length bound and for settling on V^W_b ∪ V^H_b. STATIC-DEPTH′'s per-vertex claim at other vertices is not implied (N-REL-5). Not signed |
| — | quotes | 16/17 VERBATIM in the tagged lines. The (SW) quote at RESULTS l. 3768-3769 has the same spurious "…" over a line break as P-N5-SDPRIME (N-REL-1). SHIFT=1 control 0/17 |
| §4 | data, CONJECTURE SEG-RUN, READING | not signed. The reader data reproduced (§2 below) |
No gap. Notes N-REL-1..8.

## 1. Proof check (against SPEC S1, S2, S4a, S4c; RESULTS R15 (a), (d), R17 (a), R57 (a), R18 (d) / P2, (SW), R77 (c)'s steps, R80 (a))
### 1.1 GATE-RISE
- Step 1. By (i) and (V1): Ξ_t(u) = u ⊕ Ξ_t(y1) and Ξ_{t+1}(u) = u ⊕ Ξ_{t+1}(y2). Both suffix plays avoid u, because u is off its honest cycle
  at t and at t + 1. ✓
- Step 2. τ′ = σ̄_t with u → y2. By (ii), y2's honest t-play is also its (σ_t, τ′)-play, and u's (σ_t, τ′)-play is u followed by it, so
  V_{σ_t,τ′}(u) = u ⊕ Ξ_t(y2). (VJ) (R57 (a)) gives Ξ_t(u) ⊴ that. ✓ (GR2: computed from the play, 0 failures.)
- Step 3. From u ⊕ Ξ_t(y1) ⊴ u ⊕ Ξ_t(y2) and Ξ_t(y1) ≠ Ξ_t(y2), conclude Ξ_t(y1) ◁ Ξ_t(y2).
  - The step needs u ⊕ · to be order-REFLECTING on these two values.
  - If their cycle nodes differ, u ⊕ keeps each cycle node, and the order compares cycle-node rewards first, so the order of the two values
    is kept.
  - If the cycle nodes are equal, both values are u-free (steps 1 and 2: y1's t-play by (i), y2's by (ii)). u ⊕ adds the same term to both
    path sets, or to neither, and 1 to both lengths. So the order is kept and the map is injective.
  - The packet's injectivity sentence ("x is recovered from u ⊕ x") is true for u-free x. It does not say "u-free", but both values it is
    applied to are (N-REL-2). ✓ (GR3: 0 failures.)
- Step 4. R15 (a), (d): Ξ_{t+1}(y2) ⊵ Ξ_t(y2) (GR4). (V2) on the u-free values Ξ_{t+1}(y2) (y2's (t + 1)-play avoids u by (i)) and Ξ_t(y2) (by
  (ii)). The strict step comes from step 3. ✓
- Count. Every σ̄(u)-change is CLEAN, TIE, CYC or THRU (the kinds overlap; the sum still bounds). A clean change is a transition at which Ξ(u)
  changes. A σ̄-changing transition has a changing u ∈ Q_Odd. ✓ (GRC, GRC_G: 0 failures.)

### 1.2 STATIC-DEPTH-REL
- Sets.
  - X_b is closed under "Even vertex on a member's W- or honest b-play". So every Even vertex of V^W_b ∪ V^H_b is in X_b (RCLOSE), and
    V^W_b / V^H_b are closed under their frame's b-successor.
  - The recursion's domain claims hold. σ_b(v) for Even v ∉ T lies on both of v's b-plays, so in V^W_b ∩ V^H_b. (RDOM: 0.)
- Items 1-3 are as in STATIC-DEPTH′, restricted to the relevant sets:
  - Item 1 uses only the CW_b / CH_b cycles, which persist by REL-admissibility.
  - Item 2's honest half needs σ̄ constant only at Odd v ∈ V^H_b ∖ T_H. Such a v is on the honest b-play of a member of X_b, i.e. v ∈ RO_b,
    and REL-admissibility gives exactly that. ✓
- Item 4.
  - (A): y ∈ V^H_b. Its honest b-play is a suffix of v's, with Odd vertices in RO_b. So Ξ_t(y) = Ξ_{t′}(y) by H-settledness. With (SW) and
    Ξ-SUCC the contradiction is the same as in STATIC-DEPTH′. ✓
  - (B): uses only W-plays, τ, P2 and W-MONO. ✓
  - (C): v ∈ X_b, so v's W-cycle at b is in CW_b and persists. GEN_W is used only for v's two W-plays (my used-form check on X_b). ✓
  - Nowhere does the proof read σ̄ at an Odd vertex outside RO_b, except through Ξ-SUCC and S4a's arena, which are global facts of every
    in-phase S4a transition. ✓
- Item 5.
  - For t ≥ a + max_{Q∖T} d: Even v ∈ Q ∖ T keep σ_b(v) (item 4), Even v ∈ Q ∩ T keep it (item 1), and the other Even vertices have
    out-degree 1. So σ_t = σ_b, and R80 (a) gives the length.
  - max d ≤ |Even ∖ T|: the recursion paths are acyclic and count distinct Even vertices outside T. ✓
- (H4′_rel) is not vacuous: it fails at 8 + 27 REL-admissible intervals.

### 1.3 REL-SPLIT
- REL-admissibility of [x, b_k] for b_k's sets is a per-state condition, so it is monotone in x, and a_k is well defined.
- b − a = Σ (b_i − a_i) + SEG − 1.
- For i ≥ 2, [a_i − 1, b_i] fails and [a_i, b_i] passes, so a_i − 1 → a_i either changes σ̄ at some u ∈ RO_{b_i} (counted in G(S)) or makes a
  CW_{b_i} / CH_{b_i} cycle appear (counted in CF(S)). The cuts are distinct transitions, so SEG − 1 ≤ G + CF.
- With STATIC-DEPTH-REL per segment, |S| ≤ SEG(n − 1) + SEG − 1 = SEG·n − 1. ✓ (RSCUT, RSCNT, RSsum, RSLEN, RSLEN_run: 0 failures.)

## 2. Data (own checker; every non-mutation run 0 violations)
| corpus | runs | GATE-RISE clean / TIE / CYC / THRU | REL-admissible intervals (RELCAP 60) | GEN_W used | beyond STATIC-DEPTH′ (σ̄ moves off RO_b) | Remark checks | runs S (with hyp.) / segments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| alt_all (413; given start else S3; 1 start entry validated) | 413 | 3,713 / 82 / 10 / 125 | 36,502 | 36,362 | 4,094 | 32,400 | 920 (874) / 2,874 |
| lib41_noref × 3 | 1,230 | 3,751 / 168 / 23 / 109 | 53,652 | 53,461 | 3,281 | 50,344 | 1,612 (1,536) / 4,671 |
| named (si/root/instances 7, nep90_n40) | 8 | 390 / 0 / 1 / 3 | 1,173 | 1,173 | 539 | 634 | 48 (45) / 198 |
| lane instances grun/out (28: rdr_K10, anc_K10, climbs fx_*, gc*, pg_*, sg_*, sz*, seeds) | 28 | 870 / 71 / 9 / 0 | 3,012 | 3,012 | 2,947 | 65 | 29 (29) / 407 |
| random kO n 8-20 / k2 n 6-16 (3,000 × 3 each) | 18,000 | 325 / 55 / 70 / 2 | 2,325 | 2,324 | 192 | 2,132 | 2,518 (2,517) / 3,047 |
- Reader-proofness data reproduced (seg_case.py, own engine, given starts): rdr_K10 (n 74) and anc_K10 (n 99) both have the run [1, 100] with
  |S| = 99, G = 91, SEG = 9, as §4 says.
- SEG / n:
  - max 0.792 on alt_all (so_sor5_n24), as §4's "≤ 0.79n in the library";
  - 0.95 on lib41 with a random start (lev_l_n20 #2; §4's library figure presumably uses S3 / given starts);
  - 1.00 on the lane climb sg_2, as §4's "≤ 1.00n after climbs".
  - |S| / (SEG·n) ≤ 0.917. The bound is never reached.
- Longest REL interval: 55 transitions (x32_rand64); sharp in 395 + 442 intervals.
- Without GEN_W (used form) the conclusion still held in all 132 + 164 + 1 such intervals (unsigned).
- Controls (REL_MUT on lib41 × 3; counted as failures):
  - y2rise (GATE-RISE demanded of Ξ(y2)): 3,426;
  - tie (at TIE changes): 167 (of 168), so (iii) is needed;
  - cyc (at CYC changes): 8 (of 23), so (i) is needed;
  - thru (at THRU changes): 0 of 109, so (ii)'s necessity is NOT exhibited (N-REL-3);
  - dm1 (settling from a + d − 1): 18,837;
  - nosbar (REL-admissible without σ̄ constant on RO_b): 212,050, including RLEN 1,450 and RSIG 1,450. The σ̄ condition carries the LENGTH
    bound;
  - qonly (X_b := Q, no closure): the recursion leaves its domain (RDOM 246, RCLOSE 14,331), so the closure of X_b is structurally needed.

## 3. Notes (not gaps)
- N-REL-1 (quote).
  - [Q docs/RESULTS.md@b28123a58:3768-3769] «(SW): every Even switch of N5 is to an edge … of Iσ». The "…" stands for a line break only.
  - The same cosmetic point as P-N5-SDPRIME (N-SD-1 = SDP-N3). 16/17 strictly verbatim.
- N-REL-2 (GATE-RISE step 3). State "for u-free x with a fixed cycle node" in the injectivity sentence, and note the case of different cycle
  nodes (order kept, since u ⊕ keeps the cycle node). Both values it is applied to are u-free by (i) and (ii). Wording.
- N-REL-3 (thin spot: (ii) unexercised as a necessity). All 239 THRU changes in my data (125 + 109 + 3 + 2) still raised Ξ(u).
  - (ii) is used in the proof (step 2's τ′-play), so it stays a hypothesis. The data do not show it is needed.
  - TIE (iii) and CYC (i) are needed: their controls bite.
- N-REL-4 (notation clash).
  - §2 sets "Q := the Even vertices of out-degree ≥ 2". The fleet's landed texts use Q for the ODD vertices of out-degree ≥ 2: RESULTS R56, R71,
    R80, R81, P-N5-FBC, P-N5-FBCK. This packet's own §1 Count also sums over the Odd ones.
  - A different letter (e.g. E_2) would avoid misreading. The statement is unambiguous as written, since §2 defines it.
- N-REL-5 (the Remark, not to sign).
  - "STATIC-DEPTH-REL contains STATIC-DEPTH′" holds for the length bound. With (H4′) ⇒ (H4′_rel) (a sub-recursion) and REL's T ∩ X_b = SD′'s T
    ∩ X_b, its max_{Q∖T} d is ≤ SD′'s max d (RREM, RREM_d: 0 on 85,575 checks). It also holds for per-vertex settling on V^W_b ∪ V^H_b.
  - STATIC-DEPTH′'s per-vertex settling at vertices outside V^W_b ∪ V^H_b (e.g. a reader) is NOT a conclusion of STATIC-DEPTH-REL. The Remark
    should say "contains its length bound".
- N-REL-6 (premise scope; the same point as R2-N5-SDPRIME §C.3 = SDP-N2).
  - W-MONO and Ξ-SUCC are cited from R77 (c), landed under R77's (H1), which includes λ_W constancy. REL's runs do not fix λ_W.
  - Both facts hold at every in-phase S4a transition: P2 at one step, and R15 (a), (d) with (SW).
  - The same repair wording applies.
- N-REL-7 (§4's SEG figure, not to sign). SEG reaches 0.95·n on lib41 with random starts (lev_l_n20), above §4's "≤ 0.79n in the library". The
  start sets differ. Under S3 / given starts my maximum is 0.792, matching §4.
- N-REL-8 (what the new freedom buys). REL-admissible intervals outside STATIC-DEPTH′'s hypotheses, where σ̄ moves at an Odd vertex off RO_b:
  4,094 + 3,281 + 539 + 2,947 + 192. On the lane's reader instances almost every interval is of this kind (2,947 of 3,012). That is the
  packet's point: readers change σ̄ off the relevant plays and do not cut segments (SEG 9 against G 91).

## 4. DONE / FINDINGS / NEEDS
- DONE: this report; docs/referee-2/R2-N5-REL/{rel_check.py, seg_case.py, grun.lst, inst/ (lane instance copies), run_all.sh, logs/}.
- FINDINGS:
  - GATE-RISE with its Count, STATIC-DEPTH-REL and REL-SPLIT all SIGN, no gap.
  - The σ̄ condition on RO_b carries the length bound (nosbar control). Hypotheses (i) and (iii) of GATE-RISE are needed; (ii) is not shown
    needed in data (N-REL-3).
  - The Remark holds for the length bound only (N-REL-5). Q is redefined as the Even choice vertices (N-REL-4).
- NEEDS: Lead: the §C word; route N-REL-1..8 to L-SI.
