#!/usr/bin/env python3
"""REFEREE-2 P8 analyser (own code): EXACT* (closure over the FIRED tangles F_tau), (NS*) relevant steals, PREFIX-MONO-X*
predictions, and the data statements (STEAL-ONCE), (FIRED-R) of GAP-A-M 22s-22u. Log: dtl_probe8.patch (R2P7_LOG)."""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import an7

def parse8(path):
    pr, ow, outs, tangles, calls = an7.parse(path)
    # second pass: attach fired sets to region steps, in log order
    ci = -1; pend = []; rd = None; ri = -1
    for line in open(path):
        k = line[0]
        if k == 'B': ci += 1; pend = []; ri = -1
        elif k == 'V': ri += 1; pend = []; rd = calls[ci]['rounds'][ri]; rd['fired'] = []
        elif k == 'F': pend.append(int(line.split()[1]))
        elif k == 'P': rd['fired'].append(frozenset(pend)); pend = []
        elif k == 'W': pend = []
    return pr, ow, outs, tangles, calls

def main(path):
    pr, ow, outs, tangles, calls = parse8(path)
    n = len(pr); cl, attracts = an7.make(pr, ow, outs, tangles)
    c = collections.Counter()
    for C in calls:
        R, T, p = C['R'], C['T'], C['pl']
        for rd in C['rounds']:
            P = frozenset()
            for (top, Z), Fs in zip(rd['regs'], rd['fired']):
                E = an7.excl(T, P, tangles)
                c['steps'] += 1
                if not Fs <= T - E: c['F_NOT_IN_T-E'] += 1
                if any(tangles[t][1] & P for t in Fs): c['F_MEETS_PREFIX'] += 1
                if cl(P | {top}, R, pr[top], Fs, p) == P | Z: c['EXACTstar_ok'] += 1
                else: c['EXACTstar_FAIL'] += 1; print('EXACTstar_FAIL', path, C['search'], top)
                if Fs: c['steps_with_firing'] += 1
                P = P | Z
            rd['U'] = P
        V0 = C['rounds'][0]['V'] if C['rounds'] else frozenset()
        RV = {}
        for v in V0:
            RV[v] = an7.INF
            for i, rd in enumerate(C['rounds']):
                nxt = C['rounds'][i+1]['V'] if i + 1 < len(C['rounds']) else (frozenset() if C['rv'] == -1 else rd['V'])
                if v in rd['V'] and v not in nxt: RV[v] = i + 1
        C['RV'] = RV
        C['Psi'] = [(rd['U'], tuple(sorted(rd['W'].items()))) for rd in C['rounds']]
        C['Phi'] = sum((n - top) * len(Z) for rd in C['rounds'] for top, Z in rd['regs'])
    groups = collections.defaultdict(list)
    for i, C in enumerate(calls):
        if C['rounds']: groups[(C['G'], C['pl'], C['R'])].append(i)
    def cmp(a, b):
        A, B = calls[a], calls[b]
        if A['RV'] == B['RV'] and A['Psi'] == B['Psi'] and A['Phi'] == B['Phi']: return 'equal'
        if all(A['RV'][v] <= B['RV'][v] for v in A['RV']) and A['RV'] != B['RV']: return 'rise'
        if A['RV'] == B['RV'] and len(A['Psi']) == len(B['Psi']) and all(ua <= ub and all(x[1] <= y[1] for x, y in zip(Wa, Wb)) for (ua, Wa), (ub, Wb) in zip(A['Psi'], B['Psi'])):
            if A['Psi'] != B['Psi'] or B['Phi'] < A['Phi']: return 'rise'
        return 'NONRISE'
    def steals(a, b):
        """(plain, relevant) sets of (round, top, tangle) newly stolen from a to b."""
        A, B = calls[a], calls[b]; plain, rel = set(), set()
        for ri, rd in enumerate(A['rounds']):
            rb = B['rounds'][min(ri, len(B['rounds']) - 1)]; P = frozenset()
            for (top, Z), Fs in zip(rd['regs'], rd['fired']):
                E = an7.excl(A['T'], P, tangles); Eb = an7.excl(B['T'], an7.prefix(rb['regs'], top), tangles)
                for t in (Eb & A['T']) - E: plain.add((ri, top, t))
                for t in Fs & Eb: rel.add((ri, top, t))
                P = P | Z
        return plain, rel
    def predictions(a, b):
        A, B = calls[a], calls[b]
        for ri, rd in enumerate(A['rounds']):
            rb = B['rounds'][min(ri, len(B['rounds']) - 1)]
            if not rd['V'] <= rb['V']: return 'V'
            for tau in sorted(rd['V'] | rb['V']):
                if not an7.prefix(rd['regs'], tau - 1) <= an7.prefix(rb['regs'], tau - 1): return 'P'
            if not rd['U'] <= rb['U']: return 'U'
            if rd['W'] and rb['W'] and not all(rd['W'][t] <= rb['W'][t] for t in rd['W']): return 'W'
        return None
    stats = []
    for key, idx in groups.items():
        once = collections.Counter(); fired = set(); nrel = 0
        for i in idx:
            for rd in calls[i]['rounds']:
                for Fs in rd['fired']: fired |= Fs
        for mode, pairs in (('consec', list(zip(idx, idx[1:]))), ('allpairs', [(x, y) for i, x in enumerate(idx) for y in idx[i+1:]])):
            for a, b in pairs:
                plain, rel = steals(a, b); k = cmp(a, b)
                c[f'{mode}: {"relsteal" if rel else ("plainsteal-only" if plain else "no-steal")} {"NONRISE" if k == "NONRISE" else k}'] += 1
                if rel and not plain <= plain | rel: pass
                if not rel <= plain: c[f'{mode}: REL_NOT_PLAIN'] += 1
                if not rel:
                    bad = predictions(a, b)
                    if bad: c[f'{mode}: PRED_FAIL_{bad}'] += 1; print('PRED_FAIL', path, mode, bad)
                if mode == 'consec':
                    for x in plain: once[x] += 1
                    if rel: nrel += 1
        rounds = max(len(calls[i]['rounds']) for i in idx)
        stats.append((len(key[2]), len(fired), max(once.values()) if once else 0, nrel, rounds, len(idx)))
        if once: c['ctx-phases with new steals'] += 1
        if once and max(once.values()) > 1: c['STEAL-ONCE violations (ctx-phases)'] += 1
        if nrel > rounds * n * len(fired): c['CHAIN_FAIL'] += 1
    c['max fired per ctx-phase'] = max([s[1] for s in stats] + [0])
    c['max fired/|R| x1000'] = max([1000 * s[1] // s[0] for s in stats if s[0]] + [0])
    c['max relsteal consec pairs per ctx-phase'] = max([s[3] for s in stats] + [0])
    return c

if __name__ == '__main__':
    tot = collections.Counter()
    for path in sys.argv[1:]:
        c = main(path)
        for k, v in c.items():
            if k.startswith('max'): tot[k] = max(tot[k], v)
            else: tot[k] += v
    for k in sorted(tot): print(f'{k}: {tot[k]}')
