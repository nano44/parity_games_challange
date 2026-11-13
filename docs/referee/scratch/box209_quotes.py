#!/usr/bin/env python3
"""REFEREE s33. Box 209 (claude/l-new 311bbf81, docs/new/N5-LEVEL3-box209.md): every outermost «…» of every bullet or paragraph that
carries a [Q] mark is located in the landed RESULTS entries (### R<id> … up to the next ###) and in TARGET.md. Printed per quote: the
R-ids named in the bullet before the quote, the entries that contain it. MISS = found in no entry and not in TARGET.md.
usage: box209_quotes.py <box209.md> <RESULTS.md> <TARGET.md>"""
import sys, re
txt = open(sys.argv[1], encoding='utf-8').read().split('\n'); res = open(sys.argv[2], encoding='utf-8').read().split('\n')
tgt = re.sub(r'\s+', ' ', open(sys.argv[3], encoding='utf-8').read())
ent = {}; cur = None
for l in res:
    m = re.match(r'### (R\d+) \[', l)
    if m: cur = m.group(1); ent[cur] = []
    elif l.startswith('### ') or l.startswith('## '): cur = None
    if cur: ent[cur].append(l)
ent = {r: re.sub(r'\s+', ' ', ' '.join(ls)) for r, ls in ent.items()}
def norm(s): return re.sub(r'\s+', ' ', s).strip()
bul = []; i = 0
while i < len(txt):
    if re.match(r'\s*(- |\| )', txt[i]) or (txt[i].strip() and not txt[i].startswith('#')):
        j = i + 1
        while j < len(txt) and txt[j].strip() and not re.match(r'\s*- ', txt[j]) and not txt[j].startswith('#') and not txt[j].startswith('|'): j += 1
        b = ' '.join(txt[i:j])
        if '[Q]' in b: bul.append((i + 1, b))
        i = j
    else: i += 1
nq = miss = named_ok = 0
for (ln, b) in bul:
    quotes = []; depth = 0; start = None
    for k, ch in enumerate(b):
        if ch == '«':
            if depth == 0: start = k
            depth += 1
        elif ch == '»':
            depth -= 1
            if depth == 0: quotes.append((start, b[start + 1:k]))
    for (pos, q) in quotes:
        nq += 1; n = norm(q); named = re.findall(r'R\d+', b[:pos]); hits = [r for r in ent if n in ent[r]]; intgt = n in tgt
        ok = any(h in named for h in hits)
        if not hits and not intgt: miss += 1
        named_ok += ok
        print('%s l.%d named %s found %s%s «%s»' % ('OK  ' if ok else ('MISS' if not hits and not intgt else 'ELSE'), ln, ','.join(sorted(set(named))) or '-',
              ','.join(hits) or '-', ' TARGET' if intgt else '', n if len(n) < 100 else n[:97] + '…'))
print('[Q] bullets %d, quotes %d, found in an entry named before the quote %d, found only elsewhere %d, missing %d' % (len(bul), nq, named_ok, nq - named_ok - miss, miss))
