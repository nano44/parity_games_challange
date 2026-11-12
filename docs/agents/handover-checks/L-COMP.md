# Handover check: L-COMP (successor 20, session_01V5yGRYzeDgxCBBXtVUzaJi; model and effort as the Lead set them under D21 / L51; written 2026-11-12T17:11Z by date -u)
Every answer measured from the repository at the time of writing. Successor of L-COMP 19 (handover «HANDOVER -- successor 19 (L-COMP 19;
session_01V5yGRY8iNCAZqwL8HSCXM2) PARKS 2026-11-12 (date -u in the park commit) after BOX 43. NOTHING RUNNING.», notes/L-COMP.md l. 4,
commits ae0f65c3 and a6cce717). This OVERWRITES successor 19's answers (in git history).

## 1. Branch, head, distance to trunk
- Container started on a stale local branch (1,619 commits behind origin/claude/l-comp). `git fetch --unshallow` + `git fetch origin
  claude/l-comp claude/vibrant-johnson-nxvvxo` + `git checkout claude/l-comp` + `git merge --ff-only origin/claude/l-comp` ->
  fast-forward. Working tree clean (`git status --short`: 0 lines).
- Branch `claude/l-comp` (`git branch --show-current`), HEAD = origin/claude/l-comp = a6cce71722db (rev-parse; = `git ls-remote origin
  claude/l-comp`), commit date 2026-11-12T15:47:03Z («L-COMP 19 BOX 43 item 3: TMWR48 and MWR48_2 on my engine ...»).
- Trunk origin/claude/vibrant-johnson-nxvvxo = 68c8d29339d5 («Lead: R128 first fill (P-N5-GATE over L-4 6bfde78e @ l-si 676b6a1c ...»,
  commit date 15:06:33Z). `git rev-list --left-right --count HEAD...trunk` = 198 ahead / 477 behind; merge-base ebf59a34f6c8. +1 ahead
  after this commit.
- Other lanes at my fetch (17:10Z): l-si 26704e01f901 (box 104 FREEZE), l-new 311bbf81faa5 (box 209 Add. A / box 210 Add. A), l-red
  09fa5e17e93b (one commit after 7317ed4c, the R236 classification), l-lit 9ae31ec3dfb7.
- Clock: local `date -u` 17:09:39-40Z against `date: Thu, 12 Nov 2026 17:09:40 GMT` of raw.githubusercontent.com: skew ≤ 1 s. NOT
  measured against github.com itself: its responses through this container's proxy carry no Date header (git info/refs 200 without
  Date; plain pages 400 / 403).
- Container: 4 cores, 15 GB RAM, fresh clone. No job of mine runs; `pgrep -f "bash scripts/push.sh"` empty. NOT in this clone (to be
  rebuilt / recreated before use): bin/ (box36/bin(+k), box37/bin, box38/bin) and their .git/info/exclude lines; tools/oink/build
  (verify's Oink smoke prints NOT RUN until scripts/setup_oink.sh has run); every second-engine archive of successor 19's scratchpad
  (eng/lsi100, eng/red, eng/lnew, eng/lnew208, eng/llit; rebuilt with `git archive <sha> <paths> | tar -x -C <dir>`).

## 2. Open work and the next step of each (all DATA; nothing runs; BOX 44 waits for «go»)
- BOXES 39-43: DONE (records = experiments/comp/box39..box43/README.md). Left open by 19's handover (notes/L-COMP.md l. 22-24), none
  started: (a) a depth notion TAIL cannot inflate and its count on the frozen sets; (b) the per-gate quiet-flip maximum beyond linear;
  (c) re-run run43a.sh if L-NEW publishes a --hist form of plat208.py. None is in the Lead's BOX 44; they stay open unless routed.
- MISS TO RECORD: the Lead's brief says 19's open items «list the F_n replay and the box 209 own-builder replay». At a6cce717
  `grep -n -E 'F_n|WRAP|box 104' notes/L-COMP.md` has no hit and «209» occurs only as an old iteration count (l. 470). Those two items
  exist only in the Lead's brief (BOX 44 items 1 and 2 below); I take them from there.
- BOX 44 item 1 (WRAP, third engine; after «go»). Target: claude/l-si 26704e01 docs/si/box104-map.md (Lemma WRAP, FREE-REACH),
  experiments/si/box104/ (wrap104.py, free104.py, inst/ F_2..F_8.pg, W_2..W_8.pg, WL_1..WL_4.pg, rand300.json, SHA1SUMS, out/). Next
  step: read the construction of W(H, s0) in the TEXT and quote its lines in my README; write my own builder from the text (not from
  wrap104.py); compare my build with the frozen .pg files (byte equality after canonical relabelling, else vertex / edge / priority /
  owner isomorphism; mismatches reported exactly); run N5′-xi from S3 on my engine (box34/own34.py's n5b SPEC + [N5XI] step, or a fresh
  one from SPEC + box 190's ξ rule) and Howard (switch-best, VJ values) on H; the six must-0 counters (S3 standard; standard states;
  every step a best successor by H's own valuation; fallback at T + 1; total T + 3 with one fallback; regions = Zielonka) on the 300
  random games, W_n, F_n n = 2..8, W(G_n, ι) n = 1..4; firing controls; classify any count difference (tie rule / start / fallback /
  real) as L-RED 66 did in R236 (claude/l-red 7317ed4c, experiments/red/r236/).
- BOX 44 item 2 (box 209, own builder). Target: claude/l-new 311bbf81 docs/new/N5-LEVEL3-box209.md (+ Addendum A),
  experiments/new/box209/. Next step: replay box 209's must-0 counters (LEVEL3, PLATEAU3, T3-ALL bound, N5XI-G3 iteration identity
  T3 + 3) on my own Γ3 builder (box34/own34.py) for L-NEW's frozen genomes and 1,000 random genomes; report T3 against the T3-ALL bound
  P3(n_E3 + 1) + n_E3, P3 = 2M(N + 4M), n_E3 = N + 6M + 9 (max ratio and the largest T3 seen).
- BOX 44 item 3 (if budget remains): a climb on T3 / (N + M) at N + M ≈ 300, two seed streams, bests on a second engine and frozen; a
  fit or «NOT identified».
- Limits I keep: at most 2 CPU-heavy jobs; every long job resumable and run as a tracked background task; no long job before «go».
- Alert rule (carried): anything faster than polynomial within one family, or any must-0 counter that fires outside its control ->
  Lead at once, frozen instance, two-engine numbers.

## 3. docs/GAPS.md rows owned by L-COMP
None (trunk 68c8d293 docs/GAPS.md: open rows GAP-A, GAP-C, G-S5-6, G-NEST, G-N1-LB, G-N5-TIME; none has owner L-COMP). Mention only:
G-N5-TERM (l. 16, owner «L-NEW (L-COMP checks runs)», closed). BOX 44 is DATA for G-N5-TIME (l. 11, owner L-NEW, open), on lane-level,
unrefereed items: L-SI 52's Lemma WRAP (box 104) and L-NEW's box 209 (CANDIDATE: LEVEL3, PLATEAU3, T3-ALL, N5XI-G3).

## 4. Three owner rulings that most constrain this lane (verbatim; status from trunk docs/DECISIONS-INDEX.md)
1. D18 (active, DECISIONS-INDEX.md:32; text docs/DECISIONS.md:333): «Focus on N5 and work toward proving it. Explore novel approaches,
   especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable
   assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from
   conjectures and open problems.»
2. D1 (active, DECISIONS-INDEX.md:5; docs/decisions/D001-launch-brief.md:25-26, excerpt): «A claimed polynomial algorithm is far more
   likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.»
3. D21 (active, DECISIONS-INDEX.md:46; docs/DECISIONS.md:451-454): «Okay, I want maximum effort. I want to use 200% usage in 3 days.
   There is fable 5.2 as well, use that too in dpeth everywhere where it seems fitting, use fable 5.2 at hard or xhigh. SO yes, 200%
   uage under 2 days.» (direct confirmation: «I confrim tge stuff»). Lead reading L51 (active, :47), not the owner's words: maximum
   effort to 2026-11-14 10:05Z; overage not expected (if seen: tell owner, spawn nothing new); gauntlet, landing rules and no-contact
   unchanged.

## 5. One trap that bit this lane, and the check that now prevents it
Trap: stale container start (this start: 1,619 commits behind origin while the checkout looked normal), which makes pushes fail with
«invalid refspec» and would have had me read an old notebook. Check: fetch --unshallow + fetch by branch name + ff-only +
`git branch --show-current` = claude/l-comp + HEAD == origin/claude/l-comp == ls-remote, before any read or edit (done above).
Carried from 17-19: `pgrep -f "bash scripts/push.sh"` empty before every commit and push (a commit was once made while a push ran,
88ac6b07); push.sh as a tracked background task with a 2-hour timeout, output redirected, exit code echoed, no pipes, never «&» (19's
slip); no model name in a commit (19's slip); SHAs quoted only from git output in a later step; every number names its counter (unit,
set, scope); a must-0 counter is trusted only after its control fires. New for BOX 44: an «own builder» is own only if written from
the TEXT: I open wrap104.py / L-NEW's Γ3 code only AFTER my build is compared with the frozen instances, and say so in the README.
