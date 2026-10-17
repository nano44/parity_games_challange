#!/usr/bin/env python3
"""REFEREE-2 P7 analyser (own code). Reads the R2P7_LOG of the instrumented pinned dtl.cpp and checks
EXACT, the threshold-loop identity, the survivor formula, PREFIX-MONO-X predictions, and new steals at Pi_R non-rises."""
import sys, collections
INF = 10**9
def parse(path):
    pr, ow, outs = {}, {}, {}
    calls = []; tangles = {}; G = set(); player = None; search = -1; cur = None
    for line in open(path):
        a = line.split(':'); h = a[0].split()
        k = h[0]
        if k == 'N':
            v = int(h[1]); pr[v] = int(h[2]); ow[v] = int(h[3]); outs[v] = [int(x) for x in a[1].split()]
        elif k == 'S':
            player = int(h[1]); G = frozenset(int(x) for x in a[1].split()); search += 1
        elif k == 'T':
            tangles[int(h[1])] = (int(h[2]), frozenset(int(x) for x in a[1].split()), [int(x) for x in a[2].split()])
        elif k == 'B':
            T = frozenset(t for t, (p, vs, _) in tangles.items() if p % 2 == player and vs <= G)
            cur = dict(pl=int(h[1]), R=frozenset(int(x) for x in a[1].split()), T=T, G=G, search=search, rounds=[], rv=None)
            calls.append(cur)
        elif k == 'V':
            cur['rounds'].append(dict(V=frozenset(int(x) for x in a[1].split()), regs=[], W={}))
        elif k == 'P':
            cur['rounds'][-1]['regs'].append((int(h[1]), frozenset(int(x) for x in a[1].split())))
        elif k == 'W':
            cur['rounds'][-1]['W'][int(h[1])] = frozenset(int(x) for x in a[1].split())
        elif k == 'E':
            cur['rv'] = int(h[1])
    return pr, ow, outs, tangles, calls

def make(pr, ow, outs, tangles):
    def cl(base, Rs, h, tl, p):
        Z = set(base); ch = True
        while ch:
            ch = False
            for u in Rs - Z:
                if pr[u] > h: continue
                if ow[u] == p: ok = any(w in Z for w in outs[u])
                else: ok = any(w in Z for w in outs[u]) and all((w in Z) or (w not in Rs) for w in outs[u])
                if ok: Z.add(u); ch = True
            for t in tl:
                vs = tangles[t][1]; new = vs - Z
                if not new or not new <= Rs or any(pr[w] > h for w in new): continue
                esc = tangles[t][2]
                if any((e not in Z) and (e in Rs) for e in esc) or not any(e in Z for e in esc): continue
                Z |= new; ch = True
        return frozenset(Z)
    def attracts(p, v, Z, R):
        if ow[v] == p: return any(w in Z for w in outs[v])
        return any(w in Z for w in outs[v]) and not any((w in R) and (w not in Z) for w in outs[v])
    return cl, attracts

def prefix(regs, tau):  # P(tau+): union of regions of processed tops of index > tau
    s = set()
    for top, Z in regs:
        if top > tau: s |= Z
    return frozenset(s)

def excl(T, P, tangles):
    return frozenset(t for t in T if (tangles[t][1] & P) and not tangles[t][1] <= P)

def main(path, tag):
    pr, ow, outs, tangles, calls = parse(path)
    n = len(pr); cl, attracts = make(pr, ow, outs, tangles)
    c = collections.Counter()
    for C in calls:
        R, T, p = C['R'], C['T'], C['pl']
        for ri, rd in enumerate(C['rounds']):
            P = frozenset()
            for top, Z in rd['regs']:
                c['steps'] += 1
                assert top in rd['V'] and top not in P
                E = excl(T, P, tangles)
                ex = cl(P | {top}, R, pr[top], T - E, p)
                if ex == P | Z: c['EXACT_ok'] += 1
                else: c['EXACT_FAIL'] += 1; print('EXACT_FAIL', tag, C['search'], ri, top)
                full = cl(P | {top}, R, pr[top], T, p)
                if full != P | Z: c['step_deficit(T unexcluded)'] += 1
                if E: c['steps_with_E_nonempty'] += 1
                P = P | Z
            # V tops not processed are inside the prefix
            assert all(v in P for v in rd['V']), 'top not covered'
            U = P; rd['U'] = U
            if rd['W']:
                for t, W in rd['W'].items():
                    if W == cl(U, R, t, T, p): c['W_ok'] += 1
                    else: c['W_FAIL'] += 1; print('W_FAIL', tag, C['search'], ri, t)
                surv = frozenset(v for v in rd['V'] if attracts(p, v, U, R) or any(attracts(p, v, rd['W'][t], R) for t in rd['W'] if t < pr[v]))
                nxt = C['rounds'][ri+1]['V'] if ri + 1 < len(C['rounds']) else None
                if nxt is not None:
                    c['surv_ok' if surv == nxt else 'SURV_FAIL'] += 1
        # Pi
        V0 = C['rounds'][0]['V'] if C['rounds'] else frozenset()
        RV = {}
        for v in V0:
            RV[v] = INF
            for ri, rd in enumerate(C['rounds']):
                nxt = C['rounds'][ri+1]['V'] if ri + 1 < len(C['rounds']) else (frozenset() if C['rv'] == -1 else rd['V'])
                if v in rd['V'] and v not in nxt: RV[v] = ri + 1
        C['RV'] = RV
        C['Psi'] = [(rd['U'], tuple(sorted(rd['W'].items()))) for rd in C['rounds']]
        C['Phi'] = sum((n - top) * len(Z) for rd in C['rounds'] for top, Z in rd['regs'])
    # visits
    groups = collections.defaultdict(list)
    for i, C in enumerate(calls):
        if C['rounds']: groups[(C['G'], C['pl'], C['R'])].append(i)
    def cmp(a, b):
        A, B = calls[a], calls[b]
        if A['RV'] == B['RV'] and A['Psi'] == B['Psi'] and A['Phi'] == B['Phi']: return 'equal'
        le = all(A['RV'][v] <= B['RV'][v] for v in A['RV'])
        if le and A['RV'] != B['RV']: return 'rise_RV'
        if A['RV'] == B['RV']:
            if len(A['Psi']) == len(B['Psi']) and all(ua <= ub and all(wa[1] <= wb[1] for wa, wb in zip(Wa, Wb)) for (ua, Wa), (ub, Wb) in zip(A['Psi'], B['Psi'])):
                if A['Psi'] != B['Psi']: return 'rise_Psi'
                if B['Phi'] < A['Phi']: return 'rise_Phi'
        return 'NONRISE'
    def newsteal(a, b):
        A, B = calls[a], calls[b]
        for ri, rd in enumerate(A['rounds']):
            rb = B['rounds'][min(ri, len(B['rounds']) - 1)]
            P = frozenset()
            for top, Z in rd['regs']:
                E = excl(A['T'], P, tangles)
                Pb = prefix(rb['regs'], top)
                Eb = excl(B['T'], Pb, tangles)
                if not (Eb & A['T']) <= E: return True
                P = P | Z
        return False
    def predictions(a, b):
        A, B = calls[a], calls[b]
        for ri, rd in enumerate(A['rounds']):
            rb = B['rounds'][min(ri, len(B['rounds']) - 1)]
            if not rd['V'] <= rb['V']: return 'V'
            for tau in sorted(rd['V'] | rb['V']) + [-1]:
                if not prefix(rd['regs'], tau - 1 if tau >= 0 else -1) <= prefix(rb['regs'], tau - 1 if tau >= 0 else -1): return 'P'
            if not rd['U'] <= rb['U']: return 'U'
            if rd['W'] and rb['W'] and not all(rd['W'][t] <= rb['W'][t] for t in rd['W']): return 'W'
        return None
    for key, idx in groups.items():
        for mode, pairs in (('consec', list(zip(idx, idx[1:]))), ('allpairs', [(x, y) for i, x in enumerate(idx) for y in idx[i+1:]])):
            for a, b in pairs:
                assert calls[a]['T'] <= calls[b]['T']
                ns = newsteal(a, b); k = cmp(a, b)
                c[f'{mode}: {"newsteal" if ns else "no-steal"} {"NONRISE" if k == "NONRISE" else ("equal" if k == "equal" else "rise")}'] += 1
                if not ns:
                    bad = predictions(a, b)
                    if bad: c[f'{mode}: PRED_FAIL_{bad}'] += 1; print('PRED_FAIL', tag, mode, bad, calls[a]['search'], calls[b]['search'])
    return c, calls, pr, groups

if __name__ == '__main__':
    tot = collections.Counter()
    for path in sys.argv[1:]:
        c, *_ = main(path, path); tot.update(c)
    for k in sorted(tot): print(f'{k}: {tot[k]}')
