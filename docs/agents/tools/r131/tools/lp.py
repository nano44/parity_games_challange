#!/usr/bin/env python3
"""tools/lp.py <draft>: every quotation of the draft at its commit, file and lines, by a SECOND implementation.

(1) Each entry of out/ledger.json (written by fill131.py: quotation or located passage, source key, commit, path,
    first and last line) is searched again in the bytes of `git show COMMIT:PATH` with a regular expression that
    allows any white space between its words; the recorded line range must be one of the matches.
(2) The draft itself: the multiset of its guillemet quotations outside the title line and the UPDATE line equals the
    multiset of the ledger's quotations, so no quotation was typed by hand; each quotation of the title and of the
    UPDATE is in the line; every 'q' entry is followed in the draft by its line numbers.
Negative controls: one ledger entry with its lines moved by one; one quotation of a copy of the draft with one
letter changed. Exit 1 on any failure."""
import collections
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
from lib131 import ROOT, gspans, load_cfg, loc, norm


def gitshow(commit, path, cache={}):
    k = (commit, path)
    if k not in cache:
        cache[k] = subprocess.run(["git", "-C", ROOT, "show", "%s:%s" % (commit, path)], capture_output=True, check=True).stdout.decode("utf-8")
    return cache[k]


def ranges(text, q):
    pat = r"\s+".join(re.escape(w) for w in q.split())
    out = []
    for m in re.finditer("(?=(" + pat + "))", text):
        a, b = m.start(1), m.end(1)
        out.append((text.count("\n", 0, a) + 1, text.count("\n", 0, b - 1) + 1))
    return out


def check_ledger(ledger):
    bad = []
    for e in ledger:
        r = ranges(gitshow(e["commit"], e["path"]), e["text"])
        if (e["first"], e["last"]) not in r:
            bad.append(e)
    return bad


def draft_spans(text, cfg):
    L = text.split("\n")
    b0 = [i for i, l in enumerate(L) if l.startswith("### %s [refereed-only] " % cfg["entry"])][0]
    u0 = [i for i, l in enumerate(L) if l.startswith("UPDATE <DATE> <HH:MM>Z: RESULTS %s (" % cfg["entry"])][0]
    a0 = ([i for i, l in enumerate(L) if l.startswith("Addendum (")] + [len(L)])[0]
    body = [l for i, l in enumerate(L[:a0]) if i not in (b0, u0)]
    sp = [norm(s) for _, _, s in gspans(norm(" ".join(body)))]
    tl = [norm(s) for _, _, s in gspans(L[b0])] + [norm(s) for _, _, s in gspans(L[u0])]
    return sp, tl, norm(" ".join(body))


def compare(text, ledger, cfg):
    sp, tl, body = draft_spans(text, cfg)
    led = [e["text"] for e in ledger if e["form"] in ("q", "qn")]
    a, b = collections.Counter(sp), collections.Counter(led)
    only_draft = list((a - b).elements())
    only_ledger = list((b - a).elements())
    noloc = [e for e in ledger if e["form"] == "q" and ("«%s» (%s)" % (e["text"], loc(e["first"], e["last"]))) not in body]
    linetexts = set(e["text"] for e in ledger if e["form"] == "line")
    tmiss = [t for t in tl if t not in linetexts]
    return sp, tl, only_draft, only_ledger, noloc, tmiss


def main(path):
    cfg = load_cfg()
    ledger = json.load(open(os.path.join(HERE, "out", "ledger.json"), encoding="utf-8"))
    text = open(path, encoding="utf-8").read()
    fails = 0
    bad = check_ledger(ledger)
    by = collections.Counter((e["commit"][:8], e["path"]) for e in ledger)
    forms = collections.Counter(e["form"] for e in ledger)
    print("lp (1) ledger: %d entries (quotations with lines %d, quotations without %d, located passages %d, quotations inside the line %d); "
          "recorded line range not among the matches of the second search: %d" % (len(ledger), forms["q"], forms["qn"], forms["l"], forms["line"], len(bad)))
    for e in bad[:8]:
        print("  BAD %s %s l. %d-%d %r" % (e["commit"][:8], e["path"], e["first"], e["last"], e["text"][:80]))
    fails += bool(bad)
    for (c, p), n in sorted(by.items()):
        print("  %s %s %d" % (c, p, n))
    sp, tl, od, ol, noloc, tmiss = compare(text, ledger, cfg)
    print("lp (2) draft: %d quotations outside the title and UPDATE lines, %d in them; in the draft but not in the ledger %d; in the ledger but not in the draft %d; "
          "'q' entries not followed by their line numbers %d; title / UPDATE quotations not in the line %d" % (len(sp), len(tl), len(od), len(ol), len(noloc), len(tmiss)))
    for x in (od + ol)[:6]:
        print("  DIFF %r" % x[:100])
    for e in noloc[:6]:
        print("  NOLOC %r" % e["text"][:100])
    fails += bool(od or ol or noloc or tmiss)
    # negative control 1
    i = next(k for k, e in enumerate(ledger) if e["form"] == "q" and e["occurrences"] == 1)
    mut = [dict(e) for e in ledger]
    mut[i]["first"] += 1
    mut[i]["last"] += 1
    c1 = len(check_ledger(mut)) == len(bad) + 1
    print("negative control 1 (one ledger entry moved by one line): caught %s" % c1)
    # negative control 2
    q = next(e["text"] for e in ledger if e["form"] == "q" and len(e["text"]) > 30 and text.count(e["text"]) == 1)
    j = text.index(q) + 5
    t2 = text[:j] + ("x" if text[j] != "x" else "y") + text[j + 1:]
    _, _, od2, ol2, _, _ = compare(t2, ledger, cfg)
    c2 = len(od2) == len(od) + 1 and len(ol2) == len(ol) + 1
    print("negative control 2 (one letter of one quotation changed in a copy of the draft): caught %s" % c2)
    fails += not (c1 and c2)
    print("lp: %s" % ("PASS" if fails == 0 else "FAILED"))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
