"""REFEREE successor 30: L-6 = L-5 + CHECKER 22's R6 (C135 Add. 1, claude/checker 0ffde42c). Usage: asc_l6.py L5 OUT"""
import sys, hashlib
L = open(sys.argv[1], encoding="utf-8").read()
O = ("(items 1..M compared by number, a run of forests with every chain lex-nondecreasing, an ascent a step to a larger item), a hub "
     "whose value has")
N = ("(items 1..M compared by number, a forest a map next from the items to the items and ⊥ without cycles, chain(x) := (x, next(x), "
     "next²(x), …) up to ⊥, compared as a set, a run of forests with every chain lex-nondecreasing, an ascent a step to a larger item), "
     "a hub (h_t an item or ⊥ at each time t, chain(⊥) := ∅, with chain_s(h_s) ≤ chain_t(h_t) for s < t) whose value chain_t(h_t) has")
print("R6 old occurs", L.count(O), "| new occurs", L.count(N)); assert L.count(O) == 1
X = L.replace(O, N); b = X.encode(); d = m = 0
for c in X:
    d += (c == "(") - (c == ")"); m = min(m, d)
print("parens", X.count("("), X.count(")"), "min depth", m, "| newlines", X.count("\n"), "| bars", X.count("|"),
      "| predicted L-6 sha1", hashlib.sha1(b).hexdigest(), len(b), "B")
open(sys.argv[2], "w", encoding="utf-8").write(X)
