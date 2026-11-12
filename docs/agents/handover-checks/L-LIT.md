# Handover check: L-LIT (successor after T65-T68, N5-route literature; written 2026-11-12T12:50Z by date -u; LANE-RESTART step 3)
Every answer measured from the repository at the time of writing (commands given). Predecessor's check: git history (627402e7).
Read before writing: CLAUDE.md, TARGET.md, docs/agents/LANE-RESTART.md (procedure + L-LIT rows), trunk's docs/NOW.md, docs/DECISIONS-INDEX.md,
docs/DECISIONS.md (D1, D18, D21 / L51), docs/GAPS.md (rows naming L-LIT), notes/L-LIT.md (HANDOVER, Queue, Things only I know),
docs/lit/T65, T66 (with Addenda A, B), T67 in full. docs/sources/landscape-2026.md: keyword skim only so far (secondary; full read at «go»).

## 1. Branch, head, distance to trunk
- Trap check run first: `git fetch --unshallow origin` (no-op; `git rev-parse --is-shallow-repository` -> false), then
  `git fetch origin claude/l-lit claude/vibrant-johnson-nxvvxo claude/l-new claude/l-si`, `git checkout claude/l-lit`,
  `git merge --ff-only origin/claude/l-lit`. The container's local branch was STALE: «Your branch is behind 'origin/claude/l-lit' by 5
  commits» (it sat at 6895fb31, T64); the fast-forward fixed it.
- `git branch --show-current` -> claude/l-lit. `git rev-parse HEAD origin/claude/l-lit` -> a19fff230e4c91367e6e15fb3b62724b56aa70b9
  twice (the predecessor's HANDOVER commit). Not detached.
- `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` -> 5 ahead, 1662 behind (trunk
  471aba45214c9b4009332ef1d498dd5dbc42f3cb). `git merge-base` -> 6895fb3183c993f45ca222bd54e6728bb0730d40 (T64). HEAD is not an ancestor of
  trunk (the five commits 627402e7, f5fff985, 5c53efbd, 6d5e619d, a19fff23 are lane-only). Trunk is NOT merged into this branch (Lead's
  word), so NOW / DECISIONS / GAPS / RESULTS on this branch are stale; I read them with `git show origin/claude/vibrant-johnson-nxvvxo:<file>`.

## 2. Open work and next step
- Predecessor IN FLIGHT (notes/L-LIT.md l. 23-33): nothing half-written. Two T68 remainders:
  - T68 item 3, remaining: the E-DOM test for the ranking (Disser–Loho–Maat–Mosis, arXiv 2512.16684), symmetric (van Dijk–Loho–Maat, arXiv
    2309.02223) and Mei (arXiv 2610.27386) families. Next step: open each paper, read its priority table as in T66 Addendum B (Odd choice
    vertices, their even escape, odd priorities above it), append the result to docs/lit/T66-deep3-lower-bound-families.md as an addendum.
  - T68 item 2: run L-NEW 72's box 208 must-0 counters on Friedmann's G_N and switchallexp. BLOCKED on the tool: `git ls-tree -r
    origin/claude/l-new` at 25835c59 (L-NEW 72's handover check, 10:41Z) has no box 208 file. Next step: only when the Lead sends the SHA.
- T69 (Lead brief of this session): Dijkstra-type potentials against policy iteration. Is Lemma LEVEL's argument ((m_t, −|FRONT_t|) never
  falls; rises strictly unless FRONT contains a whole Ξ-cycle) known? Next steps: open (not from memory) Cochet-Terrasson–Gaubert (re-fetch;
  PostScript), Hansen–Kaplan–Zwick «Dantzig's pivoting rule for shortest paths, deterministic MDPs, and minimum cost to time ratio cycles»,
  Post–Ye, Madani, the Fearnley / Hansen–Miltersen–Zwick constant-discount line, and the parameterized results (Gajarský et al.; treewidth /
  DAG-width / feedback-vertex-set / few-Odd-vertices parameterizations of parity games); read box 208 on claude/l-new when it exists (the
  Lead's brief is my only statement of LEVEL / WIN so far); classify LEVEL / WIN's fixed-k bound KNOWN / IMPLIED / NEW / CONTRADICTS and say
  whether a fixed-k polynomial bound for Howard, or for parity-game solving with k «controller» vertices, is published.
- Deliverables: docs/lit/T69-*.md, T66 addenda, a one-page summary for the Lead. All of it waits for the Lead's «go».

## 3. docs/GAPS.md rows I own
- None. `git show origin/claude/vibrant-johnson-nxvvxo:docs/GAPS.md | grep -n -i l-lit` -> lines 10 (G-N1-LB, owner «L-NEW (optional; not
  routed)», open), 11 (G-N5-TIME, owner cell «L-NEW (L-LIT T22; referees later)», open; T22 = the finished VJ00 Prop. 7.4 check) and 17 (G1,
  L-STRUCT, closed). L-LIT is cited as a source in all three and owns none.

## 4. Three owner rulings (verbatim), DECISIONS-INDEX status (trunk 471aba45)
1. D18 (index line 32: active; DECISIONS.md line 333):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
2. D1 (index line 5: active; DECISIONS.md lines 6-7):
   > Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
3. D21 (index line 46: active; DECISIONS.md lines 452-454; now on trunk, the predecessor could not quote it):
   > Okay, I want maximum effort. I want to use 200% usage in 3 days. There is fable 5.2 as well, use that too in dpeth everywhere where it seems fitting, use fable 5.2 at hard or xhigh. SO yes, 200% uage under 2 days.
   Follow-ups, verbatim: «act on it, I have a usage reset that is what. Iwill use» and «I also have a fable 5.2 usage reset as well on top».
   Direct confirmation in the Lead session, verbatim: «I confrim tge stuff».
   L51 (index line 47: active) is a Lead reading, not the owner's words: maximum effort to 2026-11-14 10:05Z; L-LIT is a literature role,
   not an attack lane.

## 5. Trap and check
- Trap that bit this lane, and bit again today: a stale local branch (4014 behind at T48; first push rejected at T54; today the fresh
  container was 5 commits behind origin/claude/l-lit, at T64, with no handover in its notes). Check, run before reading anything: the
  fetch above, `git merge --ff-only origin/claude/l-lit`, then `git branch --show-current` must print claude/l-lit and `git rev-parse HEAD
  origin/claude/l-lit` must print one SHA twice. Today: a19fff23 twice.
- Standing checks kept from the predecessors:
  - a paywalled or blocked source is reported NOT OPENED, never paraphrased from memory; the landscape doc is never a source by itself;
  - an unrefereed preprint's theorem is labelled a CLAIM (Zhong–Ye arXiv 2609.40147 v2);
  - subagents get the scope rule in their brief (public literature only, no GitHub calls outside this repository, no contact; T17 breach);
  - one push at a time: `pgrep -f "bash scripts/push.sh"` before every push, push.sh as a tracked background task with its output
    redirected to a file and `echo exit $?` after it (never a pipe, never a bare `&`), no commit while it runs (push.sh pushes the commit
    verified at its start; a push takes about 20 minutes here);
  - never `pkill -f` with a pattern that occurs in my own command line; SHAs only from git output; timestamps only from `date -u`.
