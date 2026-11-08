# REFEREE-2 33: byte test of P-N5-ASC line L-5 (claude/l-new e28e962d) = L-4 (a744677e) + R-A + R-I (REFEREE 29 §F add. 1; strings typed
# from the Lead's 07:48Z message to REFEREE-2; own code)
import subprocess, hashlib
sh = lambda c, f: subprocess.run(["git", "show", f"{c}:{f}"], capture_output=True).stdout
L4 = sh("a744677ea9e3721a3a29b59ffb69d3ae4272f520", "docs/new/P-N5-ASC-line-L4.txt")
L5 = sh("e28e962d214971b8ef8739967185117a3e5f221c", "docs/new/P-N5-ASC-line-L5.txt")
P4 = sh("a744677ea9e3721a3a29b59ffb69d3ae4272f520", "docs/new/P-N5-ASC.md"); P5 = sh("e28e962d214971b8ef8739967185117a3e5f221c", "docs/new/P-N5-ASC.md")
CH = [("R-A", "(items 1..M, a run of forests with every chain lex-nondecreasing)",
       "(items 1..M compared by number, a run of forests with every chain lex-nondecreasing, an ascent a step to a larger item)"),
      ("R-I", "(f, …), i.e. the first e-vertex on v's play is f and f ∈ Π_t(v), then", "(f, …), then")]
t4, t5 = L4.decode(), L5.decode()
print("L-4", hashlib.sha1(L4).hexdigest(), len(L4), "| L-5", hashlib.sha1(L5).hexdigest(), len(L5), "| packet unchanged:", P4 == P5, hashlib.sha1(P5).hexdigest()[:8])
X = t4
for k, o, n in CH:
    print(k, "old in L-4", t4.count(o), "| old in L-5", t5.count(o), "| new in L-4", t4.count(n), "| new in L-5", t5.count(n)); X = X.replace(o, n)
print("rebuild L-4 + R-A + R-I equal to L-5:", X.encode() == L5, hashlib.sha1(X.encode()).hexdigest(), len(X.encode()))
d = 0; neg = False
for c in t5: d += (c == "(") - (c == ")"); neg |= d < 0
print("L-5 newlines", t5.count("\n"), "parens", t5.count("("), t5.count(")"), "neg", neg, "pipes", t5.count("|"), "under [E-LEV]", t5.count("under [E-LEV]"))
i = t5.find("(Lemma CHAIN-DECOMP)"); print("CHAIN-DECOMP clause:", t5[i:i + 90])
