# REFEREE-2 32: byte test of line L-2 (claude/l-new a5dcf9c6) against Addendum 2's W-3 / W-4 strings (own code)
import subprocess, hashlib, re, difflib
S = "a5dcf9c642d191aa95b0bbab08a97b180ce88925"
sh = lambda f: subprocess.run(["git", "show", f"{S}:{f}"], capture_output=True).stdout
L1, L2 = sh("docs/new/P-N5-ASC-line-L1.txt"), sh("docs/new/P-N5-ASC-line-L2.txt")
for nm, b in (("L-1", L1), ("L-2", L2)):
    t = b.decode(); d = 0; neg = False
    for c in t:
        d += (c == "(") - (c == ")"); neg |= d < 0
    print(nm, hashlib.sha1(b).hexdigest(), len(b), "B", t.count("\n"), "newlines", t.count("("), "(", t.count(")"), ")", "neg", neg, "pipes", t.count("|"))
t1, t2 = L1.decode(), L2.decode()
W3o = "(consecutive state pair, W-target with Λ fixed) pairs"; W3n = "(consecutive state pair, W-target or c_W with Λ fixed) pairs"
W4bo = "UP-JUMP: violations 0 in 1,956 ascents of movers' plays with Λ below every e"
print("W-3 old in L-2:", t2.count(W3o), "| new in L-2:", t2.count(W3n), "| old in L-1:", t1.count(W3o))
print("W-4 clause string in L-2 (option (a): unchanged):", t2.count(W4bo), "| in L-1:", t1.count(W4bo))
w1, w2 = re.split(r"(\s+)", t1), re.split(r"(\s+)", t2)
sm = difflib.SequenceMatcher(a=w1, b=w2, autojunk=False)
for op, a0, a1, b0, b1 in sm.get_opcodes():
    if op != "equal": print("DIFF", op, repr("".join(w1[a0:a1])), "->", repr("".join(w2[b0:b1])))
