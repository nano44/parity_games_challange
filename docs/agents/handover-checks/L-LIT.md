# Handover check: L-LIT (successor after T69-T70; design day, candidate RF; written 2026-11-14T14:40Z by date -u; LANE-RESTART step 3)
Every answer measured from the repository at the time of writing (commands given). Predecessor's check: git history (a7c286d2).
Read before writing: CLAUDE.md, docs/agents/LANE-RESTART.md (procedure), notes/L-LIT.md (HANDOVER of 2026-11-12 14:26Z and the older
resume points), the previous check, trunk's docs/NOW.md (head, roster), docs/DECISIONS-INDEX.md (tail), docs/DECISIONS.md (D1, D26-D28,
L60, L61), docs/GAPS.md (rows naming L-LIT). docs/lit/ (BARRIERS, T27, T37, T47, T66 Add. D) is read next, before the first report.

## 1. Branch, head, distance to trunk
- Trap check run first: `git fetch origin claude/l-lit`, `git status -sb` -> «claude/l-lit...origin/claude/l-lit» (0/0),
  `git rev-parse HEAD origin/claude/l-lit` -> 9ae31ec3dfb77c077908c37d369fb37ff1daabef twice (the predecessor's last push; the Lead's
  ls-remote value). The container was NOT stale today. `git rev-parse --is-shallow-repository` -> false.
- Before the merge: `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` -> 9 ahead, 1863 behind (trunk
  15171faa822983e7c6118bb3c4be25b47469a387); merge-base 6895fb3183c993f45ca222bd54e6728bb0730d40 (T64).
- Trunk merged as the Lead ordered (`git merge --no-ff origin/claude/vibrant-johnson-nxvvxo`, a normal merge, no conflicts): local
  head 7356b42e64b5168cb1d0aa0c26f28792a66020f0; now 10 ahead / 0 behind trunk (`git merge-base --is-ancestor` trunk HEAD -> yes);
  1864 ahead of origin/claude/l-lit until the first push. .github/workflows/verify.yml now equals trunk's (the stale 30-minute copy is
  gone: `git diff 9ae31ec3 HEAD --stat -- .github/workflows/verify.yml` -> 23 insertions, 1 deletion).
- `pgrep -af push.sh` -> nothing running.

## 2. Open work and next step
- Predecessor IN FLIGHT (notes/L-LIT.md l. 29): nothing half-written. Its open leads are «only on a Lead question» and none is asked.
- Today's brief (Lead, 14:36Z): candidate RF («ROOT-FIRST», L-SI 57), a memoryless selection rule inside one-sided Vöge–Jurdziński
  strategy improvement: switch-best exactly at the improvable vertices in the sink strongly connected components of the dependency
  digraph (v depends on u iff u lies on the play from σ(v) or from one of v's improving targets). The statement of RF I hold is the
  Lead's message; origin/claude/l-si (8c062914, box 108) has no RF file yet. Three items, opened sources only:
  1. PRIOR ART (first report within 60 minutes of 14:36Z): ordered / delayed switching, Fearnley's non-oblivious rule, Schewe's
     optimal rule and Friedmann's bounds for it, Luttenberger, Björklund–Vorobyov, symmetric strategy improvement, policy iteration on
     deterministic MDPs. Next step: open each primary (arXiv / DOI), one paragraph each: rule, what is proved, whether it covers RF.
  2. APPLICABLE LOWER BOUNDS: per published family, which simultaneous or ordered switches its counter needs and whether RF's
     sink-first delay cancels them. Next step: start from T37 (families classified), T47 (snare families), T66 (Friedmann's G_n tables).
  3. Draft barrier statement docs/lit/T-next-RF-barrier.md (T71): frameworks RF is outside / not outside; what a polynomial bound
     would have to beat; what is missing for a sign-off (I do not sign off today).

## 3. docs/GAPS.md rows I own
- None. `grep -n -i l-lit docs/GAPS.md` (merged tree = trunk 15171faa) -> lines 10 (G-N1-LB, owner «L-NEW (optional; not routed)»,
  open), 11 (G-N5-TIME, owner cell «L-NEW (L-LIT T22; referees later)», open) and 17 (G1, L-STRUCT, closed). L-LIT is cited in all
  three and owns none. (G-N5-TIME's object, N5, is dead by L61; the row's status is the Lead's to change.)

## 4. Three owner rulings (verbatim), DECISIONS-INDEX status (trunk 15171faa)
1. D1 (index line 5: active; DECISIONS.md lines 6-7):
   > Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
2. D27 (index line 62: active; DECISIONS.md line 583):
   > SO we have to look for a new algorithm no? Do we have any promising lead or can convert our learning into a new promising algorithm?
3. D28 (index line 63: active; DECISIONS.md line 586):
   > I reset everything, you have until 11PM to use a full 100% usage
   L61 (index line 64: active) is a Lead reading, not the owner's words: N5 is dead; today = land R131 + a design day; D1's standard
   unchanged. Gauntlet step 3 (TARGET.md §5) is this lane's: «A barrier statement: which known lower-bound frameworks it lies outside,
   and why. L-LIT signs off.» Today's brief: a draft only, no sign-off.

## 5. Trap and check
- Trap that bit this lane: a stale local branch (4014 behind at T48; first push rejected at T54; 5 behind on 2026-11-12). Check, run
  before reading anything: fetch, `git status -sb`, `git rev-parse HEAD origin/claude/l-lit` must print one SHA twice. Today: 9ae31ec3
  twice, not stale. Second trap named by the Lead: the branch's stale 30-minute verify workflow; fixed by the trunk merge before the
  first push (answer 1).
- Standing checks kept from the predecessors:
  - a paywalled or blocked source is reported NOT OPENED, never paraphrased from memory; the landscape doc is never a source by itself;
  - an unrefereed preprint's theorem is labelled a CLAIM;
  - subagents get the scope rule in their brief (public literature only, no GitHub calls outside this repository, no contact);
  - one push at a time: `pgrep -af push.sh` before every push, push.sh as a tracked background task with its output redirected to a
    file and `echo exit $?` after it (never a pipe), no commit while it runs, `git ls-remote origin claude/l-lit` compared with the
    pushed SHA after it;
  - commits by explicit path; no rebase, amend, force-push, pull request; SHAs only from git output; timestamps only from `date -u`.
