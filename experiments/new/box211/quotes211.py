#!/usr/bin/env python3
"""P-N5-LEVEL quote check (L-NEW successor 73; record tool, not run by check.sh: it needs git objects).
Every «…» on a bullet of docs/new/P-N5-LEVEL.md that starts with a tag [Q X] must occur verbatim (whitespace normalised):
  X = Rnnn        inside the entry «### Rnnn …» of docs/RESULTS.md at the given trunk commit (up to the next «### R» header);
  X = P-N5-XICYC  in docs/new/P-N5-XICYC.md at that commit, whose sha1 must be 149e2414… (the packet landed as R118);
  X = P-N5-QN     in docs/new/P-N5-QN.md at that commit, whose sha1 must be 97254bd2… (the packet landed as R126);
  X = TARGET      in TARGET.md at that commit.
A bullet is a line «- …» (any indent) with its indented continuation lines. Prints one line per quote and a last line
«quotes N missing K (trunk SHA)»; exit 1 if K > 0 or a pinned sha1 differs.
Usage, from anywhere inside the repository: python3 experiments/new/box211/quotes211.py TRUNK_SHA"""
import hashlib, os, re, subprocess, sys
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
PINNED = {"P-N5-XICYC": ("docs/new/P-N5-XICYC.md", "149e2414be657ba12472faa4f46d5a251f2d3e98"),
          "P-N5-QN": ("docs/new/P-N5-QN.md", "97254bd2a97f28bb0c14ab5f4d236ee723821dd9")}
norm = lambda t: " ".join(t.split())
def show(sha, path):
    return subprocess.run(["git", "-C", ROOT, "show", f"{sha}:{path}"], capture_output=True, check=True).stdout
def main(sha):
    full = subprocess.run(["git", "-C", ROOT, "rev-parse", sha], capture_output=True, text=True, check=True).stdout.strip()
    res = show(full, "docs/RESULTS.md").decode("utf-8")
    entries, cur = {}, None
    for i, line in enumerate(res.split("\n"), 1):
        m = re.match(r"### (R\d+) ", line)
        if m: cur = m.group(1); entries[cur] = [i, []]
        if cur: entries[cur][1].append(line)
    src = {k: (f"RESULTS l. {v[0]}", norm("\n".join(v[1]))) for k, v in entries.items()}
    bad = 0
    packet = open(os.path.join(ROOT, "docs/new/P-N5-LEVEL.md"), encoding="utf-8").read()
    for tag, (path, want) in PINNED.items():
        raw = show(full, path); got = hashlib.sha1(raw).hexdigest()
        ok = got == want and want in packet
        print(("PIN  " if ok else "PINFAIL ") + f"{path} sha1 {got} (pinned {want}; named in the packet: {want in packet})"); bad += not ok
        src[tag] = (path, norm(raw.decode("utf-8")))
    src["TARGET"] = ("TARGET.md", norm(show(full, "TARGET.md").decode("utf-8")))
    bullets, cur = [], None
    for line in packet.split("\n"):
        if re.match(r"\s*- ", line):
            if cur is not None: bullets.append(cur)
            cur = line
        elif cur is not None and line.startswith(" ") and line.strip(): cur += " " + line
        else:
            if cur is not None: bullets.append(cur)
            cur = None
    if cur is not None: bullets.append(cur)
    n = miss = 0
    for b in bullets:
        m = re.match(r"\s*- \[Q ([^\]]+)\]", b)
        if not m: continue
        tag = m.group(1)
        for q in re.findall(r"«([^«»]*)»", b):
            n += 1; q = norm(q)
            if tag not in src: print(f"MISS [{tag}] unknown source | {q[:90]}"); miss += 1; continue
            where, text = src[tag]; ok = q in text; miss += not ok
            print(("OK   " if ok else "MISS ") + f"[{tag}] {where} | {q[:90]}")
    print(f"quotes {n} missing {miss} (trunk {full})")
    return 1 if (miss or bad) else 0
if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
