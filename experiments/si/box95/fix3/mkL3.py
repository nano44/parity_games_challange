#!/usr/bin/env python3
"""L-SI P-N5-GATE line L-3 = line L-2 (docs/si/P-N5-GATE-line-L2.txt, sha1 c0f2007d…) with fixes entry 3 applied, answering BOTH referees:
REFEREE 31 (claude/referee a401ce0e, R-P-N5-GATE §5: R-1..R-7, D-1..D-5b, G-a..G-c; byte copy ref_R-P-N5-GATE_a401ce0e.md) and REFEREE-2 37
(claude/referee-2 c035b35f, R2-P-N5-GATE §3.5: the 13 strings of its l3req.py; byte copy ref2_l3req_c035b35f.py, read with ast, never run).
Every referee string is PARSED from those copies (sha1 asserted), never retyped. Where both referees target overlapping text the two are
merged into ONE replacement (each referee Old asserted to lie inside the merged Old); every referee id is asserted to be answered by some
replacement. Each Old is asserted to occur exactly once in the text at the moment it is applied. Prints L-3 (one line), or with --table the
answer table «answers | kind» used by fixes entry 3. Usage: mkL3.py ROOT [--table]"""
import ast, hashlib, os, re, sys
ROOT = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__))
def rd(p, sha):
    b = open(p, "rb").read(); assert hashlib.sha1(b).hexdigest() == sha, p; return b.decode("utf-8")
L2 = rd(os.path.join(ROOT, "docs/si/P-N5-GATE-line-L2.txt"), "c0f2007d84afab1e00ef41e24ba8f5f064468cc5")
r31 = rd(os.path.join(HERE, "ref_R-P-N5-GATE_a401ce0e.md"), "8c24800e21109d2dec4b1525bcef3445db7f7720")
r2py = rd(os.path.join(HERE, "ref2_l3req_c035b35f.py"), "30833fcca8c56fc9e7aa19240d5e1c96355b3546")
# REFEREE 31's §5 table
A = {}
for l in r31.split("## 5. Line L-2")[1].split("\n## ")[0].split("\n"):
    m = re.match(r"\| ((?:R|D|G)-[0-9a-z]+)[^|]*\| «(.*?)» \| «(.*?)»", l)
    if m: A["31:" + m.group(1)] = (m.group(2), m.group(3))
assert len(A) == 16, sorted(A)
# REFEREE-2 37's REQ list (a literal in l3req.py)
tree = ast.parse(r2py)
req = next(n.value for n in tree.body if isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") == "REQ")
B = {"2:" + i: (o, n) for i, o, n in ast.literal_eval(req)}
assert len(B) == 13, sorted(B)
o = lambda k: (A.get(k) or B.get(k))[0]
nw = lambda k: (A.get(k) or B.get(k))[1]
NT = "Corollary NO-TIE («at every state and gate g, Ω_t(e_g) ≠ Ω_t(β_g)»), "
# FINAL replacements: (answers, kind, old, new). kind V = one referee's string verbatim; S = the two referees' strings coincide in meaning
# (one taken); M = merged by the lane.
F = [
 (["31:R-6", "31:R-7", "31:R-2", "31:G-c", "2:R-5c", "2:R-1/R-10"], "M", o("31:R-6") + " " + o("2:R-1/R-10"),
  NT + "and (E-DOM) and (Core) read off RESULTS R104's priorities and closed core with LOC-K2 (non-core vertices only: the core is entered "
  "only at K0 and then follows one fixed suffix, so K0, K3 lie on the play iff Λ is a core vertex), for IDEAL-CYC; " + nw("2:R-1/R-10")),
 (["31:R-1", "2:R-4"], "M", o("2:R-4"),
  "(Lemma PAIR-EXPEL; its Step 1 is the argument of P-N5-SPLIT §3 (a), Lemma REWIN (a), which the packet writes out in full from F1, "
  "STRICT, F3, F6, F4′, CN2-3, so no P-N5-SPLIT premise is used)"),
 (["31:R-3", "2:R-3/R-5d", "2:R-8a"], "M", o("31:R-3"),
  nw("31:R-3").replace("C ≤ A*_all ≤ 1 + M·C (on both runs)", "C ≤ A*_all ≤ 1 + M·C (on both runs, with no P-N5-SPLIT premise: each entry of "
  "a top starts a run, and every run but one starts at a change; referee-originated: REFEREE-2 R2-P-N5-GATE G-7)")),
 (["31:R-4", "2:R-5a"], "M", o("31:R-4"), "(b) F1, F2, F3, F4′'s stated clause, F6, (c) STRICT, (e) in its per-vertex form"),
 (["31:R-5", "2:R-5b"], "S", o("31:R-5"), nw("31:R-5")),
 (["31:G-a", "2:R-6a"], "M", o("31:G-a"),
  "and on Γ3 it does not occur either, by RESULTS R125's B-ONLY3, the same argument with the pads (pβ_o is never an exception; pe_o is "
  "one only when D = c_W, and then Λ(pe_o) = c_W ≠ Λ(pβ_o); referee-originated: REFEREE R-P-N5-GATE GT-1 and REFEREE-2 R2-P-N5-GATE G-5)"),
 (["31:G-b", "2:R-6b"], "M", o("31:G-b"),
  "and on Γ3 it holds at every state 0, …, T3 by RESULTS R125's B-ONLY3 at the mover D, by the same argument, so there too (b), (c) and "
  "WAIT-QUIET hold with no proviso (referee-originated: REFEREE R-P-N5-GATE GT-1 and REFEREE-2 R2-P-N5-GATE G-5)"),
 (["31:D-4", "2:R-9"], "M", o("31:D-4"),
  nw("31:D-4").replace("(REFEREE replay, own engine; the lane's lev94 compares sizes)",
                       "(REFEREE replay, own engine; L-SI's set re-measure copy95.py agrees on both engines; the lane's lev94 compares sizes)")),
 (["31:D-1"], "V", o("31:D-1"), nw("31:D-1")),
 (["31:D-2"], "V", o("31:D-2"), nw("31:D-2")),
 (["31:D-3"], "V", o("31:D-3"), nw("31:D-3")),
 (["31:D-5a"], "V", o("31:D-5a"), nw("31:D-5a")),
 (["31:D-5b"], "V", o("31:D-5b"), nw("31:D-5b")),
 (["2:R-8b"], "V", o("2:R-8b"), nw("2:R-8b")),
 (["2:R-7a"], "V", o("2:R-7a"), nw("2:R-7a")),
 (["2:R-7b"], "V", o("2:R-7b"), nw("2:R-7b")),
 (["lane"], "M", "with its fixes entries 1-2, docs/si/P-N5-GATE-fixes.md", "with its fixes entries 1-3, docs/si/P-N5-GATE-fixes.md"),
]
done = set()
for ans, kind, a, b in F:
    for k in ans:
        if k in A or k in B: assert o(k) in a, (k, "referee Old not inside the merged Old")
    done.update(ans)
miss = [k for k in list(A) + list(B) if k not in done]
miss = [k for k in miss if k != "2:R-9" or "2:R-9" not in done]
assert not [k for k in list(A) + list(B) if k not in done], [k for k in list(A) + list(B) if k not in done]
if "--table" in sys.argv:
    for ans, kind, a, b in F: print(", ".join(ans) + " | " + kind)
    sys.exit(0)
L = L2
for ans, kind, a, b in F:
    assert L.count(a) == 1, (ans, L.count(a), a[:70])
    L = L.replace(a, b)
for bad in ("§2 (a)", "P-N5-CHAIN's C-EQUIV", "lie on both of two plays", "not a premise here", "not among P-N5-CHAIN", "while its play avoids",
            "over the run then", "CTRL=a0"):
    assert bad not in L, bad
assert "|" not in L and L.count("\n") == 1 and L.endswith("\n") and L.count("(") == L.count(")")
sys.stdout.write(L)
