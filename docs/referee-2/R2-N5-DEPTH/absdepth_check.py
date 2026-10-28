#!/usr/bin/env python3
r"""REFEREE-2 successor 18 (Opus 5.5, D15): P-N5-DEPTH-box22 §1 (Fact N-MONO, Theorem ABS-DEPTH) and §4 (the instance) in the model ABS,
on my own simulator R2-N5-GCX/abs_check.py (written from P-N5-GCX §4; lane's absdepth.py / abscyc.py NOT run).
Checks per run (cyclic or acyclic models, tie rules basic / flip / random tables):
  NMONO  N_{t+1} >= N_t pointwise
  AD     ABS-DEPTH per vertex: play_t(v) = play*(v) for t >= d*(v), when GEN holds (GEN checked exactly: all simple paths from v to a terminal
         have distinct N); AD_noGEN counts runs without GEN, AD_FAIL_noGEN per-vertex failures there
  ADL    run fixed after <= max d* steps (also counted without GEN: ADL_FAIL_noGEN)
Usage: absdepth_check.py random N nmin nmax seed cyclic(0|1) [vals]  |  instance"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-GCX"))
import abs_check as A


def play(m, st, v):
    out, x = [], v
    while not m.isterm(x):
        out.append(x); x = st[x]
        if len(out) > m.n: return None
    return tuple(out + [x])


def all_N(m, v):
    """N-values of all simple paths from v to a terminal (non-terminals simple)."""
    vals = []
    def go(x, seen, acc):
        if m.isterm(x): vals.append(A.addv(acc, m.T[x - m.n])); return
        if x in seen: return
        for y in m.succ[x]: go(y, seen | {x}, A.addv(acc, m.w[x]))
    go(v, frozenset(), (0, 0))
    return vals


def runseq(m, st0, rule, table):
    seq = [tuple(st0)]
    for _ in range(8 * m.n + 10):
        new, err, Al, V = A.step(m, seq[-1], rule, table)
        if err: return None, err
        seq.append(new)
        if new == seq[-2]: return seq, None
    return None, "NOFIX"


def check(m, st0, rule, table, cnt):
    seq, err = runseq(m, st0, rule, table)
    if err: cnt[err] = cnt.get(err, 0) + 1; return
    cnt["runs"] = cnt.get("runs", 0) + 1
    s = seq[-1]
    Ns = [m.values(x)[1] for x in seq]
    for t in range(1, len(seq)):
        if any(Ns[t][v] < Ns[t - 1][v] for v in range(m.n)): A.bad(cnt, "NMONO", f"{rule}")
    dstar = {v: len(play(m, s, v)) - 1 for v in range(m.n)}
    gen = all(len(set(all_N(m, v))) == len(all_N(m, v)) for v in range(m.n))
    if not gen: cnt["AD_noGEN"] = cnt.get("AD_noGEN", 0) + 1
    fix = len(seq) - 2
    md = max(dstar.values())
    if fix > md:
        if gen: A.bad(cnt, "ADL", f"{rule} fix {fix} > max d* {md}")
        else:
            cnt["ADL_FAIL_noGEN"] = cnt.get("ADL_FAIL_noGEN", 0) + 1
            cnt["ADL_FAIL_noGEN_" + rule] = cnt.get("ADL_FAIL_noGEN_" + rule, 0) + 1
            if os.environ.get("WHERE") and rule in ("basic", "flip"):
                print("ADL_noGEN", rule, "n", m.n, "succ", m.succ, "w", m.w, "h", m.h, "T", m.T, "start", st0, "run", seq, "max d*", md, flush=True)
    if fix == md: cnt["AD_sharp"] = cnt.get("AD_sharp", 0) + 1
    for v in range(m.n):
        cnt["AD_vertex_checks"] = cnt.get("AD_vertex_checks", 0) + 1
        for t in range(dstar[v], len(seq)):
            if play(m, seq[t], v) != play(m, s, v):
                if gen: A.bad(cnt, "AD", f"{rule} v={v} t={t} d*={dstar[v]}")
                else: cnt["AD_FAIL_noGEN"] = cnt.get("AD_FAIL_noGEN", 0) + 1
                break


def main():
    a = sys.argv[1:]; cnt = {"_ex": []}
    if a[0] == "instance":
        # P-N5-DEPTH §4: non-terminals 0, 1, 2; terminals t3, t4, t5 (= 3, 4, 5 here)
        m = A.Model(3, [[1, 3], [0, 2, 5], [0, 4, 5]], [(-1, 0), (1, 0), (1, 0)], [(-1, 0), (1, 0), (-1, 0)], [(0, 0), (1, 0), (1, 0)])
        for rule in ("basic", "flip"):
            seq, err = runseq(m, (3, 5, 0), rule, None)
            print(rule, "run:", seq, err)
            if seq:
                s = seq[-1]
                for t, x in enumerate(seq):
                    print(" state", t, "play(2) =", play(m, x, 2), "N(2) =", m.values(x)[1][2])
                print(" d*(2) =", len(play(m, s, 2)) - 1, "GEN at 2:", sorted(all_N(m, 2)))
        return
    N, nmin, nmax, seed = map(int, a[1:5]); cyclic = a[5] == "1"; small = len(a) > 6 and a[6] == "vals"
    rng = random.Random(seed)
    for i in range(N):
        n = rng.randint(nmin, nmax)
        m = A.rand_model(rng, n, cyclic)
        if small:
            m.w = [(rng.randint(-2, 2), 0) for _ in range(n)]
            m.h = [(rng.randint(-2, 2), 0) for _ in m.h]; m.T = [(max(x[0], rng.randint(-2, 2)), 0) for x in m.h]
        st0 = [rng.choice(m.succ[v]) for v in range(n)]
        if m.values(st0) is None: cnt["invalid_start"] = cnt.get("invalid_start", 0) + 1; continue
        for rule in ("basic", "flip", "r0"):
            sd = rng.randrange(1 << 30)
            check(m, st0, rule, (lambda v, key, sd=sd: hash((sd, v, key)) & 0xffffff), cnt)
    ex = cnt.pop("_ex")
    print("MODE", " ".join(a))
    for k in sorted(cnt): print(f"{k}: {cnt[k]}")
    for e in ex: print("VIOLATION", e)
    print("RESULT", "FAIL" if cnt.get("VIOLATIONS") else "OK", f"violations={cnt.get('VIOLATIONS', 0)}")


if __name__ == "__main__":
    main()
