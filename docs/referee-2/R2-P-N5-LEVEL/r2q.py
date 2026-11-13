#!/usr/bin/env python3
"""REFEREE-2 successor 38: premise tool for packet P-N5-LEVEL (box 208). Own code; reads only docs/RESULTS.md (trunk, via git show)
and the packet files given. Three commands:
  r2q.py RESULTS.md render SPEC ...     SPEC = R118:a-e,i | R121 | R104:title | R123:b,c,e ...
        prints, with RESULTS line numbers, the landed entry's title sha1 / size and the lettered items of its «Claims signed» list
        («Statements as signed»); «title» prints the title line itself (R104's definitions [DEF] are in its title).
  r2q.py RESULTS.md quotes FILE ...     every balanced «…» of each FILE (whitespace-normalised): does it occur verbatim in RESULTS, and in
        which landed entries? A quote with « … » inside is tested piece by piece. Prints MISSING quotes in full.
  r2q.py RESULTS.md cites FILE ...      every R-id cited in FILE (count) and whether trunk RESULTS has «### R<id> »; every «R<id> (x)»
        item reference and whether that entry has an item (x).
"""
import sys, re, hashlib
res_path, cmd = sys.argv[1], sys.argv[2]
RAW = open(res_path, encoding="utf-8").read(); L = RAW.split("\n")
heads = [i for i, l in enumerate(L) if l.startswith("### ")]
def rid_of(i): return L[i].split()[1]
ENT = {rid_of(i): (i, heads[k + 1] if k + 1 < len(heads) else len(L)) for k, i in enumerate(heads)}
norm = lambda s: " ".join(s.split())
NRES = norm(RAW)
NENT = {r: norm("\n".join(L[a:b])) for r, (a, b) in ENT.items()}
def items(rid):
    """{letter: (first_line_index, text)} of the lettered items inside the «- Claims signed» bullet (2-space indent «(x) »)."""
    a, b = ENT[rid]; out = {}; cur = None; inside = False
    for j in range(a + 1, b):
        l = L[j]
        if l.startswith("- "):
            inside = l.startswith("- Claims signed") or l.startswith("- Setting") or l.startswith("- Statements as signed"); cur = None
            continue
        if not inside: continue
        m = re.match(r"^  \(([a-z]′?)\) ", l)
        if m: cur = m.group(1); out[cur] = [j, l.strip()]
        elif cur and l.startswith("    "): out[cur][1] += " " + l.strip()
        elif cur and l.startswith("  ") and not re.match(r"^  \(", l): out[cur][1] += " " + l.strip()
    return out
def letters(spec):
    out = []
    for part in spec.split(","):
        if "-" in part and len(part) == 3: out += [chr(c) for c in range(ord(part[0]), ord(part[2]) + 1)]
        else: out.append(part)
    return out
def quotes(s):
    out = []; i = 0
    while True:
        i = s.find("«", i)
        if i < 0: return out
        d = 0; j = i
        while j < len(s):
            if s[j] == "«": d += 1
            elif s[j] == "»":
                d -= 1
                if d == 0: break
            j += 1
        if j >= len(s): return out
        out.append(s[i + 1:j]); i = j + 1
if cmd == "render":
    print("RESULTS sha1", hashlib.sha1(RAW.encode()).hexdigest(), len(L), "lines")
    for spec in sys.argv[3:]:
        rid, _, sel = spec.partition(":")
        if rid not in ENT: print(f"== {rid}: NOT LANDED (no «### {rid} » in this RESULTS)"); continue
        a, b = ENT[rid]; t = L[a]
        print(f"== {rid}: lines {a + 1}-{b}; title {len(t.encode())} B, sha1 {hashlib.sha1(t.encode()).hexdigest()[:12]}")
        it = items(rid)
        if sel == "title" or not it: print(f"   [title, l. {a + 1}] {t}"); 
        if sel == "title": continue
        for x in (letters(sel) if sel else sorted(it)):
            if x in it: print(f"   ({x}) [l. {it[x][0] + 1}] {it[x][1]}")
            else: print(f"   ({x}) NO SUCH ITEM in {rid} (items: {' '.join(sorted(it))})")
elif cmd == "quotes":
    for fn in sys.argv[3:]:
        txt = norm(open(fn, encoding="utf-8").read()); qs = quotes(txt); miss = 0; seen = set()
        print(f"== {fn}: {len(qs)} quotes")
        for q in qs:
            if q in seen: continue
            seen.add(q)
            pieces = [p.strip() for p in re.split(r"\s…\s|\s\.\.\.\s", q) if len(p.strip()) >= 12] if (" … " in q or " ... " in q) else [q]
            ok = all(p in NRES for p in pieces)
            where = sorted({r for r, t in NENT.items() if all(p in t for p in pieces)}, key=lambda r: (r[0], int(re.sub(r"\D", "", r) or 0)))
            if ok: print(f"   FOUND {'(pieces) ' if len(pieces) > 1 else ''}in {','.join(where) if where else 'RESULTS (outside an entry / across entries)'} :: {q[:110]}{'…' if len(q) > 110 else ''}")
            else: miss += 1; print(f"   MISSING :: {q}")
        print(f"   distinct {len(seen)}, missing from RESULTS {miss} (a missing quote may be a name, a label, or a non-RESULTS source: read each)")
elif cmd == "cites":
    for fn in sys.argv[3:]:
        txt = norm(open(fn, encoding="utf-8").read()); print(f"== {fn}")
        ids = {}
        for m in re.finditer(r"\bR(\d{1,3})\b", txt): ids["R" + m.group(1)] = ids.get("R" + m.group(1), 0) + 1
        for r in sorted(ids, key=lambda r: int(r[1:])): print(f"   {r}: cited {ids[r]}×; {'landed' if r in ENT else 'NOT in trunk RESULTS'}")
        refs = sorted(set(re.findall(r"\bR(\d{1,3}) \(([a-z]′?)\)", txt)), key=lambda p: (int(p[0]), p[1]))
        for n, x in refs:
            r = "R" + n; it = items(r) if r in ENT else {}
            print(f"   {r} ({x}): {'item exists: ' + it[x][1][:90] if x in it else 'NO SUCH ITEM' if r in ENT else 'entry not landed'}")
