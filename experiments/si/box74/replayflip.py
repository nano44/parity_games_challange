#!/usr/bin/env python3
"""L-SI box 74: replay a flip witness (genome JSON with "flip_witness") with L-NEW's box 150 Gen (read-only copy in box64/ref): the
flip-free b-run from the start, then F = number of steps at which ord(A_m, B_m) = [key(A_m) < key(B_m)] changes (R104 keys, written out
here from the definition). Exit 1 if F or T differ from the stored witness. Usage: replayflip.py genome.json"""
import sys, json, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box64")); from flipdp import Ext
f = os.path.join(HERE, "..", "box64", "ref", "box150", "check.py")
ns = {"__file__": f}; exec(open(f).read().split("\nif __name__")[0], ns); Gen, restrict = ns["Gen"], ns["restrict"]
G = json.load(open(sys.argv[1])); W = G["flip_witness"]; E = Ext(G); m = max(G["lev"])
def gstep(u, b):
    sa = E.full(u, b); H = restrict(G, E.L0, sa); S, _ = Gen(H).run(H["start"])
    return tuple(S[1][v] for v in E.UP) if len(S) > 1 else u
def key(st, x):
    k = st[x]; wt = G["opts"][x][k][0]; return (G["gate"][x][k],) if wt < 0 else key(st, wt) + (G["gate"][x][k],)
u = tuple(W["start_up"]); b = W["bit"]; seq = [u]; bits = W.get("bits") or None
if bits:                                         # K-flip witness: step t uses bits[t]; ord(s_t) is read with the bit of the step making s_t
    for nb in bits:
        n = gstep(seq[-1], nb); assert n != seq[-1], "a scheduled step does not move"; seq.append(n)
    assert sum(1 for i, x in enumerate(bits) if x != ([b] + bits)[i]) <= W["K"], "too many bit changes"
    rb = [b] + bits
else:
    while len(seq) < 200:
        n = gstep(seq[-1], b)
        if n == seq[-1]: break
        seq.append(n)
    rb = [b] * len(seq)
o = []
for x, bb in zip(seq, rb):
    st = E.full(x, bb); o.append(key(st, 2 * m) < key(st, 2 * m + 1))
F = sum(1 for i in range(len(o) - 1) if o[i] != o[i + 1])
print("T", len(seq) - 1, "F", F, "stored", W["T"], W["F"], "ord", "".join(str(int(x)) for x in o))
sys.exit(0 if (F, len(seq) - 1) == (W["F"], W["T"]) else 1)
