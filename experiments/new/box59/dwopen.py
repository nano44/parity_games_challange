#!/usr/bin/env python3
"""L-NEW box 62: on dwN, check (1) the sbar-flip word is the N-bit binary counter (each increment: set the lowest 0 bit k, then reset
k-1..0 top down); (2) LATENCY at EVERY set of a bit k >= 1 (not only records): every escaping lower cycle opens before the next flip,
and at the state before cycle k-1 opens, the lane a0 carries m_k while f_(k-1) does not. Usage: dwopen.py dw_N.pg N"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import flips
path, N = sys.argv[1], int(sys.argv[2])
g, E, seq, ev = flips.run(path); lab = flips.labels(path); inv = {v: k for k, v in lab.items()}
got = [("+" if lab[e["b"]].startswith("m") else "-", int(lab[e["u"]][1:])) for e in ev]
word = []
for c in range(1, 2 ** N):
    k = (c & -c).bit_length() - 1
    word += [("+", k)] + [("-", i) for i in range(k - 1, -1, -1)]
W = got == word
def closed(st, i): return st["s"][inv[f"e{i}"]] == inv[f"f{i}"] and st["s"][inv[f"f{i}"]] == inv[f"g{i}"] and st["s"][inv[f"g{i}"]] == inv[f"h{i}"]
P = lambda j, x: E.evaluate(tuple(seq[j]["s"]))[0][inv[x]][1]
ok = True; nsets = 0
for idx, e in enumerate(ev):
    if not lab[e["b"]].startswith("m"): continue
    k = int(lab[e["u"]][1:]); t = e["j"]; nxt = ev[idx + 1]["j"] if idx + 1 < len(ev) else len(seq) - 1
    if k == 0: continue
    nsets += 1
    esc = [i for i in range(k) if seq[t + 1]["sb"][inv[f"h{i}"]] == inv[f"m{i}"]]
    opened = sorted({i for i in esc for s in range(t + 1, nxt + 1) if not closed(seq[s], i)})
    so = next(s for s in range(t + 1, len(seq)) if not closed(seq[s], k - 1))
    bit = E.bit[inv[f"m{k}"]]
    lat = bool(P(so - 1, "a0") & bit) and not (P(so - 1, f"f{k-1}") & bit)
    ok &= (opened == esc) and lat
print(f"DWOPEN N {N} word {'BINARY' if W else 'OTHER'} sets_k>=1 {nsets} every-set-opens-and-lane-first {'PASS' if ok else 'FAIL'} SBC {len({e['j'] for e in ev})}")
