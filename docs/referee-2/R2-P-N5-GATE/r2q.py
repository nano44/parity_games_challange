#!/usr/bin/env python3
# REFEREE-2 successor 37: premise check for P-N5-GATE. (1) every «…» quote of line L-2 that names a landed source occurs verbatim
# (whitespace-normalised) in trunk docs/RESULTS.md; (2) every P-N5-CHAIN fact the packet names occurs as a defined name in CHAIN's frozen
# text (93531b03, sha1 6e613ba7); (3) the packet's glosses of F3, F6, (Core) and C-EQUIV against CHAIN / SPLIT.
# Usage: r2q.py L2.txt RESULTS.md CHAIN.md SPLIT.md GATE.md
import sys, re, hashlib
L2, RES, CH, SPL, GT = (open(p, encoding="utf-8").read() for p in sys.argv[1:6])
ws = lambda s: " ".join(s.split()); RESw, CHw, SPLw, GTw = ws(RES), ws(CH), ws(SPL), ws(GT)
print("CHAIN sha1", hashlib.sha1(open(sys.argv[3], "rb").read()).hexdigest()[:8], " SPLIT sha1", hashlib.sha1(open(sys.argv[4], "rb").read()).hexdigest()[:8],
      " GATE sha1", hashlib.sha1(open(sys.argv[5], "rb").read()).hexdigest()[:8])
qs = re.findall(r"«([^«»]*(?:«[^«»]*»[^«»]*)*)»", L2)
for q in qs:
    w = ws(q); where = [nm for nm, T in (("RESULTS", RESw), ("CHAIN", CHw), ("GATE", GTw)) if w in T]
    print(("FOUND " if where else "MISSING ") + ",".join(where) + " :: " + w[:110])
for nm in ["F1.", "F2.", "F3.", "F4′.", "F5.", "F6.", "DOM.", "STRICT.", "CYC.", "(E-DOM)", "(Core)", "Lemma CN2-3.", "Lemma LOC-GATE3.",
           "Corollary NO-TIE3.", "Lemma LOC-K2-3.", "Lemma B-ONLY3.", "E-MON3", "[OPT]"]:
    print("CHAIN defines", nm, CH.count(nm) > 0)
print("C-EQUIV in CHAIN:", CH.count("C-EQUIV"), " in SPLIT:", SPL.count("**Corollary C-EQUIV.**"))
print("GATE's F3 gloss  :", "F3 (E_t(v) is the set of e-vertices on v's play at t more relevant than Λ_t(v))" in GTw)
print("CHAIN's F3 starts:", re.search(r"- F3\. ([^\n]{0,80})", CH).group(1))
print("GATE's F6 gloss  :", "F6 (an e-vertex has exactly one successor, its W-target)" in GTw)
print("CHAIN's F6 starts:", re.search(r"- F6\. ([^\n]{0,120})", CH).group(1))
print("GATE's (Core) gloss (global form):", "(Core) (K0, K3 lie on both of two plays with the same Λ or on neither)" in GTw)
print("SPLIT §2 has an item (a):", bool(re.search(r"## 2\..*?\n- \(a\)", SPL, re.S) and SPL.index("## 3.") > SPL.index("- (a)")))
print("SPLIT §3 (a) is the mover chain:", "- (a), u a mover." in SPL)
print("GATE cites SPLIT «§2 (a)»:", GT.count("§2 (a)"), " L-2:", L2.count("§2 (a)"))
print("GATE cites «P-N5-CHAIN (C-EQUIV)»:", GT.count("P-N5-CHAIN (C-EQUIV)"), " L-2 «P-N5-CHAIN's C-EQUIV»:", L2.count("P-N5-CHAIN's C-EQUIV"))
print("GATE cites L-RED R228 §2 in EXPEL-COUNT's proof:", "(≤ 3M; L-RED R228 §2)" in GTw)
print("GATE cites N5-CORE-forms for A*-EQUIV (i):", "N5-CORE-forms §3 (5): cited, not re-proved here" in GTw)
