#!/usr/bin/env python3
"""tools/upd.py: the R131 GAPS UPDATE from the line of record, with controls.

Controls (positive): updlib.build rebuilds the LANDED UPDATEs of R128, R129, R130 byte for byte from their landed
titles (RESULTS and GAPS at the trunk commit of cfg.json). Negative controls: an altered drop string, an altered
label, an altered clause end and an altered pipe string are refused; one changed byte of the line changes the UPDATE.
Exit 1 on any failure. Prints no line longer than 200 characters.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import copy

import updlib
from lib131 import line_sha1, load_cfg, sha1, short, show

CONTROLS = {
    128: {"boundary": "date", "drops": ["; G-N5-TIME stays OPEN; not a step-4 pass, not a TARGET.md claim"], "pairs": []},
    129: {"boundary": "date", "drops": ["; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim"], "pairs": []},
    130: {"boundary": "; obstruction W-FLAT (", "drops": ["; G-N5-TIME stays OPEN", "; not M3 or M4, not a TARGET.md claim"],
          "pairs": [("(F ≤ m_E − |V_E| + 1 under [RULE])", "(F ≤ m_E − (the number of Even vertices of H) + 1 under [RULE])"),
                    ("so 2^Ω(√|V|):", "so 2^Ω(√(the number of vertices)):"),
                    (", |V| = 10.5n² + 152.5n + 48", ", the number of vertices = 10.5n² + 152.5n + 48")]},
}


def landed(cfg):
    t = cfg["trunk"]["commit"]
    R = show(t, "docs/RESULTS.md").decode("utf-8").split("\n")
    G = show(t, "docs/GAPS.md").decode("utf-8").split("\n")
    row = [l for l in G if l.startswith("| %s | " % cfg["gaps"]["row_id"])]
    assert len(row) == 1
    row = row[0]
    starts = [(m.start(), int(m.group(1))) for m in re.finditer(r"UPDATE \d{4}-\d\d-\d\d \d\d:\d\dZ: RESULTS R(\d+) ", row)]
    seg = {}
    for i, (s, n) in enumerate(starts):
        e = starts[i + 1][0] if i + 1 < len(starts) else len(row) - 1
        seg[n] = row[s:e].rstrip(" ")
    return R, seg


def control(n, R, seg):
    title = [l for l in R if l.startswith("### R%d [refereed-only] " % n)]
    assert len(title) == 1
    m = re.match(r"### R%d \[refereed-only\] (.*), CHECKER PASS \(docs/checker/(C\d+)\.md, checker ([0-9a-f]+)\)$" % n, title[0])
    stmt, cnum, csha = m.group(1), m.group(2), m.group(3)
    upd = seg[n]
    pm = re.match(r"(UPDATE \d{4}-\d\d-\d\d \d\d:\d\dZ: RESULTS R%d \(([^;]+); CHECKER (C\d+) ([0-9a-f]+)\) \[refereed-only\] LANDED: )" % n, upd)
    prefix = pm.group(1)
    assert pm.group(3) == cnum and pm.group(4) == csha
    c = CONTROLS[n]
    if c["boundary"] == "date":
        b = re.search(r" \(\d{4}-\d\d-\d\d\) — ", stmt)
        head_end, bold = b.start(), stmt[b.start():b.end()]
        brep = (bold, ": ")
    else:
        head_end = updlib.once(stmt, c["boundary"], "boundary")
        brep = (c["boundary"], ": " + c["boundary"][2:])
    items = updlib.labels_auto(stmt[:head_end])
    reps = [brep] + [(d, "") for d in c["drops"]] + list(c["pairs"])
    out = updlib.build(prefix, stmt, items, reps, "G-N5-TIME stays open.")
    return out == upd, len(items), line_sha1(upd), len(upd)


def main():
    cfg = load_cfg()
    fails = 0
    line = show(cfg["line"]["commit"], cfg["line"]["path"]).decode("utf-8")
    assert line.endswith("\n") and line.count("\n") == 1
    line = line[:-1]
    upd = updlib.r131_update(cfg, line)
    print("UPDATE of %s built from line %s (%s @ %s): %d characters, %d bytes, sha1 %s (without newline, unfilled)" % (
        cfg["entry"], cfg["line"]["name"], cfg["line"]["path"], short(cfg["line"]["commit"]), len(upd), len(upd.encode("utf-8")), line_sha1(upd)))
    print("  pipes %d ; parentheses %d / %d ; fill tokens <DATE> %d <HH:MM> %d <checker> %d" % (
        upd.count("|"), upd.count("("), upd.count(")"), upd.count("<DATE>"), upd.count("<HH:MM>"), upd.count("<checker>")))
    print("  labels moved behind their clauses: %d ; drops %d ; pipe pairs %d" % (
        len(cfg["update"]["labels"]), len(cfg["update"]["drops"]), len(cfg["update"]["pipe_pairs"])))
    print("  starts %r" % upd[:120])
    print("  ends   %r" % upd[-150:])
    ok = upd.endswith(". " + cfg["update"]["ending"]) and upd.count("<checker>") == 1 and upd.count("|") == 0
    for L in cfg["update"]["labels"]:
        ok = ok and upd.count(L["label"] + L["clause_end"]) == 1
    print("  ends with the ruled sentence, one checker token, 0 pipes, every label directly before its clause end: %s" % ok)
    fails += not ok
    # the body differs from the line only by the moves and the drops
    rest = upd[upd.index("LANDED: ") + 8:-len(". " + cfg["update"]["ending"])]
    a = sorted(rest.replace(" ", ""))
    b = line[:-1]
    for d in cfg["update"]["drops"]:
        b = b.replace(d, "")
    for o, nw in cfg["update"]["pipe_pairs"]:
        b = b.replace(o, nw)
    same = a == sorted(b.replace(" ", ""))
    print("  the body is a rearrangement of the line minus the drops (same multiset of non-space characters): %s" % same)
    fails += not same
    # positive controls
    R, seg = landed(cfg)
    for n in sorted(CONTROLS):
        try:
            eq, nl, h, ln = control(n, R, seg)
        except Exception as e:                      # noqa
            eq, nl, h, ln = False, -1, "?", -1
            print("  control R%d raised %s: %s" % (n, type(e).__name__, str(e)[:120]))
        print("control R%d: landed UPDATE rebuilt from its landed title by updlib.build: byte-equal %s (labels %d, %d characters, sha1 %s)" % (n, eq, nl, ln, h))
        fails += not eq
    # negative controls
    def refused(mut):
        c = copy.deepcopy(cfg)
        mut(c)
        try:
            updlib.r131_update(c, line)
        except updlib.Refuse:
            return True
        return False

    neg = [
        ("an altered drop string", lambda c: c["update"]["drops"].__setitem__(0, c["update"]["drops"][0].replace("M3", "M5"))),
        ("an altered label", lambda c: c["update"]["labels"][0].__setitem__("label", c["update"]["labels"][0]["label"].replace("EXP-IDEAL", "EXP-IDEAL2"))),
        ("an altered clause end", lambda c: c["update"]["labels"][1].__setitem__("clause_end", "; and, PROVED-CONDITIONAL on RESULTS R125")),
        ("an added pipe pair that is not in the line", lambda c: c["update"]["pipe_pairs"].append(["so 2^Ω(√|V|):", "x"])),
    ]
    for name, mut in neg:
        r = refused(mut)
        print("negative control, %s: refused %s" % (name, r))
        fails += not r
    i = line.index("2^k − 2")
    line2 = line[:i] + "3" + line[i + 1:]
    try:
        u2 = updlib.r131_update(cfg, line2)
        diff = u2 != upd and line_sha1(u2) != line_sha1(upd)
    except updlib.Refuse:
        diff = True
    print("negative control, one changed byte of the line: a different UPDATE %s" % diff)
    fails += not diff
    print("upd: %s" % ("PASS" if fails == 0 else "FAILED (%d)" % fails))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
