"""REFEREE successor 28: every «…» in a P-N5-QUIET text (packet, fixes, or line), searched verbatim (fragments split at '…', wrapped
lines joined by one space) per '### R<k>' entry of trunk RESULTS.md and in the named frozen files. Nested «…» inside a quote: the inner
quote is searched separately (outer quotes that contain « are reported as such).
Usage: quiet_quotes.py RESULTS TEXT name1=FILE1 [name2=FILE2 ...]"""
import sys, re
J = lambda t: re.sub(r"\s*\n\s*", " ", t)
R = open(sys.argv[1], encoding="utf-8").read(); P = J(open(sys.argv[2], encoding="utf-8").read())
O = {a.split("=", 1)[0]: J(open(a.split("=", 1)[1], encoding="utf-8").read()) for a in sys.argv[3:]}
ents = [(m.start(), m.group(1)) for m in re.finditer(r"^### (R\d+|DE\d+)", R, re.M)]
spans = [(nm, J(R[s:(ents[i + 1][0] if i + 1 < len(ents) else len(R))])) for i, (s, nm) in enumerate(ents)]
n = ok = 0
for q in re.findall(r"«([^«»]*)»", P):
    q = q.strip(); fr = [f.strip() for f in q.split("…") if f.strip()]; n += 1
    hit = [nm for nm, t in spans if all(f in t for f in fr)]; oh = [k for k, t in O.items() if all(f in t for f in fr)]
    ok += bool(hit or oh); print(f"RESULTS {hit or 'NONE'} | files {oh or 'NONE'} | {q[:120]}")
print(f"quotes {n}, found {ok}, not found {n - ok}")
