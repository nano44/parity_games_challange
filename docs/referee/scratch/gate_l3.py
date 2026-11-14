"""REFEREE s31: P-N5-GATE L-3 byte test. Parses MY strings from my own report's §5 table (R-P-N5-GATE.md at a401ce0e, read from the repo),
checks: for each of my ids, its Old is gone from L-3 and (kind V/S) its New is present verbatim; then prints every hunk of L-2 -> L-3.
Usage: gate_l3.py REPORT.md L2.txt L3.txt"""
import sys, re, difflib
rep = open(sys.argv[1], encoding="utf-8").read(); L2 = open(sys.argv[2], encoding="utf-8").read(); L3 = open(sys.argv[3], encoding="utf-8").read()
sec = rep[rep.index("## 5. Line L-2"):rep.index("## 6. TARGET.md diff")]
rows = {}
for line in sec.splitlines():
    m = re.match(r"\| ([RDG]-[0-9a-c]+[ab]?)[^|]*\| «(.*)» \| «(.*)»", line)
    if m: rows[m.group(1)] = (m.group(2), m.group(3))
    m = re.match(r"\| (D-5b) \| «(.*)» \| «» ", line)
    if m: rows["D-5b"] = (m.group(2), "")
print("my ids parsed:", sorted(rows))
for k, (o, n) in sorted(rows.items()):
    print(f"{k}: old in L2 {L2.count(o)}, old in L3 {L3.count(o)}, new in L3 {L3.count(n) if n else '-'}")
print("lines", L3.count("\n"), "bars", L3.count("|"), "parens", L3.count("("), L3.count(")"))
d = 0; neg = False
for ch in L3:
    d += ch == "("; d -= ch == ")"; neg |= d < 0
print("depth never negative:", not neg)
for b in ["§2 (a)", "P-N5-CHAIN's C-EQUIV", "lie on both of two plays", "not a premise here", "not among P-N5-CHAIN", "while its play avoids", "over the run then", "CTRL=a0"]:
    print("absent?", b, L3.count(b))
a, b = re.split(r"(\s+)", L2), re.split(r"(\s+)", L3)
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
for i, (tag, i1, i2, j1, j2) in enumerate(op for op in sm.get_opcodes() if op[0] != "equal"):
    print(f"\n--- hunk {i} {tag}\nOLD: {''.join(a[i1:i2])}\nNEW: {''.join(b[j1:j2])}")
