# Quote check for docs/lit/P-N5-MPGS.md (L-LIT). Every [Q path@commit:line] «text» must be a substring of that line at that commit.
# Run from the repository root: python3 -I docs/lit/P-N5-MPGS-quotecheck.py   -> prints "quotes=N bad=M"
import re, subprocess
txt = open("docs/lit/P-N5-MPGS.md", encoding="utf-8").read()
qs = re.findall(r"\[Q ([^@\]]+)@([0-9a-f]+):(\d+)\] «([^»]*)»", txt)
bad = 0
for path, sha, ln, q in qs:
    lines = subprocess.run(["git", "show", f"{sha}:{path}"], capture_output=True, text=True, check=True).stdout.splitlines()
    if q not in lines[int(ln) - 1]:
        bad += 1; print("BAD", path, sha, ln, q[:60])
print(f"quotes={len(qs)} bad={bad}")
