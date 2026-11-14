#!/usr/bin/env python3
"""tools/shape.py <draft>: the shape of the draft: title = '### R131 [refereed-only] ' + the line (bytes of git) +
the checker token; 0 pipes and balanced brackets in the title; the block (no empty line, bullet lines, width); the
UPDATE rebuilt by updlib from the line; open-slot tokens; the recorded hashes. The open-slot word is never printed.
Exit 1 on any failure."""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
import updlib
from lib131 import OPEN_WORD, block_sha1, line_sha1, load_cfg, sha1, short, show, split_draft


def main(path):
    cfg = load_cfg()
    text = open(path, encoding="utf-8").read()
    d = split_draft(text, cfg)
    E, CN = cfg["entry"], cfg["checker_number"]
    raw = show(cfg["line"]["commit"], cfg["line"]["path"])
    line = raw.decode("utf-8")[:-1]
    title = d["block"][0]
    fails = 0

    def chk(name, ok, detail=""):
        nonlocal fails
        print("%s %s%s" % ("OK  " if ok else "FAIL", name, (": " + detail) if detail else ""))
        fails += not ok

    token = ", CHECKER PASS (docs/checker/%s.md, checker %s)" % (CN, OPEN_WORD)
    chk("title = heading + the line (git bytes, %d bytes, sha1 %s) + the checker token" % (len(raw), sha1(raw)),
        title == "### %s [refereed-only] " % E + line + token and raw.endswith(b"\n") and raw.count(b"\n") == 1,
        "line %s of %s @ %s" % (cfg["line"]["name"], cfg["line"]["path"], short(cfg["line"]["commit"])))
    chk("title: pipe characters %d" % title.count("|"), title.count("|") == 0)
    chk("title: parentheses %d / %d, square brackets %d / %d, guillemets %d / %d" % (title.count("("), title.count(")"), title.count("["), title.count("]"),
                                                                                     title.count("«"), title.count("»")),
        title.count("(") == title.count(")") and title.count("[") == title.count("]") and title.count("«") == title.count("»"))
    chk("title passes the label rule of scripts/check_docs.py", bool(re.search(r"\[(formalized|refereed-only)\]", title)))
    chk("negative control: the title without its label fails that rule", not re.search(r"\[(formalized|refereed-only)\]", title.replace("[refereed-only] ", "")))
    blk = d["block"]
    wid = max(len(x) for x in blk[1:])
    chk("block: %d lines (title + %d), no empty line, every line a bullet or a continuation, widest %d" % (len(blk), len(blk) - 1, wid),
        all(x.startswith("- ") or x.startswith("  ") for x in blk[1:]) and wid <= 140 and all(x == x.rstrip() for x in blk))
    bullets = [x[2:x.index(":") if ":" in x[:60] else 30].split(" (")[0] for x in blk if x.startswith("- ")]
    print("     bullets: " + "; ".join(b[:34] for b in bullets))
    chk("block: pipe characters %d, tabs %d" % (sum(x.count("|") for x in blk), sum(x.count("\t") for x in blk)),
        sum(x.count("|") for x in blk) == 0 and sum(x.count("\t") for x in blk) == 0)
    nb, nd = sum(x.count(OPEN_WORD) for x in blk), text.count(OPEN_WORD)
    chk("open-slot tokens: block %d (the title's checker token 1, other %d); whole draft %d" % (nb, nb - 1, nd), title.count(OPEN_WORD) == 1)
    print("     landable by this count: %s" % ("yes" if nd == 1 else "no (open slots)"))
    upd = d["update"]
    try:
        want = updlib.r131_update(cfg, line)
    except updlib.Refuse as e:
        want = "refused: %s" % e
    chk("UPDATE line = updlib.r131_update(the line): %d bytes, sha1 %s" % (len(upd.encode("utf-8")), line_sha1(upd)), upd == want)
    chk("UPDATE: pipes %d, parentheses %d / %d, fill tokens %d %d %d, ends with the ruled sentence" % (
        upd.count("|"), upd.count("("), upd.count(")"), upd.count("<DATE>"), upd.count("<HH:MM>"), upd.count("<checker>")),
        upd.count("|") == 0 and upd.count("(") == upd.count(")") and upd.count("<DATE>") == upd.count("<HH:MM>") == upd.count("<checker>") == 1
        and upd.endswith(". " + cfg["update"]["ending"]))
    h = json.load(open(os.path.join(HERE, "out", "hashes.json"), encoding="utf-8"))
    chk("recorded hashes (out/hashes.json): block sha1 %s (%d lines), UPDATE sha1 %s" % (h["block_sha1"], h["block_lines"], h["update_sha1"]),
        h["block_sha1"] == block_sha1(blk) and h["block_lines"] == len(blk) and h["update_sha1"] == line_sha1(upd))
    L = d["lines"]
    chk("first line starts '# Draft RESULTS %s ' and is not marked landed" % E, L[0].startswith("# Draft RESULTS %s " % E) and "LANDED in RESULTS" not in L[0])
    chk("layout: block at lines %d-%d, empty line %d, proposal %d-%d, UPDATE line %d" % (d["b0"] + 1, d["b1"], d["b1"] + 1, d["p0"] + 1, d["u0"], d["u0"] + 1),
        L[d["b1"]] == "" and L[d["u0"] + 1] == "")
    print("shape: %s" % ("PASS" if fails == 0 else "FAILED"))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
