# Handover check: L-NEW (successor 13, Opus 5.5 per owner D15 / Lead reading L37; written 2026-10-25 01:53Z by date -u)
This file replaces the previous answers (successors 1-12 are in git history before this commit). Each answer was measured from
the repository when written (commands named), not recalled. Predecessor: successor 12, session_01SqmdU7H8WiFZUGTRjZi1C3,
parked after box 32 (notes/L-NEW.md resume point, d72e7086).

### 1. Branch, head, ahead/behind trunk
- Branch claude/l-new. The container was STALE again: local HEAD 5961101a (successor 6), "behind 896". `git fetch origin`
  moved origin/claude/l-new to d72e7086; `git merge --ff-only origin/claude/l-new` fast-forwarded local; `git rev-parse HEAD
  origin/claude/l-new` both d72e7086.
- Before merging: `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` = 2 ahead / 14 behind trunk
  e8c26f30 ("Lead: R27 draft (P-N5-LP + P-N5-SO) for C36; NOW"); merge-base bb32e467. The one lane commit not on trunk is
  d72e7086 (handover notebook).
- Merged trunk with a merge commit (d7705c00, `--no-ff`, no conflicts; no rebase): 3 ahead / 0 behind. After this file's
  commit: 4 ahead / 0 behind (until the Lead's next trunk commit).

### 2. Open work and the next step of each
Nothing of mine is running (successor 12 killed all climbs at park).
- **P-N5-OE** (docs/new/P-N5-OE-box32.md: Lemma U-loc, Lemma OE, Corollary OX), pinned at trunk 361d18c; `sha1sum` = adeccd89…,
  matches NOW; `git diff 361d18c HEAD` on it is empty. With REFEREE succ. 6 (R-N5-OE) and REFEREE-2 succ. 6 (R2-N5-OE), both
  WORKING 01:42Z per NOW. Next step: when the Lead relays their items, answer them in a NEW file
  docs/new/P-N5-OE-fixes-box32.md; never edit the packet. Known soft spot: OE uses the full-minimiser property of σ̄(o)
  (CAP-1); cite it as P-N5-SO-fixes §1 does. Priority over research.
- **Research after GO** (o-cyclic 𝒞^1O, per phase; after R25-R27, R27 = LP + SO in landing at C36): open quantities X
  (crossings, ≡ Z up to n by R23) and K (wakes in U2/U3/U23 stretches; seen only as U3, length-only W band, W-tie switches).
  Next steps: (a) bound K (start from Lemma KW-LEN, N5-L-box32 §5; (E) is what remains there); (b) the weaker target than (X):
  rises of the used level with a crossing in their interval + non-tame crossings (what X is charged for in Corollary OX).
  Tools in experiments/new/box32 (lcheck, socheck, oddlev, orise, wakeinfo, rrclimb, lemclimb). Every cited instance
  re-verified (n5.py, Oink --zlk, check_sol2.py) and checked to have exactly one Odd vertex of out-degree > 1.
- Not routed: OB_R, OB (CONJECTURES), G-N1-LB.

### 3. docs/GAPS.md rows I own (`git show origin/claude/vibrant-johnson-nxvvxo:docs/GAPS.md | grep -n L-NEW`)
- **G-N5-TIME** (l.11): major; owner "L-NEW (L-LIT T22; referees later)"; status **open**. Latest updates: R25 (23:44Z, Theorem
  FB), R26 (00:48Z, CASC-U2/U3 on 𝒞^1O given f, K_W, E); L-NEW box 32 (P-N5-LP pinned bc42f2c, Theorem LP / Corollary LP′),
  now R27 draft with P-N5-SO at CHECKER C36.
- **G-N1-LB** (l.10): minor; owner "L-NEW (optional; not routed)"; status **open**.
- **G-N5-TERM** (l.16): major; owner "L-NEW (L-COMP checks runs)"; status **closed** (RESULTS R15).

### 4. The three owner rulings that most constrain me (verbatim), with their index status
1. D18 (docs/DECISIONS.md l.333; DECISIONS-INDEX row D18 "active"; Lead reading L40 "active", L-NEW = designer):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
2. D1 (docs/DECISIONS.md l.6-7; DECISIONS-INDEX row D1 "active"):
   > Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   For me: a bound I believe is a READING / lane PROVED until two referees sign; L-RED attacks it.
3. D14 (docs/DECISIONS.md l.246; DECISIONS-INDEX row D14 "active"):
   > You know it can also test prveiously not tested approaches, it can come up with it own as well

### 5. One trap, and the check that prevents it
- **Trap**: the stale container. It bit again here: local claude/l-new at 5961101a, 896 commits behind origin (also successors
  6, 8, 10-12). Working from it would have hidden boxes 17-32 and the pinned P-N5-OE packet.
- **Check**: `git fetch origin`, `git merge --ff-only origin/claude/l-new`, `git rev-parse HEAD origin/claude/l-new` equal
  before any work; pinned packets checked by `sha1sum` against NOW and an empty `git diff <pin> HEAD`.
- **Also carried**: stamps only from date -u (container clock slow); push.sh output to a file, then `$?`; kill by pid, never
  pkill -f; reach_o omits o (count |R| with o); ReadNotifications after every push (Lead relays queue unseen).
