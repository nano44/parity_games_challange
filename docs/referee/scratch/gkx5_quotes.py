#!/usr/bin/env python3
"""REFEREE successor 37, stage 5a: byte tests on P-N5-EXP-fixes.md, entries 2-6 (claude/l-red-b 0c8fdf9e; entries 2-5 are the file
of 24f4d436). Own script; the lane's b6fixquote.py is not imported and was not opened. Sources are read from git objects
(`git show COMMIT:PATH`); run from inside the repository.
Usage: python3 -I gkx5_quotes.py [--spoil | --pins | --facts | --lanecmp]
  default:   the objects (sha1, append-only, frozen paths), then every Q-tagged guillemet quote of entries 2-6 (lines >= 126),
             searched in the cited lines of its source (white-space runs collapsed: the fixes file re-wraps lines), per entry.
             The REF2-tagged quotes are matched BY SCRIPT ONLY (found / not found; docs/referee-2/ is not read by this session);
  --spoil:   control, the first letter of every quote replaced: every quote must be NOT found;
  --pins:    the sha1 values written in the entries against the git objects; the pin files; the pasted DATA blocks; arithmetic;
  --facts:   single factual sentences of entries 3, 5, 6 against the files they speak of;
  --lanecmp: this lane's logs gkx_logs/s37_all.out, s37_exh.out against the lane's pinned outputs (supplementary, entry 4).
A quote is the text between a balanced pair of guillemets that follows a tag [Q LABEL l. ...], further quotes of the same tag
being separated from it by white space only."""
import subprocess, sys, re, hashlib, os

FIXC = "0c8fdf9ea"                      # entry 6's commit (git resolves the prefix); the file there has entries 1-6
FIX45 = "24f4d436a0fea1f62ae736f20f78ff9e84333a90"
FIXP = "docs/red-b/P-N5-EXP-fixes.md"
PKT = "docs/red-b/P-N5-EXP.md"
D = "experiments/red-b/data/b6b/"
SRC = {
    "FROZEN": ("350d84eb", PKT),
    "REF1": ("c881709b78d8e4b2debb72baf2c487156413416f", "docs/referee/R-P-N5-EXP.md"),
    "PRE": ("06ac891df6f6212bac74259863da3105e7fe4341", "docs/referee/R-GK-precheck.md"),
    "R117": ("5d7aab0f", "docs/RESULTS.md"), "R124": ("5d7aab0f", "docs/RESULTS.md"), "R57": ("5d7aab0f", "docs/RESULTS.md"),
    "R104P": ("5d7aab0f", "docs/red/P-N5-REALIZE.md"),
    "KEY1P": ("44775605", "docs/new/P-N5-KEY1P.md"),
    "LNEW": ("aa29064d", "docs/new/P-N5-KEY1P-after-EXP-draft.md"),
    "REF2": ("33ff0e98911544cb18545541e4acbe71de84c6e0", "docs/referee-2/R2-P-N5-EXP.md"),
}
TOP = subprocess.run(["git", "rev-parse", "--show-toplevel"], check=True, capture_output=True).stdout.decode().strip()

def git(*a):
    return subprocess.run(["git"] + list(a), check=True, capture_output=True, cwd=TOP).stdout.decode("utf-8")

def show(commit, path):
    return git("show", f"{commit}:{path}")

def sha1(txt):
    return hashlib.sha1(txt.encode("utf-8")).hexdigest()

def norm(s):
    return " ".join(s.split())

def ranges(loc):
    m = re.match(r"l\.\s*(.*)$", loc.strip())
    if not m:
        return None
    out = []
    for part in m.group(1).split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-")
            out.append((int(a), int(b)))
        else:
            out.append((int(part), int(part)))
    return out

def quotes_after(text, pos):
    out, i, n = [], pos, len(text)
    while True:
        while i < n and text[i].isspace():
            i += 1
        if i >= n or text[i] != "«":
            return out
        depth, j = 0, i
        while j < n:
            if text[j] == "«":
                depth += 1
            elif text[j] == "»":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        assert j < n, "unbalanced guillemets"
        out.append(text[i + 1:j])
        i = j + 1

def entries(fix):
    """[(name, first line, last line)] of the conventions and the entries 2..6, from the headings."""
    ls = fix.split("\n")
    heads = [(i + 1, l) for i, l in enumerate(ls) if l.startswith("## ")]
    out = []
    for n, (ln, l) in enumerate(heads):
        end = heads[n + 1][0] - 1 if n + 1 < len(heads) else len(ls)
        while end > ln and not ls[end - 1].strip():          # trailing blank lines are not part of the entry
            end -= 1
        m = re.match(r"## Entry (\d+)", l)
        name = f"entry {m.group(1)}" if m else ("conventions" if l.startswith("## Entries 2-5") else l[3:20])
        out.append((name, ln, end))
    return out

def kvline(l, start=1):
    w = l.split()
    return {w[i]: w[i + 1] for i in range(start, len(w) - 1, 2)}

def main_default(spoil):
    fix = show(FIXC, FIXP)
    lines = fix.split("\n")
    ent = [e for e in entries(fix) if e[1] >= 126]
    if not spoil:
        f45, f1 = show(FIX45, FIXP), show("06d399c2", FIXP)
        p0, p1 = show("350d84eb", PKT), show(FIXC, PKT)
        print(f"fixes file at 0c8fdf9e: lines {fix.count(chr(10))} sha1 {sha1(fix)}; at 24f4d436: lines {f45.count(chr(10))} sha1 {sha1(f45)}; "
              f"at 06d399c2: lines {f1.count(chr(10))} sha1 {sha1(f1)}")
        print(f"append-only, each file a byte prefix of the next: 06d399c2 in 24f4d436 {int(f45.startswith(f1))}; 24f4d436 in 0c8fdf9e {int(fix.startswith(f45))}")
        print(f"packet sha1 at 350d84eb {sha1(p0)}; at 0c8fdf9e {sha1(p1)}; unchanged {int(p0 == p1)}")
        paths = [PKT, "experiments/red-b/gk.py", D + "G", D + "raw", D + "pg", D + "SHA1SUMS_b6b", D + "SHA1SUMS_b6b_fixes1", D + "SHA1SUMS_b6b_fixes2"]
        fz = [l for l in git("diff", "--name-status", "350d84eb", FIXC, "--", *paths[:6]).split("\n") if l.strip()]
        print(f"350d84eb -> 0c8fdf9e on the packet, gk.py, data/b6b/G, raw, pg, SHA1SUMS_b6b: modified or deleted "
              f"{sum(1 for l in fz if l.split()[0] != 'A')}; added {sum(1 for l in fz if l.split()[0] == 'A')} "
              f"({' '.join(l.split()[1].split('/')[-1] for l in fz if l.split()[0] == 'A')}: the games of entries 1 and 6)")
        ns = [l for l in git("diff", "--name-status", FIX45, FIXC, "--", "docs/red-b", "experiments/red-b").split("\n") if l.strip()]
        print(f"24f4d436 -> 0c8fdf9e under docs/red-b, experiments/red-b: added {sum(1 for l in ns if l.split()[0] == 'A')}; "
              f"modified {' '.join(sorted(l.split()[1].split('/')[-1] for l in ns if l.split()[0] == 'M'))}; "
              f"deleted {sum(1 for l in ns if l.split()[0] == 'D')}; pin files fixes1, fixes2 changed "
              f"{len([l for l in git('diff', '--name-status', FIX45, FIXC, '--', *paths[6:]).split(chr(10)) if l.strip()])}")
        print("entries by their headings: " + "; ".join(f"{n} l. {a}-{b}" for n, a, b in ent))
    pos_of_line = [0]
    for l in lines:
        pos_of_line.append(pos_of_line[-1] + len(l) + 1)
    def entry_at(pos):
        for n, a, b in ent:
            if pos_of_line[a - 1] <= pos < pos_of_line[b]:
                return n
        return None
    srcs = {}
    stat = {}                                   # entry -> [tags, quotes, found, ref2 quotes, ref2 found]
    bad = []
    for m in re.finditer(r"\[Q ([A-Za-z0-9]+)((?: [^\]]*)?)\]", fix):
        e = entry_at(m.start())
        if e is None:
            continue
        label, loc = m.group(1), m.group(2)
        qs = quotes_after(fix, m.end())
        st = stat.setdefault(e, [0, 0, 0, 0, 0])
        st[0] += 1
        if label not in srcs:
            srcs[label] = show(*SRC[label]).split("\n")
        sl = srcs[label]
        rg = ranges(loc)
        assert rg, f"tag without line numbers: {m.group(0)}"
        rtxt = [norm("\n".join(sl[a - 1:b])) for (a, b) in rg]
        for q in qs:
            nq = norm(q)
            if spoil:
                nq = ("#" if nq[0] != "#" else "%") + nq[1:]
            ok = any(nq in t for t in rtxt) or nq in " ".join(rtxt)
            if label == "REF2":
                st[3] += 1
                st[4] += int(ok)
            else:
                st[1] += 1
                st[2] += int(ok)
            if not ok and not spoil:
                bad.append(f"NOTFOUND in the cited lines: {e} {m.group(0)} «{q[:50]}…»" if label != "REF2" else f"NOTFOUND (REF2, by script): {e} {m.group(0)}")
    for b in bad:
        print(b)
    tag = "quotes control (first letter spoiled)" if spoil else "quotes"
    for n, a, b in ent:
        st = stat.get(n, [0, 0, 0, 0, 0])
        print(f"{tag}, {n} (l. {a}-{b}): tags {st[0]}; quotes with a label other than REF2 {st[1]} found in the cited lines {st[2]}; "
              f"REF2-tagged {st[3]} found {st[4]} (by script only)")
    tot = [sum(s[i] for s in stat.values()) for i in range(5)]
    print(f"{tag}, entries 2-6 together: tags {tot[0]}; quotes {tot[1] + tot[3]} = {tot[1]} + {tot[3]} (REF2); found {tot[2]} + {tot[4]}")
    if spoil:
        return
    s2 = "\n".join(srcs.get("REF2", []))
    print(f"REF2 source as the fixes file names it: claude/referee-2 33ff0e98 docs/referee-2/R2-P-N5-EXP.md lines {s2.count(chr(10))} sha1 {sha1(s2)} "
          f"(the fixes file writes 284 lines, sha1 f63e227e31586d159fad57a6c3ea986cdf644343: {int(sha1(s2) == 'f63e227e31586d159fad57a6c3ea986cdf644343' and s2.count(chr(10)) == 284)})")
    pk = norm("\n".join(show("350d84eb", PKT).split("\n")[193:196]))
    u = [norm("that the run reaches"), norm("the run reaches s_(t+P_j−1)")]
    print(f"untagged (entry 4.0, E-1 bullet): «{u[0]}» and «{u[1]}» in the fixes file {int(all('«' + x + '»' in norm(fix) for x in u))}, "
          f"verbatim in packet l. 194-196: {int(all(x in pk for x in u))} (the lane's count 75 for entries 2-5 = this script's 73 + these 2)")

PINS = [  # (object, sha1 as written in the fixes file's entries 2-6)
    ("350d84eb:docs/red-b/P-N5-EXP.md", "c0449b17193f19619f33b366096762dfde27d542"),
    ("c881709b:docs/referee/R-P-N5-EXP.md", "c662d157621671c816ef03726e1649af1b648555"),
    ("06ac891d:docs/referee/R-GK-precheck.md", "e2d7c5cb965a960bd0dc5c00d5cd50fc6d368e6f"),
    ("5d7aab0f:docs/RESULTS.md", "eecbd798b81ad431d1b753f5a7f92f3c63e56da1"),
    ("44775605:docs/new/P-N5-KEY1P.md", "f7191623e9ee212fa127c7e4a224f7ab9d689156"),
    ("5d7aab0f:docs/red/P-N5-REALIZE.md", "067f06b6c67969adf346621b4a92b253491ab2b9"),
    ("350d84eb:TARGET.md", "a41d5e1a3d251b1e7c345c159651c08d76ad8165"),
    ("350d84eb:CLAUDE.md", "1e990915503030bba02722f621767c4563c83c74"),
    ("5d7aab0f:docs/GAPS.md", "3fa61e1cf9ce48ab16ee6102c3ee145a7d7e0491"),
    ("350d84eb:" + D + "out/quote.out", "b20118000a5456610e9303b0e140a4bc53501a6f"),
    ("0c8fdf9ea:" + D + "G/G_3.json", "fe5b59464d938730eb8e19afff139d983d2c3946"),
    ("0c8fdf9ea:" + D + "G/G_4.json", "fb96a30fc1b8e5935229cad597b5b38604db7b1b"),
    ("0c8fdf9ea:" + D + "G/G_8.json", "b293075ce300b23477f3bb6ad694c6577b2c64d2"),
    ("0c8fdf9ea:" + D + "G/G_10.json", "d63509cd3dc6fc735d1452d02d371243963a40ab"),
    ("0c8fdf9ea:" + D + "raw/G_3.json", "cd3cd7e361dfe16482bbe56eb87d3e3decf9e6af"),
    ("0c8fdf9ea:" + D + "raw/G_4.json", "7a2218bfa94e37f85b3fc60d874030aeba8ca848"),
    ("0c8fdf9ea:" + D + "raw/G_8.json", "d3ad8e2e6f202eb17e66d04dad77de1a33e74eb2"),
    ("0c8fdf9ea:" + D + "raw/G_10.json", "da29d33ecaf20cb777650729e54acb1dad17cfd9"),
    ("0c8fdf9ea:" + D + "pg/G_13_g3.pg", "9d887e3bf2e1fa4912c32ee0a1ec4ed14327bf71"),
    ("0c8fdf9ea:" + D + "pg/G_9_g3.pg", "9cece8a782b6212e06a177c0899422ebac6e3b0b"),
]

def pins():
    fix = show(FIXC, FIXP)
    bad = absent = 0
    for obj, want in PINS:
        c, path = obj.split(":")
        bad += int(sha1(show(c, path)) != want)
        absent += int(want not in fix)
    print(f"pins: sha1 values written in entries 2-6 (the second referee's file excepted): {len(PINS)}; not in the fixes file {absent}; "
          f"different from the git object {bad}")
    outs = {}
    for pf in ("SHA1SUMS_b6b_fixes2", "SHA1SUMS_b6b_fixes3"):
        rows = [l.split() for l in show(FIXC, D + pf).split("\n") if l.strip()]
        mism = 0
        for want, rel in rows:
            txt = show(FIXC, D + rel)
            outs[rel] = txt
            mism += int(sha1(txt) != want)
        print(f"pins: {pf} at 0c8fdf9e: files {len(rows)}; sha1 mismatches {mism}")
    pool = set()
    for rel, txt in list(outs.items()) + [("q", show("350d84eb", D + "out/quote.out"))]:
        if not rel.endswith(".pg"):
            pool.update(l.rstrip() for l in txt.split("\n"))
    ent = [e for e in entries(fix) if e[1] >= 126]
    inblock = False
    per = {}
    for i, l in enumerate(fix.split("\n"), 1):
        if i < 126:
            continue
        if l.strip() == "```":
            inblock = not inblock
            continue
        if inblock:
            e = [n for n, a, b in ent if a <= i <= b][0]
            p = per.setdefault(e, [0, 0])
            p[0] += 1
            p[1] += int(l.rstrip() not in pool)
    print("pins: fenced DATA lines / of them not a line of a pinned output file: " + "; ".join(f"{e} {p[0]} / {p[1]}" for e, p in per.items()))
    n = lambda k: 135 * k - 230
    m = lambda k: 176 * k - 300
    N = lambda k: 9 * k - 16
    ok = [all(N(k) + 2 * N(k) == 27 * k - 48 for k in range(3, 400)), all(n(k) + m(k) == 311 * k - 530 for k in range(3, 400)),
          2 ** 12 + 1 == 4097, n(12) == 1390, n(12) + m(12) == 3202, n(12) ** 2 == 1932100,
          min(k for k in range(3, 60) if 2 ** k + 1 > n(k)) == 11, 2 ** 11 + 1 == 2049, n(11) == 1255,
          min(k for k in range(3, 60) if 2 ** k + 1 > n(k) + m(k)) == 12, 2 ** 12 + 1 < n(12) ** 2,
          min(k for k in range(3, 100) if 2 ** k - 1 > n(k) ** 2) == 23, n(23) == 2875, 2 ** 23 - 1 == 8388607,
          all(2 * (k - 3) + 2 * (k - 4) == 4 * k - 14 for k in range(4, 400)),
          n(13) == 1525, m(13) == 1988, n(13) + m(13) == 3513, n(13) ** 2 == 2325625, 2 ** 13 + 1 == 8193, 2 ** 13 - 2 == 8190,
          n(13) + m(13) < 8193 < n(13) ** 2, N(13) == 101]
    print(f"arith: entry 2 (a′) N + M = 27k − 48; (c) n + m = 311k − 530; (d) 2^12 + 1 = 4,097, n(12) = 1,390, n + m = 3,202, n² = 1,932,100, "
          f"2^k + 1 > n first at k = 11 (2,049 > 1,255), > n + m first at k = 12, 2^k − 1 > n² first at k = 23 (n = 2,875; 8,388,607); entry 5.1 "
          f"2(k − 3) + 2(k − 4) = 4k − 14; entry 6 n(13) = 1,525, m = 1,988, n + m = 3,513 < 8,193 = 2^13 + 1 < n² = 2,325,625, 2^13 − 2 = 8,190: "
          f"checks {len(ok)} failed {sum(1 for x in ok if not x)}")

def facts():
    here = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gkx_logs")
    # entry 3, the DATA sentence: frozen 9.4 (k = 3..11) and entry 1 (k = 12): its = its2 = 2^k + 1, fb = fb2 = 1, F = 2^k - 2
    rows = [kvline(l) for l in (show("350d84eb", D + "out/n5.out") + show(FIXC, D + "out/n5_k12.out")).split("\n") if l.startswith("G_")]
    ks, badr = [], 0
    for l, r in zip([l for l in (show("350d84eb", D + "out/n5.out") + show(FIXC, D + "out/n5_k12.out")).split("\n") if l.startswith("G_")], rows):
        k = int(l.split()[0][2:])
        ks.append(k)
        badr += int(not (int(r["its"]) == int(r["its2"]) == 2 ** k + 1 and r["fb"] == r["fb2"] == "1" and int(r["F"]) == 2 ** k - 2))
    print(f"facts entry 3 (DATA sentence): lines of the frozen n5.out and of entry 1's n5_k12.out: k {min(ks)}..{max(ks)} ({len(ks)} lines); "
          f"its = its2 = 2^k + 1, fb = fb2 = 1, F = 2^k − 2 fails on {badr}")
    # entry 5.1: gk.py's tie line; the lane's brtie.out against this lane's gen.out (stage 1)
    gk = show("350d84eb", "experiments/red-b/gk.py")
    tie = [kvline(l) for l in show(FIXC, D + "out/brtie.out").split("\n") if l.startswith("G_")]
    gen = {r["k"]: r for r in (kvline(l) for l in open(os.path.join(here, "gen.out"), encoding="utf-8") if l.startswith("gen k"))}
    tk = [l.split()[0][2:] for l in show(FIXC, D + "out/brtie.out").split("\n") if l.startswith("G_")]
    d51 = sum(int(r["tied"] != gen[k]["wtie"]) + int(r["rundiff"] != "0") + int(r["member2"] != "1") for k, r in zip(tk, tie))
    print(f"facts entry 5.1: gk.py has the line `order = sorted(rawrk, key=lambda b: (rawrk[b], b))` {int('order = sorted(rawrk, key=lambda b: (rawrk[b], b))' in gk)}; "
          f"brtie.out k {tk[0]}..{tk[-1]}: tied = this lane's wtie (gen.out), rundiff 0, member2 1: lines different {d51}")
    # entry 5.3: quote.out has 5 source lines, 27 FOUND lines and the summary
    q = [l for l in show("350d84eb", D + "out/quote.out").split("\n") if l.strip()]
    print(f"facts entry 5.3: quote.out lines {len(q)} = source {sum(1 for l in q if l.startswith('source '))} + FOUND {sum(1 for l in q if ' FOUND ' in l)} + 1; "
          f"last line «{q[-1]}»")
    # entry 5.4: the lane's width.out against this lane's member.out
    def after(l, word):
        w = l.split()
        return w[w.index(word) + 1]
    wd = [(l.split()[0][2:], {"N": after(l, "N"), "max": after(l, "max")}) for l in show(FIXC, D + "out/width.out").split("\n") if l.startswith("G_")]
    mem = {r["k"]: r for r in (kvline(l) for l in open(os.path.join(here, "member.out"), encoding="utf-8") if l.startswith("member k") and " ctrl 0 " in l)}
    d54 = sum(int(r["max"] != mem[k]["width"]) + int(r["N"] != mem[k]["N"]) for k, r in wd)
    print(f"facts entry 5.4: width.out k {wd[0][0]}..{wd[-1][0]}: max = this lane's width and N = this lane's N (member.out): lines different {d54}; "
          f"max per k {' '.join(r['max'] for _, r in wd)}")
    # entry 5.5 / 5.7: the pin file's length; the JSON keys of a genome of record
    import json
    g = json.loads(show(FIXC, D + "G/G_5.json"))
    print(f"facts entry 5.5, 5.7: SHA1SUMS_b6b lines {len([l for l in show('350d84eb', D + 'SHA1SUMS_b6b').split(chr(10)) if l.strip()])}; "
          f"keys of G_5.json: {' '.join(sorted(g))}; deg = {g['deg']!r}; bp all 0: {int(set(g['bp']) == {0})}")
    # entry 5.8 / 5.9: the cited commits and sentences
    pre = show("06ac891d", "docs/referee/R-GK-precheck.md").split("\n")
    pk = show("350d84eb", PKT).split("\n")
    e1 = show("06d399c2", FIXP)
    anc = lambda a, b: subprocess.run(["git", "merge-base", "--is-ancestor", a, b], cwd=TOP).returncode == 0
    print(f"facts entry 5.8, 5.9: packet l. 304-305 has «three N5 engines (n5v, n5b, n5s237) and three Γ3 builders» "
          f"{int('three N5 engines (n5v, n5b, n5s237) and three Γ3' in norm(' '.join(pk[303:305])))}; entry 1 (9.10) has «About 40% of the broken variants» "
          f"{int('About 40% of the broken variants' in e1)}; pre-check l. 86 has «counter RENUM 0» {int('counter RENUM 0' in pre[85])}; commits "
          f"dc6d831f (box48/README.md present {int(bool(show('dc6d831f', 'experiments/comp/box48/README.md')))}), c7ed9b8b (R245-kill-Gk.md present "
          f"{int(bool(show('c7ed9b8b', 'docs/red/R245-kill-Gk.md')))}), 706d1ecc an ancestor of c7ed9b8b {int(anc('706d1ecc', 'c7ed9b8b'))}")
    # entry 6: the checkpointed driver against the frozen lines; the control; the resume; the k = 13 line; the size lines
    fro = {l.split()[0]: kvline(l) for l in show("350d84eb", D + "out/n5.out").split("\n") if l.startswith("G_")}
    F12 = ("N", "M", "n", "T1p", "F", "mism", "its", "fb", "wrong", "nonmover", "gdiff", "pg_sha1")
    ck = [(l.split()[0], kvline(l)) for l in show(FIXC, D + "out/n5ck_check.out").split("\n") if l.startswith("G_")]
    ckd = sum(int(r[f] != fro[g][f]) for g, r in ck for f in F12)
    ctl = kvline([l for l in show(FIXC, D + "out/n5ck_ctrl.out").split("\n") if l.startswith("G_")][0])
    rs_l = [l for l in show(FIXC, D + "out/n5ck_resume.out").split("\n") if l.startswith("G_")][0]
    rs = kvline(rs_l)
    rsd = sum(int(rs[f] != fro[rs_l.split()[0]][f]) for f in F12)
    k13 = kvline([l for l in show(FIXC, D + "out/n5_k13.out").split("\n") if l.startswith("G_13")][0])
    want13 = {"mode": "spec", "ctrl": "0", "N": "101", "M": "202", "n": "1525", "T1p": "8190", "F": "8190", "mism": "0", "its": "8193", "fb": "1",
              "wrong": "0", "nonmover": "0", "gdiff": "0", "pg_sha1": sha1(show(FIXC, D + "pg/G_13_g3.pg")), "resumes": "0"}
    d13 = sum(int(k13.get(f) != v) for f, v in want13.items())
    sz = [kvline(l) for l in show(FIXC, D + "out/size_k13.out").split("\n") if l.startswith("G_13")]
    print(f"facts entry 6 (9.14): n5ck_check.out {' '.join(g for g, _ in ck)}: {len(ck) * len(F12)} fields against the frozen n5.out, different {ckd}; "
          f"control line (ctrl {ctl['ctrl']}) wrong {ctl['wrong']}; resume line {rs_l.split()[0]} resumes {rs['resumes']}, its {rs['its']}, fb {rs['fb']}, "
          f"twelve fields against the frozen line different {rsd}")
    print(f"facts entry 6 (9.15): n5_k13.out against N = 9k − 16, M = 2N, n = 135k − 230, T1p = F = 2^13 − 2, its = 2^13 + 1, fb 1, mism, wrong, "
          f"nonmover, gdiff 0, resumes 0, pg_sha1 = sha1 of pg/G_13_g3.pg: fields {len(want13)} different {d13}; secs {k13['secs']}; size_k13.out: "
          f"ctrl 0 n {sz[0]['n']} m {sz[0]['m']} sizediff {sz[0]['sizediff']}; ctrl 1 sizediff {sz[1]['sizediff']}")

def lanecmp():
    here = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gkx_logs")
    def mine(name):
        return [kvline(l) for l in open(os.path.join(here, name), encoding="utf-8") if l.strip()]
    def lane(name):
        rows = []
        for l in show(FIXC, D + "out/" + name).split("\n"):
            w = l.split()
            if w:
                d = {"k": w[0][2:], "_line": l}
                for i in range(1, len(w) - 1, 2):
                    if w[i].startswith("at("):
                        break
                    d[w[i]] = w[i + 1]
                rows.append(d)
        return rows
    cmp_n = bad = 0
    def eq(a, b):
        nonlocal cmp_n, bad
        cmp_n += 1
        bad += int(str(a) != str(b))
    ma = mine("s37_all.out")
    m0 = {r["k"]: r for r in ma if r["ctrl"] == "0"}
    mf = {r["k"]: r for r in ma if r["ctrl"] == "frozen"}
    m2 = {r["k"]: r for r in ma if r["ctrl"] == "2"}
    la = lane("prefix_all.out")
    for r in la:
        k = r["k"]
        eq(r["triples"], m0[k]["triples"]); eq(r["windows"], m0[k]["windows"]); eq(r["expected"], m0[k]["expected"])
        eq(r["steps"], m0[k]["pairs"]); eq(r["aviol"], m0[k]["viol"])
        eq(int(r["h1only"]) - int(m0[k]["h1only"]), 2 * (int(k) - 1))       # the lane also counts t - 1 = L + 1, L + 2 (beyond the run)
    print(f"lanecmp prefix_all.out (k {la[0]['k']}..{la[-1]['k']}): triples, windows, expected, steps = pairs, aviol = viol, "
          f"h1only − mine = 2(k − 1): compared {cmp_n} different {bad}")
    c0, b0 = cmp_n, bad
    lr = lane("prefix_run.out")
    for r in lr:
        k = r["k"]
        if k in m0:
            eq(r["windows"], m0[k]["windows"]); eq(r["pairs"], m0[k]["pairs"])
    print(f"lanecmp prefix_run.out (its k {lr[0]['k']}..{lr[-1]['k']}, mine up to 13): windows, pairs: compared {cmp_n - c0} different {bad - b0}")
    c0, b0 = cmp_n, bad
    lc = lane("prefix_ctrl.out")
    nfro = 0
    for r in lc:
        k = r["k"]
        if r["mode"] == "all" and r["ctrl"] == "5":
            nfro += 1
            eq(r["frozen_hyp_holds"], mf[k]["frozen_hyp_holds"]); eq(r["frozen_conclusion_fails"], mf[k]["frozen_conclusion_fails"])
            at = r["_line"].split("at(j,a,t)")[1].split()
            want = [f"(1,1,{2 ** int(k) - 1})"] + [f"({j},0,{2 ** int(k) - 1})" for j in range(2, int(k))]
            eq(" ".join(at), " ".join(want)); eq(mf[k]["failset_is_expected"], 1)
        if r["mode"] == "run" and r["ctrl"] == "2":
            eq(r["psched"], m2[k]["viol"])
    print(f"lanecmp prefix_ctrl.out, the lemma as frozen (its control 5, {nfro} lines) and the exchanged list (its G_5 run ctrl 2): "
          f"hyp_holds, conclusion_fails, the fail set, psched = viol: compared {cmp_n - c0} different {bad - b0}")
    c0, b0 = cmp_n, bad
    me = mine("s37_exh.out")
    cols = ("states", "c0e0", "loc", "lockeys", "stcases", "stviol", "onestate_cases", "onestate_moves", "h1only", "windows", "full",
            "proper", "steps", "pviol")
    for r in lane("prefix_exh.out") + [r for r in lc if r["mode"] == "exh"]:
        m = [x for x in me if x["k"] == r["k"] and x["ctrl"] == r["ctrl"]][0]
        for c in cols:
            eq(r[c], m[c])
    print(f"lanecmp prefix_exh.out (k 3, 4) and its exh controls 2, 3 (k 4): {len(cols)} columns each: compared {cmp_n - c0} different {bad - b0}")
    print(f"lanecmp total: compared {cmp_n} different {bad}")

if __name__ == "__main__":
    if "--pins" in sys.argv:
        pins()
    elif "--facts" in sys.argv:
        facts()
    elif "--lanecmp" in sys.argv:
        lanecmp()
    else:
        main_default("--spoil" in sys.argv)
