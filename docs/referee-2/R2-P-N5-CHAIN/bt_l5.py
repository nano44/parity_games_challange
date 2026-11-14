#!/usr/bin/env python3
"""REFEREE-2 successor 36: byte test of P-N5-CHAIN line L-5 (claude/l-new dd83371b). Own code; the lane generator is not run.
The three (old, new) pairs are parsed from fixes entry 4's «Line changes» bullets (R-U, R-L1, R-L2), whitespace inside a bullet
collapsed to one space (the bullets wrap). L-4 (a69c8aa9) + R-U + R-L1 + R-L2, each old exactly once in the line it is applied to and each
new once in the result, must equal L-5 (473344b1) byte for byte. Run from the repo root."""
import subprocess, re, hashlib
def show(p, rev="dd83371b"): return subprocess.run(["git", "show", f"{rev}:{p}"], capture_output=True, check=True).stdout
L4 = show("docs/new/P-N5-CHAIN-line-L4.txt"); L5 = show("docs/new/P-N5-CHAIN-line-L5.txt"); FX = show("docs/new/P-N5-CHAIN-fixes.md").decode()
print("L-4 sha1", hashlib.sha1(L4).hexdigest(), len(L4), "B;  L-5 sha1", hashlib.sha1(L5).hexdigest(), len(L5), "B")
e4 = FX[FX.index("## Fixes entry 4"):]; e4 = e4[e4.index("### Line changes"):e4.index("### Line L-5")]
bul = re.split(r"\n- ", e4)[1:]
pairs = []
for b in bul:
    b = " ".join(b.split()); m = re.match(r"(R-\w+): «(.*)» → «(.*)»$", b)
    assert m, b[:80]; pairs.append(m.groups())
cur = L4.decode()
for k, o, n in pairs:
    c = cur.count(o); print(k, "old count in line", c, "| new count before", cur.count(n)); assert c == 1, k
    cur = cur.replace(o, n); print(k, "new count after", cur.count(n))
print("pairs", [p[0] for p in pairs]); res = cur.encode()
print("L-4 + pairs == L-5:", res == L5, "| sha1", hashlib.sha1(res).hexdigest(), len(res), "B")
t = L5.decode()
print("one line", t.count("\n") == 1 and t.endswith("\n"), "| «|»", t.count("|"), "| ( )", t.count("("), t.count(")"),
      "| unlanded/not landed/when landed/to land", [t.count(s) for s in ("unlanded", "not landed", "when landed", "to land")])
print("CONDITIONAL count", t.count("CONDITIONAL"), "| «CONDITIONAL on P-N5-END's Theorem ENDGAME-3 (RESULTS R124)»:", "CONDITIONAL on P-N5-END's Theorem ENDGAME-3 (RESULTS R124)" in t)
