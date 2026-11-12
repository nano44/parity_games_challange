# Handover check: L-LOWER successor 14 (2026-11-12 04:03Z, date -u; LANE-RESTART step 3)
Every answer measured from the repository at the time of writing (commands named), not recalled.

## 1. Branch, head, distance to trunk
- Branch `claude/l-lower` (`git branch --show-current`). The local branch was 131 commits behind origin at start (af9a73d8) and
  was fast-forwarded (`git merge --ff-only origin/claude/l-lower`); clone not shallow (`git rev-parse --is-shallow-repository` = false).
- Head d80fffe5219e6ed8dcb51b88988ae5124b533a7c = origin/claude/l-lower (successor 13 HANDOVER).
- Trunk `claude/vibrant-johnson-nxvvxo` at 575ac9443a9d3bd49968eeb80cc1615189f5a494; merge-base 8cc6ebc6.
- `git rev-list --left-right --count origin/claude/vibrant-johnson-nxvvxo...HEAD` → 100 ahead, 800 behind.
  No trunk merge (not needed for the lane's files).

## 2. Open work and the next step of each (BOX L16, after «go»)
- BOX L16: hand-built SHARED helper cascade on the C12 base (solved c58041d5, frozen eaf68e67), sized by CONJECTURE KEY-CLOCK
  (≈ log2 P − c pairs). Target: core8 rows 0..P for P ≥ 18; milestones P = 18, 21, 24, each replayed (sim6 = fenc) and frozen;
  stretch: full core8 horizon T 510. Stop rule: no design passes P = 18 after D1-D3 → the exact obstruction is the box result.
- (D1) graft the replayed exact 3-pair cascade l15/out/E_k3_P16_shared.txt (0c6c4793) onto C12 helper levels 8-10 (movers 16-21),
  rewire q4 / f5 / q6 / f6 to read it. Next step: read the cascade's encoding (xt / rank / even / gate / start in l15 units,
  ekr.py / sim15.py) and C12's genome layout (l14 rec + rsolve.py), write the graft as a script, replay with sim6 + fenc, then
  pgad3 fixed-rank questions with XS = {8, 11, 12, 13} restricted to cascade targets at P = 17, 18.
- (D2) 4-pair cascade from kr.py's relaxed P 32 model made exact with the trajectory fixed (ekr.py), then the same graft.
- (D3) HIT7_lift_d32's own helper cascade (l9/rec) copied onto C12's helper levels as the shared clock.
- Binding question at each milestone (l14/tight.py): which client's tight change fails first (P 18 needs q6 at 16, f5 at 14,
  q4 at 13 at once).
- No runs in flight (`pgrep -af "pgad|push.sh|ann3|kr.py"` empty before this commit). Binaries (fenc, drup) to rebuild in the
  scratchpad before «go».

## 3. docs/GAPS.md rows owned by L-LOWER
None (`grep -c L-LOWER docs/GAPS.md` = 0, on this branch and on trunk). The box works against G-N5-TIME (owner L-NEW, open;
trunk docs/GAPS.md line 11).

## 4. Three owner rulings that most constrain this lane (verbatim; status from trunk docs/DECISIONS-INDEX.md)
1. D18 (active, index line 32; docs/DECISIONS.md l. 333): «Focus on N5 and work toward proving it. Explore novel approaches,
   especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make
   reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven
   results from conjectures and open problems.» Constraint: each L16 statement carries PROVED (lane) / CONJECTURE / DATA / DEAD;
   KEY-CLOCK stays a CONJECTURE whatever a single hand-built cascade does.
2. D1 (active, index line 5; docs/decisions/D001-launch-brief.md l. 25, excerpt): «A claimed polynomial algorithm is far more
   likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet
   below.» Constraint: a wall that does not appear on one base is not evidence that N5 is polynomial, and a tower past P 18 is
   not yet a super-polynomial family; scope every claim to its instance.
3. D14 (active, index line 22; docs/DECISIONS.md l. 246): «You know it can also test prveiously not tested approaches, it can
   come up with it own as well» (typos the owner's). Constraint: the hand-built cascades D1-D3 are own designs and go through the
   same freeze / replay / DRUP discipline as any other candidate.

## 5. One trap that bit this lane, and the check that prevents it
- Trap (successor 13): a wait loop on `pgrep -f "bash scripts/push.sh"` matches its own command line and never ends; and pausing
  a DRUP worker for a push lost the helper in flight (helper 41, twice). Check: poll the push task's output file for its exit
  marker instead of pgrep, and let workers finish before pushing (never commit while a push runs).
- Start trap (again this time, 131 behind): fetch --unshallow, ff-only merge, assert branch and HEAD = origin (both true above).
