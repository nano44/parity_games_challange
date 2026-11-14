"""REFEREE successor 29: every «…» in P-N5-END line L-2, searched (fragments split at '…', wrapped lines joined) in the sources it names:
trunk docs/RESULTS.md, docs/new/P-N5-XICYC.md, docs/new/P-N5-REACH.md, docs/new/N5-ssi-global.md (REV), and the lane's
docs/new/P-N5-END-fixes.md (LREV). Usage: end_l2quotes.py REV LREV L2.txt"""
import sys, re, subprocess
rev, lrev, L = sys.argv[1], sys.argv[2], open(sys.argv[3], encoding="utf-8").read()
J = lambda t: re.sub(r"\s*\n\s*", " ", t)
src = {f: J(subprocess.run(["git", "show", f"{rev}:{f}"], capture_output=True, text=True).stdout)
       for f in ["docs/RESULTS.md", "docs/new/P-N5-XICYC.md", "docs/new/P-N5-REACH.md", "docs/new/N5-ssi-global.md"]}
src["P-N5-END-fixes.md@" + lrev] = J(subprocess.run(["git", "show", f"{lrev}:docs/new/P-N5-END-fixes.md"], capture_output=True, text=True).stdout)
for q in re.findall(r"«(.*?)»", L):
    fr = [f.strip() for f in q.split("…") if f.strip()]
    hit = [k.split("/")[-1] for k, t in src.items() if all(x in t for x in fr)]
    print("OK  " if hit else "NONE", hit, "|", q[:120])
