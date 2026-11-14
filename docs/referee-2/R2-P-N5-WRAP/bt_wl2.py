#!/usr/bin/env python3
"""REFEREE-2 successor 39: own byte test of P-N5-WRAP line L-2 (claude/l-si faf0c8ff). Own parser (not mkL2.py). Pairs read from the two
reports at their pinned commits, wrapped lines joined with one space:
  REFEREE 34 (claude/referee 99df2458, docs/referee/R-P-N5-WRAP.md §5): LW-1 «old» → «new»; LW-2 / LW-3 as named there (files; «to the
  core K0-K3 (with pads pA, s, q, r)»);
  REFEREE-2 (claude/referee-2 07fd5ae4, docs/referee-2/R2-P-N5-WRAP.md 3.7): R-1 Old / New exact; R-2 New, re-anchored on LW-1's clause
  as fixes entry 1 step 3 says (LW-1 rewrote R-2's Old).
Order: LW-1 (checkpoint be7da8f3), R-1, R-2 (re-anchored), LW-2, LW-3. Every old string asserted once. Usage: bt_wl2.py L1 R34 R2 L2"""
import sys, re, hashlib
L1, R34, R2, L2 = sys.argv[1:5]
def bal(s, i):
    d = 0; j = i
    while j < len(s):
        d += (s[j] == "«") - (s[j] == "»")
        if d == 0: return s[i + 1:j], j + 1
        j += 1
def quotes(s):
    out = []; i = 0
    while True:
        i = s.find("«", i)
        if i < 0: return out
        q, i = bal(s, i); out.append(q)
def bullet(text, head):
    L = text.split("\n")
    for k, l in enumerate(L):
        if re.match(r"^\s*- " + re.escape(head), l):
            ind = len(l) - len(l.lstrip()); out = [l.strip()]
            for m in L[k + 1:]:
                if not m.strip() or (len(m) - len(m.lstrip()) <= ind and m.lstrip().startswith("- ")) or m.startswith("#"): break
                out.append(m.strip())
            return " ".join(out)
    raise KeyError(head)
r34 = open(R34, encoding="utf-8").read(); r2 = open(R2, encoding="utf-8").read()
lw1 = quotes(bullet(r34, "LW-1")); b1 = bullet(r2, "R-1 (REQUIRED)"); r1 = quotes(b1[b1.index("Old"):]); r2b = bullet(r2, "R-2 (REQUIRED"); r2q = quotes(r2b[r2b.index("Old"):])
opt = bullet(r34, "OPTIONAL (the Lead's call)"); oq = quotes(opt)
s = open(L1, encoding="utf-8").read(); h = lambda x: hashlib.sha1(x.encode()).hexdigest()
print("L-1", h(s), len(s.encode()))
def rep(s, old, new, tag):
    c = s.count(old); print(f"{tag}: old occurs {c}×"); assert c == 1, tag; return s.replace(old, new)
s = rep(s, lw1[0], lw1[1], "LW-1"); print("after LW-1", h(s), len(s.encode()))
s = rep(s, r1[0], r1[1], "R-1")
print("R-2 Old occurs after LW-1:", s.count(r2q[0]))
# R-2 re-anchored: «18 counters 0 on 523,721 runs);» (LW-1's) → «its 18 … runs); » + R-2's WRAP sentence + «;»
new = r2q[1]; ref_part = new[new.index("its 18 must-be-0"):new.index("runs);") + len("runs")]; wrap_part = new[new.index("WRAP's six"):]
s = rep(s, "18 counters 0 on 523,721 runs);", ref_part + "); " + wrap_part + ";", "R-2 re-anchored")
lw2_old = "(33 … 2,489 iterations = Howard T + 3)"; files = re.search(r"\(out/ ?(wrap_fried_xi\.out, wrap_long\.out, free_xi\.out)\)", opt).group(1)
s = rep(s, lw2_old, "(33 … 2,489 iterations = Howard T + 3; experiments/si/box104/out/" + files + ")", "LW-2")
lw3 = [q for q in oq if q.startswith("to the core K0-K3")][0]
s = rep(s, "an Even valve with an exit to R117's core", "an Even valve with an exit to " + lw3[len("to "):], "LW-3")
b = s.encode(); lane = open(L2, "rb").read()
print("rebuilt L-2", hashlib.sha1(b).hexdigest(), len(b), "B; ( ", s.count("("), ") ", s.count(")"), "«|»", s.count("|"), "lines", s.count("\n"))
print("lane L-2", hashlib.sha1(lane).hexdigest(), len(lane), "B:", "EQUAL" if lane == b else "DIFFERENT")
