"""REFEREE successor 27: every top-level «…» of P-TOWER-FUEL fixes entry 1, looked up (wrapped lines joined by one space) in my report
(807984e3), REFEREE-2's (4bede4dd), the frozen packet, or neither. Usage: tf_fixquotes.py FIXES R1 R2 PACKET"""
import sys, re
def norm(s): return re.sub(r"\s*\n\s*", " ", s)
F, R1, R2, PK = (norm(open(p, encoding="utf-8").read()) for p in sys.argv[1:5])
def toplevel(s):
    out, dep, cur = [], 0, []
    for ch in s:
        if ch == "«":
            dep += 1
            if dep == 1: cur = []; continue
        if ch == "»":
            dep -= 1
            if dep == 0: out.append("".join(cur)); continue
        if dep >= 1: cur.append(ch)
    return out
for q in toplevel(F):
    src = [n for n, T in (("R1", R1), ("R2", R2), ("packet", PK)) if q in T]
    print(("OK " if src else "-- ") + ",".join(src or ["lane text"]) + " | " + q[:110])
