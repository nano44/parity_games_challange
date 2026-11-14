# REFEREE-2 32: byte test of P-ACYC fixes entry 1 + line L-2 (claude/l-si 01a68edc) (own code)
import subprocess, hashlib, re, difflib
S = "01a68edc54e64030d3e623694c58ce0c99f4f363"; TR = "origin/claude/vibrant-johnson-nxvvxo"
sh = lambda f, c=S: subprocess.run(["git", "show", f"{c}:{f}"], capture_output=True).stdout
L1, L2, P, F = sh("docs/si/P-ACYC-line-L1.txt"), sh("docs/si/P-ACYC-line-L2.txt"), sh("docs/si/P-ACYC.md"), sh("docs/si/P-ACYC-fixes.md")
for nm, b in (("L-1", L1), ("L-2", L2), ("packet", P), ("fixes", F)):
    print(nm, hashlib.sha1(b).hexdigest(), len(b), "B")
t1, t2 = L1.decode(), L2.decode()
d = 0; neg = False
for c in t2: d += (c == "(") - (c == ")"); neg |= d < 0
print("L-2 newlines", t2.count("\n"), "parens", t2.count("("), t2.count(")"), "neg", neg, "pipes", t2.count("|"))
mine = [("W-3(a)+D-1 (Add. 1, combined)", "σ̄ off the β-face 0, non-standard states 0, genomes with first fallback after iteration N + 1 0;",
         "σ̄ off the β-face 0, states that are not standard (σ off the movers and τ) 0, genomes with no fallback 0, genomes with first fallback after iteration N + 1 0 (k = T3 + 1 is R118 (k)'s own clause, and N5's L(G) is R117's: no separate DATA);"),
        ("D-2=AC-L5 + D-3", "control, five Ξ-cyclic genomes: σ̄ off the β-face 121, C 15, R 25",
         "control, five Ξ-cyclic genomes rd2_d3, rd2_d4, rd3_d3, rf_d4, RS2 (59 states; the same counts on IDEAL-CYC and along N5′-xi on Γ3; e-priorities ordered by (lev, gate index), as in ref gamma3.build): σ̄ off the β-face in 121 (state, gate) pairs, C 15, R 25")]
for nm, o, n in mine:
    print(nm, "| old in L-1:", t1.count(o), "| old in L-2:", t2.count(o), "| new in L-2:", t2.count(n))
# word-level diff L-1 -> L-2: list every changed region
w1, w2 = re.split(r"(\s+)", t1), re.split(r"(\s+)", t2)
sm = difflib.SequenceMatcher(a=w1, b=w2, autojunk=False)
for op, a0, a1, b0, b1 in sm.get_opcodes():
    if op != "equal": print("DIFF", op, "OLD:", repr("".join(w1[a0:a1])), "\n     NEW:", repr("".join(w2[b0:b1])))
# packet replacements of entry 1: every «Old» must occur exactly once in the frozen packet (whitespace-normalised)
N = lambda s: re.sub(r"\s+", " ", s)
pn = N(P.decode()); ft = F.decode()
olds = re.findall(r"Old(?: \([^)]*\))?: «(.*?)»(?=\s*\n?\s*New)", ft, flags=re.S)
for o in olds: print("packet Old count", pn.count(N(o)), "|", N(o)[:90])
# the N-1 quote in trunk RESULTS
R = N(sh("docs/RESULTS.md", TR).decode()); q = "S1's σ̄, and τ̄ on the dual game, are pointwise optima"
print("N-1 quote in trunk RESULTS:", R.count(q))
# independent rebuild: L-1 + REFEREE's exact AC-L1..AC-L3 (claude/referee acyc_linefix.py, read as data) + my two strings
src = subprocess.run(["git", "show", "origin/claude/referee:docs/referee/scratch/acyc_linefix.py"], capture_output=True, text=True).stdout
ns = {}; exec(src.split("pos = []")[0].split("L = open")[0] + "CH = " + src.split("CH = ", 1)[1].split("\npos = []")[0], ns)
ref = {nm: (o, n) for nm, o, n in ns["CH"]}
B = t1
for k in ("AC-L1", "AC-L2", "AC-L3"): assert B.count(ref[k][0]) == 1; B = B.replace(*ref[k])
for nm, o, n in mine: assert B.count(o) == 1; B = B.replace(o, n)
bb = B.encode()
print("rebuild sha1", hashlib.sha1(bb).hexdigest(), len(bb), "B; equal to L-2:", bb == L2)
