# REFEREE succ. 13 closure with filters; prints every excluded match for audit. python3 -I closure2.py RESULTS roots...
import re, sys
txt = open(sys.argv[1]).read()
ents = {m.group(1): m.group(0) for m in re.finditer(r'^### (R\d+)\b(.*?)(?=^### R\d+\b|^## |\Z)', txt, re.S | re.M)}
def refs(r):
    out, excl = set(), []
    t = ents[r]
    for m in re.finditer(r'\bR(\d+)\b', t):
        pre, post = t[max(0, m.start()-8):m.start()], t[m.end():m.end()+2]
        why = None
        if post.startswith('-') or post.startswith('/'): why = 'doc-name'
        elif pre.endswith('L-RED ') or pre.endswith('red/') : why = 'L-RED item'
        elif pre.endswith('(') and post.startswith(')'): why = 'label (Rk)'
        elif pre.endswith('REFEREE-2 ') : why = 'R2'
        if 'R'+m.group(1) == r: continue
        if why: excl.append((why, 'R'+m.group(1), t[max(0,m.start()-50):m.end()+20].replace('\n',' ')))
        else: out.add('R'+m.group(1))
    return out, excl
roots = sys.argv[2:]
seen, todo, E, X = set(), list(roots), {}, {}
while todo:
    r = todo.pop()
    if r in seen or r not in ents: continue
    seen.add(r); E[r], X[r] = refs(r); todo += E[r]
k = lambda s: int(s[1:])
print('CLOSURE', len(seen), ' '.join(sorted(seen, key=k)))
for r in sorted(E, key=k):
    print(r, '->', ' '.join(sorted(E[r], key=k)))
print('--- excluded')
for r in sorted(X, key=k):
    for w in X[r]: print(r, *w, sep=' | ')
