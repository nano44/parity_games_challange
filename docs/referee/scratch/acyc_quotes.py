"""REFEREE successor 28: every «…» in the frozen P-ACYC packet (all sections), searched verbatim (fragments split at '…') in trunk
docs/RESULTS.md and trunk docs/new/N5-ssi-global.md, wrapped lines joined by one space (RESULTS sub-entries are wrapped). For each hit
in RESULTS: the '### R<k>' entry that contains it (entry = from its heading to the next heading). Usage: acyc_quotes.py RESULTS SPEC PACKET"""
import sys, re
def J(t): return re.sub(r"\s*\n\s*", " ", t)
R = open(sys.argv[1], encoding="utf-8").read(); SP = J(open(sys.argv[2], encoding="utf-8").read()); P = open(sys.argv[3], encoding="utf-8").read()
ents = [(m.start(), m.group(1)) for m in re.finditer(r"^### (R\d+|DE\d+)", R, re.M)]
def entry_of(pos_raw):
    e = None
    for s, nm in ents:
        if s <= pos_raw: e = nm
    return e
# map joined positions back: search per entry in joined form
spans = [(nm, J(R[s:(ents[i + 1][0] if i + 1 < len(ents) else len(R))])) for i, (s, nm) in enumerate(ents)]
sec = None; n = ok = 0
for m in re.finditer(r"«([^»]*)»|^(## [^\n]*)$", P, re.M):
    if m.group(2): sec = m.group(2)[:30]; continue
    q = J(m.group(1)); fr = [f.strip() for f in q.split("…") if f.strip()]; n += 1
    hit = [nm for nm, t in spans if all(f in t for f in fr)]; sp = all(f in SP for f in fr)
    ok += bool(hit or sp)
    print(f"[{sec}] RESULTS entries {hit or 'NONE'} | SPEC {sp} | {q[:110]}")
print(f"quotes {n}, found {ok}, not found {n - ok}")
