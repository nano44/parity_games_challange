# Handover check: L-RED successor 17 (Opus 5.5, D14/D15/D18; LANE-RESTART step 3; written 2026-10-25 16:41Z by date -u)
Every answer is measured from the repository (commands named), not recalled. Predecessor: successor 16
(session_014kwWmBLu9B31iceFsng38k), handover = R70 + notebook RESUME POINT at l-red 9589ffa3. Successor 16 wrote its own check
into notes/L-RED.md ("Handover check (successor 16)"); successor 15's answers follow below this section.

## 1. Branch, head, distance to trunk
- Branch `claude/l-red`. Fresh container: local branch 1703 commits behind origin/claude/l-red (stale clone, clean tree).
- `git fetch origin claude/l-red` (16:39Z) -> origin/claude/l-red = 9589ffa3; `git reset --hard origin/claude/l-red`;
  `git rev-parse HEAD origin/claude/l-red` -> both 9589ffa3b36d20485bffd7f5b647087e6ae986d5.
- Trunk `claude/vibrant-johnson-nxvvxo` = f7b6e688 (16:34Z). `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo`
  -> 4 ahead / 106 behind; merge-base d7df76f9. The 4: 859c137a (trunk merge), 2d9cd5f7 (lv16), 63ff3fe8 (R70 draft), 9589ffa3 (R70 final).
  Trunk merged into the lane with `git merge --no-ff` (no rebase, amend or force-push) before this file's commit.

## 2. Open work and the next step of each
Nothing in flight (`ps aux`: no lane job; the predecessor's scratch logs died with its container; verified bests are in
experiments/red/so/instances/, sha1 re-measured: nleq_cex_n48 e72e4034, tevlast_cex_n40 ff1e9cb4, tev_cex_n40 17078f78).
Oink not present in the new container: scripts/setup_oink.sh started 16:40Z (vrun.sh needs it). Open targets (RESUME POINT, none started):
- (a) A (Σ) pair with a COARSE_L(θ) rise (must end at a fallback with M_k < L by TEV-FB, RESULTS R40); it would hit RISE-LAST and
  test P-N5-ENT. Next: climb16.py new objective on rise events, seeded from the tx/conf bests, n ≥ 11 (all n ≤ 5 tables vacuous, R70 §3).
- (b) XSN-RUN aimed at n − 1 (best n − 2 at n 10, xrun8_n10). Next: random/biased search at n ≤ 12 with rnd16.py (exhaustive infeasible past n 5).
- (c) TEV-RED (5) configuration (TEVCONF): none seen. Next: conf climb with tevred16.py as the exact checker.
- (d) NJB's straddle after NL= fell (R70 §4, OPEN in GAPS G-N5-TIME); (β)-fallback count per scope run (2 seen, beta2_n11);
  "no fallback after a rise" (REFEREE-2; 1.5 M far-climb evaluations, no hit). Next: whichever the Lead routes; P-N5-LV2 is in review,
  so its LV-NONE / SCOPE-FB bounds (≤ 4·n·n_E + 3) are the nearest named lemma to attack.

## 3. docs/GAPS.md rows I own
- G-NEST (major; owner "L-RED (attacks + proof attempts); L-ALG successor if any"), status **open** (trunk docs/GAPS.md line 9).
  Its DTL line is paused under D18 (Lead reading L40).
- Attacked, not owned: G-N5-TIME (major, owner L-NEW, **open**, line 11; trunk text: "NL= FALSE (L-RED nleq_cex_n48, Lead re-run);
  NJB's straddle OPEN"). GAP-A, GAP-C (L-ALG, open; DTL paused).

## 4. The three owner rulings that most constrain me (verbatim), with their DECISIONS-INDEX status
1. D18 (docs/DECISIONS.md line 333), status **active** (DECISIONS-INDEX line 32):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
2. D1 (docs/DECISIONS.md line 7), status **active** (DECISIONS-INDEX line 5):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
3. D14 (docs/DECISIONS.md lines 245-246), status **active** (DECISIONS-INDEX line 22):
   > D
   > You know it can also test prveiously not tested approaches, it can come up with it own as well

## 5. One trap that bit this lane, and the check that now prevents it
- Trap (successor 16, R69 notebook trap 2): a borrowed checker narrower than its statement. L-SI's threv.py stops at the next
  fallback, so its "0 hits" could not refute TEV-LAST over the full window.
  Check now: write the exact checker from the frozen statement (rx16.py / tevred16.py), list each window/threshold of any borrowed
  checker against the packet text, and count a kill only with one Odd choice vertex, an Oink-verified run, and the exact obstruction.
- Also caught at this restart: stale clone (1703 behind), by fetch + reset + `rev-parse HEAD == origin/claude/l-red`.

## Successor 15 section (superseded): L-RED successor 15 (Opus 5.5, D15/D18; LANE-RESTART step 3; written 2026-10-25 ~01:05Z by date -u)
Every answer is measured from the repository (commands named), not recalled. Predecessor: successor 14
(session_01DYUCLfp4LkaCnY7moyVLAa), handover notebook notes/L-RED.md @ 97654ed9. Previous answers (successor 14) are in
history: `git show 97654ed9:docs/agents/handover-checks/L-RED.md`.

### 1. Branch, head, distance to trunk
- Branch `claude/l-red`. Container at start: local = 0d0b67a1, 706 commits behind origin/claude/l-red (stale; clean tree).
- `git fetch origin claude/l-red claude/vibrant-johnson-nxvvxo` (01:01Z): origin/claude/l-red = 97654ed9; trunk = 1ef02bb2.
- `git merge --ff-only origin/claude/l-red` -> 97654ed9 (local = origin/claude/l-red).
- `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` -> 0 ahead, 66 behind; merge-base 97654ed9
  (lane head is an ancestor of trunk). `git merge --no-edit origin/claude/vibrant-johnson-nxvvxo` fast-forwarded to 1ef02bb2:
  0 ahead / 0 behind before this file's commit (1 ahead after it). No rebase, amend or force-push.
- Packets pinned on trunk 1ef02bb2, sha1 re-measured (`git show <trunk>:<file> | sha1sum`): docs/new/P-N5-SO-box32.md deb5ee44…,
  docs/new/P-N5-LP-box32.md d2c8121a… (match the brief).

### 2. Open work and the next step of each
Nothing running in this container (`ps aux | grep -c python3` = 3: grep and harness only). Predecessor parked after box 35
with nothing in flight (notebook RESUME POINT).
- (A) Expected box (after GO, orientation only): adversary on P-N5-SO (Lemmas TH, SO, Corollary XJ) and P-N5-LP (used-level
  freeze, Theorem LP, Lemmas DF/BAND/WAKE, Corollary LP′). Next step: read both packets as frozen; check the statement of Lemma SO
  (S_o ≤ d_o(Θ+1); "minimiser set only shrinks with θ fixed, key of a surviving exit frozen") and P-N5-LP §4's J ≤ S_o against
  traces from n5.py; build a checker that tests the frozen statement exactly (trap 3), then climb for violations (o-cyclic 𝒞^1O,
  exactly one Odd vertex with out-degree > 1); then K (wakes per phase) growth. Seeds: j10_n24 (R64), u2flat73_n32 (R65).
- (B) Open kill targets from R62/R64/R65, not started: hand-built k-digit counter (R62 §1); J super-linear (R64 §2); K_W / E
  growth (R65). Next: fold J and K growth into (A).
- (C) (FBRE-F′) with the window at run index ≥ n, or excluding post-θ-change re-entries (R61): edit fbref.py's boundary and climb.
  Only if routed.
- (D) G-NEST (R48 §4): paused with the DTL line by L40 (1). Next only on a Lead route.

### 3. docs/GAPS.md rows I own
- G-NEST (major; owner "L-RED (attacks + proof attempts); L-ALG successor if any"), status **open** (docs/GAPS.md line 9).
- Attacked, not owned: GAP-A, GAP-C (L-ALG, open; DTL paused by L40); G-N5-TIME (L-NEW, open) is the target the N5 work attacks.

### 4. The three owner rulings that most constrain me (verbatim), with their DECISIONS-INDEX status
1. D18 (docs/DECISIONS.md line 333), status **active**:
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
   (Lead reading L40, active: L-RED is the N5 adversary; labels PROVED / CONJECTURE / OPEN; DTL paused.)
2. D15 (docs/DECISIONS.md line 278), status **active**:
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
   (Lead reading L37, active.)
3. D1 launch brief (docs/decisions/D001-launch-brief.md lines 92-93 and 99), status **active**:
   > Failing any step makes it a dead end, recorded with the exact obstruction or counterexample.
   > - Dead ends are kept, with the obstruction and the instance that killed them.

### 5. One trap that bit this lane, and the check that now prevents it
- Trap (R65, notebook trap 3): a reference checker (u23check.py) tested a weaker statement than the frozen packet P-N5-U23
  (U23 unchecked, (iii) at 2|R|), so "0 violations" from it would not have meant the frozen statement holds.
  Check now: read the frozen statement first, write my own checker against it (u23x.py), and list each threshold of any
  borrowed checker against the packet text before reporting. Applies directly to Lemma SO / J ≤ S_o.
- Also caught again at this restart: stale local branch (706 behind), by fetch + `merge --ff-only` + rev-parse before work.
