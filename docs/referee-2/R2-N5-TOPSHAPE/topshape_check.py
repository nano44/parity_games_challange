#!/usr/bin/env python3
r"""REFEREE-2 successor 19 (Opus 5.5, D15): mechanical check of P-N5-TOPSHAPE (docs/new/P-N5-TOPSHAPE-box49.md, sha1 c5b0e8d8 @ l-new 4c2ea43e).
State loop = my lane's SPEC loop (dual_check.Runner on si.py = SPEC S1, read-only); Xi = my own play value (rund_check.state_info, ENGXI).
Lane tools (experiments/new/box49/topmono.py, quotecheck3.py) NOT run or imported.
Phase = maximal run with (lambda_Xi, tau) constant. P_t := P(Xi_t v) as a rank mask; top_t := its highest rank or BOT; parity of a rank := Omega
of the vertex of that rank mod 2.
Checks (each must be 0):
  DELTA   Fact DELTA vs the engine's signed weight, on every P-change of every vertex (and on RANDDELTA random mask pairs per game)
  INC     weight(P_{t+1}) > weight(P_t) at every in-phase P-change (the proof's first step: MON + same cycle node + INJ)
  TSa     (a) top rises only to an even rank;  TSb  (b) an even top never falls (incl. to BOT)
  TSc     (c) the sequence of distinct tops on a phase is: strictly decreasing odd ranks, then at most one BOT, then strictly increasing even ranks
  COR     top changes per (v, phase) <= n - 1;  CORc  the sharper count <= n - 1 - rank(c) (number of ranks above c) [proved by the same argument]
  XSAMEC  TSa/TSb at phase-LEAVING transitions where v's own cycle node is unchanged (the proof needs only that; strengthening)
Controls (counted as CTL_*, expected nonzero; NOT violations): CTL_cross (TSa/TSb across phase-leaving transitions, where c may change);
CTL_flip (TSa with the parity flipped: rise to an ODD rank); CTL_deltatop (the DEAD Delta-form TOP-MONO: rises of d(P_t, P_{t+1}) along a
vertex's P-changes in a phase); CTL_counting (P-changes per (v, phase) above n - 1).
Usage: topshape_check.py files list.txt [runs] | pairs list.txt prefix | start game.pg [game.start] | random N nmin nmax seed k [starts]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RUND"))
import rund_check as R
DC, pg, Stats = R.DC, R.pg, R.Stats
RANDDELTA = int(os.environ.get("RANDDELTA", "20"))
BOT = -1


def top(m): return m.bit_length() - 1 if m else BOT


def run_game(gp, s, t, st, name, rng):
    states, fbs = DC.Runner(gp).run(s, t)
    ctx = R.Ctx(gp); g, n, E = gp, gp.n, ctx.E
    I = [R.state_info(ctx, a, b, st, f"{name}@{k}") for k, (a, b) in enumerate(states)]
    st.inc("runs"); st.inc("states", len(I))
    inv = {E.rank[v]: v for v in range(n)}
    par = {r: g.prio[inv[r]] % 2 for r in range(n)}
    def w(m):
        return sum((1 if par[r] == 0 else -1) << r for r in range(n) if m >> r & 1)
    def delta_rule(A, B):   # True iff weight(B) > weight(A), by Fact DELTA
        d = top(A ^ B)
        return (par[d] == 0 and B >> d & 1 == 1) or (par[d] == 1 and A >> d & 1 == 1)
    for _ in range(RANDDELTA):
        A, B = rng.getrandbits(n), rng.getrandbits(n)
        if A != B:
            st.inc("DELTA_rand")
            if delta_rule(A, B) != (E.weight(B) > E.weight(A)) or w(A) != E.weight(A): st.bad("DELTA", f"{name} random pair")
    key = [(I[k]["lamX"], I[k]["tu"]) for k in range(len(I))]
    for k in range(len(I) - 1):
        if key[k] != key[k + 1]:
            for v in range(n):
                A, B = I[k]["xi"][v][1], I[k + 1]["xi"][v][1]
                if A == B: continue
                ta, tb = top(A), top(B)
                st.inc("CTL_cross_checks")
                fail = (tb > ta and par[tb] == 1) or (ta != BOT and par[ta] == 0 and tb < ta)
                if fail: st.inc("CTL_cross")
                if I[k]["xi"][v][0] == I[k + 1]["xi"][v][0]:   # N-TS: same cycle node of v across a phase-leaving transition
                    st.inc("XSAMEC_checks")
                    if fail: st.bad("XSAMEC", f"{name}@{k} v={v}")
    k0 = 0
    while k0 < len(I):
        k1 = k0
        while k1 + 1 < len(I) and key[k1 + 1] == key[k0]: k1 += 1
        if k1 > k0: check_phase(ctx, g, I, k0, k1, par, delta_rule, st, name)
        k0 = k1 + 1


def check_phase(ctx, g, I, a, b, par, delta_rule, st, name):
    n, E = ctx.n, ctx.E
    st.inc("phases")
    for v in range(n):
        c = I[a]["lamX"][v]
        tops = [top(I[a]["xi"][v][1])]; pch = 0; dts = []
        for k in range(a, b):
            A, B = I[k]["xi"][v][1], I[k + 1]["xi"][v][1]
            if I[k + 1]["xi"][v][0] != c or I[k]["xi"][v][0] != c: st.bad("CYC", f"{name}@{k} v={v}")
            if A == B: continue
            pch += 1; st.inc("Pchanges")
            if not delta_rule(A, B) or not E.weight(B) > E.weight(A): st.bad("INC", f"{name}@{k} v={v}")
            if delta_rule(A, B) != (E.weight(B) > E.weight(A)): st.bad("DELTA", f"{name}@{k} v={v}")
            dts.append(top(A ^ B))
            ta, tb = top(A), top(B)
            if tb > ta:
                st.inc("TSa_checks")
                if par[tb] != 0: st.bad("TSa", f"{name}@{k} v={v} {ta}->{tb}")
                if par[tb] == 0: st.inc("CTL_flip")
            if ta != BOT and par[ta] == 0:
                st.inc("TSb_checks")
                if tb < ta: st.bad("TSb", f"{name}@{k} v={v} {ta}->{tb}")
            if tb != tops[-1]: tops.append(tb)
        if pch > n - 1: st.inc("CTL_counting")
        st.mxr("max_Pchanges_per_v_phase", (pch, name, a, b, v, n))
        if len(dts) >= 2: st.inc("CTL_deltatop_seqs")
        if any(dts[i + 1] > dts[i] for i in range(len(dts) - 1)): st.inc("CTL_deltatop")
        # (c): shape of the distinct-top sequence
        i = 0
        while i < len(tops) and tops[i] != BOT and par[tops[i]] == 1: i += 1
        odd = tops[:i]; rest = tops[i:]
        if rest and rest[0] == BOT: rest = rest[1:]
        ok = all(odd[j] > odd[j + 1] for j in range(len(odd) - 1)) and all(x != BOT and par[x] == 0 for x in rest) \
            and all(rest[j] < rest[j + 1] for j in range(len(rest) - 1))
        if not ok: st.bad("TSc", f"{name} [{a},{b}] v={v} tops {tops}")
        ch = len(tops) - 1
        if ch: st.inc("v_phases_with_top_change")
        if ch > n - 1: st.bad("COR", f"{name} [{a},{b}] v={v} {ch}")
        if ch > n - 1 - E.rank[c]: st.bad("CORc", f"{name} [{a},{b}] v={v} {ch} > {n - 1 - E.rank[c]}")
        st.mxr("max_top_changes", (ch, name, a, b, v, n))
        st.mxr("max_top_changes_over_n", (round(ch / max(1, n - 1), 3), name, a, b, v, n))
        if odd and rest: st.inc("v_phases_odd_then_even")


def main():
    st = Stats(); a = sys.argv[1:]; rng = random.Random(4949)
    if a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 3
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            gp = pg.read(os.path.join(DC.ROOT, path))
            for r in range(runs):
                s, t = R.starts(gp, r, rng); run_game(gp, s, t, st, f"{path}#{r}", rng)
    elif a[0] == "pairs":
        for line in [l.split() for l in open(a[1]) if l.strip()]:
            gp = pg.read(os.path.join(a[2], line[0]))
            if len(line) > 1:
                s, t = R.read_start(gp, os.path.join(a[2], line[1]))
                for v in range(gp.n):
                    x = s if gp.owner[v] == 0 else t
                    if x[v] not in gp.succ[v]: st.inc("INVALID_START_ENTRIES"); x[v] = gp.succ[v][0]
            else: s, t = R.starts(gp, 0, None)
            run_game(gp, s, t, st, line[0] + ("#start" if len(line) > 1 else "#S3"), rng)
    elif a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); k = int(a[5]) if len(a) > 5 else 2; ns = int(a[6]) if len(a) > 6 else 2
        rng = random.Random(seed)
        sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-H3")); import h3_check as H
        for i in range(N):
            nn = rng.randint(nmin, nmax)
            gp = DC.rand_game(rng, nn, "kO") if k == 0 else H.rand_kO(rng, nn, k)
            for r in range(ns):
                s, t = R.starts(gp, r, rng); run_game(gp, s, t, st, f"random{seed}:{i}#{r}", rng)
    elif a[0] == "start":
        gp = pg.read(a[1])
        if len(a) > 2: s, t = R.read_start(gp, a[2]); nm = os.path.basename(a[1]) + "#start"
        else: s, t = R.starts(gp, 0, None); nm = os.path.basename(a[1]) + "#S3"
        run_game(gp, s, t, st, nm, rng)
    print("MODE", " ".join(a))
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol[:40]: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")


if __name__ == "__main__":
    main()
