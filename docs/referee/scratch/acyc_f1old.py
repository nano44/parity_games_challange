"""REFEREE 28: every «…» following «Old» in P-ACYC fixes entry 1 must occur once in the frozen packet (both with wrapped lines joined
by one space; packet raw-line search also reported). Usage: acyc_f1old.py FIXES PACKET"""
import sys, re
J = lambda t: re.sub(r"\s*\n\s*", " ", t)
F = J(open(sys.argv[1], encoding="utf-8").read()); P = J(open(sys.argv[2], encoding="utf-8").read())
for m in re.finditer(r"Old[^«]{0,40}?: «(.*?)»(?= New| \(|\s)", F):
    o = re.sub(r"\s+", " ", m.group(1)); Pn = re.sub(r"\s+", " ", P)
    print(Pn.count(o), "|", o[:110])
