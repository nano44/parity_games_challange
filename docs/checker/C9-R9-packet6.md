# C9: landing gate for RESULTS R9 (packet 6: per-context budgets, GAP-A ⇐ (CTX⁺) ∧ (FALL)) — CHECKER, 2026-10-17

Target: docs/agents/R9-draft.md at trunk f3cde82 (not edited). Branch: origin/claude/checker confirmed an ancestor of the
local branch, then trunk f3cde82 merged by merge commit.
Sources (all ancestors of f3cde82):
- GAP-A-M.md §22f (line 2049) and §22j (line 2213) at the pin 8ff4085.
- docs/referee/R-P6.md: 9f77ff9 (13:14:59Z), 0c0e3ce (13:17:16Z, "Written" time corrected, nothing else changed), and §C
  at ad4be01 (13:22:33Z, +31 lines).
- docs/referee-2/R2-P6.md: 5ef09aa (12:54:31Z) and §5 at c7634a7 (13:22:37Z, +19 lines).
- Code: Oink 8fbf0a7.

## Verdict: PASS (no required fix; recommended N-1..N-5; notes N-6..N-8)
| check | verdict |
| --- | --- |
| 1 statement diff (a)-(d) and the five named points | PASS (N-1, N-2) |
| 2 verdict quotes and independence | PASS (N-3 labels, N-8) |
| 3 gap union; fall3_n76 | PASS (N-4, N-5); fall3_n76 re-run by CHECKER, reproduced |
| 4 re-run, REFEREE p6probe.py @ 9f77ff9, all 138 instances, both orders | PASS: identical to R-P6's table |

## 1. Statement diff
| draft | §22f/§22j at 8ff4085 | signed | |
| --- | --- | --- | --- |
| (a) Π_R is a function of (R, p, T); T grows; clean later visits never lower Π_R; e*-at-R transitions ≤ (F_R + 1)(H + 1), F_R counting "EVERY transition at R where Π_R does not rise (descents, incomparable steps, and Π-blind e* transitions)" | §22f: "F_R, the number of descents of Π_R along the phase" | REFEREE A1-A4 + G6-a1: "F_R := #(visit pairs of R at which Π_R neither stays equal nor rises strictly) + #(e*-transitions at R with Π_R equal)"; REFEREE-2 G-F1: "F_R := #descents of Π_R along the phase + #e*-at-R transitions at which Π_R does not rise"; §5 "F_R must count every non-rise" | OK. The corrected F_R is used, not §22f's. N-1 on "no str read" |
| (b) per-input chain ≤ n; −1 input a function of (R, X) (898-912); Dom input (X ∪ Dom_{<j}, R \ Dom_{<j}, τ_j, pr τ_j), "depends on T and is NOT fixed by (R, X)"; Dom output "the closure triggered by the new part, with only the top pushed" | §22j "Per-input budget (PROVED, reading)" with input (caller, Z_in, R, Gx, maxpr) | REFEREE G6-b1, G6-b2 (input text verbatim); REFEREE-2 R-I and §5 ("It is NOT determined by the piece's (R, X) alone") | OK |
| (c) S − 1 ≤ Σ_{R∈C_bv} (F_R + 1)(H + 1) + n·(\|C_T\| + \|C_Dom\|) + 1; C_Dom = distinct Dom INPUTS; GAP-A ⇐ (CTX⁺) ∧ (FALL); (DOM-e*) no longer needed | §22j display (identical, with +1); §22j's (CTX⁺) says "contexts of ... Dom steps" | REFEREE (b) display, G6-b2 "should say 'distinct first-difference inputs of Dom steps'"; REFEREE-2 (b) "is correct", "(DOM-e*) is no longer needed" | OK. The bound is identical, including the +1. Inputs, not contexts, as both referees require |
| (d) the raw per-input bound is vacuous: DATA, motivation only | §22j vacuity paragraph | both (c) SIGN, "stated as DATA" | OK |

The Lead's named points:
- F_R counts EVERY non-rise (G6-a1 / G-F1): yes. The parenthesis lists all three kinds that REFEREE G6-a1 names.
  - "at R" follows REFEREE's indexing by visits. REFEREE-2 indexes Π_R(T_s) over every s of the phase. §C says "Both chain
    arguments are valid and give the same bound". No change needed (N-6).
- The Dom input is NOT fixed by (R, X), and |C_Dom| counts inputs: yes, in (b) and in (c) ("C_Dom the distinct Dom INPUTS").
- (DOM-e*) is absorbed: yes. (c): "no longer needed (absorbed into |C_Dom|)". REFEREE: "It removes the hypothesis
  (e* ∉ Dom), as §22j says". REFEREE-2: "is no longer needed".
- The bound includes the +1: yes.
- REFEREE's (b) quoted as SIGN after §C: correct. §C says "I accept R2's verdict SIGN for (b) once §22j's (CTX⁺) wording
  says 'inputs' for Dom (my G6-b2 wording item). The substance stays OPEN in both reports, inside (CTX⁺)". The draft says
  "revised in the comparison §C (ad4be01) to SIGN once (CTX⁺) says 'inputs' for Dom, as (c) here does". This is exact, and
  (c) does say "inputs".
- N-1 (recommended). (a) says "(no X, str or W read)". REFEREE A1: best_vertices reads "str only at 73, where the value
  decides a str write and nothing else". R7 G-R7-7 words the same fact as "no set test reads str". Suggest "(no X or W
  read; str only at 73, deciding a str write only)".
- N-2 (recommended). REFEREE G6-b2's wording item (§22j's "(CTX⁺) counting the distinct first-difference contexts of ... Dom
  steps" must say "inputs") is closed in the reports and is to be imported into §22j. G-R9-1..3 list the imports, but this
  one is listed only implicitly under G-R9-4 (OPEN). Suggest adding to G-R9-3 or G-R9-4: "§22j's (CTX⁺) wording 'contexts'
  → 'inputs' for Dom (REFEREE G6-b2, closed as wording)".

## 2. Verdict quotes and independence: PASS
- REFEREE table: (a) SIGN WITH GAPS (G6-a1, G6-a2 closed); (b) SIGN WITH GAPS (G6-b1 closed; G6-b2 wording closed,
  substance OPEN inside (CTX⁺)), and SIGN per §C; (c) SIGN. This equals the draft.
- REFEREE-2 table: (a) SIGN WITH GAPS (G-F1); (b) SIGN, reading R-I; (c) SIGN. §5 clarifies R-I: "the input is equal in s and
  s+1 at a first difference ... NOT determined by the piece's (R, X) alone". The draft's "'fixed' means equal in s and s+1
  at a first difference, not determined by (R, X)" matches.
- Independence:
  - REFEREE: "docs/referee-2/R2-P6.md was not read"; §C "read after R-P6 was pushed and merged".
  - REFEREE-2: "docs/referee/R-P6.md was not read before this report was pushed"; §5 read 9f77ff9 "after 5ef09aa was
    pushed".
  - No REJECT.
- N-3 (recommended, labels). The reports label their items (a) §22f, (b) §22j chain + bound + GAP-A ⇐ (CTX⁺) ∧ (FALL), and
  (c) the vacuity remark. The draft's claims split the reports' (b) into (b) chain and (c) bound, so the reports' (c) is the
  draft's (d). The Signatures line uses the reports' labels: "(c) SIGN" there is the draft's (d). The draft's (c) is signed
  inside the reports' (b) (and (a) for its F_R term). Suggest the line R6 used: "Labels here differ from the reports:
  R9 (b)+(c) = reports' (b), R9 (d) = reports' (c)".
- N-8 (label). R2-P6's header says "12:58Z (date -u)", but 5ef09aa is committed at 12:54:31Z. This is the same pattern as
  C8 N-6, a stamp mismatch only. Ordering against REFEREE (9f77ff9, 13:14:59Z) is unaffected.

## 3. Gap union
| referee item | draft |
| --- | --- |
| REFEREE G6-a1 = REFEREE-2 G-F1 | G-R9-1 |
| REFEREE G6-a2 = REFEREE-2 "the Dom term is item (b)" + G-e2 +1 (§5) | G-R9-2 |
| REFEREE G6-b1 = REFEREE-2 R-I (first half) | G-R9-3 |
| REFEREE G6-b2 = REFEREE-2 §5 (inputs, not contexts); probe 105/2,110 and 111/2,166 | G-R9-4 (N-2 on the wording import) |
| both: (CTX⁺) OPEN, nested-counter core, monotone removal prefixes FALSE (spp_final_n20) | G-R9-4; Scope |
| both: "descends only where RV falls", "≤ 2 per context per phase" DATA only; REFEREE-2 "whether a dirty call can descend through Ψ or Φ_top with RV fixed is not proved" | G-R9-5 |
| REFEREE open item 3: phases ≤ D + 2; bit cost conditional on DTL-proof §3(e) (REFEREE-2 counts it done, R2-P4 (f); §C: "not a disagreement") | G-R9-6 |
| GAP-C separate | Scope |
| REFEREE-2: §22j "Where a Dom e* would come from" is a sketch, not signed | not claimed by the draft. OK |
| REFEREE "inherited nit": H's factor (d + 2) counts distinct threshold levels; the code loops t = 0..max_prio (721-722); "Still polynomial" | not carried (N-5) |
| REFEREE: "No monotone repair at fixed (R, X)": the triggered closure is not monotone in its base (reading, no instance) | not carried; optional in G-R9-4 |
- "Closed" applies only to G-R9-1..3; G-R9-4..5 are OPEN; G-R9-6 lists dependencies. Correct.
- N-4 (recommended, a data citation in G-R9-1). "0 such non-descent non-rises after L-ALG's G-Ψ tool fix (one apparent case
  on cross union 411 was a tool artifact, corrected)". The source is not on trunk. It is the [CORRECTION 13:13Z] bracket in
  §22h at l-alg e9acfb8 (not an ancestor of f3cde82). That bracket says the full re-run with the fixed tool is still to
  come ("Full re-run with the fixed tool: §22n"), and §22n does not exist at e9acfb8. The claim is supported for the
  corpus, the mixed unions and the stable cross unions ("had no length mismatch", so the old counts stand) and for union411
  (re-classified "Π rises (Ψ)"). Suggest "(l-alg e9acfb8 §22h correction; full re-run with the fixed tool pending)".
- N-5 (recommended). Carry REFEREE's inherited nit on H, one line in G-R9-6: "H's (d + 2) factor counts distinct threshold
  levels; the code loops t = 0..max_prio (721-722); still polynomial (REFEREE (a))". It affects R7 (d)'s H as written, not
  its polynomiality.

### G-R9-5 and fall3_n76 (the Lead's question)
- Source: L-RED docs/red/R31-fall3.md at l-red 065ba24, "Status: DATA, unrefereed". Neither the instance nor the report is
  on trunk (065ba24 is not an ancestor of f3cde82).
- CHECKER re-run (this gate):
  - Instance: experiments/red/carry/instances/fall3_n76.pg from 065ba24, sha1 a85133ec886b05beea2582e4a50885eb3795a243,
    as R31 states.
  - Pinned Oink 8fbf0a7 `--dtl --no-single --no-wcwc --no-loops -v`: "found 3 dominions and 56 tangles", "solved in 10
    iterations", "solution verified (35 strategies)".
  - experiments/alg/dtl_rootmono.py at trunk (identical to l-alg c8df405, which R31 used), DTL_ORDER=oink and =stable:
    "descents of Π_R per context (file, max per context, total, transitions, |G'|): (fall3_n76, 3, 3, 5, 76) phases: 1".
    There are three "FALL with only old witnesses" lines, visits 1→2, 2→3, 3→4, witnesses [6, 12, 14]; k0 20/25/31 (Oink)
    and 21/26/32 (stable), as R31 states.
  - No "DOES NOT RISE", "Ψ NOT monotone" or INCOMPLETE line.
- Ruling: acceptable to keep, with two changes.
  - Replace "Lead re-run pending" with "re-run CHECKER C9".
  - Cite "L-RED R31, l-red 065ba24, DATA, unrefereed".
  - It weakens nothing signed: "≤ 2 per context" was never signed (both referees: DATA only), and the draft already says
    "does not refute (FALL)".
  - If the Lead prefers not to cite off-trunk data in a landed result, drop the clause. Then "≤ 2" must still not be stated
    as a bound anywhere in R9, and it is not.

## 4. Re-run: REFEREE docs/referee/scratch/p6probe.py @ 9f77ff9
- p6probe.py and experiments/alg/dtl_pyref.py are identical at 9f77ff9 and at the checker HEAD.
- Run: the 138 instances of experiments/alg/instances, `p6probe.py stable` and `p6probe.py oink`, exit 0. No MONO FAIL,
  INPUT DIFFERS, NOT STRICT, CHAIN FAIL or ERR line.
  | | stable | oink | R-P6 table |
  | --- | --- | --- | --- |
  | transitions | 578 | 609 | 578 / 609 |
  | e* caller bv / −1 / Dom | 555 / 23 / 0 | 586 / 23 / 0 | 555/23/0, 586/23/0 |
  | longest per-input e* chain | 3 | 3 | 3 |
  | Dom input varies at fixed (R, X, top) | 105 / 2,110 | 111 / 2,166 | same |
  | max Dom inputs per (R, X, top) | 4 | 4 | "up to 4" |
- Identical.

## Notes
- N-6. F_R indexing: see §1 (visits vs all s). Both are valid per §C.
- N-7. G-R9-4's "(first-difference contexts ≤ 10 per phase on the SPP families)" and "(CHAIN) is FALSE (DE16)" are after the
  pin.
  - The first is GAP-A-M §22m line 2304 at f3cde82 ("at most 10 per phase (spp25_oink_n40)").
  - The second is RESULTS DE16.
  - Both are on trunk and DATA only. Not part of the signed content.

## Fix list (none required)
Recommended:
- N-1: "no str read" wording.
- N-2: §22j "contexts" → "inputs" import.
- N-3: label mapping.
- N-4: union411 source and pending re-run.
- N-5: H nit.
- fall3_n76: re-run done by CHECKER; cite R31 / 065ba24.
The draft may land as written. If edited, I re-diff the text only.

## Addendum: text re-diff at trunk b55c144 (Lead 13:42Z): PASS
History: f3cde82 is an ancestor of b55c144. Trunk b55c144 was merged into claude/checker by merge commit.
- R9-draft.md, f3cde82 → b55c144: only G-R9-5 changed (1 line → 3 lines). The new text is "by L-RED fall3_n76
  (experiments/red/carry/instances/fall3_n76.pg, sha1 a85133ec, docs/red/R31-fall3.md: 3 descents at one context, both
  orders; Lead re-ran pinned Oink (10 iterations, verified) and dtl_rootmono.py (max 3 per context, both orders)), which
  does not refute (FALL)". Nothing else moved.
- The source is now on trunk: l-red 065ba24 is an ancestor of b55c144. experiments/red/carry/instances/fall3_n76.pg at
  b55c144 has sha1 a85133ec886b05beea2582e4a50885eb3795a243, and docs/red/R31-fall3.md is present.
- The claim is reproduced twice:
  - §3 of this report: pinned Oink, 3 dominions, 56 tangles, 10 iterations, verified; dtl_rootmono.py at c8df405.
  - Again at b55c144 with the trunk dtl_rootmono.py, which now carries the G-Ψ convention (l-alg e9acfb8), both orders:
    "(fall3_n76.pg, 3, 3, 5, 76) phases: 1", with three "FALL with only old witnesses" lines.
- "max 3 per context" is accurate. The citation is resolved (my FINDING on fall3 is met). Optional: add "DATA,
  unrefereed" after the R31 citation, as R31's own Status line says. G-R9-5 is already headed "DATA only".
- N-4 update: e9acfb8 is now on trunk, and GAP-A-M §22n (line 2331, 13:36Z) gives the full re-run with the G-Ψ convention.
  "Π_R does not rise" at e* is 0/0 on every set, including cross unions 3,370/3,377, and union411 is confirmed as a tool
  artifact. G-R9-1's data sentence is now backed on trunk. Suggest citing "GAP-A-M §22n" instead of the pending wording;
  the citation is optional.
- N-1, N-2, N-3 and N-5 are not applied. They remain recommended, not required.
