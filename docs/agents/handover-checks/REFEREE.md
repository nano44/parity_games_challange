# Handover check: REFEREE

## successor 9 (2026-10-25T14:45Z by date -u; Opus 5.5 under D15/L37, label "(Opus 5.5, D15)"; predecessor successor 8, handover 4efa2a6f)
Measured from the repository at the time of writing, not recalled.

### 1. Branch, head, distance to trunk
- Branch `claude/referee`. Local branch started STALE (1505 behind origin/claude/referee). `git fetch origin claude/referee` and
  `git checkout -B claude/referee origin/claude/referee`: HEAD = origin/claude/referee = 4efa2a6f (checked with `git rev-parse`).
- Trunk = remote HEAD `claude/vibrant-johnson-nxvvxo` (`git ls-remote --symref origin HEAD`) at efa00f59 (Lead: R39 draft -> C48).
  Before merging: 3 ahead / 8 behind trunk (merge-base 1aeff933). The 8 behind: REFEREE-2 succ. 9's R2-N5-ENT (b7df84b8), OUT §C
  (2a9e8db0), ENT §C (f33884e6), their merges, and Lead commits 3a086cca, efa00f59.
- Merged trunk with `git merge --no-ff` (00bea06f): 4 ahead / 0 behind before this file's commit (merge-base efa00f59).

### 2. Open work and next step of each
- Nothing in flight. Successor 8's table: RL (R37), P1 (R36), SCOPE (R38), OUT (R39 draft, CHECKER C48), ENT all signed with §C done;
  REFEREE-2's OUT and ENT §Cs (2a9e8db0, f33884e6) report identical verdicts and an empty gap map, so nothing returns to me from them.
- Next: wait for the Lead's GO and next packet brief. On a new packet: verify the packet sha1 at its pin, build Oink
  (scripts/setup_oink.sh; not yet built in this container), reuse own tools in docs/referee/scratch/ (rl_engine.py, rl_probe.py, NO
  lane imports), report under docs/referee/R-<packet>.md before reading any docs/referee-2/R2-<packet>.
- Small item seen in LEAD-STATE 14:24Z (CHECKER 30fda11): my lane's SCOPE climb maxima rest on report text only, no committed log.
  If the Lead wants it, I can re-run the SCOPE climbs and commit the log under docs/referee/ (not started; awaiting routing).

### 3. docs/GAPS.md rows relevant to me (trunk efa00f59)
- REFEREE owns no row. The row my packets feed: G-N5-TIME | major | owner L-NEW (L-LIT T22; referees later) | **open**. Latest
  UPDATE 14:16Z: R38 (P-N5-SCOPE) LANDED; open: out-of-SN fallbacks (OUT-POLY CONJECTURE; P-N5-OUT signed by both referees, landing
  next = R39), NJB = ENT, REL(S), level −1. Related closed: G-N5-TERM (R15). DTL rows (GAP-A, GAP-C, G-S5-6, G-NEST) open but paused (D18/L40).

### 4. Three owner rulings that most constrain me (verbatim, docs/DECISIONS.md), with DECISIONS-INDEX status
1. D1 (index l.5: **active**, 2026-10-14; DECISIONS.md l.7): "A claimed polynomial algorithm is far more likely to be wrong than right.
   Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below."
2. D15 (index l.26: **active**, 2026-10-22; DECISIONS.md l.278): "q18 b. , q16 b,c. BUt I dont want it to ask these questions from me.
   Be autonomous, reason about it"
3. D18 (index l.32: **active**, 2026-10-24; DECISIONS.md l.333): "Focus on N5 and work toward proving it. Explore novel approaches,
   especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable
   assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from
   conjectures and open problems."

### 5. One trap that bit this lane, and the check that prevents it
- Trap (successor 8, N-ENT-2, missed by me, caught by REFEREE-2): copying a packet's "vacuous in data" line. REFEREE-2 found the NJB-A
  hypothesis actually occurs (698 / 601 / 701 cases). Check: for every hypothesis a packet calls vacuous or unreached, count its
  occurrences with my own probe and report the count, never the packet's word.
- Also again this restart: the clone started stale (1505 behind origin/claude/referee); checked `git rev-parse HEAD origin/claude/referee`
  equal before any work.

## successor 6 (2026-10-25T01:24Z by date -u; Opus 5.5 under D15/L37, label "(Opus 5.5, D15)"; predecessor successor 5, handover bb6f60f5)
Measured from the repository at the time of writing, not recalled.

### 1. Branch, head, distance to trunk
- Branch `claude/referee`. Local branch was STALE (73b46eb8, 672 behind origin). After `git fetch origin claude/referee
  claude/vibrant-johnson-nxvvxo` and `git merge --ff-only origin/claude/referee`: HEAD = origin/claude/referee = bb6f60f5.
- `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` -> 2 ahead, 16 behind (trunk 32f0a5e2;
  merge-base 82ba756f). The 2 ahead: 94df88bc (trunk merge) and bb6f60f5 (R-N5-LP §C). The 16 behind are Lead/lane merges
  (latest 32f0a5e2; includes L-NEW's P-N5-LP fixes file 459660c3).
- UPDATE 01:30Z (date -u): my first push was rejected: origin/claude/referee had moved to 2a0cb306 (predecessor successor 5,
  session_01VQrdgN…, 01:19Z: "R-N5-LP Part 2 addendum: SO-1 closed", via R2-N5-FB §C.3, referee-2 eb10cf7). Merged it with a
  normal merge (afa95369). Now 6 ahead / 14 behind trunk 32f0a5e2, merge-base 956359fc (before this file's commit).

### 2. Open work and next step of each
- In flight: none. Routed by the Lead's brief, waiting for GO: REFEREE's §C on packet P-N5-SO, object docs/new/P-N5-SO-box32.md
  at pin 1ef02bb (ancestor of HEAD; `git show 1ef02bb:docs/new/P-N5-SO-box32.md | sha1sum` = deb5ee4422da3ab7389ce35e4542977927b53886,
  54 lines: matches the brief). Inputs: my predecessor's review = docs/referee/R-N5-LP.md Part 2 (dcb4119; TH with SO-1 = dependency
  on R-N5-FB §4.2 full-minimiser proof, SO signed, XJ with XJ-1: f = O(n⁴(1+X)), not n³); REFEREE-2's R2-N5-LP.md §8 (ba67f41) and
  R2-N5-FB.md §C.3. Next step after GO: compare the two reviews row by row, write the joint gap map (one fixes-file line per row),
  rule on whether SO-1 is closed by REFEREE-2's adoption of the §4.2 proof (re-reading §4.2 myself; the predecessor's addendum
  2a0cb306 already says CLOSED and Lemma TH SIGNED: I check that independently, I do not inherit it), in docs/referee/R-N5-LP.md as
  §C-SO (or a section the Lead names). Probes, if any, assert exactly one Odd vertex with out-degree > 1.
- Earlier packets (P-N5-U1, FB, U23, LP; R19-R22, Z) all signed with §C done (notebook table). Open items held: none routed.
- Before running probes: rebuild Oink (scripts/setup_oink.sh; tools/ is gitignored).

### 3. docs/GAPS.md rows relevant to me (trunk 32f0a5e2)
- REFEREE owns no row. The row my packets feed: G-N5-TIME, major, owner L-NEW ("referees later"), OPEN. Last update: RESULTS R26
  landed; L-NEW box 32 packet P-N5-LP (Theorem LP, Corollary LP′, phase O(m n⁵ (1 + S_o + X + K)) on 𝒞^1O) with both referees;
  (KW-M) FALSE, NO-WAKE FALSE; S_o, X, K OPEN; L-SI (CL-S) CONJECTURE.
- G-N5-TERM closed (RESULTS R15). DTL rows GAP-A, GAP-C, G-S5-6, G-NEST open but DTL paused (D18/L40).

### 4. Three owner rulings that most constrain me (verbatim, docs/DECISIONS.md), with DECISIONS-INDEX status
1. D1 (index: active; docs/DECISIONS.md lines 7-8):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D15 (index: active; Lead reading L37 active: referees on Opus 5.5, label "(Opus 5.5, D15)"):
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
3. D18 (index: active; Lead reading L40 active: labels PROVED (by whom) / CONJECTURE / OPEN):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.

### 5. One trap that bit this lane, and the check that prevents it
- Trap (R-N5-LP / R-N5-FB, notebook lesson): VJ00 Lemma 5.8 "maximum ⇒ no improvement" (2 ⇒ 3) and "SPEC's σ̄ is VJ00's minimiser"
  both FAIL at own cycle nodes (FIX 2 DFS): Lemma DF was false (docs/referee/R-N5-LP/df_cex.pg, n 11) and CAP-1 had 925 cases.
  This is exactly what SO-1 turns on. Check: before signing any step that uses σ̄ as a minimiser or cites Lemma 5.8, test it at own
  cycle nodes explicitly (fb_probe.py / lp_probe.py modes), and verify which form (coarse vs full minimiser) the step uses.
- Also again this restart: stale local branch (73b46eb8, 672 behind); check `git rev-parse HEAD origin/claude/referee` equal before work.
