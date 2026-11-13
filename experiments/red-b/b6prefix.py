#!/usr/bin/env python3
"""L-RED-B packet P-N5-EXP, fixes entry 4 (REFEREE-2 41's G-1; REFEREE 36's E-1, E-2, E-4, E-5) and entry 5 (ties, widths):
DIRECT TESTS of the RESPONSE LEMMA as RESTATED in docs/red-b/P-N5-EXP-fixes.md entry 4 (prefix form), of Lemma LOC, of STABLE in
step form and of the standing assumption, on G_k = gk.build(k) with the model simulator onep.py. No other lane's file is needed.

Standing assumption (entry 4, S1): every wire and u_0 at option 0. s_tau := the tau-th iterate of the IDEAL step from the start
state (the step map is applied also after the run has stopped: then s_tau repeats).
PREFIX FORM (unit j, 1 <= j <= k-1; a in {0, 1}; c = 1 - a; t >= 1; s_tau := the tau-th iterate of the IDEAL step from the
start state; window [t, e], e = t + P_j - 1 for j >= 2 and t + P_1 - 2 for j = 1, P_j = 2^(k+1-j) - 1):
  (H1)  under s_(t-1): REST_j(a), REST_i(0) for every i > j, and the input (C_(j-1), E_(j-1)) of unit j is (a, a);
  (H2p) for a tau0 in the window: C_(j-1)(s_tau) = c for t <= tau <= tau0 and E_(j-1)(s_tau) = c for t <= tau <= tau0 - 1.
  Then in the steps t, ..., tau0 the movers of the units j, ..., k-1 move exactly as the frozen lemma lists (so every one of
  these steps changes a mover).
All orders are read off the simulator (onep.py): C_i(s) = [key_s(v_i) < key_s(u_i)], E_i(s) = [value_s(v_i) > value_s(u_i)];
the list is generated recursively from the lemma's text (the same generator as b6lemma.py's sched).

Modes (each prints one line per k; every counter named «must 0» is a must-0 counter, the others are descriptive):
  run k ...                 the run of G_k from its start; UNIT: a response window (j, t, a) of the proof's recursion
                            (2^(j-1) windows of unit j), resp. a (window, step) pair.
        h1     (must 0) windows whose (H1) fails under s_(t-1)
        h2     (must 0) (window, tau): C_(j-1)(s_tau) != c for a tau in [t, e], or E_(j-1)(s_tau) != c for a tau in [t, e-1]
        h2last (must 0) windows with E_(j-1)(s_e) != c (the frozen (H2) also asks for it; the prefix form does not use it)
        psched (must 0) (window, tau0): the moves of the units >= j in step tau0 differ from the list
        empty  (must 0) (window, tau): the list has no move in step tau
  all k ...                 EVERY triple (j, a, t), 1 <= t <= T + 3, on s_tau = Phi^tau(s_0) continued beyond the stop of the run
                            (s_tau = s_T for tau >= T; T = L(G_k)). UNIT: a triple with (H1) under s_(t-1).
        h1only          triples with (H1) whose (H2[t]) fails (C_(j-1)(s_t) != c): the restated lemma claims nothing there;
                        REFEREE 36's instance E-1, (j, a, t) = (1, 1, 2^k - 1), is one of them
        windows         triples with (H1) and (H2[t]); expected = 2^(k-1) - 1 (the windows of the recursion)
        aviol  (must 0) (window, tau <= tau0): step tau is not a step of the run (tau > T) or the moves of the units >= j differ
                        from the list
        control B6X_CTRL=5: the lemma AS FROZEN (its (H2) only over the tau «that the run reaches», so vacuous at t = T + 1):
                        frozen_conclusion_fails must fire, at (1, 1, 2^k - 1) and at (j, 0, 2^k - 1), j >= 2
  exh k ...                 EXHAUSTIVE (k = 3, 4): EVERY state with every wire and u_0 at option 0 (2^9 states at k = 3, 2^16 at
                            k = 4). UNIT: a state, resp. a (state, unit, bit) case, resp. a window that begins at a state.
        c0e0   (must 0) states where C_0(s) != s(v_0) or E_0(s) != s(v_0)
        loc    (must 0) states s whose triple (upper part of s, E_(j-1)(s), C_(j-1)(step(s))) has two different upper parts of
                        step(s), summed over j (LOC as a FUNCTION, checked on all states); lockeys = number of triples
        stviol (must 0) STABLE in step form, all cases (stcases); onestate_cases / onestate_moves: the frozen reading (control)
        pviol  (must 0) the restated lemma with s in the role of s_(t-1), for every state s and every (j, a) with (H1) under s
                        and C_(j-1)(step(s)) = c: (window, tau <= tau0) where the moves of the units >= j differ from the list;
                        windows, full, proper, steps as in mode off; h1only = (state, j, a) with (H1) and C_(j-1)(step(s)) != c
        controls B6X_CTRL=3 / 4: LOC's triple without C_(j-1)(step(s)) / without E_(j-1)(s): loc must fire
  stable k seed n           STABLE in STEP FORM (REFEREE 36's E-5). UNIT: (state s, unit i, b) with REST_i(b) under s and
                            E_(i-1)(s) = b; states: one third from the run, two thirds random with a planted rest (wires, u_0 at 0).
        stviol (must 0) cases with C_(i-1)(s') = b, s' = step(s), in which a mover of unit i moves
        onestate_cases / onestate_moves: the frozen one-state reading (C_(i-1)(s) = b): a firing control (moves > 0)
  u0 k seed n               REFEREE 36's E-4. UNIT: a random state with every wire at 0.
        c0e0   (must 0) states with u_0 at 0 where C_0(s) != s(v_0) or E_0(s) != s(v_0)
        c0e0_u0free     the same count with u_0 random: a firing control
  off k seed n              n start states off the run (every wire and u_0 at option 0; planted: a unit j at rest a with the units above
                            at rest 0 and a random lower part; or a state of the run with 1..3 lower movers flipped; or the
                            state before a window of the run with 1..2 movers below unit j - 1 flipped; or a splice: the
                            units >= j - 1 from the state before a window of unit j of the run, the rest from another state
                            of the run; one quarter of the starts each), each iterated
                            cap steps; UNIT: every (t, j, a) with (H1) under s_(t-1) and C_(j-1)(s_t) = c (a window that begins),
                            tau0 := the largest tau in the window for which (H2p) holds.
        pviol  (must 0) (window, tau <= tau0): the moves of the units >= j in step tau differ from the list
        windows, proper (tau0 < e: the hypothesis fails inside the window), full, properlen (sum of tau0 - t + 1 over the
        proper windows), maxproper (the longest), steps (checked), byunit (windows of unit 1, ..., k-1)
        control B6X_CTRL=1: also demand the list at step tau0 + 1 when tau0 < e (the hypothesis one step short): must fire
        control B6X_CTRL=2: the list with the two observers of every pair exchanged: must fire
  drive k seed n            the DRIVEN form (long proper prefixes). UNIT: a window (j, t, a) of the run of G_k, started from the
                            run's own state s_(t-1), in which the part below unit j is disturbed by hand: z_tau := step(z'_(tau-1)),
                            z'_(tau-1) := z_(tau-1) with 1..3 movers below unit j flipped (never a wire, never u_0, never a mover
                            of the units >= j) at a random time d in the window and, after it, at every step with probability 0.2.
                            Inputs: C_(j-1)(z_tau) and E_(j-1)(z'_(tau-1)); tau0 := the last step up to which they are c.
        dviol  (must 0) (window, tau <= tau0): the moves of the units >= j in the step z'_(tau-1) -> z_tau differ from the list
        windows, full, proper, properlen, maxproper, steps, byunit as in mode off
        control B6X_CTRL=1: also demand the list at the first step whose input is not (c, c): must fire
  loc k seed pool n         the DEPENDENCE claim behind the prefix form (Lemma LOC). UNIT: a random state s with every wire and
                            u_0 at 0. For each
                            unit j: the restriction of s' = step(s) to the movers of the units >= j must be a function of
                            (s restricted to the units >= j, E_(j-1)(s), C_(j-1)(s')).
        loc    (must 0) pairs (j, key) seen with two different restrictions of s'
        keys, hits (states whose key was seen before: the test is not vacuous)
        control B6X_CTRL=3: the key without C_(j-1)(s'); B6X_CTRL=4: the key without E_(j-1)(s): each must fire
  tie k ...                 the br tie-break (fixes entry 5): the wire options tie in the rule's rank key; the generator breaks
                            ties by beta-id. UNIT: genome. tied = adjacent tied pairs in the sorted rank key; rundiff (must 0) =
                            [the run with the ties broken the OTHER way (larger beta-id first) differs state by state]; member2 =
                            br of the variant is a bijection onto 0..M-1.
  width k ...               the number of movers on each level 0..k of G_k (fixes entry 5), descriptive.
"""
import sys, os, random
import onep, gk

CTRL = os.environ.get("B6X_CTRL", "0")


class Fam:
    def __init__(self, k, G=None, names=None):
        self.k = k
        if G is None:
            G, names = gk.build(k)
        self.G, self.names = G, names
        self.ix = {n: i for i, n in enumerate(names)}
        self.P = onep.OneP(G)
        ix = self.ix
        self.unit = {}
        for j in range(1, k):
            ms = [f"u{j}", f"v{j}", f"y{j}", f"yb{j}"]
            if 2 <= j <= k - 2:
                ms += [f"e{j}", f"yp{j}", f"ypb{j}"]
            self.unit[j] = [ix[n] for n in ms]
        self.upper = {j: sorted(x for i in range(j, k) for x in self.unit[i]) for j in range(1, k)}
        self.wires = [ix[n] for n in names if n.startswith("w")]
        self.u0 = ix["u0"]                                   # standing assumption: every wire and u_0 at option 0
        self.lower = {j: sorted(x for x in range(G["N"]) if x not in set(self.upper[j]) and x not in set(self.wires)
                                and x != self.u0) for j in range(1, k)}
        self.Pj = {j: 2 ** (k + 1 - j) - 1 for j in range(1, k)}

    def end(self, j, t):
        return t + self.Pj[j] - 1 if j >= 2 else t + self.Pj[1] - 2

    def orders(self, s):
        """C[i], E[i] for i = 0..k-1, read off the simulator"""
        key = self.P.keys(s)
        mv, _ = self.P.values(s)
        ix = self.ix
        C = [int(key[ix[f"v{i}"]] < key[ix[f"u{i}"]]) for i in range(self.k)]
        E = [int(mv[ix[f"v{i}"]] > mv[ix[f"u{i}"]]) for i in range(self.k)]
        return C, E

    def rest(self, s, j, a):
        ix, k = self.ix, self.k
        o = lambda n: s[ix[n]]
        if not (o(f"u{j}") == a and o(f"v{j}") == a and o(f"y{j}") == a and o(f"yb{j}") == 1 - a):
            return False
        if 2 <= j <= k - 2:
            return o(f"e{j}") == a and o(f"yp{j}") == a and o(f"ypb{j}") == 1 - a
        return True

    def h1(self, s, CE, j, a):
        C, E = CE
        return self.rest(s, j, a) and all(self.rest(s, i, 0) for i in range(j + 1, self.k)) and C[j - 1] == a and E[j - 1] == a

    def resp(self, j, t, a, sched, wins=None):
        """the lemma's list for a response of unit j beginning at step t from rest a; returns the last step"""
        k = self.k
        cc = 1 - a

        def add(tt, n, opt):
            sched.setdefault(tt, set()).add((n, opt))

        add(t, f"v{j}", cc)
        f, g = (f"yb{j}", f"y{j}") if a == 0 else (f"y{j}", f"yb{j}")
        if CTRL == "2":
            f, g = g, f
        if j == k - 1:
            add(t + 1, g, 1)
            add(t + 2, f"u{j}", cc)
            add(t + 2, f, 0)
            last = t + 2
        else:
            add(t + 1, f, 0)
            t1 = self.resp(j + 1, t, 0, sched, wins)
            add(t1, g, 1)
            add(t1 + 1, f"u{j}", cc)
            hasp = 2 <= j <= k - 2
            if hasp:
                fp, gp = (f"ypb{j}", f"yp{j}") if a == 0 else (f"yp{j}", f"ypb{j}")
                if CTRL == "2":
                    fp, gp = gp, fp
                add(t1 + 1, fp, 0)
            t2 = self.resp(j + 1, t1 + 1, 1, sched, wins)
            if hasp:
                add(t2, gp, 1)
                add(t2 + 1, f"e{j}", cc)
                last = t2 + 1
            else:
                last = t2
        if wins is not None:
            wins.append((j, t, a, last))
        return last

    def moves(self, p, q, j):
        """the (name, new option) of the movers of the units >= j that differ between p and q"""
        return {(self.names[x], q[x]) for x in self.upper[j] if p[x] != q[x]}

    def traj(self, s, cap):
        S = [tuple(s)]
        for _ in range(cap):
            S.append(self.P.step(S[-1], "key"))          # the iterated step map (a stopped run repeats its last state)
        return S


def mode_run(k):
    F = Fam(k)
    S = F.P.run("key")
    T = len(S) - 1
    wins = []
    F.resp(1, 1, 0, {}, wins)
    CE = [F.orders(s) for s in S]
    c = dict(h1=0, h2=0, h2last=0, psched=0, empty=0)
    pairs = 0
    for (j, t, a, last) in wins:
        cc = 1 - a
        assert last == F.end(j, t)
        if last > T or not F.h1(S[t - 1], CE[t - 1], j, a):
            c["h1"] += 1
            continue
        sched = {}
        F.resp(j, t, a, sched)
        for tau in range(t, last + 1):
            pairs += 1
            c["h2"] += int(CE[tau][0][j - 1] != cc) + int(tau < last and CE[tau][1][j - 1] != cc)
            c["empty"] += int(not sched.get(tau))
            c["psched"] += int(F.moves(S[tau - 1], S[tau], j) != sched.get(tau, set()))
        c["h2last"] += int(CE[last][1][j - 1] != cc)
    print(f"G_{k} mode run ctrl {CTRL} T {T} windows {len(wins)} pairs {pairs} h1 {c['h1']} h2 {c['h2']} h2last {c['h2last']} "
          f"psched {c['psched']} empty {c['empty']}", flush=True)


def mode_off(k, seed, n):
    F = Fam(k)
    rng = random.Random(seed)
    Srun = F.P.run("key")
    wins = []
    F.resp(1, 1, 0, {}, wins)
    cap = 2 ** (k + 1) + 8
    pviol = windows = proper = full = steps = ctrlfire = maxproper = 0
    byu = {j: 0 for j in range(1, k)}
    properlen = 0
    for it in range(n):
        if it % 4 == 0:                                   # planted rest + random lower part
            j = rng.randint(1, k - 1)
            a = rng.randint(0, 1)
            s = [0] * F.G["N"]
            for i in range(j, k):
                b = a if i == j else 0
                s[F.ix[f"u{i}"]] = s[F.ix[f"v{i}"]] = b
                s[F.ix[f"y{i}"]] = b
                s[F.ix[f"yb{i}"]] = 1 - b
                if 2 <= i <= k - 2:
                    s[F.ix[f"e{i}"]] = b
                    s[F.ix[f"yp{i}"]] = b
                    s[F.ix[f"ypb{i}"]] = 1 - b
            for x in F.lower[j]:
                s[x] = rng.randint(0, 1)
        elif it % 4 == 1:                                 # a state of the run with 1..3 lower movers flipped
            s = list(Srun[rng.randrange(len(Srun))])
            j = rng.randint(1, k - 1)
            for x in rng.sample(F.lower[j], min(len(F.lower[j]), rng.randint(1, 3))):
                s[x] = 1 - s[x]
        elif it % 4 == 3:                                 # the state before a window of the run, 1..2 movers two units below flipped
            j, t, a, _ = wins[rng.randrange(len(wins))]
            s = list(Srun[t - 1])
            low = F.lower[j - 1] if j >= 2 else F.lower[1]
            for x in rng.sample(low, min(len(low), rng.randint(1, 2))):
                s[x] = 1 - s[x]
        else:                                             # splice: the units >= j - 1 from the state before a window of unit j of
            j, t, a, _ = wins[rng.randrange(len(wins))]   # the run, everything below from another state of the run
            s = list(Srun[t - 1])
            other = Srun[rng.randrange(len(Srun))]
            for x in (F.lower[j - 1] if j >= 2 else F.lower[1]):
                s[x] = other[x]
        S = F.traj(s, cap)
        CE = [F.orders(z) for z in S]
        for t in range(1, len(S)):
            for jj in range(1, k):
                for aa in (0, 1):
                    cc = 1 - aa
                    if not F.h1(S[t - 1], CE[t - 1], jj, aa) or CE[t][0][jj - 1] != cc:
                        continue
                    e = F.end(jj, t)
                    tau0 = t
                    while tau0 < e and tau0 + 1 < len(S) and CE[tau0 + 1][0][jj - 1] == cc and CE[tau0][1][jj - 1] == cc:
                        tau0 += 1
                    if tau0 < e and tau0 + 1 >= len(S):
                        continue                          # the trajectory was cut by the cap: not counted
                    sched = {}
                    F.resp(jj, t, aa, sched)
                    windows += 1
                    byu[jj] += 1
                    if tau0 < e:
                        proper += 1
                        properlen += tau0 - t + 1
                        maxproper = max(maxproper, tau0 - t + 1)
                    else:
                        full += 1
                    for tau in range(t, tau0 + 1):
                        steps += 1
                        pviol += int(F.moves(S[tau - 1], S[tau], jj) != sched.get(tau, set()))
                    if CTRL == "1" and tau0 < e:
                        ctrlfire += int(F.moves(S[tau0], S[tau0 + 1], jj) != sched.get(tau0 + 1, set()))
    extra = f" ctrl1 {ctrlfire}" if CTRL == "1" else ""
    print(f"G_{k} mode off ctrl {CTRL} seed {seed} starts {n} cap {cap} windows {windows} full {full} proper {proper} "
          f"properlen {properlen} maxproper {maxproper} steps {steps} pviol {pviol}{extra} byunit {' '.join(str(byu[j]) for j in range(1, k))}", flush=True)


def mode_loc(k, seed, pool, n):
    F = Fam(k)
    rng = random.Random(seed)
    N = F.G["N"]
    seen = {}
    loc = hits = 0
    for j in range(1, k):
        ups = [[rng.randint(0, 1) for _ in F.upper[j]] for _ in range(pool)]
        for it in range(n):
            s = [0] * N
            up = ups[rng.randrange(pool)]
            for x, b in zip(F.upper[j], up):
                s[x] = b
            for x in F.lower[j]:
                s[x] = rng.randint(0, 1)
            s = tuple(s)
            s2 = F.P.step(s, "key")
            _, E = F.orders(s)
            C2, _ = F.orders(s2)
            key = (j, tuple(up), E[j - 1] if CTRL != "4" else None, C2[j - 1] if CTRL != "3" else None)
            out = tuple(s2[x] for x in F.upper[j])
            if key in seen:
                hits += 1
                if seen[key] != out:
                    loc += 1
            else:
                seen[key] = out
    print(f"G_{k} mode loc ctrl {CTRL} seed {seed} pool {pool} states {n * (k - 1)} keys {len(seen)} hits {hits} loc {loc}", flush=True)


def mode_tie(k):
    G, names = gk.build(k)
    N = G["N"]
    # the rule's rank key (-depth, delta) is recovered from br: two options tie iff they are wire options of equal delta
    wire = [n.startswith("w") for n in names]
    # the generator's order: by (key, beta-id); adjacent tied pairs = consecutive ranks that are wire options of the same
    # kind (wv / wu) and the same option number (equal delta)
    byrank = sorted(range(2 * N), key=lambda b: G["br"][b])
    cls = lambda b: (names[b // 2][:2], b % 2) if wire[b // 2] else None
    tied = sum(1 for p, q in zip(byrank, byrank[1:]) if cls(p) is not None and cls(p) == cls(q))
    # the variant: every maximal tied block reversed (larger beta-id first)
    br2 = list(G["br"])
    i = 0
    while i < 2 * N:
        jn = i
        while jn + 1 < 2 * N and cls(byrank[i]) is not None and cls(byrank[jn + 1]) == cls(byrank[i]):
            jn += 1
        blk = byrank[i:jn + 1]
        for r, b in zip(range(i, jn + 1), reversed(blk)):
            br2[b] = r
        i = jn + 1
    G2 = dict(G)
    G2["br"] = br2
    member2 = int(sorted(br2) == list(range(2 * N)))
    S1 = onep.OneP(G).run("key")
    S2 = onep.OneP(G2).run("key")
    print(f"G_{k} mode tie ctrl {CTRL} N {N} tied {tied} formula {max(0, 4 * k - 14)} changed {sum(1 for x, y in zip(G['br'], br2) if x != y)} "
          f"member2 {member2} T {len(S1) - 1} T2 {len(S2) - 1} rundiff {int(S1 != S2)}", flush=True)


def mode_drive(k, seed, n):
    F = Fam(k)
    rng = random.Random(seed)
    Srun = F.P.run("key")
    wins = []
    F.resp(1, 1, 0, {}, wins)
    dviol = windows = proper = full = steps = ctrlfire = maxproper = properlen = h1fail = 0
    byu = {j: 0 for j in range(1, k)}
    for it in range(n):
        j, t, a, e = wins[rng.randrange(len(wins))]
        cc = 1 - a
        low = F.lower[j]
        z = Srun[t - 1]
        if not F.h1(z, F.orders(z), j, a):
            h1fail += 1
            continue
        d = rng.randint(t, e)                             # first intervention: on z_d, before step d + 1 (d = e: none)
        sched = {}
        F.resp(j, t, a, sched)
        tau0 = None
        prev = z
        ok = True
        for tau in range(t, e + 1):
            zp = list(prev)                               # z'_(tau-1): z_(tau-1) with lower movers flipped (never a wire, never
            if tau - 1 >= d and (tau - 1 == d or rng.random() < 0.2):      # a mover of the units >= j)
                for x in rng.sample(low, min(len(low), rng.randint(1, 3))):
                    zp[x] = 1 - zp[x]
            zp = tuple(zp)
            _, Ein = F.orders(zp)
            cur = F.P.step(zp, "key")
            Cin, _ = F.orders(cur)
            good = Cin[j - 1] == cc and (tau == t or Ein[j - 1] == cc)
            if not good:
                if CTRL == "1":
                    ctrlfire += int(F.moves(prev, cur, j) != sched.get(tau, set()))
                break
            tau0 = tau
            steps += 1
            dviol += int(F.moves(prev, cur, j) != sched.get(tau, set()))
            prev = cur
        if tau0 is None:
            continue
        windows += 1
        byu[j] += 1
        if tau0 < e:
            proper += 1
            properlen += tau0 - t + 1
            maxproper = max(maxproper, tau0 - t + 1)
        else:
            full += 1
    extra = f" ctrl1 {ctrlfire}" if CTRL == "1" else ""
    print(f"G_{k} mode drive ctrl {CTRL} seed {seed} tries {n} h1fail {h1fail} windows {windows} full {full} proper {proper} "
          f"properlen {properlen} maxproper {maxproper} steps {steps} dviol {dviol}{extra} byunit {' '.join(str(byu[j]) for j in range(1, k))}", flush=True)


def mode_all(k):
    """every (j, a, t), not only the windows of the recursion; the iterated step map beyond the stop of the run"""
    F = Fam(k)
    Srun = F.P.run("key")
    T = len(Srun) - 1
    S = F.traj(F.G["start"], T + 4)                       # s_tau = Phi^tau(s_0), tau = 0 .. T + 4 (s_tau = s_T from T on)
    assert S[:T + 1] == [tuple(z) for z in Srun]
    CE = [F.orders(z) for z in S]
    aviol = windows = h1only = steps = orig = origfire = 0
    fails = []
    for t in range(1, len(S) - 1):
        for j in range(1, k):
            for a in (0, 1):
                cc = 1 - a
                if not F.h1(S[t - 1], CE[t - 1], j, a):
                    continue
                e = F.end(j, t)
                sched = {}
                F.resp(j, t, a, sched)
                if CTRL == "5":
                    # the lemma AS FROZEN: (H2) asks for the input (c, c) under s_tau only for the tau in [t, e] that the run
                    # reaches (tau <= T); if it holds (also vacuously), the frozen conclusion is demanded: the run reaches s_e
                    # and the steps t .. e are the listed ones
                    if t - 1 <= T and all(CE[tau][0][j - 1] == cc and CE[tau][1][j - 1] == cc for tau in range(t, min(e, T) + 1)):
                        orig += 1
                        bad = e > T or any(F.moves(S[tau - 1], S[tau], j) != sched.get(tau, set()) for tau in range(t, e + 1))
                        origfire += int(bad)
                        if bad:
                            fails.append(f"({j},{a},{t})")
                    continue
                if CE[t][0][j - 1] != cc:
                    h1only += 1                           # (H1) holds, (H2[tau0]) fails already at tau0 = t: no claim
                    continue
                tau0 = t
                while tau0 < e and tau0 + 1 < len(S) and CE[tau0 + 1][0][j - 1] == cc and CE[tau0][1][j - 1] == cc:
                    tau0 += 1
                windows += 1
                for tau in range(t, tau0 + 1):
                    steps += 1
                    aviol += int(tau > T or F.moves(S[tau - 1], S[tau], j) != sched.get(tau, set()))
    if CTRL == "5":
        print(f"G_{k} mode all ctrl 5 T {T} frozen_hyp_holds {orig} frozen_conclusion_fails {origfire} at(j,a,t) {' '.join(fails)}", flush=True)
    else:
        print(f"G_{k} mode all ctrl {CTRL} T {T} triples {(len(S) - 2) * (k - 1) * 2} h1only {h1only} windows {windows} "
              f"expected {2 ** (k - 1) - 1} steps {steps} aviol {aviol}", flush=True)


def mode_stable(k, seed, n):
    """STABLE in STEP FORM: REST_i(b) under s, E_(i-1)(s) = b and C_(i-1)(s') = b  =>  no mover of unit i moves in s -> s'"""
    F = Fam(k)
    rng = random.Random(seed)
    N = F.G["N"]
    Srun = F.P.run("key")
    cases = stviol = onestate = onefire = 0
    pool = [tuple(z) for z in Srun]
    for it in range(n):
        if it % 3 == 0:
            s = list(pool[rng.randrange(len(pool))])
        else:
            s = [rng.randint(0, 1) for _ in range(N)]
            i = rng.randint(1, k - 1)
            b = rng.randint(0, 1)
            s[F.ix[f"u{i}"]] = s[F.ix[f"v{i}"]] = b
            s[F.ix[f"y{i}"]] = b
            s[F.ix[f"yb{i}"]] = 1 - b
            if 2 <= i <= k - 2:
                s[F.ix[f"e{i}"]] = b
                s[F.ix[f"yp{i}"]] = b
                s[F.ix[f"ypb{i}"]] = 1 - b
        for x in F.wires:
            s[x] = 0
        s[F.u0] = 0
        s = tuple(s)
        s2 = F.P.step(s, "key")
        C, E = F.orders(s)
        C2, _ = F.orders(s2)
        for i in range(1, k):
            for b in (0, 1):
                if not F.rest(s, i, b) or E[i - 1] != b:
                    continue
                moved = any(s[x] != s2[x] for x in F.unit[i])
                if C2[i - 1] == b:                        # the step form's hypothesis
                    cases += 1
                    stviol += int(moved)
                if C[i - 1] == b:                         # the frozen one-state reading: input (b, b) under s
                    onestate += 1
                    onefire += int(moved)
    print(f"G_{k} mode stable ctrl {CTRL} seed {seed} states {n} cases {cases} stviol {stviol} onestate_cases {onestate} "
          f"onestate_moves {onefire}", flush=True)


def mode_u0(k, seed, n):
    """the level-0 formulas C_0(s) = E_0(s) = s(v_0) (K1, V1) need u_0 at option 0"""
    F = Fam(k)
    rng = random.Random(seed)
    N = F.G["N"]
    fix = free = 0
    for it in range(n):
        s = [rng.randint(0, 1) for _ in range(N)]
        for x in F.wires:
            s[x] = 0
        for u0 in (0, None):
            z = list(s)
            if u0 is not None:
                z[F.u0] = 0
            C, E = F.orders(tuple(z))
            bad = int(C[0] != z[F.ix["v0"]] or E[0] != z[F.ix["v0"]])
            if u0 is not None:
                fix += bad
            else:
                free += bad
    print(f"G_{k} mode u0 ctrl {CTRL} seed {seed} states {n} c0e0 {fix} c0e0_u0free {free}", flush=True)


def mode_exh(k):
    """EVERY state with every wire and u_0 at option 0 (2^(N - #wires - 1) states): LOC, STABLE (step form), c0e0, and the
    restated lemma on the trajectory from every state"""
    F = Fam(k)
    N = F.G["N"]
    free = [x for x in range(N) if x not in set(F.wires) and x != F.u0]
    nst = 1 << len(free)
    pos = {x: i for i, x in enumerate(free)}

    def state(code):
        s = [0] * N
        for i, x in enumerate(free):
            s[x] = (code >> i) & 1
        return tuple(s)

    def code(s):
        return sum(s[x] << pos[x] for x in free)

    nxt = [0] * nst
    CE = [None] * nst
    for c in range(nst):
        s = state(c)
        CE[c] = F.orders(s)
        nxt[c] = code(F.P.step(s, "key"))
    c0e0 = sum(1 for c in range(nst) if CE[c][0][0] != state(c)[F.ix["v0"]] or CE[c][1][0] != state(c)[F.ix["v0"]])
    # LOC: for each j the upper part of step(s) is a function of (upper part of s, E_(j-1)(s), C_(j-1)(step(s)))
    loc = lockeys = 0
    for j in range(1, k):
        seen = {}
        for c in range(nst):
            s = state(c)
            s2 = state(nxt[c])
            key = (tuple(s[x] for x in F.upper[j]), CE[c][1][j - 1] if CTRL != "4" else None,
                   CE[nxt[c]][0][j - 1] if CTRL != "3" else None)
            o = tuple(s2[x] for x in F.upper[j])
            if seen.setdefault(key, o) != o:
                loc += 1
        lockeys += len(seen)
    # STABLE, step form, and the one-state reading as a control
    cases = stviol = one = onemoves = 0
    for c in range(nst):
        s = state(c)
        s2 = state(nxt[c])
        C, E = CE[c]
        C2 = CE[nxt[c]][0]
        for i in range(1, k):
            for b in (0, 1):
                if F.rest(s, i, b) and E[i - 1] == b:
                    moved = any(s[x] != s2[x] for x in F.unit[i])
                    if C2[i - 1] == b:
                        cases += 1
                        stviol += int(moved)
                    if C[i - 1] == b:
                        one += 1
                        onemoves += int(moved)
    # the restated lemma from every state: s plays s_(t-1); the list is generated with t = 1
    windows = proper = full = steps = pviol = h1only = 0
    scheds = {}
    for c in range(nst):
        s = state(c)
        for j in range(1, k):
            for a in (0, 1):
                if not F.h1(s, CE[c], j, a):
                    continue
                cc = 1 - a
                if CE[nxt[c]][0][j - 1] != cc:
                    h1only += 1
                    continue
                if (j, a) not in scheds:
                    sc = {}
                    F.resp(j, 1, a, sc)
                    scheds[(j, a)] = sc
                sc = scheds[(j, a)]
                e = F.end(j, 1)
                windows += 1
                prev, cur, tau = c, nxt[c], 1
                while True:
                    steps += 1
                    pviol += int(F.moves(state(prev), state(cur), j) != sc.get(tau, set()))
                    if tau == e:
                        full += 1
                        break
                    n2 = nxt[cur]
                    if CE[n2][0][j - 1] != cc or CE[cur][1][j - 1] != cc:      # (H2[tau + 1]) fails
                        proper += 1
                        break
                    prev, cur, tau = cur, n2, tau + 1
    print(f"G_{k} mode exh ctrl {CTRL} states {nst} c0e0 {c0e0} loc {loc} lockeys {lockeys} stcases {cases} stviol {stviol} "
          f"onestate_cases {one} onestate_moves {onemoves} h1only {h1only} windows {windows} full {full} proper {proper} "
          f"steps {steps} pviol {pviol}", flush=True)


def mode_width(k):
    G, names = gk.build(k)
    w = [0] * (k + 1)
    for l in G["lev"]:
        w[l] += 1
    print(f"G_{k} mode width N {G['N']} levels {k + 1} widths {' '.join(map(str, w))} max {max(w)} sum {sum(w)}", flush=True)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    m = sys.argv[1]
    if m == "run":
        for a in sys.argv[2:]:
            mode_run(int(a))
    elif m == "off":
        mode_off(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    elif m == "loc":
        mode_loc(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
    elif m == "all":
        for a in sys.argv[2:]:
            mode_all(int(a))
    elif m == "exh":
        for a in sys.argv[2:]:
            mode_exh(int(a))
    elif m == "stable":
        mode_stable(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    elif m == "u0":
        mode_u0(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    elif m == "drive":
        mode_drive(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    elif m == "tie":
        for a in sys.argv[2:]:
            mode_tie(int(a))
    elif m == "width":
        for a in sys.argv[2:]:
            mode_width(int(a))
