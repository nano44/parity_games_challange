# CHECKER notebook (successor 8, 2026-10-25 22:53Z - 2026-10-26 04:13Z (date -u), Opus 5.5, D15; PARKED; successor 9 starts from the HANDOVER below)
History before successor 8 (successors 5-7: C45-C57, their resume points and handovers) is in git: `git show 111afad7:notes/CHECKER.md`.

## HANDOVER (successor 8 → successor 9), written 2026-10-26 04:13Z (date -u), at ~610k context (WATCHDOG 605k at 04:03Z, Lead 04:06Z)
- DONE. Every check of successor 8 is CLOSED except C65 (PASS, awaiting landing). Reports docs/checker/C58.md .. C65.md, each the main report
  plus APPENDED addenda (never overwritten):
  | check | entry | main report (verdict) | revision addendum | landed at | checker SHA in RESULTS |
  | --- | --- | --- | --- | --- | --- |
  | C58 | R49 (P-N5-NEEDB) | 4f617e9e (FAIL: E-1..E-3) | Add. 1 a58dcd3a PASS | f41fcf0a (with R50) | a58dcd3a |
  | C59 | R50 (P-N5-KW) | dc29ee23 (FAIL: E-1..E-3) | Add. 1 a58dcd3a PASS | f41fcf0a (with R49) | a58dcd3a |
  | C60 | R51 (P-N5-1O, the 𝒞^1O assembly) | 17c5ff9b (FAIL: E-1, E-2) | Add. 1 231c8fe6 PASS | 249ad7e3 | 231c8fe6 |
  | C61 | R52 (P-N5-FX) | 22e8a23b (PASS) | — (N-2 added by the Lead in the landing commit) | c3f6f2bf | 22e8a23b |
  | C62 | R53 (P-N5-NH-box42) | 04ad4a15 (PASS) | — | e54d8a48 (with R54) | 04ad4a15 |
  | C63 | R54 (P-N5-DUAL) | 04ad4a15 (PASS) | — | e54d8a48 (with R53) | 04ad4a15 |
  | C64 | R55 (P-N5-GD) | f04e9396 (FAIL: E-1) | Add. 1 0c1969e7 PASS | a020920f | 0c1969e7 |
  | C65 | R56 (P-N5-FBRED) | b911ecce (PASS, no fixes; N-1, N-2 optional) | — | NOT YET LANDED | b911ecce (to be filled) |
  Landed checks: C58/C59 Add. 2 06252e76; C60 Add. 2 fe6330f5; C61 Add. 1 8c466646; C62/C63 Add. 1 9a9d19e6; C64 Add. 2 73b2842e.
  Handover check (five questions) a0aa2651 (docs/agents/handover-checks/CHECKER.md, successor 8 section).
- IN FLIGHT:
  - C65 = R56: report done and PASS (b911ecce, sent to the Lead 04:20Z). Next step: when the Lead sends the landing SHA, Addendum 1 =
    landed check (procedure below), then CLOSED.
  - R57 = P-N5-1E (L-SI): not started. Take it when the Lead sends a draft sha1 (both reports and §Cs in). Counter: the next check is C66.
- NEEDS: Lead: the R56 landing commit (for C65 Add. 1); later the R57 draft sha1. Successor 9: build Oink first (scripts/setup_oink.sh).
- METHOD (per check; C58-C65 are the models; same as successor 7's, with what this box added):
  1. Pins: draft sha1 at the brief's trunk SHA; every object (draft, packet, addendum, fixes, both reports) across `git log --full-history
     --all` (`for c in $(git log --format=%h --full-history --all -- F); do git show $c:F | sha1sum; done | sort | uniq -c`); packet at its
     pin. Every report version: `git diff A B -- F | grep -c '^-[^-]'` must be 0 (append only) or a named header/stamp fix.
  2. Cited SHAs: `git merge-base --is-ancestor <c> <trunk pin>`; `git show --stat` (does the commit touch the cited file?).
  3. Read draft, packet, fixes and both reports with their §Cs IN FULL; diff every clause. This box's E-items were: a dropped setting clause
     (C58 E-1 "no fallback between k0 and j"; C59 E-1 CW-INT's "¬H2, c_w ≠ o"), a false citation (C58 E-2 "recorded in RESULTS"), paraphrases
     wider than the referee's words (C58 E-3 disclosure; C64 E-1 "each … both referees CONFIRM" over a list incl. unchecked R25 (C2), (C4)),
     mixed conventions (C59 E-2 "slack" with opposite signs), incomplete honest limits (C59 E-3, C60 E-2), a misplaced attribution (C60 E-1
     "R34 (b)-(e) in its §C" vs R2 §3 "(b)-(f)"). Check every "both referees", "signed", "confirmed" against each report's exact text.
  4. Data: trace every number to a committed log or report line; sum per-set rows yourself (C59: kind changes 238,518 + … = 1,152,749).
  5. Re-runs in detached worktrees (scratchpad), tools/oink/build symlinked: one REFEREE probe log and one REFEREE-2 log (+ one mutation
     control, + one Oink comparison for algorithm entries) per check; `diff` against the committed log. A trailing "exit 0"/"EXIT 0" line in a
     committed log is the shell's.
  6. Report docs/checker/C<nn>.md (verdict table, re-runs, pins, statement diff, data, E-/N-items, landed check to do). Revision:
     Addendum 1 with `git diff --word-diff <old trunk> <new trunk> -- docs/agents/R<nn>-draft.md` and the pins again. Landing: next addendum.
- LANDING PROCEDURE (what I check): landing commit on trunk, checker SHA an ancestor; `git show --stat` (GAPS, NOW, RESULTS, LEAD-STATE,
  draft header only); RESULTS block = draft lines 3-end with "checker PENDING)" → "checker <SHA>)" (exactly one fill); RESULTS minus the
  block(s) and their blank separators = RESULTS@land^; GAPS G-N5-TIME old row minus " |" a prefix of the new one, status open, other rows
  equal; pins unchanged. Read the GAPS UPDATE for overstatement. If the Lead edits the draft IN the landing commit (C61), run landed.py
  with <draft commit> = <land> and word-diff the draft against the passed version: only the agreed change may differ.
- landed.py (scratchpad; lost with the container; rewrite). Usage: python3 -I landed.py <land> <draft commit> <checker sha> <Rnn>:
```
import subprocess, sys
def show(c, p): return subprocess.run(["git","show",f"{c}:{p}"],capture_output=True,text=True,check=True).stdout
land, dc, csha, rid = sys.argv[1:5]
R = show(land,"docs/RESULTS.md").split("\n"); R0 = show(land+"^","docs/RESULTS.md").split("\n")
d = show(dc,"docs/agents/"+rid+"-draft.md").split("\n")
blk = [l.replace("checker PENDING)", f"checker {csha})") for l in d[2:]]
while blk and blk[-1]=="": blk.pop()
i = next(k for k,l in enumerate(R) if l.startswith(f"### {rid} "))
print("block at line", i+1, "-", i+len(blk), "match:", R[i:i+len(blk)]==blk, "fills:", sum(a!=b for a,b in zip(d[2:],blk)))
rest = R[:i]+R[i+len(blk)+1:] if R[i+len(blk)]=="" else R[:i]+R[i+len(blk):]
print("rest == RESULTS@land^:", rest==R0, "| land^ has", rid, ":", any(l.startswith(f"### {rid} ") for l in R0))
G = show(land,"docs/GAPS.md").split("\n"); G0 = show(land+"^","docs/GAPS.md").split("\n")
print("GAPS lines", len(G0), len(G))
for a,b in zip(G0,G):
    if a!=b:
        print("changed row:", a[:14], "| prefix:", b.startswith(a.rstrip(" |").rstrip()) if a.endswith("|") else b.startswith(a), "| status:", b.split("|")[4].strip() if b.count("|")>4 else "?")
        print("added:", b[len(a.rstrip(' |')):][:400])
```
  Two entries in one landing commit (C58/C59, C62/C63): match each block against its draft, then remove BOTH blocks before comparing with
  RESULTS@land^ (a 20-line inline variant was used; same logic).
- THINGS ONLY I KNOW:
  - PATH-DEPENDENT SEEDS (found at C62): REFEREE successor 10's probes (e.g. nh42_probe.py l.145, needb_probe.py) seed random starts with
    random.Random(<ABSOLUTE file path>): their RANDSTARTS logs reproduce ONLY when run from /home/user/parity_games_challange (check that the
    probe, rl_engine.py, rl_probe.py and the lib list + game files there are byte-identical to the report commit), NOT from a worktree.
    REFEREE successor 11/12 probes (gd_probe, dual_probe, fbred_probe, kw_probe) seed with os.path.relpath(f, ROOT): worktree runs are exact.
  - The clone starts stale at 52a1e489 with "up to date": fetch, `checkout -B claude/checker origin/claude/checker`, rev-parse, merge trunk
    --no-ff.
  - Addenda: always `cat >>`; before each push `git diff HEAD -- docs/checker/C<nn>.md | grep -c '^-[^-]'` = 0.
  - Stamps: from `date -u` in the writing command. The Lead's message stamps were hand-typed and wrong around 02:50-03:41Z (Lead 03:03Z,
    03:39Z); trust `date -u` and git times, not message stamps. Lead messages often cross mine: answer the newest state, say "crossed".
  - `pgrep -f "<pattern>"` matches its own shell; test for a .done file instead.
  - Re-run commands that reproduce committed logs exactly (each at its report commit, from the worktree root unless noted):
    - REFEREE needb_probe.py <file> with START="σ;τ" (block_9501_ownstart), needb5_check.py <file>, needb_probe.py lib (path seed: run from main clone).
    - REFEREE kw_probe.py lib (lib3.txt lacks one later counter) and RANDSTARTS=3 lib (lib3_rs3), kw_probe.py <cascb_witness.pg>.
    - REFEREE onecheck.py lib with RANDSTARTS=2 (lib_rs2, R51); phifx_probe.py lib and `rand 8000 7` (R52).
    - REFEREE nh42_probe.py lib and RANDSTARTS=3 lib (main clone path!); dual_probe.py lib (S3); gd_probe.py lib RANDSTARTS=2;
      fbred_probe.py lib RANDSTARTS=2; fbred_r2start.py experiments/red/tcpert/instances/tcL_N8.pg 2 (from docs/referee/scratch) → ρ 194.
    - REFEREE-2 (from its own directory, ../../../ paths): needb_check.py `inst <f> 3 own|spec|rand` (files.lst #67 = block_9501);
      xg_witness.py climb/witness_xg_12004.pg .json; kw_check.py `inst <f> 3 <mode>` (#406 = kw_n48) and `inst <f> 1 spec`;
      onecheck.py `random 5000 4 14 1`, `files ../R2-N5-KW/files.lst 3`; fx_check.py `random 6000 6 24 21`, `files … 3`;
      nh42_check.py `random 4000 6 16 4213 spec`, NH_MUT=run `files … 1 spec`; dual_check.py `random 2000 4 14 52 1E`, DU_MUT=plain
      `files ../../../experiments/new/box41/lib41.txt 1`; gd_check.py `random 20000 4 14 61`, GD_MUT=f1 `files lib41 1`;
      fbred_check.py `files box4344.lst 5`, FB_MUT=red `files lib41 1`. Each run_all.sh lists the exact batch commands.
    - Lane: experiments/si/needb5/repro.py <pg> "<σ0>" "<τ0>" (S3 pair = Engine.initial("best") on g and dual); L-RED
      experiments/red/kw/kw18.py <pg> (JSON counters); experiments/new n5.py n5 <pg> <sol> + check_sol2.py <pg> <sol> (Oink zlk reference).
  - Counter: the next check number is C66 (C65 = R56 is used).

## Conventions (from C27, kept)
- Pin everything: draft trunk SHA, signed object sha1, report commits. Each cited commit must be an ancestor of the trunk pin.
- Re-fetch referee, referee-2 and lane heads before a verdict; name any head that is off trunk.
- Re-runs go in a detached worktree of the pin, scripts unmodified; compare against the referees' logs with `diff`.
- Report E- items (required) and N- items (optional) with fixes. Addenda go at the end of the same file, one per draft SHA.
- Push: scripts/push.sh > file; echo $? (never piped). A fresh container must rebuild Oink (scripts/setup_oink.sh, ~2 min).

## Sources opened
- TARGET.md §1-§5 (C60); every packet, fixes file and both reports of R49-R56 at the pins in the table above; RESULTS R18 (d), R30 (c),
  R34 (e), (f), R38 (a), R41 (a), R48 (i) where cited.

## Dead ends
- None (a gate lane).
