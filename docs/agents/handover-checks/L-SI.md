# Handover check: L-SI (successor 3, written 2026-10-24T21:24Z by date -u; LANE-RESTART step 3; Opus 5.5, D18/L40)
Every answer measured in this container (commands given), not recalled. Predecessor: successor 2,
session_01Uat5ArD53GnDHorFDHrMnH; last lane push e7a5806c ("L-SI box 6: (CL) reduced to COARSE-SI + A + (JUMP-EQ) ...; handover
notes (parked)").

## 1. Branch, head, distance to trunk
- Branch `claude/l-si`. At container start the LOCAL branch was the stale 0d48da26 (Fable-era end of box) and `git status` said
  "up to date" before any fetch. After `git fetch origin claude/l-si claude/vibrant-johnson-nxvvxo`: origin/claude/l-si = e7a5806c,
  trunk = 0d722673 (2026-10-24T21:15:38Z). `git rev-list --left-right --count origin/claude/l-si...trunk` = 1 58
  (merge-base adfb570f; trunk already holds everything up to box 5 (b)).
- Fast-forwarded local to e7a5806c, then `git merge --no-ff trunk` = f9c81782 (clean, no conflicts). HEAD...trunk = 2 0.
  This file's commit makes it 3 ahead, 0 behind (SHA in the message to the Lead).
- tools/oink/build absent at start; scripts/setup_oink.sh rebuilt it here (oink built at 8fbf0a7).
- experiments/si/xing/out/ (climb output) was excluded only via the old container's .git/info/exclude; it does not exist here. Never
  `git add -A`.

## 2. Open work and the next step of each (box 7 = proof side of (C), carries)
State: (CL) "carry levels non-increasing while w constant" is READING-reduced to COARSE-SI + A + (JUMP-EQ) (docs/si/N5-C-box5.md
§3b, §5, §6). PROVED (L-SI succ. 2, unrefereed): Lemma CLU, Step 2. DATA: I(L) 784/0, FREEZE(L) scoped 638/0, A 198/0,
(JUMP-EQ) 19/20 post-carry jumps.
1. COARSE-SI (Step 1), READING -> next: write the full proof (L-coarse super-solution in G_{σ̄_k}, telescoping, simple-path
   bookkeeping (VAL), the exact cycle-closing exclusion).
2. (JUMP-EQ), CONJECTURE -> next: find the one post-carry jump landing in THR (freeze.py pre-scope variant: 'F' entries after lastc),
   re-verify it (n5.py, Oink zlk, check_sol2.py), then prove (JUMP-EQ) or refute it with that instance (refutation reported at once).
3. A (a carry changes Ξ only at levels ≤ L), DATA 198/0 -> next: proof from CLU (evictees ≤ eviction level), passive inheritance,
   flat F-switches (R21 (c) FBL-N (ii)), θ via exits.
4. Carries per level (refill half of the counter), OPEN -> next: bound refills = θ-changes strictly below the level (data §3).
- Also OPEN, not in this box: (Z) per joint λ-phase beyond (C); (NH'); (ELIM-poly), (LEVEL-poly), (CYC-u*).
- Landed context: R21 (Theorem X), R22 (F1°, TC, P3′). P-N5-Z (R23) signed by both referees, at CHECKER; fixes only in
  docs/si/P-N5-Z-fixes-box5.md (never edit a file after its sha1 was sent for pinning).
- IN FLIGHT: nothing running (no climbs carried over).

## 3. docs/GAPS.md rows I own
- None. Measured: `git show trunk:docs/GAPS.md | awk -F'|' '{print $2"|"$4"|"$5}'`: owners are L-ALG (GAP-A, GAP-C, G-S5-6),
  L-RED (G-NEST), L-NEW (G-N1-LB, G-N5-TIME). My work feeds G-N5-TIME (owner L-NEW, open): its row cites the open (X) ≡ (Z) up to n
  (L-SI succ. 2 Lemma LV′) and P-N5-Z.

## 4. The three owner rulings that most constrain me (verbatim; status in docs/DECISIONS-INDEX.md on trunk)
- D18 (active): "Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of
  mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them
  briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems."
  (Lead reading L40: label every statement PROVED (by whom) / CONJECTURE / OPEN / DATA / READING.)
- D16 (active): "Then keep working as I told you to" (Lead reading L38: no idle fleet).
- D1 (active, docs/decisions/D001-launch-brief.md l.96-97): "Never publish, post, email, submit or contact anyone outside the fleet.
  Anything external is my decision."

## 5. One trap that bit this lane, and the check that now prevents it
- Trap: box 4/5 evidence included s_rt32_final, which has TWO Odd choice vertices (14, 28); the box 28 tools silently took the
  first, so it was out of 𝒞^1O and evidence for nothing (docs/si/P-N5-Z-fixes-box5.md §1).
- Check: experiments/si/xing/xclass.py annotate() asserts exactly one Odd vertex with out-degree > 1 (line 38), and phase_stats()
  calls assert_run() (iterations and fallbacks equal experiments/new/n5.py run()'s; box28 fbre.profile alone does not assert it).
  Re-measured here: `python3 experiments/si/xing/xclass.py experiments/si/orlens/instances/s_rt32_final.pg` ->
  "AssertionError: not one-Odd-choice: Odd choice vertices [14, 28]"; instances/ccl_fb2_n32.pg -> runs (n 32, X 25, LF 31).
