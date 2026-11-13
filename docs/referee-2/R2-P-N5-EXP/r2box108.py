#!/usr/bin/env python3
"""REFEREE-2 successor 42: own checker for the review of L-SI's box 108 (claude/l-si 8c062914, docs/si/box108-gk-proof.md, sha1
31b7c78c…): Lemma STEP (the 32-class transition table of §5) and Lemma MOVE (§6), the second derivation of Theorem EXP-IDEAL (b).
Own code: the genome is r2exp.build (written from P-N5-EXP §3's TABLE), the model r2unit217.M1P (= R104's IDEAL model); the closed
form c_k(t), the phases and the class of a level at a step are coded here from the WORDS of box 108 §3-§5; the position row of §3,
the top positions and the 32 rows of §5 are PARSED out of the box's own file (argument DOC), so the table that is checked is the
table that is written. Nothing of experiments/si/box108/ is imported.

Counters (must 0):
  parse     the file does not hold 12 positions, 6 top positions and 32 rows with distinct names
  closed    [t]: Φ^t(s_0) ≠ c_k(t), 0 ≤ t ≤ T_k = 2^k − 2 (Φ = my model's step)
  stop      c_k(T_k) is not a fixed point of Φ, or every availability set there is a singleton, or the unstable movers at the
            stop are not exactly v_1..v_(k−1)
  step_eq   [(t, mover)]: Lemma STEP as stated: n := c_k(t + 1) (n := s at t = T_k) violates (EQ) of Lemma LATCH at s := c_k(t):
            n(x) = s(x) if pref_s(x) = s(x), else n(x) = kmin_n(x); pref from the model's value order under s, kmin from the model's
            keys under n
  table     [(t, level)]: the row of the level's class (the class named by §5's rule from the phases), rebuilt from the model —
            old Q, R, Xb; new Xb, E, Xi; per mover: option, pref, and for an unstable mover kmin and hold / move — differs from
            the row printed in the box
  rows_seen INFO: classes met (must be 32 over the k's run; `missing` = classes never met, must 0 when 3..6 are all run)
  hand      [row]: the row recomputed from (F1), (F2) and the position alone (no model) differs from the printed row
  sig       [(t, j)]: SIG: at c_k(t), P_j = v iff X_j = 1, or K_j = v iff X_j = 1, fails (model's value / key comparison)
  phase     [(t, i)]: PHASE: not exactly one of (a), (b), (c); or level 2 not in (a); or the chain claims fail
  input     [(t, i)]: INPUT (i), (ii) or (iii) fails at c_k(t)
  move      [t]: MOVE: c_k(t + 1) = c_k(t) for some t < T_k, or the proof's witness fails (i := the largest level with levels 2..i
            in case (a); i = k − 1: the top position changes; i < k − 1: level i + 1 in case (b), τ_i ∈ {2h, 4h + 1}, e_i moves)
  latch     [state]: (k = 3 only) (EQ) at s does not have exactly one solution among all 2^N states, or it is not Φ(s)
Controls (--ctrl NAME): hoff (H_i − 1 in the closed form: closed), rowmut (one cell of one parsed row flipped: table, hand),
posmut (one bit of the parsed position S4 flipped: closed, step_eq), kold (kmin read under the OLD state s: step_eq — the
simultaneity of §5), sigmut (SIG tested with K_j = v iff X_j = 0: sig), phasemut (phases with τ_(i+1) := τ_i mod (H_i + 1): closed).
Usage: r2box108.py DOC [--ctrl NAME] K..."""
import sys, os, re, random, itertools
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "R2-key"), os.path.join(HERE, "..", "R2-P-N5-END")]
import r2exp as X
import r2unit217 as U

MID = ["u", "v", "y", "yb", "yp", "ypb", "e"]; BOT = ["u", "v", "y", "yb"]


def parse(doc, C, ctrl):
    txt = open(doc, encoding="utf-8").read().split("\n")
    pos = None; top = None; rows = {}
    for ln in txt:
        if ln.startswith("| state |"):
            cells = [c.strip() for c in ln.strip().strip("|").split("|")][1:]
            pos = [tuple(int(ch) for ch in c.replace(" ", "")) for c in cells]
        if ln.startswith("Top positions"):
            top = [tuple(int(ch) for ch in g.replace(" ", "")) for g in re.findall(r"T\d = (\d\d \d\d)", ln)]
        m = re.match(r"^(bot|mid|top) (.+?)\s*\| old (.+?) \| new (.+?) \| (.+)$", ln)
        if m:
            name = m.group(1) + " " + " ".join(m.group(2).split())
            if name in rows: C["parse"] += 1
            rows[name] = (" ".join(m.group(3).split()), " ".join(m.group(4).split()), [" ".join(c.split()) for c in m.group(5).split("|")])
    if pos is None or len(pos) != 12 or any(len(p) != 7 for p in pos) or top is None or len(top) != 6 or len(rows) != 32: C["parse"] += 1
    if ctrl == "rowmut":
        o, n, cells = rows["mid S3->S4"]; cells = list(cells); cells[4] = "yp:0 p1 k1 ->1"; rows["mid S3->S4"] = (o, n, cells)
    if ctrl == "posmut":
        p = list(pos[4]); p[5] = 1 - p[5]; pos[4] = tuple(p)
    return pos, top, rows


class Box:
    def __init__(self, k, pos, top, ctrl=""):
        self.k = k; G, names, ix, _ = X.build(k); self.G, self.names, self.ix = G, names, ix; self.m = U.M1P(G); self.N = G["N"]
        self.pos, self.top, self.ctrl = pos, top, ctrl
        self.H = {i: 2 ** (k - i + 1) - 1 - (1 if ctrl == "hoff" else 0) for i in range(1, k)}; self.T = 2 ** k - 2
        self.Hmod = {i: self.H[i] + (1 if ctrl == "phasemut" else 0) for i in self.H}

    def tau(self, i, t):                       # τ_1 = t, τ_(i+1) = τ_i mod H_i
        x = t
        for j in range(1, i): x %= self.Hmod[j]
        return x

    def posidx(self, tau, h):                  # pos(τ; h), §3
        if tau in (0, 4 * h + 2): return 0
        if tau == 1: return 1
        if 2 <= tau <= h - 1: return 2
        if tau == h: return 3
        if h + 1 <= tau <= 2 * h - 1: return 4
        if tau == 2 * h: return 5
        if tau == 2 * h + 1: return 6
        if tau == 2 * h + 2: return 7
        if 2 * h + 3 <= tau <= 3 * h: return 8
        if tau == 3 * h + 1: return 9
        if 3 * h + 2 <= tau <= 4 * h: return 10
        if tau == 4 * h + 1: return 11
        return None

    def c(self, t):                            # the closed form c_k(t), §3
        k, ix = self.k, self.ix; s = [0] * self.N; s[ix["v0"]] = int(t >= 1)
        def put(i, vals, names):
            for n, b in zip(names, vals): s[ix[f"{n}{i}"]] = b
        p = self.posidx(t, self.H[2])
        if p is None: return None
        put(1, self.pos[p][:4], BOT)
        for i in range(2, k - 1):
            p = self.posidx(self.tau(i, t), self.H[i + 1])
            if p is None: return None
            put(i, self.pos[p], MID)
        tt = self.tau(k - 1, t)
        if tt > 6: return None
        put(k - 1, self.top[tt % 6], BOT)
        return tuple(s)

    def case(self, i, t):                      # PHASE: 'a', 'b', 'c' (or '?' if none / several)
        a, b = self.tau(i, t), self.tau(i, t + 1); r = ""
        if b == a + 1 and b <= 2 * self.H[i]: r += "a"
        if a == 2 * self.H[i] and b == 0: r += "b"
        if a == 0 and b == 0: r += "c"
        return r if len(r) == 1 else "?"

    def cls(self, i, t):                       # the class of level i at the step t → t + 1 (the STOP step at t = T), §5's rule
        k = self.k
        if i == 1:
            h = self.H[2]
            if t == 0: return "bot A0->A1"
            if t == 1: return "bot A1->A2"
            if 2 <= t <= h - 2: return "bot A2 stay"
            if t == h - 1: return "bot A2->A3"
            if t == h: return "bot A3->A4"
            if h + 1 <= t <= 2 * h - 2: return "bot A4 stay (E=1)"
            if t == 2 * h - 1: return "bot A4 stay (E=0)"
            if t == 2 * h: return "bot A4 stay (stop)"
            return "?"
        idle = t == self.T or self.case(i, t) in ("b", "c"); ta = self.tau(i, t)
        if i == k - 1: return "top T0 idle" if idle else f"top T{ta}->T{(ta + 1) % 6}"
        if idle: return "mid S0 idle"
        h = self.H[i + 1]
        tab = {0: "S0->S1", 1: "S1->S2", h - 1: "S2->S3", h: "S3->S4", 2 * h - 1: "S4->S5", 2 * h: "S5->S6", 2 * h + 1: "S6->S7",
               2 * h + 2: "S7->S8", 3 * h: "S8->S9", 3 * h + 1: "S9->S10", 4 * h: "S10->S11", 4 * h + 1: "S11->S0"}
        if ta in tab: return "mid " + tab[ta]
        if 2 <= ta and ta + 1 <= h - 1: return "mid S2 stay"
        if h + 1 <= ta and ta + 1 <= 2 * h - 1: return "mid S4 stay"
        if 2 * h + 3 <= ta and ta + 1 <= 3 * h: return "mid S8 stay"
        if 3 * h + 2 <= ta and ta + 1 <= 4 * h: return "mid S10 stay"
        return "?"

    def Xbit(self, s, j):
        ix = self.ix
        return s[ix["v0"]] if j == 0 else int(s[ix[f"u{j}"]] != s[ix[f"v{j}"]])

    def Ebit(self, s, i):                      # E(i + 1) under s
        ix = self.ix
        return s[ix[f"e{i + 1}"]] if i + 1 <= self.k - 2 else s[ix[f"u{i + 1}"]]

    def row(self, i, s, n):                    # the row of level i at the step s → n, from the model
        k, ix, m = self.k, self.ix, self.m; V, Xv = m.vals(s); _, key = m.keys(s if self.ctrl == "kold" else n)
        kind = "bot" if i == 1 else "top" if i == k - 1 else "mid"; names = MID if kind == "mid" else BOT
        Q = "y" if V[ix[f"y{i}"]] > V[ix[f"yb{i}"]] else "yb"
        old = f"Q={Q}" + (f" R={'yp' if V[ix[f'yp{i}']] > V[ix[f'ypb{i}']] else 'ypb'}" if kind == "mid" else "") + f" Xb={self.Xbit(s, i - 1)}"
        new = f"Xb={self.Xbit(n, i - 1)}" + (f" E={self.Ebit(n, i)}" if kind != "top" else "") + f" Xi={self.Xbit(n, i)}"
        cells = []
        for nm in names:
            x = ix[f"{nm}{i}"]; c = s[x]; P = 0 if Xv[(x, 0)] > Xv[(x, 1)] else 1
            if P == c: cells.append(f"{nm}:{c} p{P} -")
            else:
                K = 0 if key[(x, 0)] < key[(x, 1)] else 1
                cells.append(f"{nm}:{c} p{P} k{K} " + ("hold" if K == c else f"->{K}"))
        return old, new, cells


def hand(name, old, new, pos, top):
    """the row from (F1), (F2) and the position alone: old = the printed old columns, new = the printed new columns"""
    kind = name[:3]; o = dict(x.split("=") for x in old.split()); n = dict(x.split("=") for x in new.split())
    lab = name.split()[1]; a = lab.split("->")[0]
    P = (pos[int(a[1:])][:4] if kind == "bot" else pos[int(a[1:])]) if kind != "top" else top[int(a[1:])]
    names = MID if kind == "mid" else BOT; st = dict(zip(names, P)); Q = o["Q"]; Xb = int(o["Xb"]); cells = []
    pref = {"u": int(Q == "y"), "v": int(Q == "yb"), "y": Xb, "yb": 1 - Xb}
    if kind == "mid": pref.update(yp=int(Q == "y"), ypb=int(Q == "yb"), e=int(o["R"] == "yp"))
    nXb, nXi = int(n["Xb"]), int(n["Xi"]); kmin = {"u": nXb, "v": nXb, "e": nXb}
    if kind == "top": kmin.update(y=nXi, yb=nXi)
    else:
        nE = int(n["E"]); kmin.update(y=int(nE == 1 or nXi == 0), yb=int(nE == 1 or nXi == 0), yp=int(nE == 0 or nXi == 1), ypb=int(nE == 0 or nXi == 1))
    for nm in names:
        c = st[nm]; p = pref[nm]
        if p == c: cells.append(f"{nm}:{c} p{p} -")
        else: cells.append(f"{nm}:{c} p{p} k{kmin[nm]} " + ("hold" if kmin[nm] == c else f"->{kmin[nm]}"))
    return cells


def check(k, pos, top, rows, C, ctrl, seen):
    B = Box(k, pos, top, ctrl); m = B.m; ix = B.ix; T = B.T; N = B.N
    S = [tuple(B.G["start"])]
    for _ in range(T + 1):
        q = m.step(S[-1]); S.append(S[-1] if q is None else q)
    cl = [B.c(t) for t in range(T + 1)]
    for t in range(T + 1):
        if cl[t] != S[t]: C["closed"] += 1
    if S[T + 1] != S[T]: C["stop"] += 1
    _, Xf = m.vals(S[T]); A = m.avail(S[T], Xf)
    if all(len(a) == 1 for a in A) or sorted(x for x in range(N) if len(A[x]) > 1) != sorted(ix[f"v{j}"] for j in range(1, k)): C["stop"] += 1
    if any(c is None for c in cl): return
    C["u_step"] += (T + 1) * N; C["u_table"] += (T + 1) * (k - 1); C["u_states"] += T + 1
    for t in range(T + 1):
        s = cl[t]; n = cl[t + 1] if t < T else s; V, Xv = m.vals(s); mu, key = m.keys(s if ctrl == "kold" else n)
        for x in range(N):                                                 # Lemma STEP: (EQ)
            pref = 0 if Xv[(x, 0)] > Xv[(x, 1)] else 1; kmin = 0 if key[(x, 0)] < key[(x, 1)] else 1
            if n[x] != (s[x] if pref == s[x] else kmin): C["step_eq"] += 1
        for i in range(1, k):                                              # the table
            name = B.cls(i, t); seen.add(name); got = B.row(i, s, n); want = rows.get(name)
            if want is None or tuple(got) != tuple(want): C["table"] += 1
        mus, _ = m.keys(s)
        for j in range(k):                                                 # SIG
            Xj = B.Xbit(s, j); u, v = ix[f"u{j}"], ix[f"v{j}"]
            Pv = int(V[v] > V[u]); Kv = int(mus[v] < mus[u])
            if Pv != Xj or Kv != (1 - Xj if ctrl == "sigmut" else Xj): C["sig"] += 1
        for i in range(1, k):                                              # INPUT (i), (ii), (iii)
            ta = B.tau(i, t)
            if i >= 2 and B.Xbit(s, i - 1) != int(1 <= ta <= B.H[i]): C["input"] += 1
            if i == 1 and B.Xbit(s, 0) != int(t >= 1): C["input"] += 1
            if i <= k - 2:
                h = B.H[i + 1]
                if B.Ebit(s, i) != int(h <= ta % B.H[i] <= 2 * h - 1): C["input"] += 1
                if i >= 2 and B.Xbit(s, i) != int(1 <= ta <= h or 2 * h + 2 <= ta <= 3 * h + 1): C["input"] += 1
                if i == 1 and B.Xbit(s, 1) != int(1 <= t <= B.H[2]): C["input"] += 1
            else:
                if B.Xbit(s, i) != int(ta in (1, 2, 4, 5)): C["input"] += 1
        if t < T:
            cs = {i: B.case(i, t) for i in range(2, k)}                    # PHASE
            if "?" in cs.values() or cs[2] != "a": C["phase"] += 1
            for i in range(2, k - 1):
                ta = B.tau(i, t)
                if cs[i] == "a" and not (cs[i + 1] == "a" or (ta in (B.H[i] - 1, 2 * B.H[i] - 1) and cs[i + 1] == "b")): C["phase"] += 1
                if cs[i] in ("b", "c") and cs[i + 1] != "c": C["phase"] += 1
            i = 2                                                          # MOVE
            while i + 1 <= k - 1 and cs[i + 1] == "a": i += 1
            if s == n: C["move"] += 1
            if i == k - 1:
                if all(s[ix[f"{nm}{k - 1}"]] == n[ix[f"{nm}{k - 1}"]] for nm in BOT): C["move"] += 1
            else:
                h = B.H[i + 1]
                if not (cs[i + 1] == "b" and B.tau(i, t) in (2 * h, 4 * h + 1) and S[t + 1][ix[f"e{i}"]] != S[t][ix[f"e{i}"]]): C["move"] += 1
    if k == 3:                                                             # LATCH: (EQ) has exactly one solution, Φ(s)
        rng = random.Random(108); allc = list(itertools.product((0, 1), repeat=N)); keys = {c: m.keys(c)[1] for c in allc}
        for s in [S[t] for t in range(T + 1)] + [tuple(rng.randrange(2) for _ in range(N)) for _ in range(60)]:
            _, Xv = m.vals(s); pref = [0 if Xv[(x, 0)] > Xv[(x, 1)] else 1 for x in range(N)]
            sol = [c for c in allc if all(c[x] == (s[x] if pref[x] == s[x] else (0 if keys[c][(x, 0)] < keys[c][(x, 1)] else 1)) for x in range(N))]
            q = m.step(s); q = s if q is None else q; C["latch_states"] += 1
            if sol != [q]: C["latch"] += 1


MUST0 = ["parse", "closed", "stop", "step_eq", "table", "hand", "sig", "phase", "input", "move", "latch", "missing"]


def main(a):
    doc = a[0]; ctrl = ""; ks = []; i = 1
    while i < len(a):
        if a[i] == "--ctrl": ctrl = a[i + 1]; i += 2
        else: ks.append(int(a[i])); i += 1
    C = defaultdict(int); pos, top, rows = parse(doc, C, ctrl); seen = set()
    for name, (old, new, cells) in rows.items():
        if hand(name, old, new, pos, top) != cells: C["hand"] += 1
    for k in ks:
        before = dict(C); check(k, pos, top, rows, C, ctrl, seen)
        print(f"k {k} T {2 ** k - 2} | " + (" ".join(f"{c} {C[c] - before.get(c, 0)}" for c in MUST0 if C[c] - before.get(c, 0)) or "all 0"), flush=True)
    C["missing"] = len(set(rows) - seen)
    print(f"TOTAL ctrl {ctrl or '-'}: " + " ".join(f"{c} {C[c]}" for c in MUST0))
    print(f"INFO rows_parsed {len(rows)} rows_seen {len(seen)} states {C['u_states']} step_eq_units {C['u_step']} table_units {C['u_table']} latch_states {C['latch_states']} never_met: {sorted(set(rows) - seen) or 'none'}")
    print("FIRED " + (" ".join(c for c in MUST0 if C[c]) or "none"))


if __name__ == "__main__":
    main(sys.argv[1:])
