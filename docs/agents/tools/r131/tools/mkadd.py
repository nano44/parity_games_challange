#!/usr/bin/env python3
"""tools/mkadd.py: the final draft = out/draft.p1.md + the Addendum (the tools' outputs on the pass-1 draft, each
line tagged with its file and wrapped). Writes docs/agents/R131-draft.md. Pipe characters of the outputs are printed
as broken bars and guillemets as single angle marks, so the Addendum adds no pipe and no quotation to the file."""
import os
import sys
import textwrap

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
from lib131 import DRAFT, OPEN_WORD, load_cfg, sha1

FILES = [("fetch", "fetch.txt", "the record of fetch.sh (date -u, fetched heads, git ls-remote lines)"),
         ("lane", "out/lanecheck.out", "tools/lanecheck.sh: the lane's check.sh in a git archive, with a negative control"),
         ("fill", "out/fill.out", "fill131.py"),
         ("upd", "out/upd.out", "tools/upd.py: the UPDATE and its controls"),
         ("data", "out/data.out", "tools/data.py: the DATA numbers from the pinned outputs"),
         ("prem", "out/prem.out", "tools/prem.py: the premises at trunk"),
         ("shape", "out/shape.out", "tools/shape.py"),
         ("lp", "out/lp.out", "tools/lp.py: every quotation at its commit, file and lines"),
         ("sweep", "out/sweep.out", "tools/sweep.py: every guillemet quotation against the sources"),
         ("land", "out/landtest.out", "tools/landtest.py: land131.py as DRYRUN (refusals and a full dry run on a copy)")]


def main():
    cfg = load_cfg()
    p1 = open(os.path.join(HERE, "out", "draft.p1.md"), encoding="utf-8").read()
    assert p1.endswith("\n")
    n1 = p1.count("\n")
    head = ("Addendum (first fill) (built by script; for the Lead and CHECKER; does not land). The checks ran on the pass-1 draft "
            "docs/agents/tools/r131/out/draft.p1.md (sha1 %s, %d lines), which equals this file without this Addendum and its empty line (asserted "
            "by tools/mkadd.py). Outputs verbatim below, each line tagged with its file: %s. In them a pipe character is printed as a broken bar "
            "and a guillemet as a single angle mark; lines are wrapped at 150 columns (continuation lines are indented under their tag). After "
            "this file was written, tools/shape.py, tools/lp.py, tools/sweep.py and tools/landtest.py ran again on it (out/post_*.out; results in "
            "REPORT.txt). Not run: scripts/verify.sh, scripts/push.sh, the referees' own replays, Oink, Lean, any N5 engine."
            % (sha1(p1.encode("utf-8")), n1, "; ".join("[%s] %s" % (t, d) for t, _, d in FILES)))
    out = textwrap.wrap(head, 146, subsequent_indent="  ", break_long_words=False, break_on_hyphens=False)
    for tag, f, _ in FILES:
        for l in open(os.path.join(HERE, f), encoding="utf-8").read().rstrip("\n").split("\n"):
            l = l.replace("|", "¦").replace("«", "‹").replace("»", "›").replace("\t", " ").rstrip()
            assert OPEN_WORD not in l, "a tool output carries the open-slot word: %s" % f
            pre = "  [%s] " % tag
            w = textwrap.wrap(l, 150 - len(pre), subsequent_indent="    ", break_long_words=True, break_on_hyphens=False, drop_whitespace=False) or [""]
            out.extend((pre + x).rstrip() for x in w)
    final = p1 + "\n" + "\n".join(out) + "\n"
    assert final.startswith(p1) and final.split("\n")[n1] == ""
    with open(DRAFT, "w", encoding="utf-8") as fh:
        fh.write(final)
    print("mkadd: wrote docs/agents/R131-draft.md: %d lines, sha1 %s; Addendum %d lines from line %d" % (final.count("\n"), sha1(final.encode("utf-8")), len(out), n1 + 2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
