#!/usr/bin/env python3
"""REFEREE-2 successor 35: byte tests of P-N5-QUIET L-3 / L-4 and P-N5-CHAIN L-4 (claude/l-new 87603d07). The (key, old, new) lists are
read from the lane generators' SOURCE by ast (literal parsing only; lane code is NOT executed) and applied here in order to the previous
line; each old string must be once in the line it is applied to. Own code. Usage: bt_l34.py (repo root)"""
import subprocess, hashlib, ast
def show(rev, p): return subprocess.run(["git", "show", f"{rev}:{p}"], capture_output=True, check=True).stdout.decode("utf-8")
h = lambda s: hashlib.sha1(s.encode()).hexdigest()
def pairs(src):
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and getattr(node.targets[0], "id", "") in ("R", "FIX", "S"):
            return ast.literal_eval(node.value)
    raise SystemExit("no list")
T = "87603d07"
for name, prev, gen, new in [
        ("QUIET L-3", ("559cdffc", "docs/new/P-N5-QUIET-line-L2.txt"), "experiments/new/box194/mkl3_194.py", "docs/new/P-N5-QUIET-line-L3.txt"),
        ("QUIET L-4", (T, "docs/new/P-N5-QUIET-line-L3.txt"), "experiments/new/box194/mkl4_194.py", "docs/new/P-N5-QUIET-line-L4.txt"),
        ("CHAIN L-4", ("219e3933", "docs/new/P-N5-CHAIN-line-L3.txt"), "experiments/new/box196/mkl4_196.py", "docs/new/P-N5-CHAIN-line-L4.txt")]:
    old = show(*prev); tgt = show(T, new); L = old
    print(f"== {name}: base {prev[0]} {h(old)[:8]} {len(old.encode())} B -> {h(tgt)} {len(tgt.encode())} B")
    for item in pairs(show(T, gen)):
        k, o, n = item[0], item[-2], item[-1]
        print(f"  {k}: old in current {L.count(o)}, new in target {tgt.count(n)}"); L = L.replace(o, n)
    print(f"  target == base + pairs: {L == tgt}; parens {tgt.count('(')} {tgt.count(')')}; pipes {tgt.count('|')}; lines {tgt.count(chr(10))}")
