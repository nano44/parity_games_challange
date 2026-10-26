# R-N5-2T: REFEREE report on packet P-N5-2T (L-SI box 16: with ≤ 2 Odd choice vertices per honest class, late Q-runs are O(n²) and a phase has O(n³) in-phase fallbacks; Theorem FB-2T, Corollary FB-2O on 𝒞^2O)
Referee: REFEREE (successor 12, session_01KNDBjZvPFLaNjEdCmEWBcN), Opus 5.5 (owner ruling D15).
- Routing: the Lead's message of 04:30Z (Lead's stamp), item (4).
- Object: docs/si/P-N5-2T-box16.md at trunk cbb3b738, sha1 fcb91130b1f93d041233c9def50614b4d0dc9a05 (checked with
  `git show cbb3b738:docs/si/P-N5-2T-box16.md | sha1sum`; identical on my tree), 225 lines, frozen at l-si f6839fd3. Author: L-SI
  successor 11.
- Written 2026-10-26T04:50Z-04:58Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/ 2T file on my tree; none opened. No lane code run (experiments/si/fb2o/fb2o.py,
  climb2o.py); the lane's file list lib2o.txt is used as INPUT only. D1.
- Compared against: RESULTS R56 (a)-(c), (f) (landed text, docs/RESULTS.md l.2832 ff.), which my lane signed as P-N5-FBRED (R-N5-FBRED with
  §C); P-N5-FBPOLY (FBP) §0.3 (YB); RESULTS R54 (e) (Φ-kO), R38 (a).
- Tool: scratch/twot_probe.py (own engine; ARITHMETIC κ sums; any game). Logs scratch/twot_logs/ (run_all.sh).

## Verdicts (CONDITIONAL on RESULTS R56, landed, as the packet states)
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §2 | (YB_q): q ∈ Q_c on its own honest cycle ⇒ P = ∅, 1 ≤ ℓ ≤ \|U_c\| − 1, κ ∈ Cyc_c | SIGNED |
| §2 | Lemma PFZ-q: κ-PFZ_D on q-runs (only κ(q) constant), z ∈ (U_c ∖ T) ∪ {q} | SIGNED |
| §3 | Lemma ROUTE-2: Q_c = {q, q′} ⇒ at every state one of them is direct | SIGNED |
| §4 | Lemma DIR: t > g_{\|U_c\|−1}, q direct ⇒ κ_t(q) ∈ A_q, \|A_q\| ≤ d_q + w_c | SIGNED (2T-N2: holds for any \|Q_c\|) |
| §4 | Lemma SAT-2: late and saturated in q's run ⇒ κ_t(q′) ∈ V_{q′}(κ_Θ(q)), \|V\| ≤ d_{q′} + w_c | SIGNED |
| §5 | Theorem FB-2T: under (2T), N_late ≤ 1 + Σ_c (N_c − 1), N_c = O(n²) | SIGNED |
| §5 | Corollary FB-2O: on 𝒞^2O every phase has f ≤ 1 + (n − 1)(1 + 12n²) | SIGNED (2T-N1: one omitted, harmless case) |
| §6, §7 | READING, DATA | not signed (as briefed) |
No gap. Notes 2T-N1 (FB-2O's case list omits "both Odd choice vertices are cycle nodes"), 2T-N2 (DIR needs no two-terminal hypothesis),
2T-N3 (the count in FB-2T step 3 is of distinct pair VALUES; read so it is correct), 2T-N4 (DATA: DIR, SAT-2, FB-2T thin or vacuous in my
data too). Scope: FB-2O bounds in-phase fallbacks per phase on 𝒞^2O; it is not a running-time bound for N5 on any class (crossings and
transitions per phase given f are OPEN, §6). Not a TARGET.md claim; G-N5-TIME stays OPEN.

## 1. Setting and the R56 quotes
- §1's quotes of R56 (a), (b) κ-HAT-FREEZE_D (a), (c) κ-PFZ_D (with the N-FBRED-1 range) and (f) late form are verbatim against the landed
  text (docs/RESULTS.md, R56 (a)-(c), (f)) ✓. The source-state convention (FBRED-N1, landed in R56's setting line) is used throughout ✓.
- R56 (f) is "SIGNED AS A REDUCTION in ρ"; its late-form inequality f ≤ 1 + (n − 1) + (n − 1)·N_late is unconditional in N_late, and FB-2T
  bounds N_late. So the combination is an unconditional bound under (2T) ✓. (An earlier-referee point: my predecessor's FBRED-N2 and REFEREE-2's
  N-FBRED-4 say the late regime was never reached in data; that concerns data, not the statement.)
- Q_c := (Q ∩ U_c) ∖ {c}; T ∩ U_c = {c} ∪ Q_c (other cycle nodes are not in U_c) ✓. q-run: Ξ(q) constant ⇔ κ(q) constant on a phase
  ((INJ), λ constant) ✓. Direct: on its own cycle, or its play visits c before any other vertex of Q_c ✓.

## 2. (YB_q) and PFZ-q
- (YB_q): FBP (YB) with q for o, proved in place: q on its own honest cycle, whose cycle node c = λ(q) is its top; P lists vertices before c
  of rank > rank(c), which lie on that cycle, so none; ℓ ≥ 1 (q ≠ c) and ℓ ≤ |U_c| − 1 (a simple path in U_c, (SP′)) ✓. Correctly noted as
  NOT in FBRED's signed text (FBRED §4 table only); proved here ✓.
- PFZ-q, induction on j: base z = q is equality on Θ ✓. Step z ≠ q: p = z·p′, x ∈ {q} ∪ (U_c ∖ T) ✓. Odd z ∈ G_c^q ∖ {q}: not in Q, forced,
  x = next_t(z); (Aκ); hypothesis at t (t > f^Θ_j > f^Θ_{j−1}) ✓ — at x = q it is κ_t(q) = κ_Θ(q), t ∈ Θ ✓. Even z: k := f^Θ_j ∈ Θ, k < t;
  hypothesis at k (k ∈ Θ, k > f^Θ_{j−1}) ✓; κ-FB-ROUND at k (z ∈ U_c ∖ {c}, x ∈ U_c) ✓; (M2κ) from k + 1 to t ✓ (k + 1 need not be in Θ:
  only k and t are read at q). The constancy of other terminals is never used ✓: G_c^q has no other terminal, and FB-ROUND and (Aκ) need
  none. So weakening Q_c-run to q-run is correct.
- VERDICT: (YB_q), PFZ-q SIGNED.

## 3. ROUTE-2
- q not direct: not on its cycle, and its play meets q′ before c. Plays are positional, so from q′ on it is q′'s play. If q′'s play met q,
  q's play would revisit q, so q would lie on its own play's cycle: excluded. So q′'s play avoids q; it stays in U_c ((Aκ)) and its cycle
  contains c; hence q′ is on its own cycle or meets c before q, i.e. direct ✓.
- VERDICT: SIGNED.

## 4. DIR and SAT-2
- Value sets: |A_q| ≤ d_q + w_c (each successor y contributes at most one value: y = c gives κwt_c(q), y ∉ Q gives one κopt term; plus
  |Cyc_c| = w_c) ✓. |V_{q′}(α)| ≤ d_{q′} + w_c (one β per successor y ≠ q′; T ∩ U_c = {c, q, q′}, so y ∈ {q, c} or y ∉ T) ✓.
- DIR: on its cycle ⇒ (YB_q) ✓. Otherwise y := σ̄_t(q) ∈ U_c, κ_t(q) = κwt_c(q) + κ_t(y), y ≠ q. y's play is q's play minus q, which (q
  direct, not on its cycle) meets c before any vertex of Q_c and never returns to q; so y ∉ Q_c (else y itself would be met first), and y = c
  or y ∈ U_c ∖ Q ✓. y = c: (0, 0) ✓. Otherwise "≤": the prefix of y's play to c avoids Q, so it is a path of G_c ((SP′), Even σ_t edges, Odd
  forced) and κ_t(y) ≤ κopt_c(y) ✓; "≥": κ-HAT-FREEZE_D (a) with j = |U_c| − 1 at t > g_{|U_c|−1} (G_c has ≤ |U_c| vertices) ✓. So κ_t(q) ∈ A_q ✓.
  2T-N2: the proof uses only "q direct"; it never uses |Q_c| ≤ 2. DIR holds in any class (consistent with the packet's §6 "DIR holds for
  bottom terminals"). My probe checks it in every class.
- SAT-2: on its cycle ⇒ (YB_q) for q′ ✓. Otherwise y := σ̄_t(q′) ∈ U_c, y ≠ q′, y's play avoids q′ ✓. y = q: κ_Θ(q) ✓; y = c: (0, 0) ✓; y ∉ T:
  "≤" — the prefix to the first e ∈ T ∩ U_c has e ∈ {q, c}; e = c: a path of G_c (avoids q and q′) ⇒ ≤ κopt_c(y); e = q: a path of G_c^q ⇒
  κ_t(y) = κwt_c(prefix ∖ {q}) + κ_t(q) ≤ κopt^q(y) + κ_Θ(q) ✓. "≥" — κ-HAT-FREEZE_D (a) (t > g_{|U_c|−1}) for κopt_c(y); PFZ-q with
  j = |U_c| − 1 (t ∈ Θ, t > f^Θ_{|U_c|−1}; G_c^q has fewer than |U_c| vertices) for κopt^q(y) + κ_Θ(q) ✓. So κ_t(y) equals the max of the
  defined bounds, β_y(κ_Θ(q)) ✓.
- VERDICT: DIR, SAT-2 SIGNED.

## 5. Theorem FB-2T and Corollary FB-2O
- Step 1: late sources k_i (fallbacks g_j, j ≥ n) satisfy k_i > g_{n−1} ≥ g_{|U_c|−1} (|U_c| ≤ n; strict, as sources are distinct) ✓.
  x_i := (κ_{k_i}(q))_{q ∈ Q}; a vertex of Q is a cycle node (κ = (0, 0), constant) or a terminal of its class ✓. Coordinates are
  non-decreasing ((M2κ)), so equal x ⇔ same Q-run (monotone and equal at both ends ⇒ constant between) ✓, and N_late = #distinct x_i ✓
  (R56 (f)'s N_late, source convention). A coordinatewise non-decreasing sequence has 1 + #change indices distinct terms; each change
  index changes some class's sub-tuple, which (monotone) changes N′_c − 1 times ✓. So N_late ≤ 1 + Σ_c (N′_c − 1) ✓.
- Step 2 (Q_c = {q}): q is always direct (no other terminal) ✓; DIR ⇒ N′_c ≤ |A_q| ✓.
- Step 3 (Q_c = {q, q′}): ROUTE-2 + DIR ⇒ a_i ∈ A_q or b_i ∈ A_{q′} ✓. For α ∈ A_q, I_α is a consecutive index set ((M2κ)) whose sources lie in
  one q-run Θ_α ✓. An index after the first w_c elements of I_α has ≥ w_c fallbacks of Θ_α with earlier sources, so k_i > f^{Θ_α}_{w_c} ✓, and
  SAT-2 applies (k_i > g_{|U_c|−1} from step 1) ✓: b_i ∈ V_{q′}(α). 2T-N3: "the pairs with a = α number ≤ w_c + |V_{q′}(α)|" counts distinct
  pair VALUES (the first w_c indices give ≤ w_c values, the rest have b ∈ V_{q′}(α)); read so, it is correct, and that is what N′_c needs ✓.
  Symmetric for b ∈ A_{q′} ✓. N_c ≤ (d + w_c)(w_c + d + w_c)·2 = 2(d + w_c)(d + 2w_c) ✓.
- FB-2O: (2T) holds as |Q| = 2 ✓; f ≤ 1 + (n − 1)(1 + N_late) from R56 (f) ✓. Cases: one class with both terminals: N_late ≤ N_c ≤
  2(2n − 1)(3n − 2) = 12n² − 14n + 4 < 12n² ✓ (d ≤ n, w_c ≤ n − 1); two classes: ≤ 1 + 2(2n − 2) ≤ 4n ✓; one is a cycle node: ≤ |A_q| ≤
  2n − 1 ✓. 2T-N1: the case "both q1 and q2 are cycle nodes" is not listed; then every Q_c = ∅ and FB-2T gives N_late ≤ 1. Harmless
  (1 < 12n²); one line in the fixes file. Start-freeness: per phase; inductions start at the q-run or phase ✓.
- The Φ-kO remark (not a separate signed item): with ≤ n(n − 1) + d_{q1}d_{q2} phases (R54 (e)) the run has O((n² + d_{q1}d_{q2})·n³)
  in-phase fallbacks; the packet's O(n²·d_{q1}d_{q2}·n³) is a looser but valid upper bound ✓.
- VERDICT: FB-2T and FB-2O SIGNED (conditional on R56, landed).

## 6. Data (DATA, not proof; scratch/twot_probe.py, own engine; logs scratch/twot_logs/)
Checks per phase and class: YB, PFZ (every state of every q-run, every j up to the state's fallback count, every simple path of G_c^q),
ROUTE (|Q_c| = 2), DIR (any |Q_c|, where t > g_{|U_c|−1}), SAT (|Q_c| = 2, both hypotheses), FB2T (phases with (2T) and a late fallback).
Path checks for n ≤ PATHN (14 by default). Mutation TWOT_MUT=1: PFZ with j + 1 edges, DIR / SAT without Cyc_c.
| set | runs | phases (with (2T)) | YB | PFZ | ROUTE | DIR | SAT | FB2T | failures |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lib41, n ≤ 64 (367 games; path checks for n ≤ 14), S3 + 6 random | 2,569 | 12,620 (7,834) | 12,196 | 6,108 | 1,516 | 0 | 0 | 0 | 0 |
| lane list lib2o.txt (43 games with \|Q\| = 2, n ≤ 40), PATHN 16, S3 + 6 random | 301 | 870 (870) | 318 | 1,090 | 1,562 | 6 | 0 | 0 | 0 |
| lib2o.txt, PATHN 40 (every game path-checked), S3 + 2 random | 129 | 380 (380) | 126 | 127,303 | 727 | 3 | 0 | 0 | 0 |
| 3,000 random 𝒞^2O games, n 4-12, seed 52, S3 + 2 random | 9,000 | 22,073 (22,073) | 8,378 | 34,664 | 11,006 | 56 | 0 | 0 | 0 |
| MUTATION (PFZ with j + 1 edges; DIR / SAT without Cyc_c), lib41 n ≤ 64, S3 + 2 random | 1,101 | 5,393 | 5,373 | 5,312 | 748 | 0 | 0 | 0 | 125 PFZ failures (control bites) |
- 2T-N4 (thin data, stated plainly): PFZ-q, (YB_q) and ROUTE-2 are exercised often (PFZ 169,165 checks, 0 failures; the mutation bites).
  DIR's hypothesis (t after |U_c| − 1 fallbacks of the phase) is met 65 times, all OK. SAT-2's and FB-2T's hypotheses are met NEVER in my
  data (the lane: SAT-2 0, FB-2T 0, DIR 1). SAT-2, FB-2T and FB-2O's late regime rest on their proofs (§4-§5), which I checked line by line.
- Reproduce (from docs/referee/scratch): `sh twot_logs/run_all.sh`; `RANDSTARTS=2 PATHN=40 python3 -I twot_probe.py list
  ../../../experiments/si/fb2o/lib2o.txt` (fixed seed; file starts seeded by the RELATIVE path).

## 7. Notes for the fixes file
- 2T-N1: FB-2O's case list: add "both are cycle nodes: N_late ≤ 1".
- 2T-N2: DIR holds for any number of terminals (its proof uses only "direct"); optional remark.
- 2T-N3: FB-2T step 3 counts distinct pair values; optional wording.
- 2T-N4: DATA (thin: DIR checked a few dozen times, SAT-2 and FB-2T never; they rest on their proofs, as the packet says).

## §C. Comparison with REFEREE-2 (REFEREE successor 12; written 2026-10-26T05:06Z by date -u; (Opus 5.5, D15))
- Routing: the Lead's message of 04:59Z (Lead's stamp). Objects: this report (7055b4a5; §1-§7 above unchanged) and
  docs/referee-2/R2-N5-2T.md (referee-2 8f43432b + stamp fix 416334cc, successor 14), opened after 7055b4a5 was pushed. Same pinned text
  (sha1 fcb91130…).

### C.1 Verdicts side by side
| § | statement | REFEREE (7055b4a5) | REFEREE-2 (8f43432b) | joint |
| --- | --- | --- | --- | --- |
| §2 | (YB_q) | SIGNED | SIGN (N-2T-2) | signed |
| §2 | PFZ-q | SIGNED | SIGN cond. R56 (N-2T-3) | signed (cond. R56) |
| §3 | ROUTE-2 | SIGNED | SIGN | signed |
| §4 | DIR | SIGNED (2T-N2) | SIGN cond. R56 | signed (cond. R56) |
| §4 | SAT-2 | SIGNED | SIGN cond. R56 (N-2T-6) | signed (cond. R56) |
| §5 | Theorem FB-2T | SIGNED (2T-N3) | SIGN cond. R56 (N-2T-5) | signed (cond. R56) |
| §5 | Corollary FB-2O | SIGNED (2T-N1) | SIGN cond. R56 (N-2T-4) | signed (cond. R56) |
| §5 | remarks after □ (R54 (e) product; THETA-AFTER) | R54 (e) remark checked as a valid upper bound | not signed; R54 (e) remark checked; THETA-AFTER not checked | not signed |
| §6, §7 | READING, DATA | not signed | not signed | not signed |
No disagreement; no gap in either report.

### C.2 Joint note map
| REFEREE | REFEREE-2 | relation | joint status |
| --- | --- | --- | --- |
| 2T-N1 (FB-2O omits "both cycle nodes", N_late ≤ 1) | N-2T-4 (same) | SAME | fixes file |
| 2T-N3 (FB-2T step 3 counts distinct pair values) | N-2T-5 (same; also: saturation via f^Θ is conservative) | SAME | wording |
| §2 ((YB_q) proved here, not in FBRED's signed text) | N-2T-2 (same) | SAME | — |
| §2 (PFZ-q reads κ of a terminal only at q, on states of Θ) | N-2T-3 (same) | SAME | — |
| 2T-N2 (DIR's proof never uses \|Q_c\| ≤ 2) | — | ADDITIONAL from us; no conflict (FBK uses DIR in exactly that general form) | optional remark |
| §1 ("R56 quotes verbatim") | N-2T-1 (the κ-FB-ROUND parenthetical "FBP §1 verbatim with U_c, c" is FBRED §1.1's text, l.52, not R56's landed "(FBP §0.3, §1 with c for c_θ)") | ACCEPTED; MISSED by us. Confirmed: packet l.64-66 heads it "R56 (a), (b) lemmas used", and the phrase occurs in docs/new/P-N5-FBRED-box44.md l.52, not in docs/RESULTS.md. Same lemma; wording only | fixes file: cite "FBRED §1.1" for that quote |
| 2T-N4 (DATA: DIR 65 checks; SAT-2 and FB-2T never reached) | N-2T-6 (natural data never meet SAT-2 either, best −2; CONSTRUCTED disjoint unions box-43/44 ⊎ small gadgets meet it: 648 SAT checks, every proof branch, 0 violations; mutations show saturation and α are needed; FB-2T's late count never reached) | R2 went further. I RE-RAN R2's four saved witnesses (docs/referee-2/R2-N5-2T/instances/fb17_g{3,4,5,5c}_P66.pg, sha1 4f83da32, 477872f9, aca9f9d4, 5398f9d7 checked) on MY engine and probe (twot_probe.py, PATHN 40, S3): 20 phases, DIR 93 checks, SAT-2 108 checks, PFZ 180,826, 0 failures — the same DIR and SAT counts as R2's row "instances/ (4 saved witnesses)". So SAT-2's hypothesis is now met and checked on two independent engines. | DATA: SAT-2 exercised (constructed instances); FB-2T's late regime unreached in all data |
- Reproduce my witness re-run (from docs/referee/scratch): 
  → twot_logs/r2_witnesses_s3.txt.

### C.3 Joint state (for the Lead and CHECKER)
- Every to-sign item signed by both referees, conditional on R56 (landed). No gap.
- Fixes file: 2T-N1 = N-2T-4 (case list), N-2T-1 (quote provenance); wording: 2T-N3 = N-2T-5; optional: 2T-N2.
- DATA: SAT-2 exercised only on constructed unions (both engines agree); FB-2T / FB-2O's late regime never reached; they rest on their proofs.
