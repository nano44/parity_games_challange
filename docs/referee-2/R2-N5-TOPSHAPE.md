# R2-N5-TOPSHAPE: REFEREE-2 report on packet P-N5-TOPSHAPE (box 49): Fact DELTA, Lemma TOP-SHAPE (a)-(c), Corollary (top changes ≤ n − 1)
Referee: REFEREE-2 successor 19 (session_01V5yGRZzoAVpZvqB1LedCVF), Opus 5.5 (D15, L37). Written 2026-10-29 from 05:14Z (date -u).
Object: docs/new/P-N5-TOPSHAPE-box49.md, sha1 c5b0e8d86745d6db5e0c9f6e1551b10c5b511b8f (measured with `git show <ref>:<path> | sha1sum` at l-new 4c2ea43e
and origin/claude/l-new: both equal the pin), 81 lines, frozen. Author L-NEW successor 30.
INDEPENDENCE:
- I have not opened any TOPSHAPE file under docs/referee/ and have not run `git log` on origin/claude/referee.
- Name count `git ls-tree --name-only -r origin/claude/referee docs/referee/ | grep -ic topshape`: 0 at 2026-10-29 05:06:23Z, taken before I opened
  REFEREE's REL report on the Lead's word; 0 at 2026-10-29 05:18:26Z (push turn, after `git fetch origin claude/referee`). Names only.
Lane tools (experiments/new/box49/topmono.py, quotecheck3.py) NOT run or imported.
Checker: docs/referee-2/R2-N5-TOPSHAPE/topshape_check.py and repro.py (own); quotes with ../R2-N5-CORE/qcheck.py; run_all.sh; logs/.
- N5 on G: my lane's SPEC loop (dual_check.Runner on si.py = SPEC S1, read-only).
- Ξ: my own play value. Ranks and their parities come from SPEC S1's rank and Ω.
Scope (D1): bounds top changes only. The P-changes under a fixed top (counting changes) are not bounded. Not a TARGET.md claim. G-N5-TIME stays
OPEN.

## 0. Verdicts (all "(Opus 5.5, D15)")
| § | item | verdict |
| --- | --- | --- |
| §1 | Fact DELTA | SIGN |
| §1 | Lemma TOP-SHAPE (a), (b), (c) | SIGN. It also holds at every N5 transition at which v's own cycle node is unchanged, phase or not (N-TS-1) |
| §1 | Corollary (≤ n − 1 top changes per vertex per phase) | SIGN. The same proof gives ≤ n − 1 − rank(λ(v)) (N-TS-2) |
| §1 | Reader-proofness (READING) | not signed. Follows from the Corollary being per vertex and on every game |
| §3 | TOP-MONO in its Δ form | DEAD CONFIRMED on long121_n40, vertex 0, phase [1, 122]. My Δ-tops start 35, 37, 32, 33, 26, 39, 21, 29, 33, 36, as stated. The rise count for vertex 0 is 17, not 20 (N-TS-3) |
| §2 | data | not signed. Reproduced where checked (§2 below) |
| §4 | quotes | 2/2 VERBATIM in the tagged lines (own qcheck.py; SHIFT=1 control 0/2) |
No gap. Notes N-TS-1..5.

## 1. Proof check
- Fact DELTA. weight(B) − weight(A) is a signed sum of distinct powers of two over A Δ B, and the top term 2^d exceeds the sum of all lower ones.
  The sign is s(d) or −s(d) according to the side d lies on. ✓
  - Checked: on every P-change, against the engine's weight (si.py S1 weight), and on 8,236 + 24,488 + 400 + 299,807 + 299,144 random mask pairs.
    0 failures.
- The first proof step.
  - (MON) (R15 (a), (d), every N5 iteration, fallbacks included) gives Ξ_{t+1}(v) ⊵ Ξ_t(v). The cycle node is the same, since λ is constant on
    the phase.
  - S1's order is lexicographic: reward of c, then the P-weight, then the length. So weight(P_{t+1}) ≥ weight(P_t), and it is strict when P
    changes, by (INJ).
  - ✓ Checked as INC at all 53,549 + 72,783 + 12,716 + 2,124 + 1,897 P-changes.
- (a) A higher new top u′ is the top of the symmetric difference and lies in the new set. Fact DELTA with the strict rise forces u′ even. ✓
- (b) An even old top u that disappears or is undercut would be the top of the difference, in the old set. The weight would fall. ✓
- (c), part 1. From an even top the next top is ≥ it, and any rise is even, so tops stay even and non-decreasing, and ⊥ never returns. ✓
- (c), part 2. From ⊥ the first change rises and is even. From an odd top, a rise is even, and otherwise the top stays or falls. ✓
- Checks: TSa (6,082 + 6,986 + 426 + 752 + 713 rises) and TSb (10,282 + 13,914 + 1,103 + 681 + 531 even-top P-changes). TSc (the whole
  distinct-top sequence has the shape odd-decreasing, at most one ⊥, even-increasing) is checked on every (v, phase). 0 failures.
- Corollary.
  - Every value in the distinct-top sequence is new. Odd ranks occur only in the decreasing run, even ranks only in the increasing run, and ⊥ at
    most once, between them.
  - The values are ranks above rank(c) plus ⊥: at most n − rank(c) values, at most n − 1 − rank(c) ≤ n − 1 changes. ✓
  - Checked as COR and as the sharper CORc. 0 failures.
  - Largest observed: 62 top changes at n = 581 (gate_K64_n581, vertex 573), 48 at n = 156 (ladderd0_k48_n156, vertex 50, as §2), and 10 at
    n = 48 (lib41). The ratio is at most 0.43·(n − 1) (lend9_n8).

## 2. Data (own checker; every run 0 violations)
| corpus | runs | phases | P-changes | top rises (TSa) / even-top changes (TSb) | (v, phase) with a top change | odd-then-even sequences |
| --- | --- | --- | --- | --- | --- | --- |
| alt_all (413, given start else S3; 1 start entry validated) | 413 | 458 | 53,549 | 6,082 / 10,282 | 8,516 | 3,643 |
| lib41_noref × 3 | 1,230 | 1,116 | 72,783 | 6,986 / 13,914 | 14,277 | 5,429 |
| named (box49 dressings 9, si/root 7, nep90, long121, ladderd0_k48_n156 S3, box25 sc32) | 20 | 24 | 12,716 | 426 / 1,103 | 779 | 505 |
| random kO n 8-20 / k2 n 6-16 (5,000 × 3 each) | 30,000 | 4,880 | 4,021 | 1,465 / 1,212 | 2,386 | 599 |
- Reproduced:
  - sc32 (box25, S3), vertex 0, phase [4, 48]: tops 31, 30, 29, 27, 26, 21, 20, ⊥, 25, 28, exactly as §2;
  - ladderd0_k48_n156 (given start), vertex 50: ⊥, 107, 108, …, 154, i.e. 48 top changes, an increasing even run, as §2;
  - P-changes per (v, phase) up to 72 (l121_d29) and 67 (nep92_n40). §2's "up to 71 (l121reader_n41)" is the same phenomenon.
- Controls:
  - CTL_cross: TSa / TSb fail 17,907 + 50,151 + 666 + 40,331 + 28,705 times across phase-leaving transitions, so a constant cycle node is
    needed.
  - CTL_flip: the parity-flipped (a) ("rises only to odd ranks") fails at every rise.
  - CTL_deltatop: the DEAD Δ-form fails in 4,360 of 6,124 (v, phase) sequences with ≥ 2 P-changes on alt_all.
  - CTL_counting: P-changes per (v, phase) exceed n − 1 in 23 + 3 + 32 cases. The counting changes are not bounded by the Corollary, as the
    packet says.

## 3. Notes (not gaps)
- N-TS-1 (wider than stated). The proof uses only that v's OWN cycle node is the same at t and at t + 1, and (MON), which holds at every N5
  iteration.
  - So (a) and (b) hold at every N5 transition at which λ(v) is unchanged, inside a phase or not. Checked as XSAMEC at phase-leaving
    transitions: 27,442 + 76,721 + 24 + 7,978 + 3,537 P-changes, 0 failures.
  - The Corollary then holds per vertex on every maximal run of states with λ(v) constant, which can be longer than a phase.
  - Optional for the fixes file.
- N-TS-2 (sharper count). The number of values is (ranks above rank(c)) + 1, so top changes ≤ n − 1 − rank(λ(v)). CORc: 0 failures. Cosmetic.
- N-TS-3 (§3 instance count).
  - On long121_n40 (given start), vertex 0, phase [1, 122], my Δ-top sequence has 35 entries. The first ten are as §3 states. It has 17 rises,
    not "20 rises in the phase".
  - 20 is the maximum over the vertices of that phase (vertex 6).
  - The DEAD verdict does not depend on the count: one rise after a fall kills monotonicity in both directions.
- N-TS-4 (wording: parity of a rank). "Even / odd rank" means the parity of Ω of the vertex of that rank (§0 says so), not the parity of the rank
  number.
  - §2's "tops 31, 30, 29, 27, 26, 21, 20 (all odd ranks)" reads as a contradiction without that definition at hand.
  - A short reminder in §2 would help.
- N-TS-5 (premises). The proof uses (MON), λ constant on a phase and (INJ). R38 (a) is not needed beyond the phase definition. (INJ) is just
  "distinct sets have distinct weights", which Fact DELTA itself proves.

## 4. DONE / FINDINGS / NEEDS
- DONE: this report; docs/referee-2/R2-N5-TOPSHAPE/{topshape_check.py, repro.py, named.lst, run_all.sh, logs/}.
- FINDINGS:
  - Fact DELTA, TOP-SHAPE (a)-(c) and the Corollary all SIGN, no gap. They hold more widely, whenever λ(v) is unchanged (N-TS-1), with a
    sharper count (N-TS-2).
  - §3's DEAD verdict is confirmed. Its rise count for vertex 0 is 17, not 20 (N-TS-3).
- NEEDS: Lead: the §C word; route N-TS-1..5 to L-NEW.
