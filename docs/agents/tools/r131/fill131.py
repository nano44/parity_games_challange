#!/usr/bin/env python3
"""fill131.py: builds the pass-1 draft of RESULTS R131 (header, entry block, proposed GAPS UPDATE) from the sources
at the commits cfg.json names. Writes out/draft.p1.md, out/ledger.json (every quotation with its source, commit and
line numbers), out/hashes.json. Every guillemet quotation of the draft is produced by Fill.q / qn / raw, i.e. located
by script in a named source; a string that is not found, or found more than once without an explicit occurrence,
stops the build. Lead text (everything else) uses "..." only.
"""
import json
import os
import re
import sys

import datafacts
import updlib
from lib131 import (HERE, OPEN_WORD, OUT, Source, blame_ranges, block_sha1, cdate, csubject, gspans, line_sha1, load_cfg,
                    loc, norm, num, sha1, short, show, sources, wrap)

ERR = []


class Fill:
    def __init__(self, S):
        self.S, self.ledger, self.part = S, [], "header"

    def _find(self, key, text, occ):
        try:
            gspans(text)
        except ValueError as e:
            ERR.append("guillemets do not balance in a quotation of %s: %s" % (key, e))
        o = self.S[key].find(text)
        if not o:
            ERR.append("NOT FOUND in %s (%s @ %s): %r" % (key, self.S[key].path, short(self.S[key].commit), text[:110]))
            return (0, 0), 0
        if len(o) > 1 and occ is None:
            ERR.append("AMBIGUOUS in %s (%d occurrences, lines %s): %r" % (key, len(o), [a for a, _ in o][:6], text[:90]))
        if (occ or 1) > len(o):
            ERR.append("occurrence %d asked, %d found in %s: %r" % (occ, len(o), key, text[:90]))
            return o[0], len(o)
        return o[(occ or 1) - 1], len(o)

    def _add(self, form, key, text, fl, n):
        s = self.S[key]
        self.ledger.append({"form": form, "key": key, "commit": s.commit, "path": s.path, "text": norm(text),
                            "first": fl[0], "last": fl[1], "occurrences": n, "part": self.part})

    def q(self, key, text, occ=None):
        """a quotation followed by its line numbers."""
        fl, n = self._find(key, text, occ)
        self._add("q", key, text, fl, n)
        return "«%s» (%s)" % (norm(text), loc(*fl))

    def qn(self, key, text, occ=None):
        """a quotation without line numbers (they are given nearby, or the words recur in the source)."""
        fl, n = self._find(key, text, occ or 1)
        self._add("qn", key, text, fl, n)
        return "«%s»" % norm(text)

    def l(self, key, text, occ=None):
        """the line numbers of a passage, located by script; nothing is quoted."""
        fl, n = self._find(key, text, occ)
        self._add("l", key, text, fl, n)
        return loc(*fl)

    def raw(self, key, text, occ=None):
        """source text printed as the source prints it (a table cell): located as a whole, and every guillemet
        group inside it entered as a quotation of that source."""
        fl, n = self._find(key, text, occ or 1)
        self._add("l", key, text, fl, n)
        for _, _, inner in gspans(text):
            f2, n2 = self._find(key, inner, 1)
            self._add("qn", key, inner, f2, n2)
        return norm(text), fl


def table_rows(src, header_cells):
    """the rows of the markdown table whose header row has these cells: [(line_no, [cells])]."""
    hdr = "| " + " | ".join(header_cells) + " |"
    idx = [i for i, l in enumerate(src.lines) if norm(l) == hdr]
    if len(idx) != 1:
        ERR.append("table header %r found %d times in %s" % (hdr[:60], len(idx), src.key))
        return []
    out, i = [], idx[0] + 2
    while i < len(src.lines) and src.lines[i].lstrip().startswith("|"):
        cells = [c.strip() for c in src.lines[i].strip().strip("|").split("|")]
        out.append((i + 1, cells))
        i += 1
    return out


def main():
    cfg = load_cfg()
    S = sources(cfg)
    S["CHK"] = Source("CHK", cfg["heads"]["l-red-b"], "experiments/red-b/check.sh", "the lane's check.sh")
    F = Fill(S)
    q, qn, l, raw = F.q, F.qn, F.l, F.raw
    H = cfg["heads"]
    T = cfg["trunk"]["commit"]
    E, PREV, CN, PK = cfg["entry"], cfg["prev_entry"], cfg["checker_number"], cfg["packet_name"]
    FZ = cfg["packet"]["freeze_commit"]
    LB = H["l-red-b"]

    # ---------------------------------------------------------------- measurements (asserted, never typed)
    def must(c, msg):
        if not c:
            ERR.append("ASSERT: " + msg)

    pkt = S["PKT"]
    must(pkt.sha1 == cfg["packet"]["expect_sha1"] and len(pkt.lines) == cfg["packet"]["expect_lines"], "packet sha1 / lines differ from cfg")
    must(show(LB, cfg["packet"]["path"]) == pkt.raw, "the packet at the l-red-b head differs from the freeze commit")
    must(blame_ranges(LB, cfg["packet"]["path"]) == [(short(FZ), 1, len(pkt.lines))], "the packet has more than its freeze commit")
    fix = S["FIX"]
    must(fix.sha1 == cfg["fixes"]["expect_sha1"] and len(fix.lines) == cfg["fixes"]["expect_lines"], "fixes file sha1 / lines differ from cfg")
    ents = [(int(m.group(1)), i + 1) for i, x in enumerate(fix.lines) for m in [re.match(r"## Entry (\d+) ", x)] if m]
    nent = cfg["fixes"]["expected_entries"]
    must([e for e, _ in ents] == list(range(1, nent + 1)), "fixes entries by heading are %s, cfg expects 1..%d" % ([e for e, _ in ents], nent))
    fbl = blame_ranges(LB, cfg["fixes"]["path"])
    must(nent == 8 or not cfg["slots"]["entry9"]["open"], "the fixes file has %d entries: close slots.entry9 with a fill list for the entries after 8" % nent)
    f25 = show(cfg["fixes"]["entries2_5_commit"], cfg["fixes"]["path"])
    must(sha1(f25) == cfg["fixes"]["entries2_5_expect_sha1"] and f25.count(b"\n") == cfg["fixes"]["entries2_5_expect_lines"], "fixes file at the entries 2-5 commit")
    chain = [cfg["fixes"]["entry1_commit"], cfg["fixes"]["entries2_5_commit"], cfg["fixes"]["entry6_commit"], cfg["fixes"]["entry7_commit"], cfg["fixes"]["entry8_commit"], LB]
    prev = b""
    for c in chain:
        cur = show(c, cfg["fixes"]["path"])
        must(cur.startswith(prev), "fixes file at %s is not an extension of the previous stage (append-only broken)" % short(c))
        prev = cur
    f6 = show(cfg["fixes"]["entry6_commit"], cfg["fixes"]["path"])
    line_raw = S["LINE"].raw
    LN = cfg["line"]
    must(sha1(line_raw) == LN["expect_sha1"] and len(line_raw) == LN["expect_bytes"], "line sha1 / bytes differ from cfg")
    must(line_raw.endswith(b"\n") and line_raw.count(b"\n") == 1, "the line file is not one line with its newline")
    line = line_raw.decode("utf-8")[:-1]
    must(line.count("|") == 0, "the line carries pipe characters")
    must(line.count("(") == line.count(")") and line.count("[") == line.count("]"), "the line's brackets do not balance")
    must(line.endswith(")."), "the line does not end with ').'")
    must(" — " not in line and not re.search(r"\(\d{4}-\d\d-\d\d\)", line), "the line carries a date parenthesis or a dash separator")
    lspans = gspans(line)
    lm_e = re.search(r"with fixes entries (\d+-\d+)", line)
    lm_s = re.search(r"L-RED-B successors (\d+-\d+)", line)
    must(lm_e and lm_s, "the line's closing parenthesis has no 'with fixes entries a-b' / 'L-RED-B successors a-b'")
    line_entries, line_succ = (lm_e.group(1) if lm_e else "?"), (lm_s.group(1) if lm_s else "?")
    ref1, ref2 = S["REF1"], S["REF2"]
    r1bl = blame_ranges(H["referee"], cfg["referee"]["path"])
    r2bl = blame_ranges(H["referee-2"], cfg["referee2"]["path"])
    must([c for c, _, _ in r1bl] == [short(c) for _, c in cfg["referee"]["stages"]], "REFEREE's report: blame %s differs from cfg.referee.stages" % [c for c, _, _ in r1bl])
    must([c for c, _, _ in r2bl] == [short(c) for _, c in cfg["referee2"]["stages"]], "REFEREE-2's report: blame %s differs from cfg.referee2.stages" % [c for c, _, _ in r2bl])
    must(blame_ranges(H["referee"], cfg["referee"]["precheck_path"]) == [(short(cfg["referee"]["precheck_commit"]), 1, len(S["PRE"].lines))], "pre-check blame")
    gk_sha = sha1(show(FZ, "experiments/red-b/gk.py"))
    RES = S["RES"]
    heads = {m.group(1): i + 1 for i, x in enumerate(RES.lines) for m in [re.match(r"### (R\d+) \[(?:refereed-only|formalized)\] ", x)] if m}
    must(E not in heads and PREV in heads, "RESULTS at the trunk commit: %s present or %s absent" % (E, PREV))
    err_lines = [i + 1 for i, x in enumerate(RES.lines) if x.startswith(cfg["results"]["insert_before_prefix"])]
    must(len(err_lines) == 1, "RESULTS: the Erratum anchor occurs %d times" % len(err_lines))
    lasthead = max(heads.values())
    must(lasthead == heads[PREV] and heads[PREV] < err_lines[0], "RESULTS: %s is not the last heading before the Erratum anchor" % PREV)
    GAPS = S["GAPS"]
    grow = [i + 1 for i, x in enumerate(GAPS.lines) if x.startswith("| %s | " % cfg["gaps"]["row_id"])]
    must(len(grow) == 1, "GAPS row")
    closed = [i + 1 for i, x in enumerate(GAPS.lines) if x == cfg["gaps"]["closed_heading"]]
    must(len(closed) == 1, "GAPS closed heading")
    D, checks = datafacts.facts(cfg)
    must(all(ok for _, ok, _ in checks), "datafacts: %d checks failed" % sum(1 for _, ok, _ in checks if not ok))
    lc_path = os.path.join(OUT, "lanecheck.out")
    lanecheck = open(lc_path, encoding="utf-8").read() if os.path.exists(lc_path) else ""
    must("lanecheck: PASS" in lanecheck, "out/lanecheck.out missing or not PASS (build.sh runs tools/lanecheck.sh before fill131.py)")
    fetch = open(os.path.join(HERE, "fetch.txt"), encoding="utf-8").read().split("\n")
    fdate = fetch[0][5:] if fetch and fetch[0].startswith("date ") else "?"
    fheads = dict((x.split()[1].split("/")[-1], x.split()[5]) for x in fetch if x.startswith("fetch "))
    for lane, c in H.items():
        must(fheads.get(lane) == c, "cfg head of %s (%s) is not the head fetch.txt records (%s)" % (lane, short(c), short(fheads.get(lane, "?"))))
    must(fheads.get(cfg["trunk"]["branch"].split("/")[-1]) == T, "cfg trunk commit is not the trunk head fetch.txt records")
    b2, b3, b4 = D["beyond"]["n^2"], D["beyond"]["n^3"], D["beyond"]["n^4"]
    slots = cfg["slots"]

    def slot(name, open_text):
        s = slots[name]
        if s["open"]:
            assert OPEN_WORD in open_text
            return open_text
        out = []
        for it in s["fill"]:
            out.append(it["text"] if "text" in it else q(it["src"], it["quote"], it.get("occ")))
        must(out, "slot %s is closed but its fill list is empty" % name)
        return " ".join(out)

    def anyopen():
        return [n for n in ("stage5b", "r2_line", "entry9") if slots[n]["open"]] + (["line"] if LN["stand_in"] else [])

    def rng(bl, c):
        r = [(a, b) for cc, a, b in bl if cc == short(c)]
        return "l. %d-%d" % r[0]

    c8 = short
    P = []          # the block's paragraphs: (first_indent, rest_indent, text)

    TOK = {}

    def tok(text):
        for k, v in TOK.items():
            if k in text:
                text = text.replace(k, v())
        assert "@@" not in text, text[text.index("@@"):][:40]
        return text

    def bullet(text):
        P.append(("", "  ", tok(text)))

    def sub(text):
        P.append(("  ", "    ", tok(text)))

    # ================================================================ the entry block
    F.part = "block"
    TOK.update({"@@STUCK@@": lambda: qn("R104P", "stuck"), "@@CORRECT@@": lambda: qn("REF1", "CORRECT"),
                "@@NOTCLAIMED@@": lambda: qn("REF1", "Not claimed"), "@@STEPT@@": lambda: qn("REF2", "step t")})
    title = "### %s [refereed-only] %s, CHECKER PASS (docs/checker/%s.md, checker %s)" % (E, line, CN, OPEN_WORD)

    # ---- Object
    bullet(
        "- Object (L-RED-B successor 5, D1 / D18 / D22 / D25, B6 attempt 2; frozen, unchanged during review): packet %s, %s, sha1 %s, %s lines, "
        "%s bytes (claude/l-red-b %s, %s, the file's only commit; identical at %s). Both referees measured it (REFEREE %s; REFEREE-2 %s). "
        "Its own status: %s. %s. The object: rule R (packet §3) builds, for every k ≥ 3, a genome G_k of RESULTS R104's IDEAL model with levels "
        "0..k and two options per mover (%s); generator experiments/red-b/gk.py (sha1 %s at the freeze commit; REFEREE-2 %s). The claim attacked is "
        "the GAPS row G-N5-TIME, %s."
        % (PK, cfg["packet"]["path"], pkt.sha1, num(len(pkt.lines)), num(len(pkt.raw)), c8(FZ), cdate(FZ), c8(LB),
           q("REF1", "claude/l-red-b 350d84eb, docs/red-b/P-N5-EXP.md sha1 c0449b17193f19619f33b366096762dfde27d542, 569 lines"),
           q("REF2", "docs/red-b/P-N5-EXP.md, sha1 c0449b17193f19619f33b366096762dfde27d542, 569 lines, 57,511 B"),
           q("PKT", "Status: a kill candidate; lane DATA + a lane proof. Nothing here is a result until both referees sign and CHECKER passes it (D1)."),
           q("PKT", "To sign: §2 (Theorem EXP-IDEAL, Corollary EXP-N5), §4 (Lemma MEMBER), §5 (MOVE-2, K1-K4, V0-V4, WIRE), §6 (RESPONSE LEMMA, STABLE), "
                    "§7 (the proofs). To check: §8 (where the start and the orders are used), §9 (DATA reproduction), §10. Not to sign: §9's numbers as "
                    "statements (DATA), §11 (READING)"),
           q("PKT", "Counts: 2 + 2(k − 1) + (k − 3) + (k − 2) + (k − 3) + 2(k − 1) + 2(k − 3) = 9k − 16."),
           gk_sha, q("REF2", "generator experiments/red-b/gk.py, sha1 5222f555f9572e5c92119a2bc1e16d02008a96c5 (192 lines, read in full)"),
           q("GAPS", "N5 SSI-GLOBAL makes polynomially many iterations (gauntlet step 4, running time)")))
    must(gk_sha == "5222f555f9572e5c92119a2bc1e16d02008a96c5", "gk.py sha1 at the freeze commit")

    # ---- Fixes
    def fr(c):
        r = [(a, b) for cc, a, b in fbl if cc == short(c)]
        return "l. %d-%d %s %s" % (r[0][0], r[0][1], short(c), cdate(c))

    fx = cfg["fixes"]
    bullet(
        "- Fixes: %s, append-only (%s), at claude/l-red-b %s: %s lines, %s bytes, sha1 %s, entries 1-%d by their headings (git blame: entry 1 %s; "
        "entries 2-5 %s; entry 6 %s; entry 7 %s; entry 8 %s); each stage of the file is a byte prefix of the next (asserted by script). At %s it is the "
        "object of REFEREE-2's signature (829 lines, sha1 %s), at %s the object of REFEREE's (881 lines, sha1 %s). "
        "Entry 1 (L-RED-B 5): %s; six DATA subsections 9.8-9.13, a pointer correction and the reproduction erratum 10.E (at the freeze commit the "
        "runner needs an absolute root; from entry 1 on it counts a failing stage and exits 1). "
        "Entries 2-5 (L-RED-B 6) answer the referees item by item: %s. "
        "Entry 2 (labels): (a) UNCONDITIONAL, Theorem EXP-IDEAL (a)-(c) with its lemmas; (a′) %s, refuted by (b) alone; (b) Corollary EXP-N5 is %s and "
        "%s; (c) the dead-end sentences are read through R117, in full %s; (d) MEASURED: %s; (e) the correctness sentence is RESULTS R57 (b), Lemma "
        "OUT-G, for every k and DATA for the k that were run. "
        "Entry 3: Corollary EXP-N5′, %s, with %s. "
        "Entry 4: the RESPONSE LEMMA restated: %s; %s. "
        "Entry 5 (wording and records, %s): 5.1 the rank clause read with its tie-break by β-id, 5.2 %s (said once in 4.1 (S2)), 5.3 the "
        "text of §9.7's placeholder, 5.4 level widths, 5.5 genomes of record and raw files, 5.6 the mover order, 5.7 the JSON fields, 5.8 the other "
        "lanes' DATA with their commits, 5.9 two notes recorded. "
        "Entry 6: %s (N5 at k = 13, engine 1, by the checkpointed driver b6n5ck.py). "
        "Entry 7 (L-RED-B 7): REFEREE-2's F-1 to F-5 and REFEREE's stage 4, %s: 7.1 %s %s; 7.2 which frozen lines of §6 stay in force as "
        "definitions (a table of the frozen l. 191-204); 7.3 %s; 7.4 the runner run_b6fix.sh repaired (%s; its test file ends %s); 7.5 the two "
        "sentences of entry 2 (a′) labelled, %s; 7.6 guards, line L-2, pins. "
        "Entry 8: the line L-3 from L-2, %s. %s"
        % (fx["path"], q("FIX", "append-only; the packet docs/red-b/P-N5-EXP.md is never edited after its freeze commit 350d84eb"), c8(LB),
           num(len(fix.lines)), num(len(fix.raw)), fix.sha1, nent, fr(fx["entry1_commit"]), fr(fx["entries2_5_commit"]), fr(fx["entry6_commit"]),
           fr(fx["entry7_commit"]), fr(fx["entry8_commit"]), c8(fx["entries2_5_commit"]), sha1(f25), c8(fx["entry6_commit"]), sha1(f6),
           q("FIX", "extra DATA, no change to any statement, proof or hypothesis", 1),
           q("FIX", "What changes: the STATEMENTS of the RESPONSE LEMMA and of STABLE are replaced by the forms of entry 4 (the mathematics and every "
                    "number stay); the LABELS of Corollary EXP-N5 and of the dead-end paragraph are fixed by entry 2; entry 3 adds a corollary; entry 5 "
                    "is wording and records. Theorem EXP-IDEAL (a)-(c) is unchanged."),
           q("FIX", "Let IDEAL-ACYC-POLY mean: there is a polynomial q such that L(G) ≤ q(N + M) for every G ∈ IDEAL-ACYC."),
           q("FIX", "PROVED-CONDITIONAL on RESULTS R117's Theorem REACH3 AS LANDED [refereed-only].", 1),
           q("FIX", "it inherits R117's standing premises and adds none"),
           q("FIX", "under R117's Theorem REACH3 as landed, N5 (SPEC S1-S5) from its default start S3 makes at least 2^k − 1 iterations on Γ3(G_k), a "
                    "game with n = 135k − 230 vertices and n + m = 311k − 530 vertices and edges; so N5 from S3 does not run in polynomial time, cannot "
                    "pass gauntlet step 4, and G-N5-TIME is answered NO for N5 from S3."),
           q("FIX", "So no measured run lies beyond an explicit polynomial bound of degree 2 or more, and the kill rests on the PROOF: (a) with R117 "
                    "(and R124 for the exact count, entry 3)."),
           q("FIX", "For every k ≥ 3, N5 (SPEC S1-S5 with its FIX 1-4 tie-breaks) from S3 on Γ3(G_k) makes EXACTLY L(G_k) + 3 = 2^k + 1 iterations, "
                    "with exactly one fallback, at iteration 2^k − 1."),
           q("FIX", "The frozen Corollary EXP-N5 (at least 2^k − 1 iterations, by R117 alone) stays as frozen and is all the dead end needs."),
           q("FIX", "The frozen STATEMENT of the RESPONSE LEMMA (l. 192-204) is REPLACED by 4.4 and the frozen statement of STABLE (l. 258) by 4.2; "
                    "the frozen PROOF text (l. 205-257, 258-262) stays and is read as 4.5 says; Theorem EXP-IDEAL, its proof (§7, read as 4.6) and "
                    "every other statement are unchanged."),
           q("FIX", "It does not write a third form: 4.3 and 4.4 ADOPT REFEREE 36's two statements word for word, 4.4 shows that REFEREE-2's PREFIX "
                    "FORM is the same statement, and 4.5 gives the proof in the order both referees give."),
           q("FIX", "No statement changes. Each item: the referee's words, then the reading that completes or replaces the frozen words."),
           qn("FIX", "step τ"),
           q("FIX", "N5 itself at k = 13 on one engine — extra DATA, no change to any statement, proof or hypothesis"),
           q("FIX", "two readings of entry 4, one of entry 5, the runner run_b6fix.sh repaired, one label, line L-2; no statement, proof, hypothesis or "
                    "number changes"),
           q("FIX", "Accepted. Neither wording names the lower end of the range. Clause (R3) of 4.4 is to be READ, there and wherever it is cited:"),
           q("FIX", "(R3) For T = last: if j ≥ 2, then s_τ(E(j)) = a for every τ with t − 1 ≤ τ < last, and E(j) moves to c at step last"),
           q("FIX", "READ the parenthesis as: (table: every Ξ-target is a u, v, y, ȳ, y′, ȳ′ or X)."),
           q("FIX", "every failure is counted, the last line ends «failures N», and the runner exits 1 if N > 0"),
           q("FIX", "b6fixtest failed 0", 2),
           q("FIX", "The lines L-1 and L-2 carry (i) only; neither names QUIET-KEY-1P, SW-POLY or P-N5-KEY1P."),
           q("FIX", "a record of the line only, no statement, proof, hypothesis or number changes"),
           slot("entry9", "Fixes entry 9 %s (the entry that records the line of record %s; no referee has read it)." % (OPEN_WORD, LN["of_record_name"]))))

    # ---- The RESULTS line
    order = ["R104P", "RES", "REF1", "REF2", "PKT", "FIX"]
    found = []
    for i, (_, _, inner) in enumerate(lspans, 1):
        hit = None
        for k in order:
            o = S[k].find(inner)
            if o:
                hit = (k, o[0], len(o))
                break
        must(hit is not None, "quotation %d inside the line is in none of %s: %r" % (i, order, inner[:60]))
        if hit:
            F._add("line", hit[0], inner, hit[1], hit[2])
            found.append("(%d) %s %s" % (i, S[hit[0]].what, loc(*hit[1])))
    hist = " ".join((it["text"] if "text" in it else q(it["src"], it["quote"], it.get("occ"))) for it in LN.get("history", []))
    bullet(
        "- The RESULTS line is %s, %s (%s, claude/l-red-b %s, %s; %s bytes, one line with its newline; %d opening and %d closing parentheses, no "
        "square bracket, no pipe character, %d guillemet quotations). The title is the line verbatim, with nothing inserted and nothing stripped (it "
        "has no date parenthesis and no dash separator; its status phrase, scope tail, source note and final full stop are the line's own: the landed "
        "form of %s). Its quotations are found verbatim by script: %s. Its closing parenthesis names fixes entries %s and L-RED-B successors %s. "
        "History of the line (the lane's builder experiments/red-b/b6line.py, named replacements, each old text exactly once): L-1 (%s, 5,585 bytes, "
        "claude/l-red-b %s) was read by REFEREE-2 (Addendum 2 §A2.7: %s, with three notes); L-2 = L-1 with REFEREE-2's L-a (the gloss of the units), "
        "L-b (R117's premises in the words of its title line), L-c (the L41 scope tail) and the Lead's L-d (k = 13 from entry 6), fixes 7.6: %s; "
        "L-3 = L-2 with two replacements in the closing parenthesis, fixes entry 8: %s.%s%s"
        % (LN["name"], sha1(line_raw), LN["path"], c8(LN["commit"]), cdate(LN["commit"]), num(len(line_raw)), line.count("("), line.count(")"),
           len(lspans), PREV, "; ".join(found), line_entries, line_succ,
           sha1(show(fx["entries2_5_commit"], "docs/red-b/P-N5-EXP-line-L1.txt")), c8(fx["entries2_5_commit"]),
           q("REF2", "Every clause that comes from this lane's review agrees with it"),
           q("FIX", "L-2 bytes 7267 (with its newline) lines 1 pipes 0 sha1 6e047c676e582484fe8eb87891764e8c1a7d9a18"),
           q("FIX", "L-3 bytes 7267 (with its newline) lines 1 pipes 0 sha1 fd9074a3b9961f59a1b64d5acdaa28529306ede9"),
           (" " + hist) if hist else "",
           (" Line of record %s %s: this fill stands on %s as a stand-in; %s is to be %s with one clause changed (R124's Theorem ENDGAME-3-N5 named "
            "beside Corollary EXACT-L) and comes with fixes entry 9; no referee has read it." % (LN["of_record_name"], OPEN_WORD, LN["name"],
                                                                                                 LN["of_record_name"], LN["name"])) if LN["stand_in"] else ""))
    must(sha1(show(fx["entries2_5_commit"], "docs/red-b/P-N5-EXP-line-L1.txt")) == "59c5309377eda882ba436ffe7eb03fbff598c7c8", "L-1 sha1")

    # ---- Claims signed
    def rows1(src_key, header, fmt):
        out = []
        for ln, cells in table_rows(S[src_key], header):
            cs = [raw(src_key, c)[0] if c not in ("", "—") else c for c in cells]
            out.append(fmt(cs) + " (l. %d)" % ln)
        return "; ".join(out)

    t10 = rows1("REF1", ["item (packet section)", "verdict", "kind of statement", "gaps / required fixes"],
                lambda c: "%s → %s [%s; %s]" % (c[0], c[1], c[2], c[3]))
    t13 = rows1("REF1", ["statement", "where it now stands", "verdict", "kind"],
                lambda c: "%s%s → %s [%s]" % (c[0], (" (" + c[1] + ")") if c[1] else "", c[2], c[3]))
    t20 = rows1("REF2", ["statement (packet §)", "verdict", "items"], lambda c: "%s → %s [%s]" % (c[0], c[1], c[2]))
    t2a = rows1("REF2", ["entry", "this lane's items", "verdict"], lambda c: "%s (%s) → %s" % (c[0], c[1], c[2]))
    st1 = ", ".join("%s %s %s" % (n, rng(r1bl, c), c8(c)) for n, c in cfg["referee"]["stages"])
    st2 = ", ".join("%s %s %s" % (n, rng(r2bl, c), c8(c)) for n, c in cfg["referee2"]["stages"])
    bullet(
        "- Claims signed (REFEREE successors 36 and 37, %s at claude/referee %s: %s; REFEREE-2 successors 41 and 42, %s at claude/referee-2 %s: %s). "
        "REFEREE's first table (§0, stage 1), row by row as the report prints it: %s; then %s. After the fixes, REFEREE's table of what its signature "
        "covers (§13.0, stage 5a), row by row: %s; its signature line: %s. "
        "REFEREE-2's table (§0 of its report), row by row: %s; then %s. Its table on the fixes file (Addendum 2, §A2.0), row by row: %s; its "
        "signature: %s. REFEREE-2 on the two reviews together (Addendum 3): %s. No statement is REFUSED by either referee. The frozen statement of "
        "the RESPONSE LEMMA is signed by neither: both sign it in the restated form LEMMA′ of fixes entry 4 (L41, below). The joint gap map is in "
        "the Note bullet: every required item is closed by a fixes entry that the referee who raised it has checked, except what the open slots "
        "name (Signatures)."
        % (cfg["referee"]["path"], c8(H["referee"]), st1, cfg["referee2"]["path"], c8(H["referee-2"]), st2,
           t10, q("REF1", "No statement is REFUSED. Nothing found changes L(G_k) = 2^k − 2, the counts of (c), or the Corollary's numbers."),
           t13, q("REF1", "**P-N5-EXP: SIGNED with fixes entries 1-6.** What the signature covers, by kind"),
           t20, q("REF2", "No error was found in the mathematics. No counter-instance, no failing counter. The two listed items change no number."),
           t2a,
           q("REF2", "**P-N5-EXP: SIGNED with fixes entries 1-5.** The signature is §0's, with one correction (§A2.1): the statement of the RESPONSE "
                     "LEMMA that I sign is entry 4's 4.4 (LEMMA′), not the frozen l. 192-204; STABLE is signed in 4.2's step form. Every other row "
                     "of §0 stands as written. Items F-1 to F-5 are wording and tooling; none of them is a condition of the signature except the "
                     "reading F-1."),
           q("REF2", "No verdict differs after the fixes, and no number differs anywhere")))

    # ---- Statements as signed, by standing
    bullet(
        "- Setting and scope, as both referees sign it. The objects are R104's IDEAL model on the genomes G_k (k ≥ 3), the games Γ3(G_k) of RESULTS "
        "R117, and N5 (SPEC S1-S5 with FIX 1-4) from its default start S3. Statements as signed (the packet with fixes entries 1-5 for both "
        "referees, entry 6 for REFEREE), by standing:")
    sub("(a) UNCONDITIONAL (R104's definitions only; no theorem, no SPEC premise, nothing about N5). Theorem EXP-IDEAL (a) = Lemma MEMBER: G_k is a "
        "genome of R104's class in IDEAL-ACYC with N = 9k − 16 movers, M = 18k − 32 options and k + 1 levels, the rank clause read with its "
        "tie-break by β-id (fixes 5.1). MOVE-2, V0-V4, K1-K4, WIRE under the standing assumption of fixes 4.1 (S1), every wire and u_0 at option 0. "
        "The RESPONSE LEMMA as LEMMA′ (fixes 4.4) with CAUSAL (4.3) and STABLE in step form (4.2). Theorem EXP-IDEAL (b): L(G_k) = 2^k − 2 and the "
        "run stops @@STUCK@@; (c): every mover of unit j changes its option exactly 2^(j−1) times, v_0 once, u_0 and the wires never, 11·2^(k−2) − 9 "
        "changes in all. REFEREE %s (%s; %s); REFEREE-2 %s (%s; %s)."
        % (q("REF1", "(1) Theorem EXP-IDEAL (a)-(c) SIGNED (unconditional), (b), (c) through LEMMA′"),
           l("REF1", "| Theorem EXP-IDEAL (a), (b), (c), with MEMBER, MOVE-2, V0-V4, K1-K4, WIRE |"),
           l("REF1", "| RESPONSE LEMMA = LEMMA′, with CAUSAL; STABLE in step form |"),
           q("REF2", "UNCONDITIONAL (mathematics about R104's DEFINITIONS, no theorem used): Theorem EXP-IDEAL (a), (b), (c) with its lemmas."),
           l("REF2", "| Theorem EXP-IDEAL (b), (c) (§7) | **SIGN** (through the RESPONSE LEMMA with G-1 closed) | G-1 |"),
           l("REF2", "**REFEREE-2 signs 4.1 (S1)-(S4), 4.2 STABLE, 4.3 CAUSAL, 4.4 LEMMA′")))
    sub("(b) UNCONDITIONAL consequence inside the model: the statement that R104's packet names IDEAL-ACYC-POLY (%s; docs/red/P-N5-REALIZE.md at "
        "trunk) is FALSE, already for genomes of degree 2: L(G_k) = 2^k − 2 against N + M = 27k − 48. REFEREE %s; REFEREE-2 %s. Not carried by the "
        "line and not part of this entry: the second sentence of fixes entry 2 (a′), on L-NEW's lane packet P-N5-KEY1P (Not signed, below)."
        % (q("R104P", "Let IDEAL-ACYC-POLY mean: there is a polynomial q such that L(G) ≤ q(N + M) for every G ∈ IDEAL-ACYC."),
           l("REF1", "| «IDEAL-ACYC-POLY is false» | entry 2 (a′), its sentences on R104's model | **SIGNED** |"),
           q("REF2", "That IDEAL-ACYC-POLY is false follows from Theorem EXP-IDEAL (b) alone (L(G_k) = 2^k − 2 against N + M = 27k − 48): unconditional.")))
    sub("(c) PROVED-CONDITIONAL on RESULTS R117's Theorem REACH3 as landed [refereed-only], with R117's standing premises (Premise, below). "
        "Corollary EXP-N5: Γ3(G_k) has n = 135k − 230 vertices and m = 176k − 300 edges, and the N5 run of Γ3(G_k) from S3 has one FL run of length "
        "exactly 2^k − 2 and makes at least 2^k − 1 iterations; so no polynomial in n or in n + m = 311k − 530 bounds the number of iterations of "
        "N5 from S3. The dead-end sentence, as fixes entry 2 (c) reads it: through R117, N5 from S3 does not run in polynomial time, cannot pass "
        "gauntlet step 4, and G-N5-TIME is answered NO for N5 from S3. REFEREE %s and %s; REFEREE-2 %s; the sizes n and m are unconditional "
        "(REFEREE-2 signs them outright, its row l. %d)."
        % (l("REF1", "| Corollary EXP-N5 (at least 2^k − 1 iterations) | packet §2, §7 with entry 2 (b) |"),
           l("REF1", "| Dead-end paragraph | packet l. 61-71 read as entry 2 (c), (e) |"),
           q("REF2", "PROVED-CONDITIONAL on RESULTS R117 as landed: Corollary EXP-N5's iteration bound, and with it the Dead-end paragraph"),
           S["REF2"].find("the sizes n = 135k − 230 and m = 176k − 300 SIGN outright")[0][0]))
    sub("(d) PROVED-CONDITIONAL on RESULTS R124's Corollary EXACT-L and Theorem ENDGAME-3-N5 as landed [refereed-only] (premise R117 (f) = Theorem "
        "REACH3, so the premises of (c), with R124's own). Corollary EXP-N5′ (fixes entry 3): N5 from S3 on Γ3(G_k) makes exactly 2^k + 1 iterations, "
        "with exactly one fallback, at iteration 2^k − 1. An addition: the dead end needs (c) only. REFEREE: statement %s, statement and proof %s; "
        "REFEREE-2 %s and, on entry 3, %s."
        % (q("REF1", "entry 3's **Corollary EXP-N5′, the STATEMENT, is SIGNED AS PROVED-CONDITIONAL on RESULTS R124 and R117 as landed**"),
           q("REF1", "I SIGN the corollary as PROVED-CONDITIONAL on RESULTS R124 (Corollary EXACT-L, Theorem ENDGAME-3-N5) and RESULTS R117 (f) as "
                     "landed"),
           q("REF2", "Status of the exact form: PROVED-CONDITIONAL on R124 and R117 as landed; no new premise beyond those two entries."),
           q("REF2", "**Addendum 1 A1.1 → entry 3: closed.**")))
    sub("(e) MEASURED (DATA, premise-free): the runs of the model and of N5 itself (Data, below). They test every step of the proof and the "
        "predictions of R117 and R124; they kill nothing by themselves (L43, below).")

    # ---- Premise
    hl = lambda r: "RESULTS %s (l. %d)" % (r, heads[r])                      # noqa
    for r, _ in cfg["premises"]:
        must(r in heads, "premise %s has no landed heading at the trunk commit" % r)
    bullet(
        "- Premise (landed RESULTS entries only; heading lines at trunk %s by script; none is later than %s). For (a), (b): %s, DEFINITIONS ONLY "
        "(the genome, IDEAL-ACYC, the X-chain order, the IDEAL step, L(G)): packet %s; REFEREE %s. For (c): %s, Theorem REACH3 as landed, with its "
        "standing premises in R117's own words, its title line: %s (RESULTS l. %d); these are 1E-N3 = %s (b), %s (a) and (b) with %s's bridge B, "
        "%s (c) and %s (d), each a landed [refereed-only] entry; in R117's entry they are called [1E-N3], [RULE], [VJ-LOC], [TERM], and %s. REACH3's "
        "one hypothesis on the genome is %s, met by Lemma MEMBER; its clause used is %s (both in RESULTS l. %d). For (d): %s, as landed, its title "
        "line: %s and %s. For the correctness sentence: %s (b), Lemma OUT-G: %s. The premise 1E-N3 is SPEC's standing requirement, not a theorem of "
        "the fleet: REFEREE %s. Not used: %s; no theorem of R104; nothing of R125-%s. L-SI's box 108 is supporting evidence, not a premise (Referee "
        "strengthening)."
        % (c8(T), PREV, hl("R104"), q("PKT", "**R104, DEFINITIONS ONLY** (no theorem of R104 is used)."),
           q("REF1", "So «DEFINITIONS ONLY (no theorem of R104 is used)» is right; MEMBER c8 (acyclic) comes first and makes the X-chains finite. No "
                     "circularity."),
           hl("R117"),
           qn("RES", "with R104's premises as landed (1E-N3 = RESULTS R57 (b) in its two forms; RESULTS R24 (a) Lemma R and R24 (b)'s choice rule with "
                     "RESULTS R103's bridge B and (R1) ruling; RESULTS R36 (c) Lemma P1 on the dual game) and RESULTS R15 (d) for termination only"),
           heads["R117"], hl("R57"), hl("R24"), hl("R103"), hl("R36"), hl("R15"),
           q("RES", "Premises [1E-N3], [RULE], [VJ-LOC] as landed in R104: the correctness of S1's procedure stays SPEC's requirement, and the code's "
                    "match to SPEC is DATA (R57 (b))"),
           qn("RES", "for every G with an ACYCLIC Ξ-graph"),
           qn("RES", "so if L(G) ≥ 1, [0, L(G)] is one FL run of length exactly L(G) and the run makes at least L(G) + 1 iterations"),
           heads["R117"], hl("R124"),
           qn("RES", "premise RESULTS R117 (f); it uses SPEC's S1 tie-breaks, through REACH3's [RULE] choice: with another pointwise-optimal S4a choice "
                     "the identity can fail"),
           qn("RES", "premises, all under the standing SPEC premise 1E-N3 of RESULTS R57 / R104 / R117"),
           hl("R57"),
           q("RES", "In particular, on every game N5 stops (R15 (d)) and SPEC S5's output there is correct. Standing premise, as in R51 (d): OUT-G "
                    "concerns SPEC's Ξσ and σ̄; that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC conformance, and the code's match to "
                    "SPEC is DATA (R15 G-N5T-1) (1E-N3 = N-1E-1)."),
           q("REF1", "1E-N3 is the standing SPEC premise of every landed N5 result since R57"),
           q("PKT", "NOT used: R105, R113, R120."), PREV))
    for s_ in ("with R104's premises as landed (1E-N3", "for every G with an ACYCLIC Ξ-graph", "so if L(G) ≥ 1, [0, L(G)] is one FL run"):
        must(S["RES"].find(s_) and S["RES"].find(s_)[0][0] == heads["R117"], "an R117 quotation is not in R117's title line")
    for s_ in ("premise RESULTS R117 (f); it uses SPEC's S1 tie-breaks", "premises, all under the standing SPEC premise 1E-N3"):
        must(S["RES"].find(s_) and S["RES"].find(s_)[0][0] == heads["R124"], "an R124 quotation is not in R124's title line")

    # ---- L41 and L43
    bullet(
        "- L41 and L43. The packet's proofs are L-RED-B successor 5's, with one referee-originated restatement: CAUSAL and LEMMA′ (and the standing "
        "paragraph and STABLE's step form) are REFEREE 36's (its §5.3, from %s, in stage 1), adopted word for word in fixes entry 4. Under L41 (%s) the author signs "
        "and the other referee signs independently: REFEREE %s, and after the fixes entry %s; REFEREE-2 %s, on the same text: %s (REFEREE's own "
        "script: %s). The one condition of the second signature is the reading F-1 of clause (R3), which the lane takes over in fixes 7.1; its "
        "confirmation by the statement's author is part of the open slot of REFEREE (Signatures). The line names both signatures in its scope tail. "
        "L43 (%s): the DEAD rests on a PROOF, not on an instance: REFEREE %s; REFEREE-2 %s. By script from the pinned outputs: every measured run "
        "lies below n², n the number of vertices of Γ3(G_k): N5 itself for k = 3..13 (the largest, k = 13: %s iterations on n = 1,525, n² = %s) and "
        "the model alone to k = 20 (L-COMP 22: T = %s, where Γ3(G_20) would have n = 2,470, n² = %s); 2^k − 1 exceeds n² first at k = %d (n = %s: "
        "%s > %s), n³ at k = %d, n⁴ at k = %d, by exact integer arithmetic, not run. So the dead end rests on the proved growth (Theorem EXP-IDEAL "
        "for every k, put into R117), not on a measured instance, and every DATA clause below names its counter and unit."
        % (l("REF1", "### 5.3 The repair (referee-originated, L41): CAUSAL and LEMMA′"),
           q("DEC", "A proof written by one referee counts toward \"two referees signed it with its gaps listed\" (CLAUDE.md) when the author referee "
                    "signs it in its report and the OTHER referee independently checks and signs it"),
           q("REF1", "**NOT SIGNED AS WRITTEN; SIGNED in the form LEMMA′ of §5.3 below**"),
           q("REF1", "**Verdict on entry 4: it closes E-1, E-2, E-4, E-5. RESPONSE LEMMA SIGNED as restated in fixes entry 4 (= LEMMA′ of §5.3 with "
                     "CAUSAL and STABLE in step form).**"),
           q("REF2", "**REFEREE-2 signs 4.1 (S1)-(S4), 4.2 STABLE, 4.3 CAUSAL, 4.4 LEMMA′ with their proofs (4.2, 4.3, 4.5) and 4.6, as printed in "
                     "docs/red-b/P-N5-EXP-fixes.md at claude/l-red-b 24f4d436 (sha1 9dc9179f…), (R3)'s range read as t − 1 ≤ τ < last (F-1).**"),
           q("REF2", "So the text I signed in §A2.3 IS the referee-originated text, and L41's two signatures are on the same statements"),
           q("REF1", "fixes4: my §5.3 inside entry 4, white space normalised, the bold labels dropped: standing paragraph 1, CAUSAL 1, LEMMA′ 1 (1 = "
                     "verbatim)"),
           q("DEC", "«DEAD» in a landing line needs a refereed proof, or one instance exceeding an EXPLICIT bound"),
           q("REF1", "L43 («DEAD» needs a refereed proof or an instance beyond an explicit bound): the growth is PROVED for every k ≥ 3 (Theorem "
                     "EXP-IDEAL (b), unconditional; this report signs it through LEMMA′); the DEAD of «N5 runs in polynomial time» then holds under "
                     "R117's premises."),
           q("REF2", "They are far below every explicit polynomial bound (2^k − 1 < n² until k = 23, where a run would take 8.4 million iterations on "
                     "2,875 vertices): no measured instance «beyond an explicit bound» exists or is in reach of these engines. The kill rests on the "
                     "proof."),
           num(D["n5_its"][13]), num(1525 ** 2), num(2 ** 20 - 2), num(2470 ** 2), b2[0], num(b2[1]), num(b2[2]), num(b2[3]), b3[0], b4[0]))

    # ---- Not signed
    bullet(
        "- Not signed: the packet's §9 numbers as statements (DATA), §10 (reproduction; REFEREE-2 %s; REFEREE %s) and §11 (READING); the ablation "
        "rows of §9.6 (%s); the second sentence of fixes entry 2 (a′), that QUIET-KEY-1P and SW-POLY of L-NEW's lane packet P-N5-KEY1P are false, "
        "which holds only through that packet's Lemma IDEAL-1P, a lane lemma that is not landed (REFEREE-2 %s; REFEREE %s); L-SI's box 108 as a "
        "result; R117's and R124's own proofs, which are landed and were not re-refereed here (REFEREE %s); anything outside the packet's %s."
        % (q("REF2", "NOT run as written (the lane's script and archives); CHECKER's exact-commit re-run covers it"),
           q("REF1", "the lane's run_b6b.sh and its simulators / engines (onep, one217, r187, n5v, n5b) were not run: my tools replace them"),
           q("PKT", "this variant is NOT covered by the proof"),
           q("REF2", "A RESULTS line may carry the first sentence as unconditional and not the second; line L-1 does exactly that."),
           q("REF1", "The sentence of entry 2 (a′) on L-NEW's packet (QUIET-KEY-1P and SW-POLY are false) is right as worded: it holds THROUGH L-NEW's "
                     "Lemma IDEAL-1P (T_key(G) = L(G); packet P-N5-KEY1P, a frozen lane packet, signed by this lane in R-P-N5-KEY1P.md §2; not a "
                     "landed result) and is not a statement of this packet."),
           q("REF1", "R117's proofs were not re-refereed here (landed; successor 35 read them against G_k's features, §7)"),
           q("PKT", "**Not claimed.** Nothing about N5 from other start pairs; nothing about other tie rules (N5′-xi makes 7 iterations on Γ3(G_4) and "
                    "Γ3(G_6), §9.4) or about Howard / switch-best (3 or 4 steps on the model); nothing about any other candidate or about parity "
                    "games in general")))

    # ---- Referee strengthening
    b108 = S["B108"]
    bullet(
        "- Referee strengthening and supporting evidence (NOT part of this entry). (i) REFEREE 35's pre-check (%s at claude/referee %s, %s; not a "
        "signature; written from the rule as relayed, without the packet): %s. (ii) An INDEPENDENT proof of L(G_k) = 2^k − 2: L-SI successor 56's box 108 (%s, "
        "claude/l-si %s, sha1 %s, %s lines; %s; %s), by a closed form of the run and a 32-row table, with no response lemma. It was compared with the "
        "packet by REFEREE (stage 3: %s; %s) and checked by REFEREE-2 only (%s at claude/referee-2 %s: %s; %s). So it has ONE referee's check and is "
        "not a two-referee result: supporting evidence for (a), not a premise of anything here. (iii) Each referee rebuilt the family and re-ran the "
        "model and N5 with its own code (DATA counters for the cited replays, below); REFEREE stage 2 also checked a unit against arbitrary delays "
        "of the unit above (its §10.2) and stage 5a compared the k = 13 game with its own builder's (%s)."
        % (cfg["referee"]["precheck_path"], c8(cfg["referee"]["precheck_commit"]), cdate(cfg["referee"]["precheck_commit"]),
           q("PRE", "no hypothesis of R104's class or of R117's proofs is violated by G_k"),
           cfg["box108"]["path"], c8(cfg["box108"]["commit"]), b108.sha1, num(len(b108.lines)),
           q("B108", "Labels: PROVED (L-SI lane, unrefereed) / DATA (counter, unit, set, scope) / OPEN."),
           q("B108", "INDEPENDENCE: written from the Lead's rule (§1.2) and R104's definition (§1.1) only."),
           q("REF1", "Result of stage 3: no conflict between the two proofs; the verdicts of §0 stand."),
           q("REF1", "NOT refereed here: it is not my packet; its STEP table (32 transition classes) was not checked row by row."),
           cfg["referee2"]["box108_path"], c8(H["referee-2"]),
           q("R2B", "It is ONE referee's check of a lane proof. It is not a second signature on box 108"),
           q("R2B", "No gap was found in Lemma STEP or in Lemma MOVE. Three wording items (§1), none of them changes a statement."),
           q("REF1", "pg13: G_13 pgonly N 101 M 202 n 1525 m 1988 maxprio 817 L 8190 PG 0 GEN35 0")))

    # ---- Honest limits
    bullet(
        "- Honest limits: (i) Everything said about N5 is conditional: (c) on RESULTS R117 as landed and (d) on RESULTS R124 as landed, both "
        "[refereed-only], under the standing SPEC premise 1E-N3, which is not proved in the fleet; only (a) and (b), statements about R104's IDEAL "
        "model, are unconditional. (ii) It is a dead end for ONE candidate with ONE tie rule from ONE start: N5 (SPEC S1-S5 with FIX 1-4, S4a's "
        "root-first key rule) from its default start S3. Nothing is claimed about other start pairs, other tie rules (N5′-xi stops after 7 "
        "iterations on Γ3(G_4) and Γ3(G_6): DATA), Howard's rule (at most %d steps on the model: DATA), any other candidate, or parity games in "
        "general. (iii) No measured run lies beyond an explicit polynomial bound of degree 2 or more (L43, above): the largest N5 run has 8,193 "
        "iterations, above n + m = 3,513 and below n² = %s. (iv) N5's ANSWER on these games is right: %s (b), Lemma OUT-G, for every k (under "
        "1E-N3), and DATA for the k that were run (winners equal to Zielonka's for k ≤ 12 on two engines and at k = 13 on one); what fails is the "
        "polynomial bound, not the answer. (v) The growth is exponential in k and n = 135k − 230, so the bound is %s: a small base, a true "
        "exponential in n. (vi) The lane's tools were written by the lane; at k = 13 one engine ran, not two. (vii) No Lean. (viii) No algorithm "
        "and no bound is claimed, and no novelty against the literature (not M3)."
        % (D["howard_max"], num(1525 ** 2), hl("R57"), qn("PKT", "at least 2^k − 1 = 2^((n + 230)/135) − 1 iterations")))

    # ---- Data
    n5 = D["n5_its"]
    bullet(
        "- Data (DATA, not proof; every clause names its counter and unit, L43): experiments/red-b/ at claude/l-red-b %s, outputs in "
        "data/b6b/out/, pinned in %d pin files (%s; %d files, 0 sha1 mismatches against the git objects, by script) and checked by "
        "experiments/red-b/check.sh. Numbers below are read by script from the pinned outputs (tools/data.py, %d checks). Membership (unit: one "
        "genome): R104's eight clauses, must-0 counters c1-c8 and their sum viol, 0 on G_3..G_14 (member.out); 8 damaged copies of G_5 fire "
        "(member_ctrl.out). The IDEAL run (unit: one genome): must-0 counter ideq (three simulators, state by state) 0 and T = 2^k − 2 for k = 3..14 "
        "(sim.out). The proof's facts on the run (lemma.out, k = 3..14): must-0 counters kfact, vfact (unit: a (state, comparison) pair), sched "
        "(unit: a step), tlen, rest (unit: a genome), swk (unit: a mover) all 0; two controls fire (sched 19, kfact 25). LEMMA′, CAUSAL, STABLE of "
        "fixes entry 4 (b6prefix.py, prefix_*.out): must-0 counters h1, h2, psched, empty at %s response windows and %s (window, step) pairs of the "
        "runs for k = 3..14; aviol 0 on %s triples (j, a, t) for k = 3..12, where the windows are exactly the recursion's 2^(k−1) − 1; pviol 0 off "
        "the run (%s windows, %s of them proper prefixes); dviol 0 on %s driven windows (%s proper); loc 0 (CAUSAL as a function) on %s states and "
        "stviol 0 on %s cases; c0e0, loc, stviol, pviol 0 on EVERY state of G_3 (512) and G_4 (65,536) with the wires and u_0 at option 0; the "
        "lemma as frozen, as a control, fails at exactly k − 1 triples per k (k = 3..8). Clause (R3) as read in fixes 7.1 (e7_r3.out, unit: a "
        "response window): r3in, r3move, r3rest 0 at %s windows for k = 3..14. N5 itself (unit: one game Γ3(G_k); must-0 counters mism, wrong, "
        "nonmover, gdiff, and with two engines wrong2, engdiff): k = 3..11 (n5.out) and k = 12 (n5_k12.out) on two engines and two Γ3 builders, "
        "iterations %s, …, %s, %s = 2^k + 1 on n = 175, …, 1,255, 1,390 vertices, one fallback each; k = 13 on engine 1 only (n5_k13.out): %s "
        "iterations on n = 1,525, one fallback after 8,190 S4a iterations. Sizes (size.out, size_k13.out): must-0 counter sizediff, n = 135k − 230 "
        "and m = 176k − 300 on the game files, k = 3..11 and 13. Strategies (TARGET.md §5, D2 change 5): must-0 counter badstrat (harness verifier) "
        "0 for k = 3..10. Also 0: venab, kenab, movd (enab.out, k = 3..12), keep on %s gate relabelings (perm.out), startdiff, padcyc, padp, fbpos "
        "(reach.out, R117's side lemmas on these games, k = 3..8). Frozen instances: data/b6b/pg/G_k_g3.pg, k = 3..11 at %s (smallest: %d vertices, "
        "%d edges, 9 iterations), and k = 12, 13 from fixes entries 1 and 6; genomes of record data/b6b/G/G_k.json, k = 3..14. Re-run by the drafter "
        "in a git archive of %s: experiments/red-b/check.sh exit 0, %s; with one byte appended to the pinned n5_k13.out it prints %s and %s "
        "(negative control; restored)."
        % (c8(LB), len(D["pinfiles"]), ", ".join(D["pinfiles"]), D["pins"], len(checks),
           num(D["windows"]), num(D["pairs"]), num(D["triples"]), num(D["off"][0]), num(D["off"][1]), num(D["drive"][0]), num(D["drive"][1]),
           num(D["loc"][0]), num(D["stcases"]), num(D["r3"][0]),
           num(n5[3]), num(n5[11]), num(n5[12]), num(n5[13]), num(7050), c8(FZ), D["smallest"][0], D["smallest"][1], c8(LB),
           qn("CHK", "red-b check PASS"), qn("CHK", "red-b: data/b6b fixes3 SHA1SUMS mismatch"), qn("CHK", "red-b check FAILED")))
    must(n5[3] == 9 and n5[11] == 2049 and n5[12] == 4097 and n5[13] == 8193, "N5 iteration counts")

    # ---- DATA counters for the cited replays
    bullet(
        "- DATA counters for the replays the line cites, named here from their own reports (L43; cited, not re-run). L-COMP 22 BOX 48 (%s at "
        "claude/l-comp %s): the model, %s; N5, %s; the winners, %s; its own reading: %s. L-RED 70 R245 (%s at claude/l-red %s): %s; its limit: %s; "
        "it also carries N5 at k = 9 and k = 10 in two addenda (the line names k = 3 … 8 only). REFEREE 35's pre-check (%s): %s. REFEREE 36 (stage "
        "1): the model %s; N5 %s. REFEREE-2 41 (its §3.2-§3.4): counters tfail, stopfail, swfail, totfail 0 for k = 3..16 and idfail 0 for k ≤ 12; N5 on its "
        "own engine with four solvers (its counters red, zl, zh, oink-zlk, oink-tl, lane, all 0 for k = 3..11): %s."
        % (cfg["replays"]["box48_path"], c8(H["l-comp"]),
           q("BOX48", "C port: T_key = 2^k − 2 exactly for k = 3..20 (1,048,574 at k = 20, N + M 492)"),
           q("BOX48", "N5 on Γ3(G_k), k = 3..12 (n = 135k − 230 = 175 … 1,390): n5b spec 2^k + 1 iterations, 1 fallback; n5v spec the same (engdiff "
                      "0), first fallback at step 2^k − 2; wrong 0, verr 0; controls fire"),
           q("BOX48", "Oink --tl and --zlk: verified, winners = n5b's (owrong 0) for k = 3..12; control fires"),
           q("BOX48", "Whether this is a kill of N5 rests on the referees' reading of R117 and of the family's general-k proof (L-RED-B's P-N5-EXP), "
                      "not on this box."),
           cfg["replays"]["r245_path"], c8(H["l-red"]),
           q("R245", "All rows as claimed (script line «ALL ROWS AS CLAIMED»): FL run 2^k − 2, first fallback at 2^k − 1, 2^k + 1 iterations, one "
                     "fallback, every counter 0"),
           q("R245", "**What this file does NOT establish: T_key = 2^k − 2 for every k (data to k = 12; the induction proof is owed elsewhere); N5 "
                     "beyond k = 8; an independent Γ3 builder.**"),
           c8(cfg["referee"]["precheck_commit"]),
           q("PRE", "every k run (§4's table: k = 3..9 and the long runs listed there): 2^k + 1 iterations, exactly one fallback, at transition "
                    "2^k − 1; states 0..L are the standard states of the IDEAL run; every winner equals Zielonka's; 7 named counters 0; firing "
                    "control for STD and FLFB"),
           q("REF1", "run: k 3..14; L 6 14 30 62 126 254 510 1022 2046 4094 8190 16382; Lform 0 stopform 0 swk 0 maxform 0 sumform 0 nochange 0"),
           q("REF1", "n5: G_3 G_4 G_5 G_6 G_7 G_8 G_9; iterations 9 17 33 65 129 257 513; S3START 0 STD 0 FLFB 0 FLTAU 0 FLSIG 0 LASTFB 0 WIN 0 EXACT "
                     "0 PG 0; PG compared on 7 games"),
           q("REF2", "So on k = 3..11: the first fallback is transition 2^k − 1 (as REACH3 says: L(G) + 1), N5 makes 2^k + 1 iterations, and its "
                     "answer is right.")))

    # ---- Note: every item of both referees
    bullet(
        "- Note (every item of both referees and of the pre-check, and how each was closed). REFEREE 36's items (its §9 table, %s): E-1 ((H2) "
        "vacuous after the stop; the frozen lemma false at (j, a, t) = (1, 1, 2^k − 1)), E-2 (the induction uses the lemma for j + 1 before its "
        "hypothesis holds), E-4 (the standing assumption needs u_0 at option 0), E-5 (STABLE: key bit of the step) → fixes entry 4; REFEREE stage "
        "4: %s, %s, %s, %s. E-3 (rank key not injective on wire options; tie rule by β-id) → 5.1, E-6 (the placeholder of §9.7) → 5.3, E-7 "
        "(@@CORRECT@@: DATA or R57 (b)) and P-1 (R117's premises in the Corollary and the dead-end sentence) → entry 2, O-1 (optional: R124 for the "
        "exact count) → entry 3; REFEREE stage 5a: %s, %s, %s, %s. O-2 and N-1 (notes) → recorded in 5.9, no change. Stage 5a's own notes N-5a "
        "(a line range in fixes entry 2 (d) off by one), N-5b (the parenthesis of 5.1; the same point as REFEREE-2's F-3, read in fixes 7.3), N-5c "
        "(a count of quotes), N-5d (a remark on Remark 2): %s. The pre-check's items (REFEREE 35): P-1 as above; P-2 (level width) → 5.4, M-1 "
        "(genome of record and raw files) → 5.5, M-2 (mover order) → 5.6, M-3 (JSON fields) → 5.7 (%s); P-3 (scope of a kill: N5 as specified) and "
        "P-4 (L43: the proof for every k) are met by the packet's @@NOTCLAIMED@@ and by Theorem EXP-IDEAL. REFEREE-2's items: G-1 (= E-2) → entry 4, "
        "%s; M-1 (= E-3) %s; W-1 (@@STEPT@@) %s; W-2 (= P-1) %s; D-1 (= E-6) %s; O-1 (its own Γ3 builder numbers the β block in gate order: about "
        "its tool, not the packet); Addendum 1 A1.1 (the exact count) → entry 3 and A1.2 (the runner erratum) %s; its self-correction §A2.1 (%s). "
        "Its items on the fixes file, F-1 (a reading: (R3)'s range, the one condition of its signature), F-2 and F-3 (wording), F-4 (the new "
        "runner exits 0 on a failing stage; %s), F-5 (a label inside (a′); no change asked) → fixes entry 7 (7.1-7.5), which neither referee has "
        "checked yet. Its line notes L-a, L-b, L-c on L-1 → line L-2 (fixes 7.6). Agreement of the two reviews (REFEREE-2 Addendum 3): %s; on "
        "what was open between them: %s. Its three wording items S-1, S-2, S-3 concern box 108, which is not part of this entry."
        % (l("REF1", "| E-1 | §6 l. 194, 196 |") + " to " + l("REF1", "| N-1 | §1 |").replace("l. ", ""),
           qn("REF1", "**E-1 CLOSED.**"), qn("REF1", "**E-2 CLOSED.**"), qn("REF1", "**E-4 CLOSED.**"),
           qn("REF1", "**E-5 CLOSED.**") + " (" + l("REF1", "**E-4 CLOSED.**") + " to " + l("REF1", "**E-2 CLOSED.**").replace("l. ", "") + ")",
           qn("REF1", "**E-3 closed.**"), qn("REF1", "**E-6 closed.**"), qn("REF1", "**P-1 closed.**") + ", " + qn("REF1", "**E-7 closed.**"),
           qn("REF1", "**O-1 closed.**") + " (" + l("REF1", "### 13.2 Entry 2 (l. 150-244), paragraph by paragraph") + " to "
           + l("REF1", "**E-6 closed.**").replace("l. ", "") + ")",
           q("REF1", "### 13.7 Notes (no statement affected; the lane may take them into a later entry)"),
           q("REF1", "the pre-check items P-2, M-1, M-2, M-3 are answered with the right numbers"),
           q("REF2", "G-1 **closed**."),
           q("REF2", "**M-1 → 5.1: closed.**"), q("REF2", "**W-1 → 5.2 and 4.1 (S2): closed.**"), q("REF2", "**W-2 and §4 → entry 2: closed.**"),
           q("REF2", "**D-1 → 5.3: closed.**"), q("REF2", "**Addendum 1 A1.2 → entry 1, 10.E: closed**"),
           q("REF2", "That row was wrong about the STATEMENT."),
           q("REF2", "No DATA is affected"),
           q("REF2", "the same gap (E-2 = G-1) and the same rank tie (E-3 = M-1), placeholder (E-6 = D-1) and condition (P-1 = W-2) were found "
                     "independently; E-1, E-4, E-5, E-7 are REFEREE 36's alone"),
           q("REF2", "Nothing that touches a statement.")))

    # ---- Signatures
    def stg(bl, stages):
        return ", ".join("%s %s (%s %s)" % (n, rng(bl, c), c8(c), cdate(c)) for n, c in stages)

    bullet(
        "- Signatures: REFEREE %s at claude/referee %s (%s lines, sha1 %s): successor 36 wrote stages 1-4, successor 37 stage 5a: %s; the pre-check "
        "%s is successor 35's (%s; not a signature). Its signature, the last line of the file: %s; on the restated lemma %s. %s "
        "REFEREE-2 %s at claude/referee-2 %s (%s lines, sha1 %s): successor 41 wrote the report and Addendum 1, successor 42 Addenda 2 and 3: %s. "
        "Its signature: %s, with the L41 signature quoted above (%s), and on the first referee's text %s. %s "
        "Lane (claude/l-red-b): L-RED-B successor 5 (%s packet FROZEN; %s fixes entry 1), successor 6 (%s entries 2-5 and line L-1; %s entry 6), "
        "successor 7 (%s entry 7 and line L-2; %s entry 8 and line L-3). CHECKER: %s, the token in the title."
        % (cfg["referee"]["path"], c8(H["referee"]), num(len(ref1.lines)), ref1.sha1, stg(r1bl, cfg["referee"]["stages"]),
           cfg["referee"]["precheck_path"], c8(cfg["referee"]["precheck_commit"]),
           q("REF1", "**P-N5-EXP: SIGNED with fixes entries 1-6.**", 2),
           q("REF1", "**SIGNED** (§12; referee-originated, L41: it also needs REFEREE-2's independent signature)"),
           slot("stage5b", "REFEREE stage 5b %s (its §14: the line of record word by word, fixes entries 7 to 9, and its final signature line "
                           "naming the line by its sha1; stage 5a ends %s)." % (OPEN_WORD, q("REF1", "Stage 5b (line L-2, entry 7) waits for the commit."))),
           cfg["referee2"]["path"], c8(H["referee-2"]), num(len(ref2.lines)), ref2.sha1, stg(r2bl, cfg["referee2"]["stages"]),
           q("REF2", "P-N5-EXP: SIGNED with fixes entries 1-5.", 2),
           l("REF2", "Signature (L41: the statements 4.3 and 4.4 are referee-originated, REFEREE 36's; this is the independent second signature):"),
           q("REF2", "LEMMA′ and CAUSAL in entry 4 are REFEREE 36's text word for word: L41 is met."),
           slot("r2_line", "REFEREE-2 line check %s (its check of the line of record; its signature stands on fixes entries 1-5, and entries 6 to "
                           "%d and the lines after L-1 are later than its Addendum 3)." % (OPEN_WORD, nent)),
           c8(FZ), c8(fx["entry1_commit"]), c8(fx["entries2_5_commit"]), c8(fx["entry6_commit"]), c8(fx["entry7_commit"]), c8(fx["entry8_commit"]),
           CN))

    # ---- INDEPENDENCE
    bullet(
        "- INDEPENDENCE: each referee wrote its verdict without reading the other's. REFEREE: %s; stage 4 %s; stage 5a %s. REFEREE-2: %s; "
        "Addendum 2 %s; it opened the first referee's files only for Addendum 3: %s, and %s. The same gap was found twice: %s. Disclosed: the "
        "first referee's lane wrote the pre-check (%s); the restated lemma is the first referee's own text, signed by its author and, "
        "independently, by REFEREE-2 (L41, above); when REFEREE-2 signed it, what it knew of the first report was what the fixes file quotes (%s). "
        "Each referee used its own generator, model and N5 engine: REFEREE %s; REFEREE-2 %s."
        % (q("REF1", "Independence: REFEREE-2's reports and L-SI's box 108 (an independent proof of L(G_k) = 2^k − 2) were NOT read before §0-§9 "
                     "were committed."),
           q("REF1", "NOT read: docs/referee-2/ (the strings entry 4 quotes from it were matched by script only)"),
           q("REF1", "Independence: docs/referee-2/ was NOT read."),
           q("REF2", "Independence: docs/referee/ and notes/REFEREE.md were NOT read on this object"),
           q("REF2", "Independence: docs/referee/R-P-N5-EXP.md and docs/referee/R-GK-precheck.md were NOT opened before this addendum was committed."),
           q("REF2", "Written after Addendum 2 was committed (f17a2708, 17:02:13Z) and its SHA sent to the Lead (17:03Z); only then were the first "
                     "referee's files opened."),
           q("REF2", "neither report cites the other"),
           q("REF2", "the SAME gap, found independently, with the same repair (LEMMA′ / PREFIX FORM; §A2.4: one lemma)"),
           q("REF1", "This lane's pre-check (successor 35, docs/referee/R-GK-precheck.md at 06ac891d) is prior work of this lane; it had not read "
                     "the packet."),
           q("REF2", "What I know of the first referee's report is what entries 2-5 quote from it (22 tagged quotes; 5 of the pre-check)."),
           q("REF1", "the lane's gk.py, onep.py, b6*.py are not imported"),
           q("REF2", "No lane tool was imported by my checkers")))

    # ---- TARGET.md diff
    bullet(
        "- TARGET.md diff: TARGET.md §2 (M4) asks for %s; this entry claims no algorithm and no bound. It records that one candidate, N5 from S3, "
        "fails gauntlet step 4, the running-time half (TARGET.md §5: %s; CLAUDE.md: %s): through R117 as landed, its number of iterations on "
        "Γ3(G_k) is at least 2^k − 1 on an input of n + m = 311k − 530 vertices and edges, and each iteration costs at least one step in TARGET.md "
        "§3's cost model (%s; the packet: %s), so the bound is a LOWER bound on steps and needs no bit-cost argument (REFEREE-2: %s). The games are "
        "TARGET.md §1 games as they stand (REFEREE: %s, largest priority 4M + 9 ≤ n; REFEREE-2: %s). Referees: REFEREE %s; REFEREE-2 %s. It is not "
        "M3 and not M4 progress, not a TARGET.md claim and not a step-4 pass for any candidate: the question of TARGET.md stays open, in the line's "
        "words %s."
        % (q("TARGET", "There is a deterministic algorithm A and a polynomial p such that for every parity game G, A on input G halts within p(n + "
                       "m) steps and outputs the pair (W_E(G), W_O(G))."),
           q("TARGET", "4. Written correctness and running-time proofs, double-refereed with every gap listed."),
           q("CLAUDE", "Every algorithm claim runs the gauntlet in TARGET.md section 5. Failing any step makes it a dead end."),
           q("TARGET", "Word RAM with words of O(log(n + m)) bits"),
           q("PKT", "an iteration costs at least one step"),
           q("REF2", "it needs no bit-cost argument because it is a LOWER bound on steps"),
           q("REF1", "The Corollary's games are TARGET §1 games as they stand"),
           q("REF2", "so no parameter is being held small"),
           q("REF1", "«Not claimed» matches TARGET §2: the target stays open."),
           q("REF2", "No statement of the packet goes beyond TARGET.md."),
           qn("LINE", "TARGET.md §2 (M4) stays OPEN; not M3 or M4, not a TARGET.md claim")))

    # ---- Status
    op = anyopen()
    bullet(
        "- Status: DEAD END for the candidate N5 (SPEC S1-S5 with FIX 1-4, from its default start S3) as an M4 candidate: failure of gauntlet "
        "step 4 (running time), PROVED-CONDITIONAL on RESULTS R117 as landed, on the unconditional Theorem EXP-IDEAL. Obstruction RIPPLE, in the "
        "line's words: %s. The instance that kills it is the family Γ3(G_k), k ≥ 3, by the proof (frozen files for k = 3..13; the smallest has %d "
        "vertices, %d edges and 9 iterations); no single measured game exceeds n². GAPS G-N5-TIME is answered NO for N5 from S3 (through RESULTS "
        "R117 as landed, refereed-only): at landing its row takes this entry's UPDATE, its status becomes \"closed\" and it moves under the Closed "
        "table (Lead rulings G-U, G-S). No landed entry is changed: R117 and R124 are used as landed.%s"
        % (qn("LINE", "obstruction RIPPLE (S4a's root-first key rule refuses an improving switch until the key order allows it, and on Γ3(G_k) this "
                      "makes unit j + 1 respond twice in every response of unit j)"),
           D["smallest"][0], D["smallest"][1],
           (" Open slots of this fill, each marked by its word above: %s; and the checker token in the title." % ", ".join(
               {"stage5b": "REFEREE stage 5b", "r2_line": "REFEREE-2's line check", "entry9": "fixes entry 9", "line": "the line of record " + LN["of_record_name"]}[x]
               for x in op)) if op else ""))

    block = [title]
    for first, rest, text in P:
        block.extend(wrap(text, first, rest))

    # ================================================================ the UPDATE
    F.part = "proposal"
    upd = updlib.r131_update(cfg, line)
    for _, _, inner in gspans(upd):
        o = S["LINE"].find(inner)
        must(o, "a quotation of the UPDATE is not in the line")
        F._add("line", "LINE", inner, o[0] if o else (0, 0), len(o))
    for _, _, inner in gspans(title):
        o = S["LINE"].find(inner)
        F._add("line", "LINE", inner, o[0] if o else (0, 0), len(o))
    u = cfg["update"]
    prop = (
        "Proposed GAPS %s UPDATE (append-only), to go AFTER the last UPDATE on the row %s (GAPS l. %d at trunk %s; its "
        "last UPDATE is %s's, %s), as a pure insertion with one separating space before the row's closing pipe. BUILT FROM THE LINE %s by "
        "tools/upd.py (updlib.build, the landed procedure made generic: the same function rebuilds the landed UPDATEs of R128, R129, R130 byte for "
        "byte from their landed titles; four negative controls refuse; Addendum [upd]): the three labels %s, %s, %s are moved behind their "
        "clauses; the scope words %s are dropped (the landed drop of %s); the line's final full stop is stripped before the ending; no pipe pair is "
        "needed (the line has no pipe). Lead ruling G-U (%s): the UPDATE ends with the sentence %s. Lead ruling G-S (same log line): %s; "
        "land131.py therefore sets the status cell of the row to \"closed\" and moves the whole row under the table of %s (GAPS l. %d), as its last "
        "row. sha1 %s of the line below without its newline and unfilled, %d bytes, %d opening and %d closing parentheses, 0 pipe characters. "
        "<DATE>, <HH:MM> and <checker> are the landing date, time and the CHECKER commit of the PASS (%s), all filled at landing:"
        % (cfg["gaps"]["row_id"], cfg["gaps"]["row_id"], grow[0], c8(T),
           PREV, q("GAPS", "UPDATE 2026-11-13 10:06Z: RESULTS R130 (P-N5-WRAP; CHECKER C146 26e9d73c) [refereed-only] LANDED:"),
           LN["name"], qn("LINE", u["labels"][0]["label"]), qn("LINE", u["labels"][1]["label"]), qn("LINE", u["labels"][2]["label"]),
           qn("LINE", u["drops"][0]), PREV,
           l("LEAD", "LEAD RULINGS for the landing: G-S:").replace("l. ", "docs/agents/LEAD-STATE.md l. "),
           qn("LEAD", u["ending"]),
           qn("LEAD", "the status cell of GAPS G-N5-TIME becomes «closed» and the row moves to «## Closed» (check_docs accepts only open / "
                      "in-progress / closed; the gap's question is answered NO)"),
           qn("GAPS", "## Closed"), closed[0], line_sha1(upd), len(upd.encode("utf-8")), upd.count("("), upd.count(")"), CN))
    must(len(u["labels"]) == 3 and len(u["drops"]) == 1, "the proposal paragraph is written for three labels and one drop")
    prop_lines = wrap(prop, "", "", 140)

    # ================================================================ the header
    F.part = "header"
    Hd = []

    def hp(text):
        Hd.extend(wrap(text, "", "  ", 140))

    line1 = (
        "# Draft RESULTS %s (Lead; FIRST FILL by script (subagent) on %s line %s%s, %s, claude/l-red-b %s, sha1 %s) — to CHECKER %s — NOT LANDED; "
        "goes after %s (RESULTS l. %d at trunk %s), directly before the line-start %s (l. %d); its GAPS UPDATE on the row %s (GAPS l. %d), which "
        "then moves under %s"
        % (E, PK, LN["name"], (" (a STAND-IN for the line of record %s)" % LN["of_record_name"]) if LN["stand_in"] else "", LN["path"],
           c8(LN["commit"]), sha1(line_raw), CN, PREV, heads[PREV], c8(T), qn("RES", cfg["results"]["insert_before_prefix"]), err_lines[0],
           cfg["gaps"]["row_id"], grow[0], qn("GAPS", "## Closed", 1)))
    hp("FIRST FILL (this text). Built by script in docs/agents/tools/r131/ (cfg.json: every input that can move; fetch.sh: the only network step; "
       "fill131.py; tools/*.py, tools/lanecheck.sh; build.sh; land131.py), untracked; nothing in the repository was added, committed, merged or "
       "pushed by the builder, and scripts/push.sh and scripts/verify.sh were not run. Read by git show at the heads of the fetch that fetch.txt "
       "records (%s, by date -u; git ls-remote lines in the Addendum): claude/l-red-b %s, claude/referee %s, claude/referee-2 %s, claude/l-si %s, "
       "claude/l-comp %s, claude/l-red %s, trunk %s %s."
       % (fdate, H["l-red-b"], H["referee"], H["referee-2"], H["l-si"], H["l-comp"], H["l-red"], cfg["trunk"]["branch"], T))
    hp("TRUNK: %s (%s). docs/RESULTS.md sha1 %s, %s lines, %d entries, last heading %s at l. %d, Erratum anchor l. %d; docs/GAPS.md sha1 %s, %d "
       "lines, row %s l. %d (status %s), Closed heading l. %d; TARGET.md sha1 %s. land131.py works on the working tree and checks these anchors, "
       "not these sha1s."
       % (c8(T), cdate(T), RES.sha1, num(len(RES.lines)), len(heads), PREV, heads[PREV], err_lines[0], GAPS.sha1, len(GAPS.lines),
          cfg["gaps"]["row_id"], grow[0], cfg["gaps"]["status_from"], closed[0], S["TARGET"].sha1))
    hp("LINE: %s, %s at claude/l-red-b %s (%s; %s), sha1 %s, %s bytes, one line, parentheses %d / %d, pipes 0.%s"
       % (LN["name"], LN["path"], c8(LN["commit"]), cdate(LN["commit"]), csubject(LN["commit"])[:70] + " …", sha1(line_raw), num(len(line_raw)),
          line.count("("), line.count(")"),
          (" STAND-IN: the line of record will be %s (not on origin at the fetch); the second run changes cfg.json only (REPORT.txt)."
           % LN["of_record_name"]) if LN["stand_in"] else ""))
    hp("PACKET: %s FROZEN at %s (%s), sha1 %s, %s lines, %s bytes; byte-equal at %s. FIXES: %s at %s, %s lines, sha1 %s, entries 1-%d."
       % (cfg["packet"]["path"], c8(FZ), cdate(FZ), pkt.sha1, num(len(pkt.lines)), num(len(pkt.raw)), c8(LB), fx["path"], c8(LB),
          num(len(fix.lines)), fix.sha1, nent))
    hp("REFEREES (git blame at the heads). REFEREE %s at %s (%s lines): %s. REFEREE-2 %s at %s (%s lines): %s; %s (%s lines). Box 108: %s at "
       "claude/l-si %s."
       % (cfg["referee"]["path"], c8(H["referee"]), num(len(ref1.lines)), stg(r1bl, cfg["referee"]["stages"]), cfg["referee2"]["path"],
          c8(H["referee-2"]), num(len(ref2.lines)), stg(r2bl, cfg["referee2"]["stages"]), cfg["referee2"]["box108_path"], num(len(S["R2B"].lines)),
          cfg["box108"]["path"], c8(cfg["box108"]["commit"])))
    op_txt = []
    if LN["stand_in"]:
        op_txt.append("the line of record %s (%s: stand-in %s)" % (LN["of_record_name"], OPEN_WORD, LN["name"]))
    if slots["entry9"]["open"]:
        op_txt.append("fixes entry 9 (%s)" % OPEN_WORD)
    if slots["stage5b"]["open"]:
        op_txt.append("REFEREE stage 5b (%s)" % OPEN_WORD)
    if slots["r2_line"]["open"]:
        op_txt.append("REFEREE-2's line check (%s)" % OPEN_WORD)
    hp("OPEN SLOTS: %s the checker token of the title. land131.py refuses to land while the draft holds the open-slot word anywhere but in that "
       "token." % (("; ".join(op_txt) + "; and") if op_txt else "none but"))
    hp("CHECKS RUN AT THIS FILL (outputs verbatim in the Addendum): [lane] the lane's check.sh in a git archive with a negative control; [upd] "
       "the UPDATE builder with controls R128-R130 and five negative controls; [data] %d DATA checks from the pinned outputs with a negative "
       "control; [prem] the premise entries at trunk; [shape] title, block, UPDATE, pipes, brackets, open-slot tokens, check_docs on a copy with a "
       "negative control; [lp] every quotation at its commit, file and lines, by a second implementation, with two negative controls; [sweep] "
       "every guillemet quotation of the file against the sources, with a negative control; [land] land131.py: refusal on this draft, refusal on a "
       "changed block, DRYRUN on a copy." % len(checks))
    hp("FLAGS FIRST (the builder's reading; nothing in the line or in any quoted text was changed; full list in REPORT.txt). G-LINE: the title "
       "stands on %s%s. G-SLOTS: no referee has yet checked fixes entries 7 and 8 or any line after L-1; REFEREE-2's signature names entries 1-5, "
       "REFEREE's 1-6, the line's closing parenthesis names %s. G-K12 (wording inside the line): its correctness clause says \"DATA for k ≤ 12\" "
       "while its part (3) and REFEREE's table (stage 5a) have k = 13. G-R245 (note): the line gives L-RED 70's engine for k = 3 … 8; R245 also "
       "carries k = 9, 10. G-STATUS (note): the line keeps its status phrase about two referees (Lead ruling, the form of %s). G-U: the UPDATE "
       "moves three labels, drops one scope string and keeps everything else, the obstruction clause and the L41 scope tail included. G-S: the "
       "Closed table of GAPS has an empty line inside it; the row is appended after its last row. G-NOW: land131.py changes one counter of "
       "docs/NOW.md; %s's landing changed two. G-1E-N3: the N5 half is conditional on R117 as landed and on SPEC's standing premise. G-5E: the "
       "first referee's stage 5a has four notes, N-5a to N-5d."
       % (LN["name"], (", a stand-in for %s" % LN["of_record_name"]) if LN["stand_in"] else "", line_entries, PREV, PREV))

    # ================================================================ assemble pass 1
    draft = [line1] + Hd + [""] + block + [""] + prop_lines + [upd] + [""]
    text = "\n".join(draft)
    if ERR:
        for e in ERR[:60]:
            print("fill131 ERROR:", e[:300])
        print("fill131: %d errors; nothing written" % len(ERR))
        return 1
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "draft.p1.md"), "w", encoding="utf-8") as f:
        f.write(text)
    with open(os.path.join(OUT, "ledger.json"), "w", encoding="utf-8") as f:
        json.dump(F.ledger, f, ensure_ascii=False, indent=1)
    hashes = {
        "entry": E, "line_name": LN["name"], "line_sha1": sha1(line_raw), "line_stand_in": LN["stand_in"],
        "title_sha1": line_sha1(title), "block_lines": len(block), "block_sha1": block_sha1(block),
        "update_sha1": line_sha1(upd), "update_bytes": len(upd.encode("utf-8")),
        "open_tokens_block": sum(x.count(OPEN_WORD) for x in block), "checker_number": CN,
    }
    with open(os.path.join(OUT, "hashes.json"), "w", encoding="utf-8") as f:
        json.dump(hashes, f, indent=1)
        f.write("\n")
    nq = sum(1 for x in F.ledger if x["form"] in ("q", "qn"))
    print("fill131: pass-1 draft %d lines; block %d lines (sha1 %s); UPDATE sha1 %s; quotations %d, located passages %d, line-internal %d; "
          "open-slot tokens in the block %d" % (len(draft), len(block), hashes["block_sha1"], hashes["update_sha1"], nq,
                                                sum(1 for x in F.ledger if x["form"] == "l"), sum(1 for x in F.ledger if x["form"] == "line"),
                                                hashes["open_tokens_block"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
