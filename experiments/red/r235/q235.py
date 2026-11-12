#!/usr/bin/env python3
"""L-RED 66 R235: independent re-grep of box 208's quoted premises (claude/l-new 8db300fe docs/new/N5-LEVEL-box208.md) in trunk
docs/RESULTS.md at a given commit. Every «…» on a line of box 208 that starts with «- [Q]» (and its continuation lines, up to the next
line starting with «- ») is extracted; a quote counts as FOUND if, after collapsing whitespace, it is a substring of the collapsed
RESULTS text. Nested «» inside a quote are kept. Prints each quote with FOUND / MISSING and the RESULTS line of its first occurrence.
Usage: q235.py BOX208.md RESULTS.md"""
import sys, re
box = open(sys.argv[1]).read().split("\n"); res = open(sys.argv[2]).read()
flat = re.sub(r"\s+", " ", res); lines = res.split("\n")
# map flat offset -> line: build cumulative
starts = []; pos = 0
for i, l in enumerate(lines): starts.append((len(re.sub(r"\s+", " ", "\n".join(lines[:i]) + "\n")) if False else None))
blocks = []; cur = None
for l in box:
    s = l.lstrip()
    if s.startswith("- [Q]"): cur = [s]; blocks.append(cur)
    elif cur is not None and l.startswith("  ") and not s.startswith("- "): cur.append(s)
    else: cur = None
def quotes(t):
    out = []; i = 0
    while True:
        a = t.find("«", i)
        if a < 0: return out
        d = 0; j = a
        while j < len(t):
            if t[j] == "«": d += 1
            elif t[j] == "»":
                d -= 1
                if d == 0: break
            j += 1
        out.append(t[a + 1:j]); i = j + 1
n = f = 0
for b in blocks:
    t = " ".join(b)
    for q in quotes(t):
        qq = re.sub(r"\s+", " ", q).strip(); n += 1
        ok = qq in flat
        if not ok:   # try the quote's own nested «» stripped (a quote of a quote)
            ok = qq.replace("«", "").replace("»", "") in flat.replace("«", "").replace("»", "")
        f += ok
        ln = next((i + 1 for i, l in enumerate(lines) if qq[:40] in re.sub(r"\s+", " ", l)), None)
        print("FOUND  " if ok else "MISSING", "l.%s" % ln, qq[:110], flush=True)
print("TOTAL quotes", n, "found", f, "missing", n - f)
