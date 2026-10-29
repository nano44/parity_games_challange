#!/usr/bin/env python3
"""L-RED successor 26: tau(e_i) history on (variants of) Friedmann H_n: per gate e_i the compressed sequence of d (inside) / h (exit)
and the number of h -> d reopenings. Usage: gatestate.py GAME.pg START|S3"""
import sys, re; sys.path.insert(0,'experiments/n5-second'); import n5b
p, st = sys.argv[1], sys.argv[2]
g=n5b.pg.read(p); lab={int(m.group(1)):m.group(2) for l in open(p) for m in [re.match(r'\s*(\d+)\s.*"(.*)"',l)] if m}
N=n5b.N5(g); N.mode='spec'; s0,t0=(None,None) if st=='S3' else n5b.read_start(st,g); tr=[]; fb=[]; N.run(s0,t0,trace=tr,fbtrace=fb)
E=[v for v in range(g.n) if lab[v].startswith('e')]
seq={lab[v]:''.join('h' if lab[T[v]].startswith('h') else 'd' for _,T in tr) for v in E}
for k,v in seq.items():
    comp=re.sub(r'(.)\1*',r'\1',v); print(k, comp, 'reopen(h->d)', comp.count('hd'))
