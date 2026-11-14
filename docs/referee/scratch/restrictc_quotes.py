#!/usr/bin/env python3
"""REFEREE s32. Locate every outermost «…» quote of a section of a lane file in a RESULTS entry (title line + body up to the next ###).
usage: restrictc_quotes.py <lane_text_file> <start_marker> <end_marker_or_EOF> <RESULTS.md> <Rid> [<Rid> ...]
Prints, per quote: the entries (of those named) that contain it verbatim, and whether it is in the entry's title line."""
import sys, re
lane, m0, m1, res = sys.argv[1:5]; rids = sys.argv[5:]
txt = open(lane, encoding='utf-8').read()
a = txt.index(m0); b = txt.index(m1, a + 1) if m1 != 'EOF' else len(txt)
sec = txt[a:b]
# outermost quotes, nesting-aware
quotes = []; depth = 0; start = None
for i, ch in enumerate(sec):
    if ch == '«':
        if depth == 0: start = i + 1
        depth += 1
    elif ch == '»':
        depth -= 1
        if depth == 0: quotes.append(sec[start:i])
lines = open(res, encoding='utf-8').read().split('\n')
ent = {}
for r in rids:
    idx = [i for i, l in enumerate(lines) if l.startswith('### %s [' % r)]
    assert len(idx) == 1, (r, idx)
    j = idx[0] + 1
    while j < len(lines) and not lines[j].startswith('### '): j += 1
    ent[r] = (lines[idx[0]], '\n'.join(lines[idx[0]:j]))
def norm(s): return re.sub(r'\s+', ' ', s)
miss = 0
for q in quotes:
    nq = norm(q); hits = []
    for r in rids:
        t, body = ent[r]
        if nq in norm(body): hits.append(r + ('(title)' if nq in norm(t) else '(body)'))
    if not hits: miss += 1
    print(('OK   ' if hits else 'MISS ') + ','.join(hits).ljust(24) + ' «' + (nq if len(nq) < 150 else nq[:147] + '…') + '»')
print('quotes %d, missing %d' % (len(quotes), miss))
