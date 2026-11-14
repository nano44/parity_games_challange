# Handover check: L-COMP (successor 23, session_01V5yGRYgGAhamJ5yUQXcJFH; model and effort as the Lead set them; written 2026-11-14T13:47Z by date -u)
Every answer measured from the repository at the time of writing. Successor of L-COMP 22 (session_01V5yGRWfgPQ815hzDFM7SSJ), which parked
with a handover at dc6d831f («HANDOVER -- successor 22» at the top of notes/L-COMP.md; NOTHING RUNNING at the park). This OVERWRITES
successor 22's answers (in git history).

## 1. Branch, head, distance to trunk
- `git fetch origin claude/l-comp`: this container was NOT stale (HEAD = FETCH_HEAD = dc6d831f7c56 before any read; `git rev-parse
  --is-shallow-repository` = false). Branch `claude/l-comp` (`git branch --show-current`), working tree clean.
- Trunk origin/claude/vibrant-johnson-nxvvxo = aeb90ac199af (commit date 2026-11-13T19:04:18Z, «Lead: log 17:31Z-19:03Z ...»).
  `git rev-list --left-right --count HEAD...trunk` = 267 ahead / 653 behind; merge-base ebf59a34f6c8. +1 ahead after this commit.
- Other lanes at my fetch: l-red-b 10dfedb6574c, l-si 8c0629141861, l-new 0c18fbba4826, l-red c7ed9b8b6af4.
- Clock: `date -u` 13:46:18Z against `date: Sat, 14 Nov 2026 13:46:18 GMT` of a raw.githubusercontent.com response, same command: skew below 1 s.
- Container: 4 cores, 15 GB RAM. Oink built by scripts/setup_oink.sh in this container (exit 0, «oink built at 8fbf0a7»; tc, tc+,
  counter_*, rngame, verify present). No job of mine runs; `pgrep -f "bash scripts/push.sh"` empty. NOT in this clone: successor 22's
  scratchpad archives (LNEW212 / LNEW215 / LNEW217 / LRED) and box47/bin; rebuilt with git archive only if a task needs them.
- My branch's scripts/push.sh is the OLD copy (no ls-remote check; trunk's has it): I compare `git ls-remote` with my SHA after every push.

## 2. Open work and the next step of each
Successor 22's stopped lanes (K32 / K40, KD, run47e, run46f, B0 / B1, A3 probe) are NOT TO BE RESUMED (Lead 2026-11-13 13:50Z). One task
(Lead brief 2026-11-14 13:44Z, DESIGN DAY, Lead reading L61): THE BATTERY in experiments/battery/, the tool that makes gauntlet step 2 a
ten-minute run for any candidate engine.
1. Interface (engine = command: PGSolver file in, one JSON line out: winner, strategy, iterations, steps) + README with one worked
   example; reference engines: Oink zlk wrapper, a short Python Zielonka. Next step: write engines/ and the README.
2. Instance sets pinned by sha1 with source commit (copied, not regenerated where a lane froze them): (a) Γ3(G_k) k = 3..13 from l-red-b
   experiments/red-b/data/b6b/pg/; (b) wrapper family of R130 from l-si experiments/si/box104/inst; (c) M1 hard families
   (experiments/hard-families, sizes this lane reproduced); (d) frozen 300 + regressions of experiments/harness; (e) 10,000 seeded rngame
   games (agreement only). Next step: git archive the two lane directories at the fetched SHAs, copy, write SHA1SUMS.
3. run_battery.sh <engine command> [set ...]: timeout, winner vs Oink zlk (and --tl on counter_m N = 41, 42), strategy verified by my
   verifier (D2 change 5), iterations + wall time, one table per family, growth ratios over the last three sizes + power-law exponent +
   a one-word READING; non-zero exit on any wrong winner / bad strategy.
4. Self-test rows that must come out as known: N5 doubling on (a) and polynomial counts on (b); N5′-xi the opposite; Zielonka's blow-up on
   its M1 family. A known row that does not come out = the battery is wrong, said so.
FIRST USABLE VERSION (~60 min): sets (a), (b), (e) with Zielonka and N5; commit, report SHA + exact command; then (c), (d), the fit, and
the design lanes' engines as the Lead routes them. Limits: at most 2 CPU-heavy jobs including verify; a status line every 90 minutes;
park at ~450k context.

## 3. docs/GAPS.md rows owned by L-COMP
None (trunk aeb90ac1 docs/GAPS.md: open rows GAP-A (l. 6), GAP-C (l. 7), G-S5-6 (l. 8), G-NEST (l. 9), G-N1-LB (l. 10), G-N5-TIME
(l. 11); no owner is L-COMP). Mention only: G-N5-TERM (l. 16, owner «L-NEW (L-COMP checks runs)», closed).

## 4. Three owner rulings that most constrain this lane (verbatim; status from trunk docs/DECISIONS-INDEX.md)
1. D1 (active, DECISIONS-INDEX.md:5; docs/decisions/D001-launch-brief.md:25, excerpt): «A claimed polynomial algorithm is far more likely
   to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.» The battery
   is gauntlet step 2 (TARGET.md §5: «It agrees with Zielonka on 10,000 random games of varied sizes and on every hard family; runtime
   growth is plotted and recorded.»); its growth line is a READING of DATA, never a claim.
2. D2 change 5 (active, DECISIONS-INDEX.md:6; docs/DECISIONS.md:27-28; TARGET.md §5): «Gauntlet addition: every implementation also
   outputs positional strategies, and L-COMP verifies them on every test game.» Hence the strategy field in the engine interface and my
   own verifier in run_battery.sh.
3. D27 and D28, as relayed verbatim in the Lead's brief of 2026-11-14 13:44Z (NOT on trunk aeb90ac1 yet: `grep -E "D27|D28|L61"` in trunk
   docs/DECISIONS.md is empty, so I cite the brief, not the index): D27 «SO we have to look for a new algorithm no? Do we have any
   promising lead or can convert our learning into a new promising algorithm?»; D28 «I reset everything, you have until 11PM to use a
   full 100% usage». Lead reading L61 (the Lead's words, not the owner's): today is a design day; L-NEW 78 and L-SI 57 design, L-RED and
   L-RED-B attack, L-COMP builds the battery.

## 5. One trap that bit this lane, and the check that now prevents it
Trap: scripts/push.sh on this branch exits 0 even when its git push fails (HTTP 503, successor 22, 2026-11-13; origin unchanged). Check:
after EVERY push, `git ls-remote origin refs/heads/claude/l-comp` is compared with the pushed SHA in a later step, and a mismatch is a
failed push (re-run, never a second push in parallel). Carried: `pgrep -f "bash scripts/push.sh"` empty before every commit and push;
push.sh as a tracked background task, output redirected to a file, exit code echoed, no pipes, never «&»; fixes by a NEW commit (no
reset, amend, rebase); no model name in a commit; stale-container check (fetch by name + ff-only + HEAD == origin) before any read; every
number in a message pasted from a generated file with path + sha1; message stamps from date -u in the same step; a runner or a tool it
imports is never edited while a job uses it. New for the battery: a «counterexample» from an unfaithful engine is not a counterexample
(CLAUDE.md trap), so the battery's self-test rows (known doubling / known polynomial counts) must come out before any design-lane row
is read; and Oink --zlk is not the sole reference on counter_m N = 41, 42 (aborts; --tl there).
