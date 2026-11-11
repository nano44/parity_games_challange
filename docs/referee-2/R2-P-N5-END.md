# R2-P-N5-END: second-referee report on packet P-N5-END (L-NEW successors 63 / 64, box 195)
REFEREE-2 successor 34 (Opus 5.5, D1). Written 2026-11-08 by date -u (times in the commit). Independent: docs/referee/R-P-N5-END.md
(REFEREE 29) NOT read before this report is committed. L-RED 58 R223 (claude/l-red 143f0b4c) and L-RED 57 R222 are context only; I did
not read them and used only what the fixes file quotes from them. Disclosure: the fixes file (entry 2) and line L-2 quote REFEREE 29's
verdicts in outline («every row SIGN», EN-1..EN-4, LN-1..LN-8, «F = 1 on 382 of 382»). I read those quotes as part of the object; my
verdicts below rest on my own derivations and my own engine.

## Object (claude/l-new, FROZEN at 131b4c1c)
- Packet docs/new/P-N5-END.md at 131b4c1c: sha1 5cae845b1da1a1c40b52e73da6edae3d6aadbf29, 22,967 B, 228 lines (= the brief); byte-identical
  at 2fcee038.
- Fixes: docs/new/P-N5-END-fixes.md, entry 1 at a60733b8 (W-1, T-1), entry 2 at 2fcee038 (EN-1..EN-4, line L-2). 131b4c1c → a60733b8 →
  2fcee038 is an ancestor chain.
- Line L-2 at 2fcee038: docs/new/P-N5-END-line-L2.txt, sha1 e8a8ac51cc79c9de4000749899e7f0b860eeebe5, 6,988 B (= the brief). L-1
  (68a69176…, a60733b8) is superseded and not reviewed as a line.
  - The lane's generator mkl2_195.py, run on a git archive of 2fcee038 with L-1 as input, rebuilds L-2 byte-equal
    («R1-R16 old once each, applied; sha1 e8a8ac51… 6988 bytes; parens 101 101»).
- Pins: experiments/new/box195/end.pins has 41 rows. All 41 sha1 match on a git archive of 2fcee038 (the check.sh «P-N5-END» block's sed).
  The lane's check195.sh, re-run on that archive, gives output byte-equal to the pinned check195.out (exit 0; Machine checks).

## Verdicts (Opus 5.5, D1)
| statement | verdict | note |
| --- | --- | --- |
| Lemma E0 | SIGN | under 1E-N3 (W-1, fixes entry 1), as every row |
| Lemma E1 | SIGN | its Corollary holds before the first fallback only (L-R1) |
| Lemma E2 | SIGN | |
| Lemma E3 | SIGN | |
| Lemma E4 (a), (b) | SIGN | |
| Lemma TERM-XI | SIGN | |
| Theorem ENDGAME-3 | SIGN | |
| Theorem ENDGAME-3-N5 | SIGN | holds for every pointwise-optimal S4a rule (EN-2): my n5w data |
| Corollary EXACT-L | SIGN | G ∈ IDEAL-ACYC; premise R117 (f); holds under SPEC's S1 tie-breaks (EN-1), FALSE for another pointwise-optimal S4a rule (my n5w data) |
| Corollary END-T3 | SIGN as PROVED-CONDITIONAL | on REACH3-CYC (R118 (k), itself PROVED-CONDITIONAL on [REACH-L]) |
| Line L-2 | NOT YET | one REQUIRED change (L-R1: E1's «changes only at a fallback» is false as written once E3 / E4 run); notes N-1, N-2 optional |

No statement is REFUSED. No statement has a mathematical gap. The one required change is to the line's wording of E1's consequence.

## Premises (own script R2-P-N5-END/r2q.py, out r2q.out)
- Every «…» of the packet (whole text) and of L-2: 53 quotes.
  - 44 premise quotes are verbatim (whitespace-normalised) in TRUNK a1decf9a0. The sources are docs/RESULTS.md, docs/new/N5-ssi-global.md,
    docs/new/P-N5-XICYC.md, docs/new/P-N5-REACH.md and docs/red/P-N5-REALIZE.md. Every source is read by `git show`, not from a working tree.
  - The other 9 are self-quotes or labels: the Lead's freeze words, «pe at every gate, K2 → K2», «one fallback, 3 iterations from it»,
    ctrl1, ctrl2, the two check.sh block names, and W-1's sentence. W-1's sentence is verbatim in fixes entry 1. Missing: 0.
- Attribution, by entry (my script, every RESULTS «### R» block):
  - [REACH3] «Let G ∈ IDEAL-ACYC with IDEAL run …» and «transitions 1, …, L are FL transitions; transition L + 1 is a fallback» are
    in R117, item (f) Theorem REACH3 [IDEAL-ACYC]. R104 also quotes them.
  - [R3C] «visits only standard states … at iteration T3 + 1», «CONDITIONAL on P-N5-REACH's S3-START, PAD, K3, TAU3, ESC3, W3 for
    every genome» and «RESULTS R117's entry signs S3-START, PAD, K3 and TAU3 for every genome» are in R118.
  - [TERM] (a) and (c) are in R15. [1E-N3] «used in two forms: …» is in R104 (and R118). [N5XI] «with ONE change in S4a» is in R118.
    The S4a rule is in P-N5-XICYC l. 45-47.
- L-2's unquoted gloss «of these RESULTS R117 signs S3-START, PAD, K3 and TAU3 for every genome but ESC3 and W3 for acyclic Ξ-graphs
  only» is what R117 (c), (d), (e) say: «(e) The transfer lemmas … [IDEAL-ACYC; K3 and TAU3 every genome]».
  - R118 adds that R117's LINE states S3-START and PAD for acyclic Ξ-graphs only. The packet does not need S3-START from R117: its (S)
    re-derives the start from FIX 1, and I checked that by hand (pA, s, K2; xt over pb_g; pe_g over pβ_g; K2's loop over r).
- [OPT] = [1E-N3] for SPEC runs: right. σ̄ and S4a's σ_new here are the outputs of SPEC's S1 procedure inside SPEC runs, which is
  exactly what R57 (b) as landed in R104 covers. R118 (b)'s IDEAL-CYC σ̄_t is not used. W-1 (fixes entry 1) puts 1E-N3 on every row.
  I agree; the proofs use it in E0 (τ̄), (H), E1, E4 and TERM-XI.

## Re-derivation (every step redone by hand; values (c, P, ℓ) in the SPEC order)
- (R), (C), (S), (W): checked against [DEF] and [G3].
  - The core is closed: K3's only in-edge is K0's via pA, and u = K0 is entered only by the pb_g pads.
  - (W)'s length 5ℓ + 3 = 3 (g, pe, e) + 5 per level (mover, m, gate, pe, e).
  - No e and no pad lies above c_W, so P = ∅.
- (H): right as stated and as worded by EN-4.
  - When the cycle node of W*(v) is not v, a pointwise-optimal σ_new gives W*(v) = v ⊕ W*(σ_new(v)), so σ_new(v) ∈ TIE(v).
  - For N5′-xi the rule picks inside TIE(v) by definition.
  - Every vertex at which E1, E3 and E4 use (H) (K0; K1; β_g and K3) is shown not to be its own cycle node.
- E0: Iτ is a function of τ alone, because τ̄ is a pointwise optimum (1E-N3) and pointwise-optimal values are unique. TAU3 gives Iτ = ∅
  at τ0. S4b needs Iτ ≠ ∅, and S4c touches τ only when Iσ = ∅ (S4c text and FIX 3). Right.
- E1 (κ0):
  - σ̄(K2) = r: node K1 versus K2, and −p'(K1) < −p'(K2).
  - The eight core values are right.
  - Improving edges: K0's edge (K1 over pA: P differs by the odd K3) improves. K1's q is worse (the top of {K0, K3} is K3, odd). K3: node
    odd, so the longer path is better and K2 stays.
  - H: via pA the node is K2, via K1 it is K1. W*(K0) has node K2 ≠ K0, so σ_new(K0) = pA.
  - Right. The Corollary «the K-config changes only at a fallback» is right in the sense the proof uses: while the K-config is κ0, it
    leaves κ0 only at a fallback. As a sentence on its own it is false, because E3 and E4 are S4a steps that change it. The packet's
    Corollary carries the same unqualified sentence; ENDGAME-3's proof uses only the κ0 reading. See L-R1.
- E2: at the fallback Iσ ≠ ∅ (E1 (a)), so S4c is Even's and τ is kept (FIX 3). On the core only (K0, K1) improves, giving κ1. Movers
  and β's may also switch; E3 and E4 allow any σ there. Right.
- E3 (κ1):
  - σ̄(K2) = r.
  - Values: K0 (K1, {K0}, 1), q (K1, {K0}, 2), K3 (K1, {K3}, 3), pA (K1, {K3}, 4).
  - Iσ on the core is {(K1, q)}: K0 even and in q's set.
  - H: K1 → q → K0 → K1 has node K0, the top even vertex. W*(K1) = (K0, ∅, 2) ≠ K1 ⊕ W*(s) = (K0, ∅, 4), so σ_new(K1) = q. That
    changes σ, so it is not a fallback, and the result is κ2. Right.
- E4 (a) (κ2):
  - σ̄(K2) = K2 (r would lead to node K0).
  - pb_g = (K0, ∅, 1). Ξσ(xt) ⊴ the pe-play value with node c_W, and rew(c_W) < rew(K0). So (β_g, pb_g) ∈ Iσ and (K3, K1) ∈ Iσ.
  - In H, β_g and K3 are on no H-cycle. Their W* has node K0, and the alternatives have node c_W or K2. So σ_new = pb_g and K1, the
    result is κ3, and it is not a fallback. Right.
- E4 (b):
  - Every Odd deviation from ρ* reaches β_h → pb_h → K0's cycle, a larger reward. So every gate's least value is (c_W, ∅, 5ℓ + 3).
  - Every option of a level-ℓ mover has value (c_W, ∅, 5ℓ + 4): no improving edge at movers.
  - The core and the β's are not improving. Every other Even vertex has one successor. So Iσ* = ∅. Right.
- TERM-XI: τ is fixed (E0) and every counted iteration changes σ. The changed vertices take improving edges, one per vertex: an
  unambiguous non-empty switch, and the fallback switches one best edge per vertex. Ξσ does not depend on τ. So R15 (c) applies to the
  σ sequence and no σ repeats. Right.
- ENDGAME-3 / ENDGAME-3-N5: the composition is right. A run cannot stop at κ0 ((K0, K1) ∈ Iσ), and the K-config leaves κ0 only at a
  fallback. E2 → E3 → E4 then give exactly F + 2 iterations and one fallback.
  - EN-2 is right: the N5 proof uses only (H) plus SPEC's S4c, so it holds for every S4a rule whose output is a pointwise optimum of H.
    My n5w rule (Even PI in H: keep σ(v) unless strictly better, ties to the larger index) is one; see DATA.
- EXACT-L: R117 (f) gives the first fallback at L(G) + 1 (its FL transitions are non-fallback by R104's definition of an FL run), so
  F + 2 = L(G) + 3. For L = 0, F = 1 and the total is 3, consistent.
  - EN-1 is right and necessary: R117 (f) is a theorem about SPEC's tie-breaks (its proof uses [RULE] / R24 (b)'s choice). The same
    games under another pointwise-optimal S4a rule have F = 1 (DATA).
  - The Consequence is right as an iteration-count statement (EN-3 adds «iteration count»), with N + M ≤ n ≤ 7(N + M) + 10.
- END-T3: [R3C] for G places the first fallback at T3 + 1, and ENDGAME-3 gives T3 + 3. «PROVED-CONDITIONAL on REACH3-CYC, itself
  PROVED-CONDITIONAL on [REACH-L]»: [REACH-L] is R118's own condition label (its body, l. 13615, 13660-13670). Right.
- TARGET.md diff: TARGET.md §2 (M4) and §4 («Polynomial only on a restricted class (…)» under «What does not count as M4») match the
  packet's §9 and L-2's last clause. Nothing is claimed beyond Γ3(G). Not M3, not M4, not a step-4 pass; G-N5-TIME stays OPEN. Right.

## DATA replay on my own engine (R2-P-N5-END/r2end.py; driver sweep.sh; totals sweep_totals.out)
- Own code throughout (no lane, L-RED or REFEREE module): Γ3 builder with R117's pad index order (pA, s, q, r, pe, pβ, pb, m),
  SPEC S1 written from SPEC's text with FIX 2 / FIX 4 / Q2-Q4, S3 by FIX 1, S4a on the dual of H, the N5′-xi TIE rule, S4b, S4c with
  FIX 3, and IDEAL by P-N5-REALIZE §2. Every counter is computed from my own states.
- Genomes:
  - 3,000 Ξ-acyclic (seed 3401), 3,000 with Ξ-targets anywhere (seed 3402), and 1,000 with at least one Ξ self-loop (seed 3403);
  - my predecessor's wider acyclic set R2-P-ACYC/setR2_600_32.jsonl (600; d up to 8, degree up to 4);
  - the 14 R117 corpus genomes;
  - 7,614 genomes per mode, 3,751 of them IDEAL-ACYC.
- spec (N5), xi (N5′-xi), n5w (another pointwise-optimal S4a), all 7,614 each:
  - e0fail, e1fail, e2fail, e3fail, e4fail, finsbar, fintie, nofb, multifb, late, totfail, capped, oddfb and Hfail are 0 in every mode;
  - Hfail: (H) failing at K0, K1, K3 or a β when TIE is a singleton;
  - every run has exactly one fallback and F + 2 iterations;
  - s1_selfcons is 0: my S1 values equal the values of the (σ, σ̄) play;
  - s4a_not_opt is 0 (spec, n5w): S4a's output attains W* (own PI) everywhere.
- EXACT-L (spec): lfail 0 on the 3,751 IDEAL-ACYC genomes, L(G) up to 59 (RECT_d11_T59_norm: 62 iterations, F 60).
  - On the 14 corpus genomes my iteration counts equal the lane's maxxi column of sweep195.out genome for genome (12, 18, 16, 14, 16,
    27, 62, 36, 38, 47, 51, 20, 28, 34).
  - Gate e-order (R104 leaves the order of the e-priorities open; L-NEW uses (lev, gate)): spec on 3,614 acyclic genomes, lfail 0 and
    every counter 0.
- EN-1 / EN-2 (n5w):
  - F = 1 on all 7,614 runs; ENDGAME-3's shape holds (every counter 0).
  - EXACT-L fails on exactly the IDEAL-ACYC genomes with L ≥ 1: lfail 2,658 = the 2,658 such genomes (awk over sweep_n5w.out and
    sweep_spec.out); lfail with L = 0 is 0.
  - So the identity depends on SPEC's tie-breaks, as EN-1 says. This is my counter; the line cites REFEREE 29's 382 / 382, which I have
    not read.
- 1E-N3 spot check (--chkopt, 600 spec + 300 xi runs): σ̄ from my S1 equals Odd's pointwise optimum by my own PI on the dual
  (sbar_opt_fail 0).
- Controls (must fire):
  - ctrl (start τ(K2) = r, σ(K1) = q; 400 runs per mode): e0fail 800 (states), nofb 400, spec lfail 211;
  - ctrl1 (κ1 / κ2 expectations swapped, final checks on the S3 state; 100 runs per mode): e2fail, e3fail and e4fail 100 each, finsbar
    100, fintie 401 (movers).
- SELFL_n3: 3 iterations, F 1 (r2end.py, spec). My IDEAL code refuses it because its X-chain cycles: P-N5-REALIZE §2 says the chain
  ends «at the first option whose Ξ-target is X (finite for IDEAL-ACYC)». Reading B_s as the set of β-ids on the eventually periodic
  chain gives L(G) = 1, the packet's value. See N-1.

## DATA rule on L-2, clause by clause (lane tool eg195.py at 2fcee038 read line by line; outputs at the archive)
- Unit / tool / scope: «runs of N5′-xi (EG195_MODE xi) or N5 (spec) from S3 on Γ3(G) built by box189/gamma3.py, stepped by
  box190/n5v.py; tool eg195.py, run by check195.sh». Right: eg195 imports gamma3, n5v and n5x and steps n5v.step(…, MODE).
- Set:
  - 8 families × 1,500 × seeds 1951, 1952 = 24,000 runs per mode: my script over data/sweep195.out gives runs 24,000 (xi) and 24,000
    (spec);
  - the 14 corpus genomes in spec: 14 rows;
  - check195.out: 8 × 300 at seed 1953 per mode plus every pinned genome of box189 and box191-194. That is check195.sh's text.
- Counters, by condition (eg195.py l. 56-90):
  - e0fail: τ ≠ τ0 or Iτ ≠ ∅, per state (the final state included).
  - e1fail: per iteration before F, κ0 at its input, Iσ on the core = {(K0, K1)}, κ0 at its output.
  - e2fail: at F, κ0, Iσ ≠ ∅, κ1 out, τ kept.
  - e3fail: at F + 1, κ1 in, core Iσ = {(K1, q)}, not a fallback, κ2 out.
  - e4fail: at F + 2, κ2 in, core Iσ = {(K3, K1)}, (β, pb) ∈ Iσ wherever σ(β) = xt, not a fallback, κ3 out, every mover-target β on pb.
  - stopfail / finsbar / fintie: on the final state.
  - Every condition is at least as strong as its clause; e3fail and e4fail are stronger (they pin Iσ on the core). Units as in L-2.
- One gap in the counters, closed by the tally:
  - A run that stopped at F or F + 1 would trip no fail counter.
  - The clause «every run "one fallback, 3 iterations from it"» rests on the (F?, post) tally.
  - Every one of the 32 family rows and 14 corpus rows of sweep195.out has tally [((1, 3), runs)] (my script: bad tallies 0).
  - check195.out's tallies are pinned, and check.sh diffs it byte for byte.
  - So the clause is supported as written. Its support is the tally, not a fail counter; nothing to change.
- EXACT-L clause:
  - 4,297 = 4,283 random IDEAL-ACYC genomes in the spec family rows (sum of their acyc column) + 14 corpus genomes;
  - 3,000 of them from acyc (1,500 + 1,500);
  - lfail 0 in every spec row;
  - RECT_d11_T59_norm maxxi 62;
  - «record only (not re-run by check.sh, which leaves LRED unset)»: right, check195.out has acyc 0 and lfail 0 because LRED is unset.
  - acyclic() counts a Ξ self-loop as a cycle (col[x] = 1 while x's options are scanned): IDEAL-ACYC as R104 defines it.
- Controls clause:
  - check195.out l. 137: «ctrl1 … e2fail 100 e3fail 100 e4fail 100 stopfail 100 finsbar 100 fintie 100»;
  - l. 138: «ctrl2 … e0fail 200 e1fail 200 … nofb 100».
  - Equal to L-2. N-2: L-2 tags ctrl2's «e0fail 200 and e1fail 200» with «(unit: states)», while E1's own clause gives e1fail's unit as
    «iterations before the first fallback». In eg195 the two coincide: e1fail counts input states of iterations; its docstring says
    «states before the first fallback». Cosmetic, optional.
- Independent-replay clause: L-RED 57 (6f56004c), L-RED 58 (143f0b4c) and REFEREE 29 (e4cb208a) are cited by commit, «cited, not
  re-run». I have not read them. A citation of other groups' counters with their commits meets the rule as a citation; my own replay
  above is independent of all three.
- Pins clause («all pinned in box195/end.pins»): 41 of 41 match (Object).

## Line L-2: NOT YET (one REQUIRED change)
- L-R1 (REQUIRED). E1's consequence is false as a sentence on its own once E3 and E4 run: they are S4a steps that change the K-config.
  In a RESULTS line it would read as a claim about the whole run. Old string (exactly once in L-2, my grep):
  «so the K-config changes only at a fallback and the run cannot stop before one»
  New string:
  «so the K-config leaves κ0 only at a fallback and the run cannot stop before one»
  No proof changes: ENDGAME-3 uses exactly this reading.
- N-1 (optional): after «has L(G) = 1» insert « (IDEAL run read with B_s the set of β-ids on its eventually periodic X-chain; R104's
  IDEAL run is defined on IDEAL-ACYC)». R104 / P-N5-REALIZE §2 define the X-chain as finite only for IDEAL-ACYC. Old string, once in
  L-2: «has L(G) = 1 and N5 makes 3 iterations (F = 1)».
- N-2 (optional): «ctrl2 e0fail 200 and e1fail 200 (unit: states)» → «ctrl2 e0fail 200 (unit: states) and e1fail 200 (unit:
  iterations before the first fallback)». Old string once in L-2.
- With L-R1 applied (and N-1, N-2 at the lane's choice), L-2 matches the packet read with fixes entries 1-2. I have nothing else to
  change: the labels, scope, premises, DATA clauses and TARGET clause are right.

## Machine checks (all on git archives; outputs in R2-P-N5-END/)
- Archive 131b4c1c: packet sha1 5cae845b, 22,967 B. Archive 2fcee038: L-2 sha1 e8a8ac51, 6,988 B; end.pins 41 / 41 OK; mkl2_195.py
  rebuilds L-2 byte-equal; check195.sh exit 0, output byte-equal to check195.out.
- r2q.py (quotes, trunk a1decf9a0): 53 quotes, 44 in trunk sources, 9 self-quotes, 0 missing.
- r2end.py + sweep.sh: the replay above. The per-genome outputs sweep_{spec,xi,n5w,spec_gate}.out are not committed (1.5 MB); `bash
  sweep.sh CORPUS` regenerates them (fixed seeds), and the TOTAL lines are in sweep_totals.out. corpus_*.out are committed.

## Statement of independence
My verdicts were formed before reading docs/referee/R-P-N5-END.md. I will read it only after this report is committed, and write any
comparison as an Addendum.

## Addendum 1: comparison with REFEREE 29 (docs/referee/R-P-N5-END.md, claude/referee e4cb208a, §C at 407f4a21), read after 9b3cc9b6 was on origin
- Verdicts: equal on every row. All SIGN; END-T3 SIGN as PROVED-CONDITIONAL on REACH3-CYC (R118 (k), itself on [REACH-L]); [OPT] =
  [1E-N3] for SPEC runs (their §2.2 = my Premises); EN-1..EN-4 right (their §6 = my Re-derivation).
- Replays agree and are independent of each other.
  - Theirs (§4): own engine on xicyc_vj; n5b (L-COMP) for SPEC tie-breaks; t3r_sim for L(G).
  - Mine: own SPEC S1, own N5 / N5′-xi / n5w, own IDEAL.
  - The tie-break dependence is the same finding twice. Theirs: F = 1 on 382 / 382 IDEAL-ACYC genomes with L ≥ 1, seed 2951. Mine: F = 1
    on 2,658 / 2,658, and on all 7,614 runs. Their reason (at S3 every mover's options tie in H because Odd follows pe there) is
    consistent with my n5w having F = 1 on every run.
  - Corpus counts are equal (RECT_d11_T59_norm: F 60, 62 iterations, in both).
- DATA rule: equal findings.
  - The 4,283 / 3,000 / 4,297 sums; check195.sh byte-equal on re-run (they 131b4c1c, I 2fcee038); lfail «record only» because LRED is
    unset in check.sh.
  - e1fail's two unit words: their §5 / LN-6, my N-2.
  - Their §C (407f4a21, l. 201-203) accepts L-2 with «e1fail iterations before the first fallback» in the E1 clause. L-2's ctrl2 clause
    still says «e0fail 200 and e1fail 200 (unit: states)». Their LN-6 asked for one unit, and my N-2 gives the string. I leave it
    optional, as before: the two counts coincide.
- Difference 1 (mine only): L-R1, which I REQUIRE.
  - Their §3 (l. 80) uses «κ changes only at a fallback» as a proof step of ENDGAME-3. As a step it is right in the κ0 reading.
  - The line states it as E1's consequence with no restriction, and E3 / E4 make S4a steps that change the K-config.
  - I keep L-R1 REQUIRED for the line: one string, no change in meaning for the proof. Their §C L-2 MATCHES does not address this
    sentence.
- Difference 2 (mine only): N-1, optional. L(G) of SELFL_n3 needs B_s read on a non-terminating X-chain. Their §3 gets L 1 from
  t3r_sim, and I get L 1 under the set reading. The numbers agree; the note is about the definition only.
- Difference 3 (theirs only, none for me): they asked for units on nofb / late / capped (LN-6). L-2 has them («nofb 0 and capped 0
  (unit: runs), late 0 (unit: iterations after F + 2)»), and I checked them against eg195.py l. 56-90.
- Net for routing: both referees SIGN every statement. The line needs L-R1 (one old/new string, in Line L-2 above); N-1 and N-2 are
  optional. With L-R1, L-3 = L-2 + L-R1 (+ N-1, N-2 at the lane's choice) is the line I will byte-test.

## Addendum 2: byte test of line L-3 (REFEREE-2 successor 35, Opus 5.5, D1; 2026-11-08 10:54Z by date -u)
- Object: claude/l-new 8b67d40e6020d03d4eea18bf4c697a5193a709f7 (Lead 10:54Z). docs/new/P-N5-END-line-L3.txt, sha1
  d6afe92ae0d2c0021743c99d2bd10f16cad27c73, 7,215 B, one line, 105 «(» = 105 «)», no «|». 2fcee038 (L-2) is an ancestor. Fixes entry 3
  (line-only) lists S1-S5, and the Lead ruled 10:18Z «take S1-S5, DROP S6».
- Own script R2-P-N5-END/bt_l3.py (out bt_l3.out) applies the five referee strings to L-2 (e8a8ac51…). It takes L-R1, N-1 and N-2 from
  this report's «Line L-2» at 9b3cc9b6, and EL-1 and EL-2 from REFEREE 29's R-P-N5-END.md §C at claude/referee 407f4a21 l. 212-215.
  Results:
  - Each old string occurs exactly once in L-2 and 0 times in L-3. Each new string occurs 0 times in L-2 and exactly once in L-3. Each
    referee-side piece is verbatim in its referee's text.
  - **L-3 == L-2 + S1-S5: True.** Nothing else changed.
- The lane's mkl3_195.py, on a git archive of 8b67d40e, rebuilds L-3 byte-equal (d6afe92a…). box195/end.pins: 43/43 match (L-3 and
  mkl3_195.py added).
- Meaning:
  - S1 is L-R1 verbatim (REQUIRED, now met).
  - S2 and S3 are N-1 and N-2 verbatim.
  - S4 places REFEREE 29's EL-1 parenthesis after «is NOT proved». The meaning is unchanged: the transfer is not proved, and the reason is
    stated.
  - S5 is EL-2 verbatim.
  - No statement, label, premise, scope or DATA number changes.
- Verdict: **L-3 MATCHES.** All P-N5-END statement verdicts are unchanged: every row SIGN, END-T3 PROVED-CONDITIONAL on REACH3-CYC (R118
  (k), itself PROVED-CONDITIONAL on [REACH-L]). From my side P-N5-END may land with L-3.

## Addendum 3: byte test of line L-4 (REFEREE-2 successor 35, Opus 5.5, D1; 2026-11-09 05:27Z by date -u; independent of REFEREE)
- Object: claude/l-new b7faeebe (Lead 05:27Z). docs/new/P-N5-END-line-L4.txt, sha1 5f88c2971718522027ae267754814c6ba401b829, 7,230 B, one
  line, 105 «(» = 105 «)», no «|», «τ0» 0 times. Fixes entry 4. The packet is unchanged from 8b67d40e (git diff empty).
- (1) Byte test. Own script R2-P-N5-END/bt_l4.py (out bt_l4.out) uses CHECKER 23's strings, verbatim from C138 §4 at claude/checker
  46905772. R-U is applied first, then R-T0. Each old string is once in the current line and 0 times in L-4. Each new string is 0 times in
  L-3 and once in L-4. **L-4 == L-3 + R-U + R-T0: True.** Nothing else changed.
- (2) Meaning.
  - R-T0 is in ENDGAME-3's signed clause. The packet §2 (S) (l. 90) defines «S3's pair ([G3] S3-START, or FIX 1 directly): κ0; …; τ0 :=
    pe_g at every gate and K2 → K2». So τ0 is S3's τ by definition, and landed R117 S3-START / P-N5-REACH §3 give the same standard τ
    («τ(g) = pe_g at every gate, τ(K2) = K2»). «S3's τ» is exactly the proof's object, and E0 says it never changes before the end.
  - R-U is scope wording only: the same status words in the landed R123 order. END-T3's labels are untouched: «PROVED-CONDITIONAL» and
    «REACH3-CYC» each occur 2 times in L-3 and in L-4.
- (3) Fixes entry 4 is line-only. It quotes C138 E-1 / E-2 and states R-U, R-T0 and L-4, with no proof step and no statement change.
- (4) Verdict: **L-4 MATCHES** (byte test, and in meaning). Statement verdicts unchanged.
