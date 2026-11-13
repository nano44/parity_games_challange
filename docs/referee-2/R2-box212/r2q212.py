#!/usr/bin/env python3
"""REFEREE-2 40, own code: check every «…» on a bullet of box 212 marked [Q <src>] against <src>.
<src> = R<nn> (the entry «### R<nn> » of docs/RESULTS.md at trunk TRUNK) or <path>@<commit>.
Wrapped lines are joined with one space; whitespace is normalised on both sides. Nested «» kept inside the outer quote.
Usage: r2q212.py BOX_FILE_AT_COMMIT TRUNK [--ctrl]   (--ctrl: alter each quote by one character; every quote must then MISS)."""
import sys, re, subprocess
box, trunk = sys.argv[1], sys.argv[2]; ctrl = "--ctrl" in sys.argv
def show(spec):
    return subprocess.run(["git", "show", spec], capture_output=True, text=True, check=True).stdout
norm = lambda s: re.sub(r"\s+", " ", s).strip()
res = show(trunk + ":docs/RESULTS.md")
def entry(r):
    m = re.search(r"^### " + r + r" .*?(?=^### R\d+ |\Z)", res, re.S | re.M)
    return m.group(0) if m else None
lines = show(box).split("\n")
bul = []; cur = None
for l in lines:
    if re.match(r"^\s*- ", l) or re.match(r"^#|^\| ", l) or l.strip() == "" or (cur is None):
        if cur is not None: bul.append(cur)
        cur = None if (l.strip() == "" or re.match(r"^#|^\| ", l)) else l
    else: cur += " " + l.strip()
if cur is not None: bul.append(cur)
def quotes(s):
    out = []; d = 0; st = None
    for i, ch in enumerate(s):
        if ch == "«":
            if d == 0: st = i + 1
            d += 1
        elif ch == "»" and d > 0:
            d -= 1
            if d == 0: out.append(s[st:i])
    return out
tot = miss = 0
for b in bul:
    parts = re.split(r"\[Q ([^\]]+)\]", b)
    for k in range(1, len(parts), 2):
        src = parts[k].strip(); seg = parts[k + 1]
        if re.fullmatch(r"R\d+", src): txt = entry(src)
        elif "@" in src:
            p, c = src.split("@"); txt = show(c + ":" + p)
        else: txt = None
        for q in quotes(seg):
            qq = norm(q.replace("…", " ")) if False else norm(q)
            pieces = [norm(x) for x in q.split("…") if norm(x)]
            if ctrl: pieces = [x[:-1] + ("#" if x[-1] != "#" else "%") for x in pieces]
            tot += 1
            ok = txt is not None and all(x in norm(txt) for x in pieces)
            if not ok: miss += 1
            print("OK  " if ok else "MISS", src, "|", qq[:90])
print(f"quotes {tot} missing {miss}")
