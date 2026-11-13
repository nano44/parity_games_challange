#!/usr/bin/env python3
"""REFEREE s32. Box 208 (claude/l-new 8db300fe, docs/new/N5-LEVEL-box208.md): every outermost «…» of every bullet marked [Q] is located
in the landed RESULTS entries (title line + body up to the next ###).  The bullet's own R-ids (R\\d+ before the first «) name where the
quote is expected; the script prints the entries that contain it and flags a quote found in none of the bullet's named entries.
usage: box208_quotes.py <box208.md> <RESULTS.md>"""
import sys, re
txt = open(sys.argv[1], encoding='utf-8').read().split('\n'); res = open(sys.argv[2], encoding='utf-8').read().split('\n')
RIDS = ['R104', 'R118', 'R121', 'R122', 'R123', 'R126']
ent = {}
for r in RIDS:
    idx = [i for i, l in enumerate(res) if l.startswith('### %s [' % r)]; assert len(idx) == 1, (r, idx)
    j = idx[0] + 1
    while j < len(res) and not res[j].startswith('### '): j += 1
    ent[r] = (res[idx[0]], '\n'.join(res[idx[0]:j]))
def norm(s): return re.sub(r'\s+', ' ', s).strip()
# bullets: a line starting with '- [Q]' (any indent) up to the next line starting with '- ' or '#' or blank
bul = []; i = 0
while i < len(txt):
    if re.match(r'\s*- \[Q\]', txt[i]):
        j = i + 1
        while j < len(txt) and txt[j].strip() and not re.match(r'\s*- ', txt[j]) and not txt[j].startswith('#'): j += 1
        bul.append((i + 1, ' '.join(txt[i:j]))); i = j
    else: i += 1
nq = miss = off = 0
for (ln, b) in bul:
    named = re.findall(r'R\d+', b.split('«')[0]); quotes = []; depth = 0; start = None
    for k, ch in enumerate(b):
        if ch == '«':
            if depth == 0: start = k + 1
            depth += 1
        elif ch == '»':
            depth -= 1
            if depth == 0: quotes.append(b[start:k])
    for q in quotes:
        nq += 1; n = norm(q); hits = [r + ('(title)' if n in norm(ent[r][0]) else '(body)') for r in RIDS if n in norm(ent[r][1])]
        ok = any(h.split('(')[0] in named for h in hits)
        if not hits: miss += 1
        elif not ok: off += 1
        print('%s l.%d named %s found %s «%s»' % ('OK  ' if ok else ('MISS' if not hits else 'ELSE'), ln, ','.join(named), ','.join(hits) or '-', n if len(n) < 110 else n[:107] + '…'))
print('[Q] bullets %d, quotes %d, found in a named entry %d, found only elsewhere %d, missing %d' % (len(bul), nq, nq - miss - off, off, miss))
