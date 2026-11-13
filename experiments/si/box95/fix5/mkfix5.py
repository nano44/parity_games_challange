#!/usr/bin/env python3
"""L-SI P-N5-GATE fixes entry 5 (fix round 5: CHECKER C142, FAIL on the first fill of R128 with line items E-1, E-2, E-3). Prints entry 5
(appended after entries 1-4). CHECKER's strings are PARSED from the byte copy chk_C142_269effb3.md §4 (sha1 asserted; wrapped lines
joined by one space), never retyped; the numbers they carry are re-read here from the frozen box outputs by column name.
Usage: mkfix5.py ROOT L5SHA1 L5BYTES"""
import hashlib, os, re, sys
ROOT, S5, B5 = sys.argv[1], sys.argv[2], sys.argv[3]; HERE = os.path.dirname(os.path.abspath(__file__))
raw = open(os.path.join(HERE, "chk_C142_269effb3.md"), "rb").read()
assert hashlib.sha1(raw).hexdigest() == "8b005c61e217f0b3601d57a8d69a29e798fd1403"
sec = raw.decode("utf-8").split("\n## 4. Line L-5 and its UPDATE")[1].split("\n## 5. ")[0]
J = re.sub(r"\s*\n\s*", " ", sec.split("\n- Whitespace:")[0]); P = re.findall(r"«(.*?)» → «(.*?)»", J); assert len(P) == 9
assert "sha1 **7ebcf7355be9838473f05a7defe913940b6fd723**, 12,923 B" in re.sub(r"\s*\n\s*", " ", sec)
def col(path, engine, inst, name):
    L = open(os.path.join(ROOT, "experiments/si", path), encoding="utf-8").read().splitlines()
    h = [l.split() for l in L if l.split()[:3] == ["engine", engine, "instance"]]; assert len(h) == 1, (path, engine)
    r = [l.split() for l in L if l.split()[:2] == [engine, inst + ".json"]]; assert len(r) == 1, (path, engine, inst, len(r))
    return int(r[0][h[0].index(name) - 1])   # the header reads «engine <name> instance …»: one token more than a data row
for e in ("own", "g3"):
    assert [col("box90/out/mw90.out", e, i, "maxm") for i in ("MW8_2", "MW32_2")] == [8, 32]
    assert [col("box90/out/mw90.out", e, i, "C") for i in ("MW8_2", "MW32_2")] == [17, 65]
    assert [col("box90/out/fw90.out", e, i, "maxP") for i in ("FW8_2", "FW16_2")] == [54, 2583]
    assert [col("box90/out/fw90.out", e, i, "C") for i in ("FW8_2", "FW16_2")] == [3, 3]
    f91 = "box91/out/own91.out" if e == "own" else "box91/out/g391.out"
    assert [col(f91, e, i, "C") for i in ("MW8_2", "MW32_2")] == [17, 65]
    assert [col(f91, e, i, "maxflip") for i in ("MW8_2", "MW32_2")] == [34, 130]
    assert [col(f91, e, i, "maxa") for i in ("MW8_2", "MW32_2")] == [9, 33]
    f93 = "box93/out/mwr93_own.out" if e == "own" else "box93/out/mwr93_g3.out"
    assert [col(f93, e, i, "mx_flips") for i in ("MWR4_2", "MWR8_2", "MWR16_2")] == [9, 17, 33]
    assert [col(f93, e, i, "mx_ch_D") for i in ("MWR4_2", "MWR8_2", "MWR16_2")] == [4, 8, 16]
q = lambda s: "«" + s + "»"
O = []; w = O.append
w("")
w("## Entry 5 (fix round 5; L-SI successor 52; Lead 2026-11-12 17:47Z; CHECKER C142)")
w("Items: CHECKER C142 (claude/checker 269effb3, docs/checker/C142.md; byte copy experiments/si/box95/fix5/chk_C142_269effb3.md, sha1")
w("8b005c61…): FAIL on the first fill of R128, with three line items E-1, E-2, E-3 (§2) and one entry-text item E-4 (the Lead's; not in")
w("this entry). Mathematics, tools, box checks, UPDATE and placement PASS there. Strings: L-5 by fix5/mkL5.py, which parses C142 §4's nine")
w("old → new pairs from the byte copy and applies them to L-4 in §4's order, each old string asserted once, and then a tenth pair")
w("ruled by the Lead (F5-4); this text by fix5/mkfix5.py, which prints the same parsed strings. No string of CHECKER's is retyped.")
w("")
w("### F5-1 (E-1, L43, REQUIRED): the RA-MULT and RA-path DATA rows get their numbers and their source commits")
w("- CHECKER: GL-3's two rows gave formulas (m = n, P = F_(d+2) − 1) but no numbers and no source commit. R-E1, verbatim:")
w("  " + q(P[0][0]))
w("  → " + q(P[0][1]))
w("- Re-read here by column name (mkfix5.py asserts them, both engines): box90/out/mw90.out maxm 8 / 32 and C 17 / 65 on MW8_2 / MW32_2;")
w("  box90/out/fw90.out maxP 54 / 2583 and C 3 / 3 on FW8_2 / FW16_2.")
w("- Packet reading: fixes entry 4 F4-2's two DATA rows are read with these numbers and sources.")
w("")
w("### F5-2 (E-2, L43, REQUIRED): the growth clause as numbers on named instances; A*_all leaves it")
w("- CHECKER: «growth: … linear in n on every family measured» named no instance, and A*_all has no lane counter. R-E2, verbatim:")
w("  " + q(P[1][0]))
w("  → " + q(P[1][1]))
w("- Re-read here by column name (both engines): box91/out/own91.out and g391.out C 17 / 65 and maxflip 34 / 130 on MW8_2 / MW32_2;")
w("  box93/out/mwr93_own.out and mwr93_g3.out mx_flips 9 / 17 / 33 and mx_ch_D 4 / 8 / 16 on MWR4_2, MWR8_2, MWR16_2.")
w("- For the record (Lead 17:47Z): box 91's counter «maxa» is NOT A*_all. On MW8_2 / MW32_2 maxa is 9 / 33 (re-read here) while C is 17 / 65;")
w("  CHECKER cites REFEREE-2 Add. 4 for A*_all = 66 on MW32_2. The lane has no A*_all counter; the clause no longer names A*_all.")
w("")
w("### F5-3 (E-3, REQUIRED): the part markers of GATE-LOW-NULL and E-FACE-PAYS enter the line (seven insertions, no word changed)")
w("- CHECKER: the line cites E-FACE-PAYS (b), (c), (d) and GATE-LOW-NULL (a), (b′), but its statements did not mark those parts. The")
w("  markers are the packet's (§3.2, §3.4). R-E3, verbatim, in §4's order:")
for a, b in P[2:]:
    assert b.replace("(a) ", "", 1) == a or b.replace("(b) ", "", 1) == a or b.replace("(b′) ", "", 1) == a or b.replace("(c) ", "", 1) == a or b.replace("(d) ", "", 1) == a, (a, b)
    w("  - " + q(a) + " → " + q(b))
w("- mkfix5.py asserts that each new string is its old string with exactly one marker «(a) », «(b) », «(b′) », «(c) » or «(d) » inserted.")
w("")
w("### F5-4 (the tenth pair: Lead ruling 2026-11-12 17:58Z, flagged by REFEREE-2 38)")
w("- The Lead: L-5's source note must say «with its fixes entries 1-5», not «1-4». Precedent: L-4 changed «1-3» to «1-4» when the")
w("  line-only entry 4 was added. So L-5 gets a tenth pair on top of CHECKER's nine:")
w("  «docs/si/P-N5-GATE.md with its fixes entries 1-4,» → «docs/si/P-N5-GATE.md with its fixes entries 1-5,».")
w("  The successor list «L-SI successors 48-50» stays (the Lead, citing CHECKER C142 G-1: no action).")
w("")
w("### F5-5 (L-5)")
w("- After CHECKER's nine pairs (R-E1, R-E2, R-E3's seven) the line is CHECKER's target byte for byte (C142 §4: «sha1")
w("  **7ebcf7355be9838473f05a7defe913940b6fd723**, 12,923 B»): mkL5.py asserts it and prints it with --nine; check_fix5.sh re-checks it.")
w("- docs/si/P-N5-GATE-line-L5.txt = that line + the tenth pair; sha1 " + S5 + ", " + B5 + " bytes (wc -c). mkL5.py asserts each old")
w("  string once, one line with its newline, no «|», and 238 «(» = 238 «)» before and after the tenth pair.")
assert B5 == "12923" and S5 != "7ebcf7355be9838473f05a7defe913940b6fd723", (S5, B5)
sys.stdout.write("\n".join(O) + "\n")
