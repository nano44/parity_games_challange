#!/usr/bin/env python3
"""L-RED R172: runquad with ONE W-cycle node (aimed at TF-PH). Builds seg/mkr.py K m, then replaces every Odd W-loop X (an Odd vertex
with a self-loop that tau takes: C1, Cp0, T_i, Tp_i) by X -> Xhi -> Om: Xhi is a new Odd one-edge vertex whose ODD priority keeps the
loops' order and sits above every old priority; Om is one new Odd self-loop of priority 1 (all old priorities shifted up by 2).
X keeps its honest escape; tau(X) := Xhi. Intent: in G_sbar Odd still prefers the escape (its cycle z is a higher odd cycle node than
Om), in G_tau every play ends in Om, so lambda_W is constant and the loops' order lives in the top markers.
GATE=1 (default): also O (the W-sinks' old route O -> M -> z) becomes O -> {EQ, Ohi}, Ohi -> Om above every loop marker, tau(O) = Ohi
(R106's tau-stability device: EQ's other edge goes to h'). GATE=0: loops only.
Usage: mkrw.py K m OUT.pg OUT.start"""
import sys, os, re, subprocess, tempfile, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
K, m, outpg, outst = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
d = tempfile.mkdtemp(); pgp, stp = os.path.join(d, "g.pg"), os.path.join(d, "g.start")
subprocess.run([sys.executable, "-I", os.path.join(HERE, "..", "seg", "mkr.py"), K, m, pgp, stp], check=True, stdout=subprocess.DEVNULL)
rows = {}
for l in open(pgp):
    mm = re.match(r'(\d+) (\d+) ([01]) ([\d,]+) "(\S+)";', l)
    if mm: rows[int(mm.group(1))] = [int(mm.group(2)), int(mm.group(3)), list(map(int, mm.group(4).split(","))), mm.group(5)]
sig, tau = {}, {}
for l in open(stp):
    t = l.split()
    for e in t[1:]:
        v, w = map(int, e.split(":")); (sig if t[0] == "SIGMA0" else tau)[v] = w
n0 = len(rows); loops = [v for v in range(n0) if rows[v][1] == 1 and v in rows[v][2] and tau.get(v) == v]
for v in rows: rows[v][0] += 2
top = max(r[0] for r in rows.values())
om = n0; rows[om] = [1, 1, [om], "Om"]; tau[om] = om
nxt = n0 + 1; base = top + 1 + (top + 1) % 2 + 0      # first odd value above top
if base % 2 == 0: base += 1
for rank, v in enumerate(sorted(loops, key=lambda v: rows[v][0])):   # keep the loops' order: higher old loop -> higher marker
    hi = nxt; nxt += 1; rows[hi] = [base + 2 * rank, 1, [om], rows[v][3] + "hi"]; tau[hi] = om
    rows[v][2] = [hi if w == v else w for w in rows[v][2]]; tau[v] = hi
if os.environ.get("GATE", "1") == "1":   # the W-sinks' old route O -> M -> z becomes O -> {EQ, Ohi}, Ohi -> Om, tau(O) = Ohi
    ix = {r[3]: v for v, r in rows.items()}; o, eq = ix["O"], ix["EQ"]
    hi = nxt; nxt += 1; rows[hi] = [base + 2 * len(loops), 1, [om], "Ohi"]; tau[hi] = om
    rows[o][2] = [eq, hi]; tau[o] = hi
N = nxt
with open(outpg, "w") as f:
    f.write(f"parity {N - 1};\n")
    for v in range(N): f.write(f"{v} {rows[v][0]} {rows[v][1]} {','.join(map(str, rows[v][2]))} \"{rows[v][3]}\";\n")
with open(outst, "w") as f:
    f.write("SIGMA0 " + " ".join(f"{v}:{sig[v]}" for v in range(N) if rows[v][1] == 0 and v in sig) + "\n")
    f.write("TAU0 " + " ".join(f"{v}:{tau.get(v, rows[v][2][0])}" for v in range(N) if rows[v][1] == 1) + "\n")
shutil.rmtree(d, ignore_errors=True)
print(f"mkrw K {K} m {m} n {N} loops replaced {len(loops)}")
