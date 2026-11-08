"""REFEREE successor 29: every «…» in P-N5-END §1, searched (fragments split at '…', wrapped lines joined by one space) in the trunk
files the packet names: docs/RESULTS.md, docs/new/N5-ssi-global.md, docs/new/P-N5-XICYC.md, docs/new/P-N5-REACH.md (git show REV:path).
For each quote: which files hold all fragments, and in RESULTS which entry (the last «## R…» / «### R…» heading before the first fragment).
Usage: end_quotes.py REV PACKET.md"""
import sys, re, subprocess
rev, P = sys.argv[1], open(sys.argv[2], encoding="utf-8").read()
files = ["docs/RESULTS.md", "docs/new/N5-ssi-global.md", "docs/new/P-N5-XICYC.md", "docs/new/P-N5-REACH.md"]
J = lambda t: re.sub(r"\s*\n\s*", " ", t)
T = {f: subprocess.run(["git", "show", f"{rev}:{f}"], capture_output=True, text=True).stdout for f in files}
TJ = {f: J(t) for f, t in T.items()}
sec1 = P[P.index("## 1. Premises"):P.index("## 2. Facts")]
heads = [(m.start(), m.group(0)[:40]) for m in re.finditer(r"(?m)^#{2,4} .*$", TJ and T["docs/RESULTS.md"])]
for q in re.findall(r"«(.*?)»", sec1, re.S):
    q1 = J(q); fr = [f.strip() for f in q1.split("…") if f.strip()]
    hit = [f.split("/")[-1] for f in files if all(x in TJ[f] for x in fr)]
    ent = ""
    if "RESULTS.md" in hit:
        R = T["docs/RESULTS.md"]; first = fr[0]; words = first.split()
        # locate on the unjoined text by a regex allowing any whitespace between words
        m = re.search(r"\s+".join(map(re.escape, words)), R)
        if m:
            hs = [h for p, h in heads if p < m.start()]; ent = hs[-1] if hs else ""
            ent = f"l. {R.count(chr(10), 0, m.start()) + 1} under «{ent}»"
    print(("OK  " if hit else "NONE"), hit, ent, "|", q1[:110])
