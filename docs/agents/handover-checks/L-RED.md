# Handover check: L-RED successor 63 (Opus 5.5, D1/D18/D14; LANE-RESTART step 3; written 2026-11-09T03:13Z by date -u)
Every answer is measured from the repository (commands named), not recalled. Predecessor: successor 62, handover =
notes/L-RED.md «Successor 62 HANDOVER» (l. 62) at l-red bfe7692e8.

## 1. Branch, head, distance to trunk
- Trap check run first: `git fetch --unshallow origin; git fetch origin claude/l-red claude/vibrant-johnson-nxvvxo;
  git checkout claude/l-red; git merge --ff-only origin/claude/l-red` (local branch was 94 behind; fast-forwarded).
- `git branch --show-current` = claude/l-red; `git rev-parse HEAD origin/claude/l-red` -> both bfe7692e836a971adcf66011db5e23b2730fd88f.
- Trunk claude/vibrant-johnson-nxvvxo = a773c562b (committed 2026-11-09T01:59:41Z).
  `git rev-list --left-right --count origin/claude/vibrant-johnson-nxvvxo...HEAD` -> 1089 108, i.e. 108 ahead / 1089 behind
  (left = trunk-only); merge-base c2d1e88ee. Trunk not merged in (not needed for this lane's files).

## 2. Open work and the next step of each
- Nothing running: new container (`pgrep -af "push.sh|climb|own.py"`: none); `git worktree list` = main only; scratchpad empty
  (predecessor's lnew / si90 / mw archives lost; rebuild with git archive); tools/oink/build absent (scripts/setup_oink.sh before any Oink route).
- Box R229 (after «go»):
  1. ADVERSARY on L-SI 48 BOX 92 (claude/l-si d962efdb): Lemma GATE-LOW-NULL and CONJECTURE WAIT-CLOSED killer table K1-K9.
     Next step: read docs/si/box92-closed.md at d962efdb; check GATE-LOW-NULL's premises / PRIV condition / case analysis line by line;
     for each killer row K1-K9 check the cited statement is PROVED and applies to the class as stated; then counter-side attack on the
     open rows K7 (non-PRIV gate) and K6 (lagging merged copy, h ≥ 4): add a PRIV / gate-class counter to the r228 census tools
     (self228.py / split228.py) and climb for a K7 / K6 instance with C or R growing.
  2. ADVERSARY on L-NEW 67 BOX 202 (Ξ-feedback number k; T3 ≤ (N + M)^O(k)?, k = 1 first): waits for the Lead's SHA.
     Next step: read it; test on MW8_2 (k = 2) and k = 1 genomes; record k (seg228.py) for every frozen best.
  3. OWN: a k = 1 genome with R or C growing in N + M. Next step: add a k = 1 constraint (min FVS of the Ξ-graph via seg228.py) to
     mclimb228.py as a filter, climb ORDER=CT under k = 1 at caps 200 / 400; freeze bests; if bounded, report with frozen instances.
- Open from predecessors: CONJECTURE RA-MULT(K) (L-SI) unbroken at maxm 2 beyond MW (MW itself kills RA-MULT); cap-scaling C = R ≈ (2/29)(N + M).

## 3. docs/GAPS.md rows I own (trunk a773c562b)
- G-NEST (major, «L-RED (attacks + proof attempts); L-ALG successor if any», open; l. 9).
- L-RED attacks: GAP-A (blocker, open; l. 6), GAP-C (blocker, open; l. 7), G-STR (major, closed; l. 22), G-DOM (major, closed; l. 23).
- R229 works against G-N5-TIME (major, owner «L-NEW (L-LIT T22; referees later)», open; l. 11) under D1/D18.

## 4. Three owner rulings (verbatim; status from trunk docs/DECISIONS-INDEX.md)
- D1 «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own,
  as wrong until it passes the gauntlet below.» (active, index l. 5)
- D18 «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics
  and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and
  proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.» (active, index l. 32)
- D14 «You know it can also test prveiously not tested approaches, it can come up with it own as well» (active, index l. 22)

## 5. One trap that bit this lane, and the check
- Committing while a push runs (successor 61, c482e0d8: an empty task-output file read as «push finished»). Harmless because push.sh
  pushes only the verified SHA, but forbidden. Check: `pgrep -af "bash scripts/push.sh"` right before EVERY commit and every push.
- Stale local branch at start (this session: 94 behind). Check: trap-check commands above, HEAD == origin/claude/l-red before work.
