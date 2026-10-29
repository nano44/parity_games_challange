# Quote check for docs/si/P-N5-COMPOSE-fixes-box28.md (L-SI successor 26; form of docs/lit/P-N5-MPGS-fixes-quotecheck.py).
# Every [Q path@commit:a-b] «text» in the "Quote pins" section must (a) equal, after collapsing whitespace, a substring of lines a..b of
# that file at that commit (joined by spaces, whitespace collapsed), and (b) occur, whitespace collapsed, in the file above that section.
# Run from the repository root: python3 -I docs/si/P-N5-COMPOSE-fixes-quotecheck.py [file]   -> prints "quotes=N bad=M"
import re, subprocess, sys
txt = open(sys.argv[1] if len(sys.argv) > 1 else "docs/si/P-N5-COMPOSE-fixes-box28.md", encoding="utf-8").read()
body, pins = txt.split("\n## Quote pins", 1)
body = " ".join(body.split())
qs = re.findall(r"\[Q ([^@\]]+)@([0-9a-f]+):(\d+)-(\d+)\] «([^»]*)»", pins)
bad = 0
for path, sha, a, b, q in qs:
    lines = subprocess.run(["git", "show", f"{sha}:{path}"], capture_output=True, text=True, check=True).stdout.splitlines()
    src = " ".join(" ".join(lines[int(a) - 1:int(b)]).split())
    qn = " ".join(q.split())
    if qn not in src:
        bad += 1; print("BAD source", path, sha, a, b, q[:60])
    if qn not in body:
        bad += 1; print("BAD body", q[:60])
print(f"quotes={len(qs)} bad={bad}")
