#!/usr/bin/env python3
"""L-NEW box 79 (P-N5-WCH fix W1, WCH-N1 = REFEREE-2 N-2): every «…» SPEC quote of the packet must occur verbatim (whitespace-normalised)
inside the SPEC lines its CORRECTED tag names (docs/new/N5-ssi-global.md; corrected tags per docs/new/P-N5-WCH-fixes-box79.md W1-1).
Prints one row per quote and QUOTECHECK PASS / FAIL."""
import re, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
spec = open(os.path.join(ROOT, "docs/new/N5-ssi-global.md")).read().splitlines()
pk = open(os.path.join(ROOT, "docs/new/P-N5-WCH-box79.md")).read()
FIX = {"26": "27", "27-28": "28-29", "29-30": "30-31", "31": "32"}     # W1-1: the four tags one line low
norm = lambda s: re.sub(r"\s+", " ", s).strip()
fails = 0
for m in re.finditer(r"\[Q SPEC:([0-9-]+)\]\s*«(.*?)»", pk, flags=re.S):
    tag = m.group(1); tag2 = FIX.get(tag, tag)
    a, b = (tag2.split("-") + [tag2])[:2]; a, b = int(a), int(b)
    seg = norm(" ".join(spec[a - 1:b]))
    ok = norm(m.group(2)) in seg
    fails += not ok
    print(f"| SPEC:{tag} -> {tag2} | {'OK' if ok else 'NOT FOUND'} | {norm(m.group(2))[:60]} |")
print("QUOTECHECK", "PASS" if fails == 0 else "FAIL"); sys.exit(1 if fails else 0)
