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

## D11 (2026-10-16 ~16:40Z, owner via OWNER-DESK, answering Q12): contact with van Dijk
> No contact for now

Lead reading L30: Q12 option (a). No contact with the author about counter_dtl or anything else; the fleet works from the
public record (T17) and its own constructions. The p.15 recipe was already built (L-RED R14, d70e99a: no slowdown on A_DTL).
The question may be put to the owner again only if a later finding makes the author's counterexample decisive.

## L31 (Lead reading, 2026-10-16 17:25Z): C6 is not promoted to a gauntlet candidate
Basis: L-ALG's C6 scoping note (docs/alg/GAP-A-M.md §19, l-alg 16fd55b). C6 (DTL with ideal pruning) removes (H4) by
construction and has every per-context lemma proved (F, S), but its GAP-A reduces to the same core as A_DTL (a polynomial
bound on fresh, resetting child contexts per parent piece), its completeness reduces to A_DTL's GAP-C, and (H1)-(H3) are
open or dead on C6 as on A_DTL. Promoting it would add gauntlet steps 1-3 without shortening the open core. Reading:
A_DTL stays the gauntlet candidate (step-4 statement L24/L26 unchanged). C6 is used as the SIMPLER MODEL for the core: a
proof of the core on C6 is the first target, then its transfer to A_DTL (where (H4) adds deficits). Revisit if the core is
proved on C6 and the transfer fails, or if the owner decides otherwise.

## L32 (Lead reading, 2026-10-17 09:12Z): GAP-A reassessment criterion (owner asked via OWNER-DESK: "Are we narrowing down the decision to see?")
GAP-A (polynomial number of searches for A_DTL) is not converging: every per-context and per-phase potential stated so far is
dead (RESULTS DE9-DE12); the surviving statement (SPP) is DATA only (tight, 0 violations). GAP-C, by contrast, has narrowed to
one open point ((ACYC), docs/alg/STEP5.md) plus the S/T steps. Criterion:
(1) Immediate stop of the candidate (owner report at once): any Oink-verified incorrect/incomplete run under any order datum, or
    a family whose searches per phase grow super-polynomially (gauntlet step 4 fails; DTL becomes a dead end).
(2) Reassessment point: the Fable reset, 2026-10-21 21:00Z, or earlier when both lanes' boxes end with no new GAP-A reduction.
    "Progress" means a reduction of GAP-A to ONE named statement with a proof route (as GAP-C reached), or a proved polynomial
    bound on a nontrivial subclass. If neither exists at the reassessment point, the Lead puts three options to the owner:
    (a) bank the refereed partial results (GAP-C chain, Step 5) and write up DTL's status as an open candidate;
    (b) keep only the cheap adversarial side on GAP-A (L-RED climbs), no proof lane;
    (c) a new candidate or a new approach. The owner decides.
(3) Allocation until then: from the next boxes (after ~13:10Z) one lane returns to GAP-A with a fresh angle; GAP-C continues.

## D12 (2026-10-17 ~09:10Z, owner via OWNER-DESK): referees on Opus
> WE can run referees on opus too temperoraly

Lead reading L33: until the Fable reset (2026-10-21 21:00Z), REFEREE and REFEREE-2 may run on Opus 5.5. This lifts the L27
"referees wait" for that period and is the owner's own exception to D1's "never downgrade the referee". Unchanged: two
independent referees, REFEREE-2 reads docs/referee/ only after its own report, gaps listed. Every signature given on Opus
carries the label "(Opus 5.5, D12)" in its report and in RESULTS; after the reset the Lead may ask a Fable referee to re-read
any such entry. First packet: docs/alg/STEP5.md (Step 5 of GAP-C: NT-f, FM, WM, (YZ) <= (ACYC), P-KT), pinned at a trunk SHA.

## D13 (2026-10-18 ~08:53Z, owner via OWNER-DESK owner-desk f29eef5, answering Q14, the L32 reassessment)
> Keep working on the dtl and also c

Lead reading L34 (2026-10-18 08:55Z by date -u):
(1) DTL: both sides continue at the D7 rate. The proof lane (L-ALG) works on (LONG-PHASE)/(CTX⁺) toward the L32 progress
    criterion (one named statement with a proof route, or a proved polynomial bound on a nontrivial subclass). The adversarial
    lane (L-RED) works on a long phase at one context and on serialized contexts. Option (a), the write-up, was not chosen; the
    refereed record stays in RESULTS as it is.
(2) (c): a new candidate or approach runs alongside DTL. The owner named no direction, and D1 says "Spawn no attack lane before I
    approve it." So the Lead puts 2-4 concrete directions to the owner through OWNER-DESK (Q15) and starts no (c) lane until the
    owner picks one.
(3) L32 stays in force: its (1) report-at-once conditions are unchanged; the next reassessment is at the Fable reset,
    2026-10-21 21:00Z.
(4) D1 cap: at most 5 working sessions: L-ALG, L-RED, the (c) lane once approved, and at most two of REFEREE, REFEREE-2 and
    CHECKER at a time.

## D14 (2026-10-18 ~08:59Z and ~09:02Z, owner via OWNER-DESK owner-desk 64c66ac and 425a190, answering Q15, the direction for (c))
> D
> You know it can also test prveiously not tested approaches, it can come up with it own as well

Lead reading L35 (2026-10-18 09:04Z by date -u):
(1) "D" is the Lead's choice of direction for (c), and with the follow-up it is the owner's approval (D1) of ONE (c) lane that is
    not limited to the mapped options A-C: it may test approaches the fleet has not tested, including its own.
(2) The Lead's pick: a new design lane L-NEW (Opus 5.5 under D8; files docs/new/, experiments/new/, notes/L-NEW.md). Box 1:
    (i) option A first as a fast kill test, S5 (Zadeh, index tie-break) and S6 (Cunningham, index order) on the hard bench and
    under adversarial numbering, using L-SI's engine; (ii) then up to three approaches of its own, each screened against
    docs/lit/BARRIERS.md and the dead-end record before any code, and run on the hard bench before any gauntlet step.
    Option B (weak separators) is queued for after the Fable reset.
(3) Unchanged: D1 "A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the
    fleet's own, as wrong until it passes the gauntlet below."; the gauntlet (TARGET.md section 5); big numbers at bit cost.
    An approach that survives gauntlet step 2 is reported to the owner at once.
(4) Working sessions: L-ALG, L-RED, L-NEW (3 of the D1 cap of 5).


## L36 (Lead reading, 2026-10-21 21:06Z by date -u): after the weekly-cap pause and the Fable reset
Facts: every fleet session (Lead and OWNER-DESK included) stopped between 2026-10-19 03:33Z and 04:01Z with "You've hit your
weekly limit · resets Oct 21, 9pm (UTC)" (rate_limit seven_day "rejected", isUsingOverage false on all). This is the D7 automatic
pause ("We pause automatically if the cap is hit"), not paid overage; the owner could not be told at the time and was told at
21:06Z (OWNER-DESK). The reset at 21:00Z is also the Fable reset that ends the D8 period ("switch to opus 5.5 until the weekly
limit is reset") and the D12 period ("temperoraly"), and it is the L32 (2) reassessment point. Q16 (L32 options) is still open,
so D13 ("Keep working on the dtl and also c") holds. Q18 put to the owner: models after the reset.
Reading, until the owner answers Q18:
(1) Work the cap cut off finishes on its existing session: L-RED succ. 10 (box 16, R48 §4) and CHECKER (C19 Addendum 3).
(2) The (c) lane L-NEW continues its next box on its existing session (D13).
(3) Any NEW session starts on Fable 5.1, as before D8. The Fable L-ALG session paused on 2026-10-16 is not resumed: it is stale
    and the proof lane is parked (Q16 recommendation).
(4) No referee signs on Opus after the reset unless the owner extends D12; existing "(Opus 5.5, D12)" labels stay.
(5) Working sessions: 3 of 5 (L-RED, L-NEW, CHECKER).

## D15 (2026-10-22 ~06:59Z, owner via OWNER-DESK owner-desk a7578c6e, answering Q18 and Q16)
> q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it

Lead reading L37 (2026-10-22 07:00Z by date -u):
(1) Q18 (b): lanes AND referees run on Opus 5.5. This extends D12 past the reset and replaces L36 (3)/(4). New sessions start on
    Opus 5.5; referee signatures on Opus are labelled "(Opus 5.5, D15)". Fable sessions already running finish their current box and
    are then succeeded on Opus; signatures already given on Fable 5.1 (RESULTS R17) stand with their label.
(2) Q16 (b)+(c), closing the L32 reassessment: DTL keeps only the cheap adversarial side (L-RED: attacks on (NEST*-BOUNDED) and
    on GAP-A; no DTL proof lane; L-ALG stays parked). The main effort goes to (c) under D14: L-NEW on N5 and on approaches not yet
    tested, its own included. The extra "proof attempt on (NEST*-BOUNDED)" from the Lead's recommendation is dropped: the box-16-18
    data (NEST* 3 -> 6 with the number of parts) point the other way; L-RED's adversarial work on it continues.
(3) Standing instruction: the owner is not asked questions of this kind (options, models, reassessments, allocation). The Lead
    reasons and decides, records the decision as a Lead reading, and reports it as information. This supersedes the "options to the
    owner" parts of L32 (2) and L34 (2).
(4) Still the owner's (D1/D10/D11, CLAUDE.md, Lead reading): changes to TARGET.md; anything external (publishing, posting,
    emailing, submitting, contacting anyone; D11 "No contact for now"); paid overage (stop the fleet and tell the owner, D1/D7);
    restart after an owner "stop"; more than 5 working sessions (D1: "unless you justify more to me", reported with the
    justification). Reports stay as information without questions: milestones, step-2 survivors, incorrect runs, super-polynomial
    families, step-4 claims, the weekly checkpoint.
(5) D1 "Spawn no attack lane before I approve it": lanes inside the D15 (2) directions (DTL adversary; (c) new approaches per D14)
    need no further approval; that is the Lead's reading of "Be autonomous".

## D16 (2026-10-24 ~12:49Z, owner via OWNER-DESK owner-desk b3bb957, after the 12:22Z status reply "fleet idle since 08:27Z; restart only on a new idea")
> Then keep working as I told you to

Lead reading L38 (2026-10-24 12:50Z by date -u):
(1) An idle fleet is not allowed while D13 ("Keep working on the dtl and also c"), D14 ("it can also test prveiously not tested
    approaches, it can come up with it own as well") and D15 ("Be autonomous, reason about it") stand. The stand-down note's rule
    "restart only on a new idea from a lane, the literature or the owner" is WITHDRAWN: the fleet generates its own next directions.
    docs/agents/N5-STANDDOWN.md stays as the record of N5's state; its named lead is the first (c) task.
(2) Restart at once, three working lanes:
    a. DTL adversary (D13; L37 (2)): L-RED successor 13, box 30: an attack on an open DTL gap, (NEST*-BOUNDED) (G-NEST), GAP-A or
       (ACYC) (G-S5-6), the lane choosing with a stated reason.
    b. (c), N5: L-NEW successor 9, box 26: the stand-down's named lead (every re-entry into R inside a joint λ-phase is a route
       improvement against τ; count those by R17's machinery), toward (TRUST).
    c. (c), new approaches (D14): L-LIT successor, task T27: a source-checked scan for approaches not yet tested by the fleet, at least
       three, each screened against docs/lit/BARRIERS.md; no runs. The best goes to L-NEW for a falsification box.
(3) No spend limit was stated; D1/D7 (stop on paid overage and tell the owner) holds. Boxes stay about 3 h; the Lead re-runs every kill
    and claim as before.
(4) Pacing: when a line is exhausted, the Lead routes the next self-generated direction from the queue in NOW instead of idling.

## D17 (2026-10-24 ~12:57Z, owner via OWNER-DESK, right after D16)
> We have so much still of our weekly usage cap, like we are not on track to make the most of it

Lead reading L39 (2026-10-24 12:58Z by date -u):
(1) Spend signal: the owner wants the weekly allowance used for parallel work. Saving money is not a reason to idle or to cut a line short
    (this answers N5-STANDDOWN's "more boxes would mostly spend money"). D1/D7 (stop on paid overage) and the 5-working-lane cap stand.
(2) Five working lanes from now: L-RED 13 (DTL gap, box 30), L-NEW 9 (N5 lead, box 26), L-LIT (T27 untested approaches), L-COMP succ. 2
    (box 3: exhaustive small-game searches that the climbs cannot do), and a new L-SI successor on Opus (D15) (box: a new SI rule that
    avoids N5's trust-mode deadlock without collapsing to switch-all, DE34's lesson).
(3) Above 5 (D1 "unless you justify more to me"): CHECKER and the two referees are gate roles. When a kill or a claim needs them, they run
    in addition to the five lanes, so that landing never waits and no lane is parked to make room. This is reported to the owner with this
    justification; the expected peak is 7-8 sessions.
(4) Each finished box is followed by the next self-generated box from the queue in NOW (L38 (4)).

## D18 (2026-10-24 ~13:04Z, owner via OWNER-DESK, after D16/D17)
> Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.

Lead reading L40 (2026-10-24 13:11Z by date -u):
(1) Priority: N5's running time (G-N5-TIME), proof side. This narrows D13/L38 for now: the DTL attack (L-RED box 30) pauses; T27's
    C1 (Ohlmann's symmetric recursive algorithm) goes to the queue, not to a lane.
(2) All five lanes work on N5:
    a. L-NEW 9 (designer): (TRUST) = θ-THETA re-entries (≤ n per θ-change, lane-proved) + ROUTE re-entries (one-player count) + θ-changes
       per phase (CYC).
    b. L-RED 13 (adversary for N5, D1 "designer and falsifier differ"): attack each candidate lemma L-NEW states; target super-polynomial
       θ-changes inside one joint λ-phase.
    c. L-COMP succ. 2: exhaustive small-n tables (max θ-changes per phase, ROUTE/THETA counts, in-phase max) to generate exact conjectures.
    d. L-SI successor (cross-disciplinary, operations research): N5 through the discounted-game / MDP policy-iteration lens (Ye 2011,
       Hansen-Miltersen-Zwick 2013, Scherrer's analyses): look for a potential or a combinatorial discount that bounds N5's phases.
    e. L-LIT, T28 (cross-disciplinary scan): proof techniques from other areas mapped onto N5's objects (gate, trust, θ, λ-phases):
       unique sink orientations / AUSO combinatorics, Tarski fixed points on lattices, max-plus / tropical algebra, potential reduction,
       matroid or polytope path-length bounds; each with the exact N5 object it would bound.
(3) Assumptions: lanes may make reasonable assumptions; each is stated in one line and labelled ASSUMPTION; nothing resting on one is
    called PROVED.
(4) Labels, strictly: PROVED (with who checked it: lane / referees / Lean), CONJECTURE (with the data behind it), OPEN. This extends the
    existing [refereed-only] / DATA / READING scheme; reports to the owner use exactly these three words.
(5) D17/L39 stand: five working lanes; CHECKER and referees run on top when a claim needs them.

Lead reading L41 (2026-10-30 18:40Z by date -u):
Referee-originated proofs. A proof written by one referee counts toward "two referees signed it with its gaps listed" (CLAUDE.md) when
the author referee signs it in its report and the OTHER referee independently checks and signs it; both signatures and the joint gap map
are quoted in the RESULTS entry, whose scope tail says the proof is referee-originated. Applied first to FLAT-SW in R94 (SW-KEEP by
REFEREE 20, signed by REFEREE-2 23; OWN by REFEREE-2 23, signed by REFEREE 20); CHECKER C104 5c4d6e45 found it meets the rule (its N-3:
weaker than lane-authored plus two non-author checks for the general form). Lanes write line files without a heading marker (C104 N-1).
