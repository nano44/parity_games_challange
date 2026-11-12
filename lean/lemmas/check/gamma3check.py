#!/usr/bin/env python3
"""Reading check of PGLemmas/Gamma3.lean against the fleet's builders of Gamma3(G) and Gamma3*(G*).

For every genome file given, the script
  1. builds the reference game:
     mode r104 (default): experiments/new/box189/gamma3.py  build(G, {"K","pe","pb","m"})  (the builder of
                          P-N5-REACH, RESULTS R117's Gamma3(G));
     mode free (GAMMA3_MODE=free): L-SI's build_free (experiments/si/box104/free104.py on claude/l-si 3417f6c1,
                          transcribed below as build_free_ref) with carrier priorities drawn at random (seeded
                          by GAMMA3_SEED and the file name): 2M distinct integers >= 6 of either parity;
  2. writes a Lean file that defines the same genome as a `PG.Genome` and the carriers as a `Carrier`
     (mode r104: `G.r104`; mode free: the drawn table) and evaluates, for every vertex of `Genome.Vertex3`,
        (idx3, prio3, isOdd3, indices of the successors in E3, idx3 of start3, pr3);
  3. runs Lean on that file (in lean/lemmas, which must be built) and compares, vertex by vertex:
        prio, owner, successor set, start (sigma on Even's vertices, tau on Odd's: the builder's sigma0, tau0,
        «R104's stated start transported through the pads»), and the injective priority
        p'(v) = 2*rank(v) + (prio(v) mod 2), rank by (prio(v), v)  (si.py).
This is DATA about the DEFINITIONS (is the Lean game the fleet's game?), not a proof.

Usage (from the repository root):
    python3 -I lean/lemmas/check/gamma3check.py GENOME.json [GENOME.json ...]
    GAMMA3_MODE=free GAMMA3_SEED=1 python3 -I lean/lemmas/check/gamma3check.py GENOME.json ...
Control: GAMMA3_CTRL=1 swaps the indices of pe_g and pbeta_g in the Python reference; the comparison must
then report mismatches.  FREE104_SRC=<path of free104.py> also compares the transcription below with the
source's `def build_free` block, line for line (printed as «transcription match»).

Counters (must be 0): nfail (vertex count), miss (a vertex index without a Lean row), priofail, ownfail,
succfail, startfail, prfail  (unit: vertex).
"""
import ast
import json
import os
import random
import subprocess
import sys
import tempfile
import zlib

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path[:0] = [os.path.join(ROOT, "experiments", "new", "box189"), os.path.join(ROOT, "experiments", "harness"),
                os.path.join(ROOT, "experiments", "new")]
import gamma3  # noqa: E402  (the fleet's builder)
import pg  # noqa: E402

CTRL = os.environ.get("GAMMA3_CTRL") == "1"
MODE = os.environ.get("GAMMA3_MODE", "r104")
SEED = int(os.environ.get("GAMMA3_SEED", "1"))
LEAN_DIR = os.path.join(ROOT, "lean", "lemmas")
PADS = {"K", "pe", "pb", "m"}


# --- transcription of L-SI's free104.py build_free (claude/l-si 3417f6c1), with its two helpers ---
def options(G): return [(x, k) for x in range(G["N"]) for k in range(len(G["opts"][x]))]

def build_free(G, pb, pe):
    """Gamma3*(G): pb[q], pe[q] = the priorities of beta_q and e_q (distinct integers >= 6). Returns (game, sigma0, tau0, V)."""
    gm, sig, tau, V = gamma3.build(G, PADS); prio = list(gm.prio); O = options(G)
    vals = [pb[q] for q in O] + [pe[q] for q in O]
    assert len(set(vals)) == len(vals) and min(vals) >= 6, "carrier priorities must be distinct and >= 6"
    for q in O: prio[V[("b", q)]] = pb[q]; prio[V[("e", q)]] = pe[q]
    top = max(vals) + 2; top += top % 2
    K0, K1, K2, K3 = (V[("K", i)] for i in range(4))
    prio[V["cW"]] = top; prio[K0], prio[K1], prio[K2], prio[K3] = top + 2, 5, 3, top + 3
    assert all(prio[v] <= 2 for kk, v in V.items() if not (isinstance(kk, tuple) and kk[0] in ("b", "e", "K")) and kk != "cW")
    return pg.Game(prio, list(gm.owner), [list(s) for s in gm.succ]), sig, tau, V
# --- end of transcription ---


def transcription_check(path):
    """compare the `def build_free` block of the given free104.py with the transcription above (line for line)."""
    src = open(path).read().split("\n")
    i = next(j for j, ln in enumerate(src) if ln.startswith("def build_free("))
    j = next(k for k in range(i + 1, len(src)) if src[k] and not src[k].startswith(" "))
    while j > i and not src[j - 1].strip():
        j -= 1
    mine = open(os.path.abspath(__file__)).read().split("\n")
    a = next(j2 for j2, ln in enumerate(mine) if ln.startswith("def build_free("))
    return src[i:j] == mine[a:a + (j - i)], j - i


def draw_carriers(G, name):
    rnd = random.Random(SEED * 1000003 + zlib.crc32(name.encode()))
    O = options(G)
    vals = rnd.sample(range(6, 6 + 6 * len(O) + 10), 2 * len(O))
    return {q: vals[i] for i, q in enumerate(O)}, {q: vals[len(O) + i] for i, q in enumerate(O)}


def lean_source(G, carriers):
    N, lev, opts, gate, br, bp, start = G["N"], G["lev"], G["opts"], G["gate"], G["br"], G["bp"], G["start"]

    def lst(x):
        return "[" + ", ".join(lst(y) if isinstance(y, list) else str(y) for y in x) + "]"

    wt = [[(o[0] if o[0] >= 0 else N) for o in ov] for ov in opts]
    xt = [[(o[1] if o[1] >= 0 else N) for o in ov] for ov in opts]
    brk = [[br[o[2]] for o in ov] for ov in opts]
    bpk = [[bp[o[2]] for o in ov] for ov in opts]
    if carriers is None:
        car = "def π : G.Carrier := G.r104"
    else:
        pb, pe = carriers
        pbT = [[pb[(x, k)] for k in range(len(opts[x]))] for x in range(N)]
        peT = [[pe[(x, k)] for k in range(len(opts[x]))] for x in range(N)]
        car = (f"def pbT : List (List ℕ) := {lst(pbT)}\ndef peT : List (List ℕ) := {lst(peT)}\n"
               "def π : G.Carrier := ⟨fun o => look pbT o.1.val o.2.val, fun o => look peT o.1.val o.2.val⟩")
    return f"""import PGLemmas.Gamma3
open PG

def NN : ℕ := {N}
def levT : List ℕ := {lst(lev)}
def degT : List ℕ := {lst([len(o) for o in opts])}
def wtT : List (List ℕ) := {lst(wt)}
def xtT : List (List ℕ) := {lst(xt)}
def gateT : List (List ℕ) := {lst(gate)}
def brT : List (List ℕ) := {lst(brk)}
def bpT : List (List ℕ) := {lst(bpk)}
def stT : List ℕ := {lst(start)}

def toOpt (m : ℕ) : Option (Fin NN) := if h : m < NN then some ⟨m, h⟩ else none
def look (t : List (List ℕ)) (x k : ℕ) : ℕ := (t.getD x []).getD k 0

def G : Genome where
  N := NN
  lev := fun x => levT.getD x.val 0
  deg := fun x => (degT.getD x.val 1 - 1) + 1
  wt := fun o => toOpt (look wtT o.1.val o.2.val)
  xt := fun o => toOpt (look xtT o.1.val o.2.val)
  gate := fun o => look gateT o.1.val o.2.val
  brank := fun o => look brT o.1.val o.2.val
  bpar := fun o => look bpT o.1.val o.2.val
  start := fun x => ⟨stT.getD x.val 0 % ((degT.getD x.val 1 - 1) + 1), Nat.mod_lt _ (Nat.succ_pos _)⟩

{car}

def opts : List G.Opt :=
  (List.finRange G.N).flatMap (fun x => (List.finRange (G.deg x)).map (fun k => (⟨x, k⟩ : G.Opt)))
def oldv : List G.Vertex :=
  (List.finRange G.N).map Genome.Vertex.mover ++ opts.map Genome.Vertex.gate ++
    opts.map Genome.Vertex.beta ++ opts.map Genome.Vertex.eface ++
    [Genome.Vertex.cX, Genome.Vertex.cW, Genome.Vertex.K0, Genome.Vertex.K1, Genome.Vertex.K2,
      Genome.Vertex.K3]
def verts : List G.Vertex3 :=
  oldv.map Genome.Vertex3.old ++ [Genome.Vertex3.pA, Genome.Vertex3.pS, Genome.Vertex3.pQ,
    Genome.Vertex3.pR] ++ opts.map Genome.Vertex3.pe ++ opts.map Genome.Vertex3.pbeta ++
    opts.map Genome.Vertex3.pb ++ opts.map Genome.Vertex3.m
def row (v : G.Vertex3) : ℕ × ℕ × Bool × List ℕ × ℕ × ℕ :=
  (G.idx3 v, G.prio3 π v, G.isOdd3 v, (verts.filter (fun u => decide (u ∈ G.E3 v))).map G.idx3,
    G.idx3 (G.start3 v), G.pr3 π v)
#eval do
  IO.println s!"{{Fintype.card G.Vertex3}};{{G.M}};{{verts.length}}"
  for v in verts do
    let r := row v
    IO.println s!"{{r.1}};{{r.2.1}};{{r.2.2.1}};{{r.2.2.2.1}};{{r.2.2.2.2.1}};{{r.2.2.2.2.2}}"
"""


def reference(G, carriers):
    if carriers is None:
        g, sig, tau, V = gamma3.build(G, PADS)
    else:
        g, sig, tau, V = build_free(G, *carriers)
    n = g.n
    prio, own, succ = list(g.prio), list(g.owner), [sorted(s) for s in g.succ]
    start = [sig[v] if own[v] == 0 else tau[v] for v in range(n)]
    if CTRL:  # swap the indices of pe_g and pbeta_g: the Lean table must then disagree
        perm = list(range(n))
        for q in options(G):
            a, b = V[("pe", q)], V[("pbeta", q)]
            perm[a], perm[b] = b, a
        prio = [prio[perm[v]] for v in range(n)]
        own = [own[perm[v]] for v in range(n)]
        succ = [sorted(perm[u] for u in succ[perm[v]]) for v in range(n)]
        start = [perm[start[perm[v]]] for v in range(n)]
    order = sorted(range(n), key=lambda v: (prio[v], v))
    rank = [0] * n
    for r, v in enumerate(order):
        rank[v] = r
    pp = [2 * rank[v] + prio[v] % 2 for v in range(n)]
    return n, prio, own, succ, start, pp


def main():
    if os.environ.get("FREE104_SRC"):
        ok, nlines = transcription_check(os.environ["FREE104_SRC"])
        print(f"transcription match {int(ok)} ({nlines} lines of build_free)")
        if not ok:
            sys.exit(3)
    total = dict(nfail=0, miss=0, priofail=0, ownfail=0, succfail=0, startfail=0, prfail=0)
    vertices = 0
    for path in sys.argv[1:]:
        G = json.load(open(path))
        carriers = draw_carriers(G, os.path.basename(path)) if MODE == "free" else None
        n, prio, own, succ, start, pp = reference(G, carriers)
        with tempfile.TemporaryDirectory() as d:
            f = os.path.join(d, "Gamma3Check.lean")
            open(f, "w").write(lean_source(G, carriers))
            env = dict(os.environ)
            env["PATH"] = os.path.join(os.path.expanduser("~"), ".elan", "bin") + os.pathsep + env.get("PATH", "")
            out = subprocess.run(["lake", "env", "lean", f], cwd=LEAN_DIR, env=env, capture_output=True, text=True)
        if out.returncode != 0:
            print(f"{os.path.basename(path)}: LEAN FAILED (exit {out.returncode})\n{out.stdout[-2000:]}\n{out.stderr[-2000:]}")
            sys.exit(2)
        lines = out.stdout.strip().split("\n")
        card, M, nv = (int(x) for x in lines[0].split(";"))
        rows = []
        for ln in lines[1:]:
            a, b, c, l, d, e = ln.split(";")
            rows.append((int(a), int(b), c.strip() == "true", ast.literal_eval(l), int(d), int(e)))
        cnt = dict.fromkeys(total, 0)
        Mref = sum(len(o) for o in G["opts"])
        if card != n or nv != n or len(rows) != n or M != Mref or n != G["N"] + 7 * Mref + 10:
            cnt["nfail"] += 1
        byidx = {r[0]: r for r in rows}
        for v in range(n):
            if v not in byidx:
                cnt["miss"] += 1
                continue
            _, lp, lodd, lsucc, lstart, lpr = byidx[v]
            cnt["priofail"] += lp != prio[v]
            cnt["ownfail"] += int(lodd) != own[v]
            cnt["succfail"] += sorted(lsucc) != succ[v]
            cnt["startfail"] += lstart != start[v]
            cnt["prfail"] += lpr != pp[v]
        vertices += n
        for k in total:
            total[k] += cnt[k]
        print(f"{os.path.basename(path)}: N {G['N']} M {M} n {n} " + " ".join(f"{k} {v}" for k, v in cnt.items()))
    print(f"gamma3check mode {MODE} seed {SEED if MODE == 'free' else '-'} ctrl {int(CTRL)}: genomes {len(sys.argv) - 1} "
          f"vertices {vertices} " + " ".join(f"{k} {v}" for k, v in total.items()))


if __name__ == "__main__":
    main()
