"""REFEREE successor 27: every «…» in P-N5-ASC §1, searched verbatim (fragments split at '…') in trunk RESULTS.md; reports the
1-based line numbers where all fragments occur on one line, and also searches the frozen P-N5-XICYC packet.
Usage: asc_quotes.py RESULTS.md XICYC.md PACKET.md"""
import sys, re
R = open(sys.argv[1], encoding="utf-8").read().split("\n"); X = open(sys.argv[2], encoding="utf-8").read().split("\n")
P = open(sys.argv[3], encoding="utf-8").read()
sec1 = P[P.index("## 1. Premises"):P.index("## 2. Definitions")]
for q in re.findall(r"«(.*?)»", sec1, re.S):
    q1 = re.sub(r"\s*\n\s*", " ", q); fr = [f.strip() for f in q1.split("…") if f.strip()]
    rl = [i + 1 for i, l in enumerate(R) if all(f in l for f in fr)]
    xl = [i + 1 for i, l in enumerate(X) if all(f in l for f in fr)]
    print("RESULTS lines", rl or "NONE", "| XICYC lines", xl or "NONE", "|", q1[:100])
# second pass: wrapped lines joined by one space (RESULTS sub-entries and the XICYC packet are wrapped at ~140 columns)
def joined(lines):
    txt = re.sub(r"\s*\n\s*", " ", "\n".join(lines)); return txt
RJ, XJ = joined(R), joined(X)
print("--- joined-lines pass")
for q in re.findall(r"«(.*?)»", sec1, re.S):
    q1 = re.sub(r"\s*\n\s*", " ", q); fr = [f.strip() for f in q1.split("…") if f.strip()]
    print("RESULTS", all(f in RJ for f in fr), "| XICYC", all(f in XJ for f in fr), "|", q1[:80])
