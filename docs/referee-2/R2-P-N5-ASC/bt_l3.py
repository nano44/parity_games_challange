# REFEREE-2 32: byte test of P-N5-ASC line L-3 (claude/l-new a2512364) = L-2 + CHECKER C135 §5 R1..R4 (own code)
import subprocess, hashlib
S = "a2512364"
sh = lambda f: subprocess.run(["git", "show", f"{S}:{f}"], capture_output=True).stdout
L2, L3 = sh("docs/new/P-N5-ASC-line-L2.txt"), sh("docs/new/P-N5-ASC-line-L3.txt")
t2, t3 = L2.decode(), L3.decode()
R = [("R1", "; L-NEW successor 61)", "; L-NEW successors 61-62)"),
     ("R2", "; §3-§5 do not use [E-LEV]; DATA, clause by clause",
      "; §3-§5 do not use [E-LEV]; the proof of record of HUB-ASC-G's B = 0 case (F′_0 = F_0, DESC-POLY on the whole interval) is referee-originated (REFEREE R-P-N5-ASC §3 AS-1, restated in P-N5-ASC's fixes entry 1 AS-1), signed by both referees; DATA, clause by clause"),
     ("R3", "so the e-vertices of one Λ-class form one forest whose paths are the sequences seq_t(v)", "hence seq_t(v) = (f, seq_t(y_f))"),
     ("R4", "with E_t(v) the set of e-vertices in Π_t(v),",
      "with seq_t(v) the e-vertices in Π_t(v) in play order, E_t(v) their set, an ascent of seq_t(v) a step to a more relevant element,")]
B = t2
for nm, o, n in R:
    print(nm, "old in L-2", t2.count(o), "| old in L-3", t3.count(o), "| new in L-3", t3.count(n)); assert B.count(o) == 1; B = B.replace(o, n)
print("L-2", hashlib.sha1(L2).hexdigest(), len(L2), "| L-3", hashlib.sha1(L3).hexdigest(), len(L3))
print("rebuild L-2 + R1..R4 equal to L-3:", B.encode() == L3, hashlib.sha1(B.encode()).hexdigest())
d = 0; neg = False
for c in t3: d += (c == "(") - (c == ")"); neg |= d < 0
print("L-3 newlines", t3.count("\n"), "parens", t3.count("("), t3.count(")"), "neg", neg, "pipes", t3.count("|"), "dashes « — »", t3.count(" — "))
mine = {"W-1 [E-LEV] scope (Add. 2: «under [E-LEV]» per UP-B/NOUP clause)": "under [E-LEV]",
        "W-3 new": "(consecutive state pair, W-target or c_W with Λ fixed) pairs", "W-3 old": "(consecutive state pair, W-target with Λ fixed) pairs",
        "W-4 clause": "UP-JUMP: violations 0 in 1,956 ascents of movers' plays with Λ below every e"}
for k, s in mine.items(): print(k, "| L-2", t2.count(s), "| L-3", t3.count(s))
