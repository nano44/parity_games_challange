# Handover check: REFEREE

## successor 33 (2026-11-12T17:09Z by date -u; predecessor successor 32, HANDOVER NOTE in notes/REFEREE.md at 890daf41)
Measured from the repository at the time of writing, not recalled. The model label is left out of repository files (this session's
harness rule); the Lead's brief names it.

### 1. Branch, head, distance to trunk
- Trap check: `git fetch --unshallow` (repository not shallow: `git rev-parse --is-shallow-repository` = false) + fetch of claude/referee
  and trunk; the local branch was already claude/referee and 0 behind origin; `git merge --ff-only origin/claude/referee`: «Already up
  to date.»; `git branch --show-current` = claude/referee; HEAD = origin/claude/referee = 890daf41b627445e37eff8d6f6d3d5be1ff31946.
- At 890daf41: 6 ahead / 19 behind trunk claude/vibrant-johnson-nxvvxo 68c8d293 (merge-base 471aba45).
- Merged trunk with a normal merge fbc8e4ed (no rebase): 7 ahead / 0 behind before this file's commit. That merge commit carries git's
  default message and no trailer (made by `git merge --no-edit`); not amended (no-amend rule). Later commits carry this session's
  Claude-Session line only.
- Clock: local `date -u` 2026-11-12 17:08:00 against «date: Thu, 12 Nov 2026 17:08:00 GMT» of a raw.githubusercontent.com response in
  the same command: skew 0 s (to the second). github.com itself answers HEAD and GET through this container's proxy with 400 / 403 and
  no Date header, so the measurement is against that GitHub host, not github.com.
- This session's worker was restarted once during the check (about 16:10Z to 17:06Z by date -u, no work in flight, nothing committed
  before it); branch, HEAD and «no push running» were re-measured after it.

### 2. Open work and next step of each (all after «go», in the Lead's order; a Lead message with a SHA for an item preempts after the section in hand is committed)
- Predecessor's open queue (notes/REFEREE.md, HANDOVER NOTE successor 32): the formal first review of P-N5-LEVEL if box 208 is frozen;
  any byte test / CHECKER item on R127 (C141) or P-N5-GATE (R128); a RESTRICT-C packet if L-SI freezes one. Measured now: R127 is in
  docs/RESULTS.md at trunk 68c8d293 (l. 15903) and CHECKER C141 is CLOSED (claude/checker 533ccefb); no R128 heading in RESULTS.md yet
  (trunk head's subject: «R128 first fill … for C142»).
- A. PRE-READ (not a signature) of L-SI 52's Lemma WRAP (box 104; docs/si/box104-map.md is on origin/claude/l-si, head 26704e01 «box
  104 FREEZE»; I take the object only from the SHA the Lead sends). Next: fetch that SHA, sha1 the file; re-derive the proof step by
  step with focus on the new step (W4); recount the wrapper's size n + 7·m_E + 6·m_O + n_O + 9 from the construction; open the PDF of
  Friedmann, LMCS 7(3:19) 2011 (arXiv 1106.0778) myself and read Theorem 6.14 with the definition of the improvement policy it is
  stated for, to decide the tie item (is VJ switch-best with the lane's tie rule an instance of that policy as the theorem uses it);
  own replay of WRAP's six counters written from my own reading, with firing controls. Report docs/referee/R-WRAP-preread.md, GAP /
  no-gap per step.
- B. FIRST REVIEW (a signature, separate from the pre-read) of packet P-N5-LEVEL when L-NEW 73 freezes it and the Lead routes it. Next:
  read the frozen packet afresh; disclose R-box208-preread.md (7524342b) as prior work of this lane; test PR-1..PR-6, the two Lead
  caveats (ALL-SWITCH only; MAXIMISER-improves), the E-DOM / genome scope and the genome-only steps; premises by script against landed
  RESULTS; the DATA rule on the lane's tools (level208.py / plat208.py were not opened by my predecessor); Lean cited by theorem name
  and commit as «Lean-checked (lane)» unless CHECKER has passed it (own build by the notebook's recipe if the packet leans on it).
- C. PRE-READ of box 209 (T3-ALL, N5XI-G3; docs/new/N5-LEVEL3-box209.md) and its Addendum A (on origin/claude/l-new, head 311bbf81), if
  no packet arrives first.
- D. Any CHECKER item on R128 (P-N5-GATE; L-4 MATCHES in R-P-N5-GATE.md §K). Nothing in hand. Next when a SHA comes: re-run
  scratch/gate_l4.py against the routed bytes.

### 3. docs/GAPS.md rows relevant to me (trunk 68c8d293)
- REFEREE owns no row. Row the N5 packets feed into: G-N5-TIME (line 11; severity major; owner «L-NEW (L-LIT T22; referees later)»;
  status open).

### 4. Three owner rulings that most constrain me (verbatim, docs/DECISIONS.md at trunk 68c8d293), with DECISIONS-INDEX status
1. D1 (index: active; DECISIONS.md lines 7-8):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D18 (index: active; DECISIONS.md line 333):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
3. D21 (index: active; DECISIONS.md line 452, «Relayed text (OWNER-DESK, verbatim)», confirmed by the owner in the Lead session per
   line 451):
   > Okay, I want maximum effort. I want to use 200% usage in 3 days. There is fable 5.2 as well, use that too in dpeth everywhere where it seems fitting, use fable 5.2 at hard or xhigh. SO yes, 200% uage under 2 days.
   (Lead reading L51, not owner words: Fable 5.2 at xhigh for referee successors; gauntlet, landing rules and D1 unchanged.)

### 5. One trap that bit this lane, and the check that prevents it
- Trap (s27-s32): stale local branch (1300 behind at s32's start; 0 behind this time). Check: fetch, ff-only, `git branch
  --show-current` and `git rev-parse HEAD origin/claude/referee` equal before any push.sh (done above, and again after the restart).
- Trap (s32, G-P6): an induction run past the interval its lemma was proved on. Check for item A's (W4) and item B's (P6): for each
  inductive step, write down which states the cited fact was proved for, and whether the step's state lies among them.
- Trap (s31): two tool outputs printed back to back, misread. Check: one command per claim; a number enters a report only from the
  output of the command that printed it; SHAs only from git output in a step after the commit.
- Trap (this restart): `rev | cut` on a 13,222-character line of docs/NOW.md hung until the 120 s limit. Check: long-line files
  (NOW.md, GAPS.md, RESULTS.md) are read with a script that slices by character, never with rev / sed on whole lines.
- Trap (s28-s31): times written from memory. Check: date -u in the same command (this file's stamp was inserted that way).
