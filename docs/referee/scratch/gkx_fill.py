#!/usr/bin/env python3
"""REFEREE successor 36: builds docs/referee/R-P-N5-EXP.md (stage 1) from gkx_report_tmpl.md and the logs.
Usage (repository root): python3 -I docs/referee/scratch/gkx_fill.py "$(date -u +%Y-%m-%dT%H:%MZ)" > docs/referee/R-P-N5-EXP.md
Every @@NAME@@ line of the template is replaced by the lines of gkx_summ.py's output with the prefixes below (pasted, not typed);
a missing block is an error."""
import sys, os, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gkx_summ

PREFIX = {"GEN": ("packet sha1", "gen:"), "MEMBER": ("member:", "member control"), "FACTS": ("facts, ",), "FACTSCTRL": ("facts control",),
          "CAUSAL": ("causal",), "ABS": ("abs",), "RESP": ("resp",), "RUN": ("run:",), "SIZES": ("sizes files", "first k"),
          "N5": ("n5_pg", "n5:"), "N5CTL": ("n5 control",), "LEM": ("lem ",), "ORDERS": ("orders",), "QUOTES": ("tags ", "UNTAGGED", "NOTFOUND")}

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    gkx_summ.D = os.path.join(here, "gkx_logs")          # gkx_summ reads argv[1] as a directory; here argv[1] is the date
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        gkx_summ.main()
    summ = buf.getvalue().split("\n")
    out = []
    prev = ""
    for line in open(os.path.join(here, "gkx_report_tmpl.md"), encoding="utf-8").read().split("\n"):
        s = line.strip()
        if s.startswith("@@") and s.endswith("@@") and s[2:-2] in PREFIX:
            ind = prev[:len(prev) - len(prev.lstrip())]
            block = [l for l in summ if l.startswith(PREFIX[s[2:-2]])]
            assert block, f"no log lines for {s}"
            out += [ind + l for l in block]
        else:
            out.append(line.replace("@@STAGE1@@", sys.argv[1]))
        prev = line
    text = "\n".join(out)
    assert "@@" not in text, "unfilled placeholder"
    sys.stdout.write(text)

if __name__ == "__main__":
    main()
