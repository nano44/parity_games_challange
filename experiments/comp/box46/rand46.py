#!/usr/bin/env python3
"""L-COMP box 46 item (2): win46.measure on random Ξ-CYCLIC genomes by this lane's law (box43/rand43.rgen: N + M <= NMMAX, Ξ-target X
with probability PX, else a uniform mover), drawn until COUNT genomes with a Ξ-cycle (the graph x -> Ξ-target(x) has a cycle) are found;
the acyclic draws are skipped and counted. One line per genome appended to OUT; resumable (the generator is replayed, finished names
skipped). With --acyclic the Ξ-ACYCLIC draws are kept instead (names arand_...).
Usage: rand46.py SEED COUNT NMMAX PX OUT [--write DIR] [--acyclic]   (env W46_CTRL / LV46_CTRL as win46)"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "box43")]
import win46, rand43


def xcyclic(G):
    N = G["N"]; adj = [{o[1] for o in G["opts"][x] if o[1] >= 0} for x in range(N)]; col = [0] * N
    for s in range(N):
        if col[s]: continue
        st = [(s, iter(adj[s]))]; col[s] = 1
        while st:
            v, it = st[-1]; w = next(it, None)
            if w is None: col[v] = 2; st.pop(); continue
            if col[w] == 1: return True
            if col[w] == 0: col[w] = 1; st.append((w, iter(adj[w])))
    return False


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]; seed, cnt, nm, px, out = int(a[0]), int(a[1]), int(a[2]), float(a[3]), a[4]
    wdir = sys.argv[sys.argv.index("--write") + 1] if "--write" in sys.argv else None; ACYC = "--acyclic" in sys.argv
    have = {l.split()[0] for l in open(out)} if os.path.exists(out) else set(); r = random.Random(seed); found = skipped = 0
    while found < cnt:
        G = rand43.rgen(r, nm, px)
        if xcyclic(G) == ACYC: skipped += 1; continue
        name = "%srand_s%d_nm%d_px%s_%d" % ("a" if ACYC else "x", seed, nm, a[3], found); found += 1
        if wdir: json.dump(G, open(os.path.join(wdir, name + ".json"), "w"), sort_keys=True)
        if name in have: continue
        try:
            c, d, first, B = win46.measure(G); l = win46.line(name, c, d, B)
        except Exception as e: l = "%s ERROR %s %s" % (name, type(e).__name__, e)
        with open(out, "a") as f: f.write(l + " | acyclic draws skipped so far %d\n" % skipped)
