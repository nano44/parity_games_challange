# Handover check: L-RED successor 68 (Opus 5.5, high, D1/D18/D21, L53; LANE-RESTART step 3; written 2026-11-12T20:01Z by date -u)
Every answer is measured from the repository (commands named), not recalled. Predecessor: successor 67 (Fable 5.2, stopped by the
Fable weekly limit ~19:38Z, NO handover); last push 2d290a15 «R237 (2): exhaustive n = 3, part 0 of 2». Its resume point is
notes/L-RED.md «Successor 67 ... RESUME POINT» (last lines of the notebook); successor 66's handover is at l. 3477.

## 1. Branch, head, distance to trunk
- Trap check run first: `git fetch --unshallow origin; git fetch origin claude/l-red claude/vibrant-johnson-nxvvxo; git checkout
  claude/l-red; git merge --ff-only origin/claude/l-red`. The local branch was 314 behind origin/claude/l-red; fast-forwarded.
- `git branch --show-current` = claude/l-red; `git rev-parse HEAD origin/claude/l-red` -> both 2d290a15b672c9a86caa8ceb49df4adb3b4be510.
- Trunk claude/vibrant-johnson-nxvvxo = 7fa6aff4a (committed 2026-11-12T17:10:52Z).
  `git rev-list --left-right --count origin/claude/vibrant-johnson-nxvvxo...HEAD` -> 1235 192, i.e. 192 ahead / 1235 behind;
  merge-base c2d1e88ee. Trunk is not merged in; truth docs read from trunk with `git show origin/claude/vibrant-johnson-nxvvxo:<file>`.
- Clock: `date -u` 20:00:38Z against the Date header of a raw.githubusercontent.com response 20:00:38 GMT: skew 0 s.

## 2. Open work and the next step of each
- Nothing running (new container; `pgrep -af "push.sh|exh237|climb237"`: none; 4 CPUs). The four read-only archives (BOX104 26704e01,
  LNEW fcba92fc, LRED 8c01d40e, LLIT 5c53efbd; notebook «Envs») must be rebuilt in the scratchpad before any run.
- R237 (2) (WRAP step (W4), box 104), state measured from experiments/red/r237/out:
  (a) exh237 n = 3 part 0 of 2 DONE (exh3_0of2.log END: 219,488 games, all kill / N5 / (W4)-(W6) sentence counters 0, second engine
      xdiff 0 on 438 sampled, ctrl 0 = control not run in this part). Next: part 1 of 2 (PART=1/2, RESUME=1), then CTRL=1 control.
  (b) climb237 (W4) climb, two engines, CTRL=1 must fire: NOT started (no ck_*climb* checkpoint). Next: small (n <= 12) two seeds,
      then medium (n <= 30).
  (c) aim237 families aimed at single sentences of box 104's (W4) proof, incl. REFEREE 33's W-1 (pe-free play from a start outside
      the core along the 6-edge paths; starts pe, pe_o, pb, c_W): NOT started. I do not read the rest of R-WRAP-preread.md before my verdict.
  (d) docs/red/R237-w4.md (verdict «(W4) survives climb of size S» with counts, or a counter surviving engine 2 + SPEC-line check).
- Correction for R237's doc (Lead item 2): n5x236 «spec» mode is not SPEC's tie rule; n5s237 (= box 104's n5v spec) gives 5/5/5/5/6 on
  F_n n = 2..5 (out/fn_spec.out also has n5s237 6/6/6 at n = 6..8, n5x236 3); R236's «3 on every F_n» was n5x236's reading.
- Then L-SI box 105 (claude/l-si 516b6837, docs/si/box105-key.md KEY-MODEL): replay N5 spec on Γ3*(G*) = KEY rule state for state on
  n5s237, random free genomes, keyfail with controls.
- ON HOLD (Lead): DEEP3 climbs.

## 3. docs/GAPS.md rows I own (trunk 7fa6aff4a)
- G-NEST (major, «L-RED (attacks + proof attempts); L-ALG successor if any», open; l. 9).
- L-RED attacks: GAP-A (blocker, open; l. 6), GAP-C (blocker, open; l. 7), G-STR (major, closed; l. 22), G-DOM (major, closed; l. 23).
- This box works against G-N5-TIME (major, owner «L-NEW (L-LIT T22; referees later)», open; l. 11) under D1/D18: WRAP bears on the
  variant N5′-xi; the row's claim is about N5 and stays OPEN.

## 4. Three owner rulings (verbatim; status from trunk docs/DECISIONS-INDEX.md)
- D1 «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own,
  as wrong until it passes the gauntlet below.» (active, index l. 5; string found once in trunk docs/DECISIONS.md by grep -cF)
- D18 «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics
  and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and
  proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.» (active, index l. 32;
  found once by grep -cF)
- D21 «Okay, I want maximum effort. I want to use 200% usage in 3 days. There is fable 5.2 as well, use that too in dpeth everywhere
  where it seems fitting, use fable 5.2 at hard or xhigh. SO yes, 200% uage under 2 days.» (active, index l. 46; trunk DECISIONS.md
  l. 452). Lead readings (not the owner's words): L51 maximum effort to 2026-11-14 10:05Z; L52 a reset limit is a pause; L53 (Lead
  brief; not yet in trunk's index at 7fa6aff4a) this session on Opus 5.5 while the Fable weekly limit is reached (reset 2026-11-18 21:00Z).

## 5. One trap that bit this lane, and the check
- Stale local branch at start (this session: 314 behind). Check: the trap-check commands above; HEAD == origin/claude/l-red before work.
- A session stopped by a limit with no handover (successor 67, this box): check = every long job resumable from a committed
  checkpoint (exh237 PART/RESUME, climb237 out/ck_TAG.json with rng state) and a notebook resume point updated at each push.
- A «counterexample» from my own engine's tie readings (R236: n5x236 vs n5v, all tie rule). Check: no (W4) candidate is reported before
  it survives the second engine and a SPEC-line check (H, s0, sha1, state) at once.
- Typed stamps / SHAs, and commits during a push. Check: stamps from date -u in the same command; SHAs copied from git output in a
  later step; `pgrep -af "bash scripts/push.sh"` before every commit and push; <= 2 CPU-heavy jobs including verify.
