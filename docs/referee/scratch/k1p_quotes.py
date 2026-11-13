#!/usr/bin/env python3
"""REFEREE successor 36: quote check of P-N5-KEY1P (own script; the lane's quotes212.py is not used).

Usage: k1p_quotes.py PACKET RESULTS_FILE     (run from the repository root; needs `git` for path@commit labels)
A tag is [Q LABEL]. LABEL = R<number>: the quote must occur inside the RESULTS entry «### R<number> […» of RESULTS_FILE (from its
heading to the next «### » heading). LABEL = path@commit: the quote must occur in `git show commit:path`. Every guillemet segment
that follows a tag (consecutive segments separated by at most 80 characters of connecting text without brackets or guillemets)
belongs to the tag. White space is normalised on both sides, nothing else.
"""
import sys, os, re, subprocess, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gkx_quotes import norm, segments

def results_entry(text, rid):
    m = re.search(r"^### " + re.escape(rid) + r" \[", text, re.M)
    if not m:
        return None
    n = re.search(r"^### ", text[m.end():], re.M)
    return text[m.start(): m.end() + (n.start() if n else len(text))]

def main():
    pk = open(sys.argv[1], encoding="utf-8").read()
    res = open(sys.argv[2], encoding="utf-8").read()
    print(f"RESULTS file sha1 {hashlib.sha1(res.encode('utf-8')).hexdigest()}")
    segs = segments(pk)
    tags = [(m.start(), m.end(), m.group(1).strip()) for m in re.finditer(r"\[Q ([^\]]+)\]", pk)]
    cache = {}
    def source(lab):
        if lab in cache:
            return cache[lab]
        if re.fullmatch(r"R\d+", lab):
            e = results_entry(res, lab)
            cache[lab] = norm(e) if e else None
        elif "@" in lab:
            path, commit = lab.rsplit("@", 1)
            r = subprocess.run(["git", "show", f"{commit}:{path}"], capture_output=True)
            cache[lab] = norm(r.stdout.decode("utf-8")) if r.returncode == 0 else None
        else:
            cache[lab] = None
        return cache[lab]
    glue = re.compile(r"^[^«»\[\]]{0,80}$", re.S)      # at most 80 characters of connecting text, no bracket, no guillemet
    found = notfound = nosrc = 0
    seen = set()
    for (ts, te, lab) in tags:
        pos = te
        n_here = 0
        while True:
            nxt = [s for s in segs if s[0] >= pos]
            if not nxt:
                break
            s = nxt[0]
            if not glue.match(pk[pos:s[0]]):
                break
            q = norm(pk[s[0] + 1:s[1] - 1])
            src = source(lab)
            line = pk.count("\n", 0, s[0]) + 1
            if src is None:
                nosrc += 1
                print(f"NOSOURCE {lab} packet l. {line}")
            else:
                ok = q in src
                found += ok
                notfound += (not ok)
                print(f"{'FOUND' if ok else 'NOTFOUND'} {lab} packet l. {line} «{q[:80]}»")
            seen.add(s)
            n_here += 1
            pos = s[1]
        if n_here == 0:
            print(f"TAG WITHOUT QUOTE {lab} packet l. {pk.count(chr(10), 0, ts) + 1}")
    print(f"tags {len(tags)} tagged_quotes {found + notfound + nosrc} found {found} notfound {notfound} nosource {nosrc}")
    for s in segs:
        if s not in seen:
            q = norm(pk[s[0] + 1:s[1] - 1])
            if len(q) >= 40:
                print(f"UNTAGGED packet l. {pk.count(chr(10), 0, s[0]) + 1} «{q[:100]}»")

if __name__ == "__main__":
    main()
