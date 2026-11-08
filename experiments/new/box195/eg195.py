#!/usr/bin/env python3
"""Box 195 ENDGAME (L-NEW successor 63): checks, iteration by iteration, every clause of Lemmas E0-E4 and Theorem ENDGAME-3 on the
N5'-xi run (box 190 n5v.step, mode xi) from S3 on Gamma3(G) (box 189 gamma3.build, all pads).
Per run, counters (unit: states or iterations of the run):
  e0fail   states with tau != tau0 or It != empty                                  (E0)
  e1fail   states before the first fallback with K-config != k0, or Is on K != {(K0,K1)}, or S4a changing the K-config (E1)
  e2fail   first fallback not an Even fallback, or its result's K-config != k1        (E2)
  e3fail   iteration F+1: K-config != k1 at its start, Is on K != {(K1,q)}, a fallback, or result K-config != k2 (E3)
  e4fail   iteration F+2: K-config != k2, Is on K != {(K3,K1)}, some beta with sigma = its mover Xi-target lacking (beta, pb) in Is,
           a fallback, result K-config != k3, or some beta with a mover Xi-target not on pb in the result            (E4 (a))
  stopfail the state after F+2 has Is or It nonempty                                  (E4 (b))
  finsbar  in that final state: sigma-bar not pe at some gate, or sigma-bar(K2) != K2
  fintie   in that final state: some mover with two options (pads m_(x,k)) of different values
  acyc, lfail  (only with env LRED = a tree holding L-RED's experiments/red/r187 + r178) acyclic genomes, and those whose run does not have
           F = L(G) + 1 and exactly L(G) + 3 iterations (L(G) = ideal.traj, R104's IDEAL run length)
  env EG195_MODE = xi (default, N5'-xi) or spec (N5 itself, SPEC S4a)
  controls EG195_CTRL=1: E3/E4 expectations swapped and the final checks run on the state before the fallback (must fire);
           EG195_CTRL=2: start with tau(K2) = r and sigma(K1) = q (not S3; must fire e0 / e1)
  nofb     runs with no fallback (cap reached)
  (fb, post) tally: #fallbacks and iterations from the first fallback (incl.) to the end; ENDGAME-3 predicts (1, 3).
Families: the 6 structured families of L-RED R221 §11 (spost221.py gen(), transcribed with credit: esc, noesc, deep, dense, late*,
lvl0, plus acyc = Xi-edges to smaller indices only; *late here = start at the option of LEAST index-reversed order, a stand-in: own.py is L-RED's and is not imported) and plain random
(rand). Usage: eg195.py FAMILY SEED COUNT | eg195.py --files G.json ..."""
import sys, os, json, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.environ.get("EG195_ROOT") or os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [os.path.join(ROOT, "experiments/new/box189"), os.path.join(ROOT, "experiments/new/box190"),
                os.path.join(ROOT, "experiments/new/box21"), os.path.join(ROOT, "experiments/new"), os.path.join(ROOT, "experiments/si"),
                os.path.join(ROOT, "experiments/harness")]
import gamma3, n5v, n5x, pg

PADS = {"K", "pe", "pb", "m"}
MODE = os.environ.get("EG195_MODE", "xi")            # "xi" = N5'-xi; "spec" = N5 itself (SPEC S4a, box 190 n5v mode spec)
LRED = os.environ.get("LRED")                         # optional: a tree holding L-RED's experiments/red/r187 + r178 (ideal.traj, for L(G))
if LRED:
    sys.path[:0] = [os.path.join(LRED, "experiments/red/r187"), os.path.join(LRED, "experiments/red/r178")]
    import ideal

def acyclic(G):
    N, opts = G["N"], G["opts"]; col = [0] * N
    def dfs(x):
        col[x] = 1
        for o in opts[x]:
            y = o[1]
            if y >= 0 and (col[y] == 1 or (col[y] == 0 and not dfs(y))): return False
        col[x] = 2; return True
    return all(col[x] or dfs(x) for x in range(N))

def topg(g): return pg.parse(f"parity {g.n - 1};\n" + "".join(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n" for v in range(g.n)))

def check(G, cap=20000):
    g0, _, _, V = gamma3.build(G, PADS); g = topg(g0)
    K0, K1, K2, K3 = (V[("K", i)] for i in range(4)); pA, s, q, r = V["pA"], V["s"], V["q"], V["r"]
    k0, k1, k2, k3 = (pA, s, K2), (K1, s, K2), (K1, q, K2), (K1, q, K1)
    ctrl = os.environ.get("EG195_CTRL") == "1"
    if ctrl: k1, k2 = k2, k1                                    # negative control: wrong expectations must fire e2/e3/e4
    pre = None
    O = [(x, k) for x in range(G["N"]) for k in range(len(G["opts"][x]))]
    betas = [(V[("b", o)], G["opts"][o[0]][o[1]][1], V[("pb", o)]) for o in O]          # (beta, xt or -1, pb)
    gates = [(V[("g", o)], V[("pe", o)]) for o in O]
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None)
    if os.environ.get("EG195_CTRL") == "2": tau[K2] = r; sigma[K1] = q   # negative control: a non-S3 start must fire e0 / e1
    tau0 = list(n5x.start_pair(g, E, Ed, None)[1])
    kc = lambda sg: (sg[K0], sg[K1], sg[K3]); kset = lambda I: {(v, w) for v, w in I if v in (K0, K1, K3)}
    c = collections.Counter(); it = 0; F = None
    while it < cap:
        vt, _ = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
        if list(tau) != tau0 or It: c["e0fail"] += 1
        vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        res = n5v.step(g, E, Ed, sigma, tau, MODE)
        if res is None:
            if F is None: c["nofb"] += 1
            break
        ns, nt, _, _, fb = res; it += 1
        if F is None and not fb:
            if kc(sigma) != k0 or kset(Is) != {(K0, K1)} or kc(ns) != k0: c["e1fail"] += 1
        elif F is None and fb:
            F = it; pre = (list(sigma), list(tau))
            if kc(sigma) != k0 or not Is or kc(ns) != k1 or list(nt) != list(tau): c["e2fail"] += 1
        elif it == F + 1:
            if kc(sigma) != k1 or kset(Is) != {(K1, q)} or fb or kc(ns) != k2: c["e3fail"] += 1
        elif it == F + 2:
            bad = kc(sigma) != k2 or kset(Is) != {(K3, K1)} or fb or kc(ns) != k3
            bad = bad or any(xt >= 0 and sigma[b] == xt and (b, pb) not in Is for b, xt, pb in betas)
            bad = bad or any(xt >= 0 and ns[b] != pb for b, xt, pb in betas)
            if bad: c["e4fail"] += 1
        else: c["late"] += 1                                    # an iteration after F + 2
        sigma, tau = ns, nt
    else: c["capped"] += 1
    if F is not None:
        if ctrl: sigma, tau = pre                               # negative control: final checks on the pre-fallback state
        vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        vt, _ = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
        if Is or It: c["stopfail"] += 1
        if any(sbar[gt] != pe for gt, pe in gates) or sbar[K2] != K2: c["finsbar"] += 1
        bad = False
        for x in range(G["N"]):
            vals = {tuple(vs[V[("m", (x, k))]]) if isinstance(vs[V[("m", (x, k))]], (list, tuple)) else vs[V[("m", (x, k))]] for k in range(len(G["opts"][x]))}
            if len(vals) != 1: bad = True
        if bad: c["fintie"] += 1
    if LRED and acyclic(G):
        L = len(ideal.traj(G)[0]) - 1; c["acyc"] += 1
        if F is None or F != L + 1 or it != L + 3: c["lfail"] += 1   # R117 REACH3 (F = L + 1) + ENDGAME-3: total L(G) + 3
    if MODE != "spec": c.pop("lfail", None)                      # L(G) + 3 is the N5 (spec) statement only
    return dict(xi=it, F=F, post=(it - F + 1) if F else None, **c)

def gen(rng, mode):
    """L-RED R221 §11 spost221.py gen(), transcribed (credit L-RED 56); 'late' replaced (see module doc); 'rand' = d 1-5 plain."""
    d = rng.randint(6, 9) if mode == "deep" else rng.randint(1, 5); w = rng.randint(1, 2) if mode == "deep" else rng.randint(1, 3)
    D = rng.randint(3, 4) if mode in ("dense", "lvl0") else rng.choice([2, 3])
    lev = [x // w for x in range(d * w)]
    if mode == "lvl0": lev = [0] * rng.randint(2, 4) + lev
    N = len(lev); opts = []
    for x in range(N):
        oo = []
        for _ in range(D):
            wt = rng.choice([y for y in range(N) if lev[y] == lev[x] - 1]) if lev[x] else -1
            if mode == "esc": xt = -1 if rng.random() < 0.7 else rng.randrange(N)
            elif mode == "noesc": xt = rng.randrange(N)
            elif mode == "acyc": xt = rng.choice(list(range(x)) + [-1, -1])          # Xi-edges to smaller index only: acyclic
            else: xt = rng.choice(list(range(N)) + [-1])
            oo.append([wt, xt, 0])
        opts.append(oo)
    M = sum(len(o) for o in opts); perm = list(range(M)); rng.shuffle(perm); gate = []; i = 0
    for x in range(N):
        gate.append([])
        for o in opts[x]: o[2] = i; gate[x].append(perm[i]); i += 1
    br = list(range(M)); rng.shuffle(br)
    G = {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": [rng.randrange(2) for _ in range(M)],
         "start": [rng.randrange(len(o)) for o in opts]}
    if mode == "late": G["start"] = [len(o) - 1 for o in opts]
    return G

def summarize(name, rows):
    tot = collections.Counter(); tally = collections.Counter()
    for rw in rows:
        for k in ("e0fail", "e1fail", "e2fail", "e3fail", "e4fail", "stopfail", "finsbar", "fintie", "nofb", "late", "capped", "acyc", "lfail"): tot[k] += rw.get(k, 0)
        tally[(1 if rw["F"] else 0, rw["post"])] += 1
    f = " ".join(f"{k} {tot[k]}" for k in ("e0fail", "e1fail", "e2fail", "e3fail", "e4fail", "stopfail", "finsbar", "fintie", "nofb", "late", "capped", "acyc", "lfail"))
    print(f"{os.environ.get('EG195_TAG', '')}{name} mode {MODE} runs {len(rows)} {f} tally(F?,post) {sorted(tally.items())} maxxi {max(rw['xi'] for rw in rows)}", flush=True)

if __name__ == "__main__":
    if sys.argv[1] == "--files":
        for fn in sys.argv[2:]:
            G = json.load(open(fn))
            if isinstance(G, dict) and "genome" in G: G = G["genome"]
            if not (isinstance(G, dict) and "opts" in G and "start" in G): print(os.path.basename(fn), "skipped (not a genome with a start)"); continue
            summarize(os.path.basename(fn), [check(G)])
    else:
        mode, seed, cnt = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed)
        summarize(f"{mode} seed {seed}", [check(gen(rng, mode)) for _ in range(cnt)])
