# NOW (rewritten, never appended; max 150 lines)
Updated: 2026-10-14 by Lead. Phase: M0 done pending TARGET approval; M1 running; M2 BLOCKED on network (paper hosts denied).

## Milestones
| M | State | Evidence |
| --- | --- | --- |
| M0 Setup | done except owner approval of TARGET.md | this commit; CI .github/workflows/verify.yml; backstop trigger in docs/agents/LEAD-BACKSTOP.md |
| M1 Reproduce hard families | in flight (L-COMP) | experiments/ |
| M2 Audit arXiv 2511.03752 | BLOCKED: arxiv.org denied by environment network policy; 2-day clock starts when reachable | notes/L-COMP.md, docs/referee/ |
| M3 Partial results | not started; attack lanes wait for TARGET approval and L-LIT ranking | - |
| M4 Target | not started | - |

## Roster (model, effort, one-line reason; revisit at each restart)
Lead session: session_014FBi6o334DvwT5Uw2kDfoN, environment env_013N6DGgsLr96BMjKj1hpw9i, branch claude/vibrant-johnson-nxvvxo.
Effort note: create_session exposes no effort knob; every session inherits effort "high" (verified per session with get_session).
Prices per Mtok in/out (platform docs, 2026-10-14): fable-5-1 $10/$50, opus-5-5 $4/$20, sonnet-5-5 $2/$10, haiku-5-5 $0.10/$0.50.

| Role | Session id | Branch | Model | Effort | State | Reason |
| --- | --- | --- | --- | --- | --- | --- |
| Lead | session_014FBi6o334DvwT5Uw2kDfoN | claude/vibrant-johnson-nxvvxo | opus-5-5 | high | working | Owner-chosen session; routing judgement; keeps context lean |
| REFEREE | not spawned (held: needs paper hosts) | claude/referee | fable-5-1 | high | held | Most capable model; finding the error in a claimed proof decides M2 and every claim after |
| L-LIT | not spawned (held: needs paper hosts) | claude/l-lit | opus-5-5 | high | held | Source checking and barrier analysis need judgement; Fable reserved for referee; move to Fable when step-3 sign-offs start |
| L-COMP | session_014bbtNwaVKxFymHpXynjURn | claude/l-comp | opus-5-5 | high | working | Paper-to-code fidelity for M1 generators and the M2 implementation; drop to sonnet-5-5 for routine benchmarks after M2 |

## In flight
- L-COMP: setup, solver-agnostic harness, M1 hard families (Oink + PGSolver generators from GitHub). M2 implementation waits for arXiv.
- REFEREE, L-LIT: held, not spawned; a session that cannot open papers would only spend money.

## Live approaches
- (none yet)

## Dead approaches (with obstruction): see docs/RESULTS.md "Dead ends"
- (none yet)

## Best result so far
- None of the fleet's own. Known: quasi-polynomial upper bound (to be source-checked by L-LIT).

## Owner questions open
- Q0 (blocker): environment network denies arxiv.org, export.arxiv.org, doi.org, drops.dagstuhl.de, lmcs.episciences.org and other paper hosts (github.com works). Asked owner to allow them.
- Q1: approve TARGET.md (section 7 lists five choices).
- Q2: trunk branch: keep claude/vibrant-johnson-nxvvxo as trunk, or create `main`?
- Q3: environment setup script (Boost dev packages + scripts/setup_oink.sh) to save each session ~1 min of setup.

## Spend
- No cost_usd field is visible to the Lead through get_session; spend is estimated from context_usage tokens per session and the prices above.
