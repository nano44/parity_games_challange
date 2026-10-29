#!/usr/bin/env python3
"""L-COMP box 20 (Lead 2026-10-29 15:20Z): exhaustive / random tables of SBC for L-NEW's N5-SF (docs/new/N5-SF-box54.md @ l-new 56a42d4f).
N5-SF's step is lnew_box54/n5sf.py, a VERBATIM copy of claude/l-new experiments/new/box54/n5sf.py @ 56a42d4f, imported unmodified
(n5x / si.py engine; experiments/new/box21/n5x.py is identical on trunk and on 56a42d4f). Per state the step result is cached, so each
game's states are stepped once over all start pairs.
Per start pair: SF iterations, SBC_σ = SF transitions at which σ̄ (Odd's best reply to σ, n5x Engine.evaluate) changes (= L-NEW sfrun.py's
SBC), SBC_τ = the mirror (transitions at which τ̄, Even's best reply to τ on G^d, changes), SBC = SBC_σ + SBC_τ, fallbacks, and N5's
iterations from the same start (n5x.step, cached). Checks (each a kill of N5-SF): CYCLE (a (σ, τ) state repeats), REGION (S5 regions
from the final σ differ from harness/zielonka.py), OPT (the final σ still has an improving edge).
Games: exh17's model C(n) (all owners, parity patterns, successor sets) or uniform random C(n) (randtab's draw).
Usage: sf20.py N (--exhaustive [--every K --offset J] | --random COUNT SEED [--maxstarts M]) [--jobs P] --out FILE.json"""
import argparse, itertools, json, multiprocessing as mp, os, random, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "lnew_box54")); sys.path.insert(0, os.path.join(EXP, "harness")); sys.path.insert(0, os.path.join(EXP, "n5-box17"))
import n5sf  # noqa: E402  (verbatim L-NEW copy)
from n5x import Engine, dual, step as n5step  # noqa: E402
import pg, zielonka  # noqa: E402
import exh17  # noqa: E402

KEYS = ("sbc", "sbc_sigma", "sbc_tau", "sbc_over_n", "sf_it", "n5_it", "sf_minus_n5", "sf_fb")


def put(S, k, val, inst):
    if S["best"].get(k) is None or val > S["best"][k][0]:
        S["best"][k] = (val, inst)
    h = S["hist"].setdefault(k, {}); h[str(val)] = h.get(str(val), 0) + 1


def do_game(g, S):
    n = g.n; E, Ed = Engine(g), Engine(dual(g)); win = zielonka.solve(g); S["c"]["games"] += 1
    sfc, n5c, ev = {}, {}, {}

    def info(s, t):
        k = (s, t)
        if k not in ev:
            ev[k] = (tuple(E.evaluate(s)[1]), tuple(Ed.evaluate(t)[1]))
        return ev[k]
    for p in itertools.product(*g.succ):
        s0 = tuple(p[v] if g.owner[v] == 0 else -1 for v in range(n)); t0 = tuple(p[v] if g.owner[v] == 1 else -1 for v in range(n))
        S["c"]["starts"] += 1; inst = dict(prio=g.prio, owner=g.owner, succ=g.succ, start=[list(s0), list(t0)])
        # N5-SF
        x = (s0, t0); seen = set(); it = fb = sbs = sbt = 0; cyc = False
        while True:
            if x in seen:
                cyc = True; break
            seen.add(x)
            if x not in sfc:
                r = n5sf.step(g, E, Ed, list(x[0]), list(x[1]))
                sfc[x] = None if r is None else ((tuple(r[0]), tuple(r[1])), r[4])
            r = sfc[x]
            if r is None:
                break
            y, f = r; it += 1; fb += f
            a, b = info(*x), info(*y); sbs += a[0] != b[0]; sbt += a[1] != b[1]; x = y
        if cyc:
            S["viol"].append(("CYCLE", inst)); continue
        vs, _ = E.evaluate(x[0])
        if [E.par[c[0]] for c in vs] != list(win):
            S["viol"].append(("REGION", inst))
        if E.improving(x[0], vs):
            S["viol"].append(("OPT", inst))
        # N5 from the same start
        z = (s0, t0); it5 = 0
        while True:
            if z not in n5c:
                r = n5step(g, E, Ed, list(z[0]), list(z[1])); n5c[z] = None if r is None else (tuple(r[0]), tuple(r[1]))
            if n5c[z] is None:
                break
            z = n5c[z]; it5 += 1
            if it5 > 100000:
                raise RuntimeError("N5 cap")
        for k, v in (("sbc", sbs + sbt), ("sbc_sigma", sbs), ("sbc_tau", sbt), ("sf_it", it), ("n5_it", it5), ("sf_minus_n5", it - it5), ("sf_fb", fb)):
            put(S, k, v, inst)
        S["c"]["sf_it_total"] += it; S["c"]["n5_it_total"] += it5; S["c"]["sf_fb_total"] += fb
    S["c"]["states"] += len(sfc)


def new():
    return dict(c=dict(games=0, starts=0, states=0, sf_it_total=0, n5_it_total=0, sf_fb_total=0), best={}, hist={}, viol=[])


def task_ex(args):
    n, every, offset, shard = args; S = new()
    for g in exh17.games(n, False, every, offset, shard):
        do_game(g, S)
    return S


def task_rand(args):
    n, cnt, seed, k, maxst = args; rnd = random.Random(seed + n * 1000003 + k); S = new()
    for _ in range(cnt):
        while True:
            own = [rnd.randint(0, 1) for _ in range(n)]; cp = exh17.prios([rnd.randint(0, 1) for _ in range(n)]); succ = []
            for v in range(n):
                m = rnd.randint(1, (1 << n) - 1); succ.append([w for w in range(n) if (m >> w) & 1])
            st = 1
            for s in succ: st *= len(s)
            if st <= maxst: break
        do_game(pg.Game(cp, own, succ), S)
    return S


def merge(A, Bs):
    for k, v in Bs["c"].items(): A["c"][k] = A["c"].get(k, 0) + v
    for k, b in Bs["best"].items():
        if A["best"].get(k) is None or b[0] > A["best"][k][0]: A["best"][k] = b
    for k, h in Bs["hist"].items():
        H = A["hist"].setdefault(k, {})
        for x, c in h.items(): H[x] = H.get(x, 0) + c
    A["viol"] += Bs["viol"][: max(0, 50 - len(A["viol"]))]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("n", type=int); ap.add_argument("--exhaustive", action="store_true")
    ap.add_argument("--random", nargs=2, type=int); ap.add_argument("--maxstarts", type=int, default=10 ** 9)
    ap.add_argument("--every", type=int, default=1); ap.add_argument("--offset", type=int, default=0)
    ap.add_argument("--jobs", type=int, default=4); ap.add_argument("--out", required=True); a = ap.parse_args(); t0 = time.time()
    if a.exhaustive:
        jobs = [(a.n, a.every * 4, a.offset * 4 + k, sh) for sh in range(1 << a.n) for k in range(4)]; fn = task_ex
    else:
        cnt, seed = a.random; K = 4 * a.jobs; per = (cnt + K - 1) // K; jobs = [(a.n, per, seed, k, a.maxstarts) for k in range(K)]; fn = task_rand
    S = new()
    with mp.Pool(a.jobs) as pool:
        for s in pool.imap_unordered(fn, jobs):
            merge(S, s)
            for v in s["viol"][:3]: print("VIOLATION", json.dumps(v), flush=True)
    S["best"]["sbc_over_n"] = (round(S["best"]["sbc"][0] / a.n, 3), S["best"]["sbc"][1]) if S["best"].get("sbc") else None
    out = dict(n=a.n, mode="exhaustive" if a.exhaustive else f"random {a.random}", every=a.every, offset=a.offset, maxstarts=a.maxstarts,
               counts=S["c"], best=S["best"], hist=S["hist"], violations=S["viol"], seconds=round(time.time() - t0))
    json.dump(out, open(a.out, "w"), indent=1)
    print("RESULT", json.dumps(dict(n=a.n, mode=out["mode"], counts=S["c"], max={k: (S["best"][k][0] if S["best"].get(k) else None) for k in KEYS}, violations=len(S["viol"]))))


if __name__ == "__main__":
    main()
