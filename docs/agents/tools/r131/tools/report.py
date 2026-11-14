#!/usr/bin/env python3
"""tools/report.py <fail>: writes REPORT.txt (to stdout): what was built, the check results, the dry-run numbers,
the open slots, every flag, and what to change in cfg.json for the second run."""
import json
import os
import re
import sys
import textwrap

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
from lib131 import DRAFT, OPEN_WORD, load_cfg, sha1, short, split_draft


def w(s, ind=""):
    return "\n".join(textwrap.wrap(s, 118, initial_indent=ind, subsequent_indent=ind + "  ", break_long_words=False, break_on_hyphens=False))


def main(fail):
    cfg = load_cfg()
    LN = cfg["line"]
    H = cfg["heads"]
    out = []
    P = out.append
    text = open(DRAFT, encoding="utf-8").read()
    d = split_draft(text, cfg)
    h = json.load(open(os.path.join(HERE, "out", "hashes.json")))
    steps = [l.split(" ", 3) for l in open(os.path.join(HERE, "out", "steps.txt"), encoding="utf-8").read().strip().split("\n")]
    fetch = open(os.path.join(HERE, "fetch.txt"), encoding="utf-8").read().split("\n")
    lt = open(os.path.join(HERE, "out", "post_landtest.out"), encoding="utf-8").read().split("\n")
    nopen = text.count(OPEN_WORD) - 1
    P("REPORT of the R131 build (docs/agents/tools/r131/build.sh). RESULT: %s." % ("BUILD PASS: every check passed" if fail == "0" else "BUILD FAILED: see CHECKS"))
    P("Sources read at the heads fetch.txt records (%s)." % fetch[0][5:])
    P("")
    P("1. WHAT WAS BUILT")
    P(w("docs/agents/R131-draft.md: sha1 %s, %d lines. Header l. 1-%d; entry block l. %d-%d (%d lines: title + %d bullet lines; sha1 %s); proposal "
        "paragraph l. %d-%d; UPDATE line l. %d (sha1 %s without its newline, unfilled; %d bytes); Addendum from l. %d."
        % (sha1(text.encode("utf-8")), text.count("\n"), d["b0"] - 1, d["b0"] + 1, d["b1"], len(d["block"]), len(d["block"]) - 1, h["block_sha1"],
           d["p0"] + 1, d["u0"], d["u0"] + 1, h["update_sha1"], h["update_bytes"], d["a0"] + 1), "  "))
    P(w("Title = '### %s [refereed-only] ' + line %s verbatim (%s at claude/l-red-b %s, sha1 %s, %d bytes) + ', CHECKER PASS (docs/checker/%s.md, "
        "checker <open-slot word>)'. %s"
        % (cfg["entry"], LN["name"], LN["path"], short(LN["commit"]), h["line_sha1"], LN["expect_bytes"], cfg["checker_number"],
           ("THE LINE IS A STAND-IN for the line of record %s." % LN["of_record_name"]) if LN["stand_in"] else "This is the line of record."), "  "))
    P(w("Tools (all under docs/agents/tools/r131/, untracked): cfg.json (every moving input), fetch.sh (the only network step; writes fetch.txt), "
        "lib131.py, datafacts.py, updlib.py, fill131.py (builds the draft; every quotation located by script), tools/lanecheck.sh, tools/upd.py, "
        "tools/data.py, tools/prem.py, tools/shape.py, tools/lp.py, tools/sweep.py, tools/landtest.py, tools/mkadd.py, tools/report.py, build.sh, "
        "land131.py, out/ (tool outputs, ledger.json, hashes.json, draft.p1.md). tmp/ is removed at the end of every build.", "  "))
    P(w("Nothing was added, committed, merged, pushed, rebased or stashed; scripts/push.sh and scripts/verify.sh were not run; RESULTS, GAPS, "
        "NOW were read, never written (land131.py was run as DRYRUN only, into tmp/).", "  "))
    P("")
    P("2. CHECKS (out/<name>.out; last line of each)")
    for s in steps:
        P("  %-14s rc %s  %s" % (s[0], s[2], s[3] if len(s) > 3 else ""))
    P("")
    P("3. DRYRUN (land131.py %s DRYRUN, on a COPY of the draft with the open-slot words replaced and hashes recomputed; fixed stamp)" % cfg["dryrun"]["checker"])
    for l in lt:
        if l.startswith("   T2 ") or l.startswith("T1 ") or l.startswith("T3 ") or l.startswith("T4 "):
            P(w(l.strip().replace(OPEN_WORD, "<open-slot word>"), "  "))
    P("")
    P("4. OPEN SLOTS (each carries the open-slot word in the draft; land131.py refuses while any remains): %d besides the checker token" % nopen)
    if LN["stand_in"]:
        P(w("- the line of record %s (stand-in %s): title, UPDATE, the bullet 'The RESULTS line'." % (LN["of_record_name"], LN["name"]), "  "))
    for k, t in (("entry9", "fixes entry 9 (Fixes bullet)"), ("stage5b", "REFEREE stage 5b: its section 14, the line word by word, fixes entries 7 to 9, the "
                 "final signature line naming the line by sha1 (Signatures bullet)"), ("r2_line", "REFEREE-2's line check; its signature names fixes "
                 "entries 1-5 only (Signatures bullet)")):
        if cfg["slots"][k]["open"]:
            P(w("- " + t + ".", "  "))
    P(w("- the checker token of the title (filled by land131.py <checker-sha>).", "  "))
    P("")
    P("5. FLAGS (the builder's reading; nothing in the line or in any quoted text was changed)")
    flags = [
        "G-LINE (blocking until the second run): the build stands on %s; the line of record %s and fixes entry 9 were not on origin at the fetch "
        "(claude/l-red-b %s)." % (LN["name"], LN["of_record_name"], short(H["l-red-b"])),
        "G-SLOTS (blocking): no referee has checked fixes entries 7 and 8 or any line after L-1. REFEREE's signature line names entries 1-6 (stage "
        "5a, %s), REFEREE-2's names 1-5 (Addendum 2); the line's closing parenthesis names entries 1-7. REFEREE-2's reading F-1 of clause (R3) is "
        "taken over by the lane in fixes 7.1, not yet confirmed by the statement's author (REFEREE)." % short(H["referee"]),
        "G-K12 (wording inside the line, for the lane / the Lead): the correctness clause says 'DATA for k ≤ 12: winners = Zielonka's' while part "
        "(3) of the same line has k = 13 (winners equal to Zielonka's, one engine) and REFEREE's stage-5a table says 'DATA for k ≤ 13'. The entry "
        "text says 'for k ≤ 12 on two engines and at k = 13 on one'.",
        "G-R245 (note): the line gives L-RED 70's engine n5s237 'for k = 3 … 8'; R245 at c7ed9b8b also carries k = 9 and k = 10 in two addenda "
        "(REFEREE's stage 5a notes that R245's own list says N5 beyond k = 8 is not established). An understatement, not an overclaim.",
        "G-STATUS (note): the line keeps 'CONDITIONAL until two referees sign' (Lead ruling of 16:46Z on 2026-11-13; the landed form of R130) and "
        "'(Theorem EXP-IDEAL, PROVED lane; …)'.",
        "G-5E (note): the coordinator's message names notes N-5a to N-5e; REFEREE's report at %s has four, N-5a to N-5d (its l. 765-771). The "
        "entry lists four." % short(H["referee"]),
        "G-N5a (note): fixes entry 2 (d) tags a REFEREE-2 quotation 'l. 248-249'; it is at l. 247-249 (REFEREE's N-5a). The draft quotes REFEREE-2's "
        "report directly, with script-computed lines.",
        "G-1E-N3 (substance, stated in the entry): everything about N5 is PROVED-CONDITIONAL on RESULTS R117 (and R124) as landed, under SPEC's "
        "standing premise 1E-N3, which is not proved in the fleet. Unconditional: Theorem EXP-IDEAL (a)-(c) and 'IDEAL-ACYC-POLY is false'.",
        "G-L43 (substance, stated in the entry): no measured run exceeds n² (largest N5 run: k = 13, 8,193 iterations, n² = 2,325,625; the model "
        "alone to k = 20); 2^k − 1 > n² first at k = 23 (n = 2,875), by arithmetic. The dead end rests on the proof.",
        "G-BOX108 (note): L-SI's box 108 has ONE referee's check (REFEREE-2's R2-box108.md; REFEREE compared, did not referee): supporting evidence, "
        "not a premise.",
        "G-U (the UPDATE's form; Lead / CHECKER to accept): built by the landed procedure (the same function rebuilds R128, R129, R130's landed "
        "UPDATEs byte for byte). Choices: (i) the three labels are moved behind their clauses, each clause ending where cfg.json 'clause_end' says; "
        "(ii) '; obstruction RIPPLE (' is KEPT (R130 turned its boundary '; obstruction W-FLAT (' into ': '; here part (3) follows, so nothing is "
        "replaced); (iii) only '; not M3 or M4, not a TARGET.md claim' is dropped; 'TARGET.md §2 (M4) stays OPEN' and the L41 scope tail stay; (iv) "
        "the ending is the ruled sentence. All four are cfg.json 'update' values.",
        "G-S (GAPS layout): the Closed table of docs/GAPS.md has an empty line inside it (l. 18, between G1 and G-FDL). land131.py appends the row "
        "after the LAST row of the section (G-DOM), as the file's last line. cfg.json gaps.closed_position = 'end_of_first_block' puts it after G1 "
        "(l. 17) instead.",
        "G-NOW: as briefed, land131.py changes only 'R17-R130' -> 'R17-R131' (one place, the M4 row). R130's landing (a41e21c0) changed TWO "
        "counters: 'R17-R129' -> 'R17-R130' and, on NOW l. 2, 'R31-R129' -> 'R31-R130'. To mirror it add [\"R31-R130\", \"R31-R131\", 1] to "
        "cfg.json now.replacements.",
        "G-TRUNK (note): the draft reads trunk files by git show at %s (origin's trunk head at the fetch). The local HEAD may be ahead (Lead "
        "commits; uncommitted edits of docs/DECISIONS*.md were present in the working tree during the build and were not touched). land131.py "
        "works on the working tree and checks anchors, not sha1s." % short(cfg["trunk"]["commit"]),
        "G-LEN (note): the entry block has %d lines (R130's had 199, R128's 240): the four verdict tables of the two referees are printed row by "
        "row by script. If the Lead wants it shorter, drop the table rows in fill131.py ('Claims signed')." % len(d["block"]),
        "G-LEAD-EDIT (i): the cost-model clause ('each iteration costs at least one step in TARGET.md §3's cost model') is in the TARGET.md diff "
        "bullet, with TARGET.md §3 and the packet's sentence quoted.",
        "G-ADJ (quotations adjusted): none was altered. Table cells of the referees are printed as the reports print them (no guillemets around a "
        "cell; guillemet groups inside a cell are entered as quotations of that report).",
    ]
    for f in flags:
        P(w("- " + f, "  "))
    P("")
    P("6. NOT VERIFIED BY THE BUILDER")
    for f in [
        "The mathematics: no proof step was re-derived; the entry reports the referees' verdicts.",
        "The lane's DATA was not regenerated: numbers are read from the pinned outputs (sha1 pins checked against the git objects); only the "
        "lane's fast check.sh was re-run in a git archive. No N5 engine, no Oink, no Lean, no scripts/verify.sh.",
        "The referees' own logs (docs/referee/scratch/, docs/referee-2/R2-P-N5-EXP/) were not opened; L-NEW's P-N5-KEY1P was not opened.",
        "REFEREE-2's R2-box108.md and L-SI's box 108 were read for their verdict and independence lines only.",
        "The CHECKER file docs/checker/%s.md does not exist yet; land131.py does not look the checker sha up." % cfg["checker_number"],
    ]:
        P(w("- " + f, "  "))
    P("")
    P("7. CFG CHANGES FOR THE SECOND RUN (then: bash fetch.sh; bash build.sh)")
    for f in [
        "heads: the new 40-hex heads of l-red-b, referee, referee-2 (copy them from fetch.txt after bash fetch.sh); trunk.commit if origin's "
        "trunk moved (build fails with a clear message if cfg and fetch.txt disagree).",
        "line: name \"L-4\", path \"docs/red-b/P-N5-EXP-line-L4.txt\" (or the lane's name), commit (the commit that added it), stand_in false, "
        "expect_sha1, expect_bytes; optionally line.history: a fill list (text / quote items) for the sentence on L-4 in 'The RESULTS line'.",
        "fixes: expected_entries 9, expect_sha1, expect_lines of the file at the new head; slots.entry9: open false and a fill list, e.g. "
        "[{\"text\": \"Entry 9 (L-RED-B 7): the line L-4,\"}, {\"src\": \"FIX\", \"quote\": \"<verbatim words of entry 9>\"}]. fill131.py "
        "asserts the append-only chain through entry8_commit and the head; add nothing else.",
        "referee.stages: append [\"stage 5b\", \"<40-hex commit>\"] (the build fails if git blame shows a commit that cfg does not list); "
        "slots.stage5b: open false and a fill list quoting its final signature line and its verdict on the line, e.g. {\"src\": \"REF1\", "
        "\"quote\": \"...\"}.",
        "referee2.stages: append its new addendum's commit; slots.r2_line: open false and a fill list quoting its line check.",
        "update.labels[1].clause_end is already written to match both L-3 and L-4; if the line's labels or scope words change, the build "
        "refuses and names the string that no longer occurs exactly once.",
        "If a quotation that fill131.py takes from a report no longer occurs exactly once (a report grew), the build stops with 'AMBIGUOUS' or "
        "'NOT FOUND' and the string: give it an occurrence number in fill131.py (third argument of q).",
        "After the second run: python3 docs/agents/tools/r131/land131.py <checker-sha> DRYRUN <dir> must run without REFUSED; then the same "
        "without DRYRUN lands (it writes four working-tree files and commits nothing).",
    ]:
        P(w("- " + f, "  "))
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
