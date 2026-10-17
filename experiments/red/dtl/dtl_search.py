#!/usr/bin/env python3
"""Free-form hill-climb over small parity games maximising Oink DTL's learned-tangle count (L-RED, DTL box).
Fitness = tangles found by `oink --dtl --no-single --no-wcwc --no-loops` (raw solver, no preprocessing, self-loops kept;
before 16:02Z the runs used --no-single --no-wcwc only). Mutations: add/remove an edge,
change a priority, flip an owner. Usage: dtl_search.py OINK n [--steps 20000] [--seed 0] [--maxpr P] [--even-min FRAC] [--fitness tangles|unsolved|wrong|perhead|perheadsearch|persearch|prunemono|dups|straddles|alpha|strch|newrecur|maxsets|pairs|iters|restarts|maxrestarts|osc|rep|excess|carries|pviol|resets|ogate|fresh|phiflat|phicap|cidx|h4|replay2|phaselen|lemmas|nest2|nest2deep|h4ctx|h4prod|r0dips|crm|childm|cmf|nest3|r0d|lex|umono|falls|replay|fallsdef|phase|refall|spp|sharp|dvfall|absmono|abspw|dupchk|gapb|k4bp|klow|pk|kt|yzwm|ntf|yzs|yzc|slow|fdl|meet|root|evens] [--hb K] [--maxeven K] [--grow k] [--injective] [--loops] [--solver dtl|idtl] [--from game.pg] [--eval game.pg] [--out best.pg]"""
import sys, os, random, subprocess, tempfile, time, re
oink, n = sys.argv[1], int(sys.argv[2]); arg = lambda k, d: type(d)(sys.argv[sys.argv.index(k) + 1]) if k in sys.argv else d
steps, seed, maxpr = arg("--steps", 20000), arg("--seed", 0), arg("--maxpr", 2 * int(sys.argv[2])); rng = random.Random(seed)
evenmin = arg("--even-min", 0.0)
maxeven = arg("--maxeven", 0)                  # if > 0: reject games with more than this many Even-priority vertices
SOLVER = "--" + arg("--solver", "dtl")         # dtl | idtl
OINKFLAGS = ["--no-single", "--no-wcwc", "--no-loops"]   # the pinned algorithm (CHECKER C3): no preprocessing, self-loops kept
loops = "--loops" in sys.argv                  # bias mutations toward self-loops and toward renumbering equal-priority vertices
fitness = arg("--fitness", "tangles")   # tangles | unsolved (vertices DTL leaves unsolved) | perhead (max tangles learned at one top priority; use --injective)
injective = "--injective" in sys.argv    # priorities = a permutation of 0..n-1, so a tangle's priority names its top      # reject games with fewer than this fraction of Even-owned vertices (two-player search)
tmp = tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False).name


def dumps(g):
    pr, ow, succ = g
    return f"parity {n - 1};\n" + "".join(f"{v} {pr[v]} {ow[v]} {','.join(map(str, sorted(succ[v])))};\n" for v in range(n))


def score_py(g):
    """Exact per-top-vertex measures via the instrumented Python DTL (dtl_flipflop.py; slower than Oink).
    rep: sum over top vertices of (number of searches in which the top learns a tangle - 1), plus the number of searches
    (a chain of singleton tangles scores ~searches; a counter re-learns at the same tops). Fails closed on any exception."""
    import importlib.util, os as _os, io, contextlib
    if fitness == "umono":     # successor 3: (U-MONO_DTL) attack (carry/umono.py; L-ALG dtl_steal premise; LALG_DIR >= 670a762)
        specu = importlib.util.spec_from_file_location("umono", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "umono.py"))
        um = importlib.util.module_from_spec(specu); specu.loader.exec_module(um)
        try:
            return um.score(tmp)
        except Exception:
            return -1
    if fitness == "fdl":       # box 6: (R1) First-Difference Lemma gap G-h1 (carry/fdl.py; LALG12_DIR, LALG5_DIR)
        specf = importlib.util.spec_from_file_location("fdl", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "fdl.py"))
        fdl = importlib.util.module_from_spec(specf); specf.loader.exec_module(fdl)
        try:
            return fdl.score(tmp)
        except Exception:
            return -1
    if fitness == "slow":      # box 6: (S-LOW) loose/tight (carry/slow.py; LALG12_DIR >= ae7e1d3)
        specs = importlib.util.spec_from_file_location("slw", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "slow.py"))
        slw = importlib.util.module_from_spec(specs); specs.loader.exec_module(slw)
        try:
            return slw.score(tmp)
        except Exception:
            return -1
    if fitness == "yzc":       # box 6: (YZ)/(ACYC) via L-ALG dtl_yzclimb.fitness (carry/yzc.py; LALG11_DIR >= c2e80e9)
        specc2 = importlib.util.spec_from_file_location("yzc", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "yzc.py"))
        yzc = importlib.util.module_from_spec(specc2); specc2.loader.exec_module(yzc)
        try:
            return yzc.score(tmp)
        except Exception:
            return -1
    if fitness == "yzs":       # box 6: (YZ) straddle target (carry/yzs.py; L-ALG dtl_ntf.py + dtl_pnl.py; LALG10_DIR >= ced9921)
        specz = importlib.util.spec_from_file_location("yzs", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "yzs.py"))
        yzs = importlib.util.module_from_spec(specz); specz.loader.exec_module(yzs)
        try:
            return yzs.score(tmp)
        except Exception:
            return -1
    if fitness == "ntf":       # box 6: (NT-f) fitness (carry/ntf.py; L-ALG dtl_ntfclimb.fitness; LALG9_DIR >= 4841576)
        specn = importlib.util.spec_from_file_location("ntf", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "ntf.py"))
        ntf = importlib.util.module_from_spec(specn); specn.loader.exec_module(ntf)
        try:
            return ntf.score(tmp)
        except Exception:
            return -1
    if fitness == "yzwm":      # box 6: (YZ)/(WM_c1) fitness (carry/yzwm.py runs L-ALG dtl_pnl.py; LALG8_DIR >= b50e0c2)
        specy = importlib.util.spec_from_file_location("yzw", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "yzwm.py"))
        yzw = importlib.util.module_from_spec(specy); specy.loader.exec_module(yzw)
        try:
            return yzw.score(tmp)
        except Exception:
            return -1
    if fitness == "kt":        # box 6: graded (P-KT)/(KT-STEP-first) fitness (carry/kt.py; LALG7_DIR >= 312c918)
        speck = importlib.util.spec_from_file_location("ktf", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "kt.py"))
        ktf = importlib.util.module_from_spec(speck); speck.loader.exec_module(ktf)
        try:
            return ktf.score(tmp)
        except Exception:
            return -1
    if fitness == "pk":        # box 6: graded (P-K)/(K-STEP-first) fitness (carry/pk.py; LALG6_DIR >= 9000121)
        specp = importlib.util.spec_from_file_location("pkf", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "pk.py"))
        pkf = importlib.util.module_from_spec(specp); specp.loader.exec_module(pkf)
        try:
            return pkf.score(tmp)
        except Exception:
            return -1
    if fitness == "root":      # box 7: GAP-A-M §22c/§22d (#DIRTY, PREFIX-MONO, PI-RISE) via L-ALG dtl_rootmono.py unmodified (root/rootfit.py; LALGR_DIR >= 8a2a149; ROOTFIT = dirty | falls)
        specr = importlib.util.spec_from_file_location("rootfit", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "root", "rootfit.py"))
        rtf = importlib.util.module_from_spec(specr); specr.loader.exec_module(rtf)
        try:
            return rtf.score(tmp)
        except Exception:
            return -1
    if fitness == "meet":      # box 7: (MEET) of GAP-C §18r (meet/meetfit.py, L-ALG dtl_step5 unmodified; LALGM_DIR >= 2a715cd)
        specm = importlib.util.spec_from_file_location("meetfit", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "meet", "meetfit.py"))
        mtf = importlib.util.module_from_spec(specm); specm.loader.exec_module(mtf)
        try:
            return mtf.score(tmp)
        except Exception:
            return -1
    if fitness == "klow":      # box 6: graded (K-in)/(K-low) fitness (carry/klow.py; LALG5_DIR >= 31fdd98)
        specl = importlib.util.spec_from_file_location("klow", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "klow.py"))
        klw = importlib.util.module_from_spec(specl); specl.loader.exec_module(klw)
        try:
            return klw.score(tmp)
        except Exception:
            return -1
    if fitness == "k4bp":      # box 6: graded (K4-B) fitness (carry/k4bp.py; LALG5_DIR >= 31fdd98)
        speck = importlib.util.spec_from_file_location("k4bp", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "k4bp.py"))
        kbp = importlib.util.module_from_spec(speck); speck.loader.exec_module(kbp)
        try:
            return kbp.score(tmp)
        except Exception:
            return -1
    if fitness == "gapb":      # box 5: graded GAP-beta fitness (carry/gapb.py)
        specg = importlib.util.spec_from_file_location("gpb", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "gapb.py"))
        gpb = importlib.util.module_from_spec(specg); specg.loader.exec_module(gpb)
        try:
            return gpb.score(tmp)
        except Exception:
            return -1
    if fitness == "dupchk":    # box 5: GAP-C attack (carry/dupcheck.py): duplicate-check hits, unsolved / wrong vertices
        specc = importlib.util.spec_from_file_location("dpc", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "dupcheck.py"))
        dpc = importlib.util.module_from_spec(specc); specc.loader.exec_module(dpc)
        try:
            return dpc.score(tmp)
        except Exception:
            return -1
    if fitness == "abspw":     # box 5: (ABS-mono-pw) attack (carry/abspw.py)
        specw = importlib.util.spec_from_file_location("abw", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "abspw.py"))
        abw = importlib.util.module_from_spec(specw); specw.loader.exec_module(abw)
        try:
            return abw.score(tmp)
        except Exception:
            return -1
    if fitness == "absmono":   # box 5: (ABS-mono) attack (carry/absmono.py runs L-ALG dtl_dvctx.py DVC_PHI=1)
        speca = importlib.util.spec_from_file_location("abm", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "absmono.py"))
        abm = importlib.util.module_from_spec(speca); speca.loader.exec_module(abm)
        try:
            return abm.score(tmp)
        except Exception:
            return -1
    if fitness == "dvfall":    # box 5: DV-MONO attack (carry/dvfall.py runs L-ALG dtl_distval.py)
        specd = importlib.util.spec_from_file_location("dvf", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "dvfall.py"))
        dvf = importlib.util.module_from_spec(specd); specd.loader.exec_module(dvf)
        try:
            return dvf.score(tmp)
        except Exception:
            return -1
    if fitness in ("spp", "sharp"):       # box 5: searches per phase / |G'| (carry/spp.py, L-ALG dtl_phasestats; order from DTL_ORDER)
        specs = importlib.util.spec_from_file_location("spp", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "spp.py"))
        spm = importlib.util.module_from_spec(specs); specs.loader.exec_module(spm)
        try:
            return spm.score_sharp(tmp) if fitness == "sharp" else spm.score(tmp)
        except Exception:
            return -1
    if fitness in ("replay", "phase"):    # successor 3: replay depth on A_DTL (carry/replay.py, L-ALG dtl_pieces.replays2; order from DTL_ORDER)
        specp = importlib.util.spec_from_file_location("rep", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "replay.py"))
        rp = importlib.util.module_from_spec(specp); specp.loader.exec_module(rp)
        try:
            return rp.score_phase(tmp) if fitness == "phase" else rp.score(tmp)
        except Exception:
            return -1
    if fitness in ("falls", "fallsdef", "refall"):     # successor 3: >= 2 fall steps at one context (carry/lex.py score_falls)
        specf = importlib.util.spec_from_file_location("lexf", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "lex.py"))
        lexf = importlib.util.module_from_spec(specf); specf.loader.exec_module(lexf)
        try:
            return lexf.score_falls_def(tmp) if fitness == "fallsdef" else lexf.score_refall(tmp) if fitness == "refall" else lexf.score_falls(tmp)
        except Exception:
            return -1
    if fitness == "lex":       # successor 3: (LEX)/(NR) attack (carry/lex.py; L-ALG succ. 4 candidates via the Lead 16:16Z)
        specl = importlib.util.spec_from_file_location("lex", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "lex.py"))
        lex = importlib.util.module_from_spec(specl); specl.loader.exec_module(lex)
        try:
            return lex.score(tmp)
        except Exception:
            return -1
    if fitness == "r0d":       # successor 3, queue (3): r0 dips at one ideal-stable context, DEF-filtered (carry/r0d.py)
        specr = importlib.util.spec_from_file_location("r0d", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "r0d.py"))
        r0d = importlib.util.module_from_spec(specr); specr.loader.exec_module(r0d)
        try:
            return r0d.score(tmp)
        except Exception:
            return -1
    if fitness == "nest3":     # successor 3, queue (2): nested DEF blocks, 3 levels (carry/nest.py; order from DTL_ORDER)
        specn = importlib.util.spec_from_file_location("nest", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "nest.py"))
        nest = importlib.util.module_from_spec(specn); specn.loader.exec_module(nest)
        try:
            return nest.score(tmp)
        except Exception:
            return -1
    if fitness == "cmf":       # successor 3: FILTERED (CM) attack (carry/cmf.py, L-ALG dtl_childM premise; order from DTL_ORDER)
        specc = importlib.util.spec_from_file_location("cmf", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "cmf.py"))
        cmf = importlib.util.module_from_spec(specc); specc.loader.exec_module(cmf)
        try:
            return cmf.score(tmp)
        except Exception:
            return -1
    spec = importlib.util.spec_from_file_location("ff", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "dtl_flipflop.py"))
    ff = importlib.util.module_from_spec(spec); spec.loader.exec_module(ff)
    try:
        d = ff.load(tmp, "oink")
    except Exception:
        return -1
    per = {}
    for sr in d.searches:
        for top, vs, _ in sr["tangles"]: per.setdefault((sr["player"], top), set()).add(sr["index"])
    if fitness == "pviol":     # adversarial test of Claim P/Q (dtl_ctxmono.check): violations, plus recurring context pairs/1000
        spec2 = importlib.util.spec_from_file_location("cm", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "dtl_ctxmono.py"))
        cm = importlib.util.module_from_spec(spec2); spec2.loader.exec_module(cm)
        ctx, pairs, P, Q, M = cm.check(d)
        return 100 * (P + Q) + pairs / 1000.0
    if fitness == "carries":   # (CARRY) moves: consecutive same-player searches whose depth-0 piece 0 differs (removed set or kind),
        c = 0                  # plus searches/1000 as a tie-break; dominion searches excluded
        for pl in (0, 1):
            ss = [sr for sr in d.searches if sr["player"] == pl and sr["pieces"]]
            for a, b in zip(ss, ss[1:]):
                if a["dominions"] or b["G"] != a["G"]: continue
                x, y = a["pieces"][0], b["pieces"][0]
                if (x["kind"], x.get("removed")) != (y["kind"], y.get("removed")): c += 1
        return c + d.iterations / 1000.0
    if fitness == "phiflat":   # CARRY box (Opus 5.5): attack on L-ALG's Phi_idx: changes at a -1 depth-0 piece (equal context)
        spec4 = importlib.util.spec_from_file_location("ph", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "phi_idx.py"))
        ph = importlib.util.module_from_spec(spec4); spec4.loader.exec_module(ph)   # that raise no death-round record there
        try:
            e = ph.analyse(d)
        except Exception:
            return -1
        return 100 * len(e) + d.iterations / 100.0
    if fitness in ("h4", "h4ctx", "h4prod"):        # CARRY box (Opus 5.5): attack on L-ALG's (H4) (GAP-A-M 13): deficit-triggered (DEF) changes, run with
        import sys as _s       # L-ALG's own dtl_deficit.py (read-only; LALG_DIR = a checkout of claude/l-alg). Score = 100 x max DEF per
        ld = _os.environ["LALG_DIR"]                                    # (piece, context) per phase + 10 x max DEF per phase
        for q in (_os.path.join(ld, "experiments", "alg"), _os.path.join(ld, "experiments", "harness")):  # + DEF_m1m1 (re-targets)
            if q not in _s.path: _s.path.insert(0, q)
        import dtl_deficit as DD
        try:
            gg = DD.pg.read(tmp)
            if hasattr(DD, "build"):                  # l-alg >= 08bf2b5: order datum from DTL_ORDER (stable default, or oink)
                dd = DD.build(gg); dd.run()
            else:
                idx = sorted(range(gg.n), key=lambda v: (gg.prio[v], v)); new = {v: i for i, v in enumerate(idx)}
                dd = DD.T([gg.prio[v] for v in idx], [gg.owner[v] for v in idx], [[new[w] for w in gg.succ[v]] for v in idx]); dd.run()
            st = dict(calls=0, calls_def=0, weaker=0, NOT_weaker=0, DEF=0, LRN=0, LRN_lag=0, ctx_changed=0, max_def_per_ctx=0,
                      max_def_phase=(0, 0, None), n_max_def_phase=None, ex_def=[], ex_nw=[], ex_DEF_down=[], ex_DEF_other=[])
            DD.analyse(dd, st, "x")
        except Exception:
            return -1
        if fitness == "h4prod":  # compounding (Lead 13:46Z), BLOCK form (the product of totals was gameable: 2 then 3 sequential DEF
            best_b, best_1 = 0, 0  # at two contexts scored 6). Per phase, sequence of (first-difference index j, DEF?) over consecutive
            def flushp(seq):       # same-context changes; a block at level i = a DEF at i followed by the DEF changes at indices > i up
                nonlocal best_b, best_1    # to the next change at <= i. Score = 1000 x max over levels with >= 2 blocks of the sum of
                cnt = {}                   # (child DEF in the block); + 100 x max DEF per (index, context)
                for j, de, ctx in seq:
                    if de: cnt[(j, ctx)] = cnt.get((j, ctx), 0) + 1
                if cnt: best_1 = max(best_1, max(cnt.values()))
                for i in {j for j, de, _ in seq if de}:
                    blocks = []; k = 0
                    while k < len(seq):
                        if seq[k][0] == i and seq[k][1]:
                            c = 0; k += 1
                            while k < len(seq) and seq[k][0] > i:
                                c += seq[k][1]; k += 1
                            blocks.append(c)
                        elif seq[k][0] <= i: k += 1
                        else: k += 1
                    if len(blocks) >= 2 and sum(1 for c in blocks if c) >= 2: best_b = max(best_b, sum(blocks))
            seq = []
            for a, b in zip(dd.trace, dd.trace[1:]):
                if a["p"] != b["p"] or b["dom"] != a["dom"]:
                    flushp(seq); seq = []; continue
                pa, pb = a["pieces"], b["pieces"]; j = 0
                while j < min(len(pa), len(pb)) and pa[j][:3] == pb[j][:3]: j += 1
                if j >= min(len(pa), len(pb)): continue
                seq.append((j, pa[j][0] == pb[j][0] and pa[j][3:] == pb[j][3:], pa[j][0]))
            flushp(seq)
            return 1000 * best_b + 100 * best_1 + d.iterations / 1000.0
        if fitness == "h4ctx":  # weight on the per-context bound itself: 1000 x max DEF per (piece, context) + 100 x per phase + re-targets
            return 1000 * st["max_def_per_ctx"] + 100 * st["max_def_phase"][0] + 10 * st.get("DEF_m1m1", 0) + st["NOT_weaker"] + d.iterations / 1000.0
        return 100 * st["max_def_per_ctx"] + 10 * st["max_def_phase"][0] + st.get("DEF_m1m1", 0) + 1000 * st["NOT_weaker"] + d.iterations / 1000.0
    if fitness == "childm":    # L-ALG 13h candidate attack: 1000 x child-M drops across fresh contexts (phi_full.child_m_drops)
        spec11 = importlib.util.spec_from_file_location("pf", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "phi_full.py"))
        pf = importlib.util.module_from_spec(spec11); spec11.loader.exec_module(pf)
        try:
            nd, _ = pf.child_m_drops(pf.run(tmp))
        except Exception:
            return -1
        return 1000 * nd + d.iterations / 100.0
    if fitness == "crm":       # L-ALG GAP-A-M 13g (C-rM-stable) attack: per context key of L-ALG's dtl_regvec (read-only, LALG_DIR;
        import sys as _s       # order from DTL_ORDER), successive changes with the SAME ideal result and IDEAL STABLE; score = 1000 x
        ld = _os.environ["LALG_DIR"]   # #contexts whose (r0, M after) pairs repeat (+100 x max repeats in one context) + #steps
        for q in (_os.path.join(ld, "experiments", "alg"), _os.path.join(ld, "experiments", "harness")):
            if q not in _s.path: _s.path.insert(0, q)
        import dtl_regvec as RV, pg as _pg
        try:
            gg = _pg.read(tmp); dd = RV.build(gg); dd.run()
        except Exception:
            return -1
        rep = steps = mx = 0
        for key, occ in dd.calls.items():
            seq = []
            for (s1, r1, v1, h1, tl1), (s2, r2, v2, h2, tl2) in zip(occ, occ[1:]):
                if h1 != h2 or r1 == r2 or h1[0] != 1: continue
                pick = lambda r, i: r[i] if i < len(r) else frozenset()
                r0 = next(i for i in range(1, max(len(r1), len(r2)) + 1) if pick(r1, i) != pick(r2, i))
                seq.append((r0, len([x for x in r2 if x])))
            steps += len(seq)
            if len(set(seq)) < len(seq): rep += 1; mx = max(mx, len(seq) - len(set(seq)))
        return 1000 * rep + 100 * mx + steps + d.iterations / 1000.0
    if fitness == "r0dips":    # L-ALG GAP-A-M 13f candidate: 1000 x max r0 dips at one (phase, index, context) + longest r0 run
        spec10 = importlib.util.spec_from_file_location("pf", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "phi_full.py"))
        pf = importlib.util.module_from_spec(spec10); spec10.loader.exec_module(pf)   # (phi_full.r0_runs; all same-context changes)
        try:
            rr = pf.r0_runs(pf.run(tmp))
        except Exception:
            return -1
        return 1000 * max((x[5] for x in rr), default=0) + max((len(x[4]) for x in rr), default=0) + d.iterations / 1000.0
    if fitness in ("nest2", "nest2deep"):     # nest2deep: children inside cut recursions (phi_full.nest2deep). CARRY box (Opus 5.5): k=2 staircase counter score (phi_full.nest2) + longest phase/100
        spec9 = importlib.util.spec_from_file_location("pf", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "phi_full.py"))
        pf = importlib.util.module_from_spec(spec9); spec9.loader.exec_module(pf)
        try:
            dd = pf.run(tmp); sc, _ = (pf.nest2deep if fitness == "nest2deep" else pf.nest2)(dd); _, lp, _ = pf.replay_blocks(dd)
        except Exception:
            return -1
        return sc + lp / 100.0
    if fitness == "lemmas":    # CARRY box (Opus 5.5): L-ALG's Lemma S (GAP-A-M 16, proved for C6) on A_DTL: 1000 x violations
        spec8 = importlib.util.spec_from_file_location("pf", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "phi_full.py"))
        pf = importlib.util.module_from_spec(spec8); spec8.loader.exec_module(pf)   # + 10 x deficit-prone pairs (fixed-context -1 pairs)
        try:
            dd = pf.run(tmp); v = pf.lemma_s(dd)
        except Exception:
            return -1
        return 1000 * len(v) + 50 * dd.leader_drops + dd.lemma_s_pairs + d.iterations / 100.0   # leader drops: L-ALG c0aaa02
    if fitness in ("replay2", "phaselen"):   # CARRY box (Opus 5.5), Lead 12:04Z: chained resets (phi_full.replay_blocks): replay2 =
        spec7 = importlib.util.spec_from_file_location("pf", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "phi_full.py"))
        pf = importlib.util.module_from_spec(spec7); spec7.loader.exec_module(pf)   # block score + longest phase/100; phaselen = longest
        try:                                                                         # phase (searches) + block score/100
            sc, lp, _ = pf.replay_blocks(pf.run(tmp))
        except Exception:
            return -1
        return sc + lp / 100.0 if fitness == "replay2" else lp + sc / 100.0
    if fitness == "cidx":      # CARRY box (Opus 5.5): L-ALG's (H2b) reduction (GAP-A-M 11e): max over (phase, index i) of the number
        spec6 = importlib.util.spec_from_file_location("pf", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "phi_full.py"))
        pf = importlib.util.module_from_spec(spec6); spec6.loader.exec_module(pf)   # of distinct -1 Dom(prevV) contexts c_i; + sum/100
        try:
            cc = pf.ctx_counts(pf.run(tmp))
        except Exception:
            return -1
        return max((c for _, _, c in cc), default=0) + sum(c for _, _, c in cc) / 100.0 + d.iterations / 10000.0
    if fitness == "phicap":    # CARRY box (Opus 5.5): L-ALG's Phi_idx exactly (phi_full.py): 1000 x counterexamples (cap-only
        spec5 = importlib.util.spec_from_file_location("pf", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "phi_full.py"))
        pf = importlib.util.module_from_spec(spec5); spec5.loader.exec_module(pf)   # changes raising no record) + 10 x cap-only changes
        try:
            e = pf.run(tmp).events
        except Exception:
            return -1
        return 1000 * sum(1 for x in e if x["cap_only"] and not x.get("rs_resc", x["raised"])) + 10 * sum(1 for x in e if x["cap_only"]) + d.iterations / 100.0
    if fitness == "fresh":     # CARRY box (Opus 5.5): L-ALG's F_j (GAP-A-M.md section 6.3b) on this lane's tracer: per phase and depth-0
        tot = 0                # level j >= 1, the number of DISTINCT contexts R_j in which piece j changed (first difference at an
        prev = None; F = {}    # equal context). Score = sum_j (F_j - 1)^+ * (j + 1) + searches/1000.
        def flush():
            nonlocal tot
            for j, cs in F.items():
                if j >= 1: tot += max(0, len(cs) - 1) * (j + 1)
        for sr in d.searches:
            d0 = [p for p in sr["pieces"] if p["depth"] == 0]
            if prev is not None and (prev["player"] != sr["player"] or prev["dominions"] or prev["G"] != sr["G"]):
                flush(); F = {}
            elif prev is not None:
                pa = [p for p in prev["pieces"] if p["depth"] == 0]
                j = 0
                while j < min(len(pa), len(d0)) and (pa[j]["bv"]["R"], pa[j]["kind"], pa[j].get("V")) == (d0[j]["bv"]["R"], d0[j]["kind"], d0[j].get("V")):
                    j += 1
                if j < min(len(pa), len(d0)) and pa[j]["bv"]["R"] == d0[j]["bv"]["R"]:
                    F.setdefault(j, set()).add(pa[j]["bv"]["R"])
            prev = sr
        flush()
        return tot + d.iterations / 1000.0
    if fitness == "ogate":     # CARRY box (Opus 5.5): order-gate events (same sptl region set, different top SCC); OTHER weighs 100
        spec3 = importlib.util.spec_from_file_location("og", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "carry", "dtl_ogate.py"))
        og = importlib.util.module_from_spec(spec3); spec3.loader.exec_module(og)
        try:
            dd = og.run(tmp); e = dd.events
        except Exception:
            return -1
        return 1000 * len(dd.d2) + sum(100 if x["cls"] == "OTHER" else 1 for x in e) + d.iterations / 1000.0
    if fitness == "resets":    # CARRY box (Opus 5.5): (searches - dominions) * (1 + visits of a recurring (player, R) at which some
        spec2 = importlib.util.spec_from_file_location("cm", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "dtl_ctxmono.py"))
        cm = importlib.util.module_from_spec(spec2); spec2.loader.exec_module(cm)   # pruning round DROPS, i.e. fixed-context resets)
        seen, rv = {}, 0
        for sr in d.searches:
            for bv in sr["bv"]:
                if not bv["rounds"]: continue
                key = (sr["player"], bv["R"]); prof = cm.profile(bv)
                if key in seen and any(v in seen[key] and prof[v] < seen[key][v] for v in prof): rv += 1
                seen[key] = prof
        return (d.iterations - d.dominions) * (1 + rv)
    if fitness == "excess":    # searches minus distinct (player, top vertex) pairs that learn: a chain of singletons scores ~0,
        return d.iterations - d.dominions - len(per)   # a counter (few tops, many searches) scores high; dominion searches do not count
    return sum(len(x) - 1 for x in per.values()) + d.iterations


def score(g):
    open(tmp, "w").write(dumps(g))
    if fitness in ("rep", "excess", "carries", "pviol", "resets", "ogate", "fresh", "phiflat", "phicap", "cidx", "h4", "replay2", "phaselen", "lemmas", "nest2", "nest2deep", "h4ctx", "h4prod", "r0dips", "crm", "childm", "cmf", "nest3", "r0d", "lex", "umono", "falls", "replay", "fallsdef", "phase", "refall", "spp", "sharp", "dvfall", "absmono", "abspw", "dupchk", "gapb", "k4bp", "klow", "pk", "kt", "yzwm", "ntf", "yzs", "yzc", "slow", "fdl", "meet", "root"): return score_py(g)
    try:
        r = subprocess.run([oink, SOLVER] + OINKFLAGS + (["-t", "-t", "-t"] if fitness in ("strch", "newrecur", "maxsets", "pairs") else ["-t", "-t"] if fitness.startswith("per") or fitness in ("prunemono", "dups", "alpha", "straddles", "restarts", "maxrestarts", "osc") else []) + (["-v"] if fitness == "wrong" else []) + [tmp, tmp + ".sol"], capture_output=True, text=True, timeout=20)
    except subprocess.TimeoutExpired:
        return 10 ** 6          # a timeout is interesting in itself
    if fitness in ("unsolved", "wrong"):
        try: solved = sum(1 for l in open(tmp + ".sol") if l.strip() and not l.startswith("paritysol"))
        except FileNotFoundError: solved = n
        bad = 0
        if fitness == "wrong":      # Oink's own verifier (-v): a failed verification or a solver error counts 1000
            out = r.stdout + r.stderr
            bad = 1000 if ("error" in out.lower() or "verified" not in out) else 0
        return n - solved + bad
    if fitness in ("maxsets", "pairs"):   # (D): max distinct region vertex sets at one top / total distinct (top, set) pairs, all pieces
        import importlib.util, os as _os
        spec = importlib.util.spec_from_file_location("sc", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "dtl_strchanges.py"))
        sc = importlib.util.module_from_spec(spec); spec.loader.exec_module(sc)
        out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr)
        regions, seen, changes, occ, sets_per_top = sc.measure(out)
        return max((len(v) for v in sets_per_top.values()), default=0) if fitness == "maxsets" else len(seen)
    if fitness == "newrecur":        # new tangles learned at a (top, region set) seen before (the end state of the Lead's 18:02Z item 1)
        import importlib.util, os as _os
        spec = importlib.util.spec_from_file_location("sc", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "dtl_strchanges.py"))
        sc = importlib.util.module_from_spec(spec); spec.loader.exec_module(sc)
        out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr)
        return sc.measure(out)[2].get("__newrecur__", 0)
    if fitness == "strch":          # GAP-A: strategy changes at a fixed (top, region set), detector build at -t -t -t
        import importlib.util, os as _os
        spec = importlib.util.spec_from_file_location("sc", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "dtl_strchanges.py"))
        sc = importlib.util.module_from_spec(spec); spec.loader.exec_module(sc)
        out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr)
        return sum(sc.measure(out)[2].values())
    if fitness in ("alpha", "straddles"):
        # with the L-RED detector build (scratchpad oink-det): "STRADDLE tangle ..." lines at every stable pruning result,
        # "REGION top X closed 0/1" lines from sptl. straddles: count of STRADDLE lines. alpha: stable sets that have a
        # STRADDLE line and whose first sptl pass has its LOWEST top's region open (the (alpha) precondition + containment proxy)
        out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr)
        if fitness == "straddles": return out.count("STRADDLE tangle")
        score, straddle, regions, instable = 0, False, [], False
        def close_set():
            nonlocal score, straddle, regions, instable
            if instable and regions and straddle:
                # first sptl pass = the REGION lines until the top priority rises again; its last line is the lowest top
                first = [regions[0]]
                for prv, cur in zip(regions, regions[1:]):
                    if cur[0] > prv[0]: break
                    first.append(cur)
                if not first[-1][1]: score += 1
            instable = False; straddle = False; regions = []
        for line in out.splitlines():
            line = re.sub(r"^\[\s*[0-9.]+\]\s*", "", line)
            if line.startswith("STRADDLE tangle"): straddle = True
            if line.startswith("best vertices:"):
                close_set()
                if "(stable)" in line: instable = True
                continue
            if line.startswith("iteration") or line.startswith("current region"): close_set(); continue
            if instable and line.startswith("REGION top"):
                w = line.split(); regions.append((int(w[w.index("pr") + 1]), w[-1] == "1"))
        close_set()
        return score
    if fitness in ("prunemono", "dups"):
        # prunemono: vertices pruned by the first best_vertices call of a search but not by that of the previous search of
        # the same player (a non-monotone pruning, R8 section 12 / proof lane (r1)); dups: "duplicate tangle" lines
        out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr)
        if fitness == "dups": return out.count("duplicate tangle")
        searches = []; cur = None
        for line in out.splitlines():
            line = re.sub(r"^\[\s*[0-9.]+\]\s*", "", line)
            m2 = re.match(r"iteration (\d+)-(even|odd)", line)
            if m2: cur = {"player": m2.group(2), "pruned": set(), "done": False}; searches.append(cur); continue
            if cur is None or cur["done"]: continue
            if line.startswith("distance "): cur["pruned"].update(re.findall(r"(\S+?)/\d+", line.split(":", 1)[1]))
            if line.startswith("best vertices:"): cur["done"] = True
        return sum(len(b["pruned"] - a["pruned"]) for a, b in zip(searches, searches[1:]) if a["player"] == b["player"])
    if fitness == "evens":          # Even's searches only ("even iterations: k"); with --maxeven K (<= K Even-priority vertices,
        m2 = re.search(r"even iterations: (\d+)", r.stdout + r.stderr)   # i.e. <= K possible tops) more than K+1 searches force repeated learning at a top
        return int(m2.group(1)) if m2 else -1
    if fitness == "iters":          # searches in the whole run (each search after the first learns a new tangle or dominion)
        m2 = re.search(r"solved in (\d+) iterations", r.stdout + r.stderr)
        return int(m2.group(1)) if m2 else -1
    if fitness == "osc":
        # membership oscillation (L-ALG F8 shape): over the sequence of tangles learned at one top P, a vertex that leaves and
        # re-enters (or enters, leaves, re-enters) counts one per change beyond the first; summed over (P, vertex) pairs
        seq = {}
        for line in re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr).splitlines():
            m2 = re.search(r"new tangle (\d+) \((\d+)\) \(depth (\d+)\)(.*) with (\d+) escape", line)
            if m2: seq.setdefault(m2.group(1), []).append(frozenset(tok.split("->")[0] for tok in m2.group(4).split()))
        tot = 0
        for P, sets in seq.items():
            for v in set().union(*sets):
                ch = sum(1 for a, b in zip(sets, sets[1:]) if (v in a) != (v in b))
                tot += max(0, ch - 1)
        return tot
    if fitness in ("restarts", "maxrestarts"):
        # chain restarts: a new tangle at top P whose vertex set is not a superset of the previous tangle learned at P
        # (within one search tangles at a top form a growing chain, L-ALG 2026-10-16; a restart happens across searches).
        # restarts: total over tops; maxrestarts: the most at one top. Use --injective so P names the top.
        last = {}; tot = 0; per = {}
        for line in re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr).splitlines():
            m2 = re.search(r"new tangle (\d+) \((\d+)\) \(depth (\d+)\)(.*) with (\d+) escape", line)
            if not m2: continue
            P = m2.group(1); vs = frozenset(tok.split("->")[0] for tok in m2.group(4).split())
            if P in last and not vs >= last[P]: tot += 1; per[P] = per.get(P, 0) + 1
            last[P] = vs
        return tot if fitness == "restarts" else max(per.values(), default=0)
    if fitness in ("perhead", "perheadsearch", "persearch"):
        import collections
        c = collections.Counter(); it = 0
        for line in re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr).splitlines():
            if "iteration" in line: it += 1
            m2 = re.search(r"new tangle (\d+) \(", line)
            if m2: c[("*" if fitness == "persearch" else m2.group(1), 0 if fitness == "perhead" else it)] += 1
        return max(c.values(), default=0)
    m = re.search(r"found (\d+) dominions and (\d+) tangles", r.stdout + r.stderr)
    return int(m.group(2)) if m else -1


def okeven(g): return not maxeven or sum(1 for q in g[0] if q % 2 == 0) <= maxeven


def random_game():
    pr = rng.sample(range(n), n) if injective else [rng.randrange(maxpr + 1) for _ in range(n)]; ow = [rng.randrange(2) for _ in range(n)]
    if maxeven:
        ev = rng.sample(range(n), maxeven)
        pr = [(q | 1) if v not in ev else (q & ~1) for v, q in enumerate(pr)]
    succ = [{rng.randrange(n)} | {rng.randrange(n) for _ in range(rng.randrange(3))} for _ in range(n)]
    return pr, ow, succ


def mutate(g):
    pr, ow, succ = list(g[0]), list(g[1]), [set(s) for s in g[2]]
    v = rng.randrange(n); k = rng.random()
    if loops and k < 0.3:                      # self-loop on/off (never removed as the only edge)
        if v in succ[v] and len(succ[v]) > 1: succ[v].discard(v)
        else: succ[v].add(v)
        return pr, ow, succ
    if loops and k < 0.45:                     # swap the ids of two vertices of equal priority (tie order of the sort)
        same = [w for w in range(n) if pr[w] == pr[v] and w != v]
        if same:
            w = rng.choice(same)
            def sw(x): return w if x == v else v if x == w else x
            pr[v], pr[w] = pr[w], pr[v]; ow[v], ow[w] = ow[w], ow[v]
            succ = [set(map(sw, succ[sw(x)])) for x in range(n)]
        return pr, ow, succ
    if k < 0.4:
        w = rng.randrange(n)
        if w in succ[v] and len(succ[v]) > 1: succ[v].discard(w)
        else: succ[v].add(w)
    elif k < 0.75:
        if injective: w = rng.randrange(n); pr[v], pr[w] = pr[w], pr[v]
        else: pr[v] = rng.randrange(maxpr + 1)
    else: ow[v] ^= 1
    return pr, ow, succ


if "--eval" in sys.argv:          # print the fitness of one game and exit
    pr, ow, succ = [], [], []
    for line in open(sys.argv[sys.argv.index("--eval") + 1]):
        m = re.match(r"^(\d+)\s+(\d+)\s+([01])\s+([\d,]+)", line.strip())
        if m: pr.append(int(m.group(2))); ow.append(int(m.group(3))); succ.append({int(x) for x in m.group(4).split(",")})
    n = len(pr); print(f"{sys.argv[sys.argv.index('--eval') + 1].split('/')[-1]} {fitness}: {score((pr, ow, succ))}"); os.unlink(tmp); sys.exit(0)
t0 = time.time(); g = random_game()
if "--from" in sys.argv:      # start from a given game (perturbation search); n is taken from the file
    pr, ow, succ = [], [], []
    for line in open(sys.argv[sys.argv.index("--from") + 1]):
        m = re.match(r"^(\d+)\s+(\d+)\s+([01])\s+([\d,]+)", line.strip())
        if m: pr.append(int(m.group(2))); ow.append(int(m.group(3))); succ.append({int(x) for x in m.group(4).split(",")})
    n = len(pr); maxpr = max(maxpr, max(pr)); g = (pr, ow, succ)
    if "--grow" in sys.argv:      # append k fresh vertices (random priority/owner/edges, each with one edge from an old vertex)
        k = int(sys.argv[sys.argv.index("--grow") + 1])
        for j in range(k):
            pr.append(rng.randrange(maxpr + 1)); ow.append(rng.randrange(2)); v = n + j
            succ.append({rng.randrange(v + 1)} | {rng.randrange(v + 1) for _ in range(rng.randrange(3))})
            succ[rng.randrange(v)].add(v)
        n = len(pr); g = (pr, ow, succ)
while evenmin and g[1].count(0) < evenmin * n: g = random_game()
cur = score(g); best = (cur, g); hb = arg("--hb", 0)
print(f"start: {cur} n={n}", flush=True)
for i in range(steps):
    h = mutate(g)
    if evenmin and h[1].count(0) < evenmin * n: continue
    if not okeven(h): continue
    sc = score(h)
    if hb and i % hb == 0: print(f"hb step {i}: best {best[0]} ({time.time() - t0:.0f}s)", flush=True)
    if sc >= cur:
        g, cur = h, sc
        if sc > best[0]:
            best = (sc, h); print(f"step {i}: {sc} tangles ({time.time() - t0:.0f}s)", flush=True)
            if "--out" in sys.argv: open(sys.argv[sys.argv.index("--out") + 1], "w").write(dumps(h))
if "--out" in sys.argv: open(sys.argv[sys.argv.index("--out") + 1], "w").write(dumps(best[1]))
os.unlink(tmp)
print(f"n={n} seed={seed}: best {best[0]} tangles after {steps} steps ({time.time() - t0:.0f}s)")
