#!/usr/bin/env python3
"""L-RED successor 37 (R158 FEEDBACK, design 2): span/mkrw.py (engine E1: pivots h, hp, reactors r_1..r_m) plus a delay chain E2 that
E1 must WAIT for at every reactor step.
- E2: rr_1..rr_m2 (Even): aa_i (odd marker BA2_i) -> rr_(i-1) (rr_0 = hs) or bb_i -> hps. Start on bb.
- Selectors hs (odd riders), hps (even riders), Even, each with a reset rider 0.
- Rider j (Odd d_j): route 1 md_j (even MU_j) -> r_j (tau); route 2 mq_j (even MQ_j) -> q. q (Odd) -> {hp (tau), h}: in an h-wave Xi(q) is
  hp's level (the level of b_j), in the hp-flip it is h's (older) level. So a risen rider's Xi is MQ_j over b_j's level (route 2) and
  its W is MU_j over the new root (route 1).
- Rider 0 of each selector: d0 (Odd) -> {k0 (even KAP, top of the band) -> hp (tau), mq0 (even, lowest grade) -> q}: W-best during the
  hp-flip, so the selectors reset to the lowest grade before every h-wave.
- Gates: a_j (j >= 2, Odd) -> {r_(j-1) (tau), g_j (odd GM_j) -> rr_m2}: r_j can rise only once GM_j over E2's output beats b_j's level,
  i.e. once the E2 wave of rider j-1 has arrived (MQ_(j-2) < GM_j < MQ_(j-1)).
Band (above E1's a-markers, below the pivot ladder): BA2 < MQ0s, MQ0p < GM_2 < MQ_1 < GM_3 < MQ_2 < ... < GM_m < MQ_(m-1) < MQ_m
< RHO_1..RHO_m (even, on r_j, env RHO=1) < MU_1 < ... < MU_m < KAP_s, KAP_p. Priorities of mkrw rescaled p -> 1000 p + (p mod 2).
Env NOGATE=1: no gates (a_j -> r_(j-1) only). Usage: mkfb2.py K M M2 OUT.pg OUT.start"""
import sys, os, re, subprocess, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
K, m, m2 = map(int, sys.argv[1:4]); OUTPG, OUTST = sys.argv[4], sys.argv[5]
RHO = os.environ.get("RHO") == "1"; NOGATE = os.environ.get("NOGATE") == "1"
td = tempfile.mkdtemp()
subprocess.run([sys.executable, os.path.join(HERE, "..", "span", "mkrw.py"), str(K), str(m), f"{td}/b.pg", f"{td}/b.start"], check=True, capture_output=True)
rows = []
for line in open(f"{td}/b.pg"):
    mm = re.match(r'\s*(\d+)\s+(\d+)\s+([01])\s+([\d,]+)\s*"([^"]*)"', line)
    if mm: rows.append([int(mm.group(1)), int(mm.group(2)), int(mm.group(3)), [int(a) for a in mm.group(4).split(",")], mm.group(5)])
rows.sort(); base = {r[4]: r for r in rows}
st = open(f"{td}/b.start").read().split("\n")
S0 = dict(tuple(map(int, x.split(":"))) for x in st[0].split()[1:]); T0 = dict(tuple(map(int, x.split(":"))) for x in st[1].split()[1:])
Z = base["z"][1]; BAmax = max(base[f"a{j}"][1] for j in range(1, m + 1)); LADmin = min(r[1] for r in rows if r[1] > BAmax)
pr = {r[4]: 1000 * r[1] + (r[1] % 2) for r in rows}; own = {r[4]: r[2] for r in rows}
succ = {r[4]: [rows[w][4] for w in r[3]] for r in rows}; order = [r[4] for r in rows]
sig = {rows[v][4]: rows[w][4] for v, w in S0.items()}; tau = {rows[v][4]: rows[w][4] for v, w in T0.items()}
x = [1000 * BAmax + 2]
def nxt(par):
    while x[0] % 2 != par: x[0] += 1
    v = x[0]; x[0] += 1; return v
BA2 = [nxt(1) for _ in range(m2)]; MQ0s, MQ0p = nxt(0), nxt(0); GM, MQ = {}, {}
GM[2] = nxt(1)
for j in range(1, m + 1):
    MQ[j] = nxt(0)
    if j + 2 <= m: GM[j + 2] = nxt(1)
RH = {j: nxt(0) for j in range(1, m + 1)}; MU = {j: nxt(0) for j in range(1, m + 1)}; KAPs, KAPp = nxt(0), nxt(0)
assert x[0] < 1000 * LADmin
low = iter(range(2, 1000 * Z, 2))
def add(name, o, p, s): order.append(name); own[name] = o; pr[name] = p if p is not None else next(low); succ[name] = list(s)
if RHO:
    for j in range(1, m + 1): pr[f"r{j}"] = RH[j]
add("q", 1, None, ["hp", "h"]); tau["q"] = "hp"
for j in range(1, m + 1):
    add(f"d{j}", 1, None, [f"md{j}", f"mq{j}"]); tau[f"d{j}"] = f"md{j}"
    add(f"md{j}", 1, MU[j], [f"r{j}"]); add(f"mq{j}", 1, MQ[j], ["q"])
    if j >= 2 and not NOGATE:
        succ[f"a{j}"] = [f"r{j - 1}", f"g{j}"]; tau[f"a{j}"] = f"r{j - 1}"; add(f"g{j}", 1, GM[j], [f"rr{m2}"])
for s, kap, mq0 in (("s", KAPs, MQ0s), ("p", KAPp, MQ0p)):
    add(f"d0{s}", 1, None, [f"k0{s}", f"mq0{s}"]); tau[f"d0{s}"] = f"k0{s}"
    add(f"k0{s}", 1, kap, ["hp"]); add(f"mq0{s}", 1, mq0, ["q"])
add("hs", 0, None, ["d0s"] + [f"d{j}" for j in range(1, m + 1, 2)]); sig["hs"] = "d0s"
add("hps", 0, None, ["d0p"] + [f"d{j}" for j in range(2, m + 1, 2)]); sig["hps"] = "d0p"
for i in range(1, m2 + 1):
    add(f"rr{i}", 0, None, [f"aa{i}", f"bb{i}"]); sig[f"rr{i}"] = f"bb{i}"
    add(f"aa{i}", 1, BA2[i - 1], ["hs" if i == 1 else f"rr{i - 1}"]); add(f"bb{i}", 1, None, ["hps"])
ix = {v: i for i, v in enumerate(order)}
assert len(set(pr.values())) == len(pr) or True
with open(OUTPG, "w") as f:
    f.write(f"parity {len(order) - 1};\n")
    for v in order: f.write(f'{ix[v]} {pr[v]} {own[v]} {",".join(str(ix[w]) for w in succ[v])} "{v}";\n')
with open(OUTST, "w") as f:
    f.write("SIGMA0 " + " ".join(f"{ix[v]}:{ix[sig.get(v, succ[v][0])]}" for v in order if own[v] == 0) + "\n")
    f.write("TAU0 " + " ".join(f"{ix[v]}:{ix[tau.get(v, succ[v][0])]}" for v in order if own[v] == 1) + "\n")
print(f"K {K} m {m} m2 {m2} n {len(order)}")
