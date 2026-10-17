#!/usr/bin/env python3
"""L-RED CARRY box (produced on Opus 5.5): WHERE are the drivers of depth-0 transitions learned? (driver LOCALITY)
For consecutive same-player searches s, s+1 with no dominion found in s, the transition level j is the first depth-0 piece
whose (context R, kind, result set V) differs. A driver is a tangle learned in s that fires in piece j's computation in
s+1 (pruning, sptl, Dom or cut attractor). L-ALG's driver lemma: drivers are learned at a depth-0 piece k >= j or inside a
cut recursion of such a piece. Locality conjecture (R10 (F), generalised): every driver is learned in the FIRST stable
depth-0 piece after piece j in s, or inside piece j's own cut recursion. This script reports, per transition, where each
driver was learned: 'next-stable' (first stable depth-0 piece after j), 'rec-j' (inside piece j's recursion), 'same-j'
(at piece j itself), or 'later' (a later depth-0 piece, or the recursion of a later piece). 'later' events refute locality.
Usage: drivers.py GAME.pg ... | --random N NMAX SEED"""
import sys, os, importlib.util, random, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ff", os.path.join(HERE, "..", "dtl", "dtl_flipflop.py"))
ff = importlib.util.module_from_spec(spec); spec.loader.exec_module(ff)


def analyse(d):
    out = []
    for s in d.searches:
        s["d0"] = [i for i, p in enumerate(s["pieces"]) if p["depth"] == 0]
    born = {}
    for s in d.searches:
        for top, vs, pi in s["tangles"]:
            born[frozenset(vs) | {("top", top)}] = (s["index"], pi)
    tid_born = {}
    # tangle ids in creation order = order of s["tangles"] over searches
    k = 0
    for s in d.searches:
        for top, vs, pi in s["tangles"]:
            tid_born[k] = (s["index"], pi); k += 1
    ss = d.searches
    for a, b in zip(ss, ss[1:]):
        if a["player"] != b["player"] or a["dominions"] or a["G"] != b["G"]: continue
        da, db = a["d0"], b["d0"]; j = None
        for x in range(min(len(da), len(db))):
            pa, pb = a["pieces"][da[x]], b["pieces"][db[x]]
            if (pa["bv"]["R"], pa["kind"], pa.get("V")) != (pb["bv"]["R"], pb["kind"], pb.get("V")) or pa.get("removed") != pb.get("removed"):
                j = x; break
        if j is None: continue
        pj = db[j]; nxt = db[j + 1] if j + 1 < len(db) else len(b["pieces"])
        fired = {}
        for t, ln, ph in b["fired"]:
            idx = ln if ph == "prune" else ln - 1
            if pj <= idx < nxt: fired.setdefault(t, set()).add(ph if idx == pj else "rec")
        drivers = [t for t in fired if t in tid_born and tid_born[t][0] == a["index"]]
        # (F) proper: the FIRST new tangle (of search s) that fires in the CUT attractor of piece j in s+1
        cutfire = [t for t, ln, ph in b["fired"] if ph == "cut" and ln - 1 == pj and t in tid_born and tid_born[t][0] == a["index"]]
        if cutfire:
            t0 = cutfire[0]; _, bp0 = tid_born[t0]
            aj = da[j] if j < len(da) else None
            ajn = da[j + 1] if j + 1 < len(da) else len(a["pieces"])
            first_stable = next((da[x] for x in range(j + 1, len(da)) if a["pieces"][da[x]]["kind"] == "stable"), None)
            c0 = "rec-j" if (aj is not None and aj < bp0 < ajn) else "next-stable" if bp0 == first_stable else "later"
            out.append(dict(s=a["index"], level=j, t=t0, born_piece=bp0, cls="F:" + c0, kind_j="cut-first", phases="cut"))
        for t in drivers:
            _, bp = tid_born[t]
            # classify bp relative to a's depth-0 pieces
            aj = da[j] if j < len(da) else None
            ajn = da[j + 1] if j + 1 < len(da) else len(a["pieces"])
            first_stable = next((da[x] for x in range(j + 1, len(da)) if a["pieces"][da[x]]["kind"] == "stable"), None)
            if aj is not None and aj < bp < ajn and a["pieces"][bp]["depth"] > 0: cls = "rec-j"
            elif bp == aj: cls = "same-j"
            elif first_stable is not None and bp == first_stable: cls = "next-stable"
            else: cls = "later"
            out.append(dict(s=a["index"], level=j, t=t, born_piece=bp, cls=cls, kind_j=a["pieces"][aj]["kind"] if aj is not None else None,
                            phases="+".join(sorted(fired[t]))))
    return out


def write_random(path, n, rng):
    with open(path, "w") as f:
        f.write(f"parity {n-1};\n")
        for v in range(n):
            succ = sorted({rng.randrange(n)} | {rng.randrange(n) for _ in range(rng.randrange(3))})
            f.write(f"{v} {rng.randrange(n+1)} {rng.randrange(2)} {','.join(map(str, succ))};\n")


if __name__ == "__main__":
    if sys.argv[1] == "--random":
        N, nmax, seed = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); rng = random.Random(seed); files = []
        for i in range(N):
            p = tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False).name; write_random(p, rng.randint(4, nmax), rng); files.append(p)
    else:
        files = sys.argv[1:]
    tot = {}; shown = 0; trans = 0
    for f in files:
        d = ff.load(f, "oink")
        ev = analyse(d)
        for e in ev:
            key = (e["kind_j"], e["phases"], e["cls"]); tot[key] = tot.get(key, 0) + 1
            if e["cls"] == "later" and shown < 10:
                shown += 1; print(f"LATER {os.path.basename(f)}: search {e['s']} level {e['level']} (piece kind {e['kind_j']}, fires in {e['phases']}) driver t{e['t']} learned at piece {e['born_piece']}")
        if sys.argv[1] == "--random": os.unlink(f)
    print(f"games {len(files)}; drivers by (kind of piece j, phase of firing there, learning place):")
    for k in sorted(tot, key=str): print("   ", k, tot[k])
