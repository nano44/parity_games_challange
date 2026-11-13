#!/usr/bin/env python3
"""Copy CHECKER C143's verdicts and notes onto the rows of lean/lemmas/INDEX.md (L-FORMAL; Lead brief item (2)).

Inputs (no text is retyped: verdict lists and notes are parsed from C143.md):
  C143.md          docs/checker/C143.md of claude/checker 37fcbd21 (pass the path, e.g. a `git show` copy)
  c143deps.out     output of `lake env lean check/c143deps.lean` (per theorem: does its type depend on
                   PG.OptCounter, PG.Genome.IdealCycRun, PG.Genome.pr)
  INDEX.md         rewritten in place: a last column «CHECKER C143» is added (or replaced, so the script is idempotent)
Attachment rule (stated in the header paragraph the script writes):
  - verdicts: C143 §4 «PASS» list -> PASS; any other theorem of MANIFEST c8963698 (= Axioms.lean at c8963698) -> build-only;
    a theorem not in that MANIFEST -> «not in C143 (after c8963698)»;
  - notes travel with PASS theorems only (C143 §4 «Notes that travel with these rows»):
    N-1 if the type depends on PG.OptCounter («Every row that rests on F1 or IdealCycRun carries it», C143 §3);
    N-2 if it depends on PG.Genome.IdealCycRun; N-7 if it depends on PG.Genome.pr;
    N-3 on Genome.k2, N-4 on Genome.k3, N-5 on Genome.k4, N-6 on Genome.l5 and Genome.imp_non_stall (the theorems the notes name).
Usage: python3 -I check/c143notes.py C143.md check/out/c143deps.out INDEX.md AXIOMS_AT_c8963698.lean"""
import re, sys

c143, depsf, indexf, axold = sys.argv[1:5]
txt = open(c143).read().split("\n")

# notes, verbatim
notes = {}
for l in txt:
    m = re.match(r"^\s*- \(N-(\d)\) (.*)$", l)
    if m:
        notes[int(m.group(1))] = "(N-%s) %s" % (m.group(1), m.group(2))
assert sorted(notes) == [1, 2, 3, 4, 5, 6, 7], notes

# PASS list, verbatim from §4 (the lines between «**PASS**» and «**Notes»)
i0 = next(i for i, l in enumerate(txt) if l.startswith("- **PASS**"))
i1 = next(i for i, l in enumerate(txt) if l.strip().startswith("- **Notes that travel"))
passtxt = " ".join(txt[i0 + 1:i1])
passed = set()
for tok in re.split(r"[,;]", passtxt):
    tok = tok.strip().lstrip("-").strip().rstrip(".")
    if tok.startswith("Genome.") and " " in tok:   # «Genome.k1, k2, …» continues with bare names
        tok = tok.split()[0]
    if tok:
        passed.add(tok)
# bare names after «Genome.k1, …» and the run rows are in namespace PG.Genome; resolve against Axioms.lean below
old = [l.split()[2] for l in open(axold) if l.startswith("#print axioms ")]
assert len(old) == 69, len(old)
def resolve(t):
    c = [n for n in old if n == "PG." + t or n.endswith("." + t)]
    assert len(c) == 1, (t, c)
    return c[0]
passed = {resolve(t) for t in passed}
assert len(passed) == 23, sorted(passed)

deps = {}
for l in open(depsf):
    if l.startswith("DEP "):
        f = [x.strip() for x in l[4:].split("|")]
        deps[f[0]] = {k.split()[0]: k.split()[1] == "true" for k in f[1:]}
named = {"PG.Genome.k2": [3], "PG.Genome.k3": [4], "PG.Genome.k4": [5], "PG.Genome.l5": [6], "PG.Genome.imp_non_stall": [6]}

def notes_of(n):
    d = deps[n]; ks = []
    if d["OptCounter"]: ks.append(1)
    if d["IdealCycRun"]: ks.append(2)
    ks += named.get(n, [])
    if d["pr"]: ks.append(7)
    return sorted(set(ks))

allnames = list(deps)
def find(cell):
    out = []
    for n in allnames:
        parts = n.split(".")[1:]                      # drop PG
        for k in range(len(parts)):
            suf = ".".join(parts[k:])
            if re.search(r"(?<![\w.'])" + re.escape(suf) + r"(?![\w'])", cell):
                out.append(n); break
    return out

def verdict(n):
    if n in passed: return "PASS"
    if n in old: return "build-only"
    return "not in C143 (after c8963698)"

COL = "CHECKER C143"
B, E = "<!-- C143 begin (written by check/c143notes.py) -->", "<!-- C143 end -->"
doc = open(indexf).read()
if B in doc: doc = doc[:doc.index(B)] + doc[doc.index(E) + len(E):].lstrip("\n")
para = (B + "\n" + "Column «CHECKER C143» (CHECKER C143 = docs/checker/C143.md on claude/checker 37fcbd21, ruling on MANIFEST c8963698; "
        "written by check/c143notes.py, which copies the verdict lists and the notes N-1..N-7 from C143.md, not retyped): PASS = "
        "C143 §4's PASS list (cite «Lean-checked, CHECKER C143» with the Lean Statement's text and the notes on the row); build-only = "
        "«build and axioms PASS», statement NOT RULED (cite only as «builds, axioms allowed» until diffed); «not in C143» = a theorem "
        "added after c8963698. Attachment rule («L-FORMAL reading, Lead accepted 01:06Z»): notes are attached to PASS theorems only: N-1 where the theorem's type depends on PG.OptCounter, N-2 where it "
        "depends on PG.Genome.IdealCycRun, N-7 where it depends on PG.Genome.pr (computed by check/c143deps.lean, output "
        "check/out/c143deps.out), N-3..N-6 on the theorems they name. Theorems of Axioms.lean with no row here (build-only): "
        + ", ".join(n.replace("PG.", "") for n in []) + "NOROW.\n" + E + "\n")
i = doc.index("| Lane / landed text |")
doc = doc[:i] + para + "\n" + doc[i:]
doc = re.sub(r"(\n\| [^\n]*\|)\n\n(\| )", r"\1\n\2", doc)       # one table: drop blank lines between rows
lines = doc.split("\n")
out = []; rows = []
for l in lines:
    if l.startswith("| Lane / landed text |"):
        cells = l.split(" | ")
        if COL not in l: l = l + " " + COL + " |"
        out.append(l); continue
    if l.startswith("| --- |"):
        if l.count("---") == 4: l = l + " --- |"
        out.append(l); continue
    if l.startswith("| ") and " | " in l:
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", l.strip()[1:-1])]   # unescaped pipes only
        if len(cells) >= 5 and cells[4].startswith("C143:"): cells = cells[:4]   # idempotent: drop an old column
        while len(cells) < 4: cells.append("")
        names = find(cells[2])
        if not names:
            v = "C143: — (no theorem in this row)"
        else:
            groups = []                                   # theorems with the same verdict and notes share one entry
            for n in names:
                key = (verdict(n), tuple(notes_of(n)) if n in passed else ())
                for g in groups:
                    if g[0] == key: g[1].append(n); break
                else: groups.append((key, [n]))
            parts = []
            for (vd, ks), ns in groups:
                s = "%s: %s" % (", ".join(n.replace("PG.", "") for n in ns), vd)
                if ks: s += ". " + " ".join(notes[k] for k in ks)
                parts.append(s)
            v = "C143: " + " / ".join(parts)
        rows.append((names, v))
        out.append("| " + " | ".join(cells[:4]) + " | " + v + " |"); continue
    out.append(l)
cov = [n for ns, _ in rows for n in ns]
norow = [n.replace("PG.", "") for n in allnames if n not in cov]
open(indexf, "w").write("\n".join(out).replace("NOROW.", ", ".join(norow) + "."))
print("rows %d; theorems placed %d (distinct %d); PASS placed %d of %d; build-only placed %d; not-in-C143 placed %d" % (
    len(rows), len(cov), len(set(cov)), len(set(cov) & passed), len(passed),
    len({n for n in cov if verdict(n) == "build-only"}), len({n for n in cov if verdict(n).startswith("not in")})))
print("theorems of Axioms.lean in no row:", [n for n in allnames if n not in cov])
