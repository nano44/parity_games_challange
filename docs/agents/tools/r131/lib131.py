#!/usr/bin/env python3
"""Shared helpers of the R131 build (docs/agents/tools/r131/).

Everything is read from git objects (git show COMMIT:PATH) at the commits cfg.json names; the working tree is
read only by land131.py (RESULTS / GAPS / NOW / the draft). Nothing here writes outside docs/agents/tools/r131/
and docs/agents/R131-draft.md.
"""
import hashlib
import json
import os
import subprocess
import textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
OPEN_WORD = "PEND" + "ING"          # the open-slot word; spelled in two halves so that tool OUTPUT never carries it


def _root():
    p = subprocess.run(["git", "-C", HERE, "rev-parse", "--show-toplevel"], capture_output=True)
    if p.returncode != 0:
        raise SystemExit("lib131: not inside a git work tree: " + p.stderr.decode("utf-8", "replace"))
    return p.stdout.decode("utf-8").strip()


ROOT = _root()
DRAFT = os.path.join(ROOT, "docs", "agents", "R131-draft.md")


def load_cfg():
    with open(os.path.join(HERE, "cfg.json"), encoding="utf-8") as f:
        return json.load(f)


def git(*args, ok=(0,)):
    p = subprocess.run(["git", "-C", ROOT] + list(args), capture_output=True)
    if p.returncode not in ok:
        raise SystemExit("git %s: rc %d: %s" % (" ".join(args), p.returncode, p.stderr.decode("utf-8", "replace")[:300]))
    return p.stdout


def gitrc(*args):
    p = subprocess.run(["git", "-C", ROOT] + list(args), capture_output=True)
    return p.returncode, p.stdout


_SHOW = {}


def show(commit, path):
    """bytes of PATH at COMMIT (git show)."""
    k = (commit, path)
    if k not in _SHOW:
        _SHOW[k] = git("show", "%s:%s" % (commit, path))
    return _SHOW[k]


def exists(commit, path):
    rc, _ = gitrc("cat-file", "-e", "%s:%s" % (commit, path))
    return rc == 0


def sha1(b):
    return hashlib.sha1(b).hexdigest()


def full(commit):
    return git("rev-parse", "--verify", commit + "^{commit}").decode().strip()


def short(commit):
    return commit[:8]


def cdate(commit):
    """committer date of COMMIT in the form 2026-11-13T12:55:07Z (UTC asserted)."""
    d = git("log", "-1", "--format=%cI", commit).decode().strip()
    if not d.endswith("+00:00"):
        raise SystemExit("commit %s: committer date %s is not UTC" % (commit, d))
    return d[:-6] + "Z"


def csubject(commit):
    return git("log", "-1", "--format=%s", commit).decode("utf-8").strip()


def blame_ranges(commit, path):
    """[(sha8, first, last)] of PATH at COMMIT by git blame."""
    out = git("blame", "-s", "--abbrev=8", commit, "--", path).decode("utf-8", "replace").split("\n")
    res, prev, start, n = [], None, 1, 0
    for n, l in enumerate([x for x in out if x], 1):
        c = l.split()[0].lstrip("^")[:8]
        if c != prev:
            if prev is not None:
                res.append((prev, start, n - 1))
            prev, start = c, n
    if prev is not None:
        res.append((prev, start, n))
    return res


def norm(s):
    return " ".join(s.split())


def num(n):
    return "{:,}".format(n)


def loc(first, last):
    return "l. %d" % first if first == last else "l. %d-%d" % (first, last)


class Source:
    """A text file at a commit, searchable for verbatim quotations.

    House convention (the packets' own): wrapped source lines are joined, white space is normalised on both
    sides, nothing else. A quotation never crosses an empty line.
    """

    def __init__(self, key, commit, path, what, limit=None):
        self.key, self.commit, self.path, self.what = key, commit, path, what
        self.limit = limit            # quotations written in fill131.py are searched in the first `limit` lines only
        self.raw = show(commit, path)
        self.sha1 = sha1(self.raw)
        self.text = self.raw.decode("utf-8")
        self.lines = self.text.split("\n")
        if self.lines and self.lines[-1] == "":
            self.lines.pop()
        parts, pos2line = [], []
        for i, l in enumerate(self.lines, 1):
            s = norm(l)
            piece = (s if s else "\x00") + " "
            parts.append(piece)
            pos2line.extend([i] * len(piece))
        self.norm = "".join(parts)
        self.pos2line = pos2line

    def find(self, q, whole=False):
        """[(first_line, last_line)] of every occurrence of q (white space normalised); unless `whole`, only those
        that end within the described part of the file (the first `limit` lines)."""
        nq = norm(q)
        res, i = [], self.norm.find(nq)
        while i >= 0:
            fl = (self.pos2line[i], self.pos2line[i + len(nq) - 1])
            if whole or self.limit is None or fl[1] <= self.limit:
                res.append(fl)
            i = self.norm.find(nq, i + 1)
        return res

    def prefix_sha1(self, n):
        """sha1 of the first n lines (with their newlines)."""
        return sha1("".join(l + "\n" for l in self.lines[:n]).encode("utf-8"))


def sources(cfg):
    """key -> Source: every file a quotation of the draft may come from, at the commit cfg names."""
    h, t = dict(cfg["heads"]), cfg["trunk"]["commit"]
    h.update({k: v for k, v in cfg.get("pins", {}).items() if not k.startswith("_")})
    lim = {"FIX": cfg["fixes"].get("described_lines"), "REF1": cfg["referee"].get("described_lines"), "REF2": cfg["referee2"].get("described_lines")}
    spec = [
        ("PKT", cfg["packet"]["freeze_commit"], cfg["packet"]["path"], "the frozen packet"),
        ("FIX", h["l-red-b"], cfg["fixes"]["path"], "the fixes file"),
        ("LINE", cfg["line"]["commit"], cfg["line"]["path"], "the line"),
        ("REF1", h["referee"], cfg["referee"]["path"], "REFEREE's report"),
        ("PRE", h["referee"], cfg["referee"]["precheck_path"], "REFEREE's pre-check"),
        ("REF2", h["referee-2"], cfg["referee2"]["path"], "REFEREE-2's report"),
        ("R2B", h["referee-2"], cfg["referee2"]["box108_path"], "REFEREE-2's review of box 108"),
        ("B108", cfg["box108"]["commit"], cfg["box108"]["path"], "L-SI's box 108"),
        ("BOX48", h["l-comp"], cfg["replays"]["box48_path"], "L-COMP's BOX 48"),
        ("R245", h["l-red"], cfg["replays"]["r245_path"], "L-RED's R245"),
        ("RES", t, "docs/RESULTS.md", "RESULTS"),
        ("GAPS", t, "docs/GAPS.md", "GAPS"),
        ("TARGET", t, "TARGET.md", "TARGET.md"),
        ("CLAUDE", t, "CLAUDE.md", "CLAUDE.md"),
        ("DEC", t, "docs/DECISIONS.md", "DECISIONS"),
        ("LEAD", t, "docs/agents/LEAD-STATE.md", "the Lead's state log"),
        ("R104P", t, "docs/red/P-N5-REALIZE.md", "R104's packet"),
        ("R130D", t, "docs/agents/R130-draft.md", "the R130 draft"),
    ]
    return {k: Source(k, c, p, w, lim.get(k)) for k, c, p, w in spec}


def gspans(s):
    """top-level guillemet spans of s: [(start, end, inner)]; ValueError when they do not balance."""
    depth, start, out = 0, None, []
    for i, ch in enumerate(s):
        if ch == "«":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "»":
            if depth == 0:
                raise ValueError("closing guillemet without an opening one at %d: %r" % (i, s[max(0, i - 40):i + 10]))
            depth -= 1
            if depth == 0:
                out.append((start, i + 1, s[start + 1:i]))
    if depth:
        raise ValueError("unclosed guillemet from %d: %r" % (start, s[start:start + 60]))
    return out


def wrap(par, first="", rest="  ", width=140):
    w = textwrap.TextWrapper(width=width, initial_indent=first, subsequent_indent=rest,
                             break_long_words=False, break_on_hyphens=False)
    return w.wrap(norm(par))


def read_draft(path=None):
    with open(path or DRAFT, encoding="utf-8") as f:
        return f.read()


def split_draft(text, cfg):
    """the draft's parts: dict with the 0-based line indices and the lines themselves.

    block  = the line starting '### R131 [refereed-only] ' up to the last bullet line before the empty line that
             precedes the line starting 'Proposed GAPS ';
    update = the single line starting 'UPDATE <DATE> <HH:MM>Z: RESULTS R131 (' (or its filled form in a landed draft);
    addendum = from the first line starting 'Addendum (' to the end.
    """
    entry = cfg["entry"]
    L = text.split("\n")
    heads = [i for i, l in enumerate(L) if l.startswith("### %s [refereed-only] " % entry)]
    props = [i for i, l in enumerate(L) if l.startswith("Proposed GAPS ")]
    ups = [i for i, l in enumerate(L) if l.startswith("UPDATE <DATE> <HH:MM>Z: RESULTS %s (" % entry)]
    adds = [i for i, l in enumerate(L) if l.startswith("Addendum (")]
    if len(heads) != 1 or len(props) != 1 or len(ups) != 1:
        raise SystemExit("draft shape: %d title lines, %d 'Proposed GAPS' lines, %d UPDATE lines (need 1, 1, 1)"
                         % (len(heads), len(props), len(ups)))
    b0, p0, u0 = heads[0], props[0], ups[0]
    if not (b0 < p0 < u0) or L[p0 - 1] != "" or L[b0 - 1] != "":
        raise SystemExit("draft shape: order or separating empty lines wrong")
    b1 = p0 - 1                      # exclusive: L[b0:b1] is the block, L[b1] == ''
    if any(l == "" for l in L[b0:b1]):
        raise SystemExit("draft shape: empty line inside the entry block")
    a0 = adds[0] if adds else len(L)
    return {"lines": L, "b0": b0, "b1": b1, "p0": p0, "u0": u0, "a0": a0,
            "block": L[b0:b1], "update": L[u0], "header": L[:b0 - 1], "proposal": L[p0:u0]}


def block_sha1(block_lines):
    return sha1(("\n".join(block_lines) + "\n").encode("utf-8"))


def line_sha1(s):
    return sha1(s.encode("utf-8"))
