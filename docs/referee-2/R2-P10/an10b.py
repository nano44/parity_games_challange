#!/usr/bin/env python3
"""Variant: count exits/entries only at tau in V_r of the EARLIER visit of the pair (the narrow reading of 'tau in V_r'),
and test whether entries <= exits + 1 per (sigma, w) and N_ent <= X_R + steps*|R| survive under it; also the entries used
by step 1 (events) against narrow exits."""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import an8
from an9 import round_of
from an10 import tops_of
for path in sys.argv[1:]:
    pr, ow, outs, tangles, calls = an8.parse8(path)
    groups = collections.defaultdict(list)
    for i, C in enumerate(calls):
        if C['rounds']: groups[(C['G'], C['pl'], C['R'])].append(i)
    c = collections.Counter()
    for key, idx in groups.items():
        R = key[2]; V1 = sorted(calls[idx[0]]['rounds'][0]['V']); nr = max(len(calls[i]['rounds']) for i in idx)
        TO = [[tops_of(round_of(calls[i], r)) for r in range(nr)] for i in idx]
        Vr = [[round_of(calls[i], r)['V'] for r in range(nr)] for i in idx]
        Xn = collections.Counter(); En = collections.Counter(); Xw = collections.Counter()
        for p in range(len(idx) - 1):
            for r in range(nr):
                a, b = TO[p][r], TO[p + 1][r]
                for tau in V1:
                    for w in R:
                        ina = a.get(w, -1) > tau; inb = b.get(w, -1) > tau
                        if ina and not inb:
                            Xw[(r, tau, w)] += 1
                            if tau in Vr[p][r]: Xn[(r, tau, w)] += 1
                        if inb and not ina and tau in Vr[p][r]: En[(r, tau, w)] += 1
        for k in En:
            if En[k] > Xn[k] + 1: c['narrow: entries > narrow exits + 1'] += 1
        c['narrow exits'] += sum(Xn.values()); c['wide exits'] += sum(Xw.values())
        c['max narrow X(σ,w)'] = max([c['max narrow X(σ,w)']] + list(Xn.values()))
    print(path.split('/')[-1], dict(c))
