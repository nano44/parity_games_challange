#!/usr/bin/env python3
"""L-RED (produced on Opus 5.5): attack on L-ALG's Phi_idx (Lead 10:37Z), on the pinned A_DTL (this lane's tracer, exact vs
Oink; ACTUAL pruning, deficits included). Per phase and depth-0 piece INDEX i: R_i(u) = maximum death round of u in piece
i's pruning over the phase's searches so far in which piece i returned -1 (a stable result counts as infinity for its
survivors). Event: consecutive same-player searches s, s+1 (no dominion in s) whose first differing depth-0 piece is i,
with an equal context and piece i a -1 piece in s. The event RAISES the record if some vertex dies later at piece i in
s+1 than its record before s+1. Reports events that raise nothing ('flat'). Phi_idx claims that every change caused by
dead-top cap carries raises a record; a flat change is a candidate counterexample, whose drivers are then classified by hand.
Usage: phi_idx.py GAME.pg ... | --random N NMAX SEED"""
import sys, os, importlib.util, random, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ff", os.path.join(HERE, "..", "dtl", "dtl_flipflop.py"))
ff = importlib.util.module_from_spec(spec); spec.loader.exec_module(ff)
INF = 10 ** 9


def deaths(piece):
    bv = piece["bv"]; out = {}
    for r, rd in enumerate(bv["rounds"]):
        for v in rd["distractions"]: out[v] = r + 1
    if bv.get("result") == 1:
        for v in bv["V"]: out[v] = INF
    return out


def analyse(d):
    ev = []; rec = {}; prev = None
    for sr in d.searches:
        d0 = [p for p in sr["pieces"] if p["depth"] == 0]
        if prev is not None and (prev["player"] != sr["player"] or prev["dominions"] or prev["G"] != sr["G"]):
            rec = {}
        elif prev is not None:
            pa = [p for p in prev["pieces"] if p["depth"] == 0]
            j = 0
            while j < min(len(pa), len(d0)) and (pa[j]["bv"]["R"], pa[j]["kind"], pa[j].get("V")) == (d0[j]["bv"]["R"], d0[j]["kind"], d0[j].get("V")):
                j += 1
            if j < min(len(pa), len(d0)) and pa[j]["bv"]["R"] == d0[j]["bv"]["R"] and pa[j]["kind"] != "stable":
                before = rec.get(j, {})
                dn = deaths(d0[j])
                raised = [u for u, r in dn.items() if r > before.get(u, 0)]
                if not raised:
                    ev.append(dict(s=prev["index"], i=j, kind=(pa[j]["kind"], d0[j]["kind"]), V=(pa[j].get("V"), d0[j].get("V"))))
        for j, p in enumerate(d0):
            if p["kind"] != "stable":           # records come from -1 results only (a new stable result counts as infinity)
                r = rec.setdefault(j, {})
                for u, x in deaths(p).items(): r[u] = max(r.get(u, 0), x)
        prev = sr
    return ev


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
    tot = 0; flat = 0; shown = 0
    for f in files:
        d = ff.load(f, "oink")
        e = analyse(d)
        flat += len(e)
        for x in e:
            if shown < 12:
                shown += 1
                L = lambda s: sorted(d.idx[v] for v in s) if s else s
                print(f"FLAT {os.path.basename(f)}: search {x['s']}->{x['s']+1} piece {x['i']} kinds {x['kind']} V {L(x['V'][0])} -> {L(x['V'][1])}")
        if sys.argv[1] == "--random": os.unlink(f)
    print(f"games {len(files)}; flat changes (no record raised at that piece index): {flat}")
