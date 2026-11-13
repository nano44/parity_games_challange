#!/usr/bin/env python3
"""Box 108 (L-SI 56): quote check.  Every top-level «...» quote of §1.1 of the proof file, of the statement of Theorem GK (§0) and of
the STOP bullet («- t = L = T_k (STOP)») must occur in docs/red/P-N5-REALIZE.md (RESULTS R104's packet), whitespace-normalised; «…» inside a quote marks an omission (the
pieces are checked separately, in order).  argv: PROOF.md PACKET.md.  Control: QUOTES108_CTRL=1 alters one quote (must FAIL)."""
import sys, os, re
def top_quotes(text):
    out = []; depth = 0; start = None
    for i, ch in enumerate(text):
        if ch == "«":
            if depth == 0: start = i + 1
            depth += 1
        elif ch == "»" and depth > 0:
            depth -= 1
            if depth == 0: out.append(text[start:i])
    return out
norm = lambda z: re.sub(r"\s+", " ", z).strip()
doc = open(sys.argv[1], encoding="utf-8").read(); src = norm(open(sys.argv[2], encoding="utf-8").read())
REGIONS = [("### 1.1", "### 1.2"), ("- **Theorem GK", "- **Corollary SW"), ("- t = L = T_k (STOP)", "**Proof of Corollary SW")]
part = ""
for a, b in REGIONS:
    i = doc.index(a); part += doc[i:doc.index(b, i)] + "\n"
qs = top_quotes(part)
if os.environ.get("QUOTES108_CTRL") == "1": qs[0] = qs[0].replace("level", "layer", 1)
fail = 0; pieces = 0
for q in qs:
    pos = 0
    for piece in [norm(p) for p in q.split("…") if norm(p)]:
        pieces += 1; j = src.find(piece, pos)
        if j < 0: fail += 1; print("QUOTE NOT FOUND:", piece[:100])
        else: pos = j + len(piece)
print(f"QUOTES108 quotes {len(qs)} pieces {pieces} fail {fail}"); sys.exit(1 if fail or not qs else 0)
