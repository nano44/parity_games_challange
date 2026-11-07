#!/usr/bin/env python3
"""L-RED successor 39 (R167): a SELF-REFERENTIAL level-2 gate, built by design (no search).
Base: span/mkrw.py K 2 (pivot ladder h / hp, E1 reactors r_1, r_2) with fbg's level-1 binding gate a_2 -> {r_1 (tau), g_2 -> rr_m2}.
Level 2 (E2): rr_i (Even) -> {aa_i, bb_i}; aa_1 (Odd, BA2_1) -> hs; aa_i (i >= 2, Odd, BA2_i) -> {rr_(i-1) (tau), gg_i (GM2_i) -> rrr_m3};
  bb_i -> hps. hs (Even) -> d_1 -> md_1 (MU_1) -> r_1; hps (Even) -> d_2 -> md_2 (MU_2) -> r_2; b_j -> be_j -> hp.
Level 3 (E3): rrr_t (Even) -> {aaa_t (BA3_t) -> rrr_(t-1) (rrr_0 = hs2), bbb_t -> hps2}.
E3 drivers: hs2 (Even) -> {dd_i : i odd}, hps2 (Even) -> {dd_i : i even}. NEW: the rider dd_i is Odd and carries MU2_i itself:
  dd_i (MU2_i) -> {rr_i (tau), x_i (X) -> hps}.
  In W (tau) the rider reads rr_i (the E2 front: H-level once risen). In Xi, Odd escapes to hps, the SAME vertex that E2's comparison
  side bb_(k+1) -> hps reads. So the E2 gate test Xi(aa_(k+1)) vs Xi(bb_(k+1)) is self-referential: both sides end in Xi(hps), and only
  band markers decide (R159's level match, one level down). The ladder (H vs P) still decides every W choice.
Band order (ascending, between E1's a-markers and the ladder), default design D1:
  BA3_t (odd) < BA2_i (odd) < X (even) < MU_1 < MU_2 (even) < GM_2 (odd) < GM2_2 < MU2_1 < GM2_3 < MU2_2 < ... < GM2_m2 < MU2_(m2-1) < MU2_m2
  (GM2_(k+1) odd between MU2_(k-1) and MU2_k: closed while E3 reads hps2's older rider, open once E3 reaches hs2's newer rider).
Env DESIGN=<name> picks a variant (see VARIANTS). Usage: mk167.py K m2 m3 OUT.pg OUT.start"""
import sys, os, re, subprocess, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
def build(K, m2, m3, design="D1"):
    td = tempfile.mkdtemp()
    subprocess.run([sys.executable, os.path.join(HERE, "..", "span", "mkrw.py"), str(K), "2", f"{td}/b.pg", f"{td}/b.start"], check=True, capture_output=True)
    rows = []
    for line in open(f"{td}/b.pg"):
        mm = re.match(r'\s*(\d+)\s+(\d+)\s+([01])\s+([\d,]+)\s*"([^"]*)"', line)
        if mm: rows.append([int(mm.group(1)), int(mm.group(2)), int(mm.group(3)), [int(a) for a in mm.group(4).split(",")], mm.group(5)])
    rows.sort()
    st = open(f"{td}/b.start").read().split("\n")
    S0 = dict(tuple(map(int, x.split(":"))) for x in st[0].split()[1:]); T0 = dict(tuple(map(int, x.split(":"))) for x in st[1].split()[1:])
    base = {r[4]: r for r in rows}
    Z = base["z"][1]; BAmax = max(base[f"a{j}"][1] for j in (1, 2)); LADmin = min(r[1] for r in rows if r[1] > BAmax)
    order = [r[4] for r in rows]; pr = {r[4]: 1000 * r[1] + (r[1] % 2) for r in rows}; own = {r[4]: r[2] for r in rows}
    succ = {r[4]: [rows[w][4] for w in r[3]] for r in rows}
    sig = {rows[v][4]: rows[w][4] for v, w in S0.items()}; tau = {rows[v][4]: rows[w][4] for v, w in T0.items()}
    # band: list of (marker, parity) ascending
    band = [(f"BA3_{t}", 1) for t in range(1, m3 + 1)] + [(f"BA2_{i}", 1) for i in range(1, m2 + 1)]
    band += [(f"X{i}", 0) for i in range(1, m2 + 1)] + [("MU_1", 0), ("MU_2", 0), ("GM_2", 1), ("MU2_0", 0), ("GM2_2", 1)]
    for k in range(1, m2 + 1):
        band.append((f"MU2_{k}", 0))
        if k + 2 <= m2: band.append((f"GM2_{k + 2}", 1))
    if design == "D0":                     # control: no rider escape markers are used (x_i absent), MU2 on mdd (fb3 shape)
        pass
    P = {}; x = 0
    lo, hi = 1000 * BAmax + 2, 1000 * LADmin - 2           # priorities scaled by 1000 (parity kept), as fbsearch.py
    assert hi - lo > 2 * len(band) + 4, (lo, hi, len(band))
    for name, par in band:
        x = max(x, lo) if x == 0 else x
        while x % 2 != par: x += 1
        P[name] = x; x += 1
    low = iter(range(2, 1000 * Z, 1))
    used = set(pr.values()) | set(P.values())
    def nxt():
        v = next(low)
        while v in used: v = next(low)
        used.add(v); return v
    def add(name, o, p, s): order.append(name); own[name] = o; pr[name] = p; succ[name] = list(s)
    for j in (1, 2):
        add(f"d{j}", 1, nxt(), [f"md{j}"]); add(f"md{j}", 1, P[f"MU_{j}"], [f"r{j}"])
        add(f"be{j}", 1, nxt(), ["hp"]); succ[f"b{j}"] = [f"be{j}"]; tau[f"b{j}"] = f"be{j}"
    succ["a2"] = ["r1", "g2"]; tau["a2"] = "r1"; add("g2", 1, P["GM_2"], [f"rr{m2}"])
    add("hs", 0, nxt(), ["d1"]); add("hps", 0, nxt(), ["d2"])
    for i in range(1, m2 + 1):
        add(f"rr{i}", 0, nxt(), [f"aa{i}", f"bb{i}"]); sig[f"rr{i}"] = f"bb{i}"
        if i == 1: add("aa1", 1, P["BA2_1"], ["hs"])
        else: add(f"aa{i}", 1, P[f"BA2_{i}"], [f"rr{i - 1}", f"gg{i}"]); tau[f"aa{i}"] = f"rr{i - 1}"; add(f"gg{i}", 1, P[f"GM2_{i}"], [f"rrr{m3}"])
        add(f"bb{i}", 1, nxt(), ["hps"])
    for i in range(1, m2 + 1):
        if design == "D0":
            add(f"dd{i}", 1, nxt(), [f"mdd{i}"]); add(f"mdd{i}", 1, P[f"MU2_{i}"], [f"rr{i}"])
        else:
            add(f"dd{i}", 1, P[f"MU2_{i}"], [f"rr{i}", f"x{i}"]); tau[f"dd{i}"] = f"rr{i}"; add(f"x{i}", 1, P[f"X{i}"], ["hps"])
    add("dd0", 1, P["MU2_0"], ["hps"])                      # hps2's lowest rider (a floor below MU2_1; reads hps directly)
    o2 = [f"dd{i}" for i in range(1, m2 + 1, 2)]; e2 = ["dd0"] + [f"dd{i}" for i in range(2, m2 + 1, 2)]
    add("hs2", 0, nxt(), o2); add("hps2", 0, nxt(), e2)
    lowstart = os.environ.get("START_LOW") == "1"            # drivers start on their LOWEST rider (dd_1 / dd_2) instead of the top
    sig["hs2"] = o2[0] if lowstart else o2[-1]; sig["hps2"] = e2[0] if lowstart else e2[-1]
    for t in range(1, m3 + 1):
        add(f"rrr{t}", 0, nxt(), [f"aaa{t}", f"bbb{t}"]); sig[f"rrr{t}"] = f"bbb{t}"
        add(f"aaa{t}", 1, P[f"BA3_{t}"], ["hs2" if t == 1 else f"rrr{t - 1}"]); add(f"bbb{t}", 1, nxt(), ["hps2"])
    return order, pr, own, succ, sig, tau
def write(K, m2, m3, out, start, design="D1"):
    order, pr, own, succ, sig, tau = build(K, m2, m3, design)
    assert len(set(pr.values())) == len(pr), "priorities not injective"
    ix = {v: i for i, v in enumerate(order)}
    with open(out, "w") as f:
        f.write(f"parity {len(order) - 1};\n")
        for v in order: f.write(f'{ix[v]} {pr[v]} {own[v]} {",".join(str(ix[w]) for w in succ[v])} "{v}";\n')
    with open(start, "w") as f:
        f.write("SIGMA0 " + " ".join(f"{ix[v]}:{ix[sig.get(v, succ[v][0])]}" for v in order if own[v] == 0) + "\n")
        f.write("TAU0 " + " ".join(f"{ix[v]}:{ix[tau.get(v, succ[v][0])]}" for v in order if own[v] == 1) + "\n")
    return len(order)
if __name__ == "__main__":
    K, m2, m3 = map(int, sys.argv[1:4])
    n = write(K, m2, m3, sys.argv[4], sys.argv[5], os.environ.get("DESIGN", "D1")); print(f"K {K} m2 {m2} m3 {m3} n {n}")
