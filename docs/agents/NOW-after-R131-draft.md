# NOW (rewritten, never appended; max 150 lines)
Updated: <DATE> <HH:MM>Z (date -u) by Lead. FRONTIER: the fleet's candidate N5 (SSI-GLOBAL; SPEC S1-S5 with FIX 1-4, default start S3) is a DEAD END: RESULTS R131 [refereed-only] (P-N5-EXP, L-RED-B 5-7; both referees signed; CHECKER C148 <checker>): on the rule-built one-player family G_k (k ≥ 3; R104 genomes, Ξ-acyclic, degree 2, N = 9k − 16) the IDEAL model makes L(G_k) = 2^k − 2 steps exactly (UNCONDITIONAL, on R104's definitions only), so IDEAL-ACYC-POLY is false; through RESULTS R117 as landed (refereed-only) N5 from S3 makes at least 2^k − 1 iterations on Γ3(G_k) (n = 135k − 230 vertices), and through R124 exactly 2^k + 1 (PROVED-CONDITIONAL on those landed results). Every measured run (k ≤ 13 on engines, model to k = 20) is below n²; 2^k − 1 > n² first at k = 23: the dead end rests on the proof, not on a measured instance. GAPS G-N5-TIME: closed, answered NO. Not affected: N5's correctness and termination (R15, R57), every landed R-entry (L-NEW 77's consequence map, claude/l-new 0c18fbba: no landed statement contradicted; R117 and R124 are premises of the kill). NO LIVE CANDIDATE for M4. The question of TARGET.md is open, as in the literature (best known: quasi-polynomial). D18's direction («Focus on N5 and work toward proving it.») has ended with N5; the owner decides what the fleet works on next (owner question Q14 below); no new lane until then (D1: «Spawn no attack lane before I approve it.»). History of the frontier before 2026-11-13: git history of this file and docs/agents/LEAD-STATE.md.

## Milestones
| M | State | Evidence |
| --- | --- | --- |
| M0 Setup | done; TARGET v1.0 at a3777f1 (D2) | this commit; CI .github/workflows/verify.yml; backstop trigger in docs/agents/LEAD-BACKSTOP.md |
| M1 Reproduce hard families | DONE 2026-10-14 19:10Z (l-comp de7ea19): 12 of 13 families blow up as published, all strategies checked; counter_qpt superpolynomial but class open (targets a quasi-poly algorithm). Friedmann SI via REFEREE-checked PGSolver ports (reading L5). Bench LANDED on trunk (REFEREE OK ae532f6) | experiments/hard-families/README.md (l-comp) |
| M2 Audit arXiv 2511.03752 | DONE 2026-10-14 ~18:35Z: BROKEN (two independent 4-vertex counterexamples, cross-checked); RESULTS DE1 | docs/decisions/M2-arxiv-2511.03752.md |
| M3 Partial results | DONE 2026-10-15 00:17Z (novelty T10 NEW, rechecked T11 against the chapter text DTR15-4: still NEW): RESULTS R2 T-A1 [refereed-only] (psolB solves G completely iff PA**(G)); two referee signatures at l-attr 57a1515, CHECKER PASS 62cf1c4. Also R1 L4 (lemma). 2026-10-15 13:50Z: RESULTS R3 [refereed-only] original Random-Facet needs e^Omega(sqrt n) expected switches on parity games (FHZ Thm 6.3 + L-RED transfer lemma; REFEREE + REFEREE-2 signed at l-red 49ae306; CHECKER PASS 068f9de; T13 NEW as statement) | docs/RESULTS.md |
| M4 Target | NOT ACHIEVED; no live candidate. Candidate N5 SSI-GLOBAL: correct and terminating (R15, R57), but gauntlet step 4 (running time) FAILS: RESULTS R131 [refereed-only] DEAD END (exponentially many iterations on Γ3(G_k), conditional on R117 / R124 as landed; the model-level theorem unconditional). RESULTS R17-R130 [refereed-only] are partial step-4 lemmas for N5 and stay true as stated. Variant N5′-xi: DEAD END R130 (2^Ω(√n) on W(G_n, ι)). Variant N5-SF: DEAD END DE35. A_DTL route (older): step 4 open (GAP-A, GAP-C), lanes parked since 2026-10-17 | docs/RESULTS.md R131, R130; docs/GAPS.md |

## Roster (model, effort, one-line reason; revisit at each restart)
Retired rows (parked for good, paused, superseded): docs/agents/ROSTER-ARCHIVE.md.
Lead session: session_014FBi6o334DvwT5Uw2kDfoN, environment env_013N6DGgsLr96BMjKj1hpw9i, branch claude/vibrant-johnson-nxvvxo.
Effort note (2026-11-12, D21 / L51): create_session now takes effort; new sessions run on claude-fable-5-2 at xhigh, running Opus lanes switch at their next park.
Prices per Mtok in/out (platform docs, 2026-10-14): fable-5-1 $10/$50, opus-5-5 $4/$20, sonnet-5-5 $2/$10, haiku-5-5 $0.10/$0.50.

| Role | Session id | Branch | Model | Effort | State | Reason |
| --- | --- | --- | --- | --- | --- | --- |
<ROSTER ROWS: rewritten at landing from get_session per id>

## In flight (as of <DATE> <HH:MM>Z)
- R131 LANDED <HH:MM>Z (landing commit <sha>; CHECKER C148 <checker>; CI <run>). CHECKER Add. 2 on the landed entry: <state>.
- Deferred, not routed (each needs the owner's direction first): second review of P-N5-KEY1P (claude/l-new 44775605; first review all SIGNED, claude/referee a85626aa); L-SI box 108 (independent proof of L(G_k) = 2^k − 2, claude/l-si 8c062914: ONE referee's check, REFEREE-2 42, claude/referee-2 e643672d; not a two-referee result); L-FORMAL (NoFault statement d6624d10; KeyRule scratch; a Lean statement of EXP-IDEAL is possible: the family is rule-built and the proof is a finite induction); L-RED 71.
- Every lane is parked with a handover note on origin, except OWNER-DESK (idle between owner messages) and WATCHDOG (cron).

## Findings to carry
- C1 (REFEREE-checked, a data point, not M3): w(2,6)=3 < 4=s(2,6) in E, S, V; w^V(3,6)=6 < 7=s^V(3,6). Weak separators can be strictly smaller than strong ones.
- Landscape doc corrections (L-LIT, docs/lit/BARRIERS.md): d = O(log n) poly result is Jurdzinski-Lazic Thm 7 / Fearnley et al., not Calude et al.; upper-bound exponent is Jurdzinski-Lazic's; attractor-decomposition barrier is formally only Arnold-Niwinski-Parys Thm 5.1; Two Counters bound partly empirical; Random-Facet parity lower bound withdrawn (arXiv 1410.7871).
- Oink mspm at 8fbf0a7 is wrong on some games (crash at mspm.cpp:486; one answer rejected by Oink's verifier); excluded from agreement claims. Instances: experiments/harness/regressions/ (l-comp).
- PGSolver SI families (switchallexp, switchbestexp) target PGSolver's switch-all/switch-best SI, not Oink psi/ssi; port of stratimpralgs.ml queued in L-COMP.
- G_k (L-RED-B 5; rule R, experiments/red-b/gk.py at claude/l-red-b): the first family with exponentially many IDEAL steps; outside R110's 2-wide class 𝓛^R_d, which is why R113 / R120's polynomial bounds did not exclude it. Obstruction RIPPLE: unit j answers each move of unit j + 1 twice (P_(k−1) = 3, P_j = 2·P_(j+1) + 1, L = 2·P_2), a binary counter built from block pairs with observer pairs.

## Live approaches
- A2 attractor/partial solvers (L-ATTR, PARKED): T-A1 is M3 (RESULTS R2). psolC (HKP DTR15-4) measured (l-attr 02174e2): complete on all n<=3, partial on 1,380 of 27.3M n=4 games; solves 9/13 M1 families completely (incl. the 3 that defeat Zielonka and both Friedmann SI families), 0% on tc/tc+/counter_symsi/counter_rr. Smallest failure n=4 m=6 (psolc_min_n4_m6.pg): weak-parity prefix-minimum trap. Not an M4 route: DE3 (REFEREE R-psolC FAITHFUL, referee 1600917).
- A3 non-adaptive SLP lower bounds (L-LOWER): B_1(1..5) = 0,2,4,6,8 = 2n-2 (90f6928); B_2(1..4) = 0,2,4,7 (d00349a; n=4: UNSAT k=6 on a 400-game core, 7-gate witness checked on all 12.96M games; min depth 6, so cost > depth). Data only, unrefereed. T-L1 parked (data against). CDHL SODA'18 says nothing on games; adaptive two-player Büchi is Omega(n)..O(n^2) (CSL'17 Lemma 27). Next: T-L2 theory box 12h (successor): human proof of B_2(4) >= 7 from the core; does the argument grow with n? Kill criterion in notebook.
- A1 deterministic weak separators (L-STRUCT, PARKED 22:00Z): outside the strong-separator barrier (T4). Products: DE2 (T1 refuted), L4 (first referee OK), T3 data conjecture (w=s for d<=n+1, all cells to (4,5) V). Algorithmic quantity is the diagonal w^V(n,n) (REFEREE d96b686). Diagonal W=S=1,2,5,7 for n<=4 confirmed by three independent encodings (L-STRUCT, L-COMP LRAT, REFEREE b4a711c); TARGET alphabet n=2,3,4 also w=s; gaps only at d >> n. S3 to be framed as 'w=s on the TARGET alphabet' (barrier direction). Data: w=s on most small cells; w<s at (2,6),(2,10),V(3,6); s(2,2h)=h+1 but w(2,8)=w(2,10)=4. Lower-bound target T1 likely false; now measuring growth of w in d.
- N5 family (L-NEW, L-SI, L-RED, L-RED-B, L-COMP, L-LOWER, L-FORMAL; 2026-10-22 to 2026-11-13): CLOSED as a route to M4 by R131. What stays usable: the one-player reduction (R104 IDEAL model, R117 REACH3, R124 EXACT-L), the wrapper (R130 Lemma WRAP) and the family G_k as test instances for any future strategy-improvement candidate.

## Dead approaches (with obstruction): see docs/RESULTS.md "Dead ends"
- DE1 arXiv 2511.03752 (BROKEN, 4-vertex counterexamples). DE2 T1 weak-separator lower bound (refuted at (2,10)).
- N5 (SSI-GLOBAL) from S3: R131 (G_k, 2^k + 1 iterations, obstruction RIPPLE). N5′-xi: R130 (W-FLAT). N5-SF: DE35. Older: DE1-DE37 in the «Dead ends» section of docs/RESULTS.md.

## Best result so far
- M3: RESULTS R2 [refereed-only] T-A1, psolB solves G completely iff PA**(G) (L-ATTR; both referees signed 57a1515).
- M3-type: RESULTS R3 [refereed-only] original Random-Facet on parity games, e^Omega(sqrt n) expected switches (L-RED; CHECKER 068f9de).
- RESULTS R1 [refereed-only]: L4, s^V(n,n) >= n^Omega(lg n) (supporting lemma, not M3 per L7).
- Algorithmic: no polynomial algorithm (M4). The fleet's own candidate N5 is refuted as a polynomial algorithm (R131). Known: quasi-polynomial upper bounds. Best results stay R2 (T-A1) and R3 (Random-Facet lower bound).

## Owner questions open
- Q14 (<DATE> <HH:MM>Z, OPEN): N5 is dead (R131). What should the fleet work on next? Options put to the owner: (a) stop here and write the final report (docs/HUMAN-REVIEW.md packet: what is proved, what is refuted, what is open); (b) formalize the kill in Lean (L-FORMAL: EXP-IDEAL on R104's definitions), so that the main negative result is machine-checked; (c) a new candidate under D14 (L-NEW's own untested approaches; the Lead's estimate: low odds, every standard strategy-improvement rule has a published exponential family); (d) the lower-bound side (A3, L-LOWER: non-adaptive SLP bounds) or the older A_DTL route (GAP-A, GAP-C). Until the owner answers: no new lane, no new spend beyond closing the landing.
- Q11 (2026-10-16 02:10Z, CLOSED by D8 06:50Z: option (b), Opus 5.5 until the Fable reset): Fable weekly limit reached; L-ALG and L-RED (DTL proof and attack) paused until 2026-10-21 21:00Z; referees (Fable) also unavailable. Options: (a) wait for the reset (default under D7, Lead recommendation); (b) continue L-ALG/L-RED on Opus 5.5 now (attack lanes below most-capable model, D1; referees still wait); (c) owner adds usage credits (spend, owner only).
- Q3: DONE by owner 07:53Z (setup script set; applies to sessions started after it; verify on the next new session). Q2, Q4, Q5, Q6, Q7 closed (D4, L13-L17). No blocking owner questions open. Q10 CLOSED 11:12Z (Lead reading): author preprint of "Solving Parity Games, Very Slowly" opened by L-LIT (T17, tvandijk.nl/pdf/2024festschrift.pdf, sha256 8e36c373..); not diffed against the Springer version.
- Q12 CLOSED 16:40Z by D11 (owner: "No contact for now"); L30: no contact with the author.
- Q13 CLOSED 16:39Z by D10 (owner: "I dont mind the repistory is public"); L29: repository stays public.

## Spend
- 2026-10-24 12:30Z partial reading (cost_usd, cumulative, get_session per id, sessions active since 10-22): Lead $506, OWNER-DESK $159, CHECKER succ. 3 $39, L-NEW succ. 8 $32, REFEREE succ. 3 (Fable) $31, L-RED succ. 13 $24, REFEREE-2 succ. 3 (Fable) $22, L-NEW succ. 9 $11. isUsingOverage false on all. Older sessions unchanged since their last reading; the full total was last summed 10-18 (≈ $2,050 then).
- 2026-10-18 13:47Z partial reading (get_session on the sessions active since 04:00Z; others unchanged since the 04:00Z full
  reading of $1,950 on 38 sessions): Lead $330 (+26), OWNER-DESK $63 (+10), L-ALG succ. 8 $30, L-ALG succ. 9 $21, L-NEW $28,
  L-RED succ. 7 $19 (parked 03:58Z), L-NEW succ. 1 and L-ALG succ. 10 about $1 each (just started). L-RED succ. 8's usage
  field is STALE ($1.02 since 09:00Z, as seen once before for L-RED succ. 6), so its spend is not measured. Lower bound on the
  total: about $2,040-2,060 plus L-RED succ. 8. isUsingOverage false on every session read; seven_day "allowed_warning".
- 2026-10-17 19:51Z readings (cost_usd, cumulative, get_session per id, 36 sessions): total $1,781 (sessions created ≤ 2026-10-15: $1,242;
  created after: $539; readings are cumulative per session, so spend per day is not measured; since the 10-15 reading the
  total rose by about $1,089 (≈ 2.2 days, almost all Opus under D8/D12)). Largest: Lead 277, L-RED (old) 127, L-LIT 109, L-ALG succ. 6 87, L-SI 77,
  L-ALG succ. 3 76, CHECKER 72. Working now: Lead, L-ALG succ. 7 (7.5), L-RED succ. 6 (0.8). isUsingOverage false on all 36;
  seven_day "allowed_warning"; the two paused Fable sessions are "rejected" (Fable limit), resets 2026-10-21 21:00Z; D7 applies.
- Earlier reading 2026-10-15 14:55Z: sum about $692 (see git history).
