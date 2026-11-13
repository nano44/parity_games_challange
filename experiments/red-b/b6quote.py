#!/usr/bin/env python3
"""L-RED-B: quote check for a packet. Every «...» that follows a tag [Q LABEL ...] in the packet (in the same paragraph or bullet,
up to the next blank line or the next [Q tag) must occur VERBATIM (white space normalised) in the source file given for LABEL.
Prints one line per quote: LABEL, FOUND l. a-b (line numbers in the source) or NOT-FOUND, and the first 60 characters; then a
summary «quotes N found F notfound K»; exit 1 if K > 0. Nested «» inside a quote belong to the quote.
A quote may contain « … » (space, ellipsis, space) to skip text: each piece must then occur, in order.
Usage: b6quote.py PACKET.md LABEL=SOURCE ...     (LABEL is the first word after «[Q »)"""
import sys, re, hashlib


def norm_with_lines(text):
    out = []
    ln = []
    for i, line in enumerate(text.split("\n"), 1):
        for tok in line.split():
            if out:
                out.append(" ")
                ln.append(i)
            for ch in tok:
                out.append(ch)
                ln.append(i)
    return "".join(out), ln


def quotes_after(par, pos):
    """top-level «...» spans in par[pos:]"""
    res = []
    depth = 0
    start = None
    for i in range(pos, len(par)):
        ch = par[i]
        if ch == "«":
            if depth == 0:
                start = i + 1
            depth += 1
        elif ch == "»" and depth > 0:
            depth -= 1
            if depth == 0:
                res.append(par[start:i])
    return res


if __name__ == "__main__":
    packet = open(sys.argv[1], encoding="utf-8").read()
    src = {}
    for a in sys.argv[2:]:
        lab, path = a.split("=", 1)
        t = open(path, encoding="utf-8").read()
        src[lab] = (path, norm_with_lines(t), hashlib.sha1(t.encode("utf-8")).hexdigest())
    for lab, (path, _, sha) in src.items():
        print(f"source {lab} = {path.split('/')[-1]} sha1 {sha}")
    n = found = 0
    for par in re.split(r"\n\s*\n", packet):
        tags = [(m.start(), m.end(), m.group(1)) for m in re.finditer(r"\[Q ([^\s\]]+)[^\]]*\]", par)]
        for i, (s, e, lab) in enumerate(tags):
            end = tags[i + 1][0] if i + 1 < len(tags) else len(par)
            for q in quotes_after(par[:end], e):
                n += 1
                if lab not in src:
                    print(f"{lab} NO-SOURCE «{' '.join(q.split())[:60]}»")
                    continue
                text, ln = src[lab][1]
                pieces = [" ".join(p.split()) for p in re.split(r"\s…\s", " ".join(q.split()))]
                at = 0
                ok = True
                first = last = None
                for p in pieces:
                    j = text.find(p, at)
                    if j < 0:
                        ok = False
                        break
                    if first is None:
                        first = ln[j]
                    last = ln[j + len(p) - 1]
                    at = j + len(p)
                if ok:
                    found += 1
                    print(f"{lab} FOUND l. {first}-{last} «{pieces[0][:60]}»")
                else:
                    print(f"{lab} NOT-FOUND «{pieces[0][:60]}»")
    print(f"quotes {n} found {found} notfound {n - found}")
    sys.exit(1 if n != found else 0)
