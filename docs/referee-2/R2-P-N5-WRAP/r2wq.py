#!/usr/bin/env python3
"""REFEREE-2 39: quote check of P-N5-WRAP §1 [Q] items whose source is on trunk 7fa6aff4 (SPEC file, P-N5-XICYC.md, RESULTS R104 /
R15). Every balanced «…» on a §1 bullet (lines up to «## 2.») is searched whitespace-normalised in the named trunk source; nested «…»
inside a quote are searched separately. REFEREE 33's quotes (§6, §7, §9, §10) are NOT checked here (docs/referee/ not read before my
verdict). Usage: r2wq.py PACKET SPECFILE XICYC RESULTS"""
import sys, re
pk, spec, xc, res = sys.argv[1:5]
norm = lambda s: " ".join(s.split())
R = open(res, encoding="utf-8").read().split("\n"); heads = [i for i, l in enumerate(R) if l.startswith("### ")]
ENT = {R[i].split()[1]: norm("\n".join(R[i:heads[k + 1] if k + 1 < len(heads) else len(R)])) for k, i in enumerate(heads)}
SRC = {"SPEC": norm(open(spec, encoding="utf-8").read()), "N5XI": norm(open(xc, encoding="utf-8").read()),
       "1E-N3": ENT["R104"], "DUAL": ENT["R104"], "R15": ENT["R15"], "RULE": ENT["R104"]}
def quotes(s):
    out = []; i = 0
    while True:
        i = s.find("«", i)
        if i < 0: return out
        d = 0; j = i
        while j < len(s):
            d += (s[j] == "«") - (s[j] == "»")
            if d == 0: break
            j += 1
        out.append(s[i + 1:j]); i = j + 1
text = open(pk, encoding="utf-8").read(); sec1 = text[text.index("## 1. Premises"):text.index("## 2. Definitions")]
cur = None; n = miss = 0
lines = []
for l in sec1.split("\n"):
    if re.match(r"^\s*- ", l) or not lines: lines.append(l)
    else: lines[-1] += " " + l.strip()
for line in lines:
    m = re.search(r"\[(SPEC|N5XI|1E-N3|DUAL|R15a\]|RULE)", line)
    if m: cur = {"R15a]": "R15"}.get(m.group(1), m.group(1))
    if line.startswith("- [F11]"): cur = None
    if cur is None: continue
    for q in quotes(line):
        for piece in ([q] + quotes(q)) if "«" in q else [q]:
            if "«" in piece: continue
            if piece in ("the arena",): continue      # the packet's own naming («to avoid a clash … called «the arena»»), not a quote
            n += 1; ok = norm(piece) in SRC[cur]; miss += not ok
            print("FOUND  " if ok else "MISSING", cur, "«" + norm(piece)[:100] + "»")
print(f"TOTAL quotes {n} missing {miss}")
