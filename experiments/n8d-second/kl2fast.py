"""kl2.py with the least-fixed-point step (Algorithms 2-3) in C (lfp.c via ctypes). Everything else (Algorithm 1 driver,
admissible arcs, pivot rules R1/R2 incl. random.Random(seed).choice, arc choice, strategies, dual) is kl2.py's code, unchanged.
Use only after `kl2fast.py --selfcheck` and the family reproduction (README) pass. Same CLI as kl2.py."""
import array
import ctypes
import os
import random
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kl2  # noqa: E402

SRC = os.path.join(HERE, "lfp.c")
SO = os.path.join(HERE, "out", "lfp.so")


def _lib():
    if not os.path.exists(SO) or os.path.getmtime(SO) < os.path.getmtime(SRC):
        os.makedirs(os.path.dirname(SO), exist_ok=True)
        subprocess.run(["gcc", "-O2", "-shared", "-fPIC", "-o", SO + ".tmp", SRC], check=True)
        os.replace(SO + ".tmp", SO)
    lib = ctypes.CDLL(SO)
    P = ctypes.POINTER(ctypes.c_int)
    lib.kl_lfp.argtypes = [ctypes.c_int] * 4 + [P] * 8
    lib.kl_lfp.restype = ctypes.c_int
    lib.kl_adm.argtypes = [ctypes.c_int] * 4 + [P] * 9
    lib.kl_adm.restype = ctypes.c_int
    return lib


LIB = _lib()


def arr(xs):
    a = array.array("i", xs if len(xs) else [0])
    return (ctypes.c_int * len(a)).from_buffer(a)


class KLFast(kl2.KL):
    def __init__(self, prio, owner, succ, tau1="first"):
        super().__init__(prio, owner, succ, "min" if tau1 == "min" else "first")
        if tau1 == "last":                                    # box 2b: tau_1 = last successor in file order
            self.tau = {v: self.succ[v][-1] for v in self.odd_nodes}
        elif tau1.startswith("rand"):                         # box 2b: tau_1 drawn by its own generator, seed after 'rand'
            r = random.Random(int(tau1[4:]))
            self.tau = {v: r.choice(self.succ[v]) for v in self.odd_nodes}
        off, adj = [0], []
        for v in range(self.n):
            adj.extend(self.succ[v]); off.append(len(adj))
        self.c_pi, self.c_owner = arr(self.pi), arr(self.owner)
        self.c_off, self.c_adj, self.c_K = arr(off), arr(adj), arr(self.K)
        sadj = []
        for v in range(self.n):
            sadj.extend(sorted(self.succ[v]))
        self.c_sadj = arr(sadj)                       # successors in increasing id, for kl_adm (best_arc's sorted(ws))

    def c_lfp(self, tau, cm, ct):
        """mu <- mu^{G_tau up} in place on the C buffers."""
        ctau = arr([tau.get(v, -1) for v in range(self.n)])
        LIB.kl_lfp(self.n, self.h, self.d, self.ell, self.c_pi, self.c_owner, self.c_off, self.c_adj, ctau, self.c_K, cm, ct)

    def to_labels(self, cm, ct):
        h, fl, tp = self.h, list(cm), list(ct)
        return [None if tp[v] else tuple(fl[v * h:(v + 1) * h]) for v in range(self.n)]

    def run(self, rule="r1", seed=1, cap=10 ** 7, check=False):
        """kl2.KL.run line for line, with labels kept in C buffers and admissible()/best_arc() done by kl_adm."""
        if check:
            return super().run(rule, seed, cap, check)
        n = self.n
        tau = dict(self.tau)
        cm, ct = arr([0] * (n * self.h)), arr([0] * n)          # line 2: min L(T)
        self.c_lfp(tau, cm, ct)                                 # line 3
        rng = random.Random(seed) if rule == "r2" else None
        cand, carc = arr([0] * n), arr([0] * n)
        piv = 0
        while True:
            k = LIB.kl_adm(n, self.h, self.d, self.ell, self.c_pi, self.c_owner, self.c_off, self.c_sadj, self.c_K,
                           cm, ct, cand, carc)                  # line 4
            if not k:
                break
            if piv >= cap:
                raise RuntimeError(f"pivot cap {cap} reached")
            vs = list(cand[:k])
            i = 0 if rule == "r1" else vs.index(rng.choice(sorted(vs)))
            tau[vs[i]] = carc[i]                                # line 5
            self.c_lfp(tau, cm, ct)                             # line 6
            piv += 1
        return piv, tau, self.to_labels(cm, ct)

    def lfp(self, tau, mu):
        n, h = self.n, self.h
        flat, top = [], []
        z = self.zeros[h]
        for l in mu:
            if l is None:
                flat.extend(z); top.append(1)
            else:
                flat.extend(l); top.append(0)
        cm, ct = arr(flat), arr(top)
        ctau = arr([tau.get(v, -1) for v in range(n)])
        LIB.kl_lfp(n, h, self.d, self.ell, self.c_pi, self.c_owner, self.c_off, self.c_adj, ctau, self.c_K, cm, ct)
        fl, tp = list(cm), list(ct)
        return [None if tp[v] else tuple(fl[v * h:(v + 1) * h]) for v in range(n)]


kl2.KL = KLFast          # solve() and main() of kl2 now build KLFast

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--selfcheck":
        sys.argv = [sys.argv[0]] + sys.argv[2:]
        import selfcheck
        selfcheck.kl2 = kl2
        selfcheck.main()
    else:
        # kl2.main with --tau1 extended to first | min | last | rand<S> (box 2b); kl2.py itself is unchanged
        import argparse
        import time
        ap = argparse.ArgumentParser()
        ap.add_argument("game"); ap.add_argument("out", nargs="?")
        ap.add_argument("--rule", choices=["r1", "r2"], default="r1")
        ap.add_argument("--seed", type=int, default=1)
        ap.add_argument("--tau1", default="first")
        ap.add_argument("--check", action="store_true")
        a = ap.parse_args()
        g = kl2.pg.read(a.game)
        t0 = time.time()
        win, strat, pp, pd = kl2.solve(g, a.rule, a.seed, a.tau1, a.check)
        dt = time.time() - t0
        if a.out:
            kl2.pg.write_sol(win, a.out, strat)
        sys.stderr.write(f"pivots_primal {pp} pivots_dual {pd} time {dt:.3f}\n")
