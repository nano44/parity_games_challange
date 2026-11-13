#!/usr/bin/env python3
# REFEREE-2 successor 38: byte test of P-N5-GATE line L-5 (R128; CHECKER C142 E-1..E-3).
# Independent rebuild of L-5 from L-4 (claude/l-si 676b6a1c, sha1 6bfde78e, signed MATCHES in R2-P-N5-GATE Add. 3) with the
# old -> new strings parsed out of a whitespace-normalised source text: CHECKER C142 §4 (claude/checker 269effb3) in mode c142,
# or the lane's fixes entry 5 in mode fixes. No lane or CHECKER code is imported.
# Usage: bt_l5.py c142  L4.txt C142.md  OUT.txt [L5_lane.txt]
#        bt_l5.py fixes L4.txt FIXES.md OUT.txt L5_lane.txt     (pairs: every «old» → «new» of "## Entry 5", in order)
# The check against CHECKER's hash is exact only for the nine pairs of C142 §4; a tenth pair (the source note's entry count) is
# reported, and then the rebuilt text differs from 7ebcf735 by that pair alone (checked by reversing it).
import sys, hashlib, difflib
mode, pL4, pSRC, pOUT = sys.argv[1:5]; pLANE = sys.argv[5] if len(sys.argv) > 5 else None
L4 = open(pL4, encoding="utf-8").read(); raw4 = open(pL4, "rb").read(); fails = 0
def ck(n, ok, info=""):
    global fails; fails += not ok; print(("PASS " if ok else "FAIL ") + n + (" :: " + info if info else ""))
def sha(b): return hashlib.sha1(b).hexdigest()
ck("L-4 is sha1 6bfde78e, 12,562 B", sha(raw4) == "6bfde78ef050b47f43527875256c65a205869e77" and len(raw4) == 12562, f"{sha(raw4)} {len(raw4)}")
SRC = " ".join(open(pSRC, encoding="utf-8").read().split())
def quotes(s):                      # every balanced «…» of s with its span, in order (nested « » allowed)
    out = []; i = 0
    while True:
        i = s.find("«", i)
        if i < 0: return out
        d = 0; j = i
        while True:
            if s[j] == "«": d += 1
            elif s[j] == "»":
                d -= 1
                if d == 0: break
            j += 1
        out.append((s[i + 1:j], i, j + 1)); i = j + 1
def pairs(s):                       # «old» → «new»: two consecutive quotes separated by exactly " → "
    qs = quotes(s); out = []; k = 0
    while k + 1 < len(qs):
        if s[qs[k][2]:qs[k + 1][1]] == " → ": out.append((qs[k][0], qs[k + 1][0])); k += 2
        else: k += 1
    return out
if mode == "c142":
    sec = SRC[SRC.index("## 4. Line L-5 and its UPDATE"):SRC.index("## 5. Checks run")]
else:
    sec = SRC[SRC.index("## Entry 5"):]            # P-N5-GATE-fixes.md headings are «## Entry N (fix round N; …)»
    nxt = sec.find("## Entry 6")
    if nxt > 0: sec = sec[:nxt]
P = pairs(sec); print("pairs parsed:", len(P))
ck("nine old -> new pairs (R-E1, R-E2, seven of R-E3), or ten with the source note's entry count", len(P) in (9, 10), str(len(P)))
C142 = [("R-E1", "re-arm multiplicity m = n with C = 2n + 1"), ("R-E2", "growth: C, A*_all and the largest gate flip count"), ("R-E3.1", "(Lemma GATE-LOW-NULL) at a LAM"),
        ("R-E3.2", "(and they differ), so a flip at t"), ("R-E3.3", "at t, and if Λ(p_e) = Λ(p_b)"), ("R-E3.4", "(Corollary E-FACE-PAYS) relocks(o)"),
        ("R-E3.5", "UP hypothesis, at every t with e_o"), ("R-E3.6", "so if D's play avoids e_o at every state of the run then"), ("R-E3.7", "unchanged), and flips(o) ≤ 2·min")]
for nm, frag in C142: ck(f"{nm}: exactly one parsed pair's old contains its anchor", sum(frag in o for o, _ in P) == 1)
extra = [(o, n) for o, n in P if not any(frag in o for _, frag in C142)]
for o, n in extra: print("EXTRA pair (not in C142 §4):", repr(o), "->", repr(n))
L = L4
for k, (o, n) in enumerate(P):
    c = L.count(o); ck(f"pair {k + 1} old occurs once in the running text", c == 1, f"{c} :: {o[:60]}…"); L = L.replace(o, n, 1)
b = L.encode(); open(pOUT, "w", encoding="utf-8").write(L)
print("rebuilt L-5: sha1", sha(b), len(b), "B")
L9 = L
for o, n in extra:
    assert L9.count(n) == 1; L9 = L9.replace(n, o, 1)
b9 = L9.encode()
ck("rebuilt (without any EXTRA pair) = CHECKER's L-5 (sha1 7ebcf735…, 12,923 B; C142 §4)", sha(b9) == "7ebcf7355be9838473f05a7defe913940b6fd723" and len(b9) == 12923,
   f"{len(extra)} extra pair(s)")
ck("one line with its newline, 0 '|', 238 '(' = 238 ')'", L.count("\n") == 1 and L.endswith("\n") and "|" not in L and L.count("(") == L.count(")") == 238,
   f"nl {L.count(chr(10))} bars {L.count('|')} parens {L.count('(')} {L.count(')')}")
T = L
if pLANE:
    lane = open(pLANE, "rb").read(); T = lane.decode("utf-8")
    ck("lane L-5 BYTE-EQUAL to my rebuild", lane == b, f"lane {sha(lane)} {len(lane)} B")
    print("INFO lane L-5 = CHECKER's 7ebcf735…, 12,923 B:", sha(lane) == "7ebcf7355be9838473f05a7defe913940b6fd723" and len(lane) == 12923)
# --- content checks on the tested text T (the lane's L-5 if given, else my rebuild)
for bad in ["m = n", "P = F_(d+2) − 1 with", "A*_all and the largest", "linear in n", "on every family measured", "MW(n): C = 2n + 1", "MWR(n): flips", "which makes E-FACE-PAYS (d) tight",
            # banned strings of Add. 2 / Add. 3 stay absent
            "§2 (a)", "P-N5-CHAIN's C-EQUIV", "lie on both of two plays", "not a premise here", "not among P-N5-CHAIN", "while its play avoids", "over the run then",
            "CTRL=a0", "is a hypothesis here", "L-RED R228", "afail", "pxfail", "box 94's 22 instances", "RA-MULT", "K1-FLIP(c)", "a polynomial bound on the RA path count",
            "pending packet"]:
    ck("absent: " + bad, bad not in T)
REQ = {
 "E-1 m numbers": "re-arm multiplicity m 8 / 32 with C 17 / 65 on MW8_2 / MW32_2 (refutes a constant multiplicity only below 32)",
 "E-1 P numbers": "the RA path count P 54 / 2583 (= F_(d+2) − 1 at d = 8, 16) with C 3 on FW8_2 / FW16_2",
 "E-1 source": "(m and P: L-SI 47 box 90, claude/l-si 2d0344d3 and 4ded1e8d, box90/out/mw90.out maxm and fw90.out maxP, both engines)",
 "E-2 lead-in": "growth, as numbers on the named instances only (both engines; box91/out/own91.out and g391.out C and maxflip, box93/out/mwr93_own.out and mwr93_g3.out mx_flips and mx_ch_D):",
 "E-2 MW numbers": "C 17 / 65 and the largest per-gate flip count 34 / 130 on MW8_2 / MW32_2",
 "E-2 MWR numbers": "per-gate flips 9 / 17 / 33 = 2·ch_D + 1 (ch_D 4 / 8 / 16) with lamch 0 on MWR4_2, MWR8_2, MWR16_2, where E-FACE-PAYS (d) holds with equality",
 "E-3 GLN (a)": "(Lemma GATE-LOW-NULL) (a) at a LAM ∧ PRIV step",
 "E-3 GLN (b)": "(and they differ), so (b) a flip at t",
 "E-3 GLN (b′)": "changes π(E(p_e)) or π(E(p_b)) at t, and (b′) if Λ(p_e) = Λ(p_b)",
 "E-3 EFP (a)": "(Corollary E-FACE-PAYS) (a) relocks(o) ≤ ch_(p_e),",
 "E-3 EFP (b)": "UP hypothesis, (b) at every t with e_o ∉",
 "E-3 EFP (c)": "that of D does, so (c) if D's play avoids e_o at every state of the run then",
 "E-3 EFP (d)": "unchanged), and (d) flips(o) ≤ 2·min(ch_(p_e), ch_(p_b)) + 1",
}
for k, s in REQ.items(): ck("present once: " + k, T.count(s) == 1, str(T.count(s)))
ck("«A*_all» only in the A*-EQUIV statement and its DATA counters, not in a growth clause", "A*_all" not in T[T.index("growth, as numbers"):T.index("growth, as numbers") + 700] if "growth, as numbers" in T else False)
import re
print("INFO source note:", re.findall(r"with its fixes entries [0-9]+-[0-9]+", T), re.findall(r"L-SI successors [0-9, -]+", T))
# --- word-level diff L-4 -> T; E-3 regions must be pure insertions of one marker token
a, c_ = L4.split(" "), T.split(" ")
ops = [op for op in difflib.SequenceMatcher(None, a, c_, autojunk=False).get_opcodes() if op[0] != "equal"]
print("diff regions L-4 -> L-5:", len(ops))
MARK = {"(a)", "(b)", "(b′)", "(c)", "(d)"}; ins = 0
for op, i1, i2, j1, j2 in ops:
    o, n = " ".join(a[i1:i2]), " ".join(c_[j1:j2]); pure = op == "insert" and j2 - j1 == 1 and c_[j1] in MARK; ins += pure
    print("  ", op, "PURE-MARKER" if pure else "", "|", o[:160], "->", n[:260])
ck("exactly seven pure single-marker insertions", ins == 7, str(ins))
# words unchanged outside E-1 / E-2: delete the 7 markers at their insertion points and the E-1 / E-2 news -> must give L-4 back
back = T
for o, n in reversed(P): 
    c = back.count(n); ck("reverse: new occurs once", c == 1, f"{c} :: {n[:50]}…"); back = back.replace(n, o, 1)
ck("reversing the nine pairs on the tested text gives L-4 byte for byte", back.encode() == raw4)
print("FAILS", fails)
