#!/usr/bin/env python3
"""L-SI P-N5-GATE fixes entry 4 (fix round 4: REFEREE 31's L-3 byte test §I LT-1 and §J GT-10; REFEREE-2 37's L-3 test added nothing).
Prints entry 4 (appended after entries 1-3). Packet Olds asserted once in the frozen packet (wrapped lines joined by one space). Usage:
mkfix4.py ROOT L4SHA1 L4BYTES"""
import hashlib, os, re, sys
ROOT, S4, B4 = sys.argv[1], sys.argv[2], sys.argv[3]
raw = open(os.path.join(ROOT, "docs/si/P-N5-GATE.md"), "rb").read()
assert hashlib.sha1(raw).hexdigest() == "f3a584e68b5c998276ea717f42920bdeeca581ab"
pk = re.sub(r"\s*\n\s*", " ", raw.decode("utf-8"))
def q(s):
    assert pk.count(s) == 1, (pk.count(s), s[:70]); return "«" + s + "»"
O = []; w = O.append
w("")
w("## Entry 4 (fix round 4; L-SI successor 50; Lead 2026-11-12 02:57Z, 03:00Z, 03:17Z, 04:09Z)")
w("Items: REFEREE 31 (claude/referee fbc4d865, docs/referee/R-P-N5-GATE.md; byte copy experiments/si/box95/fix4/ref_R-P-N5-GATE_fbc4d865.md,")
w("sha1 9aaf92a6…): §I (L-3 byte test: entry 3 CORRECT; L-3 MATCHES except LT-1) and §J (GT-10, strings GL-1..GL-3). REFEREE-2 37's L-3")
w("byte test (claude/referee-2 6269fec5, Addendum 2): L-3 MATCHES, no new item. Strings: L-4 by fix4/mkL4.py (GL-1..GL-3 parsed from the byte")
w("copy, never retyped); this text by fix4/mkfix4.py.")
w("")
w("### F4-1 (LT-1, REQUIRED; Lead's ruling: the landing-order form)")
w("- REFEREE 31: L-3 dropped P-N5-SPLIT's pending status. Lead's ruling (02:57Z): the landing order is fixed, R126 = P-N5-QN, then R127 =")
w("  P-N5-SPLIT, then this entry; so SPLIT-COUNT and C-EQUIV are cited as «RESULTS R127 (P-N5-SPLIT)», and A*-EQUIV (ii), (iii) stay")
w("  labelled CONDITIONAL with R127 as the premise; CHECKER confirms R127 = P-N5-SPLIT at this entry's landing. (REFEREE 31's own New, «of")
w("  the pending packet P-N5-SPLIT … not landed», is superseded by the ruling.)")
w("- L-4: «C-EQUIV of P-N5-SPLIT (L-NEW, frozen claude/l-new 399cda07, sha1 5bc1b1f3);» → «C-EQUIV of RESULTS R127 (P-N5-SPLIT; L-NEW,")
w("  frozen claude/l-new 399cda07, sha1 5bc1b1f3; landing order R126 = P-N5-QN, R127 = P-N5-SPLIT, then this entry);», and «PROVED-CONDITIONAL")
w("  on P-N5-SPLIT's SPLIT-COUNT and C-EQUIV» → «PROVED-CONDITIONAL on RESULTS R127 (P-N5-SPLIT)'s SPLIT-COUNT and C-EQUIV».")
w("- Packet reading: wherever the packet (with entries 1-3) cites P-N5-SPLIT's SPLIT-COUNT or C-EQUIV as a premise (table §3.8, §3.8's")
w("  heading and (ii), (iii), §1's P-N5-SPLIT row), read «RESULTS R127 (P-N5-SPLIT)»; the labels stay CONDITIONAL on it.")
w("")
w("### F4-2 (GT-10 = L43, REQUIRED; GL-1..GL-3 verbatim): three asymptotic rows leave the DEAD list and become DATA")
w("- L43 (Lead reading, docs/DECISIONS.md, quoted by REFEREE 31 §J): a lane DEAD of an ASYMPTOTIC statement enters a RESULTS line as DATA")
w("  with its numbers and source commit, or not at all. The three rows below refute their statements only on finitely many instances.")
w("- §5 rows relabelled DATA, not DEAD (the numbers and instances stand; the word «DEAD» goes):")
w("  - " + q("| RA-MULT(K) (constant re-arm multiplicity) | m = n, C = 2n + 1 | MW8_2, MW32_2 | 66b84dcb, 445031d1 | box91 inst |"))
w("    → DATA: re-arm multiplicity m = n with C = 2n + 1 on MW8_2, MW32_2 (refutes a constant multiplicity only below 32).")
w("  - " + q("| polynomial P bound (RA path count) | P = F_(d+2) − 1 with C = 3 | FW8_2, FW16_2 | 108a63cf, 94df42b7 | box91 inst |"))
w("    → DATA: RA path count P = F_(d+2) − 1 with C = 3 on FW8_2, FW16_2 (no finite instance set refutes «polynomial»).")
w("  - " + q("| K1-FLIP(c), every constant c, at k = 1 (L-RED 63) | flips 2n + 1 with lamch 0 | MWR4_2, MWR8_2, MWR16_2 | 856d369b, 918f1414, 2ccda9a9 | box93 inst (copies of claude/l-red 406ef2fd r229/inst) |"))
w("    → DATA: per-gate flips 9 / 17 / 33 at lamch 0 on MWR4_2, MWR8_2, MWR16_2 (L-RED 63, claude/l-red 406ef2fd; refutes c·(lamch + 1)")
w("    only for c ≤ 32).")
w("- The construction rows (WC, K6 LAG TOWER, K7 probe, nesting multipliers, Db / Dbr) stay DEAD: each records that a named construction")
w("  fails to produce growth, with measured numbers; they claim no asymptotic bound (REFEREE 31 §J; the Lead, 03:00Z).")
w("- L-4: GL-1 and GL-2 delete the three from the DEAD clause; GL-3 adds them as DATA after «… inst with sha1 files» (strings in fix4/mkL4.py,")
w("  parsed from REFEREE 31 §J).")
w("")
w("### F4-3 (L-4)")
w("- docs/si/P-N5-GATE-line-L4.txt = L-3 + LT-1 (two strings) + GL-1..GL-3 + «fixes entries 1-4»; sha1 " + S4 + ", " + B4 + " bytes (wc -c).")
w("  mkL4.py asserts each Old once, that «RA-MULT», «K1-FLIP(c)» and «a polynomial bound on the RA path count» are absent, no «|», and")
w("  balanced parentheses.")
sys.stdout.write("\n".join(O) + "\n")
