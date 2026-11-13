# R245: adversarial rebuild of the kill candidate G_k (L-RED-B 5's rule-built family, rule relayed by the Lead 12:27Z) — VERDICT: SURVIVES (DATA + one trivial lemma; not a proof for all k)
L-RED successor 70 (session_01V5yGRVqzUx6dwT71TpkK6X, Fable 5.2 xhigh), D1 / D18 / D25; Lead re-target 12:19Z («You are the FIRST adversary and now the adversary OF THE KILL
CLAIM (D1 cuts both ways)»). Written 2026-11-13T12:31Z (date -u). Labels: DATA (counter, set, scope), PROVED (lane), READING. Nothing here is a RESULTS entry.
Claim attacked: for k ≥ 3 the genome G_k (Ξ-acyclic, degree 2, k + 1 W-levels, N = 9k − 16) has T_key = 2^k − 2 in 1P(G) = R104's IDEAL model, so by R117
(REACH3, REAL-IDEAL-S3) N5 from S3 on Γ3(G_k) makes at least 2^k − 2 iterations on a game with n = 135k − 230 vertices.
**What this file does NOT establish: T_key = 2^k − 2 for every k (data to k = 12; the induction proof is owed elsewhere); N5 beyond k = 8; an independent Γ3 builder.**

## 0. Verdict
SURVIVES. No clause and no instance broke in attacks (1)-(5) below. L-RED-B's files and generator were not read; everything was rebuilt from the written rule.

## 1. Rebuild (gk244.py, own generator from the rule text)
sha1 of json.dumps(G) (keys N, lev, deg, opts, gate, br, bp, start) equals the Lead's four values: G_3 cd3cd7e361dfe16482bbe56eb87d3e3decf9e6af, G_4
7a2218bfa94e37f85b3fc60d874030aeba8ca848, G_8 d3ad8e2e6f202eb17e66d04dad77de1a33e74eb2, G_10 da29d33ecaf20cb777650729e54acb1dad17cfd9 (out/gk244_build.out;
files experiments/red/r244/gk/, SHA1SUMS).

## 2. Membership in R104's class (class244.py; clauses as docs/red/P-N5-REALIZE.md §2 states them; out/gkrun244.out, k = 3..12)
- As generated: GRADED, XT, BETA (bijection onto 0..M − 1), RANK (bijection, bp ∈ {0, 1}), START, ACYC (self-loops counted) PASS; GATE («a bijection of the options
  onto 0..M − 1») FAILS, because gate = 100·level + eps.
- **Lemma RENUM (PROVED lane, trivial).** An order-preserving renumbering of the gate indices does not change the IDEAL run. Proof: the step reads gates only in
  lexicographic comparisons of key tuples of equal length (P-N5-REALIZE §2, «IDEAL step»), which depend on the order of the entries only. ∎ DATA: G_k^renum (gates
  renumbered onto 0..M − 1) passes all seven clauses, and T, every state and every switch count equal G_k's on sim244 and on r187 ideal.traj, k = 3..12.
- Wires (two options on ONE W-target, both Ξ-targets = exit), level-0 movers with exit Ξ-targets and bp = 0 everywhere violate no clause of §2. R117's statements
  are scoped «IDEAL-ACYC» or «every genome» (RESULTS R117 line, trunk 5d7aab0f) with no further hypothesis on degrees, W-targets or parities. LIMIT: I searched
  the two statements; I did not re-read every proof step of R104 / R117 for a hidden use of distinct W-targets. The N5 counters of §4 test the lemmas' conclusions.
- Every mover has degree 2 (REFEREE-2 41's LIFT caveat does not apply); movers per level at k = 5: 2, 2, 4, 7, 8, 6.

## 3. Model side, own engines (gkrun244.py; sim244 and r187 ideal.traj, states equal)
k = 3..12: T_key = 6, 14, 30, 62, 126, 254, 510, 1,022, 2,046, 4,094 = 2^k − 2; largest per-mover switch count 2^(k−2); N + M = 27k − 48; T / (N + M) from 0.182
(k 3) to 14.833 (k 12).

## 4. N5 itself (kt241.py = L-RED's SPEC-exact n5s237 from S3 on Γ3(G_k^renum) with 34 must-0 counters and the second engine n5v; zcheck244.py = the same run to
## its END against a Zielonka written here; table computed by script, out/gk_table.out)
| k | N | M | n(Γ3) | 135k-230 | T_key (N5 FL run) | 2^k-2 | first fallback | N5 iterations | 2^k+1 | fallbacks | must-0 counters nonzero / all | n5v xdiff | maxsw | to the end: iterations, wrong, bad_E, bad_O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 11 | 22 | 175 | 175 | 6 | 6 | 7 | 9 | 9 | 1 | 0 / 34 | 0 | 2 | 9, 0, 0, 0 |
| 4 | 20 | 40 | 310 | 310 | 14 | 14 | 15 | 17 | 17 | 1 | 0 / 34 | 0 | 4 | 17, 0, 0, 0 |
| 5 | 29 | 58 | 445 | 445 | 30 | 30 | 31 | 33 | 33 | 1 | 0 / 34 | 0 | 8 | 33, 0, 0, 0 |
| 6 | 38 | 76 | 580 | 580 | 62 | 62 | 63 | 65 | 65 | 1 | 0 / 34 | 0 | 16 | 65, 0, 0, 0 |
| 7 | 47 | 94 | 715 | 715 | 126 | 126 | 127 | 129 | 129 | 1 | 0 / 34 | 0 | 32 | 129, 0, 0, 0 |
| 8 | 56 | 112 | 850 | 850 | 254 | 254 | 255 | 257 | 257 | 1 | 0 / 34 | 0 | 64 | not run |
- fit: log2(iterations - 1) - k for k = [3, 4, 5, 6, 7, 8] : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0] ; iterations = 2^((n + 230) / 135) + 1 exactly on these rows
- All rows as claimed (script line «ALL ROWS AS CLAIMED»): FL run 2^k − 2, first fallback at 2^k − 1, 2^k + 1 iterations, one fallback, every counter 0
  (std, tau3, w3, KEY-TAU kp / kpf / kpa, …), n5v xdiff 0; to the END at k = 3..7: winners equal Zielonka's (wrong 0), Even's final strategy and Odd's reply both
  winning on their regions (bad_E 0, bad_O 0). Control ZCTRL=1 (priorities shifted by one for Zielonka): wrong 102 (k 3), 183 (k 4).
- Addendum (k = 9, same harness kt241, out/gk_n5_kt241_k9.out): n 985, FL run T 510, first fallback 511, iterations 513, fallbacks 1, must-0 counters nonzero 0 / 34, n5v xdiff 0, maxsw 128; as claimed (2^9 - 2, 2^9 - 1, 2^9 + 1, 135·9 - 230): True. k = 10 was still running at the commit.
- LIMIT: Γ3 is built by box 189's gamma3.build (claude/l-new a143d406, an object); L-RED has no Γ3 builder of its own, so the builder is common to all three
  checks so far (L-RED-B, the Lead, this one). N5 engine and Zielonka here are L-RED's.

## 5. Robustness (robust244.py on sim244, k = 4..7; out/robust244.out)
- EPS: 300 random renumberings of the gates inside each level ≥ 1 that keep the rule's class order (e < u < v < wires < observers): T = 2^k − 2 on all 300 at each
  k (1,200 runs). EPS-PAIR: swapping the two gates of any ONE mover of level ≥ 1: T unchanged for every mover. The run length is not an accident of ε.
- START: flipping one start option changes T for some classes (k 7: u 2 … 126, yb 2 … 48, e 8 … 43, yp 41 … 113, ypb 8 … 43) and not for others (wires, most
  v and y). The stated start is part of the rule; on Γ3 the default start S3 selects it through the pad priorities (R117 Lemma S3-START).

## 6. Why three weeks of landed lemmas did not exclude it (READING of the statements' scopes)
RESULTS R113 (ALIGN, F(l), PAIR-DOUBLE) and R120 (MOVE, DOUBLE-EQ, PULSE-NEST, GAP-NEST) are stated «on 𝓛^R_d», R110's 2-wide ladder whose two movers per level
have the pair below as W-targets. G_k is outside 𝓛^R_d: up to 9 movers on a level (k = 12), wires with both options on one W-target, observers two levels above the pair
they watch. R113's KP-MOVE («at any degree elsewhere») applies and is not violated. R244 of this lane (B rigid, no room for the memory of §2 there) is a 2-wide
statement as well: the wires and observers are exactly the memory a 2-wide ladder cannot hold.

## 7. Open (for the Lead to route)
(a) the induction proof of T_key(G_k) = 2^k − 2; (b) a Γ3 builder written from R117's text by a lane other than L-NEW; (c) N5 at k ≥ 9; (d) a referee read of
R104 / R117's proofs for the wires. Until (a) and the referees, the kill is a CANDIDATE with DATA to k = 12 (model) and k = 8 (N5).

## 8. Renamed and completed on the Lead's word (12:41Z; added 2026-11-13T12:58Z by date -u; this file was docs/red/R245-gk-verdict.md in 706d1ecc)
- Items (0)-(5) of my 12:30Z message are §1 (0 rebuild), §2 (1 membership), §3 (2 model), §4 (3 N5 itself), §5 (4 robustness), §6 (5 landed lemmas).
- The «NOT established by me» list, verbatim from that message: «What is NOT established by me: T_key = 2^k − 2 for ALL k (data to k = 12 here, a proof by
  induction is still owed); N5 beyond k = 8; an independent Γ3 builder; a line-by-line re-read of R104 / R117 proofs against wires.» Since then: N5 at k = 9
  (§4 addendum); the Lead reports (12:41Z, not checked by me) that L-RED-B 5 and L-COMP 22 each have a Γ3 builder of their own with equal .pg files to k = 9,
  so the builder is no longer common; the line-by-line re-read (wires, exit targets, all-even parities, level width) is now REFEREE 35's and successor 71's.
- Addendum (k = 10, kt241, out/gk_n5_kt241_k10.out): n 1120, FL run T 1022, first fallback 1023, iterations 1025, fallbacks 1, must-0 counters nonzero 0 / 34, n5v xdiff 0; as claimed: True.
- Files and sha1 (sha1sum; experiments/red/r244):
  126b6ce6818904a961702d624b536773e97fcaa2  gk244.py
  b83c1019d2662bc839077e73cac14f348c0d454f  class244.py
  26aad3df48c01a595cbd25d0648c9e336c45cb11  gkrun244.py
  712e1f685ca9ea27a63216d7e1a5df92375f1e44  robust244.py
  312bdc5a9644c5fe7495afb7f69614bc1b068188  zcheck244.py
  b9be6ef1429826c7fd396dd0b42383049c1ac601  sim244.py
  cd3cd7e361dfe16482bbe56eb87d3e3decf9e6af  gk/G_3.json
  7a2218bfa94e37f85b3fc60d874030aeba8ca848  gk/G_4.json
  d3ad8e2e6f202eb17e66d04dad77de1a33e74eb2  gk/G_8.json
  da29d33ecaf20cb777650729e54acb1dad17cfd9  gk/G_10.json
  fe5b59464d938730eb8e19afff139d983d2c3946  gk/G_3_renum.json
  b293075ce300b23477f3bb6ad694c6577b2c64d2  gk/G_8_renum.json
  a0f65098759a89bcf7896e151842476cd253b5f5  out/gk_table.out
  97e992ac3945bad0dc731db655c0331293cb6930  out/gkrun244.out
  16a4b4516ddb5e4c599fa28fa1f2e06ff0db610c  out/gk_n5_kt241.out
  ac8ff12a06dfa097e61588e075dad0768adb7101  out/gk_zcheck244.out
  7fe399e718c2bea62737c98ba710d5e0054de7c9  out/robust244.out
  (the sha1 of G_3, G_4, G_8, G_10 above are sha1sum of the files = sha1 of json.dumps(G), the Lead's four values; all 20 genomes: gk/SHA1SUMS)
