# Parity games fleet: read this first
A research fleet on the question in TARGET.md: can parity games be solved in polynomial time?
One Lead routes; each lane owns one line of work. The owner (human) decides scope, spend and anything external.
Playbook: docs/sources/fleet-playbook.md. Literature map (secondary source): docs/sources/landscape-2026.md.

## Where the truth lives, in order
1. TARGET.md (only the owner changes it). 2. docs/NOW.md. 3. docs/DECISIONS-INDEX.md.
4. docs/GAPS.md. 5. docs/RESULTS.md. Notebooks (notes/), logs and docs/decisions/ are history, not truth.

## Hard rules
- A claim is a result only when Lean checks it (no sorry, allowed axioms only) or two referees signed it with its gaps listed.
- Every algorithm claim runs the gauntlet in TARGET.md section 5. Failing any step makes it a dead end.
- Every theorem statement is diffed against TARGET.md before it lands.
- Every cited result has an opened source (arXiv id or DOI, theorem/section number) in your notebook. The landscape doc is never a source by itself.
- Record every dead end with the exact obstruction and the instance that killed it.
- Edit only your lane's files. Never rewrite pushed history (no rebase, amend, force-push). No pull requests.
- Push only when scripts/verify.sh passes, chained: `scripts/verify.sh && git push -u origin <your-branch>`.
- Quote the owner's rulings verbatim (docs/DECISIONS.md). A reading is labelled "Lead reading".
- Never publish, post, email, submit or contact anyone outside the fleet. No secrets in any session.
- Report outcomes faithfully: failures with their output, skipped steps named as skipped.
- End every task with DONE (SHAs, evidence) / FINDINGS (one line each) / NEEDS (<owner>: <ask>).

## Messaging
- Lanes talk only to the Lead, via send_message to the Lead session id in docs/NOW.md. First line: "From <ROLE> (<UTC time>):".
- Messages are self-contained: SHAs, files, what was done, what is needed.

## Files each lane owns
- notes/<LANE>.md (notebook: resume point, queue, sources opened, dead ends, things only I know).
- L-LIT: docs/lit/. L-COMP: experiments/ (except experiments/weak-sep/, experiments/attr/, experiments/lower/), scripts/setup_oink.sh. REFEREE: docs/referee/. L-FORMAL: lean/.
- L-STRUCT: docs/struct/, experiments/weak-sep/.
- L-ATTR: docs/attr/, experiments/attr/.
- REFEREE-2: docs/referee-2/ (independent second referee; reads docs/referee/ only after its own report).
- L-LOWER: docs/lower/, experiments/lower/.
- L-ALG: docs/alg/, experiments/alg/ (algorithm design loop; reads experiments/attr/ and experiments/harness/, does not edit them).
- CHECKER: docs/checker/ (landing gate: exact-commit re-runs and statement diffs).
- HUMAN-DESK: docs/HUMAN-REVIEW.md (packet for a human expert; owner decides any contact).
- OWNER-DESK: docs/owner-desk/ (owner Q&A; open owner questions; relays owner words to the Lead verbatim).
- Lead only: CLAUDE.md, TARGET.md (drafts; owner approves), docs/*.md, docs/agents/, scripts/verify.sh, .github/.

## Commands
- scripts/setup_oink.sh   build Oink (pinned) into tools/oink/build (gitignored); generators tc, tc+, counter_*, rngame live there.
- scripts/verify.sh       the gate: doc shape, Lean (when present), experiment checks, Oink smoke. Prints PASS/FAILED/NOT RUN per step.

## Traps
- Oink's OINK_BUILD_TOOLS target (test_solvers) needs Boost >= 1.86; setup_oink.sh turns it off.
- Count arithmetic on big numbers at its bit cost (TARGET.md section 3). Unit-cost big integers fake polynomial time.
- A "counterexample" from an unfaithful implementation is not a counterexample: the referee checks pseudocode against the paper first.
