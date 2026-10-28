#!/usr/bin/env python3
"""L-NEW box 49 (successor 30): check every verbatim quote of a fixes file. Format and rules are L-SI's experiments/si/rund/quotecheck.py
(successor 14), copied, not imported:
  [Q path@commit:L] «text»   or   [Q path@commit:L1-L2] «text»
The text must occur in `git show commit:path`, lines L..L2 joined, after whitespace normalisation; "…" inside the text separates parts, each
of which must occur, in order. Prints one line per quote and QUOTES PASS / QUOTES FAIL; exit 1 on FAIL.
Usage: quotecheck3.py FILE [--mut | --locate]
  --mut     shift every line range by one (a control that must FAIL);
  --locate  for tags written [Q path@commit:?], print the smallest line range that holds the quote (authoring aid; the check is the default mode).
Run from the repository root."""
import re, subprocess, sys

def norm(s): return " ".join(s.split())
CACHE = {}
def lines_of(c, f):
    if (c, f) not in CACHE:
        CACHE[(c, f)] = subprocess.run(["git", "show", f"{c}:{f}"], capture_output=True, text=True, check=True).stdout.splitlines()
    return CACHE[(c, f)]
def holds(src, q):
    pos = 0
    for part in [norm(p) for p in q.split("…") if norm(p)]:
        i = src.find(part, pos)
        if i < 0: return False
        pos = i + len(part)
    return True

def main():
    path = sys.argv[1]; mut = "--mut" in sys.argv; loc = "--locate" in sys.argv
    text = open(path, encoding="utf-8").read()
    pat = re.compile(r"\[Q\s+([^@\]\s]+)@([0-9a-f]{7,40}):(\?|\d+)(?:-(\d+))?\]\s*«(.*?)»", re.S)
    n = bad = 0
    for m in pat.finditer(text):
        f, c, q = m.group(1), m.group(2), norm(m.group(5))
        L = lines_of(c, f)
        if m.group(3) == "?":
            if not loc: n += 1; bad += 1; print(f"BAD {f}@{c}:? (unlocated)"); continue
            best = None
            for a in range(len(L)):
                for b in range(a, min(a + 12, len(L))):
                    if holds(norm(" ".join(L[a:b + 1])), q):
                        if best is None or b - a < best[1] - best[0]: best = (a, b)
                        break
            print(("LOC " + (f"{best[0] + 1}" + (f"-{best[1] + 1}" if best[1] > best[0] else "")) if best else "NOTFOUND") + f"  {f}@{c}  «{q[:60]}»")
            continue
        a, b = int(m.group(3)), int(m.group(4) or m.group(3))
        if mut: a, b = a + 1, b + 1
        ok = holds(norm(" ".join(L[a - 1:b])), q)
        n += 1; bad += not ok
        print(("OK  " if ok else "BAD ") + f"{f}@{c}:{a}-{b}  «{q[:70]}{'…' if len(q) > 70 else ''}»")
    if loc: return
    print(f"quotes={n} bad={bad}")
    print("QUOTES PASS" if n and not bad else "QUOTES FAIL")
    sys.exit(0 if n and not bad else 1)

if __name__ == "__main__":
    main()
