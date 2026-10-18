"""L-ALG succ. 10 (box 12, produced on Opus 5.5), GAP-A-M §32: pigeonhole keys on the FIRST-DIFFERENCE contexts R* of a phase (any
depth; first difference as in dtl_ctxclimb.fitness / fixd_fdpos.py, reduced logs). (CTX⁺) counts the distinct R* per phase. A key
κ(R*) with poly many values bounds (CTX⁺) if the distinct R* sharing one key stay poly; the strongest form is "≤ 1" (every new R*
has a new key). Keys: κ-d (depth), κ-s (|R*|), κ-ds (depth, |R*|), κ-dsm (depth, |R*|, max priority in R*),
κ-dj (depth, depth-0 chain position j of R*), κ-djs (depth, j, |R*|). Printed per corpus: transitions, distinct R* (max per phase),
and for each key the max number of distinct R* sharing one key value in one phase, with the instance.
Corpus: b12_topchain.classgames with CLASS=1, else the files. Usage: DTL_ORDER=stable|oink [CLASS=1 ...] b12_fdkey.py G.pg ...
   or: DTL_ORDER=... b12_fdkey.py climb C START.pg STEPS SEED OUTDIR   (class-preserving climb against the keys)"""
import sys, os
os.environ.setdefault("RM_DV", "0"); os.environ.setdefault("RM_LIGHT", "1")
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_rootmono as RMo
from b12_topchain import classgames
FD = RMo.FD


def fdctx(g):
    """per phase: list of (depth, R*, j) over its transitions with a first difference."""
    d0 = FD.P.X.build(g); d = RMo.RM(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
    st = {"dropped": 0, "kept: differs": 0, "kept: identical but extracts": 0}; out = []
    for ph in FD.phase_rows(d):
        for r in ph: r["log"] = RMo.FC.reduce_log(r["log"], st)
        seq = []
        for a, b in zip(ph, ph[1:]):
            la = [i for i, e in enumerate(a["log"]) if e[0] not in ("extract", "pass")]
            lb = [i for i, e in enumerate(b["log"]) if e[0] not in ("extract", "pass")]
            k = 0
            while k < min(len(la), len(lb)) and a["log"][la[k]][:4] == b["log"][lb[k]][:4]: k += 1
            if k == min(len(la), len(lb)): continue
            pos = lb[k]; rec = next((r_ for r_ in b["recs"] if r_["start"] <= pos < r_["end"]), None)
            if rec is None: continue
            dep, R = rec["key"]; c0 = b["ctx0"]; j = max((i for i, C in enumerate(c0) if R <= C), default=-1)
            seq.append((dep, frozenset(R), j))
        out.append(seq)
    return out, d0.pr


def plain(files, nmax):
    for f in files:
        try:
            g = pg.read(f)
        except ValueError:
            continue
        if g.n <= nmax: yield os.path.basename(f), g


KEYS = {"κ-d": lambda dep, R, j, pr: dep, "κ-s": lambda dep, R, j, pr: len(R), "κ-ds": lambda dep, R, j, pr: (dep, len(R)),
        "κ-dsm": lambda dep, R, j, pr: (dep, len(R), max(pr[v] for v in R)), "κ-dj": lambda dep, R, j, pr: (dep, j),
        "κ-djs": lambda dep, R, j, pr: (dep, j, len(R))}

if __name__ == "__main__" and sys.argv[1] == "climb":
    sys.setrecursionlimit(100000)
    import importlib; M = importlib.import_module("b12_fdkey")
    M.climb(int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]); sys.exit(0)

if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable")
    src = classgames(sys.argv[1:], int(os.environ.get("TRIALS", "2")), int(os.environ.get("SEED", "1")), int(os.environ.get("NMAX", "200"))) \
        if os.environ.get("CLASS") == "1" else plain(sys.argv[1:], int(os.environ.get("NMAX", "200")))
    trans = 0; mxctx = (0, None); best = {k: (0, None) for k in KEYS}
    for name, g in src:
        try:
            phases, pr = fdctx(g)
        except RecursionError:
            continue
        for seq in phases:
            trans += len(seq); ctx = {R for _, R, _ in seq}
            if len(ctx) > mxctx[0]: mxctx = (len(ctx), (name, g.n, len(seq)))
            for k, f in KEYS.items():
                by = {}
                for dep, R, j in seq: by.setdefault(f(dep, R, j, pr), set()).add(R)
                m = max((len(s) for s in by.values()), default=0)
                if m > best[k][0]: best[k] = (m, (name, g.n, len(seq)))
    print("order", order, "transitions", trans, "| max distinct R* per phase", mxctx)
    for k in KEYS: print(f"  {k:6s} max distinct R* sharing one key value in one phase: {best[k][0]:4d}  at {best[k][1]}")


def score(g):
    """(max distinct R* sharing a κ-djs value, same for κ-dsm, max distinct R* per phase, transitions) over the phases of g."""
    phases, pr = fdctx(g); best = (0, 0, 0, 0)
    for seq in phases:
        m = []
        for k in ("κ-djs", "κ-dsm"):
            by = {}
            for dep, R, j in seq: by.setdefault(KEYS[k](dep, R, j, pr), set()).add(R)
            m.append(max((len(s) for s in by.values()), default=0))
        best = max(best, (m[0], m[1], len({R for _, R, _ in seq}), len(seq)))
    return best


def climb(C, start_file, steps, seed, out):
    """class-preserving climb (fixd_oneplayer.mutate in 𝒞_C, priorities all-distinct) on score(); a first slot ≥ 2 or a second
    slot ≥ 2 is a violation of (FD-KEY-djs) / (FD-KEY-dsm) and is written to out."""
    import random
    from fixd_oneplayer import mutate
    from fixd_ctx1p import distinct
    rnd = random.Random(seed); g = distinct(pg.read(start_file)); P = max(g.prio) + 1; sg = score(g); os.makedirs(out, exist_ok=True)
    print("start", sg, flush=True)
    for it in range(steps):
        h = mutate(g, C, P, rnd)
        if h is None: continue
        h = distinct(h)
        try:
            sh = score(h)
        except (RecursionError, Exception):
            continue
        if sh >= sg:
            if sh > sg: print(it, sh, flush=True)
            g, sg = h, sh
            if sg[0] >= 2 or sg[1] >= 2:
                fn = os.path.join(out, f"fdkey_viol_C{C}_n{g.n}_s{seed}.pg"); pg.write(g, fn); print("VIOLATION", sg, fn, flush=True)
                if sg[0] >= 2 and sg[1] >= 2: return
    fn = os.path.join(out, f"fdkey_final_C{C}_n{g.n}_s{seed}.pg"); pg.write(g, fn); print("final", sg, fn)
