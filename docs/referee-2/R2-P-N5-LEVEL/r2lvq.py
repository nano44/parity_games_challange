#!/usr/bin/env python3
"""REFEREE-2 successor 39: own quote check of P-N5-LEVEL's [Q X] bullets (§1 and §13), written without reading quotes211.py.
Usage: r2lvq.py PACKET RESULTS P-N5-QN.md P-N5-XICYC.md TARGET.md
For every bullet line «- [Q X] …» (and its continuation lines) every balanced «…» must occur, whitespace-normalised, inside the named
source: RESULTS entry «### X » … next «### » for X = R<id>; the packet file for X = P-N5-QN / P-N5-XICYC; TARGET.md for X = TARGET.
A quote containing « … » (ellipsis) is tested piece by piece, in order. Prints every quote with FOUND / MISSING and a TOTAL line."""
import sys, re, hashlib
pk, res, qn, xc, tg = sys.argv[1:6]
norm = lambda s: " ".join(s.split())
R = open(res, encoding="utf-8").read().split("\n")
heads = [i for i, l in enumerate(R) if l.startswith("### ")]
ENT = {}
for k, i in enumerate(heads):
    ENT[R[i].split()[1]] = norm("\n".join(R[i:heads[k + 1] if k + 1 < len(heads) else len(R)]))
SRC = {"P-N5-QN": norm(open(qn, encoding="utf-8").read()), "P-N5-XICYC": norm(open(xc, encoding="utf-8").read()),
       "TARGET": norm(open(tg, encoding="utf-8").read())}
def quotes(s):
    out = []; i = 0
    while True:
        i = s.find("«", i)
        if i < 0: return out
        d = 0; j = i
        while j < len(s):
            if s[j] == "«": d += 1
            elif s[j] == "»":
                d -= 1
                if d == 0: break
            j += 1
        out.append(s[i + 1:j]); i = j + 1
L = open(pk, encoding="utf-8").read().split("\n")
bul = []; cur = None
for l in L:
    m = re.match(r"^\s*- \[Q ([A-Za-z0-9-]+)\]", l)
    if m: cur = [m.group(1), l]; bul.append(cur); continue
    if cur and l.startswith("  ") and not re.match(r"^\s*- ", l): cur[1] += " " + l.strip(); continue
    cur = None
nq = miss = 0
for src, text in bul:
    hay = ENT.get(src) if src.startswith("R") else SRC.get(src)
    for q in quotes(text):
        nq += 1; qn_ = norm(q)
        if hay is None: ok = False
        else:
            parts = [p for p in re.split(r"\s…\s|^…\s|\s…$", qn_) if p.strip()] if " … " in qn_ else [qn_]
            pos = 0; ok = True
            for p in parts:
                j = hay.find(p.strip(), pos)
                if j < 0: ok = False; break
                pos = j + len(p.strip())
        miss += not ok
        print(("FOUND  " if ok else "MISSING"), src, "«" + qn_[:110] + ("…" if len(qn_) > 110 else "") + "»")
print(f"TOTAL bullets {len(bul)} quotes {nq} missing {miss}; RESULTS sha1 {hashlib.sha1(open(res,'rb').read()).hexdigest()}")
