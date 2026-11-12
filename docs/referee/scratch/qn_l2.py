"""REFEREE s31: P-N5-QN L-2 = L-1 + R-D2 + R-S (strings typed from CHECKER C140 §4 at claude/checker 445372f9). Usage: qn_l2.py L1 OUT"""
import sys, hashlib
L = open(sys.argv[1], encoding="utf-8").read()
RD2 = ("; D2 «at k = 1 every gate flips at most c·(lamch(g) + 1) times», every constant c (L-RED 63's MWR(n), claude/l-red 406ef2fd, "
       "R229-box202 §2; copies experiments/new/box203/inst/MWR4_2.json sha1 856d369b, MWR8_2.json 918f1414, MWR16_2.json 2ccda9a9: gate (qz, 0) "
       "flips 2n + 1 times with lamch 0)", "")
RS = ("C = 0): MWR4/8/16_2 9 / 17 / 33,", "C = 0): MWR4/8/16_2 (L-RED 63's MWR(n), claude/l-red 406ef2fd; box203/inst/MWR4_2.json sha1 856d369b, "
      "MWR8_2.json 918f1414, MWR16_2.json 2ccda9a9) 9 / 17 / 33,")
for name, (o, n) in (("R-D2", RD2), ("R-S", RS)):
    print(name, "old count", L.count(o)); L = L.replace(o, n)
    print(name, "after: sha1", hashlib.sha1(L.encode()).hexdigest(), len(L.encode()), "B")
open(sys.argv[2], "w", encoding="utf-8").write(L)
print("lines", L.count("\n"), "bars", L.count("|"), "parens", L.count("("), L.count(")"), "D2", L.count("D2"), "406ef2fd", L.count("406ef2fd"),
      "pending", L.count("pending"), "landed", L.count("landed"))
i = L.find("lamch 0); D3"); print("join:", L[i-20:i+60] if i >= 0 else "NOT FOUND")
