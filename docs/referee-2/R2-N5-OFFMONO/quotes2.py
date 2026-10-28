#!/usr/bin/env python3
"""REFEREE-2 succ. 18: own verbatim check of the curly-quoted strings in a packet section against files pinned per file.
Usage: quotes2.py packet_file section_heading_prefix commit:path [commit:path ...]   (whitespace runs normalised; prints the
line range where each quote is found, so the packet's line numbers can be compared)"""
import sys, re, subprocess
pk, sec = sys.argv[1], sys.argv[2]
specs = sys.argv[3:]
txt = open(pk).read()
i = txt.index(sec); body = txt[i:]
j = body.find("\n## ", 5); body = body if j < 0 else body[:j]
qs = re.findall(r"“(.*?)”", body, re.S)
norm = lambda s: re.sub(r"\s+", " ", s).strip()
src = {}
for spec in specs:
    src[spec] = subprocess.run(["git", "show", spec], capture_output=True, text=True, check=True).stdout
ok = 0
for q in qs:
    nq = norm(q); hits = []
    for f, s in src.items():
        lines = s.split("\n")
        for w in range(1, 5):
            found = [a for a in range(len(lines)) if nq in norm(" ".join(lines[a:a + w]))]
            if found:
                hits.append(f"{f} l.{found[0] + 1}-{found[0] + w}" + (f" (+{len(found) - 1} more)" if len(found) > 1 else "")); break
    print(("FOUND " if hits else "MISSING ") + ("; ".join(hits)) + " | " + nq[:100])
    ok += bool(hits)
print(f"quotes {len(qs)} found {ok} missing {len(qs) - ok}")
