#!/usr/bin/env python3
"""B5 (L-RED-B successor 4; docs/red-b/B5-second-fb.md): direct test of Lemma ONE-FB (k = 1 on every guided wrapper Wg) and of its
proof's intermediate claims, per iteration of N5 (SPEC, L-NEW's box190/n5v.py mode spec) from S3 on L-SI's gscan104.wrapg wrappers
(claude/l-si 2051a0ee via git archive; core placement by env CORE = high | low, as gscan104 reads it).
Must-0 counters (unit: one wrapper):
  tau     tau changes at some iteration                       itau  I_tau is nonempty at some state
  k       the number of fallbacks is not 1                    pre   a state before the first fallback F has sigma(K0) != pA or (K0, K1) not in I_sigma
  f1      iteration F+1 is a fallback, or after it sigma(K1) != q (or the run ends before F+1)
  f2      the run reaches F+2 and iteration F+2 is a fallback or the state after it is not CLOSED (sigma(K0) = K1, sigma(K1) = q,
          every valve at pb)
  post    a fallback occurs after F, or some state from F+2 on is not CLOSED, or at some CLOSED state from F+1 on Odd's optimal
          counterstrategy (S1, si.Engine.evaluate) differs from tau at an Odd vertex
  wrong   N5's output regions != harness Zielonka on the wrapper     engdiff  (I, k) of n5v != (I, k) of n5b --mode spec (engine 2)
Variant FREE (outside the lemma's hypothesis, used as the CONTROL and for B5 part 2): every Odd vertex o of H gets, with probability
FREE, one more non-valve face o -> f1 -> ... -> f5 -> t (all pads Omega 0, 6 edges, t a random vertex of H); S3 still picks the guide
face z1 (Omega 1). On FREE wrappers the counters may fire; they are reported, not required to be 0.
CONTROLS: CTRL=1, every check is made with F + 1 in place of F (pre must fire); CTRL=2, CLOSED expects the valves at y
(f2 and post must fire).
Variant MIRROR=1 (construction X2, §4): a disjoint mirror copy of the core (owners swapped, priorities + 1) is added; Odd then
keeps a permanent improving edge, so itau fires by design and the lemma's k = 1 is replaced by k = 2 (§4).
Usage: b5lemma.py B3ROOT (states FILE... | fam NAME n... | rand SEED COUNT NMAX [FREE])     env CORE, N5B=0 skips engine 2."""
import sys, os, json, re, random, hashlib, subprocess, tempfile
root = os.path.abspath(sys.argv[1])
os.environ["LNEW"] = os.path.join(root, "lnew"); os.environ["LRED"] = os.path.join(root, "lred")
os.environ["LLIT"] = os.path.join(root, "llit"); os.environ["HN"] = os.path.join(root, "lcomp/experiments/friedmann-hn")
sys.path.insert(0, os.path.join(root, "lsi/experiments/si/box104")); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gscan104 as GS
import wrap104 as W
from wrap104 import pg, n5v, n5, n5x, zielonka
from si import Engine
N5B = os.path.join(root, "trunk/experiments/n5-second/n5b.py"); USE_N5B = os.environ.get("N5B", "1") == "1"
CORE = GS.CORE; MIRROR = os.environ.get("MIRROR", "0") == "1"; CTRL = int(os.environ.get("CTRL", "0"))   # CTRL=1: F+1 for F (pre must fire); CTRL=2: y for pb (f2, post must fire)
NAMES = ["tau", "itau", "k", "pre", "f1", "f2", "post", "wrong", "engdiff"]

def fam(name, n):
    if name == "fried": r = W.fried_game(n); return r[0], list(r[1])
    if name == "lmcs": H, s0 = W.lmcs_game(n, "fig4"); return H, list(s0)
    if name == "hn": H, s0 = GS.fam("hn", n); return H, list(s0)
    raise ValueError(name)

def build(H, s0, rho0, gamma, copy, free=None):
    """gscan104.wrapg, plus (free) extra non-valve Odd faces {o: t}. Returns g, K (4 core ids), pA, q, valves."""
    g, std_s, std_t, mp, inv, valves = GS.wrapg(H, s0, rho0, gamma, copy)
    n = H.n; K = [n, n + 1, n + 2, n + 3]; pA, q = n + 4, n + 6
    assert g.succ[K[0]] == sorted([K[1], pA]) and g.owner[K[2]] == 1 and q in g.succ[K[1]]
    if free or MIRROR:
        prio, own, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]
        for o, t in sorted((free or {}).items()):
            nxt = t
            for i in range(5): prio.append(0); own.append(0); succ.append([nxt]); nxt = len(prio) - 1
            succ[o] = sorted(succ[o] + [nxt])
        if MIRROR:   # a disjoint copy of the core with owners swapped and priorities + 1 (box 104 §7, READING «mirror image of the core»)
            b0 = len(prio); M = {x: b0 + i for i, x in enumerate(K + [pA, n + 5, q, n + 7])}
            for x in K + [pA, n + 5, q, n + 7]:
                prio.append(g.prio[x] + 1); own.append(1 - g.owner[x]); succ.append(None)
            for x in K + [pA, n + 5, q, n + 7]: succ[M[x]] = [M[y] for y in g.succ[x]]
        g = pg.Game(prio, own, [sorted(s) for s in succ])
    return g, K, pA, q, valves

def run_one(tag, g, K, pA, q, valves):
    E, Ed = Engine(g), Engine(n5.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None)
    states = [(tuple(sigma), tuple(tau))]; fbl = []; Isl = []; Itl = []; its = 0
    while its < 10 ** 6:
        r = n5v.step(g, E, Ed, sigma, tau, "spec")
        if r is None: Isl.append(None); Itl.append(None); break
        ns, nt, Is, It, fb = r; its += 1; Isl.append(Is); Itl.append(It)
        if fb: fbl.append(its)
        sigma, tau = ns, nt; states.append((tuple(sigma), tuple(tau)))
    c = dict.fromkeys(NAMES, 0); odd = [v for v in range(g.n) if g.owner[v] == 1]
    c["tau"] = int(any(states[j][1] != states[0][1] for j in range(len(states))))
    c["itau"] = int(any(It for It in Itl if It is not None))
    c["k"] = int(len(fbl) != 1)
    if fbl:
        F = fbl[0] + (CTRL == 1)
        c["pre"] = int(any(states[j][0][K[0]] != pA or (K[0], K[1]) not in set(Isl[j]) for j in range(F)))
        c["f1"] = int(its < F + 1 or (F + 1) in fbl or states[F + 1][0][K[1]] != q)
        pbs = {b: (pbof(g, b, K) if CTRL != 2 else [w for w in g.succ[b] if w != pbof(g, b, K)][0]) for b in valves}
        def closed(j): return states[j][0][K[0]] == K[1] and states[j][0][K[1]] == q and all(states[j][0][b] == pbs[b] for b in valves)
        c["f2"] = int(its >= F + 2 and ((F + 2) in fbl or not closed(F + 2)))
        bad = any(f > F for f in fbl)
        for j in range(F + 1, len(states)):
            if bad: break
            if j == F + 1 and not closed(j): continue
            if not closed(j): bad = True; break
            _, cs = E.evaluate(states[j][0]); t = states[j][1]
            bad = any(cs[o] != t[o] for o in odd)
        c["post"] = int(bad)
    else:
        c["pre"] = c["f1"] = c["f2"] = c["post"] = 1
    vs, _ = E.evaluate(states[-1][0]); win = [0 if g.prio[vs[v][0]] % 2 == 0 else 1 for v in range(g.n)]
    c["wrong"] = int(win != zielonka.solve(g))
    e2 = "skipped"
    if USE_N5B:
        fd, path = tempfile.mkstemp(suffix=".pg"); os.close(fd); pg.write(g, path)
        sha = hashlib.sha1(open(path, "rb").read()).hexdigest()
        rr = subprocess.run([sys.executable, N5B, path, "--mode", "spec"], capture_output=True, text=True); os.remove(path)
        m = re.search(r"iterations (\d+) fallbacks (\d+)", rr.stdout)
        c["engdiff"] = int(not m or (int(m.group(1)), int(m.group(2))) != (its, len(fbl))); e2 = ("I %s k %s" % m.groups()) if m else "FAILED"
    else:
        sha = "-"
    F = fbl[0] if fbl else None
    print("B5LEMMA core %s%s %s |Wg| %d sha1 %s | I %d k %d fallbacks at %s P1 %s | n5b %s | %s" % (CORE, " mirror" if MIRROR else "", tag, g.n, sha, its, len(fbl),
          fbl[:10], (its - F) if F else "-", e2, " ".join("%s %d" % (x, c[x]) for x in NAMES)), flush=True)
    return c

def pbof(g, b, K):
    """the pb successor of valve b (the one leading to K0)."""
    for w in g.succ[b]:
        if g.succ[w] == [K[0]]: return w
    raise ValueError(b)

def rand_H(rng, n):
    prio = list(range(n)); rng.shuffle(prio); own = [rng.randrange(2) for _ in range(n)]
    succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 3)))) for v in range(n)]
    return pg.Game(prio, own, succ)

def main():
    tot = dict.fromkeys(NAMES, 0); cnt = 0; mode = sys.argv[2]
    def add(c):
        nonlocal cnt
        cnt += 1
        for x in NAMES: tot[x] += c[x]
    if mode == "fam":
        name = sys.argv[3]
        for n in map(int, sys.argv[4:]):
            H, s0 = fam(name, n); EH = Engine(H)
            _, cs = EH.evaluate(tuple(s0[v] if H.owner[v] == 0 else -1 for v in range(H.n)))
            rho0 = {v: cs[v] for v in range(H.n) if H.owner[v] == 1}
            add(run_one("%s_n%d_own" % (name, n), *build(H, s0, rho0, {}, True)))
    elif mode == "states":
        for sf in sys.argv[3:]:
            S = json.load(open(sf)); base = os.path.basename(sf)[:-5]
            if base.startswith("gfam_") or base.startswith("b4c_b4_"):
                m = re.match(r"(?:gfam|b4c_b4)_([a-z]+)_n(\d+)_s\d+_c(\d)", base); H = fam(m.group(1), int(m.group(2)))[0]
                copy = m.group(3) == "1"; G = S["G"]
                s0 = [G["s0"].get(str(v), -1) if H.owner[v] == 0 else -1 for v in range(H.n)]
                rho0 = {v: G["rho"][str(v)] for v in range(H.n) if H.owner[v] == 1}
                gamma = {tuple(map(int, k.split(","))): t for k, t in G["gam"].items()}
            else:
                D = S["D"]; copy = base.endswith("_c1"); H = pg.Game(D["prio"], D["own"], D["succ"])
                s0 = [D["s0"][str(v)] if D["own"][v] == 0 else -1 for v in range(H.n)]
                rho0 = {v: D["rho"][str(v)] for v in range(H.n) if D["own"][v] == 1}
                gamma = {tuple(map(int, k.split(","))): t for k, t in D["gam"].items()}
            add(run_one(base, *build(H, s0, rho0, gamma, copy)))
    elif mode == "rand":
        seed, count, nmax = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]); free = float(sys.argv[6]) if len(sys.argv) > 6 else 0.0
        rng = random.Random(seed)
        for i in range(count):
            n = rng.randint(2, nmax); H = rand_H(rng, n)
            s0 = [rng.choice(H.succ[v]) if H.owner[v] == 0 else -1 for v in range(n)]
            rho0 = {v: (rng.choice(H.succ[v]) if rng.random() < 0.5 else rng.randrange(n)) for v in range(n) if H.owner[v] == 1}
            gamma = {(v, w): rng.randrange(n) for v in range(n) if H.owner[v] == 0 for w in H.succ[v] if rng.random() < 0.3}
            copy = rng.random() < 0.5
            fr = {v: rng.randrange(n) for v in range(n) if H.owner[v] == 1 and rng.random() < free} if free > 0 else None
            add(run_one("rand_s%d_i%d_n%d_free%s" % (seed, i, n, len(fr) if fr else 0), *build(H, s0, rho0, gamma, copy, fr)))
    print("B5LEMMA SUMMARY core %s mode %s wrappers %d | %s" % (CORE, " ".join(sys.argv[2:]), cnt, " ".join("%s %d" % (x, tot[x]) for x in NAMES)), flush=True)

if __name__ == "__main__":
    main()
