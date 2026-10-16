# Owner rulings (append only; quote verbatim; a reading is labelled "Lead reading")

## D1 (2026-10-14): launch brief
Full text, verbatim: docs/decisions/D001-launch-brief.md. Key lines:
> Spawn no attack lane before I approve it.
> Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.
> A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
> Never downgrade the referee to save money.
> At most 5 working sessions at once unless you justify more to me.
> On "stop", follow the playbook's stop procedure; restart only on my word. On paid overage, stop the fleet and tell me.

Lead reading L1 (superseded by the amended L1 under D2): M2 clock start was held while arxiv.org was blocked.
Lead reading L2: the playbook's `main` branch is replaced, until the owner says otherwise, by the Lead branch
claude/vibrant-johnson-nxvvxo as trunk; lanes merge into it only through the pipeline.

## D2 (2026-10-14 ~18:15Z): TARGET.md v0.1 approved with changes; network opened
Verbatim:
> I have provided you with full internet access,
>
> TARGET.md v0.1: approved with these changes. Record this ruling verbatim, bump to v1.0, and date it.
> 1. Section 1: priorities range over {0, ..., n} (d ≤ n + 1); the compression step stays charged to the algorithm.
> 2. Section 6: add a check that the Lean `solve` implements exactly the pseudocode whose running time is analysed.
>    The referee signs this, and the CHECKER diffs it.
> 3. 7a approved with change 1. 7c, 7d, 7e approved as written.
> 4. 7b changed: a randomized (Las Vegas, expected polynomial) algorithm is labelled M4-R, not M3, and reported to me
>    at once like an M4 claim.
> 5. Gauntlet addition: every implementation also outputs positional strategies, and L-COMP verifies them on every
>    test game.
> Attack lanes may start once v1.0 is pushed.

Lead reading L3: change 5 applies to every implementation that enters the gauntlet (fleet claims and audited external
claims such as 2511.03752); the target statement itself still requires only the regions (7d as written).
Lead reading L4: "Attack lanes may start" lifts D1's hold; lanes are still added one at a time in L-LIT's ranked order (D1).
Lead reading L1 (amended): the M2 clock starts 2026-10-14 18:30Z (paper hosts reachable, REFEREE spawned); deadline 2026-10-16 18:30Z.
Lead reading L5 (M1 wording, D1 "confirms their blow-up in Oink"): Oink has no implementation of the switch-all/switch-best rules that
Friedmann's SI games target, so those two families are confirmed with REFEREE-checked Python ports of PGSolver's SI loop, quoted as
"the strategy-improvement loop (= PGSolver with -dgo -dsd -dlo -dsg)"; the other families are confirmed in Oink itself.
Lead reading L6 (2026-10-14, on D1's M3 list): L-STRUCT's S2 target T1 (w^X(n,d) ≥ s^X(n,d−2) for deterministic weak separators over
the priority alphabet), if proved and passed through refereeing, counts as M3 "a lower bound for a broader algorithm model": each
deterministic weak separator is an algorithm via Czerwiński et al. Prop. 3.2, and weak separators strictly contain strong ones (C1).
Basis: L-LIT T5 verdict NEW (docs/lit/T5-S2-novelty.md). Scope excludes vertex-name alphabets and non-deterministic weak separators.
Lead reading L7 (2026-10-14, on D1's M3 list): S3 target T3 (w^V(n,d) = s^V(n,d) for d ≤ n+1), if proved and double-refereed,
together with L4 (s^V(n,n) ≥ n^Ω(lg n)), counts as M3 "a lower bound for a broader algorithm model" (deterministic weak separators on
the TARGET alphabet). L4 alone is recorded as a supporting lemma, not claimed as M3: it follows from CDFJLP Thm 5.1 plus a conversion
Parys-Wiacek state without proof (2305.00308 p.2); L-LIT T6 found no published vertex-priority lower bound. Owner may rule otherwise.
Lead reading L8 (2026-10-14, on D1's M3 list, "a new polynomial class"): a class counts as a new polynomial class only if its
membership is decidable in polynomial time or it is given by a natural structural condition checkable in polynomial time. A class on
which a known polynomial partial solver is merely complete (promise-only; "run it, fall back if residual") is recorded as "a tighter
analysis of a known algorithm" (D1), with correspondingly lower weight. Owner may rule otherwise.
Lead reading L9 (2026-10-14, under L8): L-ATTR's T-A1 ("psolB solves G completely ⟺ PA**(G)"; PA** ⟹ psolQ solves) is recorded,
if double-refereed, as M3 "a tighter analysis of a known algorithm": an exact structural characterisation of the class HKP call
"Solved" for psolB. It is not claimed as "a new polynomial class": PA** membership is decidable in polynomial time only by running
psolB itself (L8). Owner may rule otherwise.

## D3 (2026-10-15 ~07:26Z): owner-questions session
Verbatim:
> Lets start a subsession called owner questions where you can delegate your questions and I can ask questions about the research progress

Lead reading L10: the session is OWNER-DESK (title "Owner questions", brief docs/agents/OWNER-DESK.md). It holds the open owner
questions and answers the owner's questions about progress from the repository. It relays every owner answer or instruction to the
Lead verbatim; rulings are recorded here by the Lead as before. It has no authority over lanes and messages only the Lead.

Lead reading L11 (2026-10-15 07:55Z, on Q5): the owner answered Q5 with a file, HKP "Static analysis of parity games: alternating
reachability under parity", Imperial DoC DTR15-4 (2015); public copy sha256 a7b61fe3a72926a94a3019e34620339f38aa653fe8aeed9ab4210187763e9cd6.
If L-LIT T11 finds it is the text of LNCS 9560 pp. 159-177, R2's caveat reads "checked against arXiv 1405.0386v2 and the
pre-publication chapter text DTR15-4; Springer pages not opened" and Q5 closes. G10 is not an owner question and is not closed by it.

## D4 (2026-10-15 ~07:55Z, via OWNER-DESK owner-desk 7b5e7ef): answers to Q6, Q7, Q4, Q2, Q3
Verbatim:
> Q6. I am the only human reader, so if there is something concerining me, show it in this session. Q7. You are intelligent enough to reason about this Q4. Again, you are smart about to reason for these type of question, you are aware of the whole process, you must reason about these. Q2. What is your recommendation? Q3. Walk met hrough it

Lead reading L12 (standing): judgement calls on process, method and result classification are the fleet's to make, with reasoning
recorded here; the owner is asked only about scope, spend, anything external, and TARGET.md (CLAUDE.md line 3). Questions for the
owner go to OWNER-DESK; anything concerning the owner is shown there.
Lead reading L13 (Q6, closed): no external distribution of docs/HUMAN-REVIEW.md. The owner is its only reader, via OWNER-DESK.
Lead reading L14 (Q7, closed, delegated): L7 stands. L4 (RESULTS R1) is a supporting lemma, not M3: it is a convention variant of the
known strong-separator lower bound (CDFJLP 1807.10546 Thm 5.1) in the same algorithm model. The M3 credit is T-A1 (R2).
Lead reading L15 (Q4, closed, delegated): no session is spawned for it. When an L-COMP successor is next spawned for other work, it
runs the original PGSolver binaries once (d3cd624) to diff the hard-family ports; if the platform classifier still refuses, the
ported generators plus the REFEREE check stand (L5). M1 does not depend on it.
Lead reading L16 (Q2, closed unless the owner objects): keep claude/vibrant-johnson-nxvvxo as trunk. No pull requests are opened,
so a `main` branch would add a second name without changing any work.
Q3: OWNER-DESK walked the owner through the setup script (cloud environment menu in the title bar > Edit > Setup script). Setting it
is the owner's action; it stays listed until the owner says it is done or declines.
Lead reading L17 (2026-10-15 08:05Z, Q5 closed): L-LIT T11 (l-lit 933dc12) finds DTR15-4 very likely the chapter text (identical
29-entry reference list against Crossref; the only open-access copy of the chapter DOI is this report). Under L11, Q5 closes;
RESULTS R2 caveat updated. psolC (PA** strictly inside Solved(psolC), conditional on DTR Thm 4) is recorded as a candidate, not started.

## D5 (2026-10-15 ~09:47Z, via OWNER-DESK owner-desk 0a17fb5): aim
Verbatim:
> I want you to believe in yourself and just loo kat the decade old mathematical open questions that has been cracked this year with AI. There are hundreads of examples so dont tell me it is highly unlikely to solve the parity game problem, because it is not

Lead reading L18: M4 (and M4-R) is the fleet's primary aim, and fleet documents and reports drop the "M4 unlikely" framing. Effort shifts
toward algorithm design: a new lane L-ALG runs a falsification-driven design loop. Lower-bound work (L-LOWER) finishes its current box.
Unchanged (D1): every algorithm claim, the fleet's own included, is treated as wrong until it passes the TARGET.md section 5 gauntlet.

## D6 (2026-10-15 ~10:04Z, via OWNER-DESK owner-desk d09734b): Q8
Verbatim: > a
(Q8 as shown by OWNER-DESK: "(a) Yes: start one or more algorithm lanes now; L-LOWER continues as well. (b) Yes, and pause L-LOWER
to put the budget there. (c) No change.")
Lead reading L19: confirms L18; L-LOWER continues. The number of algorithm lanes is the Lead's call: a second lane L-SI (strategy
improvement design loop toward M4/M4-R; L-LIT RANKING rank 4) starts now, alongside L-ALG. No spend ceiling set; D1 cost policy applies.

## D7 (2026-10-15 ~12:35Z, owner in the Lead session, answering Q9): spend
Verbatim: > a
(Q9 option (a): "Continue at the current rate. We pause automatically if the cap is hit and stop at once on overage.")
Lead reading L20: the interim freeze of 12:05Z is lifted; the D1 cap (5 working lanes) and the D1 overage rule (stop the fleet
and tell the owner) still apply. Deferred items resume: L-RED (F1 fix, then S7, S5/S6), second referee on the RAR transfer lemma
(REFEREE), then L-LIT novelty check.
Lead reading L21 (2026-10-15 12:58Z): L-RED's Random-Facet transfer (docs/red/R2-RAR.md; both referees signed, REFEREE-2 995cfd3,
REFEREE 42f11c6, subject to a one-token fix in case (3)) is recorded, once the CHECKER passes, as M3-type "a tighter analysis of a
known algorithm" (as L9): original Random-Facet needs e^Omega(sqrt n) expected switches on parity games of size
Theta(n^{3/2} log^3 n). L-LIT T13 (l-lit c962d80): NEW as a published statement, low technical novelty (a faithful transfer of
FHZ 1410.7530 Thm 6.3; the encoding is the contribution; Thm 6.3 credited). Hansen's 2012 thesis unopened: matters only for an
external "first" claim (owner).
Correction to L21 (2026-10-15 13:40Z, after CHECKER C2 FAIL, checker ce07713): "both referees signed" was wrong. REFEREE-2's
R2-TL (995cfd3) is a first-referee read, not a signature (as the Lead's own 12:12Z brief asked). Signatures at 13:40Z: REFEREE
only (42f11c6/5ed56c5, condition met at l-red 49ae306). REFEREE-2 asked to sign at 49ae306 with gap list. The entry text follows
CHECKER C2's suggested wording (scaling, start sigma_{B_0}, N = |V|+|E| form, strict tie convention, gaps G-TL-1..3 + AUSO/ties).
L-LIT T13's line "signed by REFEREE-2 (995cfd3)" carries the same error (L-LIT file; corrected on its next task).

## L22 (Lead reading, 2026-10-15 16:02Z): DTL pinning after CHECKER C3
Fleet judgement under L12 (no owner question). After C3 (claude/checker 5b924e7):
- The DTL candidate is pinned as `oink --dtl --no-single --no-wcwc --no-loops` at Oink 8fbf0a7, trace = 0 (C3 option (i) for D-1). DTL itself must handle self-loops; all step-2 evidence is re-run with --no-loops.
- The theorem must hold for every order of equal-priority vertices (removes the unstable std::sort dependency, C3 D-4).
- The analysed object is the pseudocode docs/alg/candidates/C5-DTL.md, updated to the pinned run (CHECK_UNIQUE on, trace 0). The C++ correspondence is a separate signed item (C3 E-2).
- Prose proofs are step-4 input. An M4 claim still needs Lean (TARGET §5.4, C3 E-1).

## L23 (Lead reading, 2026-10-15 17:12Z): SI line parked after the obstruction map
Fleet judgement under L12. L-SI ended its box early (context 720k) with an obstruction map (l-si 0d48da2). Every memoryless
single-switch rule tried ranks by a quantity that gates, pads, priorities or numbering steer. No L-SI successor now: fleet
spend goes to DTL (gauntlet step 4) while it is the lead candidate. Queued: S5/S6 under adversarial numbering (L-RED, after
DTL); R2 transfer lemma (REFEREE-2). Revisit when DTL is settled either way.

## L24 (Lead reading, 2026-10-15 17:50Z): DTL step-4 statement frozen
Fleet judgement under L12. After CHECKER C3b (claude/checker cf3e0d2: §0 PASS, all C3 items fixed or explicitly deferred),
docs/alg/DTL-proof.md §0 at claude/l-alg ccff864 is frozen as the statement for DTL's gauntlet step 4 (Theorems D1, D2 on
A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, trace 0, every equal-priority order; analysed object
C5-DTL.md; the C++ correspondence §7 to be signed separately, C3b N-1). Changes to §0 go through the Lead and CHECKER.
This is not a TARGET.md change and not a result; GAP-C and GAP-A remain open.

## L25 (Lead reading, 2026-10-15 19:26Z): T-L2 theory goal parked
Fleet judgement under L12. L-LOWER's T-L2 theory box (claude/l-lower aa8995e, docs/lower/L2-theory.md) met the first
clause of its kill criterion: B_2(4) >= 7 is certified (68-game core, UNSAT by four solvers) and localised (28-game core in
class K), but no human-readable proof was found (DRUP 63,298 lemmas; case tree 8,561 partitions at level 4); obstruction in
§3b. Parked. Data kept: B_2(5) >= 9 (UNSAT by CaDiCaL and Glucose); |P_2| = 1 costs exactly 2n-2 at n = 5; the extra gate
is a width cost from serving priority-2 counts {1,2} together. Three k = 9 runs (B_2(5) >= 10?) continue detached in the
parked session at no extra spend; their RESULT lines are read later if the container survives. Standard for SAT data
points: UNSAT by >= 2 independent solvers; no LRAT for now.

## L26 (Lead reading, 2026-10-16 01:20Z): DTL step-4 statement re-frozen for every order datum
Fleet judgement under L12. After CHECKER C3d/C3e/C3f (claude/checker 4b15364: PASS), docs/alg/DTL-proof.md §0 at
claude/l-alg e144992 replaces the L24 freeze (ccff864). Theorems D1 and D2 are claimed for EVERY order datum omega (the eight
implementation choices O1-O8 of docs/alg/C5-orders.md; Oink 8fbf0a7's instance recorded in C5-DTL.md §0), with the pinned
parser's order- and parity-preserving renumbering of priorities named in step 0 (cost charged in D2(e)). Reason (option ii,
L-ALG C5-orders.md): consistent with L22's equal-priority clause, no cost to the proved parts, keeps the tangle bound from
depending on an order accident; L-COMP's second implementation showed counts depend on omega and regions/strategies do not.
Changes to §0 go through the Lead and CHECKER. Not a result: GAP-C and GAP-A remain open.

## D8 (2026-10-16 ~06:50Z, owner in the Lead session, answering Q11): Fable cap
> I think it is okay if we switch to opus 5.5 until the weekly limit is reset no? They produce very similiar results on the benchmarks

Lead reading L27: Q11 option (b). Until the Fable weekly limit resets (2026-10-21 21:00Z), the paused attack lanes (L-ALG,
L-RED) continue on Opus 5.5 at high effort, as fresh successor sessions under LANE-RESTART. Work produced on Opus is labelled
as such in the lane notebooks. The referees are not engaged before the reset (no complete claim is ready); if one is needed
earlier, the Lead asks the owner first, because D1 says "Never downgrade the referee to save money". The Opus weekly limit is
also at "allowed_warning": if Opus hits its cap, the fleet pauses again (D7) and the owner is told. Sweeps return to hourly.

## D9 (2026-10-16 ~10:38Z, owner in the Lead session): search for van Dijk's DTL counterexample
> Can you start a subsession that tries to look up if van dijk's DLT counter example is anywhere online available or posted

Lead reading L28: "DLT" means DTL. The target is the author's counter_dtl ("Counterexample to the DTL solver", Oink README
39254fe, 2021-06-25, never committed; T16 caveat (i)). A fresh L-LIT successor (Opus, D8) runs a read-only search; it owns
docs/lit/T17-counter-dtl-search.md. It does not contact anyone, post, file issues or log in (D1). Any find is reported to the
Lead at once with URL, commit or archive id and date; running it against DTL goes to L-RED. Working sessions: 3 of 5. Given the
narrow, read-only task, the successor answers the five LANE-RESTART questions and then proceeds without waiting for "go";
the Lead re-measures the answers afterwards.

## D10 (2026-10-16 ~16:39Z, owner via OWNER-DESK, answering Q13): repository visibility
> I dont mind the repistory is public

Lead reading L29: Q13 option (a), the repository nano44/parity_games_challange stays public. Pushing fleet work to this
repository is not "publishing" in the sense of D1; D1 still forbids every other outward act (posting, emailing, submitting,
contacting anyone, announcing or linking the repository anywhere). Consequences: (1) "No secrets in any session" now also
means nothing sensitive is ever committed, since every push is public; (2) docs/HUMAN-REVIEW.md being readable in the repo is
accepted under D10; the Q6 ruling (no external distribution by the fleet) is unchanged; (3) nothing in the repo is a claim to
anyone outside: results stay labelled as unrefereed where they are.
