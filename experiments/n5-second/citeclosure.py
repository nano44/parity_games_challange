#!/usr/bin/env python3
"""Box 11 item 1 (Lead 2026-10-26 07:15Z): mechanical check of L-NEW's (Sigma-tau) audit list (docs/new/N5-EPR-box45.md §9.2, l-new a198c9b9).
Parses docs/RESULTS.md into entries ("### Rnn ..." headers) and computes the transitive closure of RESULTS citations from given roots.
Citation tokens: "Rnn" (word boundary), with ranges "Rnn-Rmm" / "Rnn–Rmm" expanded; NOT counted: tokens inside other naming schemes
(followed by "-" + letter or digit-letter, e.g. "R2-N5-KW", "R72-fx", "R2-P4"; preceded by "/" or "-" as in docs/red/R73-..., OUT-R1,
NEB-R1; a lemma label right after a packet name, "P-N5-NH (R1)"; preceded by "L-RED",
"L-RED's", "REFEREE-2" within 12 characters, i.e. lane report numbers such as "L-RED R73").
Every citation is classified by the entry bullet it sits in: HEAD (the "### " line), OBJ (Object / Setting), CLAIM (Claims signed / premises /
the lettered items), NOTSIGNED ("Not signed"), LIMITS ("Honest limits"), DATA ("Data"), SIG ("Signatures"), TARGET ("TARGET.md diff"), OTHER.
Closures: PROOF = HEAD + OBJ + CLAIM + OTHER edges; ALL = every edge. Output: both closures, the per-edge kinds, and the diff against a list.
Usage: citeclosure.py [--roots R48,R50] [--list "R15,R17,..."]"""
import re
import sys
from collections import defaultdict

ROOT_DIR = __file__.rsplit("/experiments/", 1)[0]
TOK = re.compile(r"(?<![\w/-])R(\d+)(?:\s*[-–]\s*R(\d+))?(?![\w])(?!-[A-Za-z])(?!-\d+[A-Za-z])")
LANE = re.compile(r"(L-RED(?:'s)?|REFEREE-2|REFEREE|L-NEW|L-SI|L-LIT|L-COMP)\s*(?:succ\.?\s*\d+\s*)?$")


def kind_of(bullet):
    b = bullet.lstrip("- ").lower()
    for key, k in (("object", "OBJ"), ("setting", "OBJ"), ("claims", "CLAIM"), ("not signed", "NOTSIGNED"), ("honest limit", "LIMITS"),
                   ("data", "DATA"), ("signature", "SIG"), ("target.md", "TARGET")):
        if b.startswith(key):
            return k
    return "OTHER"


def parse(path):
    entries, cur, bullet = {}, None, None
    for line in open(path, encoding="utf-8"):
        m = re.match(r"^### R(\d+)\b", line)
        if m:
            cur = int(m.group(1)); entries[cur] = []; bullet = "HEAD"; entries[cur].append(("HEAD", line)); continue
        if line.startswith("## ") or line.startswith("### "):
            cur = None; continue
        if cur is None:
            continue
        if line.startswith("- "):
            bullet = kind_of(line)
        entries[cur].append((bullet if bullet != "HEAD" else "OTHER", line))
    return entries


def cites(entries):
    E = defaultdict(lambda: defaultdict(set))   # E[src][dst] = set of kinds
    for src, lines in entries.items():
        for kind, line in lines:
            for m in TOK.finditer(line):
                pre = line[max(0, m.start() - 14):m.start()]
                if LANE.search(pre) or re.search(r"P-N5-[\w-]+ \($", pre):   # lane report numbers; a packet's own lemma label "P-N5-NH (R1)"
                    continue
                a = int(m.group(1)); b = int(m.group(2)) if m.group(2) else a
                for dst in range(a, b + 1) if b >= a and b - a < 40 else [a]:
                    if dst != src and dst in entries:
                        E[src][dst].add(kind)
    return E


def closure(E, roots, kinds):
    seen, todo = set(), list(roots)
    while todo:
        x = todo.pop()
        if x in seen:
            continue
        seen.add(x)
        for y, ks in E[x].items():
            if ks & kinds:
                todo.append(y)
    return seen


def fmt(s):
    return ", ".join(f"R{x}" for x in sorted(s))


def main():
    a = sys.argv[1:]
    roots = [int(x.lstrip("R")) for x in (a[a.index("--roots") + 1] if "--roots" in a else "R48,R50").split(",")]
    lst = a[a.index("--list") + 1] if "--list" in a else "R15,R17,R18,R19-R34,R38,R39,R42,R44,R45,R48,R50"
    L = set()
    for part in lst.split(","):
        m = re.match(r"R(\d+)(?:-R(\d+))?", part.strip())
        L |= set(range(int(m.group(1)), int(m.group(2) or m.group(1)) + 1))
    entries = parse(ROOT_DIR + "/docs/RESULTS.md")
    E = cites(entries)
    proof = closure(E, roots, {"HEAD", "OBJ", "CLAIM", "OTHER"})
    allc = closure(E, roots, {"HEAD", "OBJ", "CLAIM", "OTHER", "NOTSIGNED", "LIMITS", "DATA", "SIG", "TARGET"})
    print("entries parsed:", len(entries), "roots:", fmt(roots))
    print("PROOF closure (", len(proof), "):", fmt(proof))
    print("ALL closure   (", len(allc), "):", fmt(allc))
    print("list (", len(L), "):", fmt(L))
    print("PROOF closure minus list:", fmt(proof - L) or "none")
    print("list minus PROOF closure:", fmt(L - proof) or "none")
    print("ALL closure minus list:", fmt(allc - L) or "none")
    print("edges into entries outside the list (src -> dst: kinds):")
    for src in sorted(allc):
        for dst, ks in sorted(E[src].items()):
            if dst not in L:
                print(f"  R{src} -> R{dst}: {','.join(sorted(ks))}")


if __name__ == "__main__":
    main()
