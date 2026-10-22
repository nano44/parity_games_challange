"""REFEREE-2, P-C1P addendum A1 (R47). DATA on the pinned C++ with r2log_a1.patch (adds "D top : X" before every V-top of a
depth-0 Dom loop, dtl.cpp 878-890 and 962-975). Per q-phase:
  DOMMONO  for every Dom input (R_j, V_j) seen in several searches of the phase, the step-output vector (X_1, ..., X_|V|)
           (X_i = X after the step of the i-th V-top; the last one = G' minus R_{j+1}) is componentwise non-decreasing.
  I        chain-keeping transitions, against the CK bound with H = 0: (n+1)(|P|+1)(1+n^2)+1 (a stricter test than CK itself)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c1pcheck import readpg, classof, run, cmp_chain
def parse2(lines):
    S = []; cur = None
    for ln in lines:
        if not ln: continue
        k = ln[0]
        if k == 'S':
            a, b = ln[2:].split(':'); cur = dict(pl=int(a), G=frozenset(map(int, b.split())), calls=[]); S.append(cur)
        elif k == 'C':
            h, R, V = ln[2:].split(':'); res, e = map(int, h.split())
            cur['calls'].append(dict(R=frozenset(map(int, R.split())), res=res, e=e if res == -1 else 0, V=frozenset(map(int, V.split())), D=[]))
        elif k == 'D':
            a, b = ln[2:].split(':'); cur['calls'][-1]['D'].append((int(a), frozenset(map(int, b.split()))))
        elif k == 'X': cur['ret'] = int(ln[2:])
    for s in S:
        cl = s['calls']; ch = []
        for i, c in enumerate(cl):
            nxt = cl[i + 1]['R'] if i + 1 < len(cl) else c['R']
            piece = c['R'] - nxt if i + 1 < len(cl) else frozenset()
            ch.append((c['R'], c['res'], c['e'], c['V'] if c['res'] != 0 else frozenset(), piece))
            if c['D']:
                Xs = [x for _, x in c['D'][1:]] + [s['G'] - nxt]
                c['vec'] = (tuple(t for t, _ in c['D']), tuple(Xs))
        s['chain'] = ch
    return S
def main(oink, tmp, files):
    tot = dict(dom_pairs=0, dom_viol=0, I=0, P=0, I_bound_viol=0, phases=0)
    for f in files:
        g = readpg(f); C = classof(g)
        if not isinstance(C, int): print(os.path.basename(f), 'not in class'); continue
        n = len(g[0]); q = 1 - C; S = parse2(run(g, os.path.join(tmp, 'a')))
        phases = []
        for s in S:
            if s['pl'] != q: continue
            if phases and phases[-1][-1]['G'] == s['G']: phases[-1].append(s)
            else: phases.append([s])
        loc = dict(dom_pairs=0, dom_viol=0, I=0, P=0)
        for ph in phases:
            tot['phases'] += 1; I = P = 0
            for a, b in zip(ph, ph[1:]):
                if cmp_chain(a['chain'], b['chain']) == '=': I += 1
                else: P += 1
            if I > (n + 1) * (P + 1) * (1 + n * n) + 1: tot['I_bound_viol'] += 1
            loc['I'] += I; loc['P'] += P
            last = {}
            for s in ph:
                for c in s['calls']:
                    if 'vec' not in c: continue
                    key = (c['R'], c['V'], c['res'])
                    if key in last:
                        loc['dom_pairs'] += 1
                        (t0, x0), (t1, x1) = last[key], c['vec']
                        if t0 != t1 or any(not (u <= w) for u, w in zip(x0, x1)): loc['dom_viol'] += 1
                    last[key] = c['vec']
        for k in loc: tot[k] += loc[k]
        print(os.path.basename(f), 'n=%d' % n, loc)
    print('TOTAL', tot)
if __name__ == '__main__': main(sys.argv[1], sys.argv[2], sys.argv[3:])
