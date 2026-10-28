# R-N5-OFFMONO-add: REFEREE report on the addendum P-N5-OFFMONO-add-box49 ((CYC-ID), (CYC-SHAPE), Remark Z-CONST, Corollary CHAIN-COUNT′, Lemma ZCH-COUNT; every game)
Referee: REFEREE (successor 15), Opus 5.5 (owner ruling D15). FIRST referee (Lead 17:40Z by date -u: review with P-N5-OFFMONO; my OFFMONO report is
docs/referee/R-N5-OFFMONO.md at 04a563d3, all signed, no gap).
- Object and pin: docs/new/P-N5-OFFMONO-add-box49.md, sha1 5911aba8fc4e968187523c27b4f48cdc55433b3f, 165 lines, author L-NEW successor 29: the
  same sha1 on my tree, at the l-new freeze b2a78eb1 and at trunk 8bfe4150 (an ancestor of HEAD).
- Written 2026-10-26T17:51Z-17:56Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/ file on OFFMONO on my tree, on trunk or on origin/claude/referee-2 (0 / 0 / 0 at 17:55Z,
  re-listed in the same turn as the fetch). No lane code run (experiments/new/box48/zch.py, quotecheck2.py neither executed nor imported). D1.
- Quotes: §8's 12 curly quotes verbatim (11 at 366fd235 in RESULTS.md, P-N5-FBPOLY, P-N5-FBRED, P-N5-OFFMONO; 1 at 331f0337 in N5-KPOLY-box49.md),
  and §5's 3 KPOLY quotes verbatim at 331f0337 (my scripts; whitespace normalised).
- Tool: scratch/zch_probe.py (own engine; offmono_probe's κ / par helpers; checks in §3). Logs scratch/zch_logs/.

## Verdicts (sign-off line per item)
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §0 | Fact (CYC-ID) | SIGNED |
| §0 | Fact (CYC-SHAPE) | SIGNED |
| §1 | Remark Z-CONST | SIGNED |
| §2 | Corollary CHAIN-COUNT′, Step A, sum form and stated form | SIGNED (a REDUCTION: EXIT_x and the offset counts v_x / D unbounded here) |
| §2 | Remarks (i)-(iii) | (ii), (iii) CHECKED; (i) CHECKED with note OFFADD-N1 (the implication goes through the sum form) |
| §3 | Lemma ZCH-COUNT (with its finer statements) and its Corollary \|ZC_c\| ≤ \|ZCH_c\| ≤ (n − 1)\|U_c\| + TIE_c + ODDC_c | SIGNED (a REDUCTION in TIE_c, ODDC_c, as the packet says) |
| §4-§7 | data, differences from KPOLY §8, open, reading | not signed (as briefed); §5's three statements about KPOLY §8 CHECKED against its text |
These signatures rest on P-N5-OFFMONO's OFFSET-MONO and CHAIN-SUM, which I signed (R-N5-OFFMONO, 04a563d3); REFEREE-2's review of both is
pending. No gap. Notes OFFADD-N1..N2. Nothing here bounds EXIT_x, TIE_c, ODDC_c or D; no running-time bound; not a TARGET.md claim; G-N5-TIME
stays OPEN.

## 1. Re-derivation (parentheticals checked one by one)
- (CYC-ID) ✓: next_t is a function, so x lies on at most one next_t-cycle, the end of its play; its play's cycle node is λ(x) = c, on that cycle;
  the cycle through c is Z_t(c) ✓.
- (CYC-SHAPE) ✓: c is the top of its own honest cycle "(P-N5-FBPOLY §0.3's (A0κ) proof)" ✓, so every other vertex of Z_t(c) has rank < rank(c),
  wt_c = 0; (Aκ) iterated with (A0κ) gives (0, s_c·ℓ), 1 ≤ ℓ ≤ n − 1 ✓.
- Z-CONST ✓: equal sequences give equal next on the cycle "(the sequence lists each vertex followed by its successor)" ✓; κ is a function of the
  walk (cycle node c at both times by R38 (a)) ✓; par is the first vertex of Q ∖ {x} on the same walk before c ✓; p on the cycle or p = c, so κ(p)
  unchanged ✓.
- CHAIN-COUNT′ ✓. Step A: off the honest cycle at t, OFFSET-MONO; on it, the transition is in CYC_c, so (not in ZC_c) not in ZCH_c, and Z-CONST
  gives equality with par_t(x) = par_{t+1}(x) ✓. Main proof: outside ZC_c, CHAIN-SUM with Step A at every level (including levels on c's cycle,
  which CHAIN-SUM alone leaves unsigned) ✓; a strictly positive term is charged to (x, t), in EXIT_x or as a strict rise on an x-piece′ where
  off(x; p) is non-decreasing (Step A, p fixed) ✓; distinct transitions, distinct charges ✓; the piece count and the D-form arithmetic ✓.
- The Lead's question, "the ZC cut is argued from the proof only": the argument is sound. Step A covers exactly the transitions outside ZC_c (by
  OFFSET-MONO or Z-CONST), and nothing covers a level on c's cycle at a transition where the cycle changes, so the proof must cut there; cutting
  more never breaks a count of this form. Whether the cut is NECESSARY is a different question, and the data say no so far: at every ZC
  transition with a level x on c's cycle at t, I checked off_{t+1}(x; par_{t+1} x) ⪰ off_t(x; ·) directly: 806 (library n ≤ 40) + 565 (random)
  checks, 0 falls (§3). Together with OFFMONO-N4 (OFFSET-MONO held at all 4,006 levels on an honest cycle at t), this suggests a CONJECTURE that
  OFFSET-MONO holds for every q ∈ Q ∩ U ∖ {c}, which would make the cut, and the CYC term, unnecessary. Not proved (OFFADD-N2).
- ZCH-COUNT ✓. The partition ✓ (N = ∅ forces next(c) to change, else Z_t(c) = Z_{t+1}(c) by tracing from c) ✓; ODDC ⇒ c ∈ Q and σ̄(c) changed ✓.
  STRICT: the charged vertex's new value is (0, s_c·ℓ), ℓ ∈ [1, n − 1] (CYC-SHAPE at t + 1) and κ(v) is non-decreasing on P (M2κ), so distinct
  strict rises of κ(v) have distinct targets: ≤ n − 1 charges per v ✓, v ∈ U_c ∖ {c} ✓. Every Even v ∈ N strictly rises ((SW), M1κ, Aκ, M2κ)
  ✓, so a TIE's N is Odd with κ unchanged ✓. CEVEN: ψ_s ∈ {(0, s_c·ℓ) : 0 ≤ ℓ ≤ n − 1} ✓, non-decreasing for Even c (M2κ, or a switch through
  Iσ_t) ✓, strict at every CEVEN transition ✓: ≤ n − 1 ✓. Sum ✓.
- §5 (not signed) checked against KPOLY §8 at 331f0337: the three quoted KPOLY sentences are verbatim; the stated differences (cut set, TIE's
  N ≠ ∅, the bound one smaller) are accurate.

## 2. Notes (none blocks a signature)
- OFFADD-N1 (Remark (i)). "CHAIN-COUNT′ implies P-N5-OFFMONO's CHAIN-COUNT" holds through the SUM form: under CHAIN-COUNT's hypothesis (≤ D values
  on every x-piece), an x-piece′ is a union of x-pieces glued at CYC ∖ ZC transitions, so Σ_{π′}(v_x(π′) − 1) ≤ (D − 1)(#x-pieces) + |CYC_c ∖ ZC_c|,
  and the sum form then gives CHAIN-COUNT's bound. The STATED form alone does not, since its D is asked on the longer pieces′; the packet says
  so ("the hypothesis … is then asked on longer pieces"), and one line naming the sum form would close it.
- OFFADD-N2 (CONJECTURE candidate). OFFSET-MONO for q on an honest cycle at t: 0 failures in 4,006 + 1,371 checks (OFFMONO-N4 and §1 above). If
  proved, CHAIN-COUNT holds with no CYC term at all.

## 3. Data (own engine; DATA, not proof; 0 failures of every signed check)
Checks: CID, CSH (every state, every class), ZC (Z-CONST at every transition with an unchanged cycle), SA (Step A at every transition outside
ZC_c, every x ∈ Q ∩ U ∖ {c}), PM (off(x; p) non-decreasing on every x-piece′), CCP (both forms, D := the actual max v_x), ZK (the four kinds, TIE / ODDC
facts, STRICT charges ≤ n − 1, CEVEN ≤ n − 1, ψ non-decreasing for Even c, the |ZCH_c| bound), ZCF (the cut question, counted).
| sample | runs | CID / CSH | Z-CONST | Step A | CHAIN-COUNT′ (max D) | ZCH: STRICT / TIE / CEVEN / ODDC | Σ CYC / ZCH / ZC | ZCF (offset falls at ZC, cycle levels) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| scratch/fbc_lib.txt, n ≤ 40 (870 files), S3 + 2 random | 2,610 | 521,530 / 19,381 | 29,793 | 33,309 | 9,024 (61) | 183 / 8 / 291 / 5 | 1,434 / 487 / 257 | 806 (0) |
| random 3,000 games (n 6-22, ≤ 8 Odd choice vertices, seed 651), S3 + 4 random | 15,000 | 126,182 / 17,811 | 11,601 | 7,966 | 8,506 (3) | 331 / 8 / 952 / 13 | 1,074 / 1,304 / 377 | 565 (0) |
- Mutations (n ≤ 40 library): MUT=1 (pieces′ not cut at ZC_c): 0 failures — does not bite, as the lane reports (§1: the cut is a proof device);
  MUT=2 (opposite length sign): Step A 1,271, PM 394, ψ 430, TIE 183 failures; MUT=3 (pieces′ not cut at EXIT_x): PM 422 failures.
- TIE_c and ODDC_c are rare (8 / 5 and 8 / 13 in the two samples), as in the packet's data.

## §C
The §C for this file is the UNIT §C at the end of docs/referee/R-N5-OFFMONO.md (OFFMONO + add1 + add2 + add3 against REFEREE-2 4e9a6372),
written 2026-10-28 by REFEREE successor 16: identical verdicts, joint gap map empty.
