# Open owner questions (OWNER-DESK; most decision-relevant first)
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
- Status: answered, verdict pending L-LIT T11 (Lead, 2026-10-15 07:55Z). The owner supplied Imperial DTR 2015/4, public at
  https://www.doc.ic.ac.uk/research/technicalreports/2015/DTR15-4.pdf (Lead re-verified sha256). Desk reading (pointer only):
  docs/owner-desk/HKP-DTR15-4-reading.md. Lead reading (to be logged in DECISIONS.md): if T11 finds DTR15-4 matches the chapter,
  R2's caveat becomes "checked against arXiv 1405.0386v2 and the pre-publication chapter text DTR15-4; Springer pages not opened"
  and Q5 closes; it reopens only on a discrepancy. G10 is not an owner question (it concerns HKP's arXiv proofs).

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
- Status: open

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
- Status: open

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
- Status: open

## Q2: trunk branch name
- id: Q2
- Background: the fleet's trunk is the Lead branch claude/vibrant-johnson-nxvvxo (Lead reading L2), in place of the playbook's
  `main`. The fleet opens no pull requests (CLAUDE.md), so the name is cosmetic.
- Options: (a) keep claude/vibrant-johnson-nxvvxo; (b) create `main` for readers.
- Lead recommendation: (a), unless the owner wants `main` for readers.
- What changes: (a) nothing. (b) the Lead creates `main` from trunk and updates CLAUDE.md/NOW.md references; lanes merge there.
- Urgency: none.
- Status: open

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
- Status: open
