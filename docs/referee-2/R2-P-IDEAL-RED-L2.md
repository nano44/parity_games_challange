# R2-P-IDEAL-RED-L2: REFEREE-2 word-diff of P-IDEAL-RED line L-2 against L-1, and match against packet + fixes
Referee: REFEREE-2 successor 26, Opus 5.5 (D15). Written 2026-11-04 (date -u; see the commit). Verdict: **MATCHES**.

## 0. Object
- Commit: claude/l-new ffeb973670db02b59e6c89f406481979fc94121c, an ancestor of origin/claude/l-new. I re-hashed every file at that commit:

| file | sha1 | lines | check |
| --- | --- | --- | --- |
| docs/new/P-IDEAL-RED.md | 06f2c18609e355a1e62c138c420bd49dc401cae4 | 261 | unchanged ✓ |
| docs/new/P-IDEAL-RED-line-L1.txt | 44d0287a5d304aa5342b8cd98c6cbccb9e8af6b3 | 1 | unchanged ✓ |
| docs/new/P-IDEAL-RED-line-L2.txt | 65ba7ca7fd6d4cb6b0de1d1c918ec181ff78fbe5 | 1, no «\|» | = Lead ✓ |
| docs/new/P-IDEAL-RED-fixes.md (entries 1-2) | 2e8c3630b16cf6cd33564433da62c0fbba1f1f4e | 83 | = Lead ✓ |

- The fixes file is append-only: `git diff b115ff3a ffeb9736` shows 0 deleted lines, and 15 added lines (entry 2).

## 1. Word-diff L-1 → L-2
- Method: difflib opcodes on space-split tokens (10 hunks), then a byte test. L-1 with exactly the 9 replacements below, each old phrase
  occurring once, equals L-2: **True**. L-R1 makes 2 of the 10 hunks.

| # | change | item | ✓ |
| --- | --- | --- | --- |
| 1 | «(L-RED R178» → «(the model first stated in L-RED R178» | optional 6 (R178 not a source) | ✓ |
| 2 | ENC: «so» → «so, with ε(x, k) := ±2^rank(x, k) (+ for even parity),» … «Ξ-target;» → «Ξ-target (ε(x, k) alone if the Ξ-target is the exit X);» | REQUIRED L-R1 = REFEREE L-1a | ✓ verbatim as I asked |
| 3 | XI-NEW: «A_(s_(t−2))(h);» → «A_(s_(t−2))(h) (A_s(h): h's current option under s and its options strictly better under s);» | REQUIRED L-R2 = REFEREE L-1b | ✓ («current» added: better than my wording; = §0's A_s) |
| 4 | RISE: + «under s_(t−2)» | optional 5 = my O-1 | ✓ |
| 5 | CHAIN-BACK: «unchained steps;» → «unchained steps t ∈ [2, T];» | REQUIRED REFEREE L-1d (I concur) | ✓ |
| 6 | TOP-MONO: + «(padded with −1 to length k)» | optional 7 | ✓ (= packet §7 definition) |
| 7 | RANK-BOUND: + «for k ≥ 1,» and «steps;» → «steps (R := 0 if U = 0);» | optional 8 | ✓ (= packet §7 and fixes F-3 P-1) |
| 8 | INTERVAL-RESTRICT: «labels agree there;» → «labels agree from the interval's third state on (step a + j of the run against step j of the restricted run, for j ≥ 2);» | REQUIRED L-R3 = REFEREE L-1e | ✓ verbatim as I asked |

- So L-2 = L-1 + the four REQUIRED changes (L-R1, L-R2, REFEREE L-1d, L-R3) + the optional items 5-8, and nothing else.
- Entry 2's own hunk list (fixes l. 72-83) agrees with mine, hunk for hunk.

## 2. Match of L-2 against the packet + fixes (entries 1-2)
- Every clause of L-1 was already matched to a signed statement with its hypotheses (R2-P-IDEAL-RED-L1.md §2). The edits only add bindings
  and scope that the packet states:
  - ε as in ENC;
  - A_s as in §0;
  - U over [2, T] as in §4's definition;
  - labels for a + 2 ≤ t < b as in INTERVAL-RESTRICT (iii);
  - TOP_k padding as in §7;
  - R := 0 as in §7 and F-3 P-1.
- The hypotheses are unchanged and correct: acyclic Ξ-graphs throughout; degree ≤ 2 exactly for KEYFLIP / KF-EQ, TOP-MONO, RANK-BOUND,
  INTERVAL-RESTRICT, INTERVAL-CHARGE and RECURSION.
- Nothing unsigned appears. F-2's remark (all-option monotonicity) is absent. The degree ≥ 3 failures appear only as «(DATA, REFEREE-2
  N-2)».
- Premise: «R104's definition of the model only, no theorem of R104 used» ✓.
- Label: «a REDUCTION / EQUIVALENCE statement inside the IDEAL model; bounds nothing polynomially» ✓.
- Tail: G-N5-TIME OPEN; not M3, not a step-4 pass, not a TARGET.md claim ✓.
- DATA (46 corpus genomes; 75,518 all-start runs) ✓, reproduced in R2-P-IDEAL-RED §4.
- Source: «with its fixes entry 1» names entry 1 only. Entry 2 holds just this line's word diff, so nothing in the packet's reading
  changes. That is acceptable. Optional: «fixes entries 1-2».

## Verdict
**MATCHES.**
- L-2 (65ba7ca7) = L-1 + exactly the four required changes + the optional items 5-8 (byte test True).
- It matches the packet read with fixes entries 1-2. Every clause is a signed statement with its exact hypotheses.

## DONE / FINDINGS / NEEDS
- DONE: re-hash; word-diff and byte test; clause match.
- FINDINGS:
  - L-2 MATCHES.
  - I concur with REFEREE L-1d, which I had missed in L-1 (unbound range of U).
- NEEDS: none. Optional: «fixes entries 1-2» in the source note.
