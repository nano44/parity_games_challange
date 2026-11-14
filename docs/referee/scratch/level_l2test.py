#!/usr/bin/env python3
"""REFEREE s34: byte test of P-N5-LEVEL L-2. Builds L-1 + my LT-1..LT-3 (level_l1fix.py's strings, imported) -> 389645a2, then
REFEREE-2's R-1, R-2 parsed by THIS script from R2-P-N5-LEVEL.md as committed at claude/referee-2 43824abc, then my LO-1 insertion.
usage: level_l2test.py L1.txt R2-P-N5-LEVEL.md OUT"""
import sys, re, hashlib, importlib.util, os
spec = importlib.util.spec_from_file_location("fx", os.path.join(os.path.dirname(os.path.abspath(__file__)), "level_l1fix.py"))
src = open(spec.origin, encoding="utf-8").read()
FIX = eval(src[src.index("FIX = [") + 6: src.index("]\nfor name")] + "]")
L = open(sys.argv[1], encoding="utf-8").read(); r2 = open(sys.argv[2], encoding="utf-8").read()
h = lambda s: hashlib.sha1(s.encode()).hexdigest()
assert h(L) == "28565b3c60fe8167f4b660c83fa27c00cd7b4fe9"
def app(name, o, n):
    global L
    k = L.count(o); print(name, "old count", k); assert k == 1; L = L.replace(o, n)
for name, o, n in FIX: app(name, o, n)
print("stage LT-1..LT-3 sha1", h(L))
def grab(tag):
    i = r2.index("- " + tag + " ("); j = r2.index("\n- ", i + 3) if tag == "R-1" else r2.index("\n\n", i)
    blk = r2[i:j]
    q = re.findall(r"«((?:[^«»]|«[^«»]*»)*)»", blk)
    q = [re.sub(r"\s*\n\s*", " ", x) for x in q]
    return q[0], q[1]
for tag in ["R-1", "R-2"]:
    o, n = grab(tag); app(tag, o, n); print("stage", tag, "sha1", h(L))
o = "the 49 must-0 counters of rv208.py"; app("LO-1", o, o + " (named in its header; a counter that is 0 is not printed)")
open(sys.argv[3], "w", encoding="utf-8").write(L)
print("L-2 sha1", h(L), len(L.encode()), "B; newlines", L.count("\n"), "bars", L.count("|"), "parens", L.count("("), L.count(")"))
