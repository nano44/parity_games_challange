# Handover check: L-NEW (successor 12, Opus 5.5 per owner D15 / Lead reading L37; written 2026-10-24 23:37Z by date -u)
This file replaces the previous answers. Successors 1-11's answers are in git history before this commit. Each answer was
measured from the repository when written (commands named), not recalled. Predecessor: successor 11,
session_01JjUBLJnxF38h9cjDCyZeZf, parked after box 31 (notes/L-NEW.md resume point 23:21Z, 0d7f7057).

### 1. Branch, head, ahead/behind trunk
- Branch claude/l-new. The container was STALE again: local HEAD was 5961101a (successor 6), "behind by 759". `git fetch origin`
  moved origin/claude/l-new to 0d7f7057; `git merge --ff-only origin/claude/l-new` fast-forwarded local to it.
- `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` gave 0 ahead / 15 behind trunk 76663365
  ("Lead: ... P-N5-U23 pinned; l-new 0d7f705 and l-red 0243539 merged"); merge-base = 0d7f7057 (trunk already holds my head).
- Merged trunk with a merge commit (4ceef47b, `--no-ff`, no conflicts; no rebase). After it: 1 ahead / 0 behind. After this
  file's commit: 2 ahead / 0 behind (until the Lead's next trunk commit).

### 2. Open work and the next step of each
Nothing of mine is running except scripts/setup_oink.sh (started 23:36Z; tools/oink/build was absent; needed for --zlk and
check_sol2.py re-verification).
- **P-N5-U23** (docs/new/P-N5-U23-box31.md: CASC-U2, CASC-U3 and corollaries), pinned at trunk 76663365; `sha1sum` = ee3e5d1e…,
  matches NOW (REFEREE succ. 5 R-N5-U23 and REFEREE-2 succ. 5 R2-N5-U23, both WORKING 23:30Z); `git diff 7666336 HEAD` on it is
  empty. Next step: when the Lead relays their items, answer them in a NEW file docs/new/P-N5-U23-fixes-box31.md; never edit the
  packet. This has priority over research.
- **Research after GO**: the open cores of (NH') on 𝒞^1O named in docs/new/N5-U23-box31.md:
  (E) = events in U3 (kind crossings, c_w's own DFS switches), (K_W) = W-changes on R outside route form.
  First step (successor 11's READING, §5): all 78/78 residual transitions are TAME (L-SI), and on tame blocks COARSE_M(Ξ) is constant
  with M non-increasing (RESULTS R25 in landing: TAME, MONO; CHECKER C34 addendum on the R25 draft). So try a coarse freeze at the
  gate level M instead of at c_w: re-run experiments/new/box31/tamecheck.py and u23check.py on the climb bests, check that (E) and
  (K_W) events are exactly the M-drops or are bounded by |R| per M-value, then try the layer induction (CASC) with M as the frozen
  frame. Then NFB-O, (X) as the Lead routes. Re-verify every cited instance with experiments/new/n5.py, Oink --zlk, check_sol2.py;
  every 𝒞^1O instance checked to have exactly one Odd vertex of out-degree > 1.
- Others (from notes / NOW): L-COMP box 7 tabulates (E) at small n; L-SI R25 (Theorem FB) at CHECKER; L-RED (X), box 34 done
  (J 10 at n 24).
- Not routed: OB_R, OB, NFB-O (CONJECTURES), G-N1-LB.

### 3. docs/GAPS.md rows I own (`grep -n "L-NEW" docs/GAPS.md` at 4ceef47b)
- **G-N5-TIME** (l.11): major; owner "L-NEW (L-LIT T22; referees later)"; status **open**. Last update 22:28Z: R24 landed
  (Theorem U1, O((f+1)|R|³) per U1 piece given f fallbacks); L-SI fallbacks ≤ n_E(2n−1)(J+1)+J, open core (J-poly); open per
  phase: Z (X), U2/U3 (my P-N5-U23 in review), NFB-O.
- **G-N1-LB** (l.10): minor; owner "L-NEW (optional; not routed)"; status **open**.
- **G-N5-TERM** (l.16): major; owner "L-NEW (L-COMP checks runs)"; status **closed** (RESULTS R15).

### 4. The three owner rulings that most constrain me (verbatim), with their index status
1. D18 (docs/DECISIONS.md l.333; DECISIONS-INDEX row D18 "active"; Lead reading L40 "active", L-NEW = designer):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
2. D1 (docs/DECISIONS.md l.6-7, full text docs/decisions/D001-launch-brief.md; DECISIONS-INDEX row D1 "active"):
   > Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   For me: a bound I believe is a READING until refereed; L-RED attacks it.
3. D14 (docs/DECISIONS.md l.245-246; DECISIONS-INDEX row D14 "active"):
   > D
   > You know it can also test prveiously not tested approaches, it can come up with it own as well

### 5. One trap, and the check that prevents it
- **Trap**: the stale container. It bit again here: local claude/l-new at 5961101a, 759 commits behind origin (also successors
  6, 8, 10, 11). Working from it would have hidden boxes 17-31 and the pinned packet.
- **Check**: `git fetch origin`, then `git merge --ff-only origin/claude/l-new` and `git rev-parse HEAD origin/claude/l-new` equal
  before any work; pinned packets checked by `sha1sum` against NOW and an empty `git diff <pin> HEAD`.
- **Also carried**: freeze / per-vertex bounds stated with their exact quantity (a route path has ≤ |R| edges; reach_o returns R
  minus o); push.sh output to a file, then `$?`; stamps only from date -u (successor 11's first stamp was 3 min ahead); kill by
  pid, never pkill -f.
