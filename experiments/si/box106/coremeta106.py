#!/usr/bin/env python3
"""L-SI box 106 §3d: the committed core set with provenance (Lead 05:57Z): out/cores106.json, a list of
{"i": index in out/cores106_L<LEN>.json, "lits": [[state, mover, bit], ...], "source": "found" | "image", "of": index of the found core
it is an image of (images only), "g": the relabelling as a list of [[x, k], [x', k']] pairs (images only), "proof": {sha1, lemmas} once
certified (merged from out/certcore106.out lines «CERTCORE106 core<i> … proof lines N sha1 S» checked VERIFIED by both checkers)}.
A found core is one printed in out/core106_L<LEN>.out (its literals in the line); every other entry must be an image of a found core under
core106.GROUP (asserted). Usage: coremeta106.py LEN"""
import sys, os, json, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import core106 as K

def parse_lits(txt):
    out = []
    for t in txt.split():
        m = re.match(r"(¬?)AV\[([01]{4})\]\[(\d)\]$", t); assert m, t
        out.append(([int(c) for c in m.group(2)], int(m.group(3)), 0 if m.group(1) else 1))
    return sorted(out)

def key(c): return json.dumps(sorted([list(S), x, b] for S, x, b in c))

def main():
    LEN = int(sys.argv[1]); cores = json.load(open(os.path.join(HERE, "out/cores106_L%d.json" % LEN)))
    found = []
    for l in open(os.path.join(HERE, "out/core106_L%d.out" % LEN)):
        m = re.match(r"CORE106 L\* >= \d+ core \d+(?: \(\+\d+ images\))?: (.*?) \| from run", l)
        if m: found.append(parse_lits(m.group(1)))
    idx = {key(c): i for i, c in enumerate(cores)}
    meta = [None] * len(cores)
    for f in found:
        assert key(f) in idx, f
        meta[idx[key(f)]] = {"i": idx[key(f)], "lits": [[S, x, b] for S, x, b in f], "source": "found"}
    for f in found:
        fi = idx[key(f)]
        for g in K.GROUP:
            im = K.image([tuple(t) for t in f], g); i = idx.get(key(im))
            if i is not None and meta[i] is None:
                meta[i] = {"i": i, "lits": [list(t) for t in im], "source": "image", "of": fi, "g": sorted([list(a), list(b)] for a, b in g.items())}
    missing = [i for i, m in enumerate(meta) if m is None]
    assert not missing, ("entries that are neither found nor an image of a found core", missing[:5])
    cert = {}
    cf = os.path.join(HERE, "out/certcore106.out")
    if os.path.exists(cf):
        lines = open(cf).read().splitlines()
        for l in lines:
            m = re.match(r"CERTCORE106 (core(\d+)) .*: UNSAT \| .* proof lines (\d+) sha1 ([0-9a-f]{40})$", l)
            if m and sum(1 for x in lines if x.startswith("CHECK106 %s " % m.group(1)) and "s VERIFIED" in x) == 2:
                cert[int(m.group(2))] = {"proof_lines": int(m.group(3)), "sha1": m.group(4)}
    for m in meta:
        if m["i"] in cert: m["proof"] = cert[m["i"]]
    json.dump(meta, open(os.path.join(HERE, "out/cores106.json"), "w"), indent=0)
    print("COREMETA106 L* >= %d: %d cores (%d found, %d images), %d certified" % (LEN, len(meta), sum(m["source"] == "found" for m in meta),
          sum(m["source"] == "image" for m in meta), len(cert)))

if __name__ == "__main__":
    main()
