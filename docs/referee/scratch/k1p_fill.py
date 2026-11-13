#!/usr/bin/env python3
"""REFEREE successor 36: builds docs/referee/R-P-N5-KEY1P.md from k1p_report_tmpl.md and the logs of k1p_logs/.
Usage (repository root): python3 -I docs/referee/scratch/k1p_fill.py "$(date -u +%Y-%m-%dT%H:%MZ)" > docs/referee/R-P-N5-KEY1P.md
Every @@NAME@@ line of the template is replaced by the lines of k1p_summ.py's output with the prefixes below (pasted, not typed)."""
import sys, os, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import k1p_summ

PREFIX = {"MODEL": ("model, ", "  tower "), "MODELCTRL": ("model control",), "N5": ("N5 itself",), "N5CTRL": ("N5 control",), "QUOTES": ("quotes:",)}

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        k1p_summ.main()
    summ = buf.getvalue().split("\n")
    out = []
    for line in open(os.path.join(here, "k1p_report_tmpl.md"), encoding="utf-8").read().split("\n"):
        s = line.strip()
        if s.startswith("@@") and s.endswith("@@") and s[2:-2] in PREFIX:
            block = [l for l in summ if l.startswith(PREFIX[s[2:-2]])]
            assert block, f"no log lines for {s}"
            out += block
        else:
            out.append(line.replace("@@K1PDATE@@", sys.argv[1]))
    text = "\n".join(out)
    assert "@@" not in text, "unfilled placeholder"
    sys.stdout.write(text)

if __name__ == "__main__":
    main()
