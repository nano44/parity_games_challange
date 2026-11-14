#!/usr/bin/env python3
"""tools/report.py <fail>: writes REPORT.txt (to stdout): what was built, the check results, the dry-run numbers,
the open slots, every flag, and what to change in cfg.json for the next run."""
import json
import os
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
    it = json.load(open(os.path.join(HERE, "out", "items.json"), encoding="utf-8"))
    steps = [l.split(" ", 3) for l in open(os.path.join(HERE, "out", "steps.txt"), encoding="utf-8").read().strip().split("\n")]
    fetch = open(os.path.join(HERE, "fetch.txt"), encoding="utf-8").read().split("\n")
    lt = open(os.path.join(HERE, "out", "post_landtest.out"), encoding="utf-8").read().split("\n")
    nopen = text.count(OPEN_WORD) - 1
    P("REPORT of the R131 build, %s fill (docs/agents/tools/r131/build.sh). RESULT: %s." % (
        cfg["fill"], "BUILD PASS: every check passed" if fail == "0" else "BUILD FAILED: see CHECKS"))
    P("Sources read at the heads fetch.txt records (%s): l-red-b %s, referee %s, referee-2 %s, trunk %s." % (
        fetch[0][5:], short(H["l-red-b"]), short(H["referee"]), short(H["referee-2"]), short(cfg["trunk"]["commit"])))
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
    P(w("Tools (docs/agents/tools/r131/): cfg.json (every moving input), fetch.sh (the only network step; writes fetch.txt), lib131.py, "
        "datafacts.py, updlib.py, fill131.py (builds the draft; every quotation located by script), tools/lanecheck.sh, tools/upd.py, tools/data.py, "
        "tools/prem.py, tools/items.py, tools/shape.py, tools/lp.py, tools/sweep.py, tools/landtest.py, tools/mkadd.py, tools/report.py, build.sh, "
        "land131.py, out/ (tool outputs, ledger.json, items.json, hashes.json, draft.p1.md). tmp/ is removed at the end of every build.", "  "))
    P(w("The builder added, committed, merged, pushed, rebased or stashed nothing; scripts/push.sh and scripts/verify.sh were not run; RESULTS, "
        "GAPS, NOW were read, never written (land131.py was run as DRYRUN only, into tmp/).", "  "))
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
    P("4. OPEN SLOTS (each carries the open-slot word in the draft; land131.py refuses while any remains): %d tokens besides the checker token" % nopen)
    if LN["stand_in"]:
        P(w("- the line of record %s (stand-in %s)." % (LN["of_record_name"], LN["name"]), "  "))
    for k, t in (("stage5b_ii", "REFEREE stage 5b (ii): its check of the lines L-4 to L-6 and of fixes entries 9-11, and its FINAL line naming the "
                  "line of record by sha1 (Signatures bullet; named in the header)"),
                 ("r2_add5", "REFEREE-2 Addendum 5: its check of the replacements after L-3 and of fixes entries 9-11, and its final line "
                  "(Signatures bullet; named in the header)")):
        if cfg["slots"][k]["open"]:
            P(w("- " + t + ".", "  "))
    P(w("- the checker token of the title (filled by land131.py <checker-sha>).", "  "))
    P("")
    P("5. FLAGS (the builder's reading; nothing in the line or in any quoted text was changed)")
    flags = [
        "G-SLOTS (blocking until the third run): no referee has checked the lines L-4 to L-6 or fixes entries 9-11. REFEREE's signature line "
        "names entries 1-6 (stage 5a) and its stage 5b (i) finds entries 7, 8 right and does NOT sign L-3; REFEREE-2's signature names entries 1-8 "
        "(Addendum 4) and does NOT sign L-3; the line's closing parenthesis names entries 1-11.",
        "G-ITEMS (the Note bullet): %d item rows of both referees and of the pre-check, each with the line that raised it and its closing text, "
        "located by script; tools/items.py scans the reports for item labels and finds none outside the table. WITHOUT a closing text in the fixes "
        "file or in a line replacement (flags, not guesses): %s. L-n2 (REFEREE: the scope tail may cite the author's acceptance of F-1; the Lead's "
        "call): L-6's tail does not cite it; the entry quotes the acceptance in the L41 bullet. N-6a, N-6b (REFEREE's notes on a loose phrase of "
        "fixes 7.6 and on the builder's own measure): no entry answers them, the referee asks for nothing. A2.1 is REFEREE-2's own correction."
        % (len(it["items"]), ", ".join(it["unmatched"])),
        "G-P4 (note): the pre-check's P-4 (L43: the kill needs the proof for every k) is matched BY CONTENT to REFEREE's L43 sentence, which does "
        "not name P-4; P-3 is matched to REFEREE's stage-2 sentence on fixes 9.13. Both are requirements on the kill, not requests to the lane.",
        "G-RELAY (provenance): fixes entries 10 and 11 quote the referees' items (F-L3-1; L3-2, L3-3, L3-5) from the Lead's relay, written before "
        "REFEREE's §14 and REFEREE-2's Addendum 4 were on origin, and say so. The draft cites the reports themselves. The wording L-5 took for the "
        "rank gloss is the one REFEREE's §14.3 says it would sign; REFEREE-2's proposed wording (Addendum 4, L3-1) differs in words, not in "
        "content. Whether each referee accepts L-6's words is the open slots.",
        "G-R245 (note): the line gives L-RED 70's engine n5s237 'for k = 3 … 8'; R245 at c7ed9b8b also carries k = 9 and k = 10 in two addenda. "
        "An understatement, not an overclaim; neither referee raised it.",
        "G-STATUS (note): the line keeps 'CONDITIONAL until two referees sign' and '(Theorem EXP-IDEAL, PROVED lane; …)' (Lead ruling; the landed "
        "form of R130); both referees call them status phrases the Lead replaces at landing (REFEREE §14.2 row 1; REFEREE-2 Addendum 4).",
        "G-1E-N3 (substance, stated in the entry): everything about N5 is PROVED-CONDITIONAL on RESULTS R117 (and R124) as landed, under SPEC's "
        "standing premise 1E-N3, which is not proved in the fleet. Unconditional: Theorem EXP-IDEAL (a)-(c) and 'IDEAL-ACYC-POLY is false'.",
        "G-L43 (substance, stated in the entry): no measured run exceeds n² (largest N5 run: k = 13, 8,193 iterations, n² = 2,325,625; the model "
        "alone to k = 20); 2^k − 1 > n² first at k = 23 (n = 2,875), by arithmetic. The dead end rests on the proof.",
        "G-BOX108 (note): L-SI's box 108 has ONE referee's check (REFEREE-2's R2-box108.md; REFEREE compared, did not referee): supporting evidence, "
        "not a premise.",
        "G-U (the UPDATE's form; Lead / CHECKER to accept): built by the landed procedure (the same function rebuilds R128, R129, R130's landed "
        "UPDATEs byte for byte). (i) The three labels are moved behind their clauses; (ii) '; obstruction RIPPLE (' is KEPT (R130 turned its "
        "boundary into ': '); (iii) only '; not M3 or M4, not a TARGET.md claim' is dropped; 'TARGET.md §2 (M4) stays OPEN' and the L41 scope tail "
        "stay; (iv) the ending is the ruled sentence. The UPDATE carries L-6's one pair of square brackets ([RULE]) and no pipe.",
        "G-S (GAPS layout, as ruled): the row goes to the END of the Closed table, after its last row (G-DOM), as the file's last line; that table "
        "has an empty line inside it (l. 18).",
        "G-NOW (as ruled): land131.py changes only 'R17-R130' -> 'R17-R131' (one place); the Lead rewrites NOW at landing.",
        "G-TRUNK (note): trunk files are read by git show at %s; RESULTS and GAPS there are byte-equal to aeb90ac1's (sha1 printed in the draft's "
        "header). land131.py works on the working tree and checks anchors, not sha1s." % short(cfg["trunk"]["commit"]),
        "G-PINS (note): claude/l-si, claude/l-comp and claude/l-red have moved since the line was written; the draft reads box 108, BOX 48 and R245 "
        "at the commits the line and the reports name (cfg.json 'pins'), each checked to be an ancestor of the fetched head.",
        "G-LEN (note): the entry block has %d lines: six verdict tables of the two referees are printed row by row and the Note lists %d items. "
        "To shorten it, drop table rows in fill131.py ('Claims signed')." % (len(d["block"]), len(it["items"])),
        "G-ADJ (quotations adjusted): none. Table cells of the referees are printed as the reports print them (no guillemets around a cell; "
        "guillemet groups inside a cell are entered as quotations of that report).",
        "CLOSED since the first build: G-LINE (L-6 is the line of record), G-K12 (L-6 says 'DATA for k ≤ 13, k = 13 on one engine'), G-5E (N-5e "
        "and F-L3-1 are named in REFEREE's §14), G-N5a (read in fixes 9.2).",
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
        "The Lead's relays quoted in fixes entries 8-11 are messages, not files: not checked.",
        "The CHECKER file docs/checker/%s.md does not exist yet; land131.py does not look the checker sha up." % cfg["checker_number"],
    ]:
        P(w("- " + f, "  "))
    P("")
    P("7. CFG CHANGES FOR THE THIRD RUN (cfg.json only; then: bash fetch.sh; bash build.sh)")
    for f in [
        "fill: \"third\".",
        "heads.referee and heads.referee-2: the new 40-hex heads (copy from fetch.txt after bash fetch.sh); heads.l-red-b and trunk.commit only if "
        "they moved (the build stops with a clear message when cfg and fetch.txt disagree).",
        "referee.stages: append [\"stage 5b (ii)\", \"<40-hex commit>\"]; referee2.stages: append [\"Addendum 5\", \"<40-hex commit>\"] (the build "
        "stops if git blame shows a commit that cfg does not list). Leave referee.described_* and referee2.described_* as they are: they pin the "
        "text this build quotes from, and the reports must still begin with it.",
        "slots.stage5b_ii: \"open\": false and \"fill\": a list, e.g. [{\"text\": \"REFEREE stage 5b (ii) (successor 37):\"}, {\"src\": \"REF1\", "
        "\"quote\": \"<its verdict on L-4 to L-6 and entries 9-11, verbatim>\"}, {\"text\": \"its final line:\"}, {\"src\": \"REF1\", \"quote\": "
        "\"<the final line naming L-6 by sha1, verbatim>\"}]. Each quote must occur exactly once in the whole report (else add \"occ\": n).",
        "slots.r2_add5: the same with \"src\": \"REF2\".",
        "Nothing else. If the lane adds a fixes entry 12: fixes.expected_entries 12, append its stage to fixes.stages, give fixes.extra_fill (text / "
        "quote items); if the line changes again: line.* and line.history (text / quote items for the new round).",
        "Then: python3 docs/agents/tools/r131/land131.py <checker-sha> DRYRUN <dir> must run without REFUSED; the same without DRYRUN lands (it "
        "writes four working-tree files and commits nothing).",
    ]:
        P(w("- " + f, "  "))
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
