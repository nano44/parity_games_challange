"""REFEREE successor 29: required change CL-1 (one span; covers the control sets and the false «every fail counter has one») to
P-N5-CHAIN line L-1. The old string must occur once. Prints counts, balance, predicted sha1 and size. Usage: chain_linefix.py L1 OUT"""
import sys, hashlib
L = open(sys.argv[1], encoding="utf-8").read()
O = ("controls fire (every fail counter has one): ctrl1 (L3 := 0, U(G) := −1) wfail 32, Tfail 22, upfail 26,477 in 50 runs; ctrl2 (order "
     "reversed) locfail 3,320; ctrl3 (no excluded vertex) bonly 2,269; spec mode nohoward 599 (rand, 200 runs) and 911 (dense, 200 runs);")
N = ("controls fire (every fail counter except ties, NO-TIE3's counter, which has none): ctrl1 (L3 := 0, U(G) := −1) wfail 32, Tfail 22, "
     "upfail 26,477; ctrl2 (order reversed) locfail 3,320; ctrl3 (no excluded vertex) bonly 2,269 (each control on 50 runs, family rand, "
     "seed 1963, check196.out); spec mode, seed 1963 (data/sweep196.out), nohoward 599 (rand, 200 runs) and 911 (dense, 200 runs);")
print("CL-1 old occurs", L.count(O), "| new occurs", L.count(N)); assert L.count(O) == 1
X = L.replace(O, N); b = X.encode()
print("parens", X.count("("), X.count(")"), "| newlines", X.count("\n"), "| predicted L-2 sha1", hashlib.sha1(b).hexdigest(), len(b), "B")
open(sys.argv[2], "w", encoding="utf-8").write(X)
