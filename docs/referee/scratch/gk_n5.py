#!/usr/bin/env python3
"""REFEREE successor 35: N5 (SPEC, from S3) on Gamma3(G_k) with this lane's own engine rl_engine.py, my Gamma3 builder, my IDEAL
simulator and my Zielonka. Counters as in gk_reach.py. usage: gk_n5.py kmin kmax [revE]   (revE: the firing control)"""
import sys
import rl_engine as eng
import gk_ideal as ideal
import gk_gamma3 as g3
import gk_build as B
import gk_reach as R

ctl = len(sys.argv) > 3 and sys.argv[3] == 'revE'          # firing control: e-indices in reversed gate order
for k in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
    G = B.genome(k)
    r = R.replay(G, eng, ideal, g3, control=ctl)
    print('G_%d%s: N %d M %d L %d n3 %d | N5 from S3: iterations %d (2^k+1 = %d) fallback transitions %s (2^k-1 = %d) | counters %s | Even wins %d of %d | %.1fs' % (
        k, ' [control revE]' if ctl else '', r['N'], r['M'], r['L'], r['n3'], r['iters'], 2 ** k + 1, r['fallbacks'], 2 ** k - 1, r['counters'], r['even_won'], r['n3'], r['secs']))
    sys.stdout.flush()
