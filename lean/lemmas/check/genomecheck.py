#!/usr/bin/env python3
"""Reading check of PGLemmas/Genome.lean against the fleet's builder of the game Gamma(G).

For every genome file given, the script
  1. builds Gamma(G) with experiments/red/r187/stab.py  build(G, 0, kgad=True, esc=True)
     (the builder that RESULTS R104 / P-N5-REALIZE section 3.1 names);
  2. writes a Lean file that defines the same genome as a `PG.Genome` and evaluates, for every
     vertex of `Genome.Vertex`, the tuple
        (idx, prio, isOdd, indices of the successors in E, idx of start0, pr);
  3. runs Lean on that file (in lean/lemmas, which must be built) and compares, vertex by vertex:
        prio, owner, successor set, start (sigma_0 on Even's vertices, tau_0 on Odd's), and the
        injective priority  p'(v) = 2*rank(v) + (prio(v) mod 2), rank by (prio(v), v)  (si.py).
This is DATA about the DEFINITIONS (is the Lean game the fleet's game?), not a proof.

Usage (from the repository root):
    python3 -I lean/lemmas/check/genomecheck.py GENOME.json [GENOME.json ...]
Control: GEN_CTRL=1 swaps the two faces' indices in the Python reference (e_g <-> beta_g); the
comparison must then report mismatches.

Counters (must be 0): nfail (vertex count), miss (a vertex index without a Lean row),
priofail, ownfail, succfail, startfail, prfail  (unit: vertex).
"""
import ast
import json
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path[:0] = [os.path.join(ROOT, "experiments", "red", "r187")]
import stab  # noqa: E402  (the fleet's builder; it adds its own import paths)

CTRL = os.environ.get("GEN_CTRL") == "1"
LEAN_DIR = os.path.join(ROOT, "lean", "lemmas")


def lean_source(G):
    N, lev, opts, gate, br, bp, start = G["N"], G["lev"], G["opts"], G["gate"], G["br"], G["bp"], G["start"]

    def lst(x):
        return "[" + ", ".join(lst(y) if isinstance(y, list) else str(y) for y in x) + "]"

    wt = [[(o[0] if o[0] >= 0 else N) for o in ov] for ov in opts]
    xt = [[(o[1] if o[1] >= 0 else N) for o in ov] for ov in opts]
    brk = [[br[o[2]] for o in ov] for ov in opts]
    bpk = [[bp[o[2]] for o in ov] for ov in opts]
    return f"""import PGLemmas.Genome
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

def opts : List G.Opt :=
  (List.finRange G.N).flatMap (fun x => (List.finRange (G.deg x)).map (fun k => (⟨x, k⟩ : G.Opt)))
def verts : List G.Vertex :=
  (List.finRange G.N).map Genome.Vertex.mover ++ opts.map Genome.Vertex.gate ++
    opts.map Genome.Vertex.beta ++ opts.map Genome.Vertex.eface ++
    [Genome.Vertex.cX, Genome.Vertex.cW, Genome.Vertex.K0, Genome.Vertex.K1, Genome.Vertex.K2,
      Genome.Vertex.K3]
def row (v : G.Vertex) : ℕ × ℕ × Bool × List ℕ × ℕ × ℕ :=
  (G.idx v, G.prio v, G.isOdd v, (verts.filter (fun u => decide (u ∈ G.E v))).map G.idx,
    G.idx (G.start0 v), G.pr v)
#eval do
  IO.println s!"{{Fintype.card G.Vertex}};{{G.M}}"
  for v in verts do
    let r := row v
    IO.println s!"{{r.1}};{{r.2.1}};{{r.2.2.1}};{{r.2.2.2.1}};{{r.2.2.2.2.1}};{{r.2.2.2.2.2}}"
"""


def reference(G):
    g, sig, tau, gv, ev, bv = stab.build(G, 0, kgad=True, esc=True)
    n = g.n
    prio, own, succ = list(g.prio), list(g.owner), [sorted(s) for s in g.succ]
    start = [sig[v] if own[v] == 0 else tau[v] for v in range(n)]
    if CTRL:  # swap the indices of e_g and beta_g: the Lean table must then disagree
        perm = list(range(n))
        for q in gv:
            perm[ev[q]], perm[bv[q]] = bv[q], ev[q]
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
    total = dict(nfail=0, miss=0, priofail=0, ownfail=0, succfail=0, startfail=0, prfail=0)
    vertices = 0
    for path in sys.argv[1:]:
        G = json.load(open(path))
        n, prio, own, succ, start, pp = reference(G)
        with tempfile.TemporaryDirectory() as d:
            f = os.path.join(d, "GenomeCheck.lean")
            open(f, "w").write(lean_source(G))
            env = dict(os.environ)
            env["PATH"] = os.path.join(os.path.expanduser("~"), ".elan", "bin") + os.pathsep + env.get("PATH", "")
            out = subprocess.run(["lake", "env", "lean", f], cwd=LEAN_DIR, env=env, capture_output=True, text=True)
        if out.returncode != 0:
            print(f"{os.path.basename(path)}: LEAN FAILED (exit {out.returncode})\n{out.stdout[-2000:]}\n{out.stderr[-2000:]}")
            sys.exit(2)
        lines = out.stdout.strip().split("\n")
        card, M = (int(x) for x in lines[0].split(";"))
        rows = []
        for ln in lines[1:]:
            a, b, c, l, d, e = ln.split(";")
            rows.append((int(a), int(b), c.strip() == "true", ast.literal_eval(l), int(d), int(e)))
        cnt = dict.fromkeys(total, 0)
        if card != n or len(rows) != n or M != sum(len(o) for o in G["opts"]):
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
    print(f"genomecheck ctrl {int(CTRL)}: genomes {len(sys.argv) - 1} vertices {vertices} "
          + " ".join(f"{k} {v}" for k, v in total.items()))


if __name__ == "__main__":
    main()
