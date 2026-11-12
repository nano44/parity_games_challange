# Handover check: REFEREE

## successor 32 (2026-11-12T11:46Z by date -u; predecessor successor 31, HANDOVER NOTE in notes/REFEREE.md at 175f125d)
Measured from the repository at the time of writing, not recalled. The model label is left out of repository files (this session's
harness rule); the Lead's brief names it.

### 1. Branch, head, distance to trunk
- Trap check: `git fetch --unshallow` + fetch of claude/referee and trunk; local claude/referee was 1300 behind origin, fast-forwarded
  with `git merge --ff-only`; `git branch --show-current` = claude/referee; HEAD = origin/claude/referee = 175f125d.
- At 175f125d: 3 ahead / 73 behind trunk claude/vibrant-johnson-nxvvxo 9c83214f (merge-base fbc4d865).
- Merged trunk with a normal merge ab23e17f (no rebase): 4/0 ahead/behind before this file's commit. Trunk re-fetched after the merge:
  still 9c83214f.

### 2. Open work and next step of each (all after «go», in the Lead's order; a byte test or CHECKER item with a SHA from the Lead preempts)
- Predecessor's open queue (notes/REFEREE.md, HANDOVER NOTE successor 31): none on QN / SPLIT / GATE. Landed per docs/RESULTS.md at
  9c83214f: R124, R125, R126 headings present; R127 (P-N5-SPLIT) and R128 (P-N5-GATE) not yet.
- A. Byte test / CHECKER item on R127 (P-N5-SPLIT, L-3 MATCHES in R-P-N5-SPLIT.md §E; fill at CHECKER C141) or on P-N5-GATE (R128, L-4
  MATCHES in R-P-N5-GATE.md §K). Nothing in hand. Next step when a SHA comes: re-run scratch/split_l3.py / gate_l4.py against the routed
  bytes; at GATE's landing confirm R127 = P-N5-SPLIT carries SPLIT-COUNT and C-EQUIV (LT-1 landing-order form), else L-4 is regenerated.
- B. PRE-PACKET READ (not a signature, labelled so) of L-NEW 72's box 208, docs/new/N5-LEVEL-box208.md on claude/l-new (SHA from the Lead
  when on origin): CANDIDATE Lemma LEVEL (potential (m_t, −|FRONT_t|) against Howard on IDEAL-CYC) and Theorem WIN (polynomial T_CYC at
  Ξ-feedback number k = 1; T_CYC ≤ (P + N)(P + 1)^k in general; IDEAL-CYC on Γ(G) only). Next: fetch the SHA, sha1 the file; re-derive
  step by step, on my own, (i) each premise against landed RESULTS text by script, (ii) the «unless FRONT contains a whole Ξ_(σ_b)-cycle»
  step, (iii) the counting; name the step that uses a genome-only fact (Friedmann's G_N, arXiv 1106.0778, outside the genome class, must
  defeat any argument without one); own-engine replay with firing controls where a step is checkable. Report
  docs/referee/R-box208-preread.md; verdict «no gap found» / GAP (exact) / FALSE (instance).
- C. Byte tests the Lead sends.

### 3. docs/GAPS.md rows relevant to me (trunk 9c83214f)
- REFEREE owns no row. Row the N5 packets feed into: G-N5-TIME (line 11; owner «L-NEW (L-LIT T22; referees later)»; open).

### 4. Three owner rulings that most constrain me (verbatim, docs/DECISIONS.md), with DECISIONS-INDEX status
1. D1 (index: active; DECISIONS.md lines 7-8):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D18 (index: active; DECISIONS.md line 333):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
3. D20 (index: active; DECISIONS.md line 423):
   > We have reset the weekly usage, so we can again work faster no?
- D21: named in the Lead's brief (2026-11-12, owner; the brief's words «maximum effort for two days», not a verbatim owner quote in my
  hands). NOT in docs/DECISIONS.md or docs/DECISIONS-INDEX.md at trunk 9c83214f (index ends at L50; the trunk head's subject says «owner
  relay D21 held pending direct confirmation»). I quote it only once it is in DECISIONS.md.

### 5. One trap that bit this lane, and the check that prevents it
- Trap (s27-s32; this restart 1300 behind): stale local branch. Check: fetch, ff-only, `git branch --show-current` and
  `git rev-parse HEAD origin/claude/referee` equal before any push.sh (done above).
- Trap (s31, R-P-N5-SPLIT §E): two tool outputs printed back to back, maxc misread as maxSPL; a note had to be withdrawn. Check: one
  command per claim, and a number enters a report only from the output of the command that printed it.
- Trap (s28-s31): times written from memory. Check: `D=$(date -u ...)` pasted into the text in the same command (this file's time came
  that way).
