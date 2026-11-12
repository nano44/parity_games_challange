#!/usr/bin/env python3
"""REFEREE s34. P-N5-LEVEL (claude/l-new 1e6df499): every outermost «…» of every bullet carrying a mark [Q X] is looked up in the
source X names: X = R<id> -> that entry of docs/RESULTS.md (### R<id> … up to the next ### or ##); X = P-N5-QN / P-N5-XICYC -> the
packet file at the trunk given (sha1 printed); X = TARGET -> TARGET.md. Whitespace normalised. Written by me, not the lane's quotes211.py.
usage: level_quotes.py PACKET.md TRUNK_SHA"""
import sys, re, subprocess, hashlib
pk = open(sys.argv[1], encoding='utf-8').read().split('\n'); tr = sys.argv[2]
def show(p): return subprocess.run(['git', 'show', f'{tr}:{p}'], capture_output=True, text=True, check=True).stdout
def norm(s): return re.sub(r'\s+', ' ', s).strip()
res = show('docs/RESULTS.md').split('\n'); ent = {}; cur = None
for l in res:
    m = re.match(r'### (R\d+) ', l)
    if m: cur = m.group(1); ent[cur] = []
    elif l.startswith('### ') or l.startswith('## '): cur = None
    if cur: ent[cur].append(l)
ent = {r: norm(' '.join(v)) for r, v in ent.items()}
src = {'TARGET': norm(show('TARGET.md'))}
for name, path in [('P-N5-QN', 'docs/new/P-N5-QN.md'), ('P-N5-XICYC', 'docs/new/P-N5-XICYC.md')]:
    t = show(path); src[name] = norm(t); print(name, path, 'sha1 at', tr[:8], hashlib.sha1(t.encode()).hexdigest())
print('RESULTS entries', len(ent), 'last', list(ent)[-1])
bul = []; i = 0
while i < len(pk):
    if re.match(r'\s*- ', pk[i]):
        j = i + 1
        while j < len(pk) and pk[j].strip() and not re.match(r'\s*- ', pk[j]) and not pk[j].startswith('#') and not pk[j].startswith('|'): j += 1
        b = ' '.join(pk[i:j])
        if '[Q ' in b: bul.append((i + 1, b))
        i = j
    else: i += 1
nq = bad = 0
for ln, b in bul:
    tags = re.findall(r'\[Q ([A-Za-z0-9-]+)\]', b)
    q = []; d = 0; st = None
    for k, ch in enumerate(b):
        if ch == '«':
            if d == 0: st = k
            d += 1
        elif ch == '»':
            d -= 1
            if d == 0: q.append(b[st + 1:k])
    for s in q:
        nq += 1; n = norm(s); where = []
        for t in tags:
            hay = ent.get(t) if t.startswith('R') else src.get(t)
            if hay is not None and n in hay: where.append(t)
        ok = bool(where); bad += not ok
        print('%s l.%d tags %s found-in %s «%s»' % ('OK  ' if ok else 'MISS', ln, ','.join(tags), ','.join(where) or '-', n if len(n) < 110 else n[:107] + '…'))
print('[Q] bullets %d, quotes %d, found in the tagged source %d, missing %d' % (len(bul), nq, nq - bad, bad))
