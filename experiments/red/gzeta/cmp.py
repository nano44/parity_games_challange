"""L-RED box 24 (produced on Opus 5.5): per-step comparison of N8d-R2's admissible-arc set with VJ's improving-switch set
on the same strategy (Lead GO 10:19Z, item 1; the Lemma 4.75 gap of docs/lit/T26-N8d-step3.md).

Objects (all imported read-only, unmodified):
- R2 = experiments/n8d-second/kl2fast.py (L-COMP's second implementation; = kl_single.py seed for seed). Only the DUAL run counts on
  G_zeta: in the dual (owners swapped, priorities + 1, kl2 C4) the Odd nodes are G_zeta's player-0 nodes (Friedmann's improver), and
  tau(v) is player 0's sigma(v). The loop below is KLFast.run line for line (same rng calls), with the comparison added; at the end
  it asserts the same pivot count and final tau as KLFast.run itself.
- VJ = experiments/si/si.py Engine (L-SI): Voege-Jurdzinski valuations of player 0's strategy sigma, improving(sigma) = arcs v->w,
  w != sigma(v), with val(w) > val(sigma(v)).
- Both engines get the SAME parsed game object (one pg.read), so vertex ids and arc sets agree by construction; asserted below.

Modes:
  r2 G.pg SEED [MAX]   follow R2's own run; at each state (tau_t, mu_t): A_t = admissible arcs (violated arcs of the dual Odd
                       nodes w.r.t. mu_t), I_t = VJ improving arcs of sigma = tau_t. Prints the first states with A != I.
  vj G.pg SEED [MAX]   follow VJ Random-Edge (vj_re.py's loop, same rng calls); at each sigma_t also keep Koh-Loho's
                       history labels mu_t = lfp(G_sigma_t, mu_{t-1}) (Algorithm 1 line 6 applied to VJ's switch) when VJ's
                       switch is admissible; prints the first state with A != I and stops tracking mu once VJ takes a
                       non-admissible arc (the history labels are then outside Algorithm 1's invariants).
Output: one line per differing state (up to MAX), then a summary line."""
import os
import random
import re
import sys

R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.insert(0, os.path.join(R, "experiments", "n8d-second"))
sys.path.insert(0, os.path.join(R, "experiments", "si"))
sys.path.insert(0, os.path.join(R, "experiments", "harness"))
sys.setrecursionlimit(100000)
import kl2fast  # noqa: E402
import kl2  # noqa: E402  (kl2.KL is KLFast after the kl2fast import)
import pg  # noqa: E402
import si  # noqa: E402

NAMES = {}


def names(path):
    out = {}
    for line in open(path):
        m = re.match(r'^\s*(\d+)\s.*"([^"]*)"', line)
        if m:
            out[int(m.group(1))] = m.group(2)
    return out


def nm(v):
    return NAMES.get(v, str(v))


def arcs_str(S, lim=12):
    s = sorted(S)
    t = ", ".join(f"{nm(v)}->{nm(w)}" for v, w in s[:lim])
    return t + (f" ... (+{len(s) - lim})" if len(s) > lim else "")


def setup(path):
    global NAMES
    NAMES = names(path)
    g = pg.read(path)
    D = kl2.KL([p + 1 for p in g.prio], [1 - o for o in g.owner], g.succ, "first")      # kl2.solve's dual (C4)
    E = si.Engine(g)
    for v in range(g.n):                                                                  # numbering check
        assert sorted(set(D.succ[v])) == E.succ[v], v
        assert (D.owner[v] == 1) == (E.owner[v] == si.EVEN), v
    return g, D, E


def cls(v, w):
    """Arc class by node names: letters of the source and target names (a1,3->a1,2 -> 'a->a')."""
    return re.sub(r"[\d,]", "", nm(v)) + "->" + re.sub(r"[\d,]", "", nm(w))


def tally(T, S):
    for v, w in S:
        c = cls(v, w); T[c] = T.get(c, 0) + 1


def adm_set(D, mu):
    return {(v, w) for v, ws in D.admissible(mu).items() for w in ws}


def strat_of(g, tau):
    return tuple(tau[v] if g.owner[v] == 0 else -1 for v in range(g.n))


def lab(l):
    return "TOP" if l is None else ".".join(map(str, l))



def run_r2(path, seed, mx):
    g, D, E = setup(path)
    n = D.n
    tau = dict(D.tau)
    cm, ct = kl2fast.arr([0] * (n * D.h)), kl2fast.arr([0] * n)
    D.c_lfp(tau, cm, ct)
    rng = random.Random(seed)
    cand, carc = kl2fast.arr([0] * n), kl2fast.arr([0] * n)
    piv = ndiff = shown = 0
    first = None
    stats = {"A_minus_I": 0, "I_minus_A": 0, "pick_not_improving": 0, "pick_worsening": 0}
    TA, TI, TP, TW, TF = {}, {}, {}, {}, {}     # classes of A-I, I-A (summed over states), R2 picks, R2 picks that VJ-worsen
    while True:
        mu = D.to_labels(cm, ct)
        A = adm_set(D, mu)
        sig = strat_of(g, tau)
        val = E.evaluate(sig)[0]
        I = set(E.improving(sig, val))
        k = kl2fast.LIB.kl_adm(n, D.h, D.d, D.ell, D.c_pi, D.c_owner, D.c_off, D.c_sadj, D.c_K, cm, ct, cand, carc)
        assert {v for v, _ in A} == set(cand[:k]), "kl_adm candidate set != python admissible"
        tally(TA, A - I); tally(TI, I - A)
        if A != I:
            ndiff += 1
            stats["A_minus_I"] += len(A - I) > 0
            stats["I_minus_A"] += len(I - A) > 0
            if first is None:
                first = piv
            if shown < mx:
                shown += 1
                print(f"state {piv}: |A| {len(A)} |I| {len(I)}  A-I [{arcs_str(A - I)}]  I-A [{arcs_str(I - A)}]")
                for (v, w) in sorted((A - I) | (I - A))[:6]:
                    c = sig[v]
                    print(f"    {nm(v)}: sigma {nm(c)} cand {nm(w)} | mu(v) {lab(mu[v])} mu(sig) {lab(mu[c])} mu(w) {lab(mu[w])}"
                          f" T(w) {lab(D.tighten(mu, v, w))} | VJ val(sig) {E.key(val[c])} val(w) {E.key(val[w])}")
        if not k:
            break
        vs = list(cand[:k])
        i = vs.index(rng.choice(sorted(vs)))
        v, w = vs[i], carc[i]
        kv = E.key(val[w]); kc = E.key(val[sig[v]])
        tally(TP, [(v, w)])
        fresh = D.lfp(tau, [D.zeros[D.h]] * D.n)
        if not D.viol(fresh, v, w):
            stats["pick_not_adm_fresh"] = stats.get("pick_not_adm_fresh", 0) + 1; tally(TF, [(v, w)])
        if (v, w) not in I:
            stats["pick_not_improving"] += 1
            if kv < kc:
                stats["pick_worsening"] += 1; tally(TW, [(v, w)])
        tau[v] = w
        D.c_lfp(tau, cm, ct)
        piv += 1
    ref = D.run("r2", seed)
    assert ref[0] == piv and ref[1] == tau, "replay differs from KLFast.run"
    print(f"SUMMARY r2 {os.path.basename(path)} seed {seed}: pivots {piv} (= KLFast.run), states with A != I {ndiff}/{piv + 1}, "
          f"first at state {first}; {stats}")
    print(f"  classes A-I {TA}\n  classes I-A {TI}\n  R2 picks {TP}\n  R2 picks that lower VJ val {TW}\n  R2 picks not admissible for the fresh lfp of the same tau {TF}")


def run_vj(path, seed, mx):
    g, D, E = setup(path)
    rng = random.Random(seed)
    strat = tuple(g.succ[v][0] if g.owner[v] == 0 else -1 for v in range(g.n))
    tau = {v: strat[v] for v in D.odd_nodes}
    mu = D.lfp(tau, [D.zeros[D.h]] * D.n)
    track = True
    it = ndiff = shown = 0
    first = lost = None
    notsub = 0; TA, TI = {}, {}
    while True:
        val = E.evaluate(strat)[0]
        I = set(E.improving(strat, val))
        if track:
            A = adm_set(D, mu)
            tally(TA, A - I); tally(TI, I - A); notsub += not I <= A
            if A != I:
                ndiff += 1
                if first is None:
                    first = it
                if shown < mx:
                    shown += 1
                    print(f"vj state {it}: |A| {len(A)} |I| {len(I)}  A-I [{arcs_str(A - I)}]  I-A [{arcs_str(I - A)}]")
                    for (v, w) in sorted((A - I) | (I - A))[:6]:
                        c = strat[v]
                        print(f"    {nm(v)}: sigma {nm(c)} cand {nm(w)} | mu(v) {lab(mu[v])} mu(sig) {lab(mu[c])} mu(w) {lab(mu[w])}"
                              f" T(w) {lab(D.tighten(mu, v, w))} | VJ val(sig) {E.key(val[c])} val(w) {E.key(val[w])}")
        if not I:
            break
        it += 1
        new = E.rule_random_edge(strat, val, sorted(I) if False else E.improving(strat, val), rng)
        v = next(u for u in range(g.n) if new[u] != strat[u])
        if track:
            if (v, new[v]) not in A:
                track = False; lost = it
                print(f"vj step {it}: VJ switch {nm(v)}->{nm(new[v])} is NOT admissible for mu; history labels dropped")
                fresh = D.lfp(tau, [D.zeros[D.h]] * D.n)          # least fixed point from the bottom for the same sigma
                Af = adm_set(D, fresh)
                print(f"  history mu: I-A [{arcs_str(I - A)}]\n  fresh mu (lfp from 0, same sigma): |A0| {len(Af)} "
                      f"I-A0 [{arcs_str(I - Af)}] A0-I [{arcs_str(Af - I)}]")
                for x in sorted({v, strat[v], new[v]} | {y for y in range(g.n) if nm(y).startswith(nm(v).split(",")[0] + ",")
                                                         and int(nm(y).split(",")[1]) <= int(nm(v).split(",")[1]) + 1}):
                    print(f"    {nm(x)}: sigma {nm(strat[x]) if strat[x] >= 0 else '-'} mu {lab(mu[x])} fresh {lab(fresh[x])} "
                          f"VJ {E.key(val[x])}")
            else:
                tau[v] = new[v]
                mu = D.lfp(tau, mu)
        strat = new
        if lost is not None and os.environ.get("STOP_AT_LOSS"):
            break
    print(f"SUMMARY vj {os.path.basename(path)} seed {seed}: iterations {it}, tracked states with A != I {ndiff}, first at {first}, "
          f"tracking lost at step {lost}; tracked states with I not a subset of A {notsub}")
    print(f"  classes A-I {TA}\n  classes I-A {TI}")


if __name__ == "__main__":
    mode, path, seed = sys.argv[1], sys.argv[2], int(sys.argv[3])
    mx = int(sys.argv[4]) if len(sys.argv) > 4 else 5
    (run_r2 if mode == "r2" else run_vj)(path, seed, mx)
