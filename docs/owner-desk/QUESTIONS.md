# Owner questions (OWNER-DESK; most decision-relevant first)
Standing instruction D15 / L37 (2026-10-22): the owner is NOT asked option, model, allocation or reassessment questions; the Lead
decides and reports. Still the owner's: TARGET.md changes; anything external (D11); paid overage (stop and tell); restart after an
owner "stop"; more than 5 working sessions. Reports continue as information only.
Standing Lead reading L12 (D4): the fleet decides process, method and result classification itself; the owner is asked only about
scope, spend, anything external, and TARGET.md.
Source: docs/NOW.md "Owner questions open" (trunk d580fcd) and the Lead's brief to OWNER-DESK (2026-10-15).
Each question is answerable in a word or a line. Owner answers are logged verbatim in docs/owner-desk/LOG.md and relayed
verbatim to the Lead; the Lead records rulings (D-numbers) in docs/DECISIONS.md and then this file marks the question closed.

## Q5: access to the published HKP chapter (LNCS 9560)
- id: Q5
- Background: the fleet's M3 result T-A1 (docs/RESULTS.md R2, [refereed-only], both referees signed at l-attr 57a1515,
  CHECKER PASS checker 62cf1c4) characterises exactly which games a known partial solver, psolB of Huth, Kuo and Piterman (HKP),
  solves completely. All checking used the arXiv version of HKP's paper (arXiv 1405.0386v2). The published version, "Static
  analysis of parity games: alternating reachability under parity", LNCS 9560 (2016), pp. 159-177, has not been opened by anyone
  in the fleet (no Springer access). Gap G10 of R2 is T-A1's dependence on HKP's proofs of Thm 7, Thm 8 and Lemma 5 (re-derived
  informally by both referees). The literature check (L-LIT T10, l-lit 1f9e9f8) rated T-A1 NEW, with the caveat that the published
  chapter could contain changes. Any external "first" or novelty claim needs the published version opened first.
- Options: (a) the owner provides the PDF, or reads those sections (Thm 7, Thm 8, Lemma 5, and whether psolB/Thm 4 changed) and
  reports; (b) leave G10 open; T-A1 stays internal-only.
- Lead recommendation: (a), when convenient.
- What changes: (a) L-LIT/referees compare the chapter with arXiv v2; G10 can close and the novelty caveat on R2 can be lifted (or
  revised if the chapter differs). (b) nothing changes now; R2 keeps its caveat and no external step is possible.
- Urgency: low while no external step is planned; it blocks Q6's natural next step.
- Status: closed, Lead reading L17 (trunk 4fb2884). L-LIT T11 (docs/lit/T11-HKP-DTR15-4.md, l-lit 933dc12; trunk 16943fa) read
  DTR15-4 in full: very likely the chapter's text up to copy-editing (its 29 references match the chapter's Crossref record entry for
  entry); agrees with the desk's points (1)-(4). T-A1 stays NEW. R2's caveat now records the chapter as read through its
  pre-publication text; the Springer pages matter only for a "first" claim leaving the fleet (owner's call). G10 is not an owner
  question. Side product: psolC, a new candidate (not started); PA** is strictly inside psolC's completely-solved class
  (L-LIT derivation from T-A1, T-A1' and DTR Thm 4; not refereed; T-A1' rests on G11's referee-level repair).

## Q6: whether, and to whom, docs/HUMAN-REVIEW.md goes
- id: Q6
- Background: HUMAN-DESK wrote a review packet for a human expert (docs/HUMAN-REVIEW.md on trunk; packet at human-desk 3b3bdde)
  presenting T-A1 and L4 for outside eyes. The fleet never contacts anyone outside itself (D1: "Anything external is my
  decision."). Whether the packet goes to anyone, and to whom, is the owner's decision alone.
- Options: (a) owner reads it, then decides a recipient; (b) owner reads it, holds; (c) do not distribute.
- Lead recommendation: the owner reads it first, and holds any contact until Q5 closes G10.
- What changes: (a) the owner contacts the recipient personally; the fleet only revises the packet on request. (b)/(c) nothing
  external happens; HUMAN-DESK stays parked.
- Urgency: low; owner's timing.
- Status: closed, D4 / Lead reading L13 (trunk 1f34679): no external distribution; the owner is the packet's only reader, via
  OWNER-DESK. Owner-relevant points shown in session 2026-10-15 ~07:55Z.


## Q7: does L4 count as an M3 result?
- id: Q7
- Background: L4 (docs/RESULTS.md R1, [refereed-only], double-refereed: referee 9bf5301, referee-2 d76c9e1; CHECKER PASS checker
  62cf1c4) proves that strong separators over the vertex-priority alphabet need n^Omega(lg n) states. It follows from a known
  separator lower bound (Czerwinski et al., arXiv 1807.10546 Thm 5.1) plus a conversion that Parys-Wiacek (2305.00308 p.2) state
  without proof. Lead reading L7: L4 alone is a supporting lemma, not M3; the M3 credit is T-A1.
- Options: (a) confirm L7 (L4 is a supporting lemma); (b) count L4 as M3 as well.
- Lead recommendation: (a), confirm L7.
- What changes: (a) the ledger stays as is. (b) R1 is relabelled M3; reporting lists two M3 results.
- Urgency: low; labelling only, no work depends on it.
- Status: closed, D4 / Lead reading L14 (delegated by the owner; trunk 1f34679): L7 stands; L4 is a supporting lemma, not M3.


## Q4: run the original PGSolver binaries once?
- id: Q4
- Background: for M1 (reproducing published hard families) L-COMP built PGSolver (tcsprojects/pgsolver d3cd624), but the session's
  permission classifier refused to run the binaries, so the hard-family generators and the strategy-improvement loop were ported to
  Python. REFEREE checked the ports against PGSolver's source; Lead reading L5 records M1 on that basis. A small fidelity caveat
  remains: the ports were never diffed against the original's output.
- Options: (a) allow running the original binaries once, to diff the ports against the original; (b) keep port plus referee check.
- Lead recommendation: (a). It is cheap and removes the caveat.
- What changes: (a) a successor L-COMP session (or the Lead) is permitted to run PGSolver binaries; one diff run; caveat removed
  or a port bug found. (b) M1 stands on the referee check; caveat stays.
- Urgency: low.
- Status: closed, D4 / Lead reading L15 (delegated by the owner; trunk 1f34679): no spawn for it; the next L-COMP successor runs
  the PGSolver binaries once to diff the ports; if the classifier refuses, ports plus REFEREE check stand (L5).


## Q2: trunk branch name
- id: Q2
- Background: the fleet's trunk is the Lead branch claude/vibrant-johnson-nxvvxo (Lead reading L2), in place of the playbook's
  `main`. The fleet opens no pull requests (CLAUDE.md), so the name is cosmetic.
- Options: (a) keep claude/vibrant-johnson-nxvvxo; (b) create `main` for readers.
- Lead recommendation: (a), unless the owner wants `main` for readers.
- What changes: (a) nothing. (b) the Lead creates `main` from trunk and updates CLAUDE.md/NOW.md references; lanes merge there.
- Urgency: none.
- Status: closed unless the owner objects, D4 / Lead reading L16 (trunk 1f34679): keep claude/vibrant-johnson-nxvvxo.


## Q3: environment setup script
- id: Q3
- Background: each new session spends about a minute installing Boost dev packages and Python packages and building Oink.
  The claude.ai environment settings (only the owner can change them) accept a setup script that runs when a session starts.
- Options: (a) add the script below to the environment's setup script; (b) leave as is.
- Lead recommendation: (a), yes.
- Proposed script (built from scripts/setup_oink.sh and .github/workflows/verify.yml at trunk d580fcd):
  ```bash
  #!/usr/bin/env bash
  set -e
  apt-get update -q
  apt-get install -y -q libboost-filesystem-dev libboost-iostreams-dev libboost-regex-dev libboost-random-dev
  python3 -m pip install python-sat==1.9.dev15 numpy==2.5.3
  ```
  Oink itself is built into the repository checkout (tools/oink, gitignored), so the build step stays in the session:
  `scripts/setup_oink.sh` (idempotent). If the owner prefers it in the setup script too, append
  `cd <repo checkout> && scripts/setup_oink.sh` with the checkout path the environment uses. Note: python3 -I (used by
  experiments/*/check.sh) ignores the user site; if pip installs to the user site, add `--break-system-packages` and run as root.
- What changes: (a) sessions start with dependencies present; fewer install steps and permission prompts. (b) nothing.
- Urgency: low; convenience.
- Status: done 2026-10-15 (owner: "I did Q3"). Applies to sessions started after it was saved; the first new session's
  setup log is the confirmation. Oink build stays in-session (Lead).


## Q8: shift effort toward algorithm (upper-bound) lanes?
- id: Q8 (raised by OWNER-DESK 2026-10-15 09:47Z after the owner's D5 message)
- Background: after D5 the only active attack lane was L-LOWER (lower bounds); no lane was building an algorithm.
- Options: (a) add algorithm lanes, L-LOWER continues; (b) add them and pause L-LOWER; (c) no change.
- Status: answered by the Lead's reading of D5 (L18, trunk dc8e41b): M4/M4-R is the primary aim; new lane L-ALG (falsification-driven
  design loop, 12 h box from ~10:00Z); L-LOWER finishes its box to 20:36Z. Open follow-ups for the owner, only if wanted: a second
  algorithm lane, a strategy-improvement design lane, a spend ceiling.
  Owner answer 2026-10-15: "a". CLOSED: D6 / Lead reading L19 (trunk 62388b3): L-LOWER continues; second algorithm lane
  L-SI (strategy-improvement rule design) added beside L-ALG; at the D1 5-session cap (owner can raise it); no spend ceiling (D1 policy).

## Q9: spend pace until the weekly allowance resets (TIME-SENSITIVE)
- id: Q9 (from the Lead, 2026-10-15 12:05Z)
- Background: at 12:02Z every fleet session reports the seven-day rate-limit window at status "allowed_warning" (not overage).
  The weekly allowance resets 2026-10-21 21:00Z (~6.4 days). D1: on paid overage, stop the fleet and tell the owner. At today's burn
  the weekly cap or overage could come well before the reset. Burn (Lead's figures): Fable lanes L-ALG $24.8, L-SI $29.1, L-LOWER
  successor $21.1, L-RED (new, not yet reported); Lead $69.1. D1 requires Fable for attack lanes and referees.
- Options: (a) continue at the current rate; accept a pause at the weekly cap until 10-21 21:00Z; stop at once on overage (D1).
  (b) throttle: current boxes finish (L-RED ~19:20Z, L-LOWER 20:36Z, L-ALG 21:55Z, L-SI ~22:10Z); then at most 2 working lanes
  until the reset, prioritised by live M4 candidates. (c) pause now: lanes write handovers and park; the Lead keeps hourly checks only.
- Lead recommendation: (b).
- Interim default until the owner answers: no new sessions or boxes; running lanes finish their boxes; one exception, a single
  referee check of L-RED's Random-Facet transfer lemma.
- Urgency: high (spend).
- Status: closed, D7 / Lead reading L20 (trunk 3a83f8b): the owner answered "a" directly in the Lead session (continue at the
  current rate). D1 overage rule still applies: on paid overage the fleet stops and the owner is told.

## Q10: van Dijk's 2024 chapter "Solving Parity Games, Very Slowly" (optional, not blocking)
- id: Q10 (raised by the Lead via L-LIT T16; listed in docs/NOW.md, not routed through this desk)
- Background: DTL (candidate C5) is van Dijk's unpublished solver; his 2024 chapter may describe it or its counterexample.
- Options: owner provides a copy if they have access; otherwise the fleet proceeds without it.
- Status: closed 2026-10-16 11:12Z (Lead reading): L-LIT T17 opened the author's preprint (tvandijk.nl/pdf/2024festschrift.pdf);
  not diffed against the Springer version.

## Q11: Fable weekly limit reached (2026-10-16 02:10Z)
- id: Q11 (asked and answered in the Lead session, not via this desk)
- Status: closed, D8 / Lead reading L27 (owner, ~06:50Z): option (b), L-ALG and L-RED continue on Opus 5.5 until the Fable reset
  2026-10-21 21:00Z; referees not engaged before the reset without asking the owner (D1 "Never downgrade the referee").

## Note on Q4 (closed under D4/L15)
- Done 2026-10-15 23:28Z (l-comp 70cc344): PGSolver d3cd624 binaries ran once; 27/27 generators byte-identical to the ports;
  switch-all/switch-best iteration counts and solutions identical. The M1 fidelity caveat is removed.

## Q13: the repository is PUBLIC (owner attention)
- id: Q13 (Lead, 2026-10-16 11:12Z; desk re-verified 16:3xZ: github.com page HTTP 200 without login, API "private": false,
  "visibility": "public")
- Background: nano44/parity_games_challange is publicly readable, so everything pushed since 2026-10-14 is public: results,
  unrefereed drafts, docs/HUMAN-REVIEW.md (Q6 ruled no external distribution), and the owner's rulings quoted verbatim in
  docs/DECISIONS.md and docs/owner-desk/LOG.md. It also appears in GitHub code search (L-LIT T17). Visibility is the owner's
  decision; the fleet changes nothing.
- Options: (a) keep public; (b) owner makes it private (GitHub > repository Settings > General > Danger Zone > Change visibility).
- Lead recommendation: none stated. Desk note: (b) matches D1 ("Never publish ...") and the Q6 ruling; copies already indexed or
  cloned cannot be recalled.
- Urgency: high (every push adds to what is public).
- Status: closed, D10 / Lead reading L29: repo stays public; pushing is not "publishing" under D1; every other outward act
  (posting, emailing, submitting, contacting, announcing or linking the repo) still forbidden; nothing sensitive is ever committed;
  HUMAN-REVIEW.md readable in the repo is accepted; Q6 (no external distribution by the fleet) unchanged.

## Q12: contact van Dijk for counter_dtl?
- id: Q12 (Lead, 2026-10-16 11:12Z; not blocking)
- Background: L-LIT T17 found no copy of the author's DTL counterexample anywhere online (it was announced in Oink's README in
  2021 but never committed). The only remaining route is to ask the author: outside contact, the owner's decision (D1).
- Options: (a) no contact for now; (b) owner contacts the author; (c) owner authorises a fleet-drafted message for the owner to send.
- Lead recommendation: (a): L-RED first builds the author's own recipe (preprint p.15).
- Status: closed, D11 / Lead reading L30: no contact with the author; the fleet works from the public record and its own
  constructions. Note: the p.15 recipe was already built (L-RED R14, l-red d70e99a): no slowdown on A_DTL.

## Q14: L32 reassessment of the DTL polynomial bound (GAP-A) — DECISION NEEDED
- id: Q14 (Lead, 2026-10-18 04:08Z; full text docs/agents/L32-REASSESSMENT.md at trunk 8a09d9f)
- Background: L32's trigger is met (both lanes' boxes ended with no new GAP-A reduction). Criterion NOT met: R7-R14 reduce GAP-A only
  to statements the referees judged equivalent to it; every constant/local premise is false on a uniform family (DE19-DE21). No stop
  condition: no incorrect run, no super-polynomial family (strongest family needs D+8 iterations). DTL stays an open candidate; the
  open core is (LONG-PHASE) = GAP-A itself. All lanes parked; nothing running. Spend $1,950 total, no overage.
- Options: (a) bank the refereed results and write up DTL's status as an open candidate (one document for the owner, no external
  contact); (b) keep only the cheap adversarial lane on GAP-A, no proof lane; (c) a new candidate or approach (needs an owner direction).
- Lead recommendation: (a) now, plus (b) until the Fable reset 2026-10-21 21:00Z, then stop unless (b) finds a long-phase family.
- Urgency: decision needed; the fleet is idle until the owner chooses.
- Status: closed, D13 / Lead reading L34: DTL continues on both sides (L-ALG proof, L-RED attack) at the D7 rate; (a) not chosen;
  (c) needs a direction (Q15); next reassessment at the Fable reset 2026-10-21 21:00Z.

## Q15: direction for option (c), run alongside DTL (one lane, Opus until the reset)
- id: Q15 (Lead, 2026-10-18 08:57Z; D1 "Spawn no attack lane before I approve it")
- Options: A. strategy improvement rules S5/S6 (Zadeh/Cunningham with index tie-breaks; only SI rules neither killed nor defended;
  cheap, fast verdict, likely negative). B. deterministic weak separators (rank 1; diagonal at n = 5 and growth; high leverage, low
  probability, SAT-heavy; better on Fable after the reset). C. lower bounds for symbolic algorithms (negative direction; no algorithm).
  D. Lead's choice.
- Lead recommendation: A now, then B after the reset.
- Status: closed, D14 / Lead reading L35 (trunk ff4e60c; owner addendum: the fleet may test untested approaches and its own ideas):
  new lane L-NEW (Opus) - kill test of S5/S6, then up to three own untested approaches; weak separators queued after the Fable reset.

## Q16: early L32 reassessment of DTL (decision requested)
- id: Q16 (Lead, 2026-10-18 22:29Z)
- Background: L-ALG tried the last two GAP-A proof routes; both failed at a named step (docs/alg/GAP-A-STATUS.md); L-ALG parked.
  L-RED disproved five statements those routes rested on within an hour (pinned games n = 20-63, Lead re-ran). DTL never wrong, no slow
  family; R4-R14 stand; L-RED: kills close proof routes, not steps to a lower bound. Open: (CTX+), needs a compounding counter.
  N5 ((c) lane): steps 2-3 passed with caveats; second implementation agrees; six killer attempts failed; termination repaired
  (unrefereed); no running-time proof.
- Options: (a) bank and write up DTL as an open candidate (mostly done); (b) keep only the cheap adversarial lane on DTL (compounding
  counter), no proof lane; (c) put the effort into a new approach (N5 already running). Or a combination / own direction.
- Lead recommendation: (b) + (c): L-RED on the counter, DTL proof lane parked, proof effort to N5 gauntlet step 4; re-ask at the
  Fable reset 2026-10-21 21:00Z. Until answered, D13 continues as is.
- Addendum (Lead, 2026-10-19 00:21Z): R15 [refereed-only] landed: N5 always terminates (two referees, CHECKER); repairs a strictness
  claim in Voege-Jurdzinski 2000 that fails at cycles. N5 running time reduced (unrefereed, K9) to (P) polynomial one-player SI and (CH)
  polynomially many opponent best-reply changes; referees checking; L-NEW on (P).
- Addendum 2 (Lead, 2026-10-19 03:32Z): R16 [refereed-only, Opus D12] landed: on the one-player-like subclass C^1P, DTL searches
  <= n^O(d) with d = NEST*; GAP-A there reduces to ONE named statement (NEST*-BOUNDED), no proof route (L32 half met); data max 3.
  Lead recommendation updated: (b)+(c) plus a proof attempt on (NEST*-BOUNDED). Fleet paused 2026-10-19 ~03:33Z-2026-10-21 21:00Z
  by the weekly cap (no overage); reassessment point reached at the reset.
- Status: closed, D15 / Lead reading L37 (trunk 0f33c77): DTL adversarial side only (L-RED), no DTL proof lane, NEST* proof attempt
  dropped; main effort (c) under D14 (N5, untested approaches incl. weak separators).

## Q17: Jens Voege's PhD thesis (optional)
- id: Q17 (Lead, 2026-10-19 00:21Z; optional, not blocking)
- Background: statement (P) (polynomial one-player strategy improvement) is stated without proof in Voege-Jurdzinski 2000 Prop. 7.4;
  Friedmann's thesis attributes a proof (switch-all only) to Voege's PhD thesis (RWTH Aachen, 2000). The host refuses access from the
  fleet's container.
- Ask: if the owner can obtain a copy, place it in the repository (any path) and tell OWNER-DESK; L-LIT checks the proof. The fleet
  contacts no one.
- Status: closed, dropped (Lead, L37): not needed; would require an external act by the owner.

## Q18: which models after the reset (D8, D12 were tied to it)
- id: Q18 (Lead, 2026-10-21 21:06Z)
- Options: (a) back to Fable 5.1 for new lanes and referees, as before D8; (b) stay on Opus 5.5 for lanes and referees; (c) Fable for
  referees, Opus for lanes.
- Interim (Lead reading L36): sessions cut off by the cap (L-RED on NEST*-BOUNDED, CHECKER on R16) finish on Opus; L-NEW resumes on its
  existing session; any NEW session starts on Fable 5.1; no Opus referee signs unless D12 is extended. Working sessions 3 of 5.
- Status: closed, D15 / L37: lanes and referees on Opus 5.5, labelled "(Opus 5.5, D15)"; R17's Fable signatures stand.
