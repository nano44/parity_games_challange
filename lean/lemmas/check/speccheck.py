#!/usr/bin/env python3
"""Machine comparison of PGLemmas/Spec.lean (N5's step as SPEC S1-S5, DEFINITIONS) against the fleet's engine, state by
state (L-FORMAL successor 4; Lead 23:53Z item (b), in the genomecheck / gamma3check pattern).

For every instance given (a .pg file; its .start file of the same stem is used if present, else SPEC S3's best-reward
start), the script
  1. runs the REFERENCE: experiments/new/box190/n5v.py `step(g, E, Ed, sigma, tau, mode)` with mode "spec" (= box21
     n5x.py `step`; valuations experiments/si/si.py Engine), from n5x.py `start_pair`, up to CAP iterations, and records
     per state (sigma, tau), Xi_sigma = E.evaluate(sigma) (valuation and sigma-bar), and per step (I_sigma, I_tau, fallback);
  2. writes a Lean file that defines the same game as a `PG.Spec.SGame` and evaluates `specRun`, and per state
     `Eng.evaluate` on G, `Eng.improving`, and the key rule `Eng.keyRule` on the four procedure calls of the step
     (G, G^d, dual(H) of S4a, H' of S4b);
  3. runs Lean (in lean/lemmas; `lake build PGLemmas.Spec` first) and compares.
This is DATA about the DEFINITIONS (is the Lean step SPEC's step?), not a proof of anything.

Counters (must be 0), with units:
  runfail   (instance)          number of iterations or the stop flag differ
  statefail (state, vertex)     sigma at Even's / tau at Odd's vertices differ
  valfail   (state, vertex)     Xi_sigma(v) = (cycle node, path mask over ranks, length) differs
  sbarfail  (state, Odd vertex) sigma-bar differs
  isfail, itfail, fbfail (step) I_sigma, I_tau (as sets of edges), the fallback flag differ
  fuelfail  (step / state)      Lean's `fuelOut` flag (a fuel bound was reached) is set
  faultfail (step / state)      Lean's `fault` flag (a si.py exception case or a None choice) is set
  keyfail   (call, vertex)      Lean's procedure output violates Lean's key rule (R24 Lemma R + TB, DATA)
Controls (must fire):
  SPEC_CTRL=idx (or xi, seq): the reference uses n5v.py mode "idx" (S4a's tie broken by the largest index), "xi" or
                "seq" instead of "spec": statefail must become > 0 on instances where the tie rule matters;
  SPEC_CTRL=fbsmall: the reference breaks S4c's fallback ties to the SMALLER index (SPEC: larger); it must fire on the
                tie instances check/spec_ties/A.pg, B.pg (Lead 03:58Z);
  keyctrl (always printed): the key rule with both comparisons reversed (largest index / lex-LARGEST key) on the same
                calls; it must fire wherever a tie with >= 2 tied successors occurs (ties are counted per mode).
Gamma3 mode (SPEC_GAMMA3=1, genome JSON files): the reference is box189 gamma3.build(G, {K, pe, pb, m}) with its start;
  Lean uses G.sgame3 G.r104 with its own start3Pair.  SPEC_START=S3 instead runs both from SPEC S3's best-reward start
  (Lean: `n5Gamma3S3`, i.e. specRun (sgame3 π) none).  Column s3eq (REFEREE-2 40 U-3): per genome, the vertices where
  Lean's Eng.initialBest on sgame3 (Even; Odd on the dual, FIX 1) differs from start3Pair (counts and the first few).
FBDETAIL lines: for every fallback step, the vertices the fallback changes, with the reference's and Lean's new successor.
Usage (from the repository root): python3 -I lean/lemmas/check/speccheck.py FILE.pg [FILE.pg ...]
  env: SPEC_CAP (default 200), SPEC_CTRL, SPEC_MAXN (skip games with more vertices; default 600), SPEC_GAMMA3, SPEC_START."""
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
LEMMAS = os.path.join(ROOT, "lean", "lemmas")
sys.path[:0] = [os.path.join(ROOT, p) for p in
                ("experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
import n5x   # noqa: E402
import n5v   # noqa: E402
from si import Engine   # noqa: E402

CAP = int(os.environ.get("SPEC_CAP", "200"))
MODE = os.environ.get("SPEC_CTRL", "spec") or "spec"
MAXN = int(os.environ.get("SPEC_MAXN", "600"))
LEAN = os.environ.get("LEAN_CMD", "lake env lean")


def reference(g, start):
    E, Ed = Engine(g), Engine(n5x.dual(g))
    sigma, tau = n5x.start_pair(g, E, Ed, start)
    states, recs = [(list(sigma), list(tau))], []
    stopped = False
    while len(recs) < CAP:
        r = n5v.step(g, E, Ed, sigma, tau, "spec" if MODE == "fbsmall" else MODE)
        if r is None:
            stopped = True
            break
        ns, nt, Is, It, fb = r
        if MODE == "fbsmall" and fb:   # CONTROL: fallback ties to the smaller index
            vs, _ = E.evaluate(tuple(sigma)); vt, _ = Ed.evaluate(tuple(tau))
            ns, nt = list(sigma), list(tau)
            if Is:
                for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), -w))
            else:
                for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), -w))
        recs.append((sorted(Is), sorted(It), fb))
        sigma, tau = list(ns), list(nt)
        states.append((sigma, tau))
    vals = []
    for s, _ in states:
        val, sbar = E.evaluate(tuple(s))
        vals.append((val, sbar))
    return states, recs, stopped, vals


def lst(x):
    return "[" + ", ".join(str(y) for y in x) + "]"


IMPORTS = "import PGLemmas.Spec\nopen PG.Spec\n"
HEADER = """
/-- CONTROL (check tool only, not a definition of the lane): the key rule with both comparisons reversed. -/
def keyCtrlAt (E : Eng) (strat : Array ℕ) (o : EvalOut) (x : ℕ) : Bool :=
  let c := (o.valOf x).c
  if E.owner[x]! != 1 || c == x then true else
  match o.tau[x]! with
  | none => false
  | some t =>
    let T := E.tied o x
    let s : Array ℕ := (Array.range E.n).map fun y =>
      if E.owner[y]! == 0 then strat[y]! else (o.tau[y]!).getD y
    T.contains t &&
      (if E.par[c]! == 0 then T.all (fun w => w ≤ t)
       else T.all (fun w => lexLe (rootKey s c E.n w) (rootKey s c E.n t)))

/-- per call: (key rule failures, control failures, ties in longest mode, ties in BFS mode) -/
def keyCounts (E : Eng) (strat : Array ℕ) (o : EvalOut) : ℕ × ℕ × ℕ × ℕ :=
  (List.range E.n).foldl (fun (a, b, c, d) x =>
    let cx := (o.valOf x).c
    let app := E.owner[x]! == 1 && cx != x
    let tie := app && (E.tied o x).length ≥ 2
    (a + (if E.keyRuleAt strat o x then 0 else 1), b + (if keyCtrlAt E strat o x then 0 else 1),
     c + (if tie && E.par[cx]! == 0 then 1 else 0), d + (if tie && E.par[cx]! == 1 then 1 else 0))) (0, 0, 0, 0)

def showP (l : List (ℕ × ℕ)) : String := String.intercalate "," (l.map fun p => s!"{p.1}:{p.2}")
def showV : Option SVal → String
  | none => "-"
  | some x => s!"{x.c},{x.mask},{x.len}"
def showO : Option ℕ → String
  | none => "-"
  | some x => toString x
"""


def lean_file(g, start, gdef=None):
    n = g.n
    succ = "#[" + ", ".join(lst(s) for s in g.succ) + "]"
    st = "none" if start is None else "some ([%s], [%s])" % (
        ", ".join("(%d, %d)" % (v, w) for v, w in sorted(start[0].items())),
        ", ".join("(%d, %d)" % (v, w) for v, w in sorted(start[1].items())))
    s3eq = "pure ()"
    if gdef is None:
        gdef = f"def g : SGame := ⟨{n}, #{lst(g.prio)}, #{lst(g.owner)}, {succ}⟩"
        pre = IMPORTS + HEADER
    else:
        gdef, pre, st, s3eq = gdef
    return pre + f"""
{gdef}

#eval do
  let E := Eng.ofGame g
  let Ed := Eng.ofGame g.dual
  let r := specRun g ({st}) {CAP}
  IO.println s!"RUN {{r.steps.length}} {{r.stopped}}"
  {s3eq}
  let mut i := 0
  for (s, t) in r.states do
    let ov := E.evaluate s
    let od := Ed.evaluate t
    let mut kc := keyCounts E s ov
    let kd := keyCounts Ed t od
    kc := (kc.1 + kd.1, kc.2.1 + kd.2.1, kc.2.2.1 + kd.2.2.1, kc.2.2.2 + kd.2.2.2)
    let Is := E.improving s ov
    let It := Ed.improving t od
    if !Is.isEmpty then
      let Er := Eng.ofGame (arenaH g s t Is).dual
      let o := Er.evaluate t
      let k := keyCounts Er t o
      kc := (kc.1 + k.1, kc.2.1 + k.2.1, kc.2.2.1 + k.2.2.1, kc.2.2.2 + k.2.2.2)
    if !It.isEmpty then
      let Er := Eng.ofGame (arenaH' g s t It)
      let o := Er.evaluate s
      let k := keyCounts Er s o
      kc := (kc.1 + k.1, kc.2.1 + k.2.1, kc.2.2.1 + k.2.2.1, kc.2.2.2 + k.2.2.2)
    IO.println s!"S {{i}} {{String.intercalate "," ((List.range g.n).map fun v => toString (if g.owner[v]! == 0 then s[v]! else t[v]!))}}"
    IO.println s!"V {{i}} {{String.intercalate ";" ((List.range g.n).map fun v => showV ov.val[v]!)}}"
    IO.println s!"B {{i}} {{String.intercalate "," ((List.range g.n).map fun v => showO ov.tau[v]!)}}"
    IO.println s!"K {{i}} {{kc.1}} {{kc.2.1}} {{kc.2.2.1}} {{kc.2.2.2}} {{ov.fuelOut || od.fuelOut}} {{ov.fault || od.fault}}"
    i := i + 1
  let mut j := 0
  for x in r.steps do
    IO.println s!"T {{j}} {{x.fb}} {{x.fuelOut}} {{x.fault}} {{showP x.Is}} {{showP x.It}}"
    j := j + 1
"""


def run_lean(src):
    with tempfile.NamedTemporaryFile("w", suffix=".lean", dir=LEMMAS, delete=False) as f:
        f.write(src)
        path = f.name
    try:
        p = subprocess.run(LEAN.split() + [path], cwd=LEMMAS, capture_output=True, text=True)
    finally:
        os.unlink(path)
    if p.returncode != 0:
        raise SystemExit("lean failed:\n" + p.stdout[-3000:] + p.stderr[-3000:])
    return p.stdout


GAMMA3 = os.environ.get("SPEC_GAMMA3") == "1"
START = os.environ.get("SPEC_START", "")


def gamma3_instance(path):
    """Gamma3(G) of a genome JSON: the reference game, start pair and the Lean text defining `g` and the start."""
    import json
    sys.path.insert(0, os.path.join(LEMMAS, "check"))
    import gamma3check   # the genome writer of check/gamma3check.py (and through it box189's gamma3.build)
    G = json.load(open(path))
    gm, sig, tau, _ = gamma3check.gamma3.build(G, gamma3check.PADS)
    start = ({v: sig[v] for v in range(gm.n) if gm.owner[v] == 0}, {v: tau[v] for v in range(gm.n) if gm.owner[v] == 1})
    src = gamma3check.lean_source(G, None)
    genome = src[:src.index("\ndef opts : List G.Opt")]
    genome = "\n".join(l for l in genome.split("\n") if not l.startswith(("import ", "open ")))
    pre = "import PGLemmas.SpecGamma3\nopen PG PG.Spec\n" + genome + "\n" + HEADER
    gdef = "def g : SGame := G.sgame3 π"
    s3eq = ("let E3 := Eng.ofGame g\n  let Ed3 := Eng.ofGame g.dual\n  let p3 := G.start3Pair\n"
            "  let be := p3.1.filter (fun (q : ℕ × ℕ) => E3.initialBest[q.1]! != q.2)\n"
            "  let bo := p3.2.filter (fun (q : ℕ × ℕ) => Ed3.initialBest[q.1]! != q.2)\n"
            "  IO.println s!\"S3EQ {be.length} {p3.1.length} {bo.length} {p3.2.length} {(be ++ bo).take 8}\"")
    if START == "S3":
        return gm, None, (gdef, pre, "none", s3eq)
    return gm, start, (gdef, pre, "some G.start3Pair", s3eq)


def main(files):
    tot = dict(runfail=0, statefail=0, valfail=0, sbarfail=0, isfail=0, itfail=0, fbfail=0, fuelfail=0, faultfail=0,
               keyfail=0)
    ctrl = dict(keyctrl=0, ties_longest=0, ties_bfs=0)
    s3 = [0, 0, 0, 0, 0]   # genomes with a difference, even diffs, even total, odd diffs, odd total
    nst = nstep = ninst = nv = 0
    skipped = []
    for path in files:
        if GAMMA3:
            g, start, gd = gamma3_instance(path)
        else:
            g = n5x.load(path)
            sp = path[:-3] + ".start"
            start = n5x.readstart(sp) if os.path.exists(sp) else None
            gd = None
        if g.n > MAXN:
            skipped.append((os.path.basename(path), g.n))
            continue
        states, recs, stopped, vals = reference(g, start)
        out = run_lean(lean_file(g, start, gd)).splitlines()
        loc = dict.fromkeys(tot, 0)
        L = {}
        T = {}
        K = {}
        s3line = None
        lrun = None
        for l in out:
            f = l.split(" ")
            if f[0] == "RUN":
                lrun = (int(f[1]), f[2] == "true")
            elif f[0] in ("S", "V", "B"):
                L[(f[0], int(f[1]))] = f[2] if len(f) > 2 else ""
            elif f[0] == "K":
                K[int(f[1])] = (int(f[2]), int(f[3]), int(f[4]), int(f[5]), f[6] == "true", f[7] == "true")
            elif f[0] == "T":
                T[int(f[1])] = (f[2] == "true", f[3] == "true", f[4] == "true", f[5] if len(f) > 5 else "",
                                f[6] if len(f) > 6 else "")
            elif f[0] == "S3EQ":
                s3line = l
        if lrun != (len(recs), stopped):
            loc["runfail"] += 1
        for i, (s, t) in enumerate(states):
            if ("S", i) not in L:
                loc["statefail"] += g.n
                continue
            ls = L[("S", i)].split(",")
            ref = [s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)]
            loc["statefail"] += sum(1 for v in range(g.n) if int(ls[v]) != ref[v])
            val, sbar = vals[i]
            lv = L[("V", i)].split(";")
            for v in range(g.n):
                rv = "%d,%d,%d" % val[v] if val[v] is not None else "-"
                if lv[v] != rv:
                    loc["valfail"] += 1
            lb = L[("B", i)].split(",")
            for v in range(g.n):
                if g.owner[v] == 1 and lb[v] != str(sbar[v]):
                    loc["sbarfail"] += 1
            kf, kcf, tl, tb, fo, fa = K[i]
            loc["keyfail"] += kf
            ctrl["keyctrl"] += kcf
            ctrl["ties_longest"] += tl
            ctrl["ties_bfs"] += tb
            loc["fuelfail"] += int(fo)
            loc["faultfail"] += int(fa)
        for j, (Is, It, fb) in enumerate(recs):
            if j not in T:
                loc["isfail"] += 1
                continue
            lfb, lfo, lfa, lIs, lIt = T[j]
            pIs = sorted(tuple(map(int, p.split(":"))) for p in lIs.split(",") if p)
            pIt = sorted(tuple(map(int, p.split(":"))) for p in lIt.split(",") if p)
            loc["isfail"] += int(pIs != sorted(map(tuple, Is)))
            loc["itfail"] += int(pIt != sorted(map(tuple, It)))
            loc["fbfail"] += int(lfb != bool(fb))
            loc["fuelfail"] += int(lfo)
            loc["faultfail"] += int(lfa)
            if fb:   # FBDETAIL: what the fallback changed (reference vs Lean)
                (s0, t0), (s1, t1) = states[j], states[j + 1]
                ls1 = L.get(("S", j + 1), "").split(",")
                for v in range(g.n):
                    a, b = (s0[v], s1[v]) if g.owner[v] == 0 else (t0[v], t1[v])
                    if a != b:
                        print("FBDETAIL %s step %d %s %d: %d -> ref %d, lean %s" % (
                            os.path.basename(path), j + 1, "sigma" if g.owner[v] == 0 else "tau", v, a, b,
                            ls1[v] if v < len(ls1) else "?"))
        if s3line:
            f = s3line.split(" ")
            de, ne, do, no = int(f[1]), int(f[2]), int(f[3]), int(f[4])
            s3[0] += int(de + do > 0); s3[1] += de; s3[2] += ne; s3[3] += do; s3[4] += no
            print("S3EQ %s: even %d of %d differ, odd %d of %d differ; first %s" % (
                os.path.basename(path), de, ne, do, no, " ".join(f[5:])))
        ninst += 1
        nst += len(states)
        nstep += len(recs)
        nv += g.n
        for k in tot:
            tot[k] += loc[k]
        print("%s n=%d iterations=%d stopped=%s fallbacks=%d start=%s %s" % (
            os.path.basename(path), g.n, len(recs), stopped, sum(r[2] for r in recs), "file" if start else "S3",
            " ".join("%s=%d" % (k, v) for k, v in loc.items() if v)), flush=True)
    print("MODE %s CAP %d%s" % (MODE, CAP, (" GAMMA3 START %s" % (START or "start3")) if GAMMA3 else ""))
    print("instances %d, vertices %d, states %d, steps %d" % (ninst, nv, nst, nstep))
    print("COUNTERS " + " ".join("%s=%d" % kv for kv in tot.items()))
    print("CONTROL " + " ".join("%s=%d" % kv for kv in ctrl.items()))
    if GAMMA3:
        print("S3EQ genomes with a difference %d of %d; Even vertices differing %d of %d; Odd vertices differing %d of %d"
              % (s3[0], ninst, s3[1], s3[2], s3[3], s3[4]))
    if skipped:
        print("SKIPPED (n > %d): %s" % (MAXN, ", ".join("%s(n=%d)" % s for s in skipped)))


if __name__ == "__main__":
    main(sys.argv[1:])
