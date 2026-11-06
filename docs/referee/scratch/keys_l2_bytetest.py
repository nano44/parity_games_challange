#!/usr/bin/env python3
"""REFEREE successor 24: byte test of P-IDEAL-KEYS line L-2 = L-1 + the replacements R1..R10 of fixes entry 1, parsed from the fixes
file itself (lines «  - Rn (...) ...: «old» → «new»», wrapped lines joined with single spaces; nested guillemets handled).
Usage: python3 -I keys_l2_bytetest.py L1.txt fixes.md L2.txt"""
import hashlib, re, sys
l1 = open(sys.argv[1], "rb").read().decode(); fx = open(sys.argv[2]).read(); l2 = open(sys.argv[3], "rb").read()
sec = fx[fx.index("### Line L-2"):fx.index("- Word diff")]
items, cur = [], None
for ln in sec.split("\n"):
    m = re.match(r"  - (R\d+) (.*)", ln)
    if m: cur = [m.group(1), m.group(2)]; items.append(cur)
    elif cur and ln.startswith("    "): cur[1] += " " + ln.strip()
    else: cur = None
def spans(t):
    out, i = [], 0
    while i < len(t):
        if t[i] == "«":
            d, j = 0, i
            while True:
                if t[j] == "«": d += 1
                elif t[j] == "»":
                    d -= 1
                    if d == 0: break
                j += 1
            out.append((i, j)); i = j + 1
        else: i += 1
    return out
out = l1
for name, txt in items:
    sp = spans(txt)
    # the pair is the last two top-level spans separated by « → »
    (a0, a1), (b0, b1) = sp[-2], sp[-1]
    assert txt[a1 + 1:b0] == " → ", (name, txt[a1 + 1:b0])
    old, new = txt[a0 + 1:a1], txt[b0 + 1:b1]
    print(name, "occurrences in L-1:", l1.count(old), "in current:", out.count(old), "len", len(old), "->", len(new))
    assert out.count(old) == 1
    out = out.replace(old, new)
exp = out.encode()
print("replacements", len(items), "expected sha1", hashlib.sha1(exp).hexdigest(), "bytes", len(exp))
print("L-2 sha1", hashlib.sha1(l2).hexdigest(), "bytes", len(l2), "EQUAL:", l2 == exp)
s = l2.decode(); d = m = 0
for ch in s:
    d += (ch == "(") - (ch == ")"); m = min(m, d)
print("( ", s.count("("), ") ", s.count(")"), "min depth", m, "| ", s.count("|"), "lines", s.count("\n"), "« ", s.count("«"), "» ", s.count("»"),
      "DEAD:", s.count("DEAD"), "tower", s.count("tower"))
