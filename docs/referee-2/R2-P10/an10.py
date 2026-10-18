#!/usr/bin/env python3
"""REFEREE-2 P10 analyser (own code). Per (context, phase), steps sigma = (r, tau) with tau any p-vertex of R (V_1) and
r < max rounds: entries/exits of each w in P_i(sigma+) (prefix BEFORE tau, virtual rounds per G9-b2); events (relevant
steals); checks ENTRY-CHARGE's three steps, |F_sigma(i)| <= |region| - 1 < |R|, N*_R <= N_ent, and X(sigma, w) maxima."""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import an7, an8
from an9 import round_of

def tops_of(rd):
    m = {}
    for top, Z in rd['regs']:
        for w in Z: m[w] = top
    return m

def main(path):
    pr, ow, outs, tangles, calls = an8.parse8(path)
    c = collections.Counter(); exits_hist = collections.Counter()
    # (2) fan-out bound at every region step of every call
    for C in calls:
        for rd in C['rounds']:
            for (top, Z), Fs in zip(rd['regs'], rd['fired']):
                c['steps'] += 1
                if len(Fs) > len(Z) - 1: c['FANOUT_FAIL |F|>|region|-1'] += 1
                if len(Fs) >= len(C['R']): c['FANOUT_FAIL |F|>=|R|'] += 1
                c['max |F_sigma|'] = max(c['max |F_sigma|'], len(Fs))
    groups = collections.defaultdict(list)
    for i, C in enumerate(calls):
        if C['rounds']: groups[(C['G'], C['pl'], C['R'])].append(i)
    for key, idx in groups.items():
        R = key[2]; V1 = sorted(calls[idx[0]]['rounds'][0]['V'])
        nr = max(len(calls[i]['rounds']) for i in idx)
        TO = [[tops_of(round_of(calls[i], r)) for r in range(nr)] for i in idx]
        X = collections.Counter(); Nent = 0; Xtot = 0; ent_by = collections.Counter()
        for p in range(len(idx) - 1):
            for r in range(nr):
                a, b = TO[p][r], TO[p + 1][r]
                for tau in V1:
                    for w in R:
                        ina = a.get(w, -1) > tau; inb = b.get(w, -1) > tau
                        if ina and not inb: X[(r, tau, w)] += 1; Xtot += 1
                        if inb and not ina: Nent += 1; ent_by[(r, tau, w)] += 1
        for k in set(ent_by) | set(X):
            if ent_by[k] > X[k] + 1: c['ALTERNATION_FAIL'] += 1
        for k, v in X.items(): exits_hist[v] += 1
        # events and steps (1)-(2)
        nev = 0; nstar = 0
        for p, (a, b) in enumerate(zip(idx, idx[1:])):
            A, B = calls[a], calls[b]; pair_has = False
            for ri, rd in enumerate(A['rounds']):
                rb = round_of(B, ri); Pa = frozenset()
                for (top, Z), Fs in zip(rd['regs'], rd['fired']):
                    Pb = an7.prefix(rb['regs'], top)
                    for t in Fs:
                        tv = tangles[t][1]
                        if (tv & Pb) and not tv <= Pb:
                            nev += 1; pair_has = True
                            if tv & Pa: c['STEP1_FAIL t∩P_i(σ⁺)≠∅'] += 1
                            if not ((tv & Pb) - Pa): c['STEP1_FAIL no entering w'] += 1
                    Pa = Pa | Z
            if pair_has: nstar += 1
        n = len(R); steps = nr * len(V1)
        if nev > n * Nent: c['ENTRY-CHARGE FAIL'] += 1
        if nstar > Nent: c['N*>N_ent FAIL'] += 1
        if Nent > Xtot + steps * n: c['N_ent bound FAIL'] += 1
        if Xtot > nstar * n * steps: c['C3 FAIL'] += 1
        if Xtot and not nstar: c['C3 FAIL (exits without relevant steal)'] += 1
        c['ctx-phases'] += 1
        if nev: c['ctx-phases with events'] += 1
        c['sum events (Σk_q)'] += nev; c['sum N*'] += nstar; c['sum N_ent'] += Nent; c['sum X'] += Xtot
        c['max X_R/|R| x100'] = max(c['max X_R/|R| x100'], 100 * Xtot // n)
        c['max X(σ,w)'] = max([c['max X(σ,w)']] + list(X.values()))
    for v, k in exits_hist.items(): c[f'(σ,w) with exactly {v} exits'] += k
    return c

if __name__ == '__main__':
    tot = collections.Counter()
    for path in sys.argv[1:]:
        cc = main(path)
        for k, v in cc.items(): tot[k] = max(tot[k], v) if k.startswith('max') else tot[k] + v
    for k in sorted(tot): print(f'{k}: {tot[k]}')
