"""L-RED box 24 (produced on Opus 5.5): EXACT per-lap failure probability of N8d-R2 from a lap-start snapshot (Lead 11:20Z (a)).
The snapshot is taken as in laptrial2.py: base seed S, after a warm-up of W pivots, the J-th increase of dual node 1's label.
From it, R2 within one lap is a finite Markov chain: a state is (tau, mu) (mu as kl2fast's C buffers); from each state R2 picks a
uniformly random node among kl2fast's own candidate set (kl_adm) and switches it to kl_adm's arc, then the C least fixed point.
States are merged on equal (tau, mu). Absorbing: SUCCESS (node 1's label changes to a larger finite value, TOP count unchanged),
FAILURE (TOP count changes, or no candidate, or node 1 decreases / becomes TOP). Probabilities: Fractions by default (exact); with FLOAT=1, doubles (relative error ~1e-15 per operation). States are stored
zlib-compressed; the processed set keeps a 16-byte blake2b digest per state.
Prints the number of distinct states per layer, the exact failure probability and its float.
Usage: exactlap.py G.pg [S] [W] [J] [MAXSTATES]"""
import os
import random
import sys
from fractions import Fraction

R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
for d in ("n8d-second", "harness"):
    sys.path.insert(0, os.path.join(R, "experiments", d))
import kl2fast  # noqa: E402
import kl2  # noqa: E402
import pg  # noqa: E402

path = sys.argv[1]
S = int(sys.argv[2]) if len(sys.argv) > 2 else 1
W = int(sys.argv[3]) if len(sys.argv) > 3 else 2000
J = int(sys.argv[4]) if len(sys.argv) > 4 else 1
MAXS = int(sys.argv[5]) if len(sys.argv) > 5 else 2 * 10 ** 6
g = pg.read(path)
D = kl2.KL([p + 1 for p in g.prio], [1 - o for o in g.owner], g.succ, "first")
n, h = D.n, D.h
LIB = kl2fast.LIB
odd = D.odd_nodes
cand, carc = kl2fast.arr([0] * n), kl2fast.arr([0] * n)
cm, ct = kl2fast.arr([0] * (n * h)), kl2fast.arr([0] * n)


def adm():
    return LIB.kl_adm(n, h, D.d, D.ell, D.c_pi, D.c_owner, D.c_off, D.c_sadj, D.c_K, cm, ct, cand, carc)


def lab1():
    return None if ct[1] else tuple(cm[h:2 * h])


# 1. the snapshot
tau = dict(D.tau)
D.c_lfp(tau, cm, ct)
rng = random.Random(S)
piv = laps = 0
while True:
    k = adm()
    assert k, "base run ended before the snapshot"
    before = lab1()
    vs = list(cand[:k]); i = vs.index(rng.choice(sorted(vs))); tau[vs[i]] = carc[i]; D.c_lfp(tau, cm, ct); piv += 1
    now = lab1()
    assert now is not None, "base run failed before the snapshot"
    if piv >= W and now != before:
        laps += 1
        if laps == J:
            break
l0, tops0 = lab1(), sum(ct)


import hashlib  # noqa: E402
import zlib  # noqa: E402
NUM = float if os.environ.get("FLOAT") else Fraction


def key(tau):
    return zlib.compress(bytes(memoryview(kl2fast.arr([tau[v] for v in odd])).cast("B")) + bytes(memoryview(cm).cast("B")) +
                         bytes(memoryview(ct).cast("B")), 1)


NODD = len(odd)


def load(st):
    raw = zlib.decompress(st)
    a, b = 4 * NODD, 4 * NODD + 4 * n * h
    memoryview(cm).cast("B")[:] = raw[a:b]
    memoryview(ct).cast("B")[:] = raw[b:]
    tv = memoryview(raw[:a]).cast("i")
    return {v: tv[i] for i, v in enumerate(odd)}


def dig(st):
    return hashlib.blake2b(st, digest_size=16).digest()


# 2. exact absorbing-chain evaluation. Every pivot strictly raises mu in the product order (the switched node's arc was violated,
#    and the least fixed point only lifts), so the potential sum_v enc(mu(v)) (enc = base-(ell+1) value of the label tuple, TOP
#    largest) strictly increases along every transition: processing states by increasing potential is a topological order of the
#    lap chain, and mass from paths of different lengths merges correctly.
import heapq  # noqa: E402
BASE = D.ell + 1
TOPV = BASE ** h


def potential():
    tot = 0
    for v in range(n):
        if ct[v]:
            tot += TOPV
        else:
            x = 0
            for j in range(v * h, v * h + h):
                x = x * BASE + cm[j]
            tot += x
    return tot


MAXPATH = bool(os.environ.get("MAXPATH"))      # also track the single most probable path into each state (Viterbi)


NLAPS = int(os.environ.get("LAPS", "1"))   # SUCCESS = node 1's label has increased NLAPS times (FAIL as before, at any point)


def chain(tau, l0, tops0):
    """Exact absorbing-chain evaluation from the current buffers and tau over NLAPS laps; returns (p_fail, p_succ, states,
    byfail, bestfail, maxheap). A state is (laps done, compressed (tau, mu)); a lap ends when node 1's label changes."""
    s0 = (0, key(tau))
    mass = {s0: NUM(1)}
    heap = [(potential(), 0, s0)]
    cnt = 1
    p_fail = NUM(0); p_succ = NUM(0); seen = set(); maxheap = 1; byfail = {}
    best = {s0: (1.0, ())} if MAXPATH else None
    bestfail = (0.0, ())
    while heap:
        pot, _, st = heapq.heappop(heap)
        ds = (st[0], dig(st[1]))
        if ds in seen:
            continue
        seen.add(ds)
        pr = mass.pop(st)
        if len(seen) > MAXS:
            print(f"ABORT: more than {MAXS} states"); sys.exit(2)
        t0 = load(st[1])
        lcur = lab1()
        bp = best.pop(st) if MAXPATH else None
        k = adm()
        if not k:
            p_fail += pr; byfail["(no candidate)"] = byfail.get("(no candidate)", 0) + pr; continue
        vs = list(cand[:k]); arcs = list(carc[:k])
        q = pr / k
        for v, w in zip(vs, arcs):
            t1 = dict(t0); t1[v] = w
            load(st[1]); D.c_lfp(t1, cm, ct)
            step = f"{v}->{w} of {sorted(vs)}"
            if sum(ct) != tops0:
                p_fail += q; fk = f"{v}->{w} |cand| {k} (lap {st[0] + 1})"; byfail[fk] = byfail.get(fk, 0) + q
                if MAXPATH and bp[0] / k > bestfail[0]:
                    bestfail = (bp[0] / k, bp[1] + (step,))
                continue
            now = lab1()
            d = st[0]
            if now != lcur:
                if now is None or now < lcur:
                    p_fail += q; fk = f"{v}->{w} |cand| {k} (node 1 not raised)"; byfail[fk] = byfail.get(fk, 0) + q
                    continue
                d += 1
                if d == NLAPS:
                    p_succ += q
                    continue
            kk = (d, key(t1))
            assert (d, dig(kk[1])) not in seen, "a transition into an already processed state (potential order violated)"
            pt = potential()
            assert pt > pot, "potential did not increase"
            if MAXPATH:
                cand_p = (bp[0] / k, bp[1] + (step,))
                if kk not in best or best[kk][0] < cand_p[0]:
                    best[kk] = cand_p
            if kk in mass:
                mass[kk] += q
            else:
                mass[kk] = q; cnt += 1; heapq.heappush(heap, (pt, cnt, kk))
        maxheap = max(maxheap, len(heap))
    return p_fail, p_succ, len(seen), byfail, bestfail, maxheap


SCAN = int(os.environ.get("SCAN", "0"))
COND = bool(os.environ.get("COND"))   # scan only: the base run redraws a pick that would fail (conditioning on survival, to reach late laps)
if SCAN:
    # 3. scan mode: from the snapshot lap on, solve the chain at EVERY lap start of the same base run for SCAN laps
    vals = {}
    worst = (-1.0, None)
    for lap in range(SCAN):
        st0 = key(tau)
        p_fail, p_succ, nst, byfail, bestfail, maxheap = chain(dict(tau), lab1(), sum(ct))
        load(st0)
        f = float(p_fail)
        kq = f"{f:.4g}"
        vals[kq] = vals.get(kq, 0) + 1
        if f > worst[0]:
            worst = (f, laps + lap, ".".join(map(str, lab1()[:6])))
        while True:                                   # advance the base run to the next lap start
            k = adm()
            if not k:
                break
            before = lab1()
            vs = list(cand[:k]); arcs = list(carc[:k]); tops = sum(ct)
            for _try in range(1000):
                i = vs.index(rng.choice(sorted(vs)))
                if not COND:
                    break
                sv = key(tau); t1 = dict(tau); t1[vs[i]] = arcs[i]; D.c_lfp(t1, cm, ct)
                bad = sum(ct) != tops or lab1() is None
                load(sv)
                if not bad:
                    break
            tau[vs[i]] = arcs[i]; D.c_lfp(tau, cm, ct); piv += 1
            if lab1() is None or lab1() != before:
                break
        if lab1() is None or not k:
            print(f"  base run ended / failed at lap {laps + lap + 1}"); break
    print(f"{os.path.basename(path)} n {n}: scan of {sum(vals.values())} laps from lap {J} (seed {S}): max exact eps {worst[0]:.4g} at lap "
          f"{worst[1]} (node 1 = {worst[2]}); distinct values (count): " +
          ", ".join(f"{k_} ({c_})" for k_, c_ in sorted(vals.items(), key=lambda x: -float(x[0]))))
    sys.exit(0)
p_fail, p_succ, nst, byfail, bestfail, maxheap = chain(dict(tau), l0, tops0)
seen = range(nst); sizes = [maxheap]
print(f"{os.path.basename(path)} n {n}: snapshot seed {S} pivot {piv} (lap {J} after W {W}); max frontier {sizes[0]}; "
      f"total states {len(seen)}")
print(f"  exact P(fail) = {float(p_fail):.6g}   P(success) = {float(p_succ):.6g}   sum = {float(p_fail + p_succ):.12g}")
for fk, pr in sorted(byfail.items(), key=lambda x: -x[1])[:8]:
    print(f"  failure mass {float(pr):.4g} from the pick {fk}")
if MAXPATH:
    print(f"  most probable failing path (probability {bestfail[0]:.4g}, {len(bestfail[1])} picks):")
    for st_ in bestfail[1]:
        print("    " + st_)
