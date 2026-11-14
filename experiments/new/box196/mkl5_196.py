#!/usr/bin/env python3
# P-N5-CHAIN line L-5 generator (L-NEW successor 69). From the repo root: python3 experiments/new/box196/mkl5_196.py
# L-5 = L-4 + R-U + R-L1 + R-L2, in that order (CHECKER C139 §4, claude/checker 389d19f8: E-1 scope-tail status words = C138's R-U with
# «P-N5-CHAIN» for «P-N5-END»; E-2 stale «unlanded» / «when landed»; CHAIN3 keeps «CONDITIONAL», premises named as RESULTS R121 / R124).
# Asserts the frozen packet's sha1, L-4's sha1, each old string exactly once where applied, one line, no «|», balanced parentheses,
# no «unlanded» / «not landed» / «when landed» / «to land», and the result sha1 C139 §4 gives (473344b1…, 9,047 B).
import hashlib
pk = open("docs/new/P-N5-CHAIN.md", encoding="utf-8").read()
assert hashlib.sha1(pk.encode()).hexdigest() == "6e613ba762b6ecf67247ef6d8674b4c960013039", "frozen packet changed"
L4 = open("docs/new/P-N5-CHAIN-line-L4.txt", encoding="utf-8").read()
assert hashlib.sha1(L4.encode()).hexdigest() == "a69c8aa96fb0b67c6c0a3f6d11670a0b57ba9331", "L-4 changed"
R = [("R-U", "; G-N5-TIME stays OPEN, N5′-xi stays a CANDIDATE (D1); TARGET.md §2 (M4) asks for an algorithm polynomial on every parity "
             "game and §4 says a bound on a restricted class is not M4: not M3, not M4, not a step-4 pass, not a TARGET.md claim (P-N5-CHAIN",
             "; N5′-xi stays a CANDIDATE (D1); TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on "
             "a restricted class is not M4, so this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (P-N5-CHAIN"),
     ("R-L1", "CONDITIONAL on the unlanded lane packets P-N5-END (ENDGAME-3) and P-N5-ASC §4 (its abstract core and F′; RESULTS R121 when "
              "landed))",
              "CONDITIONAL on P-N5-END's Theorem ENDGAME-3 (RESULTS R124) and P-N5-ASC §4 (its abstract core and F′; RESULTS R121))"),
     ("R-L2", "lane packets, not landed: P-N5-END's Theorem ENDGAME-3 (frozen at l-new 131b4c1c, REFEREE 29 SIGN) for CHAIN3, P-N5-ASC "
              "§4's game-free abstract core CS(M) and its constants F′_B (RESULTS R121 when landed) for HUB-ASC-G3 and CHAIN3;",
              "RESULTS R124's Theorem ENDGAME-3 (P-N5-END) for CHAIN3, RESULTS R121's game-free abstract core CS(M) (Lemma SKELETON, Theorem "
              "HUB-ASC(B); P-N5-ASC §4) and its constants F′_B for HUB-ASC-G3 and CHAIN3;")]
L = L4
for k, o, n in R:
    assert L.count(o) == 1, (k, L.count(o))
    L = L.replace(o, n)
    print(k, "applied; sha1", hashlib.sha1(L.encode()).hexdigest()[:8], len(L.encode()), "B")
assert L.endswith("\n") and L.count("\n") == 1 and "|" not in L and L.count("(") == L.count(")"), (L.count("("), L.count(")"))
for w in ("unlanded", "not landed", "when landed", "to land"): assert w not in L, w
b = L.encode(); h = hashlib.sha1(b).hexdigest()
assert h == "473344b1149d4b44d87bdb917607b618d05d57ce" and len(b) == 9047, (h, len(b))
open("docs/new/P-N5-CHAIN-line-L5.txt", "w", encoding="utf-8").write(L)
print("L-5 sha1", h, len(b), "bytes; parens", L.count("("), L.count(")"))
