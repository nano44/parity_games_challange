#!/usr/bin/env python3
"""REFEREE-2 successor 41: quote check of a packet whose quotes are tagged [Q LABEL ...] (P-N5-EXP's convention: every top-level «…»
after a tag, up to the next tag or the next blank line, is a verbatim quote of LABEL's source; « … » inside a quote skips text, the
pieces must occur in order). Own code; sources are read with `git show COMMIT:PATH` (run from inside the repository).
Per tagged quote: FOUND (source line of its first piece) or MISSING; for label R117 also inR117 = 1 if the quote starts inside the
RESULTS entry «### R117» (up to the next «### R<nn>» heading; else 0: found elsewhere in RESULTS). Untagged «…» are listed with the
labels whose source contains them (INFO: most are the packet's own words).
Counters: missing [tagged quote] must 0; nosource [tag] must 0; outside [R117 quote found outside the entry] must 0.
Control --ctrl: one letter of every tagged quote is changed; missing must equal the number of tagged quotes.
Usage: r2qexp.py PACKET.md COMMIT LABEL=PATH ... [--ctrl]"""
import sys, re, subprocess

def norm(t): return " ".join(t.split())
def spans(par, a, b):
    res = []; depth = 0; st = None
    for i in range(a, b):
        ch = par[i]
        if ch == "«":
            if depth == 0: st = i + 1
            depth += 1
        elif ch == "»" and depth > 0:
            depth -= 1
            if depth == 0: res.append((st, i))
    return res
def find(q, text):
    pos = 0; first = None
    for piece in [p for p in re.split(r"\s…\s", q) if p.strip()]:
        i = text.find(norm(piece), pos)
        if i < 0: return None
        if first is None: first = i
        pos = i + len(norm(piece))
    return first

def main(a):
    ctrl = "--ctrl" in a; a = [x for x in a if x != "--ctrl"]
    packet = open(a[0], encoding="utf-8").read(); commit = a[1]; src = {}; raw = {}
    for lp in a[2:]:
        lab, path = lp.split("=", 1)
        t = subprocess.run(["git", "show", f"{commit}:{path}"], capture_output=True, text=True, check=True).stdout
        raw[lab] = t; src[lab] = norm(t)
    r117 = None
    if "R117" in raw:
        lines = raw["R117"].split("\n"); idx = [i for i, l in enumerate(lines) if re.match(r"#+\s*R117\b", l)]
        if idx:
            j = idx[0]; e = j + 1
            while e < len(lines) and not re.match(r"#+\s*R\d+\b", lines[e]): e += 1
            r117 = norm("\n".join(lines[j:e]))
    C = dict(tagged=0, missing=0, nosource=0, outside=0, untagged=0); used = set()
    for par in re.split(r"\n\s*\n", packet):
        tags = [(m.start(), m.end(), m.group(1)) for m in re.finditer(r"\[Q ([^\s\]]+)[^\]]*\]", par)]
        for i, (s, e, lab) in enumerate(tags):
            end = tags[i + 1][0] if i + 1 < len(tags) else len(par)
            for (qa, qb) in spans(par, e, end):
                q = par[qa:qb]; C["tagged"] += 1; used.add(norm(q))
                if lab not in src: C["nosource"] += 1; print(f"{lab} NO-SOURCE «{norm(q)[:70]}»"); continue
                qq = q
                if ctrl:
                    k = next(i for i, ch in enumerate(q) if ch.isalpha()); qq = q[:k] + ("x" if q[k] != "x" else "y") + q[k + 1:]
                f = find(qq, src[lab])
                if f is None: C["missing"] += 1; print(f"{lab} MISSING «{norm(q)[:90]}»"); continue
                extra = ""
                if lab == "R117":
                    inside = int(r117 is not None and find(qq, r117) is not None); C["outside"] += 1 - inside; extra = f" inR117 {inside}"
                print(f"{lab} FOUND{extra} «{norm(q)[:70]}»")
        if not tags:
            for (qa, qb) in spans(par, 0, len(par)):
                q = norm(par[qa:qb])
                if q in used or len(q) < 25: continue
                C["untagged"] += 1; hit = [lab for lab in src if find(q, src[lab]) is not None]
                print(f"UNTAGGED in {hit or 'no source'} «{q[:90]}»")
    print("TOTAL " + " ".join(f"{k} {v}" for k, v in C.items()) + f" ctrl {int(ctrl)}")

if __name__ == "__main__":
    main(sys.argv[1:])
