#!/usr/bin/env python3
"""REFEREE-2 successor 42: quote check of a FIXES file whose labels point at different commits (P-N5-EXP-fixes.md entries 2-5).
r2qexp.py lineage (its norm / spans / find are imported): every top-level «…» after a tag [Q LABEL …], up to the next tag or the
next blank line, is a verbatim quote of LABEL's source; « … » inside a quote skips text, the pieces must occur in order.
Sources: LABEL=COMMIT:PATH, read with `git show`; LABEL=COMMIT:PATH#ENTRY restricts the source to the RESULTS entry «### ENTRY»
(up to the next «### R<nn>» / «### DE<nn>» heading). --defer L1,L2: quotes of these labels are counted and listed as DEFERRED and
their sources are NOT opened (used for docs/referee/ files before my own addendum is committed). --from N: only the lines ≥ N of
the file (entries 2-5 begin at line 126 of the file at l-red-b 24f4d436).
Counters: missing [tagged quote] must 0; nosource [tagged quote with a label that is neither given nor deferred] must 0.
Control --ctrl: one letter of every checked quote is changed; missing must equal the number of checked quotes.
Usage: r2qfix.py FIXES.md [--from N] [--defer L1,L2] [--ctrl] LABEL=COMMIT:PATH[#ENTRY] ..."""
import sys, os, re, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE]
from r2qexp import norm, spans, find


def main(a):
    ctrl = "--ctrl" in a; a = [x for x in a if x != "--ctrl"]; frm = 1; defer = set(); rest = []; i = 0
    while i < len(a):
        if a[i] == "--from": frm = int(a[i + 1]); i += 2
        elif a[i] == "--defer": defer = set(a[i + 1].split(",")); i += 2
        else: rest.append(a[i]); i += 1
    packet = "\n".join(open(rest[0], encoding="utf-8").read().split("\n")[frm - 1:]); src = {}
    for lp in rest[1:]:
        lab, spec = lp.split("=", 1); ent = None
        if "#" in spec: spec, ent = spec.split("#", 1)
        t = subprocess.run(["git", "show", spec], capture_output=True, text=True, check=True).stdout
        if ent:
            lines = t.split("\n"); idx = [n for n, l in enumerate(lines) if re.match(r"#+\s*" + re.escape(ent) + r"\b", l)]
            assert idx, f"entry {ent} not found in {spec}"
            j = idx[0]; e = j + 1
            while e < len(lines) and not re.match(r"#+\s*(R|DE)\d+\b", lines[e]): e += 1
            t = "\n".join(lines[j:e])
        src[lab] = norm(t)
    C = dict(tagged=0, checked=0, found=0, missing=0, deferred=0, nosource=0); per = {}
    for par in re.split(r"\n\s*\n", packet):
        tags = [(m.start(), m.end(), m.group(1)) for m in re.finditer(r"\[Q ([^\s\]]+)[^\]]*\]", par)]
        for n, (s, e, lab) in enumerate(tags):
            end = tags[n + 1][0] if n + 1 < len(tags) else len(par)
            for (qa, qb) in spans(par, e, end):
                q = par[qa:qb]; C["tagged"] += 1; per.setdefault(lab, [0, 0]); per[lab][0] += 1
                if lab in defer: C["deferred"] += 1; print(f"{lab} DEFERRED «{norm(q)[:70]}»"); continue
                if lab not in src: C["nosource"] += 1; print(f"{lab} NO-SOURCE «{norm(q)[:70]}»"); continue
                qq = q; C["checked"] += 1
                if ctrl:
                    k = next(n2 for n2, ch in enumerate(q) if ch.isalpha()); qq = q[:k] + ("x" if q[k] != "x" else "y") + q[k + 1:]
                if find(qq, src[lab]) is None: C["missing"] += 1; print(f"{lab} MISSING «{norm(q)[:90]}»"); continue
                C["found"] += 1; per[lab][1] += 1; print(f"{lab} FOUND «{norm(q)[:70]}»")
    print("PER LABEL (tagged, found) " + " ".join(f"{l} {v[0]} {v[1]}" for l, v in sorted(per.items())))
    print("TOTAL " + " ".join(f"{k} {v}" for k, v in C.items()) + f" ctrl {int(ctrl)}")


if __name__ == "__main__":
    main(sys.argv[1:])
