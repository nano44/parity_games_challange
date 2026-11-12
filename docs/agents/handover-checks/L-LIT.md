# Handover check: L-LIT (successor, N5-route literature; written 2026-11-12T10:40Z by date -u; LANE-RESTART step 3)
Every answer measured from the repository at the time of writing (commands given). Predecessor's check: git history.

## 1. Branch, head, distance to trunk
- Trap check run first: `git fetch --unshallow origin` (no-op; `git rev-parse --is-shallow-repository` -> false), then
  `git fetch origin claude/l-lit claude/vibrant-johnson-nxvvxo claude/l-si claude/l-red`.
- `git branch --show-current` -> claude/l-lit. `git rev-parse HEAD origin/claude/l-lit` -> 6895fb3183c993f45ca222bd54e6728bb0730d40 twice
  (T64, the predecessor's last push). `git rev-list --left-right --count HEAD...origin/claude/l-lit` -> 0 / 0. Not stale, not detached.
- `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` -> 0 ahead, 1659 behind (trunk 071392490dce).
  `git merge-base` = 6895fb31 = my head (`git merge-base --is-ancestor HEAD trunk` -> yes). Trunk is NOT merged into this branch (Lead's word).
- So docs/NOW.md, DECISIONS, GAPS, RESULTS on this branch are stale; I read them from trunk with `git show origin/claude/vibrant-johnson-nxvvxo:<file>`.

## 2. Open work and next step
- Predecessor IN FLIGHT: none (notes/L-LIT.md resume point, T64, 2026-11-01; lane parked since). Its open leads are «only on a Lead question».
- T65 (Lead brief, task 1): LAM-GAP / SHARP (L-SI box 101 §2, claude/l-si 4fda7245; L-RED R234 not on origin yet at 10:40Z) against the
  one-player Howard literature. Next: open Hansen-Zwick ISAAC 2010 (so far slides + abstract only, T35), Hansen's 2012 thesis (Conj. 6.1.1;
  404 on 2026-10-15), Madani / Madani-Thorup-Zwick on DMDPs, Post-Ye (opened: Thm 3.7, 4.8), VJ00 and Friedmann on one-player SI; then label
  LAM-GAP KNOWN / IMPLIED / NEW / CONTRADICTS, and say why the VJ setting escapes the mean-payoff lower bounds.
- T66 (task 2): do Friedmann's / Fearnley's / FHZ's exponential families live inside the genome class Γ3 (RESULTS R104 / R117) under N5′-xi's
  rule? Next: read R104, R117, R118, R124, R125 on trunk and this lane's T34, T37, T47, T53; then an exact embedding (for L-COMP / L-RED) or
  the exact excluding feature.
- Task 3: one docs/lit/T-<n>-*.md per task, quotes with exact locations, a one-page summary for the Lead.
- All of it waits for the Lead's «go».

## 3. docs/GAPS.md rows I own
- None. `git show origin/claude/vibrant-johnson-nxvvxo:docs/GAPS.md | grep -n -i l-lit` -> lines 10 (G-N1-LB, owner L-NEW, open), 11
  (G-N5-TIME, owner cell «L-NEW (L-LIT T22; referees later)», open; T22 = the finished VJ00 Prop. 7.4 check) and 17 (G1, L-STRUCT, closed).
  L-LIT is cited as a source in all three.

## 4. Three owner rulings (verbatim), DECISIONS-INDEX status (trunk 07139249)
1. D18 (index line 32: active; DECISIONS.md line 333):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
2. D1 (index line 5: active; DECISIONS.md lines 6-7):
   > Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
3. D15 (index line 26: active; DECISIONS.md line 278):
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
- D21 («maximum effort for the next two days») reached me only as the Lead's relay; it is not in the index or DECISIONS.md at trunk
  07139249, so I hold no verbatim text and quote none.

## 5. Trap and check
- Trap that bit this lane (notes/L-LIT.md: T48 and T54 starts): a stale local branch (4014 behind at T48; first push rejected at T54).
  Check, run before reading anything: the fetch above, then `git rev-list --left-right --count HEAD...origin/claude/l-lit` must print 0 0
  and `git branch --show-current` must print claude/l-lit. This time: 0 / 0.
- Standing checks kept from the predecessors: a paywalled or blocked source is reported NOT OPENED, never paraphrased from memory;
  subagents get the scope rule in their brief (public literature only, no code search outside this repository, no contact; T17 breach);
  push.sh pushes the commit verified at its start, so no commit while a push runs, and `pgrep -f "bash scripts/push.sh"` before every push.
