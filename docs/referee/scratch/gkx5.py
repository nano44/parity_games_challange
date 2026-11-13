#!/usr/bin/env python3
"""REFEREE successor 37: direct tests of P-N5-EXP-fixes.md entry 4 (l-red-b 24f4d436) on this lane's own model.
SUPPLEMENTARY DATA of stage 5 (report section 13.6): entry 4 was reviewed and signed in stage 4 (section 12, successor 36); these
tests were written and run before the Lead's change of order reached this session, and are kept as a second, independent check.

Built on gkx.py (own transcription of the packet's TABLE, own IDEAL step from R104's definitions). The lane's b6prefix.py and
onep.py are NOT imported and were not opened. Every order bit used here is read from the DEFINITIONS, never from the packet's
formulas K1-K4 / V1-V4:
    C_i(s) := [key_s(v_i) < key_s(u_i)]                      (key tuples of the current options, s on the lower levels)
    E_i(s) := [B_s(v_i, s(v_i)) is better than B_s(u_i, s(u_i))]   (beta-sets of the X-chains, largest rank in the difference)
s+ := the s' of R104's step; s+ := s when the step's word is «opt» or «stuck» (report section 5.3 / fixes 4.1 (S2)).
Subcommands (one line per k; named must-0 counters; `ctrl` rows are firing controls):
  all k.. [--frozen]   LEMMA' (report l. 219-225 = fixes 4.4) at EVERY triple (j, a, t), 1 <= t <= L + 3, and every T of its
                       window: hypotheses evaluated literally (with the guards «if the run reaches»), conclusion (R1)-(R3).
                       --frozen: the RESPONSE LEMMA as frozen (packet l. 192-204) at every triple; it must FAIL at (1, 1, 2^k - 1).
  exh k.. [--ctrl c]   EVERY state with the wires and u_0 at option 0: (S1) closure, C_0 = E_0 = s(v_0), s+(v_0) = 1;
                       CAUSAL as a function; STABLE in step form with entry 4.2's «hence» and «consequently» clauses;
                       LEMMA' with s in the role of s_(t-1), along s, s+, (s+)+, ...
  arb k.. --n N --seed S [--ctrl c]   STABLE and LEMMA'-from-a-state on random states (planted rests; perturbed run states)
No absolute paths. Run with python3 -I.
"""
import sys, os, random, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gkx


def take(args, flag, n=1, default=None):
    if flag in args:
        i = args.index(flag)
        v = args[i + 1:i + 1 + n]
        del args[i:i + 1 + n]
        return (v if n > 1 else v[0]) if n else True
    return default


class Model:
    def __init__(self, k):
        self.k = k
        self.G, self.meta = gkx.rule(k)
        self.ix = self.meta["idx"]
        self.names = self.meta["names"]
        self.N = self.G["N"]
        self._plus, self._bits = {}, {}
        self.unit = {}
        for i in range(1, k):
            ns = [f"u{i}", f"v{i}", f"y{i}", f"yb{i}"]
            if 2 <= i <= k - 2:
                ns += [f"e{i}", f"yp{i}", f"ypb{i}"]
            self.unit[i] = [self.ix[n] for n in ns]
        self.U = {j: [x for i in range(j, k) for x in self.unit[i]] for j in range(1, k + 1)}
        self.fixed = [x for n, x in self.ix.items() if n == "u0" or n.startswith("w")]

    def plus(self, s):
        """(s+, word); s a tuple."""
        r = self._plus.get(s)
        if r is None:
            s2, word, _ = gkx.step(self.G, list(s))
            r = (s if s2 is None else tuple(s2), word)
            self._plus[s] = r
        return r

    def bits(self, s):
        """(C, E): lists indexed 0..k-1, from the definitions."""
        r = self._bits.get(s)
        if r is None:
            G, ix = self.G, self.ix
            key = gkx.keys_of_state(G, list(s))
            C, E = [], []
            for i in range(self.k):
                v, u = ix[f"v{i}"], ix[f"u{i}"]
                C.append(int(key[v] < key[u]))
                E.append(int(gkx.ahead_sets(G, gkx.Bset(G, s, v, s[v]), gkx.Bset(G, s, u, s[u]))))
            r = (C, E)
            self._bits[s] = r
        return r

    def rest(self, s, j, a):
        return gkx.rest(self.k, self.meta, s, j, a)

    def h1(self, s, j, a):
        if not self.rest(s, j, a):
            return False
        if not all(self.rest(s, i, 0) for i in range(j + 1, self.k)):
            return False
        C, E = self.bits(s)
        return C[j - 1] == a and E[j - 1] == a

    def last(self, j, t):
        return t + gkx.P(self.k, j) - 1 if j >= 2 else t + gkx.P(self.k, 1) - 2

    def sched(self, j, a, t, swap=False):
        sc, calls = {}, []
        lst = gkx.response(self.k, self.meta, j, a, t, sc, calls, swapFB=swap)
        assert lst == self.last(j, t)
        return sc


def lemma_from(M, traj, reach, j, a, t, sc, swapctl=False):
    """LEMMA' for the window (j, a, t) on the sequence traj (traj[tau] = s_tau, continued by s+ = s after a stop; reach = the
    largest tau that the sequence reaches as a run, i.e. the first tau with (s_tau)+ = s_tau). (H1) is assumed checked.
    Returns (Tmax, npairs, viol): Tmax = the largest T <= last with (H2'_T); npairs = number of T in [t, Tmax]; viol = number of
    those T at which the conclusion fails."""
    k, names = M.k, M.names
    c = 1 - a
    last = M.last(j, t)
    Uj = M.U[j]
    viol = npairs = 0
    Tmax = t - 1
    for T in range(t, last + 1):
        # (H2'_T), the clauses that are new at T: tau = T (key) and tau = T - 1 >= t (value); guards: the run reaches s_(T-1)
        if T - 1 <= reach:
            Cn = M.bits(traj[T])[0][j - 1]            # traj[T] = (s_(T-1))+
            if Cn != c:
                break
            if T - 1 >= t and M.bits(traj[T - 1])[1][j - 1] != c:
                break
        Tmax = T
        npairs += 1
        bad = 0
        if T > reach:                                  # (R2): the run reaches s_T
            bad = 1
        else:
            if traj[T] == traj[T - 1]:                 # (R2): the step changes a mover
                bad = 1
            real = sorted((names[x], traj[T][x]) for x in Uj if traj[T][x] != traj[T - 1][x])
            if real != sorted(sc.get(T, [])):          # (R1)
                bad = 1
            if T == last:                              # (R3)
                if j >= 2:
                    e = M.ix[M.meta["E"](j)]
                    if any(traj[tau][e] != a for tau in range(t - 1, last)) or traj[last][e] != c:
                        bad = 1
                if not M.rest(traj[last], j, c) or not all(M.rest(traj[last], i, 0) for i in range(j + 1, k)):
                    bad = 1
        viol += bad
    return Tmax, npairs, viol


def cmd_all(args):
    frozen = take(args, "--frozen", 0, False)
    ctrl = int(take(args, "--ctrl", 1, 0))            # control 2: the list with the observers F / B exchanged
    for k in map(int, args):
        M = Model(k)
        S, word = gkx.run(M.G)
        S = [tuple(s) for s in S]
        L = len(S) - 1
        ext = S + [S[L]] * (gkx.P(k, 1) + 8)           # the sequence continued beyond the stop: (s_L)+ = s_L
        # the windows of the recursion (the places where the proof applies the lemma)
        sc0, calls0 = {}, []
        gkx.response(k, M.meta, 1, 0, 1, sc0, calls0)
        expected = set((j, a, t) for (j, a, t, lst) in calls0)
        if not frozen:
            triples = h1n = h1only = windows = full = pairs = viol = 0
            wset = set()
            for j in range(1, k):
                for a in (0, 1):
                    for t in range(1, L + 4):
                        triples += 1
                        if t - 1 > L:                  # «the run reaches s_(t-1)» fails: LEMMA' claims nothing
                            continue
                        if not M.h1(S[t - 1], j, a):
                            continue
                        h1n += 1
                        Tmax, npairs, v = lemma_from(M, ext, L, j, a, t, M.sched(j, a, t, swap=(ctrl == 2)))
                        viol += v
                        pairs += npairs
                        if Tmax < t:
                            h1only += 1
                        else:
                            windows += 1
                            wset.add((j, a, t))
                            full += int(Tmax == M.last(j, t))
            print(f"all k {k} ctrl {ctrl} L {L} triples {triples} h1 {h1n} h1only {h1only} windows {windows} expected {len(expected)} "
                  f"notrec {len(wset ^ expected)} full {full} pairs {pairs} viol {viol}", flush=True)
        else:
            # the lemma AS FROZEN: (H1) under s_(t-1); (H2) the input is (c, c) under s_tau for every tau in [t, t + P_j - 1]
            # THAT THE RUN REACHES; conclusion: the run reaches s_(t+P_j-1) (j = 1: s_(t+P_1-2)), the listed moves, each step
            # changes a mover, the E(j) clause, the rest states.
            hyp = fails = 0
            where = []
            for j in range(1, k):
                for a in (0, 1):
                    c = 1 - a
                    for t in range(1, L + 2):          # s_(t-1) must exist for (H1) to be a statement
                        if not M.h1(S[t - 1], j, a):
                            continue
                        hi = t + gkx.P(k, j) - 1
                        ok = True
                        for tau in range(t, min(hi, L) + 1):
                            C, E = M.bits(S[tau])
                            if (C[j - 1], E[j - 1]) != (c, c):
                                ok = False
                                break
                        if not ok:
                            continue
                        hyp += 1
                        last = M.last(j, t)
                        bad = 0
                        if last > L:
                            bad = 1
                        else:
                            sc = M.sched(j, a, t)
                            for T in range(t, last + 1):
                                real = sorted((M.names[x], S[T][x]) for x in M.U[j] if S[T][x] != S[T - 1][x])
                                if real != sorted(sc.get(T, [])) or S[T] == S[T - 1]:
                                    bad = 1
                            if not M.rest(S[last], j, c) or not all(M.rest(S[last], i, 0) for i in range(j + 1, k)):
                                bad = 1
                        if bad:
                            fails += 1
                            where.append((j, a, t))
            want = [(1, 1, 2 ** k - 1)] + [(j, 0, 2 ** k - 1) for j in range(2, k)]
            print(f"all k {k} ctrl frozen L {L} frozen_hyp_holds {hyp} frozen_conclusion_fails {fails} at_1_1_2k-1 "
                  f"{int((1, 1, 2 ** k - 1) in where)} failset_is_expected {int(sorted(where) == sorted(want))} "
                  f"holds_minus_fails {hyp - fails} recursion_windows {len(expected)}", flush=True)


def state_tests(M, s, cnt, caus, ctrl=0, do_causal=True):
    """All per-state tests of exh / arb on the standing state s (a tuple)."""
    k, ix = M.k, M.ix
    sp, word = M.plus(s)
    C, E = M.bits(s)
    Cp, Ep = M.bits(sp)
    cnt["states"] += 1
    cnt["opt"] += int(word == "opt")
    cnt["stop"] += int(sp == s)
    cnt["clos"] += int(any(sp[x] != 0 for x in M.fixed))                       # (S1): s+ keeps the wires and u_0 at 0
    cnt["c0e0"] += int(C[0] != s[ix["v0"]]) + int(E[0] != s[ix["v0"]])         # K1 / V1 at level 0
    cnt["v0plus"] += int(sp[ix["v0"]] != 1)                                    # 4.6: s+(v_0) = 1 for every state
    if do_causal:
        for j in range(1, k):
            up = tuple(s[x] for x in M.U[j])
            upp = tuple(sp[x] for x in M.U[j])
            if ctrl == 3:
                key = (j, up, E[j - 1])                     # control: without the key bit
            elif ctrl == 4:
                key = (j, up, Cp[j - 1])                    # control: without the value bit
            elif ctrl == 5:
                key = (j, up, E[j - 1], C[j - 1])           # control: the key bit read under s
            else:
                key = (j, up, E[j - 1], Cp[j - 1])
            old = caus.get(key)
            if old is None:
                caus[key] = upp
            else:
                cnt["hits"] += 1
                cnt["loc"] += int(old != upp)
    # STABLE in step form (fixes 4.2)
    for i in range(1, k):
        for b in (0, 1):
            if not (M.rest(s, i, b) and E[i - 1] == b):
                continue
            moved = any(sp[x] != s[x] for x in M.unit[i])
            if C[i - 1] == b:                               # the frozen one-state reading (control)
                cnt["onestate_cases"] += 1
                cnt["onestate_moves"] += int(moved)
            if Cp[i - 1] != b:
                continue
            cnt["stcases"] += 1
            cnt["stviol"] += int(moved)                                          # s+ = s on unit i
            cnt["sthence"] += int(not M.rest(sp, i, b)) + int(Cp[i] != 0 if i <= k - 1 else 0) + int(E[i] != 0)
            if all(M.rest(s, m, 0) for m in range(i + 1, k)):
                cnt["stcons_cases"] += 1
                cnt["stcons"] += int(any(sp[x] != s[x] for x in M.U[i]))         # s+ = s on U_i
    # LEMMA' with s in the role of s_(t-1), t = 1, along s, s+, (s+)+, ...
    for j in range(1, k):
        for a in (0, 1):
            if not M.h1(s, j, a):
                continue
            last = M.last(j, 1)
            traj = [s]
            reach = None
            for tau in range(1, last + 2):
                nx, _ = M.plus(traj[-1])
                if nx == traj[-1] and reach is None:
                    reach = tau - 1
                traj.append(nx)
            if reach is None:
                reach = last + 1
            Tmax, npairs, v = lemma_from(M, traj, reach, j, a, 1, M.sched(j, a, 1, swap=(ctrl == 2)))
            if Tmax < 1:
                cnt["h1only"] += 1
                continue
            cnt["windows"] += 1
            cnt["full"] += int(Tmax == last)
            cnt["proper"] += int(Tmax < last)
            cnt["steps"] += npairs
            cnt["pviol"] += v
            if ctrl == 1 and Tmax < last:
                # control: the list demanded one step beyond the hypothesis
                T = Tmax + 1
                real = sorted((M.names[x], traj[T][x]) for x in M.U[j] if traj[T][x] != traj[T - 1][x])
                cnt["ctrl1"] += int(real != sorted(M.sched(j, a, 1).get(T, [])) or T > reach)


CN = ("states", "opt", "stop", "clos", "c0e0", "v0plus", "hits", "loc", "stcases", "stviol", "sthence", "stcons_cases", "stcons",
      "onestate_cases", "onestate_moves", "h1only", "windows", "full", "proper", "steps", "pviol", "ctrl1")

def fmtc(cnt, skip=()):
    return " ".join(f"{c} {cnt[c]}" for c in CN if c not in skip)


def cmd_exh(args):
    ctrl = int(take(args, "--ctrl", 1, 0))
    for k in map(int, args):
        M = Model(k)
        free = [x for x in range(M.N) if x not in M.fixed]
        cnt = {c: 0 for c in CN}
        caus = {}
        for bits in itertools.product((0, 1), repeat=len(free)):
            s = [0] * M.N
            for x, b in zip(free, bits):
                s[x] = b
            state_tests(M, tuple(s), cnt, caus, ctrl)
        print(f"exh k {k} ctrl {ctrl} lockeys {len(caus)} " + fmtc(cnt, () if ctrl == 1 else ("ctrl1",)), flush=True)


def cmd_arb(args):
    ctrl = int(take(args, "--ctrl", 1, 0))
    n = int(take(args, "--n", 1, 300))
    seed = int(take(args, "--seed", 1, 1))
    for k in map(int, args):
        M = Model(k)
        rnd = random.Random(seed * 1000 + k)
        S, _ = gkx.run(M.G)
        cnt = {c: 0 for c in CN}
        caus = {}
        below = lambda j: [x for x in range(M.N) if x not in M.fixed and x not in M.U[j]]
        for it in range(n):
            j = rnd.randrange(1, k)
            if it % 2 == 0:
                # a planted rest: REST_j(a), REST_i(0) above, everything below unit j random
                a = rnd.randrange(2)
                s = [0] * M.N
                for x in below(j):
                    s[x] = rnd.randrange(2)
                for i in range(j, k):
                    b = a if i == j else 0
                    g = lambda nm: M.ix[nm]
                    s[g(f"u{i}")] = s[g(f"v{i}")] = b
                    s[g(f"y{i}")], s[g(f"yb{i}")] = b, 1 - b
                    if 2 <= i <= k - 2:
                        s[g(f"e{i}")] = b
                        s[g(f"yp{i}")], s[g(f"ypb{i}")] = b, 1 - b
            else:
                # a state of the run with 1..3 movers below unit j flipped
                s = list(S[rnd.randrange(len(S))])
                bl = below(j)
                for x in rnd.sample(bl, min(len(bl), rnd.randrange(1, 4))):
                    s[x] = 1 - s[x]
            state_tests(M, tuple(s), cnt, caus, ctrl, do_causal=False)
        print(f"arb k {k} ctrl {ctrl} seed {seed} n {n} " + fmtc(cnt, ("hits", "loc") + (() if ctrl == 1 else ("ctrl1",))), flush=True)


if __name__ == "__main__":
    cmd, args = sys.argv[1], sys.argv[2:]
    {"all": cmd_all, "exh": cmd_exh, "arb": cmd_arb}[cmd](args)
