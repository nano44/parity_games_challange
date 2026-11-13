#!/usr/bin/env python3
"""REFEREE successor 36: builds docs/referee/R-P-N5-EXP.md (stage 1) from gkx_report_tmpl.md and the logs.
Usage (repository root): python3 -I docs/referee/scratch/gkx_fill.py "$(date -u +%Y-%m-%dT%H:%MZ)" > docs/referee/R-P-N5-EXP.md
(the argument stamps the LAST appended stage, @@NOW@@ in gkx_report_stage2.md / stage3.md; stage 1 keeps its committed stamp)
Every @@NAME@@ line of the template is replaced by the lines of gkx_summ.py's output with the prefixes below (pasted, not typed);
a missing block is an error."""
import sys, os, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gkx_summ
import gkx5_summ

PREFIX = {"GEN": ("packet sha1", "gen:"), "MEMBER": ("member:", "member control"), "FACTS": ("facts, ",), "FACTSCTRL": ("facts control",),
          "CAUSAL": ("causal",), "ABS": ("abs",), "RESP": ("resp",), "RUN": ("run:",), "SIZES": ("sizes files", "first k"),
          "N5": ("n5_pg", "n5:"), "N5CTL": ("n5 control",), "LEM": ("lem ",), "ORDERS": ("orders",), "QUOTES": ("tags ", "UNTAGGED", "NOTFOUND"),
          "PG12": ("pg12:",), "STRAT": ("strat",), "UNIT": ("unit ",), "CLOSED": ("closed",), "FIXES4": ("fixes4:",)}

STAGE1 = "2026-11-13T14:56Z"          # the date -u stamp of stage 1 as committed in c881709b (kept when later stages are appended)

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    gkx_summ.D = os.path.join(here, "gkx_logs")          # gkx_summ reads argv[1] as a directory; here argv[1] is the date
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        gkx_summ.main()
    summ = buf.getvalue().split("\n")
    out = []
    prev = ""
    tmpl = open(os.path.join(here, "gkx_report_tmpl.md"), encoding="utf-8").read()
    b5 = gkx5_summ.blocks(gkx_summ.D)          # stage 5a (successor 37): blocks of the s37_*.out logs, placeholders @@S5:NAME@@
    for extra in ("gkx_report_stage2.md", "gkx_report_stage3.md", "gkx_report_stage4.md", "gkx_report_stage5.md"):   # later stages are appended, never merged into stage 1
        p = os.path.join(here, extra)
        if os.path.exists(p):
            tmpl = tmpl.rstrip("\n") + "\n\n" + open(p, encoding="utf-8").read()
    for line in tmpl.split("\n"):
        s = line.strip()
        if s.startswith("@@") and s.endswith("@@") and s[2:-2] in PREFIX:
            ind = prev[:len(prev) - len(prev.lstrip())]
            block = [l for l in summ if l.startswith(PREFIX[s[2:-2]])]
            assert block, f"no log lines for {s}"
            out += [ind + l for l in block]
        elif s.startswith("@@S5:") and s.endswith("@@"):
            ind = prev[:len(prev) - len(prev.lstrip())]
            out += [ind + l for l in b5[s[5:-2]]]
        else:
            out.append(line.replace("@@STAGE1@@", STAGE1).replace("@@NOW@@", sys.argv[1]))
        prev = line
    text = "\n".join(out)
    assert "@@" not in text, "unfilled placeholder"
    sys.stdout.write(text)

if __name__ == "__main__":
    main()
