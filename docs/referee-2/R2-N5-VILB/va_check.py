#!/usr/bin/env python3
r"""REFEREE-2 successor 13 (Opus 5.5, D15): mechanical check of packets P-N5-VILB (docs/new/P-N5-VILB-box44.md sha1 872d4400) and
P-N5-ACCEL (docs/new/P-N5-ACCEL-box44.md sha1 301f0be0), both @ trunk e7febdc2. Shared by R2-N5-VILB and R2-N5-ACCEL.
State sequence: own SPEC N5 loop (R2-N5-DUAL/dual_check.Runner, si.py read-only); honest frame and kappa from R2-N5-FBRED/fbred_check.Ctx.
The lane's experiments/new/box44/*.py are not run or imported.
Checks per phase ((lambda, tau) constant), every game:
  VILB  kappa_t(z) >= Val^{<=j}_c(z) for every class c, z in U_c, j = #in-phase fallbacks with source < t (Gamma_c: Even max, EVERY Odd
        vertex min over succ(z) & U_c, target c value (0,0), -inf elsewhere at j = 0).
  SG    every switched Even y with lambda(y) != y at an in-phase transition gains strictly (kappa_{t+1}(y) > kappa_t(y)).
  ACCa  kappa_t(z) in K_c(z) (simple-path levels of G[U_c]; n <= PATHCAP).   ACCb  transitions switching a non-cycle-node Even <= N_K, and
        per vertex <= |K_c(z)| - 1.   ACCc  f <= 1 + N_K.
  EPa   on each epoch E (sigma-bar|Q constant): kappa_t(z) >= best simple path of G_E[U_c] with <= j edges (j = #epoch fallbacks with source
        < t), kappa_t(z) <= opt_E(z); per-class freeze kappa_t = opt_E once j >= |U_c| - 1 (implied by EPa's bound; reached in data).
  EPb   after e_{n-1} inside E: no switch of a non-cycle-node Even; <= 4n(n-1) transitions with both ends in E.   EPc  f <= 1 + n N_ep.
Records: max fallbacks in one epoch minus (n - 1) (EPOCH (a)/(b) global regime reached iff >= 0), N_ep, sigma-bar|Q repeats, max |K|.
Mutations VA_MUT: vi (VILB with one extra round: Val^{<=j+1}), sg (SG asks non-strict loss), ep (EPc with n - 2 per epoch), kk (ACCb with -2).
Usage: va_check.py random N nmin nmax seed | files list.txt [runs] | climb steps nmin nmax seed outprefix"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FBRED")); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-DUAL"))
import fbred_check as FB
import dual_check as DC
pg, Engine, Stats = DC.pg, DC.Engine, DC.Stats
MUT = os.environ.get("VA_MUT", "")
PATHCAP = int(os.environ.get("PATHCAP", "11"))
NEG = None   # -infinity

def kadd(a, b): return None if a is None or b is None else (a[0] + b[0], a[1] + b[1])
def kge(a, b): return b is None or (a is not None and a >= b)

def simple_levels(ctx, verts, src, c, fixed=None):
    """all kwt sums of simple paths from src to c inside verts; edges: Even all inside, Odd all inside (fixed: dict Odd->successor);
    returns dict edges -> set of values"""
    g = ctx.g; out = {}
    def dfs(x, vis, acc, ne):
        if x == c:
            out.setdefault(ne, set()).add(acc); return
        acc2 = (acc[0] + ctx.kwt(x, c)[0], acc[1] + ctx.kwt(x, c)[1])
        nb = [fixed[x]] if (fixed is not None and g.owner[x] == 1) else sorted(set(g.succ[x]))
        for y in nb:
            if y in verts and y not in vis:
                vis.add(y); dfs(y, vis, acc2, ne + 1); vis.discard(y)
    dfs(src, {src}, (0, 0), 0)
    return out

def check_run(gp, states, fbs, st, name, rec=None):
    ctx = FB.Ctx(gp); g, n = gp, gp.n; Q = ctx.Q
    info = [ctx.state(list(s)) for s, _ in states]
    tauk = [tuple(t[v] for v in range(n) if g.owner[v] == 1) for _, t in states]
    st.inc("runs")
    key = [(info[k][2], tauk[k]) for k in range(len(states))]
    k0 = 0
    while k0 < len(states):
        k1 = k0
        while k1 + 1 < len(states) and key[k1 + 1] == key[k0]: k1 += 1
        phase(ctx, states, fbs, info, k0, k1, st, name, rec)
        k0 = k1 + 1

def phase(ctx, states, fbs, info, k0, k1, st, name, rec):
    g, n, Q = ctx.g, ctx.n, ctx.Q
    lam = info[k0][2]; C = sorted(set(lam)); T = set(C) | Q
    U = {c: [v for v in range(n) if lam[v] == c] for c in C}
    st.inc("phases")
    def kap(t, z): return ctx.kap(info[t][0][z], lam[z])
    trans = list(range(k0, k1)); fb = [k for k in trans if fbs[k]]; f = len(fb)
    # VILB: iterate Val^{<=j}
    jmax = f + (1 if MUT == "vi" else 0)
    val = {c: [{z: ((0, 0) if z == c else NEG) for z in U[c]}] for c in C}
    for c in C:
        Uc = set(U[c])
        for j in range(1, jmax + 1):
            prev = val[c][-1]; cur = {}
            for z in U[c]:
                if z == c: cur[z] = (0, 0); continue
                xs = [prev[x] for x in set(g.succ[z]) if x in Uc]
                if g.owner[z] == 0:
                    fin = [x for x in xs if x is not None]
                    best = max(fin) if fin else NEG
                else:
                    best = NEG if (not xs or any(x is None for x in xs)) else min(xs)
                cur[z] = kadd(ctx.kwt(z, c), best) if best is not None else NEG
            val[c].append(cur)
    for t in range(k0, k1 + 1):
        j = sum(1 for k in fb if k < t) + (1 if MUT == "vi" else 0)
        for c in C:
            for z in U[c]:
                st.inc("VILB_checks")
                if not kge(kap(t, z), val[c][min(j, len(val[c]) - 1)][z]): st.bad("VILB", f"{name}@{t}: z {z} c {c} j {j}")
    st.mxr("max_f", (f, name))
    # SG and ACC (b) counts
    sw_trans = 0; per = {}
    for k in trans:
        sg0, sg1 = states[k][0], states[k + 1][0]
        ys = [v for v in range(n) if g.owner[v] == 0 and sg0[v] != sg1[v] and lam[v] != v]
        if ys: sw_trans += 1
        for y in ys:
            per[y] = per.get(y, 0) + 1
            st.inc("SG_checks")
            gain = kap(k + 1, y) > kap(k, y)
            if gain == (MUT == "sg"): st.bad("SG", f"{name}@{k}: y {y}")
    # ACC (a)-(c) with K_c enumeration
    if n <= PATHCAP:
        NK = 0; K = {}
        for c in C:
            for z in U[c]:
                lv = simple_levels(ctx, set(U[c]), z, c)
                K[z] = set().union(*lv.values()) if lv else set()
                if g.owner[z] == 0 and z != c: NK += len(K[z]) - 1
                st.mxr("max_K", (len(K[z]), name))
        for t in range(k0, k1 + 1):
            for z in range(n):
                if kap(t, z) not in K[z]: st.bad("ACCa", f"{name}@{t}: z {z}")
        lim = NK - (2 if MUT == "kk" else 0)
        if sw_trans > lim: st.bad("ACCb", f"{name}: switching transitions {sw_trans} > N_K {NK}")
        for y, cnt in per.items():
            if cnt > len(K[y]) - 1: st.bad("ACCb", f"{name}: y {y} switches {cnt} > |K|-1")
        if f > 1 + NK: st.bad("ACCc", f"{name}: f {f} > 1 + N_K {NK}")
        st.inc("ACC_phases")
    # EPOCH
    sbarQ = [tuple(info[t][1][q] for q in sorted(Q)) for t in range(k0, k1 + 1)]
    epochs, cur = [], [k0]
    for t in range(k0 + 1, k1 + 1):
        if sbarQ[t - k0] == sbarQ[t - k0 - 1]: cur.append(t)
        else: epochs.append(cur); cur = [t]
    epochs.append(cur)
    Nep = len(epochs)
    st.mxr("max_epochs", (Nep, name))
    if len(set(sbarQ)) < Nep: st.inc("REC_phases_with_sbarQ_repeat")
    per_ep = n - (2 if MUT == "ep" else 1) + 1
    if f > 1 + per_ep * Nep: st.bad("EPc", f"{name}: f {f} > 1 + n N_ep ({Nep})")
    for E in epochs:
        Eset = set(E); efb = [k for k in fb if k in Eset]
        st.mxr("max_epoch_fb_minus_n1", (len(efb) - (n - 1), name))
        if rec is not None: rec["ep"] = max(rec.get("ep", -10 ** 9), len(efb) - (n - 1))
        if n > PATHCAP: continue
        sb = info[E[0]][1]
        fixed = {v: sb[v] for v in range(n) if g.owner[v] == 1}
        for c in C:
            Uc = set(U[c])
            for z in U[c]:
                lv = simple_levels(ctx, Uc, z, c, fixed)
                if not lv: continue
                byj, best = {}, None
                for ne in sorted(lv):
                    m_ = max(lv[ne]); best = m_ if best is None or m_ > best else best; byj[ne] = best
                opt = best
                for t in E:
                    j = sum(1 for k in efb if k < t)
                    lb = [w for ne, w in byj.items() if ne <= j]
                    kt = kap(t, z)
                    st.inc("EPa_checks")
                    if lb and kt < max(lb): st.bad("EPa", f"{name}@{t}: lower z {z}")
                    if kt > opt: st.bad("EPa", f"{name}@{t}: upper z {z}")
                    if j >= len(Uc) - 1:
                        st.inc("EPa_class_freeze_checks")
                        if kt != opt: st.bad("EPa", f"{name}@{t}: class freeze z {z}")
        # EPb global regime
        if len(efb) >= n - 1:
            st.inc("EPb_epochs_reached")
            after = [t for t in E if t > efb[n - 2]]
            inside = [t for t in after if t + 1 in Eset]
            if len(inside) > 4 * n * (n - 1): st.bad("EPb", f"{name}: {len(inside)} transitions after e_(n-1)")
            for t in inside:
                if any(g.owner[v] == 0 and states[t][0][v] != states[t + 1][0][v] and lam[v] != v for v in range(n)):
                    st.bad("EPb", f"{name}@{t}: non-cycle-node switch after freeze")

def run_game(gp, s, t, st, name, rec=None):
    states, fbs = DC.Runner(gp).run(s, t)
    check_run(gp, states, fbs, st, name, rec)

def main():
    st = Stats(); a = sys.argv[1:]
    if a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); rng = random.Random(seed)
        for i in range(N):
            gp = DC.rand_game(rng, rng.randint(nmin, nmax), "kO")
            s = [rng.choice(gp.succ[v]) for v in range(gp.n)]; t = [rng.choice(gp.succ[v]) for v in range(gp.n)]
            run_game(gp, s, t, st, f"random{seed}:{i}")
    elif a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 2; rng = random.Random(7171)
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            gp = pg.read(os.path.join(DC.ROOT, path))
            for r in range(runs):
                if r == 0: s, t = list(Engine(gp).initial("best")), list(Engine(DC.dual(gp)).initial("best"))
                else: s = [rng.choice(gp.succ[v]) for v in range(gp.n)]; t = [rng.choice(gp.succ[v]) for v in range(gp.n)]
                run_game(gp, s, t, st, f"{path}#{r}")
    elif a[0] == "climb":
        steps, nmin, nmax, seed, out = int(a[1]), int(a[2]), int(a[3]), int(a[4]), a[5]; rng = random.Random(seed)
        bestg = DC.rand_game(rng, rng.randint(nmin, nmax), "kO"); bestsc = -10 ** 9
        for it in range(steps):
            cand = FB.mutate(rng, bestg) if it else bestg
            if not any(len(set(cand.succ[v])) > 1 for v in range(cand.n)): continue
            rec = {}; bs = None; sc = -10 ** 9
            for r in range(4):
                s = [rng.choice(cand.succ[v]) for v in range(cand.n)]; t = [rng.choice(cand.succ[v]) for v in range(cand.n)]
                rec = {}; run_game(cand, s, t, st, f"climb{seed}:{it}:{r}", rec)
                if rec.get("ep", -10 ** 9) > sc: sc, bs = rec["ep"], (s, t)
            if sc >= bestsc and bs is not None:
                bestsc, bestg = sc, cand
                with open(out + ".pg", "w") as fh: fh.write(pg.dumps(bestg))
                with open(out + ".txt", "w") as fh: fh.write(f"score {bestsc}\nSIGMA0 {' '.join(f'{v}:{w}' for v, w in enumerate(bs[0]))}\nTAU0 {' '.join(f'{v}:{w}' for v, w in enumerate(bs[1]))}\n")
        st.mxr("climb_best_epoch_fb_minus_n1", (bestsc, out))
    print("MODE", " ".join(a), "MUT", MUT or "-")
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")

if __name__ == "__main__":
    main()
