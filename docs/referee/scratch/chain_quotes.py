"""REFEREE successor 29: every «…» in a text (P-N5-CHAIN §1, or its line), searched verbatim (fragments split at '…', wrapped lines joined
by one space) in: trunk (REV) docs/RESULTS.md, docs/new/P-N5-XICYC.md, docs/new/P-N5-REACH.md, docs/new/N5-ssi-global.md; lane objects
P-N5-END.md @131b4c1c, P-N5-ASC.md @e28e962d, P-N5-QUIET.md and its fixes and line L-2 @559cdffc; and the packet itself (self-quotes).
Usage: chain_quotes.py REV TEXTFILE [SECTION_START SECTION_END] PACKETREV"""
import sys, re, subprocess
rev, f = sys.argv[1], sys.argv[2]; T = open(f, encoding="utf-8").read(); prev = sys.argv[-1]
if len(sys.argv) == 6: T = T[T.index(sys.argv[3]):T.index(sys.argv[4])]
J = lambda t: re.sub(r"\s*\n\s*", " ", t)
G = lambda r, p: J(subprocess.run(["git", "show", f"{r}:{p}"], capture_output=True, text=True).stdout)
src = {"RESULTS": G(rev, "docs/RESULTS.md"), "XICYC": G(rev, "docs/new/P-N5-XICYC.md"), "REACH": G(rev, "docs/new/P-N5-REACH.md"),
       "SPEC": G(rev, "docs/new/N5-ssi-global.md"), "END": G("131b4c1c", "docs/new/P-N5-END.md"), "ASC": G("e28e962d", "docs/new/P-N5-ASC.md"),
       "QUIET": G("559cdffc", "docs/new/P-N5-QUIET.md") + " " + G("559cdffc", "docs/new/P-N5-QUIET-fixes.md") + " " + G("559cdffc", "docs/new/P-N5-QUIET-line-L2.txt"),
       "PACKET": G(prev, "docs/new/P-N5-CHAIN.md")}
n = bad = 0
for q in re.findall(r"«(.*?)»", J(T)):
    fr = [x.strip() for x in q.split("…") if x.strip()]; n += 1
    hit = [k for k, t in src.items() if all(x in t for x in fr)]; bad += not hit
    print("OK  " if hit else "NONE", hit, "|", q[:110])
print("quotes", n, "not found", bad)
