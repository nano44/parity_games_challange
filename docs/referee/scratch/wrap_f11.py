#!/usr/bin/env python3
"""REFEREE successor 33: Friedmann's game G_n for the locally optimizing policy, transcribed by me from the opened PDF
(arXiv 1106.0778v2, sha256 46c96f44...; p. 15 Table 4, Fact 6.1, the initial strategy; p. 16 Figure 4), and the facts the «tie item»
of L-SI 52's Statement XI-EXP (box 104 section 6) needs. No lane code; engine rl_engine.py; wrapper and counters wrap_replay.py.

Priorities: VER=fig4 (default): Figure 4's values, d_i = 4i - 1, e_i = 4i, g_i = 4i + 2, k_i = 8n + 4i + 5, f_i = 8n + 4i + 7,
h_i = 8n + 4i + 8 (injective; highest 12n + 8 = Fact 6.1); VER=table4: Table 4 as printed (those six formulas 2 higher).
Checks per n (all on H = G_n itself, Howard = every Even vertex to a best successor by H's own valuation, start iota):
  fact61    nodes != 10n + 4, edges != 1.5 n^2 + 20.5 n + 5, or (fig4) highest priority != 12n + 8 / priorities not injective
  sinkex    Sink Existence fails: x not a self-loop of priority 1 reachable from every node, or another node of priority <= 1
  w1all     my Zielonka: some node is not won by player 1                                     (Lemma 6.7 (1))
  sinkseek  (state, node): the cycle component of the node's valuation is not x              (Lemma 6.7 (2), Lemma 5.1)
  eqval     (state, unordered pair of distinct nodes) with EQUAL valuations                   (my no-tie argument: must be 0)
  tie       (state, Even node): two or more best successors                                   (the lane's «tie events»)
  T         the number of improvement steps of the run; T >= 2^n is Theorem 6.14; the lane's count is 9 * 2^n - 10
With WRAP=xi or WRAP=spec: also the 18 counters of wrap_replay.check on W(G_n, iota), and iterations against T + 3.
Usage: wrap_f11.py N1 N2 ...      env VER, WRAP, PERM"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as E
import wrap_replay as WR

VER = os.environ.get("VER", "fig4"); WRAP = os.environ.get("WRAP", "")


def build(n):
    nodes = ["x", "s", "c", "r"] + [f"t{i}" for i in range(1, 2 * n + 1)] + [f"a{i}" for i in range(1, 2 * n + 1)]
    for i in range(1, n + 1): nodes += [f"d{i}", f"e{i}", f"g{i}", f"k{i}", f"f{i}", f"h{i}"]
    idx = {nm: j for j, nm in enumerate(nodes)}
    sh = 2 if VER == "table4" else 0
    own, pr, su = {}, {}, {}

    def add(nm, player, prio, succs): own[nm], pr[nm], su[nm] = player, prio, succs
    add("t1", 0, 4 * n + 3, ["s", "r", "c"])
    for i in range(2, 2 * n + 1): add(f"t{i}", 0, 4 * n + 2 * i + 1, ["s", "r", f"t{i-1}"])
    for i in range(1, 2 * n + 1): add(f"a{i}", 1, 4 * n + 2 * i + 2, [f"t{i}"])
    add("c", 0, 8 * n + 4, ["s", "r"])
    for i in range(1, n + 1):
        add(f"d{i}", 0, 4 * i - 1 + sh, ["s", f"e{i}", "r"] + [f"a{j}" for j in range(1, 2 * i + 1)])
        add(f"e{i}", 1, 4 * i + sh, [f"d{i}", f"h{i}"])
        add(f"g{i}", 0, 4 * i + 2 + sh, [f"f{i}", f"k{i}"])
        add(f"k{i}", 0, 8 * n + 4 * i + 5 + sh, ["x"] + [f"g{j}" for j in range(i + 1, n + 1)])
        add(f"f{i}", 1, 8 * n + 4 * i + 7 + sh, [f"e{i}"])
        add(f"h{i}", 1, 8 * n + 4 * i + 8 + sh, [f"k{i}"])
    add("s", 0, 8 * n + 6, [f"f{j}" for j in range(1, n + 1)] + ["x"])
    add("r", 0, 8 * n + 8, [f"g{j}" for j in range(1, n + 1)] + ["x"])
    add("x", 1, 1, ["x"])
    iota = {"t1": "c", "c": "r", "s": "x", "r": "x"}
    for i in range(2, 2 * n + 1): iota[f"t{i}"] = "r"
    for i in range(1, n + 1): iota[f"g{i}"] = f"k{i}"; iota[f"d{i}"] = "r"; iota[f"k{i}"] = "x"
    prio = [pr[nm] for nm in nodes]; owner = [own[nm] for nm in nodes]; succ = [sorted(idx[w] for w in su[nm]) for nm in nodes]
    s0 = {idx[v]: idx[w] for v, w in iota.items()}
    assert set(s0) == {v for v in range(len(nodes)) if owner[v] == 0}
    return nodes, idx, prio, owner, succ, s0


def run(n):
    nodes, idx, prio, owner, succ, s0 = build(n); N = len(nodes); x = idx["x"]
    c = dict(fact61=0, sinkex=0, w1all=0, sinkseek=0, eqval=0, tie=0)
    edges = sum(len(s) for s in succ)
    if N != 10 * n + 4 or 2 * edges != 3 * n * n + 41 * n + 10: c["fact61"] += 1
    if VER == "fig4" and (max(prio) != 12 * n + 8 or len(set(prio)) != N): c["fact61"] += 1
    # sink existence
    reach = {x}; todo = [x]; pred = [[] for _ in range(N)]
    for v in range(N):
        for w in succ[v]: pred[w].append(v)
    while todo:
        y = todo.pop()
        for p in pred[y]:
            if p not in reach: reach.add(p); todo.append(p)
    if not (succ[x] == [x] and prio[x] == 1 and len(reach) == N and all(prio[v] > 1 for v in range(N) if v != x)): c["sinkex"] += 1
    z0, z1 = WR.zielonka(prio, owner, succ)
    if z0: c["w1all"] += 1
    Hg = E.Game(prio, owner, succ); s = dict(s0); T = 0; states = 0
    while True:
        val, _ = E.evaluate(Hg, [s.get(v) for v in range(N)]); states += 1
        for v in range(N):
            if val[v][0] != x: c["sinkseek"] += 1
        seen = {}
        for v in range(N):
            seen.setdefault(val[v], []).append(v)
        c["eqval"] += sum(len(g) * (len(g) - 1) // 2 for g in seen.values())
        new = {}; moved = False
        for v in s:
            keys = {w: Hg.key(val[w]) for w in succ[v]}; best = max(keys.values())
            bs = [w for w in succ[v] if keys[w] == best]
            if len(bs) >= 2: c["tie"] += 1
            new[v] = s[v] if keys[s[v]] == best else max(bs)
            moved |= new[v] != s[v]
        if not moved: break
        s = new; T += 1
    out = f"n {n} VER {VER} nodes {N} edges {edges} maxprio {max(prio)} | T {T} 2^n {2**n} 9*2^n-10 {9*2**n-10} states {states} | " \
          + " ".join(f"{k} {v}" for k, v in c.items())
    if WRAP:
        cc, info = WR.check(prio, owner, succ, s0, WRAP, random.Random(7 + n))
        out += f" | WRAP {WRAP} |W| {info['nW']} its {info['its']} F {info['F']} fallbacks {info['fbs']} T_W {info['T']} its-T {info['its'] - T} | " \
               + " ".join(f"{k} {cc[k]}" for k in WR.NAMES)
    print(out, flush=True)


if __name__ == "__main__":
    for a in sys.argv[1:]: run(int(a))
