# REFEREE-2 succ. 30: shape of P-IDEAL-DBL L-1 and my required replacements W-2a..d, W-3 (each old string once in L-1)
import sys, hashlib
L = open(sys.argv[1], encoding='utf-8').read()
def shape(L):
    d = m = 0
    for c in L: d += (c == '(') - (c == ')'); m = min(m, d)
    return 'sha1 %s %d B lines %d ( %d ) %d | %d mindepth %d' % (hashlib.sha1(L.encode()).hexdigest(), len(L.encode()), L.count('\n'), L.count('('), L.count(')'), L.count('|'), m)
print('L-1', shape(L))
W = [("(L-RED's dense_d5_l3_H10, start 1100110110: 10 moves against 4)",
      "(experiments/si/box76/inst/dense_d5_l3_H10.json, a byte copy of L-RED's, 𝓛^R_5, start 1100110110: mover 6 of level 3, a Ξ-target, moves 10 times, every mover of levels 0-2 and every strict Ξ-descendant of 6 at most 4 times)"),
     ("(L-LOWER's REC_d10_tower_mu30: F(0..3) = 2, 6, 14, 30)",
      "(experiments/si/box76/inst/lower/REC_d10_tower_mu30.json, a byte copy of L-LOWER's, 𝓛^R_10, its stored start 00111111010010111010: F(0..3) = 2, 6, 14, 30)"),
     ("(passfreeze77_d5: F = 2, 2, 2, 6, 6)",
      "(experiments/si/box76/inst/passfreeze77_d5.json, 𝓛^R_5, its stored start 1101111101: F = 2, 2, 2, 6, 6, the top pair never moving)"),
     ("(REC_d10_tower_mu30: 11 → 3; KILL_M2D_d6_mu13: 5 → 3)",
      "(at l = 1 in the static Ξ-graph: REC_d10_tower_mu30, 1 → 11 → 3; experiments/si/box76/inst/lower/KILL_M2D_d6_mu13.json, 2 → 5 → 3)"),
     ("(DATA: each statement 0 violations on its own unit over the 63,223 runs of the frozen P-IDEAL-MOVES corpus and the 9 L-LOWER genomes, with controls; FUEL-NEED and FUEL (i), which use L-LOWER's unrefereed FEEDBACK (b), are not stated; no statement bounds T polynomially)",
      "(DATA, experiments/si/box79/dblcheck.py, counts CORPUS / LOWER, CORPUS the 63,223 runs of the 208 𝓛^R_d genomes of the frozen P-IDEAL-MOVES corpus (every start for d ≤ 5, the stored start otherwise) and LOWER the 9 L-LOWER kill genomes from their stored starts: WINDOW-ONCE 0 violations on 577,908 / 1,736 (run, level, window, member); DBL-EQ (a) 0 on 225,647 / 72 (run, level ≥ 1), (b) 0 on 11,052 / 176 (run, doubling level, window, member), (c) 0 on the 4,534 / 12 doubling (run, level); PASS-FREEZE 0 on 23,317 / 0 (run, level) with the pair above never moving and split at the start; HIT 0 on 1,298,948 / 5,216 (run, mover, step); FUEL-EXACT 0 on 288,870 / 81 (run, level); ALT-MIN (a)-(d) 0 on 577,740 / 162 (run, mover); TOWER-NEED 0 on 9,068 / 24 (run, doubling level, member); MP-LIN, the sufficient condition of PASS-FREEZE and the DEAD-REENTRY instances (static): no separate DATA; the other three DEAD instances re-run by experiments/si/box79/dead79.py; FUEL-NEED and FUEL (i), which use L-LOWER's unrefereed FEEDBACK (b), are not stated; no statement bounds T polynomially)")]
x = L
for i, (a, b) in enumerate(W): print('W', i, 'old in L-1', L.count(a)); x = x.replace(a, b)
print('L-1 + W', shape(x))
open(sys.argv[2], 'w', encoding='utf-8').write(x)
