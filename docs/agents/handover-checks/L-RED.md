# Handover check: L-RED successor 58 (Opus 5.5, D1/D18/D14; LANE-RESTART step 3; written 2026-11-08 04:4xZ by date -u)
Every answer is measured from the repository (commands named), not recalled. Predecessor: successor 57, handover =
notes/L-RED.md «Successor 57 HANDOVER» at l-red 5fdb96b3e.

## 1. Branch, head, distance to trunk
- Trap check run first: `git fetch --unshallow origin; git fetch origin claude/l-red claude/vibrant-johnson-nxvvxo;
  git checkout claude/l-red; git merge --ff-only origin/claude/l-red` (local branch was 36 behind; fast-forwarded).
- `git branch --show-current` = claude/l-red; `git rev-parse HEAD origin/claude/l-red` -> both 5fdb96b3eef8f341f061e25f78fe0614660d7258.
- Trunk claude/vibrant-johnson-nxvvxo = 4aaba7d52 (committed 2026-11-08T03:55:48Z).
  `git rev-list --left-right --count origin/claude/vibrant-johnson-nxvvxo...HEAD` -> 50 ahead / 892 behind; merge-base c2d1e88ee.
  Trunk not merged in (not needed for this lane's files).

## 2. Open work and the next step of each
- Nothing running: new container (`pgrep -af "push.sh|own.py"`: none); `git worktree list` = main only (wtsi83, wt190, wt190b,
  wt191, wt192, wt195 of successor 57 are gone); tools/oink/build absent (scripts/setup_oink.sh needed before any Oink route).
- Done by successor 57: R222-lockup.md (LOCK-UP / LADDER-2 SURVIVE, Lemma FLIP without PRIV), R222-cyc.md (RHO-CYC, RHO-CYC-0,
  §6 lemma list), R222-end.md (box 195 ENDGAME-3 SURVIVES; EXACT-L wording gap, witness inst/SELFL_n3.json).
- Box R223 (after «go»), in order:
  1. Adversary on packet P-N5-END: waits for the Lead's freeze SHA. Then: Addendum 2's IDEAL-ACYC wording vs SELFL_n3; premises
     landed (R117 (f) REACH3, TAU3, R15 (c)); [OPT] = [1E-N3] for SPEC-run σ̄ (Lead reading); re-run the 9 families (end222.py) on the
     frozen tools (recreate worktree of the frozen SHA first).
  2. Extend Lemma FLIP: (a) Λ(B) ∉ {K1, K2} via B-ONLY (λ ≠ b_S?), (b) non-SET options, (c) β-decided switches. Next step: re-read
     R222-lockup.md §4 proof, find where Λ(B) ∈ {K1, K2} and SET are used, then try each case; priv222.py random sweep for (a)-(c).
  3. Adversary on L-SI 45's TWO COPIES PER LEVEL: waits for the Lead's candidate SHA; then own.py + (if built) Oink n5v/n5b on Γ3.

## 3. docs/GAPS.md rows I own (trunk 4aaba7d52)
- G-NEST (major, «L-RED (attacks + proof attempts); L-ALG successor if any», open).
- L-RED attacks: GAP-A (blocker, open), GAP-C (blocker, open), G-STR (major, closed), G-DOM (major, closed).
- R223 works against G-N5-TIME (major, owner «L-NEW (L-LIT T22; referees later)», open) under D1/D18.

## 4. Three owner rulings (verbatim; status from trunk docs/DECISIONS-INDEX.md)
- D1 «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own,
  as wrong until it passes the gauntlet below.» (active)
- D18 «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics
  and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and
  proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.» (active)
- D14 «You know it can also test prveiously not tested approaches, it can come up with it own as well» (active)

## 5. One trap that bit this lane, and the check
- Lanes have started on a stale local branch (this session: local claude/l-red was 36 behind origin; pushes then fail or push old
  history). Check: the trap-check commands above, then `git branch --show-current` and `HEAD == origin/claude/l-red` before any work.
- Worktrees and Oink builds live only in the container (lost on reset every ~40 min): tools record the SHA they need
  (WTSI83, WT, WT3) and are recreated from git before use; every long job is a tracked background task, `pgrep -af` first.
