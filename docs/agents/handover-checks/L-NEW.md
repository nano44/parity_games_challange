# Handover check: L-NEW (successor 11, Opus 5.5 per owner D15 / Lead reading L37; written 2026-10-24 19:53Z by date -u)
This file replaces the previous answers. Successors 1-10's answers are in git history before this commit. Each answer was
measured from the repository when written (commands named), not recalled. Predecessor: successor 10,
session_0168YKVAbrcRjhbJ6XKi3JyU, parked after box 30 (notes/L-NEW.md resume point 19:44Z, c1decb3e).

### 1. Branch, head, ahead/behind trunk
- Branch claude/l-new. The container was STALE again: local HEAD was 5961101a (successor 6). `git fetch origin claude/l-new
  claude/vibrant-johnson-nxvvxo` moved origin/claude/l-new to c1decb3e; fast-forwarded local to it.
- `git rev-list --left-right --count origin/claude/l-new...origin/claude/vibrant-johnson-nxvvxo` gave 2 ahead / 6 behind trunk
  5cf18d59 (merge-base 4d3b60d1; the 2 are ef814646, c1decb3e; `git merge-base --is-ancestor c1decb3e origin/claude/l-new` holds).
- Merged trunk with a merge commit (18115366, no conflicts; no rebase). After it: 3 ahead / 0 behind. After this file's commit:
  4 ahead / 0 behind (until the Lead's next trunk commit).

### 2. Open work and the next step of each
Nothing of mine is running. tools/oink/build was absent; scripts/setup_oink.sh started 19:53Z (needed for zlk / check_sol2.py).
- **P-N5-NH** (docs/new/P-N5-NH-box30.md, pinned at trunk c7981ee5; `sha1sum` = 382c5143…, `git diff c7981ee5 HEAD` on it empty).
  Both referees are reviewing it (trunk 5cf18d59 "Lead: P-N5-NH to both referees"). Next step: when the Lead relays their gaps,
  write the repairs in a NEW file docs/new/P-N5-NH-fixes-box30.md; never edit the packet. This has priority.
- **Box 31** (after GO). (a) Proof side of U1 kind (T) (W-tie V_mid cascades after the κ_w-freeze, docs/new/N5-U1-box30.md):
  prove CONJECTURE U1-T (≤ 2 changes per vertex per W-length value) or a polynomial substitute, or locate exactly why W-tight
  cascades can be long. First step: re-run wf0_cex_n16 and the u1climb seeds under experiments/new/box29/u1vertex.py, and model the
  tie-break (first max in Engine.evaluate DFS/BFS order) as a lexicographic perturbation of the weights, so that a kind-(T) change
  becomes a strict improvement in a perturbed one-player game; then look for a potential on the W-tight DAG.
  (b) Then U2 (honest frame not in route form), U3 (W frame not in route form), W-CYC. (c) Re-verify every cited instance with
  experiments/new/n5.py, Oink --zlk and check_sol2.py.
- Others (relayed): L-SI successor 2 reduces X to Z (evicting fallbacks); L-RED attacks (X) and U1 kind (T); L-COMP tabulates X, O.
- Not routed: OB_R, OB, NFB-O (CONJECTURES), G-N1-LB.

### 3. docs/GAPS.md rows I own (`grep -n "L-NEW" docs/GAPS.md` at 18115366)
- **G-N5-TIME** (l.11): major; owner "L-NEW (L-LIT T22; referees later)"; status **open**. Landed pieces include R18 (o-acyclic
  𝒞^1O, conditional) and R21 (in-phase O(n⁴(1 + X + O)) on one-Odd-choice games); open: X, O (via (NH')), ≥ 2 Odd choice vertices.
- **G-N1-LB** (l.10): minor; owner "L-NEW (optional; not routed)"; status **open**.
- **G-N5-TERM** (l.16): major; owner "L-NEW (L-COMP checks runs)"; status **closed** (RESULTS R15).

### 4. The three owner rulings that most constrain me (verbatim), with their index status
1. D18 (docs/DECISIONS.md l.332; DECISIONS-INDEX row D18 "active"; Lead reading L40 "active", L-NEW = designer):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
2. D1 (docs/DECISIONS.md l.3-10, full text docs/decisions/D001-launch-brief.md; DECISIONS-INDEX row D1 "active"):
   > Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   For me: a bound I believe is a READING until refereed; L-RED attacks it.
3. D14 (docs/DECISIONS.md l.244; DECISIONS-INDEX row D14 "active"):
   > D
   > You know it can also test prveiously not tested approaches, it can come up with it own as well

### 5. One trap, and the check that prevents it
- **Trap** (box 29, successor 10 notebook, "Pitfalls"): "freeze" indices were checked against the wrong bound, an off-by-one;
  the notebook's fix: "a route path has ≤ |R| edges".
- **Check**: every freeze / per-vertex bound is stated with its exact quantity (edges vs vertices) and run against the pinned data
  (u1vertex / ivsplit tables) at the bound itself before it goes in a file.
- **Also carried**: stale container (caught again here, 5961101a vs c1decb3e; check = fetch then is-ancestor before any work);
  pinned packets checked with an empty `git diff <pin> HEAD`; push.sh output to a file, then `$?`; stamps only from date -u;
  kill by pid, never pkill -f.
