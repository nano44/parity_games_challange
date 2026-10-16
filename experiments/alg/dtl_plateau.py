"""L-ALG (produced on Opus 5.5, 2026-10-16 box 4), queue item (1): DEF steps at a FIXED (context, M) on A_DTL.
For consecutive depth-0 calls at one (player, context) whose ideal (C6) result is STABLE and equal in both calls while the
actual round sequence changes (a DEF pair), with d(v) = the actual death round (stable survivors: M+1), report per step:
r0 (first differing round), M before/after, the direction of the round vector at r0 (UP: V_r0 grew, DOWN: shrank, X:
incomparable), whether the region union U at round r0 is equal, and candidate potentials:
  sumd = sum of deaths, lexdesc = deaths sorted descending (compared lexicographically), roundvec = (V_1, V_2, ...) under
  first-difference inclusion. Usage: DTL_ORDER=oink dtl_plateau.py G.pg ...  (PLATEAU_VERBOSE=1 prints every step)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_regvec as RV, dtl_ideal as I, pg

def deaths(rounds, V0):
    # stable survivors (run ends without an empty round) never die: death INF = n + 2
    M = len([x for x in rounds if x]); D = {}
    for v in V0:
        D[v] = next((i for i in range(len(rounds)) if v not in rounds[i]), INF)
    return D, M

INF = 10 ** 6
ALL = os.environ.get("PLATEAU_ALL") == "1"   # every consecutive pair at a fixed context, not only ideal-stable DEF pairs

def cmp_sets(a, b):
    return "EQ" if a == b else "UP" if a < b else "DOWN" if b < a else "X"

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    verbose = os.environ.get("PLATEAU_VERBOSE") == "1"
    tot = {}
    def inc(k): tot[k] = tot.get(k, 0) + 1
    import gen
    games = [(os.path.basename(f), pg.read(f)) for f in sys.argv[1:]]
    rnd = gen.Rng("plateau"); NMAX = int(os.environ.get("PLATEAU_NMAX", "24"))
    for i in range(int(os.environ.get("PLATEAU_RANDOM", "0"))):
        n = rnd.randint(6, NMAX); games.append((f"r{i}", gen.random_game(n, rnd.randint(2, n + 1), 1, rnd.randint(1, 3), rnd.next64())))
    for name, g in games:
        d = RV.build(g); d.run()
        for key, occ in d.calls.items():
            runs = []; lastfall = {}; lvl_max = 0   # reset nesting: level of a step = 0 if its top riser never fell, else 1 + level of the step that last made it fall
            for (s1, r1, v1, h1, *_), (s2, r2, v2, h2, *_) in zip(occ, occ[1:]):
                if r1 == r2 or (not ALL and (h1 != h2 or h1[0] != 1)): continue
                V0 = r1[0]
                D1, M1 = deaths(r1, V0); D2, M2 = deaths(r2, V0)
                L = max(len(r1), len(r2)); pick = lambda r, i: r[min(i, len(r) - 1)]   # a stable run stays at its last set
                r0 = next(i for i in range(1, L + 1) if pick(r1, i) != pick(r2, i))
                dirn = cmp_sets(pick(r1, r0), pick(r2, r0))
                Ueq = (r0 - 1 < len(v1) and r0 - 1 < len(v2) and v1[r0 - 1] == v2[r0 - 1])
                fin = lambda D: [x if x < INF else len(V0) + 2 for x in D.values()]
                sd = sum(fin(D2)) - sum(fin(D1))
                ld = sorted(D1.values(), reverse=True); ld2 = sorted(D2.values(), reverse=True)
                lexd = "UP" if ld2 > ld else "DOWN" if ld2 < ld else "EQ"
                rose = sorted(d.idx[v] for v in V0 if D2[v] > D1[v]); fell = sorted(d.idx[v] for v in V0 if D2[v] < D1[v])
                eqM = M1 == M2
                ch = [v for v in sorted(V0, reverse=True) if D1[v] != D2[v]]   # internal index descending = priority descending
                plex = "UP" if D2[ch[0]] > D1[ch[0]] else "DOWN"
                inc(f"{'eqM' if eqM else 'neqM'}_priolex_{plex}")
                if plex == "DOWN" and len(tot.setdefault("ex_priolex_DOWN", [])) < 5: tot["ex_priolex_DOWN"].append((name, len(key[1]), s1, s2, d.idx[ch[0]]))
                if fell_any := [v for v in ch if D2[v] < D1[v]]:
                    # every fallen vertex below (in index) some riser?  record max-priority riser vs max-priority faller
                    inc("fallsteps"); inc("fall_below_top_riser" if ch[0] not in fell_any else "fall_ABOVE_risers")
                    inc("fall_prio_lt_riserprio" if d.pr[max(fell_any)] < d.pr[ch[0]] else "fall_prio_ge_riserprio")
                inc("steps"); inc(("eqM" if eqM else "Mrise" if M2 > M1 else "Mdrop"))
                inc(f"{'eqM' if eqM else 'neqM'}_dir_{dirn}_U{'eq' if Ueq else 'ne'}")
                inc(f"{'eqM' if eqM else 'neqM'}_sumd_{'up' if sd > 0 else 'down' if sd < 0 else 'eq'}")
                inc(f"{'eqM' if eqM else 'neqM'}_lexdesc_{lexd}")
                runs.append((s1, s2, r0, M1, M2, dirn, Ueq, sd, rose, fell))
                if plex == "UP":
                    lev = lastfall.get(ch[0], -1) + 1
                    for v in ch:
                        if D2[v] < D1[v]: lastfall[v] = lev
                    lvl_max = max(lvl_max, lev)
                if verbose:
                    print(f"{name} |R|={len(key[1])} s{s1}->s{s2} r0={r0} M {M1}->{M2} dir={dirn} U{'=' if Ueq else '!='} "
                          f"sumd {sd:+d} lexdesc {lexd} priolex {plex}  rose {[(v, d.pr[d.idx.index(v)], D1[d.idx.index(v)], D2[d.idx.index(v)]) for v in rose]} "
                          f"fell {[(v, d.pr[d.idx.index(v)], D1[d.idx.index(v)], D2[d.idx.index(v)]) for v in fell]}")
            nfall = sum(1 for r in runs if r[9])   # (F1)/(F1-DEF): steps of this context with some death falling
            if runs: tot[f"ctx_fallsteps_{min(nfall, 3)}"] = tot.get(f"ctx_fallsteps_{min(nfall, 3)}", 0) + 1
            if runs: tot[f"reset_level_{lvl_max}"] = tot.get(f"reset_level_{lvl_max}", 0) + 1
            if runs: inc("ctx_with_def"); tot["max_def_ctx"] = max(tot.get("max_def_ctx", 0), len(runs))
    print(os.environ.get("DTL_ORDER", "stable"), dict(sorted(tot.items(), key=lambda kv: str(kv[0]))))
