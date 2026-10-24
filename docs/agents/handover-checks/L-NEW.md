# Handover check: L-NEW (successor 9, Opus 5.5 per owner D15 / Lead reading L37; written 2026-10-24 04:36Z by date -u)
Replaces the previous answers (Lead brief 04:36Z); successors 1-8's answers are in git history before this commit. Every answer
is measured from the repository at writing time (commands named), not recalled. Predecessor: successor 8,
session_017FJfp8hdPrDYKY1EZFYH16, parked after box 24 (notes/L-NEW.md resume point ~04:30Z).

### 1. Branch, head, ahead/behind trunk
- Branch claude/l-new. After `git fetch origin claude/vibrant-johnson-nxvvxo claude/l-new` the container was STALE: local 5961101a,
  origin/claude/l-new d4e1781b (171 behind). Fast-forwarded to d4e1781b.
- `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` at d4e1781b: 0 ahead, 45 behind trunk 01e4c9df.
- Trunk was a pure descendant, so `git merge --ff-only origin/claude/vibrant-johnson-nxvvxo`: fast-forward, no merge commit.
  Before this file's commit HEAD = 01e4c9df, 0 ahead / 0 behind; after it 1 ahead (this commit), 0 behind.

### 2. Open work and the next step of each
Nothing of mine is running. tools/oink/build and experiments/new/out/ are absent in this container (run scripts/setup_oink.sh
before any check_sol2 / Oink-verified run).
- Box 25 (after GO only; Lead brief "for context"): (CYC), N5 on o-CYCLIC 𝒞^1O, as designer. State (docs/new/N5-1Ocyc-box24.md
  §1-§2, §5): Lemma 1 holds on all of 𝒞^1O; Lemma 2 (θ = w at pure steps) breaks through self-throttling exits; smallest case cyc4
  (n 4, experiments/new/box22/instances/cyc4.pg, sha1 bff7a8c2…, re-measured); canonical example fts_best16
  (experiments/new/box21/instances/fts_best16.pg). Next step: an o-cyclic replacement for Lemma 2/3 that bounds θ-changes inside
  self-throttled stretches (ring structure: exits on one σ-path back to o, R58 §10), starting from Lemma 2' (proved under (H)) and
  box22/incomplete.py; any bound I believe goes to the Lead at once, labelled READING (D1).
- R18 (o-acyclic theorem, conditional on (P)): the Lead's to land after CHECKER C27; nothing for me unless C27 or the referees ask.
- Relay: L-RED box 28 (to ~07:35Z) is attacking with a nested-ring kill on o-cyclic 𝒞^1O; results reach me via the Lead.
- Other open targets from the notebook, not routed: (FO*) frozen-τ* runs in general; (BR*) ∧ (SEG-LEN*); (ALT).

### 3. docs/GAPS.md rows I own (`grep -n "L-NEW" docs/GAPS.md` at 01e4c9df)
- **G-N5-TIME** (major; owner "L-NEW (L-LIT T22; referees later)"; status **open**). R18's draft says o-acyclic 𝒞^1O closes
  conditional on (P) on landing; o-cyclic 𝒞^1O and the general case stay open.
- **G-N1-LB** (minor; owner "L-NEW (optional; not routed)"; status **open**).
- **G-N5-TERM** (major; owner "L-NEW (L-COMP checks runs)"; status **closed**, RESULTS R15).

### 4. The three owner rulings that most constrain me (verbatim), with index status
1. D1 (docs/decisions/D001-launch-brief.md l.25; DECISIONS-INDEX row D1 "active"; restated in L35 (3)):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   Box 25 is a proof attempt on a subclass: a believed bound goes to the Lead at once, labelled READING until refereed.
2. D14 (docs/DECISIONS.md#d14; DECISIONS-INDEX row D14 "active"):
   > D
   > You know it can also test prveiously not tested approaches, it can come up with it own as well
3. D15 (docs/DECISIONS.md#d15; DECISIONS-INDEX row D15 "active"):
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
   Lead reading L37 (active): main effort (c), L-NEW on N5; no option questions to the owner; I decide inside the brief and report.

### 5. One trap, and the check that prevents it
- Trap: a lemma proved on one class read as holding on a wider one. Box 24's sketch (§6 of the signed text) said Lemma 1 "has no
  analogue" on o-cyclic games, while REFEREE-2 (N-3) showed Lemma 1 holds on all of 𝒞^1O and only Lemma 2 breaks; and earlier,
  one-player statements read as two-player (R17 vs seg_r16 / vc_g25; K9's (P*) vs CDAG_n). Check: before labelling any box-25
  lemma PROVED, run it with statcheck.py / incomplete.py on the pinned o-cyclic instances (cyc4, fts_best16, i1h_fts_best16) and
  the two-player counterexamples, and state exactly which class and which player's moves it covers.
- Also carried: stale container (caught again here, 171 behind: fetch + `git rev-parse HEAD origin/claude/l-new` first);
  ReadNotifications at each milestone; push.sh output to a file, then `$?`; pkill -f matches my own shell.
