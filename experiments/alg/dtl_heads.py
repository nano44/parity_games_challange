#!/usr/bin/env python3
"""L-ALG (2026-10-16, GAP-A data): per-vertex removal heads and depth-0 piece structure across searches, from a trace of the
PATCHED debug build (notes/L-ALG.md recipe: ENTER/EXIT depth markers in search_rec, `X ∪= DomStable(V)` + `domregion P top v...`
for the untraced stable-branch Dom(V,R), dtl.cpp 876-889), run with `--dtl --no-single --no-wcwc --no-loops -t -t -t`.
head_s(v) = the depth-0 event that removed v from R in search s: ('dom', top) Dom region after a stable best_vertices,
('cut', t) the -1 cut at threshold t, ('dis', top) Dom region of distraction tops (-1, nothing attracts to X).
Reports: head transitions over consecutive same-player searches; per search the depth-0 piece sequence, the first stable
piece's R and V* and their relation to the previous search's.
Usage: dtl_heads.py GAME.pg TRACE [--list]"""
import sys, re, collections
game, trace = sys.argv[1], sys.argv[2]
pr = {}
for line in open(game):
    f = line.strip().rstrip(";").split()
    if len(f) >= 4 and f[0].isdigit(): pr[int(f[0])] = int(f[1])
def vid(tok): return int(tok.split("->")[0][1:])
heads, player, meta = [], [], []
cur = None; mode = None; depth = -1; lastbest = None; unsolved = set()
for line in open(trace):
    line = line.rstrip()
    m = re.match(r"iteration \d+-(even|odd)", line)
    if m:
        cur = {}; heads.append(cur); player.append(m.group(1)); meta.append({"pieces": []}); depth = -1; continue
    if cur is None: continue
    m = re.match(r"ENTER depth (\d+)", line)
    if m: depth = int(m.group(1)); continue
    m = re.match(r"EXIT depth (\d+)", line)
    if m: depth = int(m.group(1)) - 1; continue
    m = re.match(r"current region:(.*)", line)
    if m:
        if depth == 0 and "G" not in meta[-1]: unsolved = set(vid(t) for t in m.group(1).split()); meta[-1]["G"] = frozenset(unsolved)
        continue
    if depth != 0: continue
    if line.startswith("best vertices"):
        lastbest = "stable" if line.endswith("(stable)") else "minus1"; mode = "sptl" if lastbest == "stable" else "pending"
        V = frozenset(int(t[1:]) for t in line.split()[2:] if t.startswith("v"))
        meta[-1]["pieces"].append([lastbest, V, 0])
        if lastbest == "stable" and "Rstable" not in meta[-1]:
            meta[-1]["Rstable"] = frozenset(unsolved - set(cur)); meta[-1]["Vstable"] = V; meta[-1]["before"] = len(meta[-1]["pieces"]) - 1
        continue
    if line.startswith("X ∪= DomStable"): mode = "dom"; continue
    if line.startswith("X ∪= Dom(V)"): mode = "dis"; continue
    m = re.match(r"X ∪= attracted with threshold (\d+):(.*)", line)
    if m:
        t = int(m.group(1)); vs = [vid(tok) for tok in m.group(2).split()]
        for v in vs:
            if v not in cur: cur[v] = ("cut", t, -1)
        meta[-1]["pieces"][-1][0] = "cut"; meta[-1]["pieces"][-1][2] += len(vs); mode = None; continue
    m = re.match(r"domregion (\d+) (.*)", line)
    if m and mode == "dom":
        vs = [vid(tok) for tok in m.group(2).split()]; top = vs[0]
        for v in vs:
            if v not in cur: cur[v] = ("dom", pr[top], top)
        meta[-1]["pieces"][-1][2] += len(vs); continue
    m = re.match(r"region (\d+)(.*)", line)
    if m and mode == "dis":
        vs = [vid(tok) for tok in m.group(2).split()]
        if not vs: continue
        top = max(vs, key=lambda v: (pr[v], v))
        for v in vs:
            if v not in cur: cur[v] = ("dis", pr[top], top)
        meta[-1]["pieces"][-1][0] = "dis"; meta[-1]["pieces"][-1][2] += len(vs); continue
    m = re.search(r"new tangle (\d+) \((\d+)\) \(depth 0\)", line)
    if m: meta[-1].setdefault("tangles", 0); meta[-1]["tangles"] += 1
trans = collections.Counter(); examples = collections.defaultdict(list)
for s in range(len(heads) - 1):
    if player[s] != player[s + 1]: continue
    a, b = heads[s], heads[s + 1]
    for v in a:
        if v not in b: trans[(a[v][0], "solved")] += 1; continue
        ka, la, ta = a[v]; kb, lb, tb = b[v]
        d = "up" if lb > la else "down" if lb < la else ("same" if ta == tb else "same-level")
        key = (ka, kb, d); trans[key] += 1
        if len(examples[key]) < 2: examples[key].append((s, v, a[v], b[v]))
print(f"{game}: searches {len(heads)}; head transitions over consecutive same-player searches:")
for k, c in sorted(trans.items(), key=lambda kv: -kv[1]):
    print(f"  {k}: {c}   e.g. {examples[k]}")
for s in range(len(heads)):
    R = meta[s].get("Rstable"); V = meta[s].get("Vstable"); rel = ""
    if s > 0 and player[s - 1] == player[s] and R is not None and meta[s - 1].get("Rstable") is not None:
        Rp = meta[s - 1]["Rstable"]; Vp = meta[s - 1]["Vstable"]
        rel = f"| R vs prev: {'SUPERSET' if Rp <= R else 'SUBSET' if R <= Rp else 'CROSS'} (+{len(R - Rp)} -{len(Rp - R)}); V* vs prev: {'SUPERSET' if Vp <= V else 'SUBSET' if V <= Vp else 'CROSS'} (+{len(V - Vp)} -{len(Vp - V)})"
    sig = " ".join(f"{k[:3]}{len(V)}/{n}" for k, V, n in meta[s]["pieces"])
    print(f"  search {s} {player[s]}: |G'| {len(meta[s].get('G', ()))} tangles@0 {meta[s].get('tangles', 0)} pieces[kind|V|/removed] {sig} | first stable: idx {meta[s].get('before')} |R| {len(R) if R is not None else '-'} |V*| {len(V) if V is not None else '-'} {rel}")
if "--list" in sys.argv:
    for s, h in enumerate(heads):
        print(f"search {s} ({player[s]}): " + " ".join(f"v{v}:{k}{l}" for v, (k, l, t) in sorted(h.items())))
