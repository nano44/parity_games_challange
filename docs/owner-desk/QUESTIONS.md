# Owner questions (OWNER-DESK; most decision-relevant first)
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
- Status: open (optional).

## Q11: Fable weekly limit reached (2026-10-16 02:10Z)
- id: Q11 (asked and answered in the Lead session, not via this desk)
- Status: closed, D8 / Lead reading L27 (owner, ~06:50Z): option (b), L-ALG and L-RED continue on Opus 5.5 until the Fable reset
  2026-10-21 21:00Z; referees not engaged before the reset without asking the owner (D1 "Never downgrade the referee").

## Note on Q4 (closed under D4/L15)
- Done 2026-10-15 23:28Z (l-comp 70cc344): PGSolver d3cd624 binaries ran once; 27/27 generators byte-identical to the ports;
  switch-all/switch-best iteration counts and solutions identical. The M1 fidelity caveat is removed.
