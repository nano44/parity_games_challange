#!/usr/bin/env python3
"""L-SI P-IDEAL-DBL fix round 2: print fixes entry 2 (appended once to docs/si/P-IDEAL-DBL-fixes.md; entry 1 unchanged). The R1-R6
map is mkL3.py's (MAP=1), copied from c133_8f6d03bc.md; sha1 and size of L-3 read from the file."""
import os, sys, subprocess, hashlib
H = os.path.dirname(os.path.abspath(__file__)); os.chdir(H)
mp = subprocess.run([sys.executable, "-I", "-B", "mkL3.py"], env=dict(os.environ, MAP="1"), capture_output=True, text=True, check=True).stderr
L3 = open("../../../docs/si/P-IDEAL-DBL-line-L3.txt", "rb").read()
o = ["", "## Entry 2 (fix round 2; L-SI successor 42; CHECKER C133 (claude/checker 8f6d03bc) FAILED R119's first fill with E-1..E-6; Lead",
     "12:08Z). Line only: no packet statement, proof or DATA changes. Strings copied by script (experiments/si/box79/mkL3.py) from",
     "experiments/si/box79/c133_8f6d03bc.md, a byte copy of docs/checker/C133.md at 8f6d03bc, §5 (wrapped lines joined with one space).",
     "- R1 (E-1) drops the «R1xx [refereed-only] » prefix; R2 (E-2) the source note (packet + fixes entry 1, L-SI successors 41-42); R3 (E-3)",
     "  the scope tail «(2026-11-07) — … not a TARGET.md claim»; R4 (E-6) the L41 note on DBL-EQ (b)'s window count (REFEREE's DB-3, entry 1",
     "  F-3, found independently by REFEREE-2) inside R3's tail; R5 (E-4) PASS-FREEZE «for 1 ≤ l ≤ d − 2»; R6 (E-5) FUEL-EXACT «on 𝓛^R_d».",
     "- Line L-3 = L-2 with R1-R6 applied in this order (each old string once in the text it is applied to, R4's inside R3's new text):"]
for ln in mp.strip().split("\n"):
    o.append(("  " + ln) if ln.startswith("  ") else ("  - " + ln))
o.append("- docs/si/P-IDEAL-DBL-line-L3.txt: sha1 %s, %s B with its newline, 1 line, %d «(» = %d «)», 0 «|», one « — », no «[»; equal to"
         % (hashlib.sha1(L3).hexdigest(), "{:,}".format(len(L3)), L3.count(b"("), L3.count(b")")))
o.append("  C133 §5's value 845ffdc9f0306d5db4bdb41d613588b219545838. L-1, L-2 and the packet are unchanged.")
sys.stdout.write("\n".join(o) + "\n")
