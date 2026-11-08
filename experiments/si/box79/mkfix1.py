#!/usr/bin/env python3
"""L-SI P-IDEAL-DBL fix round 1: write fixes entry 1 (docs/si/P-IDEAL-DBL-fixes.md) by script. The PATH-RISE quotes are copied from
the frozen packet (old) and from trunk docs/RESULTS.md at 97d17f63 (new; read from `git show 97d17f63:docs/RESULTS.md` into
argv[1]); the line map is mkL2.py's (MAP=1); the level sets from reentry_levels.out; the L-2 sha1 / bytes from the file."""
import sys, os, re, hashlib, subprocess
H = os.path.dirname(os.path.abspath(__file__)); os.chdir(H)
P = open("../../../docs/si/P-IDEAL-DBL.md", encoding="utf-8").read()
R = open(sys.argv[1], encoding="utf-8").read()
i = P.index("(PATH-RISE) «"); old = P[i:P.index("»", i) + 1]
j = P.index("]", i + len(old)); old_full = P[i:j + 1]          # with the bracket «[IDEAL-ACYC, any degree, any width]»
old_full = re.sub(r"\n\s*", " ", old_full)
k = R.index("(PATH-RISE) at any degree"); new = R[k:R.index(" (2026-11-06)", k)]
new = new[:new.index(" times in a run") + len(" times in a run")]
assert R.count(new) == 1 and new == "(PATH-RISE) at any degree, the current value cv(z) of every mover z rises at most P(z) − 1 times in a run"
L2 = open("../../../docs/si/P-IDEAL-DBL-line-L2.txt", "rb").read()
ro = open("reentry_levels.out", encoding="utf-8").read()
sets = re.findall(r"(\S+\.json) sha1 (\w+) d (\d+)\n(?:.*\n)*?  reading A failing l: \{([^}]*)\}\n(?:.*\n)*?  reading B failing l: \{([^}]*)\}", ro)
mp = subprocess.run([sys.executable, "-I", "-B", "mkL2.py"], env=dict(os.environ, MAP="1"), capture_output=True, text=True, check=True).stderr
out = []
w = out.append
w("# P-IDEAL-DBL fixes (the packet docs/si/P-IDEAL-DBL.md stays frozen at f5263d5a, sha1 3573e93b…; every repair is here)")
w("")
w("## Entry 1 (fix round 1; L-SI successor 42; Lead 09:20Z: REFEREE 26 d7885be4 DB-Q1, DB-2, DB-3, DB-L1, DB-L2; REFEREE-2 30 7891ba32")
w("W-1, W-2 (a)-(d), W-3, N-1..N-3; Lead rulings 1-5). Strings copied by script: experiments/si/box79/mkfix1.py (this file) and")
w("mkL2.py (line L-2); referee reports byte-copied as experiments/si/box79/ref_d7885be4.md, ref2_7891ba32.md (pinned).")
w("")
w("### F-1 (W-1 = DB-Q1; Lead ruling 1): the PATH-RISE premise in §0 is quoted from the landed R113 text")
w("- Old (packet §0): " + old_full)
w("- New: R113 (trunk docs/RESULTS.md at 97d17f63, «### R113 [refereed-only]», stated «on acyclic Ξ-graphs»): «" + new + "», with")
w("  R113's P(z) «the number of maximal Ξ-paths from z». Same content; TOWER-NEED (§4) and FUEL-NEED (§5) use exactly this. No proof changes.")
w("")
w("### F-2 (DB-2 + W-2 (d) + N-3; Lead ruling 3): DEAD-REENTRY, reading and levels")
w("- §6 DEAD-REENTRY is to be read as: «the strict Ξ-descendants of the fuel targets U_l lie at levels > l» (static Ξ-graph; U_l as in §0:")
w("  the Ξ-targets of upward options of movers of level ≤ l; strict Ξ-descendants of y: movers reachable from y along Ξ-targets of any")
w("  options, y excluded). The packet's «the movers on the chains of the fuel targets U_l» named no l and no reading (DB-2).")
w("- MEASURED by experiments/si/box79/reentry_levels.py → reentry_levels.out (every l in 0, …, d − 2; reading A = as worded, every y ∈ U_l;")
w("  reading B = only the y ∈ U_l of level > l):")
for name, sh, d, A, B in sets:
    w("  - %s (sha1 %s…, d %s): false for l ∈ {%s} (reading A), l ∈ {%s} (reading B); true for l = 0." % (name, sh[:8], d, A, B))
w("- The line uses reading A (DB-L2's wording) with these sets and REFEREE-2's witnesses 1 → 11 → 3 (REC_d10_tower_mu30: (1, 0) → 11 of")
w("  level 5, (11, 0) → 3 of level 1) and 2 → 5 → 3 (KILL_M2D_d6_mu13: (2, 1) of level 1 → 5 of level 2, (5, 0) → 3 of level 1); each")
w("  witnesses every l ≥ 1 of its set (the first mover has level ≤ 1 ≤ l, the last has level 1 ≤ l).")
w("- The measured sets differ from both referees' statements: REFEREE 26 «fails for l = 1, …, 4» (tower) / «l = 1» (KILL_M2D) and REFEREE-2")
w("  N-3 «killed at l = 1». Both named only the witness through 11 resp. 5, valid for l ≥ 1. For the tower, 11 of level 5 is in U_l for every l")
w("  (it is the target of a level-0 mover), so with reading A the witness 1 → 11 → 3 works up to l = d − 2 = 8. The «l ≤ 4» bound holds only if")
w("  one also asks lev(11) > l, and reading B then finds other witnesses for l = 5, …, 8 (reentry_levels.out). The DEAD verdicts stand.")
w("")
w("### F-3 (DB-3, taken; Lead ruling 4): DBL-EQ proof step (iv)")
w("- Add to (iv): at a doubling level, Φ(s_0) = 2 while Φ(s_(t−1)) = 0 at every l-b-step t (DBL-EQ (a)); so step 1 is not an l-b-step,")
w("  and the l-windows are [1, t_1 − 1], [t_1, t_2 − 1], …, [t_f, T] with t_1 < … < t_f the l-b-steps: exactly F(l − 1) + 1 windows.")
w("")
w("### F-4 (DB-L1 + W-3; Lead ruling 2): DATA clause of the line, and why PASS-FREEZE keeps its count")
w("- The line's DATA clause is DB-L1's New text. Every number in it is asserted equal to dblcheck.out / dblcheck_neg2.out by mkL2.py.")
w("  W-3's no-DATA entries that DB-L1 lacks are added in place of «MP-LIN no separate DATA;»: the sufficient condition of PASS-FREEZE and")
w("  DEAD-REENTRY (static; reentry_levels.py) have no separate DATA, and the other three DEAD instances are re-run by dead79.py.")
w("- PASS-FREEZE keeps DB-L1's count (23,317 (run, level) of CORPUS, none in LOWER): it counts the lemma's conclusion F(l + 1) = F(l) on runs")
w("  where the pair above never moves and starts split (counter PF). W-3 asks «no separate DATA» only for the SUFFICIENT CONDITION (both")
w("  options of a member with target X, …), which no counter tests; the line now says exactly that. W-3's own text also carries «23,317 / 0».")
w("")
w("### F-5 (N-1, N-2): line premises and wording")
w("- N-1 (and REFEREE 26's optional note): F0 is dropped from the line's premise list (only §5's FUEL (i), not in the line, uses it).")
w("- N-2: the line's U_l now reads «whose Ξ-target has a higher level than that mover» (packet §0 «Upward option»).")
w("")
w("### Line L-2 = L-1 with these replacements (mkL2.py; each old string once in L-1, each new once in L-2)")
for blk in mp.strip().split("\n"):
    w("  " + blk if blk.startswith("  ") else "- " + blk)
w("- docs/si/P-IDEAL-DBL-line-L2.txt: sha1 %s, %s B, 1 line, %d «(» = %d «)», 0 «|»." % (
    hashlib.sha1(L2).hexdigest(), "{:,}".format(len(L2)), L2.count(b"("), L2.count(b")")))
w("- Not changed: every statement of the packet (all SIGN at both referees); L-1 and the packet stay as frozen.")
sys.stdout.write("\n".join(out) + "\n")
