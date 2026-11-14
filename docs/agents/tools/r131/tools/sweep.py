#!/usr/bin/env python3
"""tools/sweep.py <draft>: every guillemet quotation of the file is found verbatim (white space normalised) in one
of the sources at the commits of cfg.json. Reports per part and for the whole file; negative control: every
quotation with one letter changed must be missing. Exit 1 unless 0 are missing and the control misses all."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib131 import Source, gspans, load_cfg, norm, sources


def spoil(s):
    for i, ch in enumerate(s):
        if ch.isalpha():
            return s[:i] + ("Ж" if ch != "Ж" else "Я") + s[i + 1:]
    return s + "Ж"


def main(path):
    cfg = load_cfg()
    S = sources(cfg)
    S["CHK"] = Source("CHK", cfg["heads"]["l-red-b"], "experiments/red-b/check.sh", "the lane's check.sh")
    texts = [(k, s.norm) for k, s in S.items()]
    L = open(path, encoding="utf-8").read().split("\n")
    b0 = [i for i, l in enumerate(L) if l.startswith("### %s [refereed-only] " % cfg["entry"])][0]
    p0 = [i for i, l in enumerate(L) if l.startswith("Proposed GAPS ")][0]
    a0 = ([i for i, l in enumerate(L) if l.startswith("Addendum (")] + [len(L)])[0]
    parts = [("header", L[:b0]), ("title line", L[b0:b0 + 1]), ("entry block below the title", L[b0 + 1:p0]),
             ("proposal and UPDATE", L[p0:a0]), ("Addendum", L[a0:]), ("whole file", L)]
    bad = 0
    for name, lines in parts:
        try:
            sp = gspans(norm(" ".join(lines)))
        except ValueError as e:
            print("sweep %s: guillemets do not balance: %s" % (name, str(e)[:100]))
            bad += 1
            continue
        miss = [q for _, _, q in sp if not any(norm(q) in t for _, t in texts)]
        ctrl = sum(1 for _, _, q in sp if not any(norm(spoil(q)) in t for _, t in texts))
        ok = not miss and ctrl == len(sp)
        print("sweep %s: %d quotations, %d not found; control (one letter changed): %d of %d not found: %s" % (name, len(sp), len(miss), ctrl, len(sp), "ok" if ok else "FAIL"))
        for q in miss[:8]:
            print("  missing: %r" % q[:110])
        bad += not ok
    print("sweep: sources %d (%s)" % (len(texts), " ".join(k for k, _ in texts)))
    print("sweep: %s" % ("PASS" if bad == 0 else "FAILED"))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
