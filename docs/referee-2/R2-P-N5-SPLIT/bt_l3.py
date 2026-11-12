#!/usr/bin/env python3
# REFEREE-2 successor 37: independent rebuild of P-N5-SPLIT line L-3 from L-1 (8f4dab7e, sha1 634b2fdf) using the exact strings of
# docs/new/P-N5-SPLIT-fixes.md entries 3-4 at claude/l-new 621e6b77 (parsed from the whitespace-normalised fixes text; the lane's
# mkl2_199.py / mkl3_199.py are not imported). Usage: bt_l3.py L1.txt FIXES.md L3_lane.txt OUT.txt
import sys, re, hashlib, difflib
L1 = open(sys.argv[1], encoding="utf-8").read(); FX = " ".join(open(sys.argv[2], encoding="utf-8").read().split())
lane = open(sys.argv[3], "rb").read()
e3 = FX[FX.index("## Fixes entry 3"):FX.index("## Fixes entry 4")]; e4 = FX[FX.index("## Fixes entry 4"):]
def q(s, after, n=1):               # the n-th «…» (balanced, nested « » allowed) after the marker
    i = s.index(after) + len(after); out = []
    while len(out) < n:
        i = s.index("«", i); d = 0; j = i
        while True:
            if s[j] == "«": d += 1
            elif s[j] == "»":
                d -= 1
                if d == 0: break
            j += 1
        out.append(s[i + 1:j]); i = j + 1
    return out
old7, new7 = q(e3, "in L-1, replace exactly once", 2)
anchor, ins = q(e3, "and in the DATA clause, right after", 1)[0], q(e3, "insert", 1)[0]
ra, rb, rc, rd = (q(e4, f"- ({k})", 2) for k in "abcd")
steps = [("R-D7a D7", old7, new7), ("R-D7a DATA", anchor, anchor + ins), ("R-U127 (a)", *ra), ("R-U127 (b)", *rb), ("R-U127 (c)", *rc),
         ("R-U127 (d)", *rd)]
L = L1; fails = 0
for nm, o, n in steps:
    c = L.count(o); print(nm, "old count", c, "PASS" if c == 1 else "FAIL"); fails += c != 1; L = L.replace(o, n, 1)
open(sys.argv[4], "w", encoding="utf-8").write(L)
b = L.encode(); print("rebuilt sha1", hashlib.sha1(b).hexdigest(), len(b), "B; lane", hashlib.sha1(lane).hexdigest(), len(lane), "B;",
                      "BYTE-EQUAL" if b == lane else "DIFFER")
fails += b != lane
a, c_ = L1.split(" "), lane.decode().split(" ")
regs = [op for op in difflib.SequenceMatcher(None, a, c_, autojunk=False).get_opcodes() if op[0] != "equal"]
print("diff regions L-1 -> lane L-3:", len(regs))
for op, i1, i2, j1, j2 in regs: print("  ", op, "|", " ".join(a[i1:i2])[:90], "->", " ".join(c_[j1:j2])[:120])
for bad in ["RA-LOG", "MW32_2, 445031d1", "with fixes entries 1-2", "|"]: print("absent", repr(bad), bad not in lane.decode()); fails += bad in lane.decode()
print("parens", lane.decode().count("("), lane.decode().count(")"), "FAILS", fails)
