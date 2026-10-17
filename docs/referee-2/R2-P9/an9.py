#!/usr/bin/env python3
"""REFEREE-2 P9 analyser (own code): relevant-steal EVENTS per quadruple q = (round, top, fired tangle) at each context and
phase; re-steals (k_q >= 2); Lemma CHARGE's cause (an event at a pair strictly between, at a strictly earlier step:
rounds ascending, tops descending); the proof's intermediate claims with P(tau+) (prefix before tau); depth and E_d."""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import an7, an8

def round_of(C, r):
    """Round r of call C under the alignment convention: a call that stopped with 'no change' repeats its last round;
    one that stopped with all removed (-1) has empty later rounds."""
    if r < len(C['rounds']): return C['rounds'][r]
    if C['rv'] == -1: return dict(V=frozenset(), regs=[], fired=[], W={})
    return C['rounds'][-1]

def earlier(s1, s2):  # step order: rounds ascending, tops descending
    return s1[0] < s2[0] or (s1[0] == s2[0] and s1[1] > s2[1])

def main(path, verbose=False):
    pr, ow, outs, tangles, calls = an8.parse8(path)
    groups = collections.defaultdict(list)
    for i, C in enumerate(calls):
        if C['rounds']: groups[(C['G'], C['pl'], C['R'])].append(i)
    c = collections.Counter(); out = []
    for key, idx in groups.items():
        R = key[2]
        ev = []  # per consecutive pair: set of (r, top, t)
        for a, b in zip(idx, idx[1:]):
            A, B = calls[a], calls[b]; s = set()
            for ri, rd in enumerate(A['rounds']):
                rb = round_of(B, ri)
                for (top, Z), Fs in zip(rd['regs'], rd['fired']):
                    Eb = an7.excl(B['T'], an7.prefix(rb['regs'], top), tangles)
                    for t in Fs & Eb: s.add((ri, top, t))
            ev.append(s)
        byq = collections.defaultdict(list)
        for i, s in enumerate(ev):
            for q in s: byq[q].append(i)
        if not byq: continue
        c['ctx-phases with events'] += 1
        Q = len({(r, top, t) for i in idx for r, rd in enumerate(calls[i]['rounds']) for (top, Z), Fs in zip(rd['regs'], rd['fired']) for t in Fs})
        depth = {}
        for i, s in enumerate(ev):          # pairs in order; causes lie at earlier pairs, so depth is known
            for q in sorted(s):
                prev = [j for j in byq[q] if j < i]
                if not prev: depth[(i, q)] = 0; c['events depth0 (first)'] += 1; continue
                j = prev[-1]; c['RE-STEALS'] += 1
                causes = [(m, q2) for m in range(j + 1, i) for q2 in ev[m] if earlier(q2[:2], q[:2])]
                # proof's intermediate claims, with P(tau+)
                r, top, t = q; tv = tangles[t][1]
                Pj1 = an7.prefix(round_of(calls[idx[j + 1]], r)['regs'], top)
                Pi = an7.prefix(round_of(calls[idx[i]], r)['regs'], top)
                W = (tv & Pj1) - Pi
                if not W: c['CLAIM_FAIL w in t∩P_{j+1}(τ⁺)\\P_i(τ⁺)'] += 1
                if tv & Pi: c['CLAIM_FAIL t∩P_i(τ⁺)≠∅'] += 1
                Pfull_i = an7.prefix(round_of(calls[idx[i]], r)['regs'], top - 1)
                if not (tv & Pfull_i): c['note: t∩P_i(τ)=∅ (proof as written)'] += 1
                if causes:
                    depth[(i, q)] = 1 + min(depth[(m, q2)] for m, q2 in causes)
                    c['re-steals with a cause'] += 1
                else:
                    depth[(i, q)] = None; c['RE-STEAL WITHOUT CAUSE'] += 1
                out.append(dict(R=len(R), pair=i, q=q, prev=j, causes=causes[:8], ncauses=len(causes), depth=depth[(i, q)], W=sorted(W)))
        k = max(len(v) for v in byq.values())
        c['max k_q'] = max(c['max k_q'], k)
        E = collections.Counter(d for d in depth.values() if d is not None)
        for d, e in E.items():
            if d >= 1 and e > Q * E[d - 1]: c['E_d > Q*E_{d-1}'] += 1
        c['max depth'] = max([c['max depth']] + [d for d in depth.values() if d is not None])
        c['max Q'] = max(c['max Q'], Q)
    return c, out

if __name__ == '__main__':
    verbose = '-v' in sys.argv
    tot = collections.Counter()
    for path in [a for a in sys.argv[1:] if a != '-v']:
        c, out = main(path)
        for k, v in c.items():
            tot[k] = max(tot[k], v) if k.startswith('max') else tot[k] + v
        if verbose:
            for o in out: print(path.split('/')[-1], o)
    for k in sorted(tot): print(f'{k}: {tot[k]}')
