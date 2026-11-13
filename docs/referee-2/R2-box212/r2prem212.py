#!/usr/bin/env python3
"""REFEREE-2 40: which premises of box 212 are LANDED (an entry «### R<nn> » in docs/RESULTS.md at TRUNK), by script.
For the not-landed premises it checks that no RESULTS header names them, and reads the G-N5-TIME row of docs/GAPS.md.
Usage: r2prem212.py TRUNK [--ctrl]   (--ctrl: asks for R999, which must be reported NOT landed)."""
import sys, re, subprocess
tr = sys.argv[1]; ctrl = "--ctrl" in sys.argv
show = lambda p: subprocess.run(["git", "show", f"{tr}:{p}"], capture_output=True, text=True, check=True).stdout
res = show("docs/RESULTS.md"); heads = [l for l in res.splitlines() if l.startswith("### R")]
ids = {re.match(r"### (R\d+) ", h).group(1): h for h in heads if re.match(r"### (R\d+) ", h)}
landed = [("R15", "F1 source, Lemma A (RF-A, every rule)"), ("R117", "Γ3(G) (RF-D)"), ("R118", "IDEAL-CYC (a), BR-SEG-G (i) (Howard remark)"),
          ("R121", "E-DOM"), ("R123", "CN2, B-ONLY, NO-TIE, LOC-GATE, LOC-K2"), ("R124", "standard states (RF-D)"),
          ("R125", "CN2-3, LOC-GATE3, LOC-K2-3, B-ONLY3, NO-TIE3, (Core) (RF-D)"), ("R126", "QUIET-N (RF-C Howard remark)")]
if ctrl: landed.append(("R999", "control"))
for r, use in landed:
    print("LANDED    " if r in ids else "NOT LANDED", r, "|", use, "|", (ids.get(r, "")[:110]))
print("highest R id on trunk:", max(int(k[1:]) for k in ids))
for pat, what in [("P-N5-LEVEL", "P-N5-LEVEL (packet, RF-A..RF-C re-use its proofs; to land as R129 per the Lead's numbering)"),
                  ("box 209", "box 209 LEVEL3 (RF-D [L3])"), ("LEVEL3", "box 209 LEVEL3 (RF-D [L3])"), ("W-FLAT", "box 104 W-FLAT (RF-D [IMP3])"),
                  ("RF-LEVEL", "box 212 itself"), ("RF-A", "box 212 itself")]:
    hit = [h[:80] for h in heads if pat in h]
    print("in a RESULTS header" if hit else "in NO RESULTS header", "|", pat, "|", what, "|", hit[:2])
gaps = show("docs/GAPS.md")
row = [l for l in gaps.splitlines() if l.startswith("| G-N5-TIME ")]
print("GAPS G-N5-TIME:", (row[0].split("|")[4].strip() if row else "ROW MISSING"))
