#!/usr/bin/env python3
"""REFEREE s34: byte test of P-N5-WRAP L-2 (claude/l-si faf0c8ff). L-1 + my LW-1 (pwrap_l1fix.py's strings) -> be7da8f3; REFEREE-2's R-1
(parsed from R2-P-N5-WRAP.md at claude/referee-2 07fd5ae4 §3.7); R-2's New applied to LW-1's clause as fixes entry 1 item 3 describes
(old «18 counters 0 on 523,721 runs);» -> R-2's REFEREE-33 part «its 18 must-be-0 counters, named in its report, 0 on 523,721 runs» +
«); » + R-2's sentence on WRAP's six counters + «;»); LW-2 and LW-3 as fixes entry 1 items 4, 5 (my §5 content).
usage: pwrap_l2test.py L1.txt R2-P-N5-WRAP.md OUT"""
import sys, re, hashlib, os
d = os.path.dirname(os.path.abspath(__file__)); src = open(os.path.join(d, "pwrap_l1fix.py"), encoding="utf-8").read()
FIX = eval(src[src.index("FIX = [") + 6: src.index("]\nfor name")] + "]")
L = open(sys.argv[1], encoding="utf-8").read(); r2 = open(sys.argv[2], encoding="utf-8").read()
h = lambda s: hashlib.sha1(s.encode()).hexdigest()
assert h(L) == "896f9e97394695f903131f832a67f31bcfc23c28"
def app(name, o, n):
    global L
    k = L.count(o); print(name, "old count", k); assert k == 1; L = L.replace(o, n); print("  stage sha1", h(L))
for name, o, n in FIX: app(name, o, n)
def quotes(tag, nxt):
    blk = r2[r2.index("- " + tag + " ("): r2.index("- " + nxt + " (")]
    return [re.sub(r"\s*\n\s*", " ", x) for x in re.findall(r"«([^«»]*)»", blk)]
q1 = quotes("R-1", "R-2"); app("R-1", q1[-2], q1[-1])
q2 = quotes("R-2", "R-3"); old2, new2 = q2[0], q2[1]
print("R-2 old in current line:", L.count(old2))
pre = "REFEREE 33 e44ce56b / 90703a81: "; assert new2.startswith(pre)
part, rest = new2[len(pre):].split("); ", 1)
app("R-2 (adapted to LW-1's clause)", "18 counters 0 on 523,721 runs);", part + "); " + rest + ";")
app("LW-2", "(33 … 2,489 iterations = Howard T + 3)", "(33 … 2,489 iterations = Howard T + 3; experiments/si/box104/out/wrap_fried_xi.out, wrap_long.out, free_xi.out)")
app("LW-3", "an Even valve with an exit to R117's core", "an Even valve with an exit to the core K0-K3 (with pads pA, s, q, r)")
open(sys.argv[3], "w", encoding="utf-8").write(L)
print("L-2 sha1", h(L), len(L.encode()), "B; newlines", L.count("\n"), "parens", L.count("("), L.count(")"))
