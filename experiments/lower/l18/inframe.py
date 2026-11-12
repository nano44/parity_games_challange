#!/usr/bin/env python3
"""L-LOWER 18: is GENOME inside a pgad5/6 frame on BASE? Checks: wiring differs only on XS movers' options; options outside XS keep
BASE's relative rank order; FIXC movers keep signs, their level's gate bits and starts; core gates (levels < H) unchanged. Reports what
else differs (signs / helper gates / helper starts are free in the frame). Usage: inframe.py BASE GENOME XS FIXC [H=8]"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(here, '..', 'l12'))
import enc32_lcomp as e
B, G = e.rdgen(sys.argv[1]), e.rdgen(sys.argv[2]); XS = set(int(v) for v in sys.argv[3].split(',')); FX = set(int(v) for v in sys.argv[4].split(','))
H = int(sys.argv[5]) if len(sys.argv) > 5 else 8; N = 2 * B['d']; ok = True
wd = [m for m in range(2 * N) if B['xt'][m] != G['xt'][m]]
bad_w = [m for m in wd if m // 2 not in XS]; ok &= not bad_w
fixed = [m for m in range(2 * N) if m // 2 not in XS]
ob = sorted(fixed, key=lambda m: B['br'][m]); og = sorted(fixed, key=lambda m: G['br'][m]); ok &= ob == og
fs = [m for m in range(2 * N) if m // 2 in FX and B['bp'][m] != G['bp'][m]]; ok &= not fs
fl = {x // 2 for x in FX}; fg = [i for l in fl for i in range(4 * l, 4 * l + 4) if (B['gate'][i] > B['gate'][i ^ 2]) != (G['gate'][i] > G['gate'][i ^ 2])]; ok &= not fg
fst = [x for x in FX if B['start'][x] != G['start'][x]]; ok &= not fst
cg = [i for i in range(4 * H) if B['gate'][i] != G['gate'][i]]; ok &= not cg
print('INFRAME', os.path.basename(sys.argv[2]), 'vs', os.path.basename(sys.argv[1]), 'OK' if ok else 'VIOLATION', '| wiring diffs (options)', wd,
      'outside XS', bad_w, '| fixed-option order kept', ob == og, '| FIXC sign/gate/start diffs', fs, fg, fst, '| core gate diffs', cg,
      '| free diffs: signs', sum(B['bp'][m] != G['bp'][m] for m in range(2 * N)), 'helper starts', sum(B['start'][x] != G['start'][x] for x in range(2 * H, N)))
