#!/usr/bin/env python3
"""Line-citation check for PGLemmas/Spec.lean (Lead 03:58Z U4): every «si.py l. A[-B]» and «n5x.py l. A[-B]» in Spec.lean
must be one of the anchored ranges below, computed from the blobs the Lead diffed against (git cat-file -p <blob>):
si.py = experiments/si/si.py blob 0747733e, n5x.py = experiments/new/box21/n5x.py blob 21c3201f (the Lead's diff), and
n5.py = experiments/new/n5.py blob f1f82fcc, n5v.py = experiments/new/box190/n5v.py blob 73db4e89 (at 0ee5b8bc).  Each anchor names the
first and last line by their text; the script prints every anchor with its computed range and FOUND / MISSING in
Spec.lean, then every citation in Spec.lean with OK / UNKNOWN.  Exit 0 iff no MISSING and no UNKNOWN.
Usage (from lean/lemmas): python3 -I check/speccite.py"""
import re
import subprocess
import sys

BLOBS = {"si.py": "0747733e60964f6b8f32285c7a71d41a4c77ebab", "n5x.py": "21c3201f7d507397e7f2fd5ce312e2e0520f95af",
         "n5.py": "f1f82fccb067f122a1ffc59a48dad3221b19eecf", "n5v.py": "73db4e898ba04db98d93c3748f92788a2d5dc78a"}
# (file, what, first-line text, last-line text or None for a single line)
ANCHORS = [
    ("si.py", "Engine.__init__", "def __init__(self, g):", "self.mem = {}"),
    ("si.py", "succ sorted(set)", "self.succ = [sorted(set(s)) for s in g.succ]", None),
    ("si.py", "pred", "self.pred = [[] for _ in range(n)]", "self.pred[w].append(v)"),
    ("si.py", "rank", "order = sorted(range(n), key=lambda v: (g.prio[v], v))", "self.rank[v] = r"),
    ("si.py", "par", "self.par = [g.prio[v] % 2", None),
    ("si.py", "pp", "self.pp = [2 * self.rank[v]", None),
    ("si.py", "rew", "self.rew = [self.pp[v] if", None),
    ("si.py", "bit", "self.bit = [1 << self.rank[v]", None),
    ("si.py", "rankpar", "self.rankpar = [0] * n", "self.rankpar[self.rank[v]] = self.par[v]"),
    ("si.py", "weight", "def weight(self, mask):", "return w"),
    ("si.py", "key", "def key(self, val):", "return (self.rew[w], self.weight(path)"),
    ("si.py", "extend", "def extend(self, u, val):", "return (w, path | (self.bit[u]"),
    ("si.py", "evaluate", "def evaluate(self, strat):", "return res"),
    ("si.py", "gs / gp", "gs = [([strat[v]] if self.owner[v] == EVEN", "gp[w].append(v)"),
    ("si.py", "outer loop", "for v in sorted(range(n), key=lambda x: self.rew[x]):", "continue"),
    ("si.py", "outer loop (head)", "for v in sorted(range(n), key=lambda x: self.rew[x]):", None),
    ("si.py", "state init", "alive = [True] * n", "tau_full = [None] * n"),
    ("si.py", "outer body", "for v in sorted(range(n), key=lambda x: self.rew[x]):", "tau_full[x] = tau[x]"),
    ("si.py", "(i) cycle test", "rv = rank[v]", "if not found:"),
    ("si.py", "(i) loop", "while st and not found:", None),
    ("si.py", "(i) scan", "for y in gs[x]:", "seen.add(y); st.append(y)"),
    ("si.py", "(ii) R", "# R: alive vertices reaching v", "R.add(y); st.append(y)"),
    ("si.py", "(ii) loop", "while st:", None),
    ("si.py", "(ii) scan", "for y in gp[x]:", "R.add(y); st.append(y)"),
    ("si.py", "(iii) init", "hs = {x: [y for y in gs[x] if y in R] for x in R}", "path = {x: 0 for x in R}"),
    ("si.py", "reach", "def reach(start, excl):", "return s"),
    ("si.py", "reach loop", "while st2:", None),
    ("si.py", "reach scan", "for y in hp[x]:", "s.add(y); st2.append(y)"),
    ("si.py", "restrict", "def restrict(x, M):", "hs[x] = keep"),
    ("si.py", "u loop", "for u in sorted((x for x in R if rank[x] > rv)", "                            restrict(q, M)"),
    ("si.py", "u loop (head)", "for u in sorted((x for x in R if rank[x] > rv)", None),
    ("si.py", "even u", "if self.par[u] == 0:", "restrict(q, M)"),
    ("si.py", "odd u", "else:                                # Odd likes u", "restrict(q, M)"),
    ("si.py", "(iv)", "dist = {}", "layer = nxt"),
    ("si.py", "longest state", "state = {}", "dist[x] = longest(x)"),
    ("si.py", "longest", "def longest(x):", "return best + 1"),
    ("si.py", "longest (with state)", "state = {}", "return best + 1"),
    ("si.py", "for x in R: longest", "for x in R:", "dist[x] = longest(x)"),
    ("si.py", "BFS", "else:                                    # odd cycle", "layer = nxt"),
    ("si.py", "BFS loop", "while layer:", "layer = nxt"),
    ("si.py", "(v)", "# v itself: Odd's choice", "tau[v] = x if x != v else cyc"),
    ("si.py", "(v) owner test", "if self.owner[v] == ODD:", None),
    ("si.py", "(v) DFS", "par = {v: None}; st = [v]; cyc = None", "par[y] = x; st.append(y)"),
    ("si.py", "(v) par init", "par = {v: None}; st = [v]; cyc = None", None),
    ("si.py", "(v) loop", "while st and cyc is None:", None),
    ("si.py", "(v) scan", "for y in gs[x]:", "par[y] = x; st.append(y)"),
    ("si.py", "(v) y == v", "                        if y == v:", "cyc = x; break"),
    ("si.py", "(v) par[y] = x", "par[y] = x; st.append(y)", None),
    ("si.py", "(v) walk", "x = cyc", "tau[v] = x if x != v else cyc"),
    ("si.py", "(v) walk test", "while par[x] is not v and par[x] is not None:", None),
    ("si.py", "(vi)", "            for x in R:", "tau_full[x] = tau[x]"),
    ("si.py", "improving", "def improving(self, strat, val):", "return out"),
    ("si.py", "initial best", "if kind == \"best\":", "return tuple(-1 if self.owner[v] == ODD else max(self.succ[v], key=rewcmp)"),
    ("n5x.py", "step", "def step(g, E, Ed, sigma, tau):", "return ns, nt, Is, It, fb, vs, vt"),
    ("n5x.py", "S4a guard", "if Is:", None),
    ("n5x.py", "A(v)", "opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}", "succ = [sorted(opt[v]) if g.owner[v] == 0"),
    ("n5x.py", "arena H", "succ = [sorted(opt[v]) if g.owner[v] == 0", None),
    ("n5x.py", "S4a", "Er = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ)))", "if g.owner[v] == 0: ns[v] = best[v]"),
    ("n5x.py", "S4b guard", "if It:", None),
    ("n5x.py", "arena H'", "succ = [sorted(opt[v]) if g.owner[v] == 1", None),
    ("n5x.py", "S4b", "Er = Engine(pg.Game(list(g.prio), list(g.owner), succ))", "if g.owner[v] == 1: nt[v] = best[v]"),
    ("n5x.py", "Even fallback", "for v in {v for v, _ in Is}: ns[v] = max(", None),
    ("n5x.py", "Odd fallback", "for v in {v for v, _ in It}: nt[v] = max(", None),
    ("n5x.py", "start_pair", "def start_pair(g, E, Ed, start=None):", "return sigma, tau"),
    ("n5.py", "dual", "def dual(h):", None),
    ("n5v.py", "tie (extend)", "tie = [w for w in opt[v] if Er.extend(v, vh[w]) == vh[v]]", None),
]


def lines(f):
    return subprocess.run(["git", "cat-file", "-p", BLOBS[f]], capture_output=True, text=True, check=True).stdout.split("\n")


def find(L, text, start=0):
    for i in range(start, len(L)):
        if text.startswith(" "):           # an exact line (indentation included) where the text alone is not unique
            if L[i].rstrip() == text:
                return i + 1
        elif L[i].strip().startswith(text.strip()) or text.strip() in L[i]:
            return i + 1
    raise SystemExit("anchor not found: %r" % text)


src = open("PGLemmas/Spec.lean").read()
cites = set(re.findall(r"(si\.py|n5x\.py|n5\.py|n5v\.py) l\. (\d+(?:-\d+)?)", src))
known = set()
bad = 0
print("blobs: " + ", ".join("%s %s" % (f, b[:8]) for f, b in BLOBS.items()))
for f, what, a, b in ANCHORS:
    L = lines(f)
    i = find(L, a)
    j = find(L, b, i - 1) if b else i
    rng = "%d" % i if j == i else "%d-%d" % (i, j)
    known.add((f, rng))
    found = (f, rng) in cites
    print("ANCHOR %-7s %-22s l. %-8s %s" % (f, what, rng, "FOUND" if found else "(not cited)"))
for f, rng in sorted(cites, key=lambda c: (c[0], int(c[1].split("-")[0]))):
    ok = (f, rng) in known
    bad += not ok
    print("CITE   %-7s l. %-8s %s" % (f, rng, "OK" if ok else "UNKNOWN (no anchor gives this range)"))
print("citations %d, unknown %d" % (len(cites), bad))
sys.exit(1 if bad else 0)
