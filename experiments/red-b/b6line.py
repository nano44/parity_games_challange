#!/usr/bin/env python3
"""L-RED-B packet P-N5-EXP: line L-2, built from line L-1 by NAMED REPLACEMENTS (never by hand).

L-1 = docs/red-b/P-N5-EXP-line-L1.txt (sha1 59c5309377eda882ba436ffe7eb03fbff598c7c8, pinned below; never edited).
L-2 = docs/red-b/P-N5-EXP-line-L2.txt = L-1 with the replacements of CHANGES and nothing else.
Each replacement names the line item it answers (L-a, L-b, L-c: REFEREE-2 42's line notes, claude/referee-2 f17a2708,
docs/referee-2/R2-P-N5-EXP.md l. 521-527; L-d: the Lead's item, N5 at k = 13 from fixes entry 6) and its `old` text must occur EXACTLY ONCE in
L-1; the replaced spans are disjoint, so every character outside them is that of L-1 (tested: undoing the replacements on
the result gives L-1 back, byte for byte).

Usage (from anywhere; no other lane's file is needed for build / check):
  b6line.py build    write L-2; print the diff (per change: item, position in L-1, the old text, the new text, each cut down to
                     the part that differs), then the checks
  b6line.py check    rebuild in memory and compare with the committed L-2; exit 1 on any difference or failed check (check.sh)
  b6line.py quotes   check every quotation of QUOTES verbatim (white space normalised on both sides, nothing else) against its
                     source, read with `git show COMMIT:PATH` (the commits must be in the clone: fetch claude/referee,
                     claude/referee-2 and trunk first); prints the source's sha1 and the line numbers of each quotation
Checks on L-2: exactly one line (one newline, the last byte); no pipe character; the brackets ( ) [ ] { } « » balanced and
properly nested (counts printed); sha1 and byte count printed.
Control B6LINE_CTRL=1 (build / check): one unbalanced bracket is put into the result; the bracket check must fire (exit 1,
nothing is written).  Control B6LINE_CTRL=2 (quotes): one letter of every quotation is changed; each must be NOT-FOUND (exit 1)."""
import sys, os, hashlib, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
TOP = os.path.normpath(os.path.join(HERE, "..", ".."))
L1 = os.path.join(TOP, "docs", "red-b", "P-N5-EXP-line-L1.txt")
L2 = os.path.join(TOP, "docs", "red-b", "P-N5-EXP-line-L2.txt")
L1_SHA1 = "59c5309377eda882ba436ffe7eb03fbff598c7c8"
CTRL = os.environ.get("B6LINE_CTRL", "0")

R117_TITLE = ("with R104's premises as landed (1E-N3 = RESULTS R57 (b) in its two forms; RESULTS R24 (a) Lemma R and R24 (b)'s "
              "choice rule with RESULTS R103's bridge B and (R1) ruling; RESULTS R36 (c) Lemma P1 on the dual game) and RESULTS "
              "R15 (d) for termination only")
REF1_SIGN = "NOT SIGNED AS WRITTEN; SIGNED in the form LEMMA′ of §5.3 below"
REF1_SIGN4 = "RESPONSE LEMMA SIGNED as restated in fixes entry 4 (= LEMMA′ of §5.3 with CAUSAL and STABLE in step form)."
REF2_SIGN = ("REFEREE-2 signs 4.1 (S1)-(S4), 4.2 STABLE, 4.3 CAUSAL, 4.4 LEMMA′ with their proofs (4.2, 4.3, 4.5) and 4.6, as "
             "printed in docs/red-b/P-N5-EXP-fixes.md at claude/l-red-b 24f4d436 (sha1 9dc9179f…), (R3)'s range read as "
             "t − 1 ≤ τ < last (F-1).")

# (item, old text in L-1, new text in L-2)
CHANGES = [
    ("L-a",
     "per unit j a block pair u_j, v_j, an end-follower e_j, two wires wv_j, wu_j and two observer pairs Y_j, Y′_j",
     "unit j, 1 ≤ j ≤ k − 1, is a block pair u_j, v_j with an observer pair Y_j = (y_j, ȳ_j) and, for 2 ≤ j ≤ k − 2 only, an "
     "end-follower e_j and a second observer pair Y′_j = (y′_j, ȳ′_j), so the units 1 and k − 1 have four movers and the others "
     "seven; outside the units, the level-0 pair u_0, v_0 and the wires wv_j, 1 ≤ j ≤ k − 2, and wu_j, 2 ≤ j ≤ k − 2"),
    ("L-b",
     "R117's standing premises: 1E-N3 = RESULTS R57 (b), RESULTS R24 (a) and R24 (b)'s choice rule with RESULTS R103's bridge B, "
     "RESULTS R36 (c), and RESULTS R15 (d) for termination only",
     "R117's standing premises, in the words of its title line: «" + R117_TITLE + "»"),
    ("L-d (1)",
     "the largest, k = 12, makes 4,097 iterations on n = 1,390 vertices",
     "the largest, k = 13 (fixes entry 6, one engine), makes 8,193 iterations on n = 1,525 vertices"),
    ("L-d (2)",
     "gdiff 0; winners equal to Zielonka's), all files in",
     "gdiff 0; winners equal to Zielonka's), and at k = 13 on one engine, the two Γ3 builders agreeing (fixes entry 6: b6n5ck.py, "
     "n5_k13.out: 8,193 = 2^13 + 1 iterations on n = 1,525 vertices, one fallback at iteration 8,191, mover states equal to the "
     "model's; mism, wrong, nonmover, gdiff 0; winners equal to Zielonka's; game experiments/red-b/data/b6b/pg/G_13_g3.pg), all "
     "files in"),
    ("L-c",
     "not a TARGET.md claim (P-N5-EXP,",
     "not a TARGET.md claim; scope tail (Lead reading L41): CAUSAL and LEMMA′ of fixes entry 4 (4.3, 4.4) are referee-originated, "
     "stated and proved by REFEREE 36 (claude/referee c881709b, docs/referee/R-P-N5-EXP.md §5.3; its verdict on the RESPONSE "
     "LEMMA: «" + REF1_SIGN + "»; after fixes entry 4, its stage 4, claude/referee 78515253, the same file §12: «" + REF1_SIGN4
     + "»), and are signed independently by REFEREE-2 42, in the form its signature sentence gives "
     "(claude/referee-2 f17a2708, docs/referee-2/R2-P-N5-EXP.md, Addendum 2 §A2.3: «" + REF2_SIGN + "») (P-N5-EXP,"),
]

# (item, quotation, commit, path, restrict-to-entry head or None)
QUOTES = [
    ("L-b", R117_TITLE, "dba11145c222c9034144db821057485698232d44", "docs/RESULTS.md", "### R117 "),
    ("L-c", REF1_SIGN, "c881709b78d8e4b2debb72baf2c487156413416f", "docs/referee/R-P-N5-EXP.md", None),
    ("L-c", REF1_SIGN4, "78515253a74a353a829b435d53f4987a8552989a", "docs/referee/R-P-N5-EXP.md", None),
    ("L-c", REF2_SIGN, "f17a2708de653b306eaedf878f6120d2d0b31e06", "docs/referee-2/R2-P-N5-EXP.md", None),
]


def sha1(b):
    return hashlib.sha1(b).hexdigest()


def brackets(t):
    """(counts of each bracket character, [balanced and properly nested])"""
    pairs = {")": "(", "]": "[", "}": "{", "»": "«"}
    counts = {ch: t.count(ch) for ch in "()[]{}«»"}
    st = []
    for ch in t:
        if ch in "([{«":
            st.append(ch)
        elif ch in pairs:
            if not st or st[-1] != pairs[ch]:
                return counts, False
            st.pop()
    return counts, not st


def build():
    raw = open(L1, "rb").read()
    if sha1(raw) != L1_SHA1:
        raise SystemExit("b6line: L-1's sha1 differs from its pin")
    t = raw.decode("utf-8")
    spans = []
    for item, old, new in CHANGES:
        n = t.count(old)
        if n != 1:
            raise SystemExit(f"b6line: the old text of {item} occurs {n} times in L-1 (must be 1)")
        if old == new:
            raise SystemExit(f"b6line: {item} changes nothing")
        a = t.index(old)
        spans.append((a, a + len(old), item, old, new))
    spans.sort()
    for (_, b0, i0, _, _), (a1, _, i1, _, _) in zip(spans, spans[1:]):
        if a1 < b0:
            raise SystemExit(f"b6line: the spans of {i0} and {i1} overlap")
    out = []
    pos = 0
    for a, b, item, old, new in spans:
        out.append(t[pos:a])
        out.append(new)
        pos = b
    out.append(t[pos:])
    res = "".join(out)
    back = res                                  # undo: each new text occurs once in the result, and undoing gives L-1 back
    for a, b, item, old, new in spans:
        if back.count(new) != 1:
            raise SystemExit(f"b6line: the new text of {item} does not occur exactly once in the result")
        back = back.replace(new, old)
    if back != t:
        raise SystemExit("b6line: undoing the replacements does not give L-1 back")
    if CTRL == "1":
        res = res[:-1] + ")" + "\n"
    return t, res, spans


def checks(res):
    bad = []
    if not res.endswith("\n") or res.count("\n") != 1:
        bad.append("not exactly one line")
    if "|" in res:
        bad.append("a pipe character")
    counts, ok = brackets(res)
    if not ok:
        bad.append("brackets not balanced or not nested")
    return counts, ok, bad


def report(res, counts, ok, bad):
    b = res.encode("utf-8")
    print("L-2 bytes %d (with its newline) lines %d pipes %d sha1 %s" % (len(b), res.count("\n"), res.count("|"), sha1(b)))
    print("L-2 brackets " + " ".join("%s %d" % (ch, counts[ch]) for ch in "()[]{}«»") + " balanced %d" % int(ok))
    print("L-2 checks failed %d%s" % (len(bad), (": " + "; ".join(bad)) if bad else ""))


def trim(old, new):
    """the common prefix and suffix of old and new, cut off at word boundaries (the diff shows only the words that differ)"""
    p = 0
    while p < min(len(old), len(new)) and old[p] == new[p]:
        p += 1
    while p > 0 and old[p - 1] != " ":
        p -= 1
    q = 0
    while q < min(len(old), len(new)) - p and old[len(old) - 1 - q] == new[len(new) - 1 - q]:
        q += 1
    while q > 0 and old[len(old) - q] != " ":
        q -= 1
    return p, old[p:len(old) - q], new[p:len(new) - q]


def norm_with_lines(text):
    out, ln = [], []
    for i, line in enumerate(text.split("\n"), 1):
        for tok in line.split():
            if out:
                out.append(" ")
                ln.append(i)
            for ch in tok:
                out.append(ch)
                ln.append(i)
    return "".join(out), ln


def restrict(text, head):
    lines = text.split("\n")
    starts = [i for i, l in enumerate(lines) if l.startswith(head)]
    if len(starts) != 1:
        raise SystemExit(f"b6line: {len(starts)} lines start with «{head}»")
    a = starts[0]
    b = next((i for i in range(a + 1, len(lines)) if lines[i].startswith("### ") or lines[i].startswith("## ")), len(lines))
    return "\n".join(l if a <= i < b else "" for i, l in enumerate(lines))


def quotes():
    res = open(L2, encoding="utf-8").read()
    news = {}
    for item, _, new in CHANGES:
        news[item] = news.get(item, "") + new
    n = found = 0
    for item, q, commit, path, head in QUOTES:
        n += 1
        if ("«" + q + "»") not in news[item] or ("«" + q + "»") not in res:
            print(f"{item} NOT-IN-LINE «{q[:60]}»")
            continue
        r = subprocess.run(["git", "show", f"{commit}:{path}"], cwd=TOP, capture_output=True)
        if r.returncode != 0:
            print(f"{item} NO-SOURCE {commit[:8]}:{path} (fetch its branch first)")
            continue
        src = r.stdout.decode("utf-8")
        text, ln = norm_with_lines(restrict(src, head) if head else src)
        qq = " ".join(q.split())
        if CTRL == "2":
            i = next(i for i in range(len(qq) // 2, len(qq)) if qq[i].isalpha())
            qq = qq[:i] + ("x" if qq[i] != "x" else "y") + qq[i + 1:]
        j = text.find(qq)
        if j >= 0:
            found += 1
            print(f"{item} FOUND {commit[:8]}:{path} (sha1 {sha1(r.stdout)}) l. {ln[j]}-{ln[j + len(qq) - 1]} «{qq[:60]}»")
        else:
            print(f"{item} NOT-FOUND {commit[:8]}:{path} «{qq[:60]}»")
    print(f"quotes {n} found {found} notfound {n - found}")
    return 0 if n == found and n > 0 else 1


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode not in ("build", "check", "quotes"):
        print(__doc__)
        sys.exit(2)
    if mode == "quotes":
        sys.exit(quotes())
    t, res, spans = build()
    counts, ok, bad = checks(res)
    if mode == "build":
        print("L-1 bytes %d sha1 %s" % (len(t.encode("utf-8")), sha1(t.encode("utf-8"))))
        for a, b, item, old, new in spans:
            p, o, w = trim(old, new)
            print(f"--- {item}: at character {a + p} of L-1, {len(o.encode('utf-8'))} bytes removed, {len(w.encode('utf-8'))} bytes put in")
            print(f"- {o}" if o else "- (nothing removed: an insertion)")
            print(f"+ {w}")
        same = len(t) - sum(len(trim(old, new)[1]) for _, _, _, old, new in spans)
        print("changes %d; characters of L-1 kept unchanged %d of %d" % (len(spans), same, len(t)))
        report(res, counts, ok, bad)
        if bad:
            sys.exit(1)
        open(L2, "w", encoding="utf-8").write(res)
        print("written " + os.path.relpath(L2, TOP))
        sys.exit(0)
    report(res, counts, ok, bad)
    cur = open(L2, encoding="utf-8").read() if os.path.exists(L2) else None
    diff = 0 if cur == res else 1
    print("L-2 rebuilt-vs-committed diff %d" % diff)
    sys.exit(1 if (bad or diff) else 0)
