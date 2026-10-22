#!/usr/bin/env python3
"""REFEREE-2 P11 analyser (own code): Lemma CHANGE-NEW per consecutive visit pair of a best_vertices context (key: G, player,
R; the call does not read depth), D_R <= #fired+(R), N*_R <= D_R. A visit's set-level computation = its rounds (V, region
tops and sets, W_t). Firings: every 'F t' line between the call's B and E lines (regions and threshold loop)."""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import an7, an8
from an9 import round_of

def main(path):
    pr, ow, outs, tangles, calls = an8.parse8(path)
    fired_all = []; ntv = []; ci = -1; nt = 0
    for line in open(path):
        k = line[0]
        if k == 'T': nt += 1
        elif k == 'B': ci += 1; fired_all.append(set()); ntv.append(nt)
        elif k == 'F' and ci >= 0 and len(fired_all) == ci + 1: fired_all[ci].add(int(line.split()[1]))
        elif k == 'E': pass
    # F lines after E (outside best_vertices) must not be attributed: re-scan with an in-call flag
    fired_all = []; inc = False; ci = -1
    for line in open(path):
        k = line[0]
        if k == 'B': ci += 1; fired_all.append(set()); inc = True
        elif k == 'E': inc = False
        elif k == 'F' and inc: fired_all[ci].add(int(line.split()[1]))
    def sig(C):
        return tuple((rd['V'], tuple(rd['regs']), tuple(sorted(rd['W'].items()))) for rd in C['rounds'])
    groups = collections.defaultdict(list)
    for i, C in enumerate(calls): groups[(C['G'], C['pl'], C['R'])].append(i)
    c = collections.Counter()
    for key, idx in groups.items():
        D = 0; nstar = 0; fplus = set()
        for i in idx: fplus |= fired_all[i]
        for a, b in zip(idx, idx[1:]):
            A, B = calls[a], calls[b]
            if sig(A) == sig(B):
                c['pairs identical'] += 1
                if A['T'] != B['T']: c['  identical with new tangles'] += 1
                continue
            D += 1; c['pairs differing'] += 1
            born = {t for t in fired_all[b] if ntv[a] <= t < ntv[b]}
            if born: c['CHANGE-NEW holds'] += 1
            else: c['CHANGE-NEW FAIL'] += 1; print('FAIL', path, a, b)
            if A['T'] == B['T']: c['DIFFER WITH SAME T (determinism FAIL)'] += 1
        for a, b in zip(idx, idx[1:]):   # relevant-steal pairs
            A, B = calls[a], calls[b]; rel = False
            for ri, rd in enumerate(A['rounds']):
                rb = round_of(B, ri)
                for (top, Z), Fs in zip(rd['regs'], rd['fired']):
                    Pb = an7.prefix(rb['regs'], top)
                    if any((tangles[t][1] & Pb) and not tangles[t][1] <= Pb for t in Fs): rel = True
            nstar += rel
        c['contexts'] += 1
        if D > len(fplus): c['D_R > #fired+ FAIL'] += 1
        if nstar > D: c['N* > D FAIL'] += 1
        c['max D_R'] = max(c['max D_R'], D)
        if fplus: c['max D_R/#fired+ x100'] = max(c['max D_R/#fired+ x100'], 100 * D // len(fplus))
        c['max #fired+/|R| x100'] = max(c['max #fired+/|R| x100'], 100 * len(fplus) // max(1, len(key[2])))
        if len(key[2]) == len(key[0]): c['max root D'] = max(c['max root D'], D); c['max root #fired+'] = max(c['max root #fired+'], len(fplus))
    return c

if __name__ == '__main__':
    tot = collections.Counter()
    for p in sys.argv[1:]:
        for k, v in main(p).items(): tot[k] = max(tot[k], v) if k.startswith('max') else tot[k] + v
    for k in sorted(tot): print(f'{k}: {tot[k]}')
