#!/usr/bin/env python3
"""REFEREE-2 succ. 17: own verbatim check of the curly-quoted strings in a packet's quotes section against named files at a commit.
Usage: quotes.py packet_file commit section_heading_prefix file1 file2 ...   (whitespace runs normalised; reports the line range found)"""
import sys, re, subprocess
pk, commit, sec = sys.argv[1], sys.argv[2], sys.argv[3]
files = sys.argv[4:]
txt = open(pk).read()
i = txt.index(sec); body = txt[i:]
j = body.find("\n## ", 5); body = body if j < 0 else body[:j]
qs = re.findall(r"“(.*?)”", body, re.S)
norm = lambda s: re.sub(r"\s+", " ", s).strip()
src = {}
for f in files:
    src[f] = subprocess.run(["git", "show", f"{commit}:{f}"], capture_output=True, text=True, check=True).stdout
ok = 0
for q in qs:
    nq = norm(q); hits = []
    for f, s in src.items():
        lines = s.split("\n")
        # search windows of up to 4 lines
        done = False
        for w in range(1, 5):
            for a in range(len(lines)):
                if nq in norm(" ".join(lines[a:a + w])):
                    hits.append(f"{f}:{a + 1}-{a + w}"); done = True; break
            if done: break
    print(("FOUND " if hits else "MISSING ") + (hits[0] if hits else "") + " | " + nq[:110])
    ok += bool(hits)
print(f"quotes {len(qs)} found {ok} missing {len(qs) - ok}")
