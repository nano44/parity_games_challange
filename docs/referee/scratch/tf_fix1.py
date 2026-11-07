"""REFEREE successor 27, §C of R-P-TOWER-FUEL: (1) own byte test L-1 -> L-2 with the seven pairs written here (olds from the two
referee reports, news as merged in fixes entry 1 §5); (2) own measurements of fixes entry 1 §3's new counts on t3r_sim.
Usage: tf_fix1.py L1.txt L2.txt SL41_d28.txt"""
import sys, os, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tf_replay import load, R
L1, L2 = (open(p, encoding="utf-8").read() for p in sys.argv[1:3])
P = [
 ("M1", "with its notation c_l, γ_l, flip, F(l))", "with its notation c_l, γ_l, flip, F(l) and cv)"),
 ("M2", "violates PULSE, GAP ≥ 7 − j only at level 5, 30 times",
  "violates PULSE, GAP ≥ 7 − j at levels j = 1, …, 5 (unit = j-window; set = all 119 of them) only at level 5, 30 times (unit = (5-window, PULSE or GAP); in 16 of its 63 5-windows)"),
 ("M3", "while 48 of its 127 6-windows fail, in each of which the crossed pair 6 is decided by the option (9, 1) of rank 87 (in none of the other 79)",
  "while 48 of its 127 6-windows do not have exactly one move of each member of pair 6 (the movers 12 and 13, crossed onto movers 22, 11), and in each of these 48 windows [a, e] the option (9, 1) of rank 87 is dec_s(12) or dec_s(13) at some state s among s_(a−1), …, s_(e−1) (at every such state in 16 of them; at no such state in any of the other 79)"),
 ("M4", "on 24 runs from the stored start, 62 doubling levels, 757 j-windows",
  "on 24 runs from the stored start (the 15 genomes experiments/lower/l3/kill/*.json, the 7 genomes experiments/lower/l4/rec/*.json and the two instances), 62 doubling (run, level) pairs, 757 j-windows"),
 ("M5", "DOUBLE-EQ 0 violations;",
  "DOUBLE-EQ 0 violations (its first two clauses on 7,069 (step, doubling level) units, its third on the 757 j-windows, its fourth on the 62 doubling (run, level) pairs, 61 of them with F(j − 1) ≥ 1);"),
 ("M6", "DOMINANCE-FREEZE 0 on 65,885 equal-decider state pairs and on 1,390 consecutive-move pairs;",
  "DOMINANCE-FREEZE 0 on 65,885 (consecutive-state pair, mover) units with equal deciders and on 1,390 (member of a doubling pair, pair of consecutive moves) units;"),
 ("M7", "the largest rank in the symmetric difference of the chains of A_0 and A_1",
  "the largest rank in the symmetric difference of the Ξ-chains of the current options of A_0 and A_1"),
]
out = L1
for t, o, n in P:
    assert L1.count(o) == 1, (t, "old count in L-1", L1.count(o)); out = out.replace(o, n)
for t, o, n in P:
    print(t, "old once in L-1: yes; new count in L-2:", L2.count(n))
print("L-1 + 7 pairs == L-2 (bytes):", out == L2, "| L-2 sha1", hashlib.sha1(L2.encode()).hexdigest(), len(L2.encode()), "bytes",
      len(L2), "chars", L2.count("("), "(", L2.count(")"), ")", "| count:", L2.count("|"))
# (2) measurements
r = R(load(sys.argv[3])); W = r.wins(6); bad = [w for w in W if sorted(x for _, x in w[2]) != [12, 13]]; bs = {w[0] for w in bad}
park = {True: 0, False: 0}
for a, e, mv in W:
    park[a in bs] += all(r.S[t][9] == 1 for t in range(a - 1, e))
print("mover 9 on option 1 at every pre-state s_(a-1)..s_(e-1): failing", park[True], "/", len(bad), "good", park[False], "/", len(W) - len(bad))
prs = nonconst = 0
for x in (12, 13):
    ts = [t for t in range(1, r.T + 1) if r.mv(t, x)]
    for t, t2 in zip(ts, ts[1:]):
        prs += 1; nonconst += len({r.dec(r.S[v], x) for v in range(t - 1, t2)}) > 1
print("consecutive-move pairs of 12, 13:", prs, "with non-constant dec:", nonconst)
side = {}
for a, e, mv in W:
    for t in range(a - 1, e):
        st = r.S[t]
        for x in (12, 13):
            m, k = r.dec(st, x)
            if m == 19:
                A = r.G["opts"][x][k][1]
                key = ("A=%d" % A, "s(11)=%d" % st[11], "19 on chain(11)" if 19 in r.chain(st, 11, st[11]) else "19 NOT on chain(11)")
                side[key] = side.get(key, 0) + 1
print("decider-19 hits (state, member) by the Ξ-target of the deciding side:", side)
