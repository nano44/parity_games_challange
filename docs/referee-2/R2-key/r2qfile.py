#!/usr/bin/env python3
"""REFEREE-2 41, own code (after successor 40's r2q212.py): check the quote that directly follows each marker [Q <src>] in a LOCAL file.
<src> = R<nn> (the entry «### R<nn> » of docs/RESULTS.md at trunk TRUNK) or <path>@<commit>. Whitespace is normalised on both sides; a
quote is split at «…» and every piece must occur in the source; nested «» stay inside the outer quote.
Usage: r2qfile.py FILE TRUNK [--from MARK] [--ctrl]   (--from: only the text after the first line starting with MARK; --ctrl: the last
character of every piece is altered, every quote must then MISS)."""
import sys, re, subprocess
fn, trunk = sys.argv[1], sys.argv[2]; ctrl = "--ctrl" in sys.argv
txt = open(fn).read()
if "--from" in sys.argv:
    mark = sys.argv[sys.argv.index("--from") + 1]; i = txt.find("\n" + mark); assert i >= 0, "mark not found"; txt = txt[i:]
show = lambda spec: subprocess.run(["git", "show", spec], capture_output=True, text=True, check=True).stdout
norm = lambda s: re.sub(r"\s+", " ", s).strip()
res = show(trunk + ":docs/RESULTS.md"); cache = {}
def source(src):
    if src not in cache:
        if re.fullmatch(r"R\d+", src):
            m = re.search(r"^### " + src + r" .*?(?=^### R\d+ |\Z)", res, re.S | re.M); cache[src] = norm(m.group(0)) if m else None
        elif "@" in src:
            p, c = src.split("@"); cache[src] = norm(show(c + ":" + p))
        else: cache[src] = None
    return cache[src]
tot = miss = 0
for m in re.finditer(r"\[Q ([^\]]+)\]\s*«", txt):
    src = m.group(1).strip(); i = m.end(); d = 1; j = i
    while d and j < len(txt):
        d += (txt[j] == "«") - (txt[j] == "»"); j += 1
    q = txt[i:j - 1]; pieces = [norm(x) for x in q.split("…") if norm(x)]
    if ctrl: pieces = [x[:-1] + ("#" if x[-1] != "#" else "%") for x in pieces]
    s = source(src); ok = s is not None and all(x in s for x in pieces); tot += 1; miss += not ok
    print("OK  " if ok else "MISS", src, "|", norm(q)[:100])
print(f"quotes {tot} missing {miss}")
