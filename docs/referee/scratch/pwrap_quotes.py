#!/usr/bin/env python3
"""REFEREE s34: P-N5-WRAP (claude/l-si e01447e7): every outermost «…» right after a [Q] mark is looked up (whitespace normalised) in
SPEC docs/new/N5-ssi-global.md and docs/new/P-N5-XICYC.md at trunk 7fa6aff4, in each entry of docs/RESULTS.md there (by R-id), and in
docs/referee/R-WRAP-preread.md at claude/referee e44ce56b and 90703a81. Mine, not the lane's qwrap.py. usage: pwrap_quotes.py PACKET.md"""
import sys, re, subprocess
def show(c, p): return subprocess.run(["git", "show", f"{c}:{p}"], capture_output=True, text=True, check=True).stdout
def norm(s): return re.sub(r"\s+", " ", s).strip()
T = "7fa6aff4"
src = {"SPEC": norm(show(T, "docs/new/N5-ssi-global.md")), "XICYC": norm(show(T, "docs/new/P-N5-XICYC.md")),
       "PRE@e44ce56b": norm(show("e44ce56b", "docs/referee/R-WRAP-preread.md")), "PRE@90703a81": norm(show("90703a81", "docs/referee/R-WRAP-preread.md"))}
ent = {}; cur = None
for l in show(T, "docs/RESULTS.md").split("\n"):
    m = re.match(r"### (R\d+) ", l)
    if m: cur = m.group(1); ent[cur] = []
    elif l.startswith("### ") or l.startswith("## "): cur = None
    if cur: ent[cur].append(l)
for r, v in ent.items(): src[r] = norm(" ".join(v))
t = open(sys.argv[1], encoding="utf-8").read()
n = miss = 0
for m in re.finditer(r"\[Q\]\s*«", t):
    k = m.end() - 1; d = 0
    for j in range(k, len(t)):
        if t[j] == "«": d += 1
        elif t[j] == "»":
            d -= 1
            if d == 0: break
    q = norm(t[k + 1:j]); n += 1
    hits = [s for s, h in src.items() if q in h]
    if not hits:
        # a quote of a quote: «a» «b» pieces inside; check each inner «…» separately
        inner = [norm(x) for x in re.findall(r"«([^«»]*)»", q)]
        if inner and all(any(x in h for h in src.values()) for x in inner): hits = ["(each inner quote found)"]
    miss += not hits
    print("%s line %d found-in %s «%s»" % ("OK  " if hits else "MISS", t.count("\n", 0, m.start()) + 1, ",".join(hits[:4]) or "-", q[:90]))
print("quotes", n, "missing", miss)
