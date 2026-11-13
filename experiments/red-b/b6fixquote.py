#!/usr/bin/env python3
"""L-RED-B packet P-N5-EXP: quote check for the FIXES file docs/red-b/P-N5-EXP-fixes.md (entries 1-7).

Every guillemet quote that follows a Q-tag [Q LABEL ...] in the fixes file is checked verbatim by b6quote.py (same convention as
the packet). This wrapper only fetches the sources: each LABEL is a file at a NAMED COMMIT, read with `git show COMMIT:PATH` (the
commit must be in the clone: `git fetch origin <branch>` first), and for the labels R117, R124, R57 the source is trunk's
docs/RESULTS.md with every line outside that entry blanked (so a quote can only be found INSIDE the entry it is attributed to,
and the line numbers printed are the file's own).
  FROZEN  docs/red-b/P-N5-EXP.md in the working tree (sha1 must be c0449b17193f19619f33b366096762dfde27d542)
  REF2    claude/referee-2 33ff0e98  docs/referee-2/R2-P-N5-EXP.md          (REFEREE-2 41's second review)
  PRE     claude/referee   06ac891d  docs/referee/R-GK-precheck.md          (REFEREE 35's pre-check)
  REF1    claude/referee   c881709b  docs/referee/R-P-N5-EXP.md            (REFEREE 36's first review)
  R117, R124, R57          trunk 5d7aab0f docs/RESULTS.md, restricted to the entry
  R104P   trunk 5d7aab0f   docs/red/P-N5-REALIZE.md
  KEY1P   claude/l-new 44775605  docs/new/P-N5-KEY1P.md
  LNEW    claude/l-new aa29064d  docs/new/P-N5-KEY1P-after-EXP-draft.md
  n5v     claude/l-new a143d406  experiments/new/box190/n5v.py              (entry 1's tag)
  REF2B   claude/referee-2 f17a2708  docs/referee-2/R2-P-N5-EXP.md          (REFEREE-2 42's Addendum 2; entry 7's tag)
  REF1D   claude/referee   78515253  docs/referee/R-P-N5-EXP.md            (REFEREE 36's report with its stage 4; entry 7's tag)
  FIX5    claude/l-red-b   24f4d436  docs/red-b/P-N5-EXP-fixes.md           (this file as the referees read it: entries 1-5)
Usage (from anywhere inside the repository): b6fixquote.py WORKDIR [FIXESFILE]
  WORKDIR receives the source copies (WORKDIR/src/); the output is b6quote.py's (one line per quote, then «quotes N found F
  notfound K»); exit 1 if a source is missing or a quote is not found.
Control B6FQ_CTRL=1: one letter of every quote is changed before the check (every quote must then be NOT-FOUND)."""
import sys, os, subprocess, hashlib, re
HERE = os.path.dirname(os.path.abspath(__file__))
TOP = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=HERE, capture_output=True, text=True).stdout.strip()
SRC = {
    "REF2": ("33ff0e98911544cb18545541e4acbe71de84c6e0", "docs/referee-2/R2-P-N5-EXP.md", None),
    "PRE": ("06ac891df6f6212bac74259863da3105e7fe4341", "docs/referee/R-GK-precheck.md", None),
    "REF1": ("c881709b78d8e4b2debb72baf2c487156413416f", "docs/referee/R-P-N5-EXP.md", None),
    "R117": ("5d7aab0f19f664034567c3bf4f41bcf9e1684d20", "docs/RESULTS.md", "### R117 "),
    "R124": ("5d7aab0f19f664034567c3bf4f41bcf9e1684d20", "docs/RESULTS.md", "### R124 "),
    "R57": ("5d7aab0f19f664034567c3bf4f41bcf9e1684d20", "docs/RESULTS.md", "### R57 "),
    "R104P": ("5d7aab0f19f664034567c3bf4f41bcf9e1684d20", "docs/red/P-N5-REALIZE.md", None),
    "KEY1P": ("44775605d471b4f635a8c227b65744ac34bc6059", "docs/new/P-N5-KEY1P.md", None),
    "LNEW": ("aa29064d1beeaf7a25169ba273f323a187dbf4d0", "docs/new/P-N5-KEY1P-after-EXP-draft.md", None),
    "n5v": ("a143d4060d75f8463fe098b6ce18eef3febcd14b", "experiments/new/box190/n5v.py", None),
    "REF2B": ("f17a2708de653b306eaedf878f6120d2d0b31e06", "docs/referee-2/R2-P-N5-EXP.md", None),
    "REF1D": ("78515253a74a353a829b435d53f4987a8552989a", "docs/referee/R-P-N5-EXP.md", None),
    "FIX5": ("24f4d436a0fea1f62ae736f20f78ff9e84333a90", "docs/red-b/P-N5-EXP-fixes.md", None),
}
FROZEN_SHA1 = "c0449b17193f19619f33b366096762dfde27d542"


def restrict(text, head):
    lines = text.split("\n")
    starts = [i for i, l in enumerate(lines) if l.startswith(head)]
    if len(starts) != 1:
        raise SystemExit(f"b6fixquote: {len(starts)} lines start with «{head}»")
    a = starts[0]
    b = next((i for i in range(a + 1, len(lines)) if lines[i].startswith("### ") or lines[i].startswith("## ")), len(lines))
    return "\n".join(l if a <= i < b else "" for i, l in enumerate(lines))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    work = os.path.abspath(sys.argv[1])
    fixes = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else os.path.join(TOP, "docs/red-b/P-N5-EXP-fixes.md")
    os.makedirs(os.path.join(work, "src"), exist_ok=True)
    frozen = os.path.join(TOP, "docs/red-b/P-N5-EXP.md")
    if hashlib.sha1(open(frozen, "rb").read()).hexdigest() != FROZEN_SHA1:
        raise SystemExit("b6fixquote: the frozen packet's sha1 differs")
    args = [f"FROZEN={frozen}"]
    for lab, (commit, path, head) in SRC.items():
        r = subprocess.run(["git", "show", f"{commit}:{path}"], cwd=TOP, capture_output=True)
        if r.returncode != 0:
            raise SystemExit(f"b6fixquote: cannot read {commit[:8]}:{path} (fetch its branch first)")
        text = r.stdout.decode("utf-8")
        if head:
            text = restrict(text, head)
        out = os.path.join(work, "src", f"{lab}.{os.path.basename(path)}")
        open(out, "w", encoding="utf-8").write(text)
        args.append(f"{lab}={out}")
    if os.environ.get("B6FQ_CTRL") == "1":
        t = open(fixes, encoding="utf-8").read()

        def spoil(m):
            q = m.group(0)
            for i in range(len(q) // 2, len(q)):
                if q[i].isalpha():
                    return q[:i] + ("x" if q[i] != "x" else "y") + q[i + 1:]
            return q
        # change one letter inside every top-level quote that follows a Q-tag (whole paragraphs that contain a tag)
        pars = re.split(r"(\n\s*\n)", t)
        for i, p in enumerate(pars):
            if "[Q " in p:
                pos = p.index("[Q ")
                pars[i] = p[:pos] + re.sub(r"«[^«»]*»", spoil, p[pos:])
        fixes = os.path.join(work, "src", "fixes_ctrl.md")
        open(fixes, "w", encoding="utf-8").write("".join(pars))
    r = subprocess.run([sys.executable, os.path.join(HERE, "b6quote.py"), fixes] + args)
    sys.exit(r.returncode)
