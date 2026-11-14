#!/usr/bin/env python3
"""L-SI P-N5-GATE line L-2 = line L-1 (docs/si/P-N5-GATE-line-L1.txt, sha1 a44647db…) with fixes entry 2 applied: three replacements, each
Old asserted exactly once in L-1. Prints L-2 (one line). Usage: mkL2.py ROOT"""
import hashlib, os, sys
ROOT = sys.argv[1]
raw = open(os.path.join(ROOT, "docs/si/P-N5-GATE-line-L1.txt"), "rb").read()
assert hashlib.sha1(raw).hexdigest() == "a44647db487dcd5193d11ff83f80006b3533dac4"
L = raw.decode("utf-8")
R = [
 ("the proviso «D's play avoids e_o» of E-FACE-PAYS (c) and WAIT-QUIET is a hypothesis here;",
  "on IDEAL-CYC the proviso «D's play avoids e_o» of E-FACE-PAYS (c) and WAIT-QUIET always holds (Lemma PROVISO, credit L-RED 63: if "
  "e_o lay on P_t(D), the play would close at D, the vertex after e_o, so its cycle would carry e_o and Λ_t(D) would be at least as "
  "relevant as e_o, against RESULTS R123 B-ONLY at the mover D; D = c_W is its own loop), so on IDEAL-CYC E-FACE-PAYS (b) holds at every "
  "step and (c) and WAIT-QUIET hold with no proviso, B-ONLY being the one premise shared with the K10 clause above, while on Γ3 the "
  "proviso is a hypothesis here;"),
 ("claude/l-red fa4e50fe R229-box93 §2);",
  "claude/l-red fa4e50fe R229-box93 §2); PROVISO: dpass 0 (unit (gate, state); 19 instances, box 91's 11 and box 93's 8, 307,737 pairs "
  "per engine; both engines, rows identical; experiments/si/box96 d96.py), and the control with Odd made non-optimal (own engine; e-face at o, "
  "β-face at every other gate) fires on 14 of the 19;"),
 ("with its fixes entry 1, docs/si/P-N5-GATE-fixes.md", "with its fixes entries 1-2, docs/si/P-N5-GATE-fixes.md"),
]
for a, b in R:
    assert L.count(a) == 1, a[:60]
    L = L.replace(a, b)
assert "|" not in L and L.count("\n") == 1 and L.endswith("\n")
sys.stdout.write(L)
