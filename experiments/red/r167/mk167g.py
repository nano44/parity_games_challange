#!/usr/bin/env python3
"""L-RED successor 39 (R167): GENOME form of mk167.py (same graph family, every marker placed by a genome), for the climb climb167.py.
Graph: span/mkrw.py K 2 (ladder h / hp, E1 r_1, r_2), E1 riders d_j -> md_j (MU_j) -> r_j, b_j -> be_j (BE_j) -> hp, hs -> d_1, hps -> d_2,
E1 gate a_2 -> {r_1 (tau), g_2 (GM_2) -> rr_m2};
E2: rr_i -> {aa_i (BA2_i), bb_i (BB_i) -> hps}; aa_1 -> hs; aa_i (i >= 2) -> {rr_(i-1) (tau), gg_i (GM2_i) -> rrr_m3};
E3 drivers hs2 -> {dd_i: i odd}, hps2 -> {dd_0} + {dd_i: i even}; rider dd_i (Odd, MU2_i) -> {mdd_i (M2_i) -> rr_i (tau)} + escape
x_i (X_i) -> hps when ESC says so (ESC 0: none; 1: every i; 2: i >= 3 only; 3: i >= 3, and dd_1 / dd_2 escape to hs instead);
dd_0 (MU2_0) -> hps; E3: rrr_t -> {aaa_t (BA3_t) -> rrr_(t-1) | hs2, bbb_t (BBB_t) -> hps2}.
Genome: {"ESC": int, "LOW": bool (drivers start on dd_1 / dd_0), "mk": {class: null (inert) | [base, slope, parity]}}; the key of marker
class c at index i is base + slope * 0.01 * i; all placed markers are sorted by key into the band between E1's a-markers and the ladder.
Classes: BA3 BBB BA2 BB GM2 MU2 M2 X (indexed), MU0 MU_1 MU_2 GM_2 BE_1 BE_2 (single).
Usage: mk167g.py K m2 m3 GENOME.json OUT.pg OUT.start"""
import sys, os, re, subprocess, tempfile, json
HERE = os.path.dirname(os.path.abspath(__file__))
IDX = ["BA3", "BBB", "BA2", "BB", "GM2", "MU2", "M2", "X"]; ONE = ["MU0", "MU_1", "MU_2", "GM_2", "BE_1", "BE_2"]
_base = {}
def mkrw(K):
    if K not in _base:
        td = tempfile.mkdtemp()
        subprocess.run([sys.executable, os.path.join(HERE, "..", "span", "mkrw.py"), str(K), "2", f"{td}/b.pg", f"{td}/b.start"], check=True, capture_output=True)
        rows = []
        for line in open(f"{td}/b.pg"):
            mm = re.match(r'\s*(\d+)\s+(\d+)\s+([01])\s+([\d,]+)\s*"([^"]*)"', line)
            if mm: rows.append([int(mm.group(1)), int(mm.group(2)), int(mm.group(3)), [int(a) for a in mm.group(4).split(",")], mm.group(5)])
        rows.sort(); st = open(f"{td}/b.start").read().split("\n")
        _base[K] = (rows, dict(tuple(map(int, x.split(":"))) for x in st[0].split()[1:]), dict(tuple(map(int, x.split(":"))) for x in st[1].split()[1:]))
    return _base[K]
def build(K, m2, m3, gen):
    rows, S0, T0 = mkrw(K); base = {r[4]: r for r in rows}
    Z = base["z"][1]; BAmax = max(base[f"a{j}"][1] for j in (1, 2)); LADmin = min(r[1] for r in rows if r[1] > BAmax)
    order = [r[4] for r in rows]; pr = {r[4]: 1000 * r[1] + (r[1] % 2) for r in rows}; own = {r[4]: r[2] for r in rows}
    succ = {r[4]: [rows[w][4] for w in r[3]] for r in rows}
    sig = {rows[v][4]: rows[w][4] for v, w in S0.items()}; tau = {rows[v][4]: rows[w][4] for v, w in T0.items()}
    mk = gen["mk"]; ESC = gen.get("ESC", 1)
    rng = {"BA3": range(1, m3 + 1), "BBB": range(1, m3 + 1), "BA2": range(1, m2 + 1), "BB": range(1, m2 + 1), "GM2": range(2, m2 + 1),
           "MU2": range(1, m2 + 1), "M2": range(1, m2 + 1), "X": range(1, m2 + 1)}
    keyed = []
    for c in IDX:
        if mk.get(c) is not None:
            b, sl, par = mk[c]
            for i in rng[c]: keyed.append((b + sl * 0.01 * i, f"{c}_{i}", par))
    for c in ONE:
        if mk.get(c) is not None: keyed.append((mk[c][0], c, mk[c][2]))
    if "explicit" in gen:                                   # mk167m.py: every marker given as name -> [key, parity] (absent = inert)
        keyed = [(v[0], k, v[1]) for k, v in gen["explicit"].items()]
    keyed.sort()
    lo, hi = 1000 * BAmax + 2, 1000 * LADmin - 2; assert hi - lo > 2 * len(keyed) + 4
    P = {}; x = lo
    for _, name, par in keyed:
        while x % 2 != par: x += 1
        P[name] = x; x += 1
    used = set(pr.values()) | set(P.values()); low = iter(range(2, 1000 * Z))
    def nxt():
        v = next(low)
        while v in used: v = next(low)
        used.add(v); return v
    def p(name): return P[name] if name in P else nxt()
    def add(name, o, pp, s): order.append(name); own[name] = o; pr[name] = pp; succ[name] = list(s)
    for j in (1, 2):
        add(f"d{j}", 1, nxt(), [f"md{j}"]); add(f"md{j}", 1, p(f"MU_{j}"), [f"r{j}"])
        add(f"be{j}", 1, p(f"BE_{j}"), ["hp"]); succ[f"b{j}"] = [f"be{j}"]; tau[f"b{j}"] = f"be{j}"
    succ["a2"] = ["r1", "g2"]; tau["a2"] = "r1"; add("g2", 1, p("GM_2"), [f"rr{m2}"])
    add("hs", 0, nxt(), ["d1"]); add("hps", 0, nxt(), ["d2"])
    if gen.get("T2"): add("t2", 1, p("T2"), ["hp"])           # R169: second-rung sink (srz3c EXTTGT, T2HI): t2 -> hp directly
    for i in range(1, m2 + 1):
        add(f"rr{i}", 0, nxt(), [f"aa{i}", f"bb{i}"]); sig[f"rr{i}"] = f"bb{i}"
        if i == 1: add("aa1", 1, p("BA2_1"), ["hs"])
        else:
            add(f"aa{i}", 1, p(f"BA2_{i}"), [f"rr{i - 1}", f"gg{i}"] + ([f"hh{i}"] if gen.get("STATIC") else [])); tau[f"aa{i}"] = f"rr{i - 1}"
            add(f"gg{i}", 1, p(f"GM2_{i}"), [f"rrr{m3}"])
            if gen.get("STATIC"): add(f"hh{i}", 1, p(f"H_{i}"), ["t2" if not gen.get("hq", {}).get(str(i), True) else "hps"])   # R168 / R169
        add(f"bb{i}", 1, p(f"BB_{i}"), ["hps"])
    add("dd0", 1, p("MU0"), ["hps"])
    for i in range(1, m2 + 1):
        esc = ESC == 1 or (ESC in (2, 3) and i >= 3)
        tgt = "hs" if (ESC == 3 and i <= 2) else "hps"
        ss = [f"mdd{i}"] + ([f"x{i}"] if esc or (ESC == 3 and i <= 2) else [])
        if "escj" in gen:                                    # per-index escape: 0 none, 1 -> hps (self-referential), 2 -> hs (root)
            e = gen["escj"][str(i)]; tgt = {1: "hps", 2: "hs", 3: "t2", 4: f"rrr{m3}"}.get(e, "hps"); ss = [f"mdd{i}"] + ([f"x{i}"] if e else [])
        add(f"dd{i}", 1, p(f"MU2_{i}"), ss); tau[f"dd{i}"] = f"mdd{i}"; add(f"mdd{i}", 1, p(f"M2_{i}"), [f"rr{i}"])
        if len(ss) > 1: add(f"x{i}", 1, p(f"X_{i}"), [tgt])
    o2 = [f"dd{i}" for i in range(1, m2 + 1, 2)]; e2 = ["dd0"] + [f"dd{i}" for i in range(2, m2 + 1, 2)]
    add("hs2", 0, nxt(), o2); add("hps2", 0, nxt(), e2)
    sig["hs2"] = o2[0] if gen.get("LOW") else o2[-1]; sig["hps2"] = e2[0] if gen.get("LOW") else e2[-1]
    if gen.get("HPS0") == 2: sig["hps2"] = "dd2"            # R168: hps2 starts on dd_2 (srz3b HPS0=2)
    if gen.get("MID"):                                       # start mid-phase: r_1, rr_1, rr_2 risen, hs2 on dd_1, hps2 on dd_2
        sig["r1"] = "a1"; sig["rr1"] = "aa1"; sig["rr2"] = "aa2"; sig["hs2"] = "dd1"; sig["hps2"] = "dd2"
    for t in range(1, m3 + 1):
        add(f"rrr{t}", 0, nxt(), [f"aaa{t}", f"bbb{t}"]); sig[f"rrr{t}"] = f"bbb{t}"
        add(f"aaa{t}", 1, p(f"BA3_{t}"), ["hs2" if t == 1 else f"rrr{t - 1}"]); add(f"bbb{t}", 1, p(f"BBB_{t}"), ["hps2"])
    assert len(set(pr.values())) == len(pr)
    return order, pr, own, succ, sig, tau
def game(K, m2, m3, gen):
    order, pr, own, succ, sig, tau = build(K, m2, m3, gen)
    ix = {v: i for i, v in enumerate(order)}
    return order, [pr[v] for v in order], [own[v] for v in order], [[ix[w] for w in succ[v]] for v in order], \
        [ix[sig.get(v, succ[v][0])] if own[v] == 0 else -1 for v in order], [ix[tau.get(v, succ[v][0])] if own[v] == 1 else -1 for v in order]
def write(K, m2, m3, gen, out, start):
    order, pr, own, succ, s0, t0 = game(K, m2, m3, gen)
    with open(out, "w") as f:
        f.write(f"parity {len(order) - 1};\n")
        for v in range(len(order)): f.write(f'{v} {pr[v]} {own[v]} {",".join(map(str, succ[v]))} "{order[v]}";\n')
    with open(start, "w") as f:
        f.write("SIGMA0 " + " ".join(f"{v}:{s0[v]}" for v in range(len(order)) if own[v] == 0) + "\n")
        f.write("TAU0 " + " ".join(f"{v}:{t0[v]}" for v in range(len(order)) if own[v] == 1) + "\n")
    return len(order)
if __name__ == "__main__":
    K, m2, m3 = map(int, sys.argv[1:4]); gen = json.load(open(sys.argv[4]))
    print(f"K {K} m2 {m2} m3 {m3} n {write(K, m2, m3, gen, sys.argv[5], sys.argv[6])}")
