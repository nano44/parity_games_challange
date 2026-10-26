#!/usr/bin/env python3
"""L-SI (successor 14): check every verbatim quote of a fixes file. A quote is written
  [Q path@commit:L] «text»   or   [Q path@commit:L1-L2] «text»
and must occur in `git show commit:path`, lines L..L2 joined, after whitespace normalisation; "…" inside the text separates parts, each of
which must occur, in order. Prints one line per quote and QUOTES PASS / QUOTES FAIL. Usage: quotecheck.py FILE [--mut] (--mut: shift every
line range by one, a control that must fail)."""
import re, subprocess, sys

def norm(s): return " ".join(s.split())

def main():
    path = sys.argv[1]; mut = "--mut" in sys.argv
    text = open(path, encoding="utf-8").read()
    pat = re.compile(r"\[Q\s+([^@\]\s]+)@([0-9a-f]{7,40}):(\d+)(?:-(\d+))?\]\s*«(.*?)»", re.S)
    n = bad = 0; cache = {}
    for m in pat.finditer(text):
        f, c, a, b, q = m.group(1), m.group(2), int(m.group(3)), int(m.group(4) or m.group(3)), norm(m.group(5))
        if mut: a, b = a + 1, b + 1
        if (c, f) not in cache:
            cache[(c, f)] = subprocess.run(["git", "show", f"{c}:{f}"], capture_output=True, text=True, check=True).stdout.splitlines()
        lines = cache[(c, f)]; src = norm(" ".join(lines[a - 1:b]))
        pos, ok = 0, True
        for part in [norm(p) for p in q.split("…") if norm(p)]:
            i = src.find(part, pos)
            if i < 0: ok = False; break
            pos = i + len(part)
        n += 1; bad += not ok
        print(("OK  " if ok else "BAD ") + f"{f}@{c}:{a}-{b}  «{q[:70]}{'…' if len(q) > 70 else ''}»")
    print(f"quotes={n} bad={bad}")
    print("QUOTES PASS" if n and not bad else "QUOTES FAIL")

if __name__ == "__main__":
    main()
