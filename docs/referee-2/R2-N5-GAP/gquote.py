#!/usr/bin/env python3
"""REFEREE-2 succ. 21: quote check for P-N5-GAP. [Q SPEC:a-b] «…» against SPEC @ da3fa7fa (whitespace-normalised substring); the unmarked
«…» premise quotes (R15 (a), (d); R17 (a) F1; box10 [⊕], [V1], [V2]) against RESULTS / box10 @ da3fa7fa anywhere in the file. SHIFT=k control."""
import os, re, subprocess
SHIFT = int(os.environ.get("SHIFT", "0"))
show = lambda rev, p: subprocess.run(["git", "show", f"{rev}:{p}"], capture_output=True, text=True, check=True).stdout
norm = lambda s: re.sub(r"\s+", " ", s).strip()
pk = show("28ceeadc", "docs/new/P-N5-GAP-box69.md"); spec = show("da3fa7fa", "docs/new/N5-ssi-global.md").split("\n")
res = norm(show("da3fa7fa", "docs/RESULTS.md")); b10 = norm(show("da3fa7fa", "docs/new/N5-phase-bound-box10.md"))
ok = tot = 0
for m in re.finditer(r"\[Q SPEC:(\d+)(?:-(\d+))?\]\s*«(.*?)»", pk, re.S):
    a = int(m.group(1)) + SHIFT; b = int(m.group(2) or m.group(1)) + SHIFT; tot += 1
    hit = norm(m.group(3)) in norm(" ".join(spec[a - 1:b])); ok += hit
    print("OK  " if hit else "MISS", f"SPEC:{a}-{b}", norm(m.group(3))[:60])
if SHIFT == 0:
    for lab, src, rx in [("R15", res, r"\[R15\](.*?)\n- \[F1\]"), ("F1", res, r"\[F1\](.*?)\n- \[V1\]"), ("box10", b10, r"\[V1\], \[V2\], \[⊕\](.*?)These are facts")]:
        seg = re.search(rx, pk, re.S).group(1)
        for q in re.findall(r"«(.*?)»", seg, re.S):
            tot += 1; hit = norm(q) in src; ok += hit
            print("OK  " if hit else "MISS", lab, norm(q)[:60])
print(f"quotes={tot} ok={ok} SHIFT={SHIFT}")
