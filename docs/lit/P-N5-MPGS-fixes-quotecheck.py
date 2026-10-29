# Quote check for docs/lit/P-N5-MPGS-fixes.md (L-LIT). Every [Q path@commit:a-b] «text» must equal, after collapsing whitespace,
# a substring of lines a..b of that file at that commit (joined by spaces, whitespace collapsed).
# Run from the repository root: python3 -I docs/lit/P-N5-MPGS-fixes-quotecheck.py   -> prints "quotes=N bad=M"
import re, subprocess
txt = open("docs/lit/P-N5-MPGS-fixes.md", encoding="utf-8").read()
qs = re.findall(r"\[Q ([^@\]]+)@([0-9a-f]+):(\d+)-(\d+)\] «([^»]*)»", txt)
bad = 0
for path, sha, a, b, q in qs:
    lines = subprocess.run(["git", "show", f"{sha}:{path}"], capture_output=True, text=True, check=True).stdout.splitlines()
    src = " ".join(" ".join(lines[int(a) - 1:int(b)]).split())
    if " ".join(q.split()) not in src:
        bad += 1; print("BAD", path, sha, a, b, q[:60])
print(f"quotes={len(qs)} bad={bad}")
