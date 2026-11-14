#!/usr/bin/env python3
"""Box 212 quote check (L-NEW successor 74; record tool, not run by check.sh: it needs git objects).
In docs/new/N5-RFLEVEL-box212.md, every «…» that follows a tag [Q X] in the same block (a bullet with its indented continuation lines,
or a paragraph), up to the next [Q …] tag, must occur verbatim (whitespace normalised) in its source:
  X = Rnnn         inside the entry «### Rnnn …» of docs/RESULTS.md at TRUNK (up to the next «### R» header);
  X = PATH@COMMIT  in the file PATH at COMMIT (any branch's commit; fetched objects needed).
Control QCTRL=1: every quote is altered, so every quote must be MISS.
Quotes outside a [Q] block (the Lead's messages in the header) are not checked by this tool.
Prints one line per quote and a last line «quotes N missing K (trunk SHA)»; exit 1 if K > 0.
Usage, from anywhere inside the repository: python3 experiments/new/box212/quotes212.py TRUNK_SHA [DOC]  (DOC default
docs/new/N5-RFLEVEL-box212.md; box 209 Addendum B: docs/new/N5-LEVEL3-box209.md, whose «[Q]» bullets are quotes209.py's and are skipped)"""
import os, re, subprocess, sys
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
DOC = "docs/new/N5-RFLEVEL-box212.md"
norm = lambda t: " ".join(t.split())
def show(sha, path):
    return subprocess.run(["git", "-C", ROOT, "show", f"{sha}:{path}"], capture_output=True, check=True).stdout.decode("utf-8")
def blocks(text):
    out, cur = [], None
    for line in text.split("\n"):
        if not line.strip() or line.startswith("#") or line.startswith("|"):
            if cur is not None: out.append(cur)
            cur = None
        elif re.match(r"\s*- ", line) or cur is None:
            if cur is not None: out.append(cur)
            cur = line
        else: cur += " " + line
    if cur is not None: out.append(cur)
    return out
def main(trunk, doc=DOC):
    full = subprocess.run(["git", "-C", ROOT, "rev-parse", trunk], capture_output=True, text=True, check=True).stdout.strip()
    entries, cur = {}, None
    for i, line in enumerate(show(full, "docs/RESULTS.md").split("\n"), 1):
        m = re.match(r"### (R\d+) ", line)
        if m: cur = m.group(1); entries[cur] = [i, []]
        if cur: entries[cur][1].append(line)
    cache = {}
    def source(tag):
        if tag in cache: return cache[tag]
        if re.fullmatch(r"R\d+", tag):
            v = entries.get(tag); cache[tag] = (f"RESULTS l. {v[0]}", norm("\n".join(v[1]))) if v else None
        else:
            path, sha = tag.rsplit("@", 1)
            try: cache[tag] = (f"{path}@{sha}", norm(show(sha, path)))
            except subprocess.CalledProcessError: cache[tag] = None
        return cache[tag]
    n = miss = 0
    for b in blocks(open(os.path.join(ROOT, doc), encoding="utf-8").read()):
        parts = re.split(r"\[Q ([^\]]+)\]", b)
        for k in range(1, len(parts), 2):
            tag, seg = parts[k], parts[k + 1]
            for q in re.findall(r"«([^«»]*)»", seg):
                n += 1; q = norm(q) + (" #" if os.environ.get("QCTRL") == "1" else ""); src = source(tag)
                ok = src is not None and q in src[1]; miss += not ok
                print(("OK   " if ok else "MISS ") + f"[{tag}] {src[0] if src else 'NO SOURCE'} | {q[:90]}")
    print(f"quotes {n} missing {miss} (trunk {full})")
    return 1 if miss else 0
if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:3]))
