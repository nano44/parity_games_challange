#!/usr/bin/env python3
"""REFEREE successor 36: quote check of P-N5-EXP (own script; the lane's b6quote.py is not used).

Usage: gkx_quotes.py PACKET LABEL=FILE ...
Every guillemet segment that follows a tag [Q LABEL ...] (consecutive segments separated by white space only belong to the
same tag) must occur verbatim in FILE (white space normalised on both sides, nothing else). Nested guillemets are kept.
Untagged guillemet segments of 25 characters or more are listed with the sources they occur in (or NONE): these are the
packet's own phrases or untagged citations; a reader decides which.
"""
import sys, re, hashlib

def norm(t):
    return " ".join(t.split())

def segments(text):
    """Top-level guillemet segments with their start offsets (nesting-aware)."""
    out = []
    depth = 0
    start = None
    for i, ch in enumerate(text):
        if ch == "«":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "»":
            depth -= 1
            if depth == 0:
                out.append((start, i + 1))
            assert depth >= 0, f"unbalanced at {i}"
    assert depth == 0, "unbalanced guillemets"
    return out

def main():
    pk = open(sys.argv[1], encoding="utf-8").read()
    src = {}
    for a in sys.argv[2:]:
        lab, f = a.split("=", 1)
        raw = open(f, "rb").read()
        src[lab] = norm(raw.decode("utf-8"))
        print(f"source {lab} sha1 {hashlib.sha1(raw).hexdigest()} bytes {len(raw)}")
    segs = segments(pk)
    tags = [(m.start(), m.end(), m.group(1)) for m in re.finditer(r"\[Q ([A-Z0-9]+)[^\]]*\]", pk)]
    tagged = {}
    for (ts, te, lab) in tags:
        pos = te
        while True:
            nxt = [s for s in segs if s[0] >= pos]
            if not nxt:
                break
            s = nxt[0]
            if pk[pos:s[0]].strip() != "":
                break
            tagged[s] = lab
            pos = s[1]
    found = notfound = 0
    for s in segs:
        if s in tagged:
            lab = tagged[s]
            q = norm(pk[s[0] + 1:s[1] - 1])
            ok = q in src[lab]
            found += ok
            notfound += (not ok)
            line = pk.count("\n", 0, s[0]) + 1
            print(f"{'FOUND' if ok else 'NOTFOUND'} {lab} packet l. {line} «{q[:70]}»")
    print(f"tags {len(tags)} tagged_quotes {found + notfound} found {found} notfound {notfound}")
    for s in segs:
        if s not in tagged:
            q = norm(pk[s[0] + 1:s[1] - 1])
            if len(q) >= 25:
                where = [lab for lab in src if q in src[lab]]
                line = pk.count("\n", 0, s[0]) + 1
                print(f"UNTAGGED packet l. {line} in {','.join(where) if where else 'NONE'} «{q[:90]}»")

if __name__ == "__main__":
    main()
