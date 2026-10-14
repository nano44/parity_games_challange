# Claude Code Fleet Playbook

Oct 14, 2026 · @Nano

One Lead session in your chat routes about a dozen Claude Code cloud sessions on one GitHub repo. Each owns one area and works on its own branch. Every change passes an independent reviewer and an independent gate before the Lead lands it. All shared state lives in a few repo files, and every owner ruling is recorded word for word. The skeleton transfers to research, with one big swap: tests become machine-checked proofs and adversarial referees.

## At a glance

&#91;embedded content: fleet roles and the path of one change · 3 gates\]

Read it top down: the Lead assigns a task to a lane, W-REVIEW clears the lane's push, the Lead merges cleared lanes into a round, and main moves only when CI, W-REVIEW and W-GATE3 all pass on that same SHA. The dashed lines are the hourly checks that catch a stalled session.

## Roles

Every role is a separate Claude Code cloud session. Only the Lead and the guide ever talk to you; everyone else talks only to the Lead.

| Role | Count | Owns | Talks to | Lives on |
| --- | --- | --- | --- | --- |
| **Owner (you)** | 1 | Product, scope, money, legal, anything irreversible | Lead (status), guide (questions) | Your chat |
| **Lead** | 1 | Routing, rounds, landing on main, the state files, restarts, stop/resume | Everyone | Your chat; branch `claude/game-i0-audit-zdkr1f` |
| **Lanes** (A1-A6) | 6 | One code area each: sim, data/CI, client/iOS, art/audio, server, Apple/release | Lead only | One branch each |
| **Workers** | 6-8 | One job each: copy, a feature track, "feel", a spec | Lead only | One branch each |
| **W-REVIEW** | 1 | First-pass code review of every non-doc commit, and a check of every round | Lead only | `claude/w-review` |
| **W-GATE3** | 1 | Independent landing gate per round: full test run, migration rehearsal, browser journeys | Lead only | `claude/w-gate3` |
| **Watchdog** | 1 | Hourly liveness and overage check of every session; never edits anything | Lead only | No branch |
| **Guide** | 1 | Asks you every owner question, one at a time, and relays your answer verbatim | You and Lead | `claude/owner-questions-0927` |

Why split review and gate: the reviewer reads the change and plants faults to prove the tests catch them; the gate re-runs everything on the exact commit about to land. Neither wrote the code, so neither can grade its own work.

## Where the truth lives

Sessions cannot read each other's chats, and every session eventually compacts or is replaced, so anything not in a repo file is lost. Tests enforce the shape of these files.

| File | Holds | Rule that keeps it honest |
| --- | --- | --- |
| `CLAUDE.md` (root) | Facts true for weeks: layers, owners, hard rules, commands, traps | Kept short; a test caps its length |
| `<folder>/CLAUDE.md` | That area's invariants, entry points, traps | One per area; read on arrival |
| `docs/NOW.md` | Current state: phase, roster, what is in flight, rounds, owner questions | Rewritten, never appended; a test fails it over 150 lines |
| `DECISIONS.md` + `docs/DECISIONS.md` | Every owner ruling, quoted verbatim, with context and the Lead's readings | Append only; never restate a ruling stronger or broader |
| `docs/DECISIONS-INDEX.md` | One row per ruling with its current status (active, amended, superseded, reversed) | A test checks every ruling has a row and a valid status |
| `docs/KNOWN-ISSUES.md` | Every open defect or risk: id, severity, single owner, status, history | A test checks owners, severities and statuses; closed rows move to a closed list |
| `docs/<LANE>_STATUS.md` | Each lane's resume point, queue and "Things only I know" | Overwritten, about 100 lines |
| `docs/agents/LANE-RESTART.md` | The handover procedure, the five check questions, one row per restart | Row added per restart with the graded score |
| `docs/agents/LEAD-BACKSTOP.md` | The Lead's standing rules: sweep, overage stop, stop and resume | Read by the Lead at every hourly sweep |
| `docs/agents/LEAD-STATE.md` | History log (stop records, audits) | Append only; never treated as current |
| `docs/decisions/*.md` | Long analyses, review verdicts, gate reports | Linked from the files above, never pasted |

The order of trust is written into the root `CLAUDE.md`: NOW, then the index, then KNOWN-ISSUES, then the folder file, then design sources. Everything else is history.

## The pipeline

A change reaches production only through this path. Nothing skips a step, and the Lead never lands on its own judgement alone.

1. **Lane builds** on its own branch, only in files its lane owns.
2. **Local gate:** the lane runs `npm run verify` (14 steps: lockfile, lint, typecheck, build, tests, data, economy, budget, spec, audits) and pushes only if it passes, in one chained command.
3. **Handoff:** the lane reports `DONE` (SHAs, evidence), `FINDINGS` (one line each) and `NEEDS` (`<owner>: <ask>`) to the Lead.
4. **Review:** the Lead routes the SHA to W-REVIEW. It reads the diff, re-runs the tests, and plants faults (deliberately breaks the code) to prove the tests catch them. Verdict: OK, or CHANGES with numbered findings.
5. **Round assembly:** the Lead creates a worktree on `main`, merges each OK'd lane range with `--no-ff`, merges its own docs branch, and pushes `claude/round-HHMM`. Checks: each merge's `--remerge-diff` is empty, the lockfile changes only as planned, and every non-doc commit sits inside a reviewed range.
6. **Three gates on the exact SHA:** CI (7 jobs) plus iOS CI; W-REVIEW's round check; W-GATE3's independent gate (full verify, migration rehearsal live to round to rollback, browser smokes and journeys).
7. **Land:** fast-forward `main` to the round SHA, only when all three are green on that SHA.
8. **Deploy:** an owner-enabled workflow deploys every green landing (gate, build, deploy, live check). A deploy step refuses if `main` moved, so the next round lands only after the previous one is live.
9. **Record:** the Lead marks NOW live, closes or updates KNOWN-ISSUES rows, and tells the guide what reaches your phone.

To save time, the next round can be built on top of the one still gating, so `main` fast-forwards twice.

## Messaging and clocks

Sessions talk only through scheduled triggers (Routines). A message lands as a new user turn in the target session.

| Mechanism | How | Used for |
| --- | --- | --- |
| **Message** | `create_trigger` with `persistent_session_id` = the target and `run_once_at` 3-5 minutes ahead | Every Lead-to-lane and lane-to-Lead message |
| **Self check-in** | `send_later` into your own session | Polling a deploy, CI or a quiet worker; never a `sleep` loop |
| **Lead backstop** | Cron `1 * * * *` into the Lead | Hourly sweep: re-read NOW and LEAD-BACKSTOP, check the watchdog and lanes, act on exceptions only |
| **Watchdog** | Cron `30 * * * *` into the watchdog | Hourly: overage check, read every session's status, wake stalled ones, at most one message to the Lead |
| **Status read** | `get_session` per known id, never a list | Status, needs\_action, context size, overage flag |
| **CI status** | GitHub MCP `actions_list` | Runs and jobs per branch or SHA |

Message conventions:

- First line says who and what ("From the Lead (16:1xZ): round-1617 = 71f3c718").
- Self-contained: SHAs, files, what to do, what done looks like.
- Every finished task ends with DONE / FINDINGS / NEEDS.
- A message to a session that is mid-turn waits until that turn ends.
- Never `fire_trigger` with text (it can drop silently); never delete and recreate a trigger.

The watchdog and the backstop alternate on the half hour, so nothing goes more than about 30 minutes unwatched. Today the watchdog caught A5 idle for 92 minutes after announcing work it never started.

## The rules

Three lines sit at the top of the Lead's hourly prompt because they must survive even if the files are unreachable:

- **A measurement beats an inference**, and when an agent pushes back with one it is probably right.
- **A finding filed where its reader cannot see it has not been filed**, including when the Lead is the reader.
- **Never land a round with red tests in it.**

The rest, as written in the root `CLAUDE.md` and the Lead's rules:

1. **Edit only files your lane owns.** A change elsewhere is an ask to that owner, routed through the Lead.
2. **Never rewrite pushed history.** No rebase, amend or force-push on shared branches; merges only. No pull requests unless you ask.
3. **Push only on a passing gate,** chained in one command with git push's own answer.
4. **Quote owner rulings verbatim.** A reading of a ruling is labelled "Lead reading" and never stated stronger or broader.
5. **Escalate to you only for product, design, scope, legal, Apple or company matters, significant spend, or anything irreversible.** Everything else goes to the Lead. Every owner question goes through the guide (D160).
6. **Every round lands by fast-forward only,** after CI, the reviewer and the gate are green on the exact SHA.
7. **No deploy without your explicit OK.** Auto-deploy on a green landing exists only because you enabled it.
8. **Status docs are overwritten, not appended;** long analyses go in `docs/decisions/` and are linked.
9. **No secrets in any session.** No agent sees API keys or signing keys; guides never ask for passwords or codes.
10. **Report outcomes faithfully.** A failing test is reported with its output; a skipped step is named as skipped.
11. **Stop the whole fleet on overage,** and restart only on your word.

## Session lifecycle

A session that reaches about 760k tokens of context compacts on its own, mid-task. So each session is replaced on purpose at about 600k, at a natural pause (your ruling D43: "Do option 5 then").

1. **Handover (old session):** it overwrites its status doc with DONE, IN FLIGHT, NEEDS and a "Things only I know" section (traps, half-finished reasoning, who waits on what). It pushes and reports the SHA. From then on it is parked: it answers questions and pushes nothing.
2. **Spawn (Lead):** `create_session` on the lane's branch, `outcome_branch` = that branch, `clone_depth` 3000. The first prompt is the lane brief (below). No keys, no secrets.
3. **Handover check (new session):** it answers five questions from the repo, commits them to `docs/agents/handover-checks/<lane>.md`, pushes, and stops.
4. **Grade (Lead):** the Lead re-measures every answer against the repo. A miss means the gap gets written into the files before the new session starts work. Then a "go" with the first task.
5. **Record:** a row in LANE-RESTART, the roster in NOW, and the new id to the watchdog. The old session stays parked for a week; archiving needs your OK.

**The five questions:**

1. Your branch, its head SHA, and how many commits ahead of and behind `main`.
2. Your open work and the next step of each.
3. The KNOWN-ISSUES rows you own, with status.
4. The three owner rulings that most constrain you, verbatim, with their status in the index.
5. One trap that bit this lane before, and the check that now prevents it.

**The lane brief (first prompt):** "You are \<lane> (\<area>), replacing a parked session. First `git fetch` your branch and reset to it. Read the root CLAUDE.md, your folder CLAUDE.md, NOW.md, your status doc, and the index rows your status cites. Answer the five questions in LANE-RESTART.md, commit them, push, and stop. You own \<paths>. Push only to \<branch>. End every task with DONE / FINDINGS / NEEDS."

The reset line matters: fresh clones repeatedly started at an older SHA than the lane head. The Lead is the one exception: it compacts in place, because you talk to it and a new session would move your chat.

## Stop and resume

The fleet stops on overage, or when you say so (used twice: D158 and D167). The order matters, because an interrupted session is woken again by any message still queued for it.

**Stop:**

1. Write the STOP RECORD first, to `LEAD-STATE.md`: every roster session's id, status, needs\_action and resume point, plus every enabled trigger with its id and target. Commit and push.
2. `interrupt_session` on every roster session. Interrupt, never archive: nothing is lost. The guide stays up, because you talk to it.
3. Disable the watchdog's routine, and any one-shot message still scheduled to fire.
4. Tell you what stopped and that "RESUME" or "go" restarts it.
5. Last, disable the Lead's own backstop.

Your own routines that are not fleet (your daily Paris check) are never touched.

**Resume, only on your word:**

1. Re-enable the backstop, then the watchdog.
2. One message to each session that has live work; idle sessions get nothing, because a message only spends tokens.
3. Spawn successors the record says are due.
4. Record the resume as a ruling and in LEAD-STATE; read every session within the hour.

## Settings and environment

| Setting | Value here | Why |
| --- | --- | --- |
| Where sessions run | Claude Code on the web (cloud sessions), started by the Lead with `create_session` | Many sessions in parallel; nothing depends on your laptop |
| Repository | One private GitHub repo; every session has push access to it only | One source of truth |
| Branches | One per lane, worker and gate; the Lead's docs branch; `claude/round-HHMM` per round; `main` only by fast-forward | Each lane is landable alone; history never rewritten |
| Permission mode | `auto` for every session | Sessions run unattended; a denied action is a finding, not something to route around |
| Model and effort | One model for the whole fleet; effort `high` for lanes, `xhigh` for the Lead | Review quality matters more than speed |
| Environment setup script | Starts Postgres, creates the test database and role, installs pinned Python packages | Every new session can run the full gate |
| Environment variables | Test database URL only; no secrets | No agent ever sees an API or signing key |
| Network | Default allow-list through the cloud proxy | GitHub, npm, PyPI reachable |
| GitHub access | GitHub MCP tools for CI runs, jobs and logs | Sessions have no `gh` CLI |
| Clone depth | 3000 for every spawned session | Shallow clones showed phantom commits |
| CI | Required on every round SHA; auto-deploy on a green `main`, enabled by you | The gate the Lead lands on |
| Context policy | Planned restart at about 600k tokens; the Lead compacts in place | Avoids a mid-task compaction |

One recurring container problem: a container restart kills Postgres silently. Every session runs `pg_isready` before the gate and starts it once if it is down.

## Failures we hit, and the fix each got

Most of the rules above exist because one of these happened.

| Failure | What happened | Fix now in place |
| --- | --- | --- |
| Green locally, red in CI | A round was declared green on a local run while CI failed | CI on the exact SHA is the authority; the local gate prints PASS / FAILED / NOT RUN per step |
| Reports lost | Lane reports never reached the Lead | Every sweep reads each lane's status and branch head, not only its messages |
| Stalled sessions | A session ends its turn announcing work, then sits idle (A5, 92 min, today) | Hourly watchdog flags idle-but-not-done; the Lead re-sends a go |
| Mid-task compaction | Sessions near 760k context summarised themselves mid-task | Planned restart at about 600k with a graded handover |
| Old clone | New sessions started at an older SHA than the lane head | First line of every brief: fetch and reset to the lane branch |
| Over-claiming | The Lead cited the wrong SHA for a verdict and misnumbered a migration; reviewers caught both | Every claim carries a SHA; reviewers and the Lead re-measure, and corrections are filed |
| Stale rulings | Many rulings were later amended, and old versions got quoted as current | The index tracks each ruling's current status and is checked before any quote; readings are labelled |
| Tests that never ran | The gate's first step failed, no later step ran, and the output could not tell "passed" from "never started" | Gate output names every step; reviewers plant faults |
| Container restarts | Postgres died silently, so tests failed or skipped | `pg_isready` before every gate |
| Landing during a deploy | Landing a second round mid-deploy would have broken the first | Land the next round only after the previous live check |
| Branch name collision | `claude/round-1500` already existed from an older day | Check the remote before naming; never overwrite |
| Cost surprises | The fleet ran into paid overage once (10-06, about 12 minutes) before anyone saw it | Overage watched hourly; one-command stop with a record |

## Scale and cost

Measured 2026-10-14 from the repo and from the sessions' own records, five weeks after the first commit (2026-09-09).

| Measure | Value |
| --- | --- |
| Commits on `main` | 8,013 |
| Owner rulings (D1 to D168) | 168, plus sub-rulings: 215 index rows |
| Known issues filed / open | 249 / 40 |
| Round branches | 159 |
| Production deploys | 43 |
| CI runs | 2,179 |
| Planned session restarts recorded | about 85 |
| Sessions in the roster at once | about 14 |
| Lead session `cost_usd` record | about $10,950 |
| Watchdog session `cost_usd` record | about $1,197 |
| A typical lane or worker session | $15 to $40 before its handover |

I am not sure how the `cost_usd` field maps to your actual bill under your plan; read it as relative scale, not an invoice. The Lead is by far the most expensive session, because it re-reads its long context on every turn. The fleet also spent its weekly allowance often enough that pacing became an owner ruling (D141).

## Adapting it to a theoretical CS problem

Keep the skeleton: roles, state files, independent review, an independent gate, verbatim rulings, handovers, the watchdog. Change what "passing" means. In software a test suite decides; in theory the only equivalent is a proof checker such as Lean 4 with Mathlib, backed by adversarial refereeing for anything not yet formal.

| Game fleet | Research fleet | What changes |
| --- | --- | --- |
| Lanes by code area (sim, client, server) | Lanes by **line of attack**: one per approach (for example a reduction, an algebraic method, a combinatorial method), plus a **literature lane** and a **computation lane** | 3 to 5 lanes is plenty; approaches are less independent than code areas |
| Feature code | **Formal statements and proofs** in Lean, plus written proof sketches | Each claim has a statement file before any proof work starts |
| `npm run verify` | `lake build` with no `sorry`, `#print axioms` showing only allowed axioms, and every experiment re-run from its script | A proof that does not compile is a draft, not a result |
| W-REVIEW (code reviewer) | **Referee**: tries to break every lemma, checks the formal statement says what the prose claims, plants deliberate errors to calibrate itself | The most important role; consider two independent referees for big claims |
| W-GATE3 (landing gate) | **Checker gate**: builds the exact commit, re-runs all computations, diffs every theorem statement against the agreed target | Statement drift is the classic failure: a proved theorem that is not the one wanted |
| `main` | **Established results**: only machine-checked, or double-refereed with gaps listed | Nothing lands on belief |
| KNOWN-ISSUES | **Gaps and proof obligations**, each with one owner and a status | Every "clearly" in a proof becomes a row |
| NOW.md | Live state: which approaches are alive, which are dead and why, the best result so far | Same 150-line cap |
| Lane STATUS docs | Each lane's notebook, including **dead ends with the exact obstruction** | Negative results are kept, so successors do not retry them |
| Owner rulings | Your scope calls: which problem, which variant, what counts as success, budget | Recorded verbatim, as now |
| Rounds and deploys | A weekly **results ledger** update and, when earned, a write-up draft | No production, so no deploy |
| Watchdog, backstop, guide, stop/resume | Unchanged | They are about the fleet, not the domain |

## Research-specific risks

One assumption to name first: this setup makes agents reliable, auditable and hard to fool. It does not by itself supply the mathematical insight that a hard open problem needs. If the target is a famous open problem, expect the fleet to produce partial results and a well-mapped landscape, not a solution. I am not sure what your problem is; that changes this a lot.

| Risk | Why it is worse in research | Guard |
| --- | --- | --- |
| **Convincing but wrong proofs** | Models write fluent proofs with a hidden gap or a false lemma; nothing fails loudly | Only Lean-checked or double-refereed claims land; referees are graded on planted errors |
| **Statement drift** | A lane proves something weaker or different and calls it the target | One frozen `TARGET.md` (and its Lean statement) that only you change; the gate diffs every claimed theorem against it |
| **Known barriers** | Whole families of approaches are provably unable to work (for complexity separations: relativization, natural proofs, algebrization) | The literature lane checks every new approach against known barriers before anyone works on it |
| **Invented citations** | A model cites a paper or lemma that does not exist, or says it proves something it does not | Every cited result needs an opened source (arXiv id, page, theorem number) in the lane notebook |
| **Buggy experiments** | A search program with a bug "finds" a counterexample or "confirms" a pattern | Two independent implementations; both must reproduce known small cases first |
| **Groupthink** | Lanes read each other and converge on one idea | Lanes report to the Lead, not to each other; ideas cross lanes only at a weekly checkpoint |
| **Formalization cost** | The needed library may be missing; formalizing can take longer than the math | Formalize the statement first, then only the key lemmas; record the cost in KNOWN-ISSUES |
| **No natural stopping point** | Research can spend forever with no release to mark progress | A weekly budget and a checkpoint with you; graded milestones (reproduce known results, special cases, bounds) |

## Starter kit

**Day one, in order:**

1. Create a private GitHub repo and a Claude Code cloud environment. Its setup script installs Lean 4 (elan), fetches the Mathlib cache, and pins Python packages. No secrets in environment variables.
2. Write `TARGET.md` yourself: the exact statement, the variant, and what counts as success. Everything else serves it.
3. Open the Lead session in your chat with the Lead prompt below. It creates the files, the gate script and its hourly backstop routine.
4. The Lead spawns, in this order: the literature lane (known results, barriers, the best bounds), the formalization lane (the Lean statement of `TARGET.md`), the referee, then the attack lanes once the literature map exists, then the computation lane.
5. Add the watchdog once four or more sessions run at once.

**Repo layout:**

```text
CLAUDE.md                 rules, roles, where truth lives, commands
TARGET.md                 the frozen goal; only you change it
lean/                     Lean project: Target.lean, Lemmas/, Known/
experiments/<name>/       script, data, README with how to re-run
notes/<lane>.md           each lane's notebook and dead ends
docs/NOW.md               live state, under 150 lines
docs/RESULTS.md           the ledger: only checked results
docs/GAPS.md              gaps and proof obligations, one owner each
docs/DECISIONS.md         your rulings, verbatim, plus an index
docs/agents/              LEAD-BACKSTOP.md, LANE-RESTART.md, LEAD-STATE.md
docs/referee/             referee reports
scripts/verify.sh         lake build, no sorry, axioms check, re-run experiments
```

**Root `CLAUDE.md` template:**

```markdown
# <Project>: read this first
A research fleet working on the problem in TARGET.md. One Lead routes; lanes work one line of attack each.

## Where the truth lives, in order
1. TARGET.md (only the owner changes it). 2. docs/NOW.md. 3. docs/DECISIONS-INDEX.md.
4. docs/GAPS.md. 5. docs/RESULTS.md. Notebooks and logs are history, not truth.

## Hard rules
- A claim is a result only when Lean checks it (no sorry, allowed axioms only) or two referees signed it with its gaps listed.
- Every theorem statement is diffed against TARGET.md before it lands.
- Every cited result has an opened source (arXiv id, theorem number) in your notebook.
- Record every dead end with the exact obstruction.
- Edit only your lane's files. Never rewrite pushed history. Push only when scripts/verify.sh passes.
- Quote the owner's rulings verbatim. Escalate only scope, spend and irreversible actions.
- End every task with DONE (SHAs, evidence) / FINDINGS (one line each) / NEEDS (<owner>: <ask>).
```

**Lead prompt (first message in your chat):**

```markdown
You are the Lead of a research fleet on the problem in TARGET.md. You orchestrate; you do not do the
mathematics. Create the repo files in CLAUDE.md's list, scripts/verify.sh, and an hourly backstop
routine that re-reads docs/NOW.md and docs/agents/LEAD-BACKSTOP.md. Spawn lanes with create_session,
one branch each, clone_depth 3000. Message sessions only with one-shot triggers. Land a claim in
docs/RESULTS.md only after verify passes on the exact commit and the referee says OK. Restart any
session at about 600k context with a handover and the five-question check. Stop everything on
overage and restart only on my word. Report to me in short status lines; ask me only scope questions.
```

**Referee brief (the role that matters most):**

```markdown
You are the Referee. Your job is to break claims, not to approve them. For every claim routed to you:
re-derive it; check the Lean statement says exactly what the prose and TARGET.md say; list every
step that is not machine-checked as a gap; try to build a counterexample. Before each verdict on a
long proof, the Lead may plant a deliberate error: say which step is wrong if you find one.
Verdict: OK, or CHANGES with numbered findings. You never write proofs for the lanes.
```

## Open questions for you

The answers change the setup more than any rule above.

- [ ] **Which problem, stated exactly?** A famous open problem, a lesser-known conjecture, or a specific bound to improve calls for very different fleets.
- [ ] **What counts as success?** A full proof, a special case, a new bound, or a counterexample? Partial results need to count, or the fleet has no milestones.
- [ ] **Formal or informal?** Lean gives a real pass/fail but costs time; is the area covered well enough by Mathlib?
- [ ] **Budget:** how much usage per week, and do you want a hard weekly stop?
- [ ] **Human check:** can a human expert referee the final claim before you rely on it or share it?
- [ ] **Cadence:** how often do you want a checkpoint, and in which chat?
