#!/usr/bin/env python3
"""L-COMP box 28: negative tests and mutation cross-validation of frup against box27/drup.c (both deletion-applying).
Usage: negtests.py DIR   (DIR holds d2_L5_c0.cnf/.glucose4.proof (UNSAT) and d2_L4_c0.cnf/.glucose4.proof (SAT), from
box27/mkproof.py 2 5 0 DIR / 2 4 0 DIR). Mutants (seeded): drop one lemma line, flip one literal of one lemma, delete one input
clause; for each mutant both checkers run; any verdict DISAGREEMENT is printed. Reports, per kind, how many mutants each checker rejects."""
import sys, os, random, subprocess
D = sys.argv[1]; H = os.path.dirname(os.path.abspath(__file__))
FR, DR = os.path.join(H, "frup"), os.path.join(H, "..", "box27", "drup")
def run(exe, c, p):
    r = subprocess.run([exe, c, p], capture_output=True, text=True); line = [l for l in r.stdout.splitlines() if l.startswith("s ")][0]
    return ("VERIFIED" if line.startswith("s VERIFIED") else "REJECT"), line, r.returncode
def both(c, p):
    a = run(FR, c, p); b = run(DR, c, p); return a, b
dis = 0
def rep(name, c, p, want=None):
    global dis
    a, b = both(c, p); agree = a[0] == b[0]; dis += (not agree)
    ok = "" if want is None else (" OK" if a[0] == want and b[0] == want else " UNEXPECTED")
    print(f"{name}: frup «{a[1]}» drup «{b[1]}» {'agree' if agree else 'DISAGREE'}{ok}", flush=True); return a[0]
cU, pU = f"{D}/d2_L5_c0.cnf", f"{D}/d2_L5_c0.glucose4.proof"; cS, pS = f"{D}/d2_L4_c0.cnf", f"{D}/d2_L4_c0.glucose4.proof"
P = open(pU).read().splitlines(); C = open(cU).read().splitlines()
rep("d2 L5 UNSAT proof", cU, pU, "VERIFIED")
rep("d2 L4 SAT formula + solver proof", cS, pS, "REJECT")
t = f"{D}/mut.proof"; tc = f"{D}/mut.cnf"
open(t, "w").write("\n".join(P[:3000]) + "\n"); rep("L5 proof truncated to 3000 lines", cU, t, "REJECT")
nd = [l for l in P if not l.startswith("d")]; open(t, "w").write("\n".join(l for i, l in enumerate(nd) if i % 7 != 6) + "\n")
rep("L5 proof, deletions dropped, every 7th line removed", cU, t, "REJECT")
lem = [i for i, l in enumerate(P) if l and not l.startswith("d") and l.strip() != "0"]
rng = random.Random(28); N = int(os.environ.get("NMUT", "40")); stats = {}
for kind in ("drop-lemma", "flip-literal", "delete-input-clause"):
    rj = [0, 0]
    for k in range(N):
        if kind == "drop-lemma":
            i = rng.choice(lem); Q = P[:i] + P[i + 1:]; open(t, "w").write("\n".join(Q) + "\n"); cc = cU; tag = f"line {i + 1}"
        elif kind == "flip-literal":
            i = rng.choice(lem); xs = P[i].split()[:-1]; j = rng.randrange(len(xs)); xs[j] = str(-int(xs[j]))
            Q = P[:i] + [" ".join(xs + ["0"])] + P[i + 1:]; open(t, "w").write("\n".join(Q) + "\n"); cc = cU; tag = f"line {i + 1} literal {j}"
        else:
            body = [i for i, l in enumerate(C) if l and l[0] not in "cp"]; i = rng.choice(body)
            hdr = C[0].split(); Cm = [f"p cnf {hdr[2]} {int(hdr[3]) - 1}"] + [l for m, l in enumerate(C[1:], 1) if m != i]
            open(tc, "w").write("\n".join(Cm) + "\n"); cc = tc; open(t, "w").write("\n".join(P) + "\n"); tag = f"cnf line {i + 1}"
        a, b = both(cc, t); rj[0] += a[0] == "REJECT"; rj[1] += b[0] == "REJECT"
        if a[0] != b[0]: dis += 1; print(f"DISAGREE {kind} {tag}: frup «{a[1]}» drup «{b[1]}»", flush=True)
    stats[kind] = rj; print(f"{kind}: {N} mutants, rejected by frup {rj[0]}, by drup {rj[1]}", flush=True)
print(f"negtests: disagreements {dis}")
