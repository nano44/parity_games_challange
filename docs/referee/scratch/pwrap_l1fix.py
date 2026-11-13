#!/usr/bin/env python3
"""REFEREE s34: P-N5-WRAP line L-1 (claude/l-si e01447e7, sha1 896f9e97…) + required string LW-1 of R-P-N5-WRAP.md §5 (old string
asserted to occur once). usage: pwrap_l1fix.py L1.txt OUT"""
import sys, hashlib
L = open(sys.argv[1], encoding="utf-8").read()
assert hashlib.sha1(L.encode()).hexdigest() == "896f9e97394695f903131f832a67f31bcfc23c28"
FIX = [("LW-1",
 "DATA: T_n = 9·2^n − 10 for n ≤ 8 on the wrappers (this lane, L-COMP 20 aa863db5, REFEREE 33 e44ce56b / 90703a81: 18 counters 0 on "
 "523,721 runs) and n ≤ 10 on G_n;",
 "DATA (unit: T_n, the steps of Howard's run on G^L_n from ι, = N5′-xi iterations − 3 on W^L_n; experiments/si/box104/out/"
 "wrap_lmcs_xi.out and wrap_long.out, column T, with WRAP's six must-0 counters s3fail, nonstd, nohoward, fbwrong, endwrong, wrong 0 "
 "on the same rows): T_n 8, 26, 62, 134, 278, 566, 1,142, 2,294 for n = 1, …, 8 (equal to 9·2^n − 10 on these eight), and 4,598, "
 "9,206 for n = 9, 10 on G^L_n alone (REFEREE 33, claude/referee e44ce56b, docs/referee/scratch/wrap_logs/f11_H_fig4.out, column T); "
 "independent replays, every fail counter 0, their counters in their own pinned outputs, cited, not re-run: L-COMP 20 (aa863db5), "
 "REFEREE 33 (e44ce56b / 90703a81; 18 counters 0 on 523,721 runs);")]
for name, o, n in FIX:
    k = L.count(o); print(name, "old count", k); assert k == 1; L = L.replace(o, n)
open(sys.argv[2], "w", encoding="utf-8").write(L)
print("L-1' sha1", hashlib.sha1(L.encode()).hexdigest(), len(L.encode()), "B; newlines", L.count("\n"), "bars", L.count("|"), "parens", L.count("("), L.count(")"))
