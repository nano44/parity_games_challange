"""REFEREE successor 30: every «…» in P-N5-QN §1 (l. 33-75), whitespace-normalised, searched in trunk RESULTS.md and P-N5-XICYC.md
(given as files). Also reports the RESULTS entry (### R..) containing each hit. Usage: qn_quotes.py PACKET RESULTS XICYC"""
import sys, re
P = open(sys.argv[1], encoding="utf-8").read().split("\n"); R = open(sys.argv[2], encoding="utf-8").read(); X = open(sys.argv[3], encoding="utf-8").read()
sec = " ".join(l.strip() for l in P[32:75])
def norm(s): return re.sub(r"\s+", " ", s)
Rn, Xn = norm(R), norm(X)
heads = [(m.start(), m.group(1)) for m in re.finditer(r"### (R\d+)", Rn)]
qs = []; d = 0; cur = ""
for ch in sec:
    if ch == "«":
        d += 1
        if d == 1: cur = ""; continue
    if ch == "»":
        d -= 1
        if d == 0: qs.append(cur); continue
    if d >= 1: cur += ch
miss = 0
for q in qs:
    q = norm(q).strip(); i = Rn.find(q)
    if i >= 0: where = [h for p, h in heads if p <= i][-1]
    elif q in Xn: where = "P-N5-XICYC"
    else: where = "MISSING"; miss += 1
    print(where, "|", q[:110])
print("quotes", len(qs), "missing", miss)
