# Handover check: L-NEW (successor 14, Opus 5.5 per owner D15 / Lead reading L37; written 2026-10-25 04:43Z by date -u)
This file replaces the previous answers (successors 1-13 are in git history before this commit). Each answer was measured from
the repository when written (commands named), not recalled. Predecessor: successor 13, session_01525mp4dnZd1PA2Uj25tPVY,
parked after box 33 (notes/L-NEW.md resume point, 938e9eff).

### 1. Branch, head, ahead/behind trunk
- Branch claude/l-new. The container was STALE again: local HEAD 5961101a (successor 6), "behind 1107". `git fetch origin`
  moved origin/claude/l-new 5961101a..938e9eff; `git merge --ff-only origin/claude/l-new` fast-forwarded local;
  `git rev-parse HEAD origin/claude/l-new` both 938e9eff.
- Before merging: `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` = 0 ahead / 6 behind trunk
  a9fc3c97 ("Lead: SN fixes final + L-COMP park merged; R30 draft for C39; NOW"); merge-base 938e9eff (trunk already merged the
  handover notebook as da41ce79).
- Merged trunk with a merge commit (91aaba56, `--no-ff`, no conflicts; no rebase): 1 ahead / 0 behind. After this file's
  commit: 2 ahead / 0 behind (until the Lead's next trunk commit).

### 2. Open work and the next step of each
Nothing of mine is running (successor 13 killed all box-33 climbs at 03:36Z). Oink is not yet built in this container
(tools/oink/build is gitignored): first research step after GO is `scripts/setup_oink.sh`.
- **P-N5-SN** (docs/new/P-N5-SN-box33.md, pinned trunk 2c70ef6): `sha1sum` = 340d4f29…, `git diff 2c70ef6 HEAD` on it empty.
  Fixes file docs/new/P-N5-SN-fixes-box33.md final at §10, `sha1sum` = f242b011…, FROZEN (cited by R30). R30 is in landing
  (CHECKER succ. 4 C39 WORKING 04:38Z per NOW). Next step: none unless the CHECKER/Lead relays an item; any answer goes in a NEW
  file, never into the packet or the frozen fixes file.
- **Research after GO** (o-cyclic 𝒞^1O, per phase; open quantities X_SN, REL, K):
  (a) REL = exit releases at S4a steps. All seen: at w-changing transitions (13) or in scope-run prefixes before the first fallback
  (31). LEAVE says each needs an F-ward relevant change of level ≥ r = lev(θ, w). Next: test for an (A)-type freeze at a scope
  run's start (no release once the first fallback has happened and w is fixed), then try to prove it; count REL per w-epoch.
  (b) X_SN = S4a crossings in the c_w = c_θ prefix of fallback-free runs: bound via R-STICK / SN-PREFIX (inside SN under H1 the
  frames differ only R vs F).
  (c) Residue of ABS-COUNT′: ε-transitions with O_k = −1 (needs E_k = ⊥) and at fallbacks: never seen; climb for them.
  (d) Adversarial side: try to grow REL or X_SN superpolynomially from the K-chain family (kchain.py; K = Θ(n) wakes in one phase).
  Tools in experiments/new/box33 (wakes, xclass, xjoin, sn, scopecov, orxclimb MODE=rel, reabsclimb, kchain, biglev). Every cited
  instance re-verified (n5.py, Oink, check_sol2.py) and checked to have exactly one Odd vertex of out-degree > 1.
- Not routed: OB_R, OB (CONJECTURES), G-N1-LB.

### 3. docs/GAPS.md rows I own (`git show origin/claude/vibrant-johnson-nxvvxo:docs/GAPS.md | grep -n L-NEW`)
- **G-N5-TIME** (l.11): major; owner "L-NEW (L-LIT T22; referees later)"; status **open**. Latest update: R29 landed 03:43Z
  (P-N5-CLS); "In review: P-N5-SN (L-NEW: R-STICK, SN-PREFIX, LEAVE, ABS-COUNT). EXIT-R (ε form) FALSE (L-RED exitr_cex_n48).
  K = Θ(n) per phase possible (L-NEW K-chain, DATA)."
- **G-N1-LB** (l.10): minor; owner "L-NEW (optional; not routed)"; status **open**.
- **G-N5-TERM** (l.16): major; owner "L-NEW (L-COMP checks runs)"; status **closed** (RESULTS R15).

### 4. The three owner rulings that most constrain me (verbatim), with their index status
1. D18 (docs/DECISIONS.md l.333; DECISIONS-INDEX row D18 "active"; Lead reading L40, L-NEW = designer):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
2. D1 (docs/DECISIONS.md l.6-7; DECISIONS-INDEX row D1 "active"):
   > Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   For me: a bound I believe is lane PROVED / READING until two referees sign; L-RED attacks it.
3. D14 (docs/DECISIONS.md l.246; DECISIONS-INDEX row D14 "active"):
   > You know it can also test prveiously not tested approaches, it can come up with it own as well

### 5. One trap, and the check that prevents it
- **Trap**: the stale container. It bit again here: local claude/l-new at 5961101a, 1107 commits behind origin (also successors
  6, 8, 10-13). Working from it would have hidden boxes 17-33, the pinned P-N5-SN packet and its frozen fixes file.
- **Check**: `git fetch origin`, `git merge --ff-only origin/claude/l-new`, `git rev-parse HEAD origin/claude/l-new` equal
  before any work; pinned packets checked by `sha1sum` against NOW / the notebook and an empty `git diff <pin> HEAD`.
- **Also carried**: a fixes file cited by a landed or in-landing RESULTS entry is frozen (new material in a new file); stamps only
  from date -u; push.sh output to a file, then `$?`; kill by pid, never pkill -f; count K by transitions, not switches;
  c1o_list.py globs experiments/** (filter climb out/ dirs); ReadNotifications after every push.
