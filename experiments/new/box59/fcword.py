#!/usr/bin/env python3
"""L-NEW box 59: exact anatomy of N5-SF on fcN (experiments/red/sf/sbev.py N --drop fc). Checks, for the distinct-sigma sequence:
 W  the sequence of sbar-flips is the word W_N = prod_{k=0}^{N-1} [h_k+, h_{k-1}-, ..., h_0-, h_0+, ..., h_{k-1}+], one flip per SBC transition
    (+ = h_i: e_i -> m_i, Odd escapes; - = back);
 C  the resets after h_k+ sit at consecutive transitions (a cascade, top down);
 P  'prepared' vs 'record': for every set event h_j+ at transition t, t_d = the first transition s >= t after which m_j is in P(Xi(d)),
    and for every i < j with h_i escaping at t, t_i = the same for P(Xi(f_i)) (inf if never before the next flip). Printed per event.
Usage: fcword.py fc_N.pg N"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import flips
path, N = sys.argv[1], int(sys.argv[2])
g, E, seq, ev = flips.run(path); lab = flips.labels(path); inv = {v: k for k, v in lab.items()}
word = []
for k in range(N):
    word += [("+", k)] + [("-", i) for i in range(k - 1, -1, -1)] + [("+", i) for i in range(k)]
got = [("+" if lab[e["b"]].startswith("m") else "-", int(lab[e["u"]][1:])) for e in ev]
js = [e["j"] for e in ev]
W = got == word and len(set(js)) == len(js)
C = True; pos = 0
for k in range(N):
    pos += 1; r = js[pos:pos + k]
    if r != list(range(r[0], r[0] + k)) if k else False: C = False
    pos += 2 * k
vals = {}
def P(j, x):
    if j not in vals: vals[j] = E.evaluate(tuple(seq[j]["s"]))[0]
    return vals[j][inv[x]][1]
rows = []
for idx, e in enumerate(ev):
    if not lab[e["b"]].startswith("m"): continue
    j = int(lab[e["u"]][1:]); t = e["j"]; nxt = ev[idx + 1]["j"] if idx + 1 < len(ev) else len(seq) - 1
    bit = E.bit[inv[f"m{j}"]]
    def first(x):
        for s in range(t, nxt + 1):
            if P(s + 1 if s + 1 < len(seq) else s, x) & bit: return s - t
        return None
    esc = [i for i in range(j) if seq[t]["sb"][inv[f"h{i}"]] == inv[f"m{i}"]]
    rows.append((j, t, first("d"), [(i, first(f"f{i}")) for i in esc]))
print(f"FCWORD N {N} n {g.n} SBC {len(set(js))} W {'PASS' if W else 'FAIL'} C {'PASS' if C else 'FAIL'}")
for r in rows: print("SET", r)
# O: which escaping lower cycles i < j OPEN (sigma leaves the cycle at e_i, f_i or g_i) between the set event h_j+ and the next flip
def closed(st, i):
    return (st["s"][inv[f"e{i}"]] == inv[f"f{i}"] and st["s"][inv[f"f{i}"]] == inv[f"g{i}"] and st["s"][inv[f"g{i}"]] == inv[f"h{i}"])
ok = True; top = -1
for idx, e in enumerate(ev):
    if not lab[e["b"]].startswith("m"): continue
    j = int(lab[e["u"]][1:]); t = e["j"]; nxt = ev[idx + 1]["j"] if idx + 1 < len(ev) else len(seq) - 1
    rec = j > top; top = max(top, j)
    esc = [i for i in range(j) if seq[t + 1]["sb"][inv[f"h{i}"]] == inv[f"m{i}"]]
    opened = sorted({i for i in esc for s in range(t + 1, nxt + 1) if not closed(seq[s], i)})
    good = (opened == esc) if rec else (opened == [])
    ok &= good
    print("OPEN", j, "record" if rec else "re-set", "escaping-below", esc, "opened", opened, "OK" if good else "BAD")
print(f"FCOPEN N {N} {'PASS' if ok else 'FAIL'} (record: every escaping lower cycle opens before the next flip; re-set: none opens)")
# L: latency at records k >= 1: s_d = first state after h_k+ whose Xi(d)-path contains l_k (d has the news); s_z = first state with
# sigma(z_{k-1}) = v_{k-1} (the escape chain of the top lower bit has it); at s_d we print whether (z_{k-1}, v_{k-1}) is improving.
for idx, e in enumerate(ev):
    if not lab[e["b"]].startswith("m"): continue
    k = int(lab[e["u"]][1:]); t = e["j"]
    if k == 0 or any(int(lab[x["u"]][1:]) >= k for x in ev[:idx] if lab[x["b"]].startswith("m")): continue
    if k == N - 1: zv = None
    sd = next(s for s in range(t + 1, len(seq)) if P(s, "d") & E.bit[inv[f"l{k}"]])
    sz = next((s for s in range(t + 1, len(seq)) if seq[s]["s"][inv[f"z{k-1}"]] == inv.get(f"v{k-1}")), None)
    vs, _ = E.evaluate(tuple(seq[sd]["s"])); Is = set(E.improving(tuple(seq[sd]["s"]), vs))
    print("LAT", k, "set at", t, "d-has-l_k at", sd, "z_{k-1}->v_{k-1} at", sz, "improving at s_d:", (inv[f"z{k-1}"], inv[f"v{k-1}"]) in Is)
latok = True
for idx, e in enumerate(ev):
    if not lab[e["b"]].startswith("m"): continue
    k = int(lab[e["u"]][1:]); t = e["j"]
    if k == 0 or any(int(lab[x["u"]][1:]) >= k for x in ev[:idx] if lab[x["b"]].startswith("m")): continue
    so = next(s for s in range(t + 1, len(seq)) if not closed(seq[s], k - 1))
    vs, _ = E.evaluate(tuple(seq[so - 1]["s"])); Is = set(E.improving(tuple(seq[so - 1]["s"]), vs))
    print("LAT2", k, "cycle k-1 opens at state", so, "; at state", so - 1, "Xi(f_{k-1}) has m_k:", bool(P(so - 1, f"f{k-1}") & E.bit[inv[f"m{k}"]]),
          "Xi(lane a0) has m_k:", bool(P(so - 1, "a0") & E.bit[inv[f"m{k}"]]), "Xi(d) has m_k:", bool(P(so - 1, "d") & E.bit[inv[f"m{k}"]]),
          "(z,v) improving:", (inv[f"z{k-1}"], inv[f"v{k-1}"]) in Is, "(v,r_k) improving:", (inv[f"v{k-1}"], inv[f"r{k}"]) in Is if f"v{k-1}" in inv else None)
    latok &= (not P(so - 1, f"f{k-1}") & E.bit[inv[f"m{k}"]]) and bool(P(so - 1, "a0") & E.bit[inv[f"m{k}"]]) and (inv[f"z{k-1}"], inv[f"v{k-1}"]) not in Is
print(f"FCLAT N {N} {'PASS' if latok else 'FAIL'} (at every record k >= 1, the state before cycle k-1 opens: lane a0 has m_k, f_(k-1) has not, (z_(k-1), v_(k-1)) not improving)")
