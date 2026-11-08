"""REFEREE successor 28: P-N5-ASC byte test L-2 -> L-3 (CHECKER C135 §5 R1-R4, wrapped lines joined by one space); my AS-2 / AS-3
strings re-counted on L-3; contexts of R3 / R4 printed for the meaning check. Usage: asc_l3.py L2 L3"""
import sys, hashlib
L2 = open(sys.argv[1], encoding="utf-8").read(); L3 = open(sys.argv[2], encoding="utf-8").read()
R = [("R1", "; L-NEW successor 61)", "; L-NEW successors 61-62)"),
     ("R2", "; §3-§5 do not use [E-LEV]; DATA, clause by clause", "; §3-§5 do not use [E-LEV]; the proof of record of HUB-ASC-G's B = 0 case (F′_0 = F_0, DESC-POLY on the whole interval) is referee-originated (REFEREE R-P-N5-ASC §3 AS-1, restated in P-N5-ASC's fixes entry 1 AS-1), signed by both referees; DATA, clause by clause"),
     ("R3", "so the e-vertices of one Λ-class form one forest whose paths are the sequences seq_t(v)", "hence seq_t(v) = (f, seq_t(y_f))"),
     ("R4", "with E_t(v) the set of e-vertices in Π_t(v),", "with seq_t(v) the e-vertices in Π_t(v) in play order, E_t(v) their set, an ascent of seq_t(v) a step to a more relevant element,")]
X = L2
for nm, o, n in R:
    print(nm, "old in L-2:", L2.count(o), "(in X now:", X.count(o), ") | new in L-3:", L3.count(n), "| old in L-3:", L3.count(o)); X = X.replace(o, n)
h = lambda t: (hashlib.sha1(t.encode()).hexdigest(), len(t.encode()))
print("L-2 + R1..R4 == L-3:", X == L3, h(X), "| L-3", h(L3))
for s in ("UP-JUMP, UP-B and NOUP under HYPOTHESIS [E-LEV]", "(only for §6 UP-JUMP, UP-B and NOUP)", "UP-JUMP and UP-B under HYPOTHESIS [E-LEV]", "(only for §6 UP-JUMP and UP-B)", "under [E-LEV]"):
    print("L-3", L3.count(s), "|", s)
for k in ("hence seq_t(v) = (f, seq_t(y_f))", "an ascent of seq_t(v) a step"):
    i = L3.index(k); print("CTX:", L3[i - 420:i + 160])
print("parens", L3.count("("), L3.count(")"))
